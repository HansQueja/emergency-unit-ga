import numpy as np
from math import sqrt

class City:
    def __init__(self, city_data):
        self.data = city_data
        self.shape = city_data.shape
        self.size = city_data.size
        
    def get_fire_frequency(self, position):
        """Get fire frequency at specified position"""
        return self.data.flat[position]
    
    def coord_of(self, pos):
        """Convert linear index to 2D coordinates"""
        # Convert from 0-based indexing to 1-based for display
        row, col = np.unravel_index(pos, self.shape)
        return row + 1, col + 1
    
    def index_from_coord(self, x, y):
        """Convert 1-based coordinates back to 0-based linear index"""
        x = max(1, min(10, x))  # Ensure within bounds
        y = max(1, min(10, y))  # Ensure within bounds
        return np.ravel_multi_index((x - 1, y - 1), self.shape)
    
    def distance_of(self, non_proposed, proposed, fire_freq=None):
        """Calculate weighted distance between two positions"""
        xn, yn = self.coord_of(non_proposed)
        xfs, yfs = self.coord_of(proposed)
        
        # If fire frequency not provided, get it from city data
        if fire_freq is None:
            fire_freq = self.get_fire_frequency(non_proposed)
        
        distance = fire_freq * sqrt((xn - xfs)**2 + (yn - yfs)**2)
        return distance
    
    def cost_of(self, proposed):
        """Calculate total cost for a proposed fire station location"""
        cost = 0.0
        
        for pos in range(self.size):
            if pos != proposed:
                fire_freq = self.get_fire_frequency(pos)
                cost += self.distance_of(pos, proposed, fire_freq)
        
        return cost
    
    def response_time_of(self, fire_station):
        """Calculate response time based on cost"""
        r = self.cost_of(fire_station)
        time = 1.7 + 3.4 * r
        return time