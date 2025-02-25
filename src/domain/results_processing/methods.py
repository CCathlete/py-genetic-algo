"""
Various methods for processing the GA results.
"""

from enum import Enum
from aggregators.population import Population
from entities.individual import Individual
from definitions import *


def decrypt_genome(ind: Individual) -> dict[str, bool]:
    """
    Gets an individual and returns a dictionary with each category and whether it is selected or not.
    """
    return {CATEGORIES[i]: ind.genome[i] for i in range(GENOME_LEN)}


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
    Gets a population and plots a bar plot of gene expression levels
    (enrichment).\n
    TODO
    """
    pass


class Processing_method(Enum, function):
    """
    Supports:\n
    print_for_each_individual,\n
    bar_plot
    """

    PRINT: function = print_for_each_individual
    BAR_PLOT: function = bar_plot


def execute(population: Population, method: Processing_method) -> None:
    """
    Wrapper for any of the processing methods. It would activate the
    method according to the configured value of PROCESSING_METHOD.
    """

    method(population)
