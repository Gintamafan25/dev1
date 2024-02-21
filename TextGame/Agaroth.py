import random, csv
from maps import Map, Tiles
from characters import Hero, Villain
from item import Item
from skills import Skills

Heroes = []
Villains = []
Items = []
Skill = []
Location = []

with open("character_villain.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        name, str_val, int_val, agi_val, nature = line
        str_val = int(str_val)
        int_val = int(int_val)
        agi_val = int(agi_val)
        if nature == "Hero":
            Heroes.append(Hero(name, str_val, int_val, agi_val))
        else:
            average = (str_val + int_val + agi_val) / 3
            Villains.append(Villain(name, str_val, int_val, agi_val, average))

with open("items.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        name, str_val, int_val, agi_val, category = line
        str_val = int(str_val)
        int_val = int(int_val)
        agi_val = int(agi_val)
        
        Items.append(Item(name, str_val, int_val, agi_val, category))

with open("skills.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for line in reader:
        name, category, damage, cost = line
        damage = int(damage)
        cost = int(cost)

        Skill.append(Skills(name, category, damage, cost))

Agaroth = Map("Agaroth", 15, 12)
Agaroth.create_map






        
