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


def correlation_with_risk(individual: Individual) -> Result:
    """
    Integration of the risk over all values per gene over all genes.
    => Summing the effect each gene has on the risk.
    """
    total_risk: Result = 0

    for i, gene in enumerate(individual.genome):
        if gene:  # If the category is selected
            category: str = CATEGORIES[i]
            all_values_in_category: list[float] = DATASET[category]

            # Calculating the correlation of the gene with CLAIM_RISK
            # by summing the correlation of each value with
            # the CLAIM_RISK.
            correlation: Result = sum(
                value * risk for value, risk in zip(all_values_in_category, CLAIM_RISK)
            )
            total_risk += correlation

    return total_risk
