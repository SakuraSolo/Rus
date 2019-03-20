# definitions for various troop types

init python:
    all_troops = {
        'orc': {'name': 'Orcs',
            'maintenance': 1, 'morale_cost': 0.1, 'strength': 5, 'equip_strength': 5, 'research': 0,
            'type': 'soldier'},
        'cubi': {'name': 'Cubis',
            'maintenance': 4, 'morale_cost': -0.2, 'strength': 10, 'equip_strength': 0, 'research': 0.5,
            'type': 'mage'},
        'drider': {'name': 'Driders',
            'maintenance': 10, 'morale_cost': 0, 'strength': 50, 'equip_strength': 0, 'research': 0,
            'type': 'small_monster'},
    }
