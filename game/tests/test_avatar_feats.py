from rpy_code import Avatar


def test_add_feat_repeat_safety():
    '''Adding feat several times should be safe'''
    av = Avatar('dummy')
    assert av.base_skill('move_silently') == 0
    assert av.base_skill('hide') == 0
    av.add_feat('stealthy')
    assert av.base_skill('move_silently') == 1
    assert av.base_skill('hide') == 1
    av.add_feat('stealthy')
    assert av.base_skill('move_silently') == 1
    assert av.base_skill('hide') == 1


def test_add_feat_not_registered():
    '''Adding not registered feat should fail silently'''
    av = Avatar('dummy')
    assert 'dummy' not in av.feats
    av.add_feat('dummy')
    assert 'dummy' not in av.feats


def test_feat_mp_stats_effect():
    '''Feat effect for stats and mp should not be mixed with skills bonuses'''
    av = Avatar('dummy')
    av.add_feat('luck')
    # check that luck ("l") is not listed in skills
    assert 'l' not in av.skills


def test_feat_bonus_to_base_stat():
    '''Feat bonus should be added to base stat'''
    av = Avatar('dummy')
    assert av.base_luck == 1, av.base_luck
    assert av.luck == 1, av.luck
    av.add_feat('luck')
    assert av.base_luck == 3, av.base_luck
    assert av.luck == 3, av.luck


def test_feat_bonus_to_base_skill():
    '''Feat bonus should be added to base skill'''
    av = Avatar('dummy')
    assert av.base_skill('deceive') == 0
    assert av.skill('deceive') == 0
    av.add_feat('liar')
    assert av.base_skill('deceive') == 2
    assert av.skill('deceive') == 2


# disabled until feats with MP bonus
#~ def test_feat_bonus_to_base_mp():
    #~ '''Feat bonus should be added to base mp'''
    #~ av = Avatar('dummy')
    #~ assert av.base_mp == 2, av.base_mp
    #~ av.add_feat('toughness')
    #~ assert av.base_mp == 5, av.base_mp

