# dungeon - manage prisoners
screen manage_prisoners_screen():
    frame:
        background 'gui/UI_Screens/UIScreen_CastleDungeon.png'
        pos (-1, -1)
        textbutton 'Back' action Return() style 'back_button'
        text 'Dungeon' style 'room_caption'
        vbox:
            pos (34, 114)
            spacing 25
            # list of actions
            frame:
                background 'listbox_border'
                xsize 486
                xpadding 3
                ypadding 3
                vbox:
                    frame:
                        background None
                        ysize 64
                        xfill True
                        text "{} prisoners in dungeon".format(castle.buildings['dungeon'].prisoners) align (0.5, 0.5) line_spacing 0
                    frame:
                        style 'dungeon_frame'
                        text 'Sell as slave' pos (15, 15)
                        text '+5 treasury' size 20 color '#686868' pos (15, 40)
                        hbox:
                            style 'dungeon_hbox'
                            textbutton '+1' action SellPrisonerAsSlave():
                                style 'rcrect_button'
                            textbutton 'Max' action SellMaxPrisonersAsSlave():
                                style 'rcrect_button'
                            textbutton 'Auto' action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'slave'):
                                style 'rcrect_button'
                    frame:
                        style 'dungeon_frame'
                        text 'Ransom' pos (15, 15)
                        text '+10 treasury' size 20 color '#686868' pos (15, 40)
                        hbox:
                            style 'dungeon_hbox'
                            textbutton '+1' action RansomPrisoner():
                                style 'rcrect_button'
                            textbutton 'Max' action RansomMaxPrisoners():
                                style 'rcrect_button'
                            textbutton 'Auto' action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'ransom'):
                                style 'rcrect_button'
                    frame:
                        style 'dungeon_frame'
                        text 'Make gladiator' pos (15, 15)
                        text '+3 moral' size 20 color '#686868' pos (15, 40)
                        hbox:
                            style 'dungeon_hbox'
                            textbutton '+1' action MakeGladiatorPrisoner():
                                style 'rcrect_button'
                            textbutton 'Max' action MakeGladiatorMaxPrisoners():
                                style 'rcrect_button'
                            textbutton 'Auto' action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'gladiator'):
                                style 'rcrect_button'
                    frame:
                        style 'dungeon_frame'
                        text 'Make test subject' pos (15, 15)
                        text '+2 research points' size 20 color '#686868' pos (15, 40)
                        hbox:
                            style 'dungeon_hbox'
                            textbutton '+1' action TestSubjectPrisoner():
                                style 'rcrect_button'
                            textbutton 'Max' action TestSubjectMaxPrisoners():
                                style 'rcrect_button'
                            textbutton 'Auto' action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'test'):
                                style 'rcrect_button'
            hbox:
                spacing 15
                textbutton 'Fully automate all' action FullyAutomatePrisoners() style 'room_button'
                textbutton 'Disable auto' action UnAutomatePrisoners() style 'room_button'
    vbox:
        spacing -10
        align (0.97, 0.05)
        use game_time
        use info_treasury


init 1:
    style dungeon_frame is frame:
        background 'button_border'
        xfill True
        ysize 72


    style dungeon_hbox is hbox:
        xpos 270
        yalign 0.5
        spacing 10


    style dungeon_roundbox_button is textbutton:
        background 'round_rect'
        xpadding 15
        ypadding 10


    style dungeon_roundbox_button_text is text:
        line_spacing 0
        align (0.5, 0.5)


#~     frame:
#~         style "big_frame"
#~         # top panel - 'Close' button
#~         has vbox
#~         spacing 5
#~         frame:
#~             style "horiz_panel"
#~             hbox:
#~                 spacing 20
#~                 textbutton 'Close' action Return() style 'navi_button'
#~         # controls for managing prisoners
#~         frame:
#~             style 'big_frame'
#~             viewport:
#~                 style "big_viewport"
#~                 mousewheel True
#~                 scrollbars 'vertical'
#~                 # show number of prisoners and controls
#~                 vbox:
#~                     style_prefix 'small'
#~                     spacing 5
#~                     text "Prisoners in dungeon: {}".format(castle.buildings['dungeon'].prisoners)
#~                     frame:
#~                         style "horiz_panel"
#~                         has vbox
#~                         text "Sell prisoners as slaves (+5 treasury)"
#~                         hbox:
#~                             textbutton "Sell 1" action SellPrisonerAsSlave()
#~                             textbutton "Sell max" action SellMaxPrisonersAsSlave()
#~                             textbutton "Auto sell" action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'slave')
#~                     if castle.buildings['tavern'].lvl >= 1:
#~                         frame:
#~                             style "horiz_panel"
#~                             has vbox
#~                             text "Ransom prisoners (+10 treasury)"
#~                             hbox:
#~                                 textbutton "Ransom 1" action RansomPrisoner()
#~                                 textbutton "Ransom max" action RansomMaxPrisoners()
#~                                 textbutton "Auto ransom" action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'ransom')
#~                     if castle.buildings['arena'].lvl >= 1:
#~                         frame:
#~                             style "horiz_panel"
#~                             has vbox
#~                             text "Make gladiator (+3 morale)"
#~                             hbox:
#~                                 textbutton "Turn over 1" action MakeGladiatorPrisoner()
#~                                 textbutton "Turn over max" action MakeGladiatorMaxPrisoners()
#~                                 textbutton "Auto turn over" action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'gladiator')
#~                     if castle.buildings['sanctum'].lvl >= 1:
#~                         frame:
#~                             style "horiz_panel"
#~                             has vbox
#~                             text "Make test subject (+2 research points)"
#~                             hbox:
#~                                 textbutton "Turn over 1" action TestSubjectPrisoner()
#~                                 textbutton "Turn over max" action TestSubjectMaxPrisoners()
#~                                 textbutton "Auto turn over" action ToggleDict(castle.buildings['dungeon'].prisoners_auto, 'test')
#~                     frame:
#~                         style "horiz_panel"
#~                         has hbox
#~                         textbutton 'Fully automate prisoners' action FullyAutomatePrisoners()
#~                         textbutton 'Disable all automatic prisoner use' action UnAutomatePrisoners()


init python:
    class SellPrisonerAsSlave(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['slave'][0] < castle.buildings['dungeon'].prisoners_status['slave'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            castle.buildings['dungeon'].prisoners_status['slave'][0] += 1
            castle.buildings['dungeon'].prisoners -= 1
            castle.treasury += 5
            renpy.restart_interaction()


    class SellMaxPrisonersAsSlave(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['slave'][0] < castle.buildings['dungeon'].prisoners_status['slave'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            to_sell = min(castle.buildings['dungeon'].prisoners_status['slave'][1] - castle.buildings['dungeon'].prisoners_status['slave'][0], castle.buildings['dungeon'].prisoners)
            castle.buildings['dungeon'].prisoners_status['slave'][0] += to_sell
            castle.buildings['dungeon'].prisoners -= to_sell
            castle.treasury += 5 * to_sell
            renpy.restart_interaction()


    class RansomPrisoner(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['ransom'][0] < castle.buildings['dungeon'].prisoners_status['ransom'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            castle.buildings['dungeon'].prisoners_status['ransom'][0] += 1
            castle.buildings['dungeon'].prisoners -= 1
            castle.treasury += 10
            renpy.restart_interaction()


    class RansomMaxPrisoners(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['ransom'][0] < castle.buildings['dungeon'].prisoners_status['ransom'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            to_sell = min(castle.buildings['dungeon'].prisoners_status['ransom'][1] - castle.buildings['dungeon'].prisoners_status['ransom'][0], castle.buildings['dungeon'].prisoners)
            castle.buildings['dungeon'].prisoners_status['ransom'][0] += to_sell
            castle.buildings['dungeon'].prisoners -= to_sell
            castle.treasury += 10 * to_sell
            renpy.restart_interaction()


    class MakeGladiatorPrisoner(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['gladiator'][0] < castle.buildings['dungeon'].prisoners_status['gladiator'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            castle.buildings['dungeon'].prisoners_status['gladiator'][0] += 1
            castle.buildings['dungeon'].prisoners -= 1
            castle.morale += 3
            renpy.restart_interaction()


    class MakeGladiatorMaxPrisoners(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['gladiator'][0] < castle.buildings['dungeon'].prisoners_status['ransom'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            to_sell = min(castle.buildings['dungeon'].prisoners_status['gladiator'][1] - castle.buildings['dungeon'].prisoners_status['gladiator'][0], castle.buildings['dungeon'].prisoners)
            castle.buildings['dungeon'].prisoners_status['gladiator'][0] += to_sell
            castle.buildings['dungeon'].prisoners -= to_sell
            castle.morale += 3 * to_sell
            renpy.restart_interaction()


    class TestSubjectPrisoner(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['test'][0] < castle.buildings['dungeon'].prisoners_status['test'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            castle.buildings['dungeon'].prisoners_status['test'][0] += 1
            castle.buildings['dungeon'].prisoners -= 1
            castle.rp += 2
            renpy.restart_interaction()


    class TestSubjectMaxPrisoners(Action):
        def get_sensitive(self):
            # allows to sell prisoners if limit for current week is not used up
            return (castle.buildings['dungeon'].prisoners_status['test'][0] < castle.buildings['dungeon'].prisoners_status['test'][1]) and castle.buildings['dungeon'].prisoners > 0

        def __call__(self):
            to_sell = min(castle.buildings['dungeon'].prisoners_status['test'][1] - castle.buildings['dungeon'].prisoners_status['test'][0], castle.buildings['dungeon'].prisoners)
            castle.buildings['dungeon'].prisoners_status['test'][0] += to_sell
            castle.buildings['dungeon'].prisoners -= to_sell
            castle.rp += 2 * to_sell
            renpy.restart_interaction()

    class FullyAutomatePrisoners(Action):
        def __call__(self):
            # enable automation for all options that have related building built
            castle.buildings['dungeon'].prisoners_auto['slave'] = True
            if castle.buildings['tavern'].lvl >= 1:
                castle.buildings['dungeon'].prisoners_auto['ransom'] = True
            if castle.buildings['sanctum'].lvl >= 1:
                castle.buildings['dungeon'].prisoners_auto['test'] = True
            if castle.buildings['arena'].lvl >= 1:
                castle.buildings['dungeon'].prisoners_auto['gladiator'] = True
            renpy.restart_interaction()


    class UnAutomatePrisoners(Action):
        def __call__(self):
            # disable automation for all options
            castle.buildings['dungeon'].prisoners_auto['slave'] = False
            castle.buildings['dungeon'].prisoners_auto['ransom'] = False
            castle.buildings['dungeon'].prisoners_auto['test'] = False
            castle.buildings['dungeon'].prisoners_auto['gladiator'] = False
            renpy.restart_interaction()
