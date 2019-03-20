screen castle_status_st():
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        vbox:
            text 'Training coffers: [castle.training_coffers]'


# show game week and formatted date
#~ screen game_time():
#~     frame:
#~         background Frame('gui/stats_border.png', 12, 12)
#~         xalign 0.5
#~         hbox:
#~             spacing 10
#~             text 'Week: [week]'
#~             text 'Date: {}'.format(game_date(week))

