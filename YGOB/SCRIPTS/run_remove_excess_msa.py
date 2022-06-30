#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec



python remove_excess_msa.py ../EXP/MUSCLE_AA/file_names.txt ../EXP/MUSCLE_AA_FIXED
