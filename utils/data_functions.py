from json import load

def load_unit_data(unit_name: str) -> dict:
    with open('data/game_data/units.json', 'r', encoding='utf-8') as file:
        return load(file)[unit_name]

