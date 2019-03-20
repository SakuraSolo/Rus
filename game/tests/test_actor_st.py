from rpy_code import ActorSt, all_jobs, actor_stats_st


def test_actor_has_job_skills():
    '''Each actor should have skills for every job'''
    ac = ActorSt('', '')
    for job_cls in all_jobs:
        assert job_cls.uid in ac.job_skills


def test_weekly_update():
    '''Actor should have default 'weekly' method to update state'''
    ac = ActorSt('', '')
    ac.depravity = 83
    assert ac.lust == 0
    ac.weekly()
    assert ac.lust == 8


def test_actor_stats_range():
    '''Actor's stats should be in range 0-100'''
    ac = ActorSt('', '')
    for stat in actor_stats_st:
        setattr(ac, stat, -1)
        assert getattr(ac, stat) == 0
        setattr(ac, stat, 101)
        assert getattr(ac, stat) == 100


def test_actor_job_skills_range():
    '''Actor's job skills should be in range 0-100'''
    ac = ActorSt('', '')
    # filter jobs from all_jobs (skip special jobs and trainings)
    for skill in [cls.uid for cls in all_jobs if cls.type == 'job']:
        ac.set_skill(skill, -1)
        assert ac.skill(skill) == 0
        ac.set_skill(skill, 101)
        assert ac.skill(skill) == 100

# TODO: check that only jobs have skills on Actor, not trainings
