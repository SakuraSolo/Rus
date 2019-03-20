# world and map
init python:
    #Random functionality is not included in Python's base.
    import random
    import copy


    class World(object):
        '''World, holds maps'''

        def __init__(self):
            self.maps = {}
            self._cur_map_uid = None
            # this prevents current tile from being set as 'explored'
            self._prevent_exploration = False
            # if this is set, player will be pushed back to previous tile
            self._push_back = False

        @property
        def cur_map(self):
            if self._cur_map_uid:
                return self.maps[self._cur_map_uid]

        @property
        def cur_hex(self):
            '''Returns current hex under player'''
            if self._cur_map_uid:
                return self.cur_map.hexes[self.cur_map.pos_id]

        @property
        def cur_tile_type(self):
            '''Returns the type of the tile player is on now'''
            if self.cur_map:
                return terrain_data[self.cur_map.terrain(self.cur_map.pos)][1]

        def create_map(self, map_def):
            '''Creates and adds a map from given map_def'''
            self.maps[map_def['uid']] = create_map(map_def)

        def enter(self, uid):
            '''Makes map "uid" ready for exploration'''
            self._cur_map_uid = uid
            self.cur_map.visited = week

        def exit(self):
            self._cur_map_uid = None


    class Map(object):
        '''Map of separate game territory'''

        def __init__(self):
            self.uid = ''
            self.name = ''
            self.hexes = []
            self.resources = {}
            # {coords1: portal_name1, ...}
            self.portals = {}
            self.width = 0
            self.height = 0
            # player position
            self.pos = [0, 0]
            # previous position of the player
            self.previous_pos = self.pos
            # timestamp (week) of last visit to this map
            self.visited = False

        def terrain(self, coord):
            '''Returns terrain ID on given coords or hex ID'''
            if isinstance(coord, tuple) or isinstance(coord, list):
                return self.hexes[self._id_from_coord(coord)][3]
            return self.hexes[coord][3]

        def _id_from_coord(self, coord):
            return self.width * coord[1] + coord[0]

        def _coords_from_id(self, _id):
            return (_id % self.width, _id / self.width)

        @property
        def pos_id(self):
            '''Returns hex id of current player position'''
            return self._id_from_coord(self.pos)

        @pos_id.setter
        def pos_id(self, val):
            self.pos = self._coords_from_id(val)


    class MapResource(object):
        '''Base class for map resources'''
        def __init__(self, map_, coords, res_id):
            # parent map uid
            self.map_uid = map_.uid
            # coordinates of resource
            self.coords = tuple(coords)
            # resource id (type)
            self.res_id = res_id
            # uid - uid of parent map joined with coordinates
            self.uid = '_'.join((map_.uid, str(self.coords[0]), str(self.coords[1])))
            # if player saw this resource (if hex under it is visible)
            self.seen = False
            # if player visited this resource (not equal to "explored" state of hex)
            self.visited = False
            # additional state of resource (captured, destroyed)
            self.state = None
            # kind of resource (for generating name)
            self.kind = 'Resource'

        @property
        def name(self):
            return ' '.join((self.kind, str(self.coords)))

        def capture(self):
            '''Marks resource as captured'''
            self.state = 'captured'
            self.on_capture()

        def destroy(self):
            '''Marks resource as destroyed'''
            self.state = 'destroyed'

        def on_capture(self):
            '''Do something when this resource is captured'''
            pass


    class MRPortal(MapResource):
        '''Portal'''
        def __init__(self, map_, coords, res_id):
            super(MRPortal, self).__init__(map_, coords, res_id)
            self.kind = 'Portal'
            self._name = map_.portals[tuple(coords)]

        @property
        def name(self):
            return self._name


    class MRVillage(MapResource):
        '''Village'''
        def __init__(self, map_, coords, res_id):
            super(MRVillage, self).__init__(map_, coords, res_id)
            self.kind = 'Village'

        def on_capture(self):
            castle.villages += 1
            castle.villages_income += 5


    class MRMine(MapResource):
        '''Mine'''
        def __init__(self, map_, coords, res_id):
            super(MRMine, self).__init__(map_, coords, res_id)
            self.kind = 'Mine'


    class MRDriderNest(MapResource):
        '''Drider nest'''
        def __init__(self, map_, coords, res_id):
            super(MRDriderNest, self).__init__(map_, coords, res_id)
            self.kind = 'Drider nest'

        def on_capture(self):
            castle.buildings['pit'].drider_recruitment += 0.5


    class MRFortress(MapResource):
        '''Fortress (keep)'''
        def __init__(self, map_, coords, res_id):
            super(MRFortress, self).__init__(map_, coords, res_id)
            self.kind = 'Fortress'


    class MROrcTribe(MapResource):
        '''Orc tribe'''
        def __init__(self, map_, coords, res_id):
            super(MROrcTribe, self).__init__(map_, coords, res_id)
            self.kind = 'Orc tribe'


    class MRWinery(MapResource):
        '''Winery'''
        def __init__(self, map_, coords, res_id):
            super(MRWinery, self).__init__(map_, coords, res_id)
            self.kind = 'Winery'


    class MRAbbey(MapResource):
        '''Abbey'''
        def __init__(self, map_, coords, res_id):
            super(MRAbbey, self).__init__(map_, coords, res_id)
            self.kind = 'Abbey'


    def get_map_resource(map_uid, coords):
        '''Returns resource on given map and position'''
        return world.maps[map_uid].resources[tuple(coords)]
