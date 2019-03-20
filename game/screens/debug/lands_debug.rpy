# debug screen for lands (realms and locations)
screen lands_debug():
    modal True
    default sel_realm = None
    default hov_realm = None
    default hov_loc = None
    default sel_loc = None
    frame:
        background '#f99e'
        xfill True
        yfill True
    frame:
        style_group 'navi'
        ypadding 0
        xpadding 0
        vbox:
            textbutton 'Leave' action Hide('lands_debug')
            null height 20
            frame:
                background Frame('gui/stats_border.png', 12, 12)
                xysize (940, 350)
                xpos 20
                grid 3 2:
                    xfill True
                    yfill True
                    # show grid of realms
                    for realm in lands:
                        textbutton realm.name action [SetScreenVariable('sel_realm', realm.uid), SetScreenVariable('sel_loc', None), SelectedIf(realm.accessible), ToggleField(lands[realm.uid], 'accessible')]:
                            yalign 0.5
                            xalign 0.5
                            hovered SetScreenVariable('hov_realm', realm.uid)
                            unhovered SetScreenVariable('hov_realm', None)
    use realm_actions_debug(sel_realm, sel_loc)
    use portal_info(sel_realm, hov_realm, hov_loc)


# actions (locations) for selected realm
screen realm_actions_debug(sel_realm, sel_loc):
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        xalign 1.0
        yfill True
        xsize 300
        style_group 'navi'
        vbox:
            frame:
                xfill True
                background Frame('gui/stats_border.png', 12, 12)
                if sel_realm:
                    text lands[sel_realm].name xalign 0.5
                else:
                    text 'Select realm' xalign 0.5
            # show all locations for selected realm
            if sel_realm:
                if sel_loc:
                    textbutton 'Visible' action [SelectedIf(lands[sel_realm][sel_loc].visible), ToggleField(lands[sel_realm][sel_loc], 'visible')]
                    textbutton 'Accessible' action [SelectedIf(lands[sel_realm][sel_loc].accessible), ToggleField(lands[sel_realm][sel_loc], 'accessible')]
                null height 40
                for loc in lands[sel_realm]:
                    textbutton loc.name action [SelectedIf(loc.uid == sel_loc), SetScreenVariable('sel_loc', loc.uid)]:
                        hovered SetScreenVariable('hov_loc', loc.uid)
                        unhovered SetScreenVariable('hov_loc', None)


# show info for selected or hovered item
screen portal_info(sel_realm, hov_realm, hov_loc):
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        yalign 1.0
        yoffset -20
        xpos 20
        xsize 940
        ysize 250
        # priority for info display: hovered location, hovered realm, selected realm
        if hov_loc and sel_realm:
            # in case location is hovered by mouse there must be selected realm
            if hov_loc == 'explore':
                text 'Explore realm: ' + lands[sel_realm].name
            else:
                text lands[sel_realm].name + ' ---> ' + lands[sel_realm][hov_loc].name + '\n' + lands[sel_realm][hov_loc].descr
        elif hov_realm:
            text lands[hov_realm].name + '\n' + lands[hov_realm].descr
        elif sel_realm:
            text lands[sel_realm].name + '\n' + lands[sel_realm].descr
        else:
            text 'descr'

