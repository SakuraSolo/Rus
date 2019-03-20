# screen for the guest room of the castle, controls for NPC actions
screen npc_controls(bg, actor):
    add bg
    # TODO: use actor's image
    add actor.outfit_img xalign 0.5 yalign 1.0
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        pos (40, 40)
        xysize (400, 640)
        style_prefix 'menu_list'
        has vbox
        textbutton 'Schedule...' action ShowTransient('schedule_npc', actor=actor)
        textbutton 'Give gift...' action ShowTransient('give_gift_screen', actor=actor)
        textbutton 'Change outfit...' action ShowTransient('change_outfit_screen', actor=actor)
        textbutton 'Talk...' action ShowTransient('choose_titles_screen', actor=actor)
        textbutton 'Leave' action Return()
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        ypos 40
        xalign 1.0
        xoffset -40
        xysize (300, 640)
        has vbox
        spacing 5
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            xfill True
            text actor.name size 30 xalign 0.5
        for stat in actor_public_stats_st:
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xfill True
                text '{}: {}'.format(stat.capitalize(), getattr(actor, stat))
    # debug screen for NPC
    default npc_debug_details = False
    if config.developer:
        frame:
            xpos 0.35
            use npc_debug(actor, npc_debug_details)


# menu for choosing a job/training for a npc to do
screen schedule_npc(actor):
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        pos (480, 40)
        xysize (400, 640)
        style_prefix 'menu_list'
        has vbox
        textbutton 'Close' action Hide('schedule_npc')
        text 'Training coffers: [castle.training_coffers]' xalign 0.5
        viewport:
            mousewheel True
            scrollbars 'vertical'
            vbox:
                textbutton 'Rest' action (Hide('schedule_npc'), SetDict(castle.schedule, actor.uid, 'rest'), SelectedIf(castle.schedule.get(actor.uid, None) == 'rest'))
                text 'Jobs' size 30 xalign 0.5 color '#fff'
                for job in castle.jobs:
                    if job.type == 'job':
                        textbutton '{} {}E'.format(job.name, job.energy_cost):
                            action (Hide('schedule_npc'), ScheduleJob(actor, job))
                text 'Trainings' size 30 xalign 0.5 color '#fff'
                for job in castle.jobs:
                    if job.type == 'training':
                        # show name, needed/current levels, energy cost and price for training
                        textbutton '{} ({}/{}) {}E {}G'.format(job.name, job.needed_level(actor) + 1, job.level + 1, job.energy_cost, job.cost(actor)):
                            action (Hide('schedule_npc'), ScheduleJob(actor, job))


screen give_gift_screen(actor):
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        pos (480, 40)
        xysize (300, 640)
        style_prefix 'menu_list'
        has vbox
        textbutton 'Close' action Hide('give_gift_screen')
        text 'Give gift' color '#fff' xalign 0.5 size 30
        viewport:
            mousewheel True
            scrollbars 'vertical'
            vbox:
                for item in avatar.inventory.bp:
                    if item.uid in gift_affinity:
                        textbutton '{} - {} +{}'.format(avatar.inventory.bp[item], item.name, gift_affinity[item.uid]):
                            action (Hide('give_gift_screen'), GiveGift(item, actor))


# menu for choosing titles (player/NPC)
screen choose_titles_screen(actor):
    default title_for = ''
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        pos (480, 40)
        xysize (300, 640)
        style_prefix 'menu_list'
        has vbox
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            has vbox
            textbutton 'Close' action Hide('choose_titles_screen')
            textbutton 'Address me as...' action SetScreenVariable('title_for', 'player')
            textbutton 'Address yourself as...' action SetScreenVariable('title_for', 'self')
        if title_for == 'player':
            vpgrid:
                cols 1
                spacing 5
                mousewheel True
                for t in titles_player:
                    button action (Hide('choose_titles_screen'), SetPlayerTitle(actor, t)):
                        idle_child Text(t, style='menu_list_button_text')
                        hover_child Text(t, style='menu_list_button_text')
                        insensitive_child Text('???', style='menu_list_button_text')
        if title_for == 'self':
            vpgrid:
                cols 1
                spacing 5
                mousewheel True
                # TODO: it is same button as above
                for t in titles_self:
                    button action (Hide('choose_titles_screen'), SetSelfTitle(actor, t)):
                        idle_child Text(t, style='menu_list_button_text')
                        hover_child Text(t, style='menu_list_button_text')
                        insensitive_child Text('???', style='menu_list_button_text')


# small screen with input to enter a custom title
screen input_title_screen(actor, for_):
    modal True
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        align (0.5, 0.5)
        xsize 350
        style_prefix 'menu_list'
        has vbox
        if for_ == 'self':
            text '{}, address yourself as'.format(actor.name)
            input value FieldInputValue(actor, 'self_title') length 30
        elif for_ == 'player':
            text '{}, address me as'.format(actor.name)
            input value FieldInputValue(actor, 'player_title') length 30
        textbutton 'Close':
            if for_ == 'self':
                action (Hide('input_title_screen'), Jump(actor.uid + '_confirm_self_title'))
            elif for_ == 'player':
                action (Hide('input_title_screen'), Jump(actor.uid + '_confirm_player_title'))


# a confirmation message after scheduling
screen schedule_confirmation_screen(actor):
    modal True
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        align (0.5, 0.5)
        xsize 350
        style_prefix 'menu_list'
        has vbox
        text '{} is scheduled for {}'.format(castle.jobs[castle.schedule[actor.uid]].name, actor.name)
        textbutton 'Ok' action Hide('schedule_confirmation_screen') xalign 0.5


screen low_energy_schedule_screen(actor, job):
    modal True
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        align (0.5, 0.5)
        xsize 350
        style_prefix 'menu_list'
        has vbox
        text '{}\'s energy is low which will result in a penalty, do you still want to schedule {}?'.format(actor.name, job.name)
        textbutton 'No' action Hide('low_energy_schedule_screen')
        textbutton 'Yes' action (SetDict(castle.schedule, actor.uid, job.uid), Hide('low_energy_schedule_screen'), Show('schedule_confirmation_screen', actor=actor))


screen change_outfit_screen(actor):
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        pos (480, 40)
        xysize (300, 640)
        style_prefix 'menu_list'
        has vbox
        textbutton 'Close' action Hide('change_outfit_screen')
        for uid in actor.outfits:
            textbutton actor._all_outfits[uid][0] action (SetField(actor, 'outfit', uid), SensitiveIf(actor.outfit_req(uid)))


init python:
    class SetSelfTitle(Action):
        '''Set how NPC will address self'''
        def __init__(self, actor, title):
            self.actor = actor
            self.title = title

        def get_sensitive(self):
            req_met = True
            if titles_self[self.title]:
                for stat in titles_self[self.title]:
                    if getattr(self.actor, stat) <= titles_self[self.title][stat]:
                        # if any requirement is not met, title is locked
                        req_met = False
            if self.title == 'Wife' and self.actor.uid == 'alexia':
                req_met = True
            return req_met

        def __call__(self):
            if self.title == 'I':
                self.actor.self_title = self.title
                renpy.jump(self.actor.uid + '_confirm_self_title')
            elif self.title == 'Custom...':
                # title confirmation screen is jumped to from input_title_screen after input
                renpy.show_screen('input_title_screen', actor=self.actor, for_='self')
            else:
                self.actor.self_title = 'your ' + self.title.lower()
                renpy.jump(self.actor.uid + '_confirm_self_title')


    class SetPlayerTitle(Action):
        '''Set how NPC will address player'''
        def __init__(self, actor, title):
            self.actor = actor
            self.title = title

        def get_sensitive(self):
            req_met = True
            if titles_player[self.title]:
                for stat in titles_player[self.title]:
                    if getattr(self.actor, stat) <= titles_player[self.title][stat]:
                        # if any requirement is not met, title is locked
                        req_met = False
            if self.title == 'Husband' and self.actor.uid == 'alexia':
                req_met = True
            return req_met

        def __call__(self):
            if self.title == 'Rowan':
                self.actor.player_title = self.title
                renpy.jump(self.actor.uid + '_confirm_player_title')
            elif self.title == 'Custom...':
                # title confirmation screen is jumped to from input_title_screen after input
                renpy.show_screen('input_title_screen', actor=self.actor, for_='player')
            else:
                self.actor.player_title = 'my ' + self.title.lower()
                renpy.jump(self.actor.uid + '_confirm_player_title')


    class GiveGift(Action):
        def __init__(self, item, actor):
            self.item = item
            self.actor = actor

        def get_sensitive(self):
            return avatar.inventory.bp[self.item] > 0

        def __call__(self):
            avatar.inventory.remove(self.item.uid)
            self.actor.affinity += gift_affinity[self.item.uid]


    class ScheduleJob(Action):
        def __init__(self, actor, job):
            self.actor = actor
            self.job = job

        def get_sensitive(self):
            return self.job.req_met(self.actor)

        def get_selected(self):
            return self.job.uid == castle.schedule.get(self.actor.uid, None)

        def __call__(self):
            # if actor has enough energy for the job, schedule and show message
            if self.actor.energy >= self.job.energy_cost:
                castle.schedule[self.actor.uid] = self.job.uid
                renpy.show_screen('schedule_confirmation_screen', actor=self.actor)
            # if actor has less energy than needed, show the screen for making desision
            else:
                renpy.show_screen('low_energy_schedule_screen', actor=self.actor, job=self.job)
