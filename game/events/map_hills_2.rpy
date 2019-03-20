# random map events that happen on hills
init python:

    #Iron Seam
    event('iron_seam', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Landslide
    event('landslide', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label iron_seam:
#Iron Seam
#No requirements

"A distant cliff-side catching the sunlight drew Rowan's eye as he traversed the mountainous territory. He picked his way along a valley to take a closer look."
"There was definitely something up there, on that wild, sheer cliff face - a wide stripe of grey, gently glittering rock. Iron? There were surely untapped seams to be found in this difficult and distant terrain."
"Taking a closer look, however, was going to be neither easy nor safe. Rowan pondered if it was worth the effort."

menu:
    "Climb the cliff.":
        $ released_fix_rollback()
        #climb check dc12
        $ event_tmp['climb_roll'] = roll_skill('climb')[0]

        if event_tmp['climb_roll'] < 8:
        #less than 8
            "Rowan put his equipment to one side and set his hands upon the rock, gaze set upon the tantalising glitter above. He had clambered about fifteen feet up the sheer cliff face before a toehold gave way beneath his boot."
            "He half fell, half slid back down, landing heavily upon his ribs with a horrible crack. He clambered back to his feet, cursing."
            "There was no chance of a second attempt with injury clutching his side - whatever the seam was, a traveller more skilled at climbing than he would have to find out."
            #gain 10 xp and 1 wound
            $ add_exp(10)
            $ take_damage(1)
            return
        elif event_tmp['climb_roll'] < 12:
        #8-11
            "Rowan put his equipment to one side and set his hands upon the rock, gaze set upon the tantalising glitter above."
            "The climb was tough, the rock jagged, and his heart almost leapt out of his mouth when he suddenly lost his grip and fell a few feet, jarring his ankle and bloodying his nose against the stone."
            "After he’d spent a few moments taking some long, deep breaths though, he was able to continue."
            #gain 1 wound and continue to reward step
            $ take_damage(1)
        else:
        #pass
            "Rowan put his equipment to one side and set his hands upon the rock, gaze set upon the tantalising glitter above. Using all of his experience, he scaled the sheer cliff face like a lizard up a sun-bleached wall."
            "The gradient became less severe further up, and he was able to stand upon a lip of rock next to the large stripe of discoloured rock, examining it closely."

        #reward step
        $ tmp = dice(5)
        if tmp <= 2:
            $ event_tmp['reward'] = 'Big'
        elif tmp <= 4:
            $ event_tmp['reward'] = 'Average'
        else:
            $ event_tmp['reward'] = 'No reward'

        if event_tmp['reward'] == 'Big':
        #40% chance - Big score
            "His spirits rose as he set a knife to it and heard the telltale 'clink'. Iron! And a concentrated amount of it, by the looks of things; this whole mountainside could well be thick with good quality ore."
            "The only problem was getting at it. He could call in a team to construct some platforms, ramps and pulleys, but it would take time."

            menu:
                "Use orcs.":
                    $ released_fix_rollback()
                    "Rowan summoned a surly pack of orcs and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 5 morale, gain 20 xp and a medium sized mine
                    $ change_mp(-2)
                    $ change_morale(-5)
                    $ add_exp(20)
                    # add iron/week as for "important mine" #7
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[7][2]
                    return

                "Use humans.":
                    $ released_fix_rollback()
                    "Rowan followed the valley back down, found a village with men willing to be hired and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 30 treasury, gain 20 xp and a medium sized mine
                    $ change_mp(-2)
                    $ change_treasury(-30)
                    $ add_exp(20)
                    # add iron/week as for "important mine" #7
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[7][2]
                    return

                "Decide against it.":
                    $ released_fix_rollback()
                    "There'd be iron mines in terrain far easier to access, Rowan decided, and he had no wish to spend an arduous amount of time and effort setting one up here. Reluctantly he climbed back down the cliff, retrieved his possessions and set off again."
                    #gain 20xp
                    $ add_exp(20)
                    return
        elif event_tmp['reward'] == 'Average':
        #40 chance - Average Score
            "His spirits rose as he set a knife to it and heard the telltale 'clink'. Iron! There wasn't quite as much of it as he had hoped, but there still seemed to be a decent amount here, surely enough to justify establishing a mine."
            "The only problem would be getting at it. He could call in a team to construct some platforms, ramps and pulleys, but it would take time."

            menu:
                "Use orcs.":
                    $ released_fix_rollback()
                    "Rowan summoned a surly pack of orcs and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 5 morale, gain 20 xp and a small sized mine
                    $ change_mp(-2)
                    $ change_morale(-5)
                    $ add_exp(20)
                    # add iron/week as for "small mine" #6
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[6][2]
                    return

                "Use humans.":
                    $ released_fix_rollback()
                    "Rowan followed the valley back down, found a village with men willing to be hired and set them to work constructing some wooden scaffolding and rope lifts that would enable them to get at the rich iron seam and bring the ore back down."
                    "It took a tedious amount of time, but eventually the workers had a decent, makeshift system set up and picks were being set to the face. Weary but satisfied, Rowan set out again."
                    #lose 2 move points and 30 treasury, gain 20 xp and a small sized mine
                    $ change_mp(-2)
                    $ change_treasury(-30)
                    $ add_exp(20)
                    # add iron/week as for "small mine" #6
                    $ castle.mines += 1
                    $ castle.iron_per_week += mines_defs[6][2]
                    return

                "Decide against it.":
                    $ released_fix_rollback()
                    "There'd be better iron mines in terrain far easier to access, Rowan decided, and he had no wish to spend an arduous amount of time and effort setting one up here. Reluctantly he climbed back down the cliff, retrieved his possessions and set off again."
                    #gain 20xp
                    $ add_exp(20)
                    return
        else:
        #20 chance - Fuck you iron
            "Even before he set his knife to it, Rowan knew it would be useless. The blade easily passed through the glitter into crumbling rock. There was iron ore here, but it was merely a poor-quality sheen of the stuff over useless silicate."
            "Rowan clambered back down the cliff-side, retrieved his gear and set out again, attempting to shake off the feeling of being cheated by setting his best foot forward."
            #lose 2 move points, gain 20xp
            $ change_mp(-2)
            $ add_exp(20)
            return


    "Decide against it.":
        $ released_fix_rollback()
        "There'd be iron mines in terrain far easier to access, Rowan decided, and he had no wish to break a leg surveying something that might prove worthless. He secured his pack and set off again."
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label landslide:
#Landslide
#No Requirements

"The tinkle of falling pebbles. A distant, angry rumble. The warning signs of a landslide sound inconsequential, somebody else's problem. Until, very suddenly, it isn't, and it's not."
"Rowan jerked his head up in time to see the curtain of rock collapse off the mountainside, and the dusty load of boulders tumbling downwards towards him."

#spot check dc12
$ event_tmp['spot check'] = roll_skill('spot')

if event_tmp['spot check'][0] >= 12 or event_tmp['spot check'][1] == 20:
#pass
    "Rowan's highly trained subconscious had noticed the danger, however, even when the rest of his mind had been wandering."
    "Immediately he threw himself backwards, narrowly avoiding being crushed by one of the larger boulders that came crashing down, obliterating the path in front of him in a cloud of dust and debris."
    "It took him a while to stop coughing and to still his beating heart, but Rowan was otherwise unharmed. Counting his blessings and keeping a closer eye on the terrain above him, he picked out a new way forward."
    #gain 20xp
    $ add_exp(20)
    return
else:
#fail
    #escape artist check dc12
    $ event_tmp['escape artist check'] = roll_skill('escape')
    if event_tmp['escape artist check'][0] >= 12 or event_tmp['escape artist check'][1] == 20:
    #pass
        "Rowan threw his agile body into action, flinging himself beneath a lip of rock to avoid the larger weight of rocks. They flung up clouds of blinding dust as they thundered and span down in front of him, obliterating the path he had been standing on."
        "He heard the groan of rock giving above him and he swiftly rolled to one side, chest heaving as he watched the lip collapse under the weight of the last boulder that came thudding down."
        "It took him a while to stop coughing and to still his beating heart, but Rowan was otherwise unharmed. Counting his blessings and keeping a closer eye on the terrain above him, he picked out a new way forward."
        #gain 20xp
        $ add_exp(20)
        return
    elif (8 <= event_tmp['escape artist check'][0] <= 11):
    #8-11
        "Rowan threw his agile body into action, flinging himself beneath a lip of rock to avoid the larger weight of rocks. They flung up clouds of blinding dust as they thundered and span down in front of him, obliterating the path he had been standing on."
        "He heard the groan of rock giving above him, and although he tried to roll to one side he sprained his shoulder as the lip collapsed under the weight of the last boulder that came thudding down."
        "Clutching his arm and coughing, Rowan sat himself down and waited until his heart stopped trying to beat its way out of his chest. Pain clutched his shoulder and he found he could barely move it."
        "But, considering the devastation around him, things could have been a lot worse. Counting his blessings and keeping a closer eye on the terrain above him, he picked out a new way forward."
        #gain 10xp and 1 wound
        $ add_exp(10)
        $ take_damage(1)
        return
    else:
    #fail
        "Rowan froze for one fatal moment, and was enveloped in the falling debris. A brick-sized rock smashed him on the side of the head, stunning him and sending him sprawling to the deck."
        "This turned out to be a blessing in disguise - the larger boulders thudded and spun over his prone body, carried over by a lip of rock. Another chunk the size of a melon thumped into his back though, hard enough to break a rib."
        "After the landslide had subsided and at least some of the world had swum back into focus, a dust-coated Rowan dragged himself to his feet. He groaned and coughed, trying not to be sick."
        "Pain hammered through him, he felt that he could barely move, and yet he knew that he must. Clutching his side, he limped onwards."
        #gain 5 xp and 2 wounds
        $ add_exp(5)
        $ take_damage(2)
        return
