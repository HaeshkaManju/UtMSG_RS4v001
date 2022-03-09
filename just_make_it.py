# Just do it
import pyinputplus as pyip
leader_ability_bonus = ["Banner Bearer", "Craftsman", "Herald",
               "Scholar", "Pioneer", "Scavenger"]

spells = ("Might", "Fervor", "Stalwart" , "Ward", "Celerity", "Forced March",
         "Armament", "True-Cause", "Napoleon", "Mind Leech", "Force Cage", "Earth Golem")

leader_combat_skills = ["leadership", "tactics"]

squad_combat_skills = ["courage", "outmaneuver", "aggressor", "pernicious", "parry"]

###############################################################################
# Functions
###############################################################################

#######################################
# Chief Spells #
#######################################
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

#######################################
# Cohort Spells #
#######################################

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

#######################################
# Chief Skills #
#######################################

def which_chief_skills(chief_skills_known):
    print("Which skills does your Chief know?")
    choice = 1
    while choice !='':
        choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
        if choice == '':
            break
        else:
            num_of_ranks = pyip.inputInt(prompt = "How many ranks in the skill? ", blank=False)
            chief_skills_known.update({choice: num_of_ranks})
    return chief_skills_known

#######################################
# Cohort Skills #
#######################################
def which_cohort_skills(cohort_skills_known):
    print("Which skills does your Cohort know?")
    choice = 1
    while choice !='':
        choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
        if choice == '':
            break
        else:
            num_of_ranks = pyip.inputInt(prompt = "How many ranks in the skill? ", blank=False)
            cohort_skills_known.update({choice: num_of_ranks})
    return cohort_skills_known

#######################################
# Hero Skills #
#######################################
def which_hero_skills(temp_hero_skills_known):
    print("Which skills does your Hero know?")
    choice = 1
    while choice !='':
        choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
        if choice == '':
            break
        else:
            num_of_ranks = pyip.inputInt(prompt = "How many ranks in the skill? ", blank=False)
            temp_hero_skills_known.update({choice: num_of_ranks})
    return temp_hero_skills_known

#######################################
# Leadership Summary #
#######################################

def display_leader_info(chief_name, cohort_name,
                        chief_leader_ability_bonus, cohort_leader_ability_bonus,
                        chief_spells_known, cohort_spells_known, chief_skills_known,
                        cohort_skills_known):
    print("Your Chief's name is: {}".format(chief_name))
    print("Your Chief's Leader Ability is: {}".format(chief_leader_ability_bonus))
    print("Your Chief knows the following spells: ")
    for x in chief_spells_known:
        print(x)
    print("Your Chief has the following skills: ")
    for x, y in chief_skills_known.items():
        print("Skill: {}, Rank: {}".format(x, y))
    print("Your Cohort's name is: {}".format(cohort_name))
    print("Your Cohort's Leader Ability is: {}".format(cohort_leader_ability_bonus))
    print("Your Cohort knows the following spells: ")
    for x in cohort_spells_known:
        print(x)
    print("Your Cohort has the following skills: ")
    for x, y in cohort_skills_known.items():
        print("Skill: {}, Rank: {}".format(x, y))

###############################################################################
# Main Loop
###############################################################################
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
        chief_leader_ability_bonus=pyip.inputMenu(leader_ability_bonus, numbered=True, blank=False)
        leader_ability_bonus.remove(chief_leader_ability_bonus)
        print("\n")
        print("Which leader bonus do you select for your Cohort?")
        cohort_leader_ability_bonus=pyip.inputMenu(leader_ability_bonus, numbered=True, blank=False)
        print("\n")
        #######################################################################
        chief_spells_known= []
        which_chief_spells(chief_spells_known)
        cohort_spells_known= []
        which_cohort_spells(cohort_spells_known)
        #######################################################################
        chief_skills_known={}
        which_chief_skills(chief_skills_known)
        print(chief_skills_known)
        cohort_skills_known={}
        which_cohort_skills(cohort_skills_known)
        print(cohort_skills_known)

        #######################################################################

        #######################################################################
        display_leader_info(
            chief_name, cohort_name, chief_leader_ability_bonus,
            cohort_leader_ability_bonus, chief_spells_known, cohort_spells_known,
            chief_skills_known, cohort_skills_known)

        #######################################################################
        # Create Heroes
        #######################################################################
        # How many heroes do the team have?
        # < INT 0-X
        # num_of_heroes < INT
        num_of_heroes = pyip.inputInt(prompt = "How many heroes? ", min=0)
        #hero1 = {"Hero Name": "str", "Abilities Known": ['list'], "Skills": [ {"leadership":INT}, {"tactics": INT} ] }
        global hero_info
        hero_info = []
        for x in range(1, num_of_heroes+1):
            # get a name to temporarily store.
            temp_name = pyip.inputStr(prompt="What is the hero's name? ", blank=False)
            # we'll skip adding abilities for now
            # Code
            # Ask which skills the hero knows and the ranks
            temp_hero_skills_known = []
            which_hero_skills(temp_hero_skills_known)
            print(temp_hero_skills_known)
            # jam all of that info the hero
            hero_info.append("hero{}".format(int(x)))
        print(hero_info)
        for x in range(1, num_of_heroes+1):
            pass


        # Access hero_info
        ## Determine where in "x" we are (0, 1, 2, etc)
        ### Access that entry in the list (hero_info[0]),
        #### turn that string into a dictionary?????
        #######################################################################
        # Create Squads
        #######################################################################

        # How many squads
        # < INT
        # Data: # of Loops
        # Loop
        ## Name of {} squad
        ## < String
        ## Data < Name, {} for all future data
        ## < INT, 0-10
        ## Data: < Level
        ### If: Level > 0
        ### Loop: Per Level > 0
        #### For Level {}, what stat to increase?
        #### < INT, Menu (stat_list)
        #### Data: {} squad, stat+1 or up 1 category
        ## What skills known?
        ### While NOT ' '
        ### < INT, Menu (skills_squad), allow blank
        ### If: !(not) ' '
        #### What rank is {} skill?
        #### < INT 1-10
        #### Data: {skill: rank}

if __name__ == "__main__":
    main()
