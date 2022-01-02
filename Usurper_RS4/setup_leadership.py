from player_choices import playerLeadership
import pyinputplus as pyip
"""
No assumptions made here.  No using fancy calls.  No referencing other data areas.  Just get the choices from the player, add them to the player choices.
"""

def whatLeadershipValues():
    '''Verify what the Leadership values are.
    '''
    # This for loop examines each entry within the dictionary, then as key-value pairs: uses string formatting to enter them within each set of {}.
    for entry in playerLeadership:
        print("{} is {}".format(entry,playerLeadership[entry]))

# verifying the values when the script starts
whatLeadershipValues()
print("")
# This currently accepts anything that is stringable, no matter how dumb - fix later.
lnarg = pyip.inputStr(prompt="What is your Leader's Name? ")
lrarg = pyip.inputMenu(['Dwarf', 'Elf', 'Gnome', 'Goblin', 'Human', 'Reptilian', 'Orc'])
playerLeadership.update({'Leader_Name': lnarg})
playerLeadership.update({'Leader_Race': lrarg})

whatLeadershipValues()
print("")

cnarg = pyip.inputStr(prompt="What is your Cohort's Name? ")
lrarg = pyip.inputMenu(['Dwarf', 'Elf', 'Gnome', 'Goblin', 'Human', 'Reptilian', 'Orc'])
playerLeadership.update({'Cohort_Name': cnarg})
playerLeadership.update({'Cohort_Race': lrarg})

whatLeadershipValues()
print("")
