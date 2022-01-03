"""
Until I decide to use an actual database, this will be where the basic race options are stored.

Options are: Dwarves, Elves, Gnomes, Goblins, Humans, Lizardfolk, and Orcs.

Important Question:
Whether to store all of the information inside of a nested array with dictionaries, or to break-out all of these information separately for readability?  I'm going to choose readability here.
"""
Base_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 1,
    "Defense": 1,
    "Strength": 1,
    "Speed - Combat": "M",
    "Speed - Overland": 2,
    "Max Tools": 2,
    "Max Weapons": 2,
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

Dwarves = {'singular': 'Dwarf', 'plural': 'Dwarves'}
Dwarves_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 1,
    "Defense": 1,
    "Strength": 1,
    "Speed - Combat": "M",
    "Speed - Overland": 2,
    "Max Tools": 2,
    "Max Weapons": 2,
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

Elves = {'singular': 'Elf', 'plural': 'Elves'}
Elves_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 1,
    "Defense": 1,
    "Strength": 1,
    "Speed - Combat": "F",
    "Speed - Overland": 2,
    "Max Tools": 1,
    "Max Weapons": 2,
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

Gnomes = {'singular': 'Gnome', 'plural': 'Gnomes'}
Gnomes_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 1,
    "Defense": 1,
    "Strength": 1,
    "Speed - Combat": "M",
    "Speed - Overland": 2,
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

Goblins = {'singular': 'Goblin', 'plural': 'Goblins'}
Goblins_stats = {
    "Name": "",
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

Humans = {'singular': 'Human', 'plural': 'Humans'}
Humans_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 1,
    "Defense": 1,
    "Strength": 1,
    "Speed - Combat": "M",
    "Speed - Overland": 2,
    "Max Tools": 2,
    "Max Weapons": 2,
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

Lizardfolk = {'singular': 'Reptilian', 'plural': 'Lizardfolk'}
Lizardfolk_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 0,
    "Defense": 0,
    "Strength": 0,
    "Speed - Combat": "M",
    "Speed - Overland": 2,
    "Max Tools": 2,
    "Max Weapons": 2,
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

Orcs = {'singular': 'Orc', 'plural': 'Orcs'}
Orcs_stats = {
    "Name": "",
    "Level": 0,
    "Offense": 0,
    "Defense": 0,
    "Strength": 0,
    "Speed - Combat": "M",
    "Speed - Overland": 2,
    "Max Tools": 2,
    "Max Weapons": 2,
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

Standard_Races = [Dwarves, Elves, Gnomes, Goblins, Humans, Lizardfolk, Orcs]

def display_standard_race_options(Standard_Races):
    '''
        This function is designed to show what the standard race options are.
        This should loop over the Standard_Races array, and display the SINGULAR version of the Race's collective name.
    '''
    for r in Standard_Races:
        print(r['singular'])

## Lose the comments whenever need to test that a given stat block is functioning properly or not.
def displayStatBlock(statGroup):
    for entry in statGroup:
        print("Stat {} is {}".format(entry,statGroup[entry]))
    return None

# displayStatBlock(Base_stats)