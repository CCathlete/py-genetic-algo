"""
Fitness function definition and implementation of the genetic
algorithm.
"""
from definitions import *

# Fitness function - maximising the sum of selected categories.
def fitness(individual: Individual) -> Result:
  total: Result = 0
  selected: bool = True
  # Iterating over the genes of the individual and counting the
  # number of genes that are on (categories chosen).
  for i, gene in enumerate(individual.genome):
    if gene is selected:
      category: str = CATEGORIES[i]
      total += sum(DATASET[category])

  return total