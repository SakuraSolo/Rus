from rpy_code import Actor, get_actor_flag, set_actor_flag
from fixtures import all_actors, msgs_mock
import rpy_code


def test_favors(all_actors):
    '''Favors should be non-negative'''
    ac = Actor('dummy', 'dummy')
    assert ac.favors == 0
    ac.favors += 1
    assert ac.favors == 1
    ac.favors -= 2
    assert ac.favors == 0


def test_actor_flags(all_actors, msgs_mock):
    ac = Actor('dummy', 'dummy')
    assert not get_actor_flag('dummy', 'test_flag')
    set_actor_flag('dummy', 'test_flag', 'test_val')
    assert get_actor_flag('dummy', 'test_flag') == 'test_val'


def test_total_favors(all_actors):
    ac = Actor('dummy', 'dummy')
    assert ac.favors == 0
    assert ac.total_favors == 0
    ac.favors += 5
    assert ac.favors == 5
    assert ac.total_favors == 5
    ac.favors -= 3
    assert ac.favors == 2
    assert ac.total_favors == 5


def test_actor_flags_defaults_to_zero(all_actors, msgs_mock):
    ac = Actor('dummy', 'dummy')
    assert 'some_flag' not in ac.flags
    assert ac.flags['some_flag'] == 0
    ac.flags['some_flag'] += 12
    assert ac.flags['some_flag'] == 12
    assert 'some_flag' in ac.flags
    assert get_actor_flag('dummy', 'some_flag') == 12
