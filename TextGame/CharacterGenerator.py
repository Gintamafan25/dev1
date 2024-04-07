from characters import Hero, Villain
import random
import csv

def main():
    hero_count = 6
    names = ["Sam", "Rex", "Lassy", "Brian", "Lexi", "Ophrita", "Anino", "Tyr", "Luze", "Spirta", "Melro", "Hury",
             "Imtop", "Erla", "Serchy"]
    heroes = []
    while hero_count > 0:
        chosen_name = random.choice(names)
        chosen_str = random.randint(1, 7)
        chosen_int = random.randint(1, 7)
        chosen_agi = random.randint(1, 7)
        
        heroes.append(
            Hero(chosen_name, chosen_str, chosen_int, chosen_agi)
        )
        names.remove(chosen_name)
        hero_count -= 1
    
    villain_count = 8

    villains = []
    while villain_count > 0:
        chosen_name = random.choice(names)
        chosen_str = random.randint(2, 9)
        chosen_int = random.randint(2, 9)
        chosen_agi = random.randint(2, 9)
        rank = (chosen_str + chosen_int + chosen_agi) / 3
        
        villains.append(
            Villain(chosen_name, chosen_str, chosen_int, chosen_agi, rank)
            )
        names.remove(chosen_name)
        villain_count -= 1

    with open("character_villain.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["name", "str", "int", "agi", "nature"])

        for hero in heroes:
            writer.writerow([hero.name, hero.str, hero.int, hero.agi, hero.nature])
        
        for villain in villains:
            writer.writerow([villain.name, villain.str, villain.int, villain.agi, villain.nature])

main()