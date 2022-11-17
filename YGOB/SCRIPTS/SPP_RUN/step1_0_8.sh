#!/bin/bash
#SBATCH --time=08:00:00
#SBATCH --mem=512G
#SBATCH --account=def-chauvec

../../../../spp_dcj/scripts/spp_dcj.py -m ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_8.idmap -a 0.5 -b 0.25 species_tree_spp.txt \
    adj_0_8.txt > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_8.ilp 2> ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_8.spp_dcj.log
