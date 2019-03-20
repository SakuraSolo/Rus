# realms and locations (outer lands)
init python:
    # all realms of the game
    # format all_realms = {'realm_uid': {'name': 'readable name', 'locs': (list of locations)}, ...}
    all_realms = {
        'rosaria': {
            'name': 'Rosaria',
            'locs': ('rastedel', 'arthdale', 'uzzags_camp')},
        'prothea': {
            'name': 'Prothea',
            'locs': ('cathedral', 'delight_inn', 'cheapside')},
        'tundra': {
            'name': 'Frozen Tundra',
            'locs': ('uvarth', 'dragons_fall', 'frost_crown')},
        'forest': {
            'name': 'Forest of Ealoean',
            'locs': ('sharazzat', 'theralthas', 'great_tree')},
        'dragons_tail': {
            'name': 'Dragon\'s Tail',
            'locs': ('travelers_rest', 'temple_moons', 'petrified_forest')},
        'empire': {
            'name': 'Empire of Sand',
            'locs': ('qerazel', 'forgotten_city', 'oasis')},
    }

    # all locations of the game
    # format all_locs = {'loc_uid': {'name': 'readable name'}, ...}
    all_locs = {
        'rastedel': {'name': 'Rastedel'},
        'arthdale': {'name': 'Arthdale'},
        'uzzags_camp': {'name': 'Uzzag\'s Camp'},
        'uvarth': {'name': 'Uvarth'},
        'dragons_fall': {'name': 'Fel Dragon\'s Fall'},
        'frost_crown': {'name': 'Frost Crown'},
        'sharazzat': {'name': 'Sharazzat'},
        'theralthas': {'name': 'Ruins of Theralthas'},
        'great_tree': {'name': 'The Great Tree'},
        'travelers_rest': {'name': 'Travelers Rest'},
        'temple_moons': {'name': 'Temple of the Three Moons'},
        'petrified_forest': {'name': 'Petrified Forest'},
        'qerazel': {'name': 'Qerazel'},
        'forgotten_city': {'name': 'The Forgotten City'},
        'oasis': {'name': 'Crescent Oasis'},
        'cathedral': {'name': 'Cathedral of Light'},
        'delight_inn': {'name': 'The Mummer\'s Delight Inn'},
        'cheapside': {'name': 'Cheapside'},
    }

    class Lands(object):
        '''Controls all outer lands (areas/locations)'''
        def __init__(self, realms_defs, locs_defs):
            self.realms = {}
            for uid in realms_defs:
                realm_locs = {uid: locs_defs[uid] for uid in realms_defs[uid]['locs']}
                self.realms.update({uid: Realm(uid, realms_defs[uid]['name'], realm_locs)})

        def __iter__(self):
            '''Return iterator over all realms'''
            return iter(self.realms.values())

        def __getitem__(self, k):
            return self.realms[k]


    class Realm(object):
        '''One part of game world, containing locations'''
        def __init__(self, uid, name, locs):
            self.uid = uid
            self.name = name
            # realm is unlocked by default
            self.accessible = True
            # info level (0 at start)
            self.info_level = 0
            # create locations
            self.locs = {}
            for uid in locs:
                self.locs.update({uid: Location(uid, locs[uid]['name'])})

        def __iter__(self):
            '''Return iterator over all locs'''
            return iter(self.locs.values())

        def __contains__(self, loc):
            return loc in self.locs

        def __getitem__(self, k):
            return self.locs[k]

        @property
        def descr(self):
            return 'No description'


    class Location(object):
        '''Single game location'''
        def __init__(self, uid, name):
            self.uid = uid
            self.name = name
            self.accessible = False
            self.visible = False

        @property
        def descr(self):
            return 'No description'
