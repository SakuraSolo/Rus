init python:

    import math


    class Avatar(object):
        '''Avatar (character under player\'s control), with stats and inventory'''

        def __init__(self, name):
            self.name = name
            # items equipped in slots
            self.inventory = Inventory(self)
            # personal gold of current avatar
            self._gold = 0
            # total experience
            self.exp = 0
            # current level
            self.lvl = 1
            # base MP is 10 + feats bonuses
            self._base_mp = 10
            # wounds - reduce movement points (source - direct damage)
            self._wounds = 0
            # mp penalty (from other sources than body damage, from status effects)
            self._mp_penalty = 0
            # current mp
            self._mp = 10
            # bonuses to mp from items and feats
            #self._mp_bonus = 0
            # create base skills
            self.skills = {}
            # current changes in skills (from status effects)
            self.skill_changes = {}
            for skill in all_skills:
                self.skills[skill] = 0
                self.skill_changes[skill] = 0
            self.feats = []
            # status effects
            self.effects = []
            # armour penalty to some skills
            self._armour_penalty = 0
            # view distance (on map)
            self.view_distance = 1

            # stats will be created via create_avatar_stat
            self.update_stats()

        # TODO: update_stats should be called manually in case like: avatar.inventory.main = 'dagger'
        def update_stats(self):
            '''Update stats (equipment changes to base stats)'''
            # TODO: may be unsafe to reset stats, this will also remove non-item effects
            # TODO: _reset_stats should not be used, old final stats should be swapped with new final stats
            self._reset_stats()
            # apply status effects
            for se in self.effects:
                se.on_update(self)
            # iterate through equipped items and apply their modifiers
            for item in self.inventory.slots.values():
                if item:
                    # get stat effects from item defitions and apply them
                    for stat_letter in item.effects:
                        stat_name = letter_to_stat[stat_letter]
                        stat_eff = item.effects[stat_letter]
                        final_stat = stat_eff + getattr(self, stat_name)
                        # TODO: this will not protect from non-item effects dropping stats below zero
                        if final_stat < 0:
                            final_stat = 0
                        setattr(self, '_' + stat_name, final_stat)
                    self._armour_penalty += item.armour_penalty

        def _reset_stats(self):
            '''Reset all stats to their base values'''
            for stat_name in letter_to_stat.values():
                setattr(self, '_' + stat_name, getattr(self, 'base_' + stat_name))
            # reset current skill changes
            for skill in self.skill_changes:
                self.skill_changes[skill] = 0
            self._armour_penalty = 0
            self._mp_penalty = 0

        @property
        def new_exp(self):
            '''Amount of experience accumulated after last level up'''
            return self.exp - (2 ** (self.lvl - 1) - 1) * 100

        @property
        def req_exp(self):
            '''Amount of experience to complete current level'''
            return (2 ** (self.lvl - 1)) * 100

        def stat_mod(self, stat):
            '''return stat modifier'''
            return int(math.ceil(getattr(self, stat) / 10.0))

        def take_damage(self, dam):
            '''Store damage as wounds; wounds should not be higher than base MP'''
            eff_damage = min(dam, self.base_mp - self.wounds)
            self._wounds += eff_damage
            # damage should also reduce current MP
            self._mp -= min(eff_damage, self._mp)

        def heal(self, number="ALL"):
            '''Heals given number of wounds (or all)'''
            if number == "ALL":
                self._wounds = 0
            else:
                self._wounds -= min(number, self._wounds)

        def heal_injuries(self):
            '''Heals all negative effects'''
            self.effects = [eff for eff in self.effects if eff.kind != 'neg']
            self.update_stats()

        def reset_mp(self):
            '''Resets MP to their possible maximum'''
            self._mp = self._base_mp - self._wounds - self._mp_penalty

        def base_skill(self, skill):
            '''Return pure base skill, without mods and feats'''
            return self.skills[skill]

        def skill(self, skill):
            '''Return full skill (with mods from stats and feats)'''
            fin_skill = self.skills[skill] + self.skill_changes[skill]
            # bonus to skill from related stat is applied in checking functions
            if skill in skills_with_armour_penalty:
                fin_skill += self._armour_penalty
            if fin_skill < 0:
                fin_skill = 0
            return fin_skill

        def add_feat(self, feat):
            '''Adds feat and updates feats bonuses'''
            # add feat only if it not already added and if such feat is registered in all_feats
            if (not feat in self.feats) and (feat in all_feats):
                self.feats.append(feat)
                # target can be skill, stat or mp
                for trg in all_feats[feat][1]:
                    # if trg is one letter, it is letter for stat, as in 'letter_to_stat'
                    if len(trg) == 1:
                        setattr(self, 'base_' + letter_to_stat[trg], getattr(self, 'base_' + letter_to_stat[trg]) + all_feats[feat][1][trg])
                    # add bonus to overall mp bonus
                    #elif trg == 'mp':
                    #    self._mp_bonus += all_feats[feat][1][trg]
                    # add skill bonuses to base skills
                    else:
                        self.skills[trg] += all_feats[feat][1][trg]
                self.update_stats()

        def add_effect(self, eff):
            '''Adds a status effect'''
            self.effects.append(eff)
            self.update_stats()

        def weekly(self):
            '''Weekly update of avatar\'s state'''
            # update effects
            for eff in self.effects:
                eff.weekly()
            # remove expired effects
            self.effects = [eff for eff in self.effects if eff.duration]
            self.update_stats()
            self.reset_mp()

        @property
        def base_mp(self):
            return self._base_mp

        @property
        def mp(self):
            '''Current movement points'''
            return self._mp

        @mp.setter
        def mp(self, val):
            self._mp = val

        @property
        def wounds(self):
            '''Wounds that reduce MP'''
            return self._wounds

        @property
        def mp_penalty(self):
            '''Generic (non-damage) penalty to MP - from status effects'''
            return self._mp_penalty

        @property
        def gold(self):
            return self._gold

        @gold.setter
        def gold(self, val):
#~             if val < 0:
#~                 val = 0
            self._gold = val


    # maybe it is better to define stats as classes
    def create_avatar_stat(cls, name, init_val):
        '''Create standard stat for the avatar'''
        def base_getter(self):
            return getattr(self, '_base_' + name)

        def base_setter(self, val):
            if val < 0:
                val = 0
            setattr(self, '_base_' + name, val)
            self.update_stats()

        def final_getter(self):
            return getattr(self, '_' + name)

        setattr(cls, '_base_' + name, init_val)
        setattr(cls, '_' + name, init_val)
        setattr(cls, 'base_' + name, property(base_getter, base_setter))
        setattr(cls, name, property(final_getter))


    # create standard stats for Avatar class
    create_avatar_stat(Avatar, 'strength', 1)
    create_avatar_stat(Avatar, 'vitality', 1)
    create_avatar_stat(Avatar, 'reflexes', 1)
    create_avatar_stat(Avatar, 'intelligence', 1)
    create_avatar_stat(Avatar, 'luck', 1)
    create_avatar_stat(Avatar, 'corruption', 0)
    create_avatar_stat(Avatar, 'infamy', 0)
    create_avatar_stat(Avatar, 'guilt', 0)


    main_stats = ('strength', 'vitality', 'reflexes', 'intelligence', 'luck')
