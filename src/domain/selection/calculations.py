"""
Once the population is scored, we select the fittest
individuals and randomly select parents from those.
"""

from src.definitions import *
from src.aggregators.population import *


def sort_and_pick_couples(
    population: Population,
) -> list[tuple[Individual, Individual]]:
    """
    Gets an already evaluated population, sorts by fitness score,
    keeps only the top 50% and returns a list of random couples.
    """
    pairs: list[tuple[Individual, Individual]] = []

    # Sorting the population by fitness score.
    population.individuals = sorted(
        population.individuals,
        key=lambda individual: individual.fitness_score,
        reverse=True,
    )

    even_population_size: bool = POPULATION_SIZE % 2 == 0

    # Taking into account uneven population sizes.
    num_of_selected: int = int(
        POPULATION_SIZE / 2 if even_population_size else (POPULATION_SIZE + 1) / 2
    )
    # num_of_pairs: int = num_of_selected / 2

    # Keeping only the future parents.
    population.individuals = population.individuals[:num_of_selected]

    # Pairing parents. Initial len(mating_pool) = num_of_selected.
    mating_pool: list[Individual] = population.individuals
    while len(mating_pool) > 0:
        parent1: Individual = random.choice(mating_pool)
        mating_pool.remove(parent1)
        parent2: Individual = random.choice(mating_pool)
        mating_pool.remove(parent2)

        pairs.append((parent1, parent2))

    # Returning a list of tuples of parents.
    return pairs
