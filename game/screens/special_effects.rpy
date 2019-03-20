init -2:
    transform logo_eff:
        alpha 1.5
        linear 0.2 xpos -0.001 alpha 1.0
        linear 0.2 xpos 0 alpha 1.0
        linear 0.2 xpos 0.001 alpha 1.0
        linear 0.2 xpos 0 alpha 1.5
        linear 0.2 xpos -0.001 alpha 1.5
        linear 0.2 xpos 0 alpha 1.5
        linear 0.2 xpos 0.001 alpha 1.0
        linear 0.2 xpos 0 alpha 1.0
        repeat


    transform quick_eff:
        on idle:
            ypos 0
            xpos 0
        on hover:
            ypos -0.05
            linear 0.1 xpos -0.05
            linear 0.1 xpos 0
            linear 0.1 xpos 0.05
            linear 0.1 xpos 0
            repeat
        on insensitive:
            alpha 0.2


    transform pref_eff:
        on idle:
            alpha 1.0
        on hover:
            alpha 1.5
        on selected_idle:
            alpha 1.0
        on insensitive:
            alpha 0.2


    transform nav_eff:
        pass
#~         on idle:
#~             alpha 1.0
#~             ypos 0
#~             xpos 0
#~         on hover:
#~             alpha 1.5
#~             ypos -0.01
#~             linear 0.1 xpos -0.01
#~             linear 0.1 xpos 0
#~             linear 0.1 xpos 0.01
#~             linear 0.1 xpos 0
#~             repeat
#~         on selected_idle:
#~             alpha 1.0
#~         on insensitive:
#~             alpha 0.2


    transform file_eff:
        on idle:
            alpha 1.0
            ypos 0
            xpos 0
        on hover:
            alpha 1.5
            ypos -0.01
            linear 0.1 xpos -0.01
            linear 0.1 xpos 0
            linear 0.1 xpos 0.01
            linear 0.1 xpos 0
            repeat
        on selected_idle:
            alpha 1.0
        on insensitive:
            alpha 0.2


    transform scene_replay_eff:
        on idle:
            xoffset 0
        on hover:
            xoffset -2
            linear 0.1 xoffset -2
            linear 0.1 xoffset 0
            linear 0.1 xoffset 2
            linear 0.1 xoffset 0
            repeat


    style quick_button:
        idle_background None
        hover_background Frame("gui/qm_hover_back.png", 10, 10)
        insensitive_background None
        yminimum 30
        top_padding 4
        xminimum 50


    style quick_button_text:
        is default
        size 16
        idle_color "#fff"
        hover_color "#fff"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#000"
        yalign 0.5
        xalign 0.5
        kerning 2
