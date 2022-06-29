#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec



python remove_excess_msa.py ../EXP/MACSE_NT/file_names.txt ../EXP/MACSE_NT_FIXED
