"""
Fitness function definition and implementation of the genetic
algorithm.
"""

import src.domain.crossover.calculations
from src.definitions import *
from src.aggregators.population import *
import src.domain.algorithm.fitness as fitness
import src.domain.selection as selection
import src.domain.crossover as crossover
import src.domain.mutation as mutation


def genetic_algorithm(
    population: Population,
    generations: int,
) -> Population:
    """
    Implementation of simulated evolution.

    Returns:
        Population: The evolved populatino after the specified number of generations.
    """
    for generation in range(generations):
        children_pool: list[Individual] = []

        # Calculating the fitness score of each individual.
        for individual in population.individuals:
            individual.fitness_score = fitness.most_genes_max_in_each(individual)

        # Sorting the population according to the fitness score.
        # Then, reducing the population according to selection logic.
        parent_pairs: list[tuple[Individual, Individual]] = (
            selection.sort_and_pick_couples(population)
        )

        # Getting the children from each couple.
        for parent1, parent2 in parent_pairs:
            children: tuple[Individual, ...] = crossover.calculations.single_point(
                parent1, parent2
            )
            children_pool.extend(children)

        # Rebuilding the population from some of the children.
        amount_to_add: int = POPULATION_SIZE - len(population.individuals)
        joining_members: list[Individual] = random.choices(
            children_pool,
            k=amount_to_add,
        )
        population.individuals.extend(joining_members)

        # Mutating a section of the population.
        mutation.calculations.affect_population(population)

    return population
