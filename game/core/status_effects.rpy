# various status effects
init python:

    class StatusEffect(object):
        '''Basic status effect'''
        def __init__(self, name, kind, duration=1):
            # a name to show
            self.name = name
            # a duration in weeks
            self.duration = duration
            # type of effect - positive or negative ('pos', 'neg')
            self.kind = kind

        def weekly(self):
            '''Weekly update of this effect'''
            self.duration -= 1

        def on_update(self, av):
            '''Should apply actual effects to avatar; called when avatar\'s stats are updated'''
            pass

        def _change_single_target(self, av, trg, val):
            """Changes single target (avatar's stat or skill) by value"""
            if trg in av.skills:
                av.skill_changes[trg] += val
            elif trg == 'mp':
                # negative "val" for mp means positive "val" for wounds, so "-= val"
                av._mp_penalty -= max(val, -av._base_mp)
                av._mp += max(val, -av.mp)
            else:
                stat_name = '_' + trg
                # ensure that stat will be >= 0
                final_stat = max(getattr(av, stat_name) + val, 0)
                setattr(av, stat_name, final_stat)

        def __str__(self):
            return self.name


    class Injury(StatusEffect):
        '''Basic injury, a penalty for one stat'''

        def __init__(self, name, target, strength, duration=1):
            super(Injury, self).__init__(name, "neg", duration)
            # stat to decrease (strength, intelligence, reflexes, vitality, luck)
            self.target = target
            # strength of injury
            self.strength = strength

        def on_update(self, av):
            self._change_single_target(av, self.target, self.strength)

        def __str__(self):
            return '{} ({} {} for {}w)'.format(self.name, self.strength, self.target.capitalize(), self.duration)


    class MultiEffect(StatusEffect):
        '''Can contain several simple single-target effects; should be either negative or positive'''

        def __init__(self, name, kind, effects, duration=1):
            super(MultiEffect, self).__init__(name, kind, duration)
            self.kind = kind
            # list of simple effects
            self.effects = effects

        def on_update(self, av):
            for trg, val in self.effects:
                self._change_single_target(av, trg, val)

        def __str__(self):
            all_eff_str = ''
            for trg, val in self.effects:
                all_eff_str = ''.join((all_eff_str, '{} {} '.format(val, trg.capitalize())))
            return '{} ({}for {}w)'.format(self.name, all_eff_str, self.duration)
