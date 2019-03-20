# debug tools screen (info and buttons to other screens)
default debug_screen_expanded = False
screen debug_tools_screen():
    frame:
        has vbox
        if debug_screen_expanded:
            hbox:
                spacing 5
                text 'Corruption: [avatar.corruption]'
                text 'Infamy: [avatar.infamy]'
                text 'Guilt: [avatar.guilt]'
            textbutton 'Complete: {}'.format(castle.current_research.name if castle.current_research else 'No research'):
                action [SensitiveIf(castle.current_research), Function(complete_research)]
            hbox:
                vbox:
                    textbutton 'Events' action Show('events_info')
                    textbutton 'Buildings' action Show('buildings_debug')
                    textbutton 'Lands debug' action Show('lands_debug')
                    textbutton 'Actors debug' action Show('actors_debug')
                    textbutton 'Rest' action Jump('rest')
                    use journal_button
                    textbutton 'Journal: read all' action [journal.read_all, renpy.restart_interaction]
                vbox:
                    hbox:
                        text 'Treasury ({})'.format(castle.treasury)
                        textbutton '+100' action SetField(castle, 'treasury', castle.treasury + 100)
                        textbutton '-100' action SetField(castle, 'treasury', castle.treasury - 100)
                    hbox:
                        text 'Money ({})'.format(avatar.gold)
                        textbutton '+10' action SetField(avatar, 'gold', avatar.gold + 10)
                        textbutton '-10' action SetField(avatar, 'gold', avatar.gold - 10)
                    hbox:
                        text 'Prisoners ({})'.format(castle.buildings['dungeon'].prisoners)
                        textbutton '+1' action SetField(castle.buildings['dungeon'], 'prisoners', castle.buildings['dungeon'].prisoners + 1)
                        textbutton '-1' action SetField(castle.buildings['dungeon'], 'prisoners', castle.buildings['dungeon'].prisoners - 1)
                    hbox:
                        text 'Exp. ({})'.format(avatar.exp)
                        textbutton '+100' action SetField(avatar, 'exp', avatar.exp + 100)
                        textbutton '-100' action SetField(avatar, 'exp', avatar.exp - 100)
                    # access to researches
                    textbutton 'Research' action ToggleField(systems, 'research') style 'small_debug_button'
                    # access to upgrades
                    textbutton 'Building' action ToggleField(systems, 'building') style 'small_debug_button'
                    # access to NPC jobs
                    textbutton 'NPC jobs' action ToggleField(systems, 'npc_jobs') style 'small_debug_button'
                    textbutton 'Status effects' action Show('status_effects_debug')
                    textbutton 'Rumors' action Show('rumors_debug')
                    textbutton 'Raid test' action Show('raid_menu', required_mp=30)
        textbutton "Show debug" action ToggleVariable('debug_screen_expanded')


# for buildings/upgrades screen
screen adjust_treasury_minidebug():
    style_prefix None
    hbox:
        textbutton '-' action SetField(castle, 'treasury', castle.treasury - 100)
        textbutton '+' action SetField(castle, 'treasury', castle.treasury + 100)
