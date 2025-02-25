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

    # A type of dict with the categories as keys and their frequency
    # as values.
    # Has the ability count frequencies from an iterable.
    # TODO: A regular dict might suffice.
    gene_counts: Counter = Counter()

    for ind in population.individuals:
        # Tuples of (category, gene) in the individual's decrypted
        # genome.
        for category, gene in decrypt_genome(ind).items():
            if gene:  # If the category is selected.
                gene_counts[category] += 1

    # Normalisation = conversion to percentages.
    frequencies: dict[str, float] = {
        category: (count / POPULATION_SIZE) * 100
        for category, count in gene_counts.items()
    }

    # Conversion to DataFrame for plotting with seaborn.
    df_freq: pd.DataFrame = pd.DataFrame(
        frequencies.items(),
        columns=["Category", "Selection Frequency (%)"],
    )

    # Plotting.
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="Category",  # x and y axes need to be from the dataframe.
        y="Selection Frequency (%)",
        data=df_freq,
        pallete="viridis",
    )
    plt.xticks(rotation=45)
    plt.xlabel("Category")
    plt.ylabel("Selection Frequency (%)")
    plt.title("Category selection frequencies in the final population")
    # Zooming on the right part of the axis (needs to fit
    # percentages).
    plt.ylim(0, 100)
    plt.tight_layout()

    # Saving the plot.
    plt.savefig(save_path)
    print(f"Plot saved to {save_path}")


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
