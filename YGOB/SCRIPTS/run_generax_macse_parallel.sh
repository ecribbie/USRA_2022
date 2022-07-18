#!/bin/bash
#SBATCH --time=05:00:00
#SBATCH --account=def-chauvec
#SBATCH --ntasks=50
#SBATCH --output=log/generax_macse_parallel_%a.log
#SBATCH --array=1-4

mod=$(( $SLURM_ARRAY_TASK_ID % 2 ))

if [ $mod -eq "0" ]
then
        seed=123
else
        seed=321
fi


strat="SPR"


if [ ${SLURM_ARRAY_TASK_ID} -eq "1" ] || [ ${SLURM_ARRAY_TASK_ID} -eq "2" ] || [ ${SLURM_ARRAY_TASK_ID} -eq "5" ] || [ ${SLURM_ARRAY_TASK_ID} -eq "6" ]
then
        model="UndatedDL"
else
        model="UndatedDTL"
fi


echo "$seed"
echo "$strat"
echo "$model"

mpiexec -np 50 ../../../TOOLS/GeneRax/build/bin/generax -f ../DATA/generax_made_macse_family_file.txt -s ../DATA/species_tree.tree -p ../EXP/GENERAX/MACSE_PARALLEL/$SLURM_ARRAY_TASK_ID --per-family-rates --seed ${seed} --rec-model ${model} --strategy ${strat}

