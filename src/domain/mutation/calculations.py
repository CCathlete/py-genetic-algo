"""
Methods for mutation of genes.
"""

import random
from src.definitions import *
from src.entities.individual import Individual
from src.aggregators.population import Population


def flip_random_gene(ind: Individual) -> None:
    """
    Random flip Mutation of one gene (in place).
    """
    index: int = random.randint(0, GENOME_LEN - 1)
    ind.genome[index] = not ind.genome[index]


MUTATION_METHOD: Callable[[Individual], None] = flip_random_gene


def affect_population(population: Population) -> None:
    """
    Chooses random population members and mutates them (in place).
    """
    # 30 - 50% of the population might be affected.
    num_of_affected: int = random.randint(
        int(0.3 * POPULATION_SIZE),
        int(0.5 * POPULATION_SIZE),
    )

    # Choosing random population members.
    # NOTE: since Individual is a class, random.choices returns
    # references so changes are in place.
    affected_individuals: list[Individual] = random.choices(
        population.individuals,
        k=num_of_affected,
    )

    # Mutating in place.
    for individual in affected_individuals:
        MUTATION_METHOD(individual)
