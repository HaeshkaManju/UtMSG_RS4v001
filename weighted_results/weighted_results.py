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
import random

# These are stand-ins for the actual types of Encounters such as: "Necromancer" or "Trainer".
# This same process should also be applicable to other results' lists such as Scouting.
type1 ="type1"
type2 ="type2"
type3 ="type3"
type4 ="type4"

# A simple list containing three of the four available types of Encounters.
# In a normal scenario, this should be three equal weights of 33% each.
mild_success_options = [type1, type2, type3]

# TEST VALUES
# weighted option: this represents a result that would gain increased weight (chance) of happening in a given result set.
weighted_option = type2

# need a function to validate what is in the list and determining whether or not to add the weighted option to that list./
# the weighted option should only get add

def isMyTypeInList(options, weighted_opt):
    pass



x = random.choice(mild_success_options)
print(x)