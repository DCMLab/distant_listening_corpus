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

import ms3
import pandas as pd

# %%
DLC_PATH = ms3.resolve_dir("..")

# %%
dlc_metadata = ms3.load_tsv(
    "distant_listening_corpus.metadata.tsv", index_col=["corpus", "piece"]
)
dlc_metadata = dlc_metadata[dlc_metadata.label_count > 0]
dlc_metadata

# %%
pieces_per_corpus = dlc_metadata.groupby("corpus").size()
piece_is_in_minor = dlc_metadata.annotated_key.str.islower()
piece_mode = (
    piece_is_in_minor.groupby("corpus")
    .value_counts()
    .unstack()
    .fillna(0)
    .astype(int)
    .rename(columns={False: "major", True: "minor"})
)

# %%
div5, mod5 = pieces_per_corpus.divmod(5)
n_test = div5
n_train_val = 4 * n_test + mod5
split_size = pd.DataFrame(
    dict(
        N=pieces_per_corpus,
        n_major=piece_mode.major,
        n_minor=piece_mode.minor,
        n_test=n_test,
        n_train_val=n_train_val,
    )
)


def min_maj_test_split(row) -> pd.Series:
    if row.n_test == 0:
        return pd.Series(dict(n_test_major=0, n_test_minor=0, case="zero"))
    half, uneven = divmod(row.n_test, 2)
    if not uneven:
        if row.n_minor > half and row.n_major > half:
            return pd.Series(dict(n_test_major=half, n_test_minor=half, case="even"))
        # else case does not occur
    if row.n_minor > half + 1:
        return pd.Series(
            dict(n_test_major=half + 1, n_test_minor=half + 1, case="made_even")
        )
    # currently, there's always more major than minor, so we use half of the minor that's there
    n_minor = row.n_minor // 2
    return pd.Series(
        dict(n_test_major=row.n_test - n_minor, n_test_minor=n_minor, case="uneven")
    )


test_min_maj = split_size.apply(min_maj_test_split, axis=1)
pd.concat([split_size, test_min_maj], axis=1)
