#!/bin/sh
#SBATCH --account=def-chauvec
#SBATCH --time=48:00:00
#SBATCH --mem=257000M
# generate ILP
../../../../spp_dcj/scripts/spp_dcj.py -m ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.idmap -a 0.5 -b 0.25 species_tree_spp.txt \
    adjacencies_0_5.txt > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.ilp 2> ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.spp_dcj.log
# run ILP
gurobi_cl ResultFile=../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.sol ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.ilp > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.gurobi.log
# extract adjacencies from solution
../../../../spp_dcj/scripts/sol2adjacencies.py ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.sol ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I.idmap > \
    ../../EXP/SPP_DCJ/MACSE_1_I/Predictedadjacencies_macse_1_I.txt
# visualize candidate and predicted adjacencies
 ../../../../spp_dcj/scripts/visualize_genomes.py -i ../../EXP/SPP_DCJ/MACSE_1_I/Predictedadjacencies_macse_1_I.txt \
     adjacencies_0_5.txt > ../../EXP/SPP_DCJ/MACSE_1_I/Predictedadjacencies_macse_1_I.pdf
