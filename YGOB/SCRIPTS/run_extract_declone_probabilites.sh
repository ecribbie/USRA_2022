#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-1
#SBATCH --output=log/extract_declone_prob_1_%a.log
#SBATCH --error=log/extract_declone_prob_1_%a.err


ID=$((SLURM_ARRAY_TASK_ID + 0))
file_path_prefix="../EXP/DECLONE/MACSE_1_I/"
file_path_suffix=".txt"
declone_file="${file_path_prefix}${ID}${file_path_suffix}"
output_path_prefix="../EXP/DECLONE_PROBABILITY_FILES/"
output_path_suffix=".txt"
output_file="${output_path_prefix}${ID}${output_path_suffix}"

script="../DATA/declone_macse_1_script.txt"

python extract_declone_adjacency_probabilities.py ${declone_file} ${output_file} ${script}


