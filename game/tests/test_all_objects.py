from rpy_code import new_uid, del_object
import rpy_code


def test_new_uid(monkeypatch, mocker):
    all_objects = {345: 'dummy'}
    monkeypatch.setattr(rpy_code, 'all_objects', all_objects, raising=False)
    randint_mock = mocker.MagicMock()
    randint_mock.side_effect = [345, 789]
    mocker.patch('rpy_code.random.randint', new=randint_mock)
    uid = new_uid()
    assert uid == 789


def test_del_object(monkeypatch):
    all_objects = {}
    monkeypatch.setattr(rpy_code, 'all_objects', all_objects, raising=False)
    uid = new_uid()
    all_objects[uid] = 'dummy'
    assert len(all_objects) == 1
    del_object(uid)
    assert len(all_objects) == 0
