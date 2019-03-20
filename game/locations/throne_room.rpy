# Throne room of the castle
label throne_room:
    
    if get_jez_potion == True and delane_status == "tent":
        jump tarishQuestJez
        
    else:
        pass
        
    if jezDelaneHelp == "get" and delane_status == "tent":
        jump jezeraDelaneHelp
        
    else:
        pass
    
    $ _throne_room_menu_items = [
        ('Hints', '_operator_talk'),
        ('Realm reports', 'realm_reports'),
        ('Review goal', 'review_goal'),
        ]
    if can_summon_Liurial:
        $ _throne_room_menu_items.append(('Summon Liurial', 'summon_liurial'))

    call screen room_screen('images/Backgrounds/throne room.jpg', None,
        _throne_room_menu_items,
        'rowan_empty_throne_room')
    return


label review_goal:
    call screen review_goal_screen
#~     'review goal'
    jump throne_room


label realm_reports:
    call screen realms_report_screen
#~     'realm reports'
    jump throne_room

