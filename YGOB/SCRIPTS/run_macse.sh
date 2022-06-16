#!/bin/bash

#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-2
#SBATCH --output=log/macse_%a.log

file_NT=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../DATA/PILLAR_NT_FILES/file_names.txt)

file_AA="${file_NT/NT/AA}"

java -jar ../../../TOOLS/macse_v2.06.jar -prog alignSequences -seq ../DATA/PILLAR_NT_FILES/${file_NT} -out_NT ../EXP/MACSE_NT/${file_NT} -out_AA ../EXP/MACSE_AA/${file_AA}

