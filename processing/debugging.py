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

# %%
# %load_ext autoreload
# %autoreload 2
from processing import utils

DLC_PATH = ms3.resolve_dir("..")


# %%
def inspect(corpus: str, piece: str):
    corpus_obj = utils.get_ms3_corpus(os.path.join(DLC_PATH, corpus))
    piece_obj = next(
        pce for piece_id, pce in corpus_obj.iter_pieces() if piece_id == piece
    )
    labeled_pitch_array = utils.get_pitch_array_from_piece(piece_obj)
    return labeled_pitch_array


c_name, p_name = "kozeluh_sonatas", "28op30no1a"  # "beethoven_piano_sonatas", "01-1"  #
# lpa = inspect(c_name, p_name)
# lpa

# %%
corpus = utils.get_ms3_corpus(f"~/distant_listening_corpus/{c_name}")
piece = corpus[p_name]
facets = utils.get_facet_dict_from_piece(piece)
notes = facets["notes"]
labels = facets["expanded"]
measures = facets["measures"]

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
