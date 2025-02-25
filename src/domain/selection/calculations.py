"""
Once the population is scored, we select the fittest
individuals and randomly select parents from those.
"""

from definitions import *
from aggregators.population import *


def sort_and_pick_couples(
    population: Population,
) -> list[tuple[Individual, Individual]]:
    """
    Gets an already evaluated population, sorts by fitness score and returns a list of couples from the most fit ones.
    """
    # Sorting the population by fitness score.
    population.individuals = sorted(
        population.individuals,
        key=lambda individual: individual.fitness_score,
        reverse=True,
    )

    even_population_size: bool = POPULATION_SIZE % 2 == 0

    # Taking into account uneven population sizes.
    num_of_selected: int = (
        POPULATION_SIZE / 2 if even_population_size else (POPULATION_SIZE + 1) / 2
    )
    num_of_pairs: int = num_of_selected / 2

    # Keeping only the future parents.
    population.individuals = population.individuals[:num_of_selected]

    # Returning a list of tuples of parents.
    # TODO: Add num of children to reach initial pop size.

    return [tuple(random.choices(population=population.individuals, k=2))]
