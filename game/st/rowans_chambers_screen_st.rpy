# info and actions for Rowan's chambers (training version)
screen rowans_chambers_screen_st():
    # forbid rollback and mark changes made in this screen to be saved
    $ renpy.block_rollback()
    $ renpy.retain_after_load()
    # show possible actions for Rowan's room
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        style_group 'navi'
        xpos 20
        ypos 20
        vbox:
            textbutton 'Leave' action Jump('castle_map_st')
            textbutton 'Rest' action Jump('rest_st')
    # Rowan's info
    frame:
        background None
        xpadding 0
        ypadding 0
        xalign 1.0
        xoffset -20
        yalign 0.5
    use game_time
