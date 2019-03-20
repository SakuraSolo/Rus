##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():
    frame:
#~         background Frame("gui/stats_border.png", 12, 12)
        background None
        pos (585, 690)
        xsize 540
        hbox:
            xfill True
            style_prefix 'quick'
            textbutton 'Auto' action Preference("auto-forward", "toggle")
            textbutton 'Skip' action Skip()
            textbutton 'Save' action ShowMenu('save')
            textbutton 'Load' action ShowMenu('load')
            textbutton 'Settings' action ShowMenu('preferences')
