# castle (training version)
# used for training coffers and schedule

init python:
    class CastleSt(object):
        '''Castle: training coffers and schedule for NPC'''

        def __init__(self, rooms=None):
            self.training_coffers = 0
            # rooms access will be set at game start
            self.rooms_access = {}
            # if starting rooms are given, create castle rooms
            if rooms:
                for room, access in rooms.items():
                    self.rooms_access[room] = access
            self.upgrades = Upgrades(self)
            # jobs for trainable NPC
            self.jobs = Jobs()
            # guests (trainable NPCs) ({actor.uid: actor, ...})
            self.guests = {}
            # schedule for trainable NPC
            self.schedule = {}

        def end_week(self):
            '''Calculate state for next week'''
            # update guests states
            for actor in self.guests.values():
                actor.weekly()

        def add_guest(self, actor):
            self.guests[actor.uid] = actor
