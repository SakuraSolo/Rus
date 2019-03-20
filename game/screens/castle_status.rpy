screen castle_status():
    frame:
        ypos 80
        background Frame('gui/stats_border.png', 12, 12)
        align (1.0, 0.0)
        vbox:
            text 'Week: [week]'
            text 'Date: {}'.format(game_date(week))
            text 'Treasury: [castle.treasury] ({:+})'.format(castle.treasury - castle.last_week_treasury)
            text 'Morale: [castle.morale_text] ([castle.morale]%) ({:+}%)'.format(castle.morale - castle.last_week_morale)
            text 'Military capacity: [castle.military]'
            text 'Tech rate: [castle.tech]'
            if castle.current_research:
                text '{} ({}/{})'.format(castle.current_research.name, castle.current_research.rp_spent, castle.current_research.cost)
            else:
                text 'No research...'
            text 'World resources:'
            text 'Villages: {} (+{} gold)'.format(castle.villages, castle.villages_income)
            text 'Mines: {} (+{} iron)'.format(castle.mines, castle.iron_per_week)
            text 'Research bonus: {}'.format(castle.research_bonus)


# show game week and formatted date
screen game_time():
    frame:
        xysize (170, 90)
        xalign 1.0
        background Frame('gui/universal/Icon Base.png', 35, 0, 81, 0)
        add 'gui/universal/week icon.png' align (0.85, 0.6) zoom 0.8
        text '[week]' line_spacing 0 align (0.35, 0.7)
#~         text 'Date: {}'.format(game_date(week))


# info screen: castle treasury
screen info_treasury():
    frame:
        xysize (173, 90)
        xalign 1.0
        background Frame('gui/universal/Icon Base.png', 35, 0, 81, 0)
        add 'gui/universal/Gold icon.png' align (0.8, 0.55) zoom 0.7
        text '[castle.treasury]' line_spacing 0 align (0.3, 0.7)
