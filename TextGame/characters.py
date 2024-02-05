import random


class Hero:
    def __init__(self, name, Str, Int, Agi):
        self.name = name
        self.str = Str
        self.int = Int
        self.agi = Agi
        self.HP = 100
        self.MP = 200
        self.level = 1
        self.exp = 0
        self.item = []
        self.skill = []
        self.nature = "Hero"
    
    def add_item(self, item):
        if item not in self.item:
            self.item.append(item)
        else:
            print(f"    {self.name} already posses this item")
    
    def remove_item(self, item):
        if item in self.item:
            self.item.remove(item)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
    
    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)

    def check_level(self):
        limit = self.level * 15
        if self.exp >= limit:
            self.str += 1
            self.int += 1
            self.agi += 1
            self.level += 1
            self.exp = 0
            if self.HP < 100:
                self.HP += (self.HP - 100) * -1
            if self.MP < 200:
                self.MP += (self.MP - 200) * -1
            print(f"    {self.name} Has Leveled Up!")
    
    def gain_exp(self, exp):
        if self.level == 5:
            print(f"    {self.name} has reached max level")
        else:
            self.exp += exp
            self.check_level()
            
                
class Villain:
    def __init__(self, name, str, int, agi, rank):
        self.name = name
        self.str = str
        self.int = int
        self.agi = agi  
        self.HP = 150
        self.MP = 300
        self.items = []
        self.kills = []
        self.skills = []
        self.nature = "Villain"

    def add_item(self, item):
        if item not in self.item:
            self.item.append(item)
    
    def remove_item(self, item):
        if item in self.item:
            self.item.remove(item)

    def add_kill(self, name):
        if name not in self.kills:
            self.kills.append(name)
    
    def add_skills(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
    
    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
    