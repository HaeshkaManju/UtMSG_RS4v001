import pyinputplus as pyip
from class_entities import *
###############################################################################
#  Squads refer to a collective-singular group, represented as a single       #
#   entity which can perform tasks and participate in combat as a collective  #
#                Squads perform Squad actions and assist actions.             #
#      Squads Health stats represent losing members of the larger group.      #
###############################################################################
class Squad(Entity):
    # Squad Attributes
    def __init__(self, health, max_health, offense, defense, strength, race, level, level_experience, cost, upkeep, speed_combat, max_weapons, max_tools, weapons_equipped, tools_equipped, mounts_equipped, racial_ability, unique, damage_chart, available_actions, morale_status, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned):
        # Squads need ALL attributes of the Entity parent class.
        super().__init__(name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned)
        self.health = health
        # default should be 10 for normal squads.
        self.max_health = max_health
        self.offense = offense
        self.defense = defense
        self.strength = strength
        self.race = race
        # default should be level 0.
        self.level = level
        # default should be 0 XP.
        # if a squad is ever recruited at a level higher than 0, starting XP
        # should be adjusted according to the minimum to be at the given level.
        self.level_experience = level_experience
        # default should be 10
        ## Unique squads default to 15.
        self.cost = cost
        # default should be 5
        ## unique squads default to 6.
        self.upkeep = upkeep
        self.speed_combat = speed_combat
        self.max_weapons = max_weapons
        self.max_tools = max_tools
        self.weapons_equipped = weapons_equipped
        self.tools_equipped = tools_equipped
        self.mounts_equipped = mounts_equipped
        self.racial_ability = racial_ability
        # Standard squads are normally not unique.
        # The default value is therefore false.
        # If a Unique Squad is discovered, override this value to true.
        # Some components of the game will check if the entity is unique to
        # determine whether it qualifies for targeting/selection rules.
        self.unique = unique
        # The default should be "Standard_Damage_Chart"
        # It should probably be replaced by a variable name that is pertinent
        # to standard squads.
        self.damage_chart = damage_chart
        # Replace me with the actual variable name of the "Squad Available Actions" when created.
        self.available_actions = available_actions
        self.morale_status = morale_status

    def squad_take_damage(self):
        pass

    def squad_heal_damage(self):
        pass

    def equip_weapon(self):
        pass

    def dequip_weapon(self):
        pass

    def gain_level_experience(self):
        '''
        Should be used whenever leveling experience points are assigned to the
        Squad in question.
        Should evaluate the amount of experience the squad already has along
        with the amount being added.
        Should include whether or not any of the "Scholar" or "Adaptive"
        abilities are at play.
        Use these and evaluate against a switch/IF statement set to determine
        if the Squad's level has changed.  Update stats and player accordingly.
        0 XP = Level 0.
        1-3XP = Level 1-3.
        5XP = Level 4, 7XP = Level 5, 9XP = Level 6.
        12XP = level 7, 15XP = level 8, 18XP = level 9.
        22XP = level 10.
        "partials" are denoted as: "Level 4, 1XP" [for 6XP total]
        '''
        pass

    def lose_level_experience(self):
        pass

    def assign_level_experience(self):
        '''
        Should be used to decide WHICH squad gets leveling XP.
        Leveling XP is only generated if a squad is present during a successful
        action.
        Need a function to decide WHICH squad gets the leveling XP.
        '''
        pass

    def equip_tool(self):
        pass

    def dequip_tool(self):
        pass

    def equip_mount(self):
        pass

    def dequip_mount(self):
        pass

    def occupy_barracks_slot(self):
        pass

    def leave_barracks_slot(self):
        pass

    def sacrifice_to_quest(self):
        pass

    def participate_in_quest(self):
        '''
        Functionally similar to the HERO version "join a quest".
        Not sure if there should be any difference in implementation.
        '''
        pass

    def display_hero_stat_block(self):
        pass

    def morale_check(self):
        pass

    def update_morale_status(self):
        '''
        Should this just be part of morale check?
        morale check focuses on setting up the dice pool and making the roll.
        But, should that function also handle the consequence of the roll?
        '''
        pass

    def loyalty_check(self):
        pass

    def update_loyalty_status(self):
        '''
        Should this just be part of loyalty check?
        loyalty check focuses on setting up the dice pool and making the roll.
        But, should that function also handle the consequence of the roll?
        '''
        pass

    def convert_to_unique_squad(self):
        '''
        Should be called whenever a situation results in a standard squad
        becoming unique.  Usually as a result of a landmark or capture roll.
        '''
        self.unique = True
        return self.unique



###############################################################################
#   Monsters are a type of squads that are a single individual instead of a   #
#     collective entity which can perform tasks and participate in combat.    #
#              Monsters perform Squad actions and assist actions.             #
#  Monster Health stats represent taking wounds w/out performance degradation #
###############################################################################
class Monster(Squad, Entity):
    # Monster Attributes
    def __init__(self, damage_reduction, health, max_health, offense, defense, strength, race, level, level_experience, cost, upkeep, speed_combat, max_weapons, max_tools, weapons_equipped, tools_equipped, mounts_equipped, racial_ability, unique, damage_chart, available_actions, morale_status, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned):
        # Monsters need ALL attributes of the Entity parent class.
        # Monsters need MOST of the squad attributes:
        ## Exception: override the damage_chart from Squads.
        super().__init__(health, max_health, offense, defense, strength, race, level, level_experience, cost, upkeep, speed_combat, max_weapons, max_tools, weapons_equipped, tools_equipped, mounts_equipped, racial_ability, unique, damage_chart, available_actions, morale_status, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned)
        # This stat is somehow not working in the current PAPER version of the
        # game.  I'm not sure how this went 100% unnoticed during playtesting.
        self.damage_reduction = damage_reduction
        # self.health = health
        # Monsters get their own health and max health because they have
        # different base values than standard Squads.  Usually 2-3 Health.
        # self.max_health = max_health

        # I should probably be replaced by a variable name that is pertinent
        # to Monster squads.
        # "Monster_Damage_Chart"
        # self.damage_chart = damage_chart

    def convert_to_unique_monster(self):
        '''
        Should be called whenever a situation results in a Monster squad
        becoming unique.  Usually as a result of a landmark or capture roll.
        '''
        pass

###############################################################################
#  Legendary Monsters are Non-Player Characters (NPC) that function similarly #
#                              to Monsters.                                   #
# Legendary Monsters have additional features that persist outside of normal  #
# combat that can affect the scope of the game even when not actively in use. #
#       Legendary Monsters are always treated as being in an inaccessible     #
#               grid_location (such as Z0), except during combat.             #
###############################################################################
class LegendaryMonster(Monster, Squad, Entity):
    # Legendary Monster Attributes
    def __init__(self, spawn_trigger, world_effect, no_morale, unique_flag, damage_reduction, health, max_health, offense, defense, strength, race, level, level_experience, cost, upkeep, speed_combat, max_weapons, max_tools, weapons_equipped, tools_equipped, mounts_equipped, racial_ability, unique, damage_chart, available_actions, morale_status, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned):
        # Legendary Monsters need ALL attributes of the Entity parent class.
        # Legendary Monsters need MOST of the squad attributes:
        ## Exception: override the damage_chart from Squads.
        ## Exception: override the available_actions from Squads
        ## Exception: Legendary Monsters NEVER make Morale checks.  E V E R
        ## Exception: override the default for unique.  All legendary Monsters
        ## are unique.
        super().__init__(damage_reduction, health, max_health, offense, defense, strength, race, level, level_experience, cost, upkeep, speed_combat, max_weapons, max_tools, weapons_equipped, tools_equipped, mounts_equipped, racial_ability, unique, damage_chart, available_actions, morale_status, name, grid_location, team, traits, speed_overland, spells_known, skills_known, abilities_learned)
        # This should be replaced with an actual variable.
        # This default should be MODIFIED based on game DIFFICULTY settings.
        # The result here is "standard" difficulty.
        # Default: "Victory Point Threshold 5"
        self.spawn_trigger = spawn_trigger
        self.world_effect = world_effect
        # Legendary Monsters never roll Morale Checks.
        # Any effect which would normally target the Legendary Monster for a
        # Morale check is instead cancelled/ignored.
        self.no_morale = no_morale
        # Legendary Monsters take no actions.
        # Each week they apply their world effects and await combat.
        # self.available_actions = available_actions = None
        # This is set to False until the given Legendary Monster is DISCOVERED.
        # Discovered simply references to being "generated" at any point in
        # the game.
        # If this Legendary Monster is generated during a spawn trigger result, # then that Legendary Monster may NEVER be spawned again. (remove it
        # from all future instances of being "rolled" in this game instance.)
        self.unique_flag = unique_flag
        # Legendary Monsters are always Unique.
        # self.unique = unique
        # Legendary Monsters don't need an actual overland speed, they simply
        # arrive at whatever grid location they are needed for combat.
        # 1000 should be sufficient for any map/situation.
        self.speed_overland = speed_overland
        # All Legendary Monsters override the base level rule.
        # Legendary Monsters are always treated as being maximum level.
        # Maximum level is 10.
        # self.level = level

    def generate_world_effect(self):
        '''
        I feel like... this may need to be a "per legendary monster" thing with a function for each, as they are radically different.
        '''
        pass
