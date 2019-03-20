init python:

    class ActorSt(object):
        '''Actor (npc)'''

        def __init__(self, uid, name):
            self.uid = uid
            self.name = name
            # if actor alive
            self.alive = True
            # if Rowan met this actor before
            self.known = False
            # NPC stats are created via 'create_actor_stat
            self.energy = 100
            # skills for every job
            # TODO: getter/setter for limiting job_skills (0, 100)
            self.job_skills = {}
            for job_cls in all_jobs:
                self.job_skills[job_cls.uid] = 0
            # set default titles for actors
            self.self_title = 'I'
            self.player_title = 'Rowan'


        def skill(self, skill):
            return self.job_skills[skill]

        def set_skill(self, skill, val):
            '''Set job skill, keeping it in range 0-100'''
            if val < 0:
                val = 0
            elif val > 100:
                val = 100
            self.job_skills[skill] = val

        def weekly(self):
            '''Default method for updating state'''
            self.lust += int(self.depravity * 0.1)


    # actor stats
    actor_stats_st = ('energy', 'affinity', 'corruption', 'lust', 'reputation', 'depravity', 'dominance', 'obedience', 'nymphomania', 'exhibitionism')

    # stats shown at NPC screen
    # TODO: maybe this should go to GUI
    actor_public_stats_st = ('energy', 'affinity', 'depravity', 'obedience', 'exhibitionism', 'nymphomania', 'corruption')


    # current difference with avatar stat is that this has not 'base' stat, only 'final'
    def create_actor_stat(cls, name, init_val=0):
        '''Create standard stat for the actor (limited in range 0-100)'''

        def getter(self):
            return getattr(self, '_' + name)

        def setter(self, val):
            if val < 0:
                val = 0
            elif val > 100:
                val = 100
            setattr(self, '_' + name, val)

        setattr(cls, '_' + name, init_val)
        setattr(cls, name, property(getter, setter))


    # create stats for Actor class
    for stat in actor_stats_st:
        create_actor_stat(ActorSt, stat)
