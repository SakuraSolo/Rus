from rpy_code import convert_json_to_mapdef, create_blank_map, map_add_fixed_hexes, map_add_randomized_terrain, map_randomize_tile_images, map_add_random_resources, map_copy_properties


json_map_fixture = '''{ "height":10,
 "hexsidelength":0,
 "layers":[
        {
         "data":[906, 906, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 906, 906, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 906, 906, 0, 1, 0, 0, 2, 1, 0, 0, 0, 2, 906, 1, 1, 0, 1, 0, 0, 2, 2, 1, 1, 1, 906, 906, 0, 0, 0, 0, 1, 1, 1, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 1, 0, 0, 1, 3, 0, 0, 0, 5, 0, 0, 0, 0, 1, 3, 0, 0, 0, 1, 0, 0, 0, 0, 1, 3, 3, 0, 0, 0],
         "height":10,
         "name":"terrain",
         "opacity":1,
         "type":"tilelayer",
         "visible":true,
         "width":10,
         "x":0,
         "y":0
        },
        {
         "data":[0, 0, 0, 0, 920, 0, 0, 0, 0, 936, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 920, 0, 930, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 929, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 933, 0, 0, 919, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 920, 0, 0, 0, 0, 0, 923, 0, 0, 0, 0],
         "height":10,
         "name":"resources",
         "opacity":1,
         "type":"tilelayer",
         "visible":true,
         "width":10,
         "x":0,
         "y":0
        }],
 "nextobjectid":1,
 "orientation":"hexagonal",
 "properties":
    {
     "name":"Small test map",
     "portals":"[[4, 7, 'Central portal']]",
     "resources":"[[3, 2], [6, 2]]",
     "start_pos":"[4, 5]",
     "terrains":"[[0, 10, 3, 5],[1, 10, 2, 6], [2, 5, 1, 2],]",
     "uid":"test_json_map"
    },
 "propertytypes":
    {
     "name":"string",
     "portals":"string",
     "resources":"string",
     "start_pos":"string",
     "terrains":"string",
     "uid":"string"
    },
 "renderorder":"right-down",
 "staggeraxis":"x",
 "staggerindex":"odd",
 "tileheight":170,
 "tilesets":[
        {
         "firstgid":1,
         "source":"soc terrain\/soc_terrain.tsx"
        },
        {
         "firstgid":917,
         "source":"soc resources\/soc_resources.tsx"
        }],
 "tilewidth":294,
 "type":"map",
 "version":"1.0.0",
 "width":10
}'''


def test_json_to_mapdef():
    mapdef = convert_json_to_mapdef(json_map_fixture)
    assert mapdef['uid'] == 'test_json_map'
    assert mapdef['name'] == 'Small test map'
    assert mapdef['width'] == 10
    assert mapdef['height'] == 10
    assert mapdef['start_pos'] == [4, 5]
    assert mapdef['terrains'] == [[0, 10, 3, 5], [1, 10, 2, 6], [2, 5, 1, 2],]
    assert mapdef['resources'] == [[3, 2], [6, 2]]
    assert len(mapdef['fixed']) == 39
    assert mapdef['default'] == 0
    assert mapdef['portals'] == [[4, 7, 'Central portal']]


def test_create_blank_map():
    '''Blank map should have all hex links correctly set'''
    m = create_blank_map(5, 5)
    assert len(m.hexes) == 25
    # check some hexes for correct links (including boundaries)
    assert m.hexes[0][2] == [-1, -1, 1, 5, -1, -1]
    assert m.hexes[m._id_from_coord((0, 4))][2] == [m._id_from_coord((0, 3)), m._id_from_coord((1, 3)), m._id_from_coord((1, 4)), -1, -1, -1]
    assert m.hexes[m._id_from_coord((2, 2))][2] == [m._id_from_coord((2, 1)), m._id_from_coord((3, 1)), m._id_from_coord((3, 2)), m._id_from_coord((2, 3)),
        m._id_from_coord((1, 2)), m._id_from_coord((1, 1))]
    # check that coordinates are correct
    assert tuple(m.hexes[0][1]) == (0, 0)
    assert tuple(m.hexes[24][1]) == (4, 4)
    # check all hexes have undefined terrain
    assert len([hex for hex in m.hexes if hex[3] == -1]) == 25


def test_map_copy_properties():
    mapdef = convert_json_to_mapdef(json_map_fixture)
    m = create_blank_map(mapdef['width'], mapdef['height'])
    map_copy_properties(m, mapdef)
    assert m.uid == 'test_json_map'
    assert m.name == 'Small test map'
    # check starting position loaded
    assert m.pos == [4, 5]
    assert m.previous_pos == [4, 5]
    assert m.portals == {(4, 7): 'Central portal'}


def test_add_fixed_hexes():
    mapdef = convert_json_to_mapdef(json_map_fixture)
    m = create_blank_map(mapdef['width'], mapdef['height'])
    assert m.hexes[0][3] == -1
    map_add_fixed_hexes(m, mapdef)
    assert len([hex for hex in m.hexes if hex[3] >= 0]) == len(mapdef['fixed'])
    assert m.hexes[0][3] == 905
    assert m.hexes[m._id_from_coord((5, 9))][3] == 2
    # check fixed resources ( (coords, resource id) for each resource so they will be visible in error report)
    assert len([(hex[1], hex[6]) for hex in m.hexes if hex[6] >= 1]) == 9
    assert m.hexes[m._id_from_coord((4, 0))][6] == 3


def test_add_randomized_terrain():
    mapdef = convert_json_to_mapdef(json_map_fixture)
    m = create_blank_map(mapdef['width'], mapdef['height'])
    map_add_fixed_hexes(m, mapdef)
    # check that there are unassigned hexes
    assert len([hex for hex in m.hexes if hex[3] == -1]) > 0
    map_add_randomized_terrain(m, mapdef)
    # check that all hexes have some terrain assigned
    assert len([hex for hex in m.hexes if hex[3] == -1]) == 0


def test_map_randomize_tile_images():
    mapdef = convert_json_to_mapdef(json_map_fixture)
    m = create_blank_map(mapdef['width'], mapdef['height'])
    assert len([hex for hex in m.hexes if hex[10] == -1]) >= 0
    map_add_randomized_terrain(m, mapdef)
    map_randomize_tile_images(m, mapdef)
    assert len([hex for hex in m.hexes if hex[10] == -1]) == 0


def test_add_random_resources():
    mapdef = convert_json_to_mapdef(json_map_fixture)
    m = create_blank_map(mapdef['width'], mapdef['height'])
    map_add_fixed_hexes(m, mapdef)
    # there are 9 fixed resources on test map
    assert len([(hex[1], hex[6]) for hex in m.hexes if hex[6] >= 1]) == 9
    map_add_random_resources(m, mapdef)
    assert 9 < len([(hex[1], hex[6]) for hex in m.hexes if hex[6] >= 1]) <= 13
