# Castle brothel
label brothel:
    call screen room_screen('bg24', 'shaya room',
        (('Talk', '_operator_talk'),
        ('Spies', 'brothel_spies'),
        ('Watch Shaya put on a show', watchShayaShow()),
        ),
        'shaya')
    return


label brothel_spies:
    call screen spies_controls_screen
    jump brothel

init python:

    class watchShayaShow(Action):

        def get_sensitive(self):
            return shayaShow

        def __call__(self):
            renpy.jump('shaya_Show')