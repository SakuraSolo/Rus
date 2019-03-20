init python:

    #first visit to Batri in orciad camp
    event('first_visit_batri', triggers='orciad_batri', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)
    #repeat visit (if Rowan failed diplomacy check and he has not yet met Batri)
    event('visitBatri_repeat', triggers='orciad_batri', conditions=("week >= 4", 'rowan_met_batri=="repeat visit"'), depends=('first_visit_batri',), group='orciad_camp', priority=pr_map_res)
    #Repeat meetings with Batri
    #The following event occurs if Rowan returns to see Batri after meeting him the first time, and has not completed Batri's path
    # TODO: check for completion
    event('repeat_meetings_with_batri', triggers='orciad_batri', conditions=("week >= 4", 'rowan_met_batri=="met"'), depends=('first_visit_batri',),
        group='orciad_camp', priority=pr_map_res)
    event('delane_corruption_week1', triggers="week_end", conditions=("delane_corruption", 'week >=4'), group='ruler_event', run_count=1, priority=pr_story)
    event('delane_corruption_week2', triggers="week_end", conditions=("delane_corruption", 'week >=4'), depends=("delane_corruption_week1",), group='ruler_event', run_count=1, priority=pr_story)
    


#visit batri
label first_visit_batri:

#first visit
scene bg26 with fade
$ rowan_met_batri = 'repeat visit'

"Rowan walked through the camp and crossed into Batri's side.  He could tell right away that the orcs living in this area were for the most part younger than the others, fewer scars and lower quality gear."
"However, their equipment tended to be newer or more recently acquired.  Most of them were failing to care for their weapons or armor properly and he saw many pieces covered in rust, but these younger orcs were actively raiding, unlike the slightly larger camp under Ulcro."

show wild orc neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

wo "Hey! What you doing here humi?"

ro "I'm here to speak with Batri."

wo "Why would Batri want to talk to Demon cock-sucking humi?"

if check_skill(15, 'diplomacy')[0]:
    ro " Batri is skilled, Batri's boys raid many shiny strong weapons. My boss likes orcs that fight well and wants to give you lots of enemies to fight, treasures to earn, and slaves to fuck."
    wo "Hmm, dat sounds good."
    ro "We have an interest in seeing this little matter between Ulcro and Batri resolved, so you have more time for raiding and can maybe join my master's armies."
    wo "Den you do have reason to talk to Batri. Dis way."
    #Rowan can now encounter Batri's raiders while exploring the camp, in case the player wants to join a raid anyway.
    $ rowan_can_encounter_batri_s_raiders = True
    jump batriFirstMeeting

else:
    ro "My boss has an interest in seeing this matter between Ulcro and Batri resolved. So I need to talk to your boss."
    wo "Fah, Batri has no time for cock-suckers. Prove you tough warrior like orcs. Help us in raid, bring treasure, den maybe he talk to you."
    #Rowan can now encounter Batri's raiders while exploring the camp.
    #Add orciad note2 to journal.
    $ rowan_can_encounter_batri_s_raiders = True
    $ journal.add_quest_note('orciad', 'note2')
    jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label visitBatri_repeat:
#repeat visit (if Rowan failed diplomacy check and he has not yet met Batri)
scene bg26 with fade
show wild orc neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

#If Rowan has not yet joined Batri's raiders.
if not rowan_joined_batri_s_raiders:
    wo "Demon cock-sucker is back, maybe he got cum in ears too."
    wo "Batri has no time for cock-suckers. Prove you tough warrior like orcs. Help us in raid, bring treasure, den maybe he talk to you."
    jump campMenu
else:
#If Rowan has joined Batri's raiders
    wo "Well, orc raiders say dat demon's humi good fighter. Batri likes good fighters, dis way."
    jump batriFirstMeeting

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


#Batri first meeting
label batriFirstMeeting:

$ journal.complete_quest_note('orciad', 'note2')


scene bg30 with fade
show batri neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

"Rowan stepped inside the orc tent and saw Batri for the first time. The orc was big, very big. In fact, Rowan wouldn't be surprised if he was the tallest and strongest of the orcs in the entire camp."
"Batri looked over at the new arrival, then turned to face him fully to size up the human. Rowan did the same, observing how the orc moved with confidence and something approaching grace. He was adorned in looted Rosarian plate armor that had been torn apart and strapped over his large form."
"Like most of his men, Batri wasn't in the habit of maintaining his equipment. However, the very fact that he was wearing those plates at all and the way he carried himself spoke volumes about his fighting capability."
"There were some scars on his body, but fewer than most orcs at even his young age."

bat "So, you be da demon's lapdog. My boys been talking bout'you."

ro "Yes, we're looking for true orcish warriors to join Bloodmeen once again."

"The orc eyed him for a moment, then sat in a fancy chair that had no doubt been looted from a noble's keep."

bat "Well, know dat I been wronged by da false warchief Ulcro. By right, any orc can challenge da warchief for da right to rule. Ulcro has refused every challenge after he took booty that was mine."

ro "Yes, I've heard about the human woman you... acquired on a raid."

"A hoarse laugh erupted from Batri's throat."

bat "Not just any humi, beautiful noble humi. Warchief have right to take spoils, but warchief should know bettar dan to take favorite loot. I can't join your boss demon unless Ulcro fight me."
bat "I know how to get him, he obsessed with humi now. He hides her and pampers her like noble instead of proper fucktoy. Help my boys get her back, den Ulcro have to accept challenge."

ro "I assume that's where I come in?"

bat "Yeah, you be good at finding stuff? Den find my booty. She not in Ulcro's main tents, somewhere else in his camp. Look, find, come back."

ro "Alright. Good meeting you, great warrior Batri."

"The big young orc nodded and Rowan took his leave."

#Add Orciad note4 to journal
$ journal.add_quest_note('orciad', 'note4')
$ journal.add_quest_note('orciad', 'note8')

if castle.buildings['forge'].lvl >= 1:
    $ journal.add_quest_note('orciad', 'note9')

#grey out visit batri option for now, until later release
$ rowan_met_batri = 'met'
$ ghBatriHelp = "get"
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label repeat_meetings_with_batri:
#Repeat meetings with Batri
#The following event occurs if Rowan returns to see Batri after meeting him the first time, and has not completed Batri's path

if batri_power > 10:
    $ journal.complete_quest_note('orciad', 'note8')
    $ journal.complete_quest_note('orciad', 'note9')

scene bg30 with fade
show rowan necklace neutral at midleft with dissolve
show batri neutral at cliohnaright with dissolve

ro "Hello Batri."

bat "Ah, da lapdog comes back."

#If Rowan has not yet met with Lady Delane
if not met_with_delane:
    bat "Have yus found da lady yet?"
    ro "Not yet, I'm still looking for her."

    #If Batri is strong enough to attack Delane's prison.
    if batri_power > 10:
        bat "Hurry it up! We strong enough to take 'er and I wanna bash dat bastard Ulcro in."

else:
    #If Batri is not yet strong enough to attack Delane's prison.
    if batri_power <= 10:
        bat "Don forget, still need more power here. Can't take Lady yet, do more raids and get more a Ulcro's boys to join me."

    elif batri_power > 10 and delane_corrupt == False:
        bat "Stop tellin me to hold. Ya know where da girl is. We too strong for weak chief Ulcro to stop. Finish corruptin' da bitch so we can take ‘er soon."
        
        
    #If Rowan has met Delane and Batri is strong enough to attack.
    else:
        bat "Everyding iz ready here. Show my boyz where da lady is and we can do dis."
        menu:
            "Yes, let’s get her.":
                $ released_fix_rollback()
                jump delaneRecapture
                
            "No, I’m not ready yet.":
                $ released_fix_rollback()
                ro "I’m not ready yet. The moment we capture her, everything will explode. I want to be ready for that moment."
                bat "Bah. Wasting time. Must move. Hit fast. Attack."
                ro "Soon. We’ll move soon."
                bat "Hrmph. Need be sooner. Faster."
                            

#rejoin
bat "We has nothing more to talk about. Yus not getting any help from me until I gets my booty back."
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label corrupt_delane:
#if the player has met delane and batri, a new option should appear on the camp menu "Corrupt Delane (Requires available spy)"
#if the player meets all criteria, clicking it and assigning a spy should trigger the corruption path, starting with this event

"Rowan went over his list of spies in his head. Now that he had Delane’s location, it wouldn’t be that hard to bring her back into Batri’s possession, should he desire to do so. But, the operation would be far simpler with a willing Delane."
"Perhaps she might be taught to enjoy the prospect of the things that Batri would do to her..."

if avatar.corruption < 30:
    
    "The idea was abhorrent to him conceptually. It involved corrupting a kind enough member of nobility into nothing but an orc slut. But, he’d seen enough by now to know that it was doable. And the prospect of an alliance with Batri was too valuable not to consider."
    
elif (avatar.corruption > 29, avatar.corruption < 60):
    
    "Rowan shrugged. He saw little wrong with the idea of corrupting Delane into an orc slut per say. After all, she was a captive at an orc camp, why should she deserve any special treatment? Still, was he not still a hero? Was a hero supposed to do such things?"
    "But, Batri would be a powerful ally, and like it or not he needed powerful allies."
    
else:
    "Rowan almost smirked before he stopped himself. The mental image of an incubus bending over and teaching that haughty noble woman her place was certainly amusing. And such an option brought to bear the prospect of an alliance with Batri. A brutal creature but a useful one."
    
"Still, even considering the option bore risks. If he sent an incubus to corrupt her, then he likely wouldn’t be able to side with Ulcro, nor would Tarish be especially happy with using his own espionage network for his own ends. Choosing this meant choosing Batri."

"Should Rowan send a spy to corrupt Delane? (This locks off all other paths)"

menu:
        
    "Yes.":
        $ released_fix_rollback()
        $ menu_res = renpy.display_menu([(spy.name, spy.uid) for spy in get_spies('idle')])
        $ tmp_spy = get_object(menu_res)
        $ tmp_spy.mission = OrciadInfiltrate().create_sm(tmp_spy, loc=(world.cur_map.uid, tuple(world.cur_map.pos)), started=week)
        $ msgs.show('{{color=#C6FE56}}New spy mission ({}):\n "{}" at {} (dur. {}){{/color}}'.format(tmp_spy.name, tmp_spy.mission.label,
        ' '.join((str(world.cur_map.uid), str(tuple(world.cur_map.pos)))), tmp_spy.mission.duration))
        $ delane_corruption = True
        $ journal.complete_quest_note('orciad', 'note11')
        $ journal.add_quest_note('orciad', 'note12')
        jump corrupt_yes

    "No.":
        $ released_fix_rollback()
        #return to menu
        #if player chooses option again, after assigning spy, jump to the next part "corrupt_yes" of the event
        jump campMenu

label corrupt_yes:

"Rowan sent word to [tmp_spy.name] of the mission, along with Delane’s location. With that out of the way, it was merely a matter of making sure that Batri had the power position to take on Ulcro."

if avatar.corruption < 30:
    "Rowan’s hand trembled slightly. Was he really doing the right thing?"
    
else:
    pass

#spy chosen earlier is unavailable for 4 weeks
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Delane corruption - week 1
label delane_corruption_week1:

$ delane_corruption_occurred = True

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

if week > 20:
    show liurial neutral at midright with dissolve
    "Rowan was sitting at his desk doing a recount of acquired provisions for the week when [tmp_spy.name] returned to report on his/her success for the week."
    "Seeing her bosses’ visitor, Liurial rose to her feet and walked out of the room steadily. She well knew by now that such matters were above her pay grade."
    hide liurial with moveoutright

else:
   "Rowan was sitting at his desk doing a recount of acquired provisions for the week when [tmp_spy.name] returned to report on their success for the week."
   
"[tmp_spy.name] proceeded to recount the events of the past week. Disguised as an Orc guard, they made regular trips to visit Delane as the week wore on. While there, the spy wove seductive magic designed to help slip down her resistance."
"At first Delane barely wanted to speak to them. However, after a few charms and lots of boredom, Delane cracked and proved willing to engage in conversation here and there."
"She remained hesitant to so much as discuss sex, of course. But, the demon optimistically noted that there was already a seed of curiosity in her regarding her captors and her sexuality." 
"With a few well placed suggestions, some drugs, and a well staged sexual show, Delane was almost certainly more inclined to think erotic thoughts. A curse designed to keep her dreams on the subject was always a throw of the dice, but the spy believed it would be successful."
"Rowan shooed [tmp_spy.name] away when the report was done, and returned to his papers. It seemed that the plan was well on its way."

if avatar.corruption < 59:
    "..Though even as he went back to the papers, the pit in his gut just wouldn’t subside. Just what was he doing to this poor girl?"
    
else:
    "...Though even as he went back to the papers, he started to smile. There was something oddly thrilling about the entire thing. He awaited (spy name)’s next report eagerly."  

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Delane corruption - week 2

label delane_corruption_week2:
    
scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

if week > 20:
    show liurial neutral at midright with dissolve
    
else:
    pass
    
"Once more as Rowan was working keeping the army from breaking down at the seams, he was interrupted by [tmp_spy.name] returning from their mission to corrupt Delane."

if week > 20:
    "Liurial once more rose to leave the moment [tmp_spy.name] entered. However, this time, Rowan told her to stay. For better or for worse, he trusted Liurial. Or at least trusted Liurial as far as the war effort was concerned at least."

else:
    pass

"[tmp_spy.name] once more began to regail the tale of their efforts to turn Delane into a slut. Once more, it had gone well."
"Where at the beginning of the week, Delane had been hesitant to discuss her sexuality, as the week had progressed it had turned into her favorite topic of conversation. She was still shy of course, embarrassed to admit her attraction to orc cock. But, it was clearly on her mind constantly."
"On three occasions throughout the week, the spy had arranged little shows for her. Twice two orcs engaged in rough coitus at an angle that Delane could view. The third was something a bit more relevant, a female human slave girl being used by her orc master while screaming in pleasure."
"[tmp_spy.name] had been on hand on all three occasions. Each, especially the last, had their intended effect on her."
"Indeed, [tmp_spy.name] was even able to report that seemingly each night she had begun masturbating herself to sleep. She tried to muffle the sound with a blanket that Ulcro had given her, but there was no hiding matters."

if week > 20:
    show liurial aroused at midright with dissolve
    "As Liurial worked, she was pretending not to listen to the report. But, Rowan could not be fooled quite so easily. The blush on her cheeks gave away that she was very interested indeed by the matter of what they were doing to Lady Delane." 
    "Perhaps he’d have to attend to that interest after [tmp_spy.name] left..."

else:
    pass

"When the report finished, Rowan thanked [tmp_spy.name] and bid them on thier way. Delane was another step closer to corruption. At the current pace, it was almost certain that she’d be ready for Batri by the end of next week…"

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Delane corruption - week 3    
label delane_corruption_week3(tmp_spy):

$ journal.complete_quest_note('orciad', 'note12')
$ journal.add_quest_note('orciad', 'note13')


scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

if week > 20:
    show liurial neutral at midright with dissolve
    
else:
    pass

"This time when [tmp_spy.name] walked through the doors, Rowan could hardly be surprised. He looked up from his documents and asked for news of Delane, eager for anything at all to distract him from the tedium."

if week > 20:
    "Liurial didn’t budge from her seat this time. Instead, she leaned forward, eager to hear the latest details of Lady Delane’s conversion into a slut."
    
else:
    pass
    
"[tmp_spy.name] eagerly reported that the mission had been a complete success. Near the beginning of the week, they had decided that the lady was far enough along to put her newly awakened libido to the test."

#cg1
scene black with fade

"The demon had come to her in the middle of the night in the usual orc form. Delane had not complained about the presence of this nocturnal visitor. In fact, her cheeks had flushed and she showed every sign of eagerness."
"Still, for the sake of her modesty, she’d offered token protestations to the idea of something more. And yet, when [tmp_spy.name] had stripped down and revealed the bulging orc cock, there was no mistaking the look in Lady Delane’s eyes."
"[tmp_spy.name] said that she wanted it. She needed it." 
"Thus, it only took a token effort to get the noblewoman to sink down to her knees, kissing and lavishing the giant green cock in front of her. [tmp_spy.name] took great delight in describing the eagerness of her licks and her shallow panting."
"But, the goal was not to make her suck a cock. No. In her lust-bound state, it wasn’t a challenge to get her to accept being rolled up on her back and having her legs spread. She had even been begging for it, pleading for the great big orc member to enter her."

if week > 20:
    "By this point, not only had Liurial’s cheeks turned pink, but her own breath had grown shallow. She followed every word of [tmp_spy.name]’s report as though being led by leash."
    
else:
    pass

"The description that followed was the juicy part. Once [tmp_spy.name] had her on her back, the spy spared no time filling her over and over again. Lady Eleanor even had to put her hands over her mouth so she wouldn’t scream so loud she’d wake anybody."
"Pent up from weeks of [tmp_spy.name]’s teasing, and perhaps more than a little curiosity from merely living among such sexual creatures, Lady Eleanor had been an eager, if not entirely experienced, partner. Gasping and moaning and bucking through the entire process."
"By the time that [tmp_spy.name] was done with her, and she was left panting and spilling orc seed, the process had reached its zenith. The following days had been merely repetitions of the process. By this morning, she would salivate at the mere sight of orc cock."
"She would be ready for Batri if need be."

scene bg6 with fade
show rowan necklace aroused at midleft with dissolve

if week > 20:
    show liurial aroused at midright with dissolve
    
else:
    pass
    
"[tmp_spy.name] finished the report and gave a short bow, as though they had just finished a great performance. It left Rowan without much left to say besides a thank you to [tmp_spy.name] for a job well done."

if week > 20:
    "[tmp_spy.name] departed, more than satisfied,  giving Rowan one last wink. When the spy was gone, the room was left with a lingering silence, broken only by the occasional clicking of Liurial’s pencil."
    
    if avatar.corruption < 30:
        "Click. Click. Click. His mind ran with confusion over what he’d just done. This was one of the people that Solania had chosen as a noble of the realm. Yes, he’d accepted the need to work for the twins, but there was something dirty about this. Almost sacrilegious."
        "He looked over to Liurial’s blush though, and was once more reminded by the way she got turned on by the story. Even the mere thought was the basis of...stirrings."
        
    elif (avatar.corruption > 29, avatar.corruption < 60):
        "Rowan leaned back in his chair. Part of him was still quite guilty about what he’d done. He didn’t have to like it what he’d done. Afterall, the idea of so actively despoiling a noble went against everything he once believed."
        "And yet, it was necessary. An alliance with Batri was the only way. The only way at all."
        "His eyes caught sight of Liurial at her desk. The signs of arousal were obvious all over her body, from her shallower breath to red cheeks. His cock stirred lightly. He didn’t have to like what he’d done. But, he did."
        
    else:
        "When Rowan leaned back in his chair, he had a smile on his face. In all of his years fighting for Rosaria, he’d never even imagined he’d one day be turning its nobility into orc sluts."
        "Every time he thought of Lady Delane, he remembered every ineffeciency, injustice, and evil that the nobles he’d known had ever committed."
        "Perhaps the world might be a better place if their daughters learned what Lady Delane had."              
        "His eyes caught sight of Liurial at her desk. The signs of arousal were obvious all over her body, from her shallower breath to red cheeks. His cock stirred lightly and a grin spread to his face. It seemed he wasn’t the only one who had been touched by (Spy Name)’s story."

    menu:
        "Take advantage of her.":
            $ released_fix_rollback()
            jump liurialBatriSex
            
        "Leave her be.":
            $ released_fix_rollback()
            "No, he had too much work to do today."
            "Ignoring the elf's obvious arousal, he returned to the work at hand."
            $ delane_corruption = False
            $ delane_corrupt = True
            $ change_base_stat('c', 5)
            return
    
    
    label liurialBatriSex:
    
    $ liurialSex = True
    
    ro "Liurial. Come here."
    
    "The elf kept her head down, but motioned to obey him, padding over to his desk. Indeed, she didn’t even offer resistance when Rowan grabbed her and pulled her up on to his desk. Instead she squeaked loudly, and obediently spread her legs for him."
    
    ro "Did you enjoy hearing [tmp_spy.name]’s story?"
    
    liur "Yes Lord Rowan. It was quite…" 
    
    ro "Quite what?"
    
    liur "Quite evocative. It leaves one only able to imagine what you will do to the nobles of other regions once you arrive there."
    
    "Her hair fell over her face slightly. They obscured eyes that burned...burned with something. Was is lust? Was is sadism and vengeance? Perhaps a bit of both?"
    
    ro "Perhaps you should be more concerned about what I’m going to do with other people."
    ro "Like you."
    ro "Right now."
    
    "His breath grew shorter. More ragged. The distance between the two seemed to grow shorter and shorter with each passing moment. His lips nearly at her neck now."
    
    liur "Why, Lord Rowan? The answer to that is the same as always."
    liur "Whatever you want."
    
    #CG2
    scene cg213 with fade
    show rowan necklace aroused behind cg213
    show liurial aroused behind cg213
    pause 3
    
    "There was no need for any more complex courtship then that. In seconds, Liurial’s underthings had been shoved aside and Rowan’s breeches opened. Now there was nothing preventing him from slowly driving his cock into her."
    
    liur "Oh. Oh…"
    
    "She rolled her head back and groaned loudly into the air. In the process, her head piece fell from her head, letting her long golden hair splay freely backwards over Rowan’s desk." 
    "What followed was the rolling of hips, the press of body to body. His fingers seemed to dig tighter and tighter into her waist every time he rammed his hard cock into her body. His eyes became focused, carnal."
    "It was as though all of the lust, all of the guilt, all of the confusion over what he’d done to Lady Eleanor slammed into her with each thrust of his hips. It energized him, and gave him the roughness of an animal letting off steam." 
    "Perhaps, even if for a small moment, in his eyes she was Lady Delane. Her golden hair was black. Her lithe elven body supple and human. But, only for a moment."

    liur "Oh fuck...Rowan...You’ve never been…"
    
    "Papers went flying everywhere in the passion of the moment. He could feel the sweat from his brow. The hard grunts leaving his lips every time he moved inside of her. Of course, more than anything, he could feel the wonderful tightness of her insides pressing against him."
    
    liur "Fuck. Please. Oh fuck."
    
    "She was gasping now. The throes of passion were apparent in every movement. The shivering, the gasping, the shaking. Her back arched and her toes curled. The wetness of her body made her so easy to fuck, so easy to use this way."
    
    liur " I’m about to...I’m going to…"
    
    "Rowan felt a spasm. And then another. Liurial’s body went from wild thrusting and humping to almost rigid and shaking violently. In the process, her cunt squeezed down oh so powerfully. It was more than a man could stand."
    "Within moments, he too felt a high go through his body, and his cock let loose a wave deep into her."

    scene bg6 with fade
    show rowan necklace aroused at midleft with dissolve
    show liurial aroused at midright with dissolve
    
    "Rowan staggered backward into his chair, looked up with exhaustion at the blonde elf, spasming and dripping cum from the desk. What a mess. This might take an hour to clean up before they could get back to work."
    
    if avatar.corruption > 59:
        "Rowan closed his eyes. Perhaps a little clearer of mind, his thoughts returned to the orc camp, and the Rosarian noble woman who he doomed to a life servicing orc cock that dwelled within." 
        "A stray idea ran through his head. If he ever got a chance to do this again, maybe he shouldn't give the job to one of his spies."

    else:
        "Rowan closed his eyes. Once more clear of head, his mind turned back to Delane one final time for the moment. He wondered, ever so briefly, if she would be happy as an orc slut. Would she find that meaningful?"
        "Rowan hoped so."
    
else:
    "[tmp_spy.name] departed, more than satisfied,  giving Rowan one last wink. When the demon left, the room was left with a lingering silence."

$ delane_corruption = False
$ delane_corrupt = True
$ change_base_stat('c', 5)
$ journal.complete_quest_note('orciad', 'note14')
$ journal.complete_quest_note('orciad', 'note15')
$ journal.complete_quest_note('orciad', 'note16')
$ journal.complete_quest_note('orciad', 'note17')
$ journal.complete_quest_note('orciad', 'note18')
$ journal.complete_quest_note('orciad', 'note19')
$ journal.complete_quest_note('orciad', 'note20')
$ journal.complete_quest_note('orciad', 'note21')
$ journal.complete_quest_note('orciad', 'note22')
$ journal.complete_quest_note('orciad', 'note23')
$ journal.complete_quest_note('orciad', 'note24')
$ journal.complete_quest_note('orciad', 'note25')
$ journal.complete_quest_note('orciad', 'note29')
$ journal.complete_quest_note('orciad', 'note30')
$ journal.complete_quest_note('orciad', 'note31')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label delaneRecapture:

$ journal.complete_quest_note('orciad', 'note13')

ro "I think I’m ready now. I can show your men where Ulcro is hiding Lady Delane...Chief Batri."

"Batri couldn’t help smiling at that."

bat "No. Not chief yet, pink one. But, soon. Bring er bring. Bring de human."

scene bg26 with fade

"When Rowan left the tent, it was already nighttime. With no torches, the majority of the light came from the scattered campfires. As he moved, orcs started to follow along behind him one at a time."
"He was only flanked by a pair on either side, but more than twenty or thirty must have been following him in a matter of minutes."
"Caught unaware as they were, Ulcro’s guards were still able to recognize that a fight was coming to them. At the sight of Rowan’s approach, a few brandished their weapons and made a move towards him."
"He was still aided by the other orcs Batri had sent with him, but this was going to be a fight. One of Ulcro’s men came at Rowan brandishing a large cleaver. Rowan ducked out of the way and lunged low to slice his tendons. One swift strike later, the orc toppled over, no longer able to support his weight."

if check_combat(10)[0]:
    pass
    
else:
    "It would have been a successful effort...if not for the fact that a moment after Rowan noticed a sharp pain in his side. He was bleeding. His attacker had managed to knick his side with the cleaver in the first swing. Rowan grimaced. That might take a bit to recover."
    $ add_effect(Injury('Wounds', 'strength', -1))
    
"Rowan looked around. Ulcro’s guards had been fighting bravely, but there were far too few of them and they were too unprepared to hold out for long against Batri’s forces The last of them lay in the dirt, bleeding badly from his side and trying to holler out for reinforcements."
"They would need to be quick about this. It was a good thing he’d prepared Delane first."

show eleanor rags concerned at midright with moveinright

ele "Hello? What’s happening out there!? Someone needs to tell me what’s going on!"

show rowan necklace neutral at midleft with dissolve

ro "Lady Eleanor."

ele "Hero Rowan? What are you…"
ele "Was this the rescue you spoke of before?"

ro "In a sense."

"Lady Delane’s eyes narrowed. She simply didn’t trust him enough to blindly follow him around. Thankfully, she didn’t have to."

ele "No...No those were other orcs fighting outside. Why are you here?"

if avatar.corruption < 30:
    
    ro "I know this might be hard to believe my lady, but these orcs do not seek to harm you. They will keep you safe much as Ulcro was doing. The difference is that…"
    ro "Um…"
    ro "They have promised to be more considerate of your...urges then Ulcro’s men have been. I have heard reports of your nocturnal activities. If you come with me now...If you don’t fight...then you can have that. More of that."
    ro "So please. Come with me willingly. So I don’t have to bring you by force."
    "Even the words stung to say. It felt like he was twisting the knife. But, he needed to recruit Batri and he needed her to come along without resistance to Batri’s tent. He had to do this. He just had to."
    $ change_base_stat('g', 3)
    
else:
    ro "You do yourself credit with your deductive powers, my lady. Those are orcs. Orcs who have heard tales of your beauty. They seek to bring you to their leader. You will be safe with him."
    ele "The warchief from before…"
    ro "Indeed."
    ro "But, we have no time for lengthy discussions. I know about your nocturnal activities. I know you’ve been having sex with the orcs. I know that you love it deep down."
    ro "You have two choices. Fight this and be brought back kicking and screaming. Possibly be hurt along the way. Or come along with us. Sate your desires. Enjoy yourself the way you’ve wanted to enjoy yourself. You know you want it."

"At the end of the day, there was only one way this entire encounter could have ended. Rowan’s earlier efforts to corrupt her, to make her addicted to orc cock, made sure of that."
"Rowan opened the door to her cage. Lady Eleanor Delane walked out, joining the waiting pack of orcs…"

$ delane_status = "batri"
$ journal.complete_quest_note('orciad', 'note26')
$ journal.add_quest_note('orciad', 'note27')
jump campMenu
    
