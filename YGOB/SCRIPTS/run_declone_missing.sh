#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-148
#SBATCH --mem=1G
#SBATCH --output=log/declone_macse_1_S_I_missing_2_%a.log
#SBATCH --error=log/declone_macse_1_S_I_missing_2%a.err

ID1=$(sed -n "${SLURM_ARRAY_TASK_ID}p" declone_missing_macse_2.txt)
ID=$((ID1 + 9999))
line=$(sed -n "${ID}p" ../DATA/declone_macse_1_script.txt)
files=(`echo $line | tr ',' ' '`)
str2=".txt"

out_f="${ID}${str2}"

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s > ../EXP/DECLONE/MACSE_1_S/${out_f}

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -i -kT 0.1 > ../EXP/DECLONE/MACSE_1_I/${out_f}
