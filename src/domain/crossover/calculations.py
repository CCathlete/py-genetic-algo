""""""

import random
from src.definitions import *
from src.entities.individual import Individual


def single_point(
    parent1: Individual,
    parent2: Individual,
) -> tuple[Individual, ...]:
    """Single point crossover.
    The number of children is determined by NUM_OF_CHILDREN_METHOD,
    if the method is random decision, the number of children would
    change each crossover.

    Returns:
        tuple[Individual, ...]: Varying number of children.
    """
    num_of_children: int = NUM_OF_CHILDREN_METHOD()

    # We need to take genes from both sides of the crossover point
    # so we can't have the point in index 0 or len - 1.
    def give_birth() -> Individual:
        crossover_point: int = random.randint(1, GENOME_LEN - 2)
        child: Individual = Individual(
            parent1.genome[:crossover_point] + parent2.genome[crossover_point:]
        )
        return child

    children: list[Individual] = [give_birth() for _ in range(num_of_children)]

    return tuple(children)
