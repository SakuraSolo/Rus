# Debug screen for events

default evd_filtered_events = []
default evd_filtered_caption = ''


screen events_info():
    modal True
    default selected_event = None
    frame:
        background '#99fe'
        xfill True
        yfill True
        has hbox
        # buttons for various filters
        vbox:
            style_prefix 'small_debug'
            xsize 300
            textbutton 'Close' action Hide('events_info') style 'button'
            textbutton 'All events' action FilterEventsBy(lambda ev: True, 'All events')
            text 'By group'
            textbutton 'Ruler event' action FilterEventsBy(lambda ev: ev.group == 'ruler_event', 'Group: ruler_event')
            textbutton 'Alexia: job in library' action FilterEventsBy(lambda ev: ev.group == 'alexia_library', 'Group: alexia_library')
            textbutton 'Alexia: maid job' action FilterEventsBy(lambda ev: ev.group == 'alexia_maid', 'Group: alexia_maid')
            textbutton 'Alexia: barmaid job' action FilterEventsBy(lambda ev: ev.group == 'alexia_barmaid', 'Group: alexia_barmaid')
            textbutton 'Alexia: breeding job' action FilterEventsBy(lambda ev: ev.group == 'alexia_breeding', 'Group: alexia_breeding')
            textbutton 'Alexia: forge job' action FilterEventsBy(lambda ev: ev.group == 'alexia_forge', 'Group: alexia_forge')
            text 'By trigger'
            textbutton 'Week end events' action FilterEventsBy(lambda ev: 'week_end' in ev.triggers, 'Trigger: week_end')
            textbutton 'Npc events' action FilterEventsBy(lambda ev: 'npc_events' in ev.triggers, 'Trigger: npc_events')
            textbutton 'Map resource' action FilterEventsBy(lambda ev: len([True for trig in ev.triggers if trig.startswith('map_res')]) > 0, 'Trigger: map_res_###')
            textbutton 'Map exploration' action FilterEventsBy(lambda ev: 'map_expl' in ev.triggers, 'Trigger: map_expl')
            text 'Misc'
            textbutton 'With timers' action FilterEventsBy(lambda ev: len(all_events_data[ev.name]['timers']) > 0, 'With timers')
            textbutton 'Non-active' action FilterEventsBy(lambda ev: not all_events_data[ev.name]['flags']['_active'], 'Non-active')
        # filtered result
        vbox:
            text evd_filtered_caption xsize 380
            if evd_filtered_events:
                vpgrid:
                    cols 1
                    mousewheel True
                    scrollbars "vertical"
                    yminimum 670
                    for evt in evd_filtered_events:
                        textbutton evt.name action SetScreenVariable('selected_event', evt.name):
                            background Frame('gui/stats_border.png', 12, 12)
                            text_line_spacing 0
                            xsize 380
                            if ev_exhausted(evt.name):
                                text_color cl_disabled
                            elif not all_events_data[evt.name]['flags']['_active']:
                                text_color cl_inactive
    use event_details(selected_event)


# show details for one event
screen event_details(evt):
    if evt:
        frame:
            xalign 0.99
            background '#f99e'
            xsize 530
            viewport:
                mousewheel True
                yfill True
                scrollbars 'vertical'
                vbox:
                    text 'Name: {}'.format(evt)
                    text 'Already happened: {}'.format(ev_happened(evt))
                    text 'Priority: {} ({})'.format(eval(all_events[evt].priority), all_events[evt].priority)
                    if all_events[evt].group:
                        text 'Group: {}'.format(all_events[evt].group)
                    text 'Triggers:'
                    for trigger in all_events[evt].triggers:
                        text '    {}'.format(trigger)
                    textbutton 'Force run now' action [Hide('events_info'), Call(evt), SensitiveIf(evt)]
                    text '{}'.format('Active' if all_events_data[evt]['flags']['_active'] else 'Not active'):
                        if all_events_data[evt]['flags']['_active']:
                            color cl_good
                        else:
                            color cl_bad
                    # run count and controls to change it
                    hbox:
                        text 'Run count: {}/{}'.format(all_events_data[evt]['run_count'], 'Infinity' if not all_events[evt].run_count else all_events[evt].run_count):
                            if all_events_data[evt]['run_count'] < all_events[evt].run_count or not all_events[evt].run_count:
                                color cl_good
                            else:
                                color cl_bad
                        textbutton '+' action [ChangeRunCount(evt, 1), renpy.restart_interaction]
                        textbutton '-' action [ChangeRunCount(evt, -1), renpy.restart_interaction]
                    # timers
                    if all_events_data[evt]['timers']:
                        text 'Timers:' color cl_bad bold True
                        for t in all_events_data[evt]['timers']:
                            text '{}: {}'.format(t, all_events_data[evt]['timers'][t])
                    else:
                        text 'No timers' color cl_good bold True
                    # conditions
                    text 'Conditions:' bold True
                    vbox:
                        for cond in all_events[evt].conditions:
                            text '*    ' + cond.expr substitute False:
                                if cond.eval('', ''):
                                    color cl_good
                                else:
                                    color cl_bad
                    # dependencies
                    if not all_events[evt].depends:
                        text 'No dependencies' color cl_good bold True
                    else:
                        text 'Dependencies:' bold True:
                            if event_manager._check_dependencies(all_events[evt]):
                                color cl_good
                            else:
                                color cl_bad
                        # list dependencies
                        vbox:
                            for dep_string in all_events[evt].depends:
                                text '*    ' + dep_string:
                                    if event_manager._check_dependency(dep_string):
                                        color cl_good
                                    else:
                                        color cl_bad
                    # flags
                    text 'Flags:' bold True
                    vbox:
                        for flag in sorted(all_events_data[evt]['flags']):
                            text '{}: {}'.format(flag, all_events_data[evt]['flags'][flag])


init python:

    class ChangeRunCount(Action):
        '''Changes run count for an event'''

        def __init__(self, event_name, val):
            self.event_name = event_name
            self.val = val

        def get_sensitive(self):
            # don't allow setting run_count below zero
            if self.val < 0 and all_events_data[self.event_name]['run_count'] + self.val < 0:
                return False
            return True

        def __call__(self):
            all_events_data[self.event_name]['run_count'] += self.val


    class FilterEventsBy(Action):
        '''Show only filtered events'''

        def __init__(self, fil_func, fil_caption):
            self.fil_func = fil_func
            self.fil_caption = fil_caption

        def __call__(self):
            filt_events = [ev for ev in all_events.values() if self.fil_func(ev)]
            filt_events = sorted(filt_events, key=lambda ev: ev.name)
            global evd_filtered_caption
            evd_filtered_caption = '{} ({})'.format(self.fil_caption, len(filt_events))
            global evd_filtered_events
            evd_filtered_events = filt_events
            renpy.restart_interaction()
