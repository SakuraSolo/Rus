# main script for bonus slave training game


# bonus game starts here
label start_training:
    python:
        # timestamp in weeks
        week = 0
        # adult mode (NSFW)
        adult = True
        # create avatar Rowan
        avatar = Avatar('Rowan')
        # set variable to show events that this scenario is Rowan's
        Rowan_sc = True
        # add some items to backpack
        avatar.inventory.add_items(('iron_sword', 'leather_straps'))
        # equip 'sword' to main hand
        avatar.inventory.equip('iron_sword')
        avatar.inventory.equip('leather_straps')
        avatar.gold = 100
        avatar.base_strength = 10
        avatar.base_vitality = 10
        avatar.base_reflexes = 5
        avatar.base_intelligence = 5
        avatar.base_luck = 5
        avatar.heal()
        # create castle
        starting_rooms_st = {'barracks': False, 'rowans_chambers': True, 'throne_room': False,
                'library': False, 'tavern': False, 'guest_wing': True, 'brothel': False, 'portal_room': False,
                'reliquary': False, 'breeding_pits': False, 'dungeons': False}
        castle = CastleSt(starting_rooms_st)
        # unlock starting trainings (levels 0-4)
        castle.jobs['etiquette'].unlock_level(2)
        castle.jobs['obedience'].unlock_level(2)
        alexia = AlexiaSt()
        alexia.known = True
        # add Alexia to castle to make trainable (and for weekly state updates)
        castle.add_guest(alexia)

    jump week_start_training


label week_start_training:
    $ week += 1
    scene black
    centered 'Week [week]'
    scene
    # running week_start events here - tutorials, messages etc.
#~     call run_events('week_start') from _call_run_events
    # go to main castle hub
    call rowans_chambers_st from _call_rowans_chambers_training
    # run scheduled events for trainable NPCs
    python:
        for npc, task in castle.schedule.items():
            if task:
                renpy.call('run_events', 'st_' + npc + '_' + task)
    # do week calculations - pop increase, taxes etc.
    call end_week from _call_end_week_training
    jump week_start_training


# do week changes - taxes, pop change etc.
label end_week_training:
    $ castle.end_week()
    return
