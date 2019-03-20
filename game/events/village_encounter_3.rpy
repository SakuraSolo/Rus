# events for village interactions (on entry)
init python:

    #A friendly dinner.
    #triggers on arrival before choice
    event('a_friendly_dinner', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)


label a_friendly_dinner:
#A friendly dinner.
#triggers on arrival before choice

$ event_tmp['stayed_for_dinner'] = False
$ event_tmp['do_not_capture'] = False

scene bg31 with fade

"As he traveled to the next village, Rowan found himself with an unexpected companion by his side."
"When approaching the settlement, he met a young girl, no older than 14, returning home from a nearby forest with a basket full of wild berries. The girl, intrigued by the lone, mysterious wanderer, immediately approached the hero and started showering him with questions."

#if corruption greater than 49
if avatar.corruption > 49:
    "Rowan gritted his teeth in annoyance and tried to shoo the girl away."
    "Sadly, she was either far too dense to comprehend her company was not welcomed, or simply did not care. If she was so obnoxious with everyone as she was now with him, Rowan wouldn't be surprised if she got herself raped and killed one day."
    "Likely after foolishly approaching a yet another lone wanderer, one that had neither Rowan's morals or his patience."
    "Still, being obnoxious was no crime, and Rowan had no intention of lowering himself to threatening a child, so ultimately, against his better judgment, he allowed her to walk by his side as he approached the village."
    "Meanwhile, the girl continued to babble constantly, asking him question after question."
    "Finally, seeing how the silent treatment wasn't working, Rowan relented, decided to the give the girl some vague answers regarding his origins, hoping that maybe this would shut her up."
else:
#else
    "While Rowan usually avoided attracting any company in his travels, he found no reason to send the girl away. Her constant babbling a bit... Obnoxious, but it proved to be a pleasant diversion from the usual weariness of his travel."
    "After a while, he even decided to answer some of her questions, vaguely hinting about his heroic past."

#rejoin
"When he mentioned fighting in the last war, the girl stopped dumbfounded-"
"And then resumed her questioning with twice as much enthusiasm."
"After almost an hour, the two finally found themselves at the edge of the village. With the sun heading over the horizon, the young girl, whose name, Rowan learned, was Sam, insisted he should stay with her family for dinner."
"Rowan wasn’t certain if it was such a good idea, given the nature of his current “quest”, but staying with the girl’s family would probably be better than camping outside."

menu:
    "Agree.":
        $ released_fix_rollback()
        jump friendlyDinner

    "Refuse.":
        $ released_fix_rollback()
        "Rowan shook his head and answered he didn't have the time. The news saddened the girl, and she tried to change his mind, but Rowan was adamant in his decision."
        "Soon, he was left alone."
        "It was time to decide what to do with the settlement."
        jump friendlyDinnerChoice

################################################################################

label friendlyDinner:
scene bg1 with fade

$ event_tmp['stayed_for_dinner'] = True

"Against his better judgment, Rowan agreed to dine with the girl and her family, and allowed her to lead him to her home."
"Her house, a solid wooden structure, was located in the middle of the village. They were greeted by the girl's mother – who immediately realized what must have transpired, and with a practiced motion, smacked her daughter in the ear."
"She started apologizing to Rowan for her child's behavior. Apparently, it wasn't the first time she was pestering travelers."
"Rowan assured her it was nothing and went in to meet the rest of the family."

#if corruption greater than 49
if avatar.corruption > 49:
    "The evening that followed was… Uncomfortable."
    "Rowan spent far too much time among half-demons, demons, orcs and other people of questionable morality to honestly enjoy the small pleasures that came with a family life."
    "The father, a simple man in his early forties, also apologized for his daughter's obnoxious nature, but Rowan could see he didn’t really mean it. It was obvious he loved his oldest child far too much to ever scold her properly."
    "Later, he met the girl's two siblings – a brother, a year younger, and a little sister. They also started showering Rowan with questions, and this time, the hero did his best to satisfy their curiosity, as they all dined in the small, cozy chamber of their house."
    "... He shouldn't have come. It was too much of a painful reminder of what could've been if Jezera never showed at their doorstep that fateful night."
    #lose corruption
    $ change_base_stat('c', -2)
else:
#else
    "The evening passed in a pleasant atmosphere. Rowan soon met the girl’s father – a simple man in his early forties, who also apologized for his daughter’s obnoxious nature, but Rowan could see he didn’t really mean it."
    " It was obvious he loved his oldest child far too much to ever scold her properly."
    "Later, he met the girl's two siblings – a brother, a year younger, and a little sister. They also started showering Rowan with questions, and this time, the hero did his best to satisfy their curiosity, as they all dined in the small, cozy chamber of their house."
    "Seeing the three kids look up to him, excitement in their eyes, as he told the many tales of his past adventures, made his heart ache. It reminded him of what his own life could've looked like, if not for the twins."
    "..."
    "… Though perhaps, once this was all over, he and Alexia would have another shot at having a family."
    "… Maybe one day…"
    #lose guilt and corruption
    $ change_base_stat('c', -2)
    $ change_base_stat('g', -2)

#rejoin
scene black with fade

"On the morrow, Rowan bid the family farewell."

#if corruption is lower than 49
if avatar.corruption < 49:
    "He tried to offer the father some gold for all the trouble he caused them, but the man would have none of it. Rowan was a guest, after all."

#rejoin
"Behind her father's back, the young girl waved at him enthusiastically, asking if they'll ever see him again."
"… For their own good, Rowan hoped they would not."
"Well rested, the hero walked to the village center. It was time to decide what to do with the settlement."

################################################################################

label friendlyDinnerChoice:
scene bg1 with fade
$ temp3 = human_villages_defs[eventHex[6]][2]
menu:
    "Conquer the village." if not event_tmp['do_not_capture']:
        $ released_fix_rollback()
        #if stayed over for dinner
        if event_tmp['stayed_for_dinner']:
            "… Was he really considering it? Sending orcs against the people who fed him and granted him a roof over his head for no reason other than because it was the humane thing to do?"
            menu:
                "Yes":
                    $ released_fix_rollback()
                    #allocate troops, then do below. If player cancel's allocation, send them back to previous menu
                    call screen raid_menu(human_villages_defs[world.cur_hex[6]][2])
                    if not raid_state.in_raid:
                        jump friendlyDinnerChoice
                    else:
                        $ raid_state.finish()
                    "Rowans swallowed heavily. Whether he liked it or not, he had a mission to accomplish."
                    "Rowan took the time to scout the village, identifying where his orcs should strike from."
                    "An hour later, he sent a message to castle Bloodmeen, sending them the location and required number of orcs for the attack."
                    "He didn’t wait to see the result. He already knew how it would all turn out."
                    #medium gain of guilt, town is captured as normal
                    $ castle.villages += 1
                    $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                    $ change_base_stat('g', 5)
                    return

                "No.":
                    $ released_fix_rollback()
                    "… No. There were some lines he would never cross, and he didn't give a damn if the twins were going to lock him up for it."
                    #Return to decision tree. Only “Trade with it” is now selectable.
                    $ event_tmp['do_not_capture'] = True
                    jump friendlyDinnerChoice

        #else
        else:
            #conquer village normally
            call screen raid_menu(human_villages_defs[world.cur_hex[6]][2])
            if not raid_state.in_raid:
                jump friendlyDinnerChoice
            else:
                $ raid_state.finish()
            $ change_base_stat('f', 2)
            $ change_base_stat('g', 2)
            $ castle.villages += 1
            $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
            return


    "Destroy the village." if not event_tmp['do_not_capture']:
        $ released_fix_rollback()
        #if stayed over for dinner
        if event_tmp['stayed_for_dinner']:
            "… Was he really considering it? Sending orcs against the people who fed him and granted him a roof over his head for no reason other than because it was the humane thing to do?"
            menu:
                "Yes":
                    $ released_fix_rollback()
                    #allocate troops, then do below. If player cancel's allocation, send them back to previous menu
                    call screen raid_menu(human_villages_defs[world.cur_hex[6]][2])
                    if not raid_state.in_raid:
                        jump friendlyDinnerChoice
                    else:
                        $ raid_state.finish()
                    "Rowan swallowed heavily. Whether he liked it or not, he had a mission to accomplish."
                    "Rowan took the time to scout the village, identifying where his orcs should strike from."
                    "An hour later, he sent a message to castle Bloodmeen, sending them the location and required number of orcs for the attack."
                    "He didn’t wait to see the result. He already knew how it would all turn out."
                    #large gain of guilt, village is destroyed as normal
                    $ change_prisoners(3)
                    $ change_treasury(20*human_villages_defs[eventHex[6]][3])
                    # TODO Half of the village's military strength is deducted from the realm's strength.
                    # Heavy infamy and corruption penalty.  Rowan gains guilt.
                    $ change_base_stat('c', 5)
                    $ change_base_stat('f', 5)
                    $ change_base_stat('g', 2)
                    # Andras likes this choice, Alexia hates this choice in Rosaria.
                    $ change_relation('andras', 2)
                    $ change_relation('alexia', -2)
                    return

                "No.":
                    $ released_fix_rollback()
                    "… No. There were some lines he would never cross, and he didn't give a damn if the twins were going to lock him up for it."
                    #Return to decision tree. Only “Trade with it” is now selectable.
                    $ event_tmp['do_not_capture'] = True
                    jump friendlyDinnerChoice

        #else
        else:
            #destroy village normally
            call screen raid_menu(human_villages_defs[world.cur_hex[6]][2])
            if not raid_state.in_raid:
                jump friendlyDinnerChoice
            else:
                $ raid_state.finish()
            $ change_prisoners(3)
            $ change_treasury(20*human_villages_defs[eventHex[6]][3])
            # TODO Half of the village's military strength is deducted from the realm's strength.
            # Heavy infamy and corruption penalty.  Rowan gains guilt.
            $ change_base_stat('c', 5)
            $ change_base_stat('f', 5)
            $ change_base_stat('g', 2)
            # Andras likes this choice, Alexia hates this choice in Rosaria.
            $ change_relation('andras', 2)
            $ change_relation('alexia', -2)
            return


    "Trade with it.":
            $ released_fix_rollback()
            "Rowan was able to find the village elder quickly. The man proved reasonable enough, and after some negotiations, the two settled for a deal that satisfied both sides."
            "His business finished, Rowan left the village, moving on to the next location on his list."
            #add trade revenue as normal
            # Trading with it gives half to a quarter of its village value as regular income.
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)/100.0 ))
            # Gain a lose a small amount of infamy.  Lose a bit of corruption.
            $ change_base_stat('c', -1)
            $ change_base_stat('f', -1)
            # TODO The village's military strength can no longer be removed from the realm.
            # Alexia likes this choice in Rosaria.
            $ change_relation('alexia', 2)
            return
