init python:

    event('castle_access_week4', triggers="week_start", conditions=('week == 4',), run_count=1, priority=pr_system)
    event('castle_alexia_job_week23', triggers="week_start", conditions=('week == 23',), run_count=1, priority=pr_system)
    event('week4_introduction', triggers="week_start", conditions=('week == 4',), run_count=1, priority=pr_story)


label castle_access_week4:
    # this enables access to castle on week 4, enable researching and building
    $ systems.castle = True
    $ systems.research = True
    $ systems.building = True
    return


label castle_alexia_job_week23:
    $ systems.npc_jobs = True
    # assign starting job class to Alexia
    $ all_actors['alexia'].job_state = ActorJobState()
    $ castle.npc_with_jobs.append('alexia')
    $ set_job_class('alexia', 'pure_housewife')
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label week4_introduction:

#### Fix later

$ alexiaOffer = False

####### start of week 4 #######

#sunrise CG

scene black with fade

show jezera happy behind black

"Rowan awoke with a familiar form resting against him. It wasn't their home back at Arthdale, but for a moment, it might as well have been."

je "Good morning, my hero."

"Just for a moment."
"Jezera was relaxing in a nearby seat, watching the couple with a smile on her face."

scene bg9 with fade
show alexia necklace naked behind bg9
show rowan necklace naked behind bg9
show jezera happy at edgeright with dissolve

ro "How long have you been there?"

je "Only a few minutes, just thought I'd let you sleep a little longer and enjoy the scenery in the meantime."

al "Hmm... what is it Rowan?"

je "Good morning to you too, lovely lady."

show alexia necklace naked shocked behind bg9

al "Ah! What are you doing here?"

je "Dropping off breakfast and asking if you'd like your things brought over here from your room Alexia."

"She indicated the covered platters sitting on the desk behind her."

show alexia necklace naked behind bg9

al "Oh! Uh..."

"Alexia looked to her husband, unsure how she should respond."

menu:
    "Switch to one room.":
        $ released_fix_rollback()
        $ alexiaSeparateRoom = False
        "Rowan returned her look, then smiled and nodded."
        "Alexia beamed in response then turned back to the blue skinned demoness."
        al "Yes, I think I'll be sleeping here from now on."
        "Jezera nodded in response, then stood up."
        je "Very well, I'll send someone at once to take care of that. I'll also have a bath prepared for the both of you."
        je "Rowan, I will not be calling on your services until after lunch, you have the morning off."


    "Keep separate rooms.":
        $ released_fix_rollback()
        $ alexiaSeparateRoom = True
        ro "I'm probably going to be keeping odd hours and won't be around all that often, maybe you should keep your old room and we can share whenever we feel like it?"
        al "I was actually thinking the same thing. We also wouldn't have to worry about disturbing one another if... something unavoidable comes up. Though it's a relief that I didn't have to suggest it myself."
        "Alexia gave a small smile and then turned back to the blue skinned demoness."
        al "Thank you, but I think you can leave my things in my room for now."
        "Jezera nodded in response, then stood up."
        je "Very well. Then I'll make arrangements to have a bath drawn for you instead. You're free to return to your room when you wish."
        je "Rowan, I will not be calling on your services until after lunch, you have the morning off."

"She walked towards the door, then stopped just as she touched the knob."

je "Oh, and I'm so glad that the two of you didn't try to escape last night. I had a small bet with my brother that you wouldn't try something so foolish."
je "He'll be so disappointed to find out he lost."

hide jezera with moveoutright

scene black with fade
scene bg9 with fade
show rowan intro necklace happy at midleft with dissolve
show alexia necklace happy at midright with dissolve

"Half an hour later, Alexia and Rowan were eating together and discussing the demonic twins, whose whims they were now subject to."

if alexiaOffer == True:
    al "... and that's about all I know about Andras, other than..."
    show alexia necklace concerned at midright with dissolve
    "Alexia burned with shame as she struggled to get the words out. Her husband, sensing how uncomfortable the memories were making her, took her hand and moved the topic on conversation on."
    ro "Shhhh, my love. Tell me what you were able to learn about Jezera instead."
    show alexia necklace happy at midright with dissolve

else:
    al "... and that's about all I know about Andras. Like I said, I'm not sure exactly what's real or not since he was probably pretending through most of it."
    ro "Alright, what about the sister?"

al "I'm afraid I don't know much about her. After you left she lied about her life in Uvarth for a while, then revealed her true self and knocked me unconscious with some sort of magic spell."
al "She would sometimes come and visit, but never said much."
al "Both of them seem to be very good liars and have powerful magic. Darling, please be careful around them."
"Rowan smiled and nodded, and the pair spent the rest of the morning discussing happier topics of conversation, until it was time for Rowan to report to Jezera."

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve

"Shortly after lunch..."

ro "I see we're no longer under guard."

je "Yes, that was the agreement if you didn't try to escape. You're both now free to travel around the castle as you please."
je "My hero, please, walk with me."

"The blue skinned demoness started to walk down the hallway, Rowan hesitated for a moment and then followed."

ro "This isn't the way to the portal chamber."

je "No, today I'm giving you a new set of duties."

ro "And what exactly would those be?"

je "Management and advice. While we do have a mighty fortress here, it is woefully understaffed and most of the surrounding infrastructure was destroyed in the last war."
je "That's why I chose you to be our agent. You aren't the most powerful, nor the strongest, nor the smartest of the heroes that killed my father."
je "However, you are cunning and have the skills we need to change this castle into the seat of an empire."

ro "What makes you say that?"

"Jezera suddenly stopped."

show jezera happy at midright with dissolve

"After a moment turned to smile at Rowan."

je "You're the hero of the siege of Karst. After the lord died and the other nobles fled, you are the one who took command and held out for a siege that lasted four months until reinforcements from Prothea arrived to relieve it."
je "You are the one who constantly snuck out of the castle at night to smuggle in supplies."
je "You are the one who managed to repel two assaults in spite of impossible odds."

ro "Three assaults."
ro "Most don't remember the second one since they gave up after realizing I'd sabotaged the siege equipment the night before. Also the first one was doomed from the moment I'd managed to rally the garrison; they didn't have any siege equipment at the time."

je "The stories do tend to miss a lot of details and embellish some things."

ro "People always prefer the legend to reality. When I think of Karst, I see the faces of people who died. People who put their lives in my hands."

je "Still, it remains an impressive resume. Such a shame that a commoner can't become a general, let alone an officer, in Rosaria."
je "Like your little band of heroes, my brother and I aren't going to let a thing like birth get in the way of putting someone's skills to use."

ro " I think you misunderstand why I chose to go back to Arthdale."

je "Chose? Well, you've made your choice to work for us and I don't intend to let your talents go to waste."

"She resumed walking, leading Rowan into the throne room."

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg6 with fade
show rowan necklace neutral at midedgeleft with dissolve
show jezera neutral at trueedgeleft with dissolve

je "That's why I'm putting you in charge of the castle."

ro "What?"

je "My brother and I will set the quotas for what we want done, it will be your job to work out how we get there. Oh, and don't worry about the day to day operations, we still want you to be our eyes and ears in the world."
je "Your job will be to figure out the big picture."
je "That includes choosing how to spend our funds and where we should direct our research. I suppose that would make you our steward."

show clamin neutral pipe at midmidright with moveinright
show skordred neutral at skorright with moveinright

"Jezera came to a stop in front of an odd pair; a dark dwarf man and a goblin woman."
"The dwarf had a regal air about him, with his elaborate gold plated clothing, but his appearance was very typical of his race. Rowan noticed right away that the dark man did not like him, his tense stance and glare of disdain was very evident."
"The goblin woman on the other hand was all smiles. She had the look of a caravan merchant and gave off a practised sense of trying to make herself seem like she was your best friend and had the perfect item that would solve all your problems."

je "May I present to you Skordred and Cla-Min."
je "You two, this is your new boss, the hero Rowan."

"The dwarf, Skordred, spat on the floor as Jezera spoke Rowan's name. On the other hand, the goblin Cla-Min bowed deeply. Jezera ignored their actions."

je "Skordred is a dark dwarven master builder, a status that the one who built the first Castle Bloodmeen also held, and lead the team that rebuilt it for Karnas."
je "He has agreed to resume his old post in service to my brother and I, and will oversee any construction projects you allocate funds for."

sk "Listen, 'hero', I don't want to talk to you more than I have to.  Even if you serve the new masters now, you're part of the group that killed the old master.  I haven't forgiven you for that grave sin."

hide skordred neutral with moveoutright

je "Not particularly friendly, but like our mother, he is strongly drawn to the darkness. I don't doubt his loyalty in the least."

"Seemingly unable to contain herself any longer, the goblin woman jumped forward and started shaking Rowan's hand vigorously."

show clamin happy at midmidright with dissolve

cla "Tis an honor to finally meet the great master schemer Rowan! A great goblin in human flesh!"

"After a moment Rowan realized with some alarm that the green woman was genuinely fawning over him!"

cla "There have been so many stories of the great things you've done during the war, of sabotage and trickery! No cheating magic, no big man strength, just honest slinking and stinking."
cla "It'll be a real honor working under you... or over you if that's your preference."
cla " To be honest, I prefer being on top myself, but I've got lots of girls in the family who like taking it in all sorts of ways and-"

je "That's enough. Give the man some space."

"Much to Rowan's relief, the openly affectionate goblin woman stepped back then bowed to him again."

je "Cla-Min is the head of a goblin merchant caravan. She's agreed to provide us with the supplies and materials we will need in exchange for access to my portal network. If you need to upgrade your equipment or acquire adventuring gear, she's your woman."

"The short stack posed proudly and winked at the hero. Then she hesitated and seemed to be struck by a sudden inspiration."

cla "We've got lots of boys in the family too if you don't go for ladies. I'm sure we can work out-"

show jezera displeased at trueedgeleft with dissolve

je "Min!"

cla "Sorry."

"Shaking her head in dismay, Jezera lead Rowan away from the merchant towards the stairs down to the underground section of the castle."

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg8 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve

ro "That was... an interesting experience."

je "I'd assumed that Skordred would give you the cold shoulder, but Min's over exuberance was wholly unexpected.  Had you ever heard of goblins idolizing you?"

ro "I'd heard a rumor about it once, but I'd discounted it long ago."

scene bg11 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at edgeleft with dissolve
show andras displeased at midright

"The two of them found Andras in what appeared to be a barracks complex, watching orc soldiers perform training drills. Upon noticing the approaching pair, the red demon's expression soured considerably."

an "Ah, sister, and servant. Time for the inspection then?"

je "Dear brother, are you such a sore loser that you can't even manage common courtesies?"

"Andras only growled in response then waved the blue skinned woman off and indicated for Rowan to stay. Jezera waited a moment to see if her brother would say anything else before shrugging and leaving her charge behind."

hide jezera with moveoutleft

an "This is our current military facility. Skordred hasn't had enough resources to get more than an orc barracks up and running out of the ruins of the old underground."

scene black with fade

"He went on to explain in detail their current ability to support forces and his recruitment efforts.  Rowan took a tour of the area afterwards and sparred briefly with some of the soldiers."
"Afterwards he had a very good idea of the current military capacity of the castle."
"And all that he'd learned suggested that the state of things was not good."
"At maximum capacity the current facilities couldn't do much more than occupy a handful of villages, and they wouldn't be able to hold them against a major counter attack."
"On top of that, Andras's current recruitment prospects would take months to fill the barracks."
"It would take a lot of improvements to the facilities and dramatically increased recruiting to conquer a single one of the six realms, let alone all of them."

scene bg6 with fade

show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve
show andras displeased at edgeright with dissolve

je "Now that you know what our capabilities are, it's time to learn what me and my brother expect of you in the coming months."

"The three of them were back in the throne room, now with Jezera sitting on the throne and Andras standing at her side."

je "Firstly we want you to raise a force powerful enough to take Raeve keep in Rosaria, nearby my portal. This will end the baron's rule in the area and create a foothold for further conquests."

show jezera happy at midright with dissolve

je "If you can somehow sway the duke to our cause or take control of the keep through delectable subterfuge, that will satisfy us as well."

"The demoness obviously liked the idea of taking over from the shadows. Her brother snorted, clearly he'd prefer the more direct route over the alternatives that his sister had suggested."

show jezera neutral at midright with dissolve

je "In addition, bring up our overall military capacity to that of a proper army and raise our treasury to contain at least 500 gold crowns. Complete these tasks in six months."

show jezera happy at midright with dissolve

je "Succeed and you shall earn many rewards."

show andras angry at edgeright with dissolve

an "Fail, and you will suffer greatly, Alexia as well."

je "Good luck, my hero."


####new content #####

show andras displeased at edgeright with dissolve

je "With that formality out of the way, the treasury is at your disposal for your first construction projects. Skordred will tell you about what projects are available. We will also start paying you a weekly salary for your work out of the treasury."

an "I would advise against spending that money frivolously. It's what you'll be buying your personal equipment with."

ro "So I'm to work with what I have in your service? I guess Cla-Min will have to live with not seeing me as a customer for a few weeks to come."

je "Well, if she has something that will help you in our service, perhaps I can be convinced to divert some of our construction funds as a stipend for you to purchase equipment? That is, as long as you don't mind me keeping some of it for my own schemes."

ro "I'll think about it."

an "Then talk to our servants and return when you've come to your decision."

scene bg20 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan knocked on the door to Skordred's workshop."

play sound "music/SFX/door knock.ogg"
pause 1

show skordred neutral at skorright with moveinright

"A moment later, the dwarf arrived with a glare in his eyes."

ro "Let me see your current construction options."

"Evidently the dwarf had expected this, and he handed Rowan a clipboard with three diagrams on it, along with short descriptions of each. They'd probably been prepared for the twins, but now Rowan was the one to receive them."
"The builder was not happy about this."

hide skordred with moveoutright

ro "(My options are, a forge, a dark sanctum, or a tavern.)"
ro "(The forge would dramatically improve the power of our soldiers. The dark sanctum would give us another type of soldier and improve our ability to do research, helping in the long term. The tavern would increase the income for our treasury.)"

"Still holding onto the clipboard, Rowan left the workshop behind and headed towards the wagon parked a ways outside the castle's main gate."

scene bg19 with fade
show rowan necklace neutral at midleft with dissolve
show clamin neutral at midright with dissolve

"The goblin woman was much friendlier, eager to show off what goods she had available. Some of her enthusiasm faded when she found out that Rowan didn't have the money on him to buy much yet, but kept at it out of her strange adoration."
"Cla-Min had a small selection of arms available; nothing fancy, but always useful for anyone in the adventuring profession."

ro "(Well, time to come to my decision.  Should I start one of the construction projects or give up some of the treasury for a stipend to buy equipment with?)"

scene black with fade

#### give player two choices - "Purchase something from Cla-Min" or "Discuss construction with Skordred"
#### for the Cla-Min option, use the current shop we made for castle earlier with Cla-Min as the shopkeeper
#### for the Skordred option, give the player the choice of building the forge, the dark sanctum, or the tavern (must choose one before game continues)
menu:
    "Purchase something from Cla-Min":
        call screen shop_screen(castle_shop_trader)
        $ released_fix_rollback()
        scene bg6 with fade
        show rowan necklace neutral at midleft with dissolve
        show jezera neutral at midright with dissolve
        show andras displeased at edgeright with dissolve
        #If Rowan purchased equipment
        # TODO: detect if equipment was purchased actually
        je "Here is your stipend, 100 gold pieces.  I'll be keeping 50 of what we would have spent on the building, you wouldn't have been able to use it for a few weeks anyway."
        an "Such a shame that you humans need to rely on metal and tools to get things done. Very well, but know that you'd best be getting my facilities up sooner rather than later if you hope to meet the quota."
        $ change_personal_gold(100)

### end of new content ###

    "Discuss construction with Skordred":
        menu:
            'Forge':
                $ castle.scheduled_upgrades.append('forge')
                $ change_treasury(-all_buildings['forge']['cost'])
                $ released_fix_rollback()
                scene bg6 with fade
                show rowan necklace neutral at midleft with dissolve
                show jezera neutral at midright with dissolve
                show andras displeased at edgeright with dissolve
                #If Rowan built the forge
                an "Excellent. Having proper gear should make my orcs actually somewhat decent in battle. I already have someone in mind to serve as forgemaster. I'll have him in by the time Skordred is finished building the forge."

            'Dark Sanctum':
                $ castle.scheduled_upgrades.append('sanctum')
                $ change_treasury(-all_buildings['sanctum']['cost'])
                $ released_fix_rollback()
                scene bg6 with fade
                show rowan necklace neutral at midleft with dissolve
                show jezera neutral at midright with dissolve
                show andras displeased at edgeright with dissolve
                #If Rowan built the dark sanctum
                je "I'm glad we're going to finally get sorcerers around here, they'll be able to give Cliohna a hand. Hmm, I'll have to see about getting someone to keep the succubi and incubi in line."

            'Tavern':
                $ castle.scheduled_upgrades.append('tavern')
                $ change_treasury(-all_buildings['tavern']['cost'])
                $ released_fix_rollback()
                scene bg6 with fade
                show rowan necklace neutral at midleft with dissolve
                show jezera neutral at midright with dissolve
                show andras displeased at edgeright with dissolve
                #If Rowan built the tavern
                je "The earlier we build our income, the faster we will be able to build everything else. I do hope you put the intelligence we get to good use as well. You're going to be playing catch up when it comes to building our armies."


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

je "The final decision you'll have to make today is how you want to direct our librarian's research. I understand she's ready to start at anytime, so please pay her a visit right away."

show bg12 with fade

"Rowan entered into the great library of Castle Bloodmeen."

show rowan necklace neutral at midleft with dissolve

ro "Never was one for books, I do remember how ecstatic Loralyn was when she first stepped in here."

"He skimmed the aisles, looking for the librarian. There'd been several sorcerers in Karnas's armies that worked in here during the war, but Rowan couldn't remember anyone being known as 'the librarian'."

"Whoever she was, she wasn't one of the old guard like Skordred."

show cliohna neutral at cliohnaright with dissolve

"Then the hero found her, standing at a lectern in one of the alcoves. She looked very young, either in the end of her teens or barely out of them by Rowan's guess."
"Long blond hair ran down her back and she wore very revealing clothing that barely covered her body."
"The woman appeared to be deeply engrossed in the rather large tome she was currently reading. A stack of similarly sized books rested nearby with a magical staff propped against them."

hide rowan with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "So, you're the librarian?"

"As Rowan spoke, she carefully closed the book and turned to face him. Instantly the hero realized that he'd been wrong about her age; the eyes gave it away. They were not the innocent eyes of a girl, but instead ancient and filled with cynicism."

cl "Cliohna, and you must be Rowan. I have prepared a list of topics that I can focus my research on, please select the one you think will be best to begin with."

"She took a sheet of parchment off of the lectern and handed it to Rowan. He accepted it and did a quick skim of the topics outlined."

ro "Okay, I can understand why we'd need to work on diplomacy or set up a contact network for research, but why exactly do you have exploration techniques and history of the war on here?"
ro "I probably know more about the war than most, and have plenty of scouting experience."

cl "Ah, but how much do you know about how the world has been reshaped after the war? Have you worked with charting courses for armies or have you been trained in the use of cartography and surveying equipment?"

ro "Uh..."

cl "I could go to great lengths to explain why each and every one of these items will be of great use to the twins and your service to them."

ro "No, I think that's fine."

cl "Good, I'll keep it short then. Any of these are perfectly fine to start with, the main thing that will be important from here on out is that you don't focus your efforts too hard in any one category."
cl "After all, having great soldiers and knowledge of tactics will not be useful if you don't have the diplomatic skills to recruit new armies to your cause."
cl "The expertise to train and breed monsters will not go far if you haven't the skill to find their nests in the first place."
cl "Now, lord Rowan, let me know when you have made your choice."

#force Rowan to choose a research subject
call screen researches_screen(True)

cl "Very well. I will begin my work and submit a report when I've finished."

"Evidently this was the end of the conversation. Cliohna turned back around and selected a different tome from the stack. With a wave of her hand, it floated out of the pile and settled itself onto the lectern as the old book took its old place in the pile."

"Rowan simply shook his head and said goodbye before taking his leave. That woman did seem to be human, but he was certain that she was a lot older than she seemed."
"The power he felt radiating from her must have been similar to Loralyn, who herself was one of the most skilled of the remaining elven mages."

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve
show andras displeased at edgeright with dissolve

"He returned to the throne room."

an "It seems that concludes your duties, for now."

je "Are there any question you have about the castle?"

ro "I'm curious, where did you find Cliohna? I can tell she's a powerful magic user, an ancient one at that, but I've never heard of her. Even most of the elves only live for a couple centuries, but she seems even older than that."

show jezera happy at midright with dissolve

"The blue skinned demoness only smiled."

je "I don't know where Cliohna is from.  She approached us, not the other way around. The deal is, she gets full access to the library in exchange for doing our research. That's the extent of our relationship."

show jezera neutral at midright with dissolve

je "At any rate, it is getting late and you should get to bed soon. We're sending you out to explore again in the morning after all."

# add codex entries
$ codex_add('cla_min_starting')
$ codex_add('skordred_starting')
$ codex_add('cliohna_starting')
$ glossary_add('treasury')
$ glossary_add('morale_start')
$ glossary_add('military_capacity_start')
#start turn
return
#~ jump gameend
