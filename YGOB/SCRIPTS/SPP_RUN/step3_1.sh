#!/bin/sh
#SBATCH --account=def-chauvec
#SBATCH --time=4:00:00
#SBATCH --mem=64G
# run ILP
gurobi_cl ResultFile=../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.sol ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.ilp > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.gurobi.log
# extract adjacencies from solution
../../../../spp_dcj/scripts/sol2adjacencies.py ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.sol ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.idmap > \
    ../../EXP/SPP_DCJ/MACSE_1_I/Predictedadjacencies_macse_1_I_1.txt
# visualize candidate and predicted adjacencies
 ../../../../spp_dcj/scripts/visualize_genomes.py -i ../../EXP/SPP_DCJ/MACSE_1_I/Predictedadjacencies_macse_1_I_1.txt \
     adj_1.txt > ../../EXP/SPP_DCJ/MACSE_1_I/Predictedadjacencies_macse_1_I_1.pdf

