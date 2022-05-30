# Reconstructing reconciled gene trees
### Cedric Chauve

## Overview

This document describes the protocoles we will follow to reconstruct reconciled gene trees that will be used as input 
to the ancestral gene order reconstruction from YGOB data.

## Input

The input data will consist of a *species tree* for the considered species, and, for each gene family (YGOB pillar), 
of three files:
- a FASTA files containing the amino-acids sequences of all the genes in the family,
- a FASTA files containing the DNA sequences of all the genes in the family,
- a gene-to-species mapping file, in the GeneRax format described 
  <a href="https://github.com/BenoitMorel/GeneRax/wiki/Gene-to-species-mapping">here</a>.  

We assume the input families do not need to be pre-procesed to filter families and/or species, *i.e.* that this step 
has been done prior to reconstructing reconciled gene trees.

## Multiple Sequence Alignment

The first step of the reconciled gene trees reconstruction pipeline consists in generating a multiple sequence
alignment (MSA) per family, based on the sequence data.

In order to assess the impact of this step over the final result, we will consider two MSA tools:
- <a href="http://drive5.com/muscle/">muscle</a> applied to the amino-acids sequences; muscle is available on cedar (see <a href="https://docs.alliancecan.ca/wiki/Available_software">softwares available on Cedar</a>).
- <a href="https://bioweb.supagro.inra.fr/macse/">MACSE</a> applied to the DNA sequences; MACSE is not installed on Cedar.

## Reconciled Gene Trees

For each gene family, and MSA alignment for the family, a reconciled gene tree will be inferred using two competing methods:
- <a href="http://www.iqtree.org/">iqtree+fast bootstrap</a> followed by <a href="https://project.inria.fr/treerecs/">TreeRecs</a>.
- <a href="https://github.com/BenoitMorel/GeneRax/wiki/GeneRax">GeneRax</a>.

None of the tools are available on Cedar so they will need to be installed.

## Output

The output will thus consist in 4 reconciled gene trees per gene family, obtained with a combination of two MSA tools and two reconciliation tools.
