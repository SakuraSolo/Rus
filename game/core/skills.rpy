# skills and feats
init python:

    # definitions for all skills, format {'uid': ('Name', 'letter for stat mod'), ...}
    all_skills = {
        'bluff': ('Bluff', 'i'),
        'climb': ('Climb', 's'),
        'deceive': ('Deceive', 'i'),
        'decipher': ('Decipher Script', 'i'),
        'diplomacy': ('Diplomacy', 'i'),
        'disarm': ('Disarm Device', 'i'),
        'dodge': ('Dodge', 'r'),
        'escape': ('Escape Artist', 'r'),
        'hide': ('Hide', 'r'),
        'intimidate': ('Intimidate', 's'),
        'listen': ('Listen', 'i'),
        'jump': ('Jump', 's'),
        'move_silently': ('Move Silently', 'r'),
        'open_lock': ('Open Lock', 'r'),
        'search': ('Search', 'i'),
        'sleight_hand': ('Sleight of Hand', 'r'),
        'spot': ('Spot', 'i'),
        'survival': ('Survival', 'i'),
        'swim': ('Swim', 's'),
    }


    # these skills receive a penalty from heavier armour
    skills_with_armour_penalty = set(('climb', 'dodge', 'escape', 'jump', 'move_silently', 'swim'))


    # all feats, format {'uid': ('Name', {'skill, mp or stat': modifier, ...}), ...}
    # one letter is name of stat, as in items.rpy->letter_to_stat
    all_feats = {
        'acrobatic': ('Acrobatic', {'jump': 2}),
        'agile': ('Agile', {'escape': 2}),
        'alert': ('Alert', {'spot': 1, 'listen': 1}),
        'athletic': ('Athletic', {'swim': 1, 'climb': 1}),
        'deft_hands': ('Deft hands', {'sleight_hand': 2}),
        'diligent': ('Diligent', {'decipher': 2}),
        'dodge': ('Dodge', {'dodge': 2}),
        'liar': ('Expert Liar', {'deceive': 2}),
        'investigator': ('Investigator', {'search': 2}),
        'nimble_fingers': ('Nimble Fingers', {'disarm': 1, 'open_lock': 1}),
        'persuasive': ('Persuasive', {'bluff': 1, 'intimidate': 1}),
        'self_sufficient': ('Self-Sufficient', {'survival': 2}),
        'stealthy': ('Stealthy', {'hide': 1, 'move_silently': 1}),
        #'toughness': ('Toughness', {'hp': 3}),
        'luck': ('Unnatural Luck', {'l': 2}),
    }
