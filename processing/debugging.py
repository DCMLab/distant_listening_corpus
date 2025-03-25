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


def get_labels(corpus: str, piece: str):
    corpus_obj = utils.get_ms3_corpus(os.path.join(DLC_PATH, corpus))
    piece_obj = next(
        pce for piece_id, pce in corpus_obj.iter_pieces() if piece_id == piece
    )
    _, _, labels = utils.get_unfolded_facets_from_piece(piece_obj)
    return labels


def get_prepared_labels(corpus: str, piece: str):
    labels = get_labels(corpus=corpus, piece=piece)
    return utils.prepare_labels(labels)


c_name, p_name = "ABC", "n01op18-1_01"  # "beethoven_piano_sonatas", "01-1"  #
lpa = inspect(c_name, p_name)
lpa
# labels = get_prepared_labels(c_name, p_name)
# labels[labels.chord == "V(64)"]

# %%
lpa[lpa.sic_with_local.isna()]

# %%
dlc_labels = ms3.load_tsv(
    "/home/laser/Documents/Linz/DLC_version_comparison/distant_listening_corpus_v3.1/"
    "distant_listening_corpus.expanded.tsv"
)

# %%
dlc_labels.chord.notna().sum()

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
