init python:
    import random


    class Spy(object):
        '''Spy'''
        def __init__(self, sex, name=None):
            self.name = random.choice(spy_names[sex])
            self.exp = 0
            self.lvl = 0
            self.traits = []
            self.traits.append(random.choice(spy_traits[sex]))
            self.sprite = random.choice(spy_sprites[sex])
            self.mission = None
            # sex of the spy, 'f' or 'm'
            self.sex = sex
            # register self in all_objects
            self.uid = new_uid()
            all_objects[self.uid] = self

        @property
        def pers(self):
            if self.sex == 'f':
                return 'she'
            else:
                return 'he'

        @property
        def persU(self):
            if self.sex == 'f':
                return 'She'
            else:
                return 'He'

        @property
        def him_her(self):
            if self.sex == 'f':
                return 'her'
            else:
                return 'him'

        @property
        def poss(self):
            if self.sex == 'f':
                return 'her'
            else:
                return 'his'


    class SpyMission(object):
        '''Contains mission date for a spy'''
        def __init__(self, spy_uid, type, loc, duration, started, label):
            self.spy_uid = spy_uid
            # type of a mission (infiltration, dominance, diplomatic, intelligence)
            self.type = type
            # location of a mission (map_uid, coords)
            self.loc = loc
            # how long this mission will take (set at the moment a mission is created)
            self.duration = duration
            # timestamp (when mission was started)
            self.started = started
            # label that will be called when mission will be completed
            self.label = label

        @property
        def completed(self):
            if self.started + self.duration <= week:
                return True


    def get_spies(selector):
        '''Returns list of spies that match selector'''
        if selector == 'idle':
            return [spy for spy in [get_object(uid) for uid in castle.buildings['brothel'].spies] if not spy.mission]
        elif selector == 'on mission':
            return [spy for spy in [get_object(uid) for uid in castle.buildings['brothel'].spies] if spy.mission]
        elif selector == 'completed mission':
            return [spy for spy in [get_object(uid) for uid in castle.buildings['brothel'].spies] if spy.mission and spy.mission.completed]


    def assign_mission(spy_uid, type, loc, started):
        '''Assign a mission to the spy (choose randomly)'''
        spy = get_object(spy_uid)
        # choose spy mission from those definitions that match conditions
        mission_def = random.choice([smd for smd in spy_mission_defs if smd().condition(spy, loc, started) and type == smd().kind])
        # create and assign spy mission to the spy
        spy.mission = mission_def().create_sm(spy, loc, started)


    # name pool for spies
    spy_names = {'f': [
        "Vix'res",
        "Ishis",
        "Pira",
        "Mariel",
        "Q'shaal",
        "Yarashe",
        "Ata'xia",
        "Zee",
        "Siranya",
    ],
    'm': [
        "Ber'ash",
        "Rurex",
        "Lustorl",
        "Draal",
        "Ty'rann",
        "Pan'axx",
        "Marask",
        "Xarall",
        "Vas",
    ]}


    # spy traits (by sex)
    spy_traits = {'f': [
            'Shrewd negotiator',
            'Shadow',
            'Mistress',
            'Submissive seducer',
            'Impulsive',
            'Methodical',
        ],
        'm': [
            'Shrewd negotiator',
            'Shadow',
            'Master',
            'Submissive seducer',
            'Impulsive',
            'Methodical',
        ],
    }

    # recruitment lines (by sex and trait)
    spy_recruitment_lines = {
    'f':
        {'Mistress': ["My, what a lovely morsel.  I'm going to enjoy eating you up.",
            "Men, women, monsters, it makes no difference.  All of them will eventually drink from my pussy."],
        'Impulsive': ["Finally recognized for my skills.  I'm ready to put both my sets of lips to use.",
            "Oh this girl's ready to take on the world.  Look out, (name) is on the way!"],
        'Methodical': ["Unlike some ladies, I know how to take my time to make sure the job gets done right.",
            "I hadn't expected Bloodmeen to rise again so quickly.  No matter, I still have plans in the oven, so many plans for our mutual benefit."],
        },
    'm':
        {'Master': ["Looking for a real man to show you the way around a cock?  Don't worry, I'll also make you intimately familiar with some of my toys too.",
            "Hmmm, I'm looking forward to all the new playthings I'll be making in your service."],
        'Impulsive': ["Come on, come on, send me on a mission right away!  I want to bone something!",
            "Looking for someone to get the jobs done quick and efficient?  I'm the handsome man for you."],
        'Methodical': ["You made the right choice.  I'll make sure there are no loose ends.",
            "What a lovely place.  Perfect for relaxing, enjoying some holes, and for planning missions."],
        }
    }


    spy_sprites = {
        'f':
        ('succubus1',
        'succubus2',
        'succubus3',
        'succubus4',
        'succubus5',
        'succubus6',),
        'm':
        ('incubus1',
        'incubus2',
        'incubus3',
        'incubus4',
        'incubus5',
        'incubus6',)
    }
