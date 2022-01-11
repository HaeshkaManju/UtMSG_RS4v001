from standard_race_options import *
"""
A pseudo-database for all of a player's choices.

Used in place of an actual database for form a save file.
"""

playerLeadership = {
    'Leader_Name': '',
    'Leader_Race': '',
    'Cohort_Name': '',
    'Cohort_Race': ''
    }

# This dictionary is a multi-dimensional.
# Inside of dictionary array, at the "top level" should be a list of VARIABLES.
## Each of these variables represents one of the player's purchased Units.
# Each of these Units[variables], has within it the following data:
## 1) A Dictionary of the Basic Stats of that Unit.
## 2) That Unit's Name - which should be the same as the variable name.
## 3) That Unit's Race.
playerUnits = {
    # write a sample of what I *WANT* to see, then make code to make it do that thing.
    1: "Rough Riders", "Stats": 
    {
        "Race": Goblins,
        "Level": 0,
        "Offense": 1,
        "Defense": 1,
        "Strength": 1,
        "Speed - Combat": "M",
        "Speed - Overland": 3,
        "Max Tools": 3,
        "Max Weapons": 1,
        "Recruit Cost": 10,
        "Upkeep Cost": 5,
        "Racial Abilities": [],
        "Skills": {},
        "Special Abilities": [],
        "Unique Abilities": [],
        "Tools Equipped": {},
        "Weapons Equipped": {},
        "Armor Equipped": {},
        "Mounts Equipped": {}
    }
}

playerExtras = []
print(playerUnits)
print(playerUnits[1]["Stats"]["Race"])