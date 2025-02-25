"""
Fitness function definition and implementation of the genetic
algorithm.
"""

from definitions import *
from aggregators.population import *
import fitness


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
        for individual in population.individuals:
            individual.fitness_score = fitness.most_genes_max_in_each(individual)

    return population
