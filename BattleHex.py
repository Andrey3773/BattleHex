def main():
    from core.logging.logger import Logger

    # logger = Logger(__name__)


    from game.units.unit_factory import UnitFactory
    from game.field.position import Position
    from game.field.battle_field import BattleField
    from game.manager.battle_manager import BattleManager

    pikeman = UnitFactory.create('pikeman', Position(0)) #TODO хардкод-мерзость имени, хочется исправить
    archer = UnitFactory.create('archer', Position(24))
    # logger.info('юниты созданы')

    battlefield = BattleField(25)
    # logger.info('поле создано')


    battle = BattleManager(battlefield)

    battle.run(pikeman, archer)


if __name__ == "__main__":
    main()
