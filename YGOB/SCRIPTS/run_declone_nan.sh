#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-641
#SBATCH --mem=1G
#SBATCH --output=log/declone_macse_1_I_nan_%a.log
#SBATCH --error=log/declone_macse_1_I_nan_%a.err

ID=$((SLURM_ARRAY_TASK_ID))
nan_line=$(sed -n "${ID}p" nan_files.txt)
nan_line_arr=(`echo $nan_line | tr '/' ' '`)
nan_line_end_arr=(`echo ${nan_line_arr[-1]} | tr '.' ' '`)
file_num=$((${nan_line_end_arr[0]}))
line=$(sed -n "${file_num}p" ../DATA/declone_macse_1_script.txt)
files=(`echo $line | tr ',' ' '`)
str2=".txt"
out_f="${file_num}${str2}"

#../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s -v > ../EXP/DECLONE/MACSE_1_S/${out_f}
combined_trees=`python create_gene_tree_matching_root.py ${files[0]} ${files[1]}`
tree_arr=(`echo $combined_trees | tr '~' ' '`)
tree1=${tree_arr[0]}
tree2=${tree_arr[1]}

#../../../TOOLS/DeClone/DeClone -t1 ${files[0]} -t2 ${files[1]} -a ${files[2]} -s -v > ../EXP/DECLONE/MACSE_1_S/${out_f}

../../../TOOLS/DeClone/DeClone -t1 ${tree1} -t2 ${tree2} -a ${files[2]} -i -kT 0.1 -v > ../EXP/DECLONE/MACSE_1_I/${out_f}



