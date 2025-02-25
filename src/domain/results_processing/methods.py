"""
Various methods for processing the GA results.
"""

from enum import Enum
from src.aggregators.population import Population
from src.entities.individual import Individual
from src.definitions import *
from collections import Counter
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


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
        print(
            f"Individual {ind_number + 1}:\n",
            f"{'-' * 20}\n",
            f"Fitness score:\n",
            f"{individual.fitness_score}\n",
            f"{'-' * 20}\n",
            "Decrypted genome:\n",
            f"{decrypt_genome(individual)}\n",
            f"{'-' * 20}\n",
            f"{'-' * 20}\n",
        )


def bar_plot(
    population: Population,
    save_path: str = "gene_frequencies.png",
) -> None:
    """
    Gets a population and plots a bar plot of gene expression levels
    (enrichment).\n
    """

    gene_counter:


class Processing_method(Enum):
    """
    Supports:\n
    print_for_each_individual,\n
    bar_plot
    """

    PRINT = print_for_each_individual
    BAR_PLOT = bar_plot


def execute(population: Population, method: Processing_method) -> None:
    """
    Wrapper for any of the processing methods. It would activate the
    method according to the configured value of PROCESSING_METHOD.
    """

    method(population)
