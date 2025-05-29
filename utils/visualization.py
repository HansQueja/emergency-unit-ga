import matplotlib.pyplot as plt

def visualize_results(results_df):
    """Display the final results in a formatted table"""
    print("\nResults:")
    
    # Get data lists from DataFrame
    gens = results_df['Generations'].tolist()
    coords = results_df['ProposedCoordinates'].tolist()
    costs = results_df['CostValue'].tolist()
    time = results_df['ResponseTime'].tolist()

    # Get column widths (with some padding)
    gen_width = max(12, max(len(str(g)) for g in gens) + 2)
    coord_width = max(20, max(len(c) for c in coords) + 2)
    cost_width = max(12, max(len(f"{c:.6f}") for c in costs) + 2)
    time_width = max(15, max(len(t) for t in time) + 2)
    
    # Create header and separator
    header = f"| {'Generation'.center(gen_width)} | {'Coordinates'.center(coord_width)} | {'Cost'.center(cost_width)} | {'Response Time'.center(time_width)} |"
    separator = f"+-{'-' * gen_width}-+-{'-' * coord_width}-+-{'-' * cost_width}-+-{'-' * time_width}-+"
    
    # Print the table
    print(separator)
    print(header)
    print(separator)
    
    # Print data rows
    for i in range(len(gens)):
        gen = str(gens[i]).center(gen_width)
        coord = coords[i].center(coord_width)
        cost = f"{costs[i]:.6f}".center(cost_width)
        resp_time = time[i].center(time_width)
        print(f"| {gen} | {coord} | {cost} | {resp_time} |")
    
    print(separator)
    
    plt.show()  # Show the final plots