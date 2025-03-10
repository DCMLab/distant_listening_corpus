# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: dimcat
#     language: python
#     name: dimcat
# ---

# %%

import os
from enum import Enum

import ms3
import pandas as pd

from code.utils import make_pitch_array, prepare_labels, make_labeled_pitch_array

DLC_PATH = ms3.resolve_dir("~/distant_listening_corpus")


# %%
def filter_corpus(corpus):
    corpus.view.include("facets", "scores")#, "expanded")
    #corpus.disambiguate_facet("expanded")
    corpus.disambiguate_facet("scores")
    corpus.view.pieces_with_incomplete_facets = False
    
def get_ms3_corpus(corpus_path):
    corpus = ms3.Corpus(corpus_path)
    filter_corpus(corpus)
    return corpus

for subcorpus_dir in os.listdir(DLC_PATH):
    subcorpus_path = os.path.join(DLC_PATH, subcorpus_dir)
    if os.path.isfile(subcorpus_path): continue
    corpus = get_ms3_corpus(subcorpus_path)
    break
    
corpus

# %%
corpus = get_ms3_corpus("~/distant_listening_corpus/beethoven_piano_sonatas")

for _, piece in corpus.iter_pieces():
    break
    
for fileinfo, facets in piece.iter_extracted_facets(
        ("measures", "notes", "expanded"),
        force=True,
        unfold=True,
        interval_index=False
):
    break

measures = facets["measures"]
display(measures.head(3))
notes = facets["notes"]
notes.head(3)

# %%
pitch_array = make_pitch_array(notes, measures, label_notes=False)
pitch_array.to_csv("beethoven1.tsv", sep="\t", index=False)
pitch_array

# %%
labeled_pitch_array = make_labeled_pitch_array(
    notes=notes, 
    labels=facets["expanded"],
    measures=measures
)

tmp_labeled_pitch_array = labeled_pitch_array[[
    col for col 
    in labeled_pitch_array.columns 
    if col not in pitch_array.columns]]
tmp_labeled_pitch_array = prepare_labels(facets["expanded"])
labeled_pitch_array.to_csv("beethoven1_labeled.tsv", sep="\t", index=False)
labeled_pitch_array


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
    # none = unused columns should not be included in the specs


tpc_description = "Tonal Pitch Class (0=C, -1=F, 1=G, etc., aka specific pitch, aka fifths)"
spec_specs = dict(
    onset_div = dict(
        description = "Proportional integer position",
        used_for = Purpose.input,
        ),
    duration_div = dict(
        description = "Proportional integer duration",
        used_for = Purpose.input,
        ),
    pitch = dict(
        description = "MIDI value",
        used_for = Purpose.input,
        ),
    tpc = dict(
        description = tpc_description,
        used_for = Purpose.auxiliary,
        ),
    step = dict(
        description = "Note name without accidental (A-G)",
        used_for = Purpose.input,
        ),
    alter = dict(
        description = "Note accidental: [-3, 3]",
        used_for = Purpose.input,
        ),
    ts_beats = dict(
        description = "Numerator of the time signature",
        used_for = Purpose.input,
        ),
    ts_beat_type = dict(
        description = "Denominator of the time signature",
        used_for = Purpose.input,
        ),
    staff = dict(
        description = "Number of the staff containing the note, 1 being the upper staff",
        used_for = Purpose.input,
        ),
    voice = dict(
        description = "Notational layer containing the note: [1, 4]",
        used_for = Purpose.input,
        ),
    is_note_onset = dict(
        description = "False when a note is tied to a previous one",
        used_for = Purpose.input,
        ),
    beat = dict(
        description = "Values >= 1. Natural numbers represent beat positions according to the time signature. "
                      "The number of beats in a measure is defined by ts_beats but divided by 3 if it's a multiple of 3.",
        used_for = Purpose.beat_inference,
        ),
    ks_fifths = dict(
        description = "Key signature: [-7, 7]",
        used_for = Purpose.input,
        ),
    mc = dict(
        description = "Measure count, ID of the measure-like object (non-unique in unfolded score)",
        used_for = Purpose.metadata,
        ),
    mn = dict(
        description = "Measure number as per conventions. One MN can be composed of several MC.",
        used_for = Purpose.metadata,
        ),
    mc_playthrough = dict(
        description = "Measure count, unique in unfolded score",
        used_for = Purpose.metadata,
        ),
    mn_playthrough = dict(
        description = "Conventional measure numbers but for unfolded score (means of identifying complete measures)",
        used_for = Purpose.input,
        ),
    quarterbeats_playthrough = dict(
        description = "Continuous offset (\"qstamp\") in unfolded score",
        used_for = Purpose.input,
        ),
    duration = dict(
        description = "Note duration expressed as fraction of a whole note",
        used_for = Purpose.auxiliary,
        ),
    section_start = dict(
        description = "True for notes on the first position following a double/repeat bar line or section break. "
                      "True values always correspond to the beginning of an MC, so a section beginning with a rest "
                      "will not be taken into account.",
        used_for = Purpose.section_inference,
    ),
    octave = dict(
        description = "Octave of the note with 4 = middle octave. Does not always correspond to pitch // 12 - 1.",
        used_for = Purpose.metadata,
    ),
    is_harmony_onset = dict(
        description = "True for notes coinciding with a change in harmony.",
        used_for = Purpose.harmony_inference,
    ),
    cadence = dict(
        description = "Original cadence label (my include cadence subtypes)",
        used_for = Purpose.auxiliary,
    ),
    cadence_type = dict(
        description = "Cadence label ∈ (PAC, IAC, HC, EC, DC, PC)",
        used_for = Purpose.cadence_induction,
    ),
    phraseend = dict(
        description = "Original phrase labels.",
        used_for = Purpose.auxiliary,
    ),
    is_phrase_ending = dict(
        description = "True for notes that coincide with the structural ending of a phrase (i.e., the phrase can have "
                      "a codetta after this position before the next one begins).",
        used_for = Purpose.phrase_inference,
    ),
    unfolded_harmony_index = dict(
        description = "Index of the labels in the original unfolded table (before merging it with the notes)",
        used_for = Purpose.auxiliary,
    ),
    label = dict(
        description = "Original annotation labels",
        used_for = Purpose.auxiliary,
    ),
    globalkey_tpc = dict(
        description = f"Root of the global key expressed as {tpc_description}",
        used_for = Purpose.auxiliary,
    ),
    localkey_tpc = dict(
        description = f"Root of the local key expressed as {tpc_description}",
        used_for = Purpose.auxiliary,
    ),
    tonicized_tpc = dict(
        description = f"Root of the tonicized key expressed as {tpc_description}",
        used_for = Purpose.auxiliary,
    ),
    sic_with_local = dict(
        description = "Relative position of the note's tonal pitch class in the local key, expressed as "
                      "Specific Interval Class (0=unison, -1=+P4/-P5, 3=+M6/-m3, etc.)",
        used_for = Purpose.auxiliary,
    ),
    tpc_is_in_label = dict(
        description = "True if a note's pitch class is part of the harmony label",
        used_for = Purpose.harmony_inference,
    ),
    tpc_is_root = dict(
        description = "True if a note's tonal pitch class is the harmony label's root",
        used_for = Purpose.harmony_inference,
    ),
    tpc_is_bass = dict(
        description = "True if a note's tonal pitch class is the harmony label's bass",
        used_for = Purpose.harmony_inference,
    ),
)

specs = labeled_pitch_array.dtypes.rename("dtype")
specs_df = pd.concat([
    specs,
    pd.DataFrame.from_dict(spec_specs, orient="index")
], axis=1)[["dtype", "used_for", "description"]]
specs_df.to_csv("labeld_pitch_array_specs.csv", index=True)
specs_df

# %%
