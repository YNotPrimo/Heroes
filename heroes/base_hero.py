from abc import ABC

from custom_errors.energyTooHighError import EnergyTooHighError
from custom_errors.invalidEnergyError import InvalidEnergyError
from custom_errors.invalidHealthError import InvalidHealthError
from custom_errors.invalidNameError import InvalidNameError
from custom_errors.skillExistsError import SkillExistsError
from custom_errors.skillNotPresentError import SkillNotPresentError


class Hero(ABC):
    def __init__(self, name, health, energy):
        self.__name = name
        self.__health = int(health)
        self.__energy = int(energy)
        self.__weapon = ""
        self.__armour = ""
        self.__spells = {}
        self.__passives = {}

    def get_name(self):
        return self.__name

    @classmethod
    def __set_name(cls, name):
        if 2 > len(name) > 50:
            raise InvalidNameError()
        cls.__name = name

    def get_health(self):
        return self.__health

    @classmethod
    def __set_health(cls, health):
        if health <= 0 or health > 100:
            raise InvalidHealthError()
        cls.__health = health

    def get_energy(self):
        return self.__energy

    @classmethod
    def __set_energy(cls, energy):
        if energy <= 0 or energy > 100:
            raise InvalidEnergyError()
        cls.__energy = energy

    def get_weapon(self):
        return self.__weapon

    @classmethod
    def __set_weapon(cls, weapon):
        cls.__weapon = weapon

    def get_armour(self):
        return self.__armour

    @classmethod
    def __set_armour(cls, armour):
        cls.__armour = armour

    def get_spells(self):
        return self.__spells

    def learn_spell(self, name, energy, damage):
        if energy > self.get_energy():
            raise EnergyTooHighError()

        for x in self.get_spells().keys():
            if x == name:
                raise SkillExistsError()

        self.get_spells()[name] = [energy, damage]
        return f"You've learned a new spell! {name}: {energy} energy cost and {damage} damage output"

    def forget_spell(self, name):
        for x in self.get_spells().keys():
            if x == name:
                del self.get_spells()[name]
                return f"The spell, {name}, is forgotten"

        raise SkillNotPresentError()

    def get_passives(self):
        return self.__passives

    def learn_passive(self, name, energy, amp, skill):
        skill_is_present = False
        if energy > self.get_energy():
            raise EnergyTooHighError()

        for x in self.get_passives().keys():
            if x == name:
                raise SkillExistsError()

        for x in self.get_spells().keys():
            if x == skill:
                skill_is_present = True
                break

        if skill_is_present:
            self.get_spells()[name] = [energy, amp, skill]
            return f"You've learned a new passive! {name}: {energy} energy cost. The skill {skill} is amplified by {amp}!"

    def forget_passive(self, name):
        for x in self.get_passives().keys():
            if x == name:
                del self.get_passives()[name]
                return f"The passive, {name}, is forgotten"

        raise SkillNotPresentError()
