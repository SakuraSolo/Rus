# map of the castle (ground level)


# current level of castle map
default castle_map_level = 'ground'

screen castle_map():
    # forbid rollback and mark changes made in this screen to be saved
    $ renpy.block_rollback()
    $ renpy.retain_after_load()
    if castle_map_level == 'ground':
        use castle_ground_map
    else:
        use castle_basement_map
    if statusActive:
        use castle_status
    use castle_nav
    use npc_job_menu((0.5, 1.0))
    use journal_button((0.99, 1.0))

screen castle_ground_map():
    frame:
        xfill True
        yfill True
        viewport:
            child_size (1922, 1082)
            draggable True
#~             edgescroll (150, 2000, lambda x: 1 if x>0 else -1 if x<0 else 0)
            edgescroll (0, 1000)
            frame:
                xpadding 0
                ypadding 0
                add 'images/map/castle/CastleGroundFloor_Base.png'
                # image buttons for rooms
#                for (room, coords, act_name, args) in ground_rooms_imagebuttons:
                    # check if room is accessable
#~                     if castle.visitable(room):
#~                     if room in visitable_locations:
                        # special case - rowans_chambers use 'Jump' to avoid recursion
                    # create actions by selecting them from dict, to support saving/pickling
#                    $ act = {'call': Call, 'jump': Jump, 'enter_bld': EnterBuilding, 'None': None, 'SetVariable': SetVariable}[act_name]
#                    imagebutton:
#                        if act is None:
#                            action None
#                        elif args:
#                            action act(*args)
#                        else:
#                            action act()
#                        pos coords
#                        idle 'images/map/castle/' + room + '.png'
#                        hover 'images/map/castle/' + room + '_hover.png'
#                        focus_mask 'images/map/castle/' + room + '_hover.png'

#~                         if room == 'rowans_chambers':
#~                             imagebutton action Jump(room):
#~                                 pos coords
#~                                 idle 'images/map/castle/' + room + '.png'
#~                                 hover 'images/map/castle/' + room + '_hover.png'
#~                                 focus_mask 'images/map/castle/' + room + '_hover.png'
#~                         else:
#~                             imagebutton action Call(room):
#~                                 pos coords
#~                                 idle 'images/map/castle/' + room + '.png'
#~                                 hover 'images/map/castle/' + room + '_hover.png'
#~                                 focus_mask 'images/map/castle/' + room + '_hover.png'
#~                     else:
#~                         imagebutton action NullAction():
#~                             pos coords
#~                             idle 'images/map/castle/' + room + '.png'
#~                             focus_mask 'images/map/castle/' + room + '_hover.png'

#~     # map for ground floor of the castle
#~     add 'images/map/castle/castle_map_ground.png'
#~     # place image buttons for hover areas
#~     for room, coords in ground_rooms_imagebuttons.items():
#~         # check if room is accessable
#~         if castle.visitable(room):
#~             # special case - rowans_chambers use 'Jump' to avoide recursion
#~             if room == 'rowans_chambers':
#~                 imagebutton action Jump(room):
#~                     pos coords
#~                     idle 'images/map/castle/' + room + '.png'
#~                     hover 'images/map/castle/' + room + '_hover.png'
#~                     focus_mask 'images/map/castle/' + room + '_hover.png'
#~             else:
#~                 imagebutton action Call(room):
#~                     pos coords
#~                     idle 'images/map/castle/' + room + '.png'
#~                     hover 'images/map/castle/' + room + '_hover.png'
#~                     focus_mask 'images/map/castle/' + room + '_hover.png'
                # Portal Room
                imagebutton action [SetVariable('roomName', 'Portal Room'), Call('portal_room')]:
                    pos (312, 59)
                    idle bt_portal
                    hover bt_portal_h
                    focus_mask bt_portal_h

                # Stairs Up
                imagebutton:
                    pos (602, 141)
                    idle bt_stairs_up
                    hover bt_stairs_up_h
                    focus_mask bt_stairs_up_h

                # Stairs Down
                imagebutton action [SetVariable('roomName', 'Stairs Down'), SetVariable('castle_map_level', 'basement')]:
                    pos (432, 306)
                    idle bt_stairs_down
                    hover bt_stairs_down_h
                    focus_mask bt_stairs_down_h

                # Rowan's Chambers
                if alexiaSeparateRoom:
                    if rowan_shares_room_with_helayna and helayna_escaped == False:
                        imagebutton action [SetVariable('roomName', 'Rowan\'s Chambers'), Jump('rowans_chambers')]:
                            pos (749, 16)
                            idle poi_chambers2
                            hover poi_chambers2_h
                            focus_mask poi_chambers2_h
                    else:
                        imagebutton action [SetVariable('roomName', 'Rowan\'s Chambers'), Jump('rowans_chambers')]:
                            pos (749, 16)
                            idle bt_chambers
                            hover bt_chambers_h
                            focus_mask bt_chambers_h
                else:
                    if alexia_away_weeks > 0:
                        imagebutton action [SetVariable('roomName', 'Rowan\'s Chambers'), Jump('rowans_chambers')]:
                            pos (749, 16)
                            idle bt_chambers
                            hover bt_chambers_h
                            focus_mask bt_chambers_h
                    else:
                        imagebutton action [SetVariable('roomName', 'Rowan\'s Chambers'), Jump('rowans_chambers')]:
                            pos (749, 16)
                            idle poi_chambers
                            hover poi_chambers_h
                            focus_mask poi_chambers_h

                # Guest Wing
                if castle.visitable('guest_wing'):
                    imagebutton action [SetVariable('roomName', 'Guest Wing'), Call('guest_wing')]:
                        pos (745, 93)
                        idle bt_guest
                        hover bt_guest_h
                        focus_mask bt_guest_h
                else:
                    add bt_guest pos (745, 93)

                # Hallway
                imagebutton  action [SetVariable('roomName', 'Living Quarters'), Call('quarters')]:
                    pos (965, 85)
                    idle poi_hallway
                    hover poi_hallway_h
                    focus_mask poi_hallway_h

                # Liurial Room
                add bt_liurial pos (543, 224)
                #imagebutton action [SetVariable('roomName', 'Liurial Room'), Jump('liurial_room')]:
                #    pos (543, 224)
                #    idle bt_liurial
                #    hover bt_liurial_h
                #    focus_mask bt_liurial_h

                # Mess Hall
                add bt_messhall pos (1030, 162)
                #if castle.visitable('mess_hall'):
                #    imagebutton action [SetVariable('roomName', 'Mess Hall'), Call('mess_hall')]:
                #        pos (1030, 162)
                #        idle bt_messhall
                #        hover bt_messhall_h
                #        focus_mask bt_messhall_h
                #else:
                #    add bt_messhall pos (1030, 162)

                # Throne Room
                imagebutton action [SetVariable('roomName', 'Throne Room'), Call('throne_room')]:
                    pos (616, 271)
                    idle bt_throne
                    hover bt_throne_h
                    focus_mask bt_throne_h

                # Library
                imagebutton action [SetVariable('roomName', 'Library'), Call('library')]:
                    pos (273, 376)
                    idle poi_library
                    hover poi_library_h
                    focus_mask poi_library_h

                # Workshop
                imagebutton action [SetVariable('roomName', 'Workshop'), Call('workshop')]:
                    pos (546, 538)
                    idle poi_workshop
                    hover poi_workshop_h
                    focus_mask poi_workshop_h

                # Tavern
                if castle.visitable('tavern'):
                    imagebutton action [SetVariable('roomName', 'Tavern'), Call('tavern')]:
                        pos (311, 713)
                        idle poi_tavern
                        hover poi_tavern_h
                        focus_mask poi_tavern_h

                # Caravan
                imagebutton action [SetVariable('roomName', 'Caravan'), Call('caravan')]:
                    pos (1583, 850)
                    idle poi_caravan
                    hover poi_caravan_h
                    focus_mask poi_caravan_h

screen castle_basement_map():
    # map for basement of the castle
    #add 'images/map/castle/castle_map_basement.png'

    # place image buttons for hover areas
    frame:
        background '#000000'
        xfill True
        yfill True
        $directory = 'images/map/underground/'
        $extension = '.png'
        viewport:
            child_size (1400, 800)
            draggable True
            edgescroll (0, 1000)
            frame:
                background None
                xpadding 0
                ypadding 0
                add 'images/map/underground/BG_Underground_base.png' pos (200, 50)

                # Top Center Grid
                # Top
                frame:
                    background None
                    if len(castle.scheduled_upgrades) > 0:
                        if castle.buildings[castle.scheduled_upgrades[0]].name == 'Arena' and castle.buildings['arena'].lvl == 0:
                            add bt_UnderConstruction pos (105 + topOffsetX, 0 + topOffsetY)
                        elif castle.buildings['arena'].lvl >= 1:
                            pos (105 + topOffsetX, -60 + topOffsetY)
                            imagebutton action [SetVariable('roomName', 'Arena'),Call('arena')]:
                                idle bt_arena
                                hover bt_arena_h
                                focus_mask bt_arena_h
                        else:
                            add bt_emptyRoom pos (105 + topOffsetX, 0 + topOffsetX)
                    else:
                        if castle.buildings['arena'].lvl >= 1:
                            pos (105 + topOffsetX, -60 + topOffsetY)
                            imagebutton action [SetVariable('roomName', 'Arena'),Call('arena')]:
                                idle bt_arena
                                hover bt_arena_h
                                focus_mask bt_arena_h
                        else:
                            add bt_emptyRoom pos (105 + topOffsetX, 0 + topOffsetY)
                # Left
                frame:
                    background None
                    pos (10 + topOffsetX, 55 + topOffsetY)
                    imagebutton:
                        idle bt_emptyRoom
                        hover bt_emptyRoom
                        focus_mask bt_emptyRoom
                # Right
                frame:
                    background None
                    pos (210 + topOffsetX, 60 + topOffsetY)
                    imagebutton:
                        idle bt_emptyRoom
                        hover bt_emptyRoom
                        focus_mask bt_emptyRoom
                # Bottom
                frame:
                    background None
                    pos (112 + topOffsetX, 120 + topOffsetY)
                    imagebutton:
                        idle bt_UnderConstruction
                        hover bt_UnderConstruction
                        focus_mask bt_UnderConstruction

                # Top Left Cross
                frame:
                    background None
                    pos (65 + topLeftOffsetX, 10 + topLeftOffsetY)
                    imagebutton:
                        idle bt_emptyRoom
                        hover bt_emptyRoom
                        focus_mask bt_emptyRoom
                frame:
                    background None
                    pos (165 + topLeftOffsetX, 65 + topLeftOffsetY)
                    imagebutton action Return (0):
                        idle bt_UnderConstruction
                        hover bt_UnderConstruction
                        focus_mask bt_UnderConstruction

                # Stairset
                frame:
                    background None
                    pos (80 + centerOffsetX, 50 + centerOffsetY)
                    imagebutton :
                        idle bt_stairs_down
                        hover bt_stairs_down_h
                        focus_mask bt_stairs_down_h
                frame:
                    background None
                    pos (0 + centerOffsetX, 40 + centerOffsetY)
                    imagebutton action SetVariable('castle_map_level', 'ground'):
                        idle bt_stairs_up
                        hover bt_stairs_up_h
                        focus_mask bt_stairs_up_h

                # Top Right Cross
                frame:
                    background None
                    pos (165 + topRightOffsetX, 0 + topRightOffsetY)
                    imagebutton action Return (0):
                        idle bt_emptyRoom
                        hover bt_emptyRoom
                        focus_mask bt_emptyRoom
                frame:
                    background None
                    pos (70 + topRightOffsetX, 60 + topRightOffsetY)
                    imagebutton:
                        idle bt_emptyRoom
                        hover bt_emptyRoom
                        focus_mask bt_emptyRoom

                # Left Grid ** Forge ** Dungeon
                # Top
                frame:
                    background None
                    pos (105 + leftOffsetX, 0 + leftOffsetY)
                    imagebutton:
                        idle bt_dungeon
                        hover bt_dungeon_h
                        focus_mask bt_dungeon_h
                # Left ** Forge
                frame:
                    background None
                    if len(castle.scheduled_upgrades) > 0:
                        if castle.buildings[castle.scheduled_upgrades[0]].name == 'Forge' and castle.buildings['forge'].lvl == 0:
                            add bt_UnderConstruction pos (10 + leftOffsetX, 50 + leftOffsetY)
                        elif castle.buildings['forge'].lvl >= 1:
                            pos (10 + leftOffsetX, 50 + leftOffsetY)
                            imagebutton action [SetVariable('roomName', 'Forge'),Call('forge')]:
                                idle poi_forge
                                hover poi_forge_h
                                focus_mask poi_forge_h
                        else:
                            add bt_emptyRoom pos (10 + leftOffsetX, 55 + leftOffsetY)
                    else:
                        if castle.buildings['forge'].lvl >= 1:
                            pos (10 + leftOffsetX, 50 + leftOffsetY)
                            imagebutton action [SetVariable('roomName', 'Forge'),Call('forge')]:
                                idle poi_forge
                                hover poi_forge_h
                                focus_mask poi_forge_h
                        else:
                            add bt_emptyRoom pos (10 + leftOffsetX, 55 + leftOffsetY)
                # Right ** Dungeon
                frame:
                    background None
                    if castle.buildings['dungeon'].lvl >= 1:
                        pos (210 + leftOffsetX, 60 + leftOffsetY)
                        imagebutton action [SetVariable('roomName', 'Dungeon'),Call('dungeon')]:
                            idle poi_dungeon
                            hover poi_dungeon_h
                            focus_mask poi_dungeon_h
                    else:
                        pos (210 + leftOffsetX, 60 + leftOffsetY)
                        imagebutton:
                            idle bt_emptyRoom
                            hover bt_emptyRoom
                            focus_mask bt_emptyRoom
                # Bottom
                frame:
                    background None
                    add bt_dungeon pos (112 + leftOffsetX, 110 + leftOffsetY)

                # Bottom Left Cross ** Dark Sanctum
                # Top
                frame:
                    background None
                    add bt_emptyRoom pos (165 + bottomLeftOffsetX, 0 + bottomLeftOffsetY)
                # Bottom ** Dark Sanctum
                frame:
                    background None
                    if len(castle.scheduled_upgrades) > 0:
                        if castle.buildings[castle.scheduled_upgrades[0]].name == 'Dark sanctum' and castle.buildings['sanctum'].lvl == 0:
                            add bt_UnderConstruction pos (65 + bottomLeftOffsetX, 60 + bottomLeftOffsetY)
                        elif castle.buildings['sanctum'].lvl >= 1:
                            pos (65 + bottomLeftOffsetX, 60 + bottomLeftOffsetY)
                            imagebutton action [SetVariable('roomName', 'Dark Sanctum'),Call('sanctum')]:
                                idle poi_sanctum
                                hover poi_sanctum_h
                                focus_mask poi_sanctum_h
                        else:
                            add bt_emptyRoom pos (70 + bottomLeftOffsetX, 55 + bottomLeftOffsetY)
                    else:
                        if castle.buildings['sanctum'].lvl >= 1:
                            pos (65 + bottomLeftOffsetX, 60 + bottomLeftOffsetY)
                            imagebutton action [SetVariable('roomName', 'Dark Sanctum'),Call('sanctum')]:
                                idle poi_sanctum
                                hover poi_sanctum_h
                                focus_mask poi_sanctum_h
                        else:
                            add bt_emptyRoom pos (70 + bottomLeftOffsetX, 55 + bottomLeftOffsetY)
                # Right Grid ** Brothel
                # Top
                frame:
                    background None
                    pos (105 + rightOffsetX, 0 + rightOffsetY)
                    imagebutton:
                        idle bt_UnderConstruction
                        hover bt_UnderConstruction
                        focus_mask bt_UnderConstruction
                # Left
                frame:
                    background None
                    pos (10 + rightOffsetX, 55 + rightOffsetY)
                    imagebutton:
                        idle bt_UnderConstruction
                        hover bt_UnderConstruction
                        focus_mask bt_UnderConstruction
                # Right ** Brothel
                frame:
                    background None
                    if len(castle.scheduled_upgrades) >= 1:
                        if castle.buildings[castle.scheduled_upgrades[0]].name == 'Brothel' and castle.buildings['brothel'].lvl == 0:
                            add bt_UnderConstruction pos (210 + rightOffsetX, 30 + rightOffsetY)
                        elif castle.buildings['brothel'].lvl >= 1:
                            pos (210 + rightOffsetX, 30 + rightOffsetY)
                            imagebutton action [SetVariable('roomName', 'Brothel'),Call('brothel')]:
                                idle poi_brothel
                                hover poi_brothel_h
                                focus_mask poi_brothel_h
                        else:
                            add bt_emptyRoom pos (210 + rightOffsetX, 60 + rightOffsetY)
                    else:
                        if castle.buildings['brothel'].lvl >= 1:
                            pos (210 + rightOffsetX, 30 + rightOffsetY)
                            imagebutton action [SetVariable('roomName', 'Brothel'),Call('brothel')]:
                                idle poi_brothel
                                hover poi_brothel_h
                                focus_mask poi_brothel_h
                        else:
                            add bt_emptyRoom pos (210 + rightOffsetX, 60 + rightOffsetY)
                # Bottom
                frame:
                    background None
                    if castle.buildings['brothel'].lvl >= 2:
                        pos (112 + rightOffsetX, 110 + rightOffsetY)
                        imagebutton:
                            idle poi_brothel
                            hover poi_brothel_h
                            focus_mask poi_brothel_h
                    else:
                        pos (112 + rightOffsetX, 110 + rightOffsetY)
                        imagebutton:
                            idle bt_emptyRoom
                            hover bt_emptyRoom
                            focus_mask bt_emptyRoom

                # Bottom Right Cross ** Barracks
                # Top ** Barracks
                frame:
                    background None
                    pos (865, 410)
                    imagebutton action [SetVariable('roomName', 'Orc Barracks'),Call('barracks')]:
                        idle poi_barracks
                        hover poi_barracks_h
                        focus_mask poi_barracks_h
                # Bottom
                frame:
                    background None
                    if castle.buildings['barracks'].lvl >= 2:
                        pos (965, 465)
                        imagebutton action Call('barracks'):
                            idle poi_barracks
                            hover poi_barracks_h
                            focus_mask poi_barracks_h
                    else:
                        add bt_UnderConstruction pos (965, 465)
                # Bottom Center Grid ** Breeding Pit
                # Top
                frame:
                    background None
                    pos (105 + bottomOffsetX, 0 + bottomOffsetY)
                    imagebutton:
                            idle bt_emptyRoom
                            hover bt_emptyRoom
                            focus_mask bt_emptyRoom
                # Left
                frame:
                    background None
                    pos (10 + bottomOffsetX, 55 + bottomOffsetY)
                    imagebutton:
                        idle bt_UnderConstruction
                        hover bt_UnderConstruction
                        focus_mask bt_UnderConstruction
                # Right
                frame:
                    background None
                    pos (210 + bottomOffsetX, 60 + bottomOffsetY)
                    imagebutton:
                            idle bt_emptyRoom
                            hover bt_emptyRoom
                            focus_mask bt_emptyRoom
                # Bottom ** Breeding Pit
                frame:
                    background None
                    if len(castle.scheduled_upgrades) > 0:
                        if castle.buildings[castle.scheduled_upgrades[0]].name == 'Breeding pit' and castle.buildings['pit'].lvl == 0:
                            add bt_UnderConstruction pos (112 + bottomOffsetX, 110 + bottomOffsetY)

                        if castle.buildings['pit'].lvl >= 1:
                            pos (112 + bottomOffsetX, 90 + bottomOffsetY)
                            imagebutton action [SetVariable('roomName', 'Breeding Pit'),Call('pit')]:
                                idle poi_breeding_pit
                                hover poi_breeding_pit_h
                                focus_mask poi_breeding_pit_h
                        else:
                            add bt_emptyRoom pos (112 + bottomOffsetX, 110 + bottomOffsetY)
                    else:
                        if castle.buildings['pit'].lvl >= 1:
                            pos (112 + bottomOffsetX, 90 + bottomOffsetY)
                            imagebutton action [SetVariable('roomName', 'Breeding Pit'),Call('pit')]:
                                idle poi_breeding_pit
                                hover poi_breeding_pit_h
                                focus_mask poi_breeding_pit_h
                        else:
                            add bt_emptyRoom pos (112 + bottomOffsetX, 110 + bottomOffsetY)

# navigation menu for castle
screen castle_nav():

    frame:
        pos (1180, 0)
        background None
        imagebutton:
            if statusActive:
                action [SetVariable("notification", True), SetVariable("statusActive", False)]
            else:
                action [SetVariable("notification", True), SetVariable("statusActive", True)]
            idle 'gui/Castle Buttons/Button_Notification_Idle.png'
            hover 'gui/Castle Buttons/Button_Notification_Hover.png'


    if menuActive:
        frame:
            style_prefix 'menu_list'
            xsize 350
            ysize 690
            ypos 20
            background Frame('gui/stats_border.png', 12, 12)
            has vbox
            # special non-building locations
            textbutton 'Rowan\'s chambers' action [SetVariable('roomName', 'Rowan\'s Chambers'), Jump('rowans_chambers')]
            textbutton 'Throne room' action [SetVariable('roomName', 'Throne Room'), Call('throne_room')]
            textbutton 'Portal room' action [SetVariable('roomName', 'Portal Room'), Call('portal_room')]

            # Space
            null height 30

            if castle_map_level == 'ground':
                textbutton 'Basement' action SetVariable('castle_map_level', 'basement')
            elif castle_map_level == 'basement':
                textbutton 'Ground' action SetVariable('castle_map_level', 'ground')

            # Space
            null height 30

            # building-related locations
            for bld in castle.buildings.values():
                if castle.visitable(bld.uid) and (bld.uid in castle_menu[castle_map_level]):
                    textbutton bld.name:
                        if bld.name == 'Tavern':
                            action [SetVariable('roomName', 'Tavern'),Call(bld.uid)]
                        elif bld.name == 'Arena':
                            action [SetVariable('roomName', 'Arena'),Call(bld.uid)]
                        elif bld.name == 'Workshop':
                            action [SetVariable('roomName', 'Workshop'),Call(bld.uid)]
                        elif bld.name == 'Caravan':
                            action [SetVariable('roomName', 'Caravan'),Call(bld.uid)]
                        elif bld.name == 'Library':
                            action [SetVariable('roomName', 'Library'),Call(bld.uid)]
                        elif bld.name == 'Living Quarters':
                            action [SetVariable('roomName', 'Living Quarters'),Call(bld.uid)]
                        elif bld.name == 'Dungeon':
                            action [SetVariable('roomName', 'Dungeon'),Call(bld.uid)]
                        elif bld.name == 'Brothel':
                            action [SetVariable('roomName', 'Brothel'),Call(bld.uid)]
                        elif bld.name == 'Dark sanctum':
                            action [SetVariable('roomName', 'Dark Sanctum'),Call(bld.uid)]
                        elif bld.name == 'Forge':
                            action [SetVariable('roomName', 'Forge'),Call(bld.uid)]
                        elif bld.name == 'Orc Barracks':
                            action [SetVariable('roomName', 'Orc Barracks'),Call(bld.uid)]
                        elif bld.name == 'Breeding Pit':
                            action [SetVariable('roomName', 'Breeding Pit'),Call(bld.uid)]
                        else:
                            action Call(bld.uid)

    if notification == False and len(journal_quests_current_new_notes) > 0:
        add 'gui/Castle Buttons/UI_Icon_Notice.png' pos (1220, 50)

    frame:
        background None
        if menuActive:
            pos (290, 350)
        else:
            pos (-65, 350)

        imagebutton:
            if menuActive:
                idle 'gui/Castle Buttons/Button_Castle_RoomSelection_Hover.png'
                hover 'gui/Castle Buttons/Button_Castle_RoomSelection_Hover.png'
                action SetVariable("menuActive", False)

            else:
                idle 'gui/Castle Buttons/Button_Castle_RoomSelection_Idle.png'
                hover 'gui/Castle Buttons/Button_Castle_RoomSelection_Hover.png'
                action SetVariable("menuActive", True)




init python:
    class Call(Action):
        '''Call label'''
        def __init__(self, target):
            self.target = target

        def __call__(self):
            renpy.call(self.target)

    class EnterBuilding(Action):
        '''Enter in room which have related castle building. Access should be allowed when castle building have level > 0'''
        def __init__(self, bld_uid):
            self.bld_uid = bld_uid

        def get_sensitive(self):
            if self.bld_uid in castle.buildings:
                if castle.buildings[self.bld_uid].lvl > 0:
                    return True

        def __call__(self):
            '''Calls label related to building; label name should be same as uid of building'''
            renpy.call(self.bld_uid)

    # castle menu locations
    castle_menu = {'ground': ('rowans_chambers', 'portal_room', 'throne_room', 'library', 'quarters', 'tavern', 'caravan', 'workshop'),
                'basement': ('dungeon', 'barracks', 'forge', 'sanctum', 'pit', 'brothel',  'arena', 'summoning')}

    # (names, coordinates, action and action args) for imagebuttons in castle maps (order is from far rooms to close ones)
    ground_rooms_imagebuttons = [('portal_room', (312, 59), 'call', ('portal_room',)), ('stairs_up', (602, 141), 'None', None),
        ('stairs_down', (423, 306), 'SetVariable', ('castle_map_level', 'basement')),
        ('rowans_chambers', (749, 16), 'jump', ('rowans_chambers',)), ('guest_wing', (745, 93), 'call', ('guest_wing',)), ('liurial_room', (543, 224), 'None', None),
        ('mess_hall', (1030, 162), 'None', None), ('throne_room', (616, 271), 'call', ('throne_room',)), ('library', (273, 376), 'call', ('library',)),
        ('workshop', (546, 538), 'call', ('workshop',)), ('tavern', (311, 713), 'enter_bld', ('tavern',)), ('caravan', (1583, 850), 'call', ('caravan',)),]
#~         ('barracks', (350, 190)),
#~         ('brothel', (915, 171)),]

    basement_rooms_imagebuttons = 'nothing'

## castle_map.rpy stuff
# Point of Interest location and character icons
define topLeftOffsetX = 425
define topLeftOffsetY = 175
define centerOffsetX = 710
define centerOffsetY = 310
define topRightOffsetX = 785
define topRightOffsetY = 200

define bottomLeftOffsetX = 450
define bottomLeftOffsetY = 395

# GRID
define topOffsetX = 600
define topOffsetY = 60
define leftOffsetX = 265
define leftOffsetY = 250
define rightOffsetX = 975
define rightOffsetY = 280
define bottomOffsetX = 640
define bottomOffsetY = 475

#GROUND - Idle
define poi_chambers = 'images/map/character_locations/chambers.png'
define poi_chambers2 = 'images/map/character_locations/chambers2.png'
define poi_tavern = 'images/map/character_locations/tavern.png'
define poi_guest = 'images/map/character_locations/guest_wing.png'
define poi_caravan = 'images/map/character_locations/caravan.png'
define poi_library = 'images/map/character_locations/library.png'
define poi_quarters = 'images/map/character_locations/quarters.png'
define poi_workshop = 'images/map/character_locations/workshop.png'
define poi_hallway = 'images/map/character_locations/hallway.png'
#UNDERGROUND - Idle
define poi_dungeon = 'images/map/character_locations/dungeon.png'
define poi_brothel = 'images/map/character_locations/brothel.png'
define poi_sanctum = 'images/map/character_locations/sanctum.png'
define poi_forge = 'images/map/character_locations/forge.png'
define poi_barracks = 'images/map/character_locations/barracks.png'
define poi_breeding_pit = 'images/map/character_locations/breeding_pit.png'

#GROUND - Hover
define poi_chambers_h = 'images/map/character_locations/chambers_h.png'
define poi_chambers2_h = 'images/map/character_locations/chambers2_h.png'
define poi_tavern_h = 'images/map/character_locations/tavern_h.png'
define poi_guest_h = 'images/map/character_locations/guest_wing_h.png'
define poi_caravan_h = 'images/map/character_locations/caravan_h.png'
define poi_library_h = 'images/map/character_locations/library_h.png'
define poi_quarters_h = 'images/map/character_locations/quarters_h.png'
define poi_workshop_h = 'images/map/character_locations/workshop_h.png'
define poi_hallway_h = 'images/map/character_locations/hallway_h.png'
#UNDERGROUND - Hover
define poi_dungeon_h = 'images/map/character_locations/dungeon_h.png'
define poi_brothel_h = 'images/map/character_locations/brothel_h.png'
define poi_sanctum_h = 'images/map/character_locations/sanctum_h.png'
define poi_forge_h = 'images/map/character_locations/forge_h.png'
define poi_barracks_h = 'images/map/character_locations/barracks_h.png'
define poi_breeding_pit_h = 'images/map/character_locations/breeding_pit_h.png'

##Underground Buttons

define bt_neutral = '_Neutral'
define bt_hover = '_Hover'

define bt_emptyRoom = 'images/map/underground/Button_EmptyRoom' + '_Neutral.png'
define bt_UnderConstruction = 'images/map/underground/Button_UnderConstruction' + '_Neutral.png'

# Button Idle
define bt_arena = 'images/map/underground/Button_Arena' + '_Neutral.png'
define bt_barracks = 'images/map/underground/Button_Barracks' + '_Neutral.png'
define bt_breeding_pit = 'images/map/underground/Button_BreedingPit' + '_Neutral.png'
define bt_brothel = 'images/map/underground/Button_Brothel' + '_Neutral.png'
define bt_dungeon = 'images/map/underground/Button_Dungeon' + '_Neutral.png'
define bt_forge = 'images/map/underground/Button_Forge' + '_Neutral.png'
define bt_sanctum = 'images/map/underground/Button_DarkSanctum' + '_Neutral.png'
define bt_stairs_down = 'images/map/underground/Button_StairsDown' + '_Neutral.png'
define bt_stairs_up = 'images/map/underground/Button_StairsUp' + '_Neutral.png'

# Button Hover
define bt_arena_h = 'images/map/underground/Button_Arena' + '_Hover.png'
define bt_barracks_h = 'images/map/underground/Button_Barracks' + '_Hover.png'
define bt_breeding_pit_h = 'images/map/underground/Button_BreedingPit' + '_Hover.png'
define bt_brothel_h = 'images/map/underground/Button_Brothel' + '_Hover.png'
define bt_dungeon_h = 'images/map/underground/Button_Dungeon' + '_Hover.png'
define bt_forge_h = 'images/map/underground/Button_Forge' + '_Hover.png'
define bt_sanctum_h = 'images/map/underground/Button_DarkSanctum' + '_Hover.png'
define bt_stairs_down_h = 'images/map/underground/Button_StairsDown' + '_Hover.png'
define bt_stairs_up_h = 'images/map/underground/Button_StairsUp' + '_Hover.png'

# GROUND BUTTONS

# Button Idle
define bt_portal = 'images/map/castle/portal_room.png'
define bt_stairs_up = 'images/map/castle/stairs_up.png'
define bt_stairs_down = 'images/map/castle/stairs_down.png'
define bt_chambers = 'images/map/castle/rowans_chambers.png'
define bt_guest = 'images/map/castle/guest_wing.png'
define bt_liurial = 'images/map/castle/liurial_room.png'
define bt_messhall = 'images/map/castle/mess_hall.png'
define bt_throne = 'images/map/castle/throne_room.png'
define bt_library = 'images/map/castle/library.png'
define bt_workshop = 'images/map/castle/workshop.png'
define bt_tavern = 'images/map/castle/tavern.png'
define bt_caravan = 'images/map/castle/caravan.png'

# Button Hover
define bt_portal_h = 'images/map/castle/portal_room_hover.png'
define bt_stairs_up_h = 'images/map/castle/stairs_up_hover.png'
define bt_stairs_down_h = 'images/map/castle/stairs_down_hover.png'
define bt_chambers_h = 'images/map/castle/rowans_chambers_hover.png'
define bt_guest_h = 'images/map/castle/guest_wing_hover.png'
define bt_liurial_h = 'images/map/castle/liurial_room_hover.png'
define bt_messhall_h = 'images/map/castle/mess_hall_hover.png'
define bt_throne_h = 'images/map/castle/throne_room_hover.png'
define bt_library_h = 'images/map/castle/library_hover.png'
define bt_workshop_h = 'images/map/castle/workshop_hover.png'
define bt_tavern_h = 'images/map/castle/tavern_hover.png'
define bt_caravan_h = 'images/map/castle/caravan_hover.png'
