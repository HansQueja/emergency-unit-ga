import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from math import sqrt

from config import POPULATION_SIZE, GENERATIONS, TOURNAMENT_SIZE, NUM_PARENTS, MUTATION_RATE, SIGMA
from data.city_data import load_locations
from algorithms.genetic_algorithm import run_genetic_algorithm
from utils.visualization import visualize_results

def main():
    # Run the genetic algorithm
    results_df, best_location, best_cost, best_coords = run_genetic_algorithm()
    
    # Visualize the results
    visualize_results(results_df)
    
    print(f"\nFinal Best Location: Coordinates {best_coords}")
    print(f"Final Best Cost: {best_cost:.6f}")
    
    return results_df

if __name__ == "__main__":
    results = main()