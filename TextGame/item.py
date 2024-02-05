import random
import pygame

class item:
    def __init__(self, name, str, int, agi, ability, category):
        self.name = name
        self.str = str
        self.int = int
        self.agi = agi
        self.ability = ability
        self.category = category

    def equip_to(self, character):
        character.str += self.str
        character.int += self.int
        character.agi += self.agi
        
    def unquip_from(self, character):
        character.str -= self.str
        character.int -= self.int
        character.agi -= self.agi


