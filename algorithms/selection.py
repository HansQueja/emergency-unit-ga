import random

def tournament_selection(population, city, tournament_size, num_parents):
    """Select parents using tournament selection"""
    selected_parents = []
    
    for _ in range(num_parents):
        # Randomly select tournament_size individuals
        tournament_candidates = random.sample(population, tournament_size)
        # Select the best individual from the tournament
        tournament_candidates_with_costs = [(individual, city.cost_of(individual)) for individual in tournament_candidates]
        tournament_candidates_with_costs.sort(key=lambda x: x[1])  # Sort by cost (lower is better)
        best_individual = tournament_candidates_with_costs[0][0]
        selected_parents.append(best_individual)
    
    return selected_parents