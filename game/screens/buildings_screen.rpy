# castle buildings
screen buildings_screen():
    # uid of selected building
    default sel_bld = None
    frame:
        background 'gui/UI_Screens/UIScreen_Workshop.png'
        pos (-1, -1)
        textbutton 'Back' action Return() style 'back_button'
        text 'Workshop' style 'room_caption'
        if castle.scheduled_upgrades:
            text "Currently building: {}".format(castle.buildings[castle.scheduled_upgrades[0]].name) style 'sec_room_caption'
        else:
            text "Currently building: nothing" style 'sec_room_caption'
        hbox:
            pos (55, 130)
            spacing 20
            # list of buildings
            frame:
                background 'listbox_border'
                xpadding 3
                ypadding 3
                vpgrid:
                    cols 1
                    xysize (400, 550)
                    mousewheel True
                    scrollbars 'vertical'
                    spacing 1
                    for bld in sorted(castle.buildings.values(), key=lambda u: u.name):
                        # show building only if it can be built or is already built
                        if bld.can_be_shown() or bld.lvl > 0:
#~                                 textbutton bld.name + ' (lvl' + str(bld.lvl) + ')' xfill True action SetScreenVariable('sel_bld', bld.uid):
#~                                     if bld.can_be_built():
#~                                         text_color '#0f0'
#~                                     else:
#~                                         text_color '#855'
                            button:
                                right_margin 1
                                xfill True
                                ysize 72
                                background 'button_border'
                                hover_foreground 'rect_highlight'
                                action SetScreenVariable('sel_bld', bld.uid)
                                frame:
                                    background None
                                    text bld.name + ' (lvl' + str(bld.lvl) + ')' pos (15, 10):
                                        if bld.can_be_built():
                                            color '#0f0'
                                        else:
                                            color '#855'
                                    text '<upgrade type>' size 20 color '#686868' pos (15, 35)
                                    text '{} g'.format(castle.buildings[bld.uid].up_cost) xalign 1.0 xoffset -30 yalign 0.5 line_spacing 0
            vbox:
                spacing 15
                # description box
                frame:
                    background 'gui/workshop/UI_DescriptionBox.png'
                    xysize (403, 484)
#~                     xpadding 30
#~                     ypadding 25
                    if sel_bld:
                        text castle.buildings[sel_bld].name size 25 xalign 0.5 ypos 25
                        frame:
                            if sel_bld in buildings_thumbnails:
                                background buildings_thumbnails[sel_bld]
                            else:
                                background '#1b1b1b'
                            xysize (350, 199)
                            ypos 60
                            xalign 0.5
                        if sel_bld in buildings_descriptions:
                            frame:
                                background None
                                xysize (350, 150)
                                xalign 0.5
                                ypos 300
                                viewport:
                                    mousewheel True
                                    scrollbars 'vertical'
                                    text buildings_descriptions[sel_bld] size 15
                    else:
                        text 'No selection' size 25 xalign 0.5 ypos 25
                # buy button
                textbutton 'Buy...':
                    style 'room_button'
                    xysize (410, 55)
                    if sel_bld:
                        action BuildUpgrade(sel_bld)
                    else:
                        action None
    vbox:
        spacing -10
        align (0.97, 0.05)
        use game_time
        use info_treasury


#~         vbox:
#~             spacing 10
#~             style_prefix 'small'
#~             hbox:
#~                 spacing 10
#~                 yfill True
#~                 frame:
#~                     background Frame('gui/stats_border.png', 12, 12)
#~                     xsize 400
#~                     yfill True
#~                     has vbox
#~                     spacing 10
#~                     # control buttons
#~                     frame:
#~                         background Frame('gui/stats_border.png', 12, 12)
#~                         xfill True
#~                         has vbox
#~                         hbox:
#~                             spacing 10
#~                             if sel_bld:
#~                                 textbutton 'Build/Upgrade {}'.format(castle.buildings[sel_bld].up_cost) action BuildUpgrade(sel_bld)
#~                         if castle.scheduled_upgrades:
#~                             text "Building now: {}".format(castle.buildings[castle.scheduled_upgrades[0]].name)
#~                         hbox:
#~                             text 'Treasury: [castle.treasury]'
#~                             if config.developer:
#~                                 use adjust_treasury_minidebug
                    # list of buildings
                # building image and stats
#~                 frame:
#~                     background Frame('gui/stats_border.png', 12, 12)
#~                     xfill True
#~                     yfill True
#~                     viewport:
#~                         mousewheel True
#~                         scrollbars 'vertical'
#~                         yfill True
#~                         vbox:
#~                             if sel_bld:
#~                                 $ bld = castle.buildings[sel_bld]
#~                                 text 'Current stats:' size 30
#~                                 if bld.lvl == 0:
#~                                     text 'Not built yet...'
#~                                 else:
#~                                     text 'Income: {}'.format(bld.income)
#~                                     text 'Maintenance: {}'.format(bld.maintenance)
#~                                     text 'Morale generation: {}'.format(bld.morale)
#~                                     text 'Research points: {}'.format(bld.research)
#~                                     text 'Capacity: {}'.format(bld.capacity)
#~                                     text 'Recruitment: {} + {}'.format(bld.recruitment, castle.recruitment_bonuses.get(bld.uid, 0))
#~                                     # show additional info for some buildings
#~                                     if hasattr(bld, 'troops'):
#~                                         text 'Troops: {} - {}'.format(all_troops[bld.troop_type]['name'], bld.troops)
#~                                     if hasattr(bld, 'equipment'):
#~                                         text 'Equipment: {}'.format(bld.equipment)
#~                                 if bld.uid in castle.scheduled_upgrades:
#~                                     text 'Upgrading on next week...' color '#5f5'
#~                                 text 'Improvement on next level:' size 30
#~                                 if bld.lvl == 0:
#~                                     text 'Income: {}'.format(all_buildings[bld.uid]['income'])
#~                                     text 'Maintenance: {}'.format(all_buildings[bld.uid]['maintenance'])
#~                                     text 'Morale generation: {}'.format(all_buildings[bld.uid]['morale'])
#~                                     text 'Research points: {}'.format(all_buildings[bld.uid]['research'])
#~                                     text 'Capacity: {}'.format(all_buildings[bld.uid]['capacity'])
#~                                     text 'Recruitment: {} + {}'.format(all_buildings[bld.uid]['recruitment'], castle.recruitment_bonuses.get(bld.uid, 0))
#~                                 else:
#~                                     text 'Income: {}'.format(all_buildings[bld.uid]['up_income'])
#~                                     text 'Maintenance: {}'.format(all_buildings[bld.uid]['up_maintenance'])
#~                                     text 'Morale generation: {}'.format(all_buildings[bld.uid]['up_morale'])
#~                                     text 'Research points: {}'.format(all_buildings[bld.uid]['up_research'])
#~                                     text 'Capacity: {}'.format(all_buildings[bld.uid]['up_capacity'])
#~                                     text 'Recruitment: {} + {}'.format(all_buildings[bld.uid]['up_recruitment'], castle.recruitment_bonuses.get(bld.uid, 0))
#~                                 if bld.uid in buildings_descriptions:
#~                                     null height 30
#~                                     text buildings_descriptions[bld.uid]


init python:
    class BuildUpgrade(Action):
        '''Build an upgrade in the castle.'''
        def __init__(self, uid):
            self.uid = uid

        def get_sensitive(self):
            if self.uid:
                return castle.buildings[self.uid].can_be_built()

        def __call__(self):
            # schedule to build the upgrade at the start of next week
            castle.scheduled_upgrades.append(self.uid)
            castle.treasury -= castle.buildings[self.uid].up_cost
            renpy.restart_interaction()


    buildings_thumbnails = {
        'arena': 'gui/Thumbnail UI images/Icon_Workshop_Arena.png',
        'barracks': 'gui/Thumbnail UI images/Icon_Workshop_Barracks.png',
        'pit': 'gui/Thumbnail UI images/Icon_Workshop_BreedingPit.png',
        'brothel': 'gui/Thumbnail UI images/Icon_Workshop_Brothel.png',
        'dungeon': 'gui/Thumbnail UI images/Icon_Workshop_CastleDungeon.png',
        'forge': 'gui/Thumbnail UI images/Icon_Workshop_Forge.png',
        'library': 'gui/Thumbnail UI images/Icon_Workshop_Library.png',
        'quarters': 'gui/Thumbnail UI images/Icon_Workshop_LivingQuarters.png',
        'sanctum': 'gui/Thumbnail UI images/Icon_Workshop_Sanctum.png',
        'tavern': 'gui/Thumbnail UI images/Icon_Workshop_Tavern.png',
        'caravan': 'gui/Thumbnail UI images/Icon_Workshop_Wagon.png',
        'workshop': 'gui/Thumbnail UI images/Icon_Workshop_Workshop.png',
        'hall': 'gui/Thumbnail UI images/Icon_Workshop_ThroneRoom.png',
    }
