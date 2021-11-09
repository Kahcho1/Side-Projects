# Create a character (maybe if a confirmation if you want it or not (looks hard))
# Name
# Race, Gender, Hair, Hair Colour, Eye Colour
# Height (Tall or Short, maybe go further)
# Body type (Thin, Average or Fat, maybe go further)
# Classes to choose from
# Weapons and Armour to choose depend on class 
# Gifts to choose
# Stat Allocation
# Skills available depending on stat allocated
# Creates a txt file to show character created
# Extra's  Enemy Generator + Gold/Inventory Calculator + Weapon enchantments

# Step 1: Trying to create a choice from predetermined things

# look at from random import choice choice for randomised stuff
import random

raceChoice = ["Human", "Elf", "Half-Elf", "Dwarf"]
classChoice = ["Knight", "Sorcerer", "Thief"]

strScore = str(random.randint(5, 17))
dexScore = str(random.randint(5, 17))
wisScore = str(random.randint(5, 17))
intScore = str(random.randint(5, 17))
conScore = str(random.randint(5, 17))
chaScore = str(random.randint(5, 17))

weaponList = ["Sword", "Staff", "Dagger"]
armList = ["Rusty Shield", "Big Witch Hat", "Leather Bag"]
giftSel = ["HP Potion", "Four Seasons Key", "Squishy Ball"]

selRace = random.choice(raceChoice)
selClass = random.choice(classChoice)

fname = input("Enter your character's First Name:\n")
lname = input("Enter your character's Last Name:\n")

print("You have named your character " + fname + " " + lname + ".")

def raceGen():
    print("Rolled " + selRace + " as your chosen race.")

def classGen():
    print("Rolled " + selClass + " as your chosen class.")

def raceBonus():
    if selRace == "Human":
        strBonus = str(2)
        strPlus = str(int(strScore) + int(strBonus))
    elif selRace == "Elf":
        strBonus = str(3)
        strPlus = str(int(strScore) + int(strBonus))
    elif selRace == "Half-Elf":
        strBonus = str(2)
        strPlus = str(int(strScore) + int(strBonus))
    elif selRace == "Drawf":
        strBonus = str(3)
        strPlus = str(int(strScore) + int(strBonus))
    else:
        strPlus = (strScore)
    print("Character Stats:\nStrength: " + str(strPlus) + "\nDexterity: " + str(dexScore) + "\nWisdom: " + str(wisScore) + "\nIntelligence: " + str(intScore) + "\nConstitution: " + str(conScore) + "\nCharisma: " + str(chaScore))

def weapGen():
    if selClass == "Knight":
        print("A " + weaponList[0] + " has been provided to you.")
    elif selClass == "Sorcerer":
        print("A " + weaponList[1] + " has been provided to you.")
    elif selClass == "Thief":
        print("A " + weaponList[2] + " has been provided to you.")
    else:
        quit

def armGen():
    if selClass == "Knight":
        print("With a " + armList[0] + " as well.")
    elif selClass == "Sorcerer":
        print("With a " + armList[1] + " as well.")
    elif selClass == "Thief":
        print("With a " + armList[2] + " as well.")
    else:
        quit

def final():
    raceGen()
    classGen()
    raceBonus()
    weapGen()
    armGen()

final()

giftGen = int(input("Choose a gift to aid your journey using 1, 2 or 3:\n1) HP Potion\n2) Season Key\n3) Squishy Ball\n"))
if giftGen == 1:
    print("A safe choice! One can never be too carful with a " + giftSel[0] + ".")
elif giftGen == 2:
    print("Wonder where and what will open with this " + giftSel[1] + "?")
elif giftGen == 3:
    print("You held the ball in your hands: it's squishy.")
else:
    quit