# Yeast Gene Order Browser

## Overview

Link to [YGOB website](ygob.ucd.ie/ygob/)

First created a python file that takes a species genome tab file and creates a nested dictionary containing the species' genes and their relevant information such as direction, start and end coordinates and similarities section to other genes. That file is called "genome_tab_to_dictionary.py"

The species files can be found [here](ygob.ucd.ie/ygob/data/v7-Aug2012/)

The genome_tab_to_dictionary.py script currently takes all files with structure as described in the [README file](ygob.ucd.ie/ygob/data/v7-Aug2012/README) section (2) 

The Anc_tab_to_dictionary.py script currently takes the Anc genome tab file as described in the [README file](ygob.ucd.ie/ygob/data/v7-Aug2012/README) section (2) under Ancestor 


## Questions

In the [genome.tab files](ygob.ucd.ie/ygob/data/v7-Aug2012/) such as that of [Cglabrata](ygob.ucd.ie/ygob/data/v7-Aug2012/Cglabrata_genome.tab) the 9th colomn discusses the genes similarities with other genes from different species. It uses various levels of similarity; similar to, weakly similar to, highly similar to, syntenic homolog of, etc.

When creating marker assignments for these species if a gene in one species is similar to a gene in another species would we assign both of these the same marker (example call them both gene 1), assuming for simplicity that these genes are not similar to others? If so whcih of these terms above would imply using the same marker? All of them?

Why does the [S.Cerevisiae Ohnologs File](http://ygob.ucd.ie/browser/ohnologs.html) have two genes matching to each Ancestor gene


## Formatting of similarities

The following are the authors associated to certain species on the YGOB phylogeny. Since each genome tab file's similarity section is then written by a different group it's structure is different. The following summaries very briefly describe the structure of the similarity colomns for species added by the associated groups.


__Gordon et al. (2011)__

-similarities as "Anc_#.### ----" or "-----" or "trna Type:..." or nothing. Extra text sometimes added at end, ---- is a gene in Saccharomyces cerevisiae

__Scannel et al. (2011)__

-similarities as "--- (REAL or REPEAT)" where --- is a gene in Saccharomyces cerevisiae

__Scannel et al. (2007)__

-similarites as "[### nt, ### aa]"

__Dujon et al. (2004)__

-Review again more complicated and differing methods through same species

__Goffeau et al. (s. cer.)__

-no similarities relevant just descriptions it is s.cer. which most compare to. See table with Ancestor (Anc) for matches

__Souciet et al. (2009)__

-similarities as "similarity level "uniprot|--- Saccharomyces cerevisiae @@@ " description of other info" --- is uniprot code and @@@ is a gene in Saccharomyces cerevisiae

__Dietrich et al. (2004)__

-"(Non-)Syntenic homolog of Saccharomyces cerevisiae --- " or one case of "No homolog in Saccharomyces cerevisiae, similar   to Kluyveromyces lactis @@@ "  --- Saccharomyces cerivisiae gene and @@@ is Kluyveromyces lactis gene

__Wendland et al. (2011)__

-"similar to Saccharomyces cerevisiae --- " or "similar to Ashbya gossypii @@@ " --- is a gene of Saccharomyces cerevisiae  @@@ is a gene of Ashbya gossypii

__Kells et al. (2004)__

-"--- extra description) where --- is a gene of Saccharomyces cerevisiae




## Issues to resolve

How to match up similar/identical genes across species when creating family assignments
  
  -Structure of similarities column not consistent and sometimes match up to what seem to be non existent genes example: (first gene of Cglabrata is said to be similar to KLLA0E10593g from Klactis but that gene is not found in Klactis genome tab file)
  
  -How to match to the right species, matches can be to various species (very much more commonly to S.cer or Anc though)
  
Need to consider not duplicating a marker in same species


