# state of raid
init python:
    class RaidState(object):
        '''State of raid'''
        def __init__(self):
            self.in_raid = False
            self._troops = {}
            self._equipment = {}
            # reset state
            self.reset()

        @property
        def available_troops(self):
            '''Returns dict of all troops types and their quantity in the castle'''
            avt = {}
            avt['orc'] = castle.buildings['barracks'].troops
            avt['cubi'] = castle.buildings['sanctum'].troops
            avt['drider'] = castle.buildings['pit'].driders
            return avt

        @property
        def available_equipment(self):
            '''Returns dict of all troops types and their eqipment in the castle'''
            ave = {}
            ave['orc'] = castle.buildings['barracks'].equipment
            return ave

        @property
        def troops(self):
            '''Troops in raid'''
            return self._troops

        @property
        def equipment(self):
            '''Equipment in raid'''
            return self._equipment

        def change_troops(self, troop_type, val):
            '''Changes number of troop_type in current raid'''
            self._troops[troop_type] += val
            self._troops[troop_type] = min(max(0, self._troops[troop_type]), self.available_troops[troop_type])
            # auto-equip orcs
            self._equipment['orc'] = min(max(0, self._troops['orc']), self.available_equipment['orc'])

        def reset(self):
            '''Inits/resets state of raid'''
            self.in_raid = False
            for troop_type in all_troops:
                self._troops[troop_type] = 0
            # not all troops use equipment
            # TODO: maybe populate equipment based on all_troops definitions
            self._equipment['orc'] = 0

        def finish(self):
            '''Deducts raid troops from castle and resets raid'''
            self.in_raid = False
            castle.buildings['barracks'].troops -= self.troops['orc']
            castle.buildings['barracks'].equipment -= self.equipment['orc']
            castle.buildings['pit']._driders -= self.troops['drider']
            castle.buildings['sanctum'].troops -= self.troops['cubi']
            self.reset()


        @property
        def mp(self):
            '''Military power of whole raid'''
            mp = 0
            # calculate MP for normal soldiers
            for troop_type in ('orc', 'cubi'):
                mp += self.troops[troop_type] * all_troops[troop_type]['strength']
            # apply cubi bonus to normal soldiers
            mp *= 1 + self.troops['cubi'] * 0.05
            # add equipment strength for orcs
            mp += self.equipment['orc'] * all_troops['orc']['equip_strength']
            mp += self.troops['drider'] * all_troops['drider']['strength']
            return mp


    def __raid_state_init():
        store.raid_state = RaidState()

    config.start_callbacks.append(__raid_state_init)

