label delaneRescuePlan:

if delane_plan == False:

    scene bg26 with fade

    "So here he was: in the middle of an unfriendly orc camp, servant to a pair of maniacal power tripping half-demons. Once hero, now oppressor."
    "Not for long."
    "Rescuing Delane will not be an easy task. Her tent, while easy to get inside, was nevertheless in the middle of Ulcro’s camp. Rowan had to get her out of the tent, to the edge of the camp, past the guard towers and orc patrols, and into the woods."
    "A diversion would be necessary to draw attention away from Delane’s tent and his escape route. The fewer orcs there were around, the better."
    "Perhaps some of the orcs he knew could arrange for one, without asking too many questions about the purpose of it."
    "Batri orcs were always itching for a fight, so as long as he builds up their trust with him, he might be able to use them to achieve his goals."
    "Besides a diversion, he needed a reliable way out of the camp. Two cloaked figures walking into the woods would be simply too suspicious."
    "Perhaps there was someone that would help him this, but if worse came to worst, as long as he studies the perimeter carefully, he should be able to find some structural weak point to exploit."
    "With both of these elements in place, victory would be almost assured."

    $ delane_plan = True

    jump escapePlanMenu

else:
    
    jump escapePlanMenu
    

label escapePlanMenu:

$ journal.add_quest_note('orciad', 'note30')


menu:
    "Approach Batri’s men." if delane_status == "tent" and batri_raid_count > 1 and delane_plan == True and delaneDistraction == False:
        $ released_fix_rollback()
        jump batriBoysFight
         
    "See if Ulgan can help." if delane_status == "tent" and rowan_has_met_ulgan == True and delane_plan == True and delaneDistraction == False:
        $ released_fix_rollback()
        jump ulganHelp
        
    "Observe the perimeter." if delane_status == "tent" and delane_plan == True and delaneEscapePerimeter < 1:
        $ released_fix_rollback()
        jump observePerimeter
    
    "Ask the Matron for Help." if (delane_status == "tent" and delane_plan == True and delaneDistraction == False and orcMatronState == 2 and delaneEscapePerimeter < 1) or  (delane_status == "tent" and delane_plan == True and delaneDistraction == False and orcMatronState == 3 and delaneEscapePerimeter < 1):
        $ released_fix_rollback()
        jump orcMatronHelp
        
    "Rescue Delane." if delane_status == "tent" and delane_plan == True and delaneDistraction == True and delane_trust > 2 and delaneEscapePerimeter > 0:
        $ released_fix_rollback()
        jump orciadEscape
        
    "Leave the planning until later." if delane_status == "tent" and delane_plan == True:
        $ released_fix_rollback()
        jump campMenu



label batriBoysFight:

scene bg26 with fade

if batriBoysFirst == True:
    "After proving himself in raids, playing the orcs should be easy. There were several ways he could get them to cooperate and he had to decide which was best."
    "He only had one shot at it."
    $ batriBoysFirst = False
    
else:
    pass

label batriPlanMenu:
scene bg26 with fade

menu:
    "Bribe them with alcohol. (100 gold)" if avatar.gold > 99:
        $ released_fix_rollback()
        "Securing the alcohol was no problem."
        if all_actors['cla_min'].relation > 49:
            "He planned to talk with some of the merchants inside the camp, but after mentioning the issue to Cla-Min through the amulet, the thrifty goblin ended up arranging a quick delivery to the camp, just for him."
            "She still had him pay, albeit only enough to cover the expenses."
            $ avatar.gold -= 60
        else:
            "The camp had some merchants in it, that were willing to provide a barrel or two, for the right price."
            "Rowan was in no position to negotiate, but at least the whole transaction went through smoothly."
            $ avatar.gold -= 100
        "He met the orc raiders at the usual place, and his arrival was met with some enthusiastic shouts, but largely, his presence would be ignored."
        "One would think they would be more welcoming of him after all the battles he fought at their side, but the deep-rooted resentment for humanity would not be overcome so easily."
        "That’s what the alcohol was for. It was difficult to place yourself above somebody else when you were both shitfaced and laying in the mud."
        show rowan necklace happy at center with dissolve
        show wild orc neutral at edgeleft with moveinleft
        show orc soldier neutral at edgeright with moveinright
        ro "Let’s celebrate! For all the successful raid thus far, and for all the raids in the future!"
        ro "And for warchief Batri!"
        ro "The ale is on me!"
        "A boisterous cheer erupted among the orcs. They were not difficult people to please, but then again, no soldier ever complained about a free drink."
        hide wild orc with moveoutleft
        hide orc soldier with moveoutright
        "For the next two hours, Rowan traveled from group to group, laughing and drinking with them, expressing his admiration for the younger contender, and contempt for Ulcro."
        "Alcohol and tribal policy worked them up easily, but Rowan was careful not to overdo it. He needed them receptive to his words, not start a brawl."
        jump batriBoysMain
        
    "Sweet talk them." if batriSweetFail == False:
        $ released_fix_rollback()
        if check_skill(15, 'diplomacy')[0]:
            "He met the orc raiders at the usual place, and his arrival was met with enthusiastic shouts, with many of the orcs waving to him as he approached the group."
            "Ever the diplomat, he tried to be good company during the raids. After several of them, he managed to ingrain himself fairly well into the usual party." 
            show rowan necklace happy at center with dissolve
            ro "Tog, did you win the contest for Sharn’s favor?"
            show wild orc neutral at edgeleft with moveinleft
            wo "Bah, no. Stupid Ulag won, by jugglin’."
            wo "Jugglin’!"
            if avatar.corruption > 70:
                ro "Break his fingers while he sleeps. That will teach him a lesson!"
            else:
                show rowan necklace concerned at center with dissolve
                ro "That’s rough. Maybe next time."
            show rowan necklace neutral at center with dissolve
            hide wild orc with moveoutleft
            show orc soldier neutral at edgeright with moveinright
            ro "Kril, you need that armor patched. Next Rosarian knight we meet will skewer you like a fish if you don’t."
            os "Shuddup, or you’ll need your face patched!"
            hide orc solder with moveoutright
            "Rowan shook his head disapprovingly, knowing all too well he had to keep pestering him on this or else the orc will never listen."
            "He walked among them as an equal. Getting them to do his bidding would be easy. If he complained what bastards Ulcro supporters were and how he wanted to put them in their place, he was certain they would lend him his ears." 
            "And he did just that. For over two hours he worked them, and little by little the mood shifted, as the anger at Ulcro increased."
            jump batriBoysMain
        else:
            "He met the orc raiders at the usual place, and his arrival was met with some enthusiastic shouts, but largely, his presence would be ignored."
            "One would think they would be more welcoming of him after all the battles he fought at their side, but the deep-rooted resentment for humanity would not be overcome so easily."
            "Luckily for him, their resentment for Ulcro’s men was far greater."
            if check_skill(10, 'bluff')[0]:
                "For the next two hours, he walked among them, engaging in small talk."
                "He would mention, as subtly as he could, how he heard Ulcro’s men talking crap about Batri and his raiders. How they all thought his followers were undisciplined, weak little goblins."
                if all_actors['cla_min'].relation > 49:
                    show rowan necklace concerned behind bg26
                    ro "(Cla-min, forgive me.)"
                    hide rowan
                else:
                    pass
                "He told them he saw Ulcro’s slaves, and how they were obviously hogging all the good looking females to themselves."
                "That was obviously a lie, but the grass was always greener on the other side."
                "For the next two hours, he would spin more and more fantastic tales of real and imagined offenses Ulcro’s men committed against Batri’s orcs. His favorite was pissing in the same river they drink from."
                "He was fairly certain they all did so regardless. Orc had no concept of hygiene. But it got them fired up, and that’s what mattered." 
                jump batriBoysMain
            else:
                "For the next hour, he walked from group to group, trying to engage in small talk, and set them against Ulcro and his men."
                "But after a while, he saw he overplayed his hand. He spoke too harshly, too disrespectfully, and in a rare display of orc unity, Batri’s men started to defend the ruling warchief."
                "Learning his lesson, he tried to salvage the situation, but it was too late. He squandered the trust he built up during the raids, and there was no way he would be getting it back."
                "He’ll have to find another way to obtain a distraction."
                show rowan necklace angry behind bg26
                ro "(Damn it!)"
                hide rowan
                $ batriSweetFail = True
                jump batriPlanMenu
                
    "Taunt them." if batriTauntFail == False:
        $ released_fix_rollback()
        " He met the orc raiders at the usual place, and his arrival was met with some enthusiastic shouts, but largely, his presence would be ignored."
        "It wouldn’t last for long. He would be playing it loose here, but if his gambit plays off, they'll all be eating from his hand soon enough."
        show rowan necklace angry at center with dissolve
        show wild orc neutral at edgeleft with moveinleft
        show orc soldier neutral at edgeright with moveinright
        ro "I’ve been working my ass off, helping Batri show everyone what a bunch of weaklings Ulcro and his men are."
        ro "And all you guys are doing is go on a raid once a week, and call it a fucking day!"
        "He now had a small gathering around it. All he needed was…"
        wo "Hey, ya tryin’ to get yerself killed?!"
        show rowan necklace happy at center with dissolve
        ro "(So predictable.)"
        show rowan necklace angry at center with dissolve
        ro "No, I’m trying to get the orcs who are supposed to be my allies pull their damn weight!"
        "The orc growled at him and started to approach him slowly. Rowan met his furious glare with his own, cold stare."
        if check_skill(15, 'intimidate')[0]:
            "He stopped a few steps away from him. They all saw Rowan fight in the raids. They knew he was not someone they could just walk over."
            wo "Oh yeah?"
            wo "So whad’ya suggest we do?"
            wo "Or are ya here to just talk trash?"
            show rowan necklace happy at center with dissolve
            "He gathered them around and started to explain his idea. Anger, once aroused, was easy to redirect. Hey only needed some time to talk them over."
            jump batriBoysMain
        else:
            "They all saw Rowan fight. They knew he was not one to be trifled with"
            "But anger clouded the orc’s judgment. With an intimidating roar, he closed the distance between them and aimed a punch at his face."
            $ event_tmp['combat roll'] = check_combat(10)[1]
            if event_tmp['combat roll'] >= 10:
                show rowan necklace angry at midright with moveoutright
                "Rowan dodged the blow easily, and sucker punched his attacker in the stomach. He followed up with a quick uppercut, and then another punch, straight in the face."
                hide orc soldier with dissolve
                show rowan necklace angry at center with moveinright
                ro "Any more distractions, or can we move on to what is important for all of us?"
                ro "Showing Ulcro’s men where their place is."
                "The group followed with an unenthusiastic grunt of approval. Morale was low, but it didn’t matter."
                "Rowan only needed some time to talk them over, and with his position reestablished, he was free to work his magic."
                jump batriBoysMain
            else:
                "He raised his arms to block the punch, but the raw force of it sent him reeling."
                show rowan necklace angry at midleft with moveoutleft
                hide rowan with dissolve
                show orc soldier neutral at center with moveinright
                "He collapsed to the ground, the orc now hovering over him. He quickly jumped up and placed his hand on the hilt of his sword, in case the orc moved in for the kill."
                "But the warrior only looked down on him contempt."
                os "Ya good raider."
                os "Stick to dat."
                "The surrounding orcs all nodded in agreement, and the group slowly started to dissipate."
                "Whatever respect Rowan built up over the last weeks vanished into thin air. There was no way they would help him now."
                "He’ll have to find another way."
                show rowan necklace angry behind bg26
                ro "(Damn it!)"
                hide rowan
                $ batriTauntFail = True
                jump batriPlanMenu

label batriBoysMain:

scene bg26 with fade

"But his efforts did not go unnoticed. One of Batri lieutenants, that often led the raids, was watching him attentively over the course of the evening."
"He now saw fit to approach him."

show wild orc neutral at edgeright with moveinright

wo "Humi!"

show wild orc neutral at center with moveinright
show rowan necklace neutral at center with dissolve

"The orc – a young, lean, almost human-like fighter – put his arm around his shoulder, apparently trying to be friendly."

show rowan necklace happy at center with dissolve

wo "So nice to see ya."

show rowan necklace neutral at center with dissolve

wo "What’ya schemin’?"

"From what Rowan recalled, this one was one of the more aggressive supporters, not shying away from violence and underhanded tactics. Perhaps he could be of use to him."

show rowan necklace happy at midleft with moveoutleft
show wild orc neutral at midright with moveoutright

"He untangled himself from him and faced him with a friendly smile."

ro "“Scheming” already"
ro "I merely thought I’d get the boys fired up a little."

show rowan necklace happy at midleft with dissolve

ro "We’ve been raiding for weeks now, and Ulcro and his men still think they can look down on us."
ro "So I have been thinking… That maybe we could rough them up a little… Put them in their place."

"Rowan saw the orc’s eyes liven up. Nothing made the orcs more happy than the perspective of abusing others."

show rowan necklace neutral at midleft with dissolve

if avatar.corruption < 31:
    "Disgusting, really."
else:
    pass
    
show orc soldier neutral at edgeright with moveinright

"Rowan explained his idea once more. He already had the support of the regular raiders, and once the commanding officer took the bait, the matter was settled."

os "Ha ha ha! I like you Rowan."
os "Tell us when and where."

show rowan necklace happy at midleft with dissolve

ro "(Distraction acquired.)"

$ delaneDistraction = True

jump campMenu


label ulganHelp:

scene bg26 with fade 

if ulganHelpFirst == True:

    "For what he had to do, he needed expendable tools. For the most part, he wasn’t ingrained well enough into the tribe for anybody to trust him with starting a fight just because he told them to." 
    "He needed to convince them. Bribe them. And luckily for him, there was one orc who he knew he would be able to buy, despite the limited resources at his disposal."
    "Ulgan, the short, hardworking, underappreciated orc he met back when he trained his reflexes with the acolytes of the priest of Kharos."
    "Smart and ambitious, he would be the perfect right-hand man for what Rowan had planned."
    "He found him after he saw the Kharos followers return from yet another training session. He took him to the side, and briefly explained what he needed of him, and what he offered in return:"
    "An officer position among the Bloodmeen orcs, once all of this was over." 
    "He hoped it would be enough, but Ulgan didn't bite. He would get Rowan the diversion he wanted, and he wouldn't ask any question. But it would require him to call a few favors from his friend."
    "All of them were to receive officer positions in Bloodmeen. This was not negotiable." 
    "He drove a high bargain, but Rowan could make it happen. Andras did not care for individual orc promotions, so he doubted there was any risk included."
    "But it would be a massive hit to orc morale. All of them believed might makes right, and such blatant favoritism was bound to cause a backlash."

else:
    "The option of making a deal with Ulgan was still available, even if it meant potential backlash with the other orcs."


menu:
    "Agree to his terms.":
        $ released_fix_rollback()
        if serveChoice == 4:
            "The morale starts being an issue, he'll find some way to deal with it later. For now, this was the quickest way to secure a distraction."
        else:
            "Of course, Rowan couldn’t care less for orc morale. They had to perform just well enough for Andras not to cut his head off, that’s all."
        "Rowan shook his hand and told him the details.  They established a spot in Rosaria where Rowan would meet them a month after everything was resolved." 
        "Quick and easy. Amazing how having the right person for the right job sped things up."
        $ delaneDistraction = True
        $ ulganBloodmeen = True
        jump campMenu

    "Reject the deal.":
        $ released_fix_rollback()
        "Getting just one orc into Castle Bloodmeen who could suspect he had anything to do with Delane's rescue was a risk. A whole group of them was madness." 
        "He will find another way."
        jump campMenu

     
label observePerimeter:

scene bg26 with fade 

if observePerimeterFirst == True:
    "Finding a hole in the orc perimeter wasn’t difficult. Their patrols were spotty, orcs routinely failed to show at their guarding posts on time, and most of them rarely paid attention to anything."
    "But with Delane on his back, he wouldn’t have the luxury of waiting for an opening to appear. He needed a weakness he could reliably exploit when the time is right."
    "And locating one required night, after night, after night, of careful observations. Identifying what guards occupied what spots, when they arrived, when they left, and what they did before and after their shift."
    "Mind numbing work, but there was no way around it."
    "With nothing to focus on his thoughts strayed to other matters. To Castle Bloodmeen, and the people in it."
    if all_actors['alexia'].relation > 30:
        "He wondered how his wife was doing."
        if get_actor_job('alexia')=='maid':
            "Was it really okay, for him to let her work under Jezera? Rowan had no doubt the demoness would use the opportunity to mess with her, and would do so as often as possible."
            "Alexia was no hero. Could she withstand the pressure?"
            "He hoped she would."
        elif get_actor_job('alexia')=='research_assistant' and alexia_knows_magic == True:
            "It was a stroke of luck, really, to learn that Alexia had such magical potential."
            "He wasn’t certain what influence the elf sorceress would have on his wife, but it couldn’t be worse than what the twins would do to her if she didn’t have a protector like Cliohna."
            "And perhaps, in time, her newfound magic would prove helpful, in one way or another."
        elif get_actor_job('alexia')=='forge':
            "He was lucky that Andras took interest in Greyhide. The minotaur smith was most certainly a gift from the goddess."
            "As long as Alexia stayed by his side, he was sure nothing bad would happen to her."
        elif get_actor_job('alexia')=='breeding':
            "He wasn’t certain if the Breeding Pens were such a good fit for Alexia. He knew Draith wouldn’t try any funny business, but if a drider broke loose…"
            "He didn’t want to think about it."
        elif get_actor_job('alexia')=='barmaid':
            "Perhaps being a tavern wench wasn’t the peak of Alexia’s dreams, but it was the least he could do to her."
            "Give her a chance to meet, talk with someone other than the twins and their slaves."
            "… And if she hears a helpful rumor or two, it would be all the better."
        else:
            "Living in castle Bloodmeen must have been tough for her. She didn’t really complain about anything, but…"
            "If something did go astray, with Andras or with Jezera, would she even tell him? Or would she suffer the abuse in silence, unwilling to add to his worries?"
            "He couldn’t know."
    else:
        if helayna_escape_method == "no escape":
            "How was Helayna doing? Was the ring acting up again? Were the twins causing her trouble?"
            "Was Alexia causing her trouble?"
            "..."
            "A long time ago, he promised he would no woman other than Alexia in his wife. Now…"
            "Now it seemed his thoughts were occupied with anyone but her. He knew it wasn’t right, but he couldn’t help it."
        if helayna_escape_method == "rowan":
            "Was Helayna safe? Ever since her escape, he had no news about her whereabouts."
            "At least that proved the twins had yet to get their fingers on her, and Rowan took solace in that. Her escape was a considerable hit to their authority, so if they ever get their fingers on her once more, their punishment would be as public as it was cruel."
            "… If Helayna gets to Prothea unharmed, and he manages to rescue Delane, then it would be proof there was still some good he could do in the twins service."
            "Even though Helayna would never have to escape from castle Bloodmeen if he didn’t help the twins capture Reave Keep in the first place."
        else:
            if rowanJezSex > rowanAndrasSex:
                "… What will Jezera do to him if, Goddess protect him, she learns he decided to rescue Delane rather than recruit the orcs?"
                "Will she tie him up? Have him kiss her feet? Hold his head between her legs and order him to lick till she cums as many times as many weeks Rowan wasted in the orc camp?"
                show rowan necklace concerned behind bg26
                ro "…"
                hide rowan
                "He swallowed heavily. Maybe he shouldn’t be spending so much time with the demoness…"
            elif rowanAndrasSex > rowanJezSex:
                "… What will Andras do to him if, Goddess protect him, he learns he decided to rescue Delane rather than recruit the orcs?"
                "Will he fuck his mouth with his cock, force him to eat his cum? Will he take his ass, caring not for his protests?"
                show rowan necklace concerned behind bg26
                ro "…"
                hide rowan
                "He swallowed heavily. Maybe he shouldn’t be spending so much time with the demon…"
            elif rowanJezSex > 0 and rowanJezSex == rowanAndrasSex:
                "… What will the twins do to him if, Goddess protect him, they learn he decided to rescue Delane rather than recruit the orcs?"
                "Will Jezera tie him up? Have him kiss her feet? Hold his head between her legs and order him to lick till she cums as many times as many weeks Rowan wasted in the orc camp?"
                "Will Andras fuck his mouth with his cock, force him to eat his cum? Will he take his ass, caring not for his protests?"
                "Or will they both take him – Jezera forcing him to eat her pussy while Andras fucks his ass?"
                show rowan necklace concerned behind bg26
                ro "…"
                hide rowan
                "He swallowed heavily. Maybe he shouldn’t be spending so much time with the twins…"
            else:
                "… When was the last time he did something nice to his wife? He tried to be faithful, as much as he could, and he felt her drifting away from him."
                "He was saving one woman, despite slowly, but surely, losing the one he swore to protect."
                show rowan necklace angry behind bg26
                ro "(Damn it…)"
                hide rowan
                "Alexia had nobody else in the castle but him. He should pay more attention to her, if he wanted her to remain by his side when all of this was over."

    "This, and other thoughts plagued him as he studied the guards routine through the week."
    "He made note of several orcs that failed to show up on time or left early. He would have to check during his next visit if it was merely a one-time thing or a chronic occurrence."
    "For the time being, his work here was done."

    $ observePerimeterFirst = False
    $ avatar.mp = 0
    return
        
else:
    if check_skill(15, 'spot')[0] or perimeterSearchCount == 2:
        "Finally, Rowan found what he was looking for."
        "A lone orc, overlooking one of the north-east guard towers, near the area where Tarish and Ulcro’s factions bordered one another."
        "All the other towers were pretty far away, so he was largely responsible for keeping an eye on this part of the camp exit."
        "Shame he had a nasty gambling habit, and a tendency to drink while playing. Of the three shifts Rowan witnessed him on, he arrived late in all of them. Always at least half an hour late. Always leaving the tower empty, as the other guard had long since lost his patience with him."
        "This would be their escape route. It was a bit off the beaten path, but he would have plenty of leeway during the escape itself."
        if delaneDistraction == True:
            "He now he had everything he needed for the escape."
        else:
            "Now all he needed was a distraction for the guards, and they were good to go."
        $ delaneEscapePerimeter = 1
        jump campMenu

            
    else:
        "Once again, Rowan has spent the entire week looking for the hole in the orc defenses."
        "None of the openings he checked thus far proved to be reliable. One time slip-ups, all of them. Frustrating, but to be expected."
        "Perhaps next week, he’ll have more luck."
        $ perimeterSearchCount += 1
        $ avatar.mp = 0
        return


label orcMatronHelp:

scene bg26 with fade

"Rowan found the matron in Tarish camp again, teaching a teenage female orc how to cook a proper stew. Curious, he decided to stay a while, out of their field of view, to watch the elder woman work."
"The matron showed remarkable patience with her protegee, explaining everything in great detail, with only occasional snark."
"But the younger orc wasn’t one to take it stoically forever, no matter the age difference, and ended up biting back at one point."
"The orc matron smacked her over the head so hard, Rowan was sure she gave her a concussion. The younger orc merely muttered a word of apology, and got back to seeing to the cauldron."
"Not exactly his preferred method of teaching, but it wasn’t his place to speak up. Besides, he had a different objective here."
"The matron was one of the few orcs who were able to outgrow the orc’s innate desire for destruction. Anything that would put Rowan – and castle Bloodmeen by extent - in opposition to the orcs camp, was within her interest."
"Getting her to help ought to be easy."
"Not wanting to attract too much attention, he quietly relocated himself, so that the Orc Matron could see him. Her eyes found him quickly – and narrowed with anger almost instantly. To her, he was a “warbringer”."
"His presence never heralded anything good."
"Rowan signaled for her to follow, and after some hesitation, she did."

show rowan necklace neutral at midleft with dissolve

orcm "Warbringer. What do you want?"

"He led her away from the heart of the camp, to a nice, secluded spot, where they could talk freely."

ro "I’ve come to ask for a favor."

"The Matron bared her teeth. Rowan couldn’t say if she was smiling, or mocking him. Both, maybe."

orcm "How unlike you and your master. Your kind rarely asks us for anything. Usually you just take."

ro "And you give it to us freely. You always do."

show rowan necklace concerned at midleft with dissolve

ro "We’ve been through this."

"Her mocking smile faltered."

orcm "Yes. Yes we did. Which makes me wonder… What do you need of me?"
orcm "We both know how this ends. Why do you torture me with your presence?"

show rowan necklace neutral at midleft with dissolve

ro "That’s not exactly true."
ro "This time, the outcome isn’t preordained."

if orcMatronState == 2:
    "Her eyes narrowed, and she closed in, growling. Rowan felt her unpleasant breath on his face, but refused to take a step back."
    orcm "Is that so? You sounded fairly sure it was the last time we walked."
    orcm "That we would end up slaves to your master."
    "Rowan wasn’t one to allow cheap intimidation tactics like this one to work on him, so he kept his gaze steady, and his voice firm."
    ro "And it might still happen."
    ro "Or it might not."
    ro "There is… Something I need to do."
    ro "I can’t go into details, but if I am successful, things might turn out differently for you."
    ro "Maybe you won’t end slaves to my master after all."
    ro "… Maybe you will yet find peace."
    if avatar.corruption > 70:
        "He didn’t believe a thing he said. Even if by some chance the orcs escapes the twins yoke, they’ll just find themselves embroiled in another conflict soon enough."
        "They are born beasts, and they will die beasts."
        if check_skill(15, 'bluff')[0]:
            jump matronHelpGranted
        else:
            jump matronHelpDenied
    else:
        "The odds of that were slim. The orcs were a vicious race, and even if they escape the twins yoke, they were likely to find themselves embroiled in some other conflict soon enough."
        "But they would have a chance. And sometimes that was all people needed."
        if check_skill(15, 'diplomacy')[0]:
            jump matronHelpGranted
        else:
            jump matronHelpDenied

else:
    show rowan necklace concerned at midleft with dissolve
    ro "We don’t have to be slaves. We don’t have to just let fate decide our role in all this."
    "A short, dry lough escaped her lips."
    orcm "High words, given your position. Did something change, Warbringer? Are you free to do as you please?"
    "The last time they talked, in a moment of weakness, Rowan let it slip that his own role in all of this was not entirely voluntarily. Back then, he cursed himself for it."
    "But now this would be the bridge that would help close the gap between them."
    ro "No, I am not."
    if serveChoice == 2:
        ro "But I am tired of being afraid."
    elif serveChoice == 1:
        ro "But I can’t wait forever for the right time to strike."
    elif serveChoice == 3:
        ro "But I can’t doom one woman just to protect another."
    else:
        pass
    jump matronHelpMain




label matronHelpGranted:

orcm "But you need my help to succeed."

"Rowan nodded in response, and the matron growled in frustration. She paced angrily in front of him, unwilling to make the call."

orcm "Empty words. False hope, dipped in pretty rhetoric!"
orcm "… Is what I want to say."

show rowan necklace happy at midleft with dissolve

ro "Perhaps some pretty rhetoric."

show rowan necklace neutral at midleft with dissolve

ro "But these are not empty promises."
ro "What I am about to do is very dangerous, but believe me, you want me to succeed."

orcm "But you can’t tell more until I agree to help. Yeah, yeah, I get it."

"She turned away from him, turned her gaze to the orc camp."
"Rowan recognized that look instantly. He knew it by heart. He saw it every time he would order the young men of Rosaria villages to pick up arms against Karnas."
"This mixture of fear and longing. The home they grew up in, would they see it again? Will they stop the enemy before his claws reach that what is most dear to them? Will it stand without them, or will it crumble to dust the moment they turn their eyes away from it?"
"And if it does crumble to dust, will they ever find another like it?"
"How many camps was the matron part of, in her long life?"

orcm "… Fine."

"One too many."

orcm "What do you need?"

jump matronHelpMain

label matronHelpDenied:

orcm "Empty words. False hope, dipped in pretty rhetoric, meant to bend me to your will."
orcm "You want to change the outcome?"
orcm "Leave and never return. Tell your master you failed. Tell them the orcs will never serve their kind."

show rowan necklace angry at midleft with dissolve

ro "It’s not only about you-"

orcm "Of course not."
orcm "We’re just pawns here. To be used and thrown away."

"She sighed, too tired to continue. Before, Rowan guessed she must have been in her fifties, but when she slanted her shoulders in defeat, the overwhelming feeling of hopelessness added twenty more years to her body."

show rowan necklace concerned at midleft with dissolve

orcm "Just go."
orcm "Do what you must, and don’t bother me again."

"… He would find no help here."

$ orcMatronState = 5

jump campMenu


label matronHelpMain:

ro "I need you to help me smuggle someone out of the camp."
ro "I need you to help me rescue Eleanor Delane."

"He saw her eyes widen. The name was known to those who kept their ears to the ground."

orcm "Delane… The noblewoman everyone lost their head over."
orcm "She asked you to get her, right? Tarish? Batri as well? In return for their support."

show rowan necklace happy at midleft with dissolve

ro "And Ulcro wanted me to convince her to love him."

orcm "In return for support."
ro "In return for support."

orcm "…"
orcm "The entire tribe."

show rowan necklace concerned at midleft with dissolve

orcm "All the men, women and children."
orcm "Sold for one for one human pussy."
orcm "Unbelievable."

show rowan necklace happy at midleft with dissolve

"The matron let a pained groan, and Rowan couldn’t help but sympathize. He couldn’t comprehend the twins priority pyramid either."

ro "Can you get her through the camp perimeter?"

"The matron nodded, still stunned by the revelation."
"Regardless, he could leave the matter in her hands."

$ delaneEscapePerimeter = 2
jump campMenu


label orciadEscape:

$ journal.complete_quest_note('orciad', 'note14')
$ journal.complete_quest_note('orciad', 'note15')
$ journal.complete_quest_note('orciad', 'note16')
$ journal.complete_quest_note('orciad', 'note17')
$ journal.complete_quest_note('orciad', 'note18')
$ journal.complete_quest_note('orciad', 'note20')
$ journal.complete_quest_note('orciad', 'note21')
$ journal.complete_quest_note('orciad', 'note22')
$ journal.complete_quest_note('orciad', 'note23')
$ journal.complete_quest_note('orciad', 'note24')
$ journal.complete_quest_note('orciad', 'note25')
$ journal.complete_quest_note('orciad', 'note29')
$ journal.complete_quest_note('orciad', 'note30')
$ journal.complete_quest_note('orciad', 'note31')


scene bg30 with fade
show rowan necklace neutral at midleft with dissolve
show eleanor rags happy at midright with dissolve

ele "Rowan, as always your presence brightens my day. What news do you bring?"

ro "The one you were waiting for all this time."

show rowan necklace happy at midleft with dissolve
show eleanor rags concerned at midright with dissolve

ro "Everything is in place, my lady. We leave the camp tonight."

"At first, Delane did not seem to comprehend his word. For so long, the prospect of freedom seemed so far away." 
"She held on it, held on to that hope, despite knowing she was likely just deluding herself." 
"And now Rowan told her that by the end of the night, she will once more be a free woman." 

show eleanor rags happy at midright with dissolve

ele "Rowan, I ..."

if delane_corruption_occurred == True:
    show eleanor rags concerned at midright with dissolve
    ele "Thank you, thank you so much."
    show rowan necklace concerned at midleft with dissolve
    ele "Truth be told, I don't know how much longer I would be able to keep my sanity intact."
    ele "I've been visited by this... "
    show eleanor rags concerned at midright with dissolve
    "A deep blush entered her face, and she found herself unable to continue."
    ele "No, it doesn't matter anymore. What's important is finally getting out of this hellish nightmare."

elif (delane_corruption_occurred == False) and (ulcro_path > 1):
    ele "Truth be told, I was starting to lose hope."
    ele "With the way you spoke of Ulcro, I feared you had given up on finding a way to free me."
    ele "I apologize for ever doubting you. You truly are a man of your word."
    ele "Thank you, for everything."
    
else:
    ele "Thank you, for everything."
    ele "I apologize for ever doubting your intentions. You truly are a hero. "

show eleanor rags neutral at midright with dissolve

ele "..."
ele "But I should not celebrate this early. I take it the escape will not be easy?"

show rowan necklace neutral at midleft with dissolve

ro "I will explain the plan shortly, but first…"
ro "I fear you will have to suffer through one more indignity."

if delane_abduction == True:
    "He put in front of them a sack he had received from Tarish, and showed the noblewoman its contents."

else:
    "He put in front of them a sack he prepared beforehand, and showed the noblewoman its contents."
    
"Tattered, heavy robes. Jars of mud, fat. Make-up."

show eleanor rags angry at midright with dissolve

"Bindings."

ro "Even at night, I can generally explore the camp without any of the orcs disturbing me."
ro "But I cannot guarantee this will be the case if I am accompanied by a cloaked figure walking behind me."

show eleanor rags neutral at midright with dissolve

ele "So you will have me play the role of a lowly slave, freshly captured."

ro "I am afraid so."

show eleanor rags happy at midright with dissolve

ele "A small price for freedom."
ele "When do we leave?"

ro "Within the next hour. My allies will start their diversion when an opportunity presents itself."

ele "Then I’ll begin my preparations at once."

#hide delane
"Delane grabbed the sack and disappeared behind the doors. Rowan knelt before them, and bringing up a pin, started to pick to lock to her cell." 
"This was way nowhere near his usual area of expertise, but Rowan wasn’t concerned. A long time ago, an old friend explained the basic principles of the art to him, so he wasn’t a complete novice." 
"For the crude locks the orcs employed, he only needed time." 


if delane_abduction == True:
    "His fingers worked relentlessly, while his mind wandered."
    "By the time the sun rises, Delane will know the hero of Karst has betrayed her. She will be in captivity once more, this time at the mercy of someone whose plans were far more wicked than Ulcro’s ever were."
    "She will be stripped naked and used as a public relief toy to appease the camp orcs." 
    "And Jezera's potion will make sure she enjoys every moment of it."
    if avatar.corruption > 69:
        "It will most certainly be quite the show, though he expected it to be orc exclusive."
        "A bit of a shame, to be honest."
    else:
        ro "…"
        "The things he did in the twin’s service…"
        
else:
    #todo
    pass #for now
    
"By the time a distant shout crossed the air, Rowan had unlocked the doors with plenty of time to spare." 
"The cell was open. The distraction has arrived." 
"This was it."


ro "Are you ready?"

ele "Yes."

#escape outfit sprite        

"Delane stepped forward, out of her cell, her disguise ready. With an unflattering, heavy robe hiding her figure, with her hair in disarray and with her face hidden under a layer of dirt, she was almost unrecognizable from the proud lady Rowan knew."  
"She even used the presented makeup to give herself a black eye." 

show rowan necklace shock at midleft with dissolve

ro "Impressive. I believe this will fool most of the orcs we meet."

show rowan necklace happy at midleft with dissolve

ro "Well done."

#escape outfit angry
show eleanor rags angry at midright with dissolve

ele "Please do not praise me for my ability to make myself look like a beaten up slave."

ro "My deepest apologies."

"Delane scoffed, clearly not believing a word he just said. "

show rowan necklace neutral at midleft with dissolve
#escape outfit neutral
show eleanor rags neutral at midright with dissolve

"A moment of reprieve, before both of them put their lives on the line."
"Not wanting to waste any more time, Eleanor presented her hands, and Rowan put the leather bindings on. She would be of no use in a fight anyway, and this way her disguise was far more convincing."

ro "Let’s go."

hide rowan with moveoutleft
hide eleanor with moveoutleft
scene black with fade

scene bg26 with fade
show eleanor rags neutral at edgeright with dissolve
show rowan necklace neutral at midright with dissolve

"One never realized how full of life a camp at night could be, until every person passing by, every gaze met, could herald an untimely doom." 
"He and Delane traversed the camp under the cover of darkness, away from the torches and campfires." 
"Before, Rowan feared Delane would give them away – misstep and trip, likely over some random peg in the ground."
"But the noblewoman proved more competent than he expected. She stepped lightly, without a sound. Anticipating this very day, she must have practiced in her tent, and Rowan was deeply grateful for it. Because of that, he was free to lead her into the shadows whenever possible."
"But these were not always an option. Every now and then, they had to cross an open field, or some often frequented camp path."
"Whenever they did, Rowan straightened his back and put on his fiercest expression, walking with the full authority that came with being the Bloodmeen seneschal." 
"Delane lowered her head and slanted her shoulders, doing her best to appear cowed and demure, as was expected of her."

if check_skill(18, 'intimidate')[0]:
    "Obviously, they attracted some attention. Once, Rowan saw two orcs eye Delane's chest with great interest. One of them even took a step towards them – but when he saw Rowan’s cold glare, he hesitated, and backed off."
    "Not wishing to give the orcs the opportunity to change their mind, Rowan grabbed Delane by the arm and hurried on."
    hide rowan with moveoutright
    hide eleanor with moveoutright
    
else:
    "Most of the time, their deception worked. Orcs walked past them, showing some interest in Rowan’s slave, but his cold glare usually scared them away."
    "Usually."
    "A pair of orcs took great interest in her chest, and despite Rowan’s scowling, started to approach the two humans."
    if delane_abduction == True:
        "Only for a drunk orc woman to crash right into them."
        wo "Ey, watch where yous goin’!"
        femorc "Ya watch where yous standin’!"
        "Taking advantage of the distraction, Rowan grabbed Delane by the arm and quickly hurried on."
        hide rowan with moveoutright
        hide eleanor with moveoutright
    else:
        "The hero broke into cold sweat. This could get real ugly really fast. "
        ro "This way."
        "He turned right, dragging Delane with him. He tried to lose them behind a large tent-"
        wo "Ey! You!"
        "- but failed."
        ro "(Damn it!)"
        "Running was not an option, it would only attract further attention." 
        "He will have to get rid of them quietly." 
        show wild orc neutral at midleft with moveinleft
        show orc soldier neutral at edgeleft with moveinleft
        ro "What do you want. Don’t you see I’m busy?"
        wo "Pretty slave you have here, humi."
        wo "Who she for?"
        show rowan necklace neutral at midleft with moveinleft
        show wild orc neutral at midright with moveoutright
        "One of the orcs approached him, while another reached out for Delane. He grabbed her by the face roughly, but Delane didn’t give him the satisfaction of squealing in pain."
        wo "Hardy. Pretty. All teeth."
        wo "Must be worth a lot."
        "The situation was quickly spiraling out of control. He had to do something right now."
        
        menu:
            "Bluff your way out of this.":
                $ released_fix_rollback()
                show rowan necklace happy at midleft with dissolve
                ro "Oh she is worth a lot."
                ro "That’s why she belongs to warchief Ulcro."
                ro "You two morons are feeling up his property."
                if check_skill(10, 'bluff')[0]:
                    show wild orc neutral at midleft with moveoutleft
                    show rowan necklace neutral at midright with moveoutright
                    "The orc pulled his hand back, as if Delane suddenly caught on fire. Sometimes the truth made for the best lies."
                    wo "Me no mess with Ulcro slave."
                    os "Ye. Move on."
                    show rowan necklace happy at midright with dissolve
                    ro "Thank you. Have a pleasant night gentlemen."
                    hide wild orc with moveoutleft
                    hide orc soldier with moveoutleft
                    "Were the circumstances any different, he’d regret not having a hat he could tip mockingly."
                    show rowan necklace neutral at midright with dissolve
                    "But this was close. Way too close."
                    ele "Won’t they be trouble later? They might tell Ulcro they had seen you with me."
                    ro "And admit they witnessed you escaping and did nothing? "
                    show rowan necklace happy at midright with dissolve
                    ro "I think we’re good."
                    show rowan necklace neutral at midright with dissolve
                    "He allowed himself one short chuckle, then focused on the task at hand. They were nowhere close to being out of the woods yet."
                    ro "Let’s go."
                    hide rowan with moveoutright
                    hide eleanor with moveoutright
                    
                else:
                    show rowan necklace angry at midleft with dissolve
                    "The two orcs looked at one another, and burst out laughing."
                    wo "Ya, as if da warchief let you walk with his slaves." 
                    "Hard way it was then."
                    $ event_tmp['combat roll'] = check_combat(15)[1]
                    if event_tmp['combat roll'] >= 15:
                        os "Att-!"
                        "Before the other orc could shout out an alarm, Rowan took out the knife behind his belt and threw it at his throat."
                        show bg26 with sshake
                        os "Grrlgh!"
                        "Bullseye."
                        "Luck was on his side. The blade hit dead on, stopping his scream midway."
                        hide orc soldier with dissolve
                        show rowan necklace neutral at center with moveinright
                        "Rowan quickly took out his sword and finished off both orcs with a pair of quick strikes. Delane watched form the side without a word, pale with fear."
                        ro "Quickly, help me drag them to the side."
                        "She nodded numbly. Since they were now off the beaten track, they could hope nobody would discover the bodies until they were far away from the camp."
                        ro "Good, let’s go. Go!"
                        hide rowan with moveoutright
                        hide eleanor with moveoutright
                        
                    else:
                        "He drew his sword, and turned to the other orc."
                        os "Attack! We’re being att-gah!"
                        show rowan necklace angry at midleft with moveinright
                        "With a swift strike he cut his throat open. But the damage was done."
                        hide orc soldier with dissolve
                        ro "(Shit!)"
                        show bg26 with redflash
                        hide wild orc with dissolve
                        "He quickly finished off the other orc. Couldn’t let them question him."
                        ele "What now?"
                        "The plan was bust.They were too far away from their designated exit spot to reach it before somebody stops them." 
                        "It was time for plan B." 
                        ro "Don’t worry about it, just follow my lead."
                        "He sheathed his blade and quickly redirected their steps."
                        hide rowan with moveoutright
                        hide eleanor with moveoutright
                        jump desperateEscape
                    
                    
            "Kill them.":
                $ released_fix_rollback()
                "Without a moment of hesitation, Rowan punched the first orc in the face, knocking him out in an instant."
                hide wild orc with dissolve
                $ event_tmp['combat roll'] = check_combat(10)[1]
                if event_tmp['combat roll'] >= 10:
                    os "Att-!"
                    "Before the other orc could shout out an alarm, Rowan took out the knife behind his belt and threw it at his throat."
                    show bg26 with sshake
                    os "Grrlgh!"
                    "Bullseye."
                    "Luck was on his side. The blade hit dead on, stopping his scream midway."
                    hide orc soldier with dissolve
                    show rowan necklace neutral at center with moveinright
                    "Rowan quickly took out his sword and finished off both orcs with a pair of quick strikes. Delane watched form the side without a word, pale with fear."
                    ro "Quickly, help me drag them to the side."
                    "She nodded numbly. Since they were now off the beaten track, they could hope nobody would discover the bodies until they were far away from the camp."
                    ro "Good, let’s go. Go!"
                    hide rowan with moveoutright
                    hide eleanor with moveoutright
                        
                else:
                    "He drew his sword, and turned to the other orc."
                    os "Attack! We’re being att-gah!"
                    show rowan necklace angry at midleft with moveinright
                    "With a swift strike he cut his throat open. But the damage was done."
                    hide orc soldier with dissolve
                    ro "(Shit!)"
                    show bg26 with redflash
                    hide wild orc with dissolve
                    "He quickly finished off the other orc. Couldn’t let them question him."
                    ele "What now?"
                    "The plan was bust.They were too far away from their designated exit spot to reach it before somebody stops them." 
                    "It was time for plan B." 
                    ro "Don’t worry about it, just follow my lead."
                    "He sheathed his blade and quickly redirected their steps."
                    hide rowan with moveoutright
                    hide eleanor with moveoutright
                    jump desperateEscape

            "Let them feel Delane up.":
                $ released_fix_rollback()
                $ change_base_stat('c', +2)   
                show rowan necklace happy at midleft with dissolve
                ro "You should check her tits. She’s hiding a great rack behind those clothes."
                show eleanor rags angry at edgeright with dissolve
                ele "What-?!"
                ele "Ah!"
                "Needing neither encouragement nor, honestly, permission, the orc quickly grabbed Delane under her clothes, roughly feeling her chest."
                show wild orc neutral at midright with moveoutright
                show rowan necklace happy at midleft with moveoutleft
                wo "Haha, nice!"
                wo "Hey, check it out!"
                "The orc called out to his friend, who quickly turned around."
                show rowan necklace neutral at midleft with dissolve
                show bg26 with redflash
                "{i}~swish~{/i}"
                hide wild orc with dissolve
                show bg26 with redflash
                "The first orc didn’t even realize what was happening as Rowan slashed his throat open. The second got as far as opening his mouth to shout a warning, only to find his vocal slightly impaired by eight inches of sharp steel."
                hide orc soldier with dissolve
                ro "Help me hide the bodies. We’re off the beaten track, so they shouldn’t find them until it’s too late."
                ele "..."
                show rowan necklace concerned at midleft with dissolve
                ro "… Sorry for using you as a bait?"
                ele "Apology accepted. Let us never speak of this again."
                show rowan necklace neutral at midleft with dissolve
                show eleanor rags neutral at edgeright with dissolve
                "But they didn’t the time to exchange one-liners. Time was of the essence."
                hide rowan with moveoutright
                hide eleanor with moveoutright


        
scene black with fade
scene bg26 with fade

"One extremely stressful half an hour later, the camp's outer towers were within their sight."
    
    
if delane_abduction == True:
    "They were nearing the verge of Ulcro’s side of the camp. The ground where all three factions bordered one another served as a sort of unofficial “no man’s land”."
    "Near the center of the camp, it was where most faction disputes took place. But at the edges of the camp, the area was largely left unattended." 
    "It was where the guards were least attentive, if the were even present at all."  
    "It was where the wall was either weakest, or literally nonexistent."
    "Once they reached it, Tarish agents could lead them out of the camp without any interruptions."

    show rowan necklace happy at midleft with dissolve
    "Rowan turned around so Delane could see his face, and offered her a reassuring smile. “Almost there”, he mouthed."

    #escape outfit happy
    show eleanor rags happy at midright with dissolve

    "He saw her return the smile, tears forming in her eyes. She always did her best to maintain her composure, and given her background, she usually had little trouble doing so." 
    "But with freedom so close, even she couldn't contain her emotions. She quickly wiped the tears away, and mouthed “thank you” to her hero once again. To her knight in shining armor." 
    "Who was about to hand her over to a rival orc chieftain." 

    ro "(...)"

    "Tarish agents awaited them."

    menu:
        "Deliver Delane to Tarish.":
            $ released_fix_rollback()
            jump tarishEscapeFinale
            
        "Save Delane - find another way out." if avatar.corruption < 80:
           $ released_fix_rollback()
           "He couldn’t do it. Handing Delane over to Tarish was against everything he ever stood for."
           if avatar.corruption > 50:
               "No matter how far he falls, no matter how much of his soul he sacrifices to the twins, some things were simply going too far."
           else:
                pass
           ro "Change of plans. We’re going this way."
           "He quickly changed directions, yanking Delane with him. This was stupid. He knew he was being stupid." 
           "But he’d rather be a fool, than a mindless tool in the hands of evil."
           $ tarishBetrayed = True
           jump desperateEscape


else:
    "They were nearing the verge of Ulcro’s side of the camp, next to Tarish’s ground. Near the center, this would be a fairly lively place. A sort of “no man’s land” where all three factions settled their disputes." 
    "But at the edges of the camp, the area was largely left unattended."
    if delaneEscapePerimeter ==1:
        "And this was where the empty guard tower stood."
        jump escapeSoloFinale
    else:
        "And this was where the Matron told them to go."
        jump escapeMatronFinale
         
        

label tarishEscapeFinale:

if avatar.corruption > 69:
    "“You’re welcome” he mouthed in return, and continued on."
        
else:
    "Rowan tightened his jaw and turned around, so his emotions wouldn’t betray him."
    "It was all for the greater good."

"The no man’s land was the last risky part of their escape. On the other side of it, Rowan saw two cloaked figures - Tarish’s spies, sent to make sure nothing goes wrong."  
"They weren't needed. They went through without any of Ulcro's orcs paying attention to them."  
"The cloaked orcs continued to stare straight ahead. As the moved past them, one of the orcs turned around and started to follow them. Delane, having noticed it, tugged Rowan's cloak in panic."

#escape outfit concerned
show eleanor rags concerned at midright with dissolve

ro "Relax. They’re allies."

"She didn’t look reassured by his words, perhaps subconsciously realizing something was very, very wrong."
"At the edge of the camp, the met another agent, this one waiting with four horses by his side.  Rowan put Delane on one and took the other." 
"For now, they had to keep Delane away from the camp, in case Ulcro decided to turn the whole place upside down before challenging Batri."

femorc "Any complications?"

ro "No, everything went smoothly."

femorc "Good."

"Delane looked like she wanted to add some questions of her own, but in the end kept her silence." 
"They left the camp without hurry. No alarms, no ruckus. From what Tarish told him earlier, it would be some hours before Ulcro learns Tarish has been kidnapped - by Batri, as the agents she placed by his side will tell him."
"Delane still kept to herself, her enthusiasm now gone. With Rowan riding in front of her, and the two agents by her side, she could only follow them into the woods."

if avatar.corruption > 69:
    "She knew. She saw her 'hero' smirking as they left the camp, and she saw the way their “allies” were watching her. This was no rescue."
    "She had been tricked." 

else:
    "She knew. She knew the moment Rowan started to avoid her eyes. This was no rescue." 
    "She was tricked." 

"By the forest, two more orcs awaited them. With chains and a gag ready."

ele "These will not be necessary. I can see now nobody would come to my aid even if I screamed."

#escape outfit neutral
show eleanor rags neutral at midright with dissolve

"She did not raise her voice, only corrected her posture, straightening her shoulders and raising her head high. With her hope shattered, dignity was the last thing she still possessed, and she would not abandon it, even in these circumstances."
"Projecting nobility was one the last thing she still could do." 
"Now, as much as Rowan wanted to spend the rest of the night feeling her judgmental look on his back, his mission was now complete. Everything else was in Tarish's hands." 

ro "Tell your boss I'll be waiting for her message."

femorc "Aye, betta stay out of da camp for now. Things about to get hot."

ro "To put it mildly."

"He was in no mood for banter. Rowan cued the horse forward and left Delane to her fate."

$ delane_status = "tarish"
$ change_base_stat('c', +10)   

return

label escapeSoloFinale:

scene bg26 with fade

"Every step brought them closer to freedom. 100 meters. 80 meters. 50 meters." 
"The tower was clear in Rowan’s view." 
"It was empty." 

show rowan necklace neutral at midleft with moveinleft
show eleanor rags neutral at edgeleft with moveinleft

ro "Keep your head down. We might still get noticed by the other guards."

"She nodded, her entire body tense. Close, so close."

hide rowan with moveoutright
hide eleanor with moveoutright

"But they needn’t bother. No alarm was sounded. The orcs were painfully negligent, as they always were."
"They left the camp, without anyone as much as batting an eyelash at them."
"..."

jump escapeSex


label escapeMatronFinale:

"The Matron waited for them by one of the towers near the edge of Ulcro's part of the camp."
"A group of women accompanied her."

show rowan necklace neutral at midleft with moveinleft
show eleanor rags concerned at edgeleft with moveinleft

"Delane grew tense as the orcs attention focused on the escapee, no doubt afraid they were discovered."

ro "Don’t worry. They’re on our side."

"The Matron’s plan for “escape” proved to be a simple one. She ordered both of them to keep their heads low, mixed with the rest of her allies, while she walked the group out of the camp."
"The orcs had no concept of proper checkpoints. As long as they saw a familiar face they knew they could reasonably trust, they couldn’t care less for what they might have been doing." 
"And so Rowan saw the guards watch their procession, but not a single one showed even a modicum of interest in them." 

ro "Can’t believe it’s that easy…"

orcm "Only because you’re with me. "

"The matron cast a short glance at the noblewoman. With her slave disguise she didn’t look all that impressive, but the matron wasn’t one to get fooled by such tricks." 
"But her eyes narrowed ever so slightly as she kept staring at her." 

orcm "I don’t know what’s more ridiculous."
orcm "That her pussy is worth an entire tribe to the warchief."
orcm "Or that its worth even more to you."

ele "What did she say?"

show rowan necklace concerned at midleft with dissolve

ro "Nothing!"
ro "(Good heavens…) "

scene black with fade
"..."

scene bg3 with fade
show rowan necklace neutral at midleft with moveinleft
show eleanor rags neutral at edgeleft with moveinleft

orcm "We part ways here."
orcm "My companions will make some false tracks. Might throw Ulcro’s men off."

show rowan necklace happy at midleft with dissolve

ro "I think you underestimate how crazy Ulcro is about Delane."

show rowan necklace neutral at midleft with dissolve

ro "He might actually send the entire camp after us."

orcm "Possibly."

"She didn’t look too concerned."

ro "(If they catch us, it’s even better for her.)"

"They were lucky his assessment of her proved right. She was a woman of honour. She would see their deal through."

orcm "Now, don’t take it the wrong way, but I hope we never, ever see each other again."

show rowan necklace happy at midleft with dissolve

ro "The feeling is mutual." 

orcm "Good luck, Rowan."

show rowan necklace concerned at midleft with dissolve

ro "… ?"
ro "(When did I…?)"

ele "Is something wrong, Rowan?"

ro "..."

show rowan necklace neutral at midleft with dissolve

ro "No. Let’s go."

hide rowan with moveoutright
hide eleanor with moveoutright

scene black with fade

"..."

jump escapeSex


label desperateEscape:

$ desperateEscape = True

scene bg26 with fade
show rowan necklace angry at midleft with dissolve
show eleanor rags concerned at edgeleft with dissolve

ro "(Shit, shit, shit!)"

"Thanks to the arranged distraction and the late hour, their path was largely empty. Rowan picked up the pace, coming just short of a proper run."

if tarishBetrayed == True:
    "Every second counted. Someone sounded the alarm, and the orcs were already leaving their tents. Tarish wouldn’t let the escape so easily."
    
else:
    "With the alarm in full swing, every second counted. Many orcs had already left their tents, checking whatever was happening." 
    "None of them stopped Rowan and Delane yet, but it was only a matter of time before someone would."  

"No matter. His destination was already in sight: One of the camp stables." 
"Orc rarely utilized cavalry, but they had some horses at their disposal. As long as- " 

ele "Rowan!"

if tarishBetrayed == True:
    "He noticed the female orc at last possible moment. Dagger in hand, she jumped him, trying to strike him directly in the heart."
    if check_stat(25, 'strength')[0]:
        show bg26 with sshake
        "Without any time to dodge, he had to block the attack. Despite the massive difference in power between them, he somehow managed to grab her wrist with both hands, stopping the blade a mere inch from his body." 
        "The orc growled in fury and put her entire body into the push, but with the element of surprise gone she stood no chance." 
        ro "You-! "
        "He twisted her arm and struck her under the chin. Her guard dropped, and he swiftly exploited the moment to wrench the dagger out of her hand and stab it into her neck."
        ele "Rowan, are you-"
        ro "I’m fine, go, go!"
        
    else:
        "Without any time to dodge, he had to block the attack. He grabbed her by the wrist at the last possible moment-" 
        show bg26 with sshake
        show bg26 with redflash
        "Only for the orc to push her entire body forward, overpowering his block and stabbing him in the shoulder."
        ro "Ngh-!"
        ele "Rowan!"
        femorc "Did you really think you- AARGH!"
        "He pushed his fingers into her eyes with no remorse. She didn’t let go, but after he followed with a punch under her chin, her gripped finally loosened."
        show bg26 with redflash
        "He only needed a moment to draw his own dagger out and finish the job."
        ele "Rowan, you’re bleeding!"
        "The wound burned like hell. The blade went in deep - he felt it graze a bone." 
        "But he didn’t have time to evaluate the damage. He ripped it out, suppressing a cry of pain, and tossed it away." 
        ro "It’s - hrm - nothing."
        ro "Don’t just stand like that, go, go!"
        $ delaneEscapeWound = True
        
else:
    show wild orc neutral at edgeright with moveinright
    "Finally one of the orcs proved to be smart enough to connect the dots. Two axes in hand, he jumped Rowan seemingly out of nowhere."
    "With no time to dodge, Rowan grabbed his assailant by the wrists, stopping the attack with ease. The enemy orc smaller than most warriors of his kind, so Rowan should be able to- "
    show bg26 with sshake
    "The orc slammed his head into Rowan’s face."
    if check_stat(10, 'strength')[0]:
        ro "Nnn-!"
        "Despite the pain, Rowan stood his ground, and unceremoniously shoved his knee right into the orc’s groin."
        "His opponent proved far less resilient than he was. He hunched over, giving Rowan just enough time to wrench the axe from the orc’s hand and embed it into his skull."
        hide wild orc with dissolve
        ele "Rowan, are you-"
        ro "I’m fine. Go, go! "

    else:
        "The attack wasn’t strong enough to knock him out, but it did disorient him. He felt his grip weaken-"
        ele "Look out!"
        "-and the orc wrenched his hand free."
        show bg26 with sshake
        show bg26 with redflash
        "The axe struck his shoulder, easily piercing his armor, sinking deep into his body."
        ro "Nnh-! You-! "
        "The pain helped him come to his senses. He smashed his elbow into the orc’s face, returning the favour." 
        "The orc stumbled back, giving Rowan enough time to draw his sword and skewer his opponent open."
        ele "Rowan, you’re bleeding!"
        "The wound burned like hell. The blade went in deep - he felt it graze a bone." 
        "But he didn’t have time to evaluate the damage. He ripped it out, suppressing a cry of pain, and tossed it away." 
        ro "It’s - hrm - nothing."
        ro "Don’t just stand like that, go, go!"
        $ delaneEscapeWound = True


"Their fight lasted seconds, but it was enough to have orcs glancing in their general direction. They were running out of time."
"With a couple of swift jumps, Rowan was already at the stable’s entrance. With two swift strikes, he dispatched the still confused guards, while Delane caught up to him." 

ro "Can you ride?"

ele "A little- "

show eleanor rags neutral at edgeleft with dissolve

ro "Yes!"

"Not good enough. They’d need one horse then."
"He quickly took stock of what was available to them. Their choice was fairly limited, but it didn’t matter. He found the largest, strongest stallion he could get his hands on, and led them to it." 

ro "We’ll take this one. I’ll ride."
ro "We only need to put some distance between us and the camp, then we’ll go by foot and lose them in the mountains."

"He cut Delane’s binding, and ordered her to sit behind him."

"Hold tight."

scene bg26 with fade
show rowan necklace angry behind bg26

"They burst out of the stables, trampling the two orcs who were unlucky enough to a) Be born into the same age as Rowan Blackwell, and b) Stand in his way."

ro "Keep your head low! And no matter what, don’t let go!"

"The passed the guard towers, and took a straight line to the woods. He was Rowan Blackwell. As long as he had time, he would be able to cover their tracks-"
"A lone arrow struck the ground next to them. Another went by his ear." 
"The next one grazed his horse." 

ro "What the- Calm down boy, calm down!"

if delaneEscapeWound == True:
    "He tried to rein the horse in, but the moment he pulled the straps, his left arm exploded in pain."
    "The horse reared up, making them an easy target for the orcs." 
    jump desperateEscapeFail
    
else:
    if check_skill(15, 'survival')[0]:
        "With titanic strength, he pulled the reins in, stopping the stallion from rearing up."
        jump desperateEscapeSuccess
        
    else:
        "He tried to rein the horse in, but the wild beast would not listen. The horse reared up, making them an easy target for the orcs."
        jump desperateEscapeFail
    
label desperateEscapeSuccess:

ro "Giddy-up!"

"Arrows continued to rain down on them, but few orcs every practiced archery." 
"Not a single one found its mark, and soon Rowan and Delane were out of their range."
"…"

jump escapeSex

label desperateEscapeFail:

show bg26 with sshake
show bg26 with sshake
show eleanor rags concerned behind bg26

ele "Nngh! Nn!"

ro "Delane?"

ele "I’m f-fine!"
ele "Go!"

"Her voice wavered. Rowan feared the worst." 
"Arrows continued to rain down on them, leaving hero no time to worry about anything else. With titanic effort, he managed to get the horse under control, and direct it at the nearby force." 
"All he needed was time. Then… He’d make sure everything is okay." 
"Delane’s grip weakened."
"…" 

jump delaneDeath


label escapeSex:

scene bg31 with fade

show wild orc neutral at center with moveinleft
show orc soldier neutral at edgeleft with moveinleft

wo "Tracks went dis way."

"Three Orc trackers looked around the wide stretch of rocky hills that sat nearly five miles from the orc camp. Surely trackers had gone other directions as well, all in an attempt to discover where their lost prisoner had gone."
"And perhaps it would have worked, if they were not trying to find one of the foremost trackers and scouts of the age."

os "Many caves. Lots ‘o hidey holes."

wo "Maybe. But, many caves to check. Many places to search still."

"The orcs somberly agreed to move on. There was just too little they could do here."

hide wild orc with moveoutright
hide orc soldier with moveoutright

"In secret, eyes watching from a strategically chosen cave watched their departure. It meant safety."

show eleanor rags happy at edgeleft with dissolve
show rowan necklace concerned at midleft with dissolve

ele "Are they gone?"

ro "For now. They’ve moved on, but the possibility of them doubling back is real."

if desperateEscape == True:
    "The fact that they sent parties out to track them was not of much concern. He’d planned for this ahead of time, and his extra time gained from not raising the alarms allowed a more deliberate escape with fewer tracks. The odds of discovery were quite low."

    if delaneEscapePerimeter == 2:
        "Especially with the matron’s fake tracks. It was a miracle they even managed to get this far."
        
    else:
        pass
else:
    pass
    
"Delane slumped against the side of the cave wall. The two had set up a small camp a bit deeper in, where any light they’d make wouldn’t be spotted from the outside."

ro "We need to remain here for the next few hours. Until dusk at least. Moving in the day time is too dangerous."

"She nodded silently to Rowan’s suggestion and followed him deeper into the cave where their campfire waited." 
"The two huddled up close to each other for warmth in the dark bowel of the cave."

ele "I suppose...I’m free now aren’t I?"

ro "I suppose you are. How does it feel?"

"Delane paused to consider it. The weariness of the night still weighed on her."

ele "It would feel a good deal better if I were not trapped in a cave. Out one prison, into another."

show rowan necklace happy at midleft with dissolve

ro "You’re never happy."

"Delane chuckled."

ele "I suppose the distinction is that my former prison could only be escaped by bedding an orc. This one I merely have to wait until nightfall without making too much of a fuss."

ro "An impossible task. I know."

"She elbowed him in the ribs."

ele "Still, I have you to thank for all of this. Truly. You’re everything the tales told and more."

show rowan necklace concerned at midleft with dissolve

if tarishBetrayed == True:
    "Rowan smiled weakly. She couldn’t be further from truth. She’ll never know how close he was to handing her over to Tarish." 
    "In the end, he did the right thing. He proved the man they called the Hero of Karst was someone more than shunned, lowly general, or a slave to demonic forces."
    "Proved to Delane, and to himself." 
    "But he couldn’t banish the dark thoughts that now plagued his mind. If he was this close to falling off the wagon now, how will he handle the trails that laid ahead? The necklace still hanged from his neck like an anchor that dragged him further into the darkness. He was still chained to the twins." 
    "Will he be able to make the right call next time as well?"

else:
    if avatar.corruption < 30:
        "Rowan smiled weakly. Even hearing someone say that to him was something of a surprise and something of a gut punch. He’d been the captive of the twins for so many months now. And before that, he’d been an outcast."
        "For just this brief moment, Rowan was the hero of the six realms again. Not the man who’d done nothing as his world burned around him."
        "But, then that moment passed."

    else:
        "Rowan smiled weakly. The notion of what Lady Delane was saying struck him as almost absurd. He saved her to be sure. He might put on the face of the hero everyone had once called him. But, she didn’t understand him. She didn’t understand what he had done to get to this moment."
        "She didn’t understand what he would be willing to do to keep muddling through."
        "What she said came from a place of gratitude, but to Rowan’s ears it all sounded like were his own lies."

"After that the clock started to tick away. There was plenty of firewood, and Rowan had prepared food. So they were never in the dark nor miserable. But, the most tiresome thing was the monotony. On a few occasions, Rowan stealthily checked the entrance to determine time of day."
"What had first been pleasant conversation turned into long stretches of quiet. They were both too weary and had their mind too focused on the matter of making sure they got away from the orcs."
"But, it was not the only thing that their minds were focused on. Or at least it didn’t seem to be for Lady Delane." 
"Rowan was surprised when, about three hours into their time in the cavern, Lady Delane rested her head on his shoulder. The intimacy of the contact was surprising. But, he did not shake her off or otherwise dissuade her. She had been through a lot."
"But, amidst the dim light of the fire, Rowan could see the eyes she made towards him. They were not merely appreciation."
"More time passed in silence. It was only broken when Rowan felt a hand on his leg. He turned to face Eleanor and found her face perilously close to his."

ele "You’ve done so much for me. You helped me maintain my resolve. You gave me something to hope for. And now, you’ve gone a step further. You saved me."

ele "Had it not been for you, I would probably have died back at that encampment."

"Her hand slid up his leg."
"The two exchanged a glance. Her intentions could not have been any clearer had she said them out loud. If he wanted this, she would let him have her. The only question was if he wanted this."

menu:
    "Refuse her.":
        $ released_fix_rollback()
        "Before it could get any further, Rowan shook his head and carefully removed Lady Eleanor’s hand from his leg. He was here to rescue her, not here to fuck her. There was just no way he could bring himself to do that."
        "She blinked twice at this sudden refusal, but didn’t press the issue. This was a terse situation. She would understand."
        jump escapeSexConclusion
        
    "Sleep with Delane.":
        $ released_fix_rollback()
        $ eleanorCaveSex = True
        "Part of Rowan’s brain reminded him of their situation. They were alone in the woods with no backup and if discovered would be in grave danger. But, they were relatively safe here in the cave. The chance of being overheard would be minimal."
        "They had time to kill. Why not have some fun with it?"
        #noble reward CG#1
        scene black with fade
        show eleanor rags happy behind black
        show rowan necklace aroused behind black
        "Rowan didn’t do anything to dissuade the movement of her hand, even as it crept further and further up. At the first brush of her fingers against the exterior fabric covering his crotch, he exhaled sharply."
        ele "I just want to thank you for everything you’ve done for me. I want to…"
        "She slowly unlaced his breaches, and pushed her right hand all the way to his cock. He groaned out at the feeling of her delicate skin against his cock."
        ele "I want to give you some kind of token of my appreciation…"
        "Behind them, the shadow on the cave wall reflected their movement. Delane’s shadow grew closer to his until their distinct outlines became hard to see. But, when she put her hands to his cock, the way he leaned backwards re-established their outlines."
        ro "Ah…"
        "He felt the friction of her hand as it started a pumping gesture. In moment, he went from semi erect to straining with hardness. In the back of his mind he idly realized that this probably wasn’t the first man she’d jerked off."
        "But, curiosity as to the sexual escapades of a young lady in waiting took a back seat behind the raw sensation of it."
        "Stroke. She leaned in closer, eagerly awaiting his reaction. Stroke. His eyes fluttered slightly. Stroke."
        ro "Wait."
        "Delane’s hand paused in place."
        ro "Not your hand."
        "Lady Delane swallowed softly. By all rights he was well out of line. Even engaging in any sexual activity with a noblewoman was supposedly out of bounds for a commoner. Asking for penetrative sex all the more so."
        "Yet, Delane’s response was to nod. Even to start working the dirty tags that were as close as she had to an outfit off of her head. Apparently, class distinctions mattered little to two aroused traumatized people hiding in a cave."
        ele "Okay. Not my hand. But, you’re going to have to lay back, alright?"
        "Rowan had already been leaning backwards, but at Lady Eleanor’s request he adopted a position on his back, cock still erect and now pointed upwards. One presumed that the lady had learned to ride."
        #noble reward CG#2
        scene black with fade
        show eleanor naked aroused behind black
        show rowan necklace aroused behind black
        "Lady Eleanor stood up. Her body shone in the fire light with sweat. Then, with some apprehension she lowered herself down slowly. He felt something wet and hot on the very tip of his cock, and as she lowered herself the feeling crept down with her."
        "His hands dug into her hips. He saw the expression on her face shift to a gasp. It too was framed by the firelight. Now the shadow on the wall showed a single figure, albeit one with a wide base."
        ele "F...fuck."
        "Her hips rolled and bucked. At first slowly, but it did not take long for her to find her rhythm. This motion too, while not practiced, had the finesse of someone who had done it before. Before long she was bouncing up and down on his cock in a steady rhythm."
        "She cried out loudly, rolling her head back."
        ro "We have to...keep quiet…"
        "She blushed."
        ele "Right. Sorry."
        #noble reward CG#2 var 2
        scene black with fade
        show eleanor naked aroused behind black
        show rowan necklace aroused behind black
        "The brief blip threw off her rhythm, but it only took a few seconds for her to regain the momentum. Rolling and bouncing as she threw herself down at his cock. Only this time with a single hand covering her mouth to prevent her from being too loud."
        "Rowan’s nails dug into her body. Every roll of her hips brought with it more pleasure. More friction. More of the addictive motion of his cock inside of her. He too had to stifle noises."
        "Starkly lit by the flicker of the campfire. Punctuated only by what few moans and grunts they let out their hushed lips. The movement of their bodies was desperate, and weary. The sex of the reprieved and the scared."
        ele "I’m going to…"
        ro "...Shh"
        "Lady Delane threw both hands to her mouth to cover the long moan she was about to release. She started to spasm, and threw herself downward on him with one last burst of energy. A burst that was, in-turn, just enough to send him over the edge with her."
        "He gasped, and felt his load release. A moment later, he slumped down on the ground, and she collapsed forward on to him. Their breaths rose and fell almost in tandem and her breath touched his neck."
        ele "I’ve been waiting for you to do that since the first time you visited."
        ro  "That early?"
        "Delane gave a weak chuckle."
        ele "Will you not excuse a lady her knight in shining armor?"
        ro "My lady, I’m no knight."
        ele "A good thing too. If you were, you might have known better than to risk bedding someone above your station."
        "The two curled up together. Rowan only bothered to move when he saw how low the fire had gotten. The two were pressed together for the entire remainder of the their time together in the cave."
        
 
label escapeSexConclusion:

scene black with fade
show rowan necklace neutral behind black

"After enough time had passed, Rowan checked the entrance of the cave again. Now the time was ripe. Dusk had settled in and visibility would be low. Now it was time to move."

ro "Move fast, keep quiet. Don’t talk unless absolutely necessary. If we keep a steady pace we should be to a keep by nightfall."

scene bg31 with fade

"The following hours felt ploddingly slow, as every shadow behind every tree and every leaf crunch signaled a possible discovery. But, in truth it was rather dull. Slow careful movement, high strung nerves, and an absence of encounters."
"As dawn approached, Rowan spotted a small keep in the distance. His intended destination. Hardly a powerful fortress, but it would due for making sure Delane reunited with her family safe and sound."

show rowan necklace happy at midleft with dissolve
show eleanor rags happy at edgeleft with dissolve

"He stopped her by the side of the road."

ro "This is where we part ways. I need to return so my absence is not felt strongly. But, you need to continue on. If possible, all the way to Rastedel. They need to know that the situation out in the provinces are dire."

"She nodded stoically, but he caught the flash of sadness in her eyes."

ele "I will do as you bid. No one has more experience with the rampaging orcs than I."

"Rowan sincerely doubted that was true."

ele "And the prospect of reunification with my family is one I cannot pass up for a moment."
ele "What about you though? Will you be alright?"

ro "You don’t have to worry about me. I’m a survivor. I’ve lived through a lot already. I imagine I’ll be in Rastedel again before too long. We can talk then."

"Delane gave a soft nod then surprised him with a long hug. When it was released, Rowan turned and bade her a wordless farewell. His mind was already racing with other thoughts."

show rowan necklace concerned at midleft with dissolve

"The easy part was over. Without delane, his attempts to co-opt the various Orcish factions were in dire jeopardy. Back at Bloodmeen, Andras and Jezera would almost certainly be angry about the situation, even if they didn’t understand how critical a role Rowan had played in the failure."
"Still, he walked back with his head a bit higher then it had been in a long time. He was a little bit more like the man who’d first come to Bloodmeen such a deceptively short time ago."

$ delane_status = "free"
$ change_base_stat('c', -10)   
$ change_base_stat('g', -10) 

return

label delaneDeath:

scene bg31 with fade

show wild orc neutral at center with moveinleft
show orc soldier neutral at edgeleft with moveinleft

wo "Tracks went dis way."

"Three Orc trackers looked around the wide stretch of rocky hills that sat nearly five miles from the orc camp. Surely trackers had gone other directions as well, all in an attempt to discover where their lost prisoner had gone."
"And perhaps it would have worked, if they were not trying to find one of the foremost trackers and scouts of the age."

os "Many caves. Lots ‘o hidey holes."

wo "Maybe. But, many caves to check. Many places to search still."

"The orcs somberly agreed to move on. There was just too little they could do here."

hide wild orc with moveoutright
hide orc soldier with moveoutright

"In secret, eyes watching from a strategically chosen cave watched their departure. It meant safety. It meant hope."

"And the latter in particular was in short supply." 

show rowan necklace concerned at midleft with dissolve

ro "They’re gone."

"A wheezing, distant sound from somewhere deeper in the cave was his only response. Delane couldn't walk up to see the orcs leave." 
"She barely had the strength to stay conscious."  
"... He failed. He promised to get her to safety, and he failed. During their escape, two arrows struck her back. One he was able to remove." 
"The other reached her lung."

if check_skill(10, 'survival')[0]:
    "He cursed his medicinal knowledge. He knew removing the arrow would likely cause the lung to collapse, and that, adding to Delane’s already extensive injuries, would quickly kill her." 
    "He needed somewhere she could rest, and a trained Medicus that could help him stabilize her condition." 
    "But neither of these were an option to him."  
    
else:
    "He knew some first aid, but a wound like that… Was beyond him. She needed a trained Medicus." 
    "And there were none in sight." 

"Swallowing heavily, he walked further into the cave, where he set their camp. He had Delane rest on the side, close to the fire."

ro "Try not to say anything. You’ll only make it worse. "

"Again, the wheezing sound was his only response, but this time he saw her glare, and could almost hear the cutting remark. All the months of captivity could not break her spirit."
"And neither would death." 
"…"
"He couldn’t tell her. He didn’t have the heart." 
"But she felt it coming. She would not leave this cave alive." 

if tarishBetrayed == True:
    "And it was his fault. If he didn’t side with Tarish, if he didn’t waver in his convictions – maybe things would turn out differently."
    $ change_base_stat('g', +5) 
    
else:
    "And it was his fault. If only he was better. Faster. Stronger." 
    "If only he was the hero everyone took him for. "

"He knelt besides her. They had plenty of food ready, but she refused to eat any of it. She mostly just stared into nothingness, occasionally grimacing." 
"He couldn't leave her like that. He reached for one of the water bags, and brought it to her lips."  

ro "Drink. You need to stay hydrated. "

show eleanor rags concerned behind bg31

if ulcro_path > 1:
    "She shook her head slowly. She didn’t have the strength for anything more."
    ele "Should’ve… "
    "Her face contorted from the pain, but she refused to surrender to it. "
    ele "Gone… With… "
    ele "Ulcro… "
    "Her foggy eyes stared at him accusingly. Rowan put the water bag in her mouth, forcing her to drink at least a little bit. "
    $ change_base_stat('g', +3)
    
else:
    "She showed no signs of registering the water in Rowan’s hand. Her lips moved, but not to drink from it."
    ele "Wanted… "
    "Her face contorted from the pain, but she refused to surrender to it."
    ele "To… Do…"
    ele "So… Much…"
    "Her foggy eyes found his, searching for some reassurance. Rowan tried to smile, only to feel it falter." 
    "Her own mouth twitched slightly. She appreciated the attempt, if anything." 
    "Gently, he put the water bag in her mouth, making her drink at least a little bit." 

ro "You will get out of here, my lady. "

show rowan necklace happy at midleft with dissolve

ro "You will return to your family."
ro "You will yet decide what you want to do with your life."
ro "I can’t have you giving up here. "
ro "That would be unbecoming for Lady Eleanor of House Delane."

"His words, once spoken with such gusto, now sounded hollow even to him. But he had to try and bring her spirits up." 
"He saw her eyes water. She closed them, and tried to turn her head away. With no success."

hide rowan with dissolve

"Rowan turned around, deciding to give her some privacy."
"She was too proud to cry." 
"So he pretended he didn’t hear her."

scene black with fade

"..."

scene bg3 with fade

show rowan necklace neutral at midleft with dissolve

"When the sun had risen, Delane was dead."

show rowan necklace neutral at center with moveinleft

"He put the fire out, then took out a handkerchief and his water bag."
"Delicately, he cleaned Delane’s face. She still had the make-up from the night before. It did not become her." 
"Neither did the rags he had her wear for their escape, but he didn't have anything better at hand."  
"She’d hate being buried like that." 

ro "..."

"He needed a grave for her. He didn’t bring a shovel." 
"A stone mound would have to do." 

hide rowan with moveoutleft

"The orcs were gone, chasing other leads. The mountainside was empty."

scene black with fade

"For the next several hours, he wandered around the empty caves, looking for rocks, both big and small."
"Finally, he had gathered enough to make a modest pile."

scene bg3 with fade

show rowan necklace concerned at center with dissolve

"After some consideration, he ended up carrying her body outside, to the edge of the nearby forest."
"Delane liked to stroll the family gardens in the mornings. She’d enjoy being buried under the open sky, rather than in a cave." 
"…"
"Stone after stone, he put the mound together. One lifeless rock after another, placed on Delane’s lifeless body."  

ro "..."

"An hour later, the mound was ready. Only Delane’s head was visible from the impromptu grave." 
"One last thing remained." 
"Rowan cleared his throat." 

ro "Delane-"

"His voice broke. He cleared his throat again."

ro "Delane... "

"No, wrong. He cleared his throat again." 

show rowan necklace neutral at center with dissolve

ro "Lady Eleanor of House Delane was- "

menu:
    "A remarkable woman.":
        $ released_fix_rollback()
        ro "A woman of incredible character. Strong. Perceptive. Intelligent."
        ro "She showed unparalleled resilience in the face of adversity, unwilling to betray her ideals."
        
    "A noble worthy of her title.":
        $ released_fix_rollback()
        ro "She was young, and sheltered."
        ro "But unlike many in her position, she didn’t look down on others. She understood the responsibilities that came with her lineage, and did her best to rise to the occasion."
        
    "Someone who deserved better.":
        $ released_fix_rollback()
        ro "A wonderful woman, taken from us far too early."
        ro "With her wit and strength she would have made the Delane house proud, but now..."

ro "The world is a lesser place without her."
ro "All who knew her, would admire- "

menu:
    "Her vast knowledge.":
        $ released_fix_rollback()
        ro "She loved books. She loved to read."
        show rowan necklace happy at center with dissolve
        ro "She once remarked she would kill for a book, and I have no doubts she would make true of this threat, had she stayed in captivity any longer."
        show rowan necklace neutral at center with dissolve
        
    "Her cutting tongue.":
        $ released_fix_rollback()
        ro "If Ulcro understood enough of human etiquette, her offhanded jabs would quickly get her beheaded."
        ro "I imagine she would dryly complain how the low quality of the executioner's axe hardly beseeches a woman of her status."
        
    "Her incredible bravery.":
        $ released_fix_rollback()
        ro "Despite the looming threat, the only time I ever saw fear in her eyes, was when she thought of her parents, and their whereabouts."
        show rowan necklace happy at center with dissolve
        ro "Well, and maybe when we sneaked through the camp, but that’s understandable."
        show rowan necklace neutral at center with dissolve
        
ro "..."
ro "I’ll never forget how-"

menu:
    "She ordered him to save her.":
        $ released_fix_rollback()
        show rowan necklace happy at center with dissolve
        ro "“Whether you came here to rescue me or not, it is your mission now!”"
        ro "Haha… The nerve..."
        
    "Her face lit up every time she saw him visit.":
        $ released_fix_rollback()
        ro "All week, all you did was wait for my arrival. You tried to be nonchalant, but your smile betrayed you in an instant."
        ro "…. I’m sorry I couldn’t spend more time with you."
        
    "She reminded him what it meant to be a hero.":
        $ released_fix_rollback()
        ro "I knew the consequences of going against the twins would be dire, but… "
        ro "I just couldn’t leave you there."
        ro "Nobody gets left behind."
        
show rowan necklace concerned at center with dissolve

ro "…"

menu:
    "<Say a prayer to Solansia>":
        $ released_fix_rollback()
        ro "May your soul find peace with the Goddess, Delane."
        
    "<Say nothing>":
       $ released_fix_rollback()
       ro "May your soul find peace in the afterlife, Delane."
       
ro "..."

"He didn’t know what else to add." 
"He took the last set of stones, and placed them over Delane's face, covering her up completely."  
"It was over." 
"Another ally gone." 
"..."
"After they had slain Karnas, he thought he was putting these times behind him."   
"That he would never again be responsible for his shortcomings killing someone important to him."  
"Now…" 
"The village elder was dead…" 
"And so was Delane." 
"How many more?" 

ro "..."

menu:
    "He must never forget what he fights for." if serveChoice != 4:
        $ released_fix_rollback()
        "This was only the beginning. As long as he serves the twins he will have to take further and further risks in order to protect that what is most precious to him."  
        "This time, he failed." 
        "He will not do so again." 
        $ change_base_stat('c', -5)
        jump delaneDeathConc

    "It will only get worse. He must steel his heart.":
        $ released_fix_rollback()
        "This was only the beginning. He will likely have to sacrifice more, much more, as long as he serves the twins. He can’t despair over every life lost."
        ro "(I will not let this break me)."
        $ change_base_stat('c', +5)
        $ change_base_stat('g', -5)
        jump delaneDeathConc
        
    "… It’s too much …" if avatar.guilt > 70:
        $ released_fix_rollback()
        ro "..."
        "Bound by magic, under constant threat of death and torture..." 
        "His wife sharing his misery, her only crime being married to the man she loves." 
        "Bringing pain and agony wherever he arrived..." 
        "He was supposed to be a hero…"
        "But he couldn’t save even a single soul." 
        ro "..."
        "His eyes wandered to the knife by his side. His hand drew it almost of its own accord." 
        "What was the point in all of this? He was only making the situation worse." 
        "Maybe…" 
        "Maybe it would be better to just…"
        "End it?" 
        menu:
            "It’s for the best.":
                $ released_fix_rollback()
                "He aimed the blade at his heart." 
                "It would be quick. He would not miss." 
                "The hero of legends never missed." 
                ro "(I’m sorry everyone.)"
                ro "(It’s for the best.)"
                ro "(Good luck, Alexia.)"
                ro "(I love you.)"
                show bg3 with sshake
                show bg3 with redflash
                scene black with fade
                "..."
                $ renpy.full_restart()
                
            "…. No.":
                $ released_fix_rollback() 
                "His hand shaking, he put the knife away." 
                "He couldn’t."
                "Despite everything…"
                "This was not the end."
                $ change_base_stat('c', +5)
                $ change_base_stat('g', -5)
                jump delaneDeathConc

label delaneDeathConc:

"He took one last moment to take a look at Delane’s grave." 
"With any luck, the orcs won’t find the mound and her body will be left undisturbed." 
"It was all he could hope for." 
"…"

scene bg31 with fade

"For the remainder of the week, he ended up wandering across northern Rosaria, avoiding all settlements and people. He needed to clear his head. At least a little bit." 
"Soon enough, the amulet called."
"The twins awaited." 

$ delane_status = "dead"
return

