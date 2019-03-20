from rpy_code import Avatar, all_items


def test_base_stats_non_negative():
    '''Base stats should not go below zero.'''
    av = Avatar('dummy')
    for base_stat in ('base_strength', 'base_vitality', 'base_reflexes', 'base_intelligence', 'base_luck', 'base_corruption', 'base_infamy', 'base_guilt'):
        # check that starting base stats are non-negative
        assert getattr(av, base_stat) >= 0, base_stat + ' == ' + '{}'.format(getattr(av, base_stat))
        # try to set base stats to -1
        setattr(av, base_stat, -1)
        # check that base stats are still non-negative
        assert getattr(av, base_stat) >= 0, base_stat + ' == ' + '{}'.format(getattr(av, base_stat))


def test_final_stats_non_negative():
    '''Final stats should not go below zero (due to items penalties).'''
    av = Avatar('dummy')
    # set all base stats to 1
    for base_stat in ('base_strength', 'base_vitality', 'base_reflexes', 'base_intelligence', 'base_luck', 'base_corruption', 'base_infamy', 'base_guilt'):
        setattr(av, base_stat, 1)
    assert av.base_reflexes == 1
    assert av.reflexes == 1
    # check that gattsu blade has -2 to reflexes
    assert all_items['gattsu_blade'][3]['r'] == -2
    av.inventory.add_items(('gattsu_blade',))
    av.inventory.equip('gattsu_blade')
    # reflexes should be 0 instead of -1
    assert av.reflexes == 0, 'reflexes: {}'.format(av.reflexes)


def test_stats_updating():
    '''Stats should be updated when base stat was changed'''
    av = Avatar('dummy')
    for base_stat in ('base_strength', 'base_vitality', 'base_reflexes', 'base_intelligence', 'base_luck', 'base_corruption', 'base_infamy', 'base_guilt'):
        stat = base_stat[5:]
        # set all base stats to 1
        setattr(av, base_stat, 1)
        # check that all stats == 1 (no inventory or effects)
        assert getattr(av, stat) == 1, stat + ' == ' + '{}'.format(getattr(av, stat))
        # set base stats to 2
        setattr(av, base_stat, 2)
        # check that stats are updated to 2
        assert getattr(av, stat) == 2, stat + ' == ' + '{}'.format(getattr(av, stat))


def test_armour_penalties():
    '''Heavy armour items should apply penalties to some skills'''
    av = Avatar('dummy')
    av.skills['climb'] = 7
    assert av.skill('climb') == 7
    av.inventory.add('shield')
    av.inventory.equip('shield')
    assert av.skill('climb') == 6
    av.inventory.add('knights_helm')
    av.inventory.equip('knights_helm')
    assert av.skill('climb') == 4


def test_skill_with_penalty_non_negative():
    '''Skills should not drop below zero due to armour penalty'''
    av = Avatar('dummy')
    av.skills['climb'] = 1
    assert av.skill('climb') == 1
    av.inventory.add('knights_helm')
    av.inventory.equip('knights_helm')
    assert av.skill('climb') == 0
    assert av.base_skill('climb') == 1
    assert av._armour_penalty == -2


def test_gold_can_be_negative():
    '''Gold can go negative'''
    av = Avatar('dummy')
    assert av.gold == 0
    av.gold -= 10
    assert av.gold == -10, av.gold


def test_req_exp():
    '''avatar.req_exp should show amount of experience to complete current level'''
    av = Avatar('dummy')
    assert av.lvl == 1
    assert av.req_exp == 100, av.req_exp
    av.lvl = 2
    assert av.req_exp == 200, av.req_exp
    av.lvl = 3
    assert av.req_exp == 400, av.req_exp
    av.lvl = 4
    assert av.req_exp == 800, av.req_exp


def test_new_exp():
    '''avatar.new_exp should show unspent experience'''
    av = Avatar('dummy')
    assert av.lvl == 1
    assert av.new_exp == 0, av.new_exp
    av.exp += 50
    assert av.new_exp == 50, av.new_exp
    av.lvl = 2
    av.exp = 150
    assert av.new_exp == 50, av.new_exp
    av.lvl = 3
    av.exp = 370
    assert av.new_exp == 70, av.new_exp


def test_stat_mod():
    '''Test stat modifiers for various stat values'''
    av = Avatar('dummy')
    av.base_strength = 0
    assert av.stat_mod('strength') == 0, av.stat_mod('strength')
    av.base_strength = 14
    assert av.stat_mod('strength') == 2, av.stat_mod('strength')
    av.base_strength = 20
    assert av.stat_mod('strength') == 2
    av.base_reflexes = 21
    assert av.stat_mod('reflexes') == 3
    av.base_vitality = 39
    assert av.stat_mod('vitality') == 4
    # equip item with vitality +3
    av.inventory.add('knights_helm')
    av.inventory.equip('knights_helm')
    assert av.stat_mod('vitality') == 5


def test_base_mp():
    '''Avatar should have base mp == 10'''
    av = Avatar('dummy')
    assert av.base_mp == 10
    assert av.mp == 10


def test_taking_damage_increase_wounds():
    '''If avatar takes damage, that should be stored as wounds'''
    av = Avatar('dummy')
    av.heal()
    assert av.base_mp == 10
    assert av.mp == 10
    assert av.wounds == 0
    av.take_damage(3)
    assert av.wounds == 3
    assert av.base_mp == 10
    assert av.mp == 7
    av.take_damage(30)
    assert av.wounds == 10
    assert av.base_mp == 10
    assert av.mp == 0
    # check wounds after a week passed
    av.weekly()
    assert av.wounds == 10
    assert av.base_mp == 10
    assert av.mp == 0


def test_avatar_healing():
    '''Healing avatar should set wounds to zero'''
    av = Avatar('dummy')
    av.heal()
    assert av.mp == 10
    assert av.wounds == 0
    av.take_damage(1)
    assert av.mp == 9
    assert av.wounds == 1
    av.heal()
    assert av.mp == 9
    assert av.wounds == 0


def test_avatar_healing_some_wounds():
    '''If heal is called with a number, it should heal that number of wounds'''
    av = Avatar('dummy')
    av.heal()
    assert av.mp == 10
    assert av.wounds == 0
    av.take_damage(5)
    assert av.mp == 5
    assert av.wounds == 5
    av.heal(1)
    assert av.mp == 5
    assert av.wounds == 4
    av.heal(6)
    assert av.mp == 5
    assert av.wounds == 0


def test_avatar_reset_mp():
    '''New week should reset current MP to their maximum (base MP - wounds)'''
    av = Avatar('dummy')
    assert av.mp == 10
    av._mp = 4
    av._wounds = 3
    av.reset_mp()
    assert av.mp == 7

