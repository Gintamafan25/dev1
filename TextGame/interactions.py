from item import Item
from skills import Skills
from characters import Hero, Villain
from maps import Map
import random

def pick_up_item(place, character, x, y):
    for obj in place.tiles[(x,y)].objects:
        if isinstance(obj, Item):
            if obj not in character.items:
                obj.equip_to(character)
        elif isinstance(obj, Skills):
            if obj not in character.skills:
                character.skills.append(obj)

def melee_attack(attacker, defender):
    power = attacker.str
    defence = defender.str
    damage = 4
    

    if power >= defence:
        difference = power - defence
        damage += (damage * .5) + (difference * .2)
    
    else:
        difference = defence - power
        damage -= (damage * .5) + (difference * .2)
    
    defender.HP -= damage

    return round(damage,1)

def magical_attack(attacker, defender):
    power = attacker.int
    defence = defender.int
    damage = 4
    

    if power >= defence:
        difference = power - defence
        damage += (damage * .5) + (difference * .2)
    
    else:
        difference = defence - power
        damage -= (damage * .5) + (difference * .2)
    
    defender.HP -= damage

    return round(damage,1)

def killed(place, initiator, defender, initiator_cords, defender_coords):
    
    if initiator.nature == "Hero":
        initiator.gain_exp(6 + round(defender.rank))
        print(f"{initiator.name} gained {6 + round(defender.rank)} Exp ")
        
    else:
        initiator.kills.append(defender)
        print(f"{initiator.name} killed {defender.name} ")
    
    if defender.HP <= 0:
        
        place.tiles[defender_coords[0]].remove_object(defender)
        place.tiles[initiator_cords].remove_object(initiator)
        place.tiles[defender_coords[0]].add_object(initiator)

        print(f"{defender.name} died, {initiator.name} moves to {defender_coords}")

        if len(defender.items) > 0:
            print(f"{defender.name} dropped items")

            for item in defender.items:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(item)
            for item in defender.items:
                item.unequip_from(defender)

        if len(defender.skills) > 0:
            print(f"{defender.name} dropped skills")
            for skill in defender.skills:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(skill)
            for skill in defender.skill:
                defender.skills.remove(skill)

    elif initiator.HP <= 0:
        place.tiles[initiator_cords].remove_object(initiator)
        print(f"{defender.name} defended {defender_coords}")
        if len(initiator.items) > 0:
            print(f"{initiator.name} dropped items")

            for item in initiator.items:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(item)
            for item in defender.item:
                item.unequip_from(defender)

        if len(initiator.skills) > 0:
            print(f"{initiator.name} dropped skills")
            for skill in initiator.skills:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(skill)
            for skill in defender.skills:
                defender.remove(skill)

    






