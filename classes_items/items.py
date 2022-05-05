import pyinputplus as pyip
###############################################################################
#      Items is the base class from which all stored, inanimate objects       #
#                          are Inherited in Usurper.                          #
# Stored refers to the non-abstraction wherein an item must be embedded       #
#                 (associated) into a location that has "slots".              #
###############################################################################

# Who does what?!?!?
# Does an item put itself into a storage slot?
# Does the equipping Squad put an item onto itself?
# Do warehouses store items ??!?!?

# Items (take up space, have a name, and a type)
# Items -> Craftables -> Tools, Weapons, Armor (bought, sold, made, AND has various activity bonuses)
# Items -> Artifacts (not bought/sold)
# Items -> Mounts (not crafted, but still bought/sold, has activity bonuses)
# Items -> Resources (different storage ratios than craftables.)

###############################################################################
# Items (take up space, have a name, and a type)
###############################################################################
class Items:
    # Items Static attributes

    # Items attributes
    def __init__(self):
        self.? = ?

    # Items Methods
    def ?(self):
        pass

###############################################################################
# Items -> Craftables
# (bought, sold, and made)
###############################################################################
class Craftables(Items):
    # Craftables Static attributes

    # Craftables attributes
    def __init__(self):
        super().__init__():
        self.? = ?

    # Craftables Methods
    def ?(self):
        pass

###############################################################################
# Items -> Craftables -> Tools
# (bought, sold, made, AND has various activity bonuses)
###############################################################################
class Tools(Items, Craftables):
    # Tools Static attributes

    # Tools attributes
    def __init__(self):
        super().__init__():
        self.? = ?

    # Tools Methods
    def ?(self):
        pass

###############################################################################
# Items -> Craftables -> Weapons
# (bought, sold, made, AND has various activity bonuses)
###############################################################################
class Weapons(Items, Craftables):
    # Weapons Static attributes

    # Weapons attributes
    def __init__(self):
        super().__init__():
        self.? = ?

    # Weapons Methods
    def ?(self):
        pass

###############################################################################
# Items -> Craftables -> Armor
# (bought, sold, made, AND has various activity bonuses)
###############################################################################
class Armor(Items, Craftables):
    # Armor Static attributes

    # Armor attributes
    def __init__(self):
        super().__init__():
        self.? = ?

    # Armor Methods
    def ?(self):
        pass

###############################################################################
# Items -> Artifacts
# (not bought/sold)
# only go into leader carry slots or into reliquary slots.
###############################################################################
class Artifacts(Items):
    # Artifacts Static attributes

    # Artifacts attributes
    def __init__(self):
        super().__init__():
        self.? = ?

    # Artifacts Methods
    def ?(self):
        pass

###############################################################################
# Items -> Resources (different storage ratios than craftables.)
###############################################################################
class Resources(Items):
    # Artifacts Static attributes

    # Artifacts attributes
    def __init__(self):
        super().__init__():
        self.? = ?

    # Artifacts Methods
    def ?(self):
        pass



class Items:
    # Items attributes
    def __init__(self, name, item_type, purchasable, sellable):
        self.name = name
        self.item_type = item_type
        # Not every item can be purchased from the Marketplace
        self.purchasable = purchasable
        # Artifacts can never be sold.
        # Some items (such as those with "Powerful" quality, cannot be sold.)
        self.sellable = sellable

    # Item Methods
    def purchase_item(self):
        '''
        Should be called whenever a player seeks to purchase an item in
        the marketplace.
        Should be used to...?
        '''
        pass

    def sell_item(self):
        '''

        '''
        pass

class Craftables(Items):
    # Craftables attributes
    def __init__(self, storage_ratio, craft_ingredients, quality_level, quality_bonus)

class Tools(Items):
    # Tool Attributes
    def __init__(self, tool_action_bonuses, storage_ratio):
        super().__init__(name, item_type)
        self.tool_action_bonuses = tool_action_bonuses
        self.storage_ratio = storage_ratio

    # Tool Methods
    def stuff1(self):
        pass

class Weapons(Items):
    # Weapon Attributes
    def __init__(self, weapon_combat_bonuses, storage_ratio):
        super().__init__(name, item_type)
        # Is this a logical way to set up the stats?
        # Or should it be a per bonus?
        # or a per kind (dice pool + flat bonus)?
        self.weapon_combat_bonuses = weapon_combat_bonuses
        self.storage_ratio = storage_ratio

    # Weapon Methods
    def stuff2(self):
        pass

class Armor(Items):
    # Armor Attributes
    def __init__(self, armor_combat_bonuses, storage_ratio):
        super().__init__(name, item_type)
        self.armor_combat_bonuses = armor_combat_bonuses
        self.storage_ratio = storage_ratio

    # Armor Methods
    def stuff3(self):
        pass

class Mounts(Items):
    # Mounts Attributes
    ### Do Mounts make sense as items?!  They have an upkeep requirement...
    def __init__(self, mounts_combat_bonuses, mounts_speed_bonus):
        super().__init__(name, item_type)
        self.mounts_combat_bonuses = mounts_combat_bonuses
        self.mounts_speed_bonus = mounts_speed_bonus
        self.storage_ratio = storage_ratio

    # Mounts Methods
    def stuff4(self):
        pass

class Artifacts(Items):
    # Artifacts Attributes
    def __init__(self, tier, housed_bonuses, carried_bonuses):
        super().__init__(name, item_type)
        self.tier = tier
        self.housed_bonuses = housed_bonuses
        self.carried_bonuses = carried_bonuses
        self.storage_ratio = storage_ratio

    # Artifacts Methods
    def stuff5(self):
        pass

class Resources(Items):
    # Resources Attributes
    def __init__(self, high_quality, storage_ratio):
        super().__init__(name, item_type)
        # There are four standard resources and five high quality resources.
        # Lumber, Stone, Iron, and Foodstuffs
        # Erebove, Libcite, Mithril, Cured Rations, and Gems
        # This is a bool
        self.high_quality = high_quality
        # Should be expressed as a dictionary.
        # '1 Storage Slot':"X of Resource"
        self.storage_ratio = storage_ratio


    # Resources Methods
    def stuff6(self):
        pass
