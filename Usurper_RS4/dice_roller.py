import math
import random

'''
This file will hold all information pertaining to make dice rolls within the Usurper Game context.  This module should be importable anywhere that interaction involving dice rolls would occur.

The functions shall be:
- roll_std_d100: Roll a Single, Standard 100-sided die.
- roll_exploding_d100: Roll a Single, Exploding 100-sided die.
- roll_combat_dice: Roll a number of dice for a combat roll, exploding a single die if the pool is at least three (3) dice.
- roll_harvest_dice: Roll a number of dice for a harvest results roll.
'''

################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                                Dice Rolls                                    #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################

def roll_std_d100(totalModifier):
    '''
        Standard d100 rolls are for "flat" rolls (simple percentile checks), such as determining if a Unique Event occurs for a given month.
        No explosion may occur.
    '''
    # First Print Statement to create a visual separation between this function and the next during testing.
    print("This is the Standard D100 Roll Function")
    # This print to ensure that our modifiers are being passed-in properly.
    print("Current totalModifier is: ", totalModifier)
    # use the random library to get a # between 1 and 100.  "101" because 101 is the END of the range, EXCLUSIVE.
    diceRoll = random.randrange(1,101)
    # need to verify the math later, so printing the random INTeger just in case.
    print("1st Roll: ", diceRoll)
    # Math it all together, then return it to the original function CALL to be printed.
    result = diceRoll + totalModifier
    return result

def roll_exploding_d100(totalModifier):
    '''
        The rules for "Exploding" a d100 are as follows:
        If it is a skill check, and is a d100 roll, the roll can explode.
        Explosion can only happen once per roll.
        Explosion occurs if the DICE ROLL (not including any modifiers) is a result of 96, 97, 98, 99, or 100.
        On an Explosion, an additional d100 is rolled.
        This second dice roll is added to the first, along with any applicable modifiers, to determine the final result.
        An exploding die may only ever explode "once" in a given check.
    '''
    # First Print Statement to create a visual separation between this function and the next during testing.
    print("This is the Exploding D100 Roll Function")
    # This print to ensure that our modifiers are being passed-in properly.
    print("Current totalModifier is: ", totalModifier)
    # use the random library to get a # between 1 and 100.  "101" because 101 is the END of the range, EXCLUSIVE.
    diceRoll = random.randrange(1,101)
    # need to verify the math later, so printing the random INTeger just in case.
    print("1st Roll: ", diceRoll)
    # If-else is here to assess if the dice roll is within the explosion range.
    # if roll BELOW explosion range (less than 96), carry on as if the 2nd dice roll were 0.
    # if roll WITHIN explosion range (96 or greater), roll a 2nd dice and add all three values together.
    if diceRoll < 96:
        diceRoll2 = 0
        print("2nd Dice Roll is: ", diceRoll2)
        result = diceRoll + diceRoll2 + totalModifier
        return result
    else:
        diceRoll2 = random.randrange(1,101)
        print("2nd Dice Roll is: ", diceRoll2)
        result = diceRoll + diceRoll2 + totalModifier
        return result

################################################################################
#                           D100 Dice Rolls CALLS                              #
################################################################################
# Test parameters only
modifiers = 23

resultFlat = roll_std_d100(modifiers)
print("Total Flat Dice Roll: ", resultFlat)
result = roll_exploding_d100(modifiers)
print("Total Dice Roll: ", result)

################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                              Dice Pool Rolls                                 #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# test parameters only
# Dice size should ALWAYS be 4, 6, 8, or 10.
# Dice size ALWAYS correlates to a random range of "1->Size" INCLUSIVE.
diceSize = 6
dicePool = 3
poolModifiers = 7
rerollOnes = False

def roll_combat_dice(diceSize, dicePool, poolModifiers):
    '''
    Combat Dice rolls are those dice rolls which are made on behalf of Entities in combat.
    Combat Dice rolls are composed of pools of like dice + modifiers.
    Combat Dice rolls, if the pool is at least 3 dice, one of those dice can explode on a result of a 6.
    - If a die explodes, no other dice may explodes.
    '''
    print("This is the Roll Combat Dice Function")
    print("""Our Initial Arguments are:\n
 Dice Size: {}
 Dice Pool: {}
 Total Modifiers: {}""".format(diceSize, dicePool, poolModifiers))
    # We begin with the diceValues array being empty.  This is where we will store all of our dice rolls.
    # I don't know if this is even necessary.  Feels like we could just add the values to the total as we go.
    diceValues = []
    # TotalOfDice will be used to tabulate the total of all of our dice as we go.
    TotalOfDice = 0
    # Yes, I realize I can use diceSize for the Upperlimit as a reference, but I feel like this is easier to read.
    # UpperLimit refers to the "maximum" value that can be rolled on a given die, thus it will be used when determining if an explosion occurs.
    UpperLimit = diceSize
    # These ranges are +1, because they take the pool and size, use them in ranges, but ranges always stop AT the number value
    ## but, we want the full number value, so we add 1.
    for p in range(dicePool+1):
        # diceSize is used to replicate a "D4, D6, D8, and D10" entering the appropriate value in that variable will result in the range being
        ## equal to the possible dice roll.
        diceRoll = random.randrange(1, diceSize+1)
        print(diceRoll)
        diceValues.append(diceRoll)
        print(diceValues)
    if UpperLimit in diceValues:
        diceRoll2 = random.randrange(1, diceSize+1)
        diceValues.append(diceRoll2)
    for v in diceValues:
        TotalOfDice += v
    print("The Total of your Dice Pool Roll is: ", TotalOfDice)
    print("The Grand Total of your Dice Roll is: ", TotalOfDice+poolModifiers)


def roll_harvest_dice(diceSize, dicePool, poolModifiers, rerollOnes):
    '''
    Harvest Dice Rolls are those dice rolls which are made on behalf of Entities who have succeeded at a harvest nodes check, returning the # of found resources.
    Harvest Dice rolls are composed of pools of like dice + modifiers.
    Harvest Dice rolls cannot explode.
    Harvest Dice rolls sometimes must reroll all "1s" (lowest result.)  When 1st ARE to be rerolled, a result of "1" must be rerolled UNTIL a result other than 1 is found.
    '''
    print("This is the Roll Harvest Dice Function")
    print("""Our Initial Arguments are:\n
 Dice Size: {}
 Dice Pool: {}
 Total Modifiers: {}
 Rerolling 1s? {}""".format(diceSize, dicePool, poolModifiers, rerollOnes))
    # We begin with the diceValues array being empty.  This is where we will store all of our dice rolls.
    # I don't know if this is even necessary.  Feels like we could just add the values to the total as we go.
    diceValues = []
    # TotalOfDice will be used to tabulate the total of all of our dice as we go.
    TotalOfDice = 0
    # We run this process if the results are such that we need to reroll ones, otherwise- set rerollOnes to False so this step is ignored.
    if rerollOnes == True:
        for p in range(dicePool+1):
            diceRoll = random.randrange(2, diceSize+1)
            print(diceRoll)
            diceValues.append(diceRoll)
            print(diceValues)
        for v in diceValues:
            TotalOfDice += v
        print("The Total of your Dice Pool Roll is: ", TotalOfDice)
        print("The Grand Total of your Dice Roll is: ", TotalOfDice+poolModifiers)
    else:
        for p in range(dicePool+1):
            diceRoll = random.randrange(1, diceSize+1)
            print(diceRoll)
            diceValues.append(diceRoll)
            print(diceValues)
        for v in diceValues:
            TotalOfDice += v
        print("The Total of your Dice Pool Roll is: ", TotalOfDice)
        print("The Grand Total of your Dice Roll is: ", TotalOfDice+poolModifiers)
################################################################################
#                          Dice Pool Rolls CALLS                               #
################################################################################

roll_combat_dice(diceSize, dicePool, poolModifiers)

roll_harvest_dice(diceSize, dicePool, poolModifiers, rerollOnes)
