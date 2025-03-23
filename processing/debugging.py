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

import ms3
import pandas as pd

# %%
# %load_ext autoreload
# %autoreload 2
from processing import utils

DLC_PATH = ms3.resolve_dir("..")

# %%
SIMPLE_NUMERAL_AUGNET = [
    "none",
    # from here: AugmentedNet in decending order of frequency
    # n_types=132+1, n_tokens=760222 (522 of which 'none')
    "I",
    "V7",
    "V",
    "i",
    "viio7",
    "IV",
    "ii",
    "viio",
    "vi",
    "iv",
    "VI",
    "ii7",
    "ii%7",
    "Cad",
    "v",
    "N",
    "Ger7",
    "V9",
    "iii",
    "III",
    "iio",
    "vii%7",
    "vi7",
    "VII",
    "iv7",
    "IV7",
    "iio7",
    "I7",
    "It",
    "bVI",
    "VI7",
    "III+",
    "I+",
    "V+",
    "i7",
    "bVII",
    "Fr7",
    "III7",
    "vii",
    "iii7",
    "vi%7",
    "II7",
    "II",
    "V+7",
    "v7",
    "N7",
    "iiio",
    "III+7",
    "vii7",
    "#iio7",
    "Ger",
    "bVII7",
    "Fr",
    "bVI7",
    "IV+",
    "VII7",
    "#ivo7",
    "bV",
    "#io7",
    "iiio7",
    "bvi",
    "bvii",
    "#vio7",
    "#vii%7",
    "#vo7",
    "ii%",
    "vio",
    "vo",
    "V79",
    "VI+7",
    "#io",
    "#ivo",
    "vii%",
    "#V",
    "ii9",
    "bIII",
    "VI+",
    "v%7",
    "#vi%7",
    "#iii",
    "ivo7",
    "#iio",
    "bviio7",
    "#vio",
    "biii",
    "vio7",
    "#vo",
    "IV9",
    "iii%7",
    "#iv%7",
    "bIV7",
    "iv9",
    "bvii7",
    "vii+",
    "#iv",
    "io",
    "ivo",
    "#iiio7",
    "vo7",
    "iv%7",
    "#i",
    "I+7",
    "N+",
    "#vi7",
    "#vii",
    "#vii7",
    "bII",
    "bV7",
    "#iiio",
    "#vi",
    "#vii%",
    "vii%9",
    "#iv7",
    "VII+",
    "bi",
    "bVI+",
    "bbVII",
    "II+",
    "I9",
    "ii%9",
    "#III",
    "N+7",
    "bbvii",
    "iii9",
    "bv",
    "biv",
    "bi7",
    "bii7",
    "biio",
    "bI",
    "bviio",
    "#VII",
]
dlc_labels = ms3.load_tsv(
    "/home/laser/Documents/Linz/DLC_version_comparison/distant_listening_corpus_v3.1/"
    "distant_listening_corpus.expanded.tsv"
)

# %%
dlc_labels.chord.notna().sum()

# %%
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


numeral = dlc_labels.numeral.replace(REPLACE_ROOT).rename("a_simpleNumeral")

reference_is_minor = dlc_labels.relativeroot.str.islower().fillna(
    dlc_labels.localkey_is_minor
)
add_flat_for_67_minor = dlc_labels.numeral.isin(("vi", "vii")) & reference_is_minor
numeral = numeral.where(
    ~add_flat_for_67_minor, dlc_labels.numeral.replace({"vi": "bvi", "vii": "bvii"})
)

remove_sharp_for_67_in_minor = (
    dlc_labels.numeral.isin(("#vi", "#vii")) & reference_is_minor
)  # ToDo: resolve_relative )
numeral = numeral.where(
    ~remove_sharp_for_67_in_minor,
    dlc_labels.numeral.replace({"#vi": "vi", "#vii": "vii"}),
)


# add adapted chord type
adapted_chord_type = dlc_labels.chord_type.replace(ADAPT_CHORD_TYPE)
numeral = numeral + adapted_chord_type

cadential_V_mask = (dlc_labels.numeral == "V") & dlc_labels.changes.str.contains(
    "64"
).fillna(False)
numeral = numeral.where(~cadential_V_mask, "Cad")

special_column = dlc_labels.special.replace(ADAPT_SPECIAL_CHORDS)
numeral = numeral.where(special_column.isna(), special_column)

ninths = pd.Series("9", index=dlc_labels.index).where(
    dlc_labels.changes.str.contains("9"), ""
)


a_romanNumeral = numeral  # + ninths
utils.print_rn_stats(a_romanNumeral)
transformed_numeral_counts = a_romanNumeral.value_counts()
transformed_numeral_counts

# %%
vocabulary_union = set(transformed_numeral_counts.index).union(
    set(SIMPLE_NUMERAL_AUGNET)
)
dlc_exclusive = list(
    set(transformed_numeral_counts.index).difference(set(SIMPLE_NUMERAL_AUGNET))
)
print(
    f"{len(SIMPLE_NUMERAL_AUGNET)=}; {len(dlc_exclusive)=}; => {len(vocabulary_union)=}"
)
dlc_exclusive

# %%
len(dlc_exclusive) + len(SIMPLE_NUMERAL_AUGNET)

# %%
# ADAPT_CHORD_TYPE = {
#     "M": "",
#     "m": "",
#     "Mm7": "7",
#     "mm7": "7",
#     "MM7": "7",
#     "%7": "ø7",
# }
# ADAPT_SPECIAL_CHORDS = {
#     "Fr": "Fr7",
#     "Ger": "Ger7",
# }
#
# def replace_roman_numerals(column):
#     column = column.replace("bII", "N")
#     column = column.replace("#vii", "vii")
#     return column
#
#
# numeral = replace_roman_numerals(dlc_labels.numeral)
# adapted_chord_type = dlc_labels.chord_type.replace(ADAPT_CHORD_TYPE)
# numeral = numeral + adapted_chord_type
# cadential_V_mask = (dlc_labels.numeral == "V") & dlc_labels.changes.str.contains("64").fillna(False)
# numeral = numeral.where(~cadential_V_mask, "Cad")
# special_column = dlc_labels.special.replace(ADAPT_SPECIAL_CHORDS)
# numeral = numeral.where(special_column.isna(), special_column)
# relativeroot = replace_roman_numerals(dlc_labels.relativeroot)
# a_romanNumeral = (numeral + ("/" + relativeroot).fillna(""))
# transformed_numeral_counts = a_romanNumeral.value_counts()
# transformed_numeral_counts

# %%
transformed_numeral_counts.sum()

# %%
accu = 0
for i, (label, cnt) in enumerate(transformed_numeral_counts.items(), 1):
    if label not in SIMPLE_NUMERAL_AUGNET:
        accu += cnt
        print(f"{i}: {label} ({cnt})")
accu

# %%
dlc_labels[cadential_V_mask]


# %%
def inspect(corpus: str, piece: str):
    corpus_obj = utils.get_ms3_corpus(os.path.join(DLC_PATH, corpus))
    piece_obj = next(
        pce for piece_id, pce in corpus_obj.iter_pieces() if piece_id == piece
    )
    labeled_pitch_array = utils.get_pitch_array_from_piece(piece_obj)
    return labeled_pitch_array


c_name, p_name = (
    "bach_en_fr_suites",
    "BWV809_07_Gigue",
)  # "beethoven_piano_sonatas", "01-1"  #
# lpa = inspect(c_name, p_name)
# lpa

# %%
corpus = utils.get_ms3_corpus(f"~/distant_listening_corpus/{c_name}")
piece = corpus[p_name]
measures, notes, labels = utils.get_unfolded_facets_from_piece(piece)


# %%
# prepared_m = utils.prepare_measures(measures)
# prepared_m.dtypes

# %%
prepared_notes = utils.prepare_notes_with_measure_information(
    notes, measures, label_notes=True
)
prepared_notes

# %%
prepared_notes.quarterbeats_playthrough.isna().any()
