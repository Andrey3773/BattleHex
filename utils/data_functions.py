from json import load

def load_unit_data(unit_name: str) -> dict:
    """
    Загружает все данные юнита по ключу в JSON, возвращает словарь с этими данными
    :param unit_name:
    :return:
    """

    with open('data/game_data/units.json', 'r', encoding='utf-8') as file:
        return load(file)[unit_name]


def load_field_data(key: str) -> str:
    """
    Загружает из JSON данные поля
    Пока что функция довольно глупая, потому что у поля особо нет данных

    :param key:
    :return:
    """

    with open('data/game_data/field.json', 'r', encoding='utf-8') as file:
        return load(file)[key]

