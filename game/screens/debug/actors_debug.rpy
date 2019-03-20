# debug screen for actors (NPC)
screen actors_debug():
    modal True
    default selected_actor = None
    frame:
        background '#aace'
        xfill True
        yfill True
        has vbox
        textbutton 'Close' action Hide('actors_debug')
        vpgrid:
            cols 1
            mousewheel True
            scrollbars "vertical"
            xsize 300
            spacing 0
            for ac in sorted(all_actors.values(), key=lambda a: a.name):
                textbutton ac.name action SetScreenVariable('selected_actor', ac.uid):
                    background Frame('gui/stats_border.png', 12, 12)
                    text_line_spacing 0
                    xsize 250
    use actor_details(selected_actor)


screen actor_details(ac_uid):
    if ac_uid:
        $ ac = all_actors[ac_uid]
        frame:
            background '#999e'
            xpos 350
            has vbox
            text ac.name bold True size 30
            text 'relation: {} favors: {} total favors: {} corruption: {}'.format(ac.relation, ac.favors, ac.total_favors, 'infinity' if ac.inf_corruption else ac.corruption)
            if len(ac.flags) > 0:
                text 'Flags'
            else:
                text 'No flags'
            for flag, val in ac.flags.items():
                text '{}: {}'.format(flag, val)

