# debug screen for map
screen map_debug(align=(0, 0.5)):
    frame:
        background '#00f5'
        align align
        has vbox
        text 'Map tools'
        text 'MP/baseMP/wounds:'
        hbox:
            text '[avatar.mp]/[avatar.base_mp]/[avatar.wounds]'
            textbutton '+' action SetField(avatar, 'mp', avatar.mp + 1)
            textbutton '-' action SetField(avatar, 'mp', avatar.mp - 1)
        textbutton 'Trigger event' action Return('force_random_event')
        hbox:
            text 'View distance: [avatar.view_distance]'
            textbutton '+' action SetField(avatar, 'view_distance', avatar.view_distance + 1)
            textbutton '-' action SetField(avatar, 'view_distance', avatar.view_distance - 1)
        hbox:
            text 'Zoom'
            textbutton '1' action SetField(mview, 'zoom', 1.0)
            textbutton '0.7' action SetField(mview, 'zoom', 0.7)
            textbutton '0.5' action SetField(mview, 'zoom', 0.5)
            textbutton '0.3' action SetField(mview, 'zoom', 0.3)
        textbutton "Show unseen" action ToggleField(mview, 'show_unseen')
        text 'Current pos:  {} (id {})'.format(tuple(world.cur_hex[1]), world.cur_hex[0])
