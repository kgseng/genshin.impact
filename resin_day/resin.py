# Author: Kenny Seng
# Date: 1/7/2020
# Description: Program that details how to optimize resin usage

import sys
#sys.stdout = open("resin_day.txt", "w")

from datetime import date
from datetime import datetime
my_date = date.today()
# Day of the week (string)
day = my_date.strftime('%A')
# Day of the week (int), refer to day_to_num for conversions
day_num = my_date.weekday()

# Week starts with Monday
def num_to_day (day):
    num_switch = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday",
    }
    return num_switch.get(day, "Invalid day")


class Resin:

    def __init__(self, resin = 160, cap = 160, regen_rate = 0.125):
        self.__resin = resin
        self.__cap = cap
        self.__regen_rate = regen_rate

        # Wolf of the North Challenge Flag
        self.__andrius = False
        # Confront Stormterror Flag
        self.__dvalin = False
        # Enter the Golden House Flag
        self.__childe = False



    def get_resin(self):
        """Returns the player's current resin count"""
        return self.__resin

    def add_resin(self, amount):
        """Increases resin by said amount"""
        self.__resin += amount

    def sub_resin(self, amount):
        """Decreases resin by said amount"""
        self.__resin -= amount

    def get_cap(self):
        """Returns the resin cap"""
        return self.__cap

    def set_cap(self, new_cap):
        """Sets new resin cap"""
        self.__cap = new_cap
    
    def get_regen_rate(self):
        """Returns resin regen rate"""
        return self.__regen_rate

    def set_regen_rate(self, new_regen_rate):
        """Sets new regen rate"""
        self.__regen_rate = new_regen_rate

    def get_andrius(self):
        """Returns 'Wolf of the North Challenge' Flag"""
        return self.__andrius
    
    def set_andrius(self, bool):
        """Sets 'Wolf of the North Challenge' Flag T/F"""
        self.__andrius = bool

    def get_dvalin(self):
        """Returns 'Confront Stormterror' Flag"""
        return self.__dvalin

    def set_dvalin(self, bool):
        """Sets 'Confront Stormterror' Flag"""
        self.__dvalin = bool

    def get_childe(self):
        """Returns 'Enter the Golden House' Flag"""
        return self.__childe

    def set_childe(self, bool):
        """Sets 'Enter the Golden House' Flag"""
        self.__chidle = bool

    def print_day(self):
        """Prints the current day of the week with time"""

        print("Today is " + day + ' ' + str(datetime.now().time()))
        # Week starts with Monday
        day_to_num = {
            0 : "Monday",
            1 : "Tuesday",
            2 : "Wednesday",
            3 : "Thursday",
            4 : "Friday",
            5 : "Saturday",
            6 : "Sunday",
        }
        
    # If 0 do nothing (functionally)
    # Do not allow user to specify > 3
    # if they somehow do print error
    def condense_resin(self, amount=0):
        """Condenses resin by the specified amount (max 3)"""
        if 1 <= amount <= 3:
            for num in range(amount):
                if self.get_resin() >= 40:
                    self.sub_resin(40)
                    print("Condsend forty resin into (1) Condensed Resin")
        else:
            print("Amount not allowed.")

    ### def regen_resin(self, time)
    ### Import Time
    ### For every 8 minutes, increase resin by 1 up to cap of 160
    
    ### def make_condensed_resin
    ### condense resin by specified amount as long as amount < 3

    def talent_book_material(self, day_of_the_week = my_date.strftime('%A')):
        """Prints out the current day's available talent book materials from which domains"""

        print("     Available Talent Book Materials:")

        # Mondays and Thursdays are for Freedom & Prosperity
        if day_num == 0 or day_num == 3:
            print("""          Forsaken Rift: CRYO DOMAIN (Recommended Pyro & Electro)
                Freedom: 
                    Amber
                    Barbara
                    Diona
                    Klee
                    Sucrose
                    Tartaglia
                    Anemo Traveler
                    Geo Traveler
            Taishan Mansion: PYRO DOMAIN (Recommended Hydro, Cryo, & Electro)
                Prosperity: 
                    Keqing
                    Qiqi
                    Ningguang
                    Geo Traveler""")
        # Tuesdays and Fridays are for Resistance & Diligence
        if day_num == 1 or day_num == 4:
            print("""           Forsaken Rift: CRYO DOMAIN (Recommended Pyro & Electro)
                Resistance: 
                    Bennett 
                    Diluc 
                    Jean 
                    Mona 
                    Noelle 
                    Razor 
                    Anemo Traveler
                    Geo Traveler
            Taishan Mansion: PYRO DOMAIN (Recommended Hydro, Cryo, & Electro)
                Diligence: 
                    Chongyun 
                    Ganyu
                    Xiangling
                    Geo Traveler""")
        # Wednesdays and Saturdays are for Ballad & Gold
        if day_num == 2 or day_num == 5:
            print("""          Forsaken Rift: CRYO DOMAIN (Recommended Pyro & Electro)
                Ballad: 
                    Albedo
                    Fischl
                    Kaeya
                    Lisa
                    Venti
                    Anemo Traveler 
                    Geo Traveler
          Taishan Mansion: PYRO DOMAIN (Recommended Hydro, Cryo, & Electro)
                Gold: 
                    Beidou
                    Xingqiu
                    Xinyan
                    Zhongli
                    Geo Traveler""")
        if day_num == 6:
            print("""
                Forsaken Rift: CRYO DOMAIN (Recommended Pyro & Electro)
                Taishan Mansion: PYRO DOMAIN (Recommended Hydro, Cryo, & Electro)
                All access pass! All talent books are available on Sundays!""")


    def weapon_ascension_material(self, day_of_the_week = my_date.strftime('%A')):
        """Prints out the current day's available weapon ascension materials from which domains"""
        print("     Available Weapon Ascension Materials:")
        # Mondays and Thursdays are for Freedom & Prosperity
        if day_num == 0 or day_num == 3:
            print("""                Cecilia Garden: HYDRO DOMAIN (Recommended Cryo, Pyro, & Electro)
                    Tile of Decarabian's Tower
                    Debris of Decarabian's City
                    Fragment of Decarabian's Epic
                    Scattered Piece of Decarabian's Dream
                Hidden Palace of Lianshan Formula: ELECTRO DOMAIN (Recommended Pyro & Cryo)
                    Luminous Sands from Guyun
                    Lustrous Stone from Guyun
                    Relic from Guyun
                    Divine Body from Guyun""")
        # Tuesdays and Fridays are for Resistance & Diligence
        if day_num == 1 or day_num == 4:
            print("""                Cecilia Garden: HYDRO DOMAIN (Recommended Cryo, Pyro, & Electro)
                    Boreal Wolf's Milk Tooth
                    Boreal Wolf's Cracked Tooth
                    Boreal Wolf's Broken Fang
                    Boreal Wolf's Nostalgia
                Hidden Palace of Lianshan Formula: ELECTRO DOMAIN (Recommended Pyro & Cryo)
                    Mist Veiled Lead Elixir
                    Mist Veiled Mercury Elixir
                    Mist Veiled Gold Elixir
                    Mist Veiled Primo Elixir""")
        # Wednesdays and SAturdays are for Ballad & Gold
        if day_num == 2 or day_num == 5:
            print("""                Cecilia Garden: HYDRO DOMAIN (Recommended Cryo, Pyro, & Electro)
                    Fetters of the Dandelion Gladiator
                    Chains of the Dandelion Gladiator
                    Shackles of the Dandelion Gladiator
                    Dream of the Dandelion Gladiator
                Hidden Palace of Lianshan Formula: ELECTRO DOMAIN (Recommended Pyro & Cryo)
                    Grain of Aerosiderite
                    Piece of Aerosiderite
                    Bit of Aerosiderite
                    Chunk of Aerosiderite""")
        if day_num == 6:
            print("""                Cecilia Garden: HYDRO DOMAIN (Recommended Cryo, Pyro, & Electro)
                Hidden Palace of Lianshan Formula: ELECTRO DOMAIN (Recommended Pyro & Cryo)
                All access pass! All weapon ascension materials are available on Sundays!""")


    def claim_boss(self, boss_name):
        # Check Resin
        if self.get_resin() >= 60:
            # Check 'Wolf of the North' Flag
            if boss_name == 'andrius':
                # If uncleared (false)
                if self.get_andrius():
                    # Set cleared (true) and subtract resin
                    self.set_andrius(True)
                    self.sub_resin(60)
                else: # If cleared(true)
                    print("'Wolf of the North' already claimed this week.") 
            # Check 'Confront Stormterror' Flag
            if boss_name == 'dvalin':
                # If uncleared (false)
                if self.get_dvalin:
                    # Set cleared (true) and subtract resin
                    self.set_dvalin(True)
                    self.sub_resin(60)
                else: # If cleared (true)
                    print("'Confront Stormterror' already claimed this week.")
            # Check 'Enter the Golden House' Flag
            elif boss_name == 'childe':
                # If uncleared (false)
                if self.get_childe:
                    # Set as cleared and update resin
                    self.__set_childe(True)
                    self.sub_resin(60)
                else: # If cleared (true)
                    print("'Enter the Golden House' already claimed this week.")

    def print_available_bosses(self):
        print("     Available Bosses:")
        if(self.__andrius == 0):
            print("         Andrius, 'Wolf of the North'")
        if(self.__dvalin == 0):
            print("         Dvalin, 'Confront Stormterror'")
        if(self.__childe == 0):
            print("         Tartaglia, 'Enter the Golden House'")

    def print_all(self):
        self.print_day()
        self.talent_book_material()
        self.weapon_ascension_material()
        self.print_available_bosses()

    def return_all(self):
        return self.print_all()

resin_tester = Resin()
resin_tester.print_all()

# on account page, redirect output to determine if current character roster needs any of the above materials depending on the current character's talent levels