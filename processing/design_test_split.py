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
excluded_pieces = [
    ("ABC", "n01op18-1_01"),
    ("ABC", "n01op18-1_03"),
    ("ABC", "n06op18-6_03"),
    ("ABC", "n07op59-1_01"),
    ("ABC", "n08op59-2_03"),
    ("ABC", "n10op74_03"),
    ("ABC", "n10op74_04"),
    ("ABC", "n11op95_03"),
    ("ABC", "n12op127_02"),
    ("ABC", "n16op135_02"),
    ("beethoven_piano_sonatas", "01-1"),
    ("beethoven_piano_sonatas", "07-1"),
    ("beethoven_piano_sonatas", "10-1"),
    ("beethoven_piano_sonatas", "23-1"),
    ("monteverdi_madrigals", "5-04d"),
]

# %%
dlc_metadata = ms3.load_tsv(
    "distant_listening_corpus.metadata.tsv", index_col=["corpus", "piece"]
)
dlc_summary = pd.read_csv(
    "/home/laser/git/AugmentedNet/dlc_summary.tsv",
    sep="\t",
    index_col=["corpus", "piece"],
)
dlc_metadata = dlc_metadata[dlc_metadata.label_count > 0]  # only annotated pieces
dlc_metadata = pd.concat([dlc_metadata, dlc_summary], axis=1)
dlc_metadata = dlc_metadata.loc[
    dlc_metadata.index.difference(excluded_pieces)
]  # without excluded pieces
N_overall = len(dlc_metadata)
dlc_metadata


# %%


# %%
def compute_split_dimensions(
    dlc_metadata: pd.DataFrame, size_of_test_set: int = 0
) -> pd.DataFrame:
    """If size_of_test_set < 1, the size will be roughly a 5th of the total."""
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

    div5, mod5 = pieces_per_corpus.divmod(5)
    if size_of_test_set > 0:
        filtered_pieces_per_corpus = pieces_per_corpus.where(pieces_per_corpus > 5, 0)
        proportional_size = (
            filtered_pieces_per_corpus.div(len(dlc_metadata)) * size_of_test_set
        )
        n_test = proportional_size.round().astype(int)
        n_train_val = pieces_per_corpus - n_test
    else:
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
            if row.n_major > half and row.n_minor > half:
                return pd.Series(
                    dict(n_test_major=half, n_test_minor=half, case="even")
                )
            else:
                for decrease in range(0, half):
                    decreased_half = half - decrease
                    if row.n_major > decreased_half and row.n_minor > decreased_half:
                        return pd.Series(
                            dict(
                                n_test_major=decreased_half,
                                n_test_minor=decreased_half,
                                case="decreased",
                            )
                        )
                else:
                    return pd.Series(
                        dict(n_test_major=0, n_test_minor=0, case="imbalanced")
                    )
        if row.n_minor > half + 1:
            return pd.Series(
                dict(n_test_major=half + 1, n_test_minor=half + 1, case="increased")
            )
        # currently, there's always more major than minor, so we use half of the minor that's there
        n_minor = row.n_minor // 2
        return pd.Series(
            dict(n_test_major=row.n_test - n_minor, n_test_minor=n_minor, case="uneven")
        )

    test_min_maj = split_size.apply(min_maj_test_split, axis=1)
    split_dimensions = pd.concat([split_size, test_min_maj], axis=1)
    return split_dimensions


split_dimensions = compute_split_dimensions(dlc_metadata)
split_dimensions

# %% [markdown]
# # Fully annotated pieces only

# %%
dlc_fully = dlc_metadata[
    dlc_metadata.has_chords & dlc_metadata.has_cadence & dlc_metadata.has_phrase
].copy()
piece_mode_column = dlc_fully.annotated_key.str.islower().replace(
    {False: "major", True: "minor"}
)
if "piece_mode" in dlc_fully.columns:
    dlc_fully["piece_mode"] = piece_mode_column
else:
    dlc_fully.insert(0, "piece_mode", piece_mode_column)
n_test_pieces = N_overall // 5
print(
    f"{len(dlc_fully)}/{N_overall} have been fully annotated. We will pick {N_overall} // 5 = { n_test_pieces } "
    f"from those."
)
fully_annotated_split_dimensions = compute_split_dimensions(
    dlc_fully, size_of_test_set=n_test_pieces
)
n_test_pieces = (
    fully_annotated_split_dimensions[["n_test_major", "n_test_minor"]].sum().sum()
)
print(f"Resulting size of test set: {n_test_pieces}")
fully_annotated_split_dimensions

# %%
test_set_names, test_set_ids = [], []
for (c_name, mode), group_df in dlc_fully.groupby(["corpus", "piece_mode"]):
    sample_n = fully_annotated_split_dimensions.loc[c_name, f"n_test_{mode}"]
    sample = group_df.sample(n=sample_n, random_state=12)
    sampled_ids = sample.index.tolist()
    test_set_ids.extend(sampled_ids)
    sampled_nicknames = [f"{c_name}_{p_name}" for c_name, p_name in sampled_ids]
    test_set_names.extend(sampled_nicknames)
print(len(test_set_names))
list(sorted(test_set_names))

# %%
dlc_metadata.loc[test_set_ids, "split"] = "test"
ms3.write_tsv(dlc_metadata, "distant_listening_corpus.metadata.tsv", index=True)
dlc_metadata
