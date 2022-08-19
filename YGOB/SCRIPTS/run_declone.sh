#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec
#SBATCH --array=4037-4037
#SBATCH --output=log/declone_macse_2_S_I_%a.log
#SBATCH --error=log/declone_macse_2_S_I_%a.err

ID=$((SLURM_ARRAY_TASK_ID + 9999))
#8376
line=$(sed -n "${ID}p" ../DATA/declone_macse_2_script.txt)
files=(`echo $line | tr ',' ' '`)
str2=".txt"

out_f="${ID}${str2}"

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s > ../EXP/DECLONE/MACSE_2_S/${out_f}

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -i -kT 0.1 > ../EXP/DECLONE/MACSE_2_I/${out_f}
