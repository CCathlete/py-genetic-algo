""""""

import random
from definitions import *
from entities.individual import Individual


def mutate(ind: Individual) -> Individual:
    """
    Random flip Mutation of one gene.
    """
    index: int = random.randint(0, GENOME_LEN - 1)
    ind.genome[index] = not ind.genome[index]
    return ind
