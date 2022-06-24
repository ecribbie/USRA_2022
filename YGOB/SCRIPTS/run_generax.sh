#!/bin/bash
#SBATCH --time=03:00:00
#SBATCH --account=def-chauvec
#SBATCH --output=log/generax_%a.log
#SBATCH --array=1-8

mod=$(( $SLURM_ARRAY_TASK_ID % 2 ))

if [$mod -eq 0]
then
	seed=123
else
	seed=321
fi


if [${SLURM_ARRAY_TASK_ID} -gt 4]
then
	strat="EVAL"
else
	strat="SPR"
fi


if [${SLURM_ARRAY_TASK_ID} -eq 1] || [${SLURM_ARRAY_TASK_ID} -eq 2] || [${SLURM_ARRAY_TASK_ID} -eq 5] || [${SLURM_ARRAY_TASK_ID} -eq 6]
then
	model="UndatedDL"
else
	model="undatedDTL"
fi


echo "$seed"
echo "$strat"
echo "$model"

mpiexec --families ../DATA/generax_muscle_file.txt -s ../DATA/species_tree.txt -p ../EXP/GENERAX/ --per-family-rates --seed ${seed} --rec-model ${model} --strategy ${strat}
