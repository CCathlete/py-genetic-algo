"""
Initialising the population.
"""
import random
from definitions import *

class Population:
  def __init__(self):
    self.individuals = [
      # Creating a random genome for each individual.
      Individual(
        genes=random.choices(population=[True, False], k=GENOME_LEN)
      )
      for _ in range(POPULATION_SIZE)
    ]
