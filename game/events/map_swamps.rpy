# random map events that happen on swamps
init python:

    # Something glints in the bog
    event('something_glints_in_the_bog', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Lost in the Marsh
    event('lost_in_marsh', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Swamp fever (malediction)
    #No requirements
    event('swamp_fever', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Orc stragglers (benediction)
    #Orc barracks has at least 5 spaces open.
    event('orc_stragglers', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',
        "castle.buildings['barracks'].capacity - castle.buildings['barracks'].troops >= 5"), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Will o' the Wisp
    event('will_o_the_wisp', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Mysterious Shrine
    event('mysterious_shrine', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label something_glints_in_the_bog:
# Something glints in the bog
scene bg32 with fade

"While travelling through the unpleasant and dreary bog, something caught the sun's rays and momentarily shawn in Rowan's eyes."
"He was unable to determine exactly what the object was, only that it was on the other side of a particularly treacherous part of the swamp."
"Still, it wasn't something that belonged here and may be worth attempting to retrieve."

#choice
menu:
    "Leave it be.":
        $ renpy.fix_rollback()
        "With the risk of sinking, Rowan decided it was better to be safe than sorry, leaving whatever it might be behind to continue on his way."
        #end event
        return
    "Try to reach the object.":
        $ renpy.fix_rollback()
        "The hero started his trek over the muck, still water, floating islands, and endless biting insects."
        "No matter how well he'd prepared, you always got something somewhere you didn't want it when going over such poor terrain as this."
        #roll a survival check against a DC 8 (natural one always fails)
        $ temp_res = check_skill(8, 'survival')
        #if success roll another d20 and add luck mod, otherwise go to fail further down
        $ temp_res2 = dice(20) + avatar.stat_mod('luck')
        if temp_res[0]:
            "Finally, after what felt like an eternity of trudging and stomping and the misery of being harassed by the local fauna, the trek was over."
            "Rowan would still have to make the return trip, but now he knew a safe path and things would at least go faster."
            #if luck check was less than 5
            if temp_res2 < 5:
                "Unfortunately, all he found after making this trip was the fragments of a broken mirror. There were other things as well, but only rusted junk and debris."
                "Coming all this way had been a waste of time."
                #gain 10 xp
                $ add_exp(10)
                #end event
                return
            #if luck check was 6-10
            elif temp_res2 <= 10:
                "What had been reflecting the sun's rays turned out to have been a few coins that a poor soul was carrying when they fell victim to the swamp."
                "Most of them were highly corroded and worthless as currency now, though a few made it so that the trip hadn't been a complete waste of time."
                #gain 10 xp
                $ add_exp(10)
                #gain 10 gold
                $ change_personal_gold(10)
                #end event
                return
            #if luck check was 11-15
            elif temp_res2 <= 15:
                "The metal latch of a chest proved to be the source of the strange glint that Rowan had seen before."
                "Once again, the treasure contained in these strange boxes would be granted to a hero."
                #gain a random piece of low level equipment
                $ get_rnd_item(0, 150)
                #gain 10 xp
                $ add_exp(10)
                #end event
                return
            #if luck check was 16+
            else:
                "What a find! Evidently some bandit, thief, or other foul individual had been using this isolated location as a place to store their ill-gotten goods."
                "Dust and grim indicated that it had been some time since they'd been stashed, so it was unlikely that the former proprietor would be returning."
                #gain 2 random pieces of low level equipment
                $ get_rnd_item(0, 150)
                $ get_rnd_item(0, 150)
                #gain 50 gold
                #gain 10 xp
                $ change_personal_gold(50)
                $ add_exp(10)
                #end event
                return
        else:
            #if fail, roll another d20 and add luck mod
            #if luck check was less than 5
            if temp_res2 < 5:
                "Oh no, while trudging and carefully picking his way through the swamp, Rowan came under attack from a stirge!"
                "The giant mosquito-like creature found the man half stuck in mud to be easy prey and forced Rowan to abandon his attempts to recover whatever it was that had been reflecting the sun's rays."
                "Only after returning to solid ground was the creature defeated. By that time, Rowan had lost a significant amount of blood and felt weak."
                "It would be some time before he'd fully recovered from the attack."
                #lose 2-3 movement points
                $ avatar.mp -= random.choice((2, 3))
                #lose 1d6 +1 strength and 1d6+1 constitution until the end of the week
                $ add_effect(Injury('Blood loss', 'strength', -dice(6)-1))
                $ add_effect(Injury('Blood loss', 'vitality', -dice(6)-1))
                #gain 5 xp
                $ add_exp(5)
                #end event
                return
            #if luck check was 6-11
            if temp_res2 <= 11:
                "In spite of his efforts to pick his way as carefully as possible, Rowan was unable to avoid getting himself stuck in the muck."
                "It took him hours to free himself, by which point the sun had set and he had no way of finding the source of the light. All he'd done was delay himself."
                #lose 2-3 movement points
                $ avatar.mp -= random.choice((2, 3))
                #gain 5 xp
                $ add_exp(5)
                #end event
                return
            #if luck check was 12+
            else:
                "Soon Rowan realized that at some point he'd gotten turned around or something. He couldn't work out where the glint had been coming from anymore and by now he was almost certainly lost."
                "This excursion would have to end, empty handed."
                #gain 5 xp
                $ add_exp(5)
                #end event
                return

###################################################################################################
###################################################################################################
###################################################################################################


label lost_in_marsh:
    # Lost in the Marsh
    scene bg32 with fade
    $ released_fix_rollback()
    $ lost_in_marshes_right_dir = renpy.random.choice(('north', 'east', 'south', 'west'))
    $ add_exp(10)
    'Rowan had gotten himself lost and he knew it.'
    'He had though he would be through the swamp by now, but it seemed to stretch on forever in every direction around him.'
    'To make things worse, his decision to stick to dry land and avoided the bog as much as possible, had lead to him getting turned around. He could no longer be sure he wasn\'t heading back the way that he came.'
    'His only option was to pick a direction and stick with it, hoping that it would lead him back to solid land sooner rather than later.'
    menu:
        'North':
            $ released_fix_rollback()
            call .lost_in_marsh_find_way('north') from _call_lost_in_marsh_find_way
        'East':
            $ released_fix_rollback()
            call .lost_in_marsh_find_way('east') from _call_lost_in_marsh_find_way_1
        'South':
            $ released_fix_rollback()
            call .lost_in_marsh_find_way('south') from _call_lost_in_marsh_find_way_2
        'West':
            $ released_fix_rollback()
            call .lost_in_marsh_find_way('west') from _call_lost_in_marsh_find_way_3
            # end event
    return


label .lost_in_marsh_find_way(direction):
    if direction == lost_in_marshes_right_dir:
        'The Sisters must have been watching over Rowan, as by some small stroke of luck after only thirty minutes of walking through the swamp, he found it beginning to give way to much sturdier ground.'
        'Before long he was once again on his way, none the worse for the experience.'
        # no effect
    else:
        'Rowan spent the rest of the day and night trudging through the swamp to no avail, clearly just as lost as he has been before he made a decision.'
        'By the time the sun began to rise, he had finally reached the marshes\' terminus, the landscape opening up to swathes of verdant farmland before him.'
        'He was glad to once again be on his way, but there was no denying the ordeal had cost him valuable time.'
        # lose mp
        $ avatar.mp -= 1
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label swamp_fever:
#Swamp fever (malediction)
#No requirements
scene bg32 with fade
$ released_block_rollback()
"Swamplands are famous for the unusual forms of flora and fauna that call them home. This also includes the myriad of microorganisms that often live nowhere else."
"Unfortunately, many of those tiny living things can cause major problems when they get into people's bodies. Such as a tiny worm that causes a sickness called 'Swamp fever' if it manages to get inside you."
"A small fall at the wrong place and the wrong time gave one of those little worms the chance it needed, and it burrowed into Rowan's flesh. Its wastes flowed into the hero's bloodstream, making him very ill."
#End scene. 5xp. Rowan is injured.
$ add_exp(5)
$ add_effect(Injury('Swamp fever', 'strength', -2))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label orc_stragglers:
#Orc stragglers (benediction)
#Orc barracks has at least 5 spaces open.
scene bg32 with fade
$ released_block_rollback()
"While Rowan scouted the swamplands, he stumbled upon a small camp of orcs. They had the look of refugees or stragglers who had been driven into hiding here. A bunch as underfed and desperate as these would be easy recruits."
"The man sent a message to his red skinned master, who soon made his way to the swampland and proudly strode into the middle of the camp. The presence of a demon, albeit a half blooded one, left the orcs stunned and they fell on their knees in an instant."
"Andras was impressed by their obedience and desire to appease him, enough to look past their sorry state and offer them a place in his armies. They all agreed without hesitation, even abandoning their shoddy tents to following him back to the nearest portal grounds."
#End scene. 10xp. Gain five new orc soldiers.
$ add_exp(10)
$ castle.buildings['barracks'].troops += 5
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label will_o_the_wisp:
# Will o' the Wisp
scene bg32 with fade
$ released_block_rollback()
"Theories abound as to what will o' wisps are. Vindictive spirits; fairies; mirages; bubbles of magic trapped in heavy atmosphere, perhaps."
"The only thing that was agreed upon, Rowan thought as he watched this one hovering in the mist over the sullen marsh landscape a short distance away, was that to follow them was guaranteed catastrophe... or fortune."
#50% chance it's fucking with you, 50% chance treasure
$ event_tmp['bad_wisp'] = (dice(2) == 1)
#menu
menu:
    #Choice 1: Follow it
    'Follow it':
        "As warily as possible, Rowan left the path and went in the direction of the pale light. It slowly moved away, stopping whenever Rowan stopped."
        "It seemed as if with each step he took into the sucking mud though, he got a little bit closer to the hovering wisp... just a little bit closer..."

        #if bad wisp
        if event_tmp['bad_wisp']:
            #spot check dc 12
            #pass
            if check_skill(12, 'spot')[0]:
                "Rowan froze. He'd managed to tear his eyes off the wisp for a moment, and the peat in front of him had caught his attention - a suspiciously flat and undisturbed expanse."
                "He tossed a stone at it, and watched it disappear with a gloop. He snorted disgustedly as the will o' wisp winked out of existence, and carefully retraced his steps back to the path, glad at least to have avoided the pitfall."
                #gain 10 xp
                $ add_exp(10)
                #end event
                return
            #fail
            else:
                "Rowan came back to his senses as, with a horrible, cold lurch, he stepped forward and suddenly found himself up to his thigh in depthless black muck."
                "He could not help falling arms first into the sinkhole, from where it seemed to take an age to grab more solid ground and haul himself clear."
                "He was soaked from head to tail in clammy, black mud, a truly horrible sensation that was going to get worse before it got better. And what if he met someone he needed to bargain with in this state?"
                "The will o' wisp, naturally, had disappeared. Disgusted with himself for falling for it (and in more general, physical terms), Rowan trudged back to the path."
                #Diplomacy ability set to 0 until end of week, -2 move points
                # TODO - this reduces only base dimplomacy, other effects can still raise it above zero
                $ add_effect(MultiEffect('Dirty', 'neg', (('diplomacy', -avatar.skills['diplomacy']),)))
                $ change_mp(-2)
                #gain 5 xp
                $ add_exp(5)
                #end event
                return
        #if good wisp
        else:
            "Abruptly, the wisp disappeared. Rowan blinked a few times, dazed. Had its intention been to simply lead him astray?"
            "Possibly. But here, in a waterlogged hollow invisible from the path, was something of interest, a few grimy sacks and chests piled behind a rock. A robber's stash, perhaps?"
            "A less well-off robber, once Rowan had rifled through the containers and helped himself to some silver necklaces, a bulging purse of mixed currency and a fine looking piece of armor."
            "He saluted where the wisp had been, and trudged back towards the path."
            #Treasury up, + random item
            $ change_treasury(20)
            $ get_rnd_item(0, 300)
            #gain 5 xp
            $ add_exp(5)
            #end event
            return
    #Choice 2: Don't
    "Don't":
        "Rowan had enough on his plate than to follow the whims of a mischievous firefly. He pointedly ignored the wisp and continued down the faint path."
        #end event
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label mysterious_shrine:
#Mysterious Shrine
scene bg32 with fade
$ released_block_rollback()
"Whilst slowly picking his way through the treacherous bog, Rowan came upon a singular sight. In amongst the low-lying thickets a larger tree rose tall, all of its wide-set branches hung with faded ribbons, fetishes, bird skulls and charms."
"It tinkled and sighed eerily in the gentle breeze. Evidently this was a place of worship for the local people - but what God or power was honored here, Rowan could not tell."

#if Rowan has high guilt
if avatar.guilt >= 30:
    "Whatever it was, Rowan felt a deep sense of unworthiness taking in the simple peasant charms. Could he really beg any deity for blessing, with all that weighed upon his conscience? Absolutely not."
    "Unable to stomach being reminded of the blackness of his recent deeds, he swiftly left the tree behind him."
    #end event
    return
#else
else:
    #menu
    menu:
        #Choice 1: Solicit a blessing
        "Solicit a blessing":
            $ released_fix_rollback()
            "It was the work of a moment to tear a strip off his shirt and fashion a ribbon around one of the boughs of the tree. Rowan knelt in the mud and offered a general prayer of goodwill, requesting assistance in his quest."

            #Choose from the following at random
            $ event_tmp['outcome'] = dice(3)
            #Outcome #1
            if event_tmp['outcome'] == 1:
                $ released_fix_rollback()
                "The only answer was the sigh and tinkle of the wind in the branches. Not really sure what else he was expecting from a pagan shrine, Rowan picked himself up and carried on his way."
                "As the day progressed though, he felt a certain calmness and clarity of purpose, and ultimately felt better for taking the time to pray and empty his mind."
                #Corruption and Guilt both down a bit
                $ change_base_stat('c', -2)
                $ change_base_stat('g', -2)
                #5 xp
                $ add_exp(5)
                #end event
                return
            #Outcome #2
            elif event_tmp['outcome'] == 2:
                $ released_fix_rollback()
                "The wind sighed and tinkled in the branches, and Rowan felt a breath of health enter him, a spring-like freshness which spread out to his fingertips and cast a cool light over his mind."
                "He bowed his head in thanks to the shrine, picked himself up and carried on his way, calmed and refreshed."
                #Corruption down, +1 Wound healed
                $ change_base_stat('c', -2)
                # heal 1 wound
                $ heal_wounds(1)
                #5 xp
                $ add_exp(5)
                #end event
                return
            #Outcome #3
            else:
                $ released_fix_rollback()
                "The wind sighed and tinkled in the branches, and Rowan felt a surge of raw energy enter him, the strength of it making him double over."
                "It felt maddening and feral, a bolt of lightning from some primal, inhuman source that made him bare his teeth and standing the hair on his arms on end."
                "He staggered away from the shrine, heart pumping and skin shivering with energy, his thoughts and the world around him reddened with bestial, lusty thoughts."
                #Corruption up, +5 move points
                $ change_base_stat('c', 2)
                $ change_mp(5)
                #5 xp
                $ add_exp(5)
                #end event
                return
        #Choice 2: Leave
        'Leave':
            $ released_fix_rollback()
            "Best not to attempt pestering an unknown deity, Rowan felt. He carried on his way."
            #end event
            return
