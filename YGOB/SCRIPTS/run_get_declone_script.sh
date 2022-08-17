#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec

python get_declone_script.py ../DATA/adjacency.txt ../DATA/GENERAX_MAPPING_FILES/ ../DATA/DECLONE_MUSCLE_2_ADJ_PAIR_FILES/ ../DATA/declone_muscle_2_script.txt ../DATA/GENERAX_INTO_NHX_MUSCLE_2/

