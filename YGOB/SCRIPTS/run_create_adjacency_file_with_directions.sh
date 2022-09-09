#!/bin/bash
#SBATCH --time=00:20:00
#SBATCH --account=def-chauvec

module load python/3.10
python create_adjacency_file_with_directions.py ../DATA/AA_genes.txt ../DATA/adjacency_with_dir.txt ../DATA/species_genome_tabs/Cglabrata_genome.txt ../DATA/species_genome_tabs/Ecymbalariae_genome.txt ../DATA/species_genome_tabs/Egossypii_genome.txt ../DATA/species_genome_tabs/Kafricana_genome.txt ../DATA/species_genome_tabs/Klactis_genome.txt ../DATA/species_genome_tabs/Knaganishii_genome.txt ../DATA/species_genome_tabs/Lkluyveri_genome.txt ../DATA/species_genome_tabs/Lthermotolerans_genome.txt ../DATA/species_genome_tabs/Ncastellii_genome.txt ../DATA/species_genome_tabs/Ndairenensis_genome.txt ../DATA/species_genome_tabs/Scerevisiae_genome.txt ../DATA/species_genome_tabs/Tblattae_genome.txt ../DATA/species_genome_tabs/Tdelbrueckii_genome.txt ../DATA/species_genome_tabs/Tphaffii_genome.txt ../DATA/species_genome_tabs/Zrouxii_genome.txt
