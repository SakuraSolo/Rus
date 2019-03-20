# dark sanctum
label sanctum:
    call screen room_screen('bg23', 'xzaratl room',
        (('Talk', '_operator_talk'),
        ('Cubi report', 'sanctum_report'),
        ),
        'x_zaratl')
    return


label sanctum_report:
    call screen dark_sanctum_report
#~     'sanctum_report'
    jump sanctum
