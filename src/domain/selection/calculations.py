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

    # Keeping only the 50% most fit to be future parents.
    population.individuals = population.individuals[:num_of_selected]

    # Pairing parents. Initial len(mating_pool) = num_of_selected.
    mating_pool: list[Individual] = population.individuals.copy()
    while len(mating_pool) > 0:
        parent1: Individual = random.choice(mating_pool)
        mating_pool.remove(parent1)
        parent2: Individual = random.choice(mating_pool)
        mating_pool.remove(parent2)

        pairs.append((parent1, parent2))

    # Returning a list of tuples of parents.
    return pairs


def tournament_selection(
    population: Population, tournament_size: int = 3
) -> list[tuple[Individual, Individual]]:
    """
    Tournament selection for genetic diversity.
    Tournament = We're taking 3 random individuals and selecting the
    fittest.
    """
    pairs: list[tuple[Individual, Individual]] = []
    selected: list[Individual] = []

    even_population_size: bool = POPULATION_SIZE % 2 == 0

    # Taking into account uneven population sizes.
    num_of_selections: int = int(
        POPULATION_SIZE / 2 if even_population_size else (POPULATION_SIZE + 1) / 2
    )

    while len(selected) < num_of_selections:
        tournament: list[Individual] = random.sample(
            population.individuals, tournament_size
        )
        winner: Individual = max(tournament, key=lambda ind: ind.fitness_score)
        selected.append(winner)

    mating_pool: list[Individual] = selected.copy()
    # Since we're taking pairs, while >= 2 and while > 0 is the same.
    while len(mating_pool) >= 2:
        parent1, parent2 = random.sample(mating_pool, 2)
        mating_pool.remove(parent1)
        mating_pool.remove(parent2)
        pairs.append((parent1, parent2))

    return pairs
