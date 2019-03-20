# Room with portals
label portal_room:
    call screen portal_screen
    return


init python:

    class ContinueExploration(Action):
        '''Starts exproration at given map and current position'''
        def __init__(self, map_uid):
            self.map_uid = map_uid

        def __call__(self):
            # pop_call before renpy.call so after map exloration game will return to main loop instead of castle map
            renpy.pop_call()
            renpy.call('map_exploration', self.map_uid)


    class JumpToPortal(Action):
        '''Starts exploration at given map and portal coordinates'''
        def __init__(self, map_uid, portal_name):
            self.map_uid = map_uid
            self.pname = portal_name

        def get_sensitive(self):
            '''Checks if portal is accessible to player'''
            portal_coords = None
            for (coords, pname) in world.maps[self.map_uid].portals.items():
                if pname == self.pname:
                    portal_coords = coords
            if portal_coords:
                # this portal is available for jumping at if player have visited it
                if world.maps[self.map_uid].resources[tuple(portal_coords)].visited:
                    return True

        def __call__(self):
            # pop_call before renpy.call so after map exloration game will return to main loop instead of castle map
            portal_coords = None
            for (coords, pname) in world.maps[self.map_uid].portals.items():
                if pname == self.pname:
                    portal_coords = coords
            if portal_coords:
                renpy.pop_call()
                renpy.call('map_exploration', self.map_uid, portal_coords)
