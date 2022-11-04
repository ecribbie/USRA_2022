#!/bin/sh

# generate ILP
../../../../spp_dcj/scripts/spp_dcj.py -m test3.idmap -a 0.5 -b 0.25 test_tree_out.txt \
    test_script_output.txt > test3.ilp 2> test3.spp_dcj.log
# run ILP
gurobi_cl ResultFile=test3.sol test3.ilp > test3.gurobi.log
# extract adjacencies from solution
../../../../spp_dcj/scripts/sol2adjacencies.py test3.sol test3.idmap > \
    Predictedadjtest3.txt
# visualize candidate and predicted adjacencies
 ../../../../spp_dcj/scripts/visualize_genomes.py -i Predictedadjtest3.txt \
     test_script_output.txt > Predictedadjtest3.pdf
