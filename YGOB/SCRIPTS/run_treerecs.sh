#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --account=def-chauvec
#SBATCH --array=1-2
#SBATCH --output=log/treerecs_%a.log

file_newick=$(sed -n "${SLURM_ARRAY_TASK_ID}p" ../EXP/IQTREE/newick_files.txt)



../../../TOOLS/Treerecs/bin/treerecs -g ../EXP/IQTREE/${file_newick} -s ../EXP/IQTREE/${file_newick} -S ../DATA/gene_species_mapping_output.txt -o ../EXP/TREERECS
