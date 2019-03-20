from rpy_code import game_date


def test_start_date():
    # date of first week of the game
    assert game_date(1) == 'Week One of Goldwreath, 879 A.F.', game_date(1)


def test_some_dates():
    # some timestamps to convert to date
    assert game_date(2) == 'Week Two of Goldwreath, 879 A.F.', game_date(2)
    assert game_date(7) == "Week Three of Layela's Favour, 879 A.F.", game_date(7)
    assert game_date(28) == "Week Four of Whitefall, 879 A.F.", game_date(28)
    assert game_date(29) == "Week One of Hoar's Breath, 880 A.F.", game_date(29)
    assert game_date(49) == "Week One of Goldwreath, 880 A.F.", game_date(49)
    assert game_date(240) == "Week Four of Tariel's Ascent, 884 A.F.", game_date(240)
