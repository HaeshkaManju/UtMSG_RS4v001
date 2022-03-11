import pyinputplus as pyip
###############################################################################

###############################################################################

class Places:
    # Places Attributes
    def __init__(self, traits):
        self.traits = traits

    # Places Methods
    def placesmethods(self):
        pass

class Map(Places):
    # Map(s) Attributes
    # There is only ever one map per instance of a game, hence the use
    # of a singular in the class name.
    # Not even sure this will need to be a class.
    def __init__(self, size, traits):
        super().__init__(traits)
        self.size = size

    # Map Methods
    def mapmethods(self):
        pass

class Grid(Places):
    # Grid(s) Attributes
    # While a map has many grids within it, they are not a subclass.
    def __init__(self, terrain_type, terrain_name, traits):
        super().__init__(traits)
        self.terrain_type = terrain_type
        self.terrain_name = terrain_name

    # Map Methods
    def gridsmethods(self):
        pass

class Site(Grid, Places):
    # Site Attributes
    def __init__(self, site_type, terrain_type, terrain_name, traits):
        super().__init__(terrain_type, terrain_name, traits)
        self.site_type = site_type

    # Site Methods
    def sitemethods(self):
        pass

class Encounter(Grid, Places):
    # Site Attributes
    def __init__(self, encounter_type, terrain_type, terrain_name, traits):
        super().__init__(terrain_type, terrain_name, traits)
        self.encounter_type = encounter_type

    # Site Methods
    def encountermethods(self):
        pass

class Nodes(Grid, Places):
    # Site Attributes
    def __init__(self, node_type, terrain_type, terrain_name, traits):
        super().__init__(terrain_type, terrain_name, traits)
        self.node_type = node_type

    # Site Methods
    def nodemethods(self):
        pass

class Quest_Markers(Grid, Places):
    # Site Attributes
    def __init__(self, quest_type, terrain_type, terrain_name, traits):
        super().__init__(terrain_type, terrain_name, traits)
        self.quest_type = quest_type

    # Site Methods
    def questmarkermethods(self):
        pass

class Lairs(Grid, Places):
    # Site Attributes
    def __init__(self, lair_team, lair_id, obscurity_rating, obscurity_max, terrain_type, terrain_name, traits):
        super().__init__(terrain_type, terrain_name, traits)
        # Not sure if this one is strictly necessary.
        # This should simply match the Usurpation ID.
        self.lair_team = lair_team
        self.lair_id = lair_id
        # Default starts to match the obscurity max.
        self.obscurity_rating = obscurity_rating
        # Default starts at 250.  Adjusts based on game difficulty.
        self.obscurity_max = obscurity_max

    # Site Methods
    def lairmethods(self):
        pass

class Rooms(Lairs, Grid, Places):
    # Site Attributes
    def __init__(self, room_type, lair_team, lair_id, terrain_type, terrain_name, traits):
        super().__init__(lair_team, lair_id, terrain_type, terrain_name, traits)
        self.room_type = room_type

    # Site Methods
    def lairmethods(self):
        pass
