#Private winery
#When claimed, gives a one time boost to morale.
init python:

    #Castle Wine demand events
    #Triggers on a Winery raid, event can happen multiple times until all outcomes have been seen
    event('castle_wine_demand', triggers='private_winery_raid', run_count=3, group='map_res_private_winery', priority=pr_map_res)
    event('castle_wine_demand_clamin', triggers='castle_wine_demand_subevent', run_count=1, group='map_res_private_winery', priority=pr_map_res)
    event('castle_wine_demand_skordred', triggers='castle_wine_demand_subevent', run_count=1, group='map_res_private_winery', priority=pr_map_res)
    event('castle_wine_demand_jezera', triggers='castle_wine_demand_subevent', run_count=1, group='map_res_private_winery', priority=pr_map_res)


label castle_wine_demand:
#Castle Wine demand events
#Triggers on a Winery raid, event can happen multiple times until all outcomes have been seen

#winery BG
scene black with fade
show jezera happy behind black

"The raid when off without a hitch. The winery was sacked, and anything of worth was packed up and delivered to the castle via the nearest portal."
"But a few days later, Rowan was contacted with a unique opportunity."

#choose one of the following at random, each one can only occur once
$ choose_and_insert_next_event('castle_wine_demand_subevent')
return


label castle_wine_demand_clamin:
#Cla-Min request. (subevent)
#Always (no requirement)

"He got a message from Cla-Min, who told him she saw the barrels arrive at the castle. Apparently, there was some sort of big festival going on in the Empire of Sands, and they would surely be short on good alcohol."
"Cla-Min could use the opportunity to turn a nifty profit for herself."
"She would consider it a personal favor if Rowan agreed to give her the wine instead of sending it to the orcs. She would ensure he would be properly compensated for the extra trouble."

#print morale in the below
"(Morale is at: [castle.morale])"

menu:
    "Give her all of the plundered wine.":
        $ released_fix_rollback()
        "An opportunity like that didn’t happen often. Rowan told Cla-Min she was free to take all of the recent plunder and do with it as she pleased. The goblin woman would be no doubt ecstatic at the news."
        "And as was promised, after returning to the castle, Rowan would find a hefty pouch full of gold coins in his room – with a personal thank you note from Cla-Min attached to it."
        "Sadly he also learned the orcs weren't exactly pleased with the fact the wine they fought for got sent away. If Rowan wanted to keep the morale high, he should probably find another winery soon."
        #GAIN: +Big favor with Cla-Min, + Personal gold (around 100?)
        #LOSE: small amount morale.
        $ change_relation('cla_min', 10)
        $ change_personal_gold(100)
        $ change_morale(-3)
        return

    "Give her some of the plundered wine.":
        $ released_fix_rollback()
        "An opportunity like that didn't happen often, but Rowan's primary concern was keeping the orc morale high. Still, he could spare some of the wine, and that's precisely what he told Cla-Min. She could have about a third of the barrels if she wanted to."
        "While this wasn’t what Cla-Min expected, Rowan knew she would understand that he wasn't exactly free to do with his resources as he pleased."
        "Upon returning to the castle, as was promised, he would find a small pouch filled with gold coins – and a polite thank you note from Cla-Min attached to it."
        #GAIN: +Small favor with Cla-Min, + Personal gold (around 30?), + less than usual morale boost.
        $ change_relation('cla_min', 5)
        $ change_personal_gold(30)
        $ change_morale(2)
        return

    "Refuse. You need to focus on raising morale right now.":
        $ released_fix_rollback()
        "While an opportunity like that did not happen often, the Orc morale was far too low for Rowan to entertain the idea of giving the wine away. He apologized to Cla-Min, telling her precisely that."
        "Cla-Min would be no doubt unhappy with the decision, but she understood Rowan had to put his responsibilities as the castle castellan first. It was unlikely she would hold the decision against him."
        #GAIN: normal winery morale boost. Cla-Min favour doesn’t change.
        $ change_morale(5)
        return

    "Tell her that if she wants it, she can buy it just like her clients will.":
        $ released_fix_rollback()
        "An opportunity like that didn’t happen often – and like hell would Rowan allow Cla-Min to keep all the profits to herself."
        "He told her that if she is guaranteed to make a profit in the Empire, then she can surely afford to pay for the wine – just as her clients will."
        "As he expected, he got a polite (if cold) answer, that Cla-Min will of course gladly pay for the stolen wine his orcs just plundered."
        "Rowan didn't appreciate the passive-aggressive tone, but he had far more important things to take care of, so he let the insult slide."
        "Upon returning to the castle, he would be informed that Cla-Min did indeed buy some of the wine. Around half of it was taken by her caravans, and the treasury was now considerably richer than it was before."
        #GAIN: +Castle gold (around 100?), + usual leve of morale
        #-Cla-Min favour (quite high).
        $ change_morale(5)
        $ change_treasury(100)
        $ change_relation('cla_min', -5)
        return


label castle_wine_demand_skordred:
#Skordred workers request.
#Always (no requirement)

"He got a somewhat unexpected message from an unfamiliar dark dwarf. The man was one of Skordred’s workers, from the team that was responsible for the castle's renovations."
"He informed Rowan he saw the wine barrels arrive through the portal and he was wondering if Rowan would consider sending some of them to him and his team."
"While Skordred might have considered bringing the castle back to its former glory a most glorious assignment, the people who did most of the digging and hammering had a more… Grounded view of the whole ordeal."
"Some alcohol could be a nice break from the usual monotony of their daily life."
"In return, he promised they would pull some extra hours to get his next project complete ahead of time, and under the budget. If Rowan agreed, he was likely to save around twenty percent of whatever he would choose to build next."

#print morale in the below
"(Morale is at: [castle.morale])"

$ event_tmp['asked_approval'] = False

menu castle_wine_demand_skordred_menu1:
    "Did Skordred approve this?" if not event_tmp['asked_approval']:
        $ released_fix_rollback()
        "Not wishing to go behind Skordred's back, Rowan inquired what did the master builder think of the whole thing."
        "In return, he got a vague suspicious answer, that Skordred was far too busy with his own work, and that they didn’t want to pester him about mundane stuff like that."
        #Return to the choice menu, 1 no longer available.
        $ event_tmp['asked_approval'] = True
        jump castle_wine_demand_skordred_menu1

    "Agree. Send them half of the wine.":
        $ released_fix_rollback()
        "He wasn’t exactly certain how the builders were planning to get the next project 'ahead of schedule and under the budget'.  And he wasn't certain if he really wanted to know."
        "Still, if it meant getting the castle operational sooner, then he could stomach turning a blind eye to some questionable corner cutting. He told the worker he would direct half of the barrels to their quarters."
        "In return, he received a sincere thank you message and a reassurance that he will most certainly be pleased with their work in the near future."
        #GAIN: + morale (half of the usual bonus), 20% discount on next building constructed.
        #LOSE: -small Skordred influence.
        $ change_morale(3)
        $ change_relation('skordred', -3)
        # TODO: discount on next building
        return

    "Refuse. You need that wine for the orcs.":
        $ released_fix_rollback()
        "While the worker’s offer sounded tempting, Rowan wasn’t certain if he wanted his builders to have access to alcohol. Plus, the wine was necessary to keep the orcs complacent."
        "He told the worker he couldn’t grant his request. In response, the man thanked Rowan for at least considering the idea."
        "In the end, the wine found its way to the orcs barracks, as was initially planned."
        #GAIN: normal winery morale boost.
        $ change_morale(5)
        return


label castle_wine_demand_jezera:
#Jezera request.
#Always (no requirement)

"… Though perhaps “opportunity” wasn’t the right word."
"When the wine arrived at Castle Bloodmeen, he got a direct message from Jezera herself. She noticed the new wine delivered and was wondering if he wouldn't mind if she took it for herself."
"She was about to host a party for some prospective allies… And the extra alcohol could be of use to her."
"... It was unusual for her to ask for permission for, well, anything. Rowan was fairly certain she was doing this just to bask in the feeling of absolute control she had over him. If he tried to oppose, it was certain she would not take it well…"

#print morale in the below
"(Morale is at: [castle.morale])"

menu:
    "Tell Jezera you don’t mind.":
        $ released_fix_rollback()
        "Immensely pleased with herself, Jezera thanked Rowan for being oh so accommodating with her wishes."
        "Then, she cut the connection, and that was it."
        #Gain: + small jezera Influence. No morale reward.
        $ change_relation('jezera', 3)
        return

    "Explain you cannot afford to send the wine away.":
        $ released_fix_rollback()
        "Swallowing heavily, Rowan started explaining that with the current state of the orc morale, they really couldn't afford to send any of that wine away. Perhaps he could-"
        "Before Rowan could offer an alternative solution, Jezera cut him off, coldly reminding him that she really needs that wine and that most certainly there would be no issue if she grabbed some of it, right?"

        menu:
            "Stand your ground.":
                $ released_fix_rollback()
                "Against his better judgment, once more, Rowan repeated that they couldn't afford to spend the wine on parties."
                "Jezera replied with a simple “I see”, and cut the link."
                "Rowan half expected to get message sometime later that Jezera took the wine after all."
                "But to his great surprise, not only did the half-demoness respected his decision, but he also received a message from Andras, who praised him for not allowing his sister to waste valuable resources on pointless banquets."
                "He might have lost some favor with Jezera, but at least Andras and the orcs were pleased with his decision."
                #Gain: + Small Andras Influence, + usual morale.
                #LOSE: -medium Jezera influence.
                $ change_morale(5)
                $ change_relation('jezera', -5)
                $ change_relation('andras', 3)
                return

            "Relent.":
                $ released_fix_rollback()
                "Suppressing a sigh, Rowan agreed that they will probably manage to get by without it."
                "Coldness instantly evaporated from Jezera's voice, as she mockingly thanked Rowan for being oh so accommodating with her wishes."
                je "There, that wasn't so difficult, was it?"
                "She asked at the end and cut the connection between them.  Maybe next time, it would best to simply submit at the start, rather than risk Jezera's anger?"
                #Gain: + small jezera Influence. No morale reward.
                $ change_relation('jezera', 3)
                return
