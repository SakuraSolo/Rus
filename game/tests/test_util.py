import rpy_code
from rpy_code import ratio_color, get_rnd_item, all_items, Avatar, Item, lose_rnd_item, Castle, complete_research, MultiEffect, av_has_injuries, change_recruitment_bonus, change_research_bonus
from rpy_code import change_prisoners, Spy, add_spy_exp, World, create_map, capture_resource, possible_to_research

from test_create_map import map_def_fixture
from fixtures import castle, avatar, msgs_mock, renpy_mock


def test_values_equal():
    '''Use col_eq if values are equal'''
    assert ratio_color(3, 3) == '#fff'
    # non-default color
    assert ratio_color(3, 3, col_eq='ff0') == 'ff0'


def test_value1_lesser():
    '''Use col_le if val1 < val2'''
    assert ratio_color(3, 4) == '#f00'
    # non-default color
    assert ratio_color(3, 7, col_le='f30') == 'f30'


def test_value1_greater():
    '''Use col_gt if val1 > val2'''
    assert ratio_color(5, 3) == '#0f0'
    # non-default color
    assert ratio_color(4, 3, col_gt='0f2') == '0f2'


def test_get_rnd_item(monkeypatch, mocker, msgs_mock, renpy_mock):
    av_mock = mocker.Mock()
    monkeypatch.setattr(rpy_code, 'avatar', av_mock, raising=False)
    get_rnd_item(0, 100)
    assert av_mock.inventory.add.called
    # check that item that added to inventory has buy price in given range
    assert 0 <= all_items[av_mock.inventory.add.call_args[0][0]][4][0] <= 100


def test_get_rnd_item_armor(avatar, msgs_mock, renpy_mock, mocker):
    '''get_rnd_item should be able to filter items by required keyword'''
    avatar.inventory = mocker.Mock()
    get_rnd_item(0, 500, 'armour')
    assert 'armour' in all_items[avatar.inventory.add.call_args[0][0]][1]


def test_get_rnd_item_non_random(avatar, msgs_mock, renpy_mock, mocker, monkeypatch):
    avatar.inventory = mocker.Mock()
    all_items_fix = {'weap': ('dummy', ['main', 'weapon'], 1, {}, (10, 10), 'img', 'descr'),}
    monkeypatch.setattr(rpy_code, 'all_items', all_items_fix, raising=False)
    get_rnd_item(0, 500)
    assert avatar.inventory.add.called
    assert avatar.inventory.add.call_args[0][0] == 'weap'
    avatar.inventory.reset_mock()
    assert not avatar.inventory.add.called
    all_items_fix = {'weap': ('dummy', ['main', 'weapon', 'non-random'], 1, {}, (10, 10), 'img', 'descr'),}
    monkeypatch.setattr(rpy_code, 'all_items', all_items_fix, raising=False)
    get_rnd_item(0, 500)
    assert not avatar.inventory.add.called


def test_lose_rnd_item(msgs_mock, avatar, renpy_mock):
    avatar.inventory.add('leather_jerkin')
    avatar.inventory.add('iron_rapier')
    assert avatar.inventory.bp[Item('leather_jerkin')] == 1
    assert lose_rnd_item(0, 150)
    assert avatar.inventory.bp[Item('leather_jerkin')] == 0
    assert avatar.inventory.bp[Item('iron_rapier')] == 1
    # try to remove an item second time
    assert not lose_rnd_item(0, 150)
    assert avatar.inventory.bp[Item('leather_jerkin')] == 0
    assert avatar.inventory.bp[Item('iron_rapier')] == 1


def test_lose_rnd_item_non_random(msgs_mock, avatar, renpy_mock, mocker, monkeypatch):
    # check that regular item is removed from inventory
    all_items_fix = {'weap': ('dummy', ['main', 'weapon'], 1, {}, (10, 10), 'img', 'descr'),}
    monkeypatch.setattr(rpy_code, 'all_items', all_items_fix, raising=False)
    avatar.inventory.add('weap')
    assert avatar.inventory.bp[Item('weap')] == 1
    assert Item('weap') in avatar.inventory.bp
    assert lose_rnd_item(0, 150)
    assert Item('weap') not in avatar.inventory.bp
    # check that non-random item is not removed
    all_items_fix = {'weap': ('dummy', ['main', 'weapon', 'non-random'], 1, {}, (10, 10), 'img', 'descr'),}
    monkeypatch.setattr(rpy_code, 'all_items', all_items_fix, raising=False)
    avatar.inventory.add('weap')
    assert avatar.inventory.bp[Item('weap')] == 1
    assert Item('weap') in avatar.inventory.bp
    assert not lose_rnd_item(0, 150)
    assert avatar.inventory.bp[Item('weap')] == 1
    assert Item('weap') in avatar.inventory.bp


def test_complete_research(monkeypatch, mocker):
    '''complete_research should complete research normally (with results seen on next turn)'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    # insert mock instead of 'history_of_rosaria' research
    rs_mock = mocker.MagicMock()
    rs_mock.uid = 'history_of_rosaria'
    castle.researches['history_of_rosaria'] = rs_mock
    castle.set_research('history_of_rosaria')
    assert castle.current_research.uid == 'history_of_rosaria'
    complete_research()
    assert castle.current_research is None
    assert castle.completed_researches == ['history_of_rosaria']
    assert rs_mock.on_complete.called
    assert rs_mock.completed == True


def test_av_has_injuries(monkeypatch):
    avatar = Avatar('dummy')
    monkeypatch.setattr(rpy_code, 'avatar', avatar, raising=False)
    avatar.add_effect(MultiEffect('dummy', 'pos', (('luck', -1),)))
    assert not av_has_injuries()
    avatar.add_effect(MultiEffect('dummy', 'neg', (('luck', -1),)))
    assert av_has_injuries()


def test_change_recruitment_bonuses(monkeypatch, mocker):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'msgs', mocker.Mock(), raising=False)
    assert castle.recruitment_bonuses.get('sanctum', 0) == 0
    change_recruitment_bonus('sanctum', 2)
    assert castle.recruitment_bonuses.get('sanctum', 0) == 2
    # recruitment bonus should be non-negative
    change_recruitment_bonus('sanctum', -1)
    assert castle.recruitment_bonuses.get('sanctum', 0) == 1
    change_recruitment_bonus('sanctum', -5)
    assert castle.recruitment_bonuses.get('sanctum', 0) == 0


def test_change_research_bonus(monkeypatch, mocker):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'msgs', mocker.Mock(), raising=False)
    assert castle.research_bonus == 0
    change_research_bonus(4)
    assert castle.research_bonus == 4
    # research bonus should be non-negative
    change_research_bonus(-6)
    assert castle.research_bonus == 0


def test_change_prisoners(monkeypatch, mocker):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    monkeypatch.setattr(rpy_code, 'msgs', mocker.Mock(), raising=False)
    castle.buildings['dungeon'].build()
    assert castle.buildings['dungeon'].prisoners == 0
    assert castle.buildings['dungeon'].capacity == 10
    change_prisoners(5)
    assert castle.buildings['dungeon'].prisoners == 5
    change_prisoners(15)
    assert castle.buildings['dungeon'].prisoners == 10


def test_add_spy_exp(monkeypatch, mocker):
    monkeypatch.setattr(rpy_code, 'msgs', mocker.Mock(), raising=False)
    monkeypatch.setattr(rpy_code, 'all_objects', {}, raising=False)
    sp = Spy('m')
    assert sp.exp == 0
    add_spy_exp(sp.uid, 100)
    assert sp.exp == 100


def test_capture_resource(monkeypatch, mocker):
    monkeypatch.setattr(rpy_code, 'msgs', mocker.Mock(), raising=False)
    world = World()
    world.maps[map_def_fixture['uid']] = create_map(map_def_fixture)
    world.maps['test_map'].resources[(2, 0)] = mocker.Mock()
    monkeypatch.setattr(rpy_code, 'world', world, raising=False)
    assert not world.maps['test_map'].resources[(2, 0)].capture.called
    capture_resource('test_map', (2, 0))
    assert world.maps['test_map'].resources[(2, 0)].capture.called


def test_possible_to_research(castle, mocker):
    castle.researches = {}
    assert not possible_to_research()
    rs1 = mocker.Mock()
    rs1.req_met.return_value = False
    rs1.completed = False
    rs2 = mocker.Mock()
    rs2.req_met.return_value = False
    rs2.completed = False
    castle.researches = {1: rs1, 2: rs2}
    assert not possible_to_research()
    rs1.req_met.return_value = True
    assert possible_to_research()
    rs1.completed = True
    assert not possible_to_research()
