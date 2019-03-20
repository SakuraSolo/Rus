screen journal():
    default current_part = None
    modal True
    frame:
        background '#000e'
        xfill True
        yfill True
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            xysize (0.97, 0.97)
            align (0.5, 0.5)
            has vbox
            spacing 5
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xfill True
                hbox:
                    style_prefix 'small'
                    xfill True
                    textbutton 'Close':
                        xsize 140
                        action Hide('journal')
                    textbutton 'Events':
                        xsize 200
                    textbutton 'Quests{}'.format(' (' + str(journal.new_quests()) + ')' if journal.new_quests() else ''):
                        xsize 200
                        if journal.quests:
                            action [SetScreenVariable('current_part', 'journal_quests'), SetVariable('journal_quests_quest', None)]
                    textbutton 'Calendar':
                        xsize 200
                    textbutton 'Codex{}'.format(' (' + str(journal.new_codex_entries()) + ')' if journal.new_codex_entries() else ''):
                        xsize 200
                        action SetScreenVariable('current_part', 'journal_codex')
                    textbutton 'Glossary{}'.format(' (' + str(journal.new_glossary_entries()) + ')' if journal.new_glossary_entries() else ''):
                        xsize 200
                        action SetScreenVariable('current_part', 'journal_glossary')
            if current_part == 'journal_glossary':
                use journal_glossary
            elif current_part == 'journal_codex':
                use journal_codex
            elif current_part == 'journal_quests':
                use journal_quests
            else:
                frame:
                    background Frame('gui/stats_border.png', 12, 12)


# selected category in glossary
define journal_glossary_category = None

screen journal_glossary():
    frame:
        background None
        xfill True
        yfill True
        hbox:
            spacing 5
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xsize 0.3
                yfill True
                vpgrid:
                    cols 1
                    mousewheel True
                    scrollbars "vertical"
                    yminimum 0.99
                    style_prefix 'menu_list'
                    for category in sorted(journal.glossary):
                        textbutton category action [SetVariable('journal_glossary_category', category), GlossaryResetNew(category)]:
                            if journal.glossary[category]['new']:
                                text_color cl_good
            if journal_glossary_category:
                frame:
                    background Frame('gui/stats_border.png', 12, 12)
                    xfill True
                    yfill True
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        yfill True
                        vbox:
                            spacing 5
                            for entry in journal.glossary[journal_glossary_category]['entries']:
                                text glossary_entries[entry][1]


# selected category and topic in codex
define journal_codex_category = None
define journal_codex_topic = None

screen journal_codex():
    frame:
        background None
        xfill True
        yfill True
        hbox:
            spacing 5
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xsize 0.3
                yfill True
                vpgrid:
                    cols 1
                    mousewheel True
                    scrollbars "vertical"
                    yminimum 570
                    style_prefix 'menu_list'
                    for category in sorted(journal.codex):
                        textbutton category:
                            action [SetVariable('journal_codex_topic', None), SetVariable('journal_codex_category', category), SelectedIf(journal_codex_category == category)]
                            if journal.new_codex_entries_in_category(category):
                                text_color cl_good
                        # if current category is selected one, show its topics
                        if category == journal_codex_category:
                            for topic in journal.codex[category]:
                                textbutton topic:
                                    action [SetVariable('journal_codex_topic', topic), CodexResetNew(category, topic)]
                                    left_margin 25
                                    if journal.codex[category][topic]['new']:
                                        text_color cl_good
            if journal_codex_topic and journal_codex_category:
                frame:
                    background Frame('gui/stats_border.png', 12, 12)
                    xfill True
                    yfill True
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        yfill True
                        vbox:
                            spacing 5
                            for entry in journal.codex[journal_codex_category][journal_codex_topic]['entries']:
                                text codex_entries[entry][2]


# selected quest in quests log
define journal_quests_quest = None
# new entries in selected quest
define journal_quests_current_new_notes = []


screen journal_quests():
    frame:
        background None
        xfill True
        yfill True
        hbox:
            spacing 5
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xsize 0.3
                yfill True
                vpgrid:
                    cols 1
                    mousewheel True
                    scrollbars "vertical"
                    yminimum 570
                    xfill True
                    style_prefix 'menu_list'
                    for quest in sorted(journal.quests):
                        textbutton quests_entries[quest]['title']:
                            action [SetVariable('journal_quests_quest', quest), QuestsResetNew(quest)]
                            if journal.quests[quest]['new']:
                                text_color cl_good
                            elif journal.quests[quest]['state'] == 'Completed':
                                text_color cl_completed
            if journal_quests_quest:
                frame:
                    background Frame('gui/stats_border.png', 12, 12)
                    xfill True
                    yfill True
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        yfill True
                        vbox:
                            spacing 10
                            frame:
                                background Frame('gui/stats_border.png', 12, 12)
                                xfill True
                                has vbox

                                hbox:
                                    pos (15, 15)
                                    text quests_entries[journal_quests_quest]['title'] bold True size 30
                                    null width 50
                                    text journal.quests[journal_quests_quest]['state']
                                hbox:
                                    pos (15, 0)
                                    xsize 810
                                    text quests_entries[journal_quests_quest]['descr']
                            for record in journal.quests[journal_quests_quest]['notes']:
                                hbox:
                                    pos (15, 0)
                                    xsize 810
                                    text quests_entries[journal_quests_quest]['notes'][record['note']]:
                                        if record['note'] in journal_quests_current_new_notes:
                                            color cl_good
                                        elif record['completed']:
                                            color cl_completed


# screen with journal button, to include in other screens
screen journal_button(align = None):
    if hasattr(store, 'journal'):
        if journal._show:
            button:
                if align:
                    align align
                style 'quick_button'
                action Show('journal')
                text 'Journal{}'.format(' {color=#b31418}(' + str(journal.new_entries()) + '){/color}' if journal.new_entries() else ''):
                    line_spacing 0
                    size 16
                    color '#d5d3d4'
                    hover_color '#999'

#~                 if journal.new_entries():
#~                     text_color cl_good


init python:
    class GlossaryResetNew(Action):
        '''Resets "new" state of category'''
        def __init__(self, category):
            self.category = category

        def __call__(self):
            glossary_read(self.category)


    class CodexResetNew(Action):
        '''Resets "new" state of codex'''
        def __init__(self, category, topic):
            self.category = category
            self.topic = topic

        def __call__(self):
            codex_read(self.category, self.topic)


    class QuestsResetNew(Action):
        '''Resets "new" state of a quest'''
        def __init__(self, quest):
            self.quest = quest

        def __call__(self):
            # store new notes, to highlight them
            global journal_quests_current_new_notes
            journal_quests_current_new_notes = []
            for note in journal.quests[self.quest]['notes']:
                if note['new']:
                    journal_quests_current_new_notes.append(note['note'])
            # mark all notes in a quest as read
            journal.quests_read(self.quest)
