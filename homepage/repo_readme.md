# Distant Listening Corpus

Includes [dcml_corpora](https://github.com/DCMLab/dcml_corpora) (public) plus those that are to be published and merged into it. 

It has the `version_release` workflow installed. In order to automatically create a new version release that includes 
the whole corpus as datapackage, create and merge a Pull Request. However, three Frescobalid pieces currently have the 
invalid global key `e.phrygian` which is not recognized by the regEx of the DCML standard version 2.3.0. As a 
consequence, the boolean columns `globalkey_is_minor` and `localkey_is_minor` have missing values for these piece, 
which often leads to errors when wanting to load the concatenated dataframes with the correct (boolean) data type.
To avoid this, the datapackage should currently exclude the three pieces by using

    ms3 transform -M -N -X -D -e "12.31|12.33|12.45"