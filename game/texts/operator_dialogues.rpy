# greetings and dialogues for room operators
init python:
    operator_greetings = {
        'cliohna': ('Cliohna', ('... yes?', 'Research is still ongoing, what is it you need?', '*sigh*')),
        'skordred': ('Skordred', ('What dos the castle need?', 'Champion of chaos.', "Ah, it's you.")),
        'cla_min': ('Cla-Min', ('Need some new equipment?', 'The Cla caravan is at your disposal.', "Good to see you, Rowan!")),
        'indarah': ('Indarah', ('What brings you to my slice of the Wastes?', 'Business or pleasure?', "Busy day, I'll be with you in a moment.")),
        'andras_dungeon': ('Andras', ('Welcome to my domain, servant.', 'Are you feeling homesick?', "Looking for a cock to suck, by chance?")),
        'orc_soldier': ('Orc soldier', ('Yes boss?', "We's ready to fight.", "Show respect to the human boss!")),
        'greyhide': ('Greyhide', ('Hello, friend.', "It is good to see you.", "Old warrior, how can I help you?")),
        'x_zaratl': ("X'zaratl", ('*giggles*', "Welcome Rowy!", "Working right now?  Too bad.")),
        'andras_arena': ("Andras", ("Doesn't the smell of blood get you going?", "Just listen to them go at it.", "Looking to wager, servant?")),
        'draith': ("Draith", ("Yes, my lord?", "What brings you to my pits today?", "How can I help you?")),
        'rowan_empty_throne_room': ("Rowan", ("...", "(What should I do next?)", "(Best to keep working so I don't think about morals too much.)", "A moment to myself is always nice.")),
        'jezera_living_quarters': ("Jezera", ("Yes, my hero?", "Are you looking for someone?", "We still have so much to do.")),
        'alexia_pure_living_quarters': ("Alexia", ("Hello darling.", "It's always good to see you.", "I hope you haven't been forced to do anything truly horrific.")),
        'shaya': ("Shaya", ("Oh, hi.", "Hero Rowan, I do love seeing you.", "So you're done with- oh, sorry lord Rowan.  How may I help you?")),
        'helayna':("Helayna", ("Rowan, my [helaynaTitle]... I need you so much.", "I feel, so hot...", "Please fuck me!"))
    }


    # format: {operator_uid: (operator_name, ({'conditions': ('condition_to_eval1', 'condition_to_eval2', ...), 'phrase': 'phrase_text'}, ...)), ...}
    # 'conditions' part can be omitted; a phrase is choosen randomly from phrases without conditions and phrases with conditons that currently met
    operator_dialogues = {
        'cliohna': ('Cliohna', (
            {'phrase': "If you need to review any of my previous reports, you'll find them in the archives."},
            {'phrase': "I'm curious what your next move will be.  You have yet to disappoint."},
            {'phrase': "I'd rather not make small talk."},
            )),
        'rowan_empty_throne_room': ('Rowan', (
            # Next quota is due soon and you don't yet meet it.
            # TODO quota condition
            {'conditions': ('False',),
                'phrase': "(I have to focus on meeting the quota as soon as possible!  Event if it means resorting to extreme measures.  I can't risk what will happen if I fail.) "},
            # Next quota is due soon and a mission objective is incomplete.
            # TODO quota and mission condition
            {'conditions': ('False',),
                'phrase': "(I need to focus all my efforts on finishing the twin's mission.  There's no time left for delay!) "},
            # low income and low gold
            {'conditions': ('castle.treasury < 40', 'castle.treasury - castle.last_week_treasury < 5'),
                'phrase': "(The state of the treasury is not good.  I need to look out for opportunities to get any extra I can and see about finding new sources of revenue.)"},
            # low morale (<40) and falling morale
            {'conditions': ('castle.morale < 40', 'castle.morale - castle.last_week_morale < 0'),
                'phrase': "(The soldiers are growing restless.  I should either put them to work on something or see about improving entertainment in the castle.)"},
            # a barracks space is full or nearly full
            {'conditions': ('castle.buildings["barracks"].capacity - castle.buildings["barracks"].troops < 5', 'castle.buildings["barracks"].lvl > 0'),
                'phrase': "(We've reached our capacity for new (race) soldiers and are wasting recruitment.  EIther I should upgrade our capacity or put them to use in the field.)"},
            # negative income
            {'conditions': ('castle.treasury - castle.last_week_treasury < 0',),
                'phrase': "(Damn, I've let our income drop into the red.  This makes further expansion very difficult, I need to boost that income as soon as possible or use our troops to reduce our expenses.)"},
            # Default: No other option was found (the list of valid options is empty)
            {'default': True,
                'phrase': "(Things are going fairly well at the moment.  Maybe now is a good time to think about my later plans.)"},
            )),
        'jezera_living_quarters': ("Jezera", (
            {'phrase': "You wouldn't happen to know about any sapphire mines, would you?  I'm actually almost out of uncut gems for my enchanting."},
            # Pre end of first year.
            {'conditions': ('week < 48',),
                'phrase': "It's a shame that Bloodmean is so far away from any cities.  Makes it hard to find new staff."},
            # No brothel
            {'conditions': ('castle.buildings["brothel"].lvl == 0',),
                'phrase': "If you can make arrangements about getting a proper spy cadre in the castle, I'd very much appreciate it."},
            {'phrase': "Hmm, I'd say that my amulet suits you.  Don't you think so?"},
            {'phrase': "What am I up to all the time?  That's my little secret."},
        )),
        'alexia_pure_living_quarters': ("Alexia", (
            {'phrase': "Don't worry about me, just focus on finishing the tasks the twins have set.  I can manage here on my own."},
            {'phrase': "I should go to the library again, there's a book there that I'd like to finish reading."},
            {'phrase': "Being slaves to demons is kinda surreal when you stop and think about it.  I suppose you have the worse of it."},
        )),
        'skordred': ("Skordred", (
            {'phrase': "Thars still so much to fix from the war, damage you caused."},
            {'phrase': "Can we keep this quick?  I'd rathar not talk to you longer than necessary."},
            {'phrase': "Perhaps... nah, nah, farget I said anything."},
        )),
        'indarah': ("Indarah", (
            {'phrase': "Heard some juicy stories from the merchants.  Let me know if there's any specifics you're interested in."},
            {'phrase': "Save your advice and pity.  I've no regrets."},
            {'phrase': "People are starting to realize there's a storm on the horizon, something that goes beyond their own personal problems.  Be careful out there."},
        )),
        'andras_dungeon': ("Andras", (
            {'phrase': "Are you sure I can't cull the weak from our armies?  Fine, fine."},
            {'phrase': "I haven't had pussy in a while, maybe I should pay your wife a visit?"},
            # no prisoners
            {'conditions': ('castle.buildings["dungeon"].prisoners == 0',),
                'phrase': "All these empty cells make me feel unsatisfied.  Maybe you could fix that by finding a nice village to sack?"},
            # Pre ~8 weeks?
            {'conditions': ('week < 8',),
                'phrase': "Looking for your old neighbor?  Don't worry, he's in a special place now."},
        )),
        'andras_arena': ("Andras", (
            {'phrase': "Are you sure I can't cull the weak from our armies?  Fine, fine."},
            {'phrase': "I haven't had pussy in a while, maybe I should pay your wife a visit?"},
            # no prisoners
            {'conditions': ('castle.buildings["dungeon"].prisoners == 0',),
                'phrase': "All these empty cells make me feel unsatisfied.  Maybe you could fix that by finding a nice village to sack?"},
            # Pre ~8 weeks?
            {'conditions': ('week < 8',),
                'phrase': "Looking for your old neighbor?  Don't worry, he's in a special place now."},
        )),
        'greyhide': ("Greyhide", (
            {'phrase': "The witch has been telling me about other metals to make weapons from.  I wonder at what will cross my anvil in the coming years."},
            {'phrase': "It pleases me that I'm able to take a break and speak with you for a time here.  It's these moments that truly make my life here worthwhile."},
            {'phrase': "Do you have the dreams too?  Where fights you wish never happened come back night after night...."},
        )),
        'x_zaratl': ("X'zaratl", (
            {'phrase': "How have you been with your wife lately?  Any steamy action going on there?"},
            {'phrase': "Getting along well enough?  Anyone who's in need of some help in getting things along?"},
            {'phrase': "Well aren't you looking great today!  I'm glad that all that work isn't detracting from your sexy self."},
        )),
        'draith': ("Draith", (
            # No monsters
            {'conditions': ('castle.buildings["pit"].monsters == 0',),
                'phrase': "It's kinda quiet down here."},
            # No monsters
            {'conditions': ('castle.buildings["pit"].monsters == 0',),
                'phrase': "Do you think you could maybe find some monster nests?  I feel kinda useless right now."},
            # At least one monster
            {'conditions': ('castle.buildings["pit"].monsters > 0',),
                'phrase': "My charges are restless today.  I think they'd like to go hunting soon."},
            # At least one monster
            {'conditions': ('castle.buildings["pit"].monsters > 0',),
                'phrase': "Being underground and surrounded by monsters sets me at ease.  They remind me of the only things I liked from my home."},
            # no conditions
            {'phrase': "How's it going handsome?  Any chance you and me could spend some personal time with one another?"},
        )),
        'cla_min': ('Cla-Min', (
            {'phrase': "How have your travels been treating you?  I know that you aren't afforded even the comforts of a bed every night."},
            {'phrase': "Jumping from one realm to the next can be quite disorientating.  The weather being different depending on where you are in the world is just something you never thought about before."},
            {'phrase': "You know Rowan, we really should go somewhere more private and have a nice long... conversation.  There are many things we can learn about one another if you just let me sit on you for awhile."},
        )),
        'shaya': ('Shaya', (
            {'phrase': "Your presence is somewhat overwhelming.  I apologize if I'm a bit forward."},
            {'phrase': "I'm very curious about you, won't you tell me your stories later?"},
            {'phrase': "Sorry, Jezera came by a little while ago and I'm a bit out of sorts."},
        )),
        'helayna': ('Helayna', (
            {'phrase': "..."},
        )),
    }


    def choose_operator_phrase(operator_uid):
        '''Chooses one random phrase that has requirements met'''
        possible_phrases = []
        if operator_uid in operator_dialogues:
            for item in operator_dialogues[operator_uid][1]:
                if 'conditions' in item:
                    add_phrase = True
                    for condition in item['conditions']:
                        if not eval(condition):
                            add_phrase = False
                    if add_phrase:
                        possible_phrases.append(item['phrase'])
                elif 'default' not in item:
                    possible_phrases.append(item['phrase'])
            # if there is no possible phrases so far, add default ones
            if len(possible_phrases) == 0:
                for item in operator_dialogues[operator_uid][1]:
                    if 'default' in item:
                        possible_phrases.append(item['phrase'])
            return renpy.random.choice(possible_phrases)
