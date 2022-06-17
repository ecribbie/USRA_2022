# YGOB Data

## Downloading

The YGOB data were downloaded on May 25 2022 using thecommands
```
python get_ygob_fasta_file.py 'http://ygob.ucd.ie/ygob/data/v7-Aug2012/AA.fsa' 'AA.fsa'
python get_ygob_fasta_file.py 'http://ygob.ucd.ie/ygob/data/v7-Aug2012/NT.fsa' 'NT.fsa'
```
Further the `pillars.txt` file was copie pasted from 'http://ygob.ucd.ie/ygob/data/v7-Aug2012/Pillars.tab' on May 25 2022

The file `AA.fsa` contains the amnino-acid sequences of all coding
genes, in FASTA format and the file `NT.fsa` the nucleotide sequences
of all genes (including non-coding genes), also in FASTA format.

To be able to do a preliminary analysis of gene families in the YGOB
data without having to read the actual sequences, the FASTA headers of
all genes were extracted from both files:
```
grep ">" AA.fsa > AA_genes.txt
grep ">" NT.fsa > NT_genes.txt
```

The `desired_pillars.txt` file was created by running `run_create_desired_pillar_file.sh`

The `gene_species_mapping_output.txt` file was written using the gene_species_mapping function in the `data_exploration.ipynb` notebook. It is a file where each line contains a gene followed by a whit space and the that genes associated specie. It is used for associating all the genes to their corresponding specie.

