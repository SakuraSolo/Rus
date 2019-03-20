# random map events that happen on forests
init python:

    # Hunter's Trap
    event('hunter_s_trap', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Fairy spring
    #Requires Rowan not be very corrupt.
    event('fairy_spring', triggers='map_expl', conditions=('world.cur_tile_type == "forest"', 'avatar.corruption <= 6'), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Drider attack
    event('drider_attack', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # The Dead Knight
    event('dead_knight', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Necromancer's lair (malediction)
    #No requirements.
    event('necromancer_s_lair', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Forest's blessing (benediction)
    #No requirements.
    event('forest_s_blessing', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #The Trapped Dryad
    event('the_trapped_dryad', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label hunter_s_trap:
# Hunter's Trap

scene forest1
"Even survivalists of Rowan's caliber sometimes get caught unawares. Either because of momentary carelessness or just plain bad luck."
"Regardless of the cause, Rowan had now found himself with an old bear trap latched around his leg."
"It took him nearly ten minutes to free himself, but he was unable to carry on for the better part of an hour thanks to the incredible pain from the very nasty gashes now decorating his shin."
"Thankfully nothing was broken and there was no permanent damage."
"Once he got back to the castle he'd be able to get magical healing, but in the meantime he'd have to take things much slower and manage with just mundane bandages."
#lose two movement points, 1d6 + 1 dexterity damage injury until the end of the week.
$ add_effect(Injury('Wounded shin', 'reflexes', -dice(6)-1))
$ avatar.mp -= 2
#gain 10 xp
$ add_exp(10)
#end event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label fairy_spring:
# Fairy spring
#Requires Rowan not be very corrupt.

scene forest1
"Throughout most of the six realms there are small pockets of Solensia's power, around which beings of energy or strongly of the light tend to gather."
"Some of these nexuses have become the hearts of cities, others end up giving rise to great reefs in the oceans, and in this case, form the center of an enchanting forest glade with a fairy spring in the center."
"Rowan drank deeply of the pure water and filled his flasks from it before departing on his way.  Already he could feel the rejuvenating effects flow through his body."
"Jezera didn't care much for his report on the subject, and told him not to bother her about these pockets anymore."
#remove all injuries from Rowan
$ heal_injuries()
#gain 10xp
$ add_exp(10)
#end event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drider_attack:
# Drider attack

# Show forrest background.
scene forest1
$temp = current_weapon()
"Suddenly, a blur of black, white, and insectoid fur fell upon Rowan!"
"He lept back instinctively, whipping out his [temp] to face his attacker head on. The foe was a drider, a half-human half-spider monster."
"These monsters were native to the forests of Rosaria and among its most dangerous denizens. The one currently attacking Rowan, a male, obviously intended to make him into a meal if it had the chance."

# Fight challenge: total failure (should only happen when Rowan is very injured).
if avatar.wounds > avatar.base_mp * .5:
    "The creature's attacks were intense and brutal, forcing the hero back again and again. Under normal circumstances, Rowan would never have been fairing this badly, but his injuries were catching up with him."
    "After being bitten a second time and finding his strength was fading almost completely, Rowan made the decision to fall back to castle Bloodmeen. He sent a message to Jezera asking for an immediate recall."
    "Rowan vanished, leaving a very frustrated drider behind. So bad were his injuries that he was forced to rest for the remainder of the week just to get back on his feet."
    # End scene, add 5 xp return Rowan to previous space, current week of exploration ends, Rowan gains a strength injury.
    $ add_exp(5)
    $ push_to_previous_tile()
    $ add_effect(Injury('Drider bites', 'strength', -4))
    $ renpy.set_return_stack(renpy.get_return_stack()[:1])
    return

$ res_roll = check_combat(15)[1]
$ released_fix_rollback()
if res_roll < 7:
    # Fight challenge: partial failure.
    "This was not the hero's day, as he was fighting against the creature essentially blow for blow. Unfortunately, his foes blows could poison him, so Rowan was finding himself becoming weaker as the fight continued."
    "Thankfully he managed to force the creature to retreat in one desperate last attack. There was no way he could outrun a drider in the forest, so that was the only way he could turn this around."
    "Unfortunately poison didn't suddenly leave the body if you had a chance to rest for a few minutes. This was going to be another problem added to the pile."
    # End scene, add 5 xp Rowan gains a strength injury.
    $ add_exp(5)
    $ add_effect(Injury('Drider poison', 'strength', -2))
    return
elif res_roll >= 15 and (castle.buildings['pit'].free_space >= 1):
    # Fight challenge: total success (req: breeding pit with open space).
    # Rowan ends up capturing the drider and adds it to the breeding pit.
    "However, the fight quickly turned against the drider.  This beast was large, strong, and overconfident.  It obviously thought Rowan easy prey, which allowed the hero to turn its strength against it in short order."
    "Of course, there was always the possibility that things would go very badly for Rowan very quickly if he slipped up.  The drider's poison would cripple him if it managed to bite him.  It was fortunate then that Rowan didn't screw up."
    "He managed to crash the drider into one tree and then fling it down a hill where it landed in a heap, dazed.  Sensing an opportunity, Rowan quickly rushed down the slope and used some rope to bind the creature's legs and then sent a message to have it picked up."
    "A fully grown drider would be difficult to handle, but it was a prize for the breeding pits that couldn't be passed up.  How often did you capture a live drider without meaning to?"
    #End scene, gain 1 drider and extra exp.
    $ add_exp(15 + dice(10))
    $ castle.buildings['pit']._driders += 1
else:
    # Fight challenge: partial success.
    "The fighting was tense, with every moment being a chance at life or death. The hero was slightly better than his opponent, though he knew that a slip up would quickly reverse their fortunes due to the poison the creature possessed."
    "Finally he found his chance, and managed to lob one of the drider's legs clean off. It shrieked and skittered unsteadily for a moment, giving Rowan a chance to follow up and claim one of its mandibles."
    "Realizing it had been bested, the hero's foe turned away and fled into the woods. He knew that he wouldn't be able to catch a drider in the forest, even one missing a leg. Instead he simply claimed his prize and continued on his way."
    "If you could find the right alchemist or monster hunter, fresh drider poison glands were very valuable."
    #End scene, add 10 xp, get 25 gold and extra exp.
    $ add_exp(10 + dice(6))
    $ change_personal_gold(25)
    return
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label dead_knight:
    # The Dead Knight
    scene forest1
    $ released_block_rollback()
    'As the forest opened up into a small clearing. Rowan discovered, slumped against the trunk of a old oak tree, the body of a knight, riddled with arrows. This was the work of no single archer, he knew, but instead an entire gang of bandits.'
    'Against that number, even a man in armour had no chance. Many arrows had found the seams between where his plates fit poorly. A few had even punched clean through, leading Rowan think that it must have been cheap, and shoddily made.'
    'How long the body had lain there, he did not know, but it must have been a few days judging from the pungent smell of decomposing flesh.'
    'The armour was scored with tooth and claw marks as well, suggesting some of the larger forest scavengers had tried to feast on the corpse, before giving up.'
    'As far as the knight\'s killers were concerned, Rowan could see as few signs of human life in his current vicinity as he had while walking through the woods for the better part of the day.'
    'Removing the armour to search the knight would take time, leaving him exposed. He would have to think hard whether looting the body was worth the risk.'
    menu:
        'Search the knight':
            $ released_fix_rollback()
            jump .dead_knight_search
        'Leave the body':
            $ released_fix_rollback()
            'Deciding it was too dangerous, and not wanting to meet the same fate as the knight, Rowan decides not to search the body. Let somebody else take that risk, he thought, as he left it behind to continue his journey.'
            $ add_exp(5)
            return

label .dead_knight_search:
        # gain 10xp
        $ add_exp(10)
        $ res_roll = dice(4)
        if res_roll == 1:
            $ released_fix_rollback()
            'As Rowan suspected, the armour was cheaply made, and would offer more in the way of liability in a fight than it would protection. The sword, however, had been made by a craftsman of some skill.'
            'Either the dead knight had spent all his money on it at the expense of the rest of his equipment, or it had been a gift.'
            'Deciding it would be a waste to leave it here with a corpse than could no longer use it, Rowan took it from the body. At the very least, it would probably fetch a good price from the right merchant.'
            $ give_item('bastard_sword')
        elif res_roll == 2:
            $ released_fix_rollback()
            'As Rowan suspected, most of the armour was cheaply made, and would offer more in the way of liability in a fight than it would protection. The sword\'s blade was pitted, likely to shatter should it come into contact with something more solid.'
            'The helm, however, had been made by a craftsman of some skill. Either the dead knight had spent all his money on it at the expense of the rest of his equipment, or it had been a gift.'
            'Deciding it would be a waste to leave it here with a corpse than could no longer use it, Rowan took it from the body. At the very least, it would probably fetch a good price from the right merchant.'
            $ give_item('iron_sallet')
        elif res_roll == 3:
            $ released_fix_rollback()
            'As Rowan suspected, most of the armour was cheaply made, and would offer more in the way of liability in a fight than it would protection. The sword\'s blade was pitted, likely to shatter should it come into contact with something more solid.'
            'The gauntlets however, were a rare find. Expertly crafted, the plates locked together, but were well jointed to allow flexibility. Subtle runes etched onto the edges of the plate also hinted that the gauntlets had been imbued with some minor enchantment.'
            'Thanking the sisters for his luck, Rowan slipped the gloves into his pack.'
            $ give_item('gauntlets_of_might')
        elif res_roll == 4:
            $ released_fix_rollback()
            'As Rowan suspected, the armour was cheaply made, and would be offer more in the way of liability in a fight than it would protection. The sword\'s blade was pitted, likely to shatter should it come into contact with something more solid.'
            'Upon removing the boot, however, a small pouch of coins fell out from where he must have been hiding it in case of a robbery like this one.'
            'If whoever had killed him had searched him, they had not done so thoroughly enough, which turned out to be a stroke of luck for Rowan. Pocketing the coin, he thought that it had not turned out to be a bad day after all.'
            $ change_personal_gold(dice(20, 2) + 10)
        else:
            $ released_fix_rollback()
            'As Rowan suspected, the armour was cheaply made, and would offer more in the way of liability in a fight than it would protection. The sword\'s blade was pitted, likely to shatter should it come into contact with something more solid.'
            'After removing all the armour from the body, Rowan had nothing to show for it. If the man had been secreting anything on his person, it had already been picked clean by whoever had killed him.'
            'Now he was left with a wasted day, the rather unappealing corpse before him, and the hope that he\'d be able to get the smell of decomposition out of his head sooner rather than later.'
            #lose MP
            $ avatar.mp -= 1
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label necromancer_s_lair:
#Necromancer's lair (malediction)
#No requirements.

#Show forest background.
scene bg forest1

"While moving through the brush, Rowan noticed that something was wrong.  The background noises were growing quieter than they should be and he felt the tinge of magic in the air. He was on guard now, moving as quietly and as stealthily as possible."
"As he went further, the smell of rot started to fill the forest.  Birdsong and buzzing vanished entirely. This was a place of death and decay, the signs of necromancy. Sure enough, he encountered a zombie soon afterwards."
"It didn't notice him, but it's master that came soon afterwards did.  The man looked much older than he probably was, thanks to the toll on the body his dark art took. It was only through magical means that he was able to track Rowan this far, and then only thanks to having warded his slice of the forest."

#Stealth test (Move Silently skill): DC 12
if check_skill(12, 'move_silently')[0]:
    #Stealth test: Success.
    "Try as the necromancer might, neither he nor any of his undead servants, four of them now, were able to locate the hero. He took to the trees, silently shimmying from branch to branch and occasionally darting over the ground when it was clear."
    "Eventually he managed to get out of the corrupted part of the forest, at which point his hunter gave up the chase. Whoever that was, he didn't like guests and didn't seem to want anything to do with the rest of the world."
    #End scene.  20 xp.
    $ add_exp(20)
    return
else:
    #Stealth test: Failure.
    "Rowan took to the trees, silently shimmying from branch to branch. He came to a gap in the trees he'd need to dart through and waited until the necromancer and his three servants were away before making his move."
    "Then he came face to face with the fourth zombie and cursed. It let out a loud whining groan just before Rowan was able to separate the head from its body. Too late, the others had been alerted."
    "Bones started erupting from the ground, cutting off Rowan's escape path. He turned to face his hunter and the remaining three zombies."

    #Willpower test, DC6 (roll a d20, then deduct one for every ten points of corruption)
    if dice(20) - avatar.corruption >= 6:
        #Willpower test: Success.
        "Dark magic slammed into Rowan, filling his body with weakness and his mind with fear.  He pushed those feelings back and dove into combat. Another zombie went down in a single strike, but the others proved tougher once the necromancer realized his magic had failed."
        "Instead of weakening his foe, the magic user shifted his efforts towards strengthening his minions. They grew stronger, tougher, and most importantly, faster."
        "After several moments of combat that was mostly a stalemate, Rowan managed to break past the two empowered undead and fled into the forest. The necromancer sent him a parting gift, a bolt of necrotic energy that took the hero square in the back."
        "He kept running through the pain, which was apparently good enough for his opponent as they did not pursue him out of the corrupted part of the forest.  Whoever that was, they didn't seem to want anything to do with the outside world."
        #End scene.  Rowan is injured, 10 exp.
        $ add_exp(10)
        $ add_effect(Injury('Necrotic energy', 'strength', -2))
        return
    else:
        #Willpower test: Failure.
        "An incredible wave of primal fear filled Rowan, sending him into a frenzy to flee. However, at the same time his body seemed to have grown weaker and moved as if in a dream."
        "The zombies soon closed in on him and too late he realized the magical influences that had gripped him. Only after taking a few bruises was he finally able to free himself of the necromancer's magic, only for the magic user to switch to a more direct method of attack."
        "A bolt of necromantic energy struck the man, leaving him almost helpless before the undead onslaught. Sensing that any hope of surviving this confrontation was quickly fading, Rowan grabbed his amulet and begged to be brought back to Bloodmeen."
        "He soon lost consciousness, but was awoken by a purple face with mismatched eyes looking at him with disappointment. It seemed his adventuring for the week was done."
        #End scene.  Week instantly ends, tile remains unexplored, no exp.  Rowan is injured.
        $ add_effect(Injury('Necrotic energy', 'strength', -2))
        $ prevent_tile_exploration()
        jump end_map_exploration
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label forest_s_blessing:
#Forest's blessing (benediction)
#No requirements.

#Show forest background.
scene bg forest1

"A playful giggle could be heard in the air. It sounded both friendly and mischievous, which suggested that a forest spirit had taken an interest in Rowan's presence. He knew how this went."
"For the next few hours, a couple pranks were made and a game was played. The hero went along, knowing that as long as he did so the event would only last a short time. If he didn't, it was possible he might make an enemy he didn't need to make."
"Even with that being the case, he had to admit that playing with a pure spirit like this was fun."
"At the end, the creature showed itself. The pixie appeared to be a small man, about the size of his hand. The two held one another's gaze for sometime."

#Test corruption: Low/pure.
if avatar.corruption < 31:
    "Finally the spirit smiled and put his hand on Rowan's nose.  There was a small flash of light, then the tiny figure darted back into the woods with a laugh. A wry smile followed that departure, which became a more genuine one when the realization came that a blessing had been left."
    #End scene. 10xp  Rowan is blessed with better stats for three weeks.
    $ add_exp(10)
    $ add_effect(MultiEffect("Forest's blessing", 'pos', (('strength', 1), ('reflexes', 1), ('vitality', 1), ('intelligence', 1), ('luck', 1),), 3))
    return
#Test corruption: Medium.
elif avatar.corruption < 61:
    "A small frown creased the spirit's face. There was something it saw in Rowan that it didn't like. Still, it buzzed around him for a moment and a small warmth filled the man. Then it took off into the trees."
    #End scene.  10xp Rowan is blessed with better stats for two weeks.
    $ add_exp(10)
    $ add_effect(MultiEffect("Forest's blessing", 'pos', (('strength', 1), ('reflexes', 1), ('vitality', 1), ('intelligence', 1), ('luck', 1),), 2))
    return
#Test corruption: High.
else:
    "Suddenly the spirit recoiled in horror, then flew away at top speed. It vanished into the trees in an instant, leaving behind a surprised Rowan. That wasn't how fae had reacted to him before."
    #End scene. 5xp
    $ add_exp(5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_trapped_dryad:
#The Trapped Dryad

$ released_block_rollback()
scene bg3 with fade
show rowan necklace neutral behind bg3

$ dryadName = "Dryad"

"For a change, Rowan’s passage through the forest had afforded him a pleasant surprise, instead of the usual brush with danger."
"In the glade before him he could see a vision in green and brown; a pair of long legs, covered in bark and leaves, rose into a pert, round ass."
"The woman, obviously a forest spirit, was bent forward from the waist, almost horizontally, and over her back was splayed hair coloured with all the hues of autumn."
"She wriggled and squirmed, but was, rather ironically it seemed to him, rooted in place, as if held there by something."
"As Rowan was admiring the view, a voice smooth like silk rang out through the glade."

dry "Hello? Is somebody there?"
dry "I’ve been trapped here for hours, please…. Please help me..."

menu:
    "Try to free her.":
        $ released_fix_rollback()
        ro "Hang on, I’m coming."
        "Rowan hurried over to the woman in peril."
        "When he reached the far side of the glade, he discovered two things; the first was that she was just as stunning from the front as she had been the back, and the other was that the thing holding her in place was a rather elaborate looking trap."
        dry "Thank you so much. I can’t move my hands."
        ro "Let me take a look and see what I can do. I’m Rowan by the way."
        $ dryadName = "Phoebe"
        dry "Phoebe."
        ro "Nice to meet you Phoebe. We’ll have you out of here in no time."
        "The dryad flashed him a nervous smile, and the hero began to examine the trap beneath her. In her hand, she had grasped something, but what it was he could not tell inside her small fist."
        "He could only assume it had been some sort of bait, because directly beneath her hands was a metal plate. Attached to it was a metal ring, that must have sprung when she took whatever was on the in, ensnaring her hands."
        ro "I take it there was something on this plate?"
        "She nodded and opened her fist to reveal a small, brilliant red gemstone. A strange thing to use as bait Rowan though, but it had seemed to work in this case."
        "Trying the obvious solution, he reapplied pressure to the plate but it was no use; the trap must have been loaded with a spring or some similar mechanism, as putting pressure back on it loosened the ring encasing her hands in no way."
        "Looking closer, he saw there was a small keyhole on the underside of the ring. This made sense as whoever had set the trap would at some point have to undo it. Taking a small knife from his boot, he began to attempt to pick it open."

        # Open Lock DC15
        #pass
        if check_skill(15, 'open_lock')[0]:
            "After a few minutes of poking around inside the ring, Rowan heard the final click of the mechanism, and the lock popped open. Now free, the dryad stood and surprised the man with a tight embrace."
            dry "Thank you- Thank you so much! You don’t what it is like for one of the fey to feel trapped…"
            ro "It is no problem, just glad I could help."
            dry "Please, take this-"
            "She handed him the red stone; it was of little use to him as it was, but he was sure he could probably get a tidy sum for it if he were to sell it."
            dry "-and I’ll  tell the others of you, so you should be more safe from them in the future."
            "They chatted for awhile, and then exchanged pleasant goodbyes. Rowan headed off on his way, and when he glanced back, the spirit had become unrecognizable from the rest of the trees that were now behind him."
            #gain 20xp, 50 gold, and favour with the fey
            $ add_exp(20)
            $ change_treasury(50)
            $ change_favor('fey', 1)
            return
        #fail
        else:
            "Rowan tried for an hour, but the task was beyond his skill. He twisted and turned the point of the knife, but it never seemed to find the catch to release the ring’s lock."
            "Eventually he realized that he could do this all day and never get anywhere, and as much as he hated to leave the poor dryad, he had his own tasks he had to complete."
            "To her credit, Phoebe was very understanding of his situation, but he still felt the sting of guilt as he left her behind, fearing she’d be helpless when whoever had laid the trap returned to find her in it."
            #gain 5 xp, lose 1 move point, gain guilt
            $ add_exp(5)
            $ change_mp(-1)
            $ change_base_stat('g', 2)
            return
    "Take advantage of her." if avatar.corruption > 30:
        $ released_fix_rollback()
        #should probably require a certain level of corruption (TO DO)
        "Without saying a word, Rowan sidled up behind the beautiful creature, placing his hands on her svelte sides."
        dry "Hey, what in the six hells are you doing?"
        "Ignoring her question, he ran his hands down to her tight little ass. Putting his feet on the inside on hers, he used his lower body strength to force her legs apart."
        "She struggled against him to try and keep them closed, but her unsteady position gave little in the way of purchase, and she was easily overpowered."
        dry "I mean it, you better stop it or- or- else!"
        "He was not concerned with the dryad’s idle threats now, as he had created the access that he wanted. Moving one of his hands down from her behind and slid a single finger into her surprisingly tight brown pussy and began to stroke her walls with a come hither movement."
        dry "You won't get away with this, human!"
        "A sharp intake of breath, followed by a small cry signalled that the hero had found what he was looking for. Sliding another finger inside, he doubled his assault, frigging her with increasing speed."
        "Her resistance almost melted away, replaced by steady panting and quiet moans. Before long Rowan’s fingers were slick with her sticky fluids. The slut was ready for his cock."
        "Freeing it from his trousers, he ran his hand over it to coat it with her pussy juices. Teasingly he rubbed it against her opening, threatening to enter her, but stopping short each time."
        dry "You- you bastard! I’ll-"
        scene cg141 with fade
        pause 3
        "She didn't finish her sentence, as Rowan slid his cock deep inside her, causing her to let out a low moan. Wasting no time, he grabbed her by the hips and began to fuck her roughly."
        "As the fey are sexual creatures by nature, whatever feelings the dryad had about her current predicament were cast away as she lost herself in the pleasure of the act. She used whatever leverage she could get from her current position to buck back against him."
        "Reaching forward, Rowan roughly grabbed and squeezed a tit; small, almost boyish, but firm and perky. The surprise caused the dryad to tighten her cunt, squeezing his dick in a way that was almost unbearable."
        scene cg141 with sshake
        scene cg141 with sshake
        scene cg142 with flash
        pause 3
        "He felt her shudder as she came, her cries so loud that they rang out through the otherwise silent forest. The sensation was too much for him, and he came hard and deep within her."
        "He pulled his dick free of her, he shot a few more ropey lengths of jizz into the air, before untangling the two of them, tucking his member back in his pants as cum oozed from her well used cunt."
        dry "The least you could now is free me, asshole."
        "Rowan chuckled as he walked away, leaving the dryad indisposed. Curses rang out after him in a language he could not understand, but before long the forest had regained its usual uneasy quiet."
        #gain corruption, gain guilt, lose luck for 3 weeks, lose favour with the fey
        $ change_base_stat('c', 2)
        $ change_base_stat('g', 2)
        $ add_effect(MultiEffect("Cursed", 'pos', (('luck', 3),), 3))
        $ change_favor('fey', -1)
        return
    "Leave.":
        $ released_fix_rollback()
        "Rowan had heard a lot of stories about the fey, and they usually ended with some poor person being tricked in some way, or charmed."
        "The forest spirit could be in genuine need of help, but he decided it best to err on the side of caution, leaving the dryad for somebody else to deal with."
        return

