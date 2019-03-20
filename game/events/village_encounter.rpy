# events for village interactions (occypy, destroy etc.)
init python:

    # general top level event for village, town, trade center
    event('village_general', triggers=('map_res_3', 'map_res_4', 'map_res_5',), group='village', priority=pr_map_res)
    #Unscrupulous Noble
    # Only occurs after PC has ransacked one village
    event('unscrupulous_noble', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=('castle.villages > 0',), run_count=1, group='village', priority=pr_map_res)


    # Event 1: Choice between extra income or injury and extra loses.
    event('occupy_ev1', triggers='village_occupy', run_count=1, group='village_occupy', priority=pr_map_res)
    # Event 2: Chance at less guilt, Req: Rowan's morals are at least mostly intact (low corruption).
    event('occupy_ev2', triggers='village_occupy', conditions=('avatar.corruption <= 10',), run_count=1, group='village_occupy', priority=pr_map_res)
    # Event 3: More guilt, Req: Rowan's morals are intact (low-ish corruption).
    event('occupy_ev3', triggers='village_occupy', conditions=('avatar.corruption <= 10',), run_count=1, group='village_occupy', priority=pr_map_res)
    # Event 4: Neutral
    event('occupy_ev4', triggers='village_occupy', run_count=1, group='village_occupy', priority=pr_map_res)
    # Event 5: Neutral
    event('occupy_ev5', triggers='village_occupy', run_count=1, group='village_occupy', priority=pr_map_res)
    #Event 6: Neutral
    event('occupy_ev6', triggers='village_occupy', run_count=1, group='village_occupy', priority=pr_map_res)
    #############
    # Event1: Chance at more prisoners and fewer casualties.
    event('destroy_ev1', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)
    # Event 2: Neutral.
    event('destroy_ev2', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)
    # Event 3: More gold and casualties.
    event('destroy_ev3', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)
    # Event 4: Neutral.  Req: Orc soldiers participate in raid.
    # TODO check that orcs are in raid
    event('destroy_ev4', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)
    # Event 5: Less gold.  Req: Famine is not resolved.
    event('destroy_ev5', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)
    # Event 6: Neutral
    event('destroy_ev6', triggers='village_destroy',  run_count=1, group='village_destroy', priority=pr_map_res)
    ######### Trade Events ##########
    #Event 1: Neutral
    #Req: Player must not have learned the rumour about the goblin prince
    event('trade_ev1', triggers='village_trade',  conditions=('not new_goblin_prince_rumor',), run_count=1, group='village_trade', priority=pr_map_res)
    #Event 2: Less trade income
    event('trade_ev2', triggers='village_trade', run_count=1, group='village_trade', priority=pr_map_res)
    #Event 3: Free random item
    event('trade_ev3', triggers='village_trade',  run_count=1, group='village_trade', priority=pr_map_res)


label village_general:
# general event, allows to run subevents based on player choice
# for village, town, trade center
$ temp1 = human_villages_defs[eventHex[6]][0]
$ temp2 = human_villages_defs[eventHex[6]][1]
$ temp3 = human_villages_defs[eventHex[6]][2]
"Rowan has located a human village. It is a [temp2]. It has a military power of approximately [temp3], and that will need to be overcome in order to capture or destroy the [temp1]."
menu vg_menu:
    "Leave it be":
        $ released_fix_rollback()
        # No requirements.
        # Does nothing and returns you to the map without having explored the resource, allowing you to return later.
        $ prevent_tile_exploration()
    "Occupy it" if castle.military > human_villages_defs[eventHex[6]][2]:
        $ released_fix_rollback()
        $ raid_state.reset()
        # Requires non-temporary military strength > town military strength.
        # TODO Occupying it requires that you spend soldiers, magic users, or monsters on taking the village.
        call screen raid_menu(human_villages_defs[eventHex[6]][2])
        if not raid_state.in_raid:
            jump vg_menu
        else:
            $ raid_state.finish()
        # This gives regular income equal to the village's value.
        $ castle.villages += 1
        $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
        # TODO Half of the village's military strength is deducted from the realm's strength.
        # Gain a small amount of infamy.  Rowan gains guilt.
        $ change_base_stat('f', 2)
        $ change_base_stat('g', 2)
        # Scouting the village, arrival of the soldiers, people forced to recognize new masters, troops settling in.  These will sometimes change the result of capturing villages.
        # Choose one of the following at random after choosing to occupy and selecting your risked forces.
        $ choose_and_insert_next_event('village_occupy')
    "Destroy it" if castle.military > human_villages_defs[eventHex[6]][2]:
        $ released_fix_rollback()
        # Requires non-temporary military strength > town military strength.
        # TODO Destroying it requires that you spend soldiers, magic users, or monsters on taking the village.
        call screen raid_menu(human_villages_defs[eventHex[6]][2])
        if not raid_state.in_raid:
            jump vg_menu
        else:
            $ raid_state.finish()
        # This gives 20 weeks worth of income from the village immediately and captures a number of prisoners.
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
        # Raid, rape, pillage, and burn.  Loot and prisoners brought back to the castle.
        # Choose one of the following at random after choosing to destroy and selecting your risked forces.  These will sometimes modify the normal result for destroying villages.
        $ choose_and_insert_next_event('village_destroy')
    "Trade with it" if castle.buildings['tavern'].lvl > 0:
        $ released_fix_rollback()
        # Requires a tavern.
        # Trading with it gives half to a quarter of its village value as regular income.
        $ castle.villages_income += int(temp3 * ( (dice(25) + 25)/100.0 ))
        # Gain a lose a small amount of infamy.  Lose a bit of corruption.
        $ change_base_stat('c', -1)
        $ change_base_stat('f', -1)
        # TODO The village's military strength can no longer be removed from the realm.
        # Alexia likes this choice in Rosaria.
        $ change_relation('alexia', 2)
        $ choose_and_insert_next_event('village_trade')
    "Infiltrate it" if get_spies('idle'):
        $ released_fix_rollback()
        # Requires an available spy.
        # Infiltrating takes up the spy for a while, rewards are given after they finish but you cannot return to the village after starting the infiltration.
        # This gives regular income equal to the village's income.
        # Half of the village's military strength is deducted from the realm's strength.
        # TODO: deduct military from realm
        # Lose a small amount of infamy, but gain corruption.  Rowan gains guilt.
        # Jezera likes this choice.
        $ change_relation('jezera', 2)
        $ change_base_stat('f', -1)
        $ change_base_stat('c', 2)
        $ change_base_stat('g', 2)
        $ menu_res = renpy.display_menu([(spy.name, spy.uid) for spy in get_spies('idle')])
        $ assign_mission(spy_uid=menu_res, type='infiltration', loc=(world.cur_map.uid, tuple(world.cur_map.pos)), started=week)
        if get_object(menu_res).mission:
            $ msgs.show('{{color=#C6FE56}}New spy mission ({}):\n "{}" at {} (dur. {}){{/color}}'.format(get_object(menu_res).name, get_object(menu_res).mission.label,
            ' '.join((str(world.cur_map.uid), str(tuple(world.cur_map.pos)))), get_object(menu_res).mission.duration))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label occupy_ev1:
# Event 1: Choice between extra income or injury and extra loses.
scene bg4 with fade
"During the attack, Rowan found himself cornered by several of the town's people who'd taken up arms as an impromptu militia. He would easily be able to take down the unarmored townsfolk if he went all out, but most of them would die if he did."

menu:
    "Try to use non-lethal tactics.":
        $ released_fix_rollback()
        "Rowan did his best to avoid delivering lethal blows wherever possible.  This delayed him significantly and he ended up being hurt in the confused melee."
        "Once he rejoined the other attackers he realized that they'd taken more losses than they would have if he hadn't wasted as much time as he did with his own attackers."
        # Rowan is injured, lose extra soldiers, + town income.
        $ add_effect(Injury('Wound', 'strength', -2))
        # TODO lose extra soldiers
        $ castle.villages_income += 3


    "Take no chances.":
        $ released_fix_rollback()
        "In war, you cannot afford to be merciful to your enemies.  The words felt hollow to Rowan as he cut down all of the men who'd tried to stand up to him with brutal efficiency."
        "He rejoined the other soldiers soon after, helping them take down the rest of the defenders.  Afterwards they counted up the people who'd been subjugated, far fewer than they'd hoped. The militia had cost them much of their prize."
        # - town income.
        $ castle.villages_income += 3
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label occupy_ev2:
# Event 2: Chance at less guilt, Req: Rowan's morals are at least mostly intact (low corruption).
scene bg1 with fade
$ temp = human_villages_defs[world.cur_hex[6]][0]
"While scouting the [temp], Rowan unexpectedly ran into someone who'd been a soldier with him at Karst during the war. The old acquaintance quickly caught on that there was something agitating about this meeting for our hero, but wasn't sure why."
"Hoping to at least spare this one and their family from the attack that would be arriving soon, Rowan attempted to convince them to leave the village immediately."

# deceive test - difficulty 10
if check_skill(10, 'deceive')[0]:
    # success
    $ released_fix_rollback()
    "The trust that had been built up all those years ago was still intact, so the old soldier obeyed their former commander's suggestion, even without a proper explanation."
    "The family escaped the attack that followed and Rowan felt better about having not abandoned one who he'd protected all those years ago."
    # Less guilt gained.
    $ avatar.base_guilt -= 1
else:
    # failure
    $ released_fix_rollback()
    "While a strong bond of trust had been established with all his soldiers during the siege, it had been a long time since their former commander had seen or spoken to them."
    "The family wasn't willing to leave without a proper explanation why, which forced Rowan to simply let them be taken when the attack came. He couldn't bring himself to check if any of them had survived afterwards."
    # no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label occupy_ev3:
# Event 3: More guilt, Req: Rowan's morals are intact (low-ish corruption).
scene bg4 with fade

"Rowan wandered the streets, cloak held close.  It was over an hour after the attack had finished and all that was left was the aftermath. He found the occasional body laying on the ground, other times there was the sound of weeping from one of the buildings."
"Of course, there was also the patrolling soldiers.  They were excited and celebrating over the latest conquest, but Rowan hardly noticed them."
"He entered the town square where the defenders had made their last stand. This place contained a great tree in its center. A thing that had once been a sign of prosperity and joy, now bodies swung there as a warning against defiance."
"Andras had made him watch as he strung those men and women up. Even now, Rowan could neither will himself to look away, nor bare to look any longer."
#extra guilt.
$ avatar.base_guilt += 1
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label occupy_ev4:
# Event 4: Neutral
scene bg4 with fade

"Another town had fallen, with the twins power growing stronger each week. Hidden by his cloak, Rowan walked through the newest conquest he'd helped his masters claim."
"Each of the survivors was adapting in their own ways. Some drank, some tried to act like nothing had happened. He saw one woman who'd essentially offered herself to one of the orcs that had been assigned to guard this place."
"The hero watched her for a few minutes, eventually learning that the woman was a widow with two children and hoped that she'd be able to get her new man to protect her and her children. Apparently she'd done the same with the previous mayor."
"Rowan supposed that this really would be a lot like the old life for many of the villagers, only their rulers had changed. That wouldn't bring back the lives lost in the transition, but now some things were no different now than they had been."
# no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label occupy_ev5:
# Event 5: Neutral
# countryside background.
scene black with fade

"This town had been fairly normal as far as Rosarian towns went. After finishing his report, Rowan was surprised when his master started a conversation with him instead of just ending the communication there."

show rowan hood neutral at midleft with dissolve
show andras displeased behind black

an "So servant, have you finished adjusting to your duties to us? You seem calmer this time."

"Rowan thought for a moment before he answered."

# Rowan's morals are intact (low corruption).
if avatar.corruption < 5:
    $ released_fix_rollback()
    ro "No, I don't think I'll ever get use to helping you conquer people. I'd always fought to end wars, not start them."
    an "Well, as long as you do your job, I suppose I don't really care if you like it or not."
    an "Then again, you are an absolute joy to torment. It would be a shame if you got used to seeing people suffer."

# Rowan's morals are partially intact (medium corruption).
elif avatar.corruption < 10:
    $ released_fix_rollback()
    ro "I suppose I am. It still hurts whenever I watch another village be taken, but not as much as it used to."
    an "Shame. I did so like tormenting you. Still, I guess one can only spend so long with someone like me before I start to rub off on them."

# Rowan's morals are gone (high corruption).
else:
    $ released_fix_rollback()
    ro "My beliefs have shifted quite a bit while in your services. I haven't had much of a choice in the matter."
    an "While I did so enjoy tormenting you, having such a skilled and willing servant more than makes up for my lost fun."
    an "We will be there soon. It is time to bring more into our budding empire."

# no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label occupy_ev6:
#Event 6: Neutral
scene bg4 with fade

"Andras took to the field, leading the assault on the town with Rowan's report telling him exactly what to expect and deal with."
"His soldiers cheered as his demonic magic tore through the confused defenders, causing screams of panic. It truly was a horrifying thing to see such a powerful being launch a surprise attack like this, unleashing all his might at once."
"Most people had no idea what the strength and power of a demon would be, so such a show of power quickly cowed most."
"Those that did manage to stand strong would sometimes make suicidal charges against the creature, but would quickly be cut down by the red man himself, or the cloaked swordsman at his side."
"Eventually all those willing to fight were either dying or dead and the town was captured."
# no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label destroy_ev1:
# Event1: Chance at more prisoners and fewer casualties.
scene bg1 with fade

"While scouting the village, Rowan realized that these people were in pretty rough shape. A local epidemic had drastically weakened them and they'd have a very tough time mounting a strong resistance."
"Even still, when your homes and lives are at stake humans could prove to be quite tenacious."
"Struck by an idea, he retreated from the village and then returned wearing his cloak after delivering his report, but before the attack arrived."

# Diplomacy check, difficulty 10
if check_skill(10, 'diplomacy')[0]:
    # success.
    $ released_fix_rollback()
    "He managed to convince several of the people in the town to give up without a fight, given that they were already very weak. When Andras arrived, they willingly allowed themselves to be chained after the remaining defenders were dealt with."
    # Extra prisoners, fewer casualties.
    # TODO capture prisoners, casualties
else:
    # fail.
    $ released_fix_rollback()
    "Unfortunately, his attempt to cowe the people into surrendering backfired. Instead, they rallied and put together a strong defence against the oncoming attack, making up for their weakened states."
    "The town fell anyway."
    # no effect.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label destroy_ev2:
# Event 2: Neutral.
scene bg1 with fade

"Not faces, not people."
"Rowan walked the streets, noting the defences and potential defenders."
"Not screams, not tears."
"He continued on his way, never responding to the words directed to him or acknowledging friendly waves or nods."
"Not pain, not death."
"Deep inside the recesses of his mind, he heard the horrible sounds of battle and of destruction. Town bells, people screaming. Sounds he'd caused before, and was about to cause again."
"No! No!"
"Desperately he tried to ignore the phantoms within, there was no attack happening."
"Then he gave his report to Andras...."
# no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label destroy_ev3:
# Event 3: More gold and casualties.
scene bg4 with fade

"The twin's army blitzed into the town in an attempt to prevent those within from fleeing. An opportunity had presented itself here, there was a fairly sizable trading caravan currently in the town."
"Within minutes, they'd surrounded and captured the wagons after slaughtering the merchants and guards. Andras roared in triumph with his troops, then turned his attention to the approaching townsfolk."
"Ignoring Rowan's primary battle plan had given him this prize, now he would have to pay the price for it in men. The red demon didn't mind."
# gain gold, but lose soldiers.
$ change_treasury(20)
# TODO casualties
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label destroy_ev4:
# Event 4: Neutral.  Req: Orc soldiers participate in raid.
scene bg4 with fade

$ temp = human_villages_defs[world.cur_hex[6]][0]
"Having dealt with the defenders, the orcs raged through the [temp]. They exalted in their triumph and went about their work with a savage glee that made Rowan sick to his stomach."
"Homes were ransacked, everything of value thrown out onto the streets to be gathered up later. Then they burned them."
"The survivors of the carnage could only watch in horror. Then they were bound, chained, and dragged away. Soon they'd be brought to the dungeons under castle Bloodmeen. To the cells that their hero had been kept in and broken by."
"That man stood next to his new master, the red demon Andras. Once again, he'd been forced to watch as the orcs went about their work."
# no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label destroy_ev5:
# Event 5: Less gold.  Req: Famine is not resolved.
scene bg5 with fade

"They'd found so much less than he'd expected."
"Rowan picked through the loot that had been retrieved from the (villagesize) after it's destruction. The people had been right, they didn't have that much less."
"The bad harvests had hit this place particularly hard and the townspeople had sold off most of their valuables in order to buy food."
"First they had lost their food, then their money, then their homes, and now their freedom. Just what had been gained from such a steep bill?"
# - gold gained.
$ change_treasury(-10)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label destroy_ev6:
# Event 6: Neutral
scene bg4 with fade

"The sounds of battle had passed, the screams were gone, all that was left was a burning ruin. An hour ago, the (villagesize) had come under attack. Now it was empty save for a cloaked figure stalking the streets."
"It silently moved from one building to the next, checking each body it found on the ground."
"Finally it came to a young woman who'd been cut down from behind. She seemed to have been carrying something. The figure turned her over and pulled a small baby out from underneath her."
"The child cried.  It still lived, but it couldn't understand that its mother was dead."
"The cloaked figure simply took the child and walked away from the scene of devastation. Trying to forget that he was responsible for this."
# no effect.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label trade_ev1:
#Event 1: Neutral
#Req: Player must not have learned the rumour about the goblin prince
scene bg1 with fade

"While making the trading arrangements, Rowan heard a story about the goblins in Blackholt forest. While there was always some sort of news coming from there about something awful, there was something mixed in with the usual fare."
"Apparently a new leader had emerged in the tribes calling themselves 'Tue-Row'. The rumors couldn't agree on exactly what he'd accomplished, but it sounded like he'd rallied a large number of their kind under his banner."
"Already the townspeople were cursing this prince of goblins, as his name was now being cried in honor when the tribal folk of Blackholt launched attacks or fought the people of Rosaria."
"Rowan filed this information under important and resolved to seek more details when he could."
# Learn about Tue-Row the goblin prince.  This qualifies the player for Cla-Min's goblin history event.  Other events telling the player about Tue-Row are disabled.
$ new_goblin_prince_rumor = True
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label trade_ev2:
#Event 2: Less trade income
scene bg1 with fade

"In the coming weeks of trading with the village, the caravans find themselves always paying extra for the goods they trade. Whether it be due to some new tax or tariff, there's always something there so that the mayor can pocket a little extra."
"While the local people foot some of the cost of this corruption, it's mostly preying on the traders of Bloodmeen. They aren't the ones that could vote the mayor out, after all, and he's making plenty out of this to buy any votes he needs to stay in charge."
#Reduce trade income.
$ castle.villages_income -= 2
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label trade_ev3:
#Event 3: Free random item
scene bg1 with fade

"That Rowan was making trading arrangements surprised the townspeople, however they were quite willing to look past it."
"While the hero was quite versed in the arts of deception, though he rarely employed them outside of battle. At least, that was before he came into the service of the demonic twins."
"This village was in fairly dire straights before Rowan arrived today, so they were especially willing to believe whatever anyone told them if it meant they'd get a chance at the things they desperately needed."
"These people wanted to believe that their hero had brought them salvation as a trade broker. So much so, that they even gave a gift in appreciation for what had been done."
#Receive a random item, (modified by luck).
$ get_rnd_item(0, (100 + avatar.luck * 5))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label unscrupulous_noble:
#Unscrupulous Noble
$ released_block_rollback()
# Only occurs after PC has ransacked one village
# Triggers off Destroy, Conquer or Trade options
$ temp = False
$ temp1 = False
$ temp2 = False
show bg1 with fade
show rowan necklace neutral behind bg1

"Rowan was just beginning the process of reconnoitring this particular settlement, when he spotted a small party of horsed humans trotting around the perimeter - two young women and a man."
"By his straight back and fine clothes Rowan guessed the man to be of noble descent; the other two wore plainer clothes and looked uncomfortable on horseback. They seemed to be on the look-out for something."

#stealth check dc20
#Pass
if check_skill(20, 'move_silently')[0]:
    "Rowan melted quietly back into the woods and considered. He could approach them and try and parlay - or he could ignore them and launch an attack upon the village."
    # 10 XP gain
    $ add_exp(10)
    #menu
    menu:
        #Choice: Parlay (go to parlay)
        'Parlay':
            jump .parlay
        #Choice: Conquer the village (go to standard conquer outcome)
        'Conquer the village':
#~             call run_events('village_occupy', 2) from _call_run_events_4
            $ choose_and_insert_next_event('village_occupy')
            return
        #Choice: Destroy the village (go to standard destroy outcome
        'Destroy the village':
#~             call run_events('village_destroy', 2) from _call_run_events_5
            $ choose_and_insert_next_event('village_destroy')
            return
################################################################################
label .parlay:
#Fail or Parlay
rnb "Good sir!"
"As soon as the horseman spied Rowan upon the road, he cantered over with a welcoming smile."
rnb "Ah, I am glad we were in good stead to intercept you, milord. Welcome to my fiefdom - such as it is."
"He indicated the small town beyond. The two young women smiled at Rowan demurely."
ro "Charming"
rnb "Indeed. Words of your, ah, recent deeds have reached us, milord. That perhaps you serve... different masters these days."
ro "I don't know exactly what you've heard, but you must understand that I had no-"
rnb "Please, sir! I know only too well of the onuses of authority. The awful decisions that must be made, the responsibilities that must be undertook."
rnb "That, indeed, is why I am standing here. I wish to come to - let's call it a gentlemen's agreement."
rnb "My serfs and craftsmen have many things of worth I would be happy to trade to you and the, ahem, powers you represent, if you would be willing to spare this place and bring it under your aegis."
rnb "If, I say, if you are willing to come to reasonable terms. A small tariff. The Baron is unlikely to look upon high treason favorably, after all!"
ro "You bargain for better money when the lives of your subjects are at stake?"
rnb "I know how to sweeten a deal, sir."
"The nobleman indicates, and the two women clop slowly forward. Both comely village lasses, Rowan saw, one flaxen-haired and the other chestnut, sunburnt and healthy."
oll "Ooh, look at the arms on him, Brinnid. And doesn't his hair just shine!"
bri "*giggling* No, I wouldn't mind seeing to that - even if I did have to share."
rnb "You have travelled far, milord, and I suspect you have further yet to go. Wouldn't it be nice to relax in well-appointed surroundings with pleasant, willing company for a while?"
rnb "These two shall be yours, each and every time you choose to visit - if you will simply agree to a reasonable trade deal."

#menu
menu:
    #Choice: Agree (go to agree)
    'Agree':
        jump .agree
    #Choice: Agree without the girls (go to agree without the girls)
    'Agree without the girls':
        jump .agree_without_girls
    #Choice: Negotiate a better trade deal (go to negotiate a better trade deal)
    'Negotiate a better trade deal':
        jump .negotiate_better_deal
    #Choice: Negotiate for slaves (go to negotiate for slaves)
    'Negotiate for slaves':
        jump .negotiate_for_slaves
    #Choice: Refuse (go to refuse)
    'Refuse':
        jump .refuse
################################################################################
label .refuse:
#Refuse
ro "You disgust me, sir. Surrender now, or I shall take this place by force."
rnb " I- I should have known better than attempt reason with demon cocksuckers! You shall not find my men wanting steel, or bravery!"
"The nobleman quickly turned and galloped back to the village, the girls in tow. The element of surprise gone, Rowan had to decide how to approach the assault."
#menu
menu:
    #Choice: Conquer the village (go to standard conquer outcome)
    'Conquer the village':
#~         call run_events('village_occupy', 2) from _call_run_events_6
        $ choose_and_insert_next_event('village_occupy')
        return
    #Choice: Destroy the village (go to standard destroy outcome
    'Destroy the village':
#~         call run_events('village_destroy', 2) from _call_run_events_7
        $ choose_and_insert_next_event('village_destroy')
        return
################################################################################
label .agree_without_girls:
#Agree without the girls
ro "I am a married man, sir. You do everyone present a grave disservice by attempting to whore your subjects."
rnb "I- I apologize unreservedly, milord. These are... desperate times, and when I heard of what had taken place elsewhere, I thought I must-"
ro "That's enough. I have no wish to spill blood in this place, and have no issue with agreeing to a trade tariff with you, so long as the extra money goes towards the upkeep of the village."
rnb "You... truly are the hero the ballads have you as, aren't you? My word. I, of course, agree unreservedly."
"The man took off his hat and bowed sweepingly to Rowan, before slowly trotting back towards the village. Rowan could hear the two girls murmuring between themselves in slightly awestruck tones about his honor and chivalry as they followed suit."
"Of course, once the twins understood the terms under which the village fell under their control, they were less impressed."
show andras angry behind bg1
an "You AGREED to this ludicrous arrangement without any reason to?! Do you not have an army to impose your will? Are you man, or slug?"
show jezera displeased behind bg1
je "I must agree. Buying their mundane goods for better money without cause makes us look weak and incredibly foolish. No good shall come of it, once word spreads."
"Still, despite a lengthy browbeating session, Rowan got his way."
#Village taken, less income, infamy down a small amount, corruption down a small amount
$ castle.villages += 1
$ castle.villages_income += human_villages_defs[world.cur_hex[6]][3] - 2
# TODO Half of the village's military strength is deducted from the realm's strength.
$ change_base_stat('f', -2)
$ change_base_stat('c', -2)
#end event
return
################################################################################
label .negotiate_better_deal:
#Negotiate a better trade deal
ro "I would be very happy to resolve this peacefully under such tempting terms. But you must understand my masters drive a very hard bargain. Lower your demands somewhat, and we will have an agreement."

#diplomacy check DC 15
if not check_skill(15, 'diplomacy')[0]:
    #fail
    rnb "No, milord. These are my terms I must stand by them. If we are to serve you and yours, we must make the most of it."
    #menu
    menu:
        #Choice: Agree (go to agree)
        'Agree':
            jump .agree
        #Choice: Refuse (go to refuse)
        'Refuse':
            jump .refuse
else:
#pass
    rnb " It seems... trifling to note that you hold all of the cards here, milord. Very well - we shall agree upon your terms. The village is yours. Perhaps now you would like to retire with my companions? I have a place readied."
    #go to agree
    $ temp2 = True
    jump .agree
################################################################################
label .negotiate_for_slaves:
#Negotiate for slaves
ro "I would be very happy to resolve this peacefully under such tempting terms. However, you must understand that my masters are not interested merely in money."
ro "You have a whole village of peasants you are willing to bargain with - bring me a small number of them. You and the rest shall be spared, and I shall agree to your offer."

#diplomacy check DC 15
if not check_skill(15, 'diplomacy')[0]:
    #fail
    rnb "No, milord. These are my terms I must stand by them. If we are to serve you and yours, we must make the most of it."
    #menu
    menu:
        #Choice: Agree (go to agree)
        'Agree':
            jump .agree
        #Choice: Refuse (go to refuse)
        'Refuse':
            jump .refuse
else:
#pass
    rnb "I... I did suspect that this would be part of the bargain. I shall see to it. Whilst I do, perhaps you would like to retire somewhere quiet with my companions? I have a place readied."
    #go to agree
    $ temp = True
    jump .agree
################################################################################
label .agree:
#Agree
ro "Very well. Far be it from me to say no and spill blood instead of agreeing to such a pleasant arrangement."
rnb "I was always told you were a reasonable man, milord. The village is yours. Now, perhaps you would like to retire somewhere quiet with my companions? I have a place readied."

scene black with fade

"Hand-in-hand with the blonde and brunette, Rowan was led to a chalet in the woods above the village."
"The two girls chatted warmly with him, mentioning all the little eccentricities of their home and how happy they were such a storied and powerful hero of the realm now had his hand over it."
"Rowan felt himself relaxing; was this really such a terrible way to avoid bringing the orcs in and storming the place? Not at all."
"He curled his arm around Brinnid and Ollia's waist and winched the soft weight of their thighs into his side, to a chorus of coos and giggles."
"The chalet was comfortable, heavy on silk pillows, a large bucket bath in one room and a double bed in the other. Rowan wondered just how often the nobleman used this place to get away from his wife."
"All other thoughts except the growing, throbbing need in his pants disappeared, however, once he had sat himself down in a throne of pillows and Ollia began to remove his armor piece by piece."
"All the while Brinnid placed kiss after lascivious kiss upon his face and chest, pressing her firm breasts into him. Rowan gasped slightly as he felt warm, slender, work-roughened hands coil around his cock."
bri "What would you like, milord? I'm sure a worldly knight such as yourself knows all sorts of things…"
"For all their pleasantness Rowan could feel and hear urgency about the two peasant girls; a deep desire to please him and save their home in so doing."

menu:
    "Sapphic make-out.":
        $ released_fix_rollback()
        show cg184 with fade
        show rowan necklace naked behind cg184
        "Rowan's eye fell on a vial of oil upon a shelf, undoubtedly kept there for just such an occasion. He slipped out of the two girls' grasp and collected it."
        ro "Here. Oil yourselves. It would please me... for you to please yourselves."
        "He settled back amongst the cushions and watched as they slowly stripped, revealing their lean bodies and tender, small-nippled breasts, before Brinnid pooled oil onto her hands and sent them roaming across Ollia's sunburnt-striped skin."
        "They were laughingly awkward and blushing at first, not used to caressing other women quite in this way, but as more and more of their flesh gleamed wetly under the candlelight they lost themselves in it."
        "Their arousal grew as they were brushing over each others' erect nipples, delving with oil-slathered fingers between thighs to make the other gasp, jerk and moan."
        "Rowan watched it all hungrily, stroking himself, a thrill running through him each time the girls looked towards him coquettishly, slick hands imbedded deep in one another."
        "A wolfish lust overtook him, and he could not help himself reaching out to sink his hands deep in the warm, oiled flesh on display, culminating in Ollia riding him, cock jerking deep within her with each urgent push of her hips."
        "Brinnid watched, fingering her oil-smeared cunt with her thighs splayed."
        show cg184 with sshake
        show cg184 with sshake
        show cg185 with flash
        pause 3
        "Rowan groaned as the floodgates opened and he unloaded flagrantly within the girl, holding her firmly by the ass and shoulder so she took every thick, warm, flume, her moans and sighs rich in his ears."
        jump .villagegirlsconclusion

    "Double blowjob.":
        $ released_fix_rollback()
        show cg81 with fade
        show rowan necklace naked behind cg81
        pause 3
        "The sugar of power and dominance pulsing through his veins, Rowan opened his hips, hand around his thick, proud erection."
        ro "Lick, both of you. That is how you can please your lord."
        "They stripped, revealing their lean bodies and tender, small-nippled breasts, and knelt between his thighs happily enough."
        "Shoulder to shoulder, hands sliding over his flat, doughty stomach, they laid their warm, rough tongues upon his penis and lapped it up and down, laying wet kisses on its bulging head with their pretty lips, twinkling eyes fixed upon his face."
        "Pleasure flared up Rowan's shaft with tightening intensity with every pass and wick of their tongues, and at last he felt compelled to sink his fingers into each one's silken hair, holding them close to his bulging cock as orgasm overtook him."
        show cg81 with sshake
        show cg81 with sshake
        show cg82 with flash
        pause 3
        "Brinnid and Ollia twitched and laughed in soft shock as load after load surged out of his enflamed dick, painting their faces with thick, musky seed."
        "Color high on her cheeks, the former reached out her lips when Rowan had pulsed his last, enveloping his tender head and sucking it quite clean."
        jump .villagegirlsconclusion
################################################################################
label .villagegirlsconclusion:
"Still naked, the two peasant lasses heated and poured a lavender-scented bath whilst Rowan dozed in a post-coital bliss, and then relaxed in there with him, cleaning every inch of his sweaty, travel-hardened frame with slow passes of cloth, soap and pumice."
"By the time they were done Rowan's lust was almost completely rekindled - he envisaged bending one or both of them over in the hot water, rutting them senseless for their keen efforts. But..."
ro "I must go."
bri "Aww!"
oll "If you must, milord. Remember - if you pass this way again, this place of comfort is always ready to welcome you. As are we."
"His hands trailed out of theirs as he emerged out of the bath, towelled himself down, clambered back into his gear and departed down to the village's gate."

scene bg1 with fade
show rowan necklace neutral behind bg1

rnb "I note a spring in your step, milord. Did one find the comforts on offer here sufficiently diverting?"
ro "Yes."
"Now he was back in the fresh air with his balls recently emptied, Rowan felt guilt weigh upon him for his lecherous actions, a sensation not helped by the nobleman's knowing smirk."

if temp:
    #if Rowan successfully negotiated for slaves
    "It felt all the worse for the train of people behind him - five able-bodied men and women, roped together at the neck."
    "Their expressions were blank and ashen-faced, unable to believe what was being done to them."
    rnb "I trust this tribute will suffice, and we now have a deal?"
    ro "You have... you have done well, and my masters will be appeased. Go now."
    "He pointed firmly at the track leading away from the village, and with a terrible shudder and mumbling moan, the five prisoners shuffled their way into their new life. Rowan summoned some orcs to lead them to the portal."


rnb " I trust we now have a deal?"
ro "Yes. I am glad we were able to resolve this peacefully. Go now."
"He used his necklace to tell the demons about the most recent addition to their demesne."
show andras displeased behind bg1
an "Pah! It sounds as if this nobleman ran rings around you. I would have had him gutted for his arrogance, and then taken the women whilst still covered in his blood!"
show jezera happy behind bg1
je "Do stop with your awful nonsense, brother. Rowan has acted admirably. I'm so glad that he is starting to use his position of authority to enjoy the finer things in life - all the while garnering support for us without wasting a single soldier."
je "Truly how a dark lord should act!"

if temp:
    #if Rowan successfully negotiated for slaves
    an "At least he was smart enough to levy some slaves out of this worthless heap of mud. There, at least, potential lies."

"There the interview concluded, and Rowan stepped out from the newly conquered village."

#If agree: less income from village, corruption up.
$ castle.villages += 1
$ castle.villages_income += human_villages_defs[world.cur_hex[6]][3] - 2
# TODO Half of the village's military strength is deducted from the realm's strength.
# Gain a small amount of infamy.  Rowan gains guilt.
$ change_base_stat('f', 2)
$ change_base_stat('g', 2)
$ change_base_stat('c', 2)
#If successfully negotiate for better deal: 10xp, standard income from village, corruption up.
if temp2:
    $ add_exp(10)
    $ castle.villages_income += 2
    $ change_base_stat('c', 2)
if temp:
#If slaves: 10xp, less income from village, corruption up, guilt up, +5 prisoners.
    $ add_exp(10)
    $ change_base_stat('c', 2)
    $ change_base_stat('g', 2)
    $ change_prisoners(5)
#end event
return
