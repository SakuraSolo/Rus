from rpy_code import create_map, Map


map_def_fixture = {
    'uid': 'test_map',
    'name': 'Test map',
    'width': 4,
    'height': 4,
    'start_pos': [2, 3],
    'default': 0,
    'fixed': (
        [2, [2, 0], [], 1, False, False, 3, False, 0, [], -1],
        [-1, [3, 0], [], 2, False, False, 9, False, 0, [], -1],
        [6, [2, 0], [], 3, False, False, 6, False, 0, [], -1],
        [9, 0, 0, 0, False, False, 2, False, 0, [], -1],
    ),
    'terrains': [],
    'resources': [],
    'portals': [[1, 2, 'Test portal']],
}


def test_create_map():
    '''create_map should create a map from supplied map definition'''
    m = create_map(map_def_fixture)
    assert isinstance(m, Map)
    assert m.uid == 'test_map'
    assert m.name == 'Test map'
    assert m.width == 4
    assert m.height == 4
    assert m.pos == [2, 3]
    # check that position is copied, not referenced
    m.pos = [0, 3]
    assert map_def_fixture['start_pos'][0] == 2
    assert len(m.hexes) == m.width * m.height
    assert m.terrain(2) == 1
    assert m.terrain((3, 0)) == 2
    assert m.terrain(6) == 3
    assert m.terrain((0, 1)) == 0


def test_hexes_are_not_shared():
    '''check that hexes is not shared between maps'''
    m = create_map(map_def_fixture)
    assert m.hexes[2][3] == 1
    m.hexes[2][3] = -7
    m2 = create_map(map_def_fixture)
    assert m2.hexes[2][3] == 1
    assert m.hexes[2][3] == -7


def test_map_resources_added():
    '''check that required resources are created (from fixed hexes with resources)'''
    m = create_map(map_def_fixture)
    assert len(m.resources) == 4
    assert m.resources[(2, 0)].name == 'Village (2, 0)'
    assert m.resources[(3, 0)].name == 'Drider nest (3, 0)'
    assert m.resources[(2, 1)].name == 'Mine (2, 1)'
    assert m.resources[(1, 2)].name == 'Test portal'
