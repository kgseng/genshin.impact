# Author: Kenny Seng
# Date: 1/7/2020
# Description: A program that represents the stats of a generic character in Genshin Impact by miHoyo

from stats import base_stats, adv_stats, elem_type

class Details:
    """Represents a Character and their attribute details"""

    def __init__(self, base_stats=base_stats(), adv_stats=adv_stats(), elem_type=elem_type()):
        """Returns Character's details"""
        self.__base_stats = base_stats
        self.__adv_stats = adv_stats
        self.__elem_type = elem_type

    ### Base Stats ###
    def print_base_stats(self):
        """Prints the base stats of the character"""
        self.__base_stats.print_base_stats()
    
    def get_base_stats(self):
        """Returns self.__base_stats"""
        return self.__base_stats

    # restart_base_stats eventually
    def set_base_stats(self, new_max_hp=0, new_atk=0, new_defense=0, new_elem_mastery=0, new_max_stamina=0):
        """Sets the base stats of the character with the specified values (0 by default for all fields)"""
        self.__max_hp = new_max_hp
        self.__atk = new_atk
        self.__defense = new_defense
        self.__elem_mastery = new_elem_mastery
        self.__max_stamina = new_max_stamina

    ### Advanced Stats ###
    def print_adv_stats(self):
        """Prints the advanced stats of the character"""
        self.__adv_stats.print__adv_stats()

    def get_adv_stats(self):
        """Returns self.__adv_stats"""
        return self.__adv_stats

    def set_adv_stats(self, new_crit_rate=0, new_crit_dmg=0, new_healing_bonus=0, new_incoming_healing_bonus=0, new_energy_recharge=0, new_reduce_cd=0, new_powerful_shield=0):
        """Sets the advanced stats of the character with the specified values (0 by default for all fields)"""
        self.__crit_rate = new_crit_rate
        self.__crit_dmg = new_crit_dmg
        self.__healing_bonus = new_healing_bonus
        self.__incoming_healing_bonus = new_incoming_healing_bonus
        self.__energy_recharge = new_energy_recharge
        self.__reduce_cd = new_reduce_cd
        self.__powerful_shield = new_powerful_shield

    ### Elemental Types ###
    def print_elem_type(self):
        """Prints the elemental types of the character"""
        self.__elem_type.print_elem_types()
    
    def get_elem_types(self):
        """Returns self.__elem_type"""
        return self.__elem_type

    def set_elem_types(self, new_pyro_dmg_bonus=0,     new_pyro_res=0,
                       new_hydro_dmg_bonus=0,    new_hydro_res=0,
                       new_dendro_dmg_bonus=0,   new_dendro_res=0,
                       new_electro_dmg_bonus=0,  new_electro_res=0,
                       new_anemo_dmg_bonus=0,    new_anemo_res=0,
                       new_cryo_dmg_bonus=0,     new_cryo_res=0,
                       new_geo_dmg_bonus=0,      new_geo_res=0,
                       new_physical_dmg_bonus=0, new_physical_res=0):
        """Sets the elemental types of the character with the specified valeus (0 by default for all fields)"""
        self.__pyro_dmg_bonus = new_pyro_dmg_bonus
        self.__pyro_res = new_pyro_res
        self.__hydro_dmg_bonus = new_hydro_dmg_bonus
        self.__hydro_res = new_hydro_res
        self.__dendro_dmg_bonus = new_dendro_dmg_bonus
        self.__dendro_res = new_dendro_res
        self.__electro_dmg_bonus = new_electro_dmg_bonus
        self.__electro_res = new_electro_res
        self.__anemo_dmg_bonus = new_anemo_dmg_bonus
        self.__anemo_res = new_anemo_res
        self.__cryo_dmg_bonus = new_cryo_dmg_bonus
        self.__cryo_res = new_cryo_res
        self.__geo_dmg_bonus = new_geo_dmg_bonus
        self.__geo_res = new_geo_res
        self.__physical_dmg_bonus = new_physical_dmg_bonus
        self.__physical_res = new_physical_res

    def print_details(self):
        """Prints the Character's details"""
        #println("Character Details: ")
        self.__base_stats.print_base_stats()
        self.__adv_stats.print_adv_stats()
        self.__elem_type.print_elem_types()
