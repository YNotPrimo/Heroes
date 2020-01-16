from abc import ABC

from custom_errors.invalidEnergyError import InvalidEnergyError
from custom_errors.invalidHealthError import InvalidHealthError
from heroes.base_hero import Hero


class Swordmaster(Hero, ABC):
    def __init__(self, name, health, energy):
        super().__init__(name, health, energy)

    def __set_health(self, health):
        if health <= 0 or health > 200:
            raise InvalidHealthError()
        self.__health = health

    def __set_energy(self, energy):
        if energy <= 0 or energy > 200:
            raise InvalidEnergyError()
        self.__energy = energy
