"""
General definitions of types, constants, data set.
"""

import random
from typing import Union, Callable
from typing_extensions import TypeAlias

Result: TypeAlias = Union[int, float]
# Each gene represents a category, it's true if the gene is on and
# false if it's off i.e. the category was not chosen.
Gene: TypeAlias = bool


# Dummy dataset.
DATASET: dict[str, list[float]] = {
    "category_1": [1, 2, 3, 4, 5],
    "category_2": [10, 20, 30, 40, 50],
    "category_3": [100, 200, 300, 400, 500],
    "category_4": [1000, 2000, 3000, 4000, 5000],
}

# We're also running on the categories (binary, either we choose the
# category or not).
CATEGORIES: list[str] = list(DATASET.keys())
GENOME_LEN: int = len(CATEGORIES)
POPULATION_SIZE: int = 20


constant_num_of_children: Callable[[], int] = lambda: int(2)
random_num_of_children: Callable[[], int] = lambda: random.randint(0, 5)

# The method of deciding on the number of children is constant per version of the app.
NUM_OF_CHILDREN_METHOD: Callable[[], int] = random_num_of_children
