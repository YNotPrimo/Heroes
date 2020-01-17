from abc import ABC

from custom_errors import energyTooHighError
from custom_errors import invalidEnergyError
from custom_errors import invalidHealthError
from custom_errors import invalidNameError
from custom_errors import skillExistsError
from custom_errors import skillNotPresentError
from custom_errors.energyTooHighError import EnergyTooHighError
from custom_errors.invalidEnergyError import InvalidEnergyError
from custom_errors.invalidHealthError import InvalidHealthError
from custom_errors.invalidNameError import InvalidNameError
from custom_errors.skillExistsError import SkillExistsError
from custom_errors.skillNotPresentError import SkillNotPresentError


class Hero(ABC):
    def __init__(self, name, health, energy):
        self.__name = name
        self.__set_health(health)
        self.__energy = int(energy)
        self.__weapon = ""
        self.__armour = ""
        self.__spells = {}
        self.__passives = {}

    def name(self):
        return self.__name

    def __set_name(self, name):
        if 2 > len(name) > 50:
            raise InvalidNameError(invalidNameError.msg())
        self.__name = name

    def health(self):
        return self.__health

    def __set_health(self, health):
        min = self.__min_health()
        max = self.__max_health()
        if health <= 0 or health > 100:
            raise InvalidHealthError(invalidHealthError.msg())
        self.__health = health

    @classmethod
    def __min_health(cls):
        #TODO and MAX HEALTH
        return a

    def energy(self):
        return self.__energy

    @classmethod
    def __set_energy(cls, energy):
        if energy <= 0 or energy > 100:
            raise InvalidEnergyError(invalidEnergyError.msg())
        cls.__energy = energy

    def weapon(self):
        return self.__weapon

    @classmethod
    def __set_weapon(cls, weapon):
        cls.__weapon = weapon

    def armour(self):
        return self.__armour

    @classmethod
    def __set_armour(cls, armour):
        cls.__armour = armour

    def get_spells(self):
        return self.__spells

    def learn_spell(self, name, energy, damage):
        if energy > self.energy:
            raise EnergyTooHighError(energyTooHighError.msg())

        for x in self.get_spells().keys():
            if x == name:
                raise SkillExistsError(skillExistsError.msg())

        self.get_spells()[name] = [energy, damage]
        return f"You've learned a new spell! {name}: {energy} energy cost and {damage} damage output"

    def forget_spell(self, name):
        for x in self.get_spells().keys():
            if x == name:
                del self.get_spells()[name]
                return f"The spell, {name}, is forgotten"

        raise SkillNotPresentError(skillNotPresentError.msg())

    def get_passives(self):
        return self.__passives

    def learn_passive(self, name, energy, amp, skill):
        skill_is_present = False
        if energy > self.energy:
            raise EnergyTooHighError(energyTooHighError.msg())

        for x in self.get_passives().keys():
            if x == name:
                raise SkillExistsError(skillExistsError.msg())

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

        raise SkillNotPresentError(skillNotPresentError.msg())
