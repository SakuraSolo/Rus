from rpy_code import Actor, ActorJobState, set_job_class, change_actor_stress, do_job_barmaid, do_job_research_assistant, do_job_maid
from fixtures import all_actors, msgs_mock, castle, avatar
import rpy_code


def test_field():
    ajs = ActorJobState()
    assert ajs.stress == 0
    assert ajs.job_class is None
    assert ajs.job is None


def test_set_job_class(all_actors, msgs_mock):
    ac = Actor('dummy', 'Dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    assert ac.job_state.job_class is None
    set_job_class('dummy', 'pure_housewife')
    assert ac.job_state.job_class == 'pure_housewife'
    # test accessing of job skills, enjoyment
    assert ac.job_state.name == 'Pure Housewife'
    assert ac.job_state.skill('academics') == 5
    assert ac.job_state.enjoyment('academics') == 'L'


def test_change_actor_stress(all_actors, msgs_mock):
    ac = Actor('dummy', 'dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    assert ac.job_state.stress == 0
    change_actor_stress('dummy', 10)
    assert ac.job_state.stress == 10
    change_actor_stress('dummy', -5)
    assert ac.job_state.stress == 5
    change_actor_stress('dummy', -7)
    assert ac.job_state.stress == 0
    change_actor_stress('dummy', 108)
    assert ac.job_state.stress == 100


def test_job_efficiency():
    ajs = ActorJobState()
    ajs.stress = 0
    assert ajs.efficiency() == 1.0
    ajs.stress = 20
    assert ajs.efficiency() == 1.0
    ajs.stress = 100
    assert ajs.efficiency() == 0.0
    ajs.stress = 60
    assert ajs.efficiency() == 0.5
    # check job skill influence
    ajs.stress = 0
    ajs.job_class = 'pure_housewife'
    ajs.job = 'maid'
    assert ajs.efficiency() == 0.8
    # check efficiency for other jobs
    assert ajs.efficiency('maid') == 0.8
    assert ajs.efficiency('research_assistant') == 0.5
    assert ajs.efficiency('barmaid') == 0.8


def test_do_job_barmaid(castle, avatar, all_actors, msgs_mock):
    '''Barmaid job should add some money to treasury and to Rowan\'s personal gold'''
    ac = Actor('dummy', 'dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    ac.job_state.job = 'barmaid'
    ac.job_state.job_class = 'pure_housewife'
    assert castle.treasury == 0
    assert avatar.gold == 0
    assert ac.job_state.efficiency() == 0.8
    do_job_barmaid('dummy')
    assert castle.treasury == 16
    assert avatar.gold == 8
    # check additional coefficient (ex. from event)
    castle.treasury = 0
    avatar.gold = 0
    do_job_barmaid('dummy', 0.7)
    assert castle.treasury == int(16 * 0.7)
    assert avatar.gold == int(8 * 0.7)


def test_do_job_research_assistant(castle, avatar, all_actors, msgs_mock):
    '''Research assistant should add some research points'''
    ac = Actor('dummy', 'dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    ac.job_state.job = 'research_assistant'
    ac.job_state.job_class = 'pure_housewife'
    assert castle.rp == 0
    assert ac.job_state.efficiency() == 0.5
    do_job_research_assistant('dummy')
    assert castle.rp == 2
    # check additional coefficient (ex. from event)
    castle.rp = 0
    do_job_research_assistant('dummy', 1.5)
    assert castle.rp == 3


def test_do_job_maid(castle, avatar, all_actors, msgs_mock):
    '''Research assistant should add some research points'''
    ac = Actor('dummy', 'dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    ac.job_state.job = 'maid'
    ac.job_state.job_class = 'pure_housewife'
    assert castle.surface_maintenance_reduction == 0
    assert ac.job_state.efficiency() == 0.8
    do_job_maid('dummy')
    assert castle.surface_maintenance_reduction == 20
    # check additional coefficient (ex. from event)
    castle.surface_maintenance_reduction = 0
    do_job_maid('dummy', 1.5)
    assert castle.surface_maintenance_reduction == 30


def test_enjoyment_to_stress():
    ajs = ActorJobState()
    ajs.job_class = 'pure_housewife'
    assert ajs.enjoyment_coeff('domestics') == -0.3
    assert ajs.enjoyment_coeff('zoology') == 0.0
    assert ajs.enjoyment_coeff('crafting') == 0.5
    assert ajs.enjoyment_coeff('prostitution') == 1.0


def test_job_stress(castle, avatar, all_actors, msgs_mock):
    ac = Actor('dummy', 'dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    ac.job_state.job_class = 'pure_housewife'
    ac.job_state.stress = 50
    do_job_barmaid('dummy')
    assert ac.job_state.stress == 47


def test_breeding_job_effects(castle, avatar, all_actors):
    castle.buildings['pit'].build()
    assert castle.buildings['pit'].maintenance_discount == 0
    assert castle.buildings['pit'].capacity == 8
    ac = Actor('dummy', 'dummy')
    ajs = ActorJobState()
    ac.job_state = ajs
    ac.job_state.job_class = 'pure_housewife'
    ac.job_state.stress = 50
    ac.job_state.job = 'breeding'
    assert castle.buildings['pit'].bonus_capacity == 8
    assert castle.buildings['pit'].capacity == 16
    # check that increases in capacity are not affected by bonus capacity
    castle.buildings['pit'].capacity += 3
    assert castle.buildings['pit']._capacity == 11
    assert castle.buildings['pit'].maintenance_discount == 3
