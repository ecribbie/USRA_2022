#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-656
#SBATCH --mem=1G
#SBATCH --output=log/declone_macse_1_I_3_%a.log
#SBATCH --error=log/declone_macse_1_I_3_%a.err

#Last goes to 656
ID=$((SLURM_ARRAY_TASK_ID + 19998))
#add 9999 then 19998
line=$(sed -n "${ID}p" ../DATA/declone_macse_1_script.txt)
files=(`echo $line | tr ',' ' '`)
str2=".txt"

out_f="${ID}${str2}"

#../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s -v > ../EXP/DECLONE/MACSE_1_S/${out_f}

../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -i -kT 0.1 -v > ../EXP/DECLONE/MACSE_1_I/${out_f}
