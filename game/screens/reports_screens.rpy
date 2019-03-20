# research completion report
screen research_completion_report(research_uid):
    frame:
        style "big_frame"
        has vbox
        spacing 5
        # top panel - 'Close' button and research name
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
                text castle.researches[research_uid].name size 40 ypos 10
        # completed research report
        frame:
            style "big_frame"
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                # show report or placeholder text
                if research_uid in research_reports:
                    text research_reports[research_uid]
                else:
                    text 'Research {} is completed.'.format(castle.researches[research_uid].name)


screen realms_report_screen():
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # realms report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    text "Rosaria" size 30 bold True
                    # show report or placeholder text
                    text "Rosaria is Rowan's homeland, a land mostly of plains and farmland ruled over by the Baron in his capital city of Rastedel.  Like all of the six realms, it is ruled over through an ordered societal structure, in this case hereditary feudalism with the barons at the top, the dukes ruling over the various regions, and the minor nobility under them."


# throne room - review goal
screen review_goal_screen():
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # realms report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                # show list of goal subgoals
                vbox:
                    text "Review Goal" size 30 bold True
                    if goal2_completed == False:
                        text "The twins have tasked me with taking Raeve Keep, by whatever means necessary. I should raise an army, or try to find alternate means of capturing the fortress. Raeve Keep can be found by following the path southeast over the river from the portal."
                    elif goal2_completed  == True and week < 22:
                        text "I have captured Raeve Keep. I should wait for further instructions from the twins."
                    elif goal2_completed == True and (goal3_completed == False or palaceStage == 1):
                        text "With Raeve Keep now fallen, the twins want to me seek out potential allies for their conquest of Rosaria. I have heard rumours of orcs in the north, and goblins in the woods to the east (NOT YET IMPLEMENTED). \nIn addition, they also want me to travel to Rastedel, the capital in the northeast, and scout the current situation in the city."
                    elif goal3_completed == True and palaceStage > 1 and week < 61:
                        text "With preparations for Rastedel now set, I should wait for futher instructions."                    
                    else:
                        text "Now that Rosaria's main forces have been dealt with, the twins have tasked me with returning to Rastedel, in order to capture the city in their name."

# orc barracks - military report
screen orc_barracks_report():
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # military report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    text "Current number of soldiers/Maximum number of soldiers: {}/{}".format(castle.buildings['barracks'].troops, castle.buildings['barracks'].capacity)
                    if castle.buildings['forge'].lvl >= 1:
                        text "Equipped soldiers: {}/{}".format(castle.buildings['barracks'].equipment, castle.buildings['barracks'].troops)
                    text "Orcs recruitment rate: {}/week".format(castle.buildings['barracks'].recruitment)
                    text "Base military strength of one orc: {}".format(all_troops['orc']['strength'])
                    if castle.buildings['forge'].lvl >= 1:
                        text "Base military strength of one equipped orc: {}".format(all_troops['orc']['strength'] + all_troops['orc']['equip_strength'])
                    text "Soldiers currently have {}% modifier for strength".format(5 * castle.buildings['sanctum'].troops)
                    text "Total military strength of orc soldiers: {}".format(
                        castle.buildings['barracks'].troops * all_troops['orc']['strength'] * (1 + 0.05 * castle.buildings['sanctum'].troops) + castle.buildings['barracks'].equipment * all_troops['orc']['equip_strength'])
                    text "Current treasury and morale costs for each soldier: {}/{}".format(all_troops['orc']['maintenance'], all_troops['orc']['morale_cost'])
                    text "Total treasury and morale costs for orc soldiers: {}/{}".format(
                        all_troops['orc']['maintenance'] * castle.buildings['barracks'].troops, all_troops['orc']['morale_cost'] * castle.buildings['barracks'].troops)



# dark sanctum - military report
screen dark_sanctum_report():
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # military report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    text "Current number of sorcerers / Maximum number of sorcerers: {}/{}".format(castle.buildings['sanctum'].troops, castle.buildings['sanctum'].capacity)
                    text "Current weekly recruitment rate for cubi sorcerers: {}".format(castle.buildings['sanctum'].recruitment)
                    text "Base military contribution, tech points, and morale points for each cubi sorcerer: {}/{}/{}".format(
                        all_troops['cubi']['strength'], all_troops['cubi']['research'], -all_troops['cubi']['morale_cost'])
                    text "Total military contribution, tech points, and morale points for all cubi sorcerers: {}/{}/{}".format(
                        all_troops['cubi']['strength'] * castle.buildings['sanctum'].troops, all_troops['cubi']['research'] * castle.buildings['sanctum'].troops, -all_troops['cubi']['morale_cost'] * castle.buildings['sanctum'].troops)
                    text "Soldier military power bonus for each cubi sorcerer and the current total: {}%/{}%".format(5, 5 * castle.buildings['sanctum'].troops)
                    text "Current weekly treasury costs for each cubi sorcerer: {}".format(all_troops['cubi']['maintenance'])
                    text "Total weekly treasury costs for cubi sorcerers: {}".format(all_troops['cubi']['maintenance'] * castle.buildings['sanctum'].troops)



# forge - equipment report
screen forge_equipment_report():
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # military report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                vbox:
                    text "Current weekly iron available: {}".format(castle.iron_per_week)
                    text "Current amount of equipment to be produced this week: {}".format(min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity))
                    text "Benefits of each piece of equipment on each soldier: Orc (+{})".format(all_troops['orc']['equip_strength'])
                    text "Priority order for soldiers getting equipment: Orc"
                    python:
                        total_soldiers = 0
                        equipped_soldiers = 0
                        for uid in ('barracks',):
                            equipped_soldiers += castle.buildings[uid].equipment
                            total_soldiers += castle.buildings[uid].troops
                    text "Percentage of soldiers is currently equipped: {}".format(equipped_soldiers * 100.0 / total_soldiers)
                    if equipped_soldiers < total_soldiers:
                        if min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity) > 0:
                            text "Weeks it will take to fully equip the current army at the current rate: {}".format(
                                int(math.ceil((total_soldiers - equipped_soldiers) * 1.0 / (min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity)))))
                        else:
                            text "Weeks it will take to fully equip the current army at the current rate: eternity"
                        python:
                            possible_power = 0
                            current_power = 0
                            for uid in ('barracks',):
                                possible_power += castle.buildings[uid].troops * all_troops[castle.buildings[uid].troop_type]['equip_strength']
                                current_power += castle.buildings[uid].equipment * all_troops[castle.buildings[uid].troop_type]['equip_strength']
                        text "The total military power benefit of fully equipping the army: {}".format(possible_power - current_power)
                    else:
                        text "The amount of treasury being made from selling extra equipment: {}".format(5 * min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity))



# simple frame that fills whole area
style big_frame:
    xfill True
    yfill True
    background Frame('gui/stats_border.png', 12, 12)


# simple frame that fills in horizontal direction
style horiz_panel:
    xfill True
    xpadding 5
    ypadding 5
    background Frame('gui/stats_border.png', 12, 12)


# viewport that fills whole area
style big_viewport:
    xfill True
    yfill True
