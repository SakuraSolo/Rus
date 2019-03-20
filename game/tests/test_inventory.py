import pytest
from rpy_code import Inventory, Avatar, all_items, Item, equip_slots


def test_inventory_slots():
    '''Inventory should have slots for equippint items'''
    inventory = Inventory('dummy')
    assert set(inventory.slots.keys()) == set(equip_slots)


def test_add_item():
    inventory = Inventory('dummy')
    inventory.add('shield')
    assert Item('shield') in inventory.bp


def test_remove_item():
    inventory = Inventory('dummy')
    inventory.add('shield')
    assert Item('shield') in inventory.bp
    inventory.remove('shield')
    assert Item('shield') not in inventory.bp


def test_remove_last_item_non_equipped():
    '''Removing last non-equpped item in stack should not unequip item with similar slot'''
    av = Avatar('dummy')
    av.inventory.add('iron_dagger')
    av.inventory.add('iron_longsword')
    av.inventory.equip('iron_longsword')
    av.inventory.remove('iron_dagger')
    assert av.inventory.slots['main'] == Item('iron_longsword')


def test_equip_item():
    av = Avatar('dummy')
    av.inventory.add('shield')
    av.inventory.equip('shield')
    assert Item('shield') in av.inventory.bp
    assert av.inventory.slots[Item('shield').slot] == Item('shield')


def test_keyword_effect_two_handed():
    '''If "two-handed" item is equiped, offhand slot should be cleared and blocked.'''
    av = Avatar('dummy')
    # check that gattsu blade is two-handed
    assert "two-handed" in Item('gattsu_blade').keywords
    av.inventory.add_items(("gattsu_blade", 'shield'))
    # equip shield in off hand and check it is equipped
    av.inventory.equip('shield')
    assert av.inventory.slots['off'] == Item('shield')
    # equip gattsu blade and check that off hand is empty and blocked
    av.inventory.equip('gattsu_blade')
    assert av.inventory.slots['off'] is None
    assert av.inventory.blocked_slots == set(('off',))
    # try to equip shield to off hand and check that it is impossible
    av.inventory.equip( 'shield')
    assert av.inventory.slots['off'] is None
    #~ assert 'shield' in av.inventory.bp
    # unequip gattsu blade and now shield should be equippable
    av.inventory.clear_slot('main')
    assert 'off' not in av.inventory.blocked_slots
    av.inventory.equip('shield')
    assert av.inventory.slots['off'] == Item('shield')


def test_one_handed_replaces_two_handed():
    '''If normal weapon replaces two-handed, off slot should be unblocked.'''
    av = Avatar('dummy')
    # check that gattsu blade is two-handed
    assert "two-handed" in Item('gattsu_blade').keywords
    av.inventory.add_items(("gattsu_blade", 'shield', 'iron_sword'))
    av.inventory.equip('gattsu_blade')
    assert av.inventory.blocked_slots == set(('off',))
    av.inventory.equip('iron_sword')
    assert 'off' not in av.inventory.blocked_slots


def test_remove_two_handed():
    '''Removing eqipped two-handed weapon from inventory (last in its stack) should unequip it and remove its effects'''
    av = Avatar('dummy')
    # check that gattsu blade is two-handed
    assert "two-handed" in Item('gattsu_blade').keywords
    av.inventory.add_items(("gattsu_blade", 'gattsu_blade'))
    av.inventory.equip('gattsu_blade')
    # check that there is the effect of two-handed weapon
    assert av.inventory.blocked_slots == set(('off',))
    av.inventory.remove('gattsu_blade')
    # check that there is still the effect of two-handed weapon
    assert av.inventory.blocked_slots == set(('off',))
    av.inventory.remove('gattsu_blade')
    assert av.inventory.blocked_slots == set()


def test_move_item():
    '''Moving item between inventories should remove it from first and add to second'''
    inv1 = Inventory('dummy')
    inv2 = Inventory('dummy')
    inv1.add('iron_sword')
    inv1.move('iron_sword', inv2)
    assert Item('iron_sword') in inv2.bp
    assert Item('iron_sword') not in inv1.bp


def test_item_fields():
    '''Item should have all fields'''
    it = Item('shield')
    assert it.uid == 'shield'
    assert it.name == 'Shield'
    assert it.keywords == set(('shield', 'armour', 'non-random'))
    assert it.categories == set(('armour',))
    assert it.slot == 'off'
    assert it.descr == 'Item description'
    assert it.tier == 2
    assert it.effects == {'v': 2}
    assert it.img == 'images/items/shield.png'
    assert it.small_img == 'images/items/shield_small.png'
    assert it.buy_value == 1000000
    assert it.sell_value == 500000
    assert it.armour_penalty == -1


def test_item_without_slot():
    '''Items with category 'item' should not have target slots'''
    it = Item('garnet')
    assert it.slot == None


def test_remove_item_without_slot():
    '''Items without slot should be removed properly'''
    inventory = Inventory('dummy')
    inventory.add('garnet')
    assert Item('garnet') in inventory.bp
    inventory.remove('garnet')
    assert inventory.bp[Item('garnet')] == 0


def test_item_not_registered():
    '''Attempt to create item that is not registered in all_items should raise exception'''
    with pytest.raises(KeyError):
        it = Item('dummy')


def test_item_equality():
    '''Items are equal if their uids are same (since items are stateless)'''
    a = Item('shield')
    b = Item('shield')
    assert a == b


def test_item_hash():
    '''Item's hash is uid'''
    it = Item('shield')
    some_dict = {}
    some_dict[it] = 1
    assert Item('shield') in some_dict
