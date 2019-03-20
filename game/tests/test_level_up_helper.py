from rpy_code import Avatar, LevelUpHelper


def test_level_up_points():
    lvlup = LevelUpHelper()
    assert lvlup.stat_points == 3, lvlup.stat_points
    assert lvlup.skill_points == 5, lvlup.skill_points


def test_change_stat():
    '''change_stat should add point to stat_changes and reduce free points'''
    lvlup = LevelUpHelper()
    assert lvlup.stat_points == 3, lvlup.stat_points
    lvlup.change_stat('strength', 1)
    assert lvlup.stat_points == 2, lvlup.stat_points
    assert lvlup.stat_change('strength') == 1


def test_change_skill():
    '''change_skill should add point to skill_changes and reduce free points'''
    lvlup = LevelUpHelper()
    assert lvlup.skill_points == 5, lvlup.skill_points
    lvlup.change_skill('escape', 1)
    assert lvlup.skill_points == 4, lvlup.skill_points
    assert lvlup.skill_change('escape') == 1


def test_stat_change_possible():
    lvlup = LevelUpHelper()
    lvlup.stat_points = 2
    assert lvlup.stat_change_possible('reflexes', 1)
    assert lvlup.stat_change_possible('reflexes', 2)
    lvlup.stat_points = 0
    assert not lvlup.stat_change_possible('reflexes', 1)


def test_skill_change_possible_due_to_free_points():
    '''Skill change can't be bigger then free skill points'''
    lvlup = LevelUpHelper()
    av = Avatar('dummy')
    lvlup.skill_points = 7
    assert lvlup.skill_change_possible(av, 'escape', 1)
    assert lvlup.skill_change_possible(av, 'hide', 2)
    lvlup.skill_points = 0
    assert not lvlup.skill_change_possible(av, 'jump', 1)


def test_skill_change_cant_be_negative():
    lvlup = LevelUpHelper()
    av = Avatar('dummy')
    assert not lvlup.skill_change_possible(av, 'escape', -1)


def test_skill_change_possible_due_to_skill_cap():
    '''Skill changes should not allow skill to be greater than avatar.lvl + 3'''
    lvlup = LevelUpHelper()
    av = Avatar('dummy')
    av.lvl = 2
    lvlup.skill_points = 10
    lvlup.skill_changes['search'] = 3
    assert lvlup.skill_change_possible(av, 'search', 1)
    assert lvlup.skill_change_possible(av, 'search', 2)
    assert lvlup.skill_change_possible(av, 'search', 3)
    assert not lvlup.skill_change_possible(av, 'search', 4)


def test_can_choose_feat():
    '''Player can take feat on even levels'''
    lvlup = LevelUpHelper()
    av = Avatar('dummy')
    av.lvl = 2
    assert not lvlup.can_choose_feat(av)
    av.lvl = 3
    assert lvlup.can_choose_feat(av)
    lvlup.feat = 'dummy'
    assert not lvlup.can_choose_feat(av)
    lvlup.clear_feat()
    assert lvlup.can_choose_feat(av)


def test_choose_feat():
    lvlup = LevelUpHelper()
    lvlup.choose_feat('agile')
    assert lvlup.feat == 'agile'


def test_can_complete():
    lvlup = LevelUpHelper()
    av = Avatar('dummy')
    av.lvl = 2
    assert not lvlup.can_complete(av)
    lvlup.stat_points = 0
    lvlup.skill_points = 0
    assert lvlup.can_complete(av)
    av.lvl = 5
    assert not lvlup.can_complete(av)
    lvlup.choose_feat('dummy')
    assert lvlup.can_complete(av)


def test_complete():
    lvlup = LevelUpHelper()
    av = Avatar('dummy')
    av.lvl = 2
    lvlup.stat_changes = {'strength': 3}
    lvlup.skill_changes = {'jump': 3, 'escape': 2}
    lvlup.feat = 'dodge'
    lvlup.complete(av)
    assert av.base_strength == 4
    assert av.base_skill('jump') == 3
    assert av.base_skill('escape') == 2
    assert 'dodge' in av.feats
