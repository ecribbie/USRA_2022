**Yeast Gene Order Browser**

**Overview**

Link to website:ygob.ucd.ie/ygob/

First created a python file that takes a species genome tab file and creates a nested dictionary containing the species' genes and their relevant information such as direction, start and end coordinates and similarities section to other genes. That file is called "ygob_conversion.py"

The species files can be found at:ygob.ucd.ie/ygob/data/v7-Aug2012/ 

The ygob_conversion.py script currently takes all files with structure as described in the README file: ygob.ucd.ie/ygob/data/v7-Aug2012/README section (2) 

The Ancestor genome tab is structured differently and we'll need to create a new script accordingly. (should just be a change in indices)


**Questions**

In the genome.tab files found at:ygob.ucd.ie/ygob/data/v7-Aug2012/ such as:ygob.ucd.ie/ygob/data/v7-Aug2012/Cglabrata_genome.tab the 9th colomn discusses the genes similarities with other genes in different species. It uses various levels of similarity; similar to, weakly similar to, highly similar to, syntenic homolog of, etc.

When creating marker assignments for these species if a gene in one species is similar to a gene in another species would we assign both of these the same marker (example call them both gene 1), assuming for simplicity that these genes are not similar to others? If so whcih of these terms above would imply using the same marker? All of them?


**Formatting of similarities**

The following are the authors associated to certain species on the YGOB phylogeny. Since each genome tab file's similarity section is then written by a different group it's structure is different. The following summaries very briefly describe the structure of the similarity colomns for species added by the associated groups.


Gordon et al. (2011)

-similarities as "Anc_#.### ----" or "-----" or "trna Type:..." or nothing. Extra text sometimes added at end, ---- is a gene in Saccharomyces cerevisiae

Scannel et al. (2011)

-similarities as "--- (REAL or REPEAT)" where --- is a gene in Saccharomyces cerevisiae

Scannel et al. (2007)

-similarites as "[### nt, ### aa]"

Dujon et al. (2004)

-Review again more complicated and differing methods through same species

Goffeau et al. (s. cer.)

-no similarities relevant just descriptions it is s.cer. which most compare to. See table with Ancestor (Anc) for matches

Souciet et al. (2009)

-similarities as "similarity level "uniprot|--- Saccharomyces cerevisiae @@@ " description of other info" --- is uniprot code and @@@ is a gene in Saccharomyces cerevisiae

Dietrich et al. (2004)

-"(Non-)Syntenic homolog of Saccharomyces cerevisiae --- " or one case of "No homolog in Saccharomyces cerevisiae, similar   to Kluyveromyces lactis @@@ "  --- Saccharomyces cerivisiae gene and @@@ is Kluyveromyces lactis gene

Wendland et al. (2011)

-"similar to Saccharomyces cerevisiae --- " or "similar to Ashbya gossypii @@@ " --- is a gene of Saccharomyces cerevisiae  @@@ is a gene of Ashbya gossypii

Kells et al. (2004)

-"--- extra description) where --- is a gene of Saccharomyces cerevisiae
