# buildings for the castle

init python:

    class Building(object):
        '''Base class for castle buildings'''
        def __init__(self, uid):
            self.uid = uid
            self.name = all_buildings[uid]['name']
            self.lvl = 0
            # max level of this building, changing through game
            self.max_lvl = 0
            self.income = 0
            self.maintenance = 0
            self.morale = 0
            self.research = 0
            self._capacity = 0
            self.recruitment = 0
            self.description = all_buildings[uid]['name'] + ' description'

        @property
        def up_cost(self):
            '''Returns the price of new building or next upgrade'''
            if self.lvl == 0:
                return all_buildings[self.uid]['cost']
            else:
                return all_buildings[self.uid]['up_cost']

        def build(self):
            '''Builds new upgrade level for the building'''
            if self.lvl == 0:
                self.income += all_buildings[self.uid]['income']
                self.maintenance += all_buildings[self.uid]['maintenance']
                self.morale += all_buildings[self.uid]['morale']
                self.research += all_buildings[self.uid]['research']
                self._capacity += all_buildings[self.uid]['capacity']
                self.recruitment += all_buildings[self.uid]['recruitment']
            else:
                self.income += all_buildings[self.uid]['up_income']
                self.maintenance += all_buildings[self.uid]['up_maintenance']
                self.morale += all_buildings[self.uid]['up_morale']
                self.research += all_buildings[self.uid]['up_research']
                self._capacity += all_buildings[self.uid]['up_capacity']
                self.recruitment += all_buildings[self.uid]['up_recruitment']
            self.lvl += 1

        def weekly(self):
            '''Called each week to update state'''
            pass

        def can_be_built(self):
            '''Returns True if all conditions for upgrading to next level are met'''
            # can be built if there is enough money and if this upgrade is not already scheduled and if current level is lesser than max level
            return (castle.buildings[self.uid].up_cost <= castle.treasury) and (len(castle.scheduled_upgrades) == 0) and castle.buildings[self.uid].lvl < castle.buildings[self.uid].max_lvl and castle.buildings[self.uid].req_met()

        def can_be_shown(self):
            '''Returns True if building can be shown to player'''
            return castle.buildings[self.uid].lvl < castle.buildings[self.uid].max_lvl and castle.buildings[self.uid].req_met()

        def req_met(self):
            '''Returns True if building-specific conditions are met'''
            return True

        @property
        def capacity(self):
            return self._capacity

        @capacity.setter
        def capacity(self, val):
            self._capacity = val


    class Barracks(Building):
        '''Generic barracks'''
        def __init__(self, uid):
            super(Barracks, self).__init__(uid)
            self._troops = 0
            self.equipment = 0
            self.troop_type = all_buildings[self.uid]['troop_type']

        def weekly(self):
            self.troops += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
            if self.troops >= self.capacity:
                self.troops = self.capacity

        @property
        def troops(self):
            return self._troops

        @troops.setter
        def troops(self, val):
            self._troops = min(val, self.capacity)
            self._troops = max(self._troops, 0)


    class MagicBuilding(Building):
        '''Magic building that requires free library capacity to be built'''
        def __init__(self, uid):
            super(MagicBuilding, self).__init__(uid)

        def req_met(self):
            # TODO: maybe move used_library_capacity to Library class
            used_library_capacity = 0
            for bld in castle.buildings.values():
                if isinstance(bld, MagicBuilding):
                    if bld.lvl >= 1 or bld.uid in castle.scheduled_upgrades:
                        used_library_capacity += 1
            return castle.buildings['library'].capacity > used_library_capacity


    class DarkSanctum(Barracks, MagicBuilding):
        def __init__(self, uid):
            super(DarkSanctum, self).__init__(uid)
            # remove equipment (cubis don't use it)
            del self.equipment


    class Forge(Building):
        '''Converts some iron to equipment'''
        def __init__(self, uid):
            super(Forge, self).__init__(uid)

        def weekly(self):
            if castle._iron >= self.capacity:
                castle._iron -= self.capacity
                castle._equipment += self.capacity
            else:
                castle._equipment += castle._iron
                castle._iron = 0


    class Dungeon(Building):
        '''Dungeon (contains prisoners)'''
        def __init__(self, uid):
            super(Dungeon, self).__init__(uid)
            self._prisoners = 0
            # init prisoners status
            # records current status of operations with prisoners (current, week limit)
            self.prisoners_status = {
                'slave': [0, 10],
                'ransom': [0, 3],
                'gladiator': [0, 3],
                'test': [0, 5]}
            # state of "auto-sell" for prisoners
            self.prisoners_auto = {
                'slave': False,
                'ransom': False,
                'gladiator': False,
                'test': False}

        def weekly(self):
            # auto sell prisoners
            while self.prisoners > 0:
                if castle.morale < 20 and (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                elif (self.prisoners_status['ransom'][0] < self.prisoners_status['ransom'][1]) and self.prisoners_auto['ransom']:
                    castle.treasury += 10
                    self.prisoners -= 1
                    self.prisoners_status['ransom'][0] += 1
                elif castle.morale >= 20 and castle.morale < 60 and (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                elif (self.prisoners_status['test'][0] < self.prisoners_status['test'][1]) and self.prisoners_auto['test']:
                    castle.rp += 2
                    self.prisoners -= 1
                    self.prisoners_status['test'][0] += 1
                elif (self.prisoners_status['slave'][0] < self.prisoners_status['slave'][1]) and self.prisoners_auto['slave']:
                    castle.treasury += 5
                    self.prisoners -= 1
                    self.prisoners_status['slave'][0] += 1
                elif (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                else:
                    # if there is no valid option for auto sell, end auto selling
                    break
            # reset current status for prisoners limits
            self.prisoners_status['slave'][0] = 0
            self.prisoners_status['ransom'][0] = 0
            self.prisoners_status['gladiator'][0] = 0
            self.prisoners_status['test'][0] = 0

        @property
        def prisoners(self):
            return self._prisoners

        @prisoners.setter
        def prisoners(self, val):
            self._prisoners = min(val, self.capacity)
            self._prisoners = max(self._prisoners, 0)


    class Brothel(Building):
        '''Brothel (contains spies)'''
        def __init__(self, uid):
            super(Brothel, self).__init__(uid)
            self.spies = []
            self.available_spies = []

        def weekly(self):
            # delete unrecruited spies
            for uid in self.available_spies:
                del_object(uid)
            self.available_spies = []
            # create new spies to recruit from
            for sex in ['m', 'f']:
                for i in range(self.lvl):
                    self.available_spies.append(Spy(sex).uid)

        def build(self):
            super(Brothel, self).build()
            self.weekly()
            print self.available_spies

    class BreedingPit(Building):
        '''Breeding pit (contains various monsters)'''
        def __init__(self, uid):
            super(BreedingPit, self).__init__(uid)
            self._driders = 0
            self.drider_recruitment = 0
            self._capacity = 0
            # self.bonus_capacity = 0

        @property
        def capacity(self):
            return self._capacity + self.bonus_capacity

        @capacity.setter
        def capacity(self, val):
            self._capacity = val - self.bonus_capacity

        @property
        def bonus_capacity(self):
            for ac in all_actors.values():
                if hasattr(ac, 'job_state'):
                    if ac.job_state.job == 'breeding':
                        return 8
            return 0

        @property
        def maintenance_discount(self):
            for ac in all_actors.values():
                if hasattr(ac, 'job_state'):
                    if ac.job_state.job == 'breeding':
                        return int(10 * all_actors[ac.uid].job_state.efficiency())
            return 0

        @property
        def free_space(self):
            # free space = capacity - number_of_monsters1 * size1 - ...
            return self.capacity - self.monsters

        @property
        def driders(self):
            # return number of 'whole' driders
            return int(self._driders)

        @property
        def monsters(self):
            '''Returns total number of "whole" monsters, disregarding their size'''
            # TODO: multiply by size for large monsters
            return self.driders

        def weekly(self):
            self._driders += self.drider_recruitment


    # all buildings for the castle
    all_buildings = {
        'hall': {'name': 'Castle Hall',
            'cost': 0, 'up_cost': 225, 'income': 50, 'up_income': 0, 'maintenance': 10, 'up_maintenance': 10, 'morale': 23, 'up_morale': 6,
            'research': 0, 'up_research': 0, 'capacity': 1, 'up_capacity': 1, 'recruitment': 0, 'up_recruitment': 0},
        'library': {'name': 'Library',
            'cost': 0, 'up_cost': 300, 'income': 0, 'up_income': 0, 'maintenance': 5, 'up_maintenance': 5, 'morale': 0, 'up_morale': 0,
            'research': 10, 'up_research': 2, 'capacity': 1, 'up_capacity': 1, 'recruitment': 0, 'up_recruitment': 0},
        'quarters': {'name': 'Living Quarters',
            'cost': 0, 'up_cost': 600, 'income': 0, 'up_income': 0, 'maintenance': 5, 'up_maintenance': 5, 'morale': 0, 'up_morale': 10,
            'research': 0, 'up_research': 0, 'capacity': 0, 'up_capacity': 0, 'recruitment': 0, 'up_recruitment': 0},
        'tavern': {'name': 'Tavern',
            'cost': 150, 'up_cost': 300, 'income': 40, 'up_income': 40, 'maintenance': 10, 'up_maintenance': 10, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 3, 'up_capacity': 2, 'recruitment': 0, 'up_recruitment': 0},
        'caravan': {'name': 'Caravan',
            'cost': 0, 'up_cost': 300, 'income': 0, 'up_income': 0, 'maintenance': 0, 'up_maintenance': 0, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 0, 'up_capacity': 0, 'recruitment': 0, 'up_recruitment': 0},
        'workshop': {'name': 'Workshop',
            'cost': 0, 'up_cost': 0, 'income': 0, 'up_income': 0, 'maintenance': 0, 'up_maintenance': 0, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 0, 'up_capacity': 0, 'recruitment': 0, 'up_recruitment': 0},
        'dungeon': {'name': 'Dungeon',
            'cost': 0, 'up_cost': 225, 'income': 0, 'up_income': 0, 'maintenance': 0, 'up_maintenance': 0, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 10, 'up_capacity': 10, 'recruitment': 0, 'up_recruitment': 0,
            'bld_class': Dungeon},
        'barracks': {'name': 'Orc Barracks',
            'cost': 0, 'up_cost': 300, 'income': 0, 'up_income': 0, 'maintenance': 0, 'up_maintenance': 0, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 30, 'up_capacity': 30, 'recruitment': 2, 'up_recruitment': 2,
            'bld_class': Barracks, 'troop_type': 'orc'},
        'forge': {'name': 'Forge',
            'cost': 150, 'up_cost': 600, 'income': 0, 'up_income': 0, 'maintenance': 5, 'up_maintenance': 10, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 5, 'up_capacity': 10, 'recruitment': 0, 'up_recruitment': 0,
            'bld_class': Forge},
        'kennel': {'name': 'Warg kennel',
            'cost': 300, 'up_cost': 300, 'income': 0, 'up_income': 0, 'maintenance': 10, 'up_maintenance': 5, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 10, 'up_capacity': 5, 'recruitment': 0, 'up_recruitment': 0},
        'pit': {'name': 'Breeding pit',
            'cost': 300, 'up_cost': 600, 'income': 0, 'up_income': 0, 'maintenance': 0, 'up_maintenance': 0, 'morale': 0, 'up_morale': 0,
            'research': 2, 'up_research': 1, 'capacity': 8, 'up_capacity': 8, 'recruitment': 0, 'up_recruitment': 0,
            'bld_class': BreedingPit},
        'sanctum': {'name': 'Dark sanctum',
            'cost': 150, 'up_cost': 300, 'income': 0, 'up_income': 0, 'maintenance': 0, 'up_maintenance': 0, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 5, 'up_capacity': 5, 'recruitment': 1, 'up_recruitment': 0,
            'bld_class': DarkSanctum, 'troop_type': 'cubi'},
        'brothel': {'name': 'Brothel',
            'cost': 300, 'up_cost': 450, 'income': 0, 'up_income': 0, 'maintenance': 10, 'up_maintenance': 5, 'morale': 0, 'up_morale': 0,
            'research': 0, 'up_research': 0, 'capacity': 2, 'up_capacity': 1, 'recruitment': 0, 'up_recruitment': 0,
            'bld_class': Brothel},
        'arena': {'name': 'Arena',
            'cost': 225, 'up_cost': 450, 'income': 0, 'up_income': 0, 'maintenance': 7.5, 'up_maintenance': 7.5, 'morale': 23, 'up_morale': 23,
            'research': 0, 'up_research': 0, 'capacity': 0, 'up_capacity': 0, 'recruitment': 0, 'up_recruitment': 0},
        'summoning': {'name': 'Summoning Chambers',
            'cost': 300, 'up_cost': 600, 'income': 0, 'up_income': 0, 'maintenance': 10, 'up_maintenance': 10, 'morale': 0, 'up_morale': 0,
            'research': 2, 'up_research': 1, 'capacity': 0, 'up_capacity': 0, 'recruitment': 0, 'up_recruitment': 0,
            'bld_class': MagicBuilding},
    }
