####### Abbey events ########

#Weekly research bonus.

#Choose one of the following options at random, it may change the normal outcome slightly.
init python:

    #Event 1: Neutral
    event('abbey_neutral', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)
    #Event 2: Choice
    event('abbey_choice', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)
    #Abbey Event:  Solansia’s Tears
    event('abbey_solansia_s_tears', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)
    #Abbey Event:  Up in Smoke
    event('abbey_up_in_smoke', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)
    #Abbey Event: Crouching Tiger, Hidden Monk
    event('abbey_tiger_monk', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)


label abbey_neutral:
#Event 1: Neutral
#Show chapel background.
$ change_research_bonus(1)

"After bringing in a small squad of soldiers and easily subduing the monks at the abbey, Rowan was surprised when it was Cliohna that arrived to take control of the structure."
"The sorceress spent around an hour looking through the library and other facilities before turning her attention to the people who'd called this place home. Each was given a private interview and gauged to see how susceptible they were to corruption."
"Eventually she selected some of the monks and used her magic on them to make them compliant and obedient to her, the rest she killed. Those spared were granted a crystal ball to communicate with her and receive orders."
"Satisfied with her new research assistants, Cliohna vacated the building without bothering to say anything else to Rowan. He was left to arrange for the soldiers to return and continue his explorations on his own."
#no effect.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label abbey_choice:
#Event 2: Choice
#Show chapel background.
$ change_research_bonus(1)

"With Rowan at the head and Cliohna in tow, a small attack force approached the abbey.  However, as they drew close the sorceress called a stop. There was something off about this place."
"She described it as the sweet scent of corruption. The sort of aura left by demons, this one in particular seemed to be a cubi with some magical talent."
"After, the approach changed from that of attack to that of diplomacy. The squad entered openly and without weapons drawn, instantly bringing the incubus out of hiding to meet his guests."
"He welcomed them into his abode and showed off how he'd charmed the monks and even brought in a few extra 'research assistants' to help him with his work. The demon was especially interested in the story of the twins and offered to swear his loyalty to them."
"In exchange for leaving him to his work in the abbey, he would put the library and his staff at Cliohna's disposal. Whether or not to accept fell to Rowan. He looked at each of the humans in the place that had previously been holy ground."
"They were all naked, or nearly so. Bleary eyed and perhaps underfed, but with dazed smiles on their faces. These men and women were sex slaves to an incubus."
"To accept would mean their continued enslavement. However, this demon was obviously intelligent and talented. He would be very useful as a researcher here."
menu:
    #Choice: Leave the abbey to the incubus sorcerer.
    'Leave the abbey to the incubus sorcerer':
        $ released_fix_rollback()
        "Rowan agreed to leave the abbey to him. Cliohna nodded her approval. Then set to work in establishing communication lines and research structures."
        "The man left her to it, wanting to get out of this place as soon as possible. Those faces were very unsettling."
        #Extra research point each week, gain corruption, gain infamy.
        $ change_base_stat('c', 2)
        $ change_base_stat('f', 2)
        $ change_research_bonus(1)
        return

    #Choice (if you don't have an unfilled dark sanctum): Banish the incubus.
    'Banish the incubus' if (castle.buildings['sanctum'].troops >= castle.buildings['sanctum'].capacity):
        $ released_fix_rollback()
        "Rowan refused his offered deal, then surprised the incubus when he demanded control of the abbey from him. The demon was enraged by the man's apparent gall, but proved to be no match for Cliohna's magic."
        "She struck him down in an instant, then casually lamented the loss of someone so talented. The hero just shock his head before helping the enslaved people return to their homes. At least those that the sorceress wasn't going to need for researchers."
        #Lose infamy, lose corruption.
        $ change_base_stat('c', -2)
        $ change_base_stat('f', -2)
        return

    #Choice (if you have an unfilled dark sanctum): Offer him a post in the Dark Sanctum.
    'Offer him a post in the Dark Sanctum' if (castle.buildings['sanctum'].troops < castle.buildings['sanctum'].capacity):
        $ released_fix_rollback()
        "Rowan instead presented a third option, travelling to Castle Bloodmean and serving the twins directly. A chance to establish himself in proper facilities with his own kind intrigued the incubus, so he agreed."
        "The hero returned the slaves that the demon would no longer be needing, and that Cliohna would not need as research assistants, then directed his new recruit back to the portal so he could join his peers under X'zaratl."
        #Lose infamy, lose corruption, gain 1 cubi sorceror.
        $ change_base_stat('c', -2)
        $ change_base_stat('f', -2)
        $ castle.buildings['sanctum'].troops += 1
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label abbey_solansia_s_tears:
#Abbey Event:  Solansia’s Tears

"Rowan had been called away at the worst possible moment."
"He had not wanted to leave the orcs alone, they had about as much self control as a sailor in a whore house, and about as much sense."
"But when Jezera had ordered that he go to the archive immediately in search of some mystical tome that Cliohna was after, he had no reason to defy her wishes."
"To make things worse, the book hadn’t even been there, but he would have to deal with that later."
"While he’d gone to look for the book, the orcs had gone straight to the chapel where they had found the abbey’s monks huddled up in fear."
"Unarmed, and more than likely also pacifists, they were not threat to the orcs, but that hadn’t stopped the savages from killing them all. "
"By the time Rowan arrived, their corpses lay strewn across the floor of the chapel, and the orcs were whooping and roaring in triumph."
"It was a horrible sight for any man to see, but what really disturbed Rowan was the bust of Solansia on the chapel’s altar."
"Blood had sprayed up, covering the statue’s chest, but only a few drops have reached her face, creating the illusion that the goddess was crying tears of blood."
"The whole thing started to make Rowan feel sick, so he left the orcs to their revelment, hoping he’d be able to put the whole thing out of his mind."

#gain medium guilt
$ change_research_bonus(1)
$ change_base_stat('g', 3)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label abbey_up_in_smoke:
#Abbey Event:  Up in Smoke

"First he had heard the bells, ringing loudly as he approached, and then he saw a plume of black smoke rising high into the blue morning sky."
"One of the orcs had gotten sloppy and broken from the squad upon spying an attractive young nun. Rowan had moved to stop him, but it was too late; they had been seen, and the alarm had been raised."
"The ringing had stopped now."
"They were an hour out when the incident occurred, and it had given anybody who might have been at the abbey ample time to escape before the invaders arrived."
"No doubt they had taken whatever they could carry, but as for the rest, they had no intention of letting it fall into the hands of Rowan and his masters."
"Flames now licked throughout the ground floor, making any sort of ingress impossible, and it wouldn’t be long before the fire consumed the entire building."
"There was nothing here for Rowan except ashes. "

#explored but no tech points
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label abbey_tiger_monk:
#Abbey Event: Crouching Tiger, Hidden Monk

"When they had arrived at the abbey, they’d been unable to find a single soul. The place looked like it had been abandoned, but the whole thing puzzled Rowan."
"If they had left, they had taken nothing with them."
"In fact, the entire place looked lived in; beds were unmade, unfinished manuscripts lay on the shelves were the monks had been working on them. Rowan half expected to find food still cooling in the dining hall."
"Still, a thorough search of the grounds by the troops had turned up nothing. It was like they had simply vanished."
"If he hadn’t tripped on the rug in the monks' workshop, Rowan would never had discovered the trapdoor below, cut into the floor so as not to be noticeable."
"Gripping the iron ring with both hands and giving it a hefty tug, light spilled into the small, cramped space below, illuminating the faces of the abbey’s terrified occupants."

menu:
    "Call the orcs to take the monks prisoner.":
        $ released_fix_rollback()
        "Rowan called out and ten minutes later, a dozen or so men stood in room, bound in iron chains."
        "Most of the monks were elderly, but even the faces of the younger men looked drawn from fear of their fate that was to follow."
        "Not wanting to look at them anymore, the hero ordered the soldiers to take the men back to the castle."
        #gain 12 prisoners, and medium guilt
        $ change_prisoners(12)
        $ change_base_stat('g', 3)
        return

    "Close the trapdoor.":
        $ released_fix_rollback()
        "If Rowan had had a difficult time finding the trapdoor, the orcs would be very unlikely to do so."
        "There was no need for these monks to suffer at the hands of his overlords, so he closed the trapdoor and placed the rug back over the top to conceal it once more."
        "He organized a hasty removal by the troops of anything that might be useful, and then was once again on his way, leaving the monks to return to their lives without further molestation."
        #lose some guilt
        $ change_base_stat('g', -2)
        return
