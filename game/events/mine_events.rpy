# events for mines (hire workers, deploy soldiers etc.)
init python:

    # general top level event for small mine, important mine, mining network
    event('mine_general', triggers=('map_res_6', 'map_res_7', 'map_res_8',), group='mine', priority=pr_map_res)
    # Quarantined Mine
    event('quarantined_mine', triggers=('map_res_6', 'map_res_7', 'map_res_8',), conditions=("week >= 4",), run_count=1, group='mine', priority=pr_map_res)

    # Event 1: Neutral.
    event('mine_hire_ev1', triggers='mine_hire_workers', run_count=1, group='mine_event', priority=pr_map_res)
    # Event2 : Choice, less iron but no cost.  Req: Mine produces at least 4 units of iron.
    # TODO check for mine production
    event('mine_hire_ev2', triggers='mine_hire_workers', run_count=1, group='mine_event', priority=pr_map_res)
    ##############
    # Event 1: Neutral.
    event('mine_deploy_ev1', triggers='mine_deploy_soldiers', run_count=1, group='mine_event', priority=pr_map_res)
    # Event 2: Choice. Req: mine must produce at least 4 iron.
    # TODO check for mine production
    event('mine_deploy_ev2', triggers='mine_deploy_soldiers', run_count=1, group='mine_event', priority=pr_map_res)
    ######## Universal Mine Events #########
    #These events may be chosen at random, regardless of what form of labour was chosen to work the mine.
    #Event 1: Extra gold
    event('mine_universal_ev1', triggers=('mine_deploy_soldiers', 'mine_hire_workers'), run_count=1, group='mine_event', priority=pr_map_res)
    #Event 2: Injury
    event('mine_universal_ev2', triggers=('mine_deploy_soldiers', 'mine_hire_workers'), run_count=1, group='mine_event', priority=pr_map_res)
    #Event 3: Lose MP
    event('mine_universal_ev3', triggers=('mine_deploy_soldiers', 'mine_hire_workers'), run_count=1, group='mine_event', priority=pr_map_res)
    #Event 4: Blessing, healing wounds
    event('mine_universal_ev4', triggers=('mine_deploy_soldiers', 'mine_hire_workers'), run_count=1, group='mine_event', priority=pr_map_res)


label mine_general:
# general event, allows to run subevents based on player choice
# for small mine, important mine, mining network
# Rosaria abandoned mine
# intro blurb
# mine background
$ temp1 = mines_defs[eventHex[6]][0]
$ temp2 = mines_defs[eventHex[6]][1]
$ temp3 = mines_defs[eventHex[6]][2]
# cost of needed workers
$ temp4 = temp2 * miner_cost
show black with fade
"Rowan has located an abandoned iron mine. With some workers, the mine can be brought back into operation to produce iron for the twins. The source can either be locals who're hired to work, or soldiers removed from the ranked and moved to manual labor instead."
"This [temp1] will likely provide [temp3] iron once restored."
# Options (each also lists how much you'll need to spend, the more iron from the mine the more you need to spend to get it):
menu:
    # Choice 1: Hire workers
    # costs some gold.
    "Hire workers ([temp4] gold)" if castle.treasury >= temp4:
        $ released_fix_rollback()
        $ change_treasury(-temp4)
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
        # Choose one of these at random, it may have an effect on the normal outcome for restoring a mine.  Universal events are also valid.
#~         call run_events('mine_hire_workers', 2) from _call_run_events_8
        $ choose_and_insert_next_event('mine_hire_workers')
    # Choice 2: Deploy Soldiers
    # costs some soldiers, but also some morale.
    # TODO count soldiers able working at mine (different barracks)
    "Deploy Soldiers ([temp2] soldiers)" if castle.buildings['barracks'].troops >= temp2:
        $ released_fix_rollback()
        $ castle.buildings['barracks'].troops -= temp2
        $ castle.morale -= temp2
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
#~         call run_events('mine_deploy_soldiers', 2) from _call_run_events_9
        $ choose_and_insert_next_event('mine_deploy_soldiers')
    #Choice 3: Leave
    #does nothing, but leaves the mine unexplored so that the player can come back later.
    "Leave":
        $ released_fix_rollback()
        $ prevent_tile_exploration()
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_hire_ev1:
# Event 1: Neutral.

"Around an hour after he'd made his report about the site, Jezera arrived in disguise with several locals. They quickly set to work, checking the equipment that had been abandoned at the mine and the overall condition of the place."
"Rowan approached his mistress, who was wearing an appearance very similar to when he'd first met her, curious as to how she was able to locate miners so quickly and on such short notice."

show rowan necklace neutral at midleft with dissolve
show jezera disguised neutral at midright with dissolve

ro "Where exactly did you find these people? Surely you hadn't made contact with them before now."

je "No, they aren't my agents. I found them in one of the hamlets nearby out of work and hoping to find something that could help them."

ro "I'm amazed you got them to come so quickly."

je "Oh I'm a very convincing person. Besides, they use to actually work at this mine before it was shut down. Many men lost their jobs when the war with father ended, soldiers, blacksmiths, armorers, and miners like these."
je "They aren't that much use if you hardly know war except when the forces of Chaos rise up."
je "With how bad farming has been in Rosaria, there are idle men and women everywhere. You just need to know where to look."

"Rowan nodded and turned his attention back to their new employees."
#no effect
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_hire_ev2:
# Event2 : Choice, less iron but no cost.  Req: Mine produces at least 4 units of iron.

"Once the workers arrived at the mine, they surprised their new employers with a special proposal. Apparently their home was in serious need of iron to repair buildings and make tools."
"So much so that they were willing to accept payment for working the mine in iron ore, at a rate far better than you could expect anywhere else for iron. Evidently these people weren't going to be able to pay for the iron normally."
menu:
    # Choice 1: Pay them in iron.
    "Pay them in iron":
        $ released_fix_rollback()
        "After deliberating, Rowan and Jezera decided that it would be better to save the money now rather than keeping the iron for later equipment."
        "They agreed to the proposal, and set reserved some of the ore for the people to take back home with them as an alternative payment."
        # Reduce iron production by 2, reduce regular iron production cost by 4 iron for this mine.
        $ castle.iron_per_week -= 2
        # refund treasury once
        $ change_treasury(2 * miner_cost)

    # Choice 2: Pay them normally.
    "Pay them normally":
        $ released_fix_rollback()
        "After deliberating, Rowan and Jezera agreed that the iron was far more valuable to them than the money they'd save by agreeing to the proposal."
        "Instead, they payed the miners the originally agreed upon price, reserving all of the iron to be sent to Castle Bloodmeen."
        #No effect.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_deploy_ev1:
# Event 1: Neutral.

"Andras arrived soon after Rowan gave his report, a small troop of former orc soldiers in tow. When they learned what they'd be doing from now on, they were not happy at all."
"Many of them loudly proclaimed that soldiers didn't do such low work. It was their job to make others do that work!"
"Soon enough, one of them was designated as a foreman to get the others to work. He was quite happy at this assignment by his master and started wiping the others to action."
"Fear of Andras did seem to have some effect on them. While none were happy to be here, it probably wouldn't be a good idea to rely on orcs for mining, they did the work just as well as any humans would have."
# no effect.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_deploy_ev2:
# Event 2: Choice. Req: mine must produce at least 4 iron.

"Upon arriving, the orcs were surprisingly excited at the prospect of working at an iron mine. After inquiring with the one that seemed to be the most senior of the bunch, Rowan discovered that she'd figured that they were going to be driving slaves."
"This bunch was fairly certain that they weren't going to be the ones to work the mines. In fact, they were already working on plans for how to capture people that they'd be able to force to work. Never mind that Andras has already relieved them of their gear."
"The red demon himself found the whole talk amusing. Before revealing the truth to his former soldiers, he called Rowan over to talk in private."

show rowan necklace neutral at midleft with dissolve
show andras smirk at midright with dissolve

an "Maybe there is some merit to their idea. This place is big enough that it might be worth having some slaves take care of it instead."

ro "You can't be serious? We'd paint a massive target on us if we're launching regular raids around the realm to run our mines!"

an "Oh not all of them, but one or two mines run by slaves, the lords won't recognize a pattern from that."

ro "I suppose...."

"His master did have a point, though such a method was extremely distasteful to Rowan."
menu:
    # Choice 1: Use slaves this time.
    "Use slaves this time":
        $ released_fix_rollback()
        ro "...it will make the orcs happier at least. They never like being forced to do labour."
        an "Hahaha, indeed. I'll tell our savage lady that her dreams have come true. You'd best carry on with your other duties, servant."
        # No morale loss, infamy and guilt gain.
        # TODO this "return" of morale is unsafe
        $ castle.morale += temp2
        $ avatar.base_infamy += 2
        $ avatar.base_guilt += 2

    # Choice 2: Use the orcs for labour, as planned.
    "Use the orcs for labour, as planned":
        $ released_fix_rollback()
        ro "...but the random villages being conquered and destroyed is probably enough antagonizing as is."
        an "True.  Ah well, it was a fun idea at any rate. Time to go crush this savage lady's dreams. You'd best carry on with your other duties, servant."
        # No effect.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_universal_ev1:
#Event 1: Extra gold

"This particular mine had obviously been abandoned in a hurry. So much so that a large piles of iron ore were just sitting around the mine's corridors in carts or spilled onto the ground."
"Compared to the price of restoring the mine, gathering all of this iron up to bring back to Bloodmeen would be trivial. The unexpected fortune lifted Rowan's spirits somewhat, as well as brought a smile to the lips of the twin waiting outside with their new miners."
#Either get some treasury immediately, or a massive one week bonus of iron.
if dice(2) == 1:
    $ change_treasury(30)
else:
    $ castle._iron += 15
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_universal_ev2:
#Event 2: Injury

"There had been several small cave-ins here in the mine. Rowan moved around to investigate, checking to make sure that everything was still stable and that it wouldn't be dangerous to their workers."
"While most of the place proved to be quite safe, one tunnel was not. With a rumble and a crash, said tunnel collapsed with the man still inside it! His master was able to free him from the tunnel after they arrived, but Rowan would be weak for weeks thanks to his inexperience underground."
#Rowan's strength is injured for 3 weeks.
$ add_effect(Injury('Weakness', 'strength', -2, 3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_universal_ev3:
#Event 3: Lose MP

"While waiting for the workers to arrive, Rowan set to scouting the interior.  He soon found that this mine had broken into a natural cave at some point and the miners had used it along with the passages that had been dug."
"Navigating these passages was far more difficult than the carved ones, it required paying very close attention to where one's feet went to be sure you didn't go crashing down into a crevice or trip on the uneven ground."
"After walking for a time, Rowan realized that he hadn't seen signs of mining for awhile now and the natural passages just went on and on. He attempted to retrace his steps, but only found new caverns he hadn't been to before. He was lost."
"Only after nearly two days of wandering did Rowan finally find his way back to main mines and then on to the surface."
"There was no hurry to repeat the experience."
#Lose movement points.
$ avatar.mp -= 2
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mine_universal_ev4:
#Event 4: Blessing, healing wounds

"Far down in the furthest depths of the mine, Rowan stumbled onto a rather peculiar sight. What seemed to be a shrine had been set up by the previous miners. On closer investigation, he found that a nexus of divine energy swirled down here."
"It was in the stones, in the ground. A spring of pure water that flowed down one of the walls at its heart nearby the shrine. This was once a place of safety, of solitude, and of community."
"The hero took a drink of the water and offered up a small prayer at the shine. He felt, renewed afterwards. With more energy and alertness. It was no wonder this place was important enough to the people who worked here for them to decorate and worship at it."
"Soon new worshipers would probably come and claim this place once again."
#Rowan heals all wounds.  If Rowan has no wounds, he gains a small boost to vitality for two weeks instead.
if av_has_injuries():
    $ heal_injuries()
else:
    $ add_effect(MultiEffect('Blessing', 'pos', (('vitality', 2),), 2))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label quarantined_mine:
#Quarantined Mine

#50% chance flooded w/ gas, 50% chance it's fine
$ temp = dice(2)
"The sight of an abandoned mine is an eerie one - rusted ironwork and rotting wood pointing accusingly at gaping, silent holes in the earth."
"This one, Rowan noticed, had long tapestries covered in scrawl trailing down either side of its entrances, bright red once but bleached pink by long exposure to the elements."
"The spidery, vertical script was unfamiliar - goblin, perhaps? Rowan wished he had Cla-Min handy."

#Decipher Script test DC12
#pass
if check_skill(12, 'decipher')[0]:
    "Still, Rowan himself was no novice to non-human language, and with charcoal and paper he was able to roughly decipher the faded tapestries' message."

    #if gas
    if temp == 1:
        "The red color was, as he suspected, a clue. The tapestries honored the lives of the goblin miners claimed by poison gas, and warn against anyone else attempting to use this mine."
        "After adding a fresh warning in Rosarian on a prominent rock, Rowan departed."
        # 10xp, small guilt loss, mine can't be used, therefore is explored but not claimed
        $ add_exp(10)
        $ change_base_stat('g', -2)
        #end event
        return
    else:
    #else:
        "They turned out to be exaltations offered to the obscure and crowded pantheon of goblin gods for the iron produced by this mine, and regrets that they were forced to move on by human predation."
        "One greenskin's loss is a demon's gain, and after a small amount of surveying Rowan reckoned there was still plenty of ore to be had within. He now had to decide how he intended to use this mine."
        #10 xp
        $ add_exp(10)
        #standard mine options
        jump .standard_options
else:
#fail
    "Rowan was no scholar of obscure languages, and had no idea what the faded tapestries had on them. He had to make a decision - play it safe and ignore the mine, or try and make use of this valuable resource?"

    #menu
    menu:
    #Choice: Ignore
        'Ignore':
            "Better not to risk lives and time upon a suspect hole in the ground, Rowan decided. He departed without letting anyone know what he'd found."
            #Mine explored but not claimed
            #end event
            return
        #Choice: Use
        'Use':
            #Display standard mine work options
            jump .standard_options
################################################################################
label .standard_options:
$ temp1 = mines_defs[eventHex[6]][0]
$ temp2 = mines_defs[eventHex[6]][1]
$ temp3 = mines_defs[eventHex[6]][2]
# cost of needed workers
$ temp4 = temp2 * miner_cost
# Options (each also lists how much you'll need to spend, the more iron from the mine the more you need to spend to get it):
menu:
    # Choice 1: Hire workers
    # costs some gold.
    "Hire workers ([temp4] gold)" if castle.treasury >= temp4:
        $ released_fix_rollback()
        $ temp5 = True
        $ temp6 = False
    # Choice 2: Deploy Soldiers
    # costs some soldiers, but also some morale.
    # TODO count soldiers able working at mine (different barracks)
    "Deploy Soldiers ([temp2] soldiers)" if castle.buildings['barracks'].troops >= temp2:
        $ released_fix_rollback()
        $ temp5 = True
        # if orcs were used
        $ temp6 = True
    #Choice 3: Leave
    #does nothing, but leaves the mine unexplored so that the player can come back later.
    "Leave":
        $ released_fix_rollback()
        $ prevent_tile_exploration()
        return
if temp == 2 and temp5:
#If not poisonous and mine staffed:
    "Rowan watched the work gather pace with trepidation that slowly melted into satisfaction."
    if temp6:
        "The orcs reported no problems, and it seemed as if his gut feeling had been right - it was just a plain old mine with nothing wrong with it. Perhaps, at last, his luck was turning."
    else:
        "The workers reported no problems, and it seemed as if his gut feeling had been right - it was just a plain old mine with nothing wrong with it. Perhaps, at last, his luck was turning."
    #mine claimed as normal
    if not temp6:
        $ change_treasury(-temp4)
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
    else:
        $ castle.buildings['barracks'].troops -= temp2
        $ castle.morale -= temp2
        $ castle.mines += 1
        $ castle.iron_per_week += temp3
    #end event
    return
if temp == 1 and temp5:
#If poisonous and mine staffed:
    "Rowan watched the work gather pace with trepidation. He was just beginning to relax and tell himself he was silly to worry when the ground rumbled beneath his feet, and cries of alarm and horror echoed out from the entrance to the mine."
    if temp6:
        "Orcs came scrambling out of it in a panic."
    else:
        "Men came scrambling out of it in a panic."
    "Rowan managed to get a handle on the situation and helped the workers carry out their prostrate, twitching comrades, but the damage had been done."
    "The lower reaches of the mine were contaminated with asphyxiating gas that reacted alarmingly to naked flame."
    if temp6:
        "10 orcs had perished as a result."
    else:
        "8 men had perished as a result, and the rest, tearing at their hair and howling curses at Rowan, carried away their dead comrades without further ado."
    "Next time, Rowan told himself angrily as he surveyed the scene of the disaster, he would invest in some canaries."
    #If orcs were used morale down. If humans used guilt and infamy up. Gold/mil strength used lost obviously
    if temp6:
        $ change_morale(-6)
        $ castle.buildings['barracks'].troops -= 10
    else:
        $ change_treasury(-20)
    #mine is explored but unclaimed
    #end event
    return
return
