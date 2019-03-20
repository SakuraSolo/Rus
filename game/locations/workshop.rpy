# workshop
label workshop:
    call screen room_screen('bg20', 'skordred room',
        (('Talk', '_operator_talk'),
        ('Build/Upgrade', 'workshop_build'),
        ),
        'skordred')
    return


label workshop_build:
    if systems.building:
        call screen buildings_screen
    jump workshop
