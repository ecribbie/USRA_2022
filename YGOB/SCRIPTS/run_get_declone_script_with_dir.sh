#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec

python get_declone_script_with_dir.py ../DATA/adjacency.txt ../DATA/GENERAX_MAPPING_FILES/ ../DATA/DECLONE_MACSE_1_ADJ_PAIR_FILES/ ../DATA/declone_macse_1_script.txt ../DATA/GENERAX_INTO_NHX_MACSE_1/


