import pyinputplus as pyip
from class_entities import *
###############################################################################
#      Leaders refer to those non-combatants which provide "area" bonuses.    #
#                     Leaders can perform Leader actions.                     #
###############################################################################
class Leader(Entity):
    # Leader Attributes
    def __init__(self, health,leader_ability, leader_type, donkey_equipped, items_carried, available_actions, leader_bonus, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned):
        # Leaders need ALL attributes of the Entity parent class.
        super().__init__(name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned)
        # Default health = 2
        self.health = health
        self.leader_ability = leader_ability
        self.leader_type = leader_type
        self.donkey_equipped = donkey_equipped
        self.items_carried = items_carried
        # Replacement me with the actual variable name of the "Leader Available Actions" when created.
        self.available_actions = available_actions
        # Default Leader Action Bonus = 25
        self.leader_bonus = leader_bonus

    # Leader Methods
    def leader_take_damage(self):
        '''
        Should be called within the context of combat results.
        The losing side of a combat, if it had one or more leaders, may take_damage.
        If that check results in the affirmative, call this and display the results to the player.
        '''
        if self.health == 2:
            self.health = 1
            self.leader_bonus = 12
            print("{} has suffered an injury!".format(self.name))
        else:
            # health essentially drops from 1->0.
            self.health = 0
            print("{} has succumbed to their wounds and died!".format(self.name))
            # update to "dead"
            # remove from lair thread.
        return None

    def leader_heal_damage(self):
        '''
        Essentially the opposite of take damage, except that a leader cannot
        be revived from death.
        Should be called within the context of the "Rest" action.
        May be called within the context of other events that grant "Healing" to a Leader.
        '''
        if self.health == 2:
            print("{} is already at max health.  No healing was applied".format(self.name))
        else:
            self.health = 2
            self.leader_bonus = 25
        return None

    def set_type(self):
        '''
        Should be called if the chief is killed and the cohort needs to be
        "promoted" to chief.
        If an entity with type of "chief" dies, call this.  Check if
        '''
        pass

    def learn_ability(self):
        pass

    def equip_donkey(self):
        pass

    def dequip_donkey(self):
        pass

    def carry_item(self):
        pass

    def drop_item(self):
        pass

    def display_leader_stat_block(self):
        pass
