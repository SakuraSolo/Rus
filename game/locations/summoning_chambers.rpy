# summoning chambers
label summoning:
    call screen room_screen(None, None,
        (('Talk', 'talk_summoning'),
        ('Creatures report', 'summoning_report'),
        ))
    return


label talk_summoning:
    'talk_summoning'
    jump summoning


label summoning_report:
    'summoning_report'
    jump summoning
