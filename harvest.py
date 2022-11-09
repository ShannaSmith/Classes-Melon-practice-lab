############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code

        self.first_harvest = first_harvest

        self.color = color

        self.is_seedless = is_seedless

        self.is_bestseller = is_bestseller

        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk","1998","green",True,True,"Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas","2003","orange",False,False,"Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren","1996","green",False,False,"Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw","2013","yellow",False,True,"Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with")
        for item in melon_type.pairings:
            print(f"- {item}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_lookup = {}

    for melon_type in melon_types:
        melon_type_lookup[melon_type.code] = melon_type

    return melon_type_lookup


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester, name):
            self.melon_type = melon_type
            self.shape_rating = shape_rating
            self.color_rating = color_rating
            self.field = field
            self.harvester = harvester
            self.name = name


    def is_sellable(self):
        """"melon is able to be sold if both its shape and color
         ratings are greater than 5, and it didn’t come from field 3"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melon_type_by_code = make_melon_type_lookup(make_melon_types())

    melon1 = Melon(melon_type_by_code['yw'],8,7,2,"Sheila","Melon 1")
    melons.append(melon1)

    melon2 = Melon(melon_type_by_code['yw'],3,4,2,"Sheila","Melon 2")
    melons.append(melon2)

    melon3 = Melon(melon_type_by_code['yw'],9,8,3,"Sheila","Melon 3")
    melons.append(melon3)

    melon4 = Melon(melon_type_by_code['cas'],10,6,35,"Sheila","Melon 4")
    melons.append(melon4)

    melon5 = Melon(melon_type_by_code['cren'],8,9,35,"Michael","Melon 5")
    melons.append(melon5)

    melon6 = Melon(melon_type_by_code['cren'],8,2,35,"Michael","Melon 6")
    melons.append(melon6)

    melon7 = Melon(melon_type_by_code['cren'],2,3,4,"Michael","Melon 7")
    melons.append(melon7)

    melon8 = Melon(melon_type_by_code['musk'],6,7,4,"Michael","Melon 8")
    melons.append(melon8)

    melon9 = Melon(melon_type_by_code['yw'],7,10,3,"Sheila","Melon 9")
    melons.append(melon9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sell_status = "CAN BE SOLD"
        else:
            sell_status = "NOT SELLABLE"
        print(f"{melon.name}: Harvested by {melon.harvester} from Field {melon.field} ({sell_status})")






get_sellability_report(make_melons(make_melon_types))



# for item in test_melon_type_lookup.items():
#     print(f"code: {item[0]}, name: {item[1].name}, first harvest: {item[1].first_harvest}") 
#     print(f"color: {item[1].color}, is seedless: {item[1].is_seedless}, is bestseller: {item[1].is_bestseller}")
#     print()
# 
# test = test_melon_type_lookup.items()
# print(test)