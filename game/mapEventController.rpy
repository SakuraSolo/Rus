#Temp file to hold dummy event functions
#Return values are a list of two elements.
#       The first is either True or False, and tells the game if the player successfully moved into the space and explored it.
#       The second element is a number value that will be added to the player's movement points after the event.

init python:
    # {"resource id": ("name", "description", "military power", "income"), ...}
    human_villages_defs = {
        3: ('village', 'small quaint place', 50, 10),
        4: ('town', 'hub of local activity', 100, 20),
        5: ('small city', 'bustling center of trade', 150, 30),
    }
    # {"resource id": ("name", "workforce needed", "production"), ...}
    mines_defs = {
        6: ('small mine', 5, 2),
        7: ('important mine', 10, 4),
        8: ('mining network', 15, 6),
    }
    # cost of one miner to hire
    miner_cost = 6


label eventFlagTrigger (eventHex):
    #Dummy event, just return success.
    return [True, 0]


label eventResourceTrigger (eventHex):
    $ released_block_rollback()
    #Private winery
    #When claimed, gives a one time boost to morale.
    if eventHex[6] == 16:
        #Intro blurb
        #Show countryside background.
        "During his explorations of the plains of Rosaria, Rowan stumbles on a small private winery and the nearby vineyard. The wine produced in places like these is the local specialty when it comes to alcohol, you won't find a better wine in the Six Realms."
        "These yards usually have stores of their produce from each year, ready to be sold to collectors or those seeking refreshments for special occasions. While the yard itself would be useless to Bloodmeen, the stockpile could be distributed to the soldiers and seriously boost their current morale."
        "Of course, you can only collect the stockpile once and there will be no saving it with what constitutes the twin's armies."
        menu:
            #Choice: Raid the winery now.
            'Raid the winery now':
                #Trigger a winery raid event.
                $ released_fix_rollback()
                call run_events('private_winery_raid') from _call_run_events_10
                return
            #Choice: Leave it for later.
            'Leave it for later':
                $ released_fix_rollback()
                #end the event now, move Rowan back, do not mark the resource as explored.
                # TODO move Rowan back
                $ prevent_tile_exploration()
                return
    else:
        # call events for resource ID
        call run_events('map_res_{}'.format(eventHex[6])) from _event_resource_trigger
    return [True, 0]


label eventRandomTrigger (eventHex):
    # call random map events (exploration)
    call run_events('map_expl') from _event_random_trigger
    return [True, 0]
