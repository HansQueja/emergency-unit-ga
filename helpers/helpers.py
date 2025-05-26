

def load_map():

    input_map = [
        [5, 2, 4, 8, 9, 0, 3, 3, 8, 7],
        [5, 5, 3, 4, 4, 6, 4, 1, 9, 1],
        [4, 1, 2, 1, 3, 8, 7, 8, 9, 1],
        [1, 7, 1, 6, 9, 3, 1, 9, 6, 9],
        [4, 7, 4, 9, 9, 8, 6, 5, 4, 2],
        [7, 5, 8, 2, 5, 2, 3, 9, 8, 2],
        [1, 4, 0, 6, 8, 4, 0, 1, 2, 1],
        [1, 5, 2, 1, 2, 8, 3, 3, 6, 2],
        [4, 5, 9, 6, 3, 9, 7, 6, 5, 10],
        [0, 6, 2, 8, 7, 1, 2, 1, 5, 3]
    ];

    return input_map


def coordinate_value(x, y):
    print()


def response_time(x, y, city):
    cost = cost_of(x, y, city)
    return 1.7 + 3.4 * cost


def cost_of(x, y, city): 
    total_cost = 0

    for i in range(len(city)): # Loop over all positions
        for j in range(len(city[0])):
            if i == x and j == y: # Skip the proposed location
                continue  
            fire_freq = city[i][j]
            print(f"Checking ({i}, {j}) with fire frequency: {fire_freq}")
            total_cost += distance_of(i, j, x, y, fire_freq) # Total cost

    return total_cost

def distance_of(x1, y1, x2, y2, fire_freq):
    print("Distance")