# Yeast Gene Order Browser

## Overview

Link to [YGOB website](ygob.ucd.ie/ygob/)

First created a python file that takes a species genome tab file and creates a nested dictionary containing the species' genes and their relevant information such as direction, start and end coordinates and similarities section to other genes. That file is called "genome_tab_to_dictionary.py"

The species files can be found [here](ygob.ucd.ie/ygob/data/v7-Aug2012/)

The genome_tab_to_dictionary.py script currently takes all files with structure as described in the [README file](ygob.ucd.ie/ygob/data/v7-Aug2012/README) section (2) 

The Anc_tab_to_dictionary.py script currently takes the Anc genome tab file as described in the [README file](ygob.ucd.ie/ygob/data/v7-Aug2012/README) section (2) under Ancestor 


## Questions


## Information on files

  - *Pillars.tab file:*
    - Each row/pillar is a family
    - Families not yet reconcilled (may have two copies of same gene)
  - *Genome.tab files:*
    - Relevant columns: Gene name, direction, start/end coordinates
    - Can be used to extract adjacencies that will be required for SPP_DCJ


## Running Software

  - MUSCLE: after loading muscle module run with syntax muscle -in input_file -out ouput_file see [MUSCLE](http://drive5.com/muscle/)
  - MACSE: load java module and run with syntax java -jar <software directory path> -prog alignSequences -seq input -out_NT output1 -out_AA output2 see [MACSE](https://bioweb.supagro.inra.fr/macse/)
  - IQ-TREE: after loading iq-tree/2.0.7 module run with iqtree, for info run iqtree -h for help file and options or see [IQ-TREE](http://www.iqtree.org/doc/Quickstart#minimal-command-line-examples)
  - TREERECS:
  - GENERAX: use mpiexec as call to and for info/help in CL run mpiexec -h see [GENERAX](https://github.com/BenoitMorel/GeneRax/wiki/GeneRax) for more info (may require ENV not sure yet)




## Formatting of similarities (NO LONGER NEEDED)

The following are the authors associated to certain species on the YGOB phylogeny. Since each genome tab file's similarity section is then written by a different group it's structure is different. The following summaries very briefly describe the structure of the similarity colomns for species added by the associated groups.


__Gordon et al. (2011)__

  - similarities as "Anc_#.### ----" or "-----" or "trna Type:..." or nothing. Extra text sometimes added at end, ---- is a gene in Saccharomyces cerevisiae

__Scannel et al. (2011)__

  - similarities as "--- (REAL or REPEAT)" where --- is a gene in Saccharomyces cerevisiae

__Scannel et al. (2007)__

  - similarites as "[### nt, ### aa]"

__Dujon et al. (2004)__

  - Review again more complicated and differing methods through same species

__Goffeau et al. (s. cer.)__

  - no similarities relevant just descriptions it is s.cer. which most compare to. See table with Ancestor (Anc) for matches

__Souciet et al. (2009)__

  - similarities as "similarity level "uniprot|--- Saccharomyces cerevisiae @@@ " description of other info" --- is uniprot code and @@@ is a gene in Saccharomyces cerevisiae

__Dietrich et al. (2004)__

  - "(Non-)Syntenic homolog of Saccharomyces cerevisiae --- " or one case of "No homolog in Saccharomyces cerevisiae, similar   to Kluyveromyces lactis @@@ "  --- Saccharomyces cerivisiae gene and @@@ is Kluyveromyces lactis gene

__Wendland et al. (2011)__

  - "similar to Saccharomyces cerevisiae --- " or "similar to Ashbya gossypii @@@ " --- is a gene of Saccharomyces cerevisiae  @@@ is a gene of Ashbya gossypii

__Kells et al. (2004)__

  - "--- extra description) where --- is a gene of Saccharomyces cerevisiae






