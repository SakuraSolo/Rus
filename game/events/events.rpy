init -1 python:

    #some standart priorities (default = 100, higher number -> lower priority)
    pr_system = 30
    # warning events
    pr_warning = 39
    pr_story = 40
    # building intro event
    pr_bld_intro = 45
    # NPC slot
    pr_npc_high = 46
    pr_npc = 47
    pr_npc_fallback = 47
    # ruler event (higher priority for special events)
    pr_ruler_high = 52
    # ruler event
    pr_ruler = 53
    # priorities for info about new buildings, upgrades and researches
    pr_new_bld = 60
    pr_new_upgr = 61
    pr_new_rs = 62
    # priority for map resource event
    pr_map_res = 70
    # priority for map random event
    pr_map_rnd = 72
    pr_fallback = 200
    # system (silent) event that should go after all other events
    pr_system_last = 210


init python:
    pass
#~     event('nothing_happened', "act.startswith(('rosaria',))", event.solo(), priority=pr_fallback)


label nothing_happened:
    'This is debug event that should not be seen in normal game. No other events were triggered in choosen events pool.'
    return


label end_map_exploration:
    # map events can jump to this label to return from the map exploration immediately
    $ renpy.set_return_stack(renpy.get_return_stack()[:1])
    $ msgs.show('{color=#E44238}Map exploration ended by event{/color}')
    return
