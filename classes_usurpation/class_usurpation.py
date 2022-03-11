import pyinputplus as pyip
###############################################################################

###############################################################################

class Usurpations:
    # Usurpations Attributes
    def __init__(self, player_id, gold, usurpation_abilities, victory_points):
        self.player_id = player_id
        self.gold = gold
        self.usurpation_abilities = usurpation_abilities
        self.victory_points = victory_points

    # Usurpations Methods
    def usurpation_methods(self):
        pass

    def calculate_victory_points(self):
        '''
        Should be used to calculate the victory points of each individual player's Usurpation.
        There are multiple categories: Might, Lair, Economy, Mysterium, and Politics.
        Totals should be given both by individual category and by sum of all categories.
        Sum of all categories is used to check for the "Victory by Accrual" condition, as well as assess the current game progress counter.
        Might:
            1/2 GP Value of Units
            Skills: 1 point per rank (combat skills)
            Skills: 2 points per rank (advanced combat skills)
            Levels: 1 point per level
            Weapons/Armor: 1/4 GP value + 1 per quality* (equipped only)
        Lair:
            4 points per Room (beyond 1st Throne Room)
            2 points per Renovation level (beyond 1st)
            1 points per Mason/Artisan rank (does not include Extras.)
            1 points per Prisoner ever held.
            2x points per Unique event completed (x = inverse of place of completion, 1st-4th only)
        Economy:
            1/4 Gold Value of Tools (equipped only)
            1 points per quality of Tools possessed (included embedded)
            1 point per Rank in Scout/Recon/Harvest Skills
            5 points per title
            1 point per 10 Gold in Coffers
            1 point per 20 Resources in Storage.
        Mysterium:
            4 x # of Spells Known. (includes Extras)
            Each = 4 x Rank of Artifact
            1 x # of spaces in Mysterious Room
            2 x # of possessed Special Abilities owned (aside from Extras)
            2 x # of possessed Unique Abilities owned (aside from Extras)
        Politics:
            Extras: 1 points per skill rank (basic skills)
            Extras: 2 points per skill rank (advanced skills)
            Extras: 1 points for each possessed Special abilities (non-trainable)
            Extras: 2 points for each possessed Special abilities (trainable)
            Extras: 3 points for each possessed Unique abilities
            1 point per level of positive CP Diplomacy (status above indifferent)
            Fanatical Status: 2 * Size
            Negotiator/Bard = 1 points per Skill Rank
        '''
        pass

class KnownData(Usurpations):
    # KnownData Attributes
    # The data here will mostly be used to populate a player's JOURNAL page.
    # Some of the information (encounters/nodes) will be used to populate
    # each individual player's view of the game map.
    def __init__(self, settlements_discovered, heroes_discovered, noble_houses_discovered, nodes_known, quests_in_progress, quests_completed, encounters_known, landmark_thresholds_completed, player_id, gold, usurpation_abilities, victory_points):
        super().__init__(player_id, gold, usurpation_abilities, victory_points)
        # All "_discovered" are lists.
        self.settlements_discovered = settlements_discovered
        self.heroes_discovered = heroes_discovered
        self.noble_houses_discovered = noble_houses_discovered
        self.nodes_discovered = nodes_known
        self.quests_in_progress = quests_in_progress
        self.quests_completed = quests_completed
        self.encounters_discovered = encounters_known
        self.landmark_thresholds_completed = landmark_thresholds_completed

    # KnownData Methods
    def knowndata_methods(self):
        pass

        # Okay, so I initially wrote this as "add_encounter", but how about rather than one method for each of these... maybe one pair of methods that do all of the map adding together.  This will require more data pushed into the arguments, but will be more succinct code-wise.
    def add_indicator_to_player_map(self):
        '''
        Should be called whenever a scout check (or any game situation) results
        in the player learning about a new encounter at a given grid location.
        Adds the encounter to the player's list of encounters_known.
        Allows the player to access the information within their journal page.
        Allows the player to maintain understanding of which penalties (and targets) will be relevent to their activities.
        Should maybe use some sort of "visible to player" flag, so I don't have to rewrite a bunch of code for each player.
        '''
        pass

    def remove_indicatator_from_player_map(self):
        '''
        Should be called whenever an encounter is defeated (or any other game situation resulting in an encounter no longer being relevent on the game map.)
        Removes the encounter from the player's list of encounters_known.
        Allows the player to maintain understanding of which penalties (and targets) will be relevent to their activities.
        '''
        pass

    def add_discovery(self):
        '''
        Should be called whenever a new, durable datapoint is discovered, by a given player.
        These include: settlements, noble houses, nodes, quests, and encounters.
        Adds that discovery to the player's individual _discovered lists.
        A discovery is only made known to that given player.
        Example: PlayerBob enters the market in Havenin (a City).  The system generates that House Gurd'an is one of the ruling houses.  This information would be added to the list of known datapoints for that player.
        '''
        pass

    def add_completed_quest(self):
        '''
        Should be called whenever a player has completed (either through success or failure) a quest.
        These can be either settlement and/or landmark quests.
        Should add the completion indicator to the player's list.
        When viewing the journal, the player should be able to see whether they succeeded or failed in the quest.
        If successful, the player should be able to view the reward.
        This function should only handle the actual adding of the question completion indicator to the list.
        '''
        pass
