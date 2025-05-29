import random

def uniform_crossover(parents, city, population_size):
    """Perform uniform crossover between pairs of parents"""
    children = []
    
    # Process parents in pairs
    for i in range(0, len(parents), 2):
        if i + 1 < len(parents):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            
            x1, y1 = city.coord_of(parent1)
            x2, y2 = city.coord_of(parent2)
            
            # For each coordinate, randomly select from either parent
            if random.random() < 0.5:
                child_x = x1
            else:
                child_x = x2
                
            if random.random() < 0.5:
                child_y = y1
            else:
                child_y = y2
            
            # Convert back to linear index
            location = city.index_from_coord(child_x, child_y)
            
            children.append(location)
    
    return children