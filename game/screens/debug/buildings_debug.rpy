# debug screen for buildings
screen buildings_debug():
    modal True
    frame:
        background '#696e'
        xfill True
        yfill True
        vbox:
            hbox:
                spacing 10
                textbutton 'Close' action Hide('buildings_debug')
                text 'All buildings'
            viewport:
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    spacing 10
                    for bld in sorted(castle.buildings.values(), key=lambda x: x.name):
                        hbox:
                            spacing 10
                            text bld.name xsize 200
                            text  "lvl {}".format(bld.lvl)
                            # TODO maybe use built() to correctly change all stats, not only lvl
                            textbutton '-' action SetField(castle.buildings[bld.uid], 'lvl', castle.buildings[bld.uid].lvl - 1)
                            textbutton '+' action Function(bld.build)

