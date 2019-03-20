init python:

    #Alexia Locked in the Dungeon
    #If Rowan tells the twins Alexia helped Helayna escape AND NTR is on, these events happen as an extra event after the ruler event for the corresponding week
    #If NTR is turned off, Alexia is simply unavailable for the next four weeks, and should gain a large amount of stress as a result
    event('alexia_locked_in_the_dungeon', triggers="week_end", conditions=('alexia_away_weeks > 0', 'NTR'), run_count=1, priority=pr_ruler)
    #week 2
    #triggers the second week after Rowan tells on Alexia if NTR is on
    event('alexia_dungeon_second_week', triggers="week_end", conditions=('alexia_away_weeks > 0', 'NTR'), depends=('alexia_locked_in_the_dungeon',), run_count=1, priority=pr_ruler)
    #week 3
    event('alexia_dungeon_week_3', triggers="week_end", conditions=('alexia_away_weeks > 0', 'NTR'), depends=('alexia_dungeon_second_week',), run_count=1, priority=pr_ruler)
    #week 4
    event('alexia_dungeon_week_4', triggers="week_end", conditions=('alexia_away_weeks > 0', 'NTR'), depends=('alexia_dungeon_week_3',), run_count=1, priority=pr_ruler)
    # if not NTR, Alexia will just get stress in silent event
    event('alexia_locked_in_the_dungeon_not_NTR', triggers="week_end", conditions=('alexia_away_weeks > 0', 'not NTR'), run_count=1, priority=pr_ruler)

label alexia_locked_in_the_dungeon:
#Alexia Locked in the Dungeon
#If Rowan tells the twins Alexia helped Helayna escape AND NTR is on, these events happen as an extra event after the ruler event for the corresponding week
#If NTR is turned off, Alexia is simply unavailable for the next four weeks, and should gain a large amount of stress as a result

#Week One
scene black with fade

"After her role in Helayna’s escape had been revealed, two burly orc soldiers took her away, and left her in one of the castle’s dank, dark cells. A few days had passed, and, aside from the meals that appeared routinely like clockwork, she had seen no sign of any other living person."
"If there were anybody else down here in the dungeons with her, she had not heard them, and no one had replied to her cried out. No, she was alone, truly alone. Even her own husband had betrayed her."
"She had done the right thing, she knew that. Even in her current position, she had no doubt. It was bad enough that she had been entrapped by the demons and forced to be a hostage, she was not about to let it happen to another poor woman. Helayna did not deserve that."
"But, doubt aside, she was filled with a lot of other emotions. First, anger at her husband for revealing her part in the escape. She thought he would understand, hells, the man she married would have freed the poor girl himself."
"Then sadness at the realization that his time at the castle was changing Rowan and not for the better. Was this the man he was now? Who would allow the twins to use their dark magic to control Helayna? To betray all her ideals as a knight?"
"Lastly, despair. There was no way for her to get out of this jail cell, she knew that, otherwise Rowan would have managed it. She had no idea how long her captors intended to keep her down here. For all she knew they might leave her to rot, all alone in the dark."
"Time passed. She had no idea of knowing how long, as it seemed to stretch and cortort due to the solitary nature of her imprisonment. Eventually, the door opened…"

scene bg8 with fade
show alexia 2 necklace concerned at midright with dissolve

"In the doorway stood one of her captors, smiling. In his large hands, he held a small, ornate wooden box, etched with strange symbols she did not recognize. Some sort of runes, perhaps?"

show andras happy at edgeleft with moveinleft

al "What the hells do you want?"

an "That’s no way to speak to a visitor is it? Especially one who has come all the way down here to make sure you were alright."
an "I would have come sooner, but I have been very busy, I’m sure you can understand."

al "Alright? You locked me in a dungeon and left me to rot!"

an "Oh, don’t be so dramatic. What did you expect us to do? You did defy us after all, and we can’t look weak in front of everybody. We are demons, after all."

al "Well, I don’t regret it, so if you think I am going to admit some sort of wrongdoing, you’ll be waiting a long time. It wasn’t right what you two were doing to that poor girl."
al "So go ahead, do your worst, but if I had the choice I would do it again. Nothing you can do to me will change that."

an "I’m not going to harm you, you silly girl. As I have told you before, I will never lay a hand on you without your permission."

al "You’ll be waiting a long time for that, as well, as in, never."

an "We shall see. In the meantime, I just wanted to make sure you are not too uncomfortable. It is unfortunate, but I am afraid you’ll have to spend some time down here, to make it look like you are being properly punished for your disloyalty."

al "How long?"

an "A month should suffice, then you can return to your normal life."

al "A month..."

an "Oh come now, it is not that long. Our father would have executed you for far less, so you are getting off quite lightly. I’ll visit again, of course."
an "We can’t really allow you to have any other visitors though, this is supposed to be a punishment, after all."

al "…"

"The demon smiled, and tapped the wooden box he held in his hand."

an "Don’t be so down, I’m sure the time will fly by, and I have brought you a little present. Something to keep you occupied until you can go free."

al "And what exactly do you have in that box?"

an "Just something from my sister’s collection, I guess you could call it a pet. I just thought you could use something to keep you company, so you don’t feel so alone."

"He placed his hand on the box and the markings began to glow."

show bg8 with flash

an "That takes care of the pesky seal."

"With magic no longer sealing it, he simply slid open the wooden panel on the front to reveal what had been trapped inside."

scene cg158 with fade
show andras happy behind cg158
show alexia 2 necklace concerned behind cg158
pause 3

"Within the box was a round creature, the size of a small ball. It had neither skin nor fur, but seemed to Alexia to be more the consistency of putty."
"She had no idea what the thing could be, but the tiny eyes and mouth were adorable, and when it saw her, it suddenly became very excited."

al "What is it?"

an "It is called a wulump. Don’t worry, it is harmless, the box was just to keep it safe. They have a tendency to grow rather large unless they are contained, which can lead to them becoming almost insatiable."

"He placed the box on the floor, and the creature happily moved in the direction of the redhead. It had no legs to speak of, so it just sort of slithered, like a snake. When it had almost reached her feet, she kneeled and picked it up and cradled it in the palms of her hands."

al "Well, whatever it is, it is certainly very cute."

"She used her thumb to pet the wulump, and it made a strange, alien noise of contentment. It was certainly enjoying the attention it was getting."

al "Poor thing, how long have you been cooped up in that box, all alone?"

"I know the feeling, she thought to herself, in that way, there was a shared kinship between the two, as different as they were."

an "You might want to be a little careful, or--"
an "Ah."


"The woman was surprised as a small tendril shot from the top of the creature, and headed straight for her nostril."

an "I suppose I should have mentioned earlier, wulumps feed on sexual energy. Their tendrils secrete a chemical that induces feels of lust and euphoria in their victims."

"She could feel it worm its way up through her nose, inside her, and the tendril now in her skull, and whatever it was doing to her brain was starting to make her feel weird. Hazy, but not in an unpleasant way."

an "Do not worry, you are perfectly safe. It won’t harm you, it will just use you to feed on, and there’s no long term effects, so no need to worry about that."

al "Mmmm…"

scene cg159 with fade
show andras happy behind cg159
show alexia 2 necklace aroused behind cg159
pause 3

"She held the creature up, so it was close to her face. Another appendage formed, no tendril this one, thicker, more like a tentacle. It moved in the direction of her mouth. She opened wide to allow entry."

an "Most of them were killed, of course, due to the nuisance they became. The more they feed, the larger they become, and in the past, it wasn’t uncommon for them to enslave entire villages if left unchecked."

"The demon continued to talk, but Alexia was past the point of listening. She was lazily tonguing the end of the tentacle, and gently sucking on the head that had formed on the end. All she was interested in at that moment was pleasuring the creature."

an "There probably aren’t too many of them left now, mostly hiding in caves I would think. My sister managed to find this one though, and has been very careful in containing it."

"Andras saw what she was doing, and let out a low chuckle."

an "I see you aren’t really interested. Oh well, I suppose I should leave you two to get acquainted as you’ll be spending a lot of time together. The effects will wear off by the way, well, until it needs to feed again anyway."

scene cg160 with fade
pause 3

"If the woman noticed that he was leaving, she did not make it apparent, she just continued doing what she had been doing since the wulump had messed with her head."
"She was lightly stroking the tentacle now with one of her hands, as she sucked on it as best she could. The creature had slid it inside her mouth, and now was now moving it back and forth at a slow, steady pace."
"Just the taste of the tentacle against her tongue sent shivers down the woman’s spine, she wanted nothing more than to love and please the small creature that it belonged to. She encouraged it to go deeper, craving the feeling down her throat."
"The creature obliged, sliding further into the mouth until the redhead was deepthroating its faux member. Alexia let out of muffled cry of pleasure as an orgasmic wave shot through her body."
"Trying not to gag, she took the tentacle as deep as she could, and held it a few seconds, before resuming moving, giving a deep, sloppy blowjob. Lost in the euphoria of the moment, she slid her hand from the tentacle slowly down her stomach to play with her clit."
"The wulump began to move faster now, pistoning in and out of her mouth. Alexia did her best to please the creature, running her tongue against the tentacle as she took it deep in her mouth again and again."
"She began to finger her cunt, first one and then a second, greedily thrusting in and out while curling upward to stroke her g-spot. Wave after wave of orgasm coursed through her body as she continued to touch herself while deepthroating the tentacle."

show cg160 with sshake
show cg160 with sshake
scene cg161 with flash
pause 2
show cg162 with dissolve
pause 3

"Just as she thought she was going to lose her mind from pleasure, the tentacle began to spew a black, viscous fluid from its tip. She hungrily swallowed all she could, but some escaped her mouth, dripping down onto her breasts."
"Spent, the creature withdrew from her, absorbing the phallic appendage back into its body. Feeling exhausted herself, Alexia woozily lay on the straw covering the floor, placing the wulump on her chest. It seemed slightly larger than when it had been in the box."

scene black with fade
"A warm feeling of contentment overtook the woman as she drifted into sleep..."

#alexia gains 3 corruption
$ change_corruption_actor('alexia', 3)
return


########################################################################################################################
########################################################################################################################
########################################################################################################################

label alexia_dungeon_second_week:
#week 2
#triggers the second week after Rowan tells on Alexia if NTR is on

scene black with fade

"A week had passed, but Alexia would not have known it had anyone been there to ask her. She had spent the time lost in a haze, with the wulump using her body as sustenance whenever it saw fit to do so."
"In that time it had grown, and no longer resembled a small ball; now it was more the size of a small domestic animal."
"She’d given up wearing clothes, it saved her having to take them off when the wulump wanted to feed, and despite the dampness, the dungeons were quite warm. "
"The only other person who could have seen her naked body was the orc guard who brought food three times a day, but her brain was too fogged by the beast’s pheromones for her to even notice, never mind feel actual shame."

scene bg8 with fade
show alexia necklace naked at midleft with dissolve
show jezera neutral at midright with moveinright
show andras displeased at edgeright with moveinright

an "Well, here we are sister, as you asked."

je "A deal is a deal after all."


"Jezera, as inquiring as ever had consented to allow Andras to use the wulump on the proviso she could study the results."
"In the wild they grew too large, too fast, but in the dungeons of Castle Bloodmeen, with only one person for the beast to feed on, it would be more like a controlled experiment."
"It also had the bonus effect of saving the poor girl from one of her brother’s more outlandish punishments, as she had feared he might go overboard, and the female demon still favoured the carrot over the stick."

je "It has grown since you last saw it?"

an "Yes, it was smaller when I took it from the box."

je "Interesting. Even with only one person to feed on, it has expanded by three hundred, perhaps even four hundred percent."
"She looked at the woman, who was still sat on the floor. She hadn’t even bothered to cover up her naked body, which was unlike Alexia."
"Like most human women, she had so much shame; a pity, the demoness mused as she had such a nice body. Perhaps when she had time, she could help her see the error of her current viewpoint."
"At this point in time she had other things to attend to though, so it would have to wait. It seemed as if the redhead had hardly even noticed that anybody else was there."

je "Alexia, darling?"

"The girl turned to look at her, breaking from her daydream for a moment."

al "Huhh?"

je "Interesting! Her pupils are dilated and she still seems under the effects of the wulump’s pheromones, despite the fact it is dormant."
je "This would suggest that prolonged exposure causes it to have a longer effect, and explains why the women never seemed to escape whenever I encountered these things in the wild."

an "If you say so, sister."

show jezera displeased at midright with dissolve

"The male demon was clearly bored, and it showed. This annoyed his sister, who was busy wondering why he had even bothered to come, when the wulump began to stir from its slumber."

show andras smirk at edgeright with dissolve

an "Look sis, someone is hungry."

je "You aren’t the only one who has noticed."

"Alexia had turned away from Jezera now to face the beast. She opened her legs almost instinctively, inviting it to feed on her once against."

je "It is almost as if it forms some kind of psychic bond with the women it feeds on."

an "Trust you to be focused on that sort of thing when the good part is about to start."

je "We can’t all be uneducated, muscle-brained louts like you, dear brother, or we would never get anywhere."

#CG 1 - The Wulump fucks Alexia
scene cg165 with fade
pause 3

"The twins continued to bicker, but Alexia paid no attention to any of it. She was far more interested in what was about to happen to her."
"The wulump was awake now, and was clearly only interested in one thing itself. From its body, a tentacle began to emerge. As it had grown larger, so too had its tentacles become more substantial, and the thickness sent a shudder down the spine of the waiting woman’s back."
"It slithered towards her slowly, and it felt like an eternity before it made contact with the lower part of her leg. When it touched her, pleasure shot through her whole body, causing her to emit a low loud moan."
"She couldn’t wait for the beast to be inside her. To feel it fuck her. To have it explode inside her. As it worked its way up her leg towards her sex, she began to play her her cunt, already sopping wet with anticipation."
"The twins looked on, both with different intentions. Jezera was cold, interested to see how her little experiment would play out, while Andras grinned like a naughty schoolboy, waiting for the show to begin."

scene cg167 with fade
pause 3

"When the tentacle finally reached Alexia’s soaked hole, the monster did not wait for an invitation, forcing itself inside, causing the woman to shriek with pure unadulterated bliss."
"The creature was hungry and the woman was its prey; there was no confusion as to who was the master here."
"The tentacle was thick, much thicker than a human phallus, and most women would have had trouble taking it. But, as the beast had grown, with each “feeding” it had stretched her cunt a little more, almost as if it were shaping her as it did."
"What would she be forced to take if it were to become fully grown?"
"She was moving against it now, moaning lewdly as the tentacle rhythmically penetrated her pussy. If she had been oblivious to the demonic visitors before, she was completely unaware of their presence now."
"She only cared about feeding her beloved wulump, and the pleasure the act gave her."

scene cg166 with fade
pause 3

"Suddenly, the creature withdrew from her, with the tentacle rising up toward her face. The woman smiled and began to tongue the head, as if french kissing a lover. The beast’s pheromones had mixed with her juices, sending waves of pleasure throughout her body."
"Jezera found the sight very interesting. She had assumed that the wulump merely fed on the women, but it seemed to be able to create a bond of affection with them too. She even smiled a little at the sight of the redhead lovingly kissing the monster’s appendage."

scene cg168 with fade
pause 3

"After a few minutes of foreplay, the tentacle found its way back down to her pussy, and started right where it had left off. It was moving fast and hard now, as Alexia shrieked in pleasure, bucking against it."
"She wrapped both her hands, wet from her own juices, around the tentacle to increase the friction as it moved back and forth, bringing her closer to climax with each pump."
"She’d clearly orgasmed multiple times, and Jezera wondered if eventually these women lose their minds because of all the pleasure. She couldn’t let it go that far with Alexia, but she could always find other subjects."
"The display was coming to its natural conclusion now. Alexia was moving harder and faster, chasing the final, highest peak, while the tentacle worked like a piston. She felt incredibly full by its thickness, and felt like she was going to go insane."

scene cg169 with sshake
scene cg169 with sshake
scene cg170 with flash
pause 3

"She let out a savage cry as the beast exploded inside her, the black viscous fluid it excreted dripping from her overstuffed cunt as it withdrew from her. She flopped down onto the straw beneath her completely spent."
"The wulump, now sated, once again drew back into itself. Dormant for now, but it would not be long before it was ready for its next meal."

scene bg8 with fade
show jezera happy at midright with dissolve
show andras smirk at edgeright with dissolve

je "All in all, a very interesting experience."

an "I’ll say."

je "I’ll allow it to continue for now, but I will be checking in from time to time. I don’t want it to get too large, nor anything to happen to the girl we cannot undo."

show andras displeased at edgeright with dissolve

"The male demon grunted. He didn’t enjoy being told what to do by Jezera, but he had his plans, and for now at least, she wouldn’t stand in the way of them."

je "And get someone to clean her up, we aren’t savages you know."

$ change_corruption_actor('alexia', 3)
return

########################################################################################################################
########################################################################################################################
########################################################################################################################


label alexia_dungeon_week_3:
#week 3

scene bg8 with fade

"Another week passed."
"Another week of Alexia being left to satisfy the hunger of the ever growing wulump, and it was always hungry."
"It continued to feed, ravaging every hole on her body with its thick, black tentacles. With each feeding it grew larger, stronger, but that only increased its appetite."
"Meanwhile, the human woman was in a near constant state of bliss. She had both been covered in, and ingested, a great deal of the slick aphrodisiac the creature secreted, and now her alien lover was all that she thought of."
"The world outside, the castle, her husband, the horrible situation they were trapped in, all these things were like hazy recollections from a past life that belonged to someone else."
"In her mind now, there was only the wulump, and her desire to please and protect it."
"The wulump had grown large now, sated by sex. If the thing continued to increase in size substantially, the small cell would be unable to contain it."
"Any person who had seen it when it was scarcely larger than a ball, only three weeks ago, would have no trouble understanding how these things were able to become such a problem."
"Jezera had been visiting every now and then to keep an eye on her experiment, and had been content with the results. Assuming they could find a safe way to control the creature, the wulump might be a useful solution to some future problem."
"Her brother had also made infrequent trips down to the cells, but his reasons were far less academic. The redhead’s transformation, thanks to the monster’s pheromones, from haughty housewife to tentacle slut amused him, and made for an enjoyable show."
"The woman had hardly noticed their presence though, and certainly didn’t care about it. Her eyes had been then, as they were now, on her beloved wulump. It had been dormant, but now it began to stir, much to her delight."
"It was feeding time again, and despite still feeling tired from the many times it had fed on her over the past week, she was eager to ensure the beast did not go hungry."

scene cg175 with fade
pause 3

"Even if she had not been such a willing “meal”, it would have made little difference. The creature was hungry, and wasted no time in wrapping its tentacles around her limbs, lifting her into the air."
"She let out a short moan as a shiver of anticipation shot down her spine when the wulump pulled her legs as wide as they would go, to give itself access to both her waiting holes."
"Her cunt was already soaking wet, an almost pavlovian response to the beast’s awakening, the need inside her like a hole that craved to be filled, both in a literal and metaphorical sense."
"A loud cry cut through the silence of the dungeons as the first tentacle penetrated her, her pussy now well used to its thickness. She moved against it as much as she could, despite being suspended, doing her best to grind her hips down on it."
"Each thrust and recoil of the black phallus-like appendage sent waves of impossible pleasure through her as she bucked against it."

scene cg176 with fade
pause 3

"Smaller tentacles formed now, grasping other parts of her body, as she moved in the air. Two thinner ones wrapped around each of her pert breasts, squeezing them, while rubbing the tips over her sensitive nipples."
"Combined with the rhythmic pounding going on below, it was enough to bring Alexia to the peak of her first orgasm, and she screamed as she came all over the beast’s wide tentacle."

scene cg177 with fade
pause 3

"Once was not going to be another for either of them though. As if it were wanting to quiet the woman down, the wulump sent one of its thick tentacles in the direction of her mouth, and Alexia was more than willing to oblige."
"As the creature continued to fuck her sodden cunt, she hungrily tongued the head of the new dick-like tentacle."
"At this point, the taste of the wulump was almost an addiction, and it wasn’t long before the tentacle was deep in her throat, with the human doing her best to take it as far inside her as she could."
"Back and forth her head jerked, as she did her best to almost swallow the thing. A “glug, glug, glug” of gagging rang out through the room, as spit drooled from the edges of her mouth."
"Every now and then she would pull her head back and allow the tentacle to flop out, if only to stop herself from suffocating, and she would spit on the tentacle, before tonguing, and kissing it lovingly."
"Eventually, back into her mouth it would go, and the “glug, glug, glug” would resume."
"The more she deepthroated the wulump’s tentacle, the more of its slick, aphrodisiac it secreted. Before long, she found herself having to swallow the black liquid; the euphoria of the act bringing her to a second, muffled climax."
"She sagged now, tired and content after two mind-shattering orgasms."

scene cg178 with fade
pause 3

"The creature was not done however, and held in place as she was, she couldn’t have done anything if she wanted to. A fat tentacle pressed against the only orifice that was currently not full, her asshole, forcing its way inside."
"Both the tentacles moved inside her now, rubbing the walls of her cunt and anus, the pleasure threatening to make her lose her mind. The tentacle further north resumed his invasion of her throat, all three violating her holes in unison."
"It was all too much for the poor girl, who found herself orgasming again and again as the beast continued its assault on her body. At this point she’d probably be unable to remember her own name."
"Eventually, the creature was finally sated, and it relented, “cumming” by secreting copious of amounts of its oily black liquid into all three of Alexia’s orifices."

scene cg179 with sshake
scene cg179 with sshake
scene cg180 with flash
pause 3

"The sensation of such a large amount filling her was enough to make her pass out, pleasure spasming throughout her body as the wulump placed her gently back on the floor."
"Sometime later, she opened her eyes to see it, dormant inside their shared cell, and her pussy began to quiver."

scene black with fade

"Soon it would be awake again."


$ change_corruption_actor('alexia', 3)
return

########################################################################################################################
########################################################################################################################
########################################################################################################################

label alexia_dungeon_week_4:
#week 4

"The orcs came, unannounced, in the middle of week. Brandishing their swords, and torches, they clashed with the wulump."
"It had grown too large, that much was clear, and if it continued to feed, it would be big enough to force its way out of the cell into the castle proper, in search of new prey to sate its ever increasing hunger."
"As large, and fearsome as the creature had become, the orcs were able to subdue it without much collateral damage. In her research, Jezera had learned how adventurers had managed to deal with wulumps in the past - the monster was afraid of fire."
"Using their torches, the orcs were able to coral the beast into the deepest, darkest part of the castle dungeon, where no poor soul was currently dwelling, and seal the door behind them."
"Alone, with no access to anybody to feed on, it would only be a matter of weeks before the wulump was starved back to its original, much cuter, size."
"Alexia had not taken the assault on her inhuman lover very well - she had wailed while scratching, and clawing at the orcs, trying to defend it from its attackers."
"Unfortunately for her, the orcs were big, and strong, while she was less than a hundred and fifteen pounds soaking wet, so her attempts to defend the wulump were rather futile. At first the orcs found her actions humorous, but eventually they knocked the poor woman out, to save themselves the annoyance. "
"When the woman woke up, the orcs were gone, and so was her beloved wulump."

scene bg8 with fade
show alexia necklace naked aroused at midleft with dissolve

al "Mmmm..."

show jezera happy at midright with moveinright
show andras happy at edgeright with moveinright

"Alexia had been in the cell for a few days, before the twins came down to visit her. She would be returning to her normal life in the castle later in the week, and Jezera wanted to check her over one last time for research. As usual, her brother had tagged along for far less intellectual pursuits."
"The demoness came over to the part of the cell where the woman was currently laying, and took her by the hand."

je "Hello, my dear."

"Alexia looked at her for the first time, as if she recognized her, but it was only a sort of half awareness, similar to the haze she had been in earlier."

al "Oh."
al "Um, hi Jezera..."

je "Hello yourself. And how are we feeling today?"

al "Okay, I guess?"

je "I’m glad to hear. Now, just let me take a look at you."

"Jezera gently placed her hand on the other woman’s chin, and looked closely at her face. Alexia’s pupils were still dilated, and her eyes were almost glazed over."

je "If you could just stand for me, please?"

"Alexia rose without question, and the demoness did a full rotation, thoroughly inspecting her body. When she was finished, she thanked her subject, and returned to her brother by the door."

an "So?"

je "As I predicted, she is perfectly fine."

an "Doesn’t look that way to me."

je "If you’d studied the after effects of a wulump attack like I have, dear brother, you would know that while its pheromones have a lingering effects, they only a few days after the subject is separated from the monster."
je "In the short term, she is perhaps more susceptible to suggestion, and has an increased libido."
je " Long term, she’ll probably have a slightly higher libido as a result, but the pheromone acts as a sort of amnesiac, perhaps some sort of evolutionary turn to try and prevent retaliation from any victims who escape."
je "There will be no long term trauma. Well, probably not. The last few weeks in the dungeon will just be a hazey blur that she struggles to recall. By the time she is returned to her husband, the effects will have worn off completely, and she will be no worse for the experience."

"The male demon grinned."

an "That completes your research, sister. Now it is time for my part of the bargain."

"She sighed, if he was anything, her brother was utterly predictable."

je "Very well."
je "But, remember that she must be returned to the help in, let’s say “decent” condition. I’d rather not risk our productive friendship with the hero over your short sighted little pleasures. Do you plan on doing the paperwork yourself?"

show andras displeased at edgeright with dissolve

an "You’re no fun."

je "I beg to differ. Still, those are my terms. Take them or leave them."

an "Fine Fine. I’ll make sure she doesn’t have anything worse than a few bruises."

je "Now, that wasn’t too hard now, was it? Try to behave yourself."

hide jezera with moveoutright

"The demoness turned on her heel and left, leaving Andras to his dark fun."

show andras happy at midright with moveinright

an "Hello, my sweet Alexia."

al "Oh, yes. Hello Andras…"

"He leaned in and kissed her. She offered no resistance, kissing him back as their tongues met together in her mouth."

al "Mmmm…"

an "Be a good girl and kneel."

scene cg206 with fade
show andras happy behind cg206
pause 3

"Just as she had done when Jezera asked her to stand, she kneeled before the demon without question. As he towered over her, he freed his semi-erect cock, so it was directly before her."
"Still affected by the wulump’s pheromones, yet starved of its company for days, the lust had been building inside of her, and masturbation, despite being frequent, had done nothing to quell it. She started at the large dick now in front of her, with an almost ravenous hunger."

show cg207 with dissolve
pause 3

"Without waiting to be told, she began to tongue the head of the demon’s member hard. He chuckled, amused that the usually resistant woman was so plient for a change. It wasn’t enough, she began to suck on the cock taking it into her mouth."

show cg208 with dissolve
pause 3

"She bobbed her head back, at first taking the now fully engorged cock in the mouth in shallow movements, but it was still not enough. As she had with the wulump, she wanted to taste more and more, until she was hungrily deepthroating the cock."

scene cg209 with fade
show andras happy behind cg209
pause 3

"Andras could get used to this. He put his hand on the back of her head, and started to buck his hips, fucking her face."

an "That’s a good little whore, show me how much you love my cock."

"The redhead continued to accommodate him as best she could, taking his large dick deep in her mouth. He pulled out and then slammed in all the way down her throat, holding her in place for a couple of seconds,  so she was forced to gag."

show cg210 with dissolve
pause 2
show cg211 with dissolve
pause 3

"He pulled out satisfied with her skills, the creature had trained her well. If almost choking on his cock had had any effect on Alexia, it was not visible. She immediately began licking and kissing the dick again, as soon as it was out of her mouth."

#cg2
scene black with fade
show andras happy behind black
show alexia necklace naked aroused behind black

"He wanted to see what else she could do, so he instructed her to lie down on the floor, which she once again did without question, spreading her legs to show what it was that she wanted."
"He grabbed her legs and lifted them up, so that they were up in the air, with only the back of her head, and her shoulders flat against the floor. Holding her in this position, he slid two fingers into her sodden cunt, causing her to elicit a loud moan."

an "Do you like that, slut?"

"She moaned again even louder. He continued to piston his fingers in and out of her pussy, curling them to stroke her g-spot."

an "Do you want it inside you?"

al "Ohhhh…...Yessss….."

"He slid another finger in, sliding in and out between her lips faster."

an "I can’t hear you. Louder, slut."

al "Yesss! Please, Yes!"

"She screamed her reply, and as she did, a torrent of squirt shot from her cunt, soaking her chest and face. She was completely out of it now, which caused the demon smirk."

scene cg190 with fade
pause 3

"It was his turn to have some fun now. He positioned himself to slide his dick into her from above, piledriver style. A moan emerged from the sodden mess below him."

show cg191 with dissolve
pause 3

"He started slow, more moans from below. The woman was completely out of it now, in bliss from the pheromone enhanced sexual stimulation."

show cg192 with dissolve
pause 3

"He began to pound away harder and harder, until he was banging against her like a jackhammer. The moans grew louder, and louder, until Alexia was practically screaming, as she orgasmed again, and again, as he pounded away at her cunt."

show cg193 with dissolve
pause 3

"The sight of Alexia below him, covered in her own juices, and constantly orgasming, was too much for even a demon, and it wasn’t long before Andras felt himself growing close to climax."

show cg193 with sshake
show cg193 with sshake
show cg194 with flash
pause 3

"With a few last hard pumps, he buried his dick in her cunt and shot his load deep inside with a grunt. The warmth brought the redhead to another climax, and a shudder shot down her spine and throughout her body."
"He pulled out and let her legs fall. She lay on the floor in an unintelligible state, his seed oozing out of her reddened, well used cunny."
"Andras smiled to himself when he looked down at what he had done to the woman. She wouldn’t remember it, that was true, but there would be plenty of other opportunities, he was sure."
"He would let her recuperate now, but he had plans for when she returned to the castle proper."

$ change_corruption_actor('alexia', 3)
$ alexiaWulump = True
$ change_actor_num_flag('alexia', 'andras_influence', 5)
$ alexiaUnfaithful = True
$ alexiaAndrasSex =+ 1

return



########################################################################################################################
########################################################################################################################
########################################################################################################################

label alexia_locked_in_the_dungeon_not_NTR:
# if not NTR, Alexia will just get stress in silent event
$ change_actor_stress('alexia', 50)
return
