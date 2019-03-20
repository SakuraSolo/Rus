# debug screen showing current temporary vars of event
define show_story_vars_debug = False


screen story_vars_debug():
    hbox:
        xalign 1.0
        if show_story_vars_debug:
            frame:
                background '#3398'
                ypos 50
                xysize (500, 450)
                viewport:
                    mousewheel True
                    scrollbars 'vertical'
                    vbox:
                        for var_name in sorted(story_vars_list):
                            $ var_value = getattr(store, var_name, 'undefined')
                            if isinstance(var_value, dict):
                                text "{}: {}".format(var_name, '{' + str(var_value)) substitute False
                            else:
                                text "{}: {}".format(var_name, var_value) substitute False
        textbutton '<' action ToggleVariable('show_story_vars_debug') ypos 200
