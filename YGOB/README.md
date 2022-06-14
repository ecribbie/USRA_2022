# Yeast Gene Order Browser

This directory contains the data, scripts and results obtained on
yeasts data obtained from the <a href="ygob.ucd.ie/ygob/">YGOB data
repository</a>.

This directory is organized in several subdirectories:
- `DATA` contains everything related to downloading and preprocessing the data from YGOB.
- `EXP` contains the results of the expertiments ran using the YGOB data.


## YGOB Data

The data that is being used from the YGOB site is as follows:
  - Species genome tab files for each specie, these were copie pasted from the YGOB site May 2022
  - Pillars tab file, copie pasted from the YGOB site May 2022
  - AA.fsa and NT.fsa file not found in this repository due to size but was read in using the run_get_ygob_fasta_file.sh script in May 2022


In order to work with the large AA.fsa and NT.fsa files without the sequences an AA_genes.txt and NT_genes.txt file was created which contains the genes and their information without their sequences. This was done with:





## TO REORGANIZE FROM HERE





## Information on files

  - *Pillars.tab file:*
    - Each row/pillar is a family
    - Families not yet reconcilled (may have two copies of same gene)
  - *Genome.tab files:*
    - Relevant columns: Gene name, direction, start/end coordinates
    - Can be used to extract adjacencies that will be required for SPP_DCJ


## Running Software

  - MUSCLE: after loading muscle module run with syntax muscle -in input_file -out ouput_file see [MUSCLE](http://drive5.com/muscle/)
  - MACSE: load java module and run with syntax java -jar (software directory path) -prog alignSequences -seq input -out_NT output1 -out_AA output2 see [MACSE](https://bioweb.supagro.inra.fr/macse/)
  - IQ-TREE: after loading iq-tree/2.0.7 module run with iqtree, for info run iqtree -h for help file and options or see [IQ-TREE](http://www.iqtree.org/doc/Quickstart#minimal-command-line-examples)
  - TREERECS: use (path to Treerecs/bin/treerecs) as call to, for info/help add --help. See [TREERECS](https://project.inria.fr/treerecs/get-treerecs/)
  - GENERAX: use mpiexec as call to and for info/help  run mpiexec -h see [GENERAX](https://github.com/BenoitMorel/GeneRax/wiki/GeneRax) for more info (may require ENV not sure yet)

