from standard_race_options import Standard_Races, display_standard_race_options
import pyinputplus as pyip
"""
For setting up the initial usurpation.  Won't use for any other time, simply because once a game has started, players won't have the option to select ANY race, in a typical scenario.  During "character creation", players have all of the options available.

Uses the: display_standard_race_options(Standard_Races) function from the imported module.

During this process, when faced with the possibility of optimization, I will simply choose what I can write immediately.  I will leave myself comments when I believe I know the better way to do this.
"""

# This variable is set to a blank, globally, at the start of the game
# and will be modified by the verify_race_selection function.
# This iterable will contain, FOR READABILITY purposes, only the leader/cohort information for the player.
# doublequotes will be used for all instances of string variables in these
# entries, in case a player decides to use epithets or any other
# reason for an apostraphe in a name.


playerLeadership = {'leaderName': "", 'leaderRace': "", 'cohortName': "", 'cohortRace': "" }

# This function needs to be optimized for re-usability.
# refactor so that it knows the difference between leader
# and cohort, and updates accordingly.
def verify_race_selection(race_options, type):
    '''
        This function is designed to check for the following:
        1) Did the player select ANY valid choice?
        2) Did the player select a particular available option?
        3) Did the player fail to select a valid option?

        If the player doesn't select any usable (valid) option, repeat the question.

        If the player selects a particular race, have the function print out that choice and confirm.
    '''
    print(f"Please choose from among the available starting race options for your {type}")
    print("The options are: ")
    choice = pyip.inputMenu(race_options)
    return choice


# This should be a string formatted text that replaces "leader" and "cohort"
# with a replacement value, and a function that checks for each, allowing
# for code reusability.  This comment is a repeat of the comment before the
# verify_race_selection function, stated differently, as this comment
# refers to how the function is called.
standard_race_choice_leader =  verify_race_selection(Standard_Races, type = "Leader")

playerLeadership.update({'leaderRace': standard_race_choice_leader})

# this print statement is to verify and validate the code for testing purposes.
# this is bad design - this is a repeat of the above, but, for the cohort.

standard_race_choice_cohort = verify_race_selection(Standard_Races, type = "Cohort")

playerLeadership.update({'cohortRace': standard_race_choice_cohort})



##         If the player selects view - CALL the display_standard_race_options FUNC from the standard_race_options.py file to display the singular versions of the race names. ##
