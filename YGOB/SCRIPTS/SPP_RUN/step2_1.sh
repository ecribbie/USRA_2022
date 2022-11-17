#!/bin/sh
#SBATCH --account=def-chauvec
#SBATCH --time=12:00:00
#SBATCH --mem=512G
# run ILP
gurobi_cl ResultFile=../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.sol ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.ilp > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.gurobi.log


