# common fixtures for tests
import pytest
import rpy_code
from rpy_code import Castle, Avatar, Journal


@pytest.fixture
def castle(monkeypatch):
    '''Provides castle to be present as global for tests'''
    castle = Castle()
    monkeypatch.setattr(rpy_code, 'castle', castle, raising=False)
    return castle


@pytest.fixture
def avatar(monkeypatch):
    '''Provides avatar to be present as global for tests'''
    avatar = Avatar('dummy')
    monkeypatch.setattr(rpy_code, 'avatar', avatar, raising=False)
    return avatar


@pytest.fixture
def msgs_mock(monkeypatch, mocker):
    '''Mock for messaging system'''
    msgs_mock = mocker.Mock()
    monkeypatch.setattr(rpy_code, 'msgs', msgs_mock, raising=False)
    return msgs_mock


@pytest.fixture
def renpy_mock(monkeypatch, mocker):
    '''Mock for messaging system'''
    renpy_mock = mocker.Mock()
    monkeypatch.setattr(rpy_code, 'renpy', renpy_mock, raising=False)
    return renpy_mock


# fixture for all_events, so it will reset at every test
@pytest.fixture
def all_events(monkeypatch):
    '''Provides all_events to be present as global for tests (and being reset between tests)'''
    all_events = {}
    monkeypatch.setattr(rpy_code, 'all_events', all_events, raising=False)
    return all_events


@pytest.fixture
def all_events_data(monkeypatch):
    '''Provides all_events_data to be present as global for tests'''
    all_events_data = {}
    monkeypatch.setattr(rpy_code, 'all_events_data', all_events_data, raising=False)
    return all_events_data


@pytest.fixture
def all_actors(monkeypatch):
    '''Provides all_actors to be present as global for tests'''
    all_actors = {}
    monkeypatch.setattr(rpy_code, 'all_actors', all_actors, raising=False)
    return all_actors


@pytest.fixture
def glossary_entries(monkeypatch):
    '''Some test glossary entries'''
    glossary_entries = {
        'test_entry': ('Test', 'Dummy'),
        'test_entry2': ('Test', 'Dummy'),
    }
    monkeypatch.setattr(rpy_code, 'glossary_entries', glossary_entries, raising=False)
    return glossary_entries


@pytest.fixture
def codex_entries(monkeypatch):
    '''Some test codex entries'''
    codex_entries = {
        'test_entry': ('Test_category', 'Test_topic', 'Dummy'),
        'test_entry2': ('Test_category', 'Test_topic', 'Dummy'),
        'test_entry3': ('Test_category', 'Test_topic2', 'Dummy'),
        'test_entry4': ('Test_category2', 'Test_topic', 'Dummy'),
    }
    monkeypatch.setattr(rpy_code, 'codex_entries', codex_entries, raising=False)
    return codex_entries


@pytest.fixture
def journal(monkeypatch):
    '''Some test glossary entries'''
    journal = Journal()
    monkeypatch.setattr(rpy_code, 'journal', journal, raising=False)
    return journal
