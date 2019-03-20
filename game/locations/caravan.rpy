# caravan

label caravan:
    
    if get_cla_poison == True and delane_status == "tent":
        jump tarishQuestCla
    
    else:
        pass
    
    call screen room_screen('bg19', 'clamin room',
        (('Talk', '_operator_talk'),
        ('Shop', 'shop_clamin'),
        ('Get a tit job from Cla-Min', TitJobCla()),
        ),
        'cla_min')
    return


label shop_clamin:
    call screen shop_screen(castle_shop_trader)
    jump caravan

init python:

    class TitJobCla(Action):

        def get_sensitive(self):
            return cla_tit_job

        def __call__(self):
            renpy.jump('titJobCla')
