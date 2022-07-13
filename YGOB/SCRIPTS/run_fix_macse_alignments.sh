#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec

for FILE in ../EXP/MACSE_AA/*; do sed -i 's/!/-/g' $FILE; done

for FILE in ../EXP/MACSE_NT/*; do sed -i 's/!/-/g' $FILE; done

