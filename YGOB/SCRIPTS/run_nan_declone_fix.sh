#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-641
#SBATCH --mem=2G
#SBATCH --output=log/declone_macse_1_I_nan_fix_%a.log
#SBATCH --error=log/declone_macse_1_I_nan_fix_%a.err

nan_file=$(sed -n "${SLURM_ARRAY_TASK_ID}p" nan_files.txt)
ID_txt="$(echo $nan_file | cut -d'/' -f5)"
ID="$(echo $ID_txt | cut -d'.' -f1)"
line=$(sed -n "${ID}p" ../DATA/declone_macse_1_script.txt)
files=(`echo $line | tr ',' ' '`)
str2=".txt"

out_f="${ID}${str2}"

#../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s -v > ../EXP/DECLONE/MACSE_1_S/${out_f}

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -i -kT 0.1 -v > ../EXP/DECLONE/MACSE_1_I/${out_f}
