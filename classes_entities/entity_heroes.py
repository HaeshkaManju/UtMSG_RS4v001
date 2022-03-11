import pyinputplus as pyip
from class_entities import *
# from classes_entities import class_entities
###############################################################################
#  Heroes refer to Unique non-combatants which provide specialized bonuses.   #
#                Heroes perform Training and Assist Actions.                  #
###############################################################################
class Hero(Entity):
    # Hero Attributes
    def __init__(self, originating_settlement, associated_quest, cost, upkeep, available_actions, morale_modifier, morale_status, unique_flag, unique, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned):
        # Heroes need ALL attributes of the Entity parent class.
        super().__init__(name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned)
        # Originating Settlement is partially "flavor", but it also serves
        # as a triggering mechanic for the associated quest.
        # If the hero is ever brought to its originating settlement during an
        # action, the player will automatically receive the associated quest.
        self.originating_settlement = originating_settlement
        self.cost = cost
        self.upkeep = upkeep
        # See originating settlement note.
        self.associated_quest = associated_quest
        # Replace me with the actual variable name of the "Hero Available Actions" when created.
        self.available_actions = available_actions
        self.morale_modifier = morale_modifier
        self.morale_status = morale_status
        # This is set to False until the given Hero is DISCOVERED.
        # Discovered simply references to being "generated" at any point in the game.  Once a decision is made about whether or not to recruit a given
        # hero, then that hero may NEVER be recruited again. (remove it from all future instances of being "rolled" in this game instance.)
        self.unique_flag = unique_flag
        # Some components of the game will check if the entity is unique to determine whether it qualifies for targeting/selection rules.
        # Default for all heroes is True
        self.unique = unique

    # Hero Methods
    def sacrifice_to_quest(self):
        pass

    def join_quest(self):
        pass

    def discovered_flag(self):
        '''
        Should be called whenever a hero has been discovered, for any reason.
        Should be used to set the flag (which defaults to False) to True.
        Should be used in conjunction with database to make a particular
        hero unable to be discovered again.
        '''
        self.unique_flag = True
        return self.unique_flag

    def display_hero_stat_block(self):
        pass

    def morale_check(self):
        pass

    def loyalty_check(self):
        pass
