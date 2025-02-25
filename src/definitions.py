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
dataset_0: dict[str, list[float]] = {
    "category_1": [1, 2, 3, 4, 5],
    "category_2": [10, 20, 30, 40, 50],
    "category_3": [100, 200, 300, 400, 500],
    "category_4": [1000, 2000, 3000, 4000, 5000],
}


# Dummy dataset with medical categories and synthetic claim risk
# scores (matrix size 50 x 7).
dataset_1: dict[str, list[float]] = {
    "age": [random.randint(20, 80) for _ in range(50)],
    "bmi": [random.uniform(18, 35) for _ in range(50)],
    "blood_pressure": [random.randint(90, 160) for _ in range(50)],
    "cholesterol": [random.randint(150, 250) for _ in range(50)],
    "smoking": [random.choice([True, False]) for _ in range(50)],
    "exercise_frequency": [random.randint(0, 7) for _ in range(50)],
    "diabetes": [random.choice([True, False]) for _ in range(50)],
}


DATASET: dict[str, list[float]] = dataset_1

# Claim risk score for each client (column in dataset).
# Our fitness function will be the sum of correlations of each gene
# with the claim risk.
# Correlation of a gene with the claim risk is the sum products of
# all possible values in that gene (category) and the claim risk.
# Vector with size 50 x 1.
# Claim risk score considering all features
CLAIM_RISK: list[float] = [
    0.3 * (age / 80)
    + 0.25 * (bmi / 35)
    + 0.15 * (blood_pressure / 160)
    + 0.1 * (cholesterol / 250)
    + 0.1 * float(smoking)  # float(True) = 1.0, float(False) = 0.0
    + 0.05 * (exercise_frequency / 7)
    + 0.2 * float(diabetes)  # float(True) = 1.0, float(False) = 0.0
    for age, bmi, blood_pressure, cholesterol, smoking, exercise_frequency, diabetes in zip(
        DATASET["age"],
        DATASET["bmi"],
        DATASET["blood_pressure"],
        DATASET["cholesterol"],
        DATASET["smoking"],
        DATASET["exercise_frequency"],
        DATASET["diabetes"],
    )
]


# We're also running on the categories (binary, either we choose the
# category or not).
CATEGORIES: list[str] = list(DATASET.keys())
GENOME_LEN: int = len(CATEGORIES)
POPULATION_SIZE: int = 20


# We need at least 2 children currently since we currently we don't
# have a condition that prevents the population from dying out and we
# discard 50% of members each generation.
constant_num_of_children: Callable[[], int] = lambda: int(2)
random_num_of_children: Callable[[], int] = lambda: random.randint(2, 5)

# The method of deciding on the number of children is constant per version of the app.
NUM_OF_CHILDREN_METHOD: Callable[[], int] = random_num_of_children
