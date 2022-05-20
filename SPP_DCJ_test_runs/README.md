These test runs were to test the SPP_DCJ algorithm on very basic test files in order to spot mistakes/improvements to be made.

## Possible changes to be made:

-in run.sh file change Example.sol to Example1.sol on line 7 (this is just a typo and the program will not run without fixing this)

-in visualize_genomes.py script line 9 the locale variable "en_US" will not always work and is machine dependant (mine requires en_US.utf8) to find the possible values ot enter run locale -a 

-The plots and other result files are incorrect because of the issus with Example vs Example1 and therefore will need to be updated

-Line 447 typo writs whould be writes


These test runs also allowed to learn how the algorithm works, how to run it and what it is outputing.


## To run the algorithm:

-Create run.sh similar to the one provided but update paths to scripts and change if wanted the name of output and input files.

-The two input files required are the SpeciesTree.txt and AdjacenciesExample1.txt. These are just the names used in the example run.sh file provided

-Change desired settings, alpha level, beta level and if desired output file of ID-to-gene extremity mapping, in the example Example1.idmap


## Output understanding

### Predicted Adjacencies:

-This table provides the adjacencies that remain after the algorithm optimizes which adjacencies to keep and remove


### Plot summary:

-These plots are graphical representation of the genomes

-Light grey lines are a gene itself or a telomere

-Dark black lines are for all adjacencies

-Red highlights signify that that adjacency is present in the final solution

   **NOTE:Gene-telomere adjacencies will never be red**
