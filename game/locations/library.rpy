# Castle library
label library:
    
    if cliohnaDelaneHelp == "get" and delane_status == "tent":
        jump cliohnaDelaneHelp
        
    else:
        pass
    
    call screen room_screen('images/Backgrounds/library.jpg', 'cliohna room',
        (('Talk', '_operator_talk'),
        ('Visit Nasim', visitNasim()),
        ('Active research', 'library_researches' if systems.research else 'pass'),
        ),
        'cliohna')
    return

label library_researches:
    call screen researches_screen(True)
    jump library

init python:

    class visitNasim(Action):

        def get_sensitive(self):
            return nasimAvailable

        def __call__(self):
            renpy.jump('nasim_dialogue')
