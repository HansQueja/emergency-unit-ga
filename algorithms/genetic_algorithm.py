import random
import pandas as pd
import matplotlib.pyplot as plt

from config import POPULATION_SIZE, GENERATIONS, TOURNAMENT_SIZE, NUM_PARENTS, MUTATION_RATE, SIGMA
from data.city_data import load_locations
from models.city import City
from algorithms.selection import tournament_selection
from algorithms.crossover import uniform_crossover
from algorithms.mutation import gaussian_mutate

def init_population(city, population_size):
    """Initialize population with random locations"""
    # Generate random permutation of all possible locations (0 to 99)
    population = list(range(city.size))
    random.shuffle(population)
    return population[:population_size]

def run_genetic_algorithm():
    """Execute the genetic algorithm to find optimal emergency unit location"""
    # Load city data
    city_data = load_locations()
    city = City(city_data)
    
    # Initialize population and tracking variables
    population = init_population(city, POPULATION_SIZE)
    init_value = population[0]
    
    gens = [0]
    costs = [city.cost_of(init_value)]
    x, y = city.coord_of(init_value)
    coords = [f'({x}, {y})']
    time = [f'{city.response_time_of(init_value):.6f} min']
    xs = [x]
    ys = [y]
    
    print(f'Initial Coordinates: ({x}, {y})')
    print(f'Initial Cost: {city.cost_of(population[0]):.6f}')
    print('[', end='')
    
    # Set up the plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    plt.ion()  # Turn on interactive mode
    
    for generation in range(1, GENERATIONS + 1):
        # Use tournament selection
        parents = tournament_selection(population, city, TOURNAMENT_SIZE, NUM_PARENTS)
        
        # Use uniform crossover
        children = uniform_crossover(parents, city, POPULATION_SIZE)
        
        # Use Gaussian mutation
        children = gaussian_mutate(children, city, MUTATION_RATE, SIGMA)
        
        # Combine children, parents, and evaluate
        new_population = children + parents
        new_population_with_costs = [(individual, city.cost_of(individual)) for individual in new_population]
        new_population_with_costs.sort(key=lambda x: x[1])
        population = [individual for individual, _ in new_population_with_costs[:POPULATION_SIZE]]
        
        # Get best solution in this generation
        loc_of_best = population[0]
        cost_of_best = city.cost_of(loc_of_best)
        x, y = city.coord_of(loc_of_best)
        response_time_of_best = city.response_time_of(loc_of_best)
        
        print('=', end='')
        
        # Update tracking variables
        gens.append(generation)
        costs.append(cost_of_best)
        coords.append(f'({x}, {y})')
        time.append(f'{response_time_of_best:.6f} min')
        xs.append(x)
        ys.append(y)
        
        # Update plots
        ax1.clear()
        ax1.scatter(xs, ys, c='blue', alpha=0.6)
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 10)
        ax1.set_xticks(range(11))
        ax1.set_yticks(range(11))
        ax1.grid(True)
        ax1.set_title('Emergency Unit Locations Over Generations')
        ax1.set_xlabel('X Coordinate')
        ax1.set_ylabel('Y Coordinate')
        
        ax2.clear()
        ax2.scatter(gens, costs, c='blue', alpha=0.6)
        ax2.plot(gens, costs, 'r-', alpha=0.7)
        ax2.set_xlabel('Generations')
        ax2.set_ylabel('Cost Value')
        ax2.set_title('Cost Value Per Generation (100 Generations)')
        ax2.grid(True)
        
        plt.pause(0.01)  # Small pause to update the plot
    
    print(']')
    
    # Create results dataframe
    results_df = pd.DataFrame({
        'Generations': gens,
        'ProposedCoordinates': coords,
        'CostValue': costs,
        'ResponseTime': time
    })
    
    # Get final best solution
    best_location = population[0]
    best_cost = city.cost_of(best_location)
    best_coords = city.coord_of(best_location)
    
    plt.ioff()  # Turn off interactive mode
    
    return results_df, best_location, best_cost, best_coords