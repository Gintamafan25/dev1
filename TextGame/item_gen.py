from item import Item
import csv

import random

def main():

    names = ["Firebrand", "Mext", "Orzillia", "Wertru", "Liem", "Quar", "Plors", "Tyter", "Nexlu"]
    cat = ["Sword", "Staff", "Bow"]
    weapons = []
    
    while len(names) > 0:
        chosen_name = random.choice(names)
        chosen_str = random.randint(1,5)
        chosen_int = random.randint(1,5)
        chosen_agi = random.randint(1,5)
        category = random.choice(cat)
        weapons.append(Item(category + " of " + chosen_name, chosen_str, chosen_int, chosen_agi, category))
        names.remove(chosen_name)

    with open("items.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["name", "str", "int", "agi", "category"])

        for wep in weapons:
            writer.writerow([wep.name, wep.str,wep.int, wep.agi,wep.category])

        

main()