from rpy_code import (EventManager, event, update_all_events_data, set_event_timer,
    get_event_timer, update_event_timers, set_event_flag, get_event_flag, activate_event, choose_and_insert_next_event)
from fixtures import all_events, all_events_data, msgs_mock
import rpy_code


def test_choosing_events(all_events, all_events_data):
    em = EventManager()
    event('sample', triggers='day_end', priority=150)
    update_all_events_data()
    assert not em.has_event()
    em.choose_events('day_end')
    assert em.events == ['sample']
    assert em.has_event()


def test_get_event(all_events, all_events_data):
    em = EventManager()
    event('sample', triggers='day_end', priority=150)
    update_all_events_data()
    em.choose_events('day_end')
    assert em.events == ['sample']
    assert em.has_event()
    assert em.get_event() == 'sample'


def test_event_tags(all_events):
    event('sample', triggers='day_end', tags=('test1', 'test2'))
    assert all_events['sample'].tags == ('test1', 'test2')


def test_variable_priority(all_events, all_events_data, monkeypatch):
    em = EventManager()
    event('sample', triggers='day_end')
    event('ev_var_priority', triggers='day_end', priority='120 if somevar else 90')
    update_all_events_data()
    monkeypatch.setattr(rpy_code, 'somevar', True, raising=False)
    em.choose_events('day_end')
    assert em.events == ['sample', 'ev_var_priority']
    monkeypatch.setattr(rpy_code, 'somevar', False, raising=False)
    em.choose_events('day_end')
    assert em.events == ['ev_var_priority', 'sample']


def test_once_mod(all_events, all_events_data):
    em = EventManager()
    event('sample_once', run_count=1, triggers='day_end')
    event('sample_repeat', triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert 'sample_once' in em.events and 'sample_repeat' in em.events
    # get events so their run_count would be incremented
    em.get_event()
    em.get_event()
    em.choose_events('day_end')
    assert 'sample_repeat' in em.events
    assert 'sample_once' not in em.events


def test_simple_condition(all_events, all_events_data, monkeypatch):
    em = EventManager()
    event('sample', conditions=('somevar',), triggers='day_end')
    update_all_events_data()
    monkeypatch.setattr(rpy_code, 'somevar', False, raising=False)
    em.choose_events('day_end')
    assert em.events == []
    monkeypatch.setattr(rpy_code, 'somevar', True, raising=False)
    em.choose_events('day_end')
    assert em.events == ['sample']


def test_solo_mod(all_events, all_events_data, monkeypatch):
    '''Solo events should only be choosen if there are no events before it (but may be after)'''
    em = EventManager()
    event('sample_solo', solo=True, triggers='day_end', priority=110)
    event('sample', conditions=('somevar',), triggers='day_end')
    update_all_events_data()
    monkeypatch.setattr(rpy_code, 'somevar', True, raising=False)
    em.choose_events('day_end')
    assert em.events == ['sample']
    monkeypatch.setattr(rpy_code, 'somevar', False, raising=False)
    em.choose_events('day_end')
    assert em.events == ['sample_solo']


def test_only_mod(all_events, all_events_data, monkeypatch):
    '''"Only" events should only be choosen if there are no events before it, and all events after them are skipped'''
    em = EventManager()
    event('sample_only', only=True, triggers='day_end')
    event('sample_high', conditions=('somevar',), triggers='day_end', priority=90)
    event('sample_low', triggers='day_end', priority=110)
    update_all_events_data()
    monkeypatch.setattr(rpy_code, 'somevar', True, raising=False)
    em.choose_events('day_end')
    assert em.events == ['sample_high', 'sample_low']
    monkeypatch.setattr(rpy_code, 'somevar', False, raising=False)
    em.choose_events('day_end')
    assert em.events == ['sample_only']


def test_depends(all_events, all_events_data):
    em = EventManager()
    event('previous', triggers='day_end')
    event('current', depends=('previous',), triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert em.events == ['previous']
    # get event to register it as happened
    em.get_event()
    em.choose_events('day_end')
    assert 'previous' in em.events and 'current' in em.events


def test_negative_depends(all_events, all_events_data):
    em = EventManager()
    event('previous', triggers='day_end')
    event('current', depends=('not previous',), triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert set(('previous', 'current')) == set(em.events)
    # get events to register them as happened
    em.get_event()
    em.get_event()
    em.choose_events('day_end')
    assert ['previous'] == em.events


def test_group(all_events, all_events_data):
    em = EventManager()
    event('non-group', triggers='day_end')
    event('group1', group='somegroup', triggers='day_end')
    event('group2', group='somegroup', triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert len(em.events) == 2
    assert 'non-group' in em.events


def test_priorities_in_group(all_events, all_events_data):
    em = EventManager()
    event('non-group', triggers='day_end')
    event('group1_high', group='somegroup', triggers='day_end', priority=90)
    event('group1_med', group='somegroup', triggers='day_end')
    event('group1_low', group='somegroup', triggers='day_end', priority=110)
    event('group2_high', group='group2', triggers='day_end', priority=80)
    event('group2_low', group='group2', triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert len(em.events) == 3
    assert em.events == ['group2_high', 'group1_high', 'non-group']


def test_event_timers(all_events, all_events_data, msgs_mock):
    em = EventManager()
    event('sample', triggers='day_end')
    update_all_events_data()
    set_event_timer('sample', 'test_timer', 2)
    em.choose_events('day_end')
    assert em.events == []
    assert get_event_timer('sample', 'test_timer') == 2
    update_event_timers()
    assert get_event_timer('sample', 'test_timer') == 1
    update_event_timers()
    assert get_event_timer('sample', 'test_timer') is None
    em.choose_events('day_end')
    assert em.events == ['sample']


def test_event_flags(all_events, all_events_data, msgs_mock):
    em = EventManager()
    event('sample', triggers='day_end')
    update_all_events_data()
    assert get_event_flag('sample', 'test_flag') is None
    set_event_flag('sample', 'test_flag', 'test_val')
    assert get_event_flag('sample', 'test_flag') == 'test_val'


def test_deactivated_events(all_events, all_events_data, msgs_mock):
    em = EventManager()
    event('sample', triggers='day_end', active=False)
    update_all_events_data()
    em.choose_events('day_end')
    assert em.events == []
    activate_event('sample')
    em.choose_events('day_end')
    assert em.events == ['sample']


def test_initial_flags(all_events, all_events_data):
    em = EventManager()
    event('sample', triggers='day_end', init_flags={'test_flag': 'test_val'})
    update_all_events_data()
    assert get_event_flag('sample', 'dummy') is None
    assert get_event_flag('sample', 'test_flag') == 'test_val'


def test_insert_next_event(all_events, all_events_data, msgs_mock, monkeypatch):
    em = EventManager()
    monkeypatch.setattr(rpy_code, 'event_manager', em, raising=False)
    event('sample', triggers='day_end', priority=90)
    event('middle', triggers='dummy')
    event('last', triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert em.events == ['sample', 'last']
    assert em.get_event() == 'sample'
    choose_and_insert_next_event('dummy')
    assert em.get_event() == 'middle'
    assert em.get_event() == 'last'
    assert em.has_event() == False


def test_insert_next_event_failed(all_events, all_events_data, msgs_mock, monkeypatch):
    '''If there is no events matching for insertign, fail silently'''
    em = EventManager()
    monkeypatch.setattr(rpy_code, 'event_manager', em, raising=False)
    event('sample', triggers='day_end', priority=90)
    event('middle', triggers='failing')
    event('last', triggers='day_end')
    update_all_events_data()
    em.choose_events('day_end')
    assert em.events == ['sample', 'last']
    assert em.get_event() == 'sample'
    choose_and_insert_next_event('dummy')
    assert em.get_event() == 'last'
    assert em.has_event() == False
