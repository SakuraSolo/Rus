##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

#screen say(who, what, side_image=None, two_window=True):
    #add "gui/border.png"
    #window:
        #if char_right:
            #background "gui/say_box2.png"
        #else:
            #background "gui/say_box.png"
        #id "window"
        #xalign 0.5
        #yalign 0.15
        #vbox:
            #style "say_vbox"
        #text what id "what"
    #use quick_menu
    #add "gui/logo_small.png":
        #xalign 0.5
        #yalign 0.93
    #frame:
        #style "say_who_window"
        #if char_right:
            #xalign 0.99
            #yalign 1.03
        #else:
            #xalign 0.05
            #yalign 1.03
        #vbox:
            #text who:
                #id "who"
    #if side_image:
        #add side_image
    #else:
        #add SideImage() xalign 0.0 yalign 1.0



screen say(who, what, side_image=None, two_window=True):
#~     add "gui/border.png"
    default side_image = None
    default two_window = False
    add "gui/Dialogue Border.png" pos (270, 560)
    add "gui/Dialogue box full.png" yzoom -1 ypos -140 alpha 0.5
    add "gui/Dialogue box full.png" align (1.0, 1.0) yzoom 0.8 alpha 0.7
    if not two_window:
#~         window:
#~             id "window"
#~             xalign 0.5
#~             xfill True
#~             ysize 200
        if who:
            text who id "who"
        text what id "what"
    # not used
    else:
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
    # show temporary event vars
    if config.developer:
        use event_tmp_debug
        use story_vars_debug
    # show log messages (`~)
    key '`' action Show('messages')
    # show journal button
    use journal_button((0.99, 1.0))



style say_window is window:
    ypadding 0
    background None
    yalign 1.0
    ysize 180

style say_label:
    pos (275, 530)
    size 30

style say_dialogue:
    pos (295, 592)
    xsize 900
