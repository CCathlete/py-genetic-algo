from src.domain.algorithm.algo import genetic_algorithm
from src.aggregators.population import Population


def run() -> None:
    """Entry point to the app."""
    print("Initialising the population...\n")
    population: Population = Population()
    print("Evolution in progress...\n")
    optimised_population: Population = genetic_algorithm(
        population=population,
        generations=100,
    )


if __name__ == "__main__":
    run()
