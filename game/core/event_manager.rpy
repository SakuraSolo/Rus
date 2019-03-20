init -100 python:
    import random


    # dictionary holding all events, created on every game init
    all_events = {}


    def event(name, triggers, *args, **kwargs):
        ev = Event(name, triggers, *args, **kwargs)
        all_events[ev.name] = ev


    class Event(object):
        '''Event that holds some conditions and have triggers and priority'''
        def __init__(self, name, triggers, conditions = [], *args, **kwargs):
            self.name = name
            # if "triggers" is a string (only one trigger), convert it into tuple
            if isinstance(triggers, basestring):
                self.triggers = (triggers,)
            else:
                self.triggers = triggers
            # set priority (default 100, lesser number - higher priority)
            self.priority = kwargs.get('priority', 100)
            # if priority is given as interger, convert it to string (to be evaluated later)
            if isinstance(self.priority, int):
                self.priority = str(self.priority)
            # add list of conditions
            self.conditions = []
            for cond in conditions:
                if isinstance(cond, basestring):
                    self.conditions.append(EventCondition(cond))
                else:
                    self.conditions.append(cond)
            # copy tags
            self.tags = kwargs.get('tags', ())
            # allowed run count
            self.run_count = kwargs.get('run_count', None)
            # "solo" condition
            self.solo = kwargs.get('solo', None)
            self.only = kwargs.get('only', None)
            # events that this one depends on
            self.depends = kwargs.get('depends', ())
            # group this event belongs to
            self.group = kwargs.get('group', None)
            self.active = kwargs.get('active', True)
            self.init_flags = kwargs.get('init_flags', {})

        def check(self, already_passed):
            '''Checks conditions to see if this event can be run now'''
            # check if event already spent its allowed runs
            if self.run_count:
                if all_events_data[self.name]['run_count'] >= self.run_count:
                    return False
            # check for "solo" - event should be first in queue
            if self.solo or self.only:
                if len(already_passed) > 0:
                    return False
            # check for other conditions
            for condition in self.conditions:
                if not condition.eval(self.name, already_passed):
                    return False
            # check active timers
            for t in all_events_data[self.name]['timers'].values():
                if t > 0:
                    return False
            return True

        def __repr__(self):
            return '<event: ' + self.name + '>'


    class EventCondition(object):
        '''A condition (for events) that can be evaluated at any time'''

        def __init__(self, expr):
            self.expr = expr

        def eval(self, name, already_passed):
            # TODO: name and already_passed - why?
            return eval(self.expr)


    def update_all_events_data():
        '''Creates empty event data for newly added events'''
        for ev in all_events.itervalues():
            if ev.name not in all_events_data:
                all_events_data[ev.name] = {}
            if 'run_count' not in all_events_data[ev.name]:
                all_events_data[ev.name]['run_count'] = 0
            all_events_data[ev.name].setdefault('timers', {})
            all_events_data[ev.name].setdefault('flags', {})
            all_events_data[ev.name]['flags'].setdefault('_active', all_events[ev.name].active)
            for flag in ev.init_flags:
                all_events_data[ev.name]['flags'].setdefault(flag, ev.init_flags[flag])


    def update_event_timers():
        '''Updates timers for all events'''
        for ev_data in all_events_data.values():
            for t_name in ev_data['timers']:
                if ev_data['timers'][t_name] > 0:
                    ev_data['timers'][t_name] -= 1
            # remove zero timers
            ev_data['timers'] = {t_name: ev_data['timers'][t_name] for t_name in ev_data['timers'] if ev_data['timers'][t_name] != 0}


    class EventManager(object):
        '''Filters events by conditions and manages queue of events'''
        def __init__(self):
            self.events = []
            self.candidates = []

        def choose_events(self, trigger):
            '''Choose events by trigger and conditions'''
            self.candidates = []
            possible_events = []
            event_groups = {}

            # add events with required trigger to candidates
            for ev in all_events.itervalues():
                if trigger in ev.triggers and get_event_flag(ev.name, '_active'):
                    possible_events.append(ev)

            # compute priority for all possible events
            # this is done once per choosing events, so random priorities won't change during process
            possible_events_priorities = {}
            for ev in possible_events:
                possible_events_priorities[ev.name] = eval(ev.priority)

            # try to choose one event from every group
            for ev in possible_events:
                if ev.group:
                    # remove event from possible events and move it to related group
                    event_groups.setdefault(ev.group, [])
                    event_groups[ev.group].append(ev)
            # remove group events from possible events
            possible_events = [ev for ev in possible_events if not ev.group]
            for group in event_groups:
                event_groups[group].sort(key=lambda ev: possible_events_priorities[ev.name])
                # check conditions for all events in group, starting at highest priority
                cur_subgroup = []
                cur_subgroup_priority = 0
                for ev in event_groups[group]:
                    # if there is non-empty subgroup already and this event (and following) has lower priority, skip remaining events in this group
                    if len(cur_subgroup) > 0 and cur_subgroup_priority < possible_events_priorities[ev.name]:
                        break
                    # check dependencies and general conditions
                    if not self._check_dependencies(ev):
                        continue
                    # check general conditions
                    if not ev.check(self.candidates):
                        continue
                    # if subgroup is empty, update current subgroup priority
                    if len(cur_subgroup) == 0:
                        cur_subgroup_priority = possible_events_priorities[ev.name]
                    cur_subgroup.append(ev)
                if len(cur_subgroup) > 0:
                    # TODO: use different weights for events
                    if config.developer:
                        # use standard random in dev mode (so different event will be chosen after rollback)
                        chosen_from_group = random.choice(cur_subgroup)
                    else:
                        chosen_from_group = renpy.random.choice(cur_subgroup)
                    # add chosen event back to possible events
                    possible_events.append(chosen_from_group)

            # sort possible events by priority
            possible_events.sort(key=lambda ev: possible_events_priorities[ev.name])

            for ev in possible_events:
                # check dependency
                if not self._check_dependencies(ev):
                    continue
                # check general conditions
                if not ev.check(self.candidates):
                    continue
                self.candidates.append(ev)
                # if event has "only" condition set, skip all remaining events
                if ev.only:
                    break
            self.events = [candidate.name for candidate in self.candidates]

        def choose_one_event(self, trigger):
            '''Choose one event and return it'''
            candidates = []
            possible_events = []
            event_groups = {}

            # add events with required trigger to candidates
            for ev in all_events.itervalues():
                if trigger in ev.triggers and get_event_flag(ev.name, '_active'):
                    possible_events.append(ev)

            # compute priority for all possible events
            # this is done once per choosing events, so random priorities won't change during process
            possible_events_priorities = {}
            for ev in possible_events:
                possible_events_priorities[ev.name] = eval(ev.priority)

            # try to choose one event from every group
            for ev in possible_events:
                if ev.group:
                    # remove event from possible events and move it to related group
                    event_groups.setdefault(ev.group, [])
                    event_groups[ev.group].append(ev)
            # remove group events from possible events
            possible_events = [ev for ev in possible_events if not ev.group]
            for group in event_groups:
                event_groups[group].sort(key=lambda ev: possible_events_priorities[ev.name])
                # check conditions for all events in group, starting at highest priority
                cur_subgroup = []
                cur_subgroup_priority = 0
                for ev in event_groups[group]:
                    # if there is non-empty subgroup already and this event (and following) has lower priority, skip remaining events in this group
                    if len(cur_subgroup) > 0 and cur_subgroup_priority < possible_events_priorities[ev.name]:
                        break
                    # check dependencies and general conditions
                    if not self._check_dependencies(ev):
                        continue
                    # check general conditions
                    if not ev.check(candidates):
                        continue
                    # if subgroup is empty, update current subgroup priority
                    if len(cur_subgroup) == 0:
                        cur_subgroup_priority = possible_events_priorities[ev.name]
                    cur_subgroup.append(ev)
                if len(cur_subgroup) > 0:
                    # TODO: use different weights for events
                    if config.developer:
                        # use standard random in dev mode (so different event will be chosen after rollback)
                        chosen_from_group = random.choice(cur_subgroup)
                    else:
                        chosen_from_group = renpy.random.choice(cur_subgroup)
                    # add chosen event back to possible events
                    possible_events.append(chosen_from_group)

            # sort possible events by priority
            possible_events.sort(key=lambda ev: possible_events_priorities[ev.name])

            for ev in possible_events:
                # check dependency
                if not self._check_dependencies(ev):
                    continue
                # check general conditions
                if not ev.check(candidates):
                    continue
                candidates.append(ev)
                # if event has "only" condition set, skip all remaining events
                if ev.only:
                    break
            events = [candidate.name for candidate in candidates]
            if len(events) > 0:
                return events.pop(0)
            else:
                return None

        def has_event(self):
            '''Returns True if there are events in queue'''
            return len(self.events) > 0

        def get_event(self):
            '''Returns next event and removes it from queue'''
            ev_name = self.events.pop(0)
            # run_count is increased before event is actually run
            # this assumes that if events is got from event manager, it will be run
            all_events_data[ev_name]['run_count'] += 1
            return ev_name

        def _check_dependencies(self, ev):
            '''Returns True if all dependencies for ev were happened'''
            if ev.depends:
                all_dependency = True
                for dep_ev_name in ev.depends:
                    if not self._check_dependency(dep_ev_name):
                        all_dependency = False
                if all_dependency:
                    return True
            else:
                # if event has no dependencies, return True
                return True

        def _check_dependency(self, dep_string):
            '''Checks one given dependency'''
            # if dependency starts with "not", invert check
            if dep_string.startswith('not '):
                if ev_happened(dep_string[4:]):
                    return False
            elif not ev_happened(dep_string):
                return False
            return True

    def __events_init():
        store.all_events_data = {}
        store.event_manager = EventManager()
        update_all_events_data()

    config.start_callbacks.append(__events_init)
    # create default event data for all new event
    config.after_load_callbacks.append(update_all_events_data)


label run_events(trigger):

    $ event_manager.choose_events(trigger)
    while event_manager.has_event():
        $ ev_to_run = event_manager.get_event()
        $ msgs.show('{{color=#70F0F2}}--- {} --- Starting event: {} ---{{/color}}'.format(week, ev_to_run))
        call expression ev_to_run from call_expression_ev_to_run_1
        $ msgs.show('{{color=#70F0F2}}--- {} --- End of event: {} ---{{/color}}'.format(week, ev_to_run))
        # clear event's temporary variables after each event
        $ event_tmp = {}
    return


init 100:
    python hide:

        for i in all_events:
            if not renpy.has_label(i):
                raise Exception("'%s' is defined as an event somewhere in the game, but no label named '%s' was defined anywhere." % (i, i))
