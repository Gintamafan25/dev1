from skills import Skills
import random
import csv

def main():
    with open("skills.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["name", "category", "damage", "cost",])

       
        writer.writerow(["Fireball", "Magic", 5, 20])
        writer.writerow(["Lightning", "Magic", 7, 30])
        writer.writerow(["Frost Bite", "Magic", 12, 100])
        writer.writerow(["Strike", "Physical", 6, 20])
        writer.writerow(["Sneak Attack", "Physical", 10, 50])
        writer.writerow(["hit", "Physical", 3, 5])
        writer.writerow(["Magical Shot", "Magical", 2, 5])
        
        
        

main()