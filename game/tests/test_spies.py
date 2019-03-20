from rpy_code import Spy, spy_names, spy_traits, SpyMission, Castle, get_spies, get_object, assign_mission, SMInfiltrationDelays, SMInfiltrationDominatorPrisoners, spy_sprites
import rpy_code


def test_fields(monkeypatch):
    all_objects = {}
    monkeypatch.setattr(rpy_code, 'all_objects', all_objects, raising=False)
    spy = Spy('f', 'dummy')
    assert spy.name in spy_names['f']
    assert spy.exp == 0
    assert spy.lvl == 0
    assert len(spy.traits) == 1
    assert spy.traits[0] in spy_traits[spy.sex]
    assert spy.mission is None
    assert spy.sex == 'f'
    assert spy.pers == 'she'
    assert spy.poss == 'her'
    assert spy.sprite in spy_sprites['f']


def test_spy_is_added_to_all_objects(monkeypatch):
    '''When spy is created, it should add itself to all_objects'''
    all_objects = {}
    monkeypatch.setattr(rpy_code, 'all_objects', all_objects, raising=False)
    spy = Spy('m')
    assert spy in all_objects.values()


def test_spy_mission(monkeypatch):
    monkeypatch.setattr(rpy_code, 'week', 18, raising=False)
    sm = SpyMission(777, 'infiltration', ('rosaria_map', (3, 5)), 3, 17, 'dummy')
    assert sm.spy_uid == 777
    assert sm.type == 'infiltration'
    assert sm.loc == ('rosaria_map', (3, 5))
    assert sm.duration == 3
    assert sm.started == 17
    assert sm.label == 'dummy'
    assert not sm.completed
    monkeypatch.setattr(rpy_code, 'week', 20, raising=False)
    assert sm.completed


def test_get_spies(monkeypatch):
    '''get_spies should return list of spies for various selectors'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'all_objects', {}, raising=False)
    monkeypatch.setattr(rpy_code, 'week', 17, raising=False)
    castle.buildings['brothel'].spies.append(Spy('f').uid)
    assert len(get_spies('idle')) == 1
    castle.buildings['brothel'].spies.append(Spy('f').uid)
    assert len(get_spies('idle')) == 2
    get_object(castle.buildings['brothel'].spies[0]).mission = SpyMission(777, 'infiltration', ('rosaria_map', (3, 5)), 3, 17, 'dummy')
    assert len(get_spies('idle')) == 1
    assert len(get_spies('on mission')) == 1
    assert len(get_spies('completed mission')) == 0
    assert isinstance(get_spies('on mission')[0], Spy)


def test_assign_spy(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'all_objects', {}, raising=False)
    spy = Spy('f')
    assign_mission(spy.uid, 'infiltration', ('rosaria_map', (4, 5)), 5)
    assert spy.mission.spy_uid == spy.uid


def test_sm_infiltration_delays(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'all_objects', {}, raising=False)
    monkeypatch.setattr(rpy_code, 'spy_mission_defs', [SMInfiltrationDelays], raising=False)
    monkeypatch.setattr(rpy_code, 'week', 5, raising=False)
    spy = Spy('f')
    spy.traits = ['Impulsive']
    assign_mission(spy.uid, 'infiltration', ('rosaria_map', (4, 5)), 5)
    assert spy.mission.spy_uid == spy.uid
    assert not spy.mission.completed
    assert 6 <= spy.mission.duration <= 7


def test_sm_infiltration_dominator_prisoners(monkeypatch):
    castle = Castle()
    castle.buildings['dungeon'].build()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'all_objects', {}, raising=False)
    monkeypatch.setattr(rpy_code, 'spy_mission_defs', [SMInfiltrationDominatorPrisoners], raising=False)
    monkeypatch.setattr(rpy_code, 'week', 5, raising=False)
    spy = Spy('f')
    spy.traits = ['Mistress']
    assign_mission(spy.uid, 'infiltration', ('rosaria_map', (4, 5)), 5)
    assert spy.mission.spy_uid == spy.uid
    assert not spy.mission.completed
    assert 2 <= spy.mission.duration <= 3
