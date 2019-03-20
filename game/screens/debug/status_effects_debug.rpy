# debug screen for status effects of avatar
screen status_effects_debug():
    modal True
    frame:
        background '#889e'
        xfill True
        yfill True
        vbox:
            textbutton 'Close' action Hide('status_effects_debug')
            for eff in avatar.effects:
                text str(eff)

