from characters import Hero, Villain
from maps import Map
class AIAgent:
    def __init__(self, place, character):
        self.place = place
        self.character = character
    
    def get_neighbors(self, radius=1):
        neighbors = []
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                if i == 0 and j == 0:
                    continue
                
                new_i, new_j = i + new_i, new_j + j

                if 0 <= new_i < self.place.width and 0 <= new_j < self.place.height:
                    neighbors.append((new_i, new_j))
        
        return neighbors
        

    