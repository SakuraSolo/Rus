init python:

    #Humans are not welcome
    event('humans_are_not_welcome', triggers='orciad_explore', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)
    #Lost Knowledge
    #repeatable
    event('lost_knowledge', triggers='orciad_explore', conditions=("week >= 4",), group='orciad_camp', priority=pr_map_res)
    #Camp Slaves
    event('camp_slaves', triggers='orciad_explore', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)
    #Youth of the Nation
    #Requires the “Orcish Families and Neutrals” event
    event('youth_of_the_nation', triggers='orciad_explore', conditions=("week >= 4",), depends=('orcish_families_and_neutrals',), run_count=1, group='orciad_camp', priority=pr_map_res)
    #The Woods Outside of Camp
    event('the_woods_outside_of_camp', triggers='orciad_explore', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)


label humans_are_not_welcome:
#Humans are not welcome
#"Explore the Camp" event

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve
#female orc

os "Humi, you don't belong here."

"Given that this was an orc camp, it stood to reason that sooner or later someone was going to harass Rowan. Demon protection or no demon protection."

ro "I am here on demon master business and have permission from-"

femorc "Shut it, weak pink!"

"She swung an arm to slap Rowan across the face, but he reflexively jumped back to avoid it."

"If anything, this just made the orcs madder.  Then two more of them came up behind him, cutting off any chance of escape. Evidently there was some planning behind this."

ro "Then let's duel, and settle this like orcs."

os "Yous no orc. Yous has no right to duel."

"The others grumbled their assent. This wasn't looking good. He doubted these bullies wanted to kill him or even seriously injure him, they seemed like they were using him as a scapegoat for something else, maybe a failed raid or frustration over ongoing issues in the camp."
"Rowan considered his options, if worse came to worse he could always recall to the castle. However, that meant time wasted travelling back to the camp if he had further intentions here this week. He could also recall immediately to avoid being injured at all."

#(If no exploration time left)
if avatar.mp < 1:
    "Then again, it wasn't like Rowan could exactly do much more in the camp anyway before he'd have to return to the castle.  The extra few hours he might have wondering the camp were not worth getting beat up now."
    "The hero placed his hands on his necklace, then softly spoke."

    ro "Jezera, recall me to the castle."

    hide rowan with dissolve

    "Then, he vanished."
    return

#else
else:
    menu:
        "Return to the portal.":
            $ released_fix_rollback()
            "It wasn't worth taking any chances. Better an inconvenience than letting a group of orcs beat him up."
            "The hero placed his hands on his necklace, then softly spoke."
            ro "Jezera, recall me to the castle."
            hide rowan with dissolve
            "Then, he vanished."
            #Rowan is placed on the map at the portal nearest the orc camp.
            # TODO: move to the portal
            return

        "Take the beating.":
            $ released_fix_rollback()
            "His work here was too important to flee now. Rowan would have to take the beating and hope that these orcs left him in a functioning state afterwards or he had a chance to escape later."
            "Gritting his teeth, this time Rowan stayed where he was when the orc moved to hit him again, taking the full force of her slap. A grin formed on the orc woman's face, then she punched him in the gut."
            femorc "Owe. Say you want duel, but wearing dat."
            "She'd taken the brunt of the damage from that one, due to his armour. However, now several other orcs were grabbing onto his arms and tearing the armour from his body."
            os "Now we see how good pink skin do against green."
            "Another strike, this one knocked the wind from Rowan's lungs and he doubled over in pain."
            #rowan hurt
            ro "Gha. Damn."
            "Try as he might, he couldn't keep a completely straight face and the jeering orcs around him evidently noticed. Then one of them kicked him."
            femorc "See, humi weak. Humi have no place in dis camp of mighty orcs."
            "With a great force of will, the man forced himself to stand up and face his captors again. This prompted looks of annoyance, but he tried to keep his face neutral in an attempt to be as boring as possible."
            os "Hey, cry! Show us dem weak humi tears!"
            "He punched Rowan in the side of the face, drawing blood. It hurt like hell, but the man had been through worse in Andras's dungeons. He did not cry."
            #Rowan bloodied

            #vitality test (DC12)
            $ event_tmp['vitality_test'] = check_stat(12, 'vitality')
            $ released_fix_rollback()
            if event_tmp['vitality_test'][0]:
                #success
                "They wailed on him for several more minutes, however those watching soon became bored due to his lack of responses. As the audience dwindled, the ones who'd initially approached him quickly lost interest as well."
                hide orc soldier neutral with moveoutright
                #hide female orc with moveoutright
                "At the end, Rowan was bruised and a bit bloody, but standing proud."
                #gain 25 xp and one injury
                $ add_exp(25)
                $ add_effect(MultiEffect('Wound', 'neg', (('strength', -1),), 2))
                jump campMenu
            elif event_tmp['vitality_test'][1] >= 9:
                #partial success (9 or more)
                "Try as he might, eventually Rowan couldn't stay up anymore and collapsed to the ground under the pain. There he lay for several minutes taking their jeering and occasional kicks."
                "Eventually the orcs decided to go and eat or drink something in celebration of having 'dealt' with him."
                hide orc soldier neutral with moveoutright
                #hide female orc with moveoutright
                "The man was just left there, until he managed to pick himself up and clean the blood and dirt from his body. Even when he finally put everything back on and left the scene of his attack, no one approached or spoke to him."
                #rowan gains 10xp and 2 injuries
                $ add_exp(10)
                $ add_effect(MultiEffect('Wound', 'neg', (('strength', -1), ('vitality', -1)), 3))
                jump campMenu

            #fail
            else:
                "The onslaught kept coming and coming.  Somewhere along the line he'd fallen to the ground, but that didn't stop the orcs from continuing to beat him again and again."
                scene black with fade
                "Stars filled his vision as he felt what was surely a bone crunch under the boot of the orc woman who'd struck him first."
                "No, this was too much.  Rowan had to escape, desperately he tried to crawl away for a moment to the delight of his tormentors before remembering the amulet."
                "Then he was back in the castle, being carried by the castle staff up to his room to recover from the ordeal.  This week's exploration was at its end."
                #rowan gains 2 injuries, end week
                $ add_effect(MultiEffect('Wound', 'neg', (('strength', -1), ('vitality', -1)), 3))
                return

############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label lost_knowledge:
#Lost Knowledge
#"Explore the Camp" event
#repeatable

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade

"Rowan set out to examine the loot tent. It was the grandest and most imposing of the tents in camp, guarded at all times by no less than 10 orcs."
"When he approached the entrance, the guards up front had a spirited debate on whether they should kill him for approaching, or torture and then kill him for approaching."
"The chief of the loot camp guards, however, was willing to let Rowan in provided he touched nothing."
"Inside the tent, vast piles of gold, jewels, and commodities of all shapes and sizes were thrown together in seemingly random piles. To a normal man, it would be enough wealth to last a lifetime. But, Rowan could tell that for all the splendor in front of him, it wasn’t enough."
"Orcs are not harvesters or craftsman, but raiders. Their day to day survival depends on taking enough to trade for life needs. A hoard of this size could keep a tribe of this size fed for a few months at most."
"Rowan noticed an entrance to a smaller tent in the back. Here, a vast assortment of junk was strewn about. It was all trinkets and mostly worthless objects that had been collected during a raid to be sorted for value later. Much less attention was paid here then the main tent."
"Rowan stalked among the stacks, examining what they found. Orcs had no need for cutlery sets, brick making tools, or mementos. However, in one of piles he found a book with rotting pages."
"From a glance, he doubted that there were any copies back in the library of Bloodmeen. It could be useful for research purposes."
"Rowan reached out to grab the book. However, one of the guards was watching. The guard approached him, furrowing his unibrow."

#diplomacy check (dc15)
if check_skill(15, 'diplomacy')[0]:
    #success
    "Rowan disarmed the guard by explaining how worthless the book was. The guard was forced to agree, considering this was the junk tent. The guard still didn’t want Rowan to touch anything else, forcing him to swear to only take the one book. "
    "That was enough, however. While knowledge was not considered very valuable in an orc camp, in the hands of his masters it could prove a valuable weapon."
    #gain 2 research points
    $ castle.rp += 2
    jump campMenu

#fail
else:
    "Rowan attempted to explain how pointless the book was to a bunch of orcs, but all he managed to do was offend the guard. The guard captain had to intervene to prevent an attack on Rowan."
    "However, any chance of bringing the book back with him was lost at this point. Rowan had to leave the book and promise not to come back until the guard changed to even return to the tent."
    jump campMenu

############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label camp_slaves:
#Camp Slaves
#"Explore the Camp" event

scene bg26 with fade

$ change_mp(-5)
$ prevent_tile_exploration()

"This tribe didn’t place its slaves in any kind of tent. Instead, captive humans were taken to a series of caves at the base of a hillside on the north side of camp. There they were guarded day and night."
"Orcs of both gender came and went from the caves, free to use the captives for their own pleasure."
"When Rowan explored this area, he had to be careful. With their blood up, one of the orcs might have gone for him. Killing a member of the tribe wasn’t how to conduct effective diplomacy. The sounds of screams rung throughout the caves."
"Some from pleasure, some less so. It was overpowering."
"A voice called out to him from behind a set of thick steel bars. A beat up middle aged man called to him, wanting to speak. Rowan took great care not to be seen by the guards. The captive was part of a group of slaves who were planning an escape."
"They’d been building a tunnel for the past month to help their escape. Last night, their guard had taunted them with the fact that they were to be sold in the morning. Orcs sold captives to human slavers and other darker creatures."
"They needed to use their tunnel now."
"But, it wasn’t ready yet. The tunnel only emerged thirty feet behind the camp’s walls. They would need to get through the gate somehow. They needed Rowan’s help."

menu:
    "Tell the guards.":
        $ released_fix_rollback()
        "Rowan promised the man he would help. But, Rowan wasn’t here to rescue human captives. He was here to forge an alliance with the orc tribe. An hour later, Rowan approached the head guard and explained the slaves’ plan."
        "At first he was ignored, but when the guard searched the cell, he found a massive tunnel that extended most of the way out of the camp."
        "That night, the captives who had attempted to escape were flogged. To reward Rowan’s service, the tribe offered a gold gift to the Treasury."
        #Gain treasury gold and guilt
        $ change_treasury(15)
        $ change_base_stat('g', 2)
        $ orciad_betray_the_slaves = True
        jump campMenu

    "Help the slaves.":
        $ released_fix_rollback()
        "Rowan promised the man he would help. He instructed the man to wait for a signal from him, and to go later that night. Rowan would handle the door. Some of the other slaves came to the bars of the cage, reaching out to touch his hand."
        "This was going to be risky, but he couldn’t leave these people to an unknown fate. He’d already sold so much of his soul."
        "That night, he walked past the bars, and flashed a hand gesture. Afterwards he slowly made his way to the north gate. Most of the guards were on the camp walls. The orcs didn’t expect an attack from within."
        "Only one orc was stationed near the wheel that opened the gate. Though he was a big one. If he took too long dispatching the guard, then it could alert the others."
        "Rowan unsheathed his blade and quietly snuck up on him."
        #reflexes check (DC12)
        if check_stat(12, 'reflexes')[0]:
            #Success
            "Rowan snuck closer to the orc, staying in the shadows. The orc was sitting in a chair trying to keep awake. With senses dulled by sleepiness, Rowan doubted that he’d see him coming."
            "Still, he had to plan each step to ensure he didn’t make a stray sound. Getting closer, closer, closer."
            "Rowan readied his blade and moved in for the kill. It took one quick slash to the throat. The orc didn’t even know what hit him. He silently toppled back, rattling his last gurgled breaths."
            "In the shadows, Rowan saw other figures approaching. He didn’t relax until they were close enough to confirm. The captives had made it. Rowan quietly opened the gate just a crack to let the humans through."
            "In the morning, the orcs found the dead guard near the gate. An investigation of the slave’s quarters revealed the escape tunnel. Nobody ever suspected that Rowan had been the one to free them. One less weight for his conscious. "
            #lose guilt
            $ change_base_stat('g', -2)
            jump campMenu

        #fail
        else:
            "Rowan snuck closer to the orc, staying in the shadows. The orc was sitting in a chair trying to keep awake. With senses dulled by sleepiness, Rowan doubted that he’d see him coming."
            "Still, he had to plan each step to ensure he didn’t make a stray sound. Getting closer, closer, closer."
            "Rowan readied his blade and moved in for the kill. It was an especially bad time to step on a stray twig. So of course, he stepped on a twig. The guard shot awake, grabbing his blade. Rowan’s cover was lost."
            "Rowan lunged forward, striking at the guard. The captives would be arriving any second now. If they made it through quickly, there was still a chance of success. The orc guard threw a few wild swings, all missing."
            "One opened his guard enough for Rowan to close the distance and finish him."
            "There was shouting and running on the ramparts. The guards were aware something was wrong. It was thankful that at that moment, the captives arrived. Rowan opened the gate, allowing them to flee from the camp."
            "Meanwhile, Rowan made his own escape. The guards missed him by mere moments."
            "Thankfully, none of the captives were ever found. However, for the first few days there was a persistent rumor that Rowan had a part in the escape. He was the only free human in the camp."
            "To avoid causing a further stir, Rowan decided he needed to make himself scarce for the rest of the week."
            #lose guilt. Rowan can’t go the camp for a week.
            $ change_base_stat('g', -2)
            # TODO: forbid access
            return

############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label youth_of_the_nation:
#Youth of the Nation
#"Explore the Camp" event
#Requires the “Orcish Families and Neutrals” event

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg3 with fade
show rowan necklace neutral behind bg3

"Rowan returned to gathering place of the nursing females and families. He spent part of the morning speaking to some. When walking back to the rest of the camp, he noticed one young orc by the river stream."
"This young one was unusually scrawny for his age. Surprisingly, he had a book in his hand. Rowan had never seen a young orc reading before. Rowan approached the orc youth. His name was Eidood"

ro "Where did you find that?"

eid "One of human slaves. Me wanted to see pictures."

"Eidood pointed to the document. It appeared to be an illuminated manuscript. The right side of each page had a watercolor picture, while the left side had dense text about a region’s history."

eid "What that?"

ro "That’s a windmill. It's what humans use to crush grain so we can eat it."

"Eidood turned to another page. This one depicted a knight on horseback charging a unit of men-at-arms. The young orc stared at the picture."

eid "Who metal man?"

ro "That’s a knight. They’re humans who wear metal armour in battle."

eid "Armour? Why?"

ro "It blocks weapon attacks, so it makes you harder to kill. Knights are sworn to protect their people, so they need stronger weapons and armour."

"Eidood seemed confused by that. There were oaths in orcish society, but nothing as intricate or complex as a feudal relationship."

ro "The peasants, the knight’s tribe, give the knight food and treasure. The knight raises strong sons and buys powerful armour. That way the Knights protect the tribe. Knights are some of the humans' mightiest warriors."

eid "Knights be strong?"

ro "Very."

"That seemed to get through to Eidood. The Orc youth opened his jaw in awe and traced the image of the knight on horseback with his finger. Of course, Rowan had known many knights before, and few lived up to the heroic ideal etched into the manuscript."
"Still, the idea was fascinating. Could an orc learn chivalry?"

eid "Could Eidood be knight?"

ro "I’ve never met an orc knight before. It would be a strange sight."

eid "Eidood will be first orc knight then. Knights powerful. Orcs powerful. Orc Knight most powerful!"
eid "Orc knight Eidood bring glory to tribe. Burn many villages. Make enemies scream in terror. Strongest there is."

"Eidood grabbed the page with the knight, roughly tearing it out of the book. He stood up, letting the rest of the book topple off his lap. He’d shown it so much concern before, compared to how a normal orc would treat it."
"Rowan sighed. It seemed the answer was no. He picked up the manuscript from the ground. Even damaged it might still be worth something."
"Later, Rowan walked passed the fighting pit where the orcs on the cusp of manhood practiced. There was a loud commotion today. One of the fighters was doing something quite unusual. Rowan went over to watch. He found Eidood fighting one of the other orc youths."
"Only, Eidood was wearing a very primitive set of armor, misshapenly fashioned from wooden bark. Yet, it made the difference. Eidood overcame his opponent by taking a few stray blows from his club using the armor. None of the spectators knew how to react."
"The orcs valued victory, but found little glory in being armored. And Rowan? Rowan wasn’t sure if he should be proud or scared."

#gain 10 personal gold
$ change_personal_gold(10)
jump campMenu

############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_woods_outside_of_camp:
#The Woods Outside of Camp
#"Explore the Camp" event

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg3 with fade

"Rowan explored of the camp this time. He found a small forest just beyond the gate. A strange patch of green tranquility within earshot of the feasting and fighting of the orcs. He chose this opportunity to sit and rest."
"At the base of a tree, he spotted a set of old bones. By now they were broken chunks that memorialized some long dead orc warrior. A close examination of the tree itself revealed heavily faded pictograms."
"They had been carved into the wood so dissonantly in the past that they had become a whisper in the wood. Easily missed by an untrained eye."
"The picograms depicted an orc of unusual size and strength, as representative by how he towered over the others, engaging in feats of strength. Killing enemies, taking women, collecting treasure for his loot box."
"The final picture showed him bleeding surrounded by trees. No doubt much of it was false. It was a dying orc telling his own story. But, wat drew Rowan’s eye was what he included in the final picture."
"The symbol for a hidden cache."
"Rowan dug up the ground next to the bones. His curiosity was rewarded. Beneath the bones lay a rotted box, and inside the remnants of the orc’s treasure."
"It wasn’t the great sum the pictographs suggested, but what pieces hadn’t been rusted could be resold at a profit."
"The real challenge of the day proved hiding this sum of treasure from the prying eyes of his orc hosts."

#gain 25 personal gold
$ change_personal_gold(25)
jump campMenu
