#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec

python get_declone_script.py ../DATA/adjacency.txt ../DATA/GENERAX_MAPPING_FILES/ ../DATA/DECLONE_MACSE_2_ADJ_PAIR_FILES/ ../DATA/declone_macse_2_script.txt ../DATA/GENERAX_INTO_NHX_MACSE_2/

