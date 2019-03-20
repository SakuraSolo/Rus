# definitions for rumors and rumors texts
label create_rumors:
    python:
        Rumor('Goblin prince Tue-Row', sources=('rosaria', 'village', 'tavern'), state='available', priority=True)
        Rumor('Famine looms', sources=('rosaria', 'village'), state='available')
        Rumor('Orcs in the North', sources=('rosaria', 'village'), state='available')
        Rumor('Dark elf civil war', sources=('ealoean_informant', 'tavern'), kind='active')
    return
