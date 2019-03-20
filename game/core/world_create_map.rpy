# functions for creating maps
init python:
    #Random functionality is not included in Python's base.
    import random
    import copy, json, ast


    #Coded by Dark Master, Copyright belongs to Venus Noire.

    #Map generation function.
    #Input:
    #       mapWidth, positive integer, represents number of hexes in a row.
    #       mapHeight, positive integer, represnts number of hexes in a column.
    #       fixedHexes, list of map hexes, will be assigned based on either index or position to map before random terrains are assigned.
    #       mapTerrains, list of terrain data to randomly assign on the map.  Format: [ int type, int amount to place, int min cluster size, int max cluster size ]
    #       defaultTerrain, integer value given to terrain that was not assigned at any point.
    #       ToDo mapResources, list of resource data to randomly assign on the map.  Format: [ int type, int amount to place, int terrain to find ]
    #Output:
    #       allHexes, list of map hexes, generated map.

    #Map hex:
    #       (index, [pos x, pos y], [hex links], terrain type, is space visible, is space explored, resource or building in space, is secret space, false terrain, event flag list, tile image variant)
    #       (ID, [x, y], [h], t, v, e, r, s, f, l, iv) - 11 elements
    #       0 = hex ID or index
    #       1 = [pos x, pos y]
    #       2 = [h0, h1, h2, h3, h4, h5]
    #       3 = terrain type
    #       4 = is space visible
    #       5 = is space explored
    #       6 = resource or building in space
    #       7 = is secret space
    #       8 = false terrain
    #       9 = event flag list
    #       10 = tile image variant (-1 for random, 0+ for fixed)

    def create_map_from_file(fname):
        '''Loads json map file and creates map from it'''
        with renpy.file(fname) as mapdef_file:
            mapdef_str = mapdef_file.read()
        mapdef = convert_json_to_mapdef(mapdef_str)
        return create_map(mapdef)


    def create_map(map_def):
        m = create_blank_map(map_def['width'], map_def['height'])
        map_copy_properties(m, map_def)
        map_add_fixed_hexes(m, map_def)
        map_add_randomized_terrain(m, map_def)
        map_add_random_resources(m, map_def)
        map_randomize_tile_images(m, map_def)
        map_create_resource_objects(m)
        return m


    def old_create_map(map_def):
        '''Creates map from map definition'''
        #create the list that contains all our hexes
        mapWidth = copy.deepcopy(map_def['width'])
        mapHeight = copy.deepcopy(map_def['height'])
        fixedHexes = copy.deepcopy(map_def['fixed'])
        mapTerrains = copy.deepcopy(map_def['terrains'])
        defaultTerrain = copy.deepcopy(map_def['default'])
        mapResources = copy.deepcopy(map_def['resources'])
        allHexes = []

        #Variable used to track the ID number of our current hex.
        hexCount = 0

        #populate the list with hexes based on the size of the map, they start with default values.
        for i in range (0, mapHeight):
            for j in range (0, mapWidth):
                allHexes.append( [ hexCount, [j, i], [-1, -1, -1, -1, -1, -1], -1, False, False, 0, False, 0, [], -1 ] )
                hexCount = hexCount + 1

        #Determine all hex links
        for i in range (0, hexCount):
            #newPos contains the destinations for values h0-h6.  Initialize it as empty.
            #newPos[h value] [x or y]
            newPos = []

            #Add six copies of the current location to newPos
            for j in range (0,6):
                newPos.append (list(allHexes[i][1]))       #Cloning a list, otherwise we're only creating a reference.

            #Calculate new positions of h0-h6
            #h0, up
            newPos[0][1] = newPos[0][1] - 1

            #h3, down
            newPos[3][1] = newPos[3][1] + 1

             #check if x is even or odd.
            if (allHexes[i][1][0]%2 == 0):
                #h1, up right
                newPos[1][0] = newPos[1][0] + 1
                newPos[1][1] = newPos[1][1] - 1

                #h2, down right
                newPos[2][0] = newPos[2][0] + 1

                #h4, down left
                newPos[4][0] = newPos[4][0] - 1

                #h5, up left
                newPos[5][0] = newPos[5][0] - 1
                newPos[5][1] = newPos[5][1] - 1

            else:
                #h1, up right
                newPos[1][0] = newPos[1][0] + 1

                #h2, down right
                newPos[2][0] = newPos[2][0] + 1
                newPos[2][1] = newPos[2][1] + 1

                #h4, down left
                newPos[4][0] = newPos[4][0] - 1
                newPos[4][1] = newPos[4][1] + 1

                #h5, up left
                newPos[5][0] = newPos[5][0] - 1


            #Check if any of our new positions are outside the map.  If they are, set that link to -1.
            for j in range (0,6):
                if (newPos[j][0] < 0 or newPos[j][0] >= mapWidth or newPos[j][1] < 0 or newPos[j][1] >= mapHeight):
                    allHexes[i][2][j] = -1
                else:
                    #Calculate index for the new position.
                    index = newPos[j][0]+newPos[j][1]*mapWidth
                    allHexes[i][2][j] = allHexes[index][0]

                    #Find the hex in the list with the new position.
                    #Main bottleneck is when linking.
                    #for k in range (0, hexCount):                       #First loop through all the hexes.
                    #    if (allHexes[k][1] == newPos[j]):              #See if we've found the one in the right position.
                    #        allHexes[i][2][j] = allHexes[k][0]          #If yes, assign that ID value to hj.
                    #        break



        #Begin assigning terrain

        #start by creating a list of all hexes that have not been given a terrain, initially this is all of them.
        unassignedHexes = list(allHexes)        #Use list so that we're cloning the list, rather than referencing it.

        #Copy the remaining list of unassignedHexes to use when placing resources.  This happens here so we can have
            #fixed terrain tiles but with random resources on them.
        resourceHexes = list(unassignedHexes)

        #Assign all fixed hexes, remove these hexes from unassignedHexes.
        for i in range (0, len(fixedHexes)):
            if (fixedHexes[i][0] >= 0):         #Assign by index.
                index = fixedHexes[i][0]
            else:                               #Assign by position.
                index = fixedHexes[i][1][0]+fixedHexes[i][1][1]*mapWidth
            # overwrite non-geometry data of generated hex by data from fixed hex
            allHexes[index][3:] = fixedHexes[i][3:]
            for j in range (0, len(unassignedHexes)):   #remove hex from unassignedHexes.
                if (unassignedHexes[j][0] == index):
                    unassignedHexes.pop(j)
                    break

            if (fixedHexes[i][6] >= 0):                 #if hex has a fixed resource, remove it from resourceHexes.
                for j in range (0, len(resourceHexes)):
                    if (resourceHexes[j][0] == index):
                        resourceHexes.pop(j)
                        break



        #Begin assigning randomized terrain.
        while (len(unassignedHexes) > 0 and len(mapTerrains) > 0):
            connectedHexes = [] #Clear connected hexes.
            #select a hex at random from unassignedHexes and add it to connectedHexes
            connectedHexes.append(list (unassignedHexes [random.randint(0, len(unassignedHexes)-1)]) )
            #select a terrain at random we haven't finished assigning yet.
            terrainIndex = random.randint(0, len(mapTerrains)-1)
            #determine how large this cluster should be.
            clusterSize = random.randint( mapTerrains[terrainIndex][2] ,mapTerrains[terrainIndex][3] )

            #loop until we run out of connected hexes, this cluster is finished, or the terrain has been fully assigned.
            while (len(connectedHexes) > 0 and clusterSize > 0 and mapTerrains[terrainIndex][1] > 0):
                #select a hex at random from connected hexes
                currentHexIndex = random.randint (0, len(connectedHexes)-1)     #note that currentHexIndex is with reference to connectedHexes, not allHexes
                currentHex = list(connectedHexes[currentHexIndex] )

                #assign that hex our terrain type in the original hex list of allHexes
                allHexes[currentHex[0]][3] = mapTerrains[terrainIndex][0]

                #remove the currentHex from unassignedHexes and connectedHexes.
                connectedHexes.pop(currentHexIndex)     #We know the index for the connectedHex
                for i in range (0, len(unassignedHexes)):       #We need to find the index for unassignedHexes
                    if (currentHex[0] == unassignedHexes[i][0]):
                        unassignedHexes.pop(i)
                        break

                #add all hexes connected to current hex that are in unassignedHexes, but not already in connectedHexes to connectedHexes.
                for i in range (0, 6):
                    hexIndexToFind = currentHex[2][i]   #note this index is with reference to allHexes.
                    if (hexIndexToFind != -1):                  #Don't search if the index is invalid.
                        found = False                               #Use this to track if we found it or not.
                        for j in range (0, len(connectedHexes)):     #Since connectedHexes will usually be smaller, we'll search that first.
                            if (hexIndexToFind == connectedHexes[j][0]):
                                found = True
                                break
                        if (found == False):                    #If we didn't find it in connectedHexes, then we search unassigned hexes.
                            for j in range (0, len(unassignedHexes)):
                                if (hexIndexToFind == unassignedHexes[j][0]):
                                    connectedHexes.append(unassignedHexes[j])
                                    break


                #decrement our cluster size and how many terrains we have to assign.
                clusterSize = clusterSize-1
                mapTerrains[terrainIndex][1] = mapTerrains[terrainIndex][1] - 1

            #check if we've fully assigned the current terrain
            if (mapTerrains[terrainIndex][1] <= 0):
                #remove that terrain from our list of terrains to be assigned.
                mapTerrains.pop(terrainIndex)

        #All remaining unassigned hexes are given the default terrain.
        for i in range (0, len(unassignedHexes)):
            allHexes[unassignedHexes[i][0]][3] = defaultTerrain

        #Update all hexes in resourceHexes using terrains from AllHexes
        for i in range (0, len(resourceHexes)):
            resourceHexes[i] = allHexes[resourceHexes[i][0]]

        #Begin placing resources
        for i in range (0, len(mapResources)):                             #for each requested resource line
            validHexes = []                                                             #clear the list of valid hexes.
            for j in range (0, len(resourceHexes)):                        #Find all hexes in resourceHexes with the correct terrain for this resource.
                if (resourceHexes[j][3] == mapResources[i][2]):
                    validHexes.append(resourceHexes[j])               #Add them to the list of valid hexes.
            for j in range (0, mapResources[i][1]):                       #Add all of the resources that have been requested
                resourceIndex = random.randint(0, len(validHexes)-1)    #Select a valid hex at random
                allHexes[validHexes[resourceIndex][0]][6] = mapResources[i][0]  #assign that resource to that hexes.
                for k in range (0, len(resourceHexes)):
                    if (resourceHexes[k][0] == validHexes[resourceIndex][0]):
                        resourceHexes.pop(k)                                    #Remove that hex from resourceHexes
                        break
                validHexes.pop(resourceIndex)                             #Remove that hex from valid hexes.

        # objects for some map resources
        map_resources = {}

        for hex in allHexes:
            # assign random tile image variant, if terrain still has -1 as current variant
            if hex[10] < 0:
                hex[10] = random.randint(0, len(terrain_data[hex[3]][2])-1)
            # create resource object for resource, if required
            if hex[6] in resource_classes:
                mr = resource_classes[hex[6]](map_def['uid'], tuple(hex[1]), hex[6])
                map_resources[tuple(mr.coords)] = mr

        # create and return map instance
        m = Map()
        # using copy.deepcopy so created map will not contain references to map_def or local vars
        m.uid = copy.deepcopy(map_def['uid'])
        m.name = copy.deepcopy(map_def['name'])
        m.hexes = copy.deepcopy(allHexes)
        m.resources = copy.deepcopy(map_resources)
        m.width = copy.deepcopy(mapWidth)
        m.height = copy.deepcopy(mapHeight)
        m.pos = copy.deepcopy(map_def['start pos'])
        m.previous_pos = copy.deepcopy(map_def['start pos'])
        return m


    def convert_json_to_mapdef(json_str):
        '''Converts exported Tiled map (json) into standard map definition'''
        mapdef_dict = json.loads(json_str)
        mapdef = {}
        mapdef['uid'] = mapdef_dict['properties']['uid']
        mapdef['name'] = mapdef_dict['properties']['name']
        mapdef['width'] = mapdef_dict['width']
        mapdef['height'] = mapdef_dict['height']
        # read list "start_pos" from string property
        mapdef['start_pos'] = json.loads(mapdef_dict['properties']['start_pos'])
        # read list of terrains from string representation of lists
        mapdef['terrains'] = ast.literal_eval(mapdef_dict['properties']['terrains'])
        mapdef['resources'] = ast.literal_eval(mapdef_dict['properties']['resources'])
        mapdef['portals'] = ast.literal_eval(mapdef_dict['properties']['portals'])
        # populate fixed hexes
        terrain_layer = [layer for layer in mapdef_dict['layers'] if layer['name'] == 'terrain'][0]
        resources_layer = [layer for layer in mapdef_dict['layers'] if layer['name'] == 'resources'][0]
        # correct id numbers for resources - subtract resources "firstgid" from hex ids in resources layer
        resources_firstgid = [ts for ts in mapdef_dict['tilesets'] if ts['source'].endswith('soc_resources.tsx')][0]['firstgid']
        for i in range(len(resources_layer['data'])):
            resources_layer['data'][i] = resources_layer['data'][i] - resources_firstgid
        mapdef['fixed'] = []
        for i in range(mapdef['height'] * mapdef['width']):
            # Tiled shifts tile id by +1, 0 is used for empty tile
            # currenty only terrain data defines fixed hexes (i.e. fixed resources on undefined terrain will be discarded)
            if terrain_layer['data'][i] > 0:
                # usable things here is id of hex, terrain id and resource id
                mapdef['fixed'].append([i, 0, 0, terrain_layer['data'][i] - 1, False, False, resources_layer['data'][i], False, 0, [], -1])
        # read default terrain from map properties (or set to 0 - plains)
        mapdef['default'] = mapdef_dict.get('default', 0)
        return mapdef


    def create_blank_map(width, height):
        '''Creates blank map with given width and height.
        All hex links should be set, terrain and resourses should not be set'''
        m = Map()
        m.width = width
        m.height = height
        #Variable used to track the ID number of our current hex.
        hexCount = 0
        #populate the list with hexes based on the size of the map, they start with default values.
        for i in range (0, height):
            for j in range (0, width):
                m.hexes.append( [ hexCount, [j, i], [-1, -1, -1, -1, -1, -1], -1, False, False, 0, False, 0, [], -1 ] )
                hexCount = hexCount + 1
        #Determine all hex links
        # TODO: use hex rings?
        for i in range (0, hexCount):
            #newPos contains the destinations for values h0-h6.  Initialize it as empty.
            #newPos[h value] [x or y]
            newPos = []

            #Add six copies of the current location to newPos
            for j in range (0,6):
                newPos.append (list(m.hexes[i][1]))       #Cloning a list, otherwise we're only creating a reference.

            #Calculate new positions of h0-h6
            #h0, up
            newPos[0][1] = newPos[0][1] - 1

            #h3, down
            newPos[3][1] = newPos[3][1] + 1

             #check if x is even or odd.
            if (m.hexes[i][1][0]%2 == 0):
                #h1, up right
                newPos[1][0] = newPos[1][0] + 1
                newPos[1][1] = newPos[1][1] - 1
                #h2, down right
                newPos[2][0] = newPos[2][0] + 1
                #h4, down left
                newPos[4][0] = newPos[4][0] - 1
                #h5, up left
                newPos[5][0] = newPos[5][0] - 1
                newPos[5][1] = newPos[5][1] - 1
            else:
                #h1, up right
                newPos[1][0] = newPos[1][0] + 1
                #h2, down right
                newPos[2][0] = newPos[2][0] + 1
                newPos[2][1] = newPos[2][1] + 1
                #h4, down left
                newPos[4][0] = newPos[4][0] - 1
                newPos[4][1] = newPos[4][1] + 1
                #h5, up left
                newPos[5][0] = newPos[5][0] - 1
            #Check if any of our new positions are outside the map.  If they are, set that link to -1.
            for j in range (0,6):
                if (newPos[j][0] < 0 or newPos[j][0] >= width or newPos[j][1] < 0 or newPos[j][1] >= height):
                    m.hexes[i][2][j] = -1
                else:
                    #Calculate index for the new position.
                    index = newPos[j][0]+newPos[j][1]*width
                    m.hexes[i][2][j] = m.hexes[index][0]
        return m


    def map_copy_properties(m, map_def):
        '''Copy non-hex properties from mapdef to map'''
        m.uid = map_def['uid']
        m.name = map_def['name']
        m.pos = map_def['start_pos']
        m.previous_pos = map_def['start_pos']
        for portal in map_def['portals']:
            m.portals[tuple(portal[:2])] = portal[2]


    def map_add_fixed_hexes(m, map_def):
        '''Adds/replaces fixed hexes on given map by given map_def.'''
        #Assign all fixed hexes
        fixedHexes = copy.deepcopy(map_def['fixed'])
        for i in range (0, len(fixedHexes)):
            if (fixedHexes[i][0] >= 0):         #Assign by index.
                index = fixedHexes[i][0]
            else:                               #Assign by position.
                index = fixedHexes[i][1][0]+fixedHexes[i][1][1]*m.width
            # overwrite non-geometry data of generated hex by data from fixed hex
            m.hexes[index][3:] = fixedHexes[i][3:]
        # set starting player pos
        m.pos = copy.deepcopy(map_def['start_pos'])
        return m


    def map_add_randomized_terrain(m, map_def):
        '''Adds randomized terrain as required in map_def;
        if some hexes still have undefined terrain in the end, sets it to "default" one.'''
        # create a copy of "terrains" from mapdef, it will be modified in the process
        mapTerrains = copy.deepcopy(map_def['terrains'])
        defaultTerrain = copy.deepcopy(map_def['default'])
        # find all unassigned terrain
        unassignedHexesIds = [hex[0] for hex in m.hexes if hex[3] == -1]
        # randomly choose terrain (from mapTerrains) to generate one cluster, generate it and remove that terrain from mapTerrains if this terrain fully generated
        while (len(unassignedHexesIds) > 0 and len(mapTerrains) > 0):
            connectedHexesIds = [] #Clear connected hexes Ids.
            #select a hex id at random from unassignedHexesIds and add it to connectedHexesIds
            connectedHexesIds.append(random.choice(unassignedHexesIds))
            #select a terrain at random we haven't finished assigning yet.
            terrainIndex = random.randint(0, len(mapTerrains)-1)
            #determine how large this cluster should be.
            clusterSize = random.randint( mapTerrains[terrainIndex][2] ,mapTerrains[terrainIndex][3] )

            # create cluster of choosen terrain
            #loop until we run out of connected hexes, this cluster is finished, or the terrain has been fully assigned.
            while (len(connectedHexesIds) > 0 and clusterSize > 0 and mapTerrains[terrainIndex][1] > 0):
                #select a hex id at random from connected hexes
                currentHexIndex = random.choice(connectedHexesIds)

                #assign that hex our terrain type in the map
                m.hexes[currentHexIndex][3] = mapTerrains[terrainIndex][0]
                #remove the currentHex from unassignedHexes and connectedHexes.
                unassignedHexesIds.remove(currentHexIndex)
                connectedHexesIds.remove(currentHexIndex)
                #decrement our cluster size and how many terrains we have to assign.
                clusterSize = clusterSize-1
                mapTerrains[terrainIndex][1] = mapTerrains[terrainIndex][1] - 1

                #add all hexes connected to current hex that are in unassignedHexes, but not already in connectedHexes to connectedHexes.
                for i in range (0, 6):
                    hexIndexToFind = m.hexes[currentHexIndex][2][i]   #note this index is with reference to allHexes.
                    if (hexIndexToFind != -1):                  #Don't search if the index is invalid.
                        # if hexIndexToFind is already in connectedHexesIds, skip it
                        if hexIndexToFind in connectedHexesIds:
                            break
                        #If we didn't find it in connectedHexes, then we search unassigned hexes.
                        elif hexIndexToFind in unassignedHexesIds:
                            connectedHexesIds.append(hexIndexToFind)

            #check if we've fully assigned the current terrain
            if (mapTerrains[terrainIndex][1] <= 0):
                #remove that terrain from our list of terrains to be assigned.
                mapTerrains.pop(terrainIndex)

        #All remaining unassigned hexes are given the default terrain.
        for i in unassignedHexesIds:
            m.hexes[i][3] = defaultTerrain


    def map_randomize_tile_images(m, map_def):
        '''Sets tile image to random choice from available for this tile'''
        for hex in m.hexes:
            # assign random tile image variant, if terrain still has -1 as current variant
            if hex[10] < 0:
                hex[10] = random.randint(0, len(terrain_data[hex[3]][2])-1)


    def map_add_random_resources(m, map_def):
        '''Tries to add required number of additional resources to map, using simple random placement.'''
        resources_to_place = copy.deepcopy(map_def['resources'])
        # allow only passable hexes under resources
        unassignedHexesIds = [hex[0] for hex in m.hexes if terrain_data[hex[3]][0] >= 0]
        # exclude hexes around already placed resources
        for hex in m.hexes:
            if hex[6] > 0:
                if hex[0] in unassignedHexesIds:
                    unassignedHexesIds.remove(hex[0])
                for hex_id_2 in hex[2]:
                    if hex_id_2 in unassignedHexesIds:
                        unassignedHexesIds.remove(hex_id_2)
        # randomly choose resources to place, place it and remove its hex and its neighbors from unassigned hex ids
        while (len(unassignedHexesIds) > 0 and len(resources_to_place) > 0):
            hex_id = random.choice(unassignedHexesIds)
            res_index = random.randint(0, len(resources_to_place) -1)
            m.hexes[hex_id][6] = resources_to_place[res_index][0]
            resources_to_place[res_index][1] -= 1
            # if all resources of this type are placed, remove this type from resources_to_place
            if resources_to_place[res_index][1] <= 0:
                resources_to_place.pop(res_index)
            # exclude this hex and hexes around already placed resources
            unassignedHexesIds.remove(hex_id)
            for hex_id_2 in m.hexes[hex_id][2]:
                if hex_id_2 in unassignedHexesIds:
                    unassignedHexesIds.remove(hex_id_2)


    def map_create_resource_objects(m):
        '''Creates objects to store state of resources'''
        for hex in m.hexes:
            # create resource object for resource, if required
            if hex[6] in resource_classes:
                mr = resource_classes[hex[6]](m, tuple(hex[1]), hex[6])
                m.resources[tuple(mr.coords)] = mr
