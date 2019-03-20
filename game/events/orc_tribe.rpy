######## Orc tribe events ########
#Increases orc soldier recruitment rate.

#Choose one of the following options at random, it may change the normal outcome slightly.
init python:

    #Event 1: Neutral
    #Req: In Rosaria, small size resource. # 'rosaria_map' -> Rosaria, map_res_13 -> small tribe
    event('orc_tribe_neutral', triggers='map_res_13', conditions=("world._cur_map_uid == 'rosaria_map'",), group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    #Event 2: Injury, chance at reduced recruitment.
    event('orc_tribe_injury', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    #Event 3: Diplomacy test to gain extra recruitment.
    event('orc_tribe_diplomacy', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)
    #Weakened Tribe
    #Req: In Rosaria, small size. Random, Uncommon.
    # TODO: requirements
    event('weakened_tribe', triggers='map_res_13', group='map_res_orc_tribe', run_count=1, priority=pr_map_res)


label orc_tribe_neutral:
#Event 1: neutral
#Req: In Rosaria, small size resource.
#Show countryside background
$ change_recruitment_bonus('barracks', 1)
"Rowan had discovered a small tribe of orcs, hiding in the Rosarian wilds! It wasn't a terribly large group, but it was still rather amazing that they'd managed to stay hidden for so long from the baron's men."
"In fact, this group was likely fleeing from Prothean armies, forced into a nomadic lifestyle seeking a place where they could live in peace.  At least, whatever constituted peace for orcs."
"Even now, Rowan could see a fight break out between two of the brutes. He didn't know what it was about, but there was a tension among this group."
"Soon afterwards, a being landed in their midst with a crash. The fight was soon forgotten and everyone turned to face the new arrival: a red demon with an offer for these lost creatures."
#no effect.
return


label orc_tribe_injury:
#Event 2: Injury, chance at reduced recruitment.
#Show forest background.
$ change_recruitment_bonus('barracks', 1)
"In most cases, orcs respected one thing: martial might."
"So when his master was unavailable to make first contact with potential recruits, it was up to Rowan to make the case for Bloodmeen on his behalf. A first contact that would require a demonstration for the Twin's armies."

#Combat test DC12
if dice(20) >= 12:
    #Combat test: success.
    $ released_fix_rollback()
    "Rowan proved to be more than capable, defeating every orc that sought to challenge him. He wasn't able to avoid taking some hits himself, but by the end he'd seriously impressed the orcs of this tribe."
    "When Andras was able to begin recruiting from here, he found them to be extremely eager to join his armies."
    #Rowan is injured, - vitality for 2 weeks
    $ add_effect(Injury('Wounds', 'vitality', -1, 2))
    return
else:
    #Combat test: failure.
    $ released_fix_rollback()
    "Although Rowan was a very capable fighter, he wasn't able to defeat all challengers this day. His injuries were simply too great to continue. This was a great disappointment to the orcs, causing them to become much more reluctant recruits."
    # -1 recruitment rate.  Rowan is injured, - vitality for 3 weeks.
    $ change_recruitment_bonus('barracks', -1)
    $ add_effect(Injury('Wounds', 'vitality', -1, 3))
    return


label orc_tribe_diplomacy:
#Event 3: Diplomacy test to gain extra recruitment.
#Show forest background.
$ change_recruitment_bonus('barracks', 1)
"A group of orcish refugees had made this part of Rosaria their home, for the time being.  They were a people long use to rejection and being hunted. Learning from Andras that he had a place for them in his armies gave them hope, but they were wary."
"Rowan took it upon himself to try and assuage their fears of being driven out once more if they joined, or that the twins would only lose the coming war as Karnas had."

#Diplomacy test DC12
if check_skill(12, 'diplomacy')[0]:
    #Diplomacy, success:
    $ released_fix_rollback()
    "His words moved them and many were inspired when they learned that it was him who was guiding the actions of the twins. A hero of man would know how to defeat men."
    "The red demon was somewhat dismayed to discover that it was Rowan and not him that had inspired his new recruits, but he did not argue with results."
    #+1 extra orc recruitment
    $ change_recruitment_bonus('barracks', 1)
    return
else:
    #Diplomacy, failure:
    $ released_fix_rollback()
    "His words fell on deaf ears. A human was weak, a human didn't know what he was talking about. Andras laughed at Rowan's attempt, claiming that orcs only listened to strength."
    "They weren't listening to the demon either, he silently noted to himself. There would be some recruits from here, but not as many as Rowan had thought he might be able to get."
    #No effect
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label weakened_tribe:
#Weakened Tribe
#Req: In Rosaria, small size. Random, Uncommon.

"Rowan found a small tribe of orcs clinging to the hills in the Rosarian countryside. At first, he expected they would be eager allies. However the orcs he encountered, while not hostile, were weary of him."
"They shied away from his gaze and only spoke to him in short bursts before claiming they had other tasks to do."
"Rowan instead spoke to their chief. The orc chief was a greybeard, an oddity for a society where living past your prime years is so often considered a sign of weakness. He apologized for his people’s rudeness."
"The clan’s mightiest warriors had been slain in a brutal battle with the local garrison. This clan’s fighting was only a pittance of its former glory. A human attempting to raise an army could only spell disaster."
"The chief assured Rowan of his people’s eagerness for war. His own son had died on that field. If he could harm the humans, then his son’s ghost would look upon him with favor."
"He suggested that in lieu of fighting men, that the tribe offer what money and jewels it had to Rowan’s treasury."
"Taking some time to consider the offer, Rowan looks around camp. Indeed, most of the orcs he saw were the weak, the lame, the mothers, and those orcs whom fortune had favored with old age."
"However, a few males of fighting age could be found among the tents. They could perhaps produce a token levy. But, such a levy would cost the tribe the few scraps of youth that remained to it."

menu:
    "Accept the money.":
        $ released_fix_rollback()
        "Rowan considered his options. While his own forces could always use fighting men, he doubted he’d get many from here."
        "Besides, the loss of whatever men remained might leave the tribe in dire straights should something happen to them requiring the need to defend themselves. It wouldn’t be right to take what protection they had."
        "He returned to the chief and agreed to take a monetary sum. The chief, smiling from ear to ear, led Rowan behind his simple wooden throne and produced an ivory box. It’s carved spotless exterior was something totally foreign to an orc camp."
        "The chief opened it up, revealing an interior stuffed with cold coins and shattered jewelry. Rowan picked up a smashed golden bracelet with a name carved on the interior."
        "Money was money. Rowan thanked the chief for his support, and rode off. Leaving the poor orc tribe to their recovery."
        #treasury receives income, no orcs gained
        $ change_treasury(20)
        return

    "Insist on recruiting soldiers.":
        $ released_fix_rollback()
        "Rowan considered his options. While a gift of gold always had its uses, his armies desperately needed fighting men. Certainly, these orcs couldn’t produce a retinue, but their numbers would be a welcome addition to his own forces."
        "Their own safety wasn’t off too much importance. They were just orcs afterall. Rowan was sure that the young males currently at their mother’s skirts would soon be hulking killing machines to replace their fathers."
        "He returned to the orc chief and repeating his request for soldiers. The chief nodded along sadly, but could not refuse a request of this sort. The honor of his son and his clan demanded they fight alongside the forces of Bloodmeen."
        "With a sigh, he told Rowan that he could bring with him any fighter still capable of holding a war axe."
        "Rowan rode through the village. Gruff orcish warriors said terse goodbyes to their brood, and recent mothers changed from their torn aprons into war pelts. He took one last look around the village as they marched off."
        "It was quiet."
        #recruitment rate below standard for orc tribe.
        $ change_recruitment_bonus('barracks', 1)
        return
