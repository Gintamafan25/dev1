from characters import Hero, Villain
from maps import Map
from collections import defaultdict
from skills import Skills
from item import Item
from interactions import *
import copy
import math
import numpy as np
from termcolor import colored
class AIAgent:
    def __init__(self, place, character, heroes, villains):
        self.place = place
        self.character = character
        self.moves_made = []
        self.heroes = heroes
        self.villains = villains

    def location(self):
        for tile in self.place.tiles.values():
            if self.character in tile.objects:
                return (tile.tile, self.character)

    
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
    
    def evaluate_neighbors(self, neighbors, moves_made, hero, vil):
        neighbor_values = defaultdict(list)

        for nx, ny in neighbors:
            if self.place.tiles[(nx,ny)].objects:
                for obj in self.place.tiles[(nx, ny)].objects:
                    if isinstance(obj, Hero) or isinstance(obj, Villain):
                        if obj.nature != self.character.nature:
                            neighbor_values[4].append((nx,ny))
                        else:
                            neighbor_values[-2].append((nx,ny))
                        
                    elif "Blocked" in self.place.tiles[(nx,ny)].objects:
                        neighbor_values[-2].append((nx,ny))
                    elif isinstance(obj, Item) or isinstance(obj, Skills):
                        neighbor_values[3].append((nx, ny))
                    
            elif (nx,ny) in moves_made:
                neighbor_values[0].append((nx,ny))
            elif self.character.nature == "Hero" and (nx,ny) in hero:
                neighbor_values[1].append((nx,ny))
            elif self.character.nature == "Villain" and (nx,ny) in vil:
                neighbor_values[1].append((nx,ny))
            else:
                neighbor_values[2].append((nx,ny))

        return neighbor_values

    def move_score(self, sorted_value, neighbor_values):
        move_score = {}
        
        
        for value in sorted_value:
            if neighbor_values[value]:
                for coords in neighbor_values[value]:
                
                    move_score[(coords)] = value
        

        return move_score
    
    def predicter(self, start):
        moves_made_copy = self.moves_made.copy()
        hero_copy = self.place.hero_explored.copy()
        vil_copy = self.place.villain_explored.copy()
        if start not in moves_made_copy:
            moves_made_copy.append(start)
        if self.character.nature == "Hero":
            if start not in hero_copy:
                hero_copy.append(start)
        else:
            if start not in vil_copy:
                vil_copy.append(start)

        neighbors = self.get_neighbors(start[0], start[1])

        
    
        neighbor_values = self.evaluate_neighbors(neighbors, moves_made_copy, hero_copy, vil_copy)
       
        sorted_values = sorted(neighbor_values.keys(), reverse=True)

        move_score = self.move_score(sorted_values, neighbor_values)
       
        return move_score
    
    def deep_search(self, dict):
        future_score = {}
        for move in dict.keys():
            future_score = self.predicter(move)
        
        return future_score
    
    def adder(self, dict1, dict2, dict3):
        for move in dict1.keys():
            for move2 in dict2.keys():
                if move != move2:
                    if (move,move2) not in dict3:
                        dict3[(move,move2)] = 0
                    dict3[(move,move2)] += dict1[move] + dict2[move2]
            
        
    def pick_move(self):
        start = self.location()
        sorted_best_move = {}
        best_move = []
        distance_value = {}
        normalized_distance_value = {}
        next_move = {}
        if start:
            coords, player = start
            x, y = coords 
            if (x,y) not in self.moves_made:
                self.moves_made.append((x,y))
            if self.character.nature == "Hero":
                if (x,y) not in self.place.hero_explored:
                    self.place.hero_explored.append((x,y))
            else:
                if (x,y) not in self.place.villain_explored:
                    self.place.villain_explored.append((x,y))
            
            
            next_move = self.predicter(coords)
            sorted_best_move = sorted(next_move.items(), key=lambda x: x[1], reverse=True)
        
            
            

        for move, value in sorted_best_move:
            x,y = move
            center = (round(self.place.height/2), round(self.place.width/2))
            
                
            distance = math.sqrt((x - center[0])**2 + (y - center[1])**2)
            
            
            distance_value[(x,y)] = distance
        
        
        if distance_value:
            d = np.array(list(distance_value.values()))

            a = d.min()
            b = d.max()

            nd = (d-a) / (b-a)

            normalized_distance_value = {key: round(value,2) for key, value in zip(distance_value.keys(), nd)}
            

        for move, value in sorted_best_move:
            
            for coord, norm_val in normalized_distance_value.items():
                if coord == move:
                    next_move[move] -= norm_val
        
    

        for tile in self.place.hero_explored:
            if self.character.nature == "Hero":
                for object in self.place.tiles[tile].objects:
                    if isinstance(object,Villain):
                       
                        if tile not in next_move:
                            next_move[tile] = 0
                        next_move[tile] += 1
                        neighbors2 = self.get_neighbors(tile[0], tile[1])
                        for neigh in neighbors2:
                            if neigh not in next_move:
                                next_move[neigh] = 0
                            next_move[neigh] += .25
                
                break
            for tile in self.place.villain_explored:
                if self.character.nature == "Villain":
                    for object in self.place.tiles[tile].objects:
                        if isinstance(object,Hero):
                            if tile not in next_move:
                                next_move[tile] = 0
                            next_move[tile] += 1
                            neighbors2 = self.get_neighbors(tile[0], tile[1])
                            for neigh in neighbors2:
                                if neigh not in next_move:
                                    next_move[neigh] = 0
                                next_move[neigh] += .25
                        break



        sorted_best_move = sorted(next_move.items(), key=lambda x: x[1], reverse=True)
        
        
        
        
        
        
        for move, value in sorted_best_move:
            best_move.append(move)
            break
            
        return best_move 

    def make_move(self):
        start = self.pick_move()
        
        if start:
            location = self.location()
            if location == None:
                return
            coords, player = location
            
            print(coords, "start")
            
    
            territory_objects = self.place.tiles[start[0]].objects
            if territory_objects:
                territory = territory_objects[0]
            else:
                territory = None

            print(f"{self.character.name, self.character.HP, self.character.nature} moves to {start}")

            if isinstance(territory, Item) or isinstance(territory,Skills):
                self.place.tiles[(start[0][0], start[0][1])].remove_object(territory)
                self.place.tiles[coords].remove_object(self.character)
                self.place.tiles[(start[0][0], start[0][1])].add_object(self.character)
                pick_up_item(self.place, self.character, start[0][0], start[0][1])
                print(colored((f"{self.character.name} picks up {territory.name}"), "cyan"))
                return

                
            elif isinstance(territory,Hero) or isinstance(territory, Villain):
                damage = 0
                exp = 3
                if territory.nature == self.character.nature:
                    return 
                    
                print(f"{self.character.name} and {territory.name} begin fighting")
                if self.character.agi >= territory.agi:
                    if self.character.str >= self.character.int:
                        damage = melee_attack(self.character, territory)
                    else:
                        damage = magical_attack(self.character, territory)
                    
                    territory.HP -= damage
                    print(f"{self.character.name} dealt {damage} points of damage to {territory.name}")
                    
                    if territory.HP <= 0:
                    
                        
                        killed(self.place, self.character, territory, coords, start)
                        if territory.nature == "Hero":
                            for char in self.heroes:
                                if char == territory:
                                    self.heroes.remove(territory)
                        else:
                            for char in self.villains:
                                if char == territory:
                                    self.villains.remove(territory)
                        
                    else:
                        if self.character.nature == "Hero":
                            self.character.gain_exp(exp) 
                            print(f"{self.character.name} gained {exp} Exp ")
                        else:
                            territory.gain_exp(exp) 
                            print(f"{territory.name} gained {exp} Exp")
                    
                        if territory.str >= territory.int:
                            damage = melee_attack(territory, self.character)
                        else:
                            damage = magical_attack(territory, self.character)
                        
                        self.character.HP -= damage

                        print(f"{territory.name} dealt {damage} to {self.character.name}")

                        if self.character.HP <= 0:
                        
                            killed(self.place, self.character, territory, coords, start)
                            if self.character.nature == "Hero":
                                for char in self.heroes:
                                    if char == self.character:
                                        self.heroes.remove(self.character)
                                        return
                            else:
                                for char in self.villains:
                                    if char == self.character:
                                        self.villains.remove(self.character)
                                        return
                           

                else:
                    if territory.str >= territory.int:
                        damage = melee_attack(territory, self.character)
                    else:
                        damage = magical_attack(territory, self.character)
                    
                    self.character.HP -= damage
                    print(f"{territory.name} dealt {damage} to {self.character.name}")

                    if self.character.HP <= 0:
                        
                        killed(self.place, self.character, territory, coords, start)
                        if self.character.nature == "Hero":
                            for char in self.heroes:
                                if char == self.character:
                                    self.heroes.remove(self.character)
                                    return
                        else:
                            for char in self.villains:
                                if char == self.character:
                                    self.villains.remove(self.character)
                                    return
                        
                        
                    else:
                        if self.character.str >= self.character.int:
                            damage = melee_attack(self.character, territory)
                        else:
                            damage = magical_attack(self.character, territory)
                        
                        territory.HP -= damage
                        print(f"{self.character.name} dealt {damage} points of damage to {territory.name}")
                        
                        if territory.HP <= 0:
                            
                            killed(self.place, self.character, territory, coords, start)
                            if territory.nature == "Hero":
                                for char in self.heroes:
                                    if char == territory:
                                        self.heroes.remove(territory)
                            else:
                                for char in self.villains:
                                    if char == territory:
                                        self.villains.remove(territory)
                            
                        else:
                            if self.character.nature == "Hero":
                                self.character.gain_exp(exp)
                                print(f"{self.character.name} gained {exp} Exp ")
                                return
                            else:
                                territory.gain_exp(exp)
                                print(f"{territory.name} gained {exp} Exp")
                                return
            else:
                self.place.tiles[coords].remove_object(self.character)
                self.place.tiles[(start[0][0], start[0][1])].add_object(self.character)
                if (start[0][0], start[0][1]) not in self.moves_made:
                    self.moves_made.append((start[0][0], start[0][1]))
                if self.character.nature == "Hero":
                    if (start[0][0], start[0][1]) not in self.place.hero_explored:
                        self.place.hero_explored.append((start[0][0], start[0][1]))
                else:
                    if (start[0][0], start[0][1]) not in self.place.villain_explored:
                        self.place.villain_explored.append((start[0][0], start[0][1]))
                return
        else:
            return
        
                        

                        

                    


                    


            


        
            



        
    