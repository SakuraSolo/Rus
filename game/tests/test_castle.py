import rpy_code
from rpy_code import Castle, all_buildings, Building, Barracks, Research, all_researches, Avatar
from fixtures import castle, avatar, all_actors


def test_morale_range():
    '''Morale should not go out of range.'''
    castle = Castle()
    castle.morale = 0
    assert castle.morale == 0, 'morale == {}'.format(castle.morale)
    castle.morale = -1
    assert castle.morale == 0, 'morale == {}'.format(castle.morale)
    castle.morale = 100
    assert castle.morale == 100, 'morale == {}'.format(castle.morale)
    castle.morale = 101
    assert castle.morale == 100, 'morale == {}'.format(castle.morale)


def test_morale_texts():
    '''Morale text should reflect morale number'''
    castle = Castle()
    castle.morale = 0
    assert castle.morale_text == 'Terrible', 'morale == {}, morale_text == {}'.format(castle.morale, castle.morale_text)
    castle.morale = 20
    assert castle.morale_text == 'Terrible', 'morale == {}, morale_text == {}'.format(castle.morale, castle.morale_text)
    castle.morale = 40
    assert castle.morale_text == 'Poor', 'morale == {}, morale_text == {}'.format(castle.morale, castle.morale_text)
    castle.morale = 60
    assert castle.morale_text == 'Normal', 'morale == {}, morale_text == {}'.format(castle.morale, castle.morale_text)
    castle.morale = 80
    assert castle.morale_text == 'Good', 'morale == {}, morale_text == {}'.format(castle.morale, castle.morale_text)
    castle.morale = 100
    assert castle.morale_text == 'Great', 'morale == {}, morale_text == {}'.format(castle.morale, castle.morale_text)


def test_starting_resources():
    '''Resources at new castle (without buildings)'''
    castle = Castle()
    assert castle.treasury == 0
    assert castle.morale == 0
    assert castle.military == 0
    assert castle.tech == 0
    assert castle.rp == 0
    assert castle.current_research is None


def test_buildings():
    castle = Castle()
    assert len(castle.buildings) == len(all_buildings)


def test_visitable():
    castle = Castle()
    assert not castle.visitable('library')
    castle.buildings['library'].build()
    assert castle.visitable('library')
    assert castle.visitable('rowans_chambers')
    assert castle.visitable('portal_room')


def test_custom_buildings():
    '''Some buildings should be created with special classes'''
    castle = Castle()
    assert isinstance(castle.buildings['barracks'], Building)
    assert isinstance(castle.buildings['barracks'], Barracks)


def test_end_week_updates_morale(castle, avatar):
    '''End_week should update the state of the castle for new week'''
    castle.morale = 50
    castle.buildings['hall'].build()
    castle.end_week()
    # only Castle Hall changes morale for now
    assert castle.morale == 50 + 23


def test_end_week_updates_iron(castle, avatar):
    '''iron should be produced at iron_per_week rate, unused iron should be sold'''
    castle.iron_per_week = 11
    assert castle._iron == 0
    assert castle.treasury == 0
    castle.end_week()
    assert castle._iron == 0
    # avatar salary - 5 gold
    assert castle.treasury == 6


def test_end_week_sells_equipment(castle, avatar):
    '''unsused equipment should be sold at end of week'''
    castle._equipment = 12
    assert castle.treasury == 0
    castle.end_week()
    assert castle._equipment == 0
    # avatar salary - 5 gold
    assert castle.treasury == 55


def test_tech_reseted_each_week(castle, avatar):
    castle.tech = 10
    castle.rp = 10
    castle.end_week()
    # there are no buildings built, so tech should be 0
    assert castle.tech == 0
    assert castle.rp == 0


def test_end_week_updates_military(castle, avatar):
    castle.military = 0
    assert castle.military == 0
    castle.end_week()
    assert castle.military == 0
    castle.buildings['barracks'].build()
    castle.end_week()
    assert castle.buildings['barracks'].troops == 2
    assert castle.military == 10


def test_end_week_troops_morale_and_costs(castle, avatar):
    '''Various troops should change morale and treasury'''
    castle.morale = 50
    castle.treasury = 100
    castle.buildings['barracks'].build()
    castle.end_week()
    # 50 - 2 * 0.1
    assert castle.morale == 49.8
    # 100 - avatar salary - soldiers salary
    assert castle.treasury == 93


def test_end_week_troops_research(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    assert castle.tech == 0
    castle.buildings['sanctum'].build()
    castle.buildings['sanctum'].troops = 3
    #~ castle.end_week()
    castle._update_troops()
    castle._spend_research_points()
    assert castle.tech == 1.5
    assert castle.rp == 1.5


def test_end_week_builds_scheduled_upgrades(castle, avatar):
    assert castle.scheduled_upgrades == []
    castle.scheduled_upgrades = ['tavern']
    castle.end_week()
    assert castle.scheduled_upgrades == []
    assert castle.buildings['tavern'].lvl == 1


def test_end_week_spend_rp(castle, avatar, mocker):
    '''end_week should spend generated research points to current research'''
    castle.set_research('military_recreation')
    castle.buildings['library'].build()
    castle.end_week()
    assert castle.researches['military_recreation'].rp_spent == 10
    assert castle.rp == 0
    # complete research
    on_complete_mock = mocker.patch.object(castle.current_research, 'on_complete')
    castle.researches['military_recreation'].rp_spent = 97
    #~ castle.end_week()
    castle._spend_research_points()
    assert castle.researches['military_recreation'].rp_spent == 100
    assert castle.researches['military_recreation'].completed
    assert castle.current_research is None
    assert castle.rp == 7
    assert on_complete_mock.called
    # check that completed research is added to completed_researches
    assert castle.completed_researches == ['military_recreation']
    castle.end_week()
    # completed researches should be cleared by "Research report" events, not by castle.end_week
    assert castle.completed_researches == ['military_recreation']


def test_loading_researches():
    castle = Castle()
    assert len(castle.researches) == len(all_researches)
    for rs in castle.researches.values():
        assert isinstance(rs, Research)


def test_set_research():
    castle = Castle()
    castle.set_research('military_tactics')
    assert castle.current_research == castle.researches['military_tactics']


def test_completed_upgrades(castle, avatar):
    '''When scheduled upgrade is built, it should be added to list of completed upgrades'''
    castle.scheduled_upgrades.append('barracks')
    castle.end_week()
    assert castle.scheduled_upgrades == []
    assert castle.completed_upgrades == ['barracks1']
    # completed_upgrades should be cleared next week
    castle.end_week()
    assert castle.completed_upgrades == []
    # check that the building level is added correctly
    castle.scheduled_upgrades.append('barracks')
    castle.end_week()
    assert castle.completed_upgrades == ['barracks2']


def test_distribute_equipment():
    '''Equipment should be distributed between barracks, with priority'''
    castle = Castle()
    castle._equipment = 20
    castle.buildings['barracks'].capacity = 20
    castle.buildings['barracks'].troops = 11
    castle.buildings['sanctum'].capacity = 20
    castle.buildings['sanctum'].troops = 7
    castle._distribute_equipment()
    assert castle._equipment == 9
    assert castle.buildings['barracks'].equipment == 11


# TODO: maybe this should go to level of troops or buildings (barracks)
def test_equipment_adds_to_strengh():
    '''Equipment should add strength to troops'''
    castle = Castle()
    castle.buildings['barracks'].capacity = 15
    castle.buildings['barracks'].troops = 11
    castle._update_troops()
    assert castle.military == 55
    castle.buildings['barracks'].equipment = 8
    castle._update_troops()
    assert castle.military == 95


def test_cubis_add_bonus_to_military():
    '''Cubis (dark sanctum) should add 5% bonus to whole army'''
    castle = Castle()
    castle.buildings['barracks'].capacity = 8
    castle.buildings['barracks'].troops = 8
    castle._update_troops()
    assert castle.military == 40
    castle.buildings['sanctum'].capacity = 3
    castle.buildings['sanctum'].troops = 3
    castle._update_troops()
    assert castle.military == 70 * 1.15


def test_update_military_power(all_actors):
    castle = Castle()
    castle.buildings['barracks'].capacity = 8
    castle.buildings['barracks'].troops = 6
    castle._update_military_power()
    assert castle.military == 30
    castle.buildings['sanctum'].capacity = 3
    castle.buildings['sanctum'].troops = 2
    castle._update_military_power()
    assert castle.military == 50 * 1.1
    castle.buildings['pit'].capacity = 3
    castle.buildings['pit']._driders = 3.5
    castle._update_military_power()
    assert castle.buildings['pit'].driders == 3
    assert castle.military == 50 * 1.1 + 50 * 3


def test_recruitment_bonuses(monkeypatch):
    '''Buildings should add recruitment bonuses from world resources'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    castle.buildings['barracks'].capacity = 15
    castle.buildings['barracks'].troops = 3
    castle.buildings['barracks'].recruitment = 2
    castle._update_buildings()
    assert castle.buildings['barracks'].troops == 5
    castle.recruitment_bonuses['barracks'] = 3
    castle._update_buildings()
    assert castle.buildings['barracks'].troops == 10
    # recruitment bonus should not add troops above capacity
    castle.recruitment_bonuses['barracks'] = 10
    castle._update_buildings()
    assert castle.buildings['barracks'].troops == 15


def test_research_bonus(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    castle._update_buildings()
    assert castle.tech == 0
    castle.research_bonus = 3
    castle._update_buildings()
    assert castle.tech == 3


def test_avatar_weekly_salary(castle, avatar):
    castle.treasury = 100
    assert avatar.gold == 0
    assert castle.treasury == 100
    castle.end_week()
    assert avatar.gold == 5
    assert castle.treasury == 95
    # check salary while insufficient treasury
    castle.treasury = 3
    avatar.gold = 0
    castle.end_week()
    assert avatar.gold == 3
    assert castle.treasury == 0


def test_surface_maintenance_reduction(castle, avatar):
    '''Maintenance reduction (weekly) should reduce maintenance cost of surface buildings'''
    # TODO: apply discount only to surface buildings
    castle = Castle()
    castle.buildings['library'].build()
    castle.buildings['kennel'].build()
    castle.buildings['arena'].build()
    castle.buildings['summoning'].build()
    castle.treasury = 100
    assert castle.surface_maintenance_reduction == 0
    castle.end_week()
    assert castle.treasury == 67.5
    assert castle.surface_maintenance_reduction == 0
    # apply discount
    castle = Castle()
    castle.buildings['library'].build()
    castle.buildings['kennel'].build()
    castle.buildings['arena'].build()
    castle.buildings['summoning'].build()
    castle.treasury = 100
    castle.surface_maintenance_reduction = 25
    castle.end_week()
    assert castle.treasury == 75.7
    assert castle.surface_maintenance_reduction == 0

