![Version](https://img.shields.io/github/v/release/DCMLab/distant_listening_corpus?display_name=tag)
[![DOI](https://zenodo.org/badge/{{ zenodo_badge_id }}.svg)](https://zenodo.org/badge/latestdoi/{{ zenodo_badge_id }})
![GitHub repo size](https://img.shields.io/github/repo-size/DCMLab/distant_listening_corpus)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-9cf)


This is a README file for a data repository originating from the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora)
and serves as welcome page for both 

* the GitHub repo [https://github.com/DCMLab/distant_listening_corpus](https://github.com/DCMLab/distant_listening_corpus) and the corresponding
* documentation page [https://dcmlab.github.io/distant_listening_corpus](https://dcmlab.github.io/distant_listening_corpus)

For information on how to obtain and use the dataset, please refer to [this documentation page](https://dcmlab.github.io/distant_listening_corpus/introduction).

<!-- TOC -->
* [The Distant Listening Corpus](#the-distant-listening-corpus)
  * [Cite as](#cite-as)
  * [Version history](#version-history)
  * [Getting the data](#getting-the-data)
    * [With full version history](#with-full-version-history)
    * [Without full version history](#without-full-version-history)
  * [Data Formats](#data-formats)
    * [Opening Scores](#opening-scores)
    * [Opening TSV files in a spreadsheet](#opening-tsv-files-in-a-spreadsheet)
    * [Loading TSV files in Python](#loading-tsv-files-in-python)
  * [How to read `metadata.tsv`](#how-to-read-metadatatsv)
    * [File information](#file-information)
    * [Composition information](#composition-information)
    * [Score information](#score-information)
    * [Identifiers](#identifiers)
  * [Generating all TSV files from the scores](#generating-all-tsv-files-from-the-scores)
  * [Questions, Suggestions, Corrections, Bug Reports](#questions-suggestions-corrections-bug-reports)
  * [License](#license)
* [Overview](#overview)
  * [ABC](#abc)
  * [bach_en_fr_suites](#bach_en_fr_suites)
  * [bach_solo](#bach_solo)
  * [bartok_bagatelles](#bartok_bagatelles)
  * [beethoven_piano_sonatas](#beethoven_piano_sonatas)
  * [c_schumann_lieder](#c_schumann_lieder)
  * [chopin_mazurkas](#chopin_mazurkas)
  * [corelli](#corelli)
  * [couperin_clavecin](#couperin_clavecin)
  * [couperin_concerts](#couperin_concerts)
  * [cpe_bach_keyboard](#cpe_bach_keyboard)
  * [debussy_suite_bergamasque](#debussy_suite_bergamasque)
  * [dvorak_silhouettes](#dvorak_silhouettes)
  * [frescobaldi_fiori_musicali](#frescobaldi_fiori_musicali)
  * [grieg_lyric_pieces](#grieg_lyric_pieces)
  * [handel_keyboard](#handel_keyboard)
  * [jc_bach_sonatas](#jc_bach_sonatas)
  * [kleine_geistliche_konzerte](#kleine_geistliche_konzerte)
  * [kozeluh_sonatas](#kozeluh_sonatas)
  * [liszt_pelerinage](#liszt_pelerinage)
  * [mahler_kindertotenlieder](#mahler_kindertotenlieder)
  * [medtner_tales](#medtner_tales)
  * [mendelssohn_quartets](#mendelssohn_quartets)
  * [mozart_piano_sonatas](#mozart_piano_sonatas)
  * [pergolesi_stabat_mater](#pergolesi_stabat_mater)
  * [peri_euridice](#peri_euridice)
  * [pleyel_quartets](#pleyel_quartets)
  * [poulenc_mouvements_perpetuels](#poulenc_mouvements_perpetuels)
  * [rachmaninoff_piano](#rachmaninoff_piano)
  * [ravel_piano](#ravel_piano)
  * [scarlatti_sonatas](#scarlatti_sonatas)
  * [schubert_winterreise](#schubert_winterreise)
  * [schulhoff_suite_dansante_en_jazz](#schulhoff_suite_dansante_en_jazz)
  * [schumann_kinderszenen](#schumann_kinderszenen)
  * [schumann_liederkreis](#schumann_liederkreis)
  * [sweelinck_keyboard](#sweelinck_keyboard)
  * [tchaikovsky_seasons](#tchaikovsky_seasons)
  * [wagner_overtures](#wagner_overtures)
  * [wf_bach_sonatas](#wf_bach_sonatas)
<!-- TOC -->

# The Distant Listening Corpus

This corpus has been created within the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora) and employs
the [DCML harmony annotation standard](https://github.com/DCMLab/standards).

The publication covers the following public corpora (the DOI links always point at the latest version respectively):

* [Ludwig van Beethoven - String Quartets](https://zenodo.org/doi/10.5281/zenodo.7441343)
* [Ludwig van Beethoven - Piano Sonatas](https://doi.org/10.5281/zenodo.7473560)
* [Frédéric Chopin - Mazurkas](https://doi.org/10.5281/zenodo.7473566)
* [Arcangelo Corelli – Trio Sonatas](https://zenodo.org/doi/10.5281/zenodo.7504011)
* [Claude Debussy - Suite Bergamasque](https://doi.org/10.5281/zenodo.7473568)
* [Antonín Dvořák - Silhouettes](https://doi.org/10.5281/zenodo.7473576)
* [Edvard Grieg - Lyric Pieces](https://doi.org/10.5281/zenodo.7473578)
* [Franz Liszt - Années de Pèlerinage](https://doi.org/10.5281/zenodo.7473580)
* [Nikolai Medtner - Tales](https://doi.org/10.5281/zenodo.7473528)
* [Wolfgang Amadeus Mozart - Piano Sonatas](https://zenodo.org/doi/10.5281/zenodo.7424962)
* [Robert Schumann - Kinderszenen](https://doi.org/10.5281/zenodo.7473582)
* [Pyotr Tchaikovsky - The Seasons](https://doi.org/10.5281/zenodo.7473586)

Moreover, it covers the following corpora that will become public with publication of the DLC data report:

* J.S. Bach – English and French Suites
* J.S. Bach – Solo Pieces (A corpus of annotated scores)
* Béla Bartók – 14 Bagatelles, Op. 6
* François Couperin – L'art de toucher le clavecin
* François Couperin – Concerts Royaux
* Clara Schumann – Lieder
* Carl Philipp Emanuel Bach – Works for Keyboard
* Girolamo Frescobaldi (1583-1643) – Fiori Musicali, op. 12 (1635)
* Georg Friedrich Händel – Grobschmied Variations (The Harmonious Blacksmith), HWV 430
* J.C. Bach – Keyboard Sonatas
* Heinrich Schütz – Kleine Geistliche Konzerte
* Leopold Koželuch – Piano Sonatas
* Gustav Mahler – Kindertotenlieder
* Felix Mendelssohn – String Quartets
* Giovanni Battista Pergolesi – Stabat Mater (1736)
* Jacopo Peri – Euridice (1600)
* Ignaz Pleyel – String Quartets
* Francis Poulenc – Mouvements Perpetuels
* Sergei Rachmaninoff – Piano Pieces
* Maurice Ravel – Piano Pieces
* Domenico Scarlatti – Keyboard Sonatas
* Franz Schubert – Winterreise
* Erwin Schulhoff – Suite dansante en jazz
* Robert Schumann – Liederkreis
* Jan Sweelinck – Organ Pieces
* Richard Wagner – OverturesWilhelm Friedemann Bach – Piano Sonatas


## Cite as

## Version history

See the [GitHub releases](https://github.com/DCMLab/distant_listening_corpus/releases).
## Getting the data

### With full version history

The dataset is version-controlled via [git](https://git-scm.com/). In
order to download the files with all revisions they have gone through,
git needs to be installed on your machine. Then you can clone this
repository using the command

``` bash
git clone --recurse-submodules -j8 https://github.com/DCMLab/distant_listening_corpus.git
```

`-j8` is available from git \>= 2.8 and fetches up to 8 submodules at a
time in parallel

### Without full version history

If you are only interested in the current version of the corpus, you can
download the ZIP file of each submodule:

-   [ABC](https://github.com/DCMLab/ABC/archive/refs/heads/main.zip)
-   [bach_en_fr_suites](https://github.com/DCMLab/bach_en_fr_suites/archive/refs/heads/main.zip)
-   [bach_solo](https://github.com/DCMLab/bach_solo/archive/refs/heads/main.zip)
-   [bartok_bagatelles](https://github.com/DCMLab/bartok_bagatelles/archive/refs/heads/main.zip)
-   [beethoven_piano_sonatas](https://github.com/DCMLab/beethoven_piano_sonatas/archive/refs/heads/main.zip)
-   [c_schumann_lieder](https://github.com/DCMLab/c_schumann_lieder/archive/refs/heads/main.zip)
-   [chopin_mazurkas](https://github.com/DCMLab/chopin_mazurkas/archive/refs/heads/main.zip)
-   [corelli](https://github.com/DCMLab/corelli/archive/refs/heads/main.zip)
-   [couperin_clavecin](https://github.com/DCMLab/couperin_clavecin/archive/refs/heads/main.zip)
-   [couperin_concerts](https://github.com/DCMLab/couperin_concerts/archive/refs/heads/main.zip)
-   [cpe_bach_keyboard](https://github.com/DCMLab/cpe_bach_keyboard/archive/refs/heads/main.zip)
-   [debussy_suite_bergamasque](https://github.com/DCMLab/debussy_suite_bergamasque/archive/refs/heads/main.zip)
-   [dvorak_silhouettes](https://github.com/DCMLab/dvorak_silhouettes/archive/refs/heads/main.zip)
-   [frescobaldi_fiori_musicali](https://github.com/DCMLab/frescobaldi_fiori_musicali/archive/refs/heads/main.zip)
-   [grieg_lyric_pieces](https://github.com/DCMLab/grieg_lyric_pieces/archive/refs/heads/main.zip)
-   [handel_keyboard](https://github.com/DCMLab/handel_keyboard/archive/refs/heads/main.zip)
-   [jc_bach_sonatas](https://github.com/DCMLab/jc_bach_sonatas/archive/refs/heads/main.zip)
-   [kleine_geistliche_konzerte](https://github.com/DCMLab/kleine_geistliche_konzerte/archive/refs/heads/main.zip)
-   [kozeluh_sonatas](https://github.com/DCMLab/kozeluh_sonatas/archive/refs/heads/main.zip)
-   [liszt_pelerinage](https://github.com/DCMLab/liszt_pelerinage/archive/refs/heads/main.zip)
-   [mahler_kindertotenlieder](https://github.com/DCMLab/mahler_kindertotenlieder/archive/refs/heads/main.zip)
-   [medtner_tales](https://github.com/DCMLab/medtner_tales/archive/refs/heads/main.zip)
-   [mendelssohn_quartets](https://github.com/DCMLab/mendelssohn_quartets/archive/refs/heads/main.zip)
-   [mozart_piano_sonatas](https://github.com/DCMLab/mozart_piano_sonatas/archive/refs/heads/main.zip)
-   [pergolesi_stabat_mater](https://github.com/DCMLab/pergolesi_stabat_mater/archive/refs/heads/main.zip)
-   [peri_euridice](https://github.com/DCMLab/peri_euridice/archive/refs/heads/main.zip)
-   [pleyel_quartets](https://github.com/DCMLab/pleyel_quartets/archive/refs/heads/main.zip)
-   [poulenc_mouvements_perpetuels](https://github.com/DCMLab/poulenc_mouvements_perpetuels/archive/refs/heads/main.zip)
-   [rachmaninoff_piano](https://github.com/DCMLab/rachmaninoff_piano/archive/refs/heads/main.zip)
-   [ravel_piano](https://github.com/DCMLab/ravel_piano/archive/refs/heads/main.zip)
-   [scarlatti_sonatas](https://github.com/DCMLab/scarlatti_sonatas/archive/refs/heads/main.zip)
-   [schubert_winterreise](https://github.com/DCMLab/schubert_winterreise/archive/refs/heads/main.zip)
-   [schulhoff_suite_dansante_en_jazz](https://github.com/DCMLab/schulhoff_suite_dansante_en_jazz/archive/refs/heads/main.zip)
-   [schumann_kinderszenen](https://github.com/DCMLab/schumann_kinderszenen/archive/refs/heads/main.zip)
-   [schumann_liederkreis](https://github.com/DCMLab/schumann_liederkreis/archive/refs/heads/main.zip)
-   [sweelinck_keyboard](https://github.com/DCMLab/sweelinck_keyboard/archive/refs/heads/main.zip)
-   [tchaikovsky_seasons](https://github.com/DCMLab/tchaikovsky_seasons/archive/refs/heads/main.zip)
-   [wagner_overtures](https://github.com/DCMLab/wagner_overtures/archive/refs/heads/main.zip)
-   [wf_bach_sonatas](https://github.com/DCMLab/wf_bach_sonatas/archive/refs/heads/main.zip)

## Data Formats

Each piece in this corpus is represented by four files with identical
names, each in its own folder. For example, the *Prélude* of J.S. Bach's
first English Suite, BWV 806, has the following files:

-   `bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx`: Uncompressed
    MuseScore file including the music and annotation labels.
-   `bach_en_fr_suites/notes/BWV806_01_Prelude.tsv`: A table of all note
    heads contained in the score and their relevant features (not each
    of them represents an onset, some are tied together)
-   `bach_en_fr_suites/measures/BWV806_01_Prelude.tsv`: A table with
    relevant information about the measures in the score.
-   `bach_en_fr_suites/harmonies/BWV806_01_Prelude.tsv`: A list of the
    included harmony labels (including cadences and phrases) with their
    positions in the score.

### Opening Scores

After navigating to your local copy, you can open the scores in the
folder `MS3` with the free and open source score editor
[MuseScore](https://musescore.org). Please note that the scores have
been edited, annotated and tested with [MuseScore
3.6.2](https://github.com/musescore/MuseScore/releases/tag/v3.6.2).
MuseScore 4 has since been released and preliminary tests suggest that
it renders them correctly.

### Opening TSV files in a spreadsheet

Tab-separated value (TSV) files are like Comma-separated value (CSV)
files and can be opened with most modern text editors. However, for
correctly displaying the columns, you might want to use a spreadsheet or
an addon for your favourite text editor. When you use a spreadsheet such
as Excel, it might annoy you by interpreting fractions as dates. This
can be circumvented by using `Data --> From Text/CSV` or the free
alternative [LibreOffice
Calc](https://www.libreoffice.org/download/download/). Other than that,
TSV data can be loaded with every modern programming language.

### Loading TSV files in Python

Since the TSV files contain null values, lists, fractions, and numbers
that are to be treated as strings, you may want to use this code to load
any TSV files related to this repository (provided you're doing it in
Python). After a quick `pip install -U ms3` (requires Python 3.10)
you'll be able to load any TSV like this:

``` python
import ms3

labels = ms3.load_tsv('bach_en_fr_suites/harmonies/BWV806_01_Prelude.tsv')
notes = ms3.load_tsv('bach_en_fr_suites/notes/BWV806_01_Prelude.tsv')
```

## How to read `metadata.tsv`

This section explains the meaning of the columns contained in
`metadata.tsv`.

### File information

| column                 | content                                                    |
|------------------------|------------------------------------------------------------|
| **fname**              | name without extension (for referencing related files)     |
| **rel_path**           | relative file path of the score, including extension       |
| **subdirectory**       | folder where the score is located                          |    
| **last_mn**            | last measure number                                        |
| **last_mn_unfolded**   | number of measures when playing all repeats                |
| **length_qb**          | length of the piece, measured in quarter notes             |
| **length_qb_unfolded** | length of the piece when playing all repeats               |
| **volta_mcs**          | measure counts of first and second endings                 |
| **all_notes_qb**       | summed up duration of all notes, measured in quarter notes |
| **n_onsets**           | number of note onsets                                      |
| **n_onset_positions**  | number of unique note onsets ("slices")                    |


### Composition information

| column             | content                   |
|--------------------|---------------------------|
| **composer**       | composer name             |
| **workTitle**      | work title                |
| **composed_start** | earliest composition date |
| **composed_end**   | latest composition date   |
| **workNumber**     | Catalogue number(s)       |
| **movementNumber** | 1, 2, or 3                |
| **movementTitle**  | title of the movement     |

### Score information

| column          | content                                                |
|-----------------|--------------------------------------------------------|
| **label_count** | number of chord labels                                 |
| **KeySig**      | key signature(s) (negative = flats, positive = sharps) |
| **TimeSig**     | time signature(s)                                      |
| **musescore**   | MuseScore version                                      |
| **source**      | URL to the first typesetter's file                     |
| **typesetter**  | first typesetter                                       |
| **annotators**  | creator(s) of the chord labels                         |
| **reviewers**   | reviewer(s) of the chord labels                        |

### Identifiers

These columns provide a mapping between multiple identifiers for the sonatas (not for individual movements).

| column          | content                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------|
| **wikidata**    | URL of the [WikiData](https://www.wikidata.org/) item                                                   |
| **viaf**        | URL of the Virtual International Authority File ([VIAF](http://viaf.org/)) entry                        |
| **musicbrainz** | [MusicBrainz](https://musicbrainz.org/) identifier                                                      |
| **imslp**       | URL to the wiki page within the International Music Score Library Project ([IMSLP](https://imslp.org/)) |

## Generating all TSV files from the scores

When you have made changes to the scores and want to update the TSV
files accordingly, you can use the following command (provided you have
pip-installed [ms3](https://github.com/johentsch/ms3)):

``` python
ms3 extract -M -N -X -F -D # for measures, notes, expanded harmony labels, form labels, and metadata
```

If, in addition, you want to generate the reviewed scores with
out-of-label notes colored in red, you can do

``` python
ms3 review -M -N -X -F -D # for extracting measures, notes, expanded harmony labels, form labels, and metadata
```

By adding the flag `-c` to the review command, it will additionally
compare the (potentially modified) annotations in the score with the
ones currently present in the harmonies TSV files and reflect the
comparison in the reviewed scores.

## Questions, Suggestions, Corrections, Bug Reports

For questions, remarks etc., please [create an
issue](https://github.com/DCMLab/distant_listening_corpus/issues) and
feel free to fork and submit pull requests.

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

![cc-by-nc-sa-image](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

# Overview

## ABC

| file_name  |measures|labels|standard|
|------------|-------:|-----:|--------|
|n01op18-1_01|     313|   405|1.0.0   |
|n01op18-1_02|     110|   263|1.0.0   |
|n01op18-1_03|     145|   203|1.0.0   |
|n01op18-1_04|     381|   598|1.0.0   |
|n02op18-2_01|     249|   486|1.0.0   |
|n02op18-2_02|      86|   177|1.0.0   |
|n02op18-2_03|      87|   138|1.0.0   |
|n02op18-2_04|     412|   468|1.0.0   |
|n03op18-3_01|     269|   383|1.0.0   |
|n03op18-3_02|     151|   394|1.0.0   |
|n03op18-3_03|     168|   278|1.0.0   |
|n03op18-3_04|     364|   569|1.0.0   |
|n04op18-4_01|     219|   554|1.0.0   |
|n04op18-4_02|     261|   369|1.0.0   |
|n04op18-4_03|      98|   145|1.0.0   |
|n04op18-4_04|     217|   386|1.0.0   |
|n05op18-5_01|     225|   430|1.0.0   |
|n05op18-5_02|     105|   168|1.0.0   |
|n05op18-5_03|     139|   247|1.0.0   |
|n05op18-5_04|     300|   567|1.0.0   |
|n06op18-6_01|     264|   374|1.0.0   |
|n06op18-6_02|      79|   265|1.0.0   |
|n06op18-6_03|      68|   168|1.0.0   |
|n06op18-6_04|     296|   465|1.0.0   |
|n07op59-1_01|     400|   482|1.0.0   |
|n07op59-1_02|     476|   635|1.0.0   |
|n07op59-1_03|     132|   374|1.0.0   |
|n07op59-1_04|     327|   605|1.0.0   |
|n08op59-2_01|     255|   445|1.0.0   |
|n08op59-2_02|     157|   326|1.0.0   |
|n08op59-2_03|     134|   262|1.0.0   |
|n08op59-2_04|     409|   567|1.0.0   |
|n09op59-3_01|     269|   515|1.0.0   |
|n09op59-3_02|     207|   481|1.0.0   |
|n09op59-3_03|      96|   177|1.0.0   |
|n09op59-3_04|     428|   699|1.0.0   |
|n10op74_01  |     262|   446|1.0.0   |
|n10op74_02  |     169|   304|1.0.0   |
|n10op74_03  |     467|   447|1.0.0   |
|n10op74_04  |     195|   322|1.0.0   |
|n11op95_01  |     151|   245|1.0.0   |
|n11op95_02  |     192|   353|1.0.0   |
|n11op95_03  |     207|   364|1.0.0   |
|n11op95_04  |     175|   326|1.0.0   |
|n12op127_01 |     282|   558|1.0.0   |
|n12op127_02 |     126|   542|1.0.0   |
|n12op127_03 |     289|   428|1.0.0   |
|n12op127_04 |     299|   689|1.0.0   |
|n13op130_01 |     236|   723|1.0.0   |
|n13op130_02 |     107|   181|1.0.0   |
|n13op130_03 |      89|   450|1.0.0   |
|n13op130_04 |     150|   295|1.0.0   |
|n13op130_05 |      66|   189|1.0.0   |
|n13op130_06 |     493|   626|1.0.0   |
|n14op131_01 |     120|   334|1.0.0   |
|n14op131_02 |     197|   354|1.0.0   |
|n14op131_03 |      10|    30|1.0.0   |
|n14op131_04 |     276|   659|1.0.0   |
|n14op131_05 |     499|   599|1.0.0   |
|n14op131_06 |      27|    68|1.0.0   |
|n14op131_07 |     387|   522|1.0.0   |
|n15op132_01 |     264|   622|1.0.0   |
|n15op132_02 |     238|   479|1.0.0   |
|n15op132_03 |     211|   506|1.0.0   |
|n15op132_04 |      46|   113|1.0.0   |
|n15op132_05 |     404|   732|1.0.0   |
|n16op135_01 |     193|   398|1.0.0   |
|n16op135_02 |     272|   376|1.0.0   |
|n16op135_03 |      54|   178|1.0.0   |
|n16op135_04 |     282|   562|1.0.0   |


## bach_en_fr_suites

|             file_name              |measures|labels|standard|
|------------------------------------|-------:|-----:|--------|
|BWV806_01_Prelude                   |      37|   191|2.3.0   |
|BWV806_02_Allemande                 |      32|   145|2.3.0   |
|BWV806_03_Courante_I                |      20|    91|2.3.0   |
|BWV806_04_Courante_II               |      24|   104|2.3.0   |
|BWV806_05_Double_I                  |      24|   101|2.3.0   |
|BWV806_06_Double_II                 |      24|   100|2.3.0   |
|BWV806_07_Sarabande                 |      32|    72|2.3.0   |
|BWV806_08_Bouree_I                  |      48|   146|2.3.0   |
|BWV806_09_Bouree_II                 |      36|   126|2.3.0   |
|BWV806_10_Gigue                     |      40|   122|2.3.0   |
|BWV807_01_Prelude                   |     164|   564|2.3.0   |
|BWV807_02_Allemande                 |      24|   125|2.3.0   |
|BWV807_03_Courante                  |      24|   110|2.3.0   |
|BWV807_04_Sarabande                 |      28|    77|2.3.0   |
|BWV807_04a_Agrements_de_la_Sarabande|      28|    79|2.3.0   |
|BWV807_05_Bourree_I                 |      56|   165|2.3.0   |
|BWV807_06_Bourree_II                |      24|    70|2.3.0   |
|BWV807_07_Gigue                     |      74|   152|2.3.0   |
|BWV808_01_Prelude                   |     213|   358|2.3.0   |
|BWV808_02_Allemande                 |      24|   121|2.3.0   |
|BWV808_03_Courante                  |      32|   153|2.3.0   |
|BWV808_04_Sarabande                 |      24|    44|2.3.0   |
|BWV808_04a_Agrements_de_la_Sarabande|      24|    51|2.3.0   |
|BWV808_05_Gavotte_I                 |      34|   108|2.3.0   |
|BWV808_06_Gavotte_II                |      16|    57|2.3.0   |
|BWV808_07_Gigue                     |      44|   208|2.3.0   |
|BWV809_01_Prelude                   |     108|   493|2.3.0   |
|BWV809_02_Allemande                 |      24|    94|2.3.0   |
|BWV809_03_Courante                  |      20|    67|2.3.0   |
|BWV809_04_Sarabande                 |      24|    61|2.3.0   |
|BWV809_05_Menuett_I                 |      32|    82|2.3.0   |
|BWV809_06_Menuett_II                |      32|    77|2.3.0   |
|BWV809_07_Gigue                     |      52|   195|2.3.0   |
|BWV810_01_Prelude                   |     156|   415|2.3.0   |
|BWV810_02_Allemande                 |      24|   130|2.3.0   |
|BWV810_03_Courante                  |      28|    84|2.3.0   |
|BWV810_04_Sarabande                 |      24|   101|2.3.0   |
|BWV810_05_Passepied_I               |      80|   218|2.3.0   |
|BWV810_06_Passepied_II              |      24|    65|2.3.0   |
|BWV810_07_Gigue                     |      96|   200|2.3.0   |
|BWV811_01_Prelude                   |     195|   610|2.3.0   |
|BWV811_02_Allemande                 |      24|   111|2.3.0   |
|BWV811_03_Courante                  |      32|   132|2.3.0   |
|BWV811_04_Sarabande                 |      24|    60|2.3.0   |
|BWV811_05_Double                    |      24|    64|2.3.0   |
|BWV811_06_Gavotte_I                 |      32|   102|2.3.0   |
|BWV811_07_Gavotte_II                |      24|    77|2.3.0   |
|BWV811_08_Gigue                     |      56|   241|2.3.0   |
|BWV812_01_Allemande                 |      24|   133|2.3.0   |
|BWV812_02_Courante                  |      24|   101|2.3.0   |
|BWV812_03_Sarabande                 |      24|    79|2.3.0   |
|BWV812_04_Menuett_I                 |      24|    57|2.3.0   |
|BWV812_05_Menuett_II                |      40|    66|2.3.0   |
|BWV812_06_Gigue                     |      28|   125|2.3.0   |
|BWV813_01_Allemande                 |      18|   123|2.3.0   |
|BWV813_02_Courante                  |      57|   168|2.3.0   |
|BWV813_03_Sarabande                 |      24|   102|2.3.0   |
|BWV813_04_Air                       |      16|   105|2.3.0   |
|BWV813_05_Menuett                   |      32|    74|2.3.0   |
|BWV813_06_Gigue                     |      84|   141|2.3.0   |
|BWV814_01_Allemande                 |      24|   163|2.3.0   |
|BWV814_02_Courante                  |      28|   109|2.3.0   |
|BWV814_03_Sarabande                 |      24|    85|2.3.0   |
|BWV814_04_Gavotte                   |      32|   100|2.3.0   |
|BWV814_05_Menuett                   |      36|    94|2.3.0   |
|BWV814_06_Trio                      |      24|    63|2.3.0   |
|BWV814_07_Gigue                     |      68|   155|2.3.0   |
|BWV815_01_Allemande                 |      20|   104|2.3.0   |
|BWV815_02_Courante                  |      36|    89|2.3.0   |
|BWV815_03_Sarabande                 |      24|    63|2.3.0   |
|BWV815_04_Gavotte                   |      22|    85|2.3.0   |
|BWV815_05_Air                       |      22|    80|2.3.0   |
|BWV815_06_Menuett                   |      16|    45|2.3.0   |
|BWV815_07_Gigue                     |      60|   106|2.3.0   |
|BWV816_01_Allemande                 |      24|   142|2.3.0   |
|BWV816_02_Courante                  |      32|    83|2.3.0   |
|BWV816_03_Sarabande                 |      40|   106|2.3.0   |
|BWV816_04_Gavotte                   |      24|    68|2.3.0   |
|BWV816_05_Bourree                   |      30|    77|2.3.0   |
|BWV816_06_Loure                     |      16|    66|2.3.0   |
|BWV816_07_Gigue                     |      56|   162|2.3.0   |
|BWV817_01_Allemande                 |      28|   103|2.3.0   |
|BWV817_02_Courante                  |      32|    94|2.3.0   |
|BWV817_03_Sarabande                 |      24|    65|2.3.0   |
|BWV817_04_Gavotte                   |      20|    58|2.3.0   |
|BWV817_05_Polonaise                 |      24|    67|2.3.0   |
|BWV817_06_Bourree                   |      42|   122|2.3.0   |
|BWV817_07_Gigue                     |      48|   116|2.3.0   |
|BWV817_08_Menuett                   |      24|    49|2.3.0   |


## bach_solo

|        file_name         |measures|labels|standard|
|--------------------------|-------:|-----:|--------|
|BWV1001_01_Adagio         |      22|    95|2.3.0   |
|BWV1001_02_Fuga           |      94|   324|2.3.0   |
|BWV1001_03_Siciliano      |      20|   113|2.3.0   |
|BWV1001_04_Presto         |     136|   213|2.3.0   |
|BWV1002_01_Allemanda      |      24|    97|2.3.0   |
|BWV1002_02_Double         |      24|    87|2.3.0   |
|BWV1002_03_Corrente       |      80|   109|2.3.0   |
|BWV1002_04_Double         |      80|   121|2.3.0   |
|BWV1002_05_Sarabande      |      32|    68|2.3.0   |
|BWV1002_06_Double         |      32|    56|2.3.0   |
|BWV1002_07_TempoDiBorea   |      68|   101|2.3.0   |
|BWV1002_08_Double         |      68|   104|2.3.0   |
|BWV1003_01_Grave          |      23|    91|2.3.0   |
|BWV1003_02_Fuga           |     289|   479|2.3.0   |
|BWV1003_03_Andante        |      26|    79|2.3.0   |
|BWV1003_04_Allegro        |      58|   206|2.3.0   |
|BWV1004_01_Allemande      |      32|    92|2.3.0   |
|BWV1004_02_Courante       |      54|    73|2.3.0   |
|BWV1005_02_Fuga           |     354|   748|2.3.0   |
|BWV1006_04_Menuett        |      66|   124|2.3.0   |
|BWV1006_05_Bourée         |      36|    57|2.3.0   |
|BWV1006_06_Gigue          |      32|    52|2.3.0   |
|BWV1007_01_Prelude        |      42|    54|2.3.0   |
|BWV1007_02_Allemande      |      32|    75|2.3.0   |
|BWV1007_03_Courante       |      42|    66|2.3.0   |
|BWV1007_04_Sarabande      |      16|    43|2.3.0   |
|BWV1007_05_MenuetI        |      24|    35|2.3.0   |
|BWV1007_06_MenuetII       |      24|    33|2.3.0   |
|BWV1007_07_Gique          |      34|    59|2.3.0   |
|BWV1008_01_Prelude        |      63|    91|2.3.0   |
|BWV1008_02_Allemande      |      24|    70|2.3.0   |
|BWV1008_03_Courante       |      32|    50|2.3.0   |
|BWV1008_04_Sarabande      |      28|    52|2.3.0   |
|BWV1008_05_MenuetI        |      24|    44|2.3.0   |
|BWV1008_06_MenuetII       |      24|    31|2.3.0   |
|BWV1008_07_Gique          |      76|    91|2.3.0   |
|BWV1009_01_Prelude        |      88|   113|2.3.0   |
|BWV1009_02_Allemande      |      24|   106|2.3.0   |
|BWV1009_03_Courante       |      84|    83|2.3.0   |
|BWV1009_04_Sarabande      |      24|    55|2.3.0   |
|BWV1009_05_BourréeI       |      28|    64|2.3.0   |
|BWV1009_06_BourréeII      |      24|    36|2.3.0   |
|BWV1009_07_Gique          |     108|   110|2.3.0   |
|BWV1010_01_Prelude        |      91|    75|2.3.0   |
|BWV1010_02_Allemande      |      40|    97|2.3.0   |
|BWV1010_03_Courante       |      64|   106|2.3.0   |
|BWV1010_04_Sarabande      |      32|    65|2.3.0   |
|BWV1010_05_BourreeI       |      48|    78|2.3.0   |
|BWV1010_06_BourreeII      |      12|    28|2.3.0   |
|BWV1010_07_Gique          |      42|    80|2.3.0   |
|BWV1011_01_Prelude        |     223|   327|2.3.0   |
|BWV1011_02_Allemande      |      36|    70|2.3.0   |
|BWV1011_03_Courante       |      24|    68|2.3.0   |
|BWV1011_04_Sarabande      |      20|    27|2.3.0   |
|BWV1011_05_GavotteI       |      36|    80|2.3.0   |
|BWV1011_06_GavotteII      |      22|    65|2.3.0   |
|BWV1011_07_Gique          |      72|    73|2.3.0   |
|BWV1012_01_Prelude        |     104|   189|2.3.0   |
|BWV1012_02_Allemande      |      20|    80|2.3.0   |
|BWV1012_03_Courante       |      72|    90|2.3.0   |
|BWV1012_04_Sarabande      |      32|    61|2.3.0   |
|BWV1012_05_GavotteI       |      28|    58|2.3.0   |
|BWV1012_06_GavotteII      |      24|    64|2.3.0   |
|BWV1012_07_Gique          |      68|   112|2.3.0   |
|BWV1013_01_Allemande      |      46|   163|2.3.0   |
|BWV1013_02_Corrente       |      62|   120|2.3.0   |
|BWV1013_03_Sarabande      |      46|    57|2.3.0   |
|BWV1013_04_BourreeAnglaise|      70|    98|2.3.0   |


## bartok_bagatelles

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op06n01  |      18|    25|2.3.0   |
|op06n02  |      30|    57|2.3.0   |
|op06n03  |      24|    32|2.3.0   |
|op06n04  |      12|    42|2.3.0   |
|op06n05  |      90|    28|2.3.0   |
|op06n06  |      25|    53|2.3.0   |
|op06n07  |     118|   110|2.3.0   |
|op06n08  |      32|    70|2.3.0   |
|op06n09  |      70|    88|2.3.0   |
|op06n10  |     102|   224|2.3.0   |
|op06n11  |      87|   100|2.3.0   |
|op06n12  |      44|    77|2.3.0   |
|op06n13  |      26|    42|2.3.0   |
|op06n14  |     218|   199|2.3.0   |


## beethoven_piano_sonatas

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|01-1     |     152|   241|2.3.0   |
|01-2     |      61|   200|2.3.0   |
|01-3     |      73|   132|2.3.0   |
|01-4     |     196|   355|2.3.0   |
|02-1     |     336|   479|2.3.0   |
|02-2     |      80|   244|2.3.0   |
|02-3     |      68|   124|2.3.0   |
|02-4     |     187|   339|2.3.0   |
|03-1     |     257|   487|2.3.0   |
|03-2     |      82|   233|2.3.0   |
|03-3     |     127|   198|2.3.0   |
|03-4     |     312|   793|2.3.0   |
|04-1     |     362|     0|        |
|04-2     |      90|     0|        |
|04-3     |     150|     0|        |
|04-4     |     186|     0|        |
|05-1     |     284|   310|2.3.0   |
|05-2     |     112|   252|2.3.0   |
|05-3     |     122|   313|2.3.0   |
|06-1     |     202|   338|2.3.0   |
|06-2     |     170|   236|2.3.0   |
|06-3     |     150|   308|2.3.0   |
|07-1     |     344|   527|2.3.0   |
|07-2     |      87|   218|2.3.0   |
|07-3     |      86|    92|2.3.0   |
|07-4     |     113|   266|2.3.0   |
|08-1     |     310|   503|2.3.0   |
|08-2     |      73|   143|2.3.0   |
|08-3     |     210|   365|2.3.0   |
|09-1     |     161|   351|2.3.0   |
|09-2     |     178|   235|2.3.0   |
|09-3     |     131|   262|2.3.0   |
|10-1     |     200|   355|2.3.0   |
|10-2     |      90|   330|2.3.0   |
|10-3     |     254|   318|2.3.0   |
|11-1     |     199|     0|        |
|11-2     |      77|     0|        |
|11-3     |      46|     0|        |
|11-4     |     199|     0|        |
|12-1     |     219|     0|        |
|12-2     |      95|     0|        |
|12-3     |      75|     0|        |
|12-4     |     170|     0|        |
|13-1     |      86|     0|        |
|13-2     |     140|     0|        |
|13-3     |      26|     0|        |
|13-4     |     285|     0|        |
|14-1     |      69|     0|        |
|14-2     |      60|     0|        |
|14-3     |     201|     0|        |
|15-1     |     462|     0|        |
|15-2     |     103|     0|        |
|15-3     |      94|     0|        |
|15-4     |     210|     0|        |
|16-1     |     325|   303|2.3.0   |
|16-2     |     119|   285|2.3.0   |
|16-3     |     275|   703|2.3.0   |
|17-1     |     228|   352|2.3.0   |
|17-2     |     103|   223|2.3.0   |
|17-3     |     399|   460|2.3.0   |
|18-1     |     253|   269|2.3.0   |
|18-2     |     169|   273|2.3.0   |
|18-3     |      61|   178|2.3.0   |
|18-4     |     333|   410|2.3.0   |
|19-1     |     110|   193|2.3.0   |
|19-2     |     164|   384|2.3.0   |
|20-1     |     122|   286|2.3.0   |
|20-2     |     120|   169|2.3.0   |
|21-1     |     302|   616|2.3.0   |
|21-2     |      28|    82|2.3.0   |
|21-3     |     543|   739|2.3.0   |
|23-1     |     262|   434|2.3.0   |
|23-2     |      97|   220|2.3.0   |
|23-3     |     361|   395|2.3.0   |
|24-1     |     105|   286|2.3.0   |
|24-2     |     183|   317|2.3.0   |
|26-1     |     255|   537|2.3.0   |
|26-2     |      42|   127|2.3.0   |
|26-3     |     196|   317|2.3.0   |
|29-1     |     405|     0|        |
|29-2     |     175|     0|        |
|29-3     |     187|     0|        |
|29-4     |     400|     0|        |
|30-1     |      99|   252|2.3.0   |
|30-2     |     177|   320|2.3.0   |
|30-3     |     203|   656|2.3.0   |
|31-1     |     116|   339|2.3.0   |
|31-2     |     158|   201|2.3.0   |
|31-3     |     212|   644|2.3.0   |
|32-1     |     157|   576|2.3.0   |
|32-2     |     177|   869|2.3.0   |


## c_schumann_lieder

|               file_name               |measures|labels|standard|
|---------------------------------------|-------:|-----:|--------|
|op13no1 Ich stand in dunklen Traumen   |      37|   103|2.3.0   |
|op13no2 Sie liebten sich beide         |      34|   108|2.3.0   |
|op13no3 Liebeszauber                   |      54|   155|2.3.0   |
|op13no4 Der Mond kommt still gegangen  |      33|   120|2.3.0   |
|op13no5 Ich hab in deinem Auge         |      33|   109|2.3.0   |
|op13no6 Die stille Lotosblume          |      47|   118|2.3.0   |
|op23no1 Was weinst du Blumlein         |      68|   139|2.3.0   |
|op23no2 An einem lichten Morgen        |      38|    94|2.3.0   |
|op23no3 Geheimes Flustern hier und dort|      55|    74|2.3.0   |
|op23no4 Auf einem grunen Hugel         |      30|    94|2.3.0   |
|op23no5 Das ist ein Tag der klingen mag|      45|   122|2.3.0   |
|op23no6 O Lust o Lust                  |      40|    90|2.3.0   |


## chopin_mazurkas

|  file_name  |measures|labels|standard|
|-------------|-------:|-----:|--------|
|BI105-2op30-2|      64|   116|2.3.0   |
|BI105-3op30-3|      95|   159|2.3.0   |
|BI105-4op30-4|     139|   228|2.3.0   |
|BI115-1op33-1|      48|    90|2.3.0   |
|BI115-2op33-2|     135|   202|2.3.0   |
|BI115-3op33-3|      48|   119|2.3.0   |
|BI115-4op33-4|     224|   374|2.3.0   |
|BI122op41-2  |      68|   143|2.3.0   |
|BI126-1op41-4|      74|   151|2.3.0   |
|BI126-3op41-1|     139|   233|2.3.0   |
|BI126-4op41-3|      78|   120|2.3.0   |
|BI134        |     224|   312|2.3.0   |
|BI140        |     247|   213|2.3.0   |
|BI145-1op50-1|     104|   216|2.3.0   |
|BI145-2op50-2|     103|   152|2.3.0   |
|BI145-3op50-3|     192|   309|2.3.0   |
|BI153-1op56-1|     204|   444|2.3.0   |
|BI153-2op56-2|      84|   156|2.3.0   |
|BI153-3op56-3|     220|   481|2.3.0   |
|BI157-1op59-1|     130|   257|2.3.0   |
|BI157-2op59-2|     111|   209|2.3.0   |
|BI157-3op59-3|     154|   358|2.3.0   |
|BI16-1       |      32|    50|2.2.0   |
|BI16-2       |      32|    47|2.3.0   |
|BI162-1op63-1|     102|   169|2.3.0   |
|BI162-2op63-2|      56|    80|2.3.0   |
|BI162-3op63-3|      76|   123|2.3.0   |
|BI163op67-4  |      80|   118|2.3.0   |
|BI167op67-2  |      56|    78|2.3.0   |
|BI168op68-4  |      40|    80|2.3.0   |
|BI18op68-2   |      64|   127|2.3.0   |
|BI34op68-3   |      60|   109|2.3.0   |
|BI38op68-1   |      72|   139|2.3.0   |
|BI60-1op06-1 |      72|   204|2.3.0   |
|BI60-2op06-2 |      72|   105|2.3.0   |
|BI60-3op06-3 |      90|   145|2.3.0   |
|BI60-4op06-4 |      24|    67|2.3.0   |
|BI61-1op07-1 |      64|   104|2.3.0   |
|BI61-2op07-2 |      56|   114|2.3.0   |
|BI61-3op07-3 |     105|   205|2.3.0   |
|BI61-4op07-4 |      44|   104|2.3.0   |
|BI61-5op07-5 |      20|    38|2.3.0   |
|BI71         |      68|   122|2.3.0   |
|BI73         |      32|    44|2.3.0   |
|BI77-1op17-1 |      60|   112|2.3.0   |
|BI77-2op17-2 |      68|   171|2.3.0   |
|BI77-3op17-3 |      81|   214|2.3.0   |
|BI77-4op17-4 |     132|   226|2.3.0   |
|BI85         |      57|    91|2.3.0   |
|BI89-1op24-1 |      64|   123|2.3.0   |
|BI89-2op24-2 |     120|   226|2.3.0   |
|BI89-3op24-3 |      43|    65|2.3.0   |
|BI89-4op24-4 |     146|   294|2.3.0   |
|BI93-1op67-1 |      60|    94|2.3.0   |
|BI93-2op67-3 |      56|    97|2.3.0   |


## corelli

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op01n01a |      14|    64|2.3.0   |
|op01n01b |      38|   141|2.3.0   |
|op01n01c |      37|    97|2.3.0   |
|op01n01d |      98|   147|2.3.0   |
|op01n02a |      19|    76|2.3.0   |
|op01n02b |      36|   121|2.3.0   |
|op01n02c |      29|    67|2.3.0   |
|op01n02d |     117|   174|2.3.0   |
|op01n03a |      17|    66|2.3.0   |
|op01n03b |      54|   223|2.3.0   |
|op01n03c |      35|    71|2.3.0   |
|op01n03d |      97|   177|2.3.0   |
|op01n04a |      19|    52|2.3.0   |
|op01n04b |      12|    26|2.3.0   |
|op01n04c |      28|   117|2.3.0   |
|op01n04d |      39|   115|2.3.0   |
|op01n05a |      42|    90|2.3.0   |
|op01n05b |      39|   149|2.3.0   |
|op01n05c |      30|    59|2.3.0   |
|op01n05d |      59|   117|2.3.0   |
|op01n06a |      11|    44|2.3.0   |
|op01n06b |      40|   190|2.3.0   |
|op01n06c |      38|    89|2.3.0   |
|op01n06d |      69|   131|2.3.0   |
|op01n07a |      40|   161|2.3.0   |
|op01n07b |      14|    57|2.3.0   |
|op01n07c |      51|   174|2.3.0   |
|op01n08a |      16|    56|2.3.0   |
|op01n08b |      20|    76|2.3.0   |
|op01n08c |      27|   119|2.3.0   |
|op01n08d |      39|    71|2.3.0   |
|op01n09a |      39|    45|2.3.0   |
|op01n09b |      37|   153|2.3.0   |
|op01n09c |      36|    74|2.3.0   |
|op01n09d |      54|    56|2.3.0   |
|op01n10a |      12|    45|2.3.0   |
|op01n10b |      17|    70|2.3.0   |
|op01n10c |      29|   107|2.3.0   |
|op01n10d |      24|    56|2.3.0   |
|op01n10e |      84|   139|2.3.0   |
|op01n11a |      18|    60|2.3.0   |
|op01n11b |      34|   123|2.3.0   |
|op01n11c |      33|    79|2.3.0   |
|op01n11d |      18|    81|2.3.0   |
|op01n12a |      19|    64|2.3.0   |
|op01n12b |      36|   101|2.3.0   |
|op01n12c |      13|    42|2.3.0   |
|op01n12d |      62|   225|2.3.0   |
|op03n01a |      19|    78|2.3.0   |
|op03n01b |      37|   149|2.3.0   |
|op03n01c |      61|   117|2.3.0   |
|op03n01d |      40|   158|2.3.0   |
|op03n02a |      19|    68|2.3.0   |
|op03n02b |      31|   118|2.3.0   |
|op03n02c |      40|    91|2.3.0   |
|op03n02d |      43|   121|2.3.0   |
|op03n03a |      16|    59|2.3.0   |
|op03n03b |      32|    62|2.3.0   |
|op03n03c |      23|   137|2.3.0   |
|op03n03d |      60|   240|2.3.0   |
|op03n04a |      23|   137|2.3.0   |
|op03n04b |      39|   138|2.3.0   |
|op03n04c |      55|   114|2.3.0   |
|op03n04d |      50|   171|2.3.0   |
|op03n05a |      21|    89|2.3.0   |
|op03n05b |      49|   175|2.3.0   |
|op03n05c |      36|    80|2.3.0   |
|op03n05d |      33|   125|2.3.0   |
|op03n06a |      33|   119|2.3.0   |
|op03n06b |      14|    54|2.3.0   |
|op03n06c |      38|   150|2.3.0   |
|op03n06d |      41|   179|2.3.0   |
|op03n07a |      20|    76|2.3.0   |
|op03n07b |      35|   131|2.3.0   |
|op03n07c |      38|    92|2.3.0   |
|op03n07d |      28|    84|2.3.0   |
|op03n08a |      20|    90|2.3.0   |
|op03n08b |      39|   153|2.3.0   |
|op03n08c |      31|    74|2.3.0   |
|op03n08d |      40|   135|2.3.0   |
|op03n09a |      30|    69|2.3.0   |
|op03n09b |      28|   103|2.3.0   |
|op03n09c |      38|    85|2.3.0   |
|op03n09d |      28|   121|2.3.0   |
|op03n10a |      14|    49|2.3.0   |
|op03n10b |      38|   154|2.3.0   |
|op03n10c |      11|    25|2.3.0   |
|op03n10d |      31|   114|2.3.0   |
|op03n11a |      17|    68|2.3.0   |
|op03n11b |      39|   164|2.3.0   |
|op03n11c |      29|    63|2.3.0   |
|op03n11d |      45|    97|2.3.0   |
|op03n12a |      19|    17|2.3.0   |
|op03n12b |      41|     8|2.3.0   |
|op03n12c |       9|    39|2.3.0   |
|op03n12d |      29|    97|2.3.0   |
|op03n12e |      25|    76|2.3.0   |
|op03n12f |      37|   192|2.3.0   |
|op03n12g |      46|   205|2.3.0   |
|op04n01a |      17|    74|2.3.0   |
|op04n01b |      47|    75|2.3.0   |
|op04n01c |      13|    47|2.3.0   |
|op04n01d |      34|   136|2.3.0   |
|op04n02a |      20|    87|2.3.0   |
|op04n02b |      22|   111|2.3.0   |
|op04n02c |       5|     9|2.3.0   |
|op04n02d |      57|   125|2.3.0   |
|op04n03a |      18|    90|2.3.0   |
|op04n03b |      48|    87|2.3.0   |
|op04n03c |      16|    37|2.3.0   |
|op04n03d |      41|   136|2.3.0   |
|op04n04a |      20|    68|2.3.0   |
|op04n04b |      41|    80|2.3.0   |
|op04n04c |      17|   102|2.3.0   |
|op04n04d |      31|   107|2.3.0   |
|op04n05a |      20|   101|2.3.0   |
|op04n05b |      28|   105|2.3.0   |
|op04n05c |      39|    78|2.3.0   |
|op04n05d |      12|    38|2.3.0   |
|op04n06a |       6|    22|2.3.0   |
|op04n06b |      23|    41|2.3.0   |
|op04n06c |       7|    19|2.3.0   |
|op04n06d |      28|    57|2.3.0   |
|op04n06e |      10|    22|2.3.0   |
|op04n06f |      25|    76|2.3.0   |
|op04n06g |      30|    94|2.3.0   |
|op04n07a |      15|    86|2.3.0   |
|op04n07b |      46|   104|2.3.0   |
|op04n07c |       6|    12|2.3.0   |
|op04n07d |      32|    47|2.3.0   |
|op04n07e |      27|    92|2.3.0   |
|op04n08a |      38|    94|2.3.0   |
|op04n08b |      23|    88|2.3.0   |
|op04n08c |      16|    41|2.3.0   |
|op04n09a |      13|    77|2.3.0   |
|op04n09b |      44|   103|2.3.0   |
|op04n09c |      12|    49|2.3.0   |
|op04n09d |      56|   167|2.3.0   |
|op04n10a |       2|     4|2.3.0   |
|op04n10b |      33|   104|2.3.0   |
|op04n10c |       4|     8|2.3.0   |
|op04n10d |      14|    51|2.3.0   |
|op04n10e |      48|   152|2.3.0   |
|op04n11a |      24|   156|2.3.0   |
|op04n11b |      73|   116|2.3.0   |
|op04n11c |      36|   142|2.3.0   |
|op04n12a |      35|    77|2.3.0   |
|op04n12b |      39|   111|2.3.0   |
|op04n12c |      19|    62|2.3.0   |


## couperin_clavecin

|     file_name      |measures|labels|standard|
|--------------------|-------:|-----:|--------|
|00_allemande        |      13|    66|2.3.0   |
|01_premier_prelude  |      20|    40|2.3.0   |
|02_second_prelude   |      18|    48|2.3.0   |
|03_troisieme_prelude|      18|    80|2.3.0   |
|04_quatrieme_prelude|      23|    70|2.3.0   |
|05_cinquieme_prelude|      24|    96|2.3.0   |
|06_sixieme_prelude  |      59|   108|2.3.0   |
|07_septieme_prelude |      24|    87|2.3.0   |
|08_huitieme_prelude |      31|   122|2.3.0   |


## couperin_concerts

|         file_name          |measures|labels|standard|
|----------------------------|-------:|-----:|--------|
|c01n01_prelude              |      23|    94|2.3.0   |
|c01n02_allemande            |      18|    78|2.3.0   |
|c01n03_sarabande            |      28|    68|2.3.0   |
|c01n04_gavotte              |      14|    54|2.3.0   |
|c01n05_gigue                |      30|   139|2.3.0   |
|c01n06_menuet_en_trio       |      24|    47|2.3.0   |
|c02n01_prelude              |      37|    88|2.3.0   |
|c02n02_allemande_fuguee     |      24|   121|2.3.0   |
|c02n03_air_tendre           |      40|    86|2.3.0   |
|c02n04_air_contrefugue      |      62|   154|2.3.0   |
|c02n05_echos                |      85|   148|2.3.0   |
|c03n01_prelude              |      18|    83|2.3.0   |
|c03n02_allemande            |      17|   111|2.3.0   |
|c03n03_courante             |      25|   105|2.3.0   |
|c03n04_sarabande_grave      |      32|    72|2.3.0   |
|c03n05_gavotte              |      25|    85|2.3.0   |
|c03n06_musette_1            |      28|    28|2.3.0   |
|c03n07_musette_2            |      27|    34|2.3.0   |
|c03n08_chaconne_legere      |     128|   287|2.3.0   |
|c04n01_prelude              |      14|    86|2.3.0   |
|c04n02_allemande            |      14|    77|2.3.0   |
|c04n03_courante_francoise   |      21|    85|2.3.0   |
|c04n04_courante_a_litalienne|      73|   145|2.3.0   |
|c04n05_sarabande            |      24|    48|2.3.0   |
|c04n06_rigaudon             |      41|    62|2.3.0   |
|c04n07_forlane              |      55|   149|2.3.0   |
|c05n01_prelude              |      52|    99|2.3.0   |
|c05n02_allemande            |      43|   154|2.3.0   |
|c05n03_sarabande            |      24|    54|2.3.0   |
|c05n04_gavote               |      32|   104|2.3.0   |
|c05n05_musete               |      54|   118|2.3.0   |
|c06n01_grave                |      24|   111|2.3.0   |
|c06n02_allemande            |      31|   130|2.3.0   |
|c06n03_sarabande            |      44|   115|2.3.0   |
|c06n04_air_diable           |      44|   105|2.3.0   |
|c06n05_siciliene            |      21|   129|2.3.0   |
|c07n01_grave                |      14|    85|2.3.0   |
|c07n02_allemande            |      28|   139|2.3.0   |
|c07n03_sarabande            |      33|    74|2.3.0   |
|c07n04_fuguete              |      50|   142|2.3.0   |
|c07n05_gavote               |      28|    57|2.3.0   |
|c07n06_siciliene            |      18|   105|2.3.0   |
|c08n01_ouverture            |      89|   155|2.3.0   |
|c08n02_ritournele           |      61|   126|2.3.0   |
|c08n03_air                  |      31|    68|2.3.0   |
|c08n04_air_tendre           |      24|    54|2.3.0   |
|c08n05_air_leger            |      38|    75|2.3.0   |
|c08n06_Loure                |      32|   113|2.3.0   |
|c08n07_air                  |      28|    74|2.3.0   |
|c08n08_sarabande            |      24|    64|2.3.0   |
|c08n09_air_leger            |      29|    49|2.3.0   |
|c08n10_air_lentement        |      46|   102|2.3.0   |
|c08n11_air_baccantes        |      18|    59|2.3.0   |
|c09n01_charme               |      20|   129|2.3.0   |
|c09n02_lenjouement          |      34|   184|2.3.0   |
|c09n03_graces               |      22|    93|2.3.0   |
|c09n04_Lejene               |      52|   113|2.3.0   |
|c09n05_vivacite             |      35|   173|2.3.0   |
|c09n06_Sarabande            |      24|    50|2.3.0   |
|c09n07_douceur              |      42|   102|2.3.0   |
|c09n08_caetera              |      23|    75|2.3.0   |
|c10n01_gravement            |      14|    74|2.3.0   |
|c10n02_air                  |      32|   124|2.3.0   |
|c10n03_plainte              |      36|    92|2.3.0   |
|c10n04_tromba               |      42|    74|2.3.0   |
|c11n01_majestueusement      |      38|    88|2.3.0   |
|c11n02_allemande            |      22|   124|2.3.0   |
|c11n03_seconde_allemande    |      20|   117|2.3.0   |
|c11n04_courante             |      18|    83|2.3.0   |
|c11n05_seconde_courante     |      21|    84|2.3.0   |
|c11n06_sarabande            |      36|    70|2.3.0   |
|c11n07_gigue                |      43|   158|2.3.0   |
|c11n08_Rondeau              |      56|   131|2.3.0   |
|c12n01_pointe               |      41|     0|        |
|c12n02_badinage             |      59|     0|        |
|c12n03_air                  |      58|     0|        |
|c13n01_unisson              |      18|     0|        |
|c13n02_air                  |      24|     0|        |
|c13n03_sarabande            |      29|     0|        |
|c13n04_chaconne             |      93|     0|        |
|c14n01_gravement            |      15|    87|2.3.0   |
|c14n02_allemande            |      23|    99|2.3.0   |
|c14n03_sarabande            |      28|    55|2.3.0   |
|c14n04_fuguete              |      56|   225|2.3.0   |
|parnasse_01                 |      18|    82|2.3.0   |
|parnasse_02                 |      62|   251|2.3.0   |
|parnasse_03                 |      58|   116|2.3.0   |
|parnasse_04                 |      57|   105|2.3.0   |
|parnasse_05                 |      26|   106|2.3.0   |
|parnasse_06                 |      32|    62|2.3.0   |
|parnasse_07                 |      53|   235|2.3.0   |


## cpe_bach_keyboard

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|         |      19|     0|        |
|         |      12|     0|        |
|         |       3|     0|        |
|         |       7|     0|        |
|         |       4|     0|        |
|         |      14|     0|        |
|         |      14|     0|        |
|         |       8|     0|        |
|         |      18|     0|        |
|         |     125|     0|        |
|         |      48|   216|2.3.0   |
|         |      25|    42|2.3.0   |
|         |     166|   244|2.3.0   |
|         |     192|   340|2.3.0   |
|         |      31|    91|2.3.0   |
|         |     133|   215|2.3.0   |
|         |     192|   280|2.3.0   |
|         |      41|    88|2.3.0   |
|         |     100|   165|2.3.0   |
|         |     156|     0|        |
|         |      17|     0|        |
|         |     131|     0|        |
|         |     104|   386|2.3.0   |
|         |      60|   114|2.3.0   |
|         |     229|   390|2.3.0   |
|         |     234|   450|2.3.0   |
|         |      69|     0|        |
|         |      39|     0|        |
|         |      44|     0|        |
|         |      77|     0|        |
|         |      49|     0|        |
|         |     160|     0|        |
|         |      42|     0|        |
|         |      25|     0|        |
|         |      68|     0|        |
|         |     128|     0|        |
|         |      32|     0|        |
|         |     135|     0|        |
|         |      29|     0|        |
|         |      30|     0|        |
|         |      37|     0|        |
|         |      66|     0|        |
|         |      30|     0|        |
|         |     122|     0|        |
|         |     176|   435|2.3.0   |
|         |      71|   164|2.3.0   |
|         |      24|    58|2.3.0   |
|         |      48|     0|        |
|         |     149|   425|2.3.0   |
|         |      47|     0|        |
|         |      73|   101|2.3.0   |
|         |     172|     0|        |
|         |      41|     0|        |
|         |      52|     0|        |
|         |      94|     0|        |
|         |      41|     0|        |
|         |      32|     0|        |
|         |      58|     0|        |
|         |     141|     0|        |
|         |      81|     0|        |
|         |      73|     0|        |
|         |      52|     0|        |
|         |     224|     0|        |
|         |      90|     0|        |
|         |      44|     0|        |
|         |      70|     0|        |


## debussy_suite_bergamasque

|       file_name       |measures|labels|standard|
|-----------------------|-------:|-----:|--------|
|l075-01_suite_prelude  |      89|   274|2.3.0   |
|l075-02_suite_menuet   |     104|   305|2.3.0   |
|l075-03_suite_clair    |      72|   150|2.3.0   |
|l075-04_suite_passepied|     156|   284|2.3.0   |


## dvorak_silhouettes

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op08n01  |      52|    80|2.3.0   |
|op08n02  |      15|    67|2.3.0   |
|op08n03  |      72|   238|2.3.0   |
|op08n04  |      59|   136|2.3.0   |
|op08n05  |      80|   139|2.3.0   |
|op08n06  |      60|   113|2.3.0   |
|op08n07  |      38|   167|2.3.0   |
|op08n08  |      57|   100|2.3.0   |
|op08n09  |      61|    97|2.3.0   |
|op08n10  |      58|   104|2.3.0   |
|op08n11  |      44|    88|2.3.0   |
|op08n12  |      78|   210|2.3.0   |


## frescobaldi_fiori_musicali

|                               file_name                               |measures|labels|standard|
|-----------------------------------------------------------------------|-------:|-----:|--------|
|12.01_Toccata_avanti_la_Messa_della_Domenica                           |       8|    57|        |
|12.02_Kyrie_della_domenica                                             |      13|    60|        |
|12.03_Kyrie,_Tema_A                                                    |      17|    66|        |
|12.04_Christe,_Tema_B                                                  |      15|    47|        |
|12.05_Christe,_Tema_B,_alio_modo                                       |       8|    47|        |
|12.06_Christe,_Tema_B,_alio_modo_II                                    |      21|    46|        |
|12.07_Christe,_Tema_B,_alio_modo_III                                   |      14|    35|        |
|12.08_Kyrie,_Tema_C                                                    |      13|    54|        |
|12.09_Kyrie,_Tema_D,_alio_modo_I                                       |      21|    63|        |
|12.10_Kyrie,_Tema_D,_alio_modo_II                                      |      18|    52|        |
|12.11_Kyrie_ultimo                                                     |      19|    65|        |
|12.12_Kyrie,_Tema_D,_alio_modo_III                                     |      12|    84|        |
|12.13_Kyrie,_Tema_D,_alio_modo_IV                                      |      21|    48|        |
|12.14_Canzon_dopo_l’Epistola                                           |      59|   211|        |
|12.15_Recercar_dopo_il_Credo                                           |      47|   162|        |
|12.16_Toccata_cromaticha_per_l’elevatione                              |      53|   199|        |
|12.17_Canzon_post_il_Comune                                            |      80|   213|        |
|12.18_Toccata_avanti_la_Messa_delli_Apostoli                           |      21|    74|        |
|12.19_Kyrie,_Tema_E_1                                                  |      16|    46|        |
|12.20_Kyrie,_Tema_E_2                                                  |      17|    64|        |
|12.21_Kyrie,_Tema_E_3                                                  |      10|    45|        |
|12.22_Christe,_Tema_F_1                                                |      13|    43|        |
|12.23_Christe,_Tema_F_2                                                |      14|    52|        |
|12.24_Kyrie,_Tema_G_1                                                  |      27|    51|        |
|12.25_Kyrie,_Tema_G_2                                                  |      20|    65|        |
|12.26_Kyrie,_Tema_H                                                    |      20|    63|        |
|12.27_Canzon_dopo_l'Epistola                                           |      68|   210|        |
|12.28_Toccata_avanti_il_Recercar                                       |      13|    60|        |
|12.29_Recercar_cromaticho_post_il_Credo                                |      70|   248|        |
|12.30_Alto_recercar                                                    |      81|   319|        |
|12.31_Toccata_per_l'Elevatione                                         |      33|   130|        |
|12.32_Recercar_con_obligo_del_Basso_come_appare                        |      64|   219|        |
|12.33_Canzon_quarti_toni_dopo_il_post_Comune                           |      58|   208|        |
|12.34_Toccata_avanti_la_Messa_della_Madonna                            |      12|    38|        |
|12.35_Kyrie,_Tema_I                                                    |      12|    42|        |
|12.36_Kyrie,_Tema_K                                                    |      13|    46|        |
|12.37_Christe,_Tema_L                                                  |      14|    61|        |
|12.38_Christe,_Tema_M                                                  |      12|    40|        |
|12.39_Kyrie,_Tema_N                                                    |      12|    34|        |
|12.40_Kyrie,_Tema_O                                                    |       9|    53|        |
|12.41_Canzon_dopo_l'Epistola                                           |      49|   126|        |
|12.42_Recercar_dopo_il_Credo                                           |      46|   156|        |
|12.43_Toccata_avanti_il_Recercar                                       |      14|    38|        |
|12.44_Recercar_con_obligo_di_cantare_la_quinta_parte_non_senza_toccarla|      59|   202|        |
|12.45_Toccata_per_l'Elevatione                                         |      24|    85|        |
|12.46_Bergamasca                                                       |     124|   415|        |
|12.47_Capriccio_sopra_la_Girolmeta                                     |     102|   375|        |


## grieg_lyric_pieces

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op12n01  |      23|    43|2.3.0   |
|op12n02  |      79|   125|2.3.0   |
|op12n03  |      52|   110|2.3.0   |
|op12n04  |      72|    97|2.3.0   |
|op12n05  |      40|   109|2.3.0   |
|op12n06  |      56|   126|2.3.0   |
|op12n07  |      56|    74|2.3.0   |
|op12n08  |      32|    78|2.3.0   |
|op38n01  |      86|   141|2.3.0   |
|op38n02  |      41|    46|2.3.0   |
|op38n03  |      48|    87|2.3.0   |
|op38n04  |      36|    66|2.3.0   |
|op38n05  |      41|    70|2.3.0   |
|op38n06  |      47|   104|2.3.0   |
|op38n07  |      53|    55|2.3.0   |
|op38n08  |      84|   130|2.3.0   |
|op43n01  |      42|   102|2.3.0   |
|op43n02  |      30|    98|2.3.0   |
|op43n03  |      35|   112|2.3.0   |
|op43n04  |      36|    52|2.3.0   |
|op43n05  |      36|   110|2.3.0   |
|op43n06  |      72|   127|2.3.0   |
|op47n01  |     184|   158|2.3.0   |
|op47n02  |     126|   183|2.3.0   |
|op47n03  |     106|    93|2.3.0   |
|op47n04  |      38|    21|2.3.0   |
|op47n05  |      41|   109|2.3.0   |
|op47n06  |      74|    83|2.3.0   |
|op47n07  |      97|   134|2.3.0   |
|op54n01  |      61|   110|2.3.0   |
|op54n02  |     159|   286|2.3.0   |
|op54n03  |     194|   267|2.3.0   |
|op54n04  |      63|    91|2.3.0   |
|op54n05  |     204|   118|2.3.0   |
|op54n06  |      90|   171|2.3.0   |
|op57n01  |     146|   313|2.3.0   |
|op57n02  |     125|   183|2.3.0   |
|op57n03  |      67|   186|2.3.0   |
|op57n04  |      92|   116|2.3.0   |
|op57n05  |     169|   202|2.3.0   |
|op57n06  |      95|   156|2.3.0   |
|op62n01  |      90|    72|2.3.0   |
|op62n02  |      81|   163|2.3.0   |
|op62n03  |      65|    95|2.3.0   |
|op62n04  |      81|    97|2.3.0   |
|op62n05  |      62|    45|2.3.0   |
|op62n06  |     150|   173|2.3.0   |
|op65n01  |     173|   203|2.3.0   |
|op65n02  |      26|   128|2.3.0   |
|op65n03  |      58|    87|2.3.0   |
|op65n04  |      71|   112|2.3.0   |
|op65n05  |      48|   128|2.3.0   |
|op65n06  |     179|   222|2.3.0   |
|op68n01  |      56|   156|2.3.0   |
|op68n02  |      88|   186|2.3.0   |
|op68n03  |     114|   134|2.3.0   |
|op68n04  |      90|    85|2.3.0   |
|op68n05  |      43|    95|2.3.0   |
|op68n06  |     202|   200|2.3.0   |
|op71n01  |      95|   180|2.3.0   |
|op71n02  |      54|   107|2.3.0   |
|op71n03  |      79|    72|2.3.0   |
|op71n04  |      77|    87|2.3.0   |
|op71n05  |      98|   155|2.3.0   |
|op71n06  |      32|   133|2.3.0   |
|op71n07  |      74|    74|2.3.0   |


## handel_keyboard

|       file_name        |measures|labels|standard|
|------------------------|-------:|-----:|--------|
|hwv430d_Grobschmied_Aria|       9|    51|2.3.0   |
|hwv430d_Grobschmied_Var1|       8|    56|2.3.0   |
|hwv430d_Grobschmied_Var2|       8|    58|2.3.0   |
|hwv430d_Grobschmied_Var3|       8|    56|2.3.0   |
|hwv430d_Grobschmied_Var4|       8|    68|2.3.0   |
|hwv430d_Grobschmied_Var5|      12|    61|2.3.0   |


## jc_bach_sonatas

|             file_name              |measures|labels|standard|
|------------------------------------|-------:|-----:|--------|
|wa01op05no1a_Allegretto             |      82|   120|2.3.0   |
|wa01op05no1b_Tempo_di_Minuetto      |      74|   149|2.3.0   |
|wa02op05no2a_Allegro_di_molto       |     111|   262|2.3.0   |
|wa02op05no2b_Andante_di_molto       |      50|   118|2.3.0   |
|wa02op05no2c_Minuetto               |      28|    59|2.3.0   |
|wa02op05no2d_Minore                 |      24|    39|2.3.0   |
|wa03op05no3a_Allegro                |      81|   191|2.3.0   |
|wa03op05no3b_Allegretto             |      80|   127|2.3.0   |
|wa04op05no4a_Allegro                |     117|   197|2.3.0   |
|wa04op05no4b_Rondeaux               |      69|   114|2.3.0   |
|wa05op05no5a_Allegro_Assai          |      99|   209|2.3.0   |
|wa05op05no5b_Adagio                 |      55|   130|2.3.0   |
|wa05op05no5c_Prestissimo            |     102|   205|2.3.0   |
|wa06op05no6a_Grave                  |      62|   148|2.3.0   |
|wa06op05no6b_Allegro_Moderato       |      77|   281|2.3.0   |
|wa06op05no6c_Allegretto             |      46|   155|2.3.0   |
|wa07op17no1a_Minuetto_Con_Variatione|      18|   178|2.3.0   |
|wa08op17no2a_Allegro                |     121|   186|2.3.0   |
|wa08op17no2b_Andante                |      71|   144|2.3.0   |
|wa08op17no2c_Prestissimo            |     101|   216|2.3.0   |
|wa09op17no3a_Allegro_Assai          |     114|   268|2.3.0   |
|wa09op17no3b_Allegro                |     111|   186|2.3.0   |
|wa10op17no4a_Allegro                |      98|   226|2.3.0   |
|wa10op17no4b_Presto_Assai           |      99|   119|2.3.0   |
|wa11op17no5a_Allegro                |     102|   213|2.3.0   |
|wa11op17no5b_Presto                 |     127|   229|2.3.0   |
|wa12op17no6a_Allegro                |     118|   194|2.3.0   |
|wa12op17no6b_Andante                |      74|   166|2.3.0   |
|wa12op17no6c_Prestissimo            |     105|   232|2.3.0   |


## kleine_geistliche_konzerte

|                            file_name                            |measures|labels|standard|
|-----------------------------------------------------------------|-------:|-----:|--------|
|op08n01swv282_Eile_mich,_Gott,_zu_erretten                       |      68|    84|2.1.1   |
|op08n02swv283_Bringt_her_dem_Herren                              |      89|   176|2.1.1   |
|op08n03swv284_Ich_danke_dem_Herrn_von_ganzem_Herzen              |     114|   237|2.1.1   |
|op08n04swv285_O_süsser,_o_freundlicher                           |     107|   193|2.1.1   |
|op08n05swv286_Der_Herr_ist_gross                                 |      74|   139|2.1.1   |
|op08n06swv287_O_lieber_Herre_Gott                                |      96|   199|2.1.1   |
|op08n07swv288_Ihr_Heiligen,_lobsinget_dem_Herren                 |      81|   145|2.1.1   |
|op08n08swv289_Erhöre_mich,_wenn_ich_rufe                         |      65|   128|2.1.1   |
|op08n09swv290_Wohl_dem,_der_nicht_wandelt_im_Rat_der_Gottlosen   |     134|   242|2.1.1   |
|op08n10swv291_Schaffe_in_mir,_Gott,_ein_reines_Herz              |      39|   104|2.1.1   |
|op08n11swv292_Der_Herr_schauet_vom_Himmel_auf_der_Menschen_Kinder|      81|   135|2.1.1   |
|op08n12swv293_Lobet_den_Herren,_der_zu_Zion_wohnet               |      80|   137|2.1.1   |
|op08n13swv294_Eins_bitte_ich_vom_Herren                          |      86|   165|2.1.1   |
|op08n14swv295_O_hilf,_Christe_Gottes_Sohn                        |      81|   121|2.1.1   |
|op08n15swv296_Fürchte_dich_nicht                                 |      77|   167|2.1.1   |
|op08n16swv297_O_Herr_hilf                                        |      61|   170|2.1.1   |
|op08n17swv298_Das_Blut_Jesu_Christi                              |      38|     0|2.1.1   |
|op08n18swv299_Die_Gottseligkeit_ist_zu_allen_Dingen_nütz         |      51|    73|2.1.1   |
|op08n19swv300_Himmel_und_Erde_vergehen                           |      54|    91|2.1.1   |
|op08n20swv301_Nun_komm_der_Heiden_Heiland                        |      90|   165|2.1.1   |
|op08n21swv302_Ein_Kind_ist_uns_geboren                           |     125|   276|2.1.1   |
|op08n22swv303_Wir_glauben_all_an_einen_Gott                      |     120|   281|2.1.1   |
|op08n23swv304_Siehe,_mein_Fürsprecher_im_Himmel                  |      93|   172|2.1.1   |
|op08n24swv305_Ich_hab_mein_Sach_Gott_heimgestellt                |     299|   573|2.1.1   |
|op09n01swv306_Ich_will_den_Herren_loben_allezeit                 |      85|   218|2.1.1   |
|op09n02swv307_Was_hast_du_verwirket                              |      82|   184|2.1.1   |
|op09n03swv308_O_Jesu,_nomen_dulce                                |      66|   149|2.1.1   |
|op09n04swv309_O_misericordissime_Jesu                            |      92|   181|2.1.1   |
|op09n05swv310_Ich_liege_und_schlafe                              |      86|   179|2.1.1   |
|op09n06swv311_Habe_deine_Lust_an_dem_Herren                      |     141|   351|2.1.1   |
|op09n07swv312_Herr,_ich_hoffe_darauf                             |      78|   167|2.1.1   |
|op09n08swv313_Bone_Jesu,_verbum_Patris                           |     124|   268|2.1.1   |
|op09n09swv314_Verbum_caro_factum                                 |     121|   260|2.1.1   |
|op09n10swv315_Hodie_Christus_natus_est                           |      99|   241|2.1.1   |
|op09n11swv316_Wann_unsre_Augen_schlafen_ein                      |      76|   170|2.1.1   |
|op09n12swv317_Meister,_wir_haben_die_ganze_Nacht_gearbeitet      |      46|    86|2.1.1   |
|op09n13swv318_Die_Furcht_des_Herren                              |      66|   118|2.1.1   |
|op09n14swv319_Ich_beuge_meine_Knie_gegen_dem_Vater               |      95|   215|2.1.1   |
|op09n15swv320_Ich_bin_jung_gewesen_und_bin_alt_worden            |      65|   150|2.1.1   |
|op09n16swv321_Herr,_wenn_ich_nur_dich                            |      78|   187|2.1.1   |
|op09n17swv322_Rorate,_rorate_coeli                               |      64|   190|2.1.1   |
|op09n18swv323_Joseph,_du_Sohn_David                              |      77|   170|2.1.1   |
|op09n19swv324_Ich_bin_die_Auferstehung                           |      99|   234|2.1.1   |
|op09n20swv325_Die_Seele_Christi_heilige_mich                     |     114|   217|2.1.1   |
|op09n21swv326_Ich_ruf_zu_dir,_Herr_Jesu_Christ                   |      85|   180|2.1.1   |
|op09n22swv327_Allein_Gott_in_der_Höh                             |     148|   352|2.1.1   |
|op09n23swv328_Veni,_Sancte_Spiritus                              |     122|   259|2.1.1   |
|op09n24swv329_Ist_Gott_für_uns                                   |      76|   192|2.1.1   |
|op09n25swv330_Wer_will_uns_scheiden_von_der_Liebe_Gottes         |      79|   178|2.1.1   |
|op09n26swv331_Die_Stimm_des_Herren_gehet_auf_den_Wassern         |     138|   237|2.1.1   |
|op09n27swv332_Jubilate_Deo_omnis_terra                           |     130|   351|2.1.1   |
|op09n28swv333_Sei_gegrüßet,_Maria                                |     220|   376|2.1.1   |
|op09n29swv334_Ave_Maria,_qualis_est                              |     215|   376|2.1.1   |
|op09n30swv335_Was_betrübst_du_dich,_meine_Seele                  |      87|   194|2.1.1   |
|op09n31swv336_Quemadmodum_desiderat_cervus                       |     189|   478|2.1.1   |
|op09n32swv337_Aufer_immensam                                     |     165|   428|2.1.1   |


## kozeluh_sonatas

|file_name |measures|labels|standard|
|----------|-------:|-----:|--------|
|09op08no1a|     135|   272|2.1.0   |
|09op08no1b|      67|   149|2.1.0   |
|10op08no2a|     155|   350|2.1.0   |
|10op08no2b|      73|   171|2.1.0   |
|10op08no2c|     156|   493|2.1.0   |
|11op10no1a|     177|   493|2.1.0   |
|14op13no2a|     171|   213|2.1.0   |
|14op13no2b|      49|   153|2.1.0   |
|14op13no2c|      93|   193|2.1.0   |
|15op13no3a|     137|   373|2.1.0   |
|15op13no3b|      84|   234|2.1.0   |
|15op13no3c|     141|   360|2.1.0   |
|16op15no1a|      34|   111|2.1.0   |
|16op15no1b|     208|   524|2.1.0   |
|16op15no1c|     186|   523|2.1.0   |
|17op15no2a|     201|   527|2.1.0   |
|17op15no2b|      40|   140|2.1.0   |
|17op15no2c|     160|   385|2.1.0   |
|19op17no1a|      37|   123|2.1.0   |
|19op17no1b|     255|   516|2.1.0   |
|19op17no1c|     213|   345|2.1.0   |
|20op17no2a|     226|   608|2.1.0   |
|20op17no2b|     100|   291|2.1.0   |
|20op17no2c|     218|   482|2.1.0   |
|21op17no3a|     193|   543|2.1.0   |
|21op17no3b|     219|   589|2.1.0   |
|22op20no1a|     171|   291|2.1.0   |
|22op20no1b|      45|   124|2.1.0   |
|22op20no1c|     150|   267|2.1.0   |
|23op20no2a|     134|   495|2.1.0   |
|23op20no2b|      51|   150|2.1.0   |
|23op20no2c|     143|   329|2.1.0   |
|24op20no3a|     152|   351|2.1.0   |
|24op20no3b|      50|   121|2.1.0   |
|24op20no3c|     159|   453|2.1.0   |
|25op26no1a|     216|   514|2.1.0   |
|25op26no1b|      50|   153|2.1.0   |
|25op26no1c|     178|   240|2.1.0   |
|26op26no2a|     225|   473|2.1.0   |
|26op26no2b|     174|   482|2.1.0   |
|27op26no3a|     204|   555|2.1.0   |
|27op26no3b|      54|   169|2.1.0   |
|27op26no3c|     213|   246|2.1.0   |
|28op30no1a|     152|   344|2.1.0   |
|28op30no1b|      50|   185|2.1.0   |
|28op30no1c|     207|   457|2.1.0   |
|29op30no2a|     195|   405|2.1.0   |
|29op30no2b|      39|   159|2.1.0   |
|29op30no2c|     206|   474|2.1.0   |


## liszt_pelerinage

|                                file_name                                |measures|labels|standard|
|-------------------------------------------------------------------------|-------:|-----:|--------|
|160.01_Chapelle_de_Guillaume_Tell                                        |      97|   174|2.3.0   |
|160.02_Au_Lac_de_Wallenstadt                                             |     112|    84|2.3.0   |
|160.03_Pastorale                                                         |      48|   200|2.3.0   |
|160.04_Au_Bord_dUne_Source                                               |      66|   465|2.3.0   |
|160.05_Orage                                                             |     160|   307|2.1.1   |
|160.06_Vallee_dObermann                                                  |     216|   631|2.3.0   |
|160.07_Eglogue                                                           |     117|   214|2.1.1   |
|160.08_Le_Mal_du_Pays_(Heimweh)                                          |      70|   200|2.1.1   |
|160.09_Les_Cloches_de_Geneve_(Nocturne)                                  |     188|   205|2.1.1   |
|161.01_Sposalizio                                                        |     133|   237|2.1.1   |
|161.02_Il_Pensieroso                                                     |      48|    88|2.3.0   |
|161.03_Canzonetta_del_Salvator_Rosa                                      |      75|   274|2.3.0   |
|161.04_Sonetto_47_del_Petrarca                                           |      95|   153|2.3.0   |
|161.05_Sonetto_104_del_Petrarca                                          |      79|   121|2.3.0   |
|161.06_Sonetto_123_del_Petrarca                                          |      84|   149|2.3.0   |
|161.07_Apres_une_lecture_du_Dante                                        |     373|   631|2.3.0   |
|162.01_Gondoliera                                                        |     125|   121|2.3.0   |
|162.02_Canzone                                                           |      60|    98|2.3.0   |
|162.03_Tarantella_da_Guillaume_Louis_Cottrau._Presto_e_canzone_napolitana|     479|   716|2.1.1   |


## mahler_kindertotenlieder

|                file_name                |measures|labels|standard|
|-----------------------------------------|-------:|-----:|--------|
|kindertotenlieder_01_nun_will_die_sonn   |      84|   179|2.3.0   |
|kindertotenlieder_02_nun_seh_ich_wohl    |      74|    96|2.3.0   |
|kindertotenlieder_03_wenn_dein_mutterlein|      70|   118|2.3.0   |
|kindertotenlieder_04_oft_denk_ich        |      71|    53|2.3.0   |
|kindertotenlieder_05_in_diesem_wetter    |     139|   149|2.3.0   |


## medtner_tales

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op08n01  |      81|   213|2.3.0   |
|op14n01  |      85|   265|2.3.0   |
|op26n01  |      47|   180|2.3.0   |
|op26n02  |      65|   166|2.3.0   |
|op26n03  |      81|   116|2.3.0   |
|op26n04  |      77|   300|2.3.0   |
|op34n01  |     237|   669|2.3.0   |
|op34n02  |      48|   195|2.3.0   |
|op34n03  |     144|   408|2.3.0   |
|op34n04  |      61|   323|2.3.0   |
|op35n01  |      75|   272|2.3.0   |
|op35n02  |     139|   422|2.3.0   |
|op35n03  |      80|   320|2.3.0   |
|op35n04  |     122|   345|2.3.0   |
|op42n01  |     134|   479|2.3.0   |
|op42n02  |      67|   178|2.3.0   |
|op42n03  |     182|   504|2.3.0   |
|op48n01  |     553|   871|2.3.0   |
|op48n02  |     186|   282|2.3.0   |


## mendelssohn_quartets

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|01op12a  |     292|   673|2.1.0   |
|01op12b  |     128|   349|2.1.0   |
|01op12c  |      65|   212|2.1.0   |
|01op12d  |     313|   771|2.1.0   |
|02op13a  |     251|   793|2.1.0   |
|02op13b  |     125|   544|2.1.0   |
|02op13c  |     163|   415|2.1.0   |
|02op13d  |     397|   805|2.1.0   |
|03op44,1a|     374|   751|2.1.0   |
|03op44,1b|     225|   393|2.1.0   |
|03op44,1c|     155|   438|2.1.0   |
|03op44,1d|     316|   819|2.1.0   |
|04op44,2a|     277|   839|2.1.0   |
|04op44,2b|     244|   829|2.1.0   |
|04op44,2c|      83|   328|2.1.0   |
|04op44,2d|     515|   794|2.1.0   |
|05op44,3a|     369|  1044|2.1.0   |
|05op44,3b|     301|   635|2.1.0   |
|05op44,3c|     131|   385|2.1.0   |
|05op44,3d|     323|  1000|2.1.0   |
|06op80a  |     324|   729|2.1.0   |
|06op80b  |     301|   338|2.1.0   |
|06op80c  |     120|   388|2.1.0   |
|06op80d  |     461|   493|2.1.0   |


## mozart_piano_sonatas

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|K279-1   |     100|   251|        |
|K279-2   |      74|   156|        |
|K279-3   |     158|   321|        |
|K280-1   |     144|   225|        |
|K280-2   |      60|   124|        |
|K280-3   |     190|   199|        |
|K281-1   |     109|   208|        |
|K281-2   |     106|   153|        |
|K281-3   |     162|   384|        |
|K282-1   |      36|   104|        |
|K282-2   |      72|   129|        |
|K282-3   |     102|   176|        |
|K283-1   |     120|   326|        |
|K283-2   |      39|   169|        |
|K283-3   |     277|   337|        |
|K284-1   |     127|   330|        |
|K284-2   |      92|   228|        |
|K284-3   |     260|   755|        |
|K309-1   |     155|   307|        |
|K309-2   |      79|   259|        |
|K309-3   |     252|   406|        |
|K310-1   |     133|   292|        |
|K310-2   |      86|   252|        |
|K310-3   |     252|   428|        |
|K311-1   |     112|   319|        |
|K311-2   |      93|   241|        |
|K311-3   |     269|   491|        |
|K330-1   |     150|   293|        |
|K330-2   |      64|   187|        |
|K330-3   |     171|   365|        |
|K331-1   |     134|   399|        |
|K331-2   |     100|   160|        |
|K331-3   |     127|   128|        |
|K332-1   |     229|   316|        |
|K332-2   |      40|   168|        |
|K332-3   |     245|   449|        |
|K333-1   |     165|   431|        |
|K333-2   |      82|   217|        |
|K333-3   |     224|   460|        |
|K457-1   |     185|   308|        |
|K457-2   |      57|   214|        |
|K457-3   |     319|   328|        |
|K533-1   |     239|   584|        |
|K533-2   |     122|   261|        |
|K533-3   |     187|   423|        |
|K545-1   |      73|   119|        |
|K545-2   |      74|   146|        |
|K545-3   |      73|   143|        |
|K570-1   |     209|   245|        |
|K570-2   |      55|   250|        |
|K570-3   |      89|   281|        |
|K576-1   |     160|   295|        |
|K576-2   |      67|   151|        |
|K576-3   |     189|   381|        |


## pergolesi_stabat_mater

|           file_name            |measures|labels|standard|
|--------------------------------|-------:|-----:|--------|
|01. Stabat Mater dolorosa       |      47|   166|2.2.0   |
|02. Cujus animam gementem       |     108|   228|2.2.0   |
|03. O quam tristis et afflicta  |      26|    84|2.2.0   |
|04. Quae moerebat et dolebat    |     103|   214|2.2.0   |
|05. Quis est homo qui non fleret|      49|   122|2.2.0   |
|06. Vidit suum dulcem natum     |      43|   153|2.2.0   |
|07. Eja, Mater fons amois       |      94|   212|2.2.0   |


## peri_euridice

|      file_name      |measures|labels|standard|
|---------------------|-------:|-----:|--------|
|peri_euridice_scene_0|      14|    32|2.3.0   |
|peri_euridice_scene_1|     119|   341|2.3.0   |
|peri_euridice_scene_2|     288|   734|2.3.0   |
|peri_euridice_scene_3|     135|   323|2.3.0   |
|peri_euridice_scene_4|     304|   724|2.3.0   |
|peri_euridice_scene_5|     260|   735|2.3.0   |


## pleyel_quartets

|file_name |measures|labels|standard|
|----------|-------:|-----:|--------|
|b307op2n1a|     197|   403|2.3.0   |
|b307op2n1b|     107|   190|2.3.0   |
|b307op2n1c|      78|   156|2.3.0   |
|b309op2n3a|      98|   189|2.3.0   |
|b309op2n3b|     269|   507|2.3.0   |
|b309op2n3c|      74|   123|2.3.0   |


## poulenc_mouvements_perpetuels

|   file_name   |measures|labels|standard|
|---------------|-------:|-----:|--------|
|01_assez_modere|      24|    93|2.3.0   |
|02_tres_modere |      14|    58|2.3.0   |
|03_alerte      |      56|   127|2.3.0   |


## rachmaninoff_piano

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op42_05  |      16|    17|2.3.0   |
|op42_06  |      16|    82|2.3.0   |
|op42_07  |      18|    51|2.3.0   |
|op42_08  |      15|    45|2.3.0   |
|op42_09  |      19|    52|2.3.0   |
|op42_10  |      25|    45|2.3.0   |
|op42_01a |      16|    28|2.3.0   |
|op42_01b |      16|    35|2.3.0   |
|op42_02  |      16|    24|2.3.0   |
|op42_03  |      16|    52|2.3.0   |
|op42_04  |      16|    22|2.3.0   |
|op42_11  |      16|    54|2.3.0   |
|op42_12  |      23|    70|2.3.0   |
|op42_13a |      17|    69|2.3.0   |
|op42_13b |      13|    47|2.3.0   |
|op42_14  |      16|    35|2.3.0   |
|op42_15  |      26|    66|2.3.0   |
|op42_16  |      15|    58|2.3.0   |
|op42_17  |      23|    40|2.3.0   |
|op42_18  |      16|    50|2.3.0   |
|op42_19  |      17|    99|2.3.0   |
|op42_20  |      44|   101|2.3.0   |


## ravel_piano

|                 file_name                 |measures|labels|standard|
|-------------------------------------------|-------:|-----:|--------|
|Ravel_-_Jeux_dEau                          |      85|   257|2.1.0   |
|Ravel_-_Miroirs_I._Noctuelles              |     132|     0|        |
|Ravel_-_Miroirs_II._Oiseaux_tristes        |      32|     0|        |
|Ravel_-_Miroirs_III._Une_Barque_sur_l'ocean|     143|   237|2.1.0   |
|Ravel_-_Miroirs_IV._Alborada_del_gracioso  |     229|   368|2.1.0   |


## scarlatti_sonatas

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|K001     |      31|    89|2.3.0   |
|K002     |      78|   146|2.3.0   |
|K003     |      94|   198|2.3.0   |
|K004     |      39|   208|2.3.0   |
|K005     |      90|   126|2.3.0   |
|K006     |      75|    97|2.3.0   |
|K007     |     155|   270|2.3.0   |
|K008     |      47|   183|2.3.0   |
|K009     |      60|   142|2.3.0   |
|K010     |      75|   165|2.3.0   |
|K011     |      28|   101|2.3.0   |
|K012     |      48|   281|2.3.0   |
|K013     |     113|   240|2.3.0   |
|K014     |      43|   146|2.3.0   |
|K017     |     129|   198|2.3.0   |
|K018     |      51|   272|2.3.0   |
|K019     |      92|   229|2.3.0   |
|K020     |     102|   146|2.3.0   |
|K021     |     150|   270|2.3.0   |
|K022     |      78|   207|2.3.0   |
|K023     |      70|   267|2.3.0   |
|K025     |      87|   278|2.3.0   |
|K027     |      67|   204|2.3.0   |
|K031     |     114|   192|2.3.0   |
|K032     |      24|    39|2.3.0   |
|K033     |     119|   117|2.3.0   |
|K034     |      28|    67|2.3.0   |
|K035     |      40|   147|2.3.0   |
|K036     |      95|   193|2.3.0   |
|K037     |      52|   179|2.3.0   |
|K039     |      49|   217|2.3.0   |
|K040     |      24|    53|2.3.0   |
|K044     |     152|   208|2.3.0   |
|K046     |     144|   321|2.3.0   |
|K047     |      75|   309|2.3.0   |
|K048     |     124|   234|2.3.0   |
|K049     |     118|   268|2.3.0   |
|K050     |     159|   246|2.3.0   |
|K051     |      47|   257|2.3.0   |
|K052     |      55|   378|2.3.0   |
|K053     |     100|   135|2.3.0   |
|K054     |      57|   202|2.3.0   |
|K055     |     133|   197|2.3.0   |
|K056     |      58|   220|2.3.0   |
|K057     |     182|   311|2.3.0   |
|K059     |      31|    97|2.3.0   |
|K061     |     156|   268|2.3.0   |
|K062     |     109|   128|2.3.0   |
|K063     |      60|   118|2.3.0   |
|K064     |      47|    72|2.3.0   |
|K065     |      74|   137|2.3.0   |
|K066     |      32|   182|2.3.0   |
|K067     |      22|    88|2.3.0   |
|K068     |     116|   157|2.3.0   |
|K069     |      63|   162|2.3.0   |
|K071     |      29|   133|2.3.0   |
|K072     |      37|   135|2.3.0   |
|K074     |      40|    60|2.3.0   |
|K075     |      45|    98|2.3.0   |
|K076     |      67|   162|2.3.0   |
|K087     |      70|   201|2.3.0   |
|K092     |      55|   178|2.3.0   |
|K094     |      26|    56|2.3.0   |
|K095     |      23|    47|2.3.0   |
|K096     |     211|   357|2.3.0   |
|K097     |     247|   207|2.3.0   |
|K098     |     113|   165|2.3.0   |
|K099     |      86|   175|2.3.0   |
|K100     |      50|   144|2.3.0   |


## schubert_winterreise

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|n01      |     105|   214|2.1.0   |
|n02      |      51|    70|2.1.0   |
|n03      |      55|   141|2.1.0   |
|n04      |     109|   187|2.1.0   |
|n05      |      83|   245|2.1.0   |
|n06      |      32|    44|2.1.0   |
|n07      |      74|   176|2.1.0   |
|n08      |      69|   353|2.1.0   |
|n09      |      43|    72|2.1.0   |
|n10      |      67|   105|2.1.0   |
|n11      |      88|   168|2.1.0   |
|n12      |      48|    82|2.1.0   |
|n13      |      94|   111|2.1.0   |
|n14      |      44|    57|2.1.0   |
|n15      |      43|   169|2.1.0   |
|n16      |      47|   101|2.1.0   |
|n17      |      49|   112|2.1.0   |
|n18      |      19|    61|2.1.0   |
|n19      |      43|    66|2.1.0   |
|n20      |      83|   167|2.1.0   |
|n21      |      32|   153|2.1.0   |
|n22      |      46|    80|2.1.0   |
|n23      |      32|    87|2.1.0   |
|n24      |      61|    79|2.1.0   |


## schulhoff_suite_dansante_en_jazz

|            file_name            |measures|labels|standard|
|---------------------------------|-------:|-----:|--------|
|suite_dansante_en_jazz_1_stomp   |      46|    96|2.3.0   |
|suite_dansante_en_jazz_2_strait  |      39|    87|2.3.0   |
|suite_dansante_en_jazz_3_waltz   |      70|    91|2.3.0   |
|suite_dansante_en_jazz_4_tango   |      40|    63|2.3.0   |
|suite_dansante_en_jazz_5_slow    |      41|    96|2.3.0   |
|suite_dansante_en_jazz_6_fox-trot|      50|    53|2.3.0   |


## schumann_kinderszenen

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|n01      |      22|    44|2.3.0   |
|n02      |      40|   123|2.3.0   |
|n03      |      31|    58|2.3.0   |
|n04      |      17|    53|2.3.0   |
|n05      |      16|    48|2.3.0   |
|n06      |      24|    84|2.3.0   |
|n07      |      24|    71|2.3.0   |
|n08      |      32|    73|2.3.0   |
|n09      |      24|    46|2.3.0   |
|n10      |      57|    67|2.3.0   |
|n11      |      48|   140|2.3.0   |
|n12      |      32|    92|2.3.0   |
|n13      |      25|    49|2.3.0   |


## schumann_liederkreis

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op39n01  |      28|    47|2.1.0   |
|op39n02  |      30|    66|2.1.0   |
|op39n03  |      72|   106|2.1.0   |
|op39n04  |      39|    53|2.1.0   |
|op39n05  |      68|    83|2.1.0   |
|op39n06  |      30|    68|2.1.0   |
|op39n07  |      39|    66|2.1.0   |
|op39n08  |      39|    88|2.1.0   |
|op39n09  |      28|    86|2.1.0   |
|op39n10  |      41|   108|2.1.0   |
|op39n11  |      50|    67|2.1.0   |
|op39n12  |      31|    54|2.1.0   |


## sweelinck_keyboard

|        file_name         |measures|labels|standard|
|--------------------------|-------:|-----:|--------|
|SwWV258_fantasia_cromatica|     196|   501|2.1.0   |


## tchaikovsky_seasons

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op37a01  |     103|   313|2.3.0   |
|op37a02  |     169|   278|2.3.0   |
|op37a03  |      46|   119|2.3.0   |
|op37a04  |      86|   210|2.3.0   |
|op37a05  |      88|   193|2.3.0   |
|op37a06  |      99|   263|2.3.0   |
|op37a07  |      56|   179|2.3.0   |
|op37a08  |     198|   514|2.3.0   |
|op37a09  |      90|   368|2.3.0   |
|op37a10  |      56|   193|2.3.0   |
|op37a11  |      83|   168|2.3.0   |
|op37a12  |     176|   261|2.3.0   |


## wagner_overtures

|                        file_name                         |measures|labels|standard|
|----------------------------------------------------------|-------:|-----:|--------|
|WWV090_Tristan_01_Vorspiel-Prelude_Ricordi1888Floridia    |     111|   360|2.1.0   |
|WWV096-Meistersinger_01_Vorspiel-Prelude_SchottKleinmichel|     222|  1075|2.1.0   |


## wf_bach_sonatas

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|F001_n08a|      63|   204|2.3.0   |
|F001_n08b|      40|    77|2.3.0   |
|F001_n08c|     101|   217|2.3.0   |
|F002_n07a|      62|   140|2.3.0   |
|F002_n07b|      44|   120|2.3.0   |
|F002_n07c|      66|   166|2.3.0   |
|F003_n04a|      83|   316|2.3.0   |
|F003_n04b|      64|   223|2.3.0   |
|F003_n04c|     108|   290|2.3.0   |
