init python:

    event('breeding_orientation', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), group='alexia_breeding', run_count=1, priority=pr_story)
    #generic event #1
    #repeatable
    #These events play if no other event fires.
    event('alexia_breeding_generic1', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), group='alexia_breeding', priority=pr_npc_fallback)
    #Frisky drider
    #Requires at least one drider in the breeding pits.
    event('frisky_drider', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", "castle.buildings['pit'].driders >= 1"), run_count=1, group='alexia_breeding', priority=pr_npc)
    #Egg smuggling
    #Requires some positive monster recruitment rate.
    event('egg_smuggling', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", "castle.buildings['pit'].drider_recruitment >= 0.5"),
        run_count=1, group='alexia_breeding', priority=pr_npc)
    #Life as a dark elf man
    event('life_as_a_dark_elf_man', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), run_count=1, group='alexia_breeding', priority=pr_npc)
    #Cleaning cages
    #Req: Have at least one monster.
    event('cleaning_cages', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", "castle.buildings['pit'].driders >= 1"), run_count=1, group='alexia_breeding', priority=pr_npc)
    #Drider eggs and young
    #Must have greater than 0 drider recruitment rate and at least 1 open space for driders
    event('drider_eggs_and_young', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='breeding'", "castle.buildings['pit'].free_space >= 1", "castle.buildings['pit'].drider_recruitment > 0"),
        run_count=1, group='alexia_breeding', priority=pr_npc)
    #Grooming a drider
    #Requires a drider be in the pits and at least two other monsters.
    event('grooming_a_drider', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", "castle.buildings['pit'].driders >= 3"),
        run_count=1, group='alexia_breeding', priority=pr_npc)


label breeding_orientation:
#Orientation
#Event happens the first time Alexia works in the Breeding Pits.

scene bg25 with fade
show draith neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

al "Good morning Mr. Draith. I'm here to help in any way I can with your monsters."

"The dark elf recoiled from her for a moment, then stepped back forward with a somewhat defiant look in his eyes."

dra "Eh, like what... uh, housewife?!"

show alexia 2 necklace concerned at midleft with dissolve

al "(Did I say something wrong?)"

show alexia 2 necklace neutral at midleft with dissolve

al "Well, I'm not sure. I'm good at cooking and cleaning, but I'm not sure if that's something you need."

dra "Actually, that would be really useful.  As handy as these strong orcs are for dealing with unruly monsters, it's almost impossible to get them to muck out a cage or measure food correctly."

show alexia 2 necklace concerned at midleft with dissolve

al "Uh, 'muck'?"

dra "Yeah, you'll want to lose that nice dress. This is a dirty job. Wonder if I've got some overalls in your size? This place really could use a good scrub down."

"Alexia's stomach churned at the thought. There was an off smell about the place already, like a barn from the Outer Dark, now she was going to be put into the thick of it?"
"Then again, a barn from the Outer Dark was more or less what the breeding pits were. This was more or less what she should have expected from the start."
"Well, it wasn't the first time she'd gotten her hands dirty."

scene alexia_pits_1 with fade

"Working in the pits was back breaking hard work. Alexia spent most of it cleaning dirty cages, filling feeding troughs, and changing water for the monsters."
"What this place had for handlers were happy enough to move the monsters around, but Draith had been right about them skirting other jobs. The dark elf himself was the other one mainly helping her with the day to day maintenance."
"By the end of the week, he'd grown much more comfortable with Alexia's presence, though he still hesitated whenever giving directions or orders to her."

scene bg25 with fade
show draith neutral at midright with dissolve
show alexia breeding neutral at midleft with dissolve

dra "Well Alexia, I'd say that this place is significantly more livable now. As long as you stick around, I can comfortably care for more monsters around her.  Thanks a lot for your help."

show alexia breeding happy at midleft with dissolve

"Alexia forced a smile."

al "You're quite welcome Draith."

al "(Hopefully Rowan doesn't need me in here too long.  Solansia please let me wash the smell out when I can finally leave this place behind.)"
$ do_job_breeding('alexia')
return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label alexia_breeding_generic1:
#generic event #1
#repeatable
#These events play if no other event fires.

scene alexia_pits_1 with fade

"This week Alexia spent time in the breeding pits assisting Draith as a monster handler. Going through a routine not entirely unlike a farmhand for livestock. She filled feeding buckets, changed water, checked on the monsters, and cleaned out the cages."
"By far her least liked thing was to clean the cages, with the smell of manure, mold, and the monsters themselves constantly filling the air. It wasn't dangerous or difficult, just very dirty and exhausting."
"At least checking on the eggs and the young they were bringing up was somewhat endearing. They might be monsters, but that didn't stop the little ones from looking cute in their own way."
"Her ongoing help allowed the pits to support more and larger monsters at once."
$ do_job_breeding('alexia')
return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label frisky_drider:
#Frisky drider
#Requires at least one drider in the breeding pits.
$ friskyDrider = True
scene bg25 with fade

"Alexia had a moment of peace while the orc handlers were pulling one of the driders out of its cage. It was a powerfully built male creature that was straining against the chains and prods that kept it from rampaging around the pits."
"One of the orcs, a muscular woman with an arrogant look about her, seemed to be taking a particular sadistic pleasure in tormenting the beast."
"That was nothing new, Draith hadn't managed to get the orcs to be gentle, but this girl was being especially aggressive at rilling the drider up."
"She frowned, that didn't look like the right way to hold that-"

#escaping drider cg
scene black with fade

"Suddenly he managed to slip his spinner free and spray the orcs behind him! They dropped their leashes in surprise and in moments the chains were off of his legs and he leapt forward."
"His tormenter barely had time to realize what had happened before it landed on top of her and pinned the orc woman to the floor underneath his body. She yelped in shock, then growled as she tried to force the beast off of her."
"Those efforts soon proved futile as the drider pinned her arms under his legs and then used his human ones to pull the lower parts of her armor free and expose her sex underneath."
"Even if Alexia hadn't become familiar with drider libido, the look on his face told her exactly what was happening next."

menu:
    "Watch.":
        $ renpy.fix_rollback()
        jump orcDriderScene

    "Leave.":
        $ renpy.fix_rollback()
        "This wasn't something Alexia needed to see. She couldn't do anything to help recapture him anyway."
        "Luckily, he'd calmed down enough by the time he'd finished raping the orc woman that he was easily recaptured and Alexia was able to return to her work."
        return

label orcDriderScene:

scene cg131 with fade
pause 3

"There was a strange sense of fascination to Alexia as she watched the scene unfold. She couldn't exactly do anything about what was happening, that wasn't her job either."
"Instead she simply watched events unfold, watched the drider man seem to gloat down at his victim for a few seconds and savoring having her at his mercy.  Or maybe he was just waiting for his shaft, which was resting on her belly, to reach full hardness."

scene cg132 with fade
pause 3

"A moment later the drider grinned and started chittering happily as he forced his cock into the orc woman's pussy. For her part, the woman continued to struggle against his grip while making frustrated noises that were now twinged with gasps."
"The other handlers started picking themselves up off the ground and clearing the webbing from their eyes. When they saw what was happening, some laughed, some scrambled to get new chains, and one even took out his dick and started masturbating to the scene!"
"Ignoring all of them, the drider settled into a steady rhythm of slowly sliding out of the orc, but then slamming his dick home hard, out, then bam, out, then bam.  Each thrust was accompanied by a smacking sound of chitten hitting flesh and a gasp of pleasure from the victim."
"Well, victim was maybe a bit generous. The woman had almost brought this on herself, had she been paying more attention to holding the guide chains properly instead of tormenting her charge, maybe she wouldn't be pinned under him being ravaged."
"A few moments later, the beast slammed his chameric hips forward one last time, then held himself there as he emptied his twisted seed into an orcish womb. Alexia was surprised to notice that the woman had stopped struggling now, was she resigned or actually enjoying it?"

scene cg132 with sshake
scene cg132 with sshake
scene cg133 with flash
pause 3

"As he pulled back from her well used sex, a trail of his seed stuck to his shaft. A small pool also started forming as it oozed out of the hole underneath."
"The orc handlers who'd actually done their job took this moment to quickly feed chains around the beast and rebind him. He didn't have a chance and the remaining slackers quickly jumped in to do their part."

scene bg25 with fade

"They lead the drider away, towards the cleaning area for Draith to brush him down. They also left the orc woman who'd been violated laying on the ground, panting and cursing the drider for humiliating her and herself for enjoying it."

#alexia gains a small amount of corruption
$ change_corruption_actor('alexia', 2)
$ do_job_breeding('alexia')
return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label egg_smuggling:
#Egg smuggling
#Requires some positive monster recruitment rate.

scene alexia_pits_1 with fade

"While she was working, Alexia noticed something odd about the monster eggs. If she wasn't mistaken, some were missing. Worried that something might have gone wrong, she went looking for Draith."

scene bg25 with fade
show draith neutral at midright with dissolve
show alexia breeding neutral at midleft with moveinleft

al "Ah, there you are Draith."

"As was his way, the dark elf recoiled a moment in instinctive fear at the sight of Alexia. Then a moment later he relaxed and gave a friendly greeting."

dra "Hello Alexia, how can I help you?"

show alexia breeding concerned at midleft with dissolve

"She hesitated a moment, unsure how to broach the subject of his beloved monster eggs."

al "I was looking at the eggs and it looks like we're missing some.  Did you move them somewhere?"

"Now it was the dark elf's turn to look unsettled. Instead of answering right away, he went into a revery that Alexia had sometimes seen him do before. It usually meant he was thinking. When he'd finished, he waved Alexia to follow him."

dra "Let's take this somewhere a little more private."

hide alexia with moveoutleft
hide draith with moveoutleft

scene bg8 with fade
show draith neutral at midright with moveinleft
show alexia breeding concerned at midleft with moveinleft

"He led her to a secluded part of the tunnel network then checked to make sure the two were alone. At this point Alexia was starting to feel nervous and unsure about what the dark elf intended."

dra "The eggs aren't missing... I've set them aside for someone who's expressed a bit of an interest in having them for their own menagerie. I am, acquiring certain items using the funds that will give me."

show alexia breeding shocked at midleft with dissolve

dra "I wasn't intending to let you know, but I'll give you some of the money if you keep quiet. I'll even give you double if you lend a hand."

al "I take it the twins won't be too happy about this?"

dra "No, that's why I can't let them find out why their armies aren't getting as big as they should be for the next few weeks. So, can you help me? If you say no, I'll put the eggs back and we'll forget this ever happened."

$ do_job_breeding('alexia')

menu:
    "No deal.":
        $ renpy.fix_rollback()
        show alexia breeding neutral at midleft with dissolve
        al "I don't want any part of this, and I don't think this is the best use of your time either Draith. Can't you save up some money for what you want instead?"
        dra "Uh, that might take a year at this rate. Well, maybe things will get better. We'll forget this ever happened. I'll see you back in the pits, Alexia."
        hide draith with moveoutright
        scene black with fade
        "True to his word, the eggs were back when Alexia returned to her duties."
        return

    "I'll keep quiet.":
        $ renpy.fix_rollback()
        show alexia breeding neutral at midleft with dissolve
        al "Fine, I won't speak a word of this to the twins."
        dra "Okay, okay.  I'll get the money to you by tomorrow. We won't talk about this again."
        hide draith with moveoutright
        scene black with fade
        "True to his word, Alexia found a fair sum of money placed in her work apron at the start of the next day. She passed it on to Rowan, as he'd have a better use for it than her."
        #rowan gains 25 personal gold.
        #monster recruitment is reduced for next three weeks
        # TODO: recruitment reduction
        $ change_personal_gold(25)
        return

    "I'll help you.":
        $ renpy.fix_rollback()
        show alexia breeding happy at midleft with dissolve
        al "I wouldn't mind going behind the twins a little bit. I can help you."
        show draith happy at midright with dissolve
        dra "Great!  Okay, at the end of the day, I'll get you to carry up an egg to the goblin caravan and pass it on to Cla-Bow. Between the two of us, we should be able to get even more eggs to them, and more money for us."
        hide draith with moveoutright
        scene black with fade
        "Over the rest of the week, Alexia smuggled eggs out of the castle on Draith's behalf, earning some extra money for her and Rowan."
        #rowan gains 50 personal gold.
        $ change_personal_gold(25)
        #monster recruitment is reduced for next three weeks
        # TODO:
        #Alexia loses a little influence from Andras and Jezera for her little rebellion.
        $ change_actor_num_flag('alexia', 'andras_influence', -1)
        $ change_actor_num_flag('alexia', 'jezera_influence', -1)
        return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label life_as_a_dark_elf_man:
#Life as a dark elf man
#No requirements.

scene bg25 with fade
show draith neutral at midright with dissolve
show alexia breeding neutral at midleft with dissolve

al "Good morning Draith."

#draith scared

"The dark elf jumped slightly at the sound of her voice, but seemed to relax when he saw who it was."

#draith neutral
dra "Oh, uh, good morning Alexia."

"Even after that he still seemed a bit jittery and took an unconscious step away from his assistant."

al "Why are you always so nervous whenever I see you? As frightening as these... creatures are, you seem the most at ease with them."

#draith look away
dra "I... don't like women."

show alexia breeding shocked at midleft with dissolve

#draith embarassed
dra "Meaning no offense ma'am, you don't deserve how I treat you. You're nothing like my mistress and her peers from the cavernhomes, you are a decent sort."

show alexia breeding concerned at midleft with dissolve

al "You mean, your people? Dark elves?"

#draith neutral
dra "Yes. A male is property, he has no protection to his person. Should a dark elf wish to harm her male for any reason, that is her right."

"He traced a faint scar on his face, then wrung his hands which had similar markings all over them."

dra "All my life I've been fearing for my life at the hands of vindictive elves. Even when I see a human, my instinct is to get away or appease."

show draith happy at midright with dissolve

"Suddenly a smile broke on his face and he seemed like he was distracted."

dra "When I cared for a monster, I always knew what would happen. I knew how they responded to treats or touches. If one trusted you, they'd never suddenly hurt you because of their mood. In some ways, other males are the same."

al "Other males? As in, they wouldn't hurt you and you could make friends with them?"

dra "Friends, sharing plans and discussing experiments, but also sometimes..."

show draith neutral at midright with dissolve

"The distant smile faded and he started shaking again."

al "What? What's bothering you?"

dra "I'm sorry, but mistress doesn't like it when I... when I..."

"Alexia started to reach out to comfort the man, but thought better of it when he recoiled from her touch. Instead she tried to reason away his fear."

al "Your mistress can't hurt you here. You're free from her."

show draith happy at midright with dissolve

dra "That's right!"

"Abruptly he leapt up into the air and started shouting loudly through the halls."

show alexia breeding shocked at midleft with dissolve

dra " I'm free of you, Amethis! You can't touch me here in Bloodmeen! I can fuck males as much as I want!"

"That... certainly wasn't what Alexia was expecting to hear from him. She was at a loss for words as to how to respond to him."

show draith neutral at midright with dissolve

"However, Draith was now distracted by the uproad his outburst had caused in the cages down the hall."

hide draith with moveoutright

"Looking somewhat self conscious, the dark elf ran down the hall looking to comfort them."

show draith neutral behind bg25

dra "Hey, hey, it's okay. Daddy is sorry he shouted."

$ do_job_breeding('alexia')
return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label cleaning_cages:
#Cleaning cages
#Req: Have at least one monster.

scene alexia_pits_1 with fade

"Alexia arrived in the breeding pits. She pulled her overalls on over her plain dress, grimacing at the smell. Then wrapped up her hair, suppressing a gag at the slime.  And pulled on the leather work gloves and boots, desperately trying not to think about what they were doing to her skin."
"Then she looked at the schedule. The woman knew well enough what she was going to be doing today, checking was on the hope that maybe she'd been assigned to something else."
"There had been no change."
"Heaving a sigh, Alexia got her mop, filled a bucket, and went to the first stall of the day."
"Cleaning monster cages was a long and arduous process. Not only was there the dust and filth that normally accumulated, but also whatever the occupant left behind of their food and any other things their bodies might make."
"On top of all that, it was time consuming to scrub everything off and then wash it out of the cage. That wasn't it either, she also had to relay any bedding or food that the occupant needed before it could be moved back in, or whoever would be the new occupant."
"By the time she'd finished the first stall of the day, it was already getting close to noon.  With two others still to do, this was going to be a long, long day."
"Cooking and cleaning had been things she'd loved to do back home, but here... she just couldn't get her heart into it. There was no personal touches to make, no new styles to test  Everything was impersonal and efficiency was above everything else in importance."
"..."
"Hours later, she finally finished the last one and leaned against the wall for several minutes as the cage's occupant was moved back in. The beast didn't seem to much care about the effort she'd just put into fixing its mess and promptly dumped a bunch of fresh food on the floor."
"Alexia just groaned, then stomped off back towards the changing room. She threw off the gloves, overalls, and scarf with their fresh filth and headed back up to her room. All she wanted was a bath without end that would cleanse her of all that grim, sweat, and dirt."

scene black with fade

"She already knew from the last two days that wouldn't work, and she still had three more days of cleaning cages ahead of her."

#alexia gains stress
$ do_job_breeding('alexia')
$ change_actor_stress('alexia', 5)
return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label drider_eggs_and_young:
#Drider eggs and young
#Must have greater than 0 drider recruitment rate and at least 1 open space for driders

scene bg25 with fade
show draith neutral at midright with moveinleft
show alexia breeding neutral at midleft with moveinleft

al "So this is a drider egg?"

dra "That's right."

"Alexia looked back at the thing. It was about the size of her head, a big yellowish ball of jelly, sitting on a bed of straw. As she got closer, she felt a wave of heat from underneath."

al "Those look like heated rocks? I've heard that lords sometimes use those to warm their beds during winter."

dra "More or less. Drider eggs can survive cold weather, but they won't hatch without heat. So I make sure they're always toasty while mixing in the growth hormones. That's this."

"The dark elf moved to the side and opened up a cabinet to reveal a jar of some murky fluid."

dra " The main thing you need to do is keep changing the rocks to maintain temperature, keep the eggs from drying out, and apply this a couple of times over the course of a week. They grow pretty fast and hatch in about half a month from laying if you keep that up."
dra "Of course, we usually don't take the freshly laid eggs. The less time we're waiting for them to hatch, the sooner we can boost them into fearsome monsters."

hide alexia with moveoutleft
hide draith with moveoutleft

scene bg25 with fade
show draith neutral at midright with moveinleft
show alexia breeding neutral at midleft with moveinleft

"Now Draith lead the woman over to a nearby pen that had two drider young in it, who were happily leaping around and shooting web at each other in some sort of game. Chittering that almost sounded like laughter could occasionally be heard."

al "Wow, they actually look kinda cute."

dra "Eh, to each their own. Just don't underestimate them, they may be small but they've got their poison from the day they're born."

"He grabbed a hunk of meat from nearby, then glazed it in some kind of dust before casually dumping it inside the pen. At once, the two drider young ceased their game and leapt on top of the meat."

al "Ugh."

"They tore into the flesh and sinew with vigor, ripping off big chunks and then swallowing them whole. Alexia's vision of playful children was brutally replaced with that of ravenous animals with no restraint or morals."

dra "We keep this area warm too, so they've got lots of energy and a big appetite. That way they grow faster. It still takes time, but with the gift of chaos..."

"He indicated the dust."

dra "... they'll be grown up in no time.  Once a day is good enough. You won't need to worry about getting the meat, my handlers are competent at that much. If you want to slip some scraps to a favorite, that's fine. Just don't feed them anything but meat and don't overfeed."

"With only bones left of their meal, the two driders returned to their game of chase and trying to hit one another with their webbing."

dra "They really can't stop themselves from eating as much they can while on gift of chaos, so be very careful about giving them too much. Oh, and mind your arms, they'll snap at them too if you give them the chance."

al " (How can monsters be so scary and so adorable at the same time?)"

$ do_job_breeding('alexia')
return


#########################################################################################################
#########################################################################################################
#########################################################################################################


label grooming_a_drider:
#Grooming a drider
#Requires a drider be in the pits and at least two other monsters.

scene alexia_pits_1 with fade

"This week Alexia was going to be giving the monsters a brushing and cleaning. Draith usually wanted to do this himself, but he was indisposed with something else."
"The first one on the agenda was a male drider. Already he'd been brought out of his cage and fastened to a set of shackles to keep him from causing trouble, but his tugging and chittering remained deeply worrying for Alexia."
"Thankfully for the woman, once she'd started running her wet brush over his black carapace covered abdomen, the drider abruptly seemed to calm down. The angry chitters were replaced by gentle breathing and a soft tick that had to be a sign of contentment."
"This had to be the calmest Alexia had ever seen a drider while awake.  There was no aroused frenzy or struggle against their captors. Even when in their cages and not doing anything, a drider always looked like it was ready to spring like a hunter if it sensed weakness."
"Here, all the boy wanted to do was enjoy the sensation of those moist bristles run over his exoskeleton and get all the grime out of them. He even started to buck back slightly against her to increase the force of the brush, like a cat would."
"Much to her surprise, Alexia found herself cooing and gently talking to the drider while she brushed him.  The woman had never been too interested in animals before, but she understood why one would like them and why this seemed to be Draith's favorite thing to do."
"He was very polite the whole time, never even exposing himself to her while she brushed him.  Just being washed and groomed was enough. Well, as long as Alexia didn't touch the sensitive hairs on his legs."
"After finishing with the first drider, she called in the handlers to take him back to his cage.  They had significantly less trouble there than when they'd first brought him out."
"Alexia looked at her schedule as the next monster was brought into the room and chained up, then rolled her shoulders that were already feeling stiff and sore."
"A sigh escaped her lips. This was going to be a long and tiring day, in spite of how much more enjoyable the task might be than her usual duties."

#lose a little stress
$ do_job_breeding('alexia')
$ change_actor_stress('alexia', -5)
return
