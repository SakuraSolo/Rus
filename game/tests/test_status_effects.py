from rpy_code import Avatar, Injury, MultiEffect


def test_injury_decrease_stat():
    av = Avatar('dummy')
    av.base_strength = 10
    assert av.strength == 10
    av.add_effect(Injury('dummy', 'strength', -3))
    assert av.strength == 7


def test_injury_is_negative():
    inj = Injury('dummy', 'dummy', 0)
    assert inj.kind == 'neg'


def test_injuries_dont_drop_stat_below_zero():
    '''Injuries should not drop a stat below zero'''
    av = Avatar('dummy')
    av.base_reflexes = 12
    assert av.reflexes == 12
    av.add_effect(Injury('dummy', 'reflexes', -7))
    assert av.reflexes == 5
    av.add_effect(Injury('dummy', 'reflexes', -7))
    assert av.reflexes == 0
    av.effects.pop()
    av.update_stats()
    assert av.reflexes == 5


def test_str_injury():
    '''String representation of Injury'''
    inj = Injury('Curse', 'luck', -2, 7)
    assert str(inj) == 'Curse (-2 Luck for 7w)'


def test_str_multieffect():
    '''String representation of MultiEffect'''
    se = MultiEffect('Stone skin', 'pos', (('vitality', 2), ('reflexes', -1)), 7)
    assert str(se) == 'Stone skin (2 Vitality -1 Reflexes for 7w)'


def test_weekly_updates(mocker):
    av = Avatar('dummy')
    inj = Injury('dummy', 'vitality', -7)
    inj.weekly = mocker.MagicMock()
    av.add_effect(inj)
    assert not inj.weekly.called
    av.weekly()
    assert inj.weekly.called


def test_removing_expired_effects():
    av = Avatar('dummy')
    av.add_effect(Injury('dummy', 'reflexes', -7))
    assert av.reflexes == 0
    assert len(av.effects) == 1
    av.weekly()
    assert len(av.effects) == 0
    assert av.reflexes == 1


def test_heal_injuries():
    av = Avatar('dummy')
    av.add_effect(Injury('dummy', 'reflexes', -7))
    av.add_effect(Injury('dummy', 'intelligence', -3))
    assert av.reflexes == 0
    assert av.intelligence == 0
    assert len(av.effects) == 2
    av.heal_injuries()
    assert av.reflexes == 1
    assert av.intelligence == 1
    assert len(av.effects) == 0


def test_heal_only_negative():
    '''Healing should remove only negative effects'''
    av = Avatar('dummy')
    av.add_effect(Injury('dummy', 'reflexes', -1))
    av.add_effect(MultiEffect('dummy', 'neg', (('reflexes', -1),)))
    av.add_effect(MultiEffect('dummy', 'pos', (('reflexes', 3), ('vitality', -2))))
    assert len(av.effects) == 3
    av.heal_injuries()
    assert len(av.effects) == 1


def test_multieffect():
    '''MultiEffect should change multiple target stats'''
    av = Avatar('dummy')
    av.base_strength = 5
    av.base_reflexes = 5
    assert av.strength == 5
    assert av.reflexes == 5
    av.add_effect(MultiEffect('dummy', 'pos', (('strength', -1), ('reflexes', 2))))
    assert av.strength == 4
    assert av.reflexes == 7


def test_effects_on_skills():
    av = Avatar('dummy')
    av.skills['diplomacy'] = 15
    assert av.skill('diplomacy') == 15
    av.add_effect(MultiEffect('dummy', 'neg', (('diplomacy', -1),)))
    assert av.skill('diplomacy') == 14
    # check restoring skill
    av.heal_injuries()
    assert av.skill('diplomacy') == 15


def test_mp_reducing():
    av = Avatar('dummy')
    assert av.base_mp == 10
    assert av.wounds == 0
    assert av.mp_penalty == 0
    assert av.mp == 10
    av.add_effect(MultiEffect('dummy', 'neg', (('mp', -3),), 2))
    assert av.base_mp == 10
    assert av.wounds == 0
    assert av.mp_penalty == 3
    assert av.mp == 7
    av.weekly()
    assert av.base_mp == 10
    assert av.wounds == 0
    assert av.mp_penalty == 3
    assert av.mp == 7
    av.weekly()
    # status effect ended
    assert av.base_mp == 10
    assert av.wounds == 0
    assert av.mp_penalty == 0
    assert av.mp == 10


def test_mp_penalty_limits():
    av = Avatar('dummy')
    assert av.base_mp == 10
    assert av.mp_penalty == 0
    assert av.mp == 10
    av.take_damage(3)
    assert av.mp == 7
    av.add_effect(MultiEffect('dummy', 'neg', (('mp', -14),), 2))
    assert av.base_mp == 10
    assert av.mp_penalty == 10
    assert av.wounds == 3
    assert av.mp == 0
