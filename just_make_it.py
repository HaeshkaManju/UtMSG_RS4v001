# Just do it
import pyinputplus as pyip
leader_ability_bonus = ["Banner Bearer", "Craftsman", "Herald",
               "Scholar", "Pioneer", "Scavenger"]

spells = ["Might", "Fervor", "Stalwart" , "Ward", "Celerity", "Forced March",
         "Armament", "Midas Touch", "Cornucopia", "Seer", "Druid Lore",
         "Silver-Tongue", "True-Cause", "Napoleon", "Shroud", "Telescoping",
         "Runesmith", "Mind Leech", "Force Cage", "Earth Golem"]

def which_chief_spells(chief_spells_known):
    print("What spells does your Chief know?")
    choice = 1
    while choice != '':
        choice = pyip.inputMenu(spells, numbered=True, blank=True)
        if choice == '':
            break
        else:
            chief_spells_known.append(choice)
    return chief_spells_known

def which_cohort_spells(cohort_spells_known):
    print("What spells does your Cohort know?")
    choice = 1
    while choice != '':
        choice = pyip.inputMenu(spells, numbered=True, blank=True)
        if choice == '':
            break
        else:
            cohort_spells_known.append(choice)
    return cohort_spells_known

def display_leader_info():
    print("Your Chief's name is: {}".format(chief_name))
    print("Your Chief's Leader Ability is: {}".format(chief_leader_ability_bonus))
    print("Your Chief knows the following spells: ")
    for x in chief_spells_known:
        print(x)
    print("Your Cohort's name is: {}".format(cohort_name))
    print("Your Cohort's Leader Ability is: {}".format(cohort_leader_ability_bonus))
    print("Your Cohort knows the following spells: ")
    for x in cohort_spells_known:
        print(x)
    
    




def main():
    program = True
    while program:
        print("Welcome to Usurper: the Medieval Strategy Game!")
        print("Let's build your Usurpation.")
        #######################################################################
        # Create Leaders
        #######################################################################
        chief_name = pyip.inputStr("What is your Chief's name? ", blank=False)
        print("\n")
        cohort_name = pyip.inputStr("What is your Cohort's name? ", blank=False)
        print("\n")
        #######################################################################
        print("Which leader bonus do you select for your Chief?")
        chief_leader_ability_bonus=pyip.inputMenu(leader_ability_bonus, blank=False)
        leader_ability_bonus.remove(chief_leader_ability_bonus)
        print("\n")
        print("Which leader bonus do you select for your Cohort?")
        cohort_leader_ability_bonus=pyip.inputMenu(leader_ability_bonus, blank=False)
        print("\n")
        #######################################################################
        chief_spells_known= []
        which_chief_spells(chief_spells_known)
        cohort_spells_known= []
        which_cohort_spells(cohort_spells_known)
        #######################################################################
        display_leader_info()

        #######################################################################
        # Create Heroes
        #######################################################################

        #######################################################################
        # Create Squads
        #######################################################################




if __name__ == "__main__":
    main()
