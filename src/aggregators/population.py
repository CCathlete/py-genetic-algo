"""
Initialising the population.
"""

import random
from definitions import *
from entities.individual import Individual
from dataclasses import dataclass


@dataclass
class Population:
    """
    A data structure that groups all of the individuals in the
    population.
    """

    individuals = [
        # Creating a random genome for each individual.
        Individual(genes=random.choices(population=[True, False], k=GENOME_LEN))
        for _ in range(POPULATION_SIZE)
    ]
