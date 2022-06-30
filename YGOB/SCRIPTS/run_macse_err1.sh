#!/bin/bash

#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-491
#SBATCH --output=log/macse_%a.log
#SBATCH --error=log/macse_%a.err
#SBATCH --mem=512M

str2=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../DATA/macse_err1_files.txt)
str1="NT_"
str3=".fsa"
file_NT=$str1$str2$str3

file_AA="${file_NT/NT/AA}"

java -jar ../../../TOOLS/macse_v2.06.jar -prog alignSequences -seq ../DATA/PILLAR_NT_FILES/${file_NT} -out_NT ../EXP/MACSE_NT/${file_NT} -out_AA ../EXP/MACSE_AA/${file_AA}

