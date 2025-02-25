"""
Various methods for processing the GA results.
"""

from aggregators.population import Population
from entities.individual import Individual
from definitions import *

PROCESSING_METHOD: function
"""
Supports:\n
print_for_each_individual,\n
bar_plot
"""


def decrypt_genome(ind: Individual) -> dict[str, bool]:
    """
    Gets an individual and returns a dictionary with each category and whether it is selected or not.
    """
    return {CATEGORIES[i]: ind.genome[i] for i in range(GENOME_LEN)}


def execute(population: Population) -> None:
    """
    Wrapper for any of the processing methods. It would activate the
    method according to the configured value of PROCESSING_METHOD.
    """

    PROCESSING_METHOD(population)


def print_for_each_individual(population: Population) -> None:
    """
    Prints the fitness score for each individual.
    """
    for ind_number, individual in enumerate(population.individuals):
        print(f"Individual {ind_number + 1}:")
        print(f"{'-' * 20}")
        print(f"Fitness score: {individual.fitness_score}")
        print(f"{'-' * 20}")
        print("Decrypted genome:")
        print(f"{decrypt_genome(individual)}")
        print(f"{'-' * 20}")


def bar_plot(population: Population) -> None:
    """
    TODO
    """
    pass
