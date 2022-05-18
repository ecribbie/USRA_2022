<font size=8> Yeast Gene Order Browser 8 </font>

**Overview**

Link to website:ygob.ucd.ie/ygob/ First created a python file to take a species genome tab file and convert it inte a nested dictionary containig its genes and relevant information "ygob_conversion.py"

The species files can be found at:ygob.ucd.ie/ygob/data/v7-Aug2012/ The ygob_conversion.py currently takes all files with structure as described in README file:ygob.ucd.ie/ygob/data/v7-Aug2012/README section (2) Ancestor genome tab to be done seperatly

**Questions**
-in the genome.tab files found at:ygob.ucd.ie/ygob/data/v7-Aug2012/ such as:ygob.ucd.ie/ygob/data/v7-Aug2012/Cglabrata_genome.tab the 9th colomn discusses the genes similarities with other genes in different species. It uses various levels of similarity; similar to, weakly similar to, highly similar to, syntenic homolog of, etc.

When creating marker assignments for these species if a gene in one species is similar to a gene in another species would we assign both of these the same marker (example call them both gene 1), assuming for simplicity that these genes are not similar to others? If so whcih of these terms above would imply using the same marker? All of them?

Formatting of similarities
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
