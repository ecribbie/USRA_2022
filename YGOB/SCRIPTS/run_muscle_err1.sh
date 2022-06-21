#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-11
#SBATCH --output=log/muscle_%a_err1.log
#SBATCH --error=log/muscle_%a_err1.err

str2=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../DATA/muscle_err1_files.txt)
str1="AA_"
str3=".fsa"
file_AA=$str1$str2$str3

muscle -in ../DATA/PILLAR_AA_FILES/${file_AA} -out ../EXP/MUSCLE_AA/${file_AA}

