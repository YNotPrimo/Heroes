from abc import ABC

from custom_errors.invalidEnergyError import InvalidEnergyError
from custom_errors.invalidHealthError import InvalidHealthError
from heroes.base_hero import Hero


class Swordmaster(Hero, ABC):
    def __init__(self, name, health, energy):
        super().__init__(name, energy)
        self.__set_health(health)

    @classmethod
    def __set_health(cls, health):
        if health <= 0 or health > 200:
            raise InvalidHealthError()
        cls.__health = health

    @classmethod
    def __set_energy(cls, energy):
        if energy <= 0 or energy > 200:
            raise InvalidEnergyError()
        cls.__energy = energy
