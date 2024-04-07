import random


class Item:
    def __init__(self, name, str, int, agi,  category):
        self.name = name
        self.str = str
        self.int = int
        self.agi = agi
        
        self.category = category

    def equip_to(self, character):
        character.str += self.str
        character.int += self.int
        character.agi += self.agi
        character.item.append(self)
        
    def unequip_from(self, character):
        character.str -= self.str
        character.int -= self.int
        character.agi -= self.agi
        character.item.remove(self)


