# Author: Kenny Seng
# Date: 1/7/2020
# Description: Program that lists out each stat type (base stats, advanced stats, elemental types) and respective sub-fields.

class base_stats:
    """Represents a Character's max hp, atk, defense, elemental mastery, and max stamina, 0 by default."""

    def __init__(self, max_hp=0, atk=0, defense=0, elem_mastery=0, max_stamina=0):
        """Represents the base stats of the Character """
        self.__max_hp = max_hp
        self.__atk = atk
        self.__defense = defense
        self.__elem_mastery = elem_mastery
        self.__max_stamina = max_stamina

    def get_max_hp(self):
        """Returns max hp"""
        return self.__max_hp

    def set_max_hp(self, new_max_hp=0):
        """Sets max hp, 0 by default"""
        self.__max_hp = new_max_hp

    def get_atk(self):
        """Returns atk"""
        return self.__atk

    def set_atk(self, new_atk=0):
        """Sets atk, 0 by default"""
        self.__atk = new_atk

    def get_defense(self):
        """Returns defense"""
        return self.__defense

    def set_defense(self, new_defense=0):
        """Sets defense, 0 by default"""
        self.__defense = new_defense

    def get_elem_mastery(self):
        """Returns elemental mastery"""
        return self.__elem_mastery

    def set_elem_mastery(self, new_elem_mastery=0):
        """Sets elemental mastery, 0 by default"""
        self.__elem_mastery = new_elem_mastery

    def get_max_stamina(self):
        """Returns max stamina"""
        return self.__max_stamina

    def set_max_stamina(self, new_max_stamina=0):
        """Sets max stamina, 0 by default"""
        self.__max_stamina = new_max_stamina

    def set_base_stats(self, new_max_hp=0, new_atk=0, new_defense=0, new_elem_mastery=0, new_max_stamina=0):
        """Sets the base stats of the character with the specified values (0 by default for all fields)"""
        self.__max_hp = new_max_hp
        self.__atk = new_atk
        self.__defense = new_defense
        self.__elem_mastery = new_elem_mastery
        self.__max_stamina = new_max_stamina

    def print_base_stats(self):
        """Prints Base Stats"""
        print(" Base Stats:")
        print("  Max HP: " + str(base_stats.get_max_hp(self)))
        print("  ATK: " + str(base_stats.get_atk(self)))
        print("  DEF: " + str(base_stats.get_defense(self)))
        print("  Elemental Mastery: " + str(base_stats.get_elem_mastery(self)))
        print("  Max Stamina: " + str(base_stats.get_max_stamina(self)))


class adv_stats:
    """Represents the Character's crit rate, crit dmg, healing bonus, incoming healing bonus, energy recharge, reduce cd, and powerful shield, 0 by default"""

    def __init__(self, crit_rate=0, crit_dmg=0, healing_bonus=0, incoming_healing_bonus=0, energy_recharge=0, reduce_cd=0, powerful_shield=0):
        """Represents the advanced stats of the Character """
        self.__crit_rate = crit_rate
        self.__crit_dmg = crit_dmg
        self.__healing_bonus = healing_bonus
        self.__incoming_healing_bonus = incoming_healing_bonus
        self.__energy_recharge = energy_recharge
        self.__reduce_cd = reduce_cd
        self.__powerful_shield = powerful_shield

    def get_crit_rate(self):
        """Returns critical rate %"""
        return self.__crit_rate

    def set_crit_rate(self, new_crit_rate=0):
        """Sets critical rate %, 0 by default"""
        self.__crit_rate = new_crit_rate

    def get_crit_dmg(self):
        """Returns critical damage %"""
        return self.__crit_dmg

    def set_crit_dmg(self, new_crit_dmg=0):
        """Sets critical damage %, 0 by default"""
        self.__crit_dmg = new_crit_dmg

    def get_healing_bonus(self):
        """Returns healing bonus"""
        return self.__healing_bonus

    def set_healing_bonus(self, new_healing_bonus=0):
        """Sets healing bonus, 0 by default"""
        self.__healing_bonus = new_healing_bonus

    def get_incoming_healing_bonus(self):
        """Returns incoming healing bonus"""
        return self.__incoming_healing_bonus

    def set_incoming_healing_bonus(self, new_incoming_healing_bonus=0):
        """Sets incoming healing bonus, 0 by default"""
        self.__incoming_healing_bonus = new_incoming_healing_bonus

    def get_energy_recharge(self):
        """Returns energy recharge"""
        return self.__energy_recharge

    def set_energy_recharge(self, new_energy_recharge=0):
        """Sets energy recharge, 0 by default"""
        self.__energy_recharge = new_energy_recharge

    def get_reduce_cd(self):
        """Returns reduce cd"""
        return self.__reduce_cd

    def set_reduce_cd(self, new_reduce_cd=0):
        """Sets reduce cd, 0 by default"""
        self.__reduce_cd = new_reduce_cd

    def get_powerful_shield(self):
        """Returns powerful shield"""
        return self.__powerful_shield

    def set_powerful_shield(self, new_powerful_shield=0):
        """Sets powerful shield, 0 by default"""
        self.__powerful_shield = new_powerful_shield

    def set_adv_stats(self, new_crit_rate=0, new_crit_dmg=0, new_healing_bonus=0, new_incoming_healing_bonus=0, new_energy_recharge=0, new_reduce_cd=0, new_powerful_shield=0):
        """Sets the advanced stats of the character with the specified values (0 by default for all fields)"""
        self.__crit_rate = new_crit_rate
        self.__crit_dmg = new_crit_dmg
        self.__healing_bonus = new_healing_bonus
        self.__incoming_healing_bonus = new_incoming_healing_bonus
        self.__energy_recharge = new_energy_recharge
        self.__reduce_cd = new_reduce_cd
        self.__powerful_shield = new_powerful_shield

    def print_adv_stats(self):
        print(" Advanced Stats: ")
        print("  CRIT Rate: " + str(adv_stats.get_crit_rate(self)))
        print("  CRIT DMG: " + str(adv_stats.get_crit_dmg(self)))
        print("  Healing Bonus: " + str(adv_stats.get_healing_bonus(self)))
        print("  Incoming Healing Bonus: " + str(adv_stats.get_incoming_healing_bonus(self)))
        print("  Energy Recharge: " + str(adv_stats.get_energy_recharge(self)))
        print("  Reduce CD: " + str(adv_stats.get_reduce_cd(self)))
        print("  Powerful Shield: " + str(adv_stats.get_powerful_shield(self)))


class elem_type:
    """Represents the Character's elemental damage bonuses and elemental resistances, 0 by default."""

    def __init__(self, pyro_dmg_bonus=0, pyro_res=0,
                       hydro_dmg_bonus=0, hydro_res=0,
                       dendro_dmg_bonus=0, dendro_res=0,
                       electro_dmg_bonus=0, electro_res=0,
                       anemo_dmg_bonus=0, anemo_res=0,
                       cryo_dmg_bonus=0, cryo_res=0,
                       geo_dmg_bonus=0, geo_res=0,
                       physical_dmg_bonus=0, physical_res=0):

        self.__pyro_dmg_bonus = pyro_dmg_bonus
        self.__pyro_res = pyro_res

        self.__hydro_dmg_bonus = hydro_dmg_bonus
        self.__hydro_res = hydro_res

        self.__dendro_dmg_bonus = dendro_dmg_bonus
        self.__dendro_res = dendro_res

        self.__electro_dmg_bonus = electro_dmg_bonus
        self.__electro_res = electro_res

        self.__anemo_dmg_bonus = anemo_dmg_bonus
        self.__anemo_res = anemo_res

        self.__cryo_dmg_bonus = cryo_dmg_bonus
        self.__cryo_res = cryo_res

        self.__geo_dmg_bonus = geo_dmg_bonus
        self.__geo_res = geo_res

        self.__physical_dmg_bonus = physical_dmg_bonus
        self.__physical_res = physical_res

    # Pyro
    def get_pyro_dmg_bonus(self):
        """Returns pyro dmg bonus"""
        return self.__pyro_dmg_bonus

    def set_pyro_dmg_bonus(self, new_pyro_dmg_bonus=0):
        """Sets pyro dmg bonus, 0 by default"""
        self.__pyro_dmg_bonus = new_pyro_dmg_bonus

    def get_pyro_res(self):
        """Returns pyro res"""
        return self.__pyro_res

    def set_pyro_res(self, new_pyro_res=0):
        """Sets pyro res, 0 by default"""
        self.__pyro_res = new_pyro_res

    # Hydro
    def get_hydro_dmg_bonus(self):
        """Returns hydro dmg bonus"""
        return self.__hydro_dmg_bonus

    def set_hydro_dmg_bonus(self, new_hydro_dmg_bonus=0):
        """Sets hydro dmg bonus, 0 by default"""
        self.__hydro_dmg_bonus = new_hydro_dmg_bonus

    def get_hydro_res(self):
        """Returns hydro res"""
        return self.__hydro_res

    def set_hydro_res(self, new_hydro_res=0):
        """Sets hydro res, 0 by default"""
        self.__hydro_res = new_hydro_res

    # Dendro
    def get_dendro_dmg_bonus(self):
        """Returns dendro dmg bonus"""
        return self.__dendro_dmg_bonus

    def set_dendro_dmg_bonus(self, new_dendro_dmg_bonus=0):
        """Sets dendro dmg bonus, 0 by default"""
        self.__dendro_dmg_bonus = new_dendro_dmg_bonus

    def get_dendro_res(self):
        """Returns dendro res"""
        return self.__dendro_res

    def set_dendro_res(self, new_dendro_res=0):
        """Sets dendro res, 0 by default"""
        self.__dendro_res = new_dendro_res

    # Electro
    def get_electro_dmg_bonus(self):
        """Returns electro dmg bonus"""
        return self.__electro_dmg_bonus

    def set_electro_dmg_bonus(self, new_electro_dmg_bonus=0):
        """Sets electro dmg bonus, 0 by default"""
        self.__electro_dmg_bonus = new_electro_dmg_bonus

    def get_electro_res(self):
        """Returns electro res"""
        return self.__electro_res

    def set_electro_res(self, new_electro_res=0):
        """Sets electro res, 0 by default"""
        self.__electro_res = new_electro_res

    # Anemo
    def get_anemo_dmg_bonus(self):
        """Returns anemo dmg bonus"""
        return self.__anemo_dmg_bonus

    def set_anemo_dmg_bonus(self, new_anemo_dmg_bonus=0):
        """Sets anemo dmg bonus, 0 by default"""
        self.__anemo_dmg_bonus = new_anemo_dmg_bonus

    def get_anemo_res(self):
        """Returns anemo res"""
        return self.__anemo_res

    def set_anemo_res(self, new_anemo_res=0):
        """Sets anemo res, 0 by default"""
        self.__anemo_res = new_anemo_res

    # Cryo
    def get_cryo_dmg_bonus(self):
        """Returns cryo dmg bonus"""
        return self.__cryo_dmg_bonus

    def set_cryo_dmg_bonus(self, new_cryo_dmg_bonus=0):
        """Sets cryo dmg bonus, 0 by default"""
        self.__cryo_dmg_bonus = new_cryo_dmg_bonus

    def get_cryo_res(self):
        """Returns cryo res"""
        return self.__cryo_res

    def set_cryo_res(self, new_cryo_res=0):
        """Sets cryo res, 0 by default"""
        self.__cryo_res = new_cryo_res

    # Geo
    def get_geo_dmg_bonus(self):
        """Returns geo dmg bonus"""
        return self.__geo_dmg_bonus

    def set_geo_dmg_bonus(self, new_geo_dmg_bonus=0):
        """Sets geo dmg bonus, 0 by default"""
        self.__geo_dmg_bonus = new_geo_dmg_bonus

    def get_geo_res(self):
        """Returns geo res"""
        return self.__geo_res

    def set_geo_res(self, new_geo_res=0):
        """Sets geo res, 0 by default"""
        self.__geo_res = new_geo_res

    # Physical
    def get_physical_dmg_bonus(self):
        """Returns physical dmg bonus"""
        return self.__physical_dmg_bonus
    
    def set_physical_dmg_bonus(self, new_physical_dmg_bonus = 0):
        """Sets physical dmg bonus, 0 by default"""
        self.__physical_dmg_bonus = new_physical_dmg_bonus    

    def get_physical_res(self):
        """Returns physical res"""
        return self.__physical_res

    def set_physical_res(self, new_physical_res = 0):
        """Sets physical res, 0 by default"""
        self.__physical_res = new_physical_res    


    def set_elem_types(self, new_pyro_dmg_bonus = 0,     new_pyro_res = 0,
                             new_hydro_dmg_bonus = 0,    new_hydro_res = 0,
                             new_dendro_dmg_bonus = 0,   new_dendro_res = 0,
                             new_electro_dmg_bonus = 0,  new_electro_res = 0,
                             new_anemo_dmg_bonus = 0,    new_anemo_res = 0, 
                             new_cryo_dmg_bonus = 0,     new_cryo_res = 0,
                             new_geo_dmg_bonus = 0,      new_geo_res = 0,
                             new_physical_dmg_bonus = 0, new_physical_res = 0):
                            
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


    def print_elem_types(self):
        print(" Elemental Types:")
        print("  Pyro DMG Bonus: " + str(elem_type.get_pyro_dmg_bonus(self)))
        print("  Pyro RES: " + str(elem_type.get_pyro_res(self)))
        print("  Hydro DMG Bonus: " + str(elem_type.get_hydro_dmg_bonus(self)))
        print("  Hydro RES: " + str(elem_type.get_hydro_res(self)))
        print("  Dendro DMG Bonus: " + str(elem_type.get_dendro_dmg_bonus(self)))
        print("  Dendro RES: " + str(elem_type.get_dendro_res(self)))
        print("  Electro DMG Bonus: " + str(elem_type.get_electro_dmg_bonus(self)))
        print("  Electro RES: " + str(elem_type.get_electro_res(self)))
        print("  Anemo DMG Bonus: " + str(elem_type.get_anemo_dmg_bonus(self)))
        print("  Anemo RES: " + str(elem_type.get_anemo_res(self)))
        print("  Cryo DMG Bonus: " + str(elem_type.get_cryo_dmg_bonus(self)))
        print("  Cryo RES: " + str(elem_type.get_cryo_res(self)))
        print("  Geo DMG Bonus: " + str(elem_type.get_geo_dmg_bonus(self)))
        print("  Geo RES: " + str(elem_type.get_geo_res(self)))
        print("  Physical DMG Bonus: " + str(elem_type.get_physical_dmg_bonus(self)))
        print("  Physical RES: " + str(elem_type.get_physical_res(self)))

## Testing ##

"""
base_stat_tester = base_stats()
base_stat_tester.print_base_stats()

adv_stat_tester = adv_stats()
adv_stat_tester.print_adv_stats()

elem_type_tester = elem_type()
elem_type_tester.print_elem_types()
"""
