import rpy_code
from rpy_code import World, Map, create_map

from test_create_map import map_def_fixture


def test_cur_tile_type(monkeypatch):
    week = 3
    monkeypatch.setattr(rpy_code, 'week', week, raising=False)
    world = World()
    assert world.cur_tile_type == None
    world.create_map(map_def_fixture)
    world.enter('test_map')
    world.maps['test_map'].pos = [3, 0]
    assert world.cur_tile_type == 'hills'


def test_enter_sets_cur_map(monkeypatch):
    '''Entering world should set current map'''
    week = 5
    monkeypatch.setattr(rpy_code, 'week', week, raising=False)
    world = World()
    world.create_map(map_def_fixture)
    assert not world.cur_map
    world.enter('test_map')
    assert world.cur_map.uid == 'test_map'
    assert world.cur_map.visited == 5


def test_exit(monkeypatch):
    week = 7
    monkeypatch.setattr(rpy_code, 'week', week, raising=False)
    world = World()
    world.create_map(map_def_fixture)
    assert not world.cur_map
    world.enter('test_map')
    assert world.cur_map.uid == 'test_map'
    world.exit()
    assert not world.cur_map
