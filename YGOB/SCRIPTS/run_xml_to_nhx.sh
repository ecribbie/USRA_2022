#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec

python ../../RECPHYLOXML_TO_NHX/recphyloxml_to_nhx.py ../EXP/GENERAX/MUSCLE_PARALLEL/1/reconciliations/ ../DATA/GENERAX_INTO_NHX_MUSCLE_1

