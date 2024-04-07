from dice import Dice, roll_three, evaluator
from box import Box
from creatures import Creature
from stage import Stage, Tile
from termcolor import colored
import random
import numpy as np
import math

class Ai_Agent:

    def __init__(self, stage, player):
        self.stage = stage
        self.moves = []
        self.points = {}
        self.player = player
        


    def rolling(self, dice1, dice2, dice3):
        roll_three(dice1,dice2,dice3,self.points)

    def AI_move_creature(self):
        
        available_creatures = [tile for tile in self.stage.tiles.objects if isinstance(tile.artifact, Creature) 
                            and tile.artifact.owner == self.player]
        if available_creatures:
            random.shuffle(available_creatures)

            self.pick_path(available_creatures[0])
        else:
            print(colored("Error optaining creatures to move"), "red")
    
    def path_finder(self, point_a, point_b):
        tiles_traveled = []
        tile_values = {}
        distance = distance(point_a, point_b)
        neighbors = self.get_neighbors(point_a)
        
    
    def distance(self, point1, point2):
        distance = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
        return distance
        
    def get_neighbors(self, point):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_i, new_j  = point.x + i, point.y + j
                if new_i >= 0 and new_i < self.stage.height and new_j >= 0 and new_j < self.stage.width:
                    neighbors.append((new_i,new_j))
        return neighbors
    
                
                
        

            
        


