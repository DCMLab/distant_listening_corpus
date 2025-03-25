# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: dimcat
#     language: python
#     name: dimcat
# ---

# %%
import os

# %%
from enum import Enum

import ms3

# %%
# %load_ext autoreload
# %autoreload 2
import utils

# from processing.utils import create_specs

DLC_PATH = ms3.resolve_dir("..")
METADATA_PATH = "distant_listening_corpus.metadata.tsv"
DATASET = "pitch_arrays"

# %%
# bps1 = pd.read_csv("/home/laser/git/AugmentedNet/events/test/bps-01-op002-no1-1_joint.tsv", sep="\t")
# bps1.head()

# %%
# roman_numeral = bps1.a_romanNumeral.str.extract("(Ger|It|Fr|N|VII|VI|V|IV|III|II|I|vii|vi|v|iv|iii|ii|i)")
# bps1["degree1"] = ms3.transform(roman_numeral, utils.roman_numeral2scale_degree)
# bps1.head()

# %%
# bps1[bps1.a_degree1 != bps1.degree1]

# %%
# bps1[bps1.a_romanNumeral.str.contains("vii")]

# %%
utils.dataset_processing_stats(metadata_path=METADATA_PATH, dataset=DATASET)


# %%


# lpa = inspect("beethoven_piano_sonatas", "01-1")
# lpa


# %%
# corpus_subdir = "bach_en_fr_suites"
# corpus = utils.get_ms3_corpus(f"~/distant_listening_corpus/{corpus_subdir}")
# corpus

# %%
# piece = corpus["BWV806_01_Prelude"]
# facets = utils.get_facet_dict_from_piece(piece)

# %%
# utils.store_pitch_arrays_for_corpus(
#     corpus=corpus,
#     output_dir=DATASET,
#     metadata_path="distant_listening_corpus.metadata.tsv",
#     column_name=DATASET,
#     corpus_subdir=corpus_subdir,
#     reset=True
# )

# %%
# pitch_array = get_pitch_array_from_piece(piece)
# pitch_array


# %%
class Purpose(str, Enum):
    """Vocabulary defining what individual fields (columns) are used for.
    Description strings X fit gramatically as in "used for X"."""

    auxiliary = "computing fields"
    input = "input graph creation"
    metadata = "input graph metadata and informational purposes"
    beat_inference = "training beat inference task"
    cadence_induction = "training cadence induction task"
    harmony_inference = "training harmony inference task"
    phrase_inference = "training phrase inference task"
    section_inference = "training section inference task"
    note_degree_inference = "training note_degree inference task"
    filtering = "filtering notes based on the available annotations"
    # none = unused columns should not be included in the specs


tpc_description = (
    "Tonal Pitch Class (0=C, -1=F, 1=G, etc., aka specific pitch, aka fifths)"
)
specs_specs = dict(
    onset_div=dict(
        description="Proportional integer position",
        used_for=Purpose.input,
    ),
    duration_div=dict(
        description="Proportional integer duration",
        used_for=Purpose.input,
    ),
    onset_beat=dict(
        description="A continuous offset value measured in metrical beats whose durations depend "
        "on the denominators of the respective time signatures (and a measure's "
        "actual duration).",
        used_for=Purpose.input,
    ),
    pitch=dict(
        description="MIDI value",
        used_for=Purpose.input,
    ),
    tpc=dict(
        description=tpc_description,
        used_for=Purpose.auxiliary,
    ),
    step=dict(
        description="Note name without accidental (A-G)",
        used_for=Purpose.input,
    ),
    alter=dict(
        description="Note accidental: [-3, 3]",
        used_for=Purpose.input,
    ),
    beat_float=dict(
        description="The decimal beat position of any event within the current measure. A measure in n/m meter "
        "is considered to consist of n beats that have duration of 1/m of a whole note; except if "
        "n is a multiple of 3 (6, 9, 12, but not 3), in which case a measure is considered to have "
        "n/3 beats of length 3/m whole notes. All positions that fall in between downbeats are scaled "
        "linearly. For example, the first for eigths in a 9/8 meter have beat floats 1, 1.333, 1.667, "
        "2. Values are rounded to three decimals.",
        used_for=Purpose.auxiliary,
    ),
    downbeat=dict(
        description="Adopts the integer values from beat_float and the value 0 for the rest.",
        used_for=Purpose.beat_inference,
    ),
    is_downbeat=dict(
        description="Indicates whether an event falls on a downbeat or not. "
                    "Is False when downbeat == 0, True otherwise.",
        used_for=Purpose.beat_inference,
    ),
    ts_beats=dict(
        description="Numerator of the time signature",
        used_for=Purpose.input,
    ),
    ts_beat_type=dict(
        description="Denominator of the time signature",
        used_for=Purpose.input,
    ),
    staff=dict(
        description="Number of the staff containing the note, 1 being the upper staff",
        used_for=Purpose.input,
    ),
    voice=dict(
        description="Notational layer containing the note: [1, 4]",
        used_for=Purpose.input,
    ),
    duration=dict(
        description="Note duration expressed as fraction of a whole note",
        used_for=Purpose.auxiliary,
    ),
    is_note_onset=dict(
        description="False when a note is tied to a previous one",
        used_for=Purpose.input,
    ),
    ks_fifths=dict(
        description="Key signature: [-7, 7]",
        used_for=Purpose.input,
    ),
    mc=dict(
        description="Measure count, ID of the measure-like object (non-unique in unfolded score)",
        used_for=Purpose.metadata,
    ),
    mc_playthrough=dict(
        description="Measure count, unique in unfolded score",
        used_for=Purpose.metadata,
    ),
    mn=dict(
        description="Measure number as per conventions. One MN can be composed of several MC.",
        used_for=Purpose.metadata,
    ),
    mn_playthrough=dict(
        description="Conventional measure numbers but for unfolded score (means of identifying complete measures)",
        used_for=Purpose.input,
    ),
    octave=dict(
        description="Octave of the note with 4 = middle octave. Does not always correspond to pitch // 12 - 1.",
        used_for=Purpose.metadata,
    ),
    quarterbeats_playthrough=dict(
        description='Continuous offset ("qstamp") in unfolded score',
        used_for=Purpose.input,
    ),
    section_start=dict(
        description="True for notes on the first position following a double/repeat bar line or section break. "
        "True values always correspond to the beginning of an MC, so a section beginning with a rest "
        "will not be taken into account.",
        used_for=Purpose.section_inference,
    ),
    a_isOnset=dict(
        description="True for notes coinciding with a change in harmony.",
        used_for=Purpose.harmony_inference,
    ),
    cadence=dict(
        description="Original cadence label (my include cadence subtypes)",
        used_for=Purpose.auxiliary,
    ),
    cadence_type=dict(
        description="Cadence label ∈ (PAC, IAC, HC, EC, DC, PC)",
        used_for=Purpose.cadence_induction,
    ),
    phraseend=dict(
        description="Original phrase labels.",
        used_for=Purpose.auxiliary,
    ),
    a_phraseend=dict(
        description="True for all notes that coincide with the structural ending of a phrase (i.e., the phrase "
        "can have a codetta after this position before the next one begins).",
        used_for=Purpose.phrase_inference,
    ),
    unfolded_harmony_index=dict(
        description="Index of the labels in the original unfolded table (before merging it with the notes)",
        used_for=Purpose.auxiliary,
    ),
    label=dict(
        description="Original annotation labels",
        used_for=Purpose.auxiliary,
    ),
    globalkey_tpc=dict(
        description=f"Root of the global key expressed as {tpc_description}",
        used_for=Purpose.auxiliary,
    ),
    localkey_tpc=dict(
        description=f"Root of the local key expressed as {tpc_description}",
        used_for=Purpose.auxiliary,
    ),
    tonicized_tpc=dict(
        description=f"Root of the tonicized key expressed as {tpc_description}",
        used_for=Purpose.auxiliary,
    ),
    sic_with_local=dict(
        description="Relative position of the note's tonal pitch class in the local key, expressed as "
        "Specific Interval Class (0=unison, -1=+P4/-P5, 3=+M6/-m3, etc.)",
        used_for=Purpose.auxiliary,
    ),
    tpc_is_in_label=dict(
        description="True if a note's pitch class is part of the harmony label",
        used_for=Purpose.harmony_inference,
    ),
    tpc_is_root=dict(
        description="True if a note's tonal pitch class is the harmony label's root",
        used_for=Purpose.harmony_inference,
    ),
    tpc_is_bass=dict(
        description="True if a note's tonal pitch class is the harmony label's bass",
        used_for=Purpose.harmony_inference,
    ),
    a_degree1=dict(
        description="Chordal root expressed as scale degree, preceeded by '#' for sharps and '-' for flats,"
        "as music21 would output them. For applied chords, such as #vii/vi, the scale degree represents "
        "the numeral before the slash; the second part will be represented in a_degree2.",
        used_for=Purpose.harmony_inference,
    ),
    a_degree2=dict(
        description="Only defined for applied chords where this value expresses the tonicized key as a scale degree "
        "of the localkey in vigour. The format is the same as for a_degree1.",
        used_for=Purpose.harmony_inference,
    ),
    a_quality=dict(
        description="This is a mapping of the chord_type column to music21's vocabulary for chord qualities.",
        used_for=Purpose.harmony_inference,
    ),
    valid_chord_label=dict(
        description="True when a valid chord label is available for a note.",
        used_for=Purpose.filtering,
    ),
    valid_cadence_label=dict(
        description="True when some of the notes in a piece come with a cadence label.",
        used_for=Purpose.filtering,
    ),
    valid_phrase_label=dict(
        description="True when some of the notes in a piece come with a phrase label.",
        used_for=Purpose.filtering,
    ),
    valid_pedal_point_label=dict(
        description="True when pedal point annotations will be available for this piece if it has any (always True "
        "for DLC).",
        used_for=Purpose.filtering,
    ),
    valid_section_start_label=dict(
        description="True when some of the notes in a piece come with a section label.",
        used_for=Purpose.filtering,
    ),
    note_degree=dict(
        description="A string expressing a note's position relative to the scale of the localkey. "
        "E.g., for a passage in local key of F minor, "
        "F: '1', Ab: '3', A: '#3', C: '5', Ab: '6', A: '#6', Bb: '7', B: '#'. etc.",
        used_for=Purpose.note_degree_inference,
    ),
)


def inspect(corpus: str, piece: str):
    corpus_obj = utils.get_ms3_corpus(os.path.join(DLC_PATH, corpus))
    piece_obj = next(
        pce for piece_id, pce in corpus_obj.iter_pieces() if piece_id == piece
    )
    labeled_pitch_array = utils.get_pitch_array_from_piece(piece_obj)
    return labeled_pitch_array


lpa = inspect("beethoven_piano_sonatas", "01-1")
utils.create_and_store_specs(
    lpa, "dlc_pitch_array_specs.csv", specs_specs, "dlc_specs_specs.json"
)

# %%
# df = utils.load_labeled_pitch_array(
#     "labeld_pitch_array_specs.csv",
#     "pitch_arrays/kozeluh_sonatas/14op13no2c.tsv",
# )
# df

# %%
if __name__ == "__main__":
    utils.store_pitch_arrays_for_corpora(
        metacorpus_path=DLC_PATH,
        output_dir=DATASET,
        metadata_path=METADATA_PATH,
        column_name=DATASET,
        reset=False,
    )
