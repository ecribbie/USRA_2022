#!/bin/bash

#SBATCH --time=02:00:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-1
#SBATCH --output=log/macse_%a_err5.log
#SBATCH --error=log/macse_%a_err5.err
#SBATCH --mem=4096M

str2=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../DATA/macse_err5_files.txt)
str1="NT_"
str3=".fsa"
file_NT=$str1$str2$str3

file_AA="${file_NT/NT/AA}"

java -jar ../../../TOOLS/macse_v2.06.jar -prog alignSequences -seq ../DATA/PILLAR_NT_FILES/${file_NT} -out_NT ../EXP/MACSE_NT/${file_NT} -out_AA ../EXP/MACSE_AA/${file_AA}

