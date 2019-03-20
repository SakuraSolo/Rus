init python:

    #Rowan attempts to help Helayna escape
    #If Rowan resolved to help Helayna escape, triggers on week 35?
    event('rowan_attemts_to_help_helayna_escape', triggers="week_end", conditions=('week >=35', 'helayna_escape_method == "rowan"'),
        group='ruler_event', run_count=1, priority=pr_ruler_high)


label rowan_attemts_to_help_helayna_escape:
#Rowan attempts to help Helayna escape
#If Rowan resolved to help Helayna escape, triggers on week 35?

$ helayna_escaped = True
$ rowan_shares_room_with_helayna = False

# init
$ event_tmp['bodies_are_stashed'] = False
$ event_tmp['helayna_is_injured'] = False

scene bg9 with fade

"Over the last few weeks, Rowan had been making plans and gathering likely allies.  Since leaving by the portal would be impossible, two main methods of escape were available."
"Rowan would either need to lower Helayna over the outer walls or out through the underground tunnels."
"First he'd started with getting help from the castle staff, naturally since there were already those among them who knew of Helayna and were sympathetic to her cause."

scene bg14 with fade

"The cook who had been feeding her was one option. He could hide her in his carts and would be able to take her through the main hallways safely without arousing suspicions. If he planned on getting Helayna out through the tunnels, they would need to go through those central areas."
"Next was a butler from Rosaria, talented at dressing the nobility and caring for their effects.  Rumors suggested he was something of a fan of Helayna's more eccentric views. If Rowan planned to disguise Helayna, this was his man."
"Getting through side and back passageways would be much easier, though he'd have to avoid high traffic areas in case someone recognized Helayna. Getting Helayna over the walls would mean avoiding the main passages anyway."
"Lastly was the staff manager. A somewhat riskier option to seek help from, but definitely the most useful. He could coordinate the whole surface operation with ease and schedule work such that Helayna could get anywhere without running into anyone."

menu:
    "Seek help from the chef and have Helayna escape through the tunnels.":
        $ released_fix_rollback()
        "Since going through the tunnels meant they were less likely to be spotted, it was the natural path to take. So Rowan spent some time each week trying to butter up his chosen target."
        "Recruiting Helayna's chef was not difficult, he liked Helayna's refined sense of taste and felt that Bloodmeen was no place for a lady."
        $ event_tmp['surface_ally'] = 0

    "Seek help from the butler and have Helayna escape over the walls.":
        $ released_fix_rollback()
        "Rowan had a great deal of personal experience with scaling walls, so it was natural for him to plan on such an escape route. Rumors about the butler proved correct and he was all too eager to help Helayna escape."
        "What surprised Rowan was his insistence that his disguises would be strong enough to fool even the large groups in the central halls. The man hardly wanted to take that chance, so he stuck to his original plan."
        $ event_tmp['surface_ally'] = 1

    "Try and convince the manager to help for access to both options.":
        $ released_fix_rollback()
        if check_skill(15, 'diplomacy')[0]:
            "Rowan knew he was taking a big chance in seeking help from Jezera's second in command with the castle staff, but the potential upside was worth the risk. After talking with the man for a couple of weeks, he was fairly certain it had paid off."
            "With Helayna's safe passage throughout the castle secured, he could pursue both possible avenues for her escape and make the call later."
            $ event_tmp['surface_ally'] = 2

        else:
            "Rowan knew he was taking a big chance in seeking help from Jezera's second in command with the castle staff, but the potential upside was worth the risk. Unfortunately, he felt like he was making little headway towards convincing him after a couple weeks had passed."
            if check_skill(15, 'deceive')[0]:
                "Thankfully, he'd at least managed to avoid arousing suspicion that anything was amiss in the castle. For now at any rate."

            else:
                "To make things worse, the man had grown quite suspicious of Rowan after these talks and was keeping an eye on him. A complication that he'd have to work around."
                $ event_tmp['escape_suspicion'] =+ 1

            "Thankfully he still had other options he could get help from instead."

            menu:
                "Seek help from the chef and have Helayna escape through the tunnels.":
                    $ released_fix_rollback()
                    "Since going through the tunnels meant they were less likely to be spotted, it was the natural path to take. So Rowan spent some time each week trying to butter up his chosen target."
                    "Recruiting Helayna's chef was not difficult, he liked Helayna's refined sense of taste and felt that Bloodmeen was no place for a lady."
                    $ event_tmp['surface_ally'] = 0

                "Seek help from the butler and have Helayna escape over the walls.":
                    $ released_fix_rollback()
                    "Rowan had a great deal of personal experience with scaling walls, so it was natural for him to plan on such an escape route. Rumors about the butler proved correct and he was all too eager to help Helayna escape."
                    "What surprised Rowan was his insistence that his disguises would be strong enough to fool even the large groups in the central halls. The man hardly wanted to take that chance, so he stuck to his original plan."
                    $ event_tmp['surface_ally'] = 1

scene bg11 with fade

"The next step was to get supplies and equipment for her to survive outside of the castle. He'd need either to get help from some of the soldiers or to otherwise stash away things for her to use in her escape."
"The most important thing being her armor, taken as a trophy during the attack. It wasn't too hard to find parts of it, as they were prominently on display in the barracks along with a few torn standards from Reave keep. That also meant that it would be difficult to sneak off with them."
"Even still, having a suit of custom fitted plate armor at hand was far too useful for him to pass up.  Getting the full suit, or at least every part that he could get was essential in the escape."
"Rowan had a choice here.  First he could either trick or coerce one of the soldiers into gathering up the suit piece by piece while he was away, since it would be far too obvious if he did it himself during the scant few days he had in the castle."
"That was, unless he was able to place a decoy suit of armor in its place instead. That would mean buying a replacement one. An expensive prospect, but a safer one."

#if forge has been built
if castle.buildings['forge'].lvl > 0:
    "Finally he could try bringing Greyhide into his confidence and get the minotaur to collect the armor on his behalf. Rowan believed that the forgemaster would be quite willing to help out, but he'd feel guilty dragging a friend into this mess and putting him on the line for someone he didn't know."

menu:
    "Seek an orc soldier.":
        $ released_fix_rollback()
        "Rowan ultimately decided to go with an orc soldier, since they were relatively easy to manipulate. That isn't to say that the task would be trivial, he still needed to find one that was smart enough to know what to look for, but also foolish enough not to pick up on what they were doing."
        if avatar.skill('deceive') >= avatar.skill('intimidate'):
            "He had his man before too long. A small bribe here, a favor there, and now the orc was collecting all sorts of armor pieces and moving them wherever Rowan wanted. Hopefully he'd stay ignorant of the purpose behind this until it was too late."
            $ event_tmp['underground_ally'] = 0

        else:
            "He had his man before too long. A threat here, some posturing there, and now the orc was collecting all sorts of armor pieces and moving them wherever Rowan wanted. Hopefully he was cowed enough to keep his mouth shut until it was too late."
            $ event_tmp['underground_ally'] = 0

    "Buy an armor suit to use as a decoy (costs 300 gold).":
        #Costs 300 personal gold, Rowan can go into debt on this, as there's no warning this option might come up.
        $ released_fix_rollback()
        "By using another suit of armor, it would be a lot less likely that anyone realized that something was amiss.  Plus Rowan would be able to make the swaps himself, rather than needing to rely on someone else."
        "So his plans continued, while he made periodic trips to collect Helayna's armor from the barracks and stash it in a safe place."
        #lose 300 gold (including below 0)
        $ change_personal_gold(-300)
        $ event_tmp['underground_ally'] = -1

    #Only available if the forge has been built.
    "Get Greyhide to help." if castle.buildings['forge'].lvl > 0:
        $ released_fix_rollback()
        scene bg22 with fade
        "As loath as he was to drag someone who had no part into this, Greyhide had full access to the armor and equipment in the underground. He would have no problems collecting the suit, repairing it, or even refitting it if the need arose."
        "Much to Rowan's relief, he didn't ask any question and was satisfied with just doing the job. At least if the man was caught or the plot revealed, as little suspicion as possible would be cast on his friend."
        $ change_base_stat('g', 3)
        $ event_tmp['underground_ally'] = 1

"With Helayna's armor secured, the rest of the supplies needed would be relatively trivial by comparison. A bedroll, food rations, rags and oils for equipment care, items that Rowan had great ease in accessing."

scene bg9 with fade

"As the escape got closer to happening, Rowan found himself worrying more and more about how well Helayna would manage in the wastes. There was always something else that he felt he could do, but there was no time for him to do everything while he was in the castle."

menu:
    "Train Helayna in survival skills.":
        $ released_fix_rollback()
        "There could be no doubt as to the noblewoman's skills in combat and as a commander."
        "Her skill at finding food, water, shelter, or even simply navigating untamed lands was much more questionable. On the other hand, this was one of Rowan's specialities and one of the skills he was very well known for."
        "So the man spent as much time as he could in Helayna's company in the last two weeks, explaining and teaching as much as he could about the lands she would be traveling through and how to survive on her own."
        "His attention towards her did not go unnoticed, but arousing suspicion in this task was unavoidable. Spending time with Helayna was absolutely necessary if he was to teach her anything."
        $ change_base_stat('g', -2)
        $ event_tmp['escape_suspicion'] =+ 1
        $ event_tmp['extra_help'] = 0

    "Buy energy potions for Helayna (costs 100 gold).":
        ##Costs 100 personal gold, Rowan can go into debt on this, as there's no warning this option might come up.
        $ released_fix_rollback()
        "Cla-Min had in her stock a potion that was quite popular among some nobility to give themselves more energy. Getting some for Helayna would let her be much more alert and less likely to make mistakes while she was travelling through the wastes."
        "So Rowan picked several up in the last two weeks before the escape, stashing them with the supplies and armor that had already been collected. This way Helayna would be in the best possible condition during her flight."
        #lose 100 gold (including below 0)
        $ change_personal_gold(-100)
        $ change_base_stat('g', -2)
        $ event_tmp['extra_help'] = 1

    "Nothing more to avoid arousing suspicion.":
        "Considering the danger that he was already putting himself and Helayna through by attempting escape at all, Rowan forced himself to do nothing more. Although he intellectually knew that he was protecting both of them by avoiding Helayna, it didn't help his conscience."
        $ change_base_stat('g', 2)
        $ event_tmp['escape_suspicion'] =- 1
        $ event_tmp['extra_help'] = -1


#If surface ally is 1 (butler) or 2 (manager)
if event_tmp['surface_ally'] in (1, 2):
    "Going out the main gate was obviously not an option, though Rowan could lower Helayna over the walls and have her escape into the forest."
    "This would take less time during the escape, but would require preparation and stashing a rope and harness at the site. Unfortunately it would also mean that Helayna would be on her own after that."
    "Alternatively, he and Helayna could climb down the wallface. While Rowan was quite confident he could climb down, whether or not Helayna was up to the task would be a completely different matter."
    "It would let him keep the gear away from the walls and eliminate the need for rope."
    "Once she was on the ground, Helayna would make her way to the tunnel entrance that her armor was stashed in and she'd equip herself for the journey there."

#If surface ally is 0 (chef) or 2 (manager).
if event_tmp['surface_ally'] in (0, 2):
    "If Helayna was going to go down through the tunnels, the most difficult part would be the central stairwells. There was no avoiding those, as they were the only direct connections between the surface and underground parts of Bloodmeen."
    "Afterwards, Rowan did have a choice. He could pick a direct route towards the place where Helayna's armor was stashed and get her out of the castle as quickly as possible, or loop several times around the other unused passages first."
    "The direct route would take less time and mean that she would be on her way sooner. However they would be seen by more people and Rowan would be more likely to be suspected than if they spent some time throwing off their trail."
    "In either case, Helayna would gear up and then head out into the forest surrounding the castle. After that she'd be on her own out in the wilds."

menu:
    "Lower Helayna over the walls with a rope." if event_tmp['surface_ally'] in (1, 2):
        $ released_fix_rollback()
        $ event_tmp['escape_route'] = 0
        jump .surfaceEscape

    "Climb down the walls with Helayna." if event_tmp['surface_ally'] in (1, 2):
        $ released_fix_rollback()
        $ event_tmp['escape_route'] = 1
        jump .surfaceEscape

    "Take a direct route through the tunnels." if event_tmp['surface_ally'] in (0, 2):
        $ released_fix_rollback()
        $ event_tmp['escape_route'] = 2
        jump .undergroundEscape

    "Go a roundabout route through the tunnels." if event_tmp['surface_ally'] in (0, 2):
        $ released_fix_rollback()
        $ event_tmp['escape_route'] = 3
        jump .undergroundEscape


################################################################################
label .surfaceEscape:

scene bg9 with fade

"Then it came to today. Today was the day of the escape, which Rowan had planned to do the night he returned to the castle. He met in his room with Helayna after making sure no one else would be there until it was time."

show helayna 2 happy at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Okay, I'm here Helayna."

hel "Hello Rowan. Good to see you."

show rowan necklace happy at midleft with dissolve

ro "You as well. How does it feel to be in normal clothes again?"

hel "Begging your pardon, but I've never worn a maid's dress before."

ro "Well, at least it is some actual clothes."

hel "True. This is the most modest thing I've worn since your assault on Reave Keep."

show rowan necklace neutral at midleft with dissolve

ro "Well, are you ready?"

hel "Yes, I think so."

if event_tmp['surface_ally'] == 1:
    pause 0.5
    play sound "music/SFX/door knock.ogg"
    pause 1

    "Shortly after Rowan's return, a knock came at the door. Helayna stood up in shock and started glancing around the room for a hiding place as Rowan checked who was at the door."

    ro "Relax, it's our friend."

    "He stepped aside and allowed the butler to enter the room."

    scene black with fade

    "While the butler helped Helayna with her disguise, Rowan and her went over any last contingencies and concerns over potential problems during the escape."
    "Helayna had a bit of a problem in keeping herself from standing too tall for her disguise, but eventually the two men managed to get her to stoop."

    hel "This feels degrading, walking like this."

    ro "It's only for a little while and I doubt there are too many maids that walk like nobles in the castle."

    scene bg14 with fade

    "A few moments later, the two slipped out of Rowan's room into the empty hallway beyond."
    "They quickly made their way through the back passages towards the outer wall. The skill of the disguise Helayna wore allowing them to slip by the other castle staff with no problems."

else:
    ro "Alright, let's go over the plan and tell me any questions you might have."

    scene black with fade

    "They went over the route, practised a bit of what would be needed, and checked over the work schedule for the night one last time."

    scene bg9 with fade
    pause 0.5
    play sound "music/SFX/door knock.ogg"
    pause 1

    "About an hour later, a knock came at the door. Helayna stood up in shock and started glancing around the room for a hiding place as Rowan checked who was at the door."

    ro "Relax, it's our friend."

    "He stepped aside and allowed the manager to enter the room."

    man "All is ready. You must be off at once, lady Helayna."

    hel "Thank you, good sir."

    "The manager gave a formal bow, then left."

    scene bg14 with fade

    "A few moments later, the two slipped out of Rowan's room into the empty hallway beyond."
    "They quickly made their way through the back passages towards the outer wall.  Thanks to the knowledge of the staff schedule and a few small changes to their benefit, the two were able to avoid anyone who might recognize Helayna."

#battlements
scene black with fade

"The only group that gave them any pause was a pair of orcs patrolling the walls."
"It was the general lack of discipline of the soldiers that let them meet, as Rowan couldn't predict where they'd be at any given time and time was of the essence so he couldn't wait for them to pass."

#deception test, if Hel was claimed personally by Rowan and/or surface ally = 1, DC10, otherwise it is DC15
if raeve_keep_rowan_claimed_helayna or event_tmp['surface_ally'] == 1:
    $ event_tmp['deception_test_result'] = check_skill(10, 'deceive')
else:
    $ event_tmp['deception_test_result'] = check_skill(15, 'deceive')

if event_tmp['deception_test_result'][0]:
#pass
    "Although somewhat confused as to why the boss was wandering around outside so late, the orcs ultimately accepted Rowan's excuses and moved on without paying much attention to Helayna."

elif event_tmp['deception_test_result'][1] >= 6:
#partial fail 6+
    "Rowan was somewhat of a habit when coming back from his expeditions, so being outside so late immediately caught the orc's suspicions."
    "It took awhile for Rowan to finally convince them to let him be and carry on with their patrols without paying attention to Helayna."
    $ event_tmp['escape_suspicion'] =+ 1

#fail
else:
    "Rowan was somewhat of a habit when coming back from his expeditions, so being outside so late immediately caught the orc's suspicions. Things went from bad to worse when one of them started wondering who Helayna was and saying she was strangely familiar."
    "He put his hand onto the woman, causing her to suddenly pull the orc's club out of his belt and strike him with it! Instincts trained for years kicked in and Rowan immediately drew his weapon to help his charge."

    #combat test DC15
    $ event_tmp['combat_test_result'] = check_combat(15)

    if event_tmp['combat_test_result'][0]:
    #pass
        "Thankfully within a few quick strokes, the orcs had been rendered unconscious. They were bleeding a bit, but nothing serious and would live to fight another day."
        $ event_tmp['escape_suspicion'] =+ 1

    elif event_tmp['combat_test_result'][1] >= 6:
    #partial fail 6+
        "While Rowan's intention had been to try and disable the orcs without killing them, after the dust had settled a few moments later, both were dead. The man cursed under his breath while he cleaned the blood off of his weapon."

        $ event_tmp['escape_suspicion'] =+ 2
        #lose 2 orc soldiers
        $ castle.buildings['barracks'].troops -= 2

        "The two then hid their assailants in an alcove, with some crates pushed against the space. It wouldn't hide them from a dedicated search, but Rowan intended for it to be too late to get Helayna back by the time they were found."
        "It wasn't like he could pretend she hadn't vanished."
        #Note bodies are stashed.
        $ event_tmp['bodies_are_stashed'] = True

    else:
    #fail
        "In the chaos of the battle, one of the orcs managed to strike a blow on Rowan before he could be subdued. At that point, the man gave up all pretense of merely knocking the orcs out and dispatched them with brutal efficiency."

        $ event_tmp['escape_suspicion'] =+ 2
        #lose 2 orc soldiers
        $ castle.buildings['barracks'].troops -= 2
        #gain 1 injury
        $ take_damage(1)

        "The two then hid their assailants in an alcove, with some crates pushed against the space. It wouldn't hide them from a dedicated search, but Rowan intended for it to be too late to get Helayna back by the time they were found."
        "It wasn't like he could pretend she hadn't vanished."
        #Note bodies are stashed.
        $ event_tmp['bodies_are_stashed'] = True

if event_tmp['escape_route'] == 0:

    "Upon reaching the site of their escape, Rowan quickly pulled the rope he'd hid here and the harness for lowering Helayna over the wall."
    "As he was tying it around her waist, she put his hand on his and looked him in the eye as the moon poked out from the clouds above."

    #if rowan's corruption is less than 21
    if avatar.corruption < 21:
        hel "Thank you Rowan. For all that I have seen of this place and its masters, I truly believe in my heart of hearts that you are still the hero you once were that defeated Karnas seven years ago."

    #else
    else:
        hel "Thank you Rowan. For all the horrors that you have done to survive and the torment you endure in service to these monsters, it is good to know that the hero still exists inside you."

    hel "Saving me, putting yourself in such danger just to give me a chance, that is something a hero does. I will never forget this, just as I never forgot the great services you did to Rosaria and the Six Realms as a whole."
    hel "Solansia bless you. Solansia bless you my dear [helaynaTitle]."

    "A moment later, he started lowering the woman down the wall.  Soon the moon faded back behind the clouds and Helayna was lost in the darkness over the side of the wall."

    #strength test, DC12
    if check_stat(12, 'strength')[0]:
        #pass
        "After nearly ten minutes of holding her weight up, he felt the rope go slack.  Two soft tugs on it indicated that Helayna had reached the bottom of the wall."
        "So he reeled the rope back in, untied it from the wall, and stashed it back in the box."
    else:
        #fail
        "Holding onto the rope was exhausting.  Not only did Rowan have to support the woman's full weight with his hands, but he had to constantly feed more and more of the rope to get her down."
        "Eventually his hands gave out and he accidentally let it slip too far in his hands. There was a sudden jolt, then the rope when horrifyingly slack. What sounded like a woman's cry of shock came up to him."
        "This mistake left him stunned for a moment. Worried that he may have seriously hurt Helayna, Rowan resolved to climb down the rope and check on her. However, he was reassured after letting the rope fall down all the way by two soft tugs."
        "She'd made it, and she didn't need any help.  Relieved, the man reeled the rope back up, removed it from the wall, and returned it to its hiding place."
        $ event_tmp['escape_suspicion'] =+ 1
        #note Helayna is injured
        $ event_tmp['helayna_is_injured'] = True

    "There was nothing more to be done. Helayna was on her own now and Rowan had to hope she'd manage well enough with what he'd done for her."

    jump .post_escape

else:

    "Upon reaching the site of their escape, Rowan extracted the climbing gear they'd be using to scale the wall. Normally the man could make such a climb with his bare hands, but he doubted that Helayna would be up to such a task."
    "The two geared up, then started down.  Rowan went first, with Helayna coming down shortly afterwards. This way the more experienced climber could find all the best handholds and potentially catch the woman in the in the event she slipped."

    #if 'extra_help' == 1:
    if event_tmp['extra_help'] == 1:
        "The climb went well. Helayna proved to be quite a quick study and the energy potion she consumed shortly before they started seemed to do its work well. Any reservations that Rowan had steadily went away as they got further and further down the wall."

    #else strength check DC12
    else:
        if check_stat(12, 'strength')[0]:
        #pass
            "Things went well at first, but a little ways down the wall Helayna noted she was having trouble finding the holds due to feeling tired. Shortly afterwards her foot slipped and she nearly fell off the wall. Only Rowan's quick reflexes and strength made sure things didn't get worse."
            "After that episode, the hero insisted that they reduce the pace considerably both to make sure that there weren't further accidents and due to the danger and fatigue that ultimately both of them where suffering from due to the hour."
            $ event_tmp['escape_suspicion'] =+ 1
        else:
        #fail
            "Things went well at first, but a little ways down the wall Helayna noted she was having trouble finding the holds due to feeling tired. Shortly afterwards her foot slipped and she feel down onto Rowan.  He tried to catch her, but his strength wasn't up to the task."
            "After his head stopped spinning, the man thanked Solansia for having worn the climbing gear. There was no way he would have stayed on the wall had he not been wearing it."
            "For her part, the adrenalin seemed to have woken the knight up and she redoubled her efforts to hang on, for both their sakes. Even still, Rowan insisted that they take it at a slower pace until they got to the bottom of the wall."
            $ event_tmp['escape_suspicion'] =+ 1
            #rowan gains injury to intelligence
            $ add_effect(MultiEffect('Head injury', 'neg', (('intelligence', -1),), 2))

    "It was quite the relief when the two finally had solid ground under them again. Helayna let out a long breath, then spoke."

    hel "I can't believe you made me do something like that."

    ro "Relax, you did fine and we made it down together in one piece. I wouldn't have been able to stick with you past this point if we hadn't climbed down."

    "Together they set off away from the walls and towards the forests. Rowan allowed Helayna to take the lead, seeing if she could find her way to the tunnel entrance where her armor and supplies were stashed on her own."

    #if 'extra_help' == 0:
    if event_tmp['extra_help'] == 0:
        "Helayna missed a few markers and even got turned around once, but eventually she found it with only a little help from Rowan. It put his mind at ease to know she'd taken his lessons over the last few weeks to heart and should be able to manage in the Wastes."

    #else:
    else:
        "Unfortunately, after she got turned around for the second time Rowan decided to just lead her to the tunnel. He hoped she'd manage better out in the wastes than here, but it was good to know he'd made the right choice by coming with her to the tunnels."

    jump .helaynasGratitude

################################################################################
label .undergroundEscape :

"Then it came to today. Today was the day of the escape, which Rowan had planned to do the night he returned to the castle. He met in his room with Helayna after making sure no one else would be there until it was time."

show helayna 2 happy at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Okay, I'm here Helayna."

hel "Hello Rowan. Good to see you."

show rowan necklace happy at midleft with dissolve

ro "You as well. How does it feel to be in normal clothes again?"

hel "Begging your pardon, but I've never worn a workman's clothing before  Do you not think others will find me suspicious as a woman dressed such?"

ro "Well, as long as you don't talk to anyone I doubt it. Everyone who's spending any real time down in the tunnels dresses like that, even the castle staff when they need to go into the tunnels."
ro "Once we're down there, most we run into won't give you a second thought."

show rowan necklace neutral at midleft with dissolve

ro "Well, are you ready?"

hel "Yes, I think so."

ro "Alright, let's go over the plan one final time."

scene bg9 with fade
pause 0.5
play sound "music/SFX/door knock.ogg"
pause 1

"Nearly a quarter of an hour later, there was a knock at Rowan's door. Helayna shrunk back in surprise and glanced around the room for a hiding place."

ro "Relax, it's our friend."

if event_tmp['surface_ally'] == 0:
    "Pulling open the door, he revealed the chef who'd agreed to help them. Just behind him was the cart that Helayna would sneak through the castle in."

else:
    "Pulling open the door, he revealed the manager who'd agreed to help them. After slipping inside, he formally bowed to both Rowan and Helayna."

ro "Alright, I'll see you two in about half an hour at the tunnels."

scene bg14 with fade

"He left them behind and made a leisurely stroll around the castle. Remaining active the night after returning from scouting was very uncommon for him, and many took obvious note of their boss wandering the halls."
"However, none stopped or questioned him."

scene bg6 with fade

"Arriving in the throne room about ten minutes before the prescribed time, he was relieved to see no sign of the twins or anyone else for that matter. No need to clear the path then, all he had to do was wait."

if event_tmp['surface_ally'] == 0:
    "Not too long afterwards the cook wheeled his cart in. When he reached the pillar that Rowan was lounging against, he called out to them."
    ro "No trouble?"
    man "No sir."
    ro "Good, come on out now Helayna."
    "She emerged from under the cart and joined Rowan among the pillars. He nodded graciously to the chef when then continued on his way his part completed."

else:
    "Not too long afterwards Helayna and the manager hurried inside, glancing about nervously. They almost jumped when they passed the pillar that Rowan was lounging against and he cleared his throat."
    ro "No trouble?"
    man "No my lord, my preparations gave us a clear, clean path. None will know Helayna has come here and you won't find any of my people who know her underground."
    ro "Good work."
    "He nodded and hurried off, leaving Helayna and Rowan behind."


"The two of them then slipped into one of the side passages off of the throne room and down the main stairwell that lead to the castle's underground. This single stair was one of the most high traffic areas in the whole castle and most used it to get up or down."
"This actually made it very useful, as one could get lost in a crowd. Especially one where Helayna's garment fit right in and none would suspect she was travelling with Rowan. Had they taken one of the less used stairs, they would have immediately been taken note of."

if event_tmp['escape_route'] == 2:
    "At the first floor of the tunnels the two of them continued to make use of the crowd for cover, taking the halls that lead to the dungeons. They would cut across there and then into the passages where Rowan had stashed Helayna's armor."
    scene bg9 with fade
    "All those plans fell through at the sight of who happened to be currently lounging in dungeon's guardhouse. Watching the path he'd intended to follow."
    ro "(Crap, it's Andras.)"
    "fortunate before this point to have avoided the twins and thus far the brother hadn't noticed them yet."
    "Now a change of plans would be necessary, since there was little hope of getting Helayna by without the demon noticing him. Even if they snuck behind him, there were others in the dungeons that would notice this strange behavior immediately."
    "He stopped up and turned to the side, thinking about which of the two backup routes they should take. Glancing back for a moment just in time to see Helayna walk right into the very room he'd turned to avoid."
    ro "(Well, alright then.  Guess there isn't a change of plan.)"
    scene bg9 with fade
    show andras displeased at midright with dissolve
    show rowan necklace neutral at midleft with moveinleft
    "He rushed into the room, hoping to catch the demon's attention so he wouldn't notice Helayna."
    ro "Good evening master."
    an "Well now servant, this is a surprise.  What brings you to my hall of delights this evening?"
    ro "Well..."
    "He tried to cast around for an excuse, but was thankfully cut off."
    an "Don't tell me you missed your accommodations down here? I would be absolutely happy to take you in again if you needed some special treatment."

    #If there are prisoners in the dungeon:
    if castle.buildings['dungeon'].prisoners > 0:
        ro "I was more concerned about plans related to your other prisoners."
        an "Yes, yes, you do take an interest in them. I admit that I always feel a little let down when another is sent off, nevertheless if this is on business I won't keep you from it."

    #else:
    else:
        ro "I thought I'd take a look at the condition of the cells, we might be getting some prisoners soon."
        an "Well that's a first. Your conscience can be very tiresome sometimes. Very well, let us take care of the latest of your trifles."
        $ event_tmp['escape_suspicion'] =+ 1

    "After picking up the keyring off the desk, Rowan and the dungeon master went down the call hallway together. Helayna was ahead of them, thankfully still looking away so there was a good chance that Andras still didn't suspect anything."
    "Still, better to keep his attention elsewhere for as long as possible. So Rowan stopped at one of the empty cells and asked it opened. His master instead tossed the ring to him and let him sort out the lock."

    #deceive check, DC15
    if check_skill(15, 'deceive')[0]:
        #success
        "It was quite a relief to have this delay, but Rowan knew that if he let that show Andras would grow bored of him almost instantly and take an interest in something else. So instead he intentionally pretended to have trouble with the lock which elicited a chuckle from Andras."
        "Then he stepped inside the cage for a moment and the demon held out his hand for the keys to be returned."
        ro "I think I'd rather not get locked in here."
        an "That's a shame."
        "He did a circuit of the prison, pretending to check a few details then returning to the hallway. Now Helayna was well out of sight and Rowan felt the main danger was passed. Still, they looked at three more cells to try and alleviate suspicion."
        an "Has your conscience been assuaged?"
        ro "Yeah, what I was mainly worried about was disease."
        an "Hah, that's no fun. They can suffer more at once if they're at least healthy."
        "The man nodded then passed the key ring back."
        hide rowan with moveoutleft
        scene black with fade
        "The demon didn't even seem to notice the man leave in the opposite direction he came in."
    else:
        #fail
        "It was quite a relief to have this delay. However once Rowan opened up the cell he noticed that Andras wasn't paying any attention to him anymore. In fact he was absently looking around the hall. A glance down it revealed..."
        ro "(Idiot girl.)"
        "... that Helayna was looking over her shoulder back at them.  Had she just kept moving forwards without looking back she would have been fine. No doubt it was out of concern for him that she'd done this, shame it put them both in real danger."
        "There was no time to think, just act. Rowan took off at a dead run back up the hall. He didn't look back, but he could hear a whoop from his master as the demon gave chase a moment later."
        hide rowan with moveoutleft
        #tunnels
        scene black with fade
        "There was no way that the man could outright the half-demon, so he instead tried to shake him by taking sharp turns and slipping through the high traffic passages as best as he was able."

        #dexterity check, DC12
        if check_stat(12, 'reflexes')[0]:
        #pass
            "Eventually the sounds of pursuit faded away, leaving Rowan in one of the side passages with the dungeon keys still in his hands. Well, that wasn't exactly the most useful of acts, but hopefully it gave Helayna time to escape."
            "He circled around the tunnels, getting around the dungeon hoping that this time his charge had trusted he'd manage on his own."
            $ event_tmp['escape_suspicion'] =+ 1
        else:
        #fail
            "Unfortunately he wasn't able to get away."
            scene black with redflash
            ro "Argh!"
            "Incredible pain shot through his body as demonic magic took hold of him. A moment later he was writhing on the floor, completely crippled."
            an "Useless bravado. Let that be a lesson for what happens to thieves. I'll be taking my keys back and next time maybe I'll lock you up."
            #tunnels
            scene black with fade
            "Several minutes passed before Rowan was able to return to his feet. His whole body felt sore and there were several bruises where he'd hit the ground hard. Last time that magic had been used on him he'd been out for hours."
            "Thankfully it had only hit him for a moment, so he should be able to walk this off. The real question would be whether or not the distraction had been enough for Helayna to escape."
            $ event_tmp['escape_suspicion'] =+ 2
            #rowan gains an injury
            $ take_damage(1)

    "Going on ahead, the tunnels steadily grew into worse and worse condition until eventually he found Helayna had made her own way to the hiding place of her armor."
    jump .helaynasGratitude

else:
    #tunnels
    scene black with fade
    "At the first floor of the tunnels, Rowan slipped off onto a small passage quite inconspicuously. His charge followed after him rather less so, thankfully none would think much of one of the staff taking a side passage like this."
    "Together they travelled a circuit about the outer less used passages. The further they got from the main stairs, the fewer people they saw. Eventually they hit the tunnels hadn't yet been reclaimed."
    "Many of these passages had been cleared of debris and stripped of what salvaged could be found by Skordred's work teams, so travelling through them was relatively easy. Still, occasionally they found a room or hall that was still filled with rubble and had to alter course."
    "Rowan had with him one of the maps that Skordred had provided him with to navigate through the passages. Unfortunately, it didn't include details on what had or had not been cleared. Just the tunnel layout."
    "Normally that wasn't a problem, as Rowan just needed to know where to order buildings placed. Now he was actually navigating them, it mattered very much where the work had or had not been completed. Especially the question of where work was going on at this moment."
    show skordred neutral at skorright with dissolve
    show rowan necklace neutral at midleft with moveinleft
    sk "You? What'er ya doin down here?"
    "By complete accident, Rowan and Helayna had stumbled on the very dwarf and his team, returning for the night from their current work site. Helayna went rigid with surprise while Rowan thought quickly about how he should respond."
    ro "Good evening to you as well, Skordred."

    #If Rowan has some relationship/favor with Skordred
    if all_actors['skordred'].favors > 0 or all_actors['skordred'].relation > 0:
        sk "Ah, forgive me manors. Good evening champion. Is thar anything ya be needing down here?"
        ro "No, I'm quite fine thank you. Carry on."

        #diplomacy check, DC12:
        if check_skill(12, 'diplomacy')[0]:
            #pass
            "He looked at each of them for a moment, a small frown creasing his features. Helayna's discomfort was obviously strange to the dwarf. Rowan gave a relaxed shrug, then spoke."
            ro "New girl."
            "At once this set Skordred at ease and he nodded. The two groups kept on their ways without further conversation."
        else:
            #fail
            "He looked at each of them for a moment, a small frown creasing his features.  Something was bothering the dwarf, though exactly what the hero couldn't discern."
            "However, he made no move to stop the two of them from carrying on their way.  Still watching them with a confused look as they went down the hallway."
            $ event_tmp['escape_suspicion'] =+ 1

    #else:
    else:
        sk "Certainly is a lot less good with ya around."
        "This wasn't good. Skordred was one of the worst people he could have run into while going against the twins like this as the dwarf was suspicious and distrustful at even the best of times."
        show skordred happy at skorright with dissolve
        sk "Please be calm young lady. Tis merely yar companion that I find offensive."
        hel "Oh, uh, I'm sorry good sir, haven't been down here before."
        sk "Ah, yar a very well spoken, I do truly apologize for this being the place you'll be working. Sometimes our masters can be crass in who they send where."
        ro "Indeed. Why don't we continue on and-"
        show skordred angry at skorright with dissolve
        sk "Hold it up there. I think tha lady can speak for herself, boy."
        hel "Uh, has there been some slight between you two?"
        sk "I'd hardly call killing the great master Karnas a slight."
        show skordred happy at skorright with dissolve
        sk "Though yarself has not earned any ire. Ya haven't done any such crime as to harm a master of mine."
        "Helayna let out a nervous chuckle, smiled and nodded. This wasn't going well and inspite of Skordred's good nature towards the women, he'd eventually get suspicious of her."
        ro "That is quite enough of your behavior Skordred.  If you are done posturing and insulting me, we would like to be on our way."

        #intimidate check, DC12:
        if check_skill(12, 'intimidate')[0]:
            #pass
            show skordred neutral at skorright with dissolve
            "The dwarf looked like he might talk back for a moment, then he ground his teeth together and signalled for his workers to follow him through the tunnel. A moment later Helayna let out another long breath and thanked Rowan for helping her out."
            hide skordred with moveoutright
        else:
            #fail
            show skordred neutral at skorright with dissolve
            sk "Ferget yar threats. Ya may be my supperior while at work, but we aren't at work right now. Besides I have far more reason to be down here than you."
            show skordred happy at skorright with dissolve
            "He took a step forwards and smiled warmly up at Helayna, who was becoming even more nervous by the moment."
            sk "Tell me, which of our masters brought you to this fine place? Ah, no doubt it was Jezera.  Mistress brings almost all the humans we have here. She weaves quite the tales of freedom from Solansia doesn't she?"
            hel "Why would you want to be free of Solansia? Isn't she...."
            "Rowan quickly moved next to the woman and tried to subtly grab her hand in warning. She hesitated, then held her tongue from continuing."
            sk "Why would we want ta be free? Young lady, have ya seen the horrors of the nobility and her so called order? Kharos is the true path."
            "Helayna bit her lip, but held her tongue from answering any further of the zealot's questions. The white knuckle grip that Rowan had on her hand made her very aware of just how tenuous the situation was."
            ro "Let's carry on. We can discuss theology and our mistress's skill with words some other time."

            #sleight of hand, DC12
            if check_skill(12, 'sleight_hand'):
                #pass
                "More annoyance crossed the dwarf's features and he seemed likely to complain some more about what he perceived as Rowan's poor behavior."
            else:
                #fail
                "It was more than just annoyance now that was on the dwarf's features. He was becoming genuinely suspicious of the pair and looked like he might press them even more."
                $ event_tmp['escape_suspicion'] =+ 1

            hel "Good dwarf, I would be happy to continue this at a later time, if it pleases you."
            sk "Very well, I shall not detain you any longer."
            "The two started to continue on, however as Rowan passed Skordred, the dwarf reached out and grabbed his arm roughly."
            show skordred angry at skorright with dissolve
            sk "We will have words later."
            "Then he released the man and signalled his team to follow him out of the halls.  Hopefully words would be all that Rowan heard from this afterwards."
            hide skordred with moveoutright
            $ event_tmp['escape_suspicion'] =+ 1
            #lose relationship with skordred
            $ change_relation('skordred', -1)

        #tunnels
        scene black with fade
        "The two hurried on through the passages, hoping to avoid further delays. Unfortunately, a rather serious one presented itself as one of the main tunnels that Rowan had intended to take turned out to have been almost completely blocked."

        if event_tmp['extra_help'] == 0:
            "Trying to pass through it turned out to be a difficult task, especially for Helayna. Thankfully it was one she managed well enough, taking Rowan's suggestions and lessons to heart throughout the passage and avoiding any injuries from false steps."

        else:
            "Trying to pass through it turned out to not only be a difficult task, but an impossible one. Helayna simply didn't have the skills needed to climb over all that debris in a reasonable amount of time. Then she slipped and scratched up her leg."
            "So Rowan quickly had them go back down and take a different route. Unfortunately, this meant that they had to take some more central passages and were seen by more people, but nothing could be done about that."
            $ event_tmp['escape_suspicion'] =+ 1
            #note helayna is injured
            $ event_tmp['helayna_is_injured'] = True

        scene black with fade
        "Finally they reached the tunnel entrance where Helayna's armor and gear were stashed."

################################################################################
label .helaynasGratitude:

#tunnels
scene black with fade
show rowan necklace neutral at midleft with dissolve
#helayna shocked
show helayna neutral at midright with dissolve

hel "peechless, my [helaynaTitle]. You actually found my armor."

ro "Everything still fits?"

show helayna happy at midright with dissolve

hel "It's a little battered, but wearing this suit I feel whole. Like there was something regained that I hadn't even realized I'd lost."

#Helayna escape CG
scene black with fade

"Rowan then extracted the travel bag and hefted it, when he turned back around he was taken by how Helayna looked at that moment. The moon was just peeking through the trees at the edge of the tunnel, glinting off of the knight's armor and her smiling face."

#if rowan's corruption is lower than 21
if avatar.corruption < 21:
    hel "Thank you Rowan. For all that I have seen of this place and its masters, I truly believe in my heart of hearts that you are still the hero you once were that defeated Karnas seven years ago."

#else
else:
    hel "Thank you Rowan. For all the horrors that you have done to survive and the torment you endure in service to these monsters, it is good to know that the hero still exists inside you."

hel "Saving me, putting yourself in such danger just to give me a chance, that is something a hero does. I will never forget this, just as I never forgot the great services you did to Rosaria and the Six Realms as a whole. Solansia bless you. Solansia bless you my dear [helaynaTitle]."

"She accepted the bag, then turned away and set off into the night. There was nothing more to be done. Helayna was on her own now and Rowan had to hope she'd manage well enough with what he'd done for her."

################################################################################

label .post_escape:
#post escape
scene bg9 with fade

#if bodies were stashed
if event_tmp['bodies_are_stashed']:
    "In the morning, an alarm was raised after the orc wall patrol was missing and then later found stashed in an alcove."

    #if rowan claimed helayna
    if raeve_keep_rowan_claimed_helayna:
        "Rowan reported that Helayna was missing shortly afterwards, leading to a full investigation by the twins. They were certain that the woman was in such a state that she couldn't have left on her own and some conspiracy existed that was undermining their authority."

    #else
    else:
        "Around the same time Helayna was found to be missing. The twins were certain that the woman was in such a state that she couldn't have left on her own and some conspiracy existed that was undermining their authority. So they launched a full investigation."

#else
else:
    #if rowan claimed helayna
    if raeve_keep_rowan_claimed_helayna:
        "In the morning at his usual time of rising, Rowan decided to report that Helayna was missing. The twins were certain that the woman was in such a state that she couldn't have left on her own and some conspiracy existed that was undermining their authority. So they launched a full investigation."

    #else
    else:
        "In the morning, an alarm was raised when it was discovered that Helayna was missing. The twins were certain that the woman was in such a state that she couldn't have left on her own and some conspiracy existed that was undermining their authority. So they launched a full investigation."

scene bg6 with fade

"The man did his best to carry out his normal duties while events unfolded around him. He wasn't a direct part of the investigation, but he did hear whispers from the staff that gave him a rough idea of how the search went."

#if helayna was injured
if event_tmp['helayna_is_injured']:
    "Blood was found outside on the grounds before too long, no doubt from the injury that Helayna had taken during the escape, but there was no sign of her or her body. So it sounded like she has escaped in spite of his failure to get her out safely."
    #gain 3 guilt
    $ change_base_stat('g', 3)

#else
else:
    "There was no sign of Helayna or a body on the grounds or in the forest beyond. So the first of Rowan's worries was satisfied. She had successfully escaped and was probably either already at the Wastes or about to arrive."

"The twins had no way to track the woman, so she was as good as free at this point. Of course, they didn't know that, so they were also searching the castle for a place she might have hid or signs of how the escape had been accomplished."

#If suspicion is less than 1.
if event_tmp['escape_suspicion'] < 1:
    "The day wore on and it was becoming more and more apparent that Rowan had done well. Quick thinking and little delay had lead to little to no evidence implicating him in the escape."

#If suspicion is 1.
elif event_tmp['escape_suspicion'] == 1:
    "As the day wore on, Rowan heard at least one instance of him being suggested as a suspect. There was no doubt that he'd made mistakes during this escape, so it was only to be expected that at least some suspicion would be placed on him."

elif event_tmp['escape_suspicion'] == 2:
#If suspicion is 2.
    "As the day wore on, significant suspicion was falling on Rowan. This was only to be expected, there'd been problems and he'd drawn unwanted attention to himself.  It remained to be seen what would happen to him as a result."

elif event_tmp['escape_suspicion'] >= 3:
#If suspicion is 3 or more.
    "Almost immediately Rowan came under suspicion of being responsible for the escape. He'd been seen returning to his room abnormally late and many other suspicious activities were laid at his feet. It was almost certain that the twins would come for him soon."

if event_tmp['escape_suspicion'] > 0:
#If suspicion is greater than 0.
    show rowan necklace neutral at midleft with dissolve
    show jezera displeased at midright with dissolve
    show andras displeased at edgeright with dissolve

    ro "Master, mistress, is there something I can help you with?"

    an "Well?"

    ro "Well what?"

    je "Are you responsible for this incident? It's obvious that you might have a reason to want to see that girl get away from here."

    #deception check: if suspion = 1, DC7, if suspicion = 2, DC15, and if suspicion = 3 or more, DC21
    if event_tmp['escape_suspicion'] == 1:
        $ event_tmp['final_deception_result'] = check_skill(7, 'deceive')
    elif event_tmp['escape_suspicion'] == 2:
        $ event_tmp['final_deception_result'] = check_skill(15, 'deceive')
    else:
        $ event_tmp['final_deception_result'] = check_skill(21, 'deceive')

    if event_tmp['final_deception_result'][0]:
        #pass
        ro "No, she was in a horrible state and if I'd set her free I would have sentenced her to far worse in the Rackshan Wastes."

        an "Hmph."

        je "There, you see? Our Rowan is better than that."
    else:
        #fail
        ro "No, she was in a horrible state and if I'd set her free I would have sentenced her to far worse-"

        show andras angry at edgeright with dissolve

        an "SHUT UP!"

        show bg6 with redflash

        an "YOU LIAR!"

        show bg6 with redflash

        #If Rowan did not claim Helayna
        if not raeve_keep_rowan_claimed_helayna:
            an "TRAITOR! THIEF!"
        else:
        #else
            pass

        "Each accusation was followed by a flash of pain as another jolt of Andras's magic shot through Rowan's body."

        scene black with fade

        "Each accusation was followed by a flash of pain as another jolt of Andras's magic shot through Rowan's body."

        scene bg8 with fade
        show rowan jail hurt at midleft with dissolve

        ro "(Back here again.)"

        "His stirring brought the attention of someone else currently sitting in the cell."

        show jezera displeased at midright with dissolve

        je "Now why did you have to go and do this? Our best asset, working against us."

        "Rowan tried to sit up, but a fresh flash of pain made him lay back down on the ground."

        je "Don't hurt yourself. My brother is going to do enough damage to you on his own and we still need you alive."

        ro "What?"

        show jezera neutral at midright with dissolve

        je "You heard me right. You still have your position in this castle, however I cannot stop my brother from extracting his pound of flesh. All I can hope is that you will learn something from this and will avoid future tresspasses."
        je "I've arranged for you to have a few days of the week out of my brother's care to continue your duties. I do hope you don't waste them, my hero. I may not be able to stop him from hurting Alexia should you slouch in your duties."

        hide jezera with moveoutright

        "She got up and walked out of the cell, leaving Rowan laying on the ground in chains."
        "A little after that, a smile crossed Rowan's face. Even though he'd been caught and his body would suffer for it, his mind was at ease for doing good that day."

        #Successfully rescuing Helayna reduces Rowan's guilt and corruption.  If Rowan claimed Helayna, reduce corruption by a little more, remove Helayna from Rowan's room, and Alexia can now move back in.
        #Increase week count by 4 (time spent imprisoned)
        # TODO: permanent injury
        #gain 1 permanant injury
        $ week += 4
        $ change_base_stat('g', -2)
        $ change_base_stat('c', -2)
        if raeve_keep_rowan_claimed_helayna:
            $ change_base_stat('c', -2)
            $ rowan_shares_room_with_helayna = False
            # TODO: check if alexia should be moved to rowan's room in any case
        return

#else
    pass

"Frustrated by their inability to find a true culprit, Andras began lashing out at the castle's residents. He intended to make an example of someone, even if it wasn't the right person to make up for what had been lost."

#If escape route was 0 or 1.
if event_tmp['escape_route'] in (0, 1):
    "Since most of the evidence they found implicated at least some part of the surface staff, they were the ones who took the brunt of his fury. This in turn made Rowan's management of the castle more difficult."
    #Increase surface maintenance costs for five weeks.
    # TODO: increase in maintenance costs (negative surface_maintenance_reduction?)
else:
#Else (escape route was 2 or 3)
    "His soldiers eventually took the brunt of his anger, with many of his old habits of killing any of them for even the slightest failures resurfacing. This in turn made Rowan's efforts at building an army for him that much more difficult."
    #Decrease orc recruitment by 4 for next 5 weeks.  Lose 5 morale.
    $ change_morale(-5)
    # TODO: penalty to orc recruitment

"Even though he'd managed to avoid direct punishment for going against his masters and rescuing Helayna, Rowan still was the one who had to pay for it as no relaxation of his goals had been made. This was just another variable he'd have to account for in his service."
"Privately however, he felt better than he had in a long time. That day, he'd done good."

#Successfully rescuing Helayna reduces Rowan's guilt and corruption.  If Rowan claimed Helayna, reduce corruption by a little more, remove Helayna from Rowan's room, and Alexia can now move back in.
$ change_base_stat('g', -2)
$ change_base_stat('c', -2)
if raeve_keep_rowan_claimed_helayna:
    $ change_base_stat('c', -2)
    $ rowan_shares_room_with_helayna = False
    # TODO: check if alexia should be moved to rowan's room in any case
return
