#Coded by Dark Master, Copyright belongs to Venus Noire.

#Map exploration functions.
#Input
#       map = list of hexes that make up the current map.
#       playerPos = player's starting position [x, y].
#       movementPoints = how many moves the player will be able to make.
#Output
#       newResources = list of all newly gained resources.
#       event flags, map functions will tell the main game what flags need to be changed while being run.
init python:
    #Random functionality is not included in Python's base.
    import random

    # maybe less effective then filtering visible hexes using hex distance, but seems fast enough for now
    # but ineffective if view_distance > 3-4
    def set_neighbours_visible(_id, dist=1):
        '''Sets neightbours of hex "_id" visible (within given view distance)'''
        for i in range (0, 6):
            # loop through six neighbours of given hex
            curHex = world.cur_map.hexes[_id][2][i]
            # if this neighbour hex is on map, set it visible
            if (curHex >= 0):
                cur_map.hexes[curHex][4] = True
                mark_resource_seen(world.cur_map._coords_from_id(curHex))
                # recursively set hexes visible if view distance > 1
                if dist > 1:
                    set_neighbours_visible(curHex, dist-1)


    def mark_resource_visited(coords):
        '''If there is a map resource object at given coords (on current map), mark it visited'''
        if tuple(coords) in world.cur_map.resources:
            world.cur_map.resources[tuple(coords)].visited = True


    def mark_resource_seen(coords):
        '''If there is a map resource object at given coords (on current map), mark it seen by player'''
        if tuple(coords) in world.cur_map.resources:
            world.cur_map.resources[tuple(coords)].seen = True


label map_exploration(uid, coords=None):
    # run NPC slot events
    if systems.npc_jobs:
        call run_events('npc_events') from _call_run_events_1
    $ renpy.block_rollback()
    play music 'music/village loop.ogg'
    # explore map with given uid
    $ world.enter(uid)
    $ cur_map = world.cur_map


    $ done = False                   #Are we done exploring?

    $ expModifier = 0.5         #Already explored spaces have their movement costs multiplied by this value.

    $ eventChance = 10          #We have a one in this variable chance of triggering an event each time we enter an unexplored empty space.

    # if specific coordinates are supplied, move player to that place
    if coords:
        $ world.cur_map.pos = coords

    #Temp, set the current space as explored.
    # TODO: Temporary disabled, to workaround orciad camp exploration if "Explore" is used from portal room when player was in orciad camp previous turn.
    # $ world.cur_map.hexes[world.cur_map.pos_id][5] = True
    # mark current resource as visited (can potentially cause a bug because event is not triggered, but probably it will be always a portal)
    $ mark_resource_visited(world.cur_map.pos)

    #Event trigger variable
    $eventTriggered = False

    #Main exploration loop
    while (done == False):
        # block saving while player traveling maps
        $ block_saving()
        $ released_block_rollback()
        # resets 'prevent exploration' and 'push back' on each move
        $ world._prevent_exploration = False
        $ world._push_back = False
        #Mark the current space and all surrounding spaces as visible.
        $ world.cur_map.hexes[world.cur_map.pos_id][4] = True

        $ set_neighbours_visible(world.cur_map.pos_id, avatar.view_distance)

        #Keep refreshing the screen until we're done exploring.
        scene black
        call screen hex_map

        #Check if we were told we were done.
        if (_return == -1):
            $ done = True
        # forced random event triggered by devtools
        elif _return == 'force_random_event':
            call run_events('map_expl') from map_exploration_random_event
        else:
            #Otherwise, check for player movement.

            #Determine the hex ID of the hex we are moving to.
            # (get newHexID from connected hexes by direction number returned from hex_map)
            $ newHexID = cur_map.hexes[world.cur_map.pos_id][2][_return]

            #Make sure the new hex is on the map.
            if (newHexID >= 0):
                #Check the terrain we're moving to's movement cost.  If it is -1, terrain is impassible and do nothing.
                $ movementCost = terrain_data[cur_map.hexes[newHexID][3]][0]
                if (movementCost >= 0):
                    # move avatar to new hex
                    $ world.cur_map.pos_id = newHexID
                    # if there is a resource object in target hex, mark it as visited
                    $ mark_resource_visited(world.cur_map.pos)

                    #If the space is already explored, apply the explored modifier.
                    if (cur_map.hexes[newHexID][5] == True):
                        $ movementCost = movementCost * expModifier
                    #Since we moved, deduct the cost of movement
                    $ avatar.mp = avatar.mp - movementCost

                    #If there are event flags, we always trigger a specific event.
                    if (len(cur_map.hexes[world.cur_map.pos_id][9]) > 0):
                        call eventFlagTrigger (cur_map.hexes[world.cur_map.pos_id]) from _call_eventFlagTrigger
                    #Otherwise we check for resources and random events.
                    else:
                        #Only unexplored hexes can trigger events without flags.
                        if (cur_map.hexes[world.cur_map.pos_id][5] == False):
                            #Does this unexplored space have a non-road resource on it?
                            if (cur_map.hexes[world.cur_map.pos_id][6] > 1):
                                call eventResourceTrigger (cur_map.hexes[world.cur_map.pos_id]) from _call_eventResourceTrigger
                            else:
                                #Do a random check to trigger an event.
                                if (random.randint (0, eventChance) == 0):
                                    call eventRandomTrigger (cur_map.hexes[world.cur_map.pos_id]) from _call_eventRandomTrigger
                    #Set the new space as explored, if event did not prevented that
                    if not world._prevent_exploration:
                        $ cur_map.hexes[world.cur_map.pos_id][5] = True
                    if world._push_back:
                        $ cur_map.pos = cur_map.previous_pos
                    else:
                        $ cur_map.previous_pos = cur_map.pos

        if (avatar.mp <= 0):
            $ done = True

    $ world.exit()
    return
