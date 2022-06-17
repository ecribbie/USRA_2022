#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-5028
#SBATCH --output=log/muscle_%a.log
#SBATCH --error=log/muscle_%a.err

file_AA=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../DATA/PILLAR_AA_FILES/file_names.txt)


muscle -in ../DATA/PILLAR_AA_FILES/${file_AA} -out ../EXP/MUSCLE_AA/${file_AA}

