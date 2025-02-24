import random
from typing import Optional, Union
from typing_extensions import TypeAlias

Result: TypeAlias = Union[int, float]
# Each gene represents a category, it's true if the gene is on and
# false if it's off i.e. the category was not chosen.
Gene: TypeAlias =  bool

class Individual:
  def __init__(self, genes: list[Gene]) -> None:
    self.genome = genes


# Dummy dataset.
dataset: dict[str, list[int]] = {
  "category_1": [1, 2, 3, 4, 5],
  "category_2": [10, 20, 30, 40, 50],
  "category_3": [100, 200, 300, 400, 500],
  "category_4": [1000, 2000, 3000, 4000, 5000],
}

# We're also running on the categories (binary, either we choose the
# category or not).
CATEGORIES: list[str] = list(dataset.keys())
GENOME_LEN: int = len(CATEGORIES)


# Fitness function - maximising the sum of selected categories.
def fitness(individual: Individual) -> Result:
  total: Result = 0
  selected: bool = True
  # Iterating over the genes of the individual and counting the
  # number of genes that are on (categories chosen).
  for i, gene in enumerate(individual.genome):
    if gene is selected:
      category: str = CATEGORIES[i]
      total += sum(dataset[category])

  return total