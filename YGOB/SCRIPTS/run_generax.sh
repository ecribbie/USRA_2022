#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec
#SBATCH --output=log/generax_%a.log

mpiexec -f ../DATA/generax_family_file.txt -s ../DATA/species_tree.txt -p ../EXP/GENERAX/

