from player_choices import playerUnits
import pyinputplus as pyip
"""
No assumptions made here.  No using fancy calls.  No referencing other data areas.  Just get the choices from the player, add them to the player choices.
"""

def whatUnitValues():
    # I really don't understand how this works.
    # This is somehow a list comprehension
    # it seems to examine the X.join method first, then assumes a string of entries.
    #If it doesn't see a string, it will fail?
    print('\n'.join(str(entry) for entry in playerUnits))

# verifying the values when the script starts
whatUnitValues()
print("")

uarg = pyip.inputMenu(['Dwarf', 'Elf', 'Gnome', 'Goblin', 'Human', 'Reptilian', 'Orc'])
narg = pyip.inputStr(prompt="What is this Unit's name? ")
playerUnits.append(uarg)
whatUnitValues()
