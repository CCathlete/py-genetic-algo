"""
Initialising the population.
"""

import random
from src.definitions import *
from src.entities.individual import Individual


class Population:
    """
    A data structure that groups all of the individuals in the
    population.
    """

    def __init__(self):
        self.individuals: list[Individual] = [
            # Creating a random genome for each individual.
            Individual(genes=random.choices(population=[True, False], k=GENOME_LEN))
            for _ in range(POPULATION_SIZE)
        ]
