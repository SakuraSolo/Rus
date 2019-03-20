# Castle dungeon
label dungeon:
    call screen room_screen('bg dungeon', 'andras room',
        (('Talk', '_operator_talk'),
        ('Visit', 'pass'),
        ('Manage prisoners', 'manage_prisoners'),
        ),
        'andras_dungeon')
    return


label dungeon_visit:
    'dungeon visit'
    jump dungeon


label manage_prisoners:
    call screen manage_prisoners_screen
    jump dungeon
