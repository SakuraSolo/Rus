# preview maps and check their generation
screen map_preview_screen():
    style_prefix "map_preview"
    frame:
        xfill True
        yfill True
        background None
        has hbox
        frame:
            yfill True
            xsize 300
            background '#357'
            has vbox
            textbutton 'Return' action Return()
            # list of json maps in maps folder
            frame:
                xfill True
                ysize 200
                background '#333'
                viewport:
                    mousewheel True
                    scrollbars 'vertical'
                    vbox:
                        for fname in [f for f in renpy.list_files() if f.startswith('maps/') and f.endswith('.json')]:
                            textbutton fname action [MPChangeMap(fname), renpy.restart_interaction]
            # buttons for generators and durations
            frame:
                xfill True
                yfill True
                background '#579'
                if map_preview_current_path:
                    vbox:
                        text map_preview_current_path
                        textbutton 'Load fixed' action [MPLoadFixed(), renpy.restart_interaction]
                        textbutton 'Add random terrain' action [MPAddRandomTerrain(), renpy.restart_interaction]
                        textbutton 'Add random resources' action [MPAddRandomResources(), renpy.restart_interaction]
                        # durations for generation stages
                        frame:
                            xfill True
                            yalign 1.0
                            has vbox
                            for rec in map_preview_durations:
                                text '{}: {}'.format(rec, map_preview_durations[rec])
        # map view
        frame:
            xfill True
            yfill True
            background '#777'
            if map_preview_renderer:
                viewport:
                    draggable True
                    scrollbars 'both'
                    fixed:
                        at map_zoom(map_preview_renderer.zoom)
                        xysize (map_preview_renderer.width, map_preview_renderer.height)
                        add map_preview_renderer.sm
                hbox:
                    text 'Zoom'
                    textbutton '1' action SetField(map_preview_renderer, 'zoom', 1)
                    textbutton '0.6' action SetField(map_preview_renderer, 'zoom', 0.6)
                    textbutton '0.3' action SetField(map_preview_renderer, 'zoom', 0.3)
                    textbutton '0.1' action SetField(map_preview_renderer, 'zoom', 0.1)


style map_preview_frame is frame:
    xpadding 0
    ypadding 0


init python:
    from datetime import datetime


    class MPRenderer():
        '''Holds data about map and its geometry'''
        def __init__(self):
            # sprite manager and sprites
            self.sm = None
            self.sprites = []
            # width and height of map in pixels
            self.width = None
            self.height = None
            self.zoom = 1


    map_preview_maps = []
    map_preview_mapdef = None
    map_preview_current_path = None
    map_preview_renderer = MPRenderer()
    map_preview_durations = {}


    class MPChangeMap(Action):
        '''Changes current map in map preview'''
        def __init__(self, fname):
            self.fname = fname

        def __call__(self):
            # reset all preview data for new map
            global map_preview_current_path, map_preview_maps, map_preview_mapdef, map_preview_renderer, map_preview_durations
            map_preview_current_path = self.fname
            map_preview_maps = []
            map_preview_mapdef = None
            map_preview_renderer = MPRenderer()
            map_preview_durations = {}


    class MPLoadFixed(Action):
        def __call__(self):
            global map_preview_maps, map_preview_mapdef
            map_preview_maps = []
            with renpy.file(map_preview_current_path) as mapdef_file:
                mapdef_str = mapdef_file.read()
            map_preview_mapdef = convert_json_to_mapdef(mapdef_str)
            t1 = datetime.now()
            # create blank map with required dimensions
            m = create_blank_map(map_preview_mapdef['width'], map_preview_mapdef['height'])
            dt1 = datetime.now()-t1
            map_preview_durations['blank map'] = '{}.{:06}'.format(dt1.seconds, dt1.microseconds)
            t1 = datetime.now()
            # add fixed hexes to blank map
            map_add_fixed_hexes(m, map_preview_mapdef)
            dt1 = datetime.now()-t1
            map_preview_durations['fixed hexes'] = '{}.{:06}'.format(dt1.seconds, dt1.microseconds)
            map_preview_maps.append(m)
            render_map_to_sm(m)


    class MPAddRandomTerrain(Action):
        def get_sensitive(self):
            # can add random terrain if mapdef and fixed hexes are loaded
            global map_preview_maps
            if len(map_preview_maps) >= 1:
                return True

        def __call__(self):
            # remove later map stages and regenerate random terrain
            global map_preview_maps
            map_preview_maps = map_preview_maps[:1]
            m = copy.deepcopy(map_preview_maps[0])
            t1 = datetime.now()
            map_add_randomized_terrain(m, map_preview_mapdef)
            map_randomize_tile_images(m, map_preview_mapdef)
            dt1 = datetime.now()-t1
            map_preview_durations['random terrain'] = '{}.{:06}'.format(dt1.seconds, dt1.microseconds)
            map_preview_maps.append(m)
            render_map_to_sm(m)


    class MPAddRandomResources(Action):
        def get_sensitive(self):
            # can add random resources if mapdef and fixed hexes are loaded, and random terrain is added
            global map_preview_maps
            if len(map_preview_maps) >= 2:
                return True

        def __call__(self):
            # remove later map stages and regenerate random resources
            global map_preview_maps
            map_preview_maps = map_preview_maps[:2]
            m = copy.deepcopy(map_preview_maps[1])
            t1 = datetime.now()
            map_add_random_resources(m, map_preview_mapdef)
            dt1 = datetime.now()-t1
            map_preview_durations['random resources'] = '{}.{:06}'.format(dt1.seconds, dt1.microseconds)
            map_preview_maps.append(m)
            render_map_to_sm(m)


    def render_map_to_sm(m):
        global map_preview_renderer
        map_preview_renderer.sm = SpriteManager()
        map_preview_renderer.sprites = []
        for hex in m.hexes:
            # TODO: maybe it makes sense to create displaybles for each tile type and then use them (to not create image for each tile)
            # if there is a resource on tile, show it instead of tile terrain (currently resources fully hide underlaying terrain)
            if hex[6] > 0:
                map_preview_renderer.sprites.append(map_preview_renderer.sm.create(resourceImages[hex[6]]))
            # show tile variations, if hex has them already, else show first variant
            elif hex[10] >= 0:
                map_preview_renderer.sprites.append(map_preview_renderer.sm.create(terrain_data[hex[3]][2][hex[10]]))
            else:
                map_preview_renderer.sprites.append(map_preview_renderer.sm.create(terrain_data[hex[3]][2][0]))
            # set tile display coordinates
            map_preview_renderer.sprites[-1].x = hex[1][0] * int(194 * 0.75)
            if hex[1][0] % 2:
                map_preview_renderer.sprites[-1].y = hex[1][1] * 169 + 169 / 2
            else:
                map_preview_renderer.sprites[-1].y = hex[1][1] * 169
        # show player position
        map_preview_renderer.sprites.append(map_preview_renderer.sm.create('map_gui/Sword cursor.png'))
        map_preview_renderer.sprites[-1].x = m.pos[0] * int(194 * 0.75) + 58
        if m.pos[0] % 2:
            map_preview_renderer.sprites[-1].y = m.pos[1] * 169 + 30
        else:
            map_preview_renderer.sprites[-1].y = m.pos[1] * 169 - 55
        # set dimensions for whole sprite manager
        map_preview_renderer.width = m.width * int(194 * 0.75) + int(194 * 0.25) + 6
        map_preview_renderer.height = m.height * 169 + 201/2
