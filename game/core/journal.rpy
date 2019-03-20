# journal and its parts
init python:

    class Journal(object):

        def __init__(self):
            self.glossary = {}
            self.codex = {}
            self.quests = {}
            # if True, journal controls should be shown
            self._show = True

        def show(self):
            self._show = True

        def hide(self):
            self._show = False

        def read_all(self):
            '''Mark all entries in codex and glossary as read'''
            for cat in self.glossary:
                self.glossary[cat]['new'] = False
            for cat in self.codex:
                for topic in self.codex[cat]:
                    self.codex[cat][topic]['new'] = False
            for quest in self.quests:
                self.quests[quest]['new'] = False
                for note in self.quests[quest]['notes']:
                    note['new'] = False

        def new_entries(self):
            '''Returns number of new entries in any part'''
            return self.new_glossary_entries() + self.new_codex_entries() + self.new_quests()

        def new_glossary_entries(self):
            '''Returns amount of new entries in glossary'''
            return len([entry for entry in self.glossary if self.glossary[entry]['new']])

        def new_codex_entries(self):
            '''Returns amount of new entries in codex'''
            new_entries = 0
            for category in self.codex:
                for topic in self.codex[category]:
                    if self.codex[category][topic]['new']:
                        new_entries += 1
            return new_entries

        def new_codex_entries_in_category(self, category):
            '''Returns amount of new entries in codex in given category'''
            new_entries = 0
            if category in self.codex:
                for topic in self.codex[category]:
                    if self.codex[category][topic]['new']:
                        new_entries += 1
            return new_entries

        def new_quests(self):
            '''Returns number of new/changed quests'''
            return len([quest for quest in self.quests if self.quests[quest]['new']])

        def glossary_add(self, entry_uid):
            '''Adds entry in entry\'s category and marks category as "new"'''
            if entry_uid in glossary_entries:
                category = glossary_entries[entry_uid][0]
                self.glossary.setdefault(category, {'entries': [], 'new': False})
                if entry_uid not in journal.glossary[category]['entries']:
                    self.glossary[category]['entries'].append(entry_uid)
                    self.glossary[category]['new'] = True

        def glossary_read(self, category):
            '''Resets "new" flag on given glossary category'''
            self.glossary[category]['new'] = False

        def codex_add(self, entry_uid):
            '''Adds entry in entry\'s category and topic, and marks topic as "new"'''
            if entry_uid in codex_entries:
                category = codex_entries[entry_uid][0]
                topic = codex_entries[entry_uid][1]
                self.codex.setdefault(category, {})
                self.codex[category].setdefault(topic, {'entries': [], 'new': False})
                if entry_uid not in journal.codex[category][topic]['entries']:
                    self.codex[category][topic]['entries'].append(entry_uid)
                    self.codex[category][topic]['new'] = True

        def codex_read(self, category, topic):
            '''Resets "new" flag on given category and topic in codex'''
            self.codex[category][topic]['new'] = False

        def start_quest(self, quest):
            '''Starts quest - adds in to the journal'''
            if quest not in self.quests:
                self.quests[quest] = {'state': 'In progress', 'new': True, 'notes': []}

        def quests_read(self, quest):
            '''Marks a quest as read (and all its notes)'''
            self.quests[quest]['new'] = False
            for record in self.quests[quest]['notes']:
                record['new'] = False

        def add_quest_note(self, quest, note):
            '''Adds a note to the quest, if it not in quest already'''
            if quest in self.quests:
                # check if this note is already in the quest
                for record in self.quests[quest]['notes']:
                    if record['note'] == note:
                        return
                self.quests[quest]['notes'].append({'note': note, 'new': True, 'completed': False})
                self.quests[quest]['new'] = True

        def complete_quest_note(self, quest, note):
            '''Marks a note of given quest as "completed"'''
            if quest in self.quests:
                for record in self.quests[quest]['notes']:
                    if record['note'] == note and not record['completed']:
                        record['completed'] = True
                        self.quests[quest]['new'] = True
