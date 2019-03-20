# debug screen showing current temporary vars of event
define show_event_tmp_debug = False


screen event_tmp_debug():
    # show only if there are temporary vars
    if event_tmp:
        hbox:
            textbutton '>' action ToggleVariable('show_event_tmp_debug') ypos 200
            if show_event_tmp_debug:
                frame:
                    background '#3398'
                    ypos 50
                    xysize (500, 450)
                    viewport:
                        mousewheel True
                        scrollbars 'vertical'
                        vbox:
                            for var_name, var_value in sorted(event_tmp.iteritems()):
                                if isinstance(var_value, dict):
                                    text "{}: {}".format(var_name, '{' + str(var_value)) substitute False
                                else:
                                    text "{}: {}".format(var_name, var_value) substitute False
