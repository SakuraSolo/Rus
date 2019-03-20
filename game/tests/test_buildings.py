import rpy_code
from rpy_code import Building, all_buildings, Barracks, Castle, Forge, Dungeon, Brothel, BreedingPit
from fixtures import all_actors


def test_building_fields():
    bld = Building('hall')
    assert bld.uid == 'hall'
    assert bld.name == 'Castle Hall'
    assert bld.lvl == 0
    assert bld.max_lvl == 0
    assert bld.income == 0
    assert bld.maintenance == 0
    assert bld.morale == 0
    assert bld.research == 0
    assert bld.capacity == 0
    assert bld.recruitment == 0
    assert bld.description == 'Castle Hall description'
    assert bld.weekly
    assert bld.can_be_built
    assert bld.req_met


def test_up_cost():
    '''up_cost should return new building price or price of upgrading to new level'''
    bld = Building('hall')
    assert bld.up_cost == all_buildings['hall']['cost']
    bld.lvl = 1
    assert bld.up_cost == all_buildings['hall']['up_cost']


def test_build():
    bld = Building('hall')
    assert bld.lvl == 0
    bld.build()
    assert bld.lvl == 1
    assert bld.income == all_buildings[bld.uid]['income']
    assert bld.maintenance == all_buildings[bld.uid]['maintenance']
    assert bld.morale == all_buildings[bld.uid]['morale']
    assert bld.research == all_buildings[bld.uid]['research']
    assert bld.capacity == all_buildings[bld.uid]['capacity']
    assert bld.recruitment == all_buildings[bld.uid]['recruitment']
    bld.build()
    bld.build()
    assert bld.lvl == 3
    assert bld.income == all_buildings[bld.uid]['income'] + 2 * all_buildings[bld.uid]['up_income']
    assert bld.maintenance == all_buildings[bld.uid]['maintenance'] + 2 * all_buildings[bld.uid]['up_maintenance']
    assert bld.morale == all_buildings[bld.uid]['morale'] + 2 * all_buildings[bld.uid]['up_morale']
    assert bld.research == all_buildings[bld.uid]['research'] + 2 * all_buildings[bld.uid]['up_research']
    assert bld.capacity == all_buildings[bld.uid]['capacity'] + 2 * all_buildings[bld.uid]['up_capacity']
    assert bld.recruitment == all_buildings[bld.uid]['recruitment'] + 2 * all_buildings[bld.uid]['up_recruitment']


def test_custom_buildings():
    '''Some buildings should be created with custom classes'''
    bld = Barracks('barracks')
    assert isinstance(bld, Building)
    assert bld.troops == 0
    assert bld.troop_type == 'orc'


def test_barracks_weekly_recruitment(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    bld = Barracks('barracks')
    bld.build()
    assert bld.troops == 0
    bld.weekly()
    assert bld.troops == bld.recruitment
    bld.weekly()
    assert bld.troops == bld.recruitment * 2


def test_max_troops_on_weekly_update(monkeypatch):
    '''Number of troops should not go beyound current capacity on recruitment'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    bld = Barracks('barracks')
    bld.build()
    bld.capacity = 10
    bld.recruitment = 3
    bld.troops = 9
    bld.weekly()
    assert bld.troops == 10


def test_max_troops_at_capacity():
    bld = Barracks('barracks')
    bld.build()
    bld.capacity = 10
    bld.troops = 14
    assert bld.troops == 10
    bld.troops = -3
    assert bld.troops == 0
    bld.troops += 8
    assert bld.troops == 8


def test_max_prisoners_at_dungeon():
    bld = Dungeon('dungeon')
    bld.build()
    bld.capacity = 10
    bld.prisoners = 14
    assert bld.prisoners == 10
    bld.prisoners = -3
    assert bld.prisoners == 0
    bld.prisoners += 8
    assert bld.prisoners == 8


def test_can_be_built(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    assert not castle.buildings['tavern'].can_be_built()
    castle.treasury = 500
    castle.buildings['tavern'].max_lvl = 1
    assert castle.buildings['tavern'].can_be_built()
    castle.scheduled_upgrades.append('tavern')
    assert not castle.buildings['tavern'].can_be_built()


def test_only_one_upgrade_in_week(monkeypatch):
    '''Only one upgrade can be built in one week'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    assert not castle.buildings['kennel'].can_be_built()
    castle.treasury = 500
    castle.buildings['kennel'].max_lvl = 1
    assert castle.buildings['kennel'].can_be_built()
    # any scheduled upgrade should block other upgrades
    castle.scheduled_upgrades.append('sanctum')
    assert not castle.buildings['kennel'].can_be_built()
    # same upgrade should not be built twice a week
    castle.scheduled_upgrades = []
    assert castle.buildings['kennel'].can_be_built()
    castle.scheduled_upgrades.append('kennel')
    assert not castle.buildings['kennel'].can_be_built()


def test_max_troops_at_capacity_dark_sanctum(monkeypatch):
    '''Number of troops should not go beyound current capacity'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    bld = Barracks('sanctum')
    bld.build()
    bld.capacity = 10
    bld.recruitment = 3
    bld.troops = 9
    bld.weekly()
    assert bld.troops == 10


def test_magic_building_requirements(monkeypatch):
    '''Magic buildings require free library capacity'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    assert not castle.buildings['summoning'].req_met()
    castle.treasury = 500
    castle.buildings['summoning'].max_lvl = 1
    assert not castle.buildings['summoning'].can_be_built()
    castle.buildings['library'].build()
    assert castle.buildings['summoning'].req_met()
    assert castle.buildings['summoning'].can_be_built()


def test_forge_make_equipment(monkeypatch):
    '''Forge should turn iron to equipment (capacity amount)'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    castle._iron = 12
    bld = Forge('forge')
    bld.build()
    bld.weekly()
    assert castle._equipment == 5
    assert castle._iron == 7


def test_brothel_spies():
    '''Brothel should have spies'''
    bld = Brothel('brothel')
    assert bld.spies == []


def test_castle_spies_property(monkeypatch):
    '''castle.spies property should provide access to Brothel\'s spies'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    assert castle.spies is castle.buildings['brothel'].spies


def test_brothel_generates_spies(monkeypatch):
    '''Brothel should generate spies each week'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    all_objects = {}
    monkeypatch.setattr(rpy_code, 'all_objects', all_objects, raising=False)
    bld = Brothel('brothel')
    bld.build()
    assert bld.spies == []
    assert len(bld.available_spies) == 2
    bld.weekly()
    assert len(bld.spies) == 0
    assert len(bld.available_spies) == 2
    # check that old "available_spies" deleted when new ones are generated
    bld.weekly()
    assert len(bld.spies) == 0
    assert len(bld.available_spies) == 2


def test_dungeon_auto_sell_prisoners(monkeypatch):
    '''Dungeon.weekly should be able to auto sell prisoners'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    bld = Dungeon('dungeon')
    # add many prisoners and set all "auto sell" options
    bld.capacity = 30
    bld.prisoners = 30
    assert bld.prisoners == 30
    bld.prisoners_auto = {
        'slave': True,
        'ransom': True,
        'gladiator': True,
        'test': True}
    # imitate that 1 prisoner was sold in every category during week
    bld.prisoners_status = {
        'slave': [1, 10],
        'ransom': [1, 3],
        'gladiator': [1, 3],
        'test': [1, 5]}
    assert castle.treasury == 0
    assert castle.morale == 0
    assert castle.rp == 0
    bld.weekly()
    # prisoners status should be reset
    assert bld.prisoners_status == {
        'slave': [0, 10],
        'ransom': [0, 3],
        'gladiator': [0, 3],
        'test': [0, 5]}
    assert bld.prisoners == 13
    assert castle.treasury == 9*5 + 2*10
    assert castle.morale == 2*3
    assert castle.rp == 4*2


def test_dungeon_auto_sell_priorities(monkeypatch):
    '''Test to check priorities of auto selling'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    bld = Dungeon('dungeon')
    # add some prisoners (not enough for all options) and set all "auto sell" options
    bld.capacity = 30
    bld.prisoners = 5
    bld.prisoners_auto = {
        'slave': True,
        'ransom': True,
        'gladiator': True,
        'test': True}
    assert castle.treasury == 0
    assert castle.morale == 0
    assert castle.rp == 0
    bld.weekly()
    assert bld.prisoners == 0
    assert castle.treasury == 2*10
    assert castle.morale == 3*3
    assert castle.rp == 0


def test_dungeon_auto_sell_priorities2(monkeypatch):
    '''Test 2 to check priorities of auto selling'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    bld = Dungeon('dungeon')
    # add some prisoners (not enough for all options) and set all "auto sell" options
    bld.capacity = 30
    bld.prisoners = 16
    bld.prisoners_auto = {
        'slave': True,
        'ransom': True,
        'gladiator': True,
        'test': True}
    assert castle.treasury == 0
    assert castle.morale == 0
    assert castle.rp == 0
    bld.weekly()
    assert bld.prisoners == 0
    assert castle.treasury == 3*10 + 5*5
    assert castle.morale == 3*3
    assert castle.rp == 5*2


def test_breeding_pit_free_space(all_actors):
    bld = BreedingPit('pit')
    bld.build()
    assert bld.capacity == 8
    assert bld.free_space == 8


def test_breeding_pit_drider_recruitment(all_actors):
    bld = BreedingPit('pit')
    bld.build()
    bld.drider_recruitment = 0.5
    assert bld.driders == 0
    assert bld.capacity == 8
    assert bld.free_space == 8
    bld.weekly()
    # don't report halfs of driders
    assert bld.driders == 0
    assert bld.capacity == 8
    assert bld.free_space == 8
    bld.weekly()
    assert bld.driders == 1
    assert bld.capacity == 8
    assert bld.free_space == 7


def test_breeding_pit_monsters(all_actors):
    bld = BreedingPit('pit')
    bld.build()
    bld._driders = 3.5
    assert bld.driders == 3
    assert bld._driders == 3.5
    assert bld.capacity == 8
    assert bld.free_space == 5
    assert bld.monsters == 3
