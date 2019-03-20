# test outfits of Alexia
import rpy_code
from rpy_code import AlexiaSt


def test_all_outfits():
    al = AlexiaSt()
    for o in ['white', 'village', 'nude']:
        assert o in al.all_outfits


def test_outfit_def():
    al = AlexiaSt()
    assert al._all_outfits['nude'][0] == 'Nude'
    assert al._all_outfits['nude'][1] == 'images/Sprites/Alexia/alexia_nude'
    assert al._all_outfits['nude'][2] == al._nude_req


def test_available_outfits():
    '''actor.outfits should list owned outfits'''
    al = AlexiaSt()
    for o in ['white', 'village', 'nude']:
        assert o in al.all_outfits


def test_outfit_req():
    '''actor.outfit_req(uid) should check requirements for given outfit'''
    al = AlexiaSt()
    assert al.outfit_req('village') == True
    assert al.outfit_req('white') == True
    assert al.outfit_req('nude') == False
    al.depravity = 30
    assert al.outfit_req('nude') == True
    al.depravity = 0
    al.obedience = 30
    assert al.outfit_req('nude') == True


def test_setting_outfit():
    al = AlexiaSt()
    assert al.outfit == 'white'
    al.outfit = 'village'
    assert al.outfit == 'village'
    # outfit should be set only if it is available
    al.outfit = 'dummy'
    assert al.outfit == 'village'


def test_outfit_img():
    '''actor.outfit_img should provide full path to image based on current outfit and other stats'''
    al = AlexiaSt()
    assert al.outfit == 'white'
    assert al.outfit_img == 'images/Sprites/Alexia/alexia_white_outfit_lust_low.png'
    al.outfit = 'village'
    al.lust = 31
    assert al.outfit_img == 'images/Sprites/Alexia/alexia_village_lust_med.png'
    al.outfit = 'nude'
    al.lust = 61
    assert al.outfit_img == 'images/Sprites/Alexia/alexia_nude_lust_high.png'

