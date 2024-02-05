from characters import Hero, Villain
from item import item
from skills import Skills
import random

def main():
    hero_count = 4
    names = ["Sam", "Rex", "Lassy", "Brian", "Lexi", "Ophrita", "Anino", "Tyr", "Luze", "Spirta", "Melro", "Hury",
             "Imtop", "Erla", "Serchy"]
    heroes = []
    while hero_count > 0:
        chosen_name = random.shuffle(names)
        chosen_str = random.randint(1, 7)
        chosen_int = random.randint(1, 7)
        chosen_agi = random.randint(1, 7)
        names.remove(chosen_name)
        heroes.append(
            Hero(chosen_name, chosen_str, chosen_int, chosen_agi)
        )
        hero_count -= 1
    
    villain_count = 6

    