#!/bin/bash
#SBATCH --time=00:45:00
#SBATCH --account=def-chauvec

python ../../RECPHYLOXML_TO_NHX/recphyloxml_to_nhx.py ../EXP/GENERAX/MACSE_PARALLEL/1/reconciliations/ ../DATA/GENERAX_INTO_NHX_MACSE_1

python ../../RECPHYLOXML_TO_NHX/recphyloxml_to_nhx.py ../EXP/GENERAX/MACSE_PARALLEL/2/reconciliations/ ../DATA/GENERAX_INTO_NHX_MACSE_2
