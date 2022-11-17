#!/bin/bash
#SBATCH --time=12:00:00
#SBATCH --mem=512G
#SBATCH --account=def-chauvec

../../../../spp_dcj/scripts/spp_dcj.py -m ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_5.idmap -a 0.5 -b 0.25 species_tree_spp.txt \
    adjacencies_0_5.txt > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_5.ilp 2> ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_5.spp_dcj.log


