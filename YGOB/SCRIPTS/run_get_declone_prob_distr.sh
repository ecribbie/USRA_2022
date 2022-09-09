#SBATCH --time=00:30:00
#SBATCH --account=def-chauvec
#SBATCH --mem=1G

python get_declone_prob_distr.py ../EXP/DECLONE/MACSE_1_I/
