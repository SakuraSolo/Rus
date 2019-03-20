# contains labels/code related to main game loop

label week_start:
    # save game to slot 12 on page 1
    $ renpy.take_screenshot()
    $ renpy.save('1-12')
    play music 'music/title screen loop.ogg'
    $ week += 1
    $ update_event_timers()
    ####################
    # temporary, changes alexia vars # TODO
    if alexia_away_weeks > 0:
        $ alexia_away_weeks -=1
    if alexia_cant_work_weeks > 0:
        $ alexia_cant_work_weeks -=1

    # reset Liurial var
    $ liurial_orgasm_control_plea = False
    if liurial_weeks_after_blowjob_request > -1:
        $ liurial_weeks_after_blowjob_request += 1
    # count total weeks of orgasm control
    if liurial_orgasm_control_on:
        $ liurial_orgasm_control_total_time += 1

    # reset Kharos priest var (meeting_the_priest_of_kharos)
    $ orciad_priest_visited = False
    ####################
    scene black
    centered 'Week [week]'
    $ msgs.show('=== Week {} started ==='.format(week))
    $ allow_saving()
    scene
    # running week_start events here - tutorials, messages etc.
    call run_events('week_start') from _call_run_events
    # go to main castle hub, if it is allowed
    if systems.castle:
        call rowans_chambers from _call_rowans_chambers
    # if castle is disabled, force exploration mode
    else:
        call map_exploration('rosaria_map') from _call_map_exploration_1

    #reset delane visit counter
    if last_delane_visit_attempt == 1:
        $ last_delane_visit_attempt = 0

    else:
        pass


    if last_delane_visit == 1:
        $ last_delane_visit = 0

    else:
        pass


label before_week_end:
    play music 'music/title screen loop.ogg'
    # call events for end of week
    scene black
    centered 'End of week [week]'
    # show reports/events for completed spy missions
    call show_spy_results from _call_spy_results
    call show_arena_bet_results from _call_arena_bet_results
    # various 'week_end' events, like ruler events
    call run_events('week_end') from _call_run_events_week_end
    # do week calculations - update castle, avatar etc.
    call end_week from _call_end_week
    # allow to continue playing in dev mode
    $ notification = False
    jump week_start




# show result events for completed spy missions
label show_spy_results:
    while len(get_spies('completed mission')) > 0:
        $ temp_spy = get_spies('completed mission')[0]
        if temp_spy.mission.completed:
            $ msgs.show('{{color=#C6FE56}}--- {} --- Start of spy mission report: {} ---{{/color}}'.format(week, temp_spy.mission.label))
            call expression temp_spy.mission.label pass (temp_spy) from _call_expression
            $ msgs.show('{{color=#C6FE56}}--- {} --- End of spy mission report: {} ---{{/color}}'.format(week, temp_spy.mission.label))
            $ temp_spy.mission = None
    return


label show_arena_bet_results:
    if arena_bet['amount']:
        $ temp = dice(8)
        if temp <= 3:
            $ narrator('{} came {} earning you {} gold.'.format(arena_bet['fighter'], ['first', 'second', 'third'][temp-1], arena_bet['amount'] * (4 - temp)))
            $ avatar.gold += arena_bet['amount'] * (4 - temp)
        $ arena_bet['amount'] = None
    return

# do week changes - update states of castle and avatar etc.
label end_week:
    $ castle.end_week()
    $ avatar.weekly()
    return
