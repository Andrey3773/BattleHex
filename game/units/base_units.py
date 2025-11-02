from random import randint
from numpy import sign
from abc import ABC
from typing import Dict, TYPE_CHECKING
from game.field.position import Position


if TYPE_CHECKING:
    from game.field.buttle_field import BattleField


class Unit(ABC):
    def __init__(self, unit_data: dict, position: Position):
        self.name = unit_data["name"]
        self.type = unit_data["type"]
        self.health = unit_data["health"]
        self.max_health = unit_data["health"]  # для полоски здоровья
        self.attack_value = unit_data["attack"]
        self.defense = unit_data["defense"]
        self.damage_min = unit_data["damage_min"]
        self.damage_max = unit_data["damage_max"]
        self.speed = unit_data["speed"]
        self.icon = unit_data["icon"]
        self.position = position
        self.alive = True

        # TODO тут проблема, непонятно, пихать его сюда или иначе сделать
        self.range = unit_data.get("range", 1)


    def die(self, battlefield: 'BattleField'):
        self.alive = False
        self.health = 0
        battlefield.remove_unit(self)


    def _calculate_damage_to_target(self, target: 'Unit'):
        base_damage = randint(self.damage_min, self.damage_max)
        attack_defense_difference = self.attack_value - target.defense
        damage = base_damage * (
                (1 + 0.05 * sign(attack_defense_difference))
                ** min(abs(attack_defense_difference), 20)
        )
        return max(int(1), int(damage))


    def can_attack(self, target: 'Unit', battlefield: 'BattleField'):
        if not self.alive or not target.alive:
            return False

        distance = battlefield.get_distance(self.position, target.position)
        return distance <= self.range


    def attack(self, target: 'Unit', battlefield: 'BattleField'):
        if not self.can_attack(target, battlefield):
            return 0

        damage = self._calculate_damage_to_target(target)
        target.health -= damage
        print(f"Юнит {self.name} атакует юнита {target.name} и наносит {damage} урона")

        if target.health <= 0:
            print(f"Юнит {target.name} умирает")
            target.die(battlefield)

        return damage


    def __str__(self):
        return self.icon


class Infantry(Unit):
    def __init__(self, unit_data: Dict, position: Position):
        super().__init__(unit_data, position)


class Shooter(Unit):
    def __init__(self, unit_data: Dict, position: Position):
        super().__init__(unit_data, position)
        self.ammo = unit_data.get("ammo", 10)
        self.range = unit_data.get("range", 5)
        self.melee_penalty = unit_data.get("melee_penalty", 0.6)


    def can_attack(self, target: 'Unit', battlefield: 'BattleField'):
        if not self.alive or not target.alive:
            return False

        distance = battlefield.get_distance(self.position, target.position)

        if distance <= self.range and self.ammo > 0:
            return True

        if distance <= 1:
            return True

        return False


    def attack(self, target: 'Unit', battlefield: 'BattleField'):
        if not self.can_attack(target, battlefield):
            return 0

        distance = battlefield.get_distance(self.position, target.position)
        is_melee = distance <= 1 or self.ammo <= 0

        original_damage = self._calculate_damage_to_target(target)

        if is_melee:
            real_damage = int(original_damage * self.melee_penalty)
        else:
            real_damage = original_damage
            self.ammo -= 1

        real_damage = max(1, real_damage)
        target.health -= real_damage
        print(f"Юнит {self.name} атакует юнита {target.name} и наносит {real_damage} урона")
        if target.health <= 0:
            print(f"Юнит {target.name} умирает")
            target.die(battlefield)

        return real_damage



# class Flyer(Unit):
#     def __init__(self, unit_data: Dict, position: Position):
#         super().__init__(unit_data, position)
#         self.can_fly_over_obstacles = True
#TODO было принято решение пока что положить ХУЙ на летучих