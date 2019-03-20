# screen for portal room
define portal_screen_draw_last = None
define portal_screen_region = None

screen portal_screen():
    add 'gui/portal/Background_Portal_Rosaria.png' pos (-1, -1)
    textbutton 'Back' action Return() style 'back_button'

    # buttons for regions
    # sort buttons so hovered button is drawn last
    for btn_def in sorted(portal_region_buttons[portal_screen_region or 'rosaria'], key=lambda x: x[0] == portal_screen_draw_last):
        imagebutton action btn_def[4] pos btn_def[1]:
            idle btn_def[2]
            hover btn_def[3]
            hovered SetVariable('portal_screen_draw_last', btn_def[0])
            focus_mask True

    # buttons to choose regions
    hbox:
        align (0.5, 0.95)
        spacing 20
        textbutton 'Continue exploration' action ContinueExploration('rosaria_map') style 'angular_button' xpadding 35
        textbutton 'Rosaria' action SetVariable('portal_screen_region', 'rosaria') style 'angular_button' xpadding 35
        #textbutton 'Frozen Tundra' action NullAction() style 'angular_button' xpadding 35

    add 'images/map_gui/compass/BG.png' align (0.05, 0.95)
    # show info
    vbox:
        spacing 20
        align (0.97, 0.05)
        use game_time
        use info_treasury

init python:
    # definitions for buttons of various portal regions
    portal_region_buttons = {
        'rosaria': [
            ['central_rosaria', (127, 234), 'gui/portal/Button_CentralRosaria_Neutral.png', 'gui/portal/Button_CentralRosaria_Pressed.png', JumpToPortal('rosaria_map', 'Central Rosaria')],
            ['northen_rosaria', (293, 48), 'gui/portal/Button_WestRosaria_Neutral.png', 'gui/portal/Button_WestRosaria_Pressed.png', JumpToPortal('rosaria_map', 'Northern Rosaria')],
            #['east_rosaria', (470, 218), 'gui/portal/Button_EastRosaria_Neutral.png', 'gui/portal/Button_EastRosaria_Pressed.png', NullAction()],
        ],
    }
