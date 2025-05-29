def normalize_cost(cost, min_cost, max_cost):
    """Normalize cost to a 0-1 scale for visualization"""
    if max_cost == min_cost:
        return 0
    return (cost - min_cost) / (max_cost - min_cost)

def calculate_improvement(initial_cost, final_cost):
    """Calculate percentage improvement"""
    return ((initial_cost - final_cost) / initial_cost) * 100