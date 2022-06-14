# YGOB Data

## Downloading

The YGOB data were downloaded on **TO ADD: DATE** using thecommands
```
python get_ygob_fasta_file.py 'http://ygob.ucd.ie/ygob/data/v7-Aug2012/AA.fsa' 'AA.fsa'
python get_ygob_fasta_file.py 'http://ygob.ucd.ie/ygob/data/v7-Aug2012/NT.fsa' 'NT.fsa'
```

The file `AA.fsa` contains the amnino-acid sequences of all coding
genes, in FASTA format and the file `NT.fsa` the nucleotide sequences
of all genes (including non-coding genes), also in FASTA format.

To be able to do a preliminary analysis o gene families in the YGOB
data without having to read the actual sequences, the FASTA headers of
all genes were extracted from both files:
```
grep ">" AA.fsa > AA_genes.txt
grep ">" NT.fsa > NT_genes.txt
```
