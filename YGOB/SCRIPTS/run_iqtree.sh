#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-2
#SBATCH --output=log/iqtree_%a.log

file_AA=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../EXP/MUSCLE_AA/file_names.txt)

name=${file_AA/%.*}

iqtree -s ../EXP/MUSCLE_AA/${file_AA} -pre ../EXP/IQTREE/${name}


#Not necessarily right, but will need iqtree -s <input_file> , pre is supposed to help direct output if desired.
