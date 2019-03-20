# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.



##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
#~     add "gui/gm_back2.png"
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 1
            for caption, action, chosen in items:
                if action:
                    button at nav_eff:
                        action action
                        style "menu_choice_button"
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"
    # show temporary event vars
    if config.developer:
        use event_tmp_debug

init -2:
    $ config.narrator_menu = True
    style menu_window is default
    style menu_choice is button_text:
        clear
    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)
    style menu_choice_frame:
        background None
    style menu_choice_button:
#~         idle_background Frame("gui/button_idle.png", 25, 25)
#~         hover_background Frame("gui/button_hover.png", 25, 25)
#~         insensitive_background Frame(im.Grayscale("gui/button_idle.png"), 25, 25)
#~         selected_idle_background Frame("gui/button_hover.png", 25, 25)
        idle_background 'room_button'
        hover_background 'room_button_hover'
        selected_background 'room_button_hover'
        insensitive_background 'room_button_grey'
        top_padding 10
        bottom_padding 15
        xsize 1000
        ysize 65
        ymargin 5
    style menu_choice:
        xalign 0.5
        text_align 0.5
        yalign 0.5
        size 20
        bold True
        kerning 2
        outlines [(1, "#000", 0, 0)]
#~         idle_color "#fff"
#~         hover_color "#fff"
        idle_color '#575559'
        hover_color '#9c979b'
        insensitive_color '#373539'
        line_spacing 0


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    window style "input_window":
        has vbox
        text prompt style "input_prompt"
        input id "input" style "input_text"
    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    default bonus = False
    tag menu
    add "gui/title_back.jpg"
    #add "gui/logo_large.png" at logo_eff:
    add "gui/logo_large.png":
        #xalign -0.05
        #yalign 0.34
        xalign 0.09
        yalign 0.24
    frame:
        style_group "mm"
        xalign 0.09
        yalign 0.83
        if not bonus:
            vbox:
                hbox:
                    textbutton _("Start Game") action Start() at nav_eff
                    textbutton _("Load Game") action ShowMenu("load") at nav_eff
                    textbutton _("Preferences") action ShowMenu("preferences") at nav_eff
                    textbutton _("{color=#F6080C}More Games{/color}") action OpenURL("https://discord.gg/AxyR9Wu") at nav_eff
                null height -4
                hbox:
                    textbutton _("Help") action Help() at nav_eff
                    textbutton _("Bonus") action SetScreenVariable("bonus", True) at nav_eff
                    textbutton _("Quit Game") action Quit(confirm=False) at nav_eff
                null height -4
                hbox:
                    xpos 5
                    ypos 70

                    imagebutton action OpenURL("https://www.patreon.com/LordArioch"):
                        idle 'gui/Generic Buttons/button_patreon_t.png'
                        hover 'gui/Generic Buttons/button_patreon.png'
                        selected 'gui/Generic Buttons/button_patreon.png'

                    hbox:
                        xsize 30

                    imagebutton action OpenURL("https://twitter.com/venusnoiregames"):
                        idle 'gui/Generic Buttons/button_twitter_T.png'
                        hover 'gui/Generic Buttons/button_twitter.png'
                        selected 'gui/Generic Buttons/button_twitter.png'

                #hbox:
                    # button with link to Patreon
                    #textbutton "Patreon" action OpenURL("https://www.patreon.com/LordArioch") align (0.01, 0.99) style "mm_button"

        # show "bonus" menu if related button was clicked
        else:
            vbox:
                # TODO: layout this better
                null height 160
                hbox:
                    textbutton _("CG Gallery") action Show("cg_gallery", g_cg=regular_gallery, cg_seq=gallery_cg_items) at nav_eff
                    textbutton _("Training Gallery") action Show("cg_gallery", g_cg=training_gallery, cg_seq=training_cg_items) at nav_eff
                hbox:
                    textbutton _("Jukebox") action Show("music_room") at nav_eff
                    textbutton _("Scene Replay") action ShowMenu("scene_replay") at nav_eff
                null height -4
                hbox:
                    xalign 0.5
                    textbutton _("Return") action SetScreenVariable("bonus", False) at nav_eff
                    textbutton _("Slave Training") action Start('start_training') at nav_eff
    # button to map previews
    if config.developer:
        textbutton 'Preview maps' action Start('map_preview')

init -2:
    style mm_frame:
        background None
    style mm_button:
        idle_background "gui/button_idle.png"
        hover_background "gui/button_hover.png"
        insensitive_background im.Grayscale("gui/button_idle.png")
        selected_idle_background "gui/button_hover.png"
        xminimum 252
        xmaximum 252
        ymaximum 61
        yminimum 61
        ymargin 5
        top_padding 20
    style mm_button_text:
        xalign 0.5
        text_align 0.5
        yalign 0.5
        size 18
        bold True
        kerning 2
        outlines [(1, "#000", 0, 0)]
        idle_color "#fff"
        hover_color "#fff"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigatio

screen pause_menu():
    modal True
    add "gui/gm_back2.png"
    frame:
        background Frame("gui/paper_back.png", 20, 20)
        xalign 0.25
        yalign 0.88
        xmaximum 689
        ymaximum 208
        xpadding 40
        ypadding 25
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 689
            ymaximum 208
            text "{size=25}Thank You!{/size}"
            null height -5
            text "{size=20}Thanks for playing, it wouldn't be possible without the support of all of you. Please consider contributing to the Patreon, so we can continue to make the game we want to create.{/size}":
                line_spacing -2
    frame:
        background Frame("gui/paper_back.png", 20, 20)
        xalign 0.23
        yalign 0.25
        xmaximum 680
        xminimum 680
        ymaximum 400
        yminimum 400
        xpadding 10
        ypadding 10
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 680
            ymaximum 400
            add "gui/pause_image1.jpg"
    vbox:
        add Frame("gui/frame3.png", 20, 20)
        xalign 0.22
        yalign 0.245
        xmaximum 710
        xminimum 710
        ymaximum 430
        yminimum 430

    use navigation

screen navigation():
    vbox:
        add "gui/nav_frame.png"
        xalign 1.0
        yalign 0.5
    vbox:
        style_group "navi"
        yalign 0.5
        xalign 0.99
        textbutton _("Return") action Return() at nav_eff
        if not main_menu:
            textbutton _("Save Game") action (ShowMenu("save"), Hide("pause_menu"), SensitiveIf(saving_allowed)) at nav_eff
        textbutton _("Load Game") action (ShowMenu("load"), Hide("pause_menu")) at nav_eff
        textbutton _("Preferences") action (ShowMenu("preferences"), Hide("pause_menu")) at nav_eff
        if not main_menu:
            textbutton _("Main Menu") action MainMenu() at nav_eff
        textbutton _("Help") action Help() at nav_eff
        textbutton _("Quit") action Quit() at nav_eff

screen bonus_navigation():
    vbox:
        add "gui/nav_frame.png"
        xalign 1.0
        yalign 0.5
    vbox:
        style_group "navi"
        yalign 0.5
        xalign 0.99
        textbutton _("Return") action Return() at nav_eff
        textbutton _("CG Gallery") action Show("cg_gallery", g_cg=regular_gallery, cg_seq=gallery_cg_items) at nav_eff
        textbutton _("Training Gallery") action Show("cg_gallery", g_cg=training_gallery, cg_seq=training_cg_items) at nav_eff
        textbutton _("Jukebox") action Show("music_room") at nav_eff
        textbutton _("Scene Replay") action ShowMenu("scene_replay") at nav_eff
        textbutton _("Help") action Help() at nav_eff
        textbutton _("Quit") action Quit() at nav_eff

init -2:
    style navi_frame:
        background None
    style navi_button:
        idle_background "gui/button_idle.png"
        hover_background "gui/button_hover.png"
        insensitive_background im.Grayscale("gui/button_idle.png")
        selected_idle_background "gui/button_hover.png"
        xminimum 252
        xmaximum 252
        ymaximum 61
        yminimum 61
        ymargin 5
        top_padding 20
    style navi_button_text:
        xalign 0.5
        text_align 0.5
        yalign 0.5
        size 20
        kerning 2
        outlines [(1, "#000", 0, 0)]
        idle_color "#fff"
        hover_color "#fff"



##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():
    vbox:
        add "gui/frame.png"
        xalign 0.05
        yalign 0.5
    vbox:
        style "file_picker_frame"
        $ columns = 4
        $ rows = 3
        xalign 0.115
        yalign 0.72
        grid columns rows:
            transpose True
            xfill False
            style_group "file_picker"
            for i in range(1, columns * rows + 1):
                button at file_eff:
                    action FileAction(i)
                    xfill True
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        null height 8
                        add FileScreenshot(i)
                        null height 3
                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        text "[file_name]. [file_time!t]\n[save_name!t]"
                        key "save_delete" action FileDelete(i)
    vbox:
        add "gui/bar.png"
        xalign 0.14
        yalign 0.86
    hbox:
        style_group "file_picker_nav"
        xalign 0.14
        yalign 0.865
        null width 17
        textbutton _("Auto") at file_eff:
            action FilePage("auto")
        textbutton _("Quick") at file_eff:
            action FilePage("quick")
        for i in range(1, 18):
            textbutton str(i) at file_eff:
                action FilePage(i)

screen save():
    tag menu
    if main_menu:
        add "gui/gm_back.jpg"
    else:
        add "gui/gm_back2.png"
    use navigation
    use file_picker

screen load():
    tag menu
    if main_menu:
        add "gui/gm_back.jpg"
    else:
        add "gui/gm_back2.png"
    use navigation
    use file_picker

init -2:
    style file_picker_frame:
        xminimum 740
        yminimum 590
        top_padding 30
        bottom_padding 60
        xpadding 20
        background "gui/frame.png"
    style file_picker_nav_button:
        idle_background None
        hover_background Frame("gui/qm_hover_back.png", 10, 10)
        insensitive_background None
        yminimum 10
        ymaximum 10
        xmaximum 10
        xminimum 10
    style file_picker_nav_button_text:
        size 16
        idle_color "#fff"
        hover_color "#fff"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#000"
        yalign 0.5
        xalign 0.5
        kerning 1
        outlines [(1, "#000", 0, 0)]
    style file_picker_button:
        idle_background Frame("gui/file_picker_idle.png", 24, 24)
        hover_background Frame(im.MatrixColor("gui/file_picker_idle.png", im.matrix.hue(320)), 24, 24)
        insensitive_background Frame(im.Grayscale("gui/file_picker_idle.png"), 24, 24)
        selected_idle_background Frame(im.MatrixColor("gui/file_picker_idle.png", im.matrix.hue(320)), 24, 24)
        xmaximum 235
        ymaximum 135
        xminimum 235
        yminimum 135
        top_padding 10
        bottom_padding -23
        xmargin -1
        ymargin -1
    style file_picker_text:
        size 13
        xalign 0.5
        outlines [(1, "#fff", 0, 0)]



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():
    tag menu
    if main_menu:
        add "gui/gm_back.jpg"
    else:
        add "gui/gm_back2.png"
    use navigation
    vbox:
        add "gui/frame.png"
        xalign 0.05
        yalign 0.5
    grid 3 1:
        style_group "prefs"
        yalign 0.5
        xalign 0.11
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Display")
                textbutton _("Window") action Preference("display", "window") at pref_eff
                textbutton _("Fullscreen") action Preference("display", "fullscreen") at pref_eff
            frame:
                style_group "pref"
                has vbox
                label _("Text Speed")
                bar value Preference("text speed") at pref_eff
            frame:
                style_group "pref"
                has vbox
                textbutton _("Joystick...") action Preference("joystick") at pref_eff
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen") at pref_eff
                textbutton _("All Messages") action Preference("skip", "all") at pref_eff
            frame:
                style_group "pref"
                has vbox
                textbutton _("Begin Skipping") action Skip() at pref_eff
            frame:
                style_group "pref"
                has vbox
                label _("Auto-Forward Time")
                bar value Preference("auto-forward time") at pref_eff
                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle") at pref_eff
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop") at pref_eff
                textbutton _("Keep Skipping") action Preference("after choices", "skip") at pref_eff
            frame:
                style_group "pref"
                has vbox
                label _("Music Volume")
                bar value Preference("music volume") at pref_eff
            frame:
                style_group "pref"
                has vbox
                label _("Sound Volume")
                bar value Preference("sound volume") at pref_eff
                if config.sample_sound:
                    textbutton _("Test") at pref_eff:
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"
            #if config.has_voice:
            #    frame:
            #        style_group "pref"
            #        has vbox
            #        label _("Voice Volume")
            #        bar value Preference("voice volume")
            #        textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
            #        if config.sample_voice:
            #            textbutton _("Test"):
            #                action Play("voice", config.sample_voice)
            #                style "soundtest_button"

init -2:
    style pref_frame:
        background Frame("gui/frame.png", 40, 40)
        xmaximum 315
        ypadding 30
        xpadding 28
        xmargin 2
        ymargin 2
    style pref_vbox:
        xfill True
        xalign 0.5
    style pref_label:
        xalign 0.5
        outlines [(1, "#000", 0, 0)]
    style pref_button:
        idle_background "gui/Generic Buttons/button_generic_idle.png"
        hover_background "gui/Generic Buttons/button_generic_hover.png"
        insensitive_background im.Grayscale("gui/Generic Buttons/button_generic_idle.png")
        selected_idle_background "gui/Generic Buttons/button_generic_hover.png"
        xminimum 252
        xmaximum 252
        ymaximum 61
        yminimum 61
        ymargin 5
        top_padding 20
    style pref_button_text:
        xalign 0.5
        text_align 0.5
        yalign 0.5
        size 20
        outlines [(1, "#000", 0, 0)]
        kerning 2
        idle_color "#fff"
        hover_color "#fff"
    style pref_slider:
        right_bar Frame("gui/button_idle.png", 15, 15)
        left_bar Frame("gui/button_hover.png", 15, 15)
        hover_left_bar Frame("gui/button_hover.png", 15, 15)
        xmaximum 250
        yminimum 48
        ymaximum 48
        thumb None
        xalign 0.5

    style soundtest_button:
        xalign 0.5


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    modal True
    add "gui/gm_back2.png"
    add "gui/yesno_back.png":
        xalign 0.5
        yalign 0.5
    vbox:
        style_group "yesno"
        xalign .5
        yalign .46
        ypos 0.45
        spacing 10
        label _(message):
            xalign 0.5
            yalign 0.5
    hbox:
        style_group "yesno"
        xalign 0.5
        yalign 0.569
        spacing 20
        textbutton _("Yes") action yes_action at nav_eff
        textbutton _("No") action no_action at nav_eff
    key "game_menu" action no_action

init -2:
    style yesno_button:
        idle_background "gui/button_idle.png"
        hover_background "gui/button_hover.png"
        insensitive_background im.Grayscale("gui/button_idle.png")
        selected_idle_background "gui/button_hover.png"
        xminimum 252
        xmaximum 252
        ymaximum 61
        yminimum 61
        ymargin 5
        top_padding 20

    style yesno_label_text:
        text_align 0.5
        size 24
        layout "subtitle"
        outlines [(1, "#000", 0, 0)]

    style yesno_button_text:
        xalign 0.5
        text_align 0.5
        yalign 0.5
        size 20
        outlines [(1, "#000", 0, 0)]
        kerning 2
        idle_color "#fff"
        hover_color "#fff"
