#!/bin/bash
#SBATCH --time=01:30:00
#SBATCH --account=def-chauvec
#SBATCH --mem=17G

python get_declone_prob_distr.py ../EXP/DECLONE/MACSE_1_I/
