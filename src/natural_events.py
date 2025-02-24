"""
Selection, Crossover and Mutation.
"""

from definitions import *
from population import *


def select(population: Population) -> tuple[Individual, ...]:
    """
    Tournament selection process.
    """
    return tuple(random.choices(population=population.individuals, k=2))


def crossover(
    parent1: Individual,
    parent2: Individual,
) -> tuple[Individual, Individual]:
    """Single point crossover.

    Returns:
        tuple[Individual, Individual]: Two children.
    """
    # We need to take genes from both sides of the crossover point
    # so we can't have the point in index 0 or len - 1.
    crossover_point: int = random.randint(1, GENOME_LEN - 2)
    child1: Individual = Individual(
        parent1.genome[:crossover_point] + parent2.genome[crossover_point:]
    )
    child2: Individual = Individual(
        parent2.genome[:crossover_point] + parent1.genome[crossover_point:]
    )

    return child1, child2


def mutate(ind: Individual) -> Individual:
    """
    Random flip Mutation of one gene.
    """
    index: int = random.randint(0, GENOME_LEN - 1)
    ind.genome[index] = not ind.genome[index]
    return ind
