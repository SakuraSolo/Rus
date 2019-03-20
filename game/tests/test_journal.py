from rpy_code import Journal, glossary_add, glossary_read, quests_entries
import rpy_code
from fixtures import glossary_entries, codex_entries, journal


def test_glossary_add(glossary_entries, monkeypatch):
    journal = Journal()
    monkeypatch.setattr(rpy_code, 'journal', journal, raising=False)
    assert journal.new_entries() == 0
    assert journal.glossary == {}
    glossary_add('test_entry')
    assert journal.new_entries() == 1
    assert journal.glossary['Test'] == {'new': True, 'entries': ['test_entry']}


def test_glossary_read(glossary_entries, monkeypatch):
    journal = Journal()
    monkeypatch.setattr(rpy_code, 'journal', journal, raising=False)
    glossary_add('test_entry')
    assert journal.new_entries() == 1
    glossary_read('Test')
    assert journal.new_entries() == 0
    glossary_add('test_entry2')
    assert journal.new_entries() == 1


def test_glossary_duplicate_entry(glossary_entries, monkeypatch):
    '''Adding same entry should not set "new" flag or add duplicate entry'''
    journal = Journal()
    monkeypatch.setattr(rpy_code, 'journal', journal, raising=False)
    glossary_add('test_entry')
    assert journal.new_entries() == 1
    glossary_read('Test')
    assert journal.new_entries() == 0
    glossary_add('test_entry')
    assert journal.new_entries() == 0
    assert len(journal.glossary['Test']['entries']) == 1


def test_codex_add(codex_entries, journal):
    assert journal.new_entries() == 0
    journal.codex_add('test_entry')
    assert journal.new_entries() == 1
    assert journal.new_codex_entries_in_category('Test_category') == 1
    assert journal.new_codex_entries_in_category('Test_category2') == 0


def test_codex_read(codex_entries, journal):
    journal.codex_add('test_entry')
    journal.codex_add('test_entry2')
    journal.codex_add('test_entry3')
    journal.codex_add('test_entry4')
    assert journal.new_entries() == 3
    assert journal.new_codex_entries_in_category('Test_category') == 2
    assert journal.new_codex_entries_in_category('Test_category2') == 1
    journal.codex_read('Test_category', 'Test_topic')
    assert journal.new_entries() == 2
    assert journal.new_codex_entries_in_category('Test_category') == 1
    assert journal.new_codex_entries_in_category('Test_category2') == 1
    journal.codex_read('Test_category2', 'Test_topic')
    assert journal.new_entries() == 1
    assert journal.new_codex_entries_in_category('Test_category') == 1
    assert journal.new_codex_entries_in_category('Test_category2') == 0


def test_adding_quests_and_notes(journal):
    assert journal.quests == {}
    journal.start_quest('orciad')
    assert journal.quests == {'orciad': {'new': True, 'state': 'In progress', 'notes': []}}
    assert journal.new_quests() == 1
    assert journal.new_entries() == 1
    journal.quests_read('orciad')
    assert journal.new_quests() == 0
    journal.add_quest_note('orciad', 'note2')
    journal.add_quest_note('orciad', 'note4')
    assert journal.new_quests() == 1
    assert len([rec for rec in journal.quests['orciad']['notes'] if rec['new']]) == 2
    # check that "new" marks on notes are also reset
    journal.quests_read('orciad')
    assert journal.new_quests() == 0
    assert len([rec for rec in journal.quests['orciad']['notes'] if rec['new']]) == 0


def test_quest_note_fields(journal):
    journal.start_quest('orciad')
    journal.add_quest_note('orciad', 'note2')
    assert journal.quests['orciad']['notes'][0] == {'note': 'note2', 'new': True, 'completed': False}


def test_complete_note(journal):
    journal.start_quest('orciad')
    journal.add_quest_note('orciad', 'note2')
    journal.add_quest_note('orciad', 'note3')
    assert journal.new_entries() == 1
    journal.read_all()
    assert journal.new_entries() == 0
    journal.complete_quest_note('orciad', 'note2')
    assert journal.new_entries() == 1
    assert journal.quests['orciad']['notes'][0]['completed'] == True
    assert journal.quests['orciad']['notes'][1]['completed'] == False


def test_adding_duplicate_note(journal):
    journal.start_quest('orciad')
    journal.add_quest_note('orciad', 'note2')
    journal.add_quest_note('orciad', 'note3')
    journal.read_all()
    assert journal.new_entries() == 0
    journal.add_quest_note('orciad', 'note3')
    assert journal.new_entries() == 0


def test_complete_note_twice(journal):
    journal.start_quest('orciad')
    journal.add_quest_note('orciad', 'note4')
    journal.add_quest_note('orciad', 'note1')
    journal.read_all()
    assert journal.new_entries() == 0
    journal.complete_quest_note('orciad', 'note4')
    assert journal.new_entries() == 1
    assert journal.quests['orciad']['notes'][0]['completed'] == True
    # try to complete note again
    journal.read_all()
    journal.complete_quest_note('orciad', 'note4')
    assert journal.new_entries() == 0
    assert journal.quests['orciad']['notes'][0]['completed'] == True


def test_adding_note_to_not_started_quest(journal):
    journal.add_quest_note('orciad', 'note4')
    assert journal.new_entries() == 0
    assert 'orciad' not in journal.quests


def test_completing_note_to_not_started_quest(journal):
    journal.complete_quest_note('orciad', 'note4')
    assert journal.new_entries() == 0
    assert 'orciad' not in journal.quests
