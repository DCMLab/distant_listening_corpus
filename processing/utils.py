import itertools
import json
import os
import re
import warnings
from fractions import Fraction
from functools import cache
from typing import Any, Dict, Iterable, Literal, Optional, Tuple, overload

import git
import ms3
import numpy as np
import pandas as pd
from dimcat.data.resources.facets import (
    extend_cadence_feature,
    extend_harmony_feature,
    extend_keys_feature,
)
from numpy._typing import NDArray

# region DivMaker


class DivMaker:
    """This is a convenient object for turning sequences of fractions into commensurate divs.
    It is equivalent to concatenating all sequences, passing them to the function shown below, and splitting them again.

        def fractions2divs(fracs: Iterable[Fraction]) -> NDArray[int]:
            numerators, denominators = np.array([(item.numerator,item.denominator) for item in fracs]).T
            lcm = np.lcm.reduce(denominators) # least common multiple
            return (numerators * lcm / denominators).astype(int)

    Example:

        STAR_WARS = np.array([ # durations of the star wars theme
            (1, 12),
            (1, 12),
            (1, 12),
            (1, 2),
            (1, 2),
            (1, 12),
            (1, 12),
            (1, 12),
            (1, 2),
            (1, 4)
        ])
        div_maker = DivMaker(STAR_WARS)
        div_maker[0] # yields [1, 1, 1, 6, 6, 1, 1, 1, 6, 3]

        POSITIONS = [Fraction(1, 20), Fraction(1, 32)] # fractions that we need our durations to be commensurate with
        div_maker.add_iterable_of_fractions(POSITIONS)
        durations, pos = div_maker # object is iterable (iterates through sequences added without names)
        list(durations) # yields [40, 40, 40, 240, 240, 40, 40, 40, 240, 120]

        OTHER_VALUES = (Fraction(i, 7) for i in range(7))
        div_maker.add_iterable_or_array(OTHER_VALUES, "other") # add the other values with a name
        div_maker[(1, "other", 0)] # when retrieving we can mix assigned names and indices of nameless sequences
        # OUTPUT:
        # (array([168, 105]),
        #  array([   0,  480,  960, 1440, 1920, 2400, 2880]),
        #  array([ 280,  280,  280, 1680, 1680,  280,  280,  280, 1680,  840]))

        div_maker.lcm # yields 3660, the common denominator for all values (least common multiple)
    """

    def __init__(
        self,
        *iterable_or_array: Iterable[Fraction] | NDArray[int],
        **named_iterables_or_arrays: Iterable[Fraction] | NDArray[int],
    ):
        """Pass one or several 2d-arrays (where one axis has shape 2) or one or several iterables of fractions.
        By passing keyword arguments you can assign names which you can use to retrieve the respective div sequences.
        """
        self.dict_of_frac_arrays: Dict[int | str, NDArray[int]] = {}
        for ioa in iterable_or_array:
            _ = self.add_iterable_or_array(ioa)
        for name, ioa in named_iterables_or_arrays.items():
            _ = self.add_iterable_or_array(ioa, name)

    @staticmethod
    def iterable_of_fractions_to_array(
        iterable_of_fractions: Iterable[Fraction],
    ) -> NDArray[int]:
        """Returns a numpy array of shape (2,n) for a given iterable of n :obj:`Fraction` objects."""
        return np.array(
            [(frac.numerator, frac.denominator) for frac in iterable_of_fractions]
        ).T

    def _get_next_consecutive_integer(self) -> int:
        return next(i for i in itertools.count() if i not in self.dict_of_frac_arrays)

    def add_iterable_of_fractions(
        self,
        iterable_of_fractions: Iterable[Fraction],
        name: Optional[str | int] = None,
    ) -> int | str:
        """Adds some iterable of :obj:`Fraction` objects that can then be retrieved as divs.
        If you assign a name you can retrieve it under that name, otherwise by the integer corresponding to the
        order in which it was added. Iteration over the object goes only through nameless objects in their adding
        order, meaning that you can assign an integer name that will not be taken into account when iterating
        through the object.
        """
        arr = self.iterable_of_fractions_to_array(iterable_of_fractions)
        return self.add_frac_array(arr, name=name)

    @staticmethod
    def _check_array(arr: NDArray) -> NDArray:
        arr = np.asarray(arr)
        assert arr.ndim == 2, f"Expected a 2D numpy array, not {arr.ndim}D"
        assert (
            2 in arr.shape
        ), f"One of the 2 dimensions needs to have shape 2. Received shape: {arr.shape}"
        if arr.shape[0] == 2:
            return arr
        return arr.T

    def add_frac_array(
        self, arr: NDArray[int], name: Optional[str | int] = None
    ) -> int | str:
        """Adds a 2d-array where one axis has shape 2, representing numerators and denominators of
        a sequence of fractions.
        If you assign a name you can retrieve it under that name, otherwise by the integer corresponding to the
        order in which it was added. Iteration over the object goes only through nameless objects in their adding
        order, meaning that you can assign an integer name that will not be taken into account when iterating
        through the object.
        """
        arr = self._check_array(arr)
        if name is None:
            name = self._get_next_consecutive_integer()
        assert isinstance(
            name, (str, int)
        ), f"Name is expected to be a string or int, not a {type(name)!r}"
        if name in self.dict_of_frac_arrays:
            warnings.warn(
                f"A sequence for the name {name!r} had already been added. It was overwritten."
            )
        self.dict_of_frac_arrays[name] = arr
        return name

    def add_iterable_or_array(
        self,
        iterable_or_array: Iterable[Fraction] | NDArray[int],
        name: Optional[str | int] = None,
    ):
        """Convenience function for calling either .add_iterable_of_fractions() or .add_frac_array() based on the
        input.
        """
        if isinstance(iterable_or_array, np.ndarray):
            return self.add_frac_array(iterable_or_array, name)
        return self.add_iterable_of_fractions(iterable_or_array, name)

    def concatenated_frac_arrays(
        self, names: Optional[str | int | Iterable[str | int]] = None
    ) -> NDArray:
        """Concatenate the requested arrays in order to compute their LCM. All arrays have shape (2, n) and so does
        their concatenation ("horizontal stacking").
        """
        if names:
            names = self._names_to_tuple(names)
            arrays = tuple(self.dict_of_frac_arrays[name] for name in names)
        else:
            if len(self.dict_of_frac_arrays) == 0:
                raise ValueError(
                    "No data has been added to this object. "
                    "Use the method .add_iterable_or_array() first"
                )
            arrays = tuple(self.dict_of_frac_arrays.values())
        if len(arrays) == 1:
            return arrays[0]
        return np.hstack(arrays)

    def get_divs(self, name: str | int) -> NDArray[int]:
        """Retrieve one of the previous inputs as divs, based on the LCM computed for all inputs together.
        Name can be a number for retrieving nameless inputs based on their input order.
        """
        if name not in self.dict_of_frac_arrays:
            raise KeyError(name)
        numerators, denominators = self.dict_of_frac_arrays[name]
        lcm = self.least_common_multiple()
        return (numerators * lcm / denominators).astype(int)

    @cache
    def _least_common_multiple(self, names: Tuple[str | int]) -> int:
        _, denominators = self.concatenated_frac_arrays(names)
        return np.lcm.reduce(denominators)

    def least_common_multiple(
        self, names: Optional[str | int | Iterable[str | int]] = None
    ) -> int:
        """By default, the LCM is computed based on all sequences of fractions that this object holds.
        When you retrieve divs, they are always commensurate between all sequences."""
        names = self._names_to_tuple(names)
        return self._least_common_multiple(names)

    @property
    def lcm(self):
        """For convenience."""
        return self.least_common_multiple()

    def _names_to_tuple(
        self, names: Optional[str | int | Iterable[str | int]] = None
    ) -> Tuple[str | int]:
        """Process input arguments."""
        if not names:
            names = tuple(self.dict_of_frac_arrays.keys())
        elif isinstance(names, (str, int)):
            names = (names,)
        else:
            names = tuple(names)
        assert len(names) > 0, f"Cannot compute LCM from the names {names!r}"
        return names

    @overload
    def __getitem__(self, names: str | int) -> NDArray: ...

    @overload
    def __getitem__(self, names: Iterable[str | int]) -> Tuple[NDArray]: ...

    def __getitem__(
        self, names: str | int | Iterable[str | int]
    ) -> NDArray | Tuple[NDArray]:
        if isinstance(names, (str, int)):
            return self.get_divs(names)
        names = tuple(names)
        return tuple(self.get_divs(name) for name in names)

    def __iter__(self):
        existing_consecutive_integers = itertools.takewhile(
            lambda x: x in self.dict_of_frac_arrays, itertools.count()
        )
        for i in existing_consecutive_integers:
            yield self.get_divs(i)


# endregion DivMaker
# region prepare_measures


def make_continuous_mc_beats_series(
    measures: pd.DataFrame,
    negative_anacrusis: Optional[Fraction] = None,
    beat_decimals: Optional[int] = None,
    name: str = "onset_beat",
) -> pd.Series:
    """This is an adapted copy of ms3.utils.make_continuous_offset_series() which is originally used for getting the
    quarternote offset position ("quarterbeats") for the beginning of each measure (MC).
    Here, it is adapted for getting beat offset positions according to the respective time signatures.

    Accepts a measure table without 'quarterbeats' column and computes each MC's offset from the piece's beginning.
    Deal with voltas before passing the table.


    Args:
        measures:
            A measures table with 'normal' RangeIndex containing the column 'act_durs' and one of
            'mc' or 'mc_playthrough' (if repeats were unfolded).
        negative_anacrusis:
            By default, the first value is 0. If you pass a fraction here, the first value will be its negative and the
            second value will be 0.
        beat_decimals:
            If None (default) the continous beats are added as Fraction objects,
            otherwise as floats rounded to beat_decimals decimals.


    Returns:
        Cumulative sum of the actual durations, shifted down by 1.

    Raises:
        ValueError
    """
    durations_in_beats = ms3.transform(
        measures,
        onset2beat,
        ["act_dur", "timesig"],
        beat_decimals=beat_decimals,
        first_beat=0,
    )
    result = durations_in_beats.cumsum()
    # last_val = result.iloc[-1]
    # last_ix = result.index[-1] + 1
    result = result.shift(fill_value=0)
    # ending = pd.Series([last_val, last_val], index=[last_ix, "end"])
    # result = pd.concat([result, ending])
    if negative_anacrusis is not None:
        result -= abs(negative_anacrusis)
    return result.rename(name)


def make_continuous_mn_beats_series(
    measures: pd.DataFrame,
    negative_anacrusis: Optional[Fraction] = None,
    beat_decimals: Optional[int] = None,
    name: str = "onset_beat",
    mn_col_name: str = "mn_playthrough",
) -> pd.Series:
    """Gets the continuous MC beats and drops the MC rows that duplicate MN values.
    This creates a mapping from measure numbers to continuous beat positions which can
    be used to create a continuous_beat columns for events by adding their beat_float but where
    beat 1 == beat_float 0.0.

    Args:
        measures:
        negative_anacrusis:
        beat_decimals:
        name:
        mn_col_name:

    Returns:

    """
    continuous_mc_beats = make_continuous_mc_beats_series(
        measures=measures,
        negative_anacrusis=negative_anacrusis,
        beat_decimals=beat_decimals,
        name=name,
    )
    continuous_mc_beats.index = measures[mn_col_name]
    return continuous_mc_beats[~continuous_mc_beats.index.duplicated()]


def make_onset_beat_column(
    mn_column: pd.Series,
    beat_float_column: Optional[pd.Series],
    mn_offsets: pd.Series | dict,
    name: str = "onset_beat",
) -> pd.Series:
    """This is an adapted copy of ms3.utils.make_quarterbeats_column()

    Turn each combination of mc and mc_onset into a quarterbeat value using the mn_offsets that maps mc to
    the measure's quarterbeat position (distance from the beginning of the piece).

    Args:
        mn_column: A sequence of MC values, each of which will be mapped to its quarterbeats value in ``mn_offsets``.
        beat_float_column: If specified, these values will be added to the mapped quarterbeats values.
        mn_offsets: {mc -> quarterbeats}, can be a Series.
        name: Name of the returned Series.

    Returns:
        Quarterbeats column.
    """
    onset_beat = mn_column.map(mn_offsets)
    if beat_float_column is not None:
        onset_beat += beat_float_column
    return onset_beat.rename(name)


def add_continuous_beat_column(merged, measures, beat_decimals):
    beat = ms3.transform(
        merged,
        onset2beat,
        ["mn_onset", "timesig"],
        first_beat=0,
        beat_decimals=beat_decimals,
    )
    anacrusis_mask = merged.mn_playthrough == "0a"
    if anacrusis_mask.any():
        # beats of an anacrusis measure need to start from zero rather than their metrical value
        anacrusis_beats = beat[anacrusis_mask].copy()
        first_value = anacrusis_beats.iat[0]
        anacrusis_beats -= first_value
        beat.loc[anacrusis_mask] = anacrusis_beats
    mn_offsets = make_continuous_mn_beats_series(measures, beat_decimals=beat_decimals)
    onset_beat = make_onset_beat_column(
        mn_column=merged.mn_playthrough, beat_float_column=beat, mn_offsets=mn_offsets
    )
    merged = pd.concat([merged, onset_beat], axis=1)
    return merged


def make_section_start_column(
    measures: pd.DataFrame,
) -> pd.Series:
    """Returns a column of nullable "boolean" dtype."""
    section_start = (
        (measures.repeats == "firstMeasure")
        .fillna(False)
        .rename("section_start")
        .astype("boolean")
    )
    section_start |= (measures.repeats == "start").fillna(False)
    section_start |= (measures.repeats.shift() == "end").fillna(False)
    section_start |= measures.breaks.shift().str.contains("section").fillna(False)
    section_start |= (measures.barline.shift() == "double").fillna(False)
    return section_start


def prepare_measures(
    measures: pd.DataFrame,
    beat_decimals: Optional[int] = None,
) -> pd.DataFrame:
    """

    Args:
        measures:
        beat_decimals:
            If None (default) the continous beats are added as Fraction objects,
            otherwise as floats rounded to beat_decimals decimals.

    Returns:

    """
    section_start_column = make_section_start_column(measures)
    continous_beats_column = make_continuous_mc_beats_series(
        measures, beat_decimals=beat_decimals
    )
    measures = pd.concat(
        [
            measures.drop(columns="quarterbeats"),
            continous_beats_column,
            section_start_column,
        ],
        axis=1,
    )
    measures.keysig = measures.keysig.astype("Int64")
    return measures


# endregion prepare_measures
# region make_pitch_array
KEEP_ORIGINAL_COLUMNS = [
    "mc",
    "mn",
    "mc_playthrough",
    "mn_playthrough",
    "quarterbeats_playthrough",
    "duration",
    "staff",
    "voice",
    "is_note_onset",
    "tpc",
]  # columns to keep from the original notes table
RENAME_ORIGINAL_COLUMNS = dict(  # columns to keep under a different name
    midi="pitch", keysig="ks_fifths"
)
COLUMN_ORDER = [
    "onset_div",
    "duration_div",
    "onset_beat",
    "pitch",
    "tpc",
    "step",
    "alter",
    "beat_float",
    "downbeat",
    "is_downbeat",
    "ts_beats",
    "ts_beat_type",
    "staff",
    "voice",
]
PITCH_ARRAY_DTYPES = dict(  # dtype dict passed to pd.DataFrame.astype()
    mn_playthrough="string",
)
MERGE_MEASURE_COLUMNS = ["keysig"]  # columns to merge into notes from measures table
MERGE_LABEL_COLUMNS = [
    "section_start"
]  # columns to merge additionally when label_notes = True


def _ts_beat_size(numerator: int, denominator: int) -> Fraction:
    beat_numerator = 3 if numerator % 3 == 0 and numerator > 3 else 1
    result = Fraction(beat_numerator, denominator)
    return result


@cache
def ts_beat_size(ts: str) -> Fraction:
    """Pass a time signature to get the beat size which is based on the fraction's
    denominator ('2/2' => 1/2, '4/4' => 1/4, '4/8' => 1/8). If the nominator is
    a higher multiple of 3, the threefold beat size is returned
    ('12/8' => 3/8, '6/4' => 3/4).
    """
    numerator, denominator = str(ts).split("/")
    result = _ts_beat_size(int(numerator), int(denominator))
    return result


@overload
def onset2beat(
    onset: Fraction, timesig: str, beat_decimals: Literal[None]
) -> Fraction: ...


@overload
def onset2beat(onset: Fraction, timesig: str, beat_decimals: int) -> float: ...


@cache
def onset2beat(
    onset: Fraction,
    timesig: str,
    beat_decimals: Optional[int] = None,
    first_beat: float | int = 1.0,
) -> float | Fraction:
    """Turn an offset in whole notes into a beat based on the time signature.
        Uses: ts_beat_size()

    Args:
        onset:
            Offset from the measure's beginning as fraction of a whole note.
        timesig:
            Time signature, i.e., a string representing a fraction.
        beat_decimals:
            If None (default) the beat is returned as Fraction, otherwise as float rounded to beat_decimals decimals.
    """
    size = ts_beat_size(timesig)
    beat, remainder = divmod(onset, size)
    subbeat = remainder / size
    result = beat + first_beat + subbeat
    return result if beat_decimals is None else round(float(result), beat_decimals)


def prepare_notes_with_measure_information(
    notes: pd.DataFrame,
    measures: pd.DataFrame,
    label_notes: bool = False,
    beat_decimals: Optional[int] = None,
) -> pd.DataFrame:
    """Add key signature from measure table and, optionally, labels created from it.

    Args:
        notes:
        measures:
        label_notes:
            If set to True, the measures table is used to create binary labels that are True for MCs
            where a new section begins.
        beat_decimals:

    Returns:

    """
    prepared_measures = prepare_measures(measures, beat_decimals=beat_decimals)
    potential_columns = ["quarterbeats_playthrough"] + MERGE_MEASURE_COLUMNS
    if label_notes:
        potential_columns += MERGE_LABEL_COLUMNS
    merge_measure_columns = [
        col for col in potential_columns if col in prepared_measures.columns
    ]

    merged = pd.merge(
        left=notes,
        right=prepared_measures[merge_measure_columns],
        on="quarterbeats_playthrough",
        how="outer",
    )
    merged.keysig = merged.keysig.ffill().bfill()
    if label_notes:
        merged.section_start = merged.section_start.fillna(False)

    merged = merged.dropna(subset="tpc")
    # continuous beats
    merged = add_continuous_beat_column(merged, measures, beat_decimals)
    return merged


def float_is_integer(f: float) -> bool:
    try:
        return f.is_integer()
    except Exception:
        print(f"Unable to evaluate whether {f!r} is an integer.")
        return False


def prepare_notes(
    notes: pd.DataFrame,
    beat_decimals: Optional[int] = None,
    beat_float_name: str = "beat_float",
    downbeat_name: str = "downbeat",
) -> pd.DataFrame:
    dtype_dict = dict(
        staff="Int64",
        voice="Int64",
        mc="Int64",
        mc_playthrough="Int64",
        mn="Int64",
    )
    notes = notes.drop(columns="quarterbeats").astype(dtype_dict)
    beat_float = ms3.transform(
        notes, onset2beat, ["mn_onset", "timesig"], beat_decimals=beat_decimals
    )
    downbeat_mask = beat_float.map(float_is_integer)
    downbeat = beat_float.where(downbeat_mask, 0).astype("Int64")
    beat_columns = pd.DataFrame(
        {
            beat_float_name: beat_float,
            downbeat_name: downbeat,
            "is_downbeat": downbeat_mask,
        },
        index=notes.index,
    )
    mn_onset_pos = notes.columns.get_loc("mn_onset") + 1
    return pd.concat(
        [notes.iloc[:, :mn_onset_pos], beat_columns, notes.iloc[:, mn_onset_pos:]],
        axis=1,
    )


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def colorprint(txt, color=bcolors.WARNING):
    print(f"{color}{txt}{bcolors.ENDC}", end="")


def make_pitch_array(
    notes: pd.DataFrame,
    measures: Optional[pd.DataFrame] = None,
    beat_decimals: Optional[int] = 3,
    label_notes: bool = False,
) -> pd.DataFrame:
    """Transformation of a notes table to a pitch array that can be transformed into a graph.

    Args:
        beat_decimals:
            Integer controlling the number of decimal places in the column "beat_float". If you pass None,
            the column will contain :obj:`Fraction` objects.
        label_notes:
            By default, this function includes only transformations that are part of the input representation.
            Set to True in order to include training labels from the measures table as well (for details,
            see prepare_notes_with_measure_information()).


    """
    colorprint("N")
    prepared_notes = prepare_notes(notes, beat_decimals=beat_decimals)
    if measures is not None:
        prepared_notes = prepare_notes_with_measure_information(
            prepared_notes,
            measures,
            label_notes=label_notes,
            beat_decimals=beat_decimals,
        )
    colorprint("N", bcolors.OKGREEN)

    colorprint("D")
    div_maker = DivMaker(
        onsets=prepared_notes.quarterbeats_playthrough,
        durations=prepared_notes.duration
        * 4,  # normally duration_qb but due to a bug these are currently floats
    )
    onset_div, duration_div = div_maker[("onsets", "durations")]
    colorprint("D", bcolors.OKGREEN)

    colorprint("C")
    potential_columns = list(set(KEEP_ORIGINAL_COLUMNS).union(set(COLUMN_ORDER)))
    if label_notes:
        potential_columns += MERGE_LABEL_COLUMNS
    keep_original_columns = [
        col for col in potential_columns if col in prepared_notes.columns
    ]

    original_columns = prepared_notes[keep_original_columns]

    rename_original_columns = {
        k: v for k, v in RENAME_ORIGINAL_COLUMNS.items() if k in prepared_notes.columns
    }
    renamed_columns = prepared_notes[list(rename_original_columns.keys())].rename(
        columns=rename_original_columns
    )

    new_dataframes = []  # will be added as-is
    new_columns = dict()  # will be renamed based on the keys

    new_columns["is_note_onset"] = prepared_notes.tied.fillna(1) == 1

    # specific pitch
    specific_pitch = prepared_notes.name.str.extract(
        r"^(?P<step>[A-G])(?P<accidentals>b*|#*)(?P<octave>\d)$"
    )
    new_columns["step"] = specific_pitch.step.astype("string")
    new_columns["octave"] = specific_pitch.octave.astype("Int64")
    alter_col = specific_pitch.accidentals.str.count(
        "#"
    ) - specific_pitch.accidentals.str.count("b")
    new_columns["alter"] = alter_col.astype("Int64")

    # time signatures & beats
    new_dataframes.append(
        prepared_notes.timesig.str.extract(r"^(?P<ts_beats>\d+)/(?P<ts_beat_type>\d+)$")
    )

    result = pd.concat(
        [
            pd.DataFrame(
                dict(onset_div=onset_div, duration_div=duration_div), dtype="Int64"
            ),
            pd.concat(new_columns, axis=1),
            renamed_columns,
            original_columns,
        ]
        + new_dataframes,
        axis=1,
    )
    colorprint("C", bcolors.OKGREEN)
    column_order = [col for col in COLUMN_ORDER if col in result.columns]
    column_order += sorted(col for col in result.columns if col not in column_order)
    return convert_column_types(result[column_order], **PITCH_ARRAY_DTYPES)


# endregion make_pitch_array
# region make_labeled_pitch_array
# columns are converted based on the dtypes assigned in the following
INT_COLUMNS = [
    "unfolded_harmony_index",
    "root",
    "bass_note",
    "root_tpc",
    "bass_note_tpc",
    "globalkey_tpc",
    "localkey_tpc",
    "tonicized_tpc",
    "ts_beats",
    "ts_beat_type",
    "a_inversion",
    "downbeat",
]
BOOL_COLUMNS = [
    "globalkey_is_minor",
    "localkey_is_minor",
    "a_isOnset",
    "a_phraseend",
    "section_start",
    "valid_chord_label",
    "valid_cadence_label",
    "valid_phrase_label",
    "valid_pedal_point_label",
    "valid_section_start_label",
    "is_downbeat",
]
STRING_COLUMNS = [
    "label",
    "alt_label",
    "globalkey",
    "localkey",
    "pedal",
    "chord",
    "special",
    "numeral",
    "form",
    "figbass",
    "changes",
    "relativeroot",
    "cadence",
    "phraseend",
    "chord_type",
    "globalkey_mode",
    "localkey_mode",
    "localkey_resolved",
    "localkey_and_mode",
    "root_roman",
    "relativeroot_resolved",
    "effective_localkey",
    "effective_localkey_resolved",
    "effective_localkey_is_minor",
    "chord_reduced",
    "chord_reduced_and_mode",
    "pedal_resolved",
    "chord_and_mode",
    "applied_to_numeral",
    "numeral_or_applied_to_numeral",
    "cadence_type",
    "_merge",
    "a_root",
    "a_bass",
    "a_localKey",
    "a_tonicizedKey",
    "note_degree",
]
OBJECT_COLUMNS = [
    "chord_tones",
    "added_tones",
]  # unused, leave them as they are
NON_FORWARD_FILLING_COLUMNS = [
    "a_isOnset",
    "cadence",
    "cadence_type",
    "cadence_subtype",
    "phraseend",
    "a_phraseend",
    "section_start",
]  # these are not propagated over the whole duration of their harmony label and are therefore moved to the left
# of the column unfolded_harmony_index which serves as the boundary between (non-forward-filled) notes on the left,
# and forward-filled (within the reach of each valid label) labels on the right


def convert_roman_numerals_to_fifths(labels: pd.DataFrame) -> pd.DataFrame:
    concatenate_this = [
        labels,
        (
            globalkey_tpc := ms3.transform(
                labels.globalkey,
                ms3.name2fifths,
            )
        ).rename("globalkey_tpc"),
        (
            ms3.transform(
                labels[["localkey", "globalkey_is_minor"]], ms3.roman_numeral2fifths
            )
            + globalkey_tpc
        ).rename("localkey_tpc"),
        (
            ms3.transform(
                labels[["effective_localkey_resolved", "globalkey_is_minor"]],
                ms3.roman_numeral2fifths,
            )
            + globalkey_tpc
        ).rename("tonicized_tpc"),
    ]
    labels = pd.concat(concatenate_this, axis=1)
    return labels


def convert_chord_tones_to_tpc(labels: pd.DataFrame) -> pd.DataFrame:
    concatenate_this = [
        labels,
        (labels.localkey_tpc + labels.root).rename("root_tpc"),
        (labels.localkey_tpc + labels.bass_note).rename("bass_note_tpc"),
    ]
    labels = pd.concat(concatenate_this, axis=1)
    return labels


def convert_tpc_to_note_names(labels: pd.DataFrame) -> pd.DataFrame:
    concatenate_this = [
        labels,
        ms3.transform(labels.root_tpc, ms3.fifths2name).rename("a_root"),
        ms3.transform(labels.bass_note_tpc, ms3.fifths2name).rename("a_bass"),
        ms3.transform(labels.localkey_tpc, ms3.fifths2name).rename("a_localKey"),
        ms3.transform(labels.tonicized_tpc, ms3.fifths2name).rename("a_tonicizedKey"),
    ]
    labels = pd.concat(concatenate_this, axis=1)
    return labels


def add_boolean_phrase_labels(labels: pd.DataFrame) -> pd.DataFrame:
    concatenate_this = [
        labels,
        labels.phraseend.isin([r"\\", "}", "}{"]).rename("a_phraseend"),
    ]
    labels = pd.concat(concatenate_this, axis=1)
    return labels


def add_boolean_annotation_type_columns(labels: pd.DataFrame) -> pd.DataFrame:
    concatenate_this = [
        labels,
        labels.root.notna().rename("valid_chord_label"),
        pd.Series(
            labels.cadence.notna().any(),
            index=labels.index,
            dtype="boolean",
            name="valid_cadence_label",
        ),
        pd.Series(
            labels.phraseend.notna().any(),
            index=labels.index,
            dtype="boolean",
            name="valid_phrase_label",
        ),
        pd.Series(
            True, index=labels.index, dtype="boolean", name="valid_pedal_point_label"
        ),
        pd.Series(
            True, index=labels.index, dtype="boolean", name="valid_section_start_label"
        ),
    ]
    labels = pd.concat(concatenate_this, axis=1)
    return labels


def convert_roman_numerals_to_scale_degrees(
    labels: pd.DataFrame,
    flat_character: str = "b",
) -> pd.DataFrame:
    concatenate_this = [
        labels,
        (
            ms3.transform(
                labels.numeral,
                roman_numeral2scale_degree,
                flat_character=flat_character,
            )
        )
        .astype("string")
        .rename("a_degree1"),
        (
            ms3.transform(
                labels.relativeroot_resolved,
                roman_numeral2scale_degree,
                flat_character=flat_character,
            )
        )
        .astype("string")
        .rename("a_degree2"),
    ]
    labels = pd.concat(concatenate_this, axis=1)
    return labels


DLC_CHORD_TYPE_MAPPING = {
    "M": "major triad",
    "m": "minor triad",
    "o": "diminished triad",
    "+": "augmented triad",
    "+7": "augmented seventh chord",  # check if that's what's meant in music21
    "+M7": "augmented major tetrachord",  # check if that's what's meant in music21
    "mm7": "minor seventh chord",
    "MM7": "major seventh chord",
    "Mm7": "dominant seventh chord",
    "incomplete dominant-seventh chord": "incomplete dominant-seventh chord",  # not available in DLC
    "o7": "diminished seventh chord",
    "%7": "half-diminished seventh chord",
    "It": "Italian augmented sixth chord",
    "Ger": "German augmented sixth chord",
    "Fr": "French augmented sixth chord",
    "mM7": "minor-augmented tetrachord",
    pd.NA: "None",
}


def convert_chord_types_to_qualities(labels: pd.DataFrame) -> pd.DataFrame:
    return pd.concat(
        [
            labels,
            labels.chord_type.map(DLC_CHORD_TYPE_MAPPING)
            .astype("string")
            .rename("a_quality"),
        ],
        axis=1,
    )


FIGBASS2INVERSION = {"6": "1", "65": "1", "64": "2", "43": "2", "42": "3", "2": "3"}


def convert_figbass_to_inversion(labels: pd.DataFrame) -> pd.DataFrame:
    inversion_column = (
        labels.figbass.replace(FIGBASS2INVERSION)
        .fillna("0")
        .astype("Int64")
        .rename("a_inversion")
    )
    inversion_column = inversion_column.where(labels.chord.notna(), pd.NA)
    return pd.concat(
        [
            labels,
            inversion_column,
        ],
        axis=1,
    )


def convert_column_types(labels: pd.DataFrame, **kwargs) -> pd.DataFrame:
    conversion_dict = {col: "Int64" for col in INT_COLUMNS if col in labels.columns}
    conversion_dict.update(
        {col: "boolean" for col in BOOL_COLUMNS if col in labels.columns}
    )
    conversion_dict.update(
        {col: "string" for col in STRING_COLUMNS if col in labels.columns}
    )
    conversion_dict.update(kwargs)
    # print(conversion_dict)
    return labels.astype(conversion_dict)


REPLACE_ROOT = {"bII": "N", "@none": "none"}
ADAPT_CHORD_TYPE = {
    "M": "",
    "m": "",
    "M7": "",
    "Mm7": "7",
    "mm7": "7",
    "MM7": "7",
    "mM7": "7",
    "+M7": "+7",
}
ADAPT_SPECIAL_CHORDS = {
    "Fr": "Fr7",
    "Ger": "Ger7",
}


def add_simpleNumeral_columns(labels: pd.DataFrame) -> pd.DataFrame:

    numeral = labels.numeral.replace(REPLACE_ROOT)

    reference_is_minor = labels.relativeroot_resolved.str.islower().fillna(
        labels.localkey_is_minor
    )
    add_flat_for_67_minor = labels.numeral.isin(("vi", "vii")) & reference_is_minor
    numeral = numeral.where(
        ~add_flat_for_67_minor, labels.numeral.replace({"vi": "bvi", "vii": "bvii"})
    )

    remove_sharp_for_67_in_minor = (
        labels.numeral.isin(("#vi", "#vii")) & reference_is_minor
    )
    numeral = numeral.where(
        ~remove_sharp_for_67_in_minor,
        labels.numeral.replace({"#vi": "vi", "#vii": "vii"}),
    )

    # add adapted chord type
    adapted_chord_type = labels.chord_type.replace(ADAPT_CHORD_TYPE)
    numeral = numeral + adapted_chord_type

    cadential_V_mask = (labels.numeral == "V") & labels.changes.str.contains(
        "64"
    ).fillna(False)
    numeral = numeral.where(~cadential_V_mask, "Cad")

    if "special" in labels.columns:
        special_column = labels.special.replace(ADAPT_SPECIAL_CHORDS)
        numeral = numeral.where(special_column.isna(), special_column)

    # ninths = pd.Series("9", index=dlc_labels.index).where(dlc_labels.changes.str.contains("9"), "")
    a_romanNumeral = numeral.astype("string")  # + ninths

    return pd.concat(
        [
            labels,
            a_romanNumeral.rename("a_simpleNumeral"),
        ],
        axis=1,
    )


def prepare_labels(labels: pd.DataFrame) -> pd.DataFrame:
    labels = labels.drop(columns="quarterbeats")
    labels = extend_keys_feature(labels)
    labels["a_isOnset"] = True
    ffilled_chord = labels.chord.ffill().fillna("") + labels.localkey_resolved
    labels.a_isOnset = labels.a_isOnset.where(
        labels.chord.notna() & (ffilled_chord != ffilled_chord.shift(1)).fillna(True),
        False,  # set False where the label does not define a harmony or merely the same harmony as the preceding one
    )
    labels.index.rename("unfolded_harmony_index", inplace=True)
    labels.reset_index(drop=False, inplace=True)
    labels = extend_harmony_feature(labels)
    labels = add_simpleNumeral_columns(labels)
    labels = convert_roman_numerals_to_scale_degrees(labels, flat_character="-")
    labels = convert_roman_numerals_to_fifths(labels)
    labels = convert_chord_tones_to_tpc(labels)
    labels = convert_tpc_to_note_names(labels)
    labels = convert_chord_types_to_qualities(labels)
    labels = convert_figbass_to_inversion(labels)
    labels = extend_cadence_feature(labels)
    labels = add_boolean_phrase_labels(labels)
    labels = add_boolean_annotation_type_columns(labels)
    column_order = [col for col in NON_FORWARD_FILLING_COLUMNS if col in labels.columns]
    column_order += [col for col in labels.columns if col not in column_order]
    return convert_column_types(labels[column_order])


def compute_interval_classes_to_keys(merged: pd.DataFrame) -> pd.DataFrame:
    concatenate_this = [
        merged,
        (merged.tpc - merged.globalkey_tpc).rename("sic_with_global"),
        (merged.tpc - merged.localkey_tpc).rename("sic_with_local"),
        (merged.tpc - merged.tonicized_tpc).rename("sic_with_tonicized"),
    ]
    return pd.concat(concatenate_this, axis=1)


def fifths2scale_degree(fifths, minor=False):
    try:
        return ms3.fifths2sd(fifths=fifths, minor=minor)
    except Exception:
        return pd.NA


def add_note_degree_column(merged: pd.DataFrame) -> pd.DataFrame:
    note_degree = ms3.transform(
        merged, fifths2scale_degree, ["sic_with_local", "localkey_is_minor"]
    )
    return pd.concat([merged, note_degree.rename("note_degree")], axis=1)


def add_boolean_label_columns(merged: pd.DataFrame) -> pd.DataFrame:

    def is_in_chord_tones(sic: int, chord_tones: Tuple[int]) -> bool:
        """Used for element-wise containment check"""
        try:
            return sic in chord_tones
        except TypeError:
            # print(f"{sic} in {chord_tones} resulted in {e!r}")
            return pd.NA

    concatenate_this = [
        merged,
        ms3.transform(merged, is_in_chord_tones, ["sic_with_local", "chord_tones"])
        .astype("boolean")
        .rename("tpc_is_in_label"),
        (merged.sic_with_local == merged.root).rename("tpc_is_root"),
        (merged.sic_with_local == merged.bass_note).rename("tpc_is_bass"),
    ]
    return pd.concat(concatenate_this, axis=1)


def make_labeled_pitch_array(
    notes: pd.DataFrame,
    labels: pd.DataFrame,
    measures: Optional[pd.DataFrame] = None,
    beat_decimals: Optional[int] = 3,
    drop_labels_starting_between_notes: bool = True,
):
    pitch_array = make_pitch_array(
        notes, measures, label_notes=True, beat_decimals=beat_decimals
    )
    colorprint("L")
    prepared_labels = prepare_labels(labels)
    colorprint("L", bcolors.OKGREEN)

    colorprint("M")
    merged = pd.merge(
        left=pitch_array,
        right=prepared_labels.drop(
            columns=[
                "mc",
                "mn",
                "mc_playthrough",
                "mn_playthrough",
                "quarterbeats_all_endings",
                "duration_qb",
                "mc_onset",
                "mn_onset",
                "timesig",
                "staff",
                "voice",
            ]
        ),
        on="quarterbeats_playthrough",
        how="outer",
        sort=True,
        suffixes=("", "_label"),
        indicator=False,
    )
    merged.a_isOnset = merged.a_isOnset.fillna(False)
    merged.a_phraseend = merged.a_phraseend.fillna(False)
    colorprint("M", bcolors.OKGREEN)

    colorprint("P")
    harmony_side = merged.loc[:, "unfolded_harmony_index":]
    harmony_grouper = harmony_side.unfolded_harmony_index.where(
        harmony_side.chord.notna()
    ).ffill()  # takes only index positions for which a harmony is defined
    # and forward-fills gaps with indices of the harmonies
    bfill = False
    if pd.isnull(harmony_grouper.iloc[0]):
        warnings.warn(
            "The first row of the merged pitch array does not come with a valid label. "
            "The first label will be considered to start with the first note of the piece."
        )
        harmony_grouper = harmony_grouper.bfill()
        bfill = True
    filled_harmony_side = harmony_side.groupby(harmony_grouper).ffill()
    if bfill:
        # this extends the info of the first label back to the notes occurring before it
        # This probably contradicts the annotator's intention but is better than having no
        # key information etc. filled
        columns_exept_valid = [
            c for c in filled_harmony_side.columns if c != "valid_chord_label"
        ]
        filled_harmony_side.loc[:, columns_exept_valid] = filled_harmony_side.loc[
            :, columns_exept_valid
        ].bfill()
        filled_harmony_side.valid_chord_label = (
            filled_harmony_side.valid_chord_label.fillna(False)
        )
    merged.loc[:, "unfolded_harmony_index":] = filled_harmony_side
    if drop_labels_starting_between_notes:
        merged = merged.dropna(subset="tpc")
    colorprint("P", bcolors.OKGREEN)
    colorprint("C")
    merged = compute_interval_classes_to_keys(merged)
    merged = add_note_degree_column(merged)
    merged = add_boolean_label_columns(merged)
    colorprint("C", bcolors.OKGREEN)
    return merged


# endregion make_labeled_pitch_array
def filter_corpus(corpus):
    corpus.view.include("facets", "measures", "notes", "expanded")  # , "expanded")
    # corpus.disambiguate_facet("expanded")
    # corpus.disambiguate_facet("scores")
    corpus.view.pieces_with_incomplete_facets = False


def get_ms3_corpus(corpus_path):
    corpus = ms3.Corpus(corpus_path)
    # filter_corpus(corpus)
    return corpus


def get_unfolded_facets_from_piece(
    piece: ms3.Piece,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    (_, measures), (_, notes), (_, labels) = piece.get_parsed_tsvs(
        ("measures", "notes", "expanded"), unfold=True, force=True, choose="auto"
    )
    return measures, notes, labels


def get_pitch_array_from_piece(
    piece: ms3.Piece, drop_labels_starting_between_notes: bool = True
):
    measures, notes, labels = get_unfolded_facets_from_piece(piece)
    return make_labeled_pitch_array(
        notes=notes,
        labels=labels,
        measures=measures,
        beat_decimals=3,
        drop_labels_starting_between_notes=drop_labels_starting_between_notes,
    )


def store_pitch_array(pitch_array: pd.DataFrame, output_dir: str, tsv_name: str):
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, tsv_name)
    pitch_array.to_csv(filepath, sep="\t", index=False)
    print(filepath, end="")
    return filepath


def load_metadata(metadata_path):
    metadata = ms3.load_tsv(metadata_path, index_col=["corpus", "piece"])
    return metadata


def dataset_processing_stats(metadata_path, dataset) -> Optional[pd.Series]:
    metadata = load_metadata(metadata_path)
    if dataset not in metadata.columns:
        return None
    return metadata[dataset].value_counts(dropna=False)


def get_commit_where_file_last_changed(repo: git.Repo, paths: str) -> git.Commit:
    try:
        return next(repo.iter_commits(paths=paths))
    except StopIteration as e:
        raise StopIteration(f"{repo!r} does not have any commits for {paths}") from e


def describe_commit_where_file_last_changed(repo: git.Repo, paths: str) -> str:
    file_last_changed_commit = get_commit_where_file_last_changed(repo, paths=paths)
    file_last_changed_commit_sha = file_last_changed_commit.hexsha
    file_last_changed_commit_version = repo.git.describe(
        file_last_changed_commit_sha, tags=True, always=True
    )
    return file_last_changed_commit_version


def store_pitch_arrays_for_corpus(
    corpus: ms3.Corpus,
    output_dir: str,
    metadata_path: str,
    column_name: str,
    corpus_subdir: bool = True,
    reset: bool = False,
):
    """

    Args:
        corpus:
        output_dir:
        metadata_path:
        column_name: The name of the column in which the progress for parsing the dataset will be stored.
        corpus_subdir:
        reset: Set to True in order to not skip pieces that have already been marked as processed in the metadata.

    Returns:

    """
    output_dir = ms3.resolve_dir(output_dir)
    if corpus_subdir:
        output_dir = os.path.join(output_dir, corpus.name)
    metadata = load_metadata(metadata_path)

    def insert_column_if_missing(
        df: pd.DataFrame, col_name, position=0, value: Any = ""
    ):
        if col_name not in df.columns:
            df.insert(position, col_name, value=value)

    insert_column_if_missing(metadata, column_name, value=False)
    insert_column_if_missing(metadata, "last_modified", position=1)
    insert_column_if_missing(metadata, "last_modified_url", position=2)

    if reset:
        piece_names = corpus.get_all_pnames(pieces_not_in_metadata=False)
        ids = [(corpus.name, piece) for piece in piece_names]
        metadata.loc[ids, column_name] = False
        ms3.write_tsv(metadata, metadata_path, index=True)
    for piece_id, piece in corpus.iter_pieces():
        id_tuple = (corpus.name, piece_id)
        print(f"\n{id_tuple}", end=" ")
        if id_tuple not in metadata.index:
            print("NOT ANNOTATED")
            continue
        if metadata.loc[id_tuple, column_name]:
            print("SKIPPED")
            continue
        try:
            colorprint("I")
            pitch_array = get_pitch_array_from_piece(piece)
            _ = store_pitch_array(
                pitch_array, output_dir=output_dir, tsv_name=f"{piece_id}.tsv"
            )
            colorprint("i", bcolors.OKGREEN)

            colorprint("O")
            musescore_file_info, _ = piece.get_parsed_score()
            rel_filepath = musescore_file_info.rel_path
            last_modified = describe_commit_where_file_last_changed(
                corpus.repo, rel_filepath
            )
            last_modified_url = f"https://github.com/DCMLab/{corpus.name}/blob/{last_modified}/{rel_filepath}"
            metadata.loc[id_tuple, column_name] = True
            metadata.loc[id_tuple, "last_modified"] = last_modified
            metadata.loc[id_tuple, "last_modified_url"] = last_modified_url
            ms3.write_tsv(metadata, metadata_path, index=True)
            colorprint("O", bcolors.OKGREEN)
        except Exception as e:
            print(e)

    colorprint(f"\n{corpus.name} DONE", bcolors.OKGREEN)


def store_pitch_arrays_for_corpora(
    metacorpus_path: str,
    output_dir: str,
    metadata_path: str,
    column_name: str,
    corpus_subdir: bool = True,
    reset: bool = False,
):
    """

    Args:
        metacorpus_path:
        output_dir:
        metadata_path:
        column_name: The name of the column in which the progress for parsing the dataset will be stored.
        corpus_subdir:
        reset: Set to True in order to not skip pieces that have already been marked as processed in the metadata.
    """
    for subcorpus_dir in sorted(os.listdir(metacorpus_path)):
        if subcorpus_dir.startswith("."):
            continue
        subcorpus_path = os.path.join(metacorpus_path, subcorpus_dir)
        if os.path.isfile(subcorpus_path):
            continue
        try:
            corpus = get_ms3_corpus(subcorpus_path)
        except AssertionError as e:
            print(f"{subcorpus_path} seems not be a corpus: failed with {e}")
            continue
        store_pitch_arrays_for_corpus(
            corpus=corpus,
            output_dir=output_dir,
            metadata_path=metadata_path,
            column_name=column_name,
            corpus_subdir=corpus_subdir,
            reset=reset,
        )

    colorprint("\nEVERYTHING DONE", bcolors.OKGREEN)


def safe_fraction(s: str) -> Fraction | str:
    try:
        return Fraction(s)
    except Exception:
        return s


def str2inttuple(tuple_string: str, strict: bool = True) -> Tuple[int]:
    tuple_string = tuple_string.strip("[](),")
    if tuple_string == "":
        return tuple()
    res = []
    for s in tuple_string.split(", "):
        try:
            res.append(int(s))
        except ValueError:
            if strict:
                print(
                    f"String value '{s}' could not be converted to an integer, "
                    f"'{tuple_string}' not to an integer tuple."
                )
                raise
            if s[0] == s[-1] and s[0] in ('"', "'"):
                s = s[1:-1]
            try:
                res.append(int(s))
            except ValueError:
                res.append(s)
    return tuple(res)


def load_labeled_pitch_array(
    specs_csv: str, pitch_array_tsv: str, dropna: bool = True, **replace_dtypes
) -> pd.DataFrame:
    """

    Args:
        specs_csv:
            Path to a CSV file where the first column contains the column names of the pitch array
            to be loaded and a column "dtype" containing the corresponding dtypes as output by
            pd.DataFrame.dtypes
        pitch_array_tsv:
        dropna:
        **replace_dtypes: Keyword arguments can be used to overwrite the dtypes from the CSV.
    """
    loaded_specs = pd.read_csv(specs_csv, index_col=0)
    converters = dict(
        chord_tones=str2inttuple,
        added_tones=str2inttuple,
        duration=safe_fraction,
        quarterbeats_playthrough=safe_fraction,
    )
    dtype_dict = {
        col: dtype
        for col, dtype in loaded_specs.dtype.replace(replace_dtypes).items()
        if col not in converters
    }
    result = pd.read_csv(
        pitch_array_tsv, sep="\t", dtype=dtype_dict, converters=converters
    )
    return result.dropna(subset="tpc") if dropna else result


def split_scale_degree(sd, count=False) -> Tuple[Optional[int], Optional[str]]:
    """Copied from ms3 @ v2.6.0
    Splits a scale degree such as 'bbVI' or 'b6' into accidentals and numeral.

    sd : :obj:`str`
        Scale degree.
    count : :obj:`bool`, optional
        Pass True to get the accidentals as integer rather than as string.
    """
    m = re.match(
        r"^(#*|b*|-*)(Cad|Ger|It|Fr|N|VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)$",
        str(sd),
    )
    if m is None:
        if "/" in sd:
            raise ValueError(
                f"{sd} needs to be resolved, which requires information about the mode of the local key. "
                f"You can use ms3.utils.resolve_relative_keys(scale_degree, is_minor_context)."
            )
        else:
            raise ValueError(f"{sd} is not a valid scale degree.")
    acc, num = m.group(1), m.group(2)
    if count:
        acc = acc.count("#") - acc.count("b") - acc.count("-")
    return acc, num


ROMAN_NUMERAL2SCALE_DEGREE = {
    "I": ("1", 0),
    "II": ("2", 0),
    "III": ("3", 0),
    "IV": ("4", 0),
    "V": ("5", 0),
    "VI": ("6", 0),
    "VII": ("7", 0),
    "FR": ("2", 0),
    "GER": ("4", 1),
    "IT": ("4", 1),
    "N": ("2", -1),
    "CAD": ("1", 0),
}


def roman_numeral2scale_degree(
    RN: str,
    key_is_minor: Optional[bool] = None,
    flat_character: str = "b",
):
    """Copied from ms3 @ v2.6.0
    Turn a Roman numeral into a scale degree, assuming that the accidentals are the same. Does not accept slash
    notation.

    If you need to convert between different meaning of scale degrees 6 and 7 in minor, you need apply
    roman_numeral2fifths() using the appropriate ``meaning_of_vi_and_vii`` parameter, and then fifths2sd().


    Args:
        RN:
        key_is_minor:
            If you pass True the capitalization of the RN is exceptionally taken into account in the for degrees
            VI and VII: if they are lowercase, #6 and #7 are returned rather than 6 and 7, which is the default for
            major and upper case. In other words, True says we are in minor and we are dealing with music21's
            default behaviour which interprets scale degrees based on the chord quality. On the flipside, to use this
            on DCML labels for the same result, do not pass this parameter for consistent results.
        flat_character:

    Returns:

    """
    if pd.isnull(RN):
        return RN
    try:
        alter, rn_step = split_scale_degree(RN, count=True)
    except Exception:
        return None
    if any(v is None for v in (alter, rn_step)):
        return None
    rn_step_upper = rn_step.upper()
    degree, degree_alter = ROMAN_NUMERAL2SCALE_DEGREE[rn_step_upper]
    alter += degree_alter
    if key_is_minor and rn_step_upper in ("VI", "VII"):
        if rn_step.islower() and RN[0] != "#":
            alter += 1
        elif RN[0] in (
            "b",
            "-",
        ):  # opposite case where an already flat numeral comes with flat
            alter += 1
    if alter == 0:
        return degree
    if alter > 0:
        accidentals = alter * "#"
    elif alter < 0:
        accidentals = -alter * flat_character
    return accidentals + degree


def create_and_store_specs(
    lpa: pd.DataFrame,
    specs_csv_path: str,
    specs_specs: Optional[Dict[str, dict] | str] = None,
    specs_specs_json_path: Optional[str] = None,
):
    """

    Args:
        lpa: Labelled pitch array from which the dtypes are derived.
        specs_csv_path: Path where to store the complete column specs as a CSV file.
        specs_specs:
            {column_name -> dict} where at least one of all dicts needs to contain the key
            "description" and at least one the key "used_for". All used keys become a column
            in the specs.
        specs_specs_json_path:
            If you also want to store the specs_specs as a JSON file, specify its path.
            This can be useful to easily edit it at a later point while still having the
            dtype column updated automatically.

    Returns:

    """
    specs_df = create_specs(lpa=lpa, specs_specs=specs_specs)
    specs_df.to_csv(specs_csv_path, index=True)
    if not specs_specs_json_path:
        return
    if isinstance(specs_specs, str):
        specs_specs = load_json_file(specs_specs)
    with open(specs_specs_json_path, "w", encoding="utf-8") as f:
        json.dump(specs_specs, f, indent=2)


def create_specs(
    lpa: pd.DataFrame, specs_specs: Optional[Dict[str, dict] | str] = None
) -> pd.DataFrame:
    """

    Args:
        lpa: Labelled pitch array from which the dtypes are derived.
        specs_specs:
            {column_name -> dict} where at least one of all dicts needs to contain the key
            "description" and at least one the key "used_for". All used keys become a column
            in the specs.

    Returns:

    """
    dtypes = lpa.dtypes.rename("dtype")
    if not specs_specs:
        return dtypes.to_frame()
    if isinstance(specs_specs, str):
        specs_specs = load_json_file(specs_specs)
    specs_df = pd.DataFrame.from_dict(specs_specs, orient="index")
    specs_df = pd.concat([dtypes, specs_df], axis=1)
    column_order = ["dtype", "used_for", "description"]
    return specs_df[
        column_order + [col for col in specs_df.columns if col not in column_order]
    ]


def load_json_file(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_rn_stats(label_column: pd.Series) -> None:
    value_counts = label_column.value_counts()
    print(
        f"n_types={len(value_counts) - 1}, n_tokens={value_counts.sum()} "
        f"({value_counts.loc['none']} of which 'none')"
    )
