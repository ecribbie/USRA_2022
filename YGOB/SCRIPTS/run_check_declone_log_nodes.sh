#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec

python check_declone_log_nodes.py declone_macse_1_I_files.txt

