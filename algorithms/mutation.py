import random

def gaussian_mutate(children, city, mutation_rate, sigma=1.0):
    """Apply Gaussian mutation to children"""
    
    for i in range(len(children)):
        if random.random() < mutation_rate:
            x, y = city.coord_of(children[i])
            
            # Add Gaussian noise to coordinates
            x_offset = int(round(random.gauss(0, sigma)))
            y_offset = int(round(random.gauss(0, sigma)))
            
            new_x = max(1, min(10, x + x_offset))  # Ensure within bounds
            new_y = max(1, min(10, y + y_offset))  # Ensure within bounds
            
            # Convert back to linear index
            children[i] = city.index_from_coord(new_x, new_y)
    
    return children