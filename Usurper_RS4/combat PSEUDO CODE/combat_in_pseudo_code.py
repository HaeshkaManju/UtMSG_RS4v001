'''
This is for pseudo-coding only.
I will attempt to recreate the combat steps, one at a time, in extremely explicit detail.
'''
################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                               External Needs                                 #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################

# We will need three components of the Dice Roller file:
## - roll_std_d100: Roll a Single, Standard 100-sided die.
## - roll_exploding_d100: Roll a Single, Exploding 100-sided die.
## - roll_combat_dice: Roll a number of dice for a combat roll, exploding a single die if the pool is at least three (3) dice.
# Whenever a reference is made to a "Flat" or "Standard" Dice Roll:
## Use "roll_std_d100".
# Whenever a reference is made to an "Exploding" or "Open-ended"  Dice Roll:
## Use "roll_exploding_d100".
# Whenever a reference is made to a "Dice Pool", or a "Combat Check":
## Use "roll_combat_dice".
from dice_roller import roll_std_d100, roll_exploding_d100, roll_combat_dice

# We will need to setup the baseline Entity Data from somewhere.
## Could be a database or a flat file or what-have-you.
# Right now, all of the base information is written in standard_race_options.py

################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                            Outline of Combat                                 #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################

# Combat is Divided into Phases and Sub-Phases.
# Each Phase is done in order.
# The Strategy and Magic phases are done ONCE in a given combat.
# Ranged Combat is usually done ONCE in a given combat, though it is possible for multiple rounds to occur depending upon skills/magic.
# Melee Combat is done ONCE in a Short Battle.
# Melee Combat is done UP TO six times in a Full Battle.
# After each complete round of Melee, determine if there is a clear winner.  If yes, one side is declared "Victorious" the other is declared "Defeated".
## If a Short Battle, and no side is the clear winner...
### If only one Team is "Attacking", that Team is declared "Defeated".
### IF both Teams are "Attacking", both sides are declared "Defeated."
## If a Full Battle, and no side is the clear winner after six rounds of melee, the team which lost (either through being Destroyed or Fleeing) the most Squads is "Defeated".  If equal, both sides are "Defeated."

############################################
#             Individual Phases            #
############################################

# Each phase is performed in order.
# If a phase is ever repeated, perform all aspects of that phase again - while maintaining record of any damage/losses that have occured.
# Determine Forces, Strategy, and Magic are NEVER repeated.
# The following are the phases:
## Sub-phases - components of the overall phase, done in order, explained more explicitly.

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#     Determine Forces    #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# At least one side is identified as an Attacker.  The other side is either an Attacker or Defender. (this usually doesn't make a difference, though there are a few abilities which affect this.  Those affects which only trigger while being an Attacker or Defender will be annotated as "Attacer-only" and "Defender-only" respectively.
## "Attacker" and "Defender" ONLY serve to identify certain bonuses that are available.  ALL Squads participating in a combat "attack each other", in terms of which rolls are made.
# Identify which Entities are involved.
# Total all bonuses (save for those with the Annotation of "Strategy" or "Magic") and record them to their appropriate positions.
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#        Strategy         #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# Examine each side.  Determine if ANY Entity, on either/both sides has the Tactics skill.
## If neither side has the Tactics skill - treat both sides as having FAILED the check.
## If one side has the Tactics skill and the other does not, roll an opposed FLAT Roll, but only the side possessing the skill can "win."
### A side is determined to have "won" (A successful roll) if their total is greater than the other side.
### If the side without the skill rolls greater than the side with the skill, the result is "failed" for both sides.
## If both sides have the Tactics skill, roll an opposed FLAT Roll.
### Whichever side wins the result is "passed", the other side is "failed".
### Whichvever side passed the tactics roll receives an additional "+2" to Combat Checks made for Offense Rolls, during the FIRST round of combat.

# Repeat this process for the Outmaneuver skill.
## If either side passes the Outmaneuver check, then raise a flat to handle an additional round of ranged combat.  Only the winning side rolls attacks in that round.
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#           Magic         #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# Check if any Spells have been "ticked" (checked) on each side.
## This means a given spell is available and will be used.
### If no Spells are noted, skip all further components of the Magic section.
## Allow user to identify that a spell is available, and select a target for that spell (for "Friendly" spells.)
## Allow user to identify that a spell is available, and randomly select a target for that spell (for "Enemy" spells.)
# Apply the bonuses for friendly spells just like adding-in bonuses from the Determine Forces Phase.
# Roll appropriate checks for any enemy spells.
## Apply results.
### Some spells may cause an Entity's stat block to change.  This would last for the duration of this combat and then would be reverted to the original stat value.
### Future Feature: Nullification effects.  Not going to worry about this right now. ###
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#      Ranged combat      #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# Only Squads with have "Ranged Weapons" or Abilities with the annotation "Ranged" will make Attack combat checks here.
# All Squads "participate" in Ranged combat, in the sense that any Squad can be the target of Ranged Combat.

# Phase Description: Ranged Combat represents a flurry of distraction, confusion, arrows, slings, and other tactical diversions meant to disorganize and disrupt the opposing force.  This is abstractly handled as a series of attacks, which have the potential to reduce morale, reduce combat values, and even force Units to flee from the fight.

# Ranged Combat happens in descending speed order.
# Squads which have the same speed make their checks "simultaneously" (see terminology section.)
# There is typically only one "round" of Ranged Combat. (i.e. all those with ranged weapons make a single Combat Dice Roll to attack another unit.)
## If a Team won the Tactics roll, that team gains a second round of Ranged Combat.
# See Combat Dice Rolls for how the attack rolls take place.
# Squads automatically target the LOWEST level opposing Squad first.
## If multiple such squads exist (example: two level 0 squads on one side), then [for each attacking Squad] roll randomly for which Squad is targeted.  The attacking Squad will continue to attack this opposing Squad until it is defeated.
# Primary Difference between Ranged Combat and Melee Combat: Ranged Combat can NEVER produce CASUALTIES.  Instead, whenever a Damage Roll is made, use the Ranged Combat Damage Table.  Ranged Combat can cause penalties to accrue on a target.

# Bonuses are added to rolls only if they are applicable to Ranged Combat (a Unit does not get a bonus to its Offense and Damage rolls for having Melee Weapons, for example.)
## The easiest way to handle/apply this is the annotation: "Ranged".
### Future Feature: Additional Rounds.  Not going to worry about this right now. ###
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#       Melee combat      #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# All Squads participate in melee combat.
# Bonuses are added to rolls only if they are applicable to Melee Combat (a Unit does not get a bonus to its Offense rolls for having Ranged Weapons, for example.)
## The easiest way to handle/apply this is the annotation: "Melee".

# Phase Description: Melee Combat is slightly more literal - in that damage which occurs in Melee, results in deaths to the members (PAX) of individual Units.  Melee Combat occurs in speed order, as with Ranged Combat.

# See Combat Dice Rolls for how the attack rolls take place.

# Melee Combat happens in descending speed order.
# Squads which have the same speed make their checks "simultaneously" (see terminology section.)

# In a Short Battle, there is only one round of Melee.
# In a Full Battle, there will be up to six rounds of Melee.
## If one force is "decimated" (all Squads are destroyed and/or flee the battlefield, then there is no need to keep rolling.)

# Squads automatically target the LOWEST level opposing Squad first.
## If multiple such squads exist (example: two level 0 squads on one side), then [for each attacking Squad] roll randomly for which Squad is targeted.  The attacking Squad will continue to attack this opposing Squad until it is defeated.  If the targeted Squad was already established during Ranged Combat, this target remains the same.

# Primary Difference between Melee Combat and Ranged Combat: Melee Combat DOES product Casualties.  Use the appropriate damage chart (for Squads or Monsters) when rolling damage.  Damage resulting in penalties to Morale accrue and remain throughout the Combat, but are removed at the end of Combat.  Damage resulting in Casualties remains even after combat ends.  (Healing Squads is not handled in this module.
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#    Combat Dice Rolls    #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# Determine Dice Pool.
## Unless EXPLICITLY stated otherwise, all dice Pools are automatically d6s (that is, representing a six-sided die).
## The number of dice in a dice pool is equal to the value of the appropriate Stat.
## Additional dice are added for equipment, spells, etc.
## Determine Bonuses and Penalties to Pool.
### Total all relevant bonuses (as a positive value) and from that, subtract all appropriate penalties.
#### This should form a "pool" that would be represented something like: 4d6+7.
##### Any time the numeric value in FRONT of the die-type is at least 3, then this pool may "Explode". (See dice roller and/or terminology.)

# Whenever one Squad attacks another perform the following steps:

# Does the Squad have a target, yet?
## If no: determine target.  This becomes the target for the duration of combat or until the target Squad is eliminated (either killed or the Squad flees.)
## If yes, do not change target, continue to next step.

# Determine "Attacker's" Offense Dice Pool.
## (See Determine Dice Pools Section at beginning of this section.)
## Offense Pool uses the Off(ense) Stat.

# Determine "Defender's" Defense Dice Pool.
## (See Determine Dice Pools Section at beginning of this section.)
## Defense Pool uses the Def(ense) Stat.

# Roll opposed combat checks with these pools.
## If the Attacker's roll is greater than the Defender's roll, then a Hit is scored.
### For each value of 10 by which the Attack roll exceeds the Defense roll add: +1 to the subsequent damage roll (only for this attack, not for future attacks.)
## If the Defender's roll is greater than the Attacker's roll, then the attack Misses.
### If the attack misses, skip further steps on this attack.

# Determine Attacker's Damage Dice Pool.
## (See Determine Dice Pools Section at beginning of this section.)
## Damage Pool uses the Str(ength) Stat.

# Determine Defender's Armor Dice Pool.
## (See Determine Dice Pools Section at beginning of this section.)
## Armor Pool does not use a Stat, instead only certain spells, skills, abilities, and equipped armor matter here.

# Roll opposed combat checks with these pools.
## Compare the checks against the appropriate Damage vs Armor chart.

# This attack is now complete.
## Save the results of this attack.
## ONLY apply the results of the attack at the end of the given speed.
### i.e. if three Squads are all "Fast", complete the attack process for EACH squad that attacks at Fast speed before applying the damage from ANY attack.
#### Yes, this explicitly means that it is possible for:
##### Team1/SquadA to attack enemy Team2/Squad4, kill it, and then Team1/SquadB ends up attacking that same (Team2/Squad4) enemy Squad.

# Once a given speed is completed, all Squads which had a hit scored against them must make a Morale Check, using the Exploding Roll.
################################################################################


#!!!!!!!!!!!!!!!!!!!!!!!!!#
#     Check Combat End    #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# Determine if Combat has ended:
# If a Short Battle: combat ends once a full round of Melee is completed.
# If a Full Battle: combat ends once a six rounds of Melee are completed.
## The above two statements are true, EVEN if both forces are still on the battlefield.
# If One side is decimated - i.e. has no Squads remaining on the battlefield, Combat ends.
# If Both sides are decimated - i.e. neither side has Squads remaining on the battlefield, Combat ends.

# If combat has not ended, return back to the Melee Phase and repeat all steps.
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!#
#   Determine Aftermath   #
#!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# The winner of the combat is determined by the following criteria:
## If one side was completely destroyed - they are "Defeated".
## If one side was forced to flee - they are "Defeated".
## If neither of the above occurred:
### If a Short Battle, and no side is the clear winner...
#### If only one Team is "Attacking", that Team is declared "Defeated".
#### If both Teams are "Attacking", both sides are declared "Defeated."
### If a Full Battle, and no side is the clear winner after six rounds of melee, the team which lost (either through being Destroyed or Fleeing) the most Squads is "Defeated".  If equal, both sides are "Defeated."
################################################################################

################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                            Combat Terminology                                #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################
# Entity
## The catch-all term for all "characters", be they: Leaders, Extras, Legendary Foes, Single Entity Units, or Units
# Leaders
## Defined in two sub-types: Leader and Cohort.  They do not participate/fight as Squad, but instead lend their bonuses when they are present in a Combat.
# Heroes
## As leaders, they do not participate/fight as Squads would, but instead lend their bonsues when they are present in a Combat.
# Squad/Units
##	A group of 10 personnel (PAX) that work and fight together.
# Monster
##	A single individual that stands-for the same relative capacity as 10 Personnel (PAX). Fights as if it were a Unit.
# Dice
## The die type and # of dice used to determine a particular bonus.
# Dice Pool
## The total number of dice used in a given roll.  Units have a initial dice pool for Attack, Defense, and Damage rolls equal to their respective Off, Def, and Str stats.
# Rolls	'Check' or 'Roll' are used interchangably.
## This is the actual 'roll of the dice' to determine the total score/bonus of a portion of combat.
# Casualties
## These are the number of Personnel (PAX) which have been killed from a given Unit.   Casualties persist even after combat.  Casualties do not occur in Ranged Combat.
#Speed
## There are two types of speed: Combat and Overland.  Combat speed is represented by 1 to 2 letters.  This is the only speed that applies during Combat.
## Combat Speeds are as follows (in descending order):
### C->Celeritous
### VF->Very Fast
### F->Fast
### M->Medium
### S->Slow
### VS->Very Slow
# Damage
## Damage represents the results of an opposed check between a Damage Roll vs an Armor Roll. Damage remains on a Unit until the end of Combat.   Damage does not mean casualties.  Damage can occur in both Ranged and Melee Combat.  Damage is cumulative and persists until the end of combat.  Damage can be represented through reduced bonuses, reduced dice pools, and/or penalties to morale.
# Phase
## An individual steps of Combat.
# Off(ense)
## Short-form of Offense.  Representing the relative skill at "scoring a hit" that a given Entity has.
# Def(ense)
## Short-form of Defense.  Representing the relative skill at "avoiding being hit" that a given Entity has.
# Str(ength)
## Short-form of Strength.  Representing the relative skill at causing damage that a given Entity has.
# Arm(or)
## Short-form of Armor.  Representing the relative capacity at avoiding damage that a given Entity has.
# Spell
## An ability that an Entity can assign before the beginning of combat, the effects of which are applied in the "Magic" phase of combat.  Spell effects are resolved as either permanent modifiers or one-time effects depending upon the spell.  Any effect which would take place during the "Magic" phase of Combat will have the annotation "Magic".
# Skill
## An ability that an Entity has which provides modifiers to dice rolls during combat.  Some skills affect the "Strategy" phase of Combat.  These skills will have the annotation "Strategy".
# Attack
## A Combat check made using the Offense Stat.  This is an "Attack check" or "Attack roll".  Attacks are made
# Simultaneous
## An effect/phase/situation is deemed to be simultaneous if two or more participants have rolls or effects that are technically done at the same time.  To reflect this, the EFFECTS from those rolls/abilities are applied all at once, at the end of a given speed order.  For example: two Squads, on opposing sides are both MEDIUM speed.  They would attack simultaneously.  This means if Squad A attacked Squad 2, and scored damage: that damage would be applied after ALL Medium speed Squads had made their attack rolls.
# Morale
## A Squad's overall tenacity and willingness to stay in the fight.  Whenever a Squad sustains a hit, it must make a morale check (Exploding Dice Roll) to determine if it is willing to stay in the fight.
## Anytime a morale penalty is applied, that penalty remains for the duration of the entire combat.
################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                               Combat Charts                                  #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# RANGED DAMAGE vs ARMOR ROLLS  #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# Damage vs Armor | Result
#-----------------|----------------------------
# D <= A	      | -1 to Defensive/Armor Rolls
# D  > A	      | -1 to Defensive/Armor Rolls
# D  > A+12	      | -2 to Defensive/Armor Rolls
# D  > A+24	      | -2 to Defensive/Armor Rolls
# D  > A+36		  | -3 to Defensive/Armor Rolls
# D  > A+48	      | -3 to Defensive/Armor Rolls

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#  MELEE DAMAGE vs ARMOR ROLLS  #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# Damage vs Armor | Result
#-----------------|----------------------------
# D <= A	      | -1 to Defensive/Armor Rolls
# D  > A          | -1 PAX
# D  > A+12       | -2 PAX
# D  > A+24       | -3 PAX
# D  > A+36       | -5 PAX
# D  > A+48       | Unit slain outright

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# DAMAGE vs ARMOR ROLLS [Monsters] #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# Damage vs Armor | Result
#-----------------|----------------------------
# D <= A	      | -3 to Morale checks.
# D  > A	      | -1 to Defensive/Armor Rolls
# D  > A+12	      | -1 HP
# D  > A+24	      | -1 HP
# D  > A+36	      | -2 HP
# D  > A+48	      | -2 HP

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#          Morale Checks           #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#  Roll  | Success Level | Explanation
#--------|---------------|----------------------------------------------
# 1-25   |	Demoralized	 | The Unit flees the battle.
#                          Your subsequent Loyalty check is at a -5.
# 26-49	 |  Panicked	 | The Unit flees the battle.
# 50-74	 |  Battered	 | The Unit is battered. -10 to Morale,
#                          and -3 to Off, Def, and Str pools.
# 75-100 |  Shaken	     | The Unit is shaken. -10 to Morale.
# 101+   |  Resolute!    | No penalties.  The Unit is resolute!

# When Morale checks are made, all penalties are cumulative.  If a Squad makes three morale checks: Battered, Shaken, and Resolute; this Squad will have a total of -20 to all future Morale checks, and -3 to Off, Def, and Str pools for the remainder of combat.
