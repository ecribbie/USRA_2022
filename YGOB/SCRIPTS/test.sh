#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --account=def-chauvec
#SBATCH --mem=16G

python test.py
