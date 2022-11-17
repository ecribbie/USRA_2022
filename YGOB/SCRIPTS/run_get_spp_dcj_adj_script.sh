#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec

python get_spp_dcj_adj_script.py ../EXP/DECLONE_PROBABILITY_FILES/ SPP_RUN/adjacencies_0_8.txt 0.8
