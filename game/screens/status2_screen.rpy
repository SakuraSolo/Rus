# status screen (stats, skills, feats)
screen status2_screen():
    # forbid rollback and mark changes made in this screen to be saved
    $ renpy.block_rollback()
    $ renpy.retain_after_load()
    frame:
        background 'gui/statsinventory_backdrop.png'
        textbutton 'Back' action Return() style 'back_button'
        # buttons to switch inventory/status
        use inventory_status_switch
        # list of skills/feats
        frame:
            pos (540, 140)
            background 'listbox_border'
            xpadding 3
            ypadding 3
            vpgrid:
                cols 1
                xysize (700, 550)
                mousewheel True
                scrollbars 'vertical'
                spacing 1
                frame:
                    xfill True
                    ysize 30
                    background None
                    left_padding 10
                    text 'Skills' bold True
                    text 'Feats' xpos 350  bold True
                # length of lists - lenghth of list of skills or feate, which is longer
                $ list_length = max(len(avatar.skills), len(avatar.feats))
                for i in range(list_length):
                    frame:
                        xfill True
                        ysize 30
                        background None
                        # show next skill, if list of skills still not ended
                        if i < len(avatar.skills):
                            $ skill = sorted(avatar.skills)[i]
                            frame:
                                xsize 340
                                left_padding 20
                                background None
                                text '{}'.format(all_skills[skill][0])
                                text '{{color={}}}{}{{/color}}/{}'.format(ratio_color(avatar.skill(skill), avatar.base_skill(skill)), avatar.skill(skill), avatar.base_skill(skill)) xalign 1.0
                        # show next feat, if still there are some left
                        if i < len(avatar.feats):
                            $ feat = sorted(avatar.feats)[i]
                            frame:
                                xsize 340
                                xalign 1.0
                                background None
                                right_padding 20
                                text all_feats[feat][0]
                                # show bonuses for every stat or skill
#~                                 hbox:
#~                                     xalign 1.0
#~                                     spacing 5
#~                                     for trg, bonus in all_feats[feat][1].items():
#~                                         # skill
#~                                         if trg in all_skills:
#~                                             text '{} {:+}'.format(all_skills[trg][0], bonus)
#~                                         # stat
#~                                         elif len(trg) == 1:
#~                                             text '{} {:+}'.format(letter_to_stat[trg].capitalize(), bonus)
#~                                         # hp
#~                                         else:
#~                                             text 'Hp {:+}'.format(bonus)

        # show level up button if there is enough exp
        if avatar.new_exp >= avatar.req_exp:
            textbutton 'Level up' action Show('avatar_level_up'):
                style 'rcrect_button'
                text_color '#d5d3d4'
                pos (350, 31)


        # show equipment slots
        use equipment_slots_screen
        # some info about stats and level
        use avatar_info


#~     # show level up button if there is enough exp
#~     if avatar.new_exp >= avatar.req_exp:
#~         textbutton 'Level up' action Show('avatar_level_up'):
#~             style 'small_textbutton'
#~             pos (350, 40)
#~     frame:
#~         background Frame('gui/stats_border.png', 12, 12)
#~         style_group 'navi'
#~         xysize (800, 680)
#~         xalign 1.0
#~         xoffset -5
#~         ypos 20
#~         hbox:
#~             xfill True
#~             # avatar's stats
#~             use avatar_core_info
#~             # avatar's skills
#~             frame:
#~                 background Frame('gui/stats_border.png', 12, 12)
#~                 yalign 0.5
#~                 vbox:
#~                     text 'Skills'
#~                     vpgrid:
#~                         cols 1
#~                         mousewheel True
#~                         scrollbars 'vertical'
#~                         side_xalign 0.5
#~                         for skill in sorted(avatar.skills):
#~                             frame:
#~                                 xsize 200
#~                                 text '{}: {{color={}}}{}{{/color}}/{}'.format(all_skills[skill][0], ratio_color(avatar.skill(skill), avatar.base_skill(skill)), avatar.skill(skill), avatar.base_skill(skill))
#~             # avatar's feats
#~             frame:
#~                 background Frame('gui/stats_border.png', 12, 12)
#~                 yalign 0.5
#~                 yfill True
#~                 xsize 250
#~                 vbox:
#~                     yfill True
#~                     text 'Feats'
#~                     viewport:
#~                         mousewheel True
#~                         scrollbars 'vertical'
#~                         yfill True
#~                         xsize 250
#~                         vbox:
#~                             spacing 5
#~                             for feat in sorted(avatar.feats):
#~                                 frame:
#~                                     background Frame('gui/stats_border.png', 12, 12)
#~                                     xfill True
#~                                     vbox:
#~                                         text all_feats[feat][0] color '#ff0'
#~                                         # show bonuses for everey stat or skill
#~                                         for trg, bonus in all_feats[feat][1].items():
#~                                             # skill
#~                                             if trg in all_skills:
#~                                                 text '{} {:+}'.format(all_skills[trg][0], bonus)
#~                                             # stat
#~                                             elif len(trg) == 1:
#~                                                 text '{} {:+}'.format(letter_to_stat[trg].capitalize(), bonus)
#~                                             # hp
#~                                             else:
#~                                                 text 'Hp {:+}'.format(bonus)


# display for stats, gold and level info
screen avatar_core_info():
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        vbox:
            use stat_widget('Gold', 'gui/stats_gold.png', avatar.gold)
            use stat_widget('MP', 'gui/stats_reflexes.png', avatar.base_mp - avatar.wounds - avatar.mp_penalty, avatar.base_mp)
            use stat_widget('Strength', 'gui/stats_strength.png', avatar.strength, avatar.base_strength)
            use stat_widget('Vitality', 'gui/stats_vitality.png', avatar.vitality, avatar.base_vitality)
            use stat_widget('Reflexes', 'gui/stats_reflexes.png', avatar.reflexes, avatar.base_reflexes)
            use stat_widget('Intelligence', 'gui/stats_intelligence.png', avatar.intelligence, avatar.base_intelligence)
            use stat_widget('Luck', 'gui/stats_luck.png', avatar.luck, avatar.base_luck)
            use stat_widget('Experience', 'gui/stats_intelligence.png', avatar.exp)
            use stat_widget('Level', 'gui/stats_intelligence.png', '[avatar.lvl]: [avatar.new_exp]/[avatar.req_exp]')


# small widget for one stat
screen stat_widget(stat_name, pic, val, val2=None):
    vbox:
        text stat_name line_spacing 0
        hbox:
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xysize (48, 48)
                add pic xalign 0.5 yalign 0.5
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xysize (200, 48)
                if not val2:
                    text '{}'.format(val) xalign 0.5 yalign 0.5 bold True line_spacing 0
                else:
                    text '{{color={}}}{}{{/color}}/{}'.format(ratio_color(val, val2), val, val2) xalign 0.5 yalign 0.5 bold True line_spacing 0


# widget for leveling up
screen avatar_level_up():
    modal True
    window:
        background '#000a'
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        ypos 20
        ysize 680
        xalign 0.5
        default lvl_up_hlp = LevelUpHelper()
        style_group 'small'
        vbox:
            hbox:
                text 'New level: {}'.format(avatar.lvl + 1) size 30
                textbutton 'Complete' action [SensitiveIf(lvl_up_hlp.can_complete(avatar)), Function(lvl_up_hlp.complete, avatar), Hide('avatar_level_up'), renpy.restart_interaction] xsize 200
            hbox:
                spacing 10
                frame:
                    background Frame('gui/stats_border.png', 12, 12)
                    vbox:
                        text 'Stat points: [lvl_up_hlp.stat_points]'
                        for stat in main_stats:
                            hbox:
                                frame:
                                    xsize 120
                                    background None
                                    text stat.capitalize() xalign 0.5 yalign 0.5 line_spacing 0
                                #textbutton '-' action [SensitiveIf(lvl_up_hlp.stat_change_possible(stat, -1)), Function(lvl_up_hlp.change_stat, stat, -1)]
                                imagebutton action [SensitiveIf(lvl_up_hlp.stat_change_possible(stat, -1)), Function(lvl_up_hlp.change_stat, stat, -1)]:
                                    idle 'gui/Generic Buttons/Button_Stats_Decrease.png'
                                    hover 'gui/Generic Buttons/Button_Stats_Decrease.png'
                                #textbutton '+' action [SensitiveIf(lvl_up_hlp.stat_change_possible(stat, 1)), Function(lvl_up_hlp.change_stat, stat, 1)]
                                imagebutton action [SensitiveIf(lvl_up_hlp.stat_change_possible(stat, 1)), Function(lvl_up_hlp.change_stat, stat, 1)]:
                                        idle 'gui/Generic Buttons/Button_Stats_Increase.png'
                                        hover 'gui/Generic Buttons/Button_Stats_Increase.png'
                                frame:
                                    xsize 30
                                    background None
                                    text str(lvl_up_hlp.stat_change(stat)) xalign 0.5 yalign 0.5 line_spacing 0
                frame:
                    background Frame('gui/stats_border.png', 12, 12)
                    vbox:
                        text 'Skill points: [lvl_up_hlp.skill_points]'
                        vpgrid:
                            cols 1
                            mousewheel True
                            scrollbars 'vertical'
                            side_xalign 0.5
                            for skill in sorted(avatar.skills):
                                hbox:
                                    frame:
                                        xsize 150
                                        background None
                                        text all_skills[skill][0].capitalize() xalign 0.5 yalign 0.5 line_spacing 0
                                    #textbutton '-' action [SensitiveIf(lvl_up_hlp.skill_change_possible(avatar, skill, -1)), Function(lvl_up_hlp.change_skill, skill, -1)]
                                    imagebutton action [SensitiveIf(lvl_up_hlp.skill_change_possible(avatar, skill, -1)), Function(lvl_up_hlp.change_skill, skill, -1)]:
                                        idle 'gui/Generic Buttons/Button_Stats_Decrease.png'
                                        hover 'gui/Generic Buttons/Button_Stats_Decrease.png'

                                    #textbutton '+' action [SensitiveIf(lvl_up_hlp.skill_change_possible(avatar, skill, 1)), Function(lvl_up_hlp.change_skill, skill, 1)]
                                    imagebutton action [SensitiveIf(lvl_up_hlp.skill_change_possible(avatar, skill, 1)), Function(lvl_up_hlp.change_skill, skill, 1)]:
                                            idle 'gui/Generic Buttons/Button_Stats_Increase.png'
                                            hover 'gui/Generic Buttons/Button_Stats_Increase.png'
                                    frame:
                                        xsize 30
                                        background None
                                        text str(lvl_up_hlp.skill_change(skill)) xalign 0.5 yalign 0.5 line_spacing 0
                # if avatar's level is odd, allow to choose a feat
                if avatar.lvl % 2 == 1:
                    frame:
                        background Frame('gui/stats_border.png', 12, 12)
                        vbox:
                            if lvl_up_hlp.feat:
                                text 'Choosen feat: {}'.format(all_feats[lvl_up_hlp.feat][0])
                            else:
                                text 'Choose feat'
                            viewport:
                                mousewheel True
                                scrollbars 'vertical'
                                xsize 330
                                vbox:
                                    spacing 5
                                    for feat in sorted(all_feats):
                                        frame:
                                            background Frame('gui/stats_border.png', 12, 12)
                                            vbox:
                                                textbutton all_feats[feat][0] action (SensitiveIf(feat not in avatar.feats), SelectedIf(feat == lvl_up_hlp.feat), Function(lvl_up_hlp.choose_feat, feat)):
                                                    xsize 300
                                                # show bonuses for every stat or skill
                                                for trg, bonus in all_feats[feat][1].items():
                                                    # skill
                                                    if trg in all_skills:
                                                        text '{} {:+}'.format(all_skills[trg][0], bonus)
                                                    # stat
                                                    elif len(trg) == 1:
                                                        text '{} {:+}'.format(letter_to_stat[trg].capitalize(), bonus)
                                                    # hp
                                                    else:
                                                        text 'Hp {:+}'.format(bonus)
