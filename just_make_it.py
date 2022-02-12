# Just do it
import pyinputplus as pyip
leader_ability_bonus = ["Banner Bearer", "Craftsman", "Herald", 
               "Scholar", "Pioneer", "Scavenger"]

spells = ["Might", "Fervor", "Stalwart" , "Ward", "Celerity", "Forced March",
         "Armament", "Midas Touch", "Cornucopia", "Seer", "Druid Lore",
         "Silver-Tongue", "True-Cause", "Napoleon", "Shroud", "Telescoping",
         "Runesmith", "Mind Leech", "Force Cage", "Earth Golem"]

def which_leader_spells():
    print("What spells does your leader know?")
    while choice not '':
        choice = pyip.inputMenu(spells, numbered=True, blank=True)
    leader_spells_known


def display_leader_info():
    print("Your Chief's name is: {}".format(chief_name))
    print("Your Cohort's name is: {}".format(cohort_name))




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
        chief_leader_ability_bonus=pyip.inputMenu(leader_ability_bonus, blank=False)
        print("\n")
        #######################################################################
        leader_spells_known= []
        
        
        #######################################################################
        # Create Heroes
        #######################################################################
        
        #######################################################################
        # Create Squads
        #######################################################################




if __name__ == "__main__":
    main()
