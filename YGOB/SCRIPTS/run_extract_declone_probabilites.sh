#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-656
#SBATCH --output=log/extract_declone_prob_3_%a.log
#SBATCH --error=log/extract_declone_prob_3_%a.err

#total will be 20654, will need 3 runs. (1-9999),9999+(1-9999),19998+(1-656)
#make sure to change output/error path to 1,2 or 3 
ID=$((SLURM_ARRAY_TASK_ID + 19998))
file_path_prefix="../EXP/DECLONE/MACSE_1_I/"
file_path_suffix=".txt"
declone_file="${file_path_prefix}${ID}${file_path_suffix}"
output_path_prefix="../EXP/DECLONE_PROBABILITY_FILES/"
output_path_suffix=".txt"
output_file="${output_path_prefix}${ID}${output_path_suffix}"

script="../DATA/declone_macse_1_script.txt"

mapping_prefix="../DATA/GENERAX_INTO_NHX_MACSE_1/"
mapping_suffix="_reconciliated.nhx"

python extract_declone_adjacency_probabilities.py ${declone_file} ${output_file} ${script} ${mapping_prefix} ${mapping_suffix}


