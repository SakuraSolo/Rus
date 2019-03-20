init python:

    class Flags(dict):
        '''Stores flags'''

        def __getitem__(self, key):
            if key not in self:
                return 0
            else:
                return dict.__getitem__(self, key)


    class Actor(object):
        '''Actor (npc)'''

        def __init__(self, uid, name):
            self.uid = uid
            self.name = name
            self.flags = Flags()
            self._favors = 0
            self._total_favors = 0
            self.inf_corruption = False
            # register self in all actors
            all_actors[self.uid] = self

        @property
        def favors(self):
            return self._favors

        @favors.setter
        def favors(self, val):
            self._total_favors += max(0, val - self._favors)
            self._favors = max(0, val)

        @property
        def total_favors(self):
            return self._total_favors


    # actor stats
    actor_stats = ('corruption', 'relation')


    # current difference with avatar stat is that this has not 'base' stat, only 'final'
    def create_actor_stat(cls, name, init_val=0):
        '''Create standard stat for the actor (limited in range 0-100)'''

        def getter(self):
            return getattr(self, '_' + name)

        def setter(self, val):
            if val < 0:
                val = 0
            elif val > 100:
                val = 100
            setattr(self, '_' + name, val)

        setattr(cls, '_' + name, init_val)
        setattr(cls, name, property(getter, setter))


    # create stats for Actor class
    for stat in actor_stats:
        create_actor_stat(Actor, stat)


    # create "all_actors" at game start (similar to events)
    def __actors_init():
        store.all_actors = {}


    config.start_callbacks.append(__actors_init)
