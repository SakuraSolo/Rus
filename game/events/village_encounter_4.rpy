#Orc wants to lead
#Can trigger on either choosing to capture, or destroy a village

#randomly determine type of orc:
#flag 1 - Competent orc
#flag 2 - Foolish orc

init python:
    event('orc_wants_to_lead', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)
    event('old_hero_destroy', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=("week >= 4",'old_hero_event==False'), run_count=1, group='village', priority=pr_map_res)
    event('old_hero_occupy', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=("week >= 4", 'old_hero_event==False'), run_count=1, group='village', priority=pr_map_res)
    event('old_hero_trade', triggers=('map_res_3', 'map_res_4', 'map_res_5',), conditions=("week >= 4", 'old_hero_event==False'), run_count=1, group='village', priority=pr_map_res)
    #event('a_cheating_elder', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)


label orc_wants_to_lead:
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve

if renpy.random.randint(0,10) > 5:
    $ competent_orc = True
    $ foolish_orc = False
else:
    $ competent_orc = False
    $ foolish_orc = True

"As always, the strike force arrived incredibly quickly."

show rowan necklace shock at midleft with dissolve

"... So quickly in fact, that Rowan sometimes wondered if Jezera could actually open portals everywhere, but had him use predetermined sites just to mess with him."
"On one hand, it would be both incredibly petty to do, and so short sighted and enormously harmful to their overall efforts that only a power-tripping teenage girl could consider it a good idea."

show rowan necklace neutral at midleft with dissolve

"On the other hand… It would indeed be both incredibly petty to do, and so short sighted and enormously harmful to their overall efforts that only a power-tripping teenage girl could consider it a good idea."
"Rowan rubbed his temples and decided that maybe it was better not to think about it."

"Regardless of whatever space bending abilities his orcs possessed, they were now present, ready to receive their orders – but before Rowan could give them out, one of the orcs stepped forward and interrupted him quite rudely."
"The orc demanded an opportunity for him and his people to prove themselves to their demon overlords. Rather than follow Rowan's lead, he alone wanted to command the group, to show the twins they didn’t need Rowan to babysit them."
"Usually, while he rarely took to the field himself, it fell to Rowan to devise the “battle plan” when attacking keeps and villages. In case of the villages, the term had to be used quite loosely."
"Rosaria’s settlements consisted almost exclusively of peasants (as one would expect) and had next to no serious fortifications."

if avatar.corruption > 74:
    show rowan necklace angry at midleft with dissolve
    "A prospect that was growing increasingly tempting by the moment."
    "Why, exactly, was it his bloody responsibility to make sure the orcs didn’t burn anything of worth, or allow the villagers to escape?"
    "Why was he walking around the entire bloody realm, locating settlements that anyone with a functional eyesight could easily locate on a Goddess damned map?"
    "The twin’s told him they needed him to help them manage the castle, so why exactly was he overseeing every single, no matter how fucking minor task, instead of focusing on stuff that’s actually important?!"
    "Oh, that’s right."
    "Because Andras was too fucking busy trying to fuck his wife to train his fucking troops properly, while Jezera’s concept of leadership consisted of a) Fucking the people she likes, and b) Stabbing the people she doesn’t like."

    if serveChoice == 4:
        "Rowan couldn’t believe he actually allowed himself to be convinced by two amateurs who think they’re hot shit just because their father was the literal fucking avatar of destruction."

    else:
        "He should probably be happy at how completely inept the twin’s were, but the moment the only emotion he could feel was his growing desire to smack the orc in front of him with something heavy, preferably a war-hammer."

    ro "“(...)”"

    show rowan necklace happy at midleft with dissolve
    ro "You know what? I have a better idea."
    "Smiling pleasantly, Rowan addressed the now confused orc."
    ro "How about you all charge into the village straight away, alright?"
    "For every piece of equipment damaged in battle, I’m cutting 5 fingers. Chosen out random. For every villager you kill, I’m sending you for 2 months of excavation works. For every five villagers dead, I’m executing one of you randomly."
    ro "Everything clear? Alright, go charge."
    "The orcs stared at him, dumbstruck."
    show rowan necklace angry at midleft with dissolve
    ro "I SAID CHARGE YOU DIMWITS!"
    show rowan necklace happy at midleft with dissolve
    "That did the trick. The orcs raised a couple of careful war cries, then rushed in the direction of the village."
    "..."
    show rowan necklace concerned at midleft with dissolve
    "..."
    show rowan necklace shock at midleft with dissolve
    ro "(Oh Goddess, what have I done?)"
    "Rowan watched, terrified, as the village descended into the usual chaotic infighting. Even from where he stood, a fair distance away from the settlement, he could hear the shouts and cries coming from the both sides."
    "It shouldn’t be happening like this… It shouldn’t..."
    show rowan necklace concerned at midleft with dissolve
    ro "..."
    "This shouldn’t have happened. He’d never… Let himself lose control like that. It wasn’t like him to let himself slip."
    "He was spending too much time with the twins. Their casual cruelty and disregard for others was starting to rub off on him."
    "How much longer till outburst like that become a common occurrence?"
    show rowan necklace neutral at midleft with dissolve
    "He couldn’t allow that. He had to get a hold of himself."
    "… Not that committing atrocities with a steady heart was any better."
    "Before Rowan could spiral into self-deprecation any further, he noticed an orc in the front signaling him the village was secured."
    "Self loathing could wait. It was time to assess the damage."

    scene bg1 with fade
    "The attack went… Well."
    "His makeshift threat worked. There were far less casualties among the villagers than usual."
    "But also far more peasants managed to escape. And his orcs… Looked beaten up, and thoroughly displeased with the outcome."
    "Rowan didn’t allow his inner conflict to show, and started giving up orders to clean up the whole mess."
    "He would ponder on his outburst later."
    $ change_base_stat('g', 5)
    $ change_base_stat('c', -3)
    $ castle.morale -= 10
    #village is captured or destroyed based on player choice
    return

else:
    if avatar.corruption > 49:
        "However, letting the orcs do as they pleased usually resulted in unnecessary damage and pointless loss of life. As annoying as it was to micromanage-"
        "-which is to say, pretty annoying-"
        "-doing so ensured the best possible result for every raid, loot wise."

    else:
        "However, letting the undisciplined orcs do as they wanted usually resulted in pointless deaths. Even if he had to do some despicable acts in the service of the twins, he could at least ensure innocent people wouldn’t die needlessly."

    "So Rowan wasn’t all too keen on letting some orc he knew nothing about lead the raid without his supervision. But giving the orcs a chance would no doubt improve the orc morale…"
    "And if the orc leading them proved to be competent, he could be a valuable asset to their army"

    menu:
        "Let him lead.":
            $ released_fix_rollback()
            "Without much enthusiasm, Rowan allowed the orc to proceed with whatever it was that he had planned."

            #if flag = competent orc
            if competent_orc:
                "Much to Rowan’s surprise, the attack went swimmingly. The orc split their forces into two groups and hit the settlement from both sides, preventing the villagers from getting away."
                show rowan necklace neutral at midleft with dissolve
                "It was more or less what Rowan planned as well, and by itself it was hardly impressive."
                "The fact neither group scattered in search of a fight when they entered the village proved the ambitious orc commanded enough respect within this particular strike force to maintain basic discipline."
                "Which usually meant he was chieftain material."
                show rowan necklace happy at midleft with dissolve
                "Orc commander standards weren’t particularly high."
                "Once the battle was over and Rowan inspected the end result, he offered some sparse word of praise to the orc, and made a mental note to promote him as soon he returns to the castle."
                "This should help keep the orcs in check."
                $ castle.morale += 5
                #village is captured or destroyed based on player choice
                return

            #if flag = foolish orc
            else:
                "The attack went about as well as Rowan expected – with the orcs rushing into battle without any plan whatsoever."
                show rowan necklace angry at midleft with dissolve
                "Why he believed even for second that this would go any other way, was beyond him."
                "Rowan covered his face with the hood of his cape, and quickly rode into the village to salvage the situation."
                hide rowan with dissolve
                "..."
                show rowan necklace concerned at midleft with dissolve
                "Some damage was already done, but somehow he managed prevent the chaos from spreading."
                "Half an hour later, the village was subjugated, and the orc he allowed to lead the charge knelt before him."
                show rowan necklace angry at midleft with dissolve
                "Rowan looked down on him, jaw clenched."
                if avatar.corruption > 49:
                    ro "Cut his head off."
                    "The orc stared in disbelief, eyes wide. He lunged forward – only to be stopped by his companions."
                    "Nobody wanted to be the one who told the twins their precious slave was killed by one of their own."
                    "Rowan turned around, and let the other soldiers carry out his order. His business here was done."
                else:
                    ro "Mine duty for three months."
                    "The orc grunted, displeased, but said nothing else. Rowan’s word was law."
                    "With the matter settled, Rowan turned around, and left the village. His business here was done, the orcs knew what they had to do."
                    #village is captured or destroyed based on player choice
                    #village drops in size if possible (TO DO LATER)
                    return

        "Stick to your plan.":
            $ released_fix_rollback()
            show rowan necklace angry at midleft with dissolve
            "But Rowan had no intention of gambling with human life. Coldly, he told the orcs they will stick to the original plan and if any of them even think about disobeying him, there will be consequences."
            "His soldiers grumbled in response, displeased, but nobody dared to voice further opposition."
            "Rowan gave them all their orders and, when the time was right, commenced the attack."
            "And as expected, everything went swimmingly, with minimal losses on both sides."
            "The only thing that really suffered was the orcs' morale, but that was a problem Rowan would deal with another day."
            $ castle.morale -= 5
            #village is captured or destroyed based on player choice
            return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Old Hero.
#Requirement: Week: 20+

#show normal village menu at first, then, split into two branches.
#branch 1 - if the player chooses to capture or destroy the village
#branch 2 - if the player chooses to trade with the village

#branch 1 - capture / destroy
label old_hero_destroy:
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve

$ old_her_event = True
if avatar.corruption > 74:
    "Impatient to bring another village under the twins thrall, Rowan decided that this time he would deviate from the usual procedure and oversee the attack personally."
    "Quickly bringing order to the orc detachment that arrived from castle Bloodmeen, Rowan split his forces into three groups, surrounding the village and closing the usual escape routes."
    "At dusk, he ordered a simultaneous attack from all sides."
    "As always, the village could only offer a token resistance. Caught by surprise, a few men tried to fight back – only to be struck down."
    "It all went according to plan – until Rowan heard sounds of an actual fight going on near the center of the village. Displeased by the prospect of unforeseen complications, Rowan hurried his horse forward."
    "There, he saw a man in an old, battered armor, aided by a handful of young men, engaging his orcs."
    "Despite being vastly outnumbered and clearly fighting a lost battle, the villagers seemed determined to protect their village to the end."
    "Normally, Rowan would applaud such a display of heroism, except this time it was working against him. Without a second thought, he galloped forward and readied his sword."
    "The old man saw him coming – and at the last second turned in his direction, raising his own sword to parry the incoming blow. Too slow – years of peasant life must have dulled his reflexes."
    "Rowan’s blade made its way past his guard and struck the man right in the neck."
    "A young boy shouted in horror. Rowan slowed down, and turned around to observe how the last stand of the village defenders fell apart."
    "Without the old man shouting orders and encouragements, the remaining peasants quickly lost their spirit. Some turned around to flee, others threw their weapons down and begged for their life."
    "Others yet decided to give their life with their hero."
    "And they would do precisely that."
    "Soon, the battle was over."

    #if player chose to destroy village
    "Their defenders beaten down, the orcs scattered across the village, capturing people and grabbing anything that was of any worth to the Twins."

    #rejoin
    "Meanwhile Rowan inspected the now dead hero – the man who dared to oppose his forces, against all odds."
    "The wound was fatal – as Rowan intended it to be. The man bled out to death, red blood staining his clothes and armour."
    "His breastplate bore the insignia of Rosaria military."
    "Once, Rowan wore a similar armour."
    "Felt like it was an eternity ago."

    if avatar.guilt > 50:
        "Slowly, Rowan knelt besides the man. He said a silent prayer in his name, and closed his unseeing eyes."
        "… He lingered for a while, uncertain of his own feeling at the moment. But there was no use in regretting his actions now. Rowan stood up, and turned around without another word."

    else:
        "Rowan stared at the body for a short while, then turned around without a word."

    "This village was done with. It was time to move on."
    #capture or destroy the village based on player choice
    #lose 5 orcs
    $ castle.buildings['barracks'].troops -= 5
    return

else:
    "As always not so keen on seeing the result of his choices, Rowan ordered his orcs to attack without him. He would observe from a safe distance, only intervening if the situation called for it."
    "… The fighting went on a bit longer than usual and Rowan was slowly starting to worry something indeed went wrong."
    "He checked his equipment, still unwilling to participate in the attack – but as he lingered, he finally saw the one of his grunts exiting the village."
    "The orc signaled the village was pacified, and Rowan could safely take stock of the situation."
    "Apparently the village elder was some sort of war veteran, who managed to organize a makeshift defense force at the center of the village. He was dead now, but because of his interference they lost more soldiers than usual."
    "An unpleasant surprise, but these things happened. Rowan nodded to the orc and told him to proceed with the rest of the plan."
    "Another day, another village at the mercy of the Twins."
    #capture or destroy the village based on player choice
    #lose 10 orcs
    $ castle.buildings['barracks'].troops -= 10
    return

label old_hero_occupy:
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve
$ old_her_event = True
if avatar.corruption > 74:
    "Impatient to bring another village under the twins thrall, Rowan decided that this time he would deviate from the usual procedure and oversee the attack personally."
    "Quickly bringing order to the orc detachment that arrived from castle Bloodmeen, Rowan split his forces into three groups, surrounding the village and closing the usual escape routes."
    "At dusk, he ordered a simultaneous attack from all sides."
    "As always, the village could only offer a token resistance. Caught by surprise, a few men tried to fight back – only to be struck down."
    "It all went according to plan – until Rowan heard sounds of an actual fight going on near the center of the village. Displeased by the prospect of unforeseen complications, Rowan hurried his horse forward."
    "There, he saw a man in an old, battered armor, aided by a handful of young men, engaging his orcs."
    "Despite being vastly outnumbered and clearly fighting a lost battle, the villagers seemed determined to protect their village to the end."
    "Normally, Rowan would applaud such a display of heroism, except this time it was working against him. Without a second thought, he galloped forward and readied his sword."
    "The old man saw him coming – and at the last second turned in his direction, raising his own sword to parry the incoming blow. Too slow – years of peasant life must have dulled his reflexes."
    "Rowan’s blade made its way past his guard and struck the man right in the neck."
    "A young boy shouted in horror. Rowan slowed down, and turned around to observe how the last stand of the village defenders fell apart."
    "Without the old man shouting orders and encouragements, the remaining peasants quickly lost their spirit. Some turned around to flee, others threw their weapons down and begged for their life."
    "Others yet decided to give their life with their hero."
    "And they would do precisely that."
    "Soon, the battle was over."

    #if player chose to capture village
    "Their defenders beaten down, the orcs lined the remaining villagers and started explaining them how they served Castle Bloodmeen now."

    #rejoin
    "Meanwhile Rowan inspected the now dead hero – the man who dared to oppose his forces, against all odds."
    "The wound was fatal – as Rowan intended it to be. The man bled out to death, red blood staining his clothes and armour."
    "His breastplate bore the insignia of Rosaria military."
    "Once, Rowan wore a similar armour."
    "Felt like it was an eternity ago."

    if avatar.guilt > 50:
        "Slowly, Rowan knelt besides the man. He said a silent prayer in his name, and closed his unseeing eyes."
        "… He lingered for a while, uncertain of his own feeling at the moment. But there was no use in regretting his actions now. Rowan stood up, and turned around without another word."

    else:
        "Rowan stared at the body for a short while, then turned around without a word."

    "This village was done with. It was time to move on."
    #capture or destroy the village based on player choice
    #lose 5 orcs
    $ castle.buildings['barracks'].troops -= 5
    return

else:
    "As always not so keen on seeing the result of his choices, Rowan ordered his orcs to attack without him. He would observe from a safe distance, only intervening if the situation called for it."
    "… The fighting went on a bit longer than usual and Rowan was slowly starting to worry something indeed went wrong."
    "He checked his equipment, still unwilling to participate in the attack – but as he lingered, he finally saw the one of his grunts exiting the village."
    "The orc signaled the village was pacified, and Rowan could safely take stock of the situation."
    "Apparently the village elder was some sort of war veteran, who managed to organize a makeshift defense force at the center of the village. He was dead now, but because of his interference they lost more soldiers than usual."
    "An unpleasant surprise, but these things happened. Rowan nodded to the orc and told him to proceed with the rest of the plan."
    "Another day, another village at the mercy of the Twins."
    #capture or destroy the village based on player choice
    #lose 5 orcs
    $ castle.buildings['barracks'].troops -= 10
    return

label old_hero_trade:
#branch 2 - trade
scene bg31 with fade
show rowan necklace neutral at midleft with dissolve
$ old_her_event = True
$ temp3 = human_villages_defs[eventHex[6]][2]
"The village elder was an energetic man in his forties, with a short beard, tanned skin and, as it happened, military background."
"Upon seeing Rowan, he squinted his eyes, as if uncertain if they’ve been deceiving him. Then, realization crossed his face - he straightened his back, and saluted the approaching hero."
"”General Blackwell”, the elder called him."
"When Karnas invaded the six realms, it was obvious they would need every living man, from peasant to noble, involved in the war. Not that many people were willing to join – but they didn’t exactly had a choice in that regard."
"The entire countryside was full of veterans. Rowan expected more of them to assume the position of village elders."
"At least those would not end up bandits, mercenaries, or broken men."
"War usually brought out the worst in people. He was glad to see someone who didn’t end up finding himself on that path."
"Rowan returned the salute, then extended his hand. The elder grabbed it with a smile."
"The village elder –  Gregory, as Rowan soon learned, invited the hero to his home, serving beer and bread to his guest. The two exchanged pleasantries and, much to Rowan’s dissatisfaction, the subject of his adventures after the war came up."
"Rowan delivered a handful of noncommittal answers, as always not so keen on sharing his current predicament."
"He tried to power through the conversation as quickly as possible, so he could raise the matter of a potential trade agreement – but the elder had something different planned."
"He revealed to Rowan, voice grave, that he knew of orc activity in the region. Mines were taken, villages were plundered, but the nobles weren’t doing anything about it. He feared, that if nothing was done, in time his own village might be in danger."
"Rowan’s arrival must have been a sign of Solania’s favor, for he was about to take a handful of strong, young lads, and scout the nearby territory for signs of the greenskin."
"The hero's tracking abilities were a thing of legend – with him leading the expedition, they could quickly find any nearby  orc encampments and put an end to this menace before it could threaten his hometown."
"To Rowan, that was obviously not an option, for he had no time to run around Rosaria chasing orcs that quite literally did his bidding."
"And he had a far better solution available to him."
"Having already decided the village would not be a target for an orc raiding party, Rowan explained to the elder he was already working on the problem. He had “allies” who were attempting to contain the orc threat."
"But they could not count on the noble’s backing – the aristocracy cared not for the countryside (a fact that allowed the twins to slowly take over the region in the first place), so they had to take care of the financing themselves."
"Which is what brought Rowan to the village in the first place – he explained he was attempting to secure more funding by signing trade agreement with numerous Rosaria settlements."
"The elder nodded slowly, a soft scowl on his face. For a man of action like himself, sitting around and letting others deal with the problem was clearly frustrating."
"But if Rowan believed this was the best course of action, he would follow suit without a word of complaint."
"He only needed to know what was expected of him."

if avatar.corruption > 74:
    menu:
        "Sign a normal trade agreement.":
            $ released_fix_rollback()
            "Rowan presented him with the usual deal, one that was generally considered acceptable to both sides. And as he expected, the elder agreed to it quickly, stating the terms were indeed reasonable."
            "Satisfied with the result, Rowan warned him not to go Orc hunting on his own. Regardless of what happens in Rosaria, he and the villagers should just sit tight, while Rowan and his “allies” deal with the problem."
            "The elder proposed Rowan should stay the night, as it was getting late, and the prospect of getting a good night of sleep on a proper bed was simply too good to pass."
            #gain 2 move points due to good rest
            $ avatar.mp += 2
            #gain standard village trade income
            return

        "Use your reputation to sign a more lucrative agreement.":
            $ released_fix_rollback()
            "Rowan presented him with a slightly harsher deal than usual, unbeknownst to the elder."
            "The man listened to the terms carefully, and 15 minutes later, after a long consideration, agreed to them without any even attempting to bargain."
            "He said that if Rowan needed the money so badly, the village would provide it. Everything for the hero of Karst."
            "Feeling a bit guilty for using his reputation like that, but nevertheless grateful the elder didn’t pry on the circumstances, the two signed the deal."
            "Rowan warned the elder once more not to go hunting the orcs on his own, and to sit tight no matter what happens in Rosaria. He and his “allies” would deal with the issue."
            "The elder proposed Rowan should stay the night, as it was getting late, but knowing he was already exploiting the elder for his own gain, Rowan decided to pass on the offer and resumed his travels immediately."
            #gain 1.5 times the usual village trade income
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)/50.0 ))
            return

        #only available if rowan's corruption is greater than 74
        "Make him give the twins almost everything.":
            $ released_fix_rollback()
            "Voice heavy, Rowan explained to the man he and his allies had very limited resources available to them. They really couldn’t afford to spread themselves over the entire region."
            "Only places deemed “strategically important” ended up protected."
            "Rowan could see how the realization dawned on the man. Slowly, the elder asked what would it take for his village to be considered “strategically important”."
            "Quietly, Rowan listed the amount of goods they would have to contribute in order to ensure  his “allies” deal with the orc problem."
            "It was far beyond what he usually demanded during trade agreements. Even though Castle Bloodmeen would provide some token payment for the goods, at this point the village would be better off simply being conquered."
            "The elder didn’t answer at first. He sat there, motionless, fists clenched."
            "Finally, he swallowed heavily and answered that, if that’s what was necessary to protect the village from the orcs, he would agree to it."
            "Trying not to think how just basically forced a village into poverty to fuel the Twins war machine, Rowan explained the details of their arrangement."
            "He reminded the elder not to go hunting orcs on his own, and to sit tight no matter what happens in Rosaria. He and his “allies” would take care of everything –"
            "- as long as he sticks to his side of the deal."
            #gain 2 times the usual village trade income
            $ change_base_stat('g', 3)
            $ change_base_stat('c', 3)
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)))
            return
else:
    menu:
        "Sign a normal trade agreement.":
            $ released_fix_rollback()
            "Rowan presented him with the usual deal, one that was generally considered acceptable to both sides. And as he expected, the elder agreed to it quickly, stating the terms were indeed reasonable."
            "Satisfied with the result, Rowan warned him not to go Orc hunting on his own. Regardless of what happens in Rosaria, he and the villagers should just sit tight, while Rowan and his “allies” deal with the problem."
            "The elder proposed Rowan should stay the night, as it was getting late, and the prospect of getting a good night of sleep on a proper bed was simply too good to pass."
            #gain 2 move points due to good rest
            $ avatar.mp += 2
            #gain standard village trade income
            return

        "Use your reputation to sign a more lucrative agreement.":
            $ released_fix_rollback()
            "Rowan presented him with a slightly harsher deal than usual, unbeknownst to the elder."
            "The man listened to the terms carefully, and 15 minutes later, after a long consideration, agreed to them without any even attempting to bargain."
            "He said that if Rowan needed the money so badly, the village would provide it. Everything for the hero of Karst."
            "Feeling a bit guilty for using his reputation like that, but nevertheless grateful the elder didn’t pry on the circumstances, the two signed the deal."
            "Rowan warned the elder once more not to go hunting the orcs on his own, and to sit tight no matter what happens in Rosaria. He and his “allies” would deal with the issue."
            "The elder proposed Rowan should stay the night, as it was getting late, but knowing he was already exploiting the elder for his own gain, Rowan decided to pass on the offer and resumed his travels immediately."
            #gain 1.5 times the usual village trade income
            $ castle.villages_income += int(temp3 * ( (dice(25) + 25)/50.0 ))
            return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#A cheating Elder:
#No requirement.

label a_cheating_elder:
scene bg1 with fade

"Rowan walked through the village, taking stock of their defenses. This particular village wasn’t too well defended. It would be an target for his orcs – if he choose to send them in."

#Give normal village menu. Then, split:

#branch one - capture or destroy:
"Rowan expected the attack to go well, but not this well."
"After his forces arrived at the village, the elder instantly surrendered, without as much as a stone cast at his soldiers. His orcs quickly scattered across the village, rounding up villagers, while the elder was brought before him."
"He was a scrawny old fellow, terrified out of his wits, as Rowan quickly after looking at his pats. He prostrated himself before him and with shaking voice asked Rowan to spare the village and himself."

#if player chose to destroy the village
"From beneath his hood, Rowan nodded slowly. He quietly informed the man who his new masters were, and what was expected of them."
"To drive the point home, he ordered all the gathered villagers to kneel along the elder."
"If anyone hesitated, one his orcs would strike them in the back, forcing them down. It was a crude method, but he needed to make sure the villagers wouldn’t be causing any troubles in the future."
"He took another look at the village elder, who was still shaking in  fear. With this man at the helm… He doubted they would."
#village is destroyed as normal
return

#if player chose to capture the village
"Rowan looked down on the man with pity. If only he knew..."
"He turned to the orc besides him and spoke."
show rowan necklace neutral behind bg1
ro "You know your orders."
"The elder looked up confused – only to be knocked out by a blow straight between the eyes."
"Some of the gathered villagers tried to resist, but the orcs subjugated them quickly. Nobody had any weapons to really be a threat, so his soldiers managed to do so without killing anyone."
"Once the people were tied up and ready for transportation, his orcs would then scatter across the village, pillaging food, gold, and valuable tools."
"It was nice to see things go so well for a change."
#village is captured as normal
#gain ten slaves
return

#branch two - trade
"Rowan headed to the center of the village, to meet the elder. He found him quickly – he was a scrawny old fellow, polite and pleasant, who reacted to Rowan’s proposal with great enthusiasm."
"As usual, after a long series of negotiations, Rowan managed to strike a deal that more or less satisfied both sides."
"However, this time things did not go as smoothly as he expected."
"A few days after departing from the village, Rowan received a message from the castle. Apparently, the goods provided by the elder were not what they’d been expecting. The quality was simply below below the usual standard."
"However, the elder still expected to be paid the agreed amount, and wouldn’t listen to his emissaries at all. Castle Bloodmeen was to either pay and take the goods or the deal was off."
"As the trade still benefited the Twins, their representatives reluctantly agreed, much to the elder’s satisfaction. But they were now asking how to proceed from here on. If the matter was left as it stood, the village would provide only half of the usual income."
"Rowan did not have the time to chase after every elder who tried to scam him, as tempting as it was."
"He had to rely on what resources he had to deal with the issue."

menu:
    "Leave the village alone – accept the subpar goods.":
        $ released_fix_rollback()
        "Gritting his teeth, Rowan told the castle staff to leave the village alone. He couldn’t punish the whole village for the actions of one dishonest elder."
        "They would have to accept the deal as it was."
        $ change_base_stat('c', -3)
        #village provides half the usual gold from trade
        return

    "Send the orcs to conquer the village.":
        $ released_fix_rollback()
        "Trading with Rosaria villages was already less profitable than simply conquering them. If Rowan wanted to remain in the Twin’s favor, he couldn’t afford being deceived like that."
        "He told the staff to send an orc detachment to deal the elder, and bring the village under the twin’s control. He knew it was as little defended as most villages were, so he foresaw light casualties at best."
        #lose 3 orcs
        #apply the usual reward from destroying the village
        return

    "Send the orcs to occupy the village.":
        $ released_fix_rollback()
        "Rowan gritted his teeth. Trading with Rosaria villages was already considerably less profitable than some of the other options he had at his disposal. He was protecting them from the twins, and this was how they repaid the favor?!"
        show rowan necklace neutral behind bg1
        ro "…"
        ro "Send the orcs in. The village is scarcely defended, so you don’t need a big group."
        ro "Enslave everyone, take anything of value, then burn down what remains."
        ro "And have this done by the end of the week."
        "That, and no less, was the price the elder and his people would pay for their dishonesty."
        #lose 3 orcs
        #apply the usual reward from capturing the village
        return

    #only available if the brothel is built, and the player has at least one unassigned spy
    "Send a demonic spy to convinces the elder to change his mind.":
       $ released_fix_rollback()
       "Rowan groaned in annoyance. To think he would have to deal with mundane problems like this one…"
       "Luckily for him, he had just the right tool for the job. "
       #give player a choice of available spies, chosen spy becomes unavailable for two weeks
       "He ordered the staff to have one of his agents visit the village and show the elder the error of his ways. It should take a while… But he doubted the demon would have any difficulties with the task."
       #gain standard village trading income
       return
