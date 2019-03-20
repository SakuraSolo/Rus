init python:

    #Spy on the orcs
    #Requirement - orciad main story not complete.
    event('spy_on_the_orcs', triggers='orciad_explore', conditions=("week >= 4", "orciad_state <=1"), run_count=1, group='orciad_camp', priority=pr_map_res)
    #The Woodcarver
    event('the_woodcarver', triggers='orciad_explore', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)
    #The (un)lucky slave.
    #Requires seeing the “Orc families” event.
    event('the_unlucky_slave', triggers='orciad_explore', conditions=("week >= 4",), depends=('orcish_families_and_neutrals',), run_count=1, group='orciad_camp', priority=pr_map_res)
    #Meeting the priest of Kharos
    #Requirement: Third visit to the camp (for reason no other than for the initial description to make sense)
    event('meeting_the_priest_of_kharos', triggers='orciad_explore', conditions=("week >= 4", "orciad_explore >= 3", 'not orciad_priest_visited'), group='orciad_camp', priority=pr_map_res)
    # small events for "meeting_the_priest_of_kharos"
    event('orciad_returning_to_camp_climb', triggers='map_res_105', active=False, run_count=1, group='orciad_camp', priority=pr_story)
    event('orciad_returning_to_camp_sneak', triggers='map_res_105', active=False, run_count=1, group='orciad_camp', priority=pr_story)
    event('orciad_returning_to_camp_listen', triggers='map_res_105', active=False, run_count=1, group='orciad_camp', priority=pr_story)
    event('orciad_returning_to_camp_dodge', triggers='map_res_105', active=False, run_count=1, group='orciad_camp', priority=pr_story)


label spy_on_the_orcs:
#Spy on the orcs
#Requirement - orciad main story not complete.

$ change_mp(-5)
$ prevent_tile_exploration()
#init
$ event_tmp['orcSpyTarget'] = None
$ event_tmp['reroll_random'] = False
$ event_tmp['spot_check_passed'] = False

scene bg26 with fade
show rowan necklace neutral behind bg26

#if first visit
if orciad_explore == 0:
    "To an extent, the division inside the camp was absolutely fascinating. This wasn’t the first time Rowan witnessed disagrees among the higher echelons of command, but this was the first he saw an argument physically divide the camp."
    "He would find it amusing, if not for the fact the orcs were supposed to be their allies in the near future, and the divide left the camp so horribly open to enemy attacks it was almost painful to observe."
    "With a lack of unified leadership, their entire defense was absolutely disorganized. There was no logic to their patrol routes, and the guards were mostly preoccupied with glaring menacingly at the orc from the rival camp."
    "If someone wanted to infiltrate the camp and engage in some subterfuge, they would little challenge in sneaking around."
    "… Which was precisely what Rowan intended to do."
    "Dark clouds covered the sky the entire day, and when night came, neither the moon nor the stars were visible. A perfect night to do some damage to one of the warchiefs… Or to engage in some mild deception.  He had some options available to him-"
    "The only question was – who to strike against, or who to help?"
else:
#else
    "Dark clouds covered the sky during the day, and when night came, neither the moon nor the stars were visible. Once more, the night was perfect to engage in some subterfuge. There was still much to be done in the camp."
    "The only question was – who to strike against, or who to help?"

#rejoin

menu:
    "Try to sabotage Ulcro.":
        $ released_fix_rollback()
        $ event_tmp['orcSpyTarget'] = 'Ulcro'
        jump orcSpyRNG

    "Try to sabotage Batri.":
        $ released_fix_rollback()
        $ event_tmp['orcSpyTarget'] = 'Batri'
        jump orcSpyRNG

    #requires player to have chosen to betray the slaves in the event orc slaves and EITHER of the following:
    #Corruption lower than 50 / Guilt higher than 49
    "Help the slaves." if orciad_betray_the_slaves and (avatar.corruption < 50 or avatar.guilt > 49):
        $ released_fix_rollback()
        jump orcSpySlaves

################################################################################
label orcSpyRNG:

#choose one of the following at random:

if dice(2) == 1:
    #1
    jump anOfficerDrunk
else:
    #2
    jump unhappyOrcs

################################################################################
label anOfficerDrunk:

"Sometimes later, he found what could’ve been an opportunity."

if event_tmp['orcSpyTarget'] == 'Ulcro':
    "Sitting around a campfire with a handful of henchmen, Rowan noticed someone he knew was a prominent Ulcro supporter."

else:
    "Sitting around a campfire with a handful of henchmen, Rowan noticed someone he knew was a prominent Batri supporter."

"He was drinking quite heavily from a barrel of what Rowan assumed was stolen beer, and judging from the jovial atmosphere, both he and his friend were at it for quite some time."
"It didn’t look like they intended to stop anytime soon. Which is where the opportunity came from."
"He could eliminate him. A drunk orc made an easy target, and there was no doubt the orc would sooner or later wander off to take a piss or something. Stabbing him in the dark would be easy… And while Rowan despised such tactics…"
"Did he really have the luxury of being honorable, and even if he did – did the orcs deserve it?"

menu:
    "Kill the orc captain.":
        $ released_fix_rollback()
        "… No, they did not. Besides, Rowan made his choice a long time ago, when he joined the Twins. Murdering an orc officer in cold blood didn’t even come close to the worst thing he would be forced to perform in their service."
        "So he waited patiently, hiding in the shadows, for the right opportunity to strike."
        "An hour later, he finally found one. The beer barrel was emptied, and after voicing their displeasure for several long minutes, the orcs finally decided to call it a night. All of them headed off to their tents – including the captain."
        "Rowan followed him, stepping lightly."

        if event_tmp['orcSpyTarget'] == 'Ulcro':
            "Unfortunately, it seemed that finding the orc in such a vulnerable state exhausted his reserves of good luck for the night. The drunken captain had his tent fairly close to Ulcro’s own... And the guards were much more alert in this area…"

        else:
            "Unfortunately, it seemed that finding the orc in such a vulnerable state exhausted his reserves of good luck for the night. The drunken captain had his tent fairly close to Batri’s own... And the guards were much more alert in this area…"

        #spot check, DC12
        if check_skill(12, 'spot')[0]:
            #pass
            $ event_tmp['spot_check_passed'] = True
            "… But as it happened, not nearly alert enough. After observing the area for some time, Rowan was able to spot a gap in their patrol routes."
            "He waited some more – to make sure the captain falls asleep in his tent – then hastily crossed the inner camp. With his knife, he cut the side of the tent open, and entered inside."
            jump orcSpyTent
        else:
            #fail
            "… But they weren’t the first guards Rowan had to fool in his life. He waited for a while, to make sure the captain falls asleep in his tent, then, identifying the right opportunity, carefully crossed the inner camp."

        #move silently check, DC12
        if check_skill(12, 'move_silently')[0]:
            #pass
            "Just as he planned, nobody saw him. With his knife, he cut the side of the tent open, and entered inside."
            jump orcSpyTent
        else:
            #fail
            orc1 "Huh? Wat was dat?"
            "Rowan stopped, frozen. Not daring to even breathe, he slowly turned to the direction of the voice."
            "A lone orc was staring right at him, squinting his eyes. He could not see him – at least not yet. Not from that distance."
            orc2 "Wus wrong?"

            $ orcName = 'Orc 1'

            orc1 "Me heard something. I think."
            "The orc turned to address his companion, and Rowan instantly capitalized on the lucky distraction to flee the scene. Too close, much too close."
            jump campMenu


    "Look for something else." if not event_tmp['reroll_random']:
        $ released_fix_rollback()
        if event_tmp['orcSpyTarget'] == 'Ulcro':
            "The night was still young, and Rowan had no intention of devolving into some common murderer for hire. There were others way of sabotaging Ulcro."
        else:
            "The night was still young, and Rowan had no intention of devolving into some common murderer for hire. There were others way of sabotaging Batri."
        #reroll random event, only allow this option once
        $ event_tmp['reroll_random'] = True
        jump orcSpyRNG

################################################################################
label orcSpyTent:

"The orc captain laid in his cot, snoring loudly. Good."
"Now all that remained was choosing the right tool for the deed."

#if strength is 15 or more
if avatar.strength >= 15:
    "His eyes laid on a bucket of clean water in the corner."
    "Well then."
    "Unceremoniously, Rowan rolled the orc off his cot, on his stomach. Completely drunk, the orc merely grunted in annoyance."
    "He sat on his back, and adjusted his weight to properly immobilize the orc. Then, he put his arm around the orc’s neck –"
    "And started to strangle him."
    "The orc woke up almost immediately, but it was far too late for him to do anything. Rowan had him in an iron grip, and no matter how hard the orc struggled, he wouldn’t be able to get free, nor would he be able to call for help."
    "… A couple of minutes later, it was all over. The orc laid limp beneath him."
    "Rowan stood up, and carried his body over to the bucket. He place him lying in front of it, face in the water. Getting drunk and falling asleep while trying to get some fresh water. Such a tragic fate."
    "Was it believable? Not at all. Would a simple autopsy reveal no water in the orc’s lungs? Very much so. Did the orcs ever bothered to investigate dead bodies or even understood what the word “autopsy” meant?"
    "Rowan doubted that."
    jump orcSpyLeave

#else
else:
    "Rowan scanned the tent carefully. Soon, he found his weapon of murder – a crude dagger with a barbed blade."
    "He grabbed it with his hand, and slashed the orc’s throat without a moment of hesitation."

if avatar.corruption < 50:
#if corruption is less than 50
    "Rowan watched, jaw clenched, as the orc opens his eyes. Making gurgling sound, he tried to close the gap in his throat, but it was no use – before he do anything else, Rowan finished him off by pushing the dagger straight into his skull."
    "A brutal death, but Rowan could not find it in himself to feel pity for the orc. While he tried to have some sympathy for his soon to be underlings, orc raid leaders were usually the worst of their kind. The world would not miss him."
    "Other orc’s would probably wonder what exactly happened, but there was no risk of them ever tracking the assassination back to the hero."
    jump orcSpyLeave

#else
else:
    "He watched, disinterested, as the orc opened his eyes. Making gurgling sound, the pitiful creature beneath the hero tried to stop the bleeding, but it was no use."
    "Before the orc could do anything else, Rowan finished him off by pushing the dagger straight into his skull. He couldn’t risk him causing a ruckus."
    "Other orcs would no doubt wonder what exactly happened. Not that Rowan cared. There was no way any of them would be able to trace this back to him."
    jump orcSpyLeave

################################################################################
label orcSpyLeave:

#if earlier spot check was passed
if event_tmp['spot_check_passed']:
    "Turning around, Rowan peered through the hole in the tent. It was probably best not to linger."
    "Luckily for him, he already knew the guards blind spots. Waiting for the right moment, he quickly left the tent – and disappeared into the night."
    jump campMenu

#else
else:
    "Not wishing to risk discovery at this point, Rowan contacted Jezera to have the demoness teleport him back to the castle, so he could resume his travels from the northern portal. A mild inconvenience, but better safe than sorry. "
    #move Rowan to northern portal
    # TODO: moving avatar out of camp to given map location
    # change Rowans location to hex(id 86)
    $ world.cur_map.pos_id = 86
    return

################################################################################
label unhappyOrcs:

"Lady luck seemed to have smiled on him this night. As he was sneaking through the camp, he noticed two orcs, away from their brethren, and whispering between themselves."

#listen check, DC12
if check_skill(12, 'listen')[0]:
    #pass
    "Rowan sneaked up to the two, and started listening to their conversation."
    jump unhappyOrcsPassTests
else:
#fail
    if check_skill(12, 'move_silently')[0]:
    #move silently check, DC12
        #pass
        "While they were too far to hear properly, it only took Rowan a couple of seconds to sneak up to them, and eavesdrop on their conversation."
        jump unhappyOrcsPassTests
    else:
        #fail
        $ orcName = 'Orc 1'
        "However, they were too far away to hear properly. As Rowan attempted to sneak on them, he must’ve make sort of the noise, because the two orcs suddenly went silent."
        orc1 "Wazz that? "
        orc2 "Don’t know. But better talk tomorrow."
        orc1 "Ya."
        "Grinding his teeth, Rowan retreated before the orcs could find him. All that sneaking around, for naught!"
        jump campMenu

label unhappyOrcsPassTests:
#rejoin (after passing on either test)
"Quickly, the topic of their discussion became apparent. The two orcs weren’t too happy with how their respective raid leaders handled the recent division of spoils."

$ orcName = 'Orc 1'
orc1 "…And the pale, big titty one?"

orc2 "Black hair, black dress?"

orc1 "Ya."

if event_tmp['orcSpyTarget'] == 'Ulcro':
    orc2 "Grott took her."

else:
    orc2 "Trott took her."

orc1 "Ass."

if event_tmp['orcSpyTarget'] == 'Ulcro':
    orc2 "Yes. Grott always takes the big titty ones. We get the flat ones. Cow shit."

else:
    orc2 "Yes. Trott always takes the big titty ones. We get the flat ones. Cow shit."

orc1 "Bah! Who do we smash to get a big titty slave?"

"… Rowan closed his eyes and tried not to sigh. His future soldiers. Lovely."
"No matter. If someone was willing to die for you, you had not right to look down on them. The nobles made that mistake, and Rowan had no intention of doing the same."

ro " If you are dissatisfied with your raid leaders, then I believe we can help one another."

"Rowan stepped from the shadows, and the two orcs looked at him in surprise. He pulled down his hood, revealing his face to the two orcs. One of them seemed to have realized who they were talking to."

orc2 "Demon’s Hand. What you want?"

"While reserved, this particular orc appeared to hold at least some degree of respect for him. He must’ve have been one the few who saw him enter with Andras, and decided it was best not to annoy the emissary of his future boss."
"Good. This made things easier."
"It won’t be too hard to get the two orcs to switch allegiances. But who should they pledge themselves to?"

if event_tmp['orcSpyTarget'] == 'Ulcro':
    menu:
        "Batri.":
            $ released_fix_rollback()
            jump orcSpyBatri

        "Tarish.":
            $ released_fix_rollback()
            jump orcSpyTarish

else:
    menu:
        "Ulcro.":
            $ released_fix_rollback()
            jump orcSpyUlcro

        "Tarish.":
            $ released_fix_rollback()
            jump orcSpyTarish

################################################################################
label orcSpyUlcro:

ro "Andras grows tired of Batri pretending he’s anything more than cocky musclehead. Warchief Ulcro knows how to lead properly, and wouldn’t allow for such injustice to stand. You’re fighting on the wrong side here."

orc2 "And you say Warchief Ulcro would treat us fair?"

ro "Once Warchief Ulcro pledges himself to the Bloodmeen, Andras will make sure all orcs get exactly what they deserve."

"… Was he overdoing? Perhaps a little. But he was an emissary to the future demon lord. Being vaguely ominous was almost expected of him."

#decrease support for batri by 1
$ batri_power -= 1
jump orcSpyEnd

################################################################################
label orcSpyBatri:

ro "Andras has no need for a warchief that would rather hide in his tent than meet his opponent in an open field. Your raid leaders would never steal from you if you had a strong leader keeping things in order."

orc2 "And you say Batri will set them straight?"

ro "Warchief Batri will have no patience for orc raiders stealing from others. Andras expects discipline."
ro "And he will have it."

"Was the veiled threat too much? Probably not. Orcs respected strength, and only accepted discipline if it was forced upon them."

#increase support for batri by 1
$ batri_power += 3
jump orcSpyEnd

################################################################################
label orcSpyTarish:

ro "Andras tires of this conflict. If Ulcro is too afraid to face Batri, and Batri is too weak to take what he thinks belongs to him, then neither deserve to serve the Chosen of Kharos."

orc2 "Then who-"

ro "We don’t care. And neither should you. Just pray you won’t be on the side of either when the time of judgment comes."

"… Was he overdoing it? Oh, most definitely. But he needed to scare as many orcs as he could away from both Batri and Ulcro. It will make Tarish transition into power easier."

#increase support for tanish by 1
$ tarish_power += 1
jump orcSpyEnd

################################################################################
label orcSpyEnd:

"Both orcs looked at one another. They didn’t seem all too convinced, but it didn’t matter. They didn’t care for politics. They just wanted their fair share of loot, and they both knew it wouldn’t happen with their current raid leaders."
"After a few long moments, one of the orcs, the one Rowan was talking with, offered a tentative nod."

orc2 "Demon’s Hand speaks for the demon lord. Will trust his words."

orc1 "Others angry. Will make them follow."

ro "Good."

show rowan necklace happy behind bg26

ro "Your loyalty will be rewarded."

orc2 "Only want fair spoils. Nothing more."

orc1 "… And big tittied slave."

orc2 "And big tittied slave."

"Again, Rowan suppressed the urge to sigh. He hoped these two will have enough common sense to keep their mouth shut about his own involvement in the matter."
"For now, all he had to do was wait. When the time comes for Batri and Ulcro to fight, his little trick will likely have borne fruit, even if he himself won’t notice the results. Individually, small time orcs like these two mattered little…"
"But sway enough of them to your cause, and your victory was assured."

jump campMenu

################################################################################
label orcSpySlaves:

"As much as Rowan wanted to, he couldn’t forget how he betrayed the human slaves. They put his trust in him… And he turned his back on them."
"Yes, he couldn’t risk alienating the orc camp."
"He had to do it."
"He had to sacrifice them."
"For the greater good."
"…How many more compromises will he be forced to make, serving the Twins?"

#if Rowan was convinced by Jezera in the intro
if introserve == 3:
    "He wanted to make the world a better place. A place where people would be finally free of oppression. And what had he done instead? Sold out the human captives, just as he sold his own soul."

#else
else:
    "He couldn’t move against them, not yet. But was it really an excuse to simply do their bidding blindly? Would he now spend his entire life committing one atrocity after the other, telling herself “I had no choice” over and over again?"

#rejoin
"Rowan swallowed heavily. A part of him knew he couldn’t allow that guild to eat him up. But another part cherished it. Cherished the fact he was still capable of caring."
"Traitor or not, he was still a Hero."
"He couldn’t do anything about the slaves that were sold. That ship had sailed. But since then, the orc surely caught new ones."
"He intended to do something to ease their burden, even if just a little bit."
"Approaching the slave caves, Rowan was only partially pleased to see the very same orc on guard duty as before. He had hoped to never again see his face… But… It could play to his advantage now."
"Dropping his hood, Rowan stepped out of the shadows and crossed the remaining distance in the open. Soon, the orc noticed him, and broke into a wide smile."

orc1 "Humi! Nice to see you! Checking on the slaves again? Ha ha! We be keeping an eye on them, no worry, no worry!"

"Rowan wanted to grit his teeth in fury, but instead smiled pleasantly to the orc guard."

ro "Good. Thought I’ll take a look. Make sure they’re behaving."

orc1 "Bwahaha! Sure, sure, come inside!"

"Rowan passed the orc without another word. For what it was worth, informing him about the planned escape made Rowan trustworthy enough to be allowed free entry into the slave caves."
"…"
"Inside, in the darkness, he saw scared eyed turn around to see the face of their new tormentor. None recognized him, and the fact he was human did nothing to ease their suspicion. Did words of his betrayal reach their ears?"
"Did they know some humans cooperated with the orcs? Or did they simply knew they couldn’t trust anyone anymore?"
"Rowan pushed these thoughts aside, Rowan regarded the slaves with cold indifference. He knew the orc was still watching him. He walked from cage to cage, eyeing the slaves. Old, young… Few women."
"The others were no doubt taken away for nightly “entertainment”."
"He heard the orc grunt and turn around. Perfect."
"Rowan approached the metal bars. A hunched over, elderly man sat in front of them, watching his movements with dead eyes. It did not take long to break a man."

#if Rowan was convinced by not wanting to go crazy in the intro
if introserve == 1:
    "Would Rowan turn out just like that if he remained in the Twin’s dungeon? Would he go crazy like the other captive inside the Bloodmeen cells or just… Wither into nothing, like this man?"
    "He betrayed his ideals to escape a fate he now forced upon others. How low had he fallen…"
#gain small amount of guilt and corruption
$ change_base_stat('g', 2)
$ change_base_stat('c', 2)

"Rowan crouched in front of him. The man did nothing, only kept staring. Rowan placed his finger on his lips, ordering him to remain silent."
"Slowly, he reached beneath his cloak and took out a previously well hidden, large package. He unwrapped it partially, revealing its content to the man."
"Food. Dried beef, mostly. And some herbs, for injuries."
"It was not much, Rowan knew that much. It would not last a day."
"But it was something. A ray of hope. It was the least the he could do."
"The man’s eyes widened, shining with greed and feverish hunger. His hand snapped forward to grab the package – only to be stopped by Rowan’s own."
"The hero held his hand in an iron grip, his expression grim. At first, the man tried to pull his hand back, but he had no more strength left in his weak body."
"… Slowly, the slave calmed down. He gave Rowan a small nod, unhappy with what was expected of him, but knowing he had no choice on the matter. Rowan released his arm, and the old man grabbed the package carefully."
"Clutching it to his chest, he hurried to the other slaves, to share what given to him."
"Rowan stood up, and adopted his best nonchalant expression. He returned to the orcish guard, and engaged in some casual slaver-to-slaver conversation about future slave raids and how joining the twins would provide orcs with ample raiding opportunities."
"Once Rowan was sure the slaves hid the provisions away, he bid the orc farewell, and left the caves."
"It was a small gesture. But perhaps it would help rekindle that small ember of hope, which Rowan had to extinguish in the earlier slaves…"
# lose some personal gold and guilt (partially offsets the penalties for betraying the slaves earlier)
$ change_personal_gold(-20)
$ change_base_stat('g', -2)
jump campMenu


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_woodcarver:
#The Woodcarver
# init
$ event_tmp['spot_success'] = False

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade

"Orcs were never known for their discipline, a fact Rowan exploited several times during the war."
"While most warchiefs usually understood the importance of maintaining a secured perimeter around the camp, forcing regular grunts to keep watch and stick to the established patrol routes was never an easy task."

#feud is unresolved
if orciad_state <= 1:
    "His future allies were no different. With every step, he kept finding more and more gaps in their defenses."
    "With their leadership divided, sneaking inside to poison their food supplies or to set fire to their tents would have been child’s play. He could only hope things would improve once the chain of command is restored."

#else
else:
    "Despite that, it seemed the orcs had no intention of leaving themselves exposed."
    "Several watchtowers have been constructed at the edges of the camp, and while they were located too far from one another to properly fulfill their function, they were nevertheless all manned, with keen eyed orcs watching him suspiciously as he passed under them."
    "He also passed several patrols. One of them even questioned him, rightfully finding his snooping around their defenses suspicious."
    "Leveraging his position as Andras emissary and the warchief close confidant, he quickly managed to get them to leave him alone, but judging by their expressions they would no doubt inform their supervisors of this incident."
    "All in all the camp was better protected than he expected. There were still some blind spots, and someone like Rowan would have little trouble infiltrating it, but it was something they could work on once the army was integrated with their own forces."
    "With some effort, they could be brought up to human standards."

#rejoin
scene bg31 with fade
show rowan necklace neutral behind bg31
show wild orc neutral behind bg31

"As Rowan was walking along the edge of the camp, something caught his attention. A lone orc sat on a fallen tree, away from his compatriots. Judging from the amount of scars on his back, he must have been one the orcs that once served in Karnas invasion force."
"Maybe even from the very start of his conquest. Orc veterans were a rare find, so it might be worth to exchange a few words with him."

menu:
    "Approach him.":
        $ released_fix_rollback()
        "Driven by curiosity, Rowan approached the old warrior. Quickly, he noticed his initial assumption that the orc was keeping watch of the distant woods was incorrect. The orc wasn’t looking into the distance, instead, he had his eyes focused on something in his hands."
        "It was an almost finished wooden figurine. With swift movements of a hunting knife in his right hand, the orc worked it relentlessly, not paying much attention to Rowan."

        #spot check: dc10
        if check_skill(10, 'spot')[0]:
        #success
            $ event_tmp['spot_success'] = True
            "Neither did he pay any attention to the two orc kids, hiding in the tall grass nearby. The younglings observed the unexpected craftsman with visible excitement, whispering between themselves."

        #rejoin
        "Knowing better than to interrupt someone so engrossed in his work, Rowan stopped nearby, and continued to observe without a word."
        "The figurine was that of a feral wolf, shown prowling."
        "Baring its teeth, the beast growled at some unseen opponent. Rowan couldn’t see all the minor details from where he was standing, but he quickly noticed, that even though the carving was rather crude, it was no doubt exceptional work."
        "There was a primal charm to it. The wolf looked almost lifelike. Maybe it was something the orc had to fight at some point his life? Rowan couldn’t tell."
        "Meanwhile, the orc continued to carve the hard wood, finishing the last of the wolf’s paws. The knife, far too big for such delicate work, was nevertheless wielded with great finesse, cutting into the wood precisely as its owner desired."
        "The orc not only had plenty of experience, but, as Rowan imagined, had to have no small amount of talent in order to produce such a realistic replica."
        "It was almost bizarre, for an orc, who usually were seen as little more than simple brutes, to be capable of creating something so enchanting."
        "As the orc’s work was almost at its end, Rowan decided to stick around and see what the amateur craftsman intended to do with it."
        "Fifteen minutes later, the figurine was finished. The orc put his knife down, and turned the wooden wolf in his fingers several times."
        "Rowan couldn’t quite read his expression. Was he happy with the result? He continued to wear the same face as when he was working – that of bored indifference."
        "Without as much as a word, the orc tossed the figurine over his shoulder."

        #if previous spot check succeeded
        if event_tmp['spot_success']:
            "In an instant, the two orc kids jumped forward, trying to get their hands on the wooden wolf. Kicking and screaming, they started fighting over it, neither willing to part with what was apparently seen as a valuable trophy."

        #else
        else:
            "Out of nowhere, a pair of two orc kids jumped forward, trying to get their hands on the wooden wolf. Kicking and screaming, they started fighting over it, neither willing to part with what was apparently seen as a valuable trophy."

        #rejoin
        "Meanwhile, the orc took another piece of wood, and started his work anew, not bothering to acknowledge neither the fight nor his silent audience. Seeing as they wouldn’t get anywhere without him speaking up, Rowan decided to finally address the orc."
        ro "Were you not satisfied with the result?"
        "The knife stopped midway, and his owner looked up. For what it was worth, he didn’t seem too annoyed at being interrupted. Furrowing his eyebrows, he answered in low monotone:"
        wo "Is worthless."
        "-and added nothing more. Rowan looked over his shoulder, at the fighting kids."
        ro "The kids might disagree."
        wo "Kids dumb. Is worthless."
        "A long silence followed. Despite the harsh words towards his own creation, the Orc didn’t seem to be displeased at it."
        ro "Then why make it?"
        "The orc shrugged."
        wo "Good for boredom. But is worthless."
        "In Rowan’s eyes, the wooden toy was far from worthless. While not the most intricate work of art, it was nevertheless a pretty trinket, it would probably sell for a nice penny at any human bazaar."
        "He told him just that. Again, the orc shrugged in response."
        wo "Pinks dumb. Is worthless. All wood animals worthless."
        "Another long silence followed, broken only by the sounds of the two kids still fighting. Rowan heard a victorious shriek, and noticed one of them finally triumphed over the other."
        "Holding the figuring high to the sky, he now ran back to the camp, laughing with glee. His companion limped behind him, muttering curses."
        "The woodcarver didn’t look in their direction. But Rowan noticed his expression grew distant, and his thumb caressed the wood piece he still held onto almost affectionately. The moment passed in a blink of an eye, and the orc now wore the same bored scowl as he did earlier."
        "… Did the orcs even understood the concept of art? For them, the wooden animal might have been truly worthless. It only served as something for the kids to fight over."
        "But if the orc wanted to created something “valuable”, then he could’ve made a carving of an orcish warrior. Rowan knew some orcs thought they brought good luck, and would be willing to pay for them."
        "Yet he chose to make wooden animals. Why? Was it for the kids?"

        #if the player has scene the orc families scene
        if ev_happened('orcish_families_and_neutrals'):
            "Men usually didn’t participate in their education, so was it the only way he could do something nice for them without being ridiculed for it?"

        #rejoin
        " Or did he simply enjoy making something that looked nice, despite it not having actual value? Rowan couldn’t tell, and his strange companion was unlikely to shine further light on the matter, having already resumed carving the next figurine."
        "…"
        "Maybe the orc himself didn’t quite understand why he kept making the figurines.  All orcs were raised to be warriors. To enjoy something that didn’t involve violence… Must’ve felt wrong to the orc."
        "But it didn’t stop him from doing it."
        "Rowan couldn’t help but smile a little."
        ro "I see. I apologize for taking your time."
        "The orc nodded slightly, his knife cutting into the wood."
        "He added nothing else, and Rowan knew better than to keep pestering the orc. He bid the woodcarver farewell, and resumed his earlier task of checking the defense perimeter, his spirits a bit higher from the odd encounter."
        #lower guilt by small amount
        $ change_base_stat('g', -2)
        $ woodCarverSaw = True
        jump campMenu

    "Move along.":
        $ released_fix_rollback()
        "Rowan considered speaking to the orc, but he doubted the old warrior would be able to offer any valuable insight. Orc expertise lay in rape and plunder – and Rowan had no intention of seeking advice in that area."
        "He left the orc alone, and resumed his inspection."
        jump campMenu


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_unlucky_slave:
#The (un)lucky slave.
#Requires seeing the “Orc families” event.

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade
show rowan necklace neutral behind bg26

#if feud is unresolved
if orciad_state <=1:
    "Scouring the camp for further displays of internal division that he could use to his advantage, Rowan came across an unusual sight."
#else
else:
    "Inspecting the camp of his allies, Rowan came across an unusual sight."

#rejoin
"As he walked past the section where the orc mothers resided, he noticed a pale figure sitting by the side of one of the tents. A plain, human woman, in a slave collar, but also dressed up – in what appeared to be orcish garments."
"Hunched over a with needle in her hand, she was repairing a pair of torn pants. Even at a distance, he could see that for a slave, the woman was much healthier than what Rowan would expect. Far less malnourished."
"Curious, he approached her. He took down his hood, hoping the simple gesture will help garner at least some goodwill in the woman."
"But that seemed to have the opposite result. When the girl turned her head up at the sound of his steps, and she saw his face, fear entered her eyes. She stood up abruptly-"
"- revealing the soft bulge of her stomach -"
"- and turned around, trying to flee. She seemed to have forgotten her position, for she stopped midway at the sight of the orcs that naturally filled the place."
" Overcome with terror, she turned to Rowan once more, and then clumsily tried to tip toe away from the hero, as if that actually made her behaviour any less suspicious."

menu:
    "Call out to her.":
        $ released_fix_rollback()
        ro "Wait! I mean you no-"
        "The woman shook her head, not willing to listen. Hiding her face in her hands, she turned away from the hero."
        orcm "What is this commotion?!"

    "Stop in your tracks.":
        $ released_fix_rollback()
        "Rowan stopped. Was the woman forbidden from interacting with other humans? If so, she would get into trouble if he tried to talk with her."
        "Instead, he raised his hands, and took a step back."
        orcm "Ha! Afraid of a pregnant woman, human?"

$ matronName = "Orc Matron"

"An elder orc matron came out from the nearby tent. Scars decorated her lithe body, but the years took much from who Rowan assumed was once a respected warrior. Her hair was gray and thin. Wrinkles decorated her face, and one of her eyes was whited over, blind to the world."
"But the other was healthy and alert, and as soon as it recognized Rowan, turned ice cold with hatred."

#if feud is unresolved
if orciad_state <= 1:
    orcm "Warbringer. Have you grown tired of sowing lies among our kind? Checking how many of our younglings are big enough to carry an axe? I’m afraid you will have to wait quite some time for this one."

#else
else:
    orcm "Warbringer. Come to inspect your master’s legions? See how many of our younglings are big enough to carry an axe?  I’m afraid this one is not quite ready to join your legions of doom."

#rejoin
"She bared her teeth, smiling wickedly."

orcm "I guess the girl could join, if you need her to. Not much of a fighter this one, but I believe human women can be skewered by a sword just like an orc."

"Rowan found himself at a loss for words, stunned by the sudden hostility. But, not being easily intimidated, he quickly regained his composure and met the woman’s glare with his own cold, indifferent expression."

ro "I was merely passing by. Nobody plans to send children, or pregnant women, to war."

orcm " Is that so? Oh, bless the ancestors then! Isn’t your master just the kindest of all demon lords? Please, send him over the next time he visits, so I can suck his cock and kiss his ass in gratitude! Oh, bless be the demon boss! "

"She bowed mockingly, her voice dripping with venom. Behind her, the human woman continued to observe the two, hiding behind the tent."

#if feud is unresolved
if orciad_state <= 1:
    "Rowan frowned. Few orcs lived pass forty, and this woman was well in her fifties. She likely had at least some degree of respect among other orcs, and even though he no longer needed to seek support from them, hearing her speak of Andras so coldly did not bode well."

#else
else:
    "Rowan frowned. Few orcs lived pass forty, and this woman was well in her fifties. She likely had at least some degree of respect among other orcs, and hearing her speak so coldly of Andras was alarming to say the least."

menu:
    "Intimidate her into obedience.":
        $ released_fix_rollback()
        $ orcMatronState = 1
        #if might is right
        if society_type == 'might':
            ro "Master Andras will soon lead your kind into victory over all humans in Rosaria. And he does not take kindly to dissenters. You would be wise to show him respect he deserves."
        #else
        else:
            ro "Emperor Andras will soon lead your kind into victory over all humans in Rosaria. And he does not take kindly to dissenters. You would be wise to show him respect he deserves."
        #rejoin
        orcm "Ha! What’s this? A slave threatens a free orc?! What’s next, will the sky rain rotten fish? Will Solansia herself appear before us to lick my cunt? Haha!"
        "Her fake smile disappeared, now replaced with a furious scowl."
        orcm "I have no patience for your poisonous words, Warbringer. Leave, and bother me no more. Pray I die in servitude to your master."
        "The air around them grew heavy."
        "Rowan feared confrontation with the orc matron was inevitable, however, after some consideration, he decided to back down. If the woman started causing trouble, it was the warchief responsibility to take care of her."
        "He would have to ask about the pregnant girl some other time. Throwing the matron one last threatening glare, he retreated. He had other things to take care of."
        jump campMenu

    "Address this diplomatically.":
        $ released_fix_rollback()
        "Rowan’s lips tightened. She was not the first orc to try an offend him. But he had a feeling there was more to the matter than mere dislike of demons and humans. At the moment, confrontation would lead him nowhere."
        "Instead, he decided it would be better to try and coax out some information first."
        ro "You called me “Warbringer” earlier. Why?"
        orcm "Isn’t that what you are, slave? A bringer of war? Bringer of death?"
        "Her face twisted in rage."
        orcm "We heard of your master, Warbringer, of the red demon lord-apparent. Not a chosen Kharas, this one. If he was, he would strike both Ulcro and Batri, the two fools, and have us all kneel. No. He’s far too weak for that, is he not?"
        orcm "And like all weak fools, what he lack in power, he makes up in ambition. He dreams of being the next demon lord I bet. And for that, he needs us, no? He needs mindless slaves to bleed for his fool’s crusade.  "
        #if feud is unresolved
        if orciad_state <= 1:
            orcm "And so he sends you, his trusted slave, to sway us to his cause. To bring an end to this ridiculous feud, and have us march along him. It’s only been a ten-year since your heroes slayed the previous demon lord, and yet you already bring a new war to us."
            orcm "And with you carry a collar. One you know we will put on ourselves willingly."
        #else
        else:
            orcm "So he sent you, his trusted slave, to choose the willing puppet to lead his army."
            orcm "A slave brought us a collar, and we happily put it on ourselves. It’s only been a ten-year since your heroes slayed the last demon lord, and yet we already sold ourselves into slavery once more."
        #rejoin
        "Bitterness entered her voice, and for a moment, her mask of anger dropped, revealing the pain that ran underneath."
        "She fought under Karnas, no doubt. What did she lose in his service, that made her despise the demons so much? So much, that she was able to overcome the orcs natural desire for war?"
        orcm "Centuries after centuries, the Kharos chosen comes to us, and demands we spill blood in his name. And like the fools we are, we obey, only to be slaughtered by your kind."
        orcm "How long will this go on, Warbringer? How many more sons, daughters and loved ones must be sacrificed to fuel ambitions of demons like your master?"
        "A dry laugh escaped her lips."
        orcm "I guess it doesn’t really matter to you, does it? No, I do not believe it does. You’ve already betrayed your own kind, I doubt you care for mine."

        #if corruption is greater than 49
        if avatar.corruption > 49:
            $ orcMatronState = 2
            ro "..."
            "And she was right, he did not."
            "Slaves to Kharos or not, he could not forget the countless atrocities orcs committed during the last war. Rape, murder, slavery. Even if they were done at Karnas orders…"
            "… Then the countless crimes orcs commit during the centuries it takes for another demon lord to arrive, were not."
            "Demonic heritage or not, orcs were still responsible for their own fate."
            ro "I do not. And neither do you care for humans, so let’s drop the pretense."
        #if feud is unresolved
            if orciad_state <= 1:
                ro "Whether you like or not, once the chiefs feud is over, your brethren will fight for us. But I assure you, I have no intention of letting you mindless brutes drag me down."
        #else
            else:
                ro "Whether you like or not, your brethren will fight for us. But I assure you, I have no intention of letting you mindless brutes drag me down."
            #rejoin
            ro "The twins are far more cunning than Karnas was. Things will turn out differently this time."
            orcm "More poison. Do you think-"
            ro "I don’t have time to listen to some decrepit old woman’s depressing backstory. You have two choices here, hag. Fall in line, and help us conquer the six realms. Or run. I care not which."
            "… Her hand reached for the dagger by her side."
            orcm "There is a third choice here, Warbringer…"
            "Rowan smiled slightly. "
            ro "You are free to try. But even if you succeed, it won’t change anything."
            "The two stared one another, Rowan’s cold eyes into the orc’s furious one. Neither moved an inch."
            "Finally, the matron relented. Her shoulders dropped, and all strength seemed to leave her posture."
            orcm "No, it would not. Another slave would merely take your place. "
            orcm "… Do your worst Warbringer."

        if avatar.corruption < 49 or introserve == 3:
            $ orcMatronState = 3
            ro "…"
            "It was true Rowan found it difficult to sympathize with the orcs. Slaves to Kharos or not, their kind committed countless atrocities, both during the war, and outside of it – of their own accord."
            "They were corrupt to the core, and a few odd individuals with a conscience did not change that fact."
            "But… Whether he liked it or not, they were his underlings now. He had no intention of simply throwing their lives away without a good reason."
            ro "… It is true, that until now, your masters haven’t been exactly… Considerate of oricsh lives. But we have no intention of repeating their mistakes."
            ro "The twins are far more cunning than Karnas was. The reason why Andras didn’t simply slay both Ulcro and Batri wasn’t because he was unable to."
            ro "It was because we believe that willing and organized orc warband makes for a far better ally than some leaderless mob."
            orcm "Empty words, Warbringer."
            ro "Perhaps.  But even if we did leave you alone… Do you really believe you wouldn’t find some other war to fight with?"
            "The orc matron stared at him for a long time."
            "Finally, she turned her head away."
            orcm "No, I do not."
        if avatar.corruption < 49 and introserve != 3:
            $ orcMatronState = 3
            "Rowan felt his throat tighten. “Betrayer of humanity”. “Warbringer”. He could secretly plan a thousand plots to bring forth the Twins downfall, but for now, that was all he was. And while he couldn’t exactly sympathize with the orcs…"
            "They were murderers and rapist, though how much of their vile nature stemmed from their corrupt ancestry was unknown to him…"
            "The Matron’s words wound him in ways he did not expect. How much suffering will he bring to those around him, before an apt opportunity to backstab his accursed masters presents itself? How many more speeches like this one will he be forced to listen to?"
            "Usually, he kept those thoughts pushed aside. But every now and then they surged forward, only to be forced down in a moments noticed."
            "The same happened now – but for a second, his usually unreadable expression must have slipped, for he saw the orcs eyes go wide in surprise."
            orcm "..."
            ro "..."
            "Rowan swallowed heavily."
            ro "This time things will be different. No more blood will be spilled than absolutely necessary."
            orcm "… Aye, that would be nice."
            "A sad smile graced her lips."
            orcm "But I fear you are not in any position to offer such guarantees, slave."
            "As far as she was concerned, he was still only a messenger. A powerless puppet to Andras Perhaps she would think differently if she knew who he really was."
            "… But he already revealed far too much than he should’ve. It was best to keep quiet for now."

        #rejoin
        $ emmaMet = True
        "An uncomfortable silence followed. The orc’s anger subsided, replaced by melancholy. Now that the matron was properly… Subdued, he could ask her about the pregnant woman. The plain girl still watched them from a distance, too far away to hear their quiet, if lively, “discussion”."
        "Rowan nodded in her general direction, prompting the orc to turn around."
        ro "This girl. She looks… Taken care of."
        orcm "… She is. Emma! Come here!"
        "The girl approached them shyly. She kept her head down, refusing to look Rowan in the eyes."
        "His initial assessment proved to be correct. He couldn’t see any signs of beatings, and her cheeks had a healthy tint to them. While the slavery had clearly taken its toll on the girl, it wasn’t the level of physical abuse he came to expect from the orcs."
        "There was only one explanation to that."
        ro "She carries a half-orc."
        "He stated more then asked. The matron bared her teeth in a humorless smile."
        orcm "Little Emma liked getting her cunt stuffed so much, she kept asking to be fucked every night. Who knew she would get pregnant?"
        "The poor girl turned red in shame, but said nothing."
        orcm "As to what she carries… We do not know. Maybe an orc. Maybe a human. The child will prove who they are."
        "Rowan furrowed his brows. That… Wasn’t how it worked. Half orcs were rare, but they did exist. Almost exclusively conceived through violence, among humans, they were usually pariahs. Apparently orcs did not view them this way."

        #if corruption is greater than 49
        if avatar.corruption > 49:
            $ emmaIgnored = True
            "His curiosity sated, Rowan bid the orc matron farewell. He had far more important things to do than concern himself with every human slave he stumbled upon."
            jump campMenu

        #else
        else:
            ro "I see. Do you mind if I talk with Emma in private?"
            "The matron shrugged in response."

        #if feud is unresolved
        if orciad_state <= 1:
            orcm "Do what you want, Warbringer."

        #else
        else:
            orcm "It’s your camp now, Warbringer."

        #rejoin
        "The orc left them alone. Emma didn’t seem all too happy about that – if anything, her expression became even more pained than before. Rowan led her to the bench she was residing on earlier, and sat beside her."
        "He was considering how to help the girl calm down, before the pressure finally proved to be too much for her, and she exploded suddenly-"
        emm "I didn’t want to! I didn’t-!"
        "Her voice broke, and she hid her face in her hands once more."
        emm "I didn’t- I didn’t want to, but- They worked us hard, that I thought it would- that it would be easier to just…"
        ro "..."
        "Rowan placed his arm around her, and hugged her gently."
        ro "It’s ok. You did what you had to do. Nobody is judging you."
        emm "I thought it would be easier! I just thought it would be easier…"
        "She started to weep in his arms, while Rowan whispered soothing reassurance to her. There wasn’t much he could do about her current predicament, not right now. But… Even if all he had to offer was this momentary kindness, it was still better than nothing."
        "Perhaps later, he will be able to help her in some other way. But not now."
        #lower guilt by small amount
        $ change_base_stat('g', -2)
        jump campMenu


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label meeting_the_priest_of_kharos:
#Meeting the priest of Kharos
#Requirement: Third visit to the camp (for reason no other than for the initial description to make sense)

$ change_mp(-5)
$ prevent_tile_exploration()

scene bg26 with fade

#first time intro
if orciad_priest_visit_count > 0:
    jump .after_intro

"During his last visit to the camp, Rowan had seen a rather curious gatherings of orcs, carrying various equipment, depart from the settlement, to head to the nearby words. While armed, they clearly weren’t heading out for a raid – too many of them were visibly injured."
"At least one of them was limping, and another one was missing an eye. One orc was ostensibly hiding his right hand, and back then Rowan suspected he was trying to hide some sort of serious injury."
"Today, again, he noticed the same gathering. While he could no longer see the one eyed orc, the limping one was still there, and so was the one who attempted to keep his hand hidden. They were preparing for another departure."
"Not willing to let the opportunity pass him by again, Rowan approached the gathering, and inquired about its exact purpose."

lorc "Priest teaches. We go."

"… Was the only answer he managed to get out of them. Contrary to most orcs he met thus far, this group wasn’t particularly talkative."
"They didn’t even bother to call him a “demon cock-sucker”, which was a refreshing change of pace."
"Idly, he wondered who this “Priest” was. From what he knew, the orcs usually referred to their spiritual leaders as “shamans”. A “Priest” could only mean…"
"A servant of Kharos."
"While he had seen signs of Kharos worship around the camp, the orcs did not strike him as particularly religious, and he had yet to meet a single priest of the Many Faced God. Such an opportunity did not present itself often."
"He asked the orcs if he could join them, and while none of them looked too pleased about the prospect, neither voiced their opposition out loud."
"That was good enough for him, and soon he was walking some distance behind the orcs – as to not irate his new companions with his presence."
"Not least not any more than necessary."

scene bg3 with fade
show rowan necklace neutral behind bg3

"… The orc priest was not what Rowan expected."
"Rowan had his share of stories with Kharos clerics back in the war, but those were usually demons, and as such usually adhered to very stereotype of a cleric to a dark god. But the orc priest, on the other hand, looked almost… Mild in comparison."
"The priest was waiting for the orc group at a small clearing in the forest. Sitting on a large rock, he greeted them with a wide smile."
"He didn’t appear to be particularly stronger or more intimidating than any other orc Rowan met thus far. If not for the sigil of Kharos tattooed on his bare chest, Rowan might have easily mistaken him for any other orc."
"The priest wasn’t alone. By his side stood four orcs - three men and one woman. His acolytes, Rowan presumed."
"Still silent, and still smiling, the priest pointed to the grassland around them. A group of orcs split off without a word, each one heading to a different location. Meanwhile, the priest beckoned to one of the other orcs to come forward."
"Rowan continued to watch all of this from a distance, neither hiding, nor trying to presents himself to the priest yet."
"But his arrival did not go unnoticed. The priest’s eyes met his own, and Rowan could swear his smile grew wider. But he said nothing of the hero’s presence. Instead, he addressed the orc that came forth."

orcp "Speak your shame."

"His voice was low, steady. He spoke slowly, as if savoring every word."

lorc "Varf slow. Varf let slave run away."

orcp "Great shame. Go with Sog."

"One of the acolytes stepped forward, and led the orc away. The processes repeated itself several times, with acolytes returning to swiftly to take away the next orc."
"It didn’t take long for Rowan to realize the purpose of this gathering."
"He saw the limping orc from before set up several targets on the trees by the edge of the clearing. With a rather primitive bow in his hands (how many orcs did Rowan ever saw with a bow?) he was practicing archery."
"The orc that kept hiding his hand – which Rowan could now see lacked all but the two smallest fingers – was trying to fend another orc with a sword in his left hand.  Another, far away from the central group, was attempting to dodge blows with a blindfold over his eyes."
"Training. They were all training. Actually training, not just… Starting fights."
"Rowan kept his astonishment to himself. Despite taking care of the orc soldiers in the Twins service, he really did not understand much about their culture."
"A few moments later, the last of the orc managed to find a teacher, and the priest turned his eyes to Rowan. Just as before, he beckoned for the man to step forward. His smile had yet to drop, even for a moment."

orcp "Human. Speak your shame."

#Check: Intelligence = DC: 10
if check_stat(10, 'intelligence')[0]:
#Success:
    ro "Ignorance."
    "The orc tilted his head, amused, then nodded in approval."
    orcp "Yes, ignorance."

#Failure.
else:
    ro "… Excuse me?"
    orcp "Ignorance, then."

    orcp "Your master did a poor job, educating you, human."

    ro "So it would seem."

    orcp " I will rid you of your shame, human. If you wish to be rid of it."

    ro "Just like you’re doing it for them?"

    "Rowan pointed to the nearby orcs. The priest nodded."

    orcp "Yes. They are weak."
    orcp "And to be weak is a sin in the eyes of Kharos."
    orcp "… But to remain weak is a far greater offense."

    "The priest added nothing more, and instead settled for observing Rowan. His gaze was sharp, piercing even. The priest spoke little, but saw much."
    "And the smile on his lips never reached his eyes."

jump orcPriestMenu

################################################################################
label .after_intro:
#after first visit intro

scene bg3 with fade
show rowan necklace neutral behind bg3

"Walking by the edge of the camp, Rowan realized he was nearing the area where the orc priest was holding his lessons. Should he visit him this week?"

menu:
    "Yes.":
        $ released_fix_rollback()
        "Rowan headed to the familiar clearing. The orc were already there, running their usual training regimes. The orc priest watched over them, grinning from ear to ear as he always did."
        "Seeing Rowan approach them, he lowered his head in what usually would be a respectful greeting, if not for the mocking smile on his lips. He greeted the hero jovially, and asked him if he could be of any assistance today."
        jump orcPriestMenu

    "No.":
        $ released_fix_rollback()
        "Now was not the time for it. He had more important matters to attend to."
        #don't trigger the event again this turn
        $ orciad_priest_visited = True
        jump campMenu

################################################################################
label orcPriestMenu:

$ orciad_priest_visit_count += 1

menu:
    "Ask about Kharos and Orcs":
        $ released_fix_rollback()
        ro " I believe this is the first time I’ve witnessed… Anything being done in Kharos name, in your camp."
        orcp "Rituals are… Pointless. Good for shamans."
        orcp "Kharos path is the path of action. Path of blood. Not of stories and songs."
        "Rowan waited for the orc to continue, but the orc merely tilted his head to side, amused."
        orcp "If you wish to learn of Kharos, you will not do so with words. Words are weak. Kharos must be learned with the body. With pain and blood."
        "… And that was all he had to say on the matter. Perhaps it would be best to consult Cliohna or the twins on such topics."
        jump orcPriestMenu

    #if feud is not resolved
    "Ask about the orc feud." if orciad_state <= 1:
        $ released_fix_rollback()
        "Rowan looked around the clearing. He wasn’t entirely sure about the loyalties of most of the gathered orcs, but he was fairly certain warriors of both warchiefs were present."
        ro "I see you have the respect of both Ulcro’s and Batri’s followers."
        orcp "All orcs know Kharos by blood. All follow him, no matter the chief."
        ro "… Does it really not matter?"
        "The priest did not answer at first. He watched Rowan intensely, and only after a while, responded in a low voice."
        orcp "… The stronger one will emerge victorious."
        "-His eyes narrowed ever so slightly-"
        orcp "… Unless someone interferes."
        orcp "Pick your master’s servants carefully, human."
        "It appeared the priest was neutral… To an extent. If the priest adhered to Kharos principle of “might makes right” – and he obviously did – then Tarish was likely unacceptable for him."
        "Though perhaps he could be swayed to either Batri or Ulcro… Once Rowan is able to gain his respect."
        jump orcPriestMenu

    "Ask about training.":
        $ released_fix_rollback()
        "As much as Rowan hated to admit it, his skills… Atrophied."
        "Several months of beating and starving during his captivity in Castle Bloodmeen took its toll on his body. He was far weaker than he was during the war, or even before his imprisonment. In the last few months, he had next to no time to rest and regain his strength."
        "… But as far as the twins were considered, whatever he did in the orc camps must have been important enough for him to stay there for several days at times. He could use this to his advantage…"
        "He wasn’t certain how reliable of a teacher the Kharos Priest would be, but months have passed, and this was his first opportunity at getting a trainer, any trainer. He doubted another occasion would present itself anytime soon."
        ro "Is the training for orcs only?"
        "The orc tilted his head, then spread his arms in a welcoming gesture."
        orcp "All who are ashamed of their weakness can join. Even you, human."
        "Rowan briefly wondered if the offer also covered slaves."
        "Probably not."
        "Regardless, whatever training he intended to ask for, it would likely take several days to complete. In order to gain the benefit of it, if he is recalled to the castle during that time, he would have to return to his training immediately after returning to the orc camp."
        "He had to consider carefully if now was the proper time to undergo it."
        #unlock training options
        $ orciad_priest_training_unlocked = True
        jump orcPriestMenu

    #All options below require said skill to have below 5 points in them. #5 is a joke option. Rowan can take any 3 of #1-#4 options, but they are all one time only.
    #Each training session takes 7/8 (?) movement points.
    #If the player runs out of Movement points during it, he gets a short message telling him he will return to finish it at the start of his next visit.

    #unlocks after discussing training
    "Train climbing." if orciad_priest_training_unlocked and orciad_priest_complete_count < 3 and avatar.skill('climb') < 5 and (not orciad_priest_complete_climb):
        $ released_fix_rollback()
        #if first time any training is chosen
        if orciad_priest_first_training:
            "Addressing the Priest, Rowan explained the nature of his problem. While he didn’t go into much detail on why his skills were no longer up to par, he did admit he was horribly out of practice with them."
            "The priest listened carefully, and while Rowan could see he wished to learn more, the hero kept his answers as vague as possible."
            "Finally, the orc gave up, and moved on to the nature of his request."
        else:
        #if after first time
            "Again, Rowan explained the nature of his problems. Again, he tried to be as vague as possible."
            "But this time, the priest did not press for further information. Rather, there was a hint of amusement in his eyes as Rowan talked."
            "Whatever he wished to learn about the hero, he already did from their first session. So now he simply listened, and once Rowan was done, addressed the problem."

        $ orciad_priest_first_training = False
        #rejoin
        orcp "Only slaves and fools keep their eyes on the ground. It is good you are ashamed of this."
        "He turned to the side and nodded at one of the acolytes. The orc stepped forward and beckoned for Rowan to follow him. He would be his instructor for this."
        "The two of them headed to the edge of the clearing, where the forest ended. They traveled along the border for a short while, with the orc inspecting every tree on their way."
        "They stopped suddenly, right next to a wide tree with plenty of branches."
        orca "Dis one, humi. Climb dis one."
        ro "What? Just like that?"
        "The orc grunted in displeasure."
        orca "Humi know wat do. Humi just need do."
        "… It was true his main problem was a lack of form, rather than the lack of knowledge. Jumping right into it might indeed be the best solution."
        "Rowan started climbing – but the moment his second foot left the ground, the orc behind his back slapped his hand with a broken branch, making him lose his grip."
        "Rowan fell down, hitting the grass. He looked up to shoot the orc a dirty look."
        orca "Lesson one. Learn to fall."
        ro "(How very enlightened.)"
        "And so began Rowan’s tedious training regime with the orc acolyte. After the initial “lesson”, the orc allowed him to climb the tree at his own pace."
        "Once he could do that at a fair speed, the orc started introducing handicaps – hitting him with a broken branch, or throwing stones at him to disrupt his concentration."
        "Surprisingly, the orc did offer him some actual advice - tips on how to use his feet and shoulders, how to balance the center of his body, and how to plan his route to the top."
        "Despite the simplistic language, and more or less overt hostility in his tone, the acolyte did know how his stuff, and put real effort to have the human improve."
        "After a few days, once he was sure Rowan could handle himself with relative ease, he ordered him to climb once more, but this time using only his right hand. This proved to be a challenge, but, again, thanks to the acolyte’s tips, Rowan was able to get fairly high as soon as the next day."

        #if rowan has enough MP left to complete
        if avatar.mp >= 7:
            "Finally, after a week of practice, his training was officially over. Some of his climbing skills returned – not to the level they were before the imprisonment, but it was progress."
            "He thanked the priest and his acolyte, and returned to the orc camp. Other responsibilities called."
            #gain 2 points in climb
            $ avatar.skills['climb'] += 2
            $ change_mp(-7)
            $ orciad_priest_complete_climb = True
            $ orciad_priest_complete_count += 1
            jump campMenu
        else:
        #Does not have enough movement points remaining.
            "Sadly, in the middle of his training he was summoned back by the twins to attend to the castle matters. He would have to finish his regime during his next visit to the orc camp."
            #see "returning to camp - climbing" text further down
            $ avatar.mp = 0
            $ activate_event('orciad_returning_to_camp_climb')
            return

     #unlocks after discussing training
    "Train sneaking." if orciad_priest_training_unlocked and orciad_priest_complete_count < 3 and avatar.skill('move_silently') < 5 and avatar.skill('spot') < 5 and (not orciad_priest_complete_sneak):
        $ released_fix_rollback()
        #if first time any training is chosen
        if orciad_priest_first_training:
            "Addressing the Priest, Rowan explained the nature of his problem. While he didn’t go into much detail on why his skills were no longer up to par, he did admit he was horribly out of practice with them."
            "The priest listened carefully, and while Rowan could see he wished to learn more, the hero kept his answers as vague as possible."
            "Finally, the orc gave up, and moved on to the nature of his request."
        else:
        #if after first time
            "Again, Rowan explained the nature of his problems. Again, he tried to be as vague as possible."
            "But this time, the priest did not press for further information. Rather, there was a hint of amusement in his eyes as Rowan talked."
            "Whatever he wished to learn about the hero, he already did from their first session. So now he simply listened, and once Rowan was done, addressed the problem."

        #rejoin
        orcp "There is no dishonor in ambushing your enemy. A foe weak enough to be caught unware does not deserve a fair battle."
        "He turned to the side and nodded at one of the acolytes. The orc stepped forward and beckoned for Rowan to follow him."
        "They headed to the side of the clearing – towards a blindfolded orc Rowan saw earlier. Rather than training with one of the acolytes, he was now assisted by a stocky orc woman, who eyed the hero angrily, but remained silent."
        orca "Change of plans. Yous train with humi now."
        "The orc lifted his blindfold. Seeing Rowan, he bared his teeth aggressively, but just like the orc woman, said nothing. The priest’s word was law here."
        "Together, they entered the woods nearby, and continued walking until the forest became quite dense. Then, they stopped, and the acolyte explained the exercise to them."
        "Rowan’s objective was simple – he was to sneak up to the orc, who would remain blindfolded. The orc woman would oversee the exercise – decide Rowan’s angle of approach, how much time he had in order to reach him, and when to start sneaking."
        "The nearby branches made things somewhat difficult for him, but other than that, it wasn’t anything that Rowan was unfamiliar with. It did take him some time to get into the right mindset."
        "Moving silently wasn’t just about stepping carefully – he also had to plan his route ahead of time, to avoid any spots that could be difficult to sneak through."
        "His opponent proved to fairly attentive, and was able to capitalize on most of Rowan’s mistakes. When evening came, while neither would admit it out loud, both of them benefited from the exercise greatly."
        "The following day, they trained back in the clearing. The orc woman gathered a basket full of dry branches, and scattered them around the area to make things a little bit more difficult for Rowan, since the sounds of other orcs exercising helped mask his approach."
        "She kept piling on handicaps for him – requiring him to circle the orc at least once, or giving him an oppressively short amount of time to reach him."

        #if rowan has enough MP left to complete
        if avatar.mp >= 7:
            "They altered between the two training regimes for a couple of days, before Rowan decided he couldn’t commit any more time to the exercise. They could keep ramping up the difficult, but other matters required his attention."
            "He thanked the two orcs, and departed from the clearing, content he was able to regain some of his lost abilities."
            #Gain Move silently +1, Spot +1
            $ avatar.skills['move_silently'] += 1
            $ avatar.skills['spot'] += 1
            $ change_mp(-7)
            $ orciad_priest_complete_sneak = True
            $ orciad_priest_complete_count += 1
            jump campMenu
        else:
        #Does not have enough movement points remaining.
            "Sadly, in the middle of his training he was summoned back by the twins to attend to the castle matters. He would have to finish his regime during his next visit to the orc camp."
            #see "returning to camp - sneaking" text further down
            $ avatar.mp = 0
            $ activate_event('orciad_returning_to_camp_sneak')
            return

    #unlocks after discussing training
    "Train hearing." if orciad_priest_training_unlocked and orciad_priest_complete_count < 3 and avatar.skill('listen') < 5 and (not orciad_priest_complete_listen):
        $ released_fix_rollback()
        #if first time any training is chosen
        if orciad_priest_first_training:
            "Addressing the Priest, Rowan explained the nature of his problem. While he didn’t go into much detail on why his skills were no longer up to par, he did admit he was horribly out of practice with them."
            "The priest listened carefully, and while Rowan could see he wished to learn more, the hero kept his answers as vague as possible."
            "Finally, the orc gave up, and moved on to the nature of his request."
        else:
        #if after first time
            "Again, Rowan explained the nature of his problems. Again, he tried to be as vague as possible."
            "But this time, the priest did not press for further information. Rather, there was a hint of amusement in his eyes as Rowan talked."
            "Whatever he wished to learn about the hero, he already did from their first session. So now he simply listened, and once Rowan was done, addressed the problem."

        #rejoin
        orcp "Eyes can deceive you. It is wise to try and hear."
        "To his immense surprise, the priest didn’t turn to any of his acolytes. Instead he jumped down from his rock, right before Rowan."
        orcp "I will rid you of your shame."
        "His smile grew wider. One of the acolytes came forward, and handed Rowan a blindfold, while another bought two staffs, one for each of them."
        orcp "Come, human."
        "Rowan’s expression grew tense. He didn’t like where this was going, but he couldn’t back down now. For what it was worth, he believed he wasn’t in any danger… But the priest clearly had something planned for him."
        "They walked to the side, to give themselves some room. Many of the surrounding orcs stopped their training regimes and turned around to observe the spectacle."
        orcp "Put the blindfold. Close your eyes. Then-"
        "The priest readied his staff."
        orcp "-Endure."
        "No further explanation was required. As far training went, this one was fairly standard. Bordering on cliché, even."
        "Didn’t mean Rowan could take it easy. Not with the priest of Kharos as his opponent."
        "Rowan put on the blindfold, and readied his weapon. With everyone watching, the clearing grew quiet. The only sounds that reached him were that of the surrounding forest."
        "He heard the staff whoosh through the air and his left hand exploded with pain. He had no time to react. He didn’t hear the orc approach him at all-"
        "Another whoosh, and this time it was his right hand that was struck. Another painful blow – but not nearly painful enough to prevent him from holding his own weapon."
        "… Of course. The priest didn’t want to cripple him. He merely wished to make him suffer."
        "Rowan gritted his teeth, and put his guard up."
        "Not that it would do him any good. For the next five minute, strike after strike, the orc’s staff would fall upon him. He could hear it – but never soon enough to react properly."
        "Quickly, his movements would become sluggish. He suffered far too much damage to keep up with the priest’s relentless assault. Rowan was about to give up, when he heard the staff come from his left – and this time, he was able to block."
        "But not because he unlocked some hidden talent and untapped power inside him. The priest simply slowed down his strike so Rowan could keep up with them now. He was toying with him."
        "He pushed him to the edge, and only then, when every step was agony to him, did he give Rowan the chance to react."

        #if corruption is greater than 49
        if avatar.corruption > 49:
            "The hero blocked another strike. If the priest thought Rowan, one of the six heroes who slayed Karnas, would allow himself to be humiliated like that, then he was in for a rude awakening."
            "The exercise lasted for about an hour. Normally, Rowan would drop from exhaustion at his point, but cold fury kept pushing him forward. Fury, and raw, undiluted, hate. It numbed the pain and sharpened his senses."
            "And it gave him the patience to wait for the right opportunity to present itself."
            "Finally, he heard it - a low whoosh on his left side. A vertical strike, aimed at his torso."
            "He didn’t block it this time. Instead he raised his arm, and when the staff hit him, locked it in place under his armpit. In a desperate attempt to strike back, he swung his own staff high, right where he believed the priest’s head was."
            "He felt his staff connect, but there was no grunt of pain."
            "Neither of them moved. Slowly, he released the orc’s staff, and lifted his blindfold."
            "The priest blocked his weapon with his left arm. His grin, which by now Rowan despised wholeheartedly, was ever present."
            orcp "Good. Lesson over."
        else:
        #else
            "The hero blocked another strike. If the priest thought he would break him with this, he would be sorely disappointed. Slave to the Twins or not, Rowan was one of the six heroes who slayed Karnas. He’s been through worse."
            "The exercise last for about an hour. By the end of it, Rowan pushed himself forward by sheer stubbornness only. The worst part in all of it was keeping his senses sharp, while also trying to ignore the pain. If he wanted to win, he had to be on his guard constantly."
            "… Though technically, this wasn’t a competition. It was a training session. “Winning” wasn’t the objective here."
            "And yet pride forbade him from just passively taking the beating."
            "He waited, teeth clenched, for the right moment to strike back."
            "Finally, he heard it - a low whoosh on his right side. A vertical strike, aimed at his torso."
            "Instead of blocking, Rowan flipped his staff, and delivered a downwards strike to where he believed the orc’s hand was."
            "He felt his staff connect, but there was no grunt of pain from the priest. No matter. Putting his strength into the strike, he forced his staff down."
            "…The enemy strike never connected. Slowly, Rowan took of his blindfold. Just as he suspected, he did manage to hit the orc’s staff. After pushing it to the ground, it was now locked under his own."
            "The priest did not try to free it. Instead, he kept his eyes on Rowan, with the usual annoying grin dancing on his lips."
            orcp "Good. Lesson over."

        #rejoin
        "After that, the priest never trained with him again. Whatever he wished to know about Rowan, he learned from that one exercise."
        "Rowan repeated said exercise twice, once with one of the acolytes, and then with one of the orcs from the camp."
        "He had a gnawing suspicion it was only to add credibly to the one he underwent with the priest - detecting incoming strike while blindfolded didn’t require keen hearing alone. One also had to have good reflexes and no small amount of fighting experience."
        "Unsurprisingly, at the end of the second day one of the acolytes told him that from now on, they would be training back in orc camp. The rowdy settlement was far better suited for practicing one’s hearing than the rather quiet clearing."
        "There, he sat for hours, eyes closed, trying to identify the many elements of a camp life by their sound alone. Fighting, arguing, fucking… Discerning all of that was a challenging task."

        #if rowan has enough MP left to complete
        if avatar.mp >= 7:
            "However, after a few days of practice, he started to get a hang of it. This would come handy in the future."
            #gain 2 Listening
            $ avatar.skills['listen'] += 2
            $ change_mp(-7)
            $ orciad_priest_complete_listen = True
            $ orciad_priest_complete_count += 1
            jump campMenu
        else:
        #Does not have enough movement points remaining.
            "However, as usual he had to take a break to address the ever mounting issues that plagued castle Bloodmeen. He would have to finish his training later."
            #see "returning to camp - hearing" text further down
            $ avatar.mp = 0
            $ activate_event('orciad_returning_to_camp_listen')
            return

    #unlocks after discussing training
    "Train dodging."  if orciad_priest_training_unlocked and orciad_priest_complete_count < 3 and avatar.skill('dodge') < 5 and (not orciad_priest_complete_dodge):
        $ released_fix_rollback()
        #if first time any training is chosen
        if orciad_priest_first_training:
            "Addressing the Priest, Rowan explained the nature of his problem. While he didn’t go into much detail on why his skills were no longer up to par, he did admit he was horribly out of practice with them."
            "The priest listened carefully, and while Rowan could see he wished to learn more, the hero kept his answers as vague as possible."
            "Finally, the orc gave up, and moved on to the nature of his request."
        else:
        #if after first time
            "Again, Rowan explained the nature of his problems. Again, he tried to be as vague as possible."
            "But this time, the priest did not press for further information. Rather, there was a hint of amusement in his eyes as Rowan talked."
            "Whatever he wished to learn about the hero, he already did from their first session. So now he simply listened, and once Rowan was done, addressed the problem."

        #rejoin
        orcp "A strong armor is good. Not needing armor is better."
        "He turned to the side and nodded at the female acolyte by his side. The orc woman stepped forward, and beckoned Rowan to follow her."
        "Together they approached one of the orcs that was training on his own near the middle of the clearing – a short and bulky old warrior, which Rowan guessed only recently reached adulthood. He was doing a traditional forward-backward sprint, running between two set rocks."
        "It was immediately obvious why the acolyte wanted to pair the two of them up. Being shorter than even Rowan, the orc had no chance of ever overpowering most of his brethren."
        "At the same time, his wide body structure also rendered him slower than most. These were natural handicaps for a fighter, especially for an orc, who favored raw physical power."
        "The orc acolyte explained the situation to the short orc. From now on, he would train with Rowan. The two would spar, with the orc being ordered to focus on trying to hit him, and Rowan – to dodge his strikes."
        " The orc woman would observe them, at least initially – with only 4 acolytes split between about 20 orcs, they usually didn’t commit all their time to one individual."
        "Judging from his partner’s expression, the young orc wasn’t particularly pleased by this arrangement. It was already shameful enough that he needed training, having to train with a human was simply adding insult to injury."
        "But the orc dared not to voice any opposition to the idea. Not with the acolyte nearby."
        "So they started to spar –"
        "-And it quickly became obvious just how horribly outclassed the orc was."
        "Weakened by his imprisonment or not, Rowan was still a trained fighter. Without a handicap, he could easily dance circle around the much slower orc."
        "He almost pitied his opponent, who, despite several failures, quickly adopted a determined expression, and kept trying to gain the upper hand over Rowan."
        orca "Wrong. All wrong."
        "The acolyte striked the orc with her staff, stopping their battle midway."
        orca "No good. Need more practice."
        "She started explaining the exercise routine both of them would follow in the upcoming day. Rowan was familiar with most of them – dot drills, shuttle runs, tuck jumps… The acolyte might not have been familiar with the proper terminology, but she knew her stuff."
        "The routine she had prepared for them would be no doubt exhausting, and it had to be diluted with some regular exercises so they don’t overexert their legs, but all in all, Rowan found it quite sensible."
        "Unfortunately, it did force both him and the orc to take numerous breaks during the day. Breaks they had to spend in each other’s company."
        "While Rowan had next to no intention of befriending any of the camp orcs, the heavy atmosphere and, frankly speaking, boredom of sitting around in silence proved too much for the hero to stomach. He started to chat the orc up. Just a little bit."
        "The orc wasn’t exactly friendly, but he must have been bored as well, since it didn’t take Rowan long to have him open up."
        "His name was Ulgan, and he proved to be a fairly decent fellow. He wasn’t too keen on sharing his story, but Rowan was able to piece it together quite easily from the vague answers the orc was giving him."
        "As he expected, from the earliest years, Ulgan didn’t have much success fighting his physically superior opponents. In the orc society, that usually meant ostracism – being relegated to menial tasks, more suited to a slave than a proud orc warrior."
        "He had to learn how to fight with his head, rather than his body – but even that only got him so far."
        "Rowan couldn’t help but feel for the orc. He showed all signs of an excellent military officer – a cool head, sound judgment, and iron determination. But for orcs, such qualities had no value if one couldn’t back them up with martial prowess. So much talent wasted…"
        "Bitterly, Rowan reminisced on how he himself was elevated to general. If not for the horrible situation on the front, the nobles would have never listened to a commoner like him."
        "Ironic how the two sides suffered from similar problems, despite being so radically different."

        #if rowan has enough MP left to complete
        if avatar.mp >= 7:
            "After a week, their training came to an end, and Rowan had to bid his newfound companion goodbye. He earnestly wished him good luck, hoping that Ulgan will one day gain the recognition he rightfully deserved."
            #note Rowan has met Ulgan
            #gain 2 Dodge
            $ rowan_has_met_ulgan = True
            $ avatar.skills['dodge'] += 2
            $ change_mp(-7)
            $ orciad_priest_complete_dodge = True
            $ orciad_priest_complete_count += 1
            jump campMenu
        else:
        #Does not have enough movement points remaining.
            "Sadly, one of his causal chats with Ulgan was interrupted by Jezera demanding his attention back in the castle. He would have to finish their training later."
            #note Rowan has met Ulgan
            $ rowan_has_met_ulgan = True
            $ avatar.mp = 0
            $ activate_event('orciad_returning_to_camp_dodge')
            #see "returning to camp - dodging" text further down
            return

    #unlocks after discussing training
    "Train escaping bonds." if orciad_priest_training_unlocked:
        $ released_fix_rollback()
        "Rowan briefly considered if he should allow a potentially hostile priest of a borderline mad god to tie him so he could practice breaking free."
        ro "…"
        ro "(Nope!)"
        jump orcPriestMenu

    #unlocks after discussing training
    "Leave":
        $ released_fix_rollback()
        "After some consideration, Rowan decided now was not the right time to concern himself with the orc priest and his training lessons."
        "Perhaps later."
        jump campMenu


################################################################################
label orciad_returning_to_camp_climb:
### returning to camp - climbing
#This text should appear when Rowan arrives at the camp the following week after not having enough MP to complete training, afterwards, return to usual orc camp option screen

"Before moving on to his usual business with the orcs, Rowan headed to the clearing where the priest of Kharos usually resided. He had to finish his earlier climbing lessons."
"It took a while to get back to the pace of things, but soon enough, Rowan was back in the established regime. A few days later, his training was complete."
"Some of his skill returned - not to the level they were before the imprisonment, but it was progress. He thanked the priest and his acolyte, and returned to the orc camp."
#gain 2 climbing
$ avatar.skills['climb'] += 2
$ change_mp(-7)
$ orciad_priest_complete_climb = True
$ orciad_priest_complete_count += 1
jump campMenu


################################################################################
label orciad_returning_to_camp_sneak:
### returning to camp - sneak
#This text should appear when Rowan arrives at the camp the following week after not having enough MP to complete training, afterwards, return to usual orc camp option screen

"Before moving on to his usual business with the orcs, Rowan headed to the clearing, to complete his sneaking training with the two orcs."
"Sometime later, Rowan was happy to note he got more or less all he could from the exercise. He could keep ramping up the difficulty, if he wanted, but he already wasted far too much time in the clearing. Other responsibilities required his attention."
"He thanked the two orcs and left, content that he was able to regain at least some of his lost abilities."
#gain Move silently +1, Spot +1
$ avatar.skills['spot'] += 1
$ avatar.skills['move_silently'] += 1
$ change_mp(-7)
$ orciad_priest_complete_sneak = True
$ orciad_priest_complete_count += 1
jump campMenu


################################################################################
label orciad_returning_to_camp_listen:
### returning to camp - hearing
#This text should appear when Rowan arrives at the camp the following week after not having enough MP to complete training, afterwards, return to usual orc camp option screen
"Before starting with his usual camp affairs, Rowan paid visit to the orc priest. He informed the acolyte he would remain in the orc camp for some time and would like to resume training."
"The next few days they continued their usual exercise of trying to untangle the many sounds that made the orc camp. In time, Rowan grew proficient enough in doing so that the orc acolyte judged his training complete."
"Once more, he regained a part of his old prowess."
#gain 2 Listening
$ avatar.skills['listen'] += 2
$ change_mp(-7)
$ orciad_priest_complete_listen = True
$ orciad_priest_complete_count += 1
jump campMenu


################################################################################
label orciad_returning_to_camp_dodge:
### returning to camp - dodging
#This text should appear when Rowan arrives at the camp the following week after not having enough MP to complete training, afterwards, return to usual orc camp option screen

"Upon returning to the camp, Rowan headed to the clearing where the priest of Kharos provided his lessons. There was no point in leaving his training unfinished, and he was eager to check on the progress Ulgan made during his absence."
"His newfound companion greeted him politely, and after exchanging pleasantries, they resumed their established routine."
"In the end, Rowan made considerable progress on his dodging skills, and managed to meet someone who might one day grow up to be a valuable ally. He earnestly wished Ulgan the best of luck, hoping he will one day gain the recognition he rightfully deserved."
#gain 2 Dodge
$ avatar.skills['dodge'] += 2
$ change_mp(-7)
$ orciad_priest_complete_dodge = True
$ orciad_priest_complete_count += 1
jump campMenu
