#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-9999
#SBATCH --output=log/declone_muscle_2_S_%a.log
#SBATCH --error=log/declone_muscle_2_S_%a.err

ID=$((SLURM_ARRAY_TASK_ID + 0))
#8376
line=$(sed -n "${ID}p" ../DATA/declone_muscle_1_script.txt)
files=(`echo $line | tr ',' ' '`)
str2=".txt"

out_f="${ID}${str2}"

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s > ../EXP/DECLONE/MUSCLE_1_S/${out_f}

