import rpy_code
from rpy_code import Research, all_researches, all_research_categories, Castle, SurvivalismAndCartography, Avatar, SurveyingAndTelescopics


def test_research_fields():
    rs = Research()
    assert rs.uid
    assert rs.name
    assert rs.category
    assert rs.cost == 0
    assert rs.rp_spent == 0
    assert rs.req_met
    assert rs.req_met() == True
    assert rs.on_complete
    assert rs.completed == False
    assert rs.requires == 'nothing'
    assert rs.unlocks == 'nothing'


def test_categories():
    '''Check categories of researches (for typos)'''
    for rs in all_researches:
        assert rs.category in all_research_categories


def test_history_of_rosaria_req_met(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    assert not castle.researches['history_of_rosaria'].req_met()
    castle.researches['world_and_the_war'].completed = True
    assert castle.researches['history_of_rosaria'].req_met()


def test_military_tactics_opens_barracks(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    castle.buildings['barracks'].build()
    assert castle.buildings['barracks'].lvl == 1
    assert castle.buildings['barracks'].max_lvl == 0
    castle.researches['military_tactics'].on_complete()
    assert castle.buildings['barracks'].lvl == 1
    assert castle.buildings['barracks'].max_lvl == 2


def test_SurvivalismAndCartography_adds_mp(monkeypatch):
    '''Completing Survivalism and Cartography should add 2 mp to avatar'''
    av = Avatar('dummy')
    monkeypatch.setattr(rpy_code, 'avatar', av, raising=False)
    rs = SurvivalismAndCartography()
    assert av.base_mp == 10
    rs.on_complete()
    assert av.base_mp == 12


def test_SurveyingAndTelescopics_adds_mp(monkeypatch):
    '''Completing Survivalism and Cartography should add 2 mp to avatar'''
    av = Avatar('dummy')
    monkeypatch.setattr(rpy_code, 'avatar', av, raising=False)
    rs = SurveyingAndTelescopics()
    assert av.view_distance == 1
    rs.on_complete()
    assert av.view_distance == 2
