init python:

    #Orcish families and the neutrals
    event('orcish_families_and_neutrals', triggers='orciad_explore', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)
    #Batri's men going on a raid
    #Requires that player have visited Batri's tent once, but they don't need to have accessed it.
    event('batri_s_men_going_on_raid', triggers='orciad_explore', conditions=("week >= 4", "rowan_met_batri != 'first visit'"), group='orciad_camp', priority=pr_map_res)
    #Find noblewoman's prison (Side quest storyline)
    #Requires that the player have spoken to either Ulcro or Batri.  Priority event that always happens first when exploring until the player succeeds.
    event('find_noblewoman_s_prison', triggers='orciad_explore', conditions=("week >= 4", 'found_delane_tent == False', "rowan_met_batri=='met' or rowan_met_ulcro=='met'", "last_delane_visit_attempt < 1"),
        group='orciad_camp', priority=pr_story)
    #Orcish courtship in action
    event('orcish_courtship_in_action', triggers='orciad_explore', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)


label orcish_families_and_neutrals:
#Orcish families and the neutrals
#"Explore The Camp" event

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade

#If (Orciad quest is still incomplete)
if orciad_state == 1:
    "In the main camp area, but nearby where Tarish had set herself up as a third party to the conflict between the main leaders, Rowan noticed that most of the women had taken up residence here along with the mothers and children."

#If (Orciad quest is complete)
elif orciad_state == 2:
    "An area near the center of the camp had been set aside for the mothers and their children to live in."

    "From his experience during the war and his time in Bloodmeen, Rowan was very familiar with the fact that orc women were just as capable as the men in combat. Though there usually wasn't quite as many of them in the armies of chaos as the men."
    "Here he could see why, since having and raising children still fell to them. The mothers all gathered together to help each other raise their children communally. Sometimes a male would come by to check up on things, but the young were primarily the mothers' responsibility."
    "He found the communal parents included pregnant orcs, those with newly born children nursing, and those supervising toddlers involved in large playfighting brawls. There was even one mother who was teaching her daughter how to swing a weapon."
    "Orcs lived to fight, even from childhood. Once one was old enough to fight with an axe, club, or sword, they left their mothers and joined the ranks of warriors. The only reason one left that position was if they were injured, sick, or had to raise a child."
    "Then you returned to fighting as soon as you could. To do otherwise was considered cowardly and meant you'd almost certainly be either killed or banished from the tribe."
    "This everyday existence was such a stark contrast to the way that Rowan lived, where fighting was only as a necessity. Even still, he could see the looks of pride the mothers had for their children when they did well, a look he'd seen his parent's faces."

#If (orciad sidequest is incomplete)
if orciad_state == 1:
    "Rowan left the mothers behind and explored more of this area of the camp. The sheer number of females relative to the number of males stood out to him right away. At first he thought that maybe these were more of Tarish's supporters, but they were distinctly still part of Ulcro's camp."
    "After asking a few questions and listening to several of the orcs talk, it became apparent that this group was mostly neutral in the spat between the two orc leaders. The women especially didn't have many good things to say about this bickering over a captured pink skin lady."

#rejoin
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label batri_s_men_going_on_raid:
#Batri's men going on a raid
#"Explore The Camp" event
#Requires that player have visited Batri's tent once, but they don't need to have accessed it.

#Rowan meets a group of Batri's soldiers and can choose to join them on a raid.  Doing so triggers a skill check and Rowan gains guilt.
#If successful, Batri's power in the camp increases, Rowan gets some personal money, and the player can access his tent if they can't already.

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade

#Variant if Orc-iad is not complete
if orciad_state == 1:
    "Rowan stumbled on a group of orcs on the challenger, Batri's, side of the camp that were gathering up warriors for a raid. The targets were naturally the nearby human settlements, farms, and caravans if they could find them."
    "As the warchief didn't seem to care that much about attacking or otherwise harming them, they didn't need to worry about reprisals in their absence."
    "As a human, Rowan was not approached to go on this attack."

    #if Rowan has no access to Batri's tent
    if rowan_met_batri != 'met':
        "However, he could offer to join in order to gain a meeting with Batri himself."

    #if Rowan has access to Batri's tent
    else:
        "However, joining would give him a chance to build up Batri's power in the camp."

    #rejoin
    "He'd even get his own share of the loot."
    "That is, if his conscience could handle him attacking his countrymen."

#If orciad is complete, it is a generic group of raiders instead.  The player can still get some personal money at the cost of guilt by going on a raid.
else:
    "Rowan stumbled on a team of orcs looking for warriors to go on a raid. This was a smaller scale attack on the surrounding Rosarian countryside."
    "Given his good graces with the warchief, Rowan was naturally invited to come along on the raid. A fair share of the loot was promised if he joined, as well as a hearty celebration afterwards."
    "That is, if his conscience could handle him attacking his countrymen."

#rejoin
menu:
    "Go on an orc raid.":
        $ released_fix_rollback()
        $ rowan_joined_batri_s_raiders = True
        jump orcRaid

    "Not today.":
        $ released_fix_rollback()
        #no effect
        jump campMenu

################################

label orcRaid:

#countryside bg
scene black with fade

#roll a d20 and add the players luck modifer
$ event_tmp['raid_luck_roll'] = roll_stat('luck')[0]

if event_tmp['raid_luck_roll'] <= 7:
#low luck (less than 7) # less or equal
    #Attacking a weak farm.
    #No combat roll needed, always succeeds.

    "Pickings were slim on this raid. There wasn't enough orcs on this raid to hit large targets, so they went around hitting smaller farms and homesteads, most of which had already been abandoned or picked over."
    "Even still, there was more than one desperate plea for mercy laid at Rowan's feet that day as he helped pacify what little resistance the farmers and peasants were able to muster against this force."
    "While little was gained, they did not return to the camp empty handed."
    #Roll for loot and Batri strength. Inform the player how much Rowan's share was. Value should be fairly small.
    $ temp = dice(10) + 5
    $ change_personal_gold(temp)
    "Rowan's share: [temp] gold"
    $ batri_power += dice(10) + 5
    $ delane_gifts += 3
    #Rowan gains some experience, guilt, and a small amount of infamy.
    $ add_exp(15)
    $ change_base_stat('g', 2)
    $ change_base_stat('f', 2)
    jump campMenu

elif event_tmp['raid_luck_roll'] <= 14:
#medium luck (8-14)
    #Attacking a small hamlet

    "The orcs lead Rowan to one of the hamlets in the region. It was a fairly easy target, but would be able to put up more resistance than random farms and homesteads would."
    "The hero's natural inclination in these sorts of situations was always to take charge, though the orcs simply weren't interested in listening to his plans or sending any form of scouting forward. They just fell upon the peasant in a furious battle charge."

    #Roll combat test, DC8.
    if check_combat(8)[0]:
    #Pass
        "In spite of the efforts of the locals to muster a militia to fight back against the raid, things went very poorly for them. Within minutes the orcs had swarmed over the people and were bagging up all the valuables they could find."
        "Then there was a flash of light, and a fire was started on one of the houses.  Roaring with triumph, the orcs made their escape with their loot. Using the burning buildings as cover, they easily made it back to the camp with a few prisoners as well."
        #Roll for loot and Batri strength.  Inform the player how much Rowan's share was.  Value should be middling.
        $ temp = dice(10) + 15
        $ change_personal_gold(temp)
        "Rowan's share: [temp] gold"
        $ batri_power += dice(10) + 10
        $ delane_gifts += 5
        #Rowan gains some experience, guilt, and a small amount of infamy.
        $ add_exp(20)
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 2)
        jump campMenu

    #Failure
    else:
        "While the orcs were able to bowl over the townsfolk through sheer force of numbers, they did take far more casualties than they should have. Among them was Rowan, who was unfortunate enough to take an arrow right after the battle was joined."
        "His retreat to tend to his wounds did not go over well with the orcs, who refused to share any of their spoils with him when they returned to the camp."
        #End event, Rowan gets an injury.
        $ add_effect(MultiEffect('Wound', 'neg', (('strength', -1),), 2))
        #Rowan gains some experience, guilt, and a small amount of infamy.
        $ add_exp(15)
        $ change_base_stat('g', 2)
        $ change_base_stat('f', 2)
        jump campMenu

elif event_tmp['raid_luck_roll'] <= 20:
#high luck (15-20)
    #Attacking a trade caravan

    "Shortly after leaving the camp, the raiders were fortunate enough to stumble on the tracks of a caravan that recently pass through, probably travelling between Prothea and Rastedel."
    "Rowan soon identified the direction it was going and lead them to their quarry."
    "It turned out to be merchants, amongst the best targets they could be hitting, but also one of the most dangerous. This would be a difficult fight, one that the orcs were all too eager to start."

    #Roll combat test, DC14.
    $ event_tmp['raid_combat_roll'] = check_combat(14)
    #Pass
    if event_tmp['raid_combat_roll'][0]:
        "Although the guards were ready for an attack, especially a disorganized one from bandits or orcs, they were not prepared for what Rowan brought upon them."
        "Quickly he identified who the commanders were, and struck them down with several arrows in quick succession. Then he joined the orc raiders as they set upon the now disorganized and demoralized mercenaries."
        "His companions didn't seem to realize just how instrumental he was in helping them win this battle, but the raiders did think he'd earned a good share of their loot when they returned to the camp with their trinkets and weapons they'd looted from the merchants."
        #Roll for loot and Batri strength.  Inform the player how much Rowan's share was.  Value should be high.  Rowan gets a little extra experience for this result.
        $ delane_gifts += 7
        $ temp = dice(10) + 25
        $ change_personal_gold(temp)
        "Rowan's share: [temp] gold"
        $ batri_power += dice(10) + 15
        #Rowan gains some experience, guilt, and a small amount of infamy.
        $ add_exp(25)
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 2)
        jump campMenu

    #Partial pass (10+)
    elif event_tmp['raid_combat_roll'][1] >= 10:
        "The guards were ready for sudden disorganized attacks, like from bandits or these orcs. So the fighting was quite fierce after it was joined. Pretty much everyone, including Rowan, got some scratches during the melee."
        "Ultimately what won the battle was the orc's stubbornness. The humans eventually decided they'd taken too much damage and made a retreat, leaving their wagons behind."
        "While they were bruised and battered, this attack was considered a success, by and large, through Rowan thought it a bit of a pyrrhic victory. Still, he'd earned his fair share."
        #Roll for loot and Batri strength.  Inform the player how much Rowan's share was.  Value should be high on loot, middling on Batri strength.  Rowan is injured.
        $ delane_gifts += 5
        $ temp = dice(10) + 25
        $ change_personal_gold(temp)
        "Rowan's share: [temp] gold"
        $ batri_power += dice(10) + 10
        $ add_effect(MultiEffect('Wound', 'neg', (('strength', -1),), 2))
        #Rowan gains some experience, guilt, and a small amount of infamy.
        $ add_exp(20)
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 2)
        jump campMenu

    #Failure
    else:
        "The guards were ready for sudden disorganized attacks, like from bandits or these orcs. Try as Rowan might, he couldn't do anything with the mob he'd joined, and their ferocity proved no match for the mercenary's discipline."
        "Charge after furious charge was thrown back, with more and more losses mounting. Finally the hero was able to get the orcs to retreat before the entire force was wiped out, but he took a lot of damage himself in the process."
        "This wasn't the first failed raid to return to the camp, though few returned so bloody. Some called them cowards, others commended them for their scars. As far as reputation went, Rowan figured he'd mostly broke even."
        "However his body was rather worse for wear."
        #Rowan is seriously injured.
        $ add_effect(MultiEffect('Wound', 'neg', (('strength', -2),), 3))
        #Rowan gains some experience, guilt, and a small amount of infamy.
        $ add_exp(15)
        $ change_base_stat('g', 3)
        $ change_base_stat('f', 2)
        jump campMenu

#luck critical (21+)
else:
    #Attacking a weakly defended noble retinue

    "To their great folly, a member of the Rosarian nobility had decided to travel the roads on this day with minimal escort. When Rowan informed them exactly who they were tracking, the orcs became very excited and set a pace that almost wore Rowan out."
    "However, they quickly caught up with the small retinue and quickly defeated the meager force through superior numbers. Much to the orc's pleasure, the noble refused to surrender and went down fighting."
    "As they divvied up the spoils, Rowan soon realized the purpose of this trip. It seemed to be to deliver a gift to another of the nobility, possibly several. There was quite a few rare items here he could choose from for his share."
    #Player is presented a list of items and chooses one.  Jewelry and a noblewoman dress are potential options, which can each be gifted to Ulcro once to then give to Delane.  They can also be sold to merchants for a profit. (TODO)
    # TODO: jewerly and dress
    $ delane_gifts += 10
    $ temp = dice(10) + 35
    $ change_personal_gold(temp)
    #Roll for Batri strength.  Value should be high.
    $ batri_power += dice(10) + 20
    #Rowan gains some experience, guilt, and a small amount of infamy.
    $ add_exp(25)
    $ change_base_stat('g', 3)
    $ change_base_stat('f', 2)
    jump campMenu


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label find_noblewoman_s_prison:
#Find noblewoman's prison (Side quest storyline)
#"Explore The Camp" event
#Requires that the player have spoken to either Ulcro or Batri.  Priority event that always happens first when exploring until the player succeeds.

if met_with_delane == False:

    $ change_mp(-5)
    $ prevent_tile_exploration()
    # using this var for attempt to find tent also
    $ last_delane_visit_attempt = 1

    scene bg26 with fade

    "During Rowan's explorations of the orcish camp, he kept an eye out for where the captured noblewoman might be held captive."

    #Spot check (DC15) to locate noblewoman
    if check_skill(15, 'spot')[0]:
        #Success, trigger first time visit to Delane.
        "There was an odd concentration of soldiers in a secluded part of Ulcro's side of the camp. It was almost opposite where Tarish was holled up, at the other end of the gorge."
        "Sensing that this might be what he was looking for, Rowan set about covertly observing the patrols and movements about this part of the camp."
        "Fortunately for him, while these orcs were well disciplined, they were not the sharpest observers. It didn't take that long to slip out of their sight and patiently watch from the shadows."
        "After a few hours, he changed his hiding hole and watched again. Then again around an hour after that."
        "The hero figured he was close when he found a large tent that was under continuous watch from three different guard posts. His suspicion was confirmed when he noticed that the tent was actually a building disguised as a tent."
        "Orcs would never go through the trouble of doing something as elaborate as this unless it was as special as the noblewoman evidently was to Ulcro."
        "Now Rowan could try to sneak in to see her for himself."
        #Player can now sneak to visit Delane on the camp menu, but they will have to wait a week between visits.  It is listed as visiting a noblewoman.  Add note6 to journal.
        $ journal.add_quest_note('orciad', 'note6')
        $ found_delane_tent = True
        jump campMenu

    #Failure, trigger a different random camp event.
    else:
        $ choose_and_insert_next_event('orciad_explore')
        return
        
else:
    $ choose_and_insert_next_event('orciad_explore')
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label orcish_courtship_in_action:
#Orcish courtship in action
#"Explore the Camp" event

scene bg26 with fade

"This part of the camp was particularly rowdy today, with lots of guttural shouting and chest pounding."
"After getting closer, Rowan found that a large section of ground had been cleared for several competitions. Orcs were in the process of digging holes by hand, lifting various heavy objects, and balancing a plate on the end of a stick."
"Other contests seemed like they'd finished not too long ago, with debris scattered around from what had been going on before. After watching for several minutes, the man finally started to get an idea of what was going on."
"This was some kind of courtship ritual, the contests having been started by orcish woman who wanted to have a child. Each set their own contest for the men to attempt, first by showing how good they were at it and then taking challengers to prove themselves worthy of her."
"It wasn't just a contest of being the best, you also had to have endurance. No orcs were ever eliminated unless they were severely outclassed. One kept at it until they either withdrew or were the only one left."
"At least two couples who'd been decided by previous contests were also watching the show, plus a woman who'd been tied up to a pole and occasionally had dirt thrown in her face by other female orcs."
"Rowan had to ask why she was being publically humiliated. After a few questions he worked out that she'd tried to start a competition she was very bad at, unworthy of orcs giving her a child. All orcs had to be powerful, not just the men."
"In off comment, the hero had wondered if the woman hadn't really wanted a child, but to have some fun. That got him a dirty look and a suggestion that if all she wanted to do was get off she should have gone to find some prisoners to fuck."
"After that, he returned to watching the ongoing three contests. These ones seemed like they'd only just started.and were still getting new competitors joining in to the feats of strength, speed, and dexterity."

menu:
    "Try your hand at strength, digging holes bare handed.":
        $ released_fix_rollback()
        show orc soldier neutral at midright with dissolve
        show wild orc neutral at edgeright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        "Rowan stepped forward among the competitors.  Right away one of them put a hand on his shoulder."
        os "What you doing humi?  Dis orc sport for who get to make babies."
        ro "Yes, I'm here to compete."
        os "Eh? What makes you dink that okay?"
        ro "What, are you afraid I might beat you?"
        "That got the orc's attention. He wheeled around and started the next round without another word. No one else made any attempt to stop Rowan when he participated in that round."
        "That didn't stop the crowd of orcs from jeering at him when it was his turn."

        #strength check (DC18)
        if check_stat(18, 'strength')[0]:
            $ released_fix_rollback()
            #success
            "Digging holes barehanded was tiring and very intensive for what the orcs were demanding in this contest, but Rowan didn't let that slow him down. Again and again, he was able to match or at least come close to his competitors."
            "Sudden cheering drew his attention away for a moment, as he saw the runners had declared a winner. Yet among his group only two of the ten or so competitors.  He did draw some satisfaction that the one who'd challenged him was among those who'd given up."
            "Soon afterwards the other competition ended. Rowan realized that perhaps this had been a mistake, while he'd certainly put on quite a bit more musculature since joining the twins, could he really beat orcs in a test a strength?"
            hide wild orc with moveoutright
            "Digging and digging wore on, lasting hours.  Most of the time Rowan didn't even realize when another orc dropped out, but he steadily held out round after round."
            "His hands felt numb, his arms on fire, but he never stopped grabbing another handful of dirt."
            hide orc soldier with moveoutright
            "Finally, when it was nearly dark out, powerful hands gripped him from behind and lifted him up from the ground. He was turned around and found himself facing the orc woman who'd started this contest."
            #show female orc
            "She ran her callased hands over his, dirt caked deep under both their nails. For his part, the man found looking over her powerful, yet still feminine body almost a relief."
            "The end of the digging along felt wonderful.  Their eyes met, white pupiless orbs searching the man's brown ones."
            femorc "Yous really strong for a humi. Dis should be fun."
            jump courtshipVictory

        #fail
        else:
            $ released_fix_rollback()
            "Rowan did well enough for the first few rounds, however it soon became apparent that he'd probably made a mistake in challenging the orcs to feats of strength."
            "Already he was tiring fast, but those around him looked to be still doing quite well. Realizing that he'd never be able to pull this off, he decided to try and at least keep digging long enough for at least one of the orcs to give up."
            "Much to his satisfaction, and the pleasure of the observers, the original orc who'd challenged him proved to be the first to withdraw from the contest. Rowan stopped soon after himself, but there was no jeering at him now."
            jump courtshipFail

    "See if you're a faster runner than orcs, in foot racing.":
        $ released_fix_rollback()
        show orc soldier neutral at midright with dissolve
        show wild orc neutral at edgeright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        "Rowan stepped forward among the competitors.  Right away one of them put a hand on his shoulder."
        os "What you doing humi?  Dis orc sport for who get to make babies."
        ro "Yes, I'm here to compete."
        os "Eh? What makes you dink that okay?"
        ro "What, are you afraid I might beat you?"
        "That got the orc's attention. He wheeled around and started the next round without another word. No one else made any attempt to stop Rowan when he participated in that round."

        #reflexes check (DC18)
        if check_stat(18, 'reflexes')[0]:
            $ released_fix_rollback()
            #success
            "Speed was Rowan's speciality. In battle he always tried to be one step ahead of his opponent's, one arm length apart, one breath beyond."
            "This was why he'd eschewed metal armor during the war even after it became available, sticking with the leather he'd been initially issued."
            "Now, speed in battle is different from running speed, but this was just as much of a contest of endurance as it was of speed. Rowan did the laps again and again, amazing the crowd and the other competitors."
            hide wild orc with moveoutright
            "Soon, those watching had traded their jeers to cheers as he finished yet another lap, leaving the one orc still trying to best him almost in the dust."
            "He tried to call foul, bringing up the same argument that a human shouldn't be able to compete again."
            "However, now the onlookers were against him and demanding he withdraw after such a poor final showing. He looked like he'd do something more, but then was tackled from behind by the woman who'd started the contest."
            hide orc soldier with moveoutright
            #show female orc
            "After bringing him down and stomping on the fallen form once, the orcish woman turned to Rowan."
            femorc "I say, yous da winner!"
            "A final cheer went up from the onlookers, celebrating the human's victory as if it were one of their own."
            jump courtshipVictory

        #fail
        else:
            $ released_fix_rollback()
            "While racing against orcs was certainly one of the easier competitions Rowan could have joined, the difference in height between the human man and the orc men soon proved to be a bit of an issue."
            "Their strides were much longer than Rowan's, so he had to put a lot more work into moving his legs just to match his competitors."
            "The pace that was set and the sheer number times that same run was done soon started to take its toll on his endurance."
            "Thankfully, many other orcs were finding this particular contest was beyond them and Rowan's withdrawal was about after half of the others had left."
            "Even getting a few nods of approval from the crowd as he rejoined them and beating out the orc who'd first stopped him."
            jump courtshipFail

    "Competing to mate with an orc woman isn't something you want to do.":
        $ released_fix_rollback()
        jump courtshipFail


label courtshipVictory:

"The orc woman wrapped her arm around the slightly smaller man and started leading him away from the competition grounds."

scene bg30 with fade

show rowan necklace neutral at midleft with dissolve
#show female orc

"She led him to a tent that seemed to be empty, then gave Rowan a curious look."

femorc "Well? You gonna fuck me?"

"He was normally more of a lover than a fucker, but Rowan figured that orcs tended to be just as ferocious in bed as on the battlefield. So he was going to be a lot more aggressive than he usually was."

#kissing and fondling/stripping CG.
scene black with fade
show rowan necklace neutral behind black
#show female orc behind black

"Deciding to just act on instinct, he stepped forward and pulled the woman into a deep kiss.  She seemed confused at first, but soon got into it and forced her tongue into his mouth in response. That gesture was appreciated, as it hurt to press against her tusks."

"After a moment she pushed Rowan back and smiled."

femorc "Humis have funny way to fuck."

ro "It's better if we have some foreplay."

femorc "Show me."

"Once again, the two kissed, pushing their tongues into one another's mouths and exploring the difference in anatomy. The hero essentially ignored the irritation caused by those big teeth. They weren't sharp, just awkward."
"Instead, he focused on other parts of her, like her rump.  Copping a feel, the orc let out a snort of amusement, but didn't break off the kiss. This only encouraged her to pull him in closer so she could do the same."
"Rowan used the hand on her backside now to slip up along her back, and into her meager garments to start removing them."
"This did cause the his partner to pull back from him. While worried at first that maybe he'd done something wrong, the orc instead helped him pull her armor off. She tried to start on Rowan's gear after that, though her efforts were mostly fumbling until she started getting frustrated."
"Rather than letting her force them off, the man undid his armor and then pulled off his clothes himself.  As soon as she saw dick, she crashed into Rowan and brought him to the ground."

#Show 69 CG.
scene cg189 with fade
show rowan necklace naked behind cg189
#show female orc behind cg189
pause 3

"With some effort, and fumbling of his own to finally get his pants off, Rowan managed to wrestle himself on top to take the lead again. During the scuffle, the two found themselves face to face with each other's naughty bits in a 69."

femorc "Silly humi, you got us da wrong way round!"

ro "I wouldn't say that..."

"He opened his mouth and ran his tongue over the green pussy in front of him. Following his lead, once again, the orc ran her tongue over his balls and up his hard shaft."

femorc "Dis is different, but fun."

"The man nibbled on her lower lips as he repositioned his hips to push his cock past her upper ones. There was no resistance as he sunk down past her tusks and into her throat. In fact, she was very eager to swallow his length and gave a deep blowjob."
"Bobbing his hips up and down several times and enjoying the sensation immensely, Rowan also put some more effort into teasing and play biting the orc's womanhood. She really liked him being forceful, so he was constantly being a little bit harder, a little rougher."

#Show fucking missionary CG.
scene cg110 with fade
pause 3

"Deciding that was enough foreplay, the human pulled himself fully free and flipped around so he was face to face with the orc woman again. Instinctively he lined up and pushed himself inside her passage in two quick motions. She had said she wanted to be fucked, after all."
"Her cunt was very slick, as well as deeper and wider than a human's. It also felt more flexible and squeezed down on him a bit to make up for being looser. There were other differences, but Rowan was a bit distracted to focus on them."
"He pumped himself in and out of her as quickly as he could, with her moving her hips up to meet him with each thrust. A loud meaty smack accompanied each of these motions, along with grunts of pleasure from both of them."
"This was what orcs were used to; rough hard animalistic fucking.  That didn't stop the man from reaching out and, 'appreciating' her softer assets. As before, as soon as he started fondling her, the orc did the same to him."
"She was especially fond of pulling him down insider faster and harder."

#Show cuming CG.
scene cg110 with sshake
scene cg110 with sshake
scene cg111 with flash
show rowan necklace naked behind cg111
#show female orc behind black

"Rowan didn't even notice that he was approaching his peak, so it surprised him a bit when he came inside the orc. Given the noises she was making and the rippling feeling of her passage, there were unlikely to be any complaints from the woman."

femorc "Hehe, yus was good. Doubt a humi will give me a baby, but letten you have your way with me makes up for it."

ro "Ha, I certainly liked having you under me for the evening. How did foreplay compare to skipping straight to the action?"

femorc "Different. I'm a probly start another contest as soon as is proper if I don't get a baby. Wouldn't mind if you want to try for me again."

ro "Intriguing."

#rowan gains a small amount of corruption
$ change_base_stat('c', 2)
jump campMenu


label courtshipFail:

"Rowan watched the rest of the competition, interested to see how the orcs fared at each of the challenges.  One by one, competitors withdrew as rounds concluded and they realized they were outclassed."
"The runners were the first to declare a winner, who promptly ran off with the woman on the line to claim his prize. After that was the plate balancers.  Unlike the runners, these quit in frustration rather than because they were exhausted."
"Unsurprising for orcs, the contest of strength was still going on when Rowan decided to move on over three hours later. Even when it came to something as mundane as digging a hole, orcs were surprising powerhouses."
"He did notice as he left that the woman who'd been tied up had left at some point during the contest. Presumably someone had let her down, so it wasn't that long of a punishment."
jump campMenu

############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
