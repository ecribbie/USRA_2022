for FILE in ../EXP/GENERAX/MUSCLE_top_10/1/reconciliations/*; do sed -i 's/node/node_/g' $FILE; done
sed -i 's/node/node_/g' ../EXP/GENERAX/MUSCLE_top_10/1/species_trees/inferred_species_tree.newick
