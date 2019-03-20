# Breeding pits of the castle
label pit:
    call screen room_screen('bg25', 'draith room',
        (('Talk', '_operator_talk'),
        ('Fuck Draith', PitFuckDraith()),
        ('Monsters report', 'pits_report'),
        ),
        'draith')
    return


label pits_report:
    'pits_report'
    jump pit


init python:

    class PitFuckDraith(Action):

        def get_sensitive(self):
            return rowan_draith_sex

        def __call__(self):
            renpy.jump('draithRepeat')
