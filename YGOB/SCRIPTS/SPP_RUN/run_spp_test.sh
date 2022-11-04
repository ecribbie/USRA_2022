#!/bin/sh

# generate ILP
../../../../spp_dcj/scripts/spp_dcj.py -m Example1.idmap -a 0.5 -b 0.25 test_tree_out.txt \
    test_script_output.txt > Example1.ilp 2> Example1.spp_dcj.log
# run ILP
gurobi_cl ResultFile=Example.sol Example1.ilp > Example1.gurobi.log
# extract adjacencies from solution
../../../../spp_dcj/scripts/sol2adjacencies.py Example1.sol Example1.idmap > \
    PredictedAdjacenciesExample1.txt
# visualize candidate and predicted adjacencies
../../../../spp_dcj/scripts/visualize_genomes.py -i PredictedAdjacenciesExample1.txt \
     AdjacenciesExample1.txt > PredictedAdjacenciesExample1.pdf
