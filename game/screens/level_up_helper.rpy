init python:

    # TODO: probably it is better to pass avatar to levelup helper at init
    class LevelUpHelper(object):
        '''Helper for Level Up screen'''

        def __init__(self):
            self.stat_points = 3
            self.skill_points = 5
            self.feat = None
            self.stat_changes = {}
            for stat in main_stats:
                self.stat_changes[stat] = 0
            self.skill_changes = {}
            for skill in all_skills:
                self.skill_changes[skill] = 0

        def change_stat(self, stat, val):
            '''Change prepared stat points by val'''
            self.stat_changes[stat] += val
            self.stat_points -= val

        def change_skill(self, skill, val):
            self.skill_changes[skill] += val
            self.skill_points -= val

        def stat_change(self, stat):
            '''Show points for stat'''
            return self.stat_changes[stat]

        def skill_change(self, skill):
            return self.skill_changes[skill]

        def stat_change_possible(self, stat, val):
            '''Check if it is possible to change stat points by val'''
            if val >= 0:
                return self.stat_points >= val
            else:
                return self.stat_changes[stat] >= -val

        def skill_change_possible(self, av, skill, val):
            '''Check if it is possible to change skill points for avatar by val'''
            if val >= 0:
                # skill cap is current avatar level + 3 + 1 (+1 because level will be +1 after level up)
                return (self.skill_points >= val) and (av.base_skill(skill) + val + self.skill_changes[skill] <= av.lvl + 4)
            else:
                return self.skill_changes[skill] >= -val

        def can_choose_feat(self, av):
            # player can choose feat on even levels, so current level should be odd
            return (av.lvl % 2 == 1) and not self.feat

        def choose_feat(self, feat):
            self.feat = feat

        def clear_feat(self):
            self.feat = None

        def can_complete(self, av):
            '''If level up can be completed now'''
            return (self.stat_points == 0) and (self.skill_points == 0) and (not self.can_choose_feat(av))

        def complete(self, av):
            '''Apply change points to stats of avatar and reset self'''
            for stat in self.stat_changes:
                setattr(av, 'base_' + stat, getattr(av, 'base_' + stat) + self.stat_changes[stat])
            for skill in self.skill_changes:
                av.skills[skill] += self.skill_changes[skill]
            av.add_feat(self.feat)
            av.lvl += 1
