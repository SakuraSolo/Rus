import rpy_code
from rpy_code import Upgrade, Upgrades, all_upgrades, Castle


def test_upgrade_fields():
    up = Upgrade('tavern', None)
    assert up.name == 'Tavern'
    assert up.rp_cost == 25
    assert up.gold_cost == 500
    assert up.descr == 'Opens location. Small increases to morale and economy.'
    assert up.state == 'locked'
    assert up.open_room == 'tavern'
    assert up.on_build == None


def test_all_upgrades():
    '''Upgrades should contain all possible upgrades from all_upgrades'''
    ups = Upgrades('dummy')
    assert len(ups) == len(all_upgrades)
    for up in ups:
        assert type(up) == Upgrade


#~ def test_upgrade_states(monkeypatch):
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ ups = Upgrades('dummy')
    #~ assert ups['barracks_exp'].locked
    #~ ups.unlock('barracks_exp')
    #~ assert ups['barracks_exp'].unlocked
    #~ ups.build('barracks_exp')
    #~ assert ups['barracks_exp'].built


#~ def test_unlock_safety(monkeypatch):
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ ups = Upgrades('dummy')
    #~ assert ups['barracks_exp'].locked
    #~ # multiple unlock() should be safe
    #~ ups.unlock('barracks_exp')
    #~ ups.unlock('barracks_exp')
    #~ assert ups['barracks_exp'].unlocked
    #~ ups.build('barracks_exp')
    #~ assert ups['barracks_exp'].built
    #~ # unlocking already built upgrade should be safe (should not reset 'built' state)
    #~ ups.unlock('barracks_exp')
    #~ assert ups['barracks_exp'].built


#~ def test_room_access_on_upgrade():
    #~ castle = Castle(starting_rooms)
    #~ assert castle.rooms_access['tavern'] == False
    #~ castle.upgrades.build('tavern')
    #~ assert castle.rooms_access['tavern'] == True


#~ def test_on_build_action(monkeypatch):
    #~ '''Each upgrade should support "on_build" action'''
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ start_dp = castle.dp
    #~ castle.upgrades.build('walls')
    #~ assert castle.dp == start_dp + 50


#~ def test_upgrades_state_counts(monkeypatch):
    #~ '''Upgrades should provide counts for all, unlocked and built upgrades'''
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ ups = castle.upgrades
    #~ ups['barracks_exp'].unlock()
    #~ ups['granary'].unlock()
    #~ ups['walls'].build()
    #~ assert len(ups) == len(all_upgrades)
    #~ assert ups.unlocked_count == 3
    #~ assert ups.built_count == 1

