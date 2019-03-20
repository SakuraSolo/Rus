# jobs, special jobs, classes
init python:

    class Job(object):
        '''A base class for jobs for trainable NPC'''
        type = 'job'

        def do(self, actor):
            castle.training_coffers += self.reward(actor)
            actor.set_skill(self.uid, actor.skill(self.uid) + dice(3) + 3)
            # reduce affinity if actor has not enough energy for job
            if actor.energy < self.energy_cost:
                actor.affinity -= int(0.2 *(self.energy_cost - actor.energy))
            actor.energy -= self.energy_cost


    class MaidJob(Job):
        uid = 'maid'

        def __init__(self):
            self.name = 'Maid'
            self.energy_cost = 5
            self.descr = 'Cleaning around the castle'
            super(MaidJob, self).__init__()

        def req_met(self, actor):
            '''Returns True if requirements for this job are met'''
            return True

        def reward(self, actor):
            return int_ceil(actor.skill('maid') / 5.0 + dice(10))


    class LibrarianJob(Job):
        uid = 'librarian'

        def __init__(self):
            self.name = 'Librarian'
            self.energy_cost = 10
            self.descr = 'Re-shelving books and other menial tasks in the castle library'
            super(LibrarianJob, self).__init__()

        def req_met(self, actor):
            '''Returns True if requirements for this job are met'''
            return True

        def reward(self, actor):
            return int_ceil(actor.skill('librarian') / 4.0 + dice(10) + 5)


    class WenchJob(Job):
        uid = 'wench'

        def __init__(self):
            self.name = 'Tavern wench'
            self.energy_cost = 15
            self.descr = 'Serving drinks at the castle tavern'
            super(WenchJob, self).__init__()

        def req_met(self, actor):
            '''Returns True if requirements for this job are met'''
            if castle.upgrades['tavern'].built:
                return True

        def reward(self, actor):
            return int_ceil(actor.skills('wench') / 3.0 + dice(10) + 10)


    class DancerJob(Job):
        uid = 'dancer'

        def __init__(self):
            self.name = 'Dancer'
            self.energy_cost = 20
            self.descr = 'Dancing at the tavern'
            super(DancerJob, self).__init__()

        def req_met(self, actor):
            '''Returns True if requirements for this job are met'''
            if castle.upgrades['tavern'].built:
                if actor.obedience >= 30 and actor.depravity >= 20:
                    return True

        def reward(self, actor):
            return int_ceil(actor.skill('dancer') / 2.0 + dice(10) + 15)


    class WhoreJob(Job):
        uid = 'whore'

        def __init__(self):
            self.name = 'Whore'
            self.energy_cost = 25
            self.descr = 'Working in the castle brothel'
            super(WhoreJob, self).__init__()

        def req_met(self, actor):
            '''Returns True if requirements for this job are met'''
            if castle.upgrades['brothel'].built:
                if actor.obedience >= 50 and actor.depravity >= 50:
                    return True

        def reward(self, actor):
            return int_ceil(actor.skill('whore') + dice(10) + 20)

        def do(self, actor):
            super(WhoreJob, self).do(actor)
            actor.lust = 0


    class Training(Job):
        '''Base class for trainings (classes for NPC)'''
        type = 'training'
        # -1 means that training is locked
        level = -1
        energy_cost = 10

        def unlock_level(self, lvl):
            '''Unlocks new level of the training'''
            if lvl > 4:
                lvl = 4
            if lvl > self.level:
                self.level = lvl

        def do(self, actor):
            castle.training_coffers -= self.cost(actor)
            setattr(actor, self.stat, getattr(actor, self.stat) + dice(5) + 5)
            # reduce affinity if actor has not enough energy for job
            if actor.energy < self.energy_cost:
                actor.affinity -= int(0.2 *(self.energy_cost - actor.energy))
            actor.energy -= self.energy_cost

        def req_met(self, actor):
            '''Returns True if all requirements are met'''
            if self.needed_level(actor) <= self.level:
                if self.cost(actor) <= castle.training_coffers:
                    return True

        def needed_level(self, actor):
            '''Returns a needed level of training for a given actor'''
            return int(getattr(actor, self.stat) / 20)

        def cost(self, actor):
            return 5 * (self.needed_level(actor) + 1)


    class EtiquetteTraining(Training):
        uid = 'etiquette'
        name = 'Etiquette'
        stat = 'depravity'

        def cost(self, actor):
            return (50, 100, 250, 250, 250)[self.needed_level(actor)]


    class ObedienceTraining(Training):
        uid = 'obedience'
        name = 'Obedience'
        stat = 'obedience'

        def cost(self, actor):
            return (50, 100, 250, 250, 250)[self.needed_level(actor)]


    class SlutTraining(Training):
        uid = 'slut'
        name = 'Slut'
        stat = 'nymphomania'


    class ExhibitionismTraining(Training):
        uid = 'exhibitionism'
        name = 'Exhibitionism'
        stat = 'exhibitionism'


    # all jobs for NPC
    all_jobs = (MaidJob, LibrarianJob, WenchJob, DancerJob, WhoreJob)


    all_trainings = (EtiquetteTraining, ObedienceTraining, SlutTraining, ExhibitionismTraining)


    class Jobs(object):
        '''A collection of jobs, special jobs and trainings for NPC'''
        def __init__(self):
            self._jobs = {}
            # create instances of all jobs and store them
            for job_cls in all_jobs + all_trainings:
                job = job_cls()
                self._jobs[job.uid] = job

        def __len__(self):
            return len(self._jobs)

        def __iter__(self):
            return iter(self._jobs.values())

        def __getitem__(self, uid):
            return self._jobs[uid]


    def do_job(actor):
        '''Do scheduled job for given actor, including rewards, energy loss etc.'''
        job = castle.jobs[castle.schedule[actor.uid]]
        job.do(actor)
        castle.schedule[actor.uid] = None
