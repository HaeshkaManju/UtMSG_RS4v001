'''
This file shall handle random result generation for weighted results.
The intent is to start off rather simple in execution, using hard-coded data,
then move up to making the system more contextual.
Weighted Results refers to the System (Game) process where there's a standard set of results,
but one or more results gain additional "weight" thereby skewing the statistical odds of rolling
that particular result.

Common example of this: When scouting a grid, there's an equal chance of finding:
- A Hostile Encounter,
- A Resource Node (if it's not a Plains Grid.)
- An Encounter and a Node.

Because there are three possibilities, there should be a roughly 33% chance of any result.
If, due to the month's events, or some other effect: one of the results has "an additional weight" (let's say: Resource Nodes has the additional weight), then the list of possibilities would look like this:
- Encounter,
- Resource Node,
- Resource Node,
- Encounter and Node

This means that each result has a 25% chance of happening, with Resource Nodes occupying two of those potential results - thus Resource Nodes would have a 50% chance of being the result.  While an Encounter alone would have a 25% chance, and finding both an Encounter and a Node would have a 25% chance.

################################################################################
Basic Rules of Scouting Weights
################################################################################
1) If a player wants to SCOUT a Grid and has not discovered the Settlement in that Grid, then: finding the Settlement gains 1 Weight.
2) If a player wants to SCOUT a Grid and has discovered the Settlement in that Grid, then: finding the Settlement is not in the list of options.

################################################################################
Basic Rules of Exploration Weights
################################################################################
The possible options (number of items to be considered in weights) is dependent upon the success threshold.

If an event creates a weight for a particular Exploration Result (such as finding a "Trainer"), then that weight is ONLY added if that result is even possible at that threshold in the first place.

Example: The Necromancer Explore option does not appear for Partial Success Thresholds.  During the current month - there is an event that adds a weight to the Necromancer result.  Player Bob rolls a partial success during their Explore Check - this explore check will NOT have any chance of finding a Necromancer, because that was not on the list in the first place.
'''

#########################
#  Necromancer Results  #
#########################
Necromancer_partial = { 
    "Mechanic": "You may Sacrifice one level of one Unit of your Choice. Gain 3 skill XP, which you may assign as you see fit to whomever you see fit."
}

Necromancer_success = {
    "Mechanic": "Sap the energy of one of your Units. It loses 3 levels (and the accompanying stat points.) Gain 9 Gold. If this causes the Unit to be reduced below level 0, it dies. In addition, gain 6 skill XP, which you may assign as you see fit to whomever you see fit."
}

Necromancer_significant = {
    "Mechanic": "Siphon the energy of one of your Units or Sacrifice one Extra of your Choice. (If a Unit, choose a number of levels to lose up to to 5. Multiply this # by 3, you gain this much Gold and this much skill XP. If this causes a Unit to be reduced below level 0, it dies. If you sacrifice an Extra, instead: receive 1 Spell of your Choice. Then, multiply the Extra's Tier by 4: gain this much Skill XP, which you may assign as you see fit to whomever you see fit."
}

Necromancer_astounding = {
    "Mechanic": "Siphon the energy of one of your Units or Sacrifice one Extra of your Choice. (If a Unit, choose a number of levels to lose up to to 7. Multiply this # by 4, you gain this much Gold. Multiply the # of levels sacrificed by 3, and gain this much skill XP. If this causes a Unit to be reduced below level 0, it dies. If you sacrifice an Extra, instead: receive 1 Spell of your Choice. Then, multiply the Extra's Tier by 6: gain this much Skill XP, which you may assign as you see fit to whomever you see fit."
}

Necromancer_epic = {
    "Mechanic": "(If Unit(s), choose a number of levels to lose up to to 10 (may not reduce any Unit below -1). Multiply this # by 5, you gain this much Gold. Multiply the amount of levels sacrificed by 4 and gain this much skill XP. If this causes a Unit(s) to be reduced below level 0, it dies. (If not, lose appropriate stat points.) Assign to whomever you see fit. If you sacrifice an Extra, instead: receive 1 Spell of your Choice. Then, multiply the Extra's Tier by 8: gain this much Skill XP, which you may assign as you see fit to whomever you see fit."
}

Militia_Duty_partial = {
    "Mechanic": "Donate 4 x any one Resource. Reduce the Upkeep of up to 3 Units by 1 Gold each."
}

Militia_Duty_success = {
    "Mechanic": "Donate 4 x any one Resource. Reduce the Upkeep of up to 3 Units by 1 Gold each."
}

Militia_Duty_significant = {
    "Mechanic": "Donate 4 x any one Resource. Reduce the Upkeep of up to 3 Units by 1 Gold each."
}

Militia_Duty_astounding = {
    "Mechanic": "Donate 4 x any one Resource. Reduce the Upkeep of up to 3 Units by 1 Gold each."
}

Militia_Duty_epic = {
    "Mechanic": "Donate 4 x any one Resource. Reduce the Upkeep of up to 3 Units by 1 Gold each."
}

Soothsayer_partial = {
    "Mechanic": ""
}

Soothsayer_success = {
    "Mechanic": ""
}

Soothsayer_significant = {
    "Mechanic": ""
}

Soothsayer_astounding = {
    "Mechanic": ""
}

Soothsayer_epic = {
    "Mechanic": ""
}

explore_Partial_Success_Pot_Results = [Necromancer_partial, Militia_Duty_partial, Soothsayer, Trainer, Teacher, Request]

explore_Success_Pot_Results = []

explore_Significant_Success_Pot_Results = []

explore_Astounding_Success_Pot_Results = []

explore_Epic_Success_Pot_Results = []
