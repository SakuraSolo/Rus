# debug screen for map resources
default map_resources_debug_expanded = False
screen map_resources_debug():
    frame:
        background '#55f5'
        xalign 0.4
        has vbox
        textbutton 'Resources' action ToggleVariable('map_resources_debug_expanded')
        if map_resources_debug_expanded:
            viewport:
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    for res in world.cur_map.resources.values():
                        hbox:
                            frame:
                                xsize 200
                                text res.name
                            frame:
                                xsize 200
                                text "{} ({})".format(str(res.res_id), res.kind)
                            frame:
                                xsize 100
                                if res.seen:
                                    text 'Seen' color '#4f4'
                                else:
                                    text 'Not seen' color '#f44'
                            frame:
                                xsize 150
                                if res.visited:
                                    text 'Visited' color '#4f4'
                                else:
                                    text 'Not visited' color '#f44'
                            frame:
                                xsize 150
                                if res.state == 'captured':
                                    text 'Captured' color '#4f4'
                                elif res.state == 'destroyed':
                                    text 'Destroyed' color '#f44'
                                else:
                                    text 'N/A' color '#555'

