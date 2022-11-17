#!/bin/bash
#SBATCH --time=03:00:00
#SBATCH --mem=32G
#SBATCH --account=def-chauvec

../../../../spp_dcj/scripts/spp_dcj.py -m ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.idmap -a 0.5 -b 0.25 species_tree_spp.txt \
    adj_1.txt > ../../EXP/SPP_DCJ/MACSE_1_I/macse_1_I_1.ilp

