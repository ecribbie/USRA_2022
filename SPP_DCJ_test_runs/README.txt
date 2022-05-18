Possible changes to be made:
-in run.sh file change Example.sol to Example1.sol on line 7 (this is just a typo and the program will not run without fixing this)
-in visualize_genomes.py script line 9 the locale variable "en_US" will not always work and is machine dependant (mine requires en_US.utf8) to find the possible values ot enter run locale -a 
-The plots and other result files are incorrect because of the issus with Example vs Example1 and therefore will need to be updated


Plot summary:
-Light grey is for a gene itself or a telomare
-Dark black is for adjacencies
-Red highlight signifies that that adjacencies is present in the final solution
*NOTE:Gene-telomare adjacencies will never be red
