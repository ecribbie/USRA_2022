#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec

python get_declone_script.py ../DATA/adjacency.txt ../DATA/GENERAX_MAPPING_FILES/ ../DATA/DECLONE_ADJ_PAIR_FILES/

