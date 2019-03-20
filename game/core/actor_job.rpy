init python:

    class ActorJobState(object):
        '''Stores data about a job'''

        def __init__(self):
            self.stress = 0
            self.job_class = None
            self.job = None

        @property
        def name(self):
            if self.job_class:
                return all_actor_job_classes[self.job_class]['name']
            else:
                return 'No class'

        def skill(self, skill_name):
            if self.job_class:
                return all_actor_job_classes[self.job_class]['skills'][skill_name][0]
            else:
                return 0

        def enjoyment(self, skill_name):
            if self.job_class:
                return all_actor_job_classes[self.job_class]['skills'][skill_name][1]
            else:
                return 'R'

        def enjoyment_coeff(self, skill_name):
            '''Returns coefficient for stress increase (depending on current class)'''
            if self.enjoyment(skill_name) == 'L':
                return -0.3
            elif self.enjoyment(skill_name) == 'N':
                return 0.0
            elif self.enjoyment(skill_name) == 'D':
                return 0.5
            elif self.enjoyment(skill_name) == 'H':
                return 1.0
            else:
                return 1.0

        def efficiency(self, _job=None):
            '''Returns current (or passed as argument) job efficiency depending on stress and job skill'''
            eff = 1.0
            # decrease efficiency depending on job skill
            eff *= self.job_skill(_job) / 10.0
            if self.stress > 20:
                # 0-20 stress: no effect, 20-100 stress: linearly decrease efficiency to zero
                eff *= (1 -(self.stress - 20) / 80.0)
            return eff

        def job_skill(self, _job=None):
            '''Returns level of main skill of current (or given) job, depending on job class'''
            if _job:
                return all_actor_job_classes[self.job_class]['skills'][all_actor_jobs[_job]['skill']][0]
            elif self.job:
                return all_actor_job_classes[self.job_class]['skills'][all_actor_jobs[self.job]['skill']][0]
            else:
                return 10


    def do_job_barmaid(ac_uid, coeff=1.0):
        '''Do barmaid job - add money to treasury and Rowan\'s money'''
        change_treasury(20 * all_actors[ac_uid].job_state.efficiency() * coeff)
        change_personal_gold(10 * all_actors[ac_uid].job_state.efficiency() * coeff)
        change_actor_stress(ac_uid, 10 * all_actors[ac_uid].job_state.enjoyment_coeff(all_actor_jobs['barmaid']['skill']))


    def do_job_research_assistant(ac_uid, coeff=1.0):
        '''Do job as a research assistant - add research points'''
        castle.rp += int(5 * all_actors[ac_uid].job_state.efficiency() * coeff)
        change_actor_stress(ac_uid, 10 * all_actors[ac_uid].job_state.enjoyment_coeff(all_actor_jobs['research_assistant']['skill']))


    def do_job_maid(ac_uid, coeff=1.0):
        '''Reduce maintenance cost of surface buildings'''
        castle.surface_maintenance_reduction = int(25 * all_actors[ac_uid].job_state.efficiency() * coeff)
        change_actor_stress(ac_uid, 10 * all_actors[ac_uid].job_state.enjoyment_coeff(all_actor_jobs['maid']['skill']))


    def do_job_breeding(ac_uid, coeff=1.0):
        '''Building effects are in BreedingPit, only change stress'''
        change_actor_stress(ac_uid, 10 * all_actors[ac_uid].job_state.enjoyment_coeff(all_actor_jobs['breeding']['skill']))


    def do_job_forge(ac_uid, coeff=1.0):
        '''Reduced armour craft cost / resource usage / convert more iron into equipment'''
        # TODO: convert more iron
        change_actor_stress(ac_uid, 10 * all_actors[ac_uid].job_state.enjoyment_coeff(all_actor_jobs['forge']['skill']))


    all_actor_job_classes = {
        'pure_housewife': {'name': 'Pure Housewife',
            'skills': {'academics': (5, 'L'), 'crafting': (4, 'D'), 'domestics': (8, 'L'), 'fighting': (0, 'R'), 'prostitution': (3, 'H'), 'zoology': (5, 'N')}},
        'magic_apperentice': {'name': 'Magic Apprentice',
            'skills': {'academics': (8, 'L'), 'crafting': (3, 'D'), 'domestics': (6, 'N'), 'fighting': (0, 'R'), 'prostitution': (2, 'H'), 'zoology': (3, 'H')}},
        'tainted_slut': {'name': 'Tainted Slut',
            'skills': {'academics': (0, 'R'), 'crafting': (1, 'H'), 'domestics': (3, 'D'), 'fighting': (0, 'R'), 'prostitution': (6, 'L'), 'zoology': (2, 'H')}},
        'tainted_informant': {'name': 'Tainted Informant',
            'skills': {'academics': (5, 'N'), 'crafting': (4, 'N'), 'domestics': (7, 'N'), 'fighting': (0, 'R'), 'prostitution': (4, 'N'), 'zoology': (5, 'N')}},
    }


    all_actor_jobs = {
        'maid': {'name': 'Maid',
            'skill': 'domestics', 'boss': 'Jezera', 'effect': 'Reduced maintenance cost of surface buildings'},
        'research_assistant': {'name': 'Research Assistant',
            'skill': 'academics', 'boss': 'Cliohna', 'effect': 'Extra research points'},
        'barmaid': {'name': 'Barmaid',
            'skill': 'domestics', 'boss': 'Indarah', 'effect': 'Boosted tavern income and some extra weekly money'},
        'breeding': {'name': 'Breeding',
            'skill': 'zoology', 'boss': 'Draith', 'effect': 'Capacity, reduced maintenance of monsters'},
        'forge': {'name': 'Forge hand',
            'skill': 'crafting', 'boss': 'Greyhide', 'effect': 'Reduced armour craft cost / resource usage / convert more iron into equipment'},
    }
