import rpy_code
import mock
from rpy_code import Job, Jobs, all_jobs, all_upgrades, ActorSt, do_job, Castle, WhoreJob, LibrarianJob, DancerJob, EtiquetteTraining, ObedienceTraining, all_trainings


def test_job_fields():
    job = DancerJob()
    assert job.name == 'Dancer'
    assert job.uid == 'dancer'
    assert job.type == 'job'
    assert job.energy_cost == 20
    assert job.descr == 'Dancing at the tavern'


def test_jobs():
    jobs = Jobs()
    assert len(jobs) == len(all_jobs) + len(all_trainings)
    assert isinstance(jobs._jobs['maid'], Job)
    assert isinstance(jobs._jobs['slut'], Job)


def test_jobs_iteration():
    jobs = Jobs()
    for job in jobs:
        assert isinstance(job, Job)


def test_job_reward(mocker):
    job = LibrarianJob()
    ac = ActorSt('', '')
    ac.job_skills['librarian'] = 44
    dice_mock = mocker.patch.object(rpy_code, 'dice')
    dice_mock.return_value = 10
    assert job.reward(ac) == 26


#~ def test_do_job(mocker, monkeypatch):
    #~ '''Helper "do_job" should get scheduled job and call its "do" method, then reset schedule for given actor'''
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ castle.schedule['dummy'] = 'librarian'
    #~ job = mock.MagicMock()
    #~ castle.jobs._jobs['librarian'] = job
    #~ ac = Actor('dummy', 'Dummy')
    #~ do_job(ac)
    #~ assert job.do.called
    #~ assert castle.schedule['dummy'] is None


#~ def test_job_do(mocker, monkeypatch):
    #~ '''Job should raise training_coffers and actor's skill, reduce actor's energy when done
    #~ WhoreJob should also reset "lust" to zero'''
    #~ dice_mock = mocker.patch.object(rpy_code, 'dice')
    #~ # return value both for reward and skill increase
    #~ dice_mock.return_value = 3
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ ac = Actor('dummy', 'Dummy')
    #~ ac.lust = 53
    #~ ac.job_skills['whore'] = 8
    #~ job = WhoreJob()
    #~ job.do(ac)
    #~ # 'whore' job should reset actor's lust to zero
    #~ assert ac.lust == 0
    #~ assert castle.training_coffers == 31
    #~ assert ac.job_skills['whore'] == 14
    #~ assert ac.energy == 75


#~ def test_job_req_met(monkeypatch):
    #~ '''job.req_met(actor) should check for all requiremnts for that job'''
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ ac = Actor('dummy', 'Dummy')
    #~ job = WhoreJob()
    #~ assert not job.req_met(ac)
    #~ ac.obedience = 50
    #~ ac.depravity = 50
    #~ castle.upgrades.build('brothel')
    #~ assert job.req_met(ac)


#~ def test_job_insufficient_energy_reduce_affinity(mocker, monkeypatch):
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ dice_mock = mocker.patch.object(rpy_code, 'dice')
    #~ dice_mock.return_value = 3
    #~ ac = Actor('dummy', 'Dummy')
    #~ job = WhoreJob()
    #~ ac.affinity = 100
    #~ ac.energy = 5
    #~ job.do(ac)
    #~ assert ac.affinity == 96


def test_training_fields():
    job = ObedienceTraining()
    assert job.uid == 'obedience'
    assert job.name == 'Obedience'
    assert job.stat == 'obedience'
    assert job.energy_cost == 10
    # -1 means that training is locked
    assert job.level == -1


def test_etiquette_training_needed_levels():
    '''Trainings should tell which level is needed for current actor's skill'''
    job = EtiquetteTraining()
    ac = ActorSt('', '')
    assert ac.depravity == 0
    assert job.needed_level(ac) == 0
    ac.depravity = 80
    assert job.needed_level(ac) == 4


def test_etiquette_training_max_levels():
    '''Level of a training is raised (unlocked) during the game'''
    job = EtiquetteTraining()
    assert job.level == -1
    job.unlock_level(1)
    assert job.level == 1
    # max level for a training is 4 (master)
    job.unlock_level(7)
    assert job.level == 4


def test_unlock_level_safety():
    '''Unlock_level should not reset level to lower one'''
    job = EtiquetteTraining()
    job.unlock_level(4)
    assert job.level == 4
    job.unlock_level(2)
    assert job.level == 4


def test_training_do(mocker, monkeypatch):
    job = EtiquetteTraining()
    ac = ActorSt('', '')
    dice_mock = mocker.patch.object(rpy_code, 'dice')
    dice_mock.return_value = 3
    castle = Castle()
    castle.training_coffers = 100
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    job.do(ac)
    assert ac.depravity == 8
    assert castle.training_coffers == 50
    assert ac.energy == 100 - job.energy_cost


def test_training_requirements(monkeypatch):
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    castle.training_coffers = 50
    job = EtiquetteTraining()
    job.unlock_level(0)
    ac = ActorSt('', '')
    assert job.req_met(ac)
    ac.depravity = 60
    assert not job.req_met(ac)
    job.unlock_level(3)
    assert not job.req_met(ac)
    castle.training_coffers = 250
    assert job.req_met(ac)
    ac.depravity = 80
    assert not job.req_met(ac)


#~ def test_training_insufficient_energy_reduce_affinity(mocker, monkeypatch):
    #~ castle = Castle()
    #~ monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    #~ dice_mock = mocker.patch.object(rpy_code, 'dice')
    #~ dice_mock.return_value = 3
    #~ ac = Actor('dummy', 'Dummy')
    #~ job = EtiquetteTraining()
    #~ ac.affinity = 100
    #~ ac.energy = 5
    #~ job.do(ac)
    #~ assert ac.affinity == 99

