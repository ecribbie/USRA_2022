#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-5028
#SBATCH --output=log/iqtree_%a.log

file_AA=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../EXP/MUSCLE_AA/file_names.txt)

name=${file_AA/%.*}

iqtree -s ../EXP/MUSCLE_AA/${file_AA} -m MFP -pre ../EXP/IQTREE/${name}

#when running on NT files use -st CODON
