init python:

    # map letters to stat names
    letter_to_stat = {'s': 'strength', 'v': 'vitality', 'r': 'reflexes',
                    'i': 'intelligence', 'l': 'luck', 'c': 'corruption', 'f': 'infamy', 'g': 'guilt'}


    # item categories (item def should contain one to be shown in inventory screen)
    item_categories = ('weapon', 'armour', 'accessory', 'item', 'quest')


    # equipment slots (item def should contain exactly one if it ever be equipped)
    equip_slots = ('head', 'chest', 'waist', 'hands', 'feet', 'main', 'off', 'finger', 'neck', 'other')


    # penalties to certain skills due to armour weight
    armour_weight_penalties = {'plate': -2, 'shield': -1, 'chain': -1}


    # all items in the game
    # format for item entry: uid: (name, list of keywords, tier, stats effects, (buy value, sell value), big image, description)
    all_items = {
        'iron_sword': ('Iron Sword', ['main', 'weapon', 'sword'], 1, {'s': 1}, (100, 50), 'images/items/iron_sword.png',
            'Rowan\'s sword. While unremarkable, it has always served him well'),
        # armour
        #'robe': ('Robe', ['chest', 'armour', 'cloth'], 1, {'i': 2}, (50, 10), 'images/items/Item_Robe.png',
        'robe': ('Robe', ['chest', 'armour', 'cloth'], 1, {'i': 2}, (50, 10), 'images/items/Robe.png',
            ''),
        'cloth_hat': ('Cloth Hat', ['head', 'armour', 'cloth'], 1, {'i': 1}, (30, 6), 'images/items/Cloth Hat.png',
            ''),
        'gloves': ('Gloves', ['hands', 'armour', 'cloth'], 1, {'i': 1}, (20, 4), 'images/items/Gloves.png',
            ''),
        'shoes': ('Shoes', ['feet', 'armour'], 1, {'i': 1}, (20, 4), 'images/items/Shoes.png',
            ''),
        'leather_helm': ('Leather Helm', ['head', 'armour', 'leather'], 1, {'v': 1}, (40, 8), 'images/items/Leather Helm.png',
            ''),
        'leather_gloves': ('Leather Gloves', ['hands', 'armour', 'leather'], 1, {'v': 1}, (35, 7), 'images/items/Leather Gloves.png',
            ''),
        'leather_boots': ('Leather Boots', ['feet', 'armour', 'leather'], 1, {'v': 1}, (35, 7), 'images/items/Leather Boots.png',
            ''),
        'studded_helm': ('Studded Helm', ['head', 'armour', 'leather'], 1, {'v': 2, 'r': -1}, (60, 12), 'images/items/Studded Helm.png',
            ''),
        'studded_gloves': ('Studded Gloves', ['hands', 'armour', 'leather'], 1, {'v': 2, 'r': -1}, (50, 10), 'images/items/Studded Gloves.png',
            ''),
        'iron_sallet': ('Iron Sallet', ['head', 'armour', 'plate', 'iron'], 1, {'v': 4, 'r': -3}, (150, 30), 'images/items/Iron Sallet.png',
            ''),
        'iron_mail_coif': ('Iron Mail Coif', ['head', 'armour', 'chain', 'iron'], 1, {'v': 3, 'r': -2}, (100, 20), 'images/items/Iron Mail Coif.png',
            ''),
        'iron_gauntlets': ('Iron Gauntlets', ['hands', 'armour', 'plate', 'iron'], 1, {'v': 3, 'r': -2}, (100, 20), 'images/items/Iron Gauntlets.png',
            ''),
        'iron_sabatons': ('Iron Sabatons', ['feet', 'armour', 'plate', 'iron'], 1, {'v': 3, 'r': -2}, (100, 20), 'images/items/Iron Sabatons.png',
            ''),
        'leather_straps': ('Leather Straps', ['chest', 'armour', 'leather'], 1, {'v': 1}, (0, 0), 'images/items/Leather Straps.png',
            'Rowan\'s old armour from his adventuring days'),
        'leather_jerkin': ('Leather Jerkin', ['chest', 'armour', 'leather'], 1, {'v': 1, 'r': 1}, (75, 15), 'images/items/Leather Jerkin.png',
            'A simple leather chestpiece, offering a small amount of protection, without sacrificing movement'),
        'studded_coat': ('Studded Coat', ['chest', 'armour', 'leather'], 1, {'v': 2, 'r': -1}, (100, 20), 'images/items/Studded Coat.png',
            'A leather chestpiece riveted with metal studs to provide extra protection'),
        'iron_hauberk': ('Iron Hauberk', ['chest', 'armour', 'chain', 'iron'], 1, {'v': 3, 'r': -2}, (150, 30), 'images/items/Iron Hauberk.png',
            'A shirt of small iron links, sturdy enough to impede an arrow, or light weapon blow'),
        'iron_brigandine': ('Iron Brigandine', ['chest', 'armour', 'iron'], 1, {'v': 4, 'r': -3}, (200, 40), 'images/items/Iron Brigandine.png',
            'A leather chestpiece, lined with small oblong steel plates, riveted to the fabric'),
        'iron_plackart': ('Iron Plackart', ['chest', 'armour', 'plate', 'iron'], 1, {'v': 5, 'r': -4}, (250, 20), 'images/items/Iron Plackart.png',
            'A chest piece of plate that covers half the torso, offering a great deal of protection without full weight of a breastplate'),
        'iron_breastplate': ('Iron Breastplate', ['chest', 'armour', 'plate', 'iron'], 1, {'v': 6, 'r': -5}, (300, 60), 'images/items/Iron Breastplate.png',
            'Two conjoined large plates, molded around the torso to offer maximum protection at the cost of a great deal of dexterity'),
        'iron_dagger': ('Iron Dagger', ['weapon', 'dagger', 'main'], 1, {'s': 1, 'r': 1}, (100, 70), 'images/items/Iron_Dagger.png',
            'A simple dagger made from iron; lightweight and razor sharp'),
        'iron_longsword': ('Iron Longsword', ['weapon', 'sword', 'main'], 1, {'s': 2}, (200, 150), 'images/items/Iron_Longsword.png',
            'Standard issue for most knights of the Six Realms, unremarkable, but well made swords like these are found at every blacksmith\'s'),
        'iron_rapier': ('Iron Rapier', ['weapon', 'sword', 'main'], 1, {'s': 2, 'v': 1}, (300, 200), 'images/items/Iron_Rapier.png',
            'A slender, sharply pointed blade best suited for thrusting. The decorative pommel offers a small amount of protection.'),
        'balasts_brand': ('Balast\'s Brand', ['weapon', 'sword', 'magic', 'minor', 'main'], 2, {'s': 3, 'r': 2}, (750, 500), 'images/items/Balast_s_Brand.png',
            'A number of these blades were forged by the priests of Balast for soldiers who took part in the fifth crusade.'),
        # discounted Balast's Brand for Cla-Min bribe
        'balasts_brand_discounted': ('Balast\'s Brand', ['weapon', 'sword', 'magic', 'minor', 'main', 'non-random'], 2, {'s': 3, 'r': 2}, (300, 300), 'images/items/Balast_s_Brand.png',
            'A number of these blades were forged by the priests of Balast for soldiers who took part in the fifth crusade.'),
        # gifted Balast's Brand for Cla-Min bribe
        'balasts_brand_gifted': ('Balast\'s Brand', ['weapon', 'sword', 'magic', 'minor', 'main', 'non-random'], 2, {'s': 3, 'r': 2}, (750, 500), 'images/items/Balast_s_Brand.png',
            'A number of these blades were forged by the priests of Balast for soldiers who took part in the fifth crusade. (Gifted by Cla-Min)'),
        'bastard_sword': ('Bastard Sword', ['weapon', 'sword', 'main'], 1, {'s': 3, 'r': -1}, (400, 300), 'images/items/Bastard_Sword.png',
            'The sword falls somewhere between a longsword and a greatsword. Sturdy, but heavy.'),
        'zweihander': ('Zweihander', ['weapon', 'sword', 'two-handed', 'main'], 1, {'s': 5, 'r': -3}, (600, 400), 'images/items/Zweihander.png',
            'A two-handed sword popular with mercenaries. Heavy enough to break a bones beneath plate.'),
        'wooden_shield': ('Wooden Shield', ['armour', 'shield', 'off'], 1, {'v': 1}, (100, 75), 'images/items/Wooden_Shield.png',
            'A simple round shield made from non-splitting wood, reinforced using leather, with a metal rim'),
        'buckler': ('Buckler', ['armour', 'shield', 'off'], 1, {'v': 2}, (200, 150), 'images/items/Buckler.png',
            'A round, metal shield; useful for deflecting blows, but too small to be much use against missiles.'),
        'knights_shield': ('Knight\'s Shield', ['armour', 'shield', 'off'], 1, {'v': 3}, (350, 225), 'images/items/Knight_s_Shield.png',
            'A triangular shield carried by most soldiers and knights in the realms. More often than not, they are decorated with a coat of arms or heraldry.'),
        'knights_helm': ('Knight\'s Helm', ['armour', 'head', 'plate'], 1, {'v': 3, 'r': -1}, (150, 35), 'images/items/Knight_s_Helm.png',
            'A well crafted helm, offering a good deal of protection at the cost of some of the wearer\'s peripheral vision.'),
        'gauntlets_of_might': ('Gauntlets of Might', ['armour', 'hands', 'plate', 'magic', 'minor'], 2, {'v': 3, 's': 2, 'r': -2}, (250, 50), 'images/items/Gauntlets of Might.png',
            'As well as affording excellent protection, the wearer also feels stronger upon donning the gloves.'),
        'garnet': ('Garnet', ['gemstone', 'item'], 1, {}, (100, 70), 'images/items/Garnet.png',
            'A precious gemstone that can be given as a gift or sold for a good price.'),
        'topaz': ('Topaz', ['gemstone', 'item'], 1, {}, (200, 125), 'images/items/Topaz.png',
            'A precious gemstone that can be given as a gift or sold for a good price.'),
        'emerald': ('Emerald', ['gemstone', 'item'], 1, {}, (350, 250), 'images/items/Emerald.png',
            'A precious gemstone that can be given as a gift or sold for a good price.'),
        'ruby': ('Ruby', ['gemstone', 'item'], 1, {}, (500, 350), 'images/items/Ruby.png',
            'A precious gemstone that can be given as a gift or sold for a good price.'),
        'diamond': ('Diamond', ['gemstone', 'item'], 1, {}, (1000, 750), 'images/items/Diamond.png',
            'A precious gemstone that can be given as a gift or sold for a good price.'),
        'selanis_ring': ('Selani\'s Ring', ['finger', 'accessory', 'ring', 'magic', 'minor', 'non-random'], 1, {'l': 2}, (100, 50), 'images/items/Selani_s_Ring.png',
            'A simple elven made band of silver. It has always brought her luck.'),
        'monster_brain': ('Monster\'s Brain', ['ingredient', 'item', 'organ', 'non-random'], 1, {}, (200, 150), 'images/items/Monster_s_Brain.png',
            'The brain of a monster, primary used for alchemical purposes.'),
        'monster_heart': ('Monster\'s Heart', ['ingredient', 'item', 'organ', 'non-random'], 1, {}, (300, 200), 'images/items/Monster_s_Heart.png',
            'The heart of a monster, primary used for alchemical purposes.'),
        'monster_blood': ('Monster\'s Blood', ['ingredient', 'item', 'blood', 'non-random'], 1, {}, (100, 70), 'images/items/Monster_s_Blood.png',
            'The blood of a monster, primary used for alchemical purposes.'),
        # gattsu_blade and shield are added just for testing (high prices so they not fit for get_rnd_item etc.)
        'gattsu_blade': ('Gattsu Blade', ['main', 'weapon', 'sword', 'two-handed', 'non-random'], 3, {'s': 3, 'r': -2}, (1000000, 500000), 'images/items/gattsublade.png',
            'Three times as heavy and thick as a normal sword. Immesely powerful, but difficult to wield'),
        'shield': ('Shield', ['off', 'shield', 'armour', 'non-random'], 2, {'v': 2}, (1000000, 500000), 'images/items/shield.png',
            'Item description'),
    }


    # affinity increase when some items are gifted
    gift_affinity = {
        'garnet': 1, 'topaz': 2, 'emerald': 3, 'ruby': 4, 'diamond': 5}
