# upgrades for the castle
init python:
    # TODO: effects from buildings
    # all upgrades, format: {'uid': ('Name', RP price, gold price, 'uid of room to open or None', on_build action, weekly action, 'description'), ...}
    all_upgrades = {
        'tavern': ('Tavern', 25, 500, 'tavern', None, None, 'Opens location. Small increases to morale and economy.'),
        'brothel': ('Brothel', 25, 500, 'brothel', None, None,  'Opens location. Small increases to morale and economy.'),
        'reliquary': ('Reliquary', 15, 300, 'reliquary', None, None,  'Opens location with magic item NPC seller.'),
        'breeding_pits': ('Breeding Pits', 15, 300, 'breeding_pits', None, None,  'Opens location. Small increase to population.'),
        'forge': ('Forge', 10, 200, None, None, None,  'Allows forging of weapons in barracks, pre-requisite for making armour.'),
        'tannery': ('Tannery', 10, 200, None, None, None,  'Pre-requisite for making armour.'),
        'alchemy_lab': ('Alchemy Lab', 25, 500, None, None, None,  'Opens location with NPC that allows crafting of alchemical items and potions.'),
        'black_market': ('Black Market', 15, 300, None, None, None,  'New magic and illegal items added to shop inventories.'),
        'arena': ('Arena', 25, 500, None, None, None,  'Small increase to morale. Allows hosting of tournament that lowers unrest.'),
        'granary': ('Granary', 15, 300, None, None, None,  'Increases food production.'),
        'housing': ('Housing', 10, 200, None, None, None,  'Increase population cap.'),
        'barracks_exp': ('Barracks Expansion', 10, 200, None, None, None,  'Increase soldier cap.'),
        'walls': ('Reinforce Walls', 50, 1000, None, None, None,  'Large boost to DP.'),
        'watch_tower': ('Watch Tower', 10, 200, None, None, None,  'Small boost to DP.'),
        'siege_weapon': ('Siege Weapon', 25, 500, None, None, None,  'Medium boost to DP.'),
    }


    # upgrades that unlocked at start of the game
    starting_upgrades = ('granary', 'housing', 'barracks_exp', 'walls', 'watch_tower', 'siege_weapon')


    class Upgrade(object):
        '''Upgrade for the castle'''
        def __init__(self, uid, ups):
            self.uid = uid
            # set parent 'upgrades'
            self.ups = ups
            self.name = all_upgrades[uid][0]
            self.rp_cost = all_upgrades[uid][1]
            self.gold_cost = all_upgrades[uid][2]
            self.descr = all_upgrades[uid][6]
            self.state = 'locked'
            self.open_room = all_upgrades[uid][3]
            self.on_build = all_upgrades[uid][4]
            self.weekly = all_upgrades[uid][5]

        def unlock(self):
            if self.state == 'locked':
                self.state = 'unlocked'

        def build(self):
            if self.open_room:
                self.ups.castle.rooms_access[self.open_room] = True
            # do on_build action
            if self.on_build:
                self.on_build()
            self.state = 'built'

        @property
        def locked(self):
            return self.state == 'locked'

        @property
        def unlocked(self):
            return self.state == 'unlocked'

        @property
        def built(self):
            return self.state == 'built'


    class Upgrades(object):
        '''All upgrades for a castle'''
        def __init__(self, castle):
            self.castle = castle
            self._upgrades = {}
            for uid in all_upgrades:
                self._upgrades.update({uid: Upgrade(uid, self)})

        def unlock(self, uid):
            '''Unlock an upgrade (allow it to be built)'''
            self._upgrades[uid].unlock()

        def build(self, uid):
            self._upgrades[uid].build()

        def __len__(self):
            return len(self._upgrades)

        def __iter__(self):
            return iter(self._upgrades.values())

        def __getitem__(self, uid):
            return self._upgrades[uid]

        # TODO: this functionality is similar to codex, maybe share some code
        @property
        def unlocked_count(self):
            '''Return number of unlocked upgrades (including built ones)'''
            return len([up for up in self._upgrades.values() if up.unlocked or up.built])

        @property
        def built_count(self):
            '''Return number of built upgrades'''
            return len([up for up in self._upgrades.values() if up.built])
