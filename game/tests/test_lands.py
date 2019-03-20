from rpy_code import Lands, Realm, Location


# fixture for testing (in format like all_realms and all_locs)
fixt_realms = {'realm1': {'name': 'Realm1', 'locs': ('loc1',)}, 'realm2': {'name': 'Realm2', 'locs': ('loc2', 'loc3')}}
fixt_locs = {'loc1': {'name': 'Loc1'}, 'loc2': {'name': 'Loc2'}, 'loc3': {'name': 'Loc3'}}


def test_all_areas_added():
    lands = Lands(fixt_realms, fixt_locs)
    assert len(lands.realms) == 2


def test_lands_iteration():
    '''simply check if lands is iterable and return realms on iteration'''
    lands = Lands(fixt_realms, fixt_locs)
    for realm in lands:
        assert type(realm) == Realm
        # check that all realms is accessible by default
        assert realm.accessible == True


def test_no_descripton_realm():
    '''Default description for a realm that has not one'''
    realm = Realm('uid', 'dummy', ())
    assert realm.descr == 'No description'


def test_lands_return_realm():
    '''lands[uid] should return realm'''
    lands = Lands(fixt_realms, fixt_locs)
    assert lands['realm1'].name == 'Realm1'


def test_realm_have_locations():
    '''Created realms should contain locations'''
    # create realms with all locations in fixt_locs
    realm = Realm('uid', 'dummy', fixt_locs)
    for loc in fixt_locs:
        assert loc in realm
        assert type(realm[loc]) == Location
        # check that new locations are invisible and inaccessible
        assert realm[loc].accessible == False
        assert realm[loc].visible == False


def test_location_defaults():
    '''location should provide uid, name and default description'''
    loc = Location('uid', 'dummy')
    assert loc.descr == 'No description'
    assert loc.uid == 'uid'
    assert loc.name == 'dummy'
