# troops management menu for raids
screen raid_menu(required_mp):
    modal True
    zorder 100
    frame:
        xfill True
        yfill True
        background '#000c'
        frame:
            style_prefix 'small'
            background Frame('gui/stats_border.png', 12, 12)
            align (0.5, 0.5)
            xsize 500
            has vbox
            text 'Create group with military power not less that [required_mp]'
            vbox:
                hbox:
                    frame:
                        style 'raid_menu_text_frame'
                        text 'Orcs: {}/{}'.format(raid_state.troops['orc'], raid_state.available_troops['orc']) style 'raid_menu_text'
                    textbutton '+' action RaidChangeTroop('orc', 1, required_mp)
                    textbutton '-' action RaidChangeTroop('orc', -1, required_mp)
                text 'Equipped orcs: {}/{}'.format(raid_state.equipment['orc'], raid_state.available_equipment['orc'])
            hbox :
                frame:
                    style 'raid_menu_text_frame'
                    text 'Cubis: {}/{}'.format(raid_state.troops['cubi'], raid_state.available_troops['cubi']) style 'raid_menu_text'
                textbutton '+' action RaidChangeTroop('cubi', 1, required_mp)
                textbutton '-' action RaidChangeTroop('cubi', -1, required_mp)
            hbox :
                frame:
                    style 'raid_menu_text_frame'
                    text 'Driders: {}/{}'.format(raid_state.troops['drider'], raid_state.available_troops['drider']) style 'raid_menu_text'
                textbutton '+' action RaidChangeTroop('drider', 1, required_mp)
                textbutton '-' action RaidChangeTroop('drider', -1, required_mp)
            text 'Total military power: {}'.format(raid_state.mp)
            hbox:
                textbutton 'Start' action [RaidStart(required_mp), Hide('raid_menu'), Return()]
                textbutton 'Abort' action [raid_state.reset, Hide('raid_menu'), Return()]

style raid_menu_text_frame is frame:
    background None
    xpadding 0
    ypadding 0
    xysize (200, 65)

style raid_menu_text is text:
    yalign 0.5
    size 30

init python:
    class RaidChangeTroop(Action):
        '''Changes number of given troop_type in current raid'''
        def __init__(self, troop_type, val, required_mp):
            self.troop_type = troop_type
            self.val = val
            self.required_mp = required_mp

        def get_sensitive(self):
            # do not allow to add more troops to raid than needed
            if self.val > 0 and raid_state.mp >= self.required_mp:
                return False
            elif 0 <= raid_state.troops[self.troop_type] + self.val <= raid_state.available_troops[self.troop_type]:
                return True

        def __call__(self):
            raid_state.change_troops(self.troop_type, self.val)
            renpy.restart_interaction()


    class RaidStart(Action):
        '''Finishes troops assignment and starts the raid'''
        def __init__(self, required_mp):
            self.required_mp = required_mp

        def get_sensitive(self):
            if raid_state.mp >= self.required_mp:
                return True

        def __call__(self):
            raid_state.in_raid = True


    class RaidAbort(Action):
        '''Aborts raid assignment'''
        def __call__(self):
            raid_state.reset()
