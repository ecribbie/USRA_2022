#!/bin/bash
#SBATCH --time=08:00:00
#SBATCH --mem=256G
#SBATCH --account=def-chauvec

../../../../spp_dcj/scripts/spp_dcj.py -m ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_9.idmap -a 0.5 -b 0.25 species_tree_spp.txt \
    adj_0_9.txt > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_9.ilp 2> ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_0_9.spp_dcj.log
