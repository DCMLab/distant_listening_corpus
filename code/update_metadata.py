#!/usr/bin/env python
# coding: utf-8
"""Script to update the data.metadata.tsv file, its descriptor, and the overview tables at the bottom of the README.
When the file is executed, it assumes to be located in a folder at the top level of a full recursive clone of
https://github.com/Chorale-Corpus/data

Requirements:

    pip install ms3
"""

import os
import subprocess
from typing import Optional
from ms3.utils import concat_metadata


def update_metadata():
    """Calls ms3 transform, assuming that the current working directory is a meta-corpus."""
    subprocess.call(["ms3", "transform", "-D", "--resources", "--uncompressed"])

def main(
        path: Optional[str] = None
):
    """Do the thing. Assumes the current working directory to be a meta-corpus."""
    if path is None:
        path = os.getcwd()
    update_metadata()
    concat_metadata(
        meta_corpus_dir=path,
        out=path,
        tsv_name="distant_listening_corpus.metadata.tsv",
    )



def run(
        path: Optional[str] = None
):
    """Set up the desired parameters."""
    previous_cwd = None
    if path is not None:
        # change the current working directory to the target path and then change back
        previous_cwd = os.getcwd()
        os.chdir(path)

    try:
        main()
    finally:
        if previous_cwd:
            os.chdir(previous_cwd)



if __name__ == "__main__":
    this_file = os.path.abspath(__file__)
    path = os.path.abspath(
        os.path.join(
            os.path.dirname(this_file),
            ".."
        )
    )
    run(path)
