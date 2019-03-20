# random map events that happen on plains
init python:

    #Brigand Slavers
    #Requires: After first warning of famine sweeping area, after Castle Raeve assault at least
    # TODO: probably switch dependence to rumor of famine
    event('brigand_slavers', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, depends=('famine_looms', 'raeve_keep_visit_goal2'),
        group='map_expl', priority=pr_map_rnd)
    #Tower Ruin
    event('tower_ruin', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label brigand_slavers:
#Brigand Slavers
#Requires: After first warning of famine sweeping area, after Castle Raeve assault at least
scene bg31 with fade

"Rowan heard the group long before they came into view."
"Many feet, marching out of time; Rough laughter and swearing asides; the rattle and clink of chains. Half a dozen men, armed with knives, swords and crossbows, marching twenty souls in rags, bound together at the wrists."
"When he saw Rowan on the road ahead, the leader called a halt with a sharp jerk of his hand."

if avatar.infamy < 10:
#infamy low to medium
    brig "'ere, I know you. The big peasant hero from the last war, ain't it? Reagan, or summat. I've worked with lads who marched under you, once upon a time."
    "He gave the train behind him a lazy eye. A couple of the other brigands looked away, bitterness on their lean, dirty faces."
    brig "Well, hero lad, we ain't got no quarrel with you. These are different times, when ordinary jacks got to do some hard things in order to stay alive."
    brig "Reckon a real man of the people would see that, and go about his business, and let us go about ours. That sound about right?"
    "The other bandits watched Rowan carefully, hands close to their weapons. The slaves at the head of the train looked at Rowan, hollow-eyed and helpless."
    jump .brigmenu
#else
else:
    brig "'Ere, I know you. The big peasant hero from the last war, ain't it? Reagan, or summat. Sounds as if you've been changing your stripes, though. Sad state of this world, eh?"
    ro "What are you doing?"
    brig "Getting by. Ordinary jacks got to set their hands to some hard things to do that, these days. But I reckon a pragmatic gentleman such as yourself can appreciate that. Perhaps you'd be interested in buying some of our stock?"
    brig "They'll be cheap - can't afford to feed 'em all, that being the truth. Gonna have to get rid of some, ‘tween here and the pits."
    "The other bandits watched Rowan carefully, hands close to their weapons. The slaves at the head of the train looked at Rowan helplessly."
    jump .brigmenu

label .brigmenu:

menu:

    "Let them go.":
        $ released_fix_rollback()
        ro "I have no interest in any of this. Get out of my sight."
        "The brigand leader smirked, and his compatriots relaxed."
        brig "I'm glad you've got some sense about you, at least. A pleasant day, Sir Robert, or whatever it was."
        "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
        #gain a small amount of infamy
        $ change_base_stat('f', 1)

    #low corruption only
    "Demand they release the slaves." if avatar.corruption < 10:
        $ released_fix_rollback()
        ro "You will release those people this instant, or I'll kill you where you stand, blaggard."
        brig "Shame. I was led to believe you were smart."
        "One of the other men suddenly raised his crossbow and fired."

        #dodge check DC12
        $ event_tmp['dodge check'] = check_skill(12, 'dodge')
        if not event_tmp['dodge check'][0]:
        #fail
            "Rowan jerked to one side, but could not stop the bolt thudding with numbing force into his armor."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan acrobatically flung himself to one side, and the bolt whistled past his shoulder. Then the brigand leader was upon him, foul-smelling and fierce, trying to bear hug him into the point of his dirk."

        $ event_tmp['strength check'] = check_stat(10, 'strength')
        #strength check DC10
        if not event_tmp['strength check'][0]:
        #fail
            "Rowan struggled hard and managed to pull away enough to stop the blade piercing his innards, but still received a vicious slice across his ribs."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan struggled like a wolverine, landing an uppercut on the man's unshaven chin and making him swing the vicious blade into empty air."

        if not event_tmp['strength check'][0] and not event_tmp['dodge check'][0]:
        #Failed both checks
            "Doubled up in shock from his wounds, Rowan could not stop the brute punching him in the gut and sending him sprawling into the roadside ditch."
            "Jeering laughter and cheers from the other bandits, interspersed with aghast groans from the slaves, accompanied his fall."
            brig "This world ain't got a place for your type anymore, hero lad. Learn that, or die."
            "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
            return
        else:
        #passed one check    # or two
            "Rowan pulled away long enough to pull out his own blade, and swung it hard and true across his assailant's unguarded throat. With a wet choke, he collapsed into the dirt."
            ro "Run, or face me, cowards."
            "The other brigands' eyes flicked between the body of their leader and Rowan, then first one then the rest turned and fled. Rowan searched the corpse's pockets, and duly found a key that fitted the shackles of the slaves."
            slave "I - I don't know what we'll do, truth be told, master. We were fleeing south from the famine when they jumped us. They took what little we had. But... anything is better than being at the mercy of men like that."
            slave "We'll think of something. Thank you so much, Sir Rowan - for as long as I live, I will tell anyone that cares to listen that you are the last truly honourable man in Rosaria."
            "Rowan watched them depart, aglow with chivalric pride."
            #gain 25 xp, lose some infamy and guilt
            $ add_exp(25)
            $ change_base_stat('f', -1)
            $ change_base_stat('g', -1)
            return

    "Buy Slaves.":
        $ released_fix_rollback()

        ro "They're offering these prisoners for cheaper than what I could probably ransom them for. And even being at the whim of Andras and Jezera is better than being marched to their deaths by this lot..."
        ro "Alright. I'll take some."
        brig "How many?"

        menu:
            "Can't afford any.":
                $ released_fix_rollback()
                ro "On second thoughts..."
                brig "Humph. Just as well we didn't try to rob you. What a waste of time."
                "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
                #small infamy boost
                $ change_base_stat('f', 1)
                return

            #allow extra choices to buy [5], [10], [15], or [20] slaves with the following outcome
            # TODO: check for free space for prisoners?
            'Buy 5' if castle.treasury >= 5 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 5
            'Buy 10' if castle.treasury >= 10 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 10
            'Buy 15' if castle.treasury >= 15 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 15
            'Buy 20' if castle.treasury >= 20 * 5:
                $ released_fix_rollback()
                $ event_tmp['buy slaves'] = 20
        $ released_fix_rollback()
        "Keeping a watchful eye on the other brigands, Rowan handed the gold over."
        #if not 20
        if event_tmp['buy slaves'] < 20:
            "The leader produced a key, and snapped clear the number of ragged souls Rowan had just purchased."
        #else
        else:
            "The brigands shoved forward the full score of ragged souls Rowan had just purchased."
        slave "You- you have no right to do this! We are just ordinary men, like you-"
        brig "Quit yer yapping, dog! A pleasure doing business with you, Sir Redmond. I only hope we get to do so again."
        "With the crystal, it only took Rowan a few minutes to call in a squad of orcs, who roughly led the ragged chattel away."
        "Watching them go, Rowan could almost convince himself he'd more or less rescued these people from being either marched to death, or sold to even worse masters. Almost."
        #minus gold (5 gold per prisoner) and gain prisoners equal to the number of slaves purchased, medium guilt and infamy gains
        $ change_treasury(-5 * event_tmp['buy slaves'])
        $ change_prisoners(event_tmp['buy slaves'])
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 3)
        return

    #High corruption only
    "Kill Them, Take the Slaves For Yourself." if avatar.corruption >= 10:
        $ released_fix_rollback()
        ro "Filth like you don't deserve slaves. I believe I'll kill you, and take them as my own."
        brig "You will, will you?"
        "One of the other men suddenly raised his crossbow and fired."

        #dodge check DC12
        $ event_tmp['dodge check'] = check_skill(12, 'dodge')
        if not event_tmp['dodge check'][0]:
        #fail
            "Rowan jerked to one side, but could not stop the bolt thudding with numbing force into his armor."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan acrobatically flung himself to one side, and the bolt whistled past his shoulder. Then the brigand leader was upon him, foul-smelling and fierce, trying to bear hug him into the point of his dirk."

        $ event_tmp['strength check'] = check_stat(10, 'strength')
        #strength check DC10
        if not event_tmp['strength check'][0]:
        #fail
            "Rowan struggled hard and managed to pull away enough to stop the blade piercing his innards, but still received a vicious slice across his ribs."
            #gain one wound
            $ take_damage(1)
        else:
        #pass
            "Rowan struggled like a wolverine, landing an uppercut on the man's unshaven chin and making him swing the vicious blade into empty air."

        if not event_tmp['strength check'][0] and not event_tmp['dodge check'][0]:
        #failed both checks
            "Doubled up in shock from his wounds, Rowan could not stop the brute punching him in the gut and sending him sprawling into the roadside ditch. Jeering laughter and cheers from the other bandits accompanied his fall."
            brig "Those were some big words for an absolute streak of piss. Keep them to yourself next time."
            "He jerked his hand brusquely, and the other brigands shoved the slave train back into motion. The sound of chains and shuffling of feet took a while to fade entirely out of range of Rowan's ears."
            return
        else:
        #succeeded one or more
            "Rowan pulled away long enough to pull out his own blade, and swung it hard and true across his assailant's unguarded throat. With a wet choke, he collapsed into the dirt."
            "Rowan advanced upon the other brigands, face alive and terrible with blood lust. Before he'd even reached the first, though, they had fled, unnerved and aghast at this living embodiment of chaos they'd been unfortunate to happen upon."
            "The slaves drew back from him and the corpse twitching in the dirt, ashen terror chalked on their gaunt faces."
            ro "Do exactly as I say and you won't share the fate of that fool."
            "With the crystal, it only took Rowan a few minutes to call in a squad of orcs, who roughly led the ragged chattel away. Rowan watched them go, thoroughly satisfied with his catch and the manner in which it was gained."
            #gain 20 prisoners, gain 25 xp, gain a large amount of infamy
            $ change_prisoners(20)
            $ add_exp(25)
            $ change_base_stat('f', 5)
            return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tower_ruin:
#Tower Ruin
#No requirements
scene bg31 with fade

"Stood on top of a nearby hill was the ruin of an old watchtower - a solitary finger of stone crumbling off into nothing thirty feet off the ground, a remnant from a different age of man."
"It would be the den of ne'er-do-wells, or haunted, Rowan guessed. In the lowlands, unguarded finished stone was rarely left for long before it was appropriated by peasantry. He had to consider whether it was worth the risk and time to explore the ruin."

menu:
    "Search.":
        $ released_fix_rollback()
        "Rowan made his way up the rubble-strewn hill and entered the tower through a gap in the wall. There was bad taste to the air inside, a feeling of malignity and despair seemingly baked into the stone itself, confirming his suspicion that the place was haunted."
        #stealth check DC12
        if not check_skill(12, 'move_silently')[0]:
        #fail
            "Rowan tried to remain as quiet as possible as he picked his way through the stone and rotting furniture inside, searching for anything that might be valuable, but the black atmosphere compressed around him until it felt like he was suffocating, body and mind."
            "It was like drowning at the bottom of a deep, deep well. Down which {i}things{/i} were whispering terrible things..."
            "Rowan's nerve failed, and he stumbled desperately back to the gap in the wall and collapsed out of it, heaving down great lungfuls of air once he was back outside."
            "He recovered his breath after a few moments - but the feeling of being tainted, black words and thoughts insinuated into his mind, remained."
            #lose 1 move point, gain a small amount of corruption
            $ change_mp(-1)
            $ change_base_stat('c', 1)
            return
        else:
        #pass
            "Rowan kept as quiet as possible as he picked his way through the stone and rotting furniture inside, searching for anything that might be valuable.The ominous oppressiveness of the tower remained, but Rowan kept his thoughts as innocuous and quiet as his footstep, and this way it seemed he avoided disturbing the unsleeping shades that lurked within it."
            "The ominous oppressiveness of the tower remained, but Rowan kept his thoughts as innocuous and quiet as his footstep, and this way it seemed he avoided disturbing the unsleeping shades that lurked within it."
            #lose one move point
            $ change_mp(-1)

        #loot rolls
        $ event_tmp['loot rolls'] = dice(4)
        $ released_fix_rollback()

        if event_tmp['loot rolls'] == 1:
        #1/4 chance - nothing
            "Unfortunately, there was nothing of interest in the tower. The ghosts here guarded nothing but bitter memories of their own demise, it seemed. Disappointed, Rowan crept carefully back out of the ruin and continued on his way."
            #gain 20 xp
            $ add_exp(20)
            return
        elif event_tmp['loot rolls'] == 2:
        #1/4 chance - random piece of armour
            "Halfway up the stairway that wound around the inside of the tower Rowan found skeletal remains, an arrow running through its leering skull."
            "Clutched in its hands was a piece of armor - something the warrior had failed to pull on in time, perhaps. Guarded from the elements, it still looked in good condition."
            "Rowan carefully retrieved it from the bony, moldering hands of its former owner and then retraced his steps, glad to make his way back down the hill with his prize and leave the ruin far behind."
            #gain one random piece of armour, gain 20 xp
            $ add_exp(20)
            $ get_rnd_item(0, 500, 'armour')
            return
        elif event_tmp['loot rolls'] == 3:
        #1/4 chance - money
            "In the tower's lower level, Rowan found a storage area, which looked like it had already been ransacked - and within which a large number of people had met unpleasant ends, going off the number of skeletons he had to toe his way around."
            "In a small depression by the far wall, he found a small chest filled with thick coins. Ancient denomination, but gleaming softly with gold."
            "The chest wasn't hidden. Why hadn't it been taken? Cursed? Nothing bad seemed to happen when Rowan gingerly fingered the coins, then transferred them to his own pouch, then retraced his steps back out of the tower."
            "Happy with his prize and even happier to leave the haunted ruin behind him, he headed back down the hill and continued on his way."
            #gain one hundred gold for the treasury, gain 20 xp
            $ change_treasury(100)
            $ add_exp(20)
            return
        else:
            #1/4 chance military information
            "There was nothing of material value in the tower, all of it lost to whatever catastrophe had befallen the place when it had known living occupants. However - in the main chamber, Rowan found a large map nailed to the wall, crumbling but still well preserved."
            "It showed mountains, rivers, fortresses and arsenals, troop movements, terrain bottlenecks, where stores would be kept in times of war."
            "It was clearly outdated, but from his own knowledge Rowan could discern that it was a map of Rosaria, its main settlements and granaries unchanged."
            "He thought this information may well allow him to guess how and where the Baron's forces were likely to line up, maybe even get the jump on them should it come to a straight fight."
            "He carefully copied the map's details down, then retraced his steps out of the tower, happy to leave the cursed place behind."
            #todo - Rosaria loses military points
            #gain 20 xp
            $ add_exp(20)
            return

    "Leave it alone.":
        $ released_fix_rollback()
        "Let sleeping towers lie, Rowan decided. He continued on his way, quickly leaving the ruin behind."
        return

