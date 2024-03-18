from item import Item
from skills import Skills
from characters import Hero, Villain
from maps import Map
import random

def pick_up_item(place, character, x, y):
    for obj in place.tiles[(x,y)].objects:
        if isinstance(obj, Item):
            if obj not in character.item:
                obj.equip_to(character)
        elif isinstance(obj, Skills):
            if obj not in character.skill:
                character.skill.append(obj)

def melee_attack(attacker, defender):
    power = attacker.str
    defence = defender.str
    damage = 10
    

    if power >= defence:
        difference = power - defence
        damage += (damage * .5) + (difference * .2)
    
    else:
        difference = defence - power
        damage -= (damage * .5) + (difference * .2)
    
    defender.HP -= damage

    return damage

def magical_attack(attacker, defender):
    power = attacker.int
    defence = defender.int
    damage = 10
    

    if power >= defence:
        difference = power - defence
        damage += (damage * .5) + (difference * .2)
    
    else:
        difference = defence - power
        damage -= (damage * .5) + (difference * .2)
    
    defender.HP -= damage

    return damage

def killed(place, initiator, defender, initiator_cords, defender_coords):
    
    if initiator.nature == "Hero":
        initiator.exp += defender.rank + 6
        
    else:
        initiator.kills.append(defender)
    
    if defender.HP <= 0:
        place.tiles[defender_coords].remove(defender)
        place.tiles[initiator_cords].remove(initiator)
        place.tiles[defender_coords].append(initiator)

        if len(defender.item) > 0:

            for item in defender.item:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(item)
            for item in defender.item:
                item.unequip_from(defender)

        if len(defender.skills) > 0:
            for skill in defender.skill:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(skill)
            for skill in defender.skill:
                defender.skill.remove(skill)

    elif initiator.HP <= 0:
        place.tiles[initiator_cords].remove(initiator)
        if len(initiator.item) > 0:

            for item in initiator.item:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(item)
            for item in defender.item:
                item.unequip_from(defender)

        if len(initiator.skills) > 0:
            for skill in initiator.skill:
                open_space = [tile for tile in place.tiles.values() if len(tile.objects) == 0]
                random.shuffle(open_space)
                open_space[0].add_object(skill)
            for skill in defender.skill:
                defender.remove(skill)

    






