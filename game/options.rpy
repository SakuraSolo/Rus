
init -1 python hide:
    config.developer = True
    # log file for game activity (relative to renpy executable)
    if config.developer:
        config.log = 'game_log.txt'
    config.screen_width = 1280
    config.screen_height = 720
    config.window_title = u"Seeds of Chaos"
    config.name = "Seeds of Chaos"
    config.window_icon = "gui/icon.png"
    config.version = "0.0.05"
    config.has_sound = True
    config.has_music = True
    config.has_voice = True
    config.thumbnail_width = 200
    config.thumbnail_height = 113
    config.mouse = {"default": [("gui/mouse_cursor.png", 10, 10)]}
    config.quit_action = Quit(confirm=True)
    config.default_fullscreen = False
    config.default_text_cps = 30
    config.default_afm_time = 10
    config.main_menu_music = "music/title screen loop.ogg"
    config.help = "README.html"
    config.enter_transition = dissolve
    config.exit_transition = dissolve
    config.intra_transition = dissolve
    config.main_game_transition = dissolve
    config.game_main_transition = dissolve
    config.end_splash_transition = dissolve
    config.end_game_transition = dissolve
    config.after_load_transition = dissolve
    config.window_show_transition = dissolve
    config.window_hide_transition = dissolve
    config.adv_nvl_transition = dissolve
    config.nvl_adv_transition = dissolve
    config.enter_yesno_transition = dissolve
    config.exit_yesno_transition = dissolve
    config.enter_replay_transition = dissolve
    config.exit_replay_transition = dissolve
    config.say_attribute_transition = dissolve
    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"
    # config.sample_sound = "click.wav"

    theme.roundrect(
        widget = "#003c78",
        widget_hover = "#0050a0",
        widget_text = "#c8ffff",
        widget_selected = "#ffffc8",
        disabled = "#404040",
        disabled_text = "#c8c8c8",
        label = "#ffffff",
        frame = "#6496c8",
        mm_root = "#dcebff",
        gm_root = "#dcebff",
        rounded_window = False,
        )


    #style.say_who_window.background = None
    #style.window.xmaximum = 494
    style.window.xpadding = 50
    style.window.ypadding = 40
    #style.window.top_padding = 50
    #style.window.yminimum = 208
    #style.window.ymaximum = 208
    style.default.font = "kinesis.otf"
    style.default.color = "#ffffff"
    style.default.size = 22
    style.default.line_spacing = 10
    style.default.outlines = [ (1.0, "#000", 0, 0) ]
    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

python early:
    config.save_directory = "seeds_of_chaos-1446566129"


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "seeds-of-chaos-0.2.42"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "seeds-of-chaos"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpt', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
