# castle and settlement

init python:
    class Castle(object):
        '''Castle and settlement stats'''

        def __init__(self):
            self.treasury = 0
            # military capacity
            self.military = 0
            # tech rate (research points generated at start of a week)
            self.tech = 0
            # overflow research points at start of new week, hidden
            self.rp = 0
            self._morale = 0
            # last week stats, for calculating changes (including changes from events)
            self.last_week_treasury = 0
            self.last_week_morale = 0
            # castle buildings {uid: building, ...}
            self.buildings = {}
            self._load_buildings()
            # weekly reduction of maintenance of surface buildings
            self.surface_maintenance_reduction = 0
            # all researches {uid: research, ...}
            self.researches = {}
            self._current_research = None
            self.completed_researches = []
            self._load_researches()
            # scheduled upgrades (to be built on new week)
            self.scheduled_upgrades = []
            # list of completed upgrades, for events
            self.completed_upgrades = []
            # world resources, should probably go to World class
            self.villages = 0
            self.villages_income = 0
            self.mines = 0
            self.iron_per_week = 0
            self.recruitment_bonuses = {}
            self.research_bonus = 0
            # temp vars (used in end_week)
            self._iron = 0
            self._equipment = 0
            # visitable locations and buildings
            self._visitable = set(visitable_locations)
            # npc that participate in jobs
            self.npc_with_jobs = []

        def _load_buildings(self):
            '''Add all buildings to the castle at the beginning'''
            for uid in all_buildings:
                if 'bld_class' in all_buildings[uid]:
                    self.buildings[uid] = all_buildings[uid]['bld_class'](uid)
                else:
                    self.buildings[uid] = Building(uid)

        def _load_researches(self):
            '''Add all researches to the castle at the beginning'''
            for rs_cls in all_researches:
                self.researches[rs_cls.uid] = rs_cls()

        def end_week(self):
            '''Calculate state for next week'''
            # record current treasury and morale as "last week" numbers
            self.last_week_treasury = self.treasury
            self.last_week_morale = self.morale
            # clear completed_upgrades and completed_researches from previous week
            self.completed_upgrades = []
            # self.completed_researches = []
            # updates resources from various sources
            self._add_world_resources()
            self._update_buildings()
            self._distribute_equipment()
            self._update_troops()
            # build scheduled upgrades
            while self.scheduled_upgrades:
                uid = self.scheduled_upgrades.pop()
                self.completed_upgrades.append(uid + str(self.buildings[uid].lvl + 1))
                self.buildings[uid].build()
            # spend resources
            self._spend_research_points()
            self._sell_unused_resources()
            # pay salary to Rowan from treasury
            avatar.gold += min(5, castle.treasury)
            castle.treasury -= min(5, castle.treasury)
            self.surface_maintenance_reduction = 0

        def _add_world_resources(self):
            '''Gather weekly surplus of world resources to the castle'''
            self.treasury += self.villages_income
            self._iron += self.iron_per_week

        def _update_buildings(self):
            '''Weekly update of buildings. Adds their resources to the castle.'''
            # call weekly actions for upgrades that have them
            for bld in self.buildings.values():
                bld.weekly()
            # update money, morale and research points from buildings
            self.tech = 0
            for bld in self.buildings.values():
                self.morale += bld.morale
                self.treasury += bld.income
                if hasattr(bld, 'maintenance_discount'):
                    self.treasury -= int(bld.maintenance * (100 - self.surface_maintenance_reduction - bld.maintenance_discount) / 10.0) / 10.0
                else:
                    self.treasury -= int(bld.maintenance * (100 - self.surface_maintenance_reduction) / 10.0) / 10.0
                self.tech += bld.research
            # add research bonus from world resources
            self.tech += self.research_bonus

        def _update_troops(self):
            '''Weekly update of troops. Adds/removes their resources.'''
            for bld in self.buildings.values():
                if hasattr(bld, 'troops'):
                    # update morale and money
                    self.morale -= bld.troops * all_troops[bld.troop_type]['morale_cost']
                    self.treasury -= bld.troops * all_troops[bld.troop_type]['maintenance']
                    self.tech += bld.troops * all_troops[bld.troop_type]['research']
            self._update_military_power()

        def _update_military_power(self):
            '''Updates military power of the castle'''
            self.military = self.military_power()

        def military_power(self):
            '''Returns military power of current castle troops and effects'''
            mp = 0
            for bld in self.buildings.values():
                # TODO: maybe it makes sense to simply add 'troops' to base class
                # gather MP from barracks-like buildings
                if hasattr(bld, 'troops'):
                    mp += bld.troops * all_troops[bld.troop_type]['strength']
            # add cubis bonus to all regular soldiers
            mp *= 1 + 0.05 * self.buildings['sanctum'].troops
            # add equipment strength
            for bld in self.buildings.values():
                if hasattr(bld, 'equipment') and hasattr(bld, 'troops'):
                    mp += min(bld.equipment, bld.troops) * all_troops[bld.troop_type]['equip_strength']
            # add driders
            mp += self.buildings['pit'].driders * all_troops['drider']['strength']
            return mp

        def _distribute_equipment(self):
            '''Distribute equipment between various barracks (with priority)'''
            for uid in ('barracks',):
                unequipped = self.buildings[uid].troops - self.buildings[uid].equipment
                if unequipped > 0:
                    self.buildings[uid].equipment += min(self._equipment, unequipped)
                    self._equipment -= min(self._equipment, unequipped)

        def _spend_research_points(self):
            '''Spends research points accumulated this week.'''
            # store research points in self.rp (to spend later)
            self.rp += self.tech
            # spend rp
            if self.current_research:
                rp_to_complete = self.current_research.cost - self.current_research.rp_spent
                if self.rp < rp_to_complete:
                    self.current_research.rp_spent += self.rp
                    self.rp = 0
                else:
                    self.current_research.rp_spent += rp_to_complete
                    # TODO: transfer unspent rp to next research
                    self.rp -= rp_to_complete
                    self.current_research.on_complete()
                    self.current_research.completed = True
                    self.completed_researches.append(self.current_research.uid)
                    self._current_research = None

        def _sell_unused_resources(self):
            '''Sells unused resources at very end of weekly update'''
            # sell all unused iron
            self.treasury += self._iron
            self._iron = 0
            # sell all unused equipment
            self.treasury += self._equipment * 5
            self._equipment = 0
            # research points should not go to next week
            self.rp = 0

        def set_research(self, uid):
            '''Sets current research'''
            self._current_research = uid

        def visitable(self, uid):
            '''Returns True if location is visitable'''
            if uid in self._visitable:
                # if location is building, ensure that it is built at least to lvl 1
                if uid in self.buildings:
                    if self.buildings[uid].lvl >= 1:
                        return True
                    else:
                        return False
                else:
                    # allow visiting of non-buildings (like stairs)
                    return True
                return True

        @property
        def current_research(self):
            '''Returns current research'''
            if self._current_research:
                return self.researches[self._current_research]

        # TODO: maybe this should be part of gui, not model
        @property
        def morale_text(self):
            '''Morale as text'''
            if self.morale <= 20:
                return 'Terrible'
            elif self.morale <= 40:
                return 'Poor'
            elif self.morale <= 60:
                return 'Normal'
            elif self.morale <= 80:
                return 'Good'
            else:
                return 'Great'

        @property
        def morale(self):
            '''Numeric morale value'''
            return self._morale

        @morale.setter
        def morale(self, val):
            '''Sets morale in allowed range'''
            if val < 0:
                val = 0
            if val > 100:
                val = 100
            self._morale = val

        @property
        def spies(self):
            '''Quick access to Brothel\'s spies'''
            return self.buildings['brothel'].spies


    # buildings that should be built at start of new game
    starting_buildings = ('hall', 'library', 'quarters', 'dungeon', 'barracks', 'caravan', 'workshop')

    # visitable locations - they have related locations (labels) in locations folder; this can be changed via castle.visitable later
    visitable_locations = ('rowans_chambers', 'stairs_up', 'stairs_down', 'mess_hall', 'portal_room', 'liurial_room', 'throne_room', 'library', 'quarters', 'tavern', 'caravan', 'workshop', 'dungeon', 'barracks', 'forge', 'sanctum', 'pit', 'brothel', 'arena', 'summoning')


    # control flags for various systems of the game
    class Systems(object):
        def __init__(self):
            # access to research system/controls (in library)
            self.research = False
            # access to building/upgrading
            self.building = False
            # access to NPC jobs
            self.npc_jobs = False
            # access to castle as a whole
            self.castle = False
