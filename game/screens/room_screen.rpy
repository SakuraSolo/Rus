# screen for the room of the castle

# initial phrase for a screen (to override greeting) (will not be saved)
define room_screen_initial_phrase = None

screen room_screen(bg, actor, items, operator_uid=None, back_action=None):
    default operator_phrase = None
    # "actor" is an image of operator
    # "operator" is uid of operator (just for choosing dialogues),
    add bg
    add actor xalign 0 yalign 0
    # show custom "back" button or default one
    hbox:
        xpos 20
        ypos 10
        if back_action:
            #textbutton 'Back' action back_action style 'back_button'
            imagebutton action back_action:
                    idle 'gui/button_idle_s.png'
                    hover 'gui/button_hover_s.png'
                    selected 'gui/button_hover_s.png'
        else:
            #textbutton 'Back' action Return() style 'back_button'
            imagebutton action Return():
                    idle 'gui/button_idle_s.png'
                    hover 'gui/button_hover_s.png'
                    selected 'gui/button_hover_s.png'

    # room name
    #$ roomName = actor;
    #if str(actor) != 'None':
    #    frame:
    #        background im.Flip('gui/Generic Buttons/title area.png', horizontal=True, vertical=False)
    #        pos (450 , 20)
    #        xysize (100, 100)
    #    $ nameSplit = actor.split(' ')
    #    $ nameLength = len(nameSplit)
    #    text str(nameSplit[0].capitalize() + '\'s ' +  nameSplit[1].capitalize()) style 'room_caption'
    frame:
        background im.Flip('gui/Generic Buttons/title area.png', horizontal=True, vertical=False)
        pos (450 , 20)
        xysize (100, 100)
        hbox:
            xsize 385
            ypos 28
            text roomName xalign 0.5 yalign 0.5
            # style 'room_title_text'

    #else:
    #    text 'room' style 'room_caption'

    # room actions list (buttons)
    vbox:
        pos (31, 100)
        xsize 350
        spacing 10
        for txt, act_str in items:
            # menu button can have 'pass, 'return', '<label to jump>' or other actions
            # '_operator_talk' to show random phrase from operator
            # ':sm:<menu>' to ShowMenu(<menu>)
            if isinstance(act_str, Action):
                # if act_str is subclass of Action, use it directly
                $ act = act_str
            elif isinstance(act_str, tuple) or isinstance(act_str, list):
                $ act = act_str
            elif act_str == 'pass':
                $ act = (NullAction(), SensitiveIf(False))
            elif act_str == 'return':
                $ act = Return()
            elif act_str == '_operator_talk':
                $ act = SetScreenVariable('operator_phrase', choose_operator_phrase(operator_uid))
            elif act_str.startswith(':sm:'):
                $ act = ShowMenu(act_str[4:])
            else:
                $ act = Jump(act_str)
            textbutton txt action act:
                xfill True
                style 'room_button'
    # greetings/dialogues
    # if operator is set and has greetings
    if operator_uid in operator_greetings:
        frame:
            background Frame('gui/Dialogue box full.png', 12, 12)
            #background Solid('#000a')
            pos (0, 510)
            #pos (290, 510)
            xysize (1280, 225)
            #xysize (800, 65)
        frame:
            background Frame('gui/Dialogue Border.png', 12, 12)
            pos (270, 500)
            xysize (100, 100)
        frame:
            background im.Flip('gui/Dialogue Border.png', horizontal=True, vertical=True)
            pos (900, 520)
            #pos (900, 570)
            xysize (100, 100)
        frame:
            #background Solid('#000a')
            background Null(width=10)
            pos (290, 525)
            xysize (690, 65)
            left_padding 20
            right_padding 0
            if operator_phrase:
                text operator_phrase align (0.0, 0.5) line_spacing 0
    # room menu
#~     frame:
#~         background Frame('gui/stats_border.png', 12, 12)
#~         pos (40, 40)
#~         xysize (400, 640)
#~         vbox:
#~             for txt, act_str in items:
#~                 # menu button can have 'pass, 'return', '<label to jump>' or other actions
#~                 # '_operator_talk' to show random phrase from operator
#~                 # ':sm:<menu>' to ShowMenu(<menu>)
#~                 if isinstance(act_str, Action):
#~                     # if act_str is subclass of Action, use it directly
#~                     $ act = act_str
#~                 elif isinstance(act_str, tuple) or isinstance(act_str, list):
#~                     $ act = act_str
#~                 elif act_str == 'pass':
#~                     $ act = (NullAction(), SensitiveIf(False))
#~                 elif act_str == 'return':
#~                     $ act = Return()
#~                 elif act_str == '_operator_talk':
#~                     $ act = SetScreenVariable('operator_phrase', choose_operator_phrase(operator_uid))
#~                 elif act_str.startswith(':sm:'):
#~                     $ act = ShowMenu(act_str[4:])
#~                 else:
#~                     $ act = Jump(act_str)
#~                 textbutton txt action act:
#~                     xfill True
#~                     xalign 0.5
#~                     style 'small_textbutton'
#~                     text_xalign 0.5
#~                     text_line_spacing 0
#~                     ypadding 15
#~     # greetings/dialogues box
#~     # if operator is set and has greetings
#~     if operator_uid in operator_greetings:
#~         frame:
#~             background Frame('gui/stats_border.png', 12, 12)
#~             pos (480, 530)
#~             xysize (760, 150)
#~             vbox:
#~                 if operator_phrase:
#~                     if operator_uid:
#~                         text operator_greetings[operator_uid][0] bold True
#~                     text operator_phrase
    vbox:
        spacing -10
        align (0.97, 0.015)
        use game_time
        use info_treasury
#~    vbox:
#~        spacing -10
#~        align (0.84, 0.015)
#~Z        use info_treasury
    # debug tools
    if config.developer:
        frame:
            yalign 1.0
            xalign 0.0
            use debug_tools_screen

    # show log messages (`~)
    key '`' action Show('messages')

    # if initial phrase was set, show it in dialog box and erase initial phrase
    if room_screen_initial_phrase:
        on 'show' action [SetScreenVariable('operator_phrase', room_screen_initial_phrase), SetVariable('room_screen_initial_phrase', None)]
    else:
        # else choose random greeting when room is entered
        if operator_uid:
            if actor == 'naked helayna room' and halaynas_display == False and halaynas_day_off:
                on 'show' action Call('Heltest')
            else:
                on 'show' action SetScreenVariable('operator_phrase', renpy.random.choice(operator_greetings[operator_uid][1]))
