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

from processing import utils

DLC_PATH = ms3.resolve_dir("..")


def inspect(corpus: str, piece: str):
    corpus_obj = utils.get_ms3_corpus(os.path.join(DLC_PATH, corpus))
    piece_obj = next(
        pce for piece_id, pce in corpus_obj.iter_pieces() if piece_id == piece
    )
    labeled_pitch_array = utils.get_pitch_array_from_piece(piece_obj)
    return labeled_pitch_array
