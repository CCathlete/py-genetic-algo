from src.domain.algorithm.algo import genetic_algorithm
from src.aggregators.population import Population
import src.domain.results_processing.methods as process_results


def run() -> None:
    """Entry point to the app."""
    print("Initialising the population...\n")
    population: Population = Population()
    print("Evolution in progress...\n")
    optimised_population: Population = genetic_algorithm(
        population=population,
        generations=19000,
    )
    process_results.execute(
        optimised_population,
        process_results.Processing_method.PRINT,
    )


if __name__ == "__main__":
    run()
