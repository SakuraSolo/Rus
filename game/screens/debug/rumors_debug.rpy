# debug screen for rumors
screen rumors_debug():
    modal True
    frame:
        background '#696e'
        xfill True
        yfill True
        vbox:
            hbox:
                spacing 10
                textbutton 'Close' action Hide('rumors_debug')
                text 'Rumors'
            viewport:
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    spacing 10
                    for rumor in sorted(all_rumors.values(), key=lambda x: x.name):
                        hbox:
                            spacing 10
                            frame:
                                xsize 300
                                text rumor.name
                            frame:
                                xsize 100
                                text  "{}".format(rumor.kind):
                                    if rumor.kind == 'passive':
                                        color '#888'
                            frame:
                                xsize 100
                                if rumor.priority:
                                    text  "high".format(rumor.priority):
                                        color '#66f'
                                else:
                                    text  "normal".format(rumor.priority)
                            frame:
                                xsize 130
                                text  "{}".format(rumor.state)

