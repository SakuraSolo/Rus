# Barracks room
label barracks:
    call screen room_screen('images/Backgrounds/barracks.jpg', 'orc soldier room',
        (('Army report', 'barracks_army_report'),
        ),
        'orc_soldier')
    return


label barracks_army_report:
    call screen orc_barracks_report
#~     'army report'
    jump barracks
