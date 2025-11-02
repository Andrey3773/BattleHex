from game.units.unit_factory import UnitFactory
from game.field.position import Position
from game.field.buttle_field import BattleField

pikeman = UnitFactory.create('pikeman', Position(0)) #TODO хардкод мерзость имени, хочется исправить
archer = UnitFactory.create('archer', Position(14))

battlefield = BattleField(16)

battlefield.add_unit(pikeman)
battlefield.add_unit(archer)

while pikeman.alive and archer.alive:
    if not pikeman.can_attack(archer, battlefield):
        battlefield.move_unit(pikeman, pikeman.position + pikeman.speed)
    else:
        pikeman.attack(archer, battlefield)

    print(battlefield, '\n')

    if archer.can_attack(pikeman, battlefield):
        archer.attack(pikeman, battlefield)
    else:
        battlefield.move_unit(archer, archer.position - archer.speed)

    print(battlefield, '\n')
