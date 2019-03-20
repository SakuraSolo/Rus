from rpy_code import Map, create_map, MapResource, get_map_resource, World, Castle, MRDriderNest, MRVillage
import rpy_code

from test_create_map import map_def_fixture


def test_map_fields():
    m = Map()
    assert m.hexes == []
    assert m.resources == {}
    assert m.uid == ''
    assert m.name == ''
    assert m.width == 0
    assert m.height == 0
    assert m.pos == [0, 0]
    assert m.previous_pos == m.pos
    assert m.visited == False
    assert m.portals == {}


def test_coors_from_id():
    m = create_map(map_def_fixture)
    assert m._coords_from_id(3) == (3, 0)
    assert m._coords_from_id(0) == (0, 0)
    assert m._coords_from_id(8) == (0, 2)


def test_pos_id():
    m = create_map(map_def_fixture)
    assert m.pos == [2, 3]
    assert m.pos_id == 14
    m.pos = [3, 1]
    assert m.pos == [3, 1]
    assert m.pos_id == 7


def test_starting_previous_pos():
    '''Previous position should be same as start position on new map'''
    m = create_map(map_def_fixture)
    assert m.pos == [2, 3]
    assert m.previous_pos == [2, 3]
    m.pos = [1, 3]
    assert m.previous_pos == [2, 3]


def test_coping_previous_pos():
    '''Changing current position should not change previous position'''
    m = create_map(map_def_fixture)
    assert m.pos == [2, 3]
    assert m.previous_pos == [2, 3]
    # move player
    m.pos = [1, 3]
    # previous position should be same
    assert m.previous_pos == [2, 3]
    m.previous_pos = m.pos
    assert m.previous_pos == [1, 3]
    # move player
    m.pos = [1, 2]
    assert m.previous_pos == [1, 3]


def test_map_resources_fields():
    '''check generic map resource object'''
    m = Map()
    m.uid = 'dummy'
    mr = MapResource(m, (2, 3), 3)
    assert mr.coords == (2, 3)
    assert mr.uid == 'dummy_2_3'
    assert mr.seen == False
    assert mr.visited == False
    assert mr.res_id == 3
    assert mr.map_uid == 'dummy'
    assert mr.state == None
    assert mr.name == 'Resource (2, 3)'


def test_capturing_destroying():
    '''Map resource should change its state when it is captured/destroyed'''
    mr = MapResource(Map(), (1, 5), 3)
    assert mr.state is None
    mr.capture()
    assert mr.state == 'captured'
    mr.destroy()
    assert mr.state == 'destroyed'


def test_get_map_resource(monkeypatch):
    world = World()
    world.maps[map_def_fixture['uid']] = create_map(map_def_fixture)
    monkeypatch.setattr(rpy_code, 'world', world, raising=False)
    assert get_map_resource('test_map', [2, 0]).name == 'Village (2, 0)'


def test_on_capture_drider_nest(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    dn = MRDriderNest(Map(), (1, 1), 9)
    assert castle.buildings['pit'].drider_recruitment == 0
    dn.capture()
    assert castle.buildings['pit'].drider_recruitment == 0.5


def test_on_capture_village(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    vi = MRVillage(Map(), (1, 1), 3)
    assert castle.villages_income == 0
    assert castle.villages == 0
    vi.capture()
    assert castle.villages_income == 5
    assert castle.villages == 1

