from rpy_code import RaidState
from fixtures import castle


def test_fields():
    rs = RaidState()
    assert rs.in_raid is False
    assert rs.troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    assert rs.equipment == {'orc': 0}


def test_available_troops(castle):
    rs = RaidState()
    assert rs.available_troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    castle.buildings['barracks'].build()
    castle.buildings['barracks'].troops = 10
    assert castle.buildings['barracks'].troops == 10
    castle.buildings['pit'].build()
    castle.buildings['pit']._driders = 10
    assert castle.buildings['pit'].driders == 10
    assert rs.available_troops == {'orc': 10, 'cubi': 0, 'drider': 10}


def test_change_troops(castle):
    '''change_troops should change number of given troops in raid (in available range)'''
    rs = RaidState()
    assert rs.available_troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    castle.buildings['barracks'].build()
    castle.buildings['barracks'].troops = 10
    assert rs.troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    rs.change_troops('orc', 2)
    assert rs.troops == {'orc': 2, 'cubi': 0, 'drider': 0}
    rs.change_troops('orc', 15)
    assert rs.troops == {'orc': 10, 'cubi': 0, 'drider': 0}
    rs.change_troops('orc', -3)
    assert rs.troops == {'orc': 7, 'cubi': 0, 'drider': 0}
    rs.change_troops('orc', -13)
    assert rs.troops == {'orc': 0, 'cubi': 0, 'drider': 0}


def test_auto_equip(castle):
    '''Changing number of orcs should change their equipment also (auto-equip)'''
    rs = RaidState()
    castle.buildings['barracks'].build()
    castle.buildings['barracks'].troops = 10
    castle.buildings['barracks'].equipment = 5
    assert rs.available_troops == {'orc': 10, 'cubi': 0, 'drider': 0}
    assert rs.available_equipment == {'orc': 5}
    assert rs.troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    assert rs.equipment == {'orc': 0}
    rs.change_troops('orc', 5)
    assert rs.troops == {'orc': 5, 'cubi': 0, 'drider': 0}
    assert rs.equipment == {'orc': 5}
    rs.change_troops('orc', 5)
    assert rs.troops == {'orc': 10, 'cubi': 0, 'drider': 0}
    assert rs.equipment == {'orc': 5}
    rs.change_troops('orc', -7)
    assert rs.troops == {'orc': 3, 'cubi': 0, 'drider': 0}
    assert rs.equipment == {'orc': 3}
    castle.buildings['sanctum'].build()
    castle.buildings['sanctum'].troops = 1
    rs.change_troops('cubi', 1)
    assert rs.troops == {'orc': 3, 'cubi': 1, 'drider': 0}
    assert rs.equipment == {'orc': 3}


def test_raid_mp():
    rs = RaidState()
    assert rs.mp == 0
    rs._troops = {'orc': 4, 'cubi': 0, 'drider': 0}
    assert rs.mp == 20
    rs._troops = {'orc': 4, 'cubi': 2, 'drider': 0}
    assert rs.mp == (4 * 5 + 2 * 10 ) * 1.1
    rs._troops = {'orc': 4, 'cubi': 3, 'drider': 4}
    assert rs.mp == (4 * 5 + 3 * 10) * 1.15 + 4 * 50
    # add equipment
    rs._equipment = {'orc': 3}
    assert rs.mp == (4 * 5 + 3 * 10) * 1.15 + 3 * 5 + 4 * 50


def test_raid_reset():
    rs = RaidState()
    rs._troops = {'orc': 4, 'cubi': 3, 'drider': 4}
    rs.in_raid = True
    assert rs.troops == {'orc': 4, 'cubi': 3, 'drider': 4}
    assert rs.in_raid
    rs.reset()
    assert rs.troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    assert not rs.in_raid


def test_finish(castle):
    rs = RaidState()
    castle.buildings['barracks'].build()
    castle.buildings['barracks'].troops = 10
    castle.buildings['barracks'].equipment = 3
    castle.buildings['pit'].build()
    castle.buildings['pit']._driders = 3.5
    castle.buildings['sanctum'].build()
    castle.buildings['sanctum'].troops = 2
    rs.change_troops('orc', 5)
    rs.change_troops('drider', 2)
    rs.change_troops('cubi', 1)
    assert rs.troops == {'orc': 5, 'cubi': 1, 'drider': 2}
    assert rs.equipment == {'orc': 3}
    rs.finish()
    assert rs.troops == {'orc': 0, 'cubi': 0, 'drider': 0}
    assert rs.equipment == {'orc': 0}
    assert castle.buildings['barracks'].troops == 5
    assert castle.buildings['barracks'].equipment == 0
    assert castle.buildings['pit'].driders == 1
    assert castle.buildings['pit']._driders == 1.5
    assert castle.buildings['sanctum'].troops == 1
    assert not rs.in_raid

