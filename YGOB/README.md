# Yeast Gene Order Browser

This directory contains the data, scripts and results obtained on
yeasts data obtained from the <a href="ygob.ucd.ie/ygob/">YGOB data
repository</a>.

This directory is organized in several subdirectories:
- `DATA` contains everything related to downloading and preprocessing the data from YGOB.
- `SCRIPTS` contains all scripts
- `EXP` contains the results of the expertiments ran using the YGOB data.


## YGOB Data

The data that is being used from the YGOB site is as follows:
  - Species genome tab files for each specie, these were copie pasted from the YGOB site May 2022
  - Pillars tab file, copie pasted from the YGOB site May 2022
  - AA.fsa and NT.fsa file not found in this repository due to size but was read in using the run_get_ygob_fasta_file.sh script in May 2022

An explanation of the files can be found in the <a href="http://ygob.ucd.ie/ygob/data/v7-Aug2012/README">YGOB README file</a>.


In order to work with the large AA.fsa and NT.fsa files without the sequences an AA_genes.txt and NT_genes.txt file was created which contains the genes and their information without their sequences. 

This was done with:

`grep ">" AA.fsa > AA_genes.txt`

`grep ">" NT.fsa > NT_genes.txt`


## Functions

Several functions that are used in various scripts as well as the Exploration Notebook were written in a functions.py file in order to easily access them and avoid rewriting the same code over and over again.

## Initial Exploration

In order to better understand the data at hand and in order to select a subset of species and pillars that better fit our goal a Jupyter Notebook `data_exploration.ipynb` was created. 

This Notebook explains the steps taken and and selections made. 

## Preparing Files for Software

The first step was to create a `gene_species_mapping_output.txt` file in `DATA` with the gene-species mappings, this is a file where each line contains a gene followed by a space and then its specie. This was in fact done in the data exploration using a function from the functions file.

The second step was to create a file `desired_pillar.txt` containing the desired pillars, in this case this meant removing genes that were not part of selected species as well as removing pillars with less than 3 genes in it. This was done with `run_get_desired_pillars.sh`

Finally two folders were created `PILLARS_AA_FILES` and `PILLARS_NT_FILES` in the `DATA` folder. By running `run_AA_get_family_files` and `run_NT_get_family_files`, several fasta files were created into these folders. Each file contained in fasta format the genes for a specific pillar in our `desired_pillar.txt` file including either their amino-acid or nucleotide sequences respectively. Each folder also contains a list of all the file names `file_names.txt`, done with `printf '%s\n' * > file_names.txt` from each folder 


## Running Software

The First step was to create sequence alignments. This was done with two different softwares in order to later test the methods robustness. For this step [MUSCLE](http://drive5.com/muscle/) and [MACSE](https://bioweb.supagro.inra.fr/macse/) were used. They each were run on all of the `PILLARS_AA_FILES` and `PILLARS_NT_FILES` respectively. This was done with the `run_muscle.sh` and `run_macse.sh` scripts. The result from MUSCLE was a set of files that contained aligned sequences for each gene in a specific family. These files were saved into a precreated folder in `EXP` called `MUCLES_AA`. As for MACSE the result was two similar sets of files with aligned sequences for all genes in a specific family, a group of AA sequence files and a group of NT sequence files. They were also saved into precreated folders in `EXP` called `MACSE_AA` and `MACSE_NT`. The logs for these runs are saved into a folder called `log` in the `SCRIPTS` folder. After the initial run `printf '%s\n' * > file_names.txt` was run in the three output folders. From there I noticed that there were not all the files that there should have been. Using the `find_missing_files.py` script I created files such as `macse_err1_files.txt` that held the family names of the output files that were not created. Then using scripts such as `run_macse_err1.sh` to rerun the problamatic files by increasing the allocation that was problematic such as time or memory. This was determined by checking the corresponding output files for the problematic runs. From here in order to run the [GENERAX](https://github.com/BenoitMorel/GeneRax/wiki/GeneRax) software on these outputs, specific family files need to be created. This was done with `make_generax_family_files.py`.  `GENERAX` is then run with `run_generax.sh`.




#### Software Use Explanation (to be removed later)
  - MUSCLE: after loading muscle module run with syntax muscle -in input_file -out ouput_file see [MUSCLE](http://drive5.com/muscle/)
  - MACSE: load java module and run with syntax java -jar (software directory path) -prog alignSequences -seq input -out_NT output1 -out_AA output2 see [MACSE](https://bioweb.supagro.inra.fr/macse/)
  - IQ-TREE: after loading iq-tree/2.0.7 module run with iqtree, for info run iqtree -h for help file and options or see [IQ-TREE](http://www.iqtree.org/doc/Quickstart#minimal-command-line-examples)
  - TREERECS: use (path to Treerecs/bin/treerecs) as call to, for info/help add --help. See [TREERECS](https://project.inria.fr/treerecs/get-treerecs/)
  - GENERAX: use mpiexec as call to and for info/help  run mpiexec -h see [GENERAX](https://github.com/BenoitMorel/GeneRax/wiki/GeneRax) for more info (may require ENV not sure yet)

