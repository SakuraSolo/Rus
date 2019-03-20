# rumors
init python:
    class Rumor(object):
        '''A rumor'''
        def __init__(self, name, sources, state='unavailable', kind='passive', priority=False):
            # unique name
            self.name = name
            # sources for the rumor: region, village, tavern
            self.sources = sources
            # state of the rumor: unavailable, available, discovered, read
            self.state = state
            # higher priority (for story rumors)
            self.priority = priority
            # type of the rumor: active, passive
            self.kind = kind
            # add self to all_rumors
            all_rumors[self.name] = self


    # create "all_rumors" at game start (similar to events)
    def __rumors_init():
        store.all_rumors = {}


    config.start_callbacks.append(__rumors_init)
