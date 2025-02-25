"""
Definition of oe individual inthe population.
"""

from definitions import *


class Individual:
    def __init__(self, genes: list[Gene]) -> None:
        self.genome: list[Gene] = genes
        self.fitness_score: float = 0
