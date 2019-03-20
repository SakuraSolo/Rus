# savegame patches for developer mode
label after_load:
    # if saved version is lower than current one, cumulatively apply patches up to current version
    while sgv < current_sgv:
        $ sgv += 1
        $ patch_name = ''.join(('sg_patch', str(sgv)))
        $ globals()[patch_name]()


init python:
    # current version for savegames (most recent)
    current_sgv = 17


    # savegame version at a game start, will be saved in savegames
    def __sgv_init():
        store.sgv = 17

    config.start_callbacks.append(__sgv_init)


init -1 python:
    def sg_patch2():
        for spy in castle.buildings['brothel'].spies:
            spy.uid = new_uid()
            all_objects[spy.uid] = spy


    def sg_patch3():
        # replace spies in brothel by their uids
        castle.buildings['brothel'].spies = [spy.uid for spy in castle.buildings['brothel'].spies]


    def sg_patch4():
        # add names for existing spies
        for uid in castle.buildings['brothel'].spies:
            spy = get_object(uid)
            spy.name = random.choice(spy_names[spy.sex])


    def sg_patch5():
        # add available_spies
        castle.buildings['brothel'].available_spies = []


    def sg_patch6():
        # add prisoners status
        castle.buildings['dungeon'].prisoners_status = {
            'slave': [0, 10],
            'ransom': [0, 3],
            'gladiator': [0, 3],
            'test': [0, 5]}
        castle.buildings['dungeon'].prisoners_auto = {
                'slave': False,
                'ransom': False,
                'gladiator': False,
                'test': False}


    def sg_patch7():
        # add levels and traits to existing spies
        for obj in all_objects.itervalues():
            if isinstance(obj, Spy):
                obj.lvl = 0
                obj.traits.append(random.choice(spy_traits[obj.sex]))


    def sg_patch8():
        # add Arthdale
        world.maps['first_map'].hexes[14] = [ 14, [2, 1], [2, 3, 15, 26, 13, 1], 0, False, False, 102, False, 0, [] , 0]


    def sg_patch9():
        store.tania_name = 'Woman'


    def sg_patch10():
        # add drider nest
        world.maps['first_map'].hexes[133] = [ 133, [1, 11], [121, 134, 146, 145, 144, 132], 0, False, False, 9, False, 0, [] , 0]


    def sg_patch11():
        # fix rumors states
        if all_rumors['Goblin prince Tue-Row'].state == 'unavailable':
            all_rumors['Goblin prince Tue-Row'].state = 'available'
        if all_rumors['Famine looms'].state == 'unavailable':
            all_rumors['Famine looms'].state = 'available'
        if all_rumors['Orcs in the North'].state == 'unavailable':
            all_rumors['Orcs in the North'].state = 'available'

    def sg_patch12():
        # change "breeding pit" class to BreedingPit
        old_lvl = castle.buildings['pit'].lvl
        castle.buildings['pit'] = BreedingPit('pit')
        while castle.buildings['pit'].lvl < old_lvl:
            castle.buildings['pit'].build()


    def sg_patch13():
        # add Orciad camp
        if world.maps['rosaria_map'].hexes[41][6] != 105:
            world.maps['rosaria_map'].hexes[41][6] = 105
            world.maps['rosaria_map'].hexes[41][5] = False


    def sg_patch14():
        # add Tamir
        Actor('tamir', 'Tamir')
        store.journal = Journal()
        for entry in ['checks_start', 'checks_partial', 'corruption_start', 'corruption_increasing', 'gold_start', 'intelligence_start',
            'luck_start', 'primary_statistics', 'reflexes', 'skills', 'strength', 'vitality']:
            journal.glossary_add(entry)
        for entry in ['rowan_starting', 'alexia_starting', 'village_elder_starting', 'karnas_starting', 'deanara_starting', 'jezera_starting',
            'andras_starting', 'arthdale_starting', 'bloodmeen_starting', 'punishment', 'solansia_starting', 'kharos_starting', 'six_realms_starting',
            'solance_starting']:
            journal.codex_add(entry)
        # set up Alexia's magic if "alexia_s_power" happened
        if ev_happened('alexia_s_power'):
            store.alexia_knows_magic = True
            store.alexia_ice_shard = 1

        castle.surface_maintenance_reduction = 0


    def sg_patch15():
        store.avatar._mp_penalty = 0


    def sg_patch16():
        for ac in all_actors.values():
            ac._total_favors = ac._favors
        if 'andras_influence' not in all_actors['alexia'].flags:
            all_actors['alexia'].flags['andras_influence'] = 0
        if 'jezera_influence' not in all_actors['alexia'].flags:
            all_actors['alexia'].flags['jezera_influence'] = 0
        for bld in castle.buildings.values():
            if bld.lvl > 0:
                bld._capacity = all_buildings[bld.uid]['capacity'] + bld.lvl * all_buildings[bld.uid]['up_capacity']
            else:
                bld._capacity = 0


    def sg_patch17():
        global ground_rooms_imagebuttons
        ground_rooms_imagebuttons = [('portal_room', (312, 59), 'call', ('portal_room',)), ('stairs_up', (602, 141), 'None', None),
            ('stairs_down', (423, 306), 'SetVariable', ('castle_map_level', 'basement')),
            ('rowans_chambers', (749, 16), 'jump', ('rowans_chambers',)), ('guest_wing', (745, 93), 'call', ('guest_wing',)), ('liurial_room', (543, 224), 'None', None),
            ('mess_hall', (1030, 162), 'None', None), ('throne_room', (616, 271), 'call', ('throne_room',)), ('library', (273, 376), 'call', ('library',)),
            ('workshop', (546, 538), 'call', ('workshop',)), ('tavern', (311, 713), 'enter_bld', ('tavern',)), ('caravan', (1583, 850), 'call', ('caravan',)),]
        global visitable_locations
        visitable_locations = ('rowans_chambers', 'stairs_up', 'stairs_down', 'mess_hall', 'portal_room', 'liurial_room', 'throne_room', 'library', 'quarters', 'tavern', 'caravan', 'workshop', 'dungeon', 'barracks', 'forge', 'sanctum', 'pit', 'brothel', 'arena', 'summoning')
        # add new actor
        Actor('xzaratl', 'X’zaratl')
