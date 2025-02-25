"""
Fitness score calculations for each individual.
"""

from src.definitions import *
from src.entities.individual import Individual


# Maximising the sum of selected categories.
def most_genes_max_in_each(individual: Individual) -> Result:
    total: Result = 0
    selected: bool = True
    # Iterating over the genes of the individual and counting the
    # number of genes that are on (categories chosen).
    for i, gene in enumerate(individual.genome):
        if gene is selected:
            category: str = CATEGORIES[i]
            total += sum(DATASET[category])

    return total
