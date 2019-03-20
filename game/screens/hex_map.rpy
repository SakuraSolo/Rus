# screen for map exploration

transform map_zoom(map_zoom):
    zoom map_zoom


screen hex_map:
    frame:
        xpadding 0
        ypadding 0
        # bottom layer of decorative textures
        background 'map_gui/texture back.png'

        #Terrain and resource hexes
        frame:
            xpadding 0
            ypadding 0
            background None
            at map_zoom(mview.zoom)
            # assuming map uses full 1280*720 screen
            pos (int(640*(1-mview.zoom)), int(360*(1-mview.zoom)))
            for i in range (0, len(world.cur_map.hexes)):
                # only draw hexes that are in viewport
                if mview.in_viewport(i):
                    $ (screen_x, screen_y) = mview.screen_coords_from_id(i)
                    # Display visible hexes
                    if (world.cur_map.hexes[i][4] == True):
                        # if there is a resource, it will be drawn, else terrain will be drawn
                        if (world.cur_map.hexes[i][6] > 0):
                            $ tile_img = resourceImages[world.cur_map.hexes[i][6]]
                        else:
                            $ tile_img = terrain_data[world.cur_map.hexes[i][3]][2][world.cur_map.hexes[i][10]]
                        #If tile was not visited yet, draw it with less brightness (except of impassable terrains)
                        if (world.cur_map.hexes[i][5] == True or (terrain_data[world.cur_map.hexes[i][3]][0] < 0)):
                            add tile_img pos (screen_x, screen_y)
                        else:
                            add im.MatrixColor(tile_img, im.matrix.brightness(-0.25)) pos (screen_x, screen_y)
                    else:
                        # draw unseen tiles
                        if mview.show_unseen:
                            # if there is a resource, it will be drawn, else terrain will be drawn
                            if (world.cur_map.hexes[i][6] > 0):
                                $ tile_img = resourceImages[world.cur_map.hexes[i][6]]
                            else:
                                $ tile_img = terrain_data[world.cur_map.hexes[i][3]][2][world.cur_map.hexes[i][10]]
                            add im.MatrixColor(tile_img, mview.unseen_tint) pos (screen_x, screen_y)
                        else:
                            add 'map tiles/unseen.png' pos (screen_x, screen_y)
            # draw buttons on adjacent hexes, if they are passable
            for i in range(6):
                $ linked_hex_id = world.cur_hex[2][i]
                # if hex in direction "i" is linked
                if linked_hex_id > 0:
                    # if terrain is passable
                    if terrain_data[world.cur_map.hexes[linked_hex_id][3]][0] > 0:
                        $ (screen_x, screen_y) = mview.screen_coords_from_id(linked_hex_id)
                        imagebutton pos (screen_x, screen_y) action Return(i):
                            idle "hex_highlight"
                            hover "hex_highlight_hover"
                            focus_mask "hex_highlight"
            # 3192x4505

            #$ xOverLayOffset = 700;
            #$ yOverLayOffset = 262;

            #$ widthOffset = 194
            #$ heightOffset = 169

            #$ widthOddset = 50
            #$ heightOddset = heightOffset/2

            #$ playerX = -tuple(world.cur_hex[1])[0]
            #$ playerY = -tuple(world.cur_hex[1])[1]

            #$ hexXPos = xOverLayOffset + (widthOffset * playerX)
            #$ hexYPos = yOverLayOffset + (heightOffset * playerY)

            #if tuple(world.cur_hex[1])[0] % 2 == 1:
            #    $ hexXPos = xOverLayOffset + (widthOffset * playerX) - widthOddset
            #    $ hexYPos = yOverLayOffset + (heightOffset * playerY) - heightOddset
            #if (world.cur_map.pos[0]%2 == 0):
            #     $ hexXPos = xOverLayOffset + (widthOffset * playerX) + widthOddset
            #     $ hexYPos = yOverLayOffset + (heightOffset * playerY) + heightOddset
            #else:
            #     $ hexXPos = xOverLayOffset + (widthOffset * playerX) - widthOddset
            #     $ hexYPos = yOverLayOffset + (heightOffset * playerY) - heightOddset

            #add 'map_gui/overworld detail done a.png' pos (hexXPos, hexYPos)

        #Player icon
        add 'map_gui/Sword cursor.png' pos (mview.mapXCenter+mview.playerOffset, mview.mapYCenter-55)
        # top layer of decorative textures
        add 'map_gui/texture top.png'

        #Buttons (compass) to control character

        frame:
            background None
            pos (12, 500)
            add 'map_gui/compass/BG.png' pos (5, 35)
            imagebutton pos (75, 31) action Return (1):
                idle 'map_gui/compass/NE idle.png'
                hover 'map_gui/compass/NE hover.png'
                focus_mask 'map_gui/compass/NE hover.png'
            imagebutton pos (75, 98) action Return (2):
                idle 'map_gui/compass/SE idle.png'
                hover 'map_gui/compass/SE hover.png'
                focus_mask 'map_gui/compass/SE hover.png'
            imagebutton pos (60, 96) action Return (3):
                idle 'map_gui/compass/s idle.png'
                hover 'map_gui/compass/S hover.png'
                focus_mask 'map_gui/compass/S hover.png'
            imagebutton pos (0, 98) action Return (4):
                idle 'map_gui/compass/SW idle.png'
                hover 'map_gui/compass/SW hover.png'
                focus_mask 'map_gui/compass/SW hover.png'
            imagebutton pos (0, 31) action Return (5):
                idle 'map_gui/compass/NW idle.png'
                hover 'map_gui/compass/NW hover.png'
                focus_mask 'map_gui/compass/NW hover.png'
            imagebutton pos (60, 0) action Return (0):
                idle 'map_gui/compass/N idle.png'
                hover 'map_gui/compass/N hover.png'
                focus_mask 'map_gui/compass/N hover.png'

        key 'w' action Return(0)
        key 'e' action Return(1)
        key 'd' action Return(2)
        key 's' action Return(3)
        key 'a' action Return(4)
        key 'q' action Return(5)

        #Movement points remaining.
        #add 'map_gui/Area name copy 3.png' xalign 0.90 yalign 0.02
        add 'map_gui/move icon.png' xalign 0.99  yalign 0.18
        text str(avatar.mp) xalign 0.92 yalign 0.21 size 35 color '#d4d4d4'
        # name of the map
        add 'map_gui/Area name.png' xalign 0.4 yalign 0.99
        text world.cur_map.name xalign 0.5 yalign 0.95 size 40 color '#d4d4d4'
        # current week
        add 'map_gui/Area name copy 2.png'  xalign 0.97 yalign 0.04
        text '[week]' xalign 0.92  yalign 0.06 size 35 color '#d4d4d4'
        # "End exploration" button
        textbutton "End exploration" action Return(-1) :
            align (0.01, 0.02)
            style 'navi_button'

        if config.developer:
            use map_debug((0, 0.2))
            use map_resources_debug

        # show log messages (`~)
        key '`' action Show('messages')

        use journal_button((0.99, 1.0))


init python:
    class MapView():
        '''Various data related to map exploration and displaying'''

        def __init__(self):
            # dimensions of a tile image, including transparent area
            self.tileImgHeight = 201
            self.tileImgWidth = 200
            # dimensions of a hex (center of hex == center of tile)
            self.hexHeight = 169                    #Size of hex images, used by map displayer.
            self.hexMaxWidth = 194
            self.hexWidth = int(self.hexMaxWidth * 0.75)
            self.hexOffset = self.hexHeight / 2  #Offset of hexes in odd numbered columns
            self.resourceXOffset = 10        #How much to offset the resource icon from the top left corner of the hex.
            self.resourceYOffset = 10
            self.playerOffset = 58            #How much to offset the player icon from the top left corner of the hex.
            # center of screen minus half of full tile img dimensions
            self.mapXCenter = 540          #Where are we centering the screen?
            self.mapYCenter = 260
            # zoom level of map
            self.zoom = 1.0
            # debug - show unseen tiles
            self.show_unseen = False
            self.unseen_tint = im.matrix.tint(.8, .8, 1.0)

        def in_viewport(self, _id):
            '''Returns True if hex "_id" is in viewport'''
            # coords of hex "_id" and player position
            coords = world.cur_map._coords_from_id(_id)
            p_pos = world.cur_map.pos
            if abs(p_pos[0] - coords[0]) <= int_ceil(4/self.zoom) and abs(p_pos[1] - coords[1]) <= int_ceil(2/self.zoom):
                return True

        def screen_coords_from_id(self, hex_id):
            '''Returns screen coords for hex_id, on current map, depending on player\'s position'''
            x = (world.cur_map.hexes[hex_id][1][0]-world.cur_map.pos[0])*self.hexWidth+self.mapXCenter
            y = (world.cur_map.hexes[hex_id][1][1]-world.cur_map.pos[1])*self.hexHeight+self.mapYCenter
            # calculate offset based on player's position
            if ((world.cur_map.hexes[hex_id][1][0]-world.cur_map.pos[0]) % 2 == 1):
                # offset odd (relatively to player) hex columns vertically depending if player on even or odd column
                if (world.cur_map.pos[0]%2 == 0):
                    y = y + self.hexOffset
                else:
                    y = y - self.hexOffset
            return (x, y)

    mview = MapView()
