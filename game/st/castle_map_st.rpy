# map of the castle (training version)


screen castle_map_st():
    # forbid rollback and mark changes made in this screen to be saved
    $ renpy.block_rollback()
    $ renpy.retain_after_load()
    default map_level = 'ground'
    use castle_ground_map_st
#~     if map_level == 'ground':
#~         use castle_ground_map_st
#~     else:
#~         use castle_basement_map
    use castle_status_st
    use game_time


screen castle_ground_map_st():
    # map for ground floor of the castle
    add 'images/map/castle/castle_map_ground.png'
    # place image buttons for hover areas
    for room, coords in ground_rooms_imagebuttons_st.items():
        # check if room is accessable
        if castle.rooms_access[room]:
            # special case - rowans_chambers use 'Jump' to avoide recursion
            if room == 'rowans_chambers':
                # special version for training
                imagebutton action Jump('rowans_chambers_st'):
                    pos coords
                    idle 'images/map/castle/' + room + '.png'
                    hover 'images/map/castle/' + room + '_hover.png'
                    focus_mask 'images/map/castle/' + room + '_hover.png'
            else:
                imagebutton action Call(room):
                    pos coords
                    idle 'images/map/castle/' + room + '.png'
                    hover 'images/map/castle/' + room + '_hover.png'
                    focus_mask 'images/map/castle/' + room + '_hover.png'
    # button to switch map level
#~     textbutton 'Basement' action SetScreenVariable('map_level', 'basement'):
#~         style 'small_textbutton'
#~         xalign 0.9
#~         yalign 0.9


init python:
    class Call(Action):
        '''Call label'''
        def __init__(self, target):
            self.target = target

        def __call__(self):
            renpy.call(self.target)

    # names and coordinates for imagebuttons in castle maps
    ground_rooms_imagebuttons_st = {'barracks': (350, 190), 'rowans_chambers': (320, 370),
        'throne_room': (424, 265), 'library': (45, 437), 'tavern': (668, 423),
        'guest_wing': (830, 286), 'brothel': (915, 171), 'portal_room': (759, 178),
        'reliquary': (827, 111)}
    basement_rooms_imagebuttons = {'breeding_pits': (800, 93), 'dungeons': (352, 234)}
