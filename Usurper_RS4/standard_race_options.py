"""
Until I decide to use an actual database, this will be where the basic race options are stored.

Options are: Dwarves, Elves, Gnomes, Goblins, Humans, Lizardfolk, and Orcs.

Important Question:
Whether to store all of the information inside of a nested array with dictionaries, or to break-out all of these information separately for readability?  I'm going to choose readability here.
"""

Dwarves = {'singular': 'Dwarf', 'plural': 'Dwarves'}
Dwarves_stats = {}

Elves = {'singular': 'Elf', 'plural': 'Elves'}
Elves_stats = {}

Gnomes = {'singular': 'Gnome', 'plural': 'Gnomes'}
Gnomes_stats = {}

Goblins = {'singular': 'Goblin', 'plural': 'Goblins'}
Goblins_stats = {}

Humans = {'singular': 'Human', 'plural': 'Humans'}
Humans_stats = {}

Lizardfolk = {'singular': 'Reptilian', 'plural': 'Lizardfolk'}
Lizardfolk_stats = {}

Orcs = {'singular': 'Orc', 'plural': 'Orcs'}
Orcs_stats = {}

Standard_Races = [Dwarves, Elves, Gnomes, Goblins, Humans, Lizardfolk, Orcs]

def display_standard_race_options(Standard_Races):
    '''
        This function is designed to show what the standard race options are.
        This should loop over the Standard_Races array, and display the SINGULAR version of the Race's collective name.
    '''
    for r in Standard_Races:
        print(r['singular'])
