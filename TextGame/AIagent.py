from characters import Hero, Villain
from maps import Map
from collections import defaultdict
from skills import Skills
from item import Item\
from interactions import *
class AIAgent:
    def __init__(self, place, character):
        self.place = place
        self.character = character
        self.moves_made = []

    def location(self):
        character_location = [(tile.tile, obj) for tile in self.place.tiles.values() for obj in tile.objects if isinstance(obj, Hero) 
                              or isinstance(obj, Villain) if obj.name == self.character.name]
        
        if character_location:
            return character_location[0]
        else:
            return None

    
    def get_neighbors(self, x, y, radius=1):
        neighbors = []

        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                if i == 0 and j == 0:
                    continue
                
                new_i, new_j = i + x, j + y

                if new_i >= 0 and new_i <= self.place.height - 1 and new_j >= 0 and new_j <= self.place.width - 1:
                    neighbors.append((new_i, new_j))
        
        return neighbors
    
    def evaluate_neighbors(self, neighbors):
        neighbor_values = defaultdict(list)

        for nx, ny in neighbors:
            if self.place.tiles[(nx,ny)].objects:
                for obj in self.place.tiles[(nx, ny)].objects:
                    if isinstance(obj, Hero) or isinstance(obj, Villain):
                        if obj.nature != self.character.nature:
                            neighbor_values[4].append((nx,ny))
                        else:
                            neighbor_values[0].append((nx,ny))
                    elif "Blocked" in self.place.tiles[(nx,ny)].objects:
                        neighbor_values[0].append((nx,ny))
                    elif isinstance(obj, Item) or isinstance(obj, Skills):
                        neighbor_values[3].append((nx, ny))
            elif (nx,ny) in self.moves_made:
                neighbor_values[1].append((nx,ny))
            else:
                neighbor_values[2].append((nx,ny))

        return neighbor_values

    def move_score(self, sorted_value, neighbor_values):
        move_score = {}
        for value in sorted_value:
            if neighbor_values[value]:
                nx, ny = neighbor_values[value][0]
                
                move_score[(nx,ny)] = value
        return move_score
                

        
    def pick_move(self):
        start = self.location()

        if start:
            coords, player = start
            x, y = coords 
            if (x,y) not in self.moves_made:
                self.moves_made.append((x,y))
            
            best_move = []
            next_move = {}

            neighbors = self.get_neighbors(x,y)

            neighbor_values = self.evaluate_neighbors(neighbors)

            sorted_values = sorted(neighbor_values.keys(), reverse=True)

            move_score = self.move_score(sorted_values, neighbor_values)

            for move in move_score.keys():
                move_x, move_y = move
                move_neighbors = self.get_neighbors(move_x, move_y)

                move_neighbors_values = self.evaluate_neighbors(move_neighbors)

                move_sorted_values = sorted(move_neighbors_values.keys(), reverse=True)

                future_move_score = self.move_score(move_sorted_values, move_neighbors_values)
                
                for move2 in future_move_score.keys():
                    if (move, move2) not in next_move:
                        next_move[(move,move2)] = 0
                    next_move[(move, move2)] += move_score[move] + future_move_score[move2]
            
            sorted_best_move = sorted(next_move.values(), reverse=True)

            for move, move2 in sorted_best_move[0]:
                new_x, new_y = move

                best_move.append((new_x, new_y))
        return best_move 

    def make_move(self):
        start = self.pick_move()
        if start:
            location = self.location()
            coords, player = location

            territory = self.place.tiles[(start[0], start[1])].object

            if isinstance(territory, Item) or isinstance(territory,Skills):
                self.place.tiles[(start[0],start[1])].remove(territory)
                pick_up_item(self.place, self.character, start[0], start[1])

                
            elif isinstance(territory,Hero) or isinstance(territory, Villain):
                damage = 0
                if self.character.agi >= territory.agi:
                    if self.character.str >= self.character.int:
                        damage = melee_attack(self.character, territory)
                    else:
                        damage = magical_attack(self.character, territory)
                    
                    territory.hp -= damage
                    
                    if territory.hp <= 0:
                        killed(self.place, self.character, territory, coords, start)
                    else:
                        self.character.exp += 3
                    
                    if territory.str >= territory.int:
                        damage = melee_attack(territory, self.character)
                    else:
                        damage = magical_attack(territory, self.character)
                    
                    self.character.hp -= damage

                    if self.character.hp <= 0:
                        killed(self.place, self.character, territory, coords, start)
                    
                    
                    
                    

                else:
                    if territory.str >= territory.int:
                        damage = melee_attack(territory, self.character)
                    else:
                        damage = magical_attack(territory, self.character)
                    
                    self.character.hp -= damage

                    if self.character.hp <= 0:
                        killed(self.place, self.character, territory, coords, start)
                    
                    if self.character.str >= self.character.int:
                        damage = melee_attack(self.character, territory)
                    else:
                        damage = magical_attack(self.character, territory)
                    
                    territory.hp -= damage
                    
                    if territory.hp <= 0:
                        killed(self.place, self.character, territory, coords, start)
                    else:
                        self.character.exp += 3
                    

                        

                    


                    


            


        
            



        
    