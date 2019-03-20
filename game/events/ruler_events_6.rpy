init python:

    # Jezera and Shaya have personal time
    # Req Brothel exist.  High priority until change to NPC events or end date is extended.
    event('jezera_and_shaya_personal_time', triggers="week_end", conditions=('castle.buildings["brothel"].lvl >= 1', 'week >=4'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Drider egg found (benediction)
    #Requires that the breeding pit exist and have an open space.
    event('drider_egg_found', triggers="week_end", conditions=('castle.buildings["pit"].lvl >= 1', 'castle.buildings["pit"].free_space >= 1', 'week >=4'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Cliohna's Unwanted Results
    #Req:  Cliohna's hero studies
    event('cliohna_s_unwanted_results', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, depends=("cliohna_s_hero_studies",), priority=pr_ruler)
    #Breeding pit's first monster (worldbuilding)
    #Requires that breeding pits have a monster in them.  High priority.
    event('breeding_pit_first_monster', triggers="week_end", conditions=('week >=4', 'castle.buildings["pit"].free_space < castle.buildings["pit"].capacity'), group='ruler_event',
        run_count=1, priority=pr_ruler_high)
    #Drider gets loose (malediction, sex)
    #Requires that there be at least one drider in the breeding pits and four orc soldiers.
    event('drider_gets_loose', triggers="week_end", conditions=('castle.buildings["pit"].driders >= 1', 'castle.buildings["barracks"].troops >= 4', 'week >=4'),
        group='ruler_event', run_count=1, priority=pr_ruler)


label jezera_and_shaya_personal_time:
# Jezera and Shaya have personal time
# Req Brothel exist.  High priority until change to NPC events or end date is extended.

scene bg24 with fade
show alexia 2 necklace neutral at midleft with moveinleft

al "Hello, Shaya?"

"Alexia glanced around the brothel's entrance, looking for the operator and trying to ignore the sounds of the other residents engaged in other activities. A male slave with a particularly well shaped chest made this rather difficult."

#al blush
al "Oh, uh, no! Shaya?"

"After stepping around the back of the counter, she knocked on the door to the office.  This unintentionally pushed it open and revealed an empty room beyond."

#al confused
al "Is there anyone in here?"

"The woman glanced over her shoulder to see if anyone was watching her, then slipped into the room while closing the door behind her."

#al serious
"The room was dominated by a small private stage with several couches surrounding it. There were two other areas divided by screens: a sleeping area and a dressing area. They were also deserted."
"Shaya's quarters had a similar level of excessive decoration and finery that the rest of the brothel had, but a much more imperial feel. This room reminded Alexia of Rowan's stories about the Empire of Sand, in the Northern reaches of the Six Realms."
"For a moment she hesitated, listening for the sounds of anyone coming, then decided to focus instead on snooping when all she heard was the sounds of at least two women moaning in pleasure."
"Since there was no desk, Alexia instead started pulling open Shaya's drawers to see if there was anything of note in there. She only found hair brushes, jewelry, and soft silks. Then the woman's heart almost jumped out of her chest at the sound of the door suddenly opening!"

show alexia 2 necklace concerned at midleft with dissolve
show jezera neutral behind bg24

je "...always short something, so revisions are common."

show alexia 2 necklace concerned at edgeleft with moveoutleft
hide jezera

"Trying to make as little sound as possible, Alexia crept to one of the cracks between the screen separating the dressing area from the rest of the room and peeked out at the two women who were entering into the room."

show jezera happy at midright with moveinright
show shaya neutral at edgeright with moveinright

je "My, my, you've really spruced this place up, feels just like home!"

sha "I had some free time after getting settled, so I made it a personal project to bring a slice of civilization to this corner of the world. As my staff grows, I doubt I'll have the chance again."

"The half-demoness took a seat on one of the couches, directing her companion to take the spot next to her. Alexia noted to herself that seemed a bit rude, considering this was Shaya's room."

je "So, how soon do you think you'll be ready with this change?"

je "It will take a couple months at least. However, I'm unconvinced that this project will be cost effective, Jessy, are you sure that this pirate will even make three hundred crowns with that kidnapping?"

show jezera displeased at midright with dissolve

je "Of course! Are you doubting my sense for this?"

"Shaya seemed to want to say something, but held her tongue. At the same time, Jezera was looking around the room again. After a moment her eyes lit up."

show jezera happy at midright with dissolve

je "Wait, this is- Shaya, you didn't!"

show shaya happy at edgeright with dissolve

je "Oh you little minx! Come here."

"Abruptly the blue skinned woman wrapped her arm around Shaya's neck and pulled her into a deep kiss. Alexia watched with wide eyes as the act grew more and more passionate, tongues being very liberally involved."

menu:

    "Alexia was forced to watch since she couldn't sneak past them undetected.":
        $ released_fix_rollback()
        jump .jezShayaSex

    "The two women moved to the sleeping area, allowing Alexia to sneak away.":
        $ released_fix_rollback()
        scene bg24 with fade
        #al blush
        show alexia 2 necklace concerned at edgeleft with dissolve
        show jezera happy at midright with dissolve
        show shaya happy at edgeright with dissolve
        hide shaya with moveoutright
        hide jezera with moveoutright
        "Much to Alexia's relief, the two women got up together and moved across the room to the sleeping area, shedding their clothing along the way."
        hide alexia with moveoutleft
        "Once they were behind the screen and the sounds of moans drifted over it, Alexia took the opportunity to sneak back out of Shaya's quarters while taking care to close the door as quietly as possible."
        #end scene
        return

####################################
label .jezShayaSex:

#CG of Jezera and Shaya kissing (for scene replay)
scene cg188 with fade
show jezera happy behind cg188
pause 3

"Alexia's eyes darted around the room, searching for any chance of escape. Unfortunately, the path back to the door was completely exposed and she had no realistic chance of getting past without being spotted."
"To make matters worse, the two women didn't look like they'd be moving somewhere else anytime soon. For the moment, the red haired woman had become an unwitting audience."
"Without breaking the kiss, Jezera's hand moved down Shaya's body, caressing the exposed skin and then slipping around the soft fabric covering her womanhood. A moan could be heard in response to the touch, muffled as it was uttered into the other woman's mouth."
"Finally Jezera pulled her head back with a giggle and ran her tongue over her lips."

je "I love the taste of your mouth, darling."

scene cg124 with fade
show jezera naked happy behind cg124
show shaya happy behind cg124
pause 3

"Shaya didn't respond right away, instead she laid down across Jezera's lap and slid the two straps on her lover's top, revealing two pert blue breasts."

sha "And I love the taste of your breasts."

"She cupped one breast and ran her tongue around the nipple of the other. A wide smile formed in response to her ministrations, followed by a small gasp."

je "Hmm, yesss... Oh! Cheeky little biter!"

"A moment after that, there was a sharp gasp from Shaya."

sha "Jessy, my ass?"

je "Relax, it's just my pinky."

sha "That's not what I'm worried about."

je "Hush, just work your magic while I work mine."

"It seemed like there'd be another response, but that was silenced by Jezera forcing her back onto her breasts."
"Based on the noises that Jezera was making, Shaya was nipping at her again in protest, but the demoness did not release her from her breast until she pulled a sullied hand from the dancer's loins."

je "See, you love it."

sha "Jessy, we've talked about this, please don't touch my ass."

je "Hmm, perhaps a more direct demonstration is in order then?"

"After a wave of her hand, a dildo attached to a harness appeared in Jezera's grip."

je "I'm sure I could convince you with this that-"

scene black with fade
show jezera naked happy behind black
show shaya happy behind black

"Shaya snached up the strap-on from Jezera's hands and jumped to her feet.  Then with a spin and a flurry of silks managed to both remove her pants and don the device in about a second!"

sha "Since I've already cum, I think it's more appropriate if I make use of this."

je "What a naughty girl you are, rejecting my gift and then stealing from me!"

"However, as she spoke she rolled up the skirt of her dress and presented herself to her partner with an exaggerated stretch."

scene cg68 with fade
show jezera naked happy behind cg68
show shaya happy behind cg68
pause 2

"Shaya wasted no time and climbed on top of Jezera, sliding into her ass in one smooth motion."

je "Oh, feisty! Come on, Shaya, take me hard!"

"The dancer obliged her, moving her hips hard and fast, eliciting loud gasps of pleasure from the blue skinned woman. In spite of the frantic pace, Jezera got into the act by using one hand to play with her breast and another to finger herself."
"She gasped, moaned, then came, all in the span of about fifteen seconds. Alexia was surprised at just how quickly it happened, and Shaya seemed to be just as surprised."

sha "Wow, it's not like you to be in such a hurry."

"Jezera's legs came up and wrapped around Shaya's head at the same time that the strap-on vanished from her legs and appeared spinning on its creator's finger."

je "There, now that I have cum, let's discuss that lovely ass of yours again."

scene bg24 with fade
#al blush
show alexia 2 necklace concerned at edgeleft with dissolve
show jezera happy at midright with dissolve
show shaya happy at edgeright with dissolve

sha "Wait no, Jes-"

hide shaya with moveoutright
hide jezera with moveoutright

"She was silenced by another kiss, then lead up from the couch and around towards the sleeping area and out of Alexia's sight. Evidently Jezera wasn't in the mood to argue this point anymore as she didn't give Shaya a chance to speak again."

hide alexia with moveoutleft

"Once the sounds of wet slapping and moans drifted over the screen, Alexia took the opportunity to sneak back out Shaya's quarters while taking care to close the door as quietly as possible."

#Alexia gains a small amount of corruption
$ all_actors['alexia'].corruption += 2
#end scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drider_egg_found:
#Drider egg found (benediction)
#Requires that the breeding pit exist and have an open space.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with moveinright
show skordred neutral at skorright with moveinright

ro "Something to report?"

sk "Aye. Excavashun' team stumbled on an old nest way down in the ruined catacombs ah tha old castles. We found eggs, so I called Draith to take a look."

dra "They're ancient drider eggs, several centuries old."

"Rowan set down his work and straightened up."

ro "But even after all this time they're still viable?"

show draith happy at midright with dissolve

dra "Yes! Well, one at least."

sk "Right, I'll leave ya two to it then."

hide skordred with moveoutright

dra "Drider eggs go into hibernation when they're cold and only hatch in a warm environment. They're human-spider hybrids, but are endothermic so can't survive really cold places."

ro "I know what a drider is, Draith."

show draith neutral at midright with dissolve

dra "Right, sorry sir. Since the excavation teams have breached the chamber, I don't expect these eggs to last in there, so I'd like to hatch what I can now and add them to the pit."
dra "If you can't spare the cage space, I understand."

#player can choose whether they want a drider or not, if pits capacity is full, first option should be greyed out

menu:
    "Gain a drider." if castle.buildings['pit'].free_space >= 1:
        $ released_fix_rollback()
        #line below should display correctly depending if player already has a drider or not
        if castle.buildings["pit"]._driders >= 1:
            ro "Please hatch the egg Draith, we can definitely use another drider."
        else:
            ro "Please hatch the egg Draith, we can definitely use a drider."
        show draith happy at midright with dissolve
        dra "Understood sir! I'll get started right away."
        #Gain a drider and end event
        $ castle.buildings["pit"]._driders += 1
        return

    "Leave the cell open.":
        $ released_fix_rollback()
        ro "Sorry Draith, but I don't want you to hatch that egg."
        #dra sad
        dra "Alright, understood sir."
        #end event
        return
return
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label cliohna_s_unwanted_results:
#Cliohna's Unwanted Results
#Req:  Cliohna's hero studies

scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "I got your message, what would you like to talk to me about?"

"The woman put down her work immediately, but didn't turn to speak to Rowan."

ro "Is now a bad time?"

cl "No."

"However, she still didn't turn around or look at the man she'd called here."

ro "Well then... what is it?"

"Finally she looked at him, revealing an expression that Rowan hadn't seen on her face before. In fact, he couldn't remember seeing much of any expression on her face."

show cliohna angry at cliohnaright with dissolve
cl "It is not through any fault of yours, but you have vexed me greatly."

"She looked, annoyed? Frustrated? Maybe even exhausted?"

cl "Since you were gracious enough to provide me with your seed, I have spent nearly all of my personal time attempting to discern what, if any, magical power you have."
cl "Again, and again, and again, all of my efforts have disproved every possible avenue that could conceivably grant you such potential. I can only conclude, with great reluctance, that you truly are an ordinary man."

"Rowan spread his arms wide and gave a big shrug."

ro "Well, I did warn you about that, though it does sounds like you did the most thorough test anyone's done of me."

"The sorcerer broke eye contact and started drumming her fingers on the table for a few seconds."

"Right away Rowan could tell that there was something else she hadn't said yet, some people had these kinds of ticks when they were trying to decide if they should say something or not. Considering it had to do with him, the hero decided it was worth pushing her just a bit."

ro "With all those tests, surely there was something interesting you found out?"

show cliohna neutral at cliohnaright with dissolve

"Cliohna let out a long sigh and stopped rapping her knuckles."

cl "Yes, I did detect what appeared to be faint magical potential within you at first that I couldn't eliminate, but the more I looked the more I realized that it was someone else that you'd been in contact with. There were other auras, but this one I couldn't identify."

ro "Really? Who do you think it was?"

cl "I assume it was someone you met while out travelling, there was no demonic energy to it and I've already tested the major castle staff you work with every day."

ro "I do encounter a great number of people like that, but would they really have rubbed off their aura's onto my seed from such a short visit?"

cl "No sweethearts, no repeatedly visited acquaintances?"

ro "No."

cl "Fascinating, then there must be someone in the castle that I missed. Who have you been sleeping with? Anyone you've spent a significant amount of time in the presence of over the last year?"

ro "Well...."

scene bg12 with fade
show cliohna angry at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral behind bg12

"It was nearly an hour later and Cliohna was just finishing a quick surface test on the most likely person that Rowan thought it could be."

ro "So, what's the results?"

cl "I cannot believe this.  It defies all logic.  How is it you have nothing, YET SHE DOES?!"

show rowan necklace shock at midleft with dissolve

"That was the first time Rowan had ever heard Cliohna raise her voice.  Feeling the air start to crackle with static, the hero wisely started to back off."

al "Uh... should I leave?"

hide alexia
show alexia 2 necklace concerned at edgeleft with moveinleft

"The man hastily mimed to his wife to stay silent while the sorcerer continued to fume.  He took her hand and the two edged away together."

show bg12 with flash

cl "Drast!"

"She almost screamed that while the test tube in her hand exploded with a blast of crackling electricity.  The couple had nearly reached the main hallway for the library."

show bg12 with flash

cl "A FUCKING HOUSEWIFE!"

hide alexia with moveoutleft
hide rowan with moveoutleft

"Another burst of energy flashed around the place where the tube had been once again, then another. At this point, Rowan and Alexia were able to slip around a corner and hurry out of the library, leaving the muffled cries of indignant rage behind them."

scene black with fade

"It would probably be best to wait a time before approaching Cliohna about this subject again. Even so, this revelation was quite a bit to sink in, apparently Alexia had magical potential!"

#end scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label breeding_pit_first_monster:
#Breeding pit's first monster (worldbuilding)
#Requires that breeding pits have a monster in them.  High priority.

scene bg25 with fade
show draith neutral at midright with dissolve
show andras displeased at edgeright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Master, Draith, I understand we have our first monster now?"

show draith happy at midright with dissolve
show andras happy at edgeright with dissolve

an "Ah servant, how wonderful for you to join us for this glorious occasion! Let us enjoy this together."

dra "Then, if you handsome men would follow me?"

"The dark elf lead the small group down the row of cages until they arrived at one where several orc handlers were attempting to either coax or force out the creature that was contained inside."

#if first monster is a drider
# TODO: ignore monster type for now

"Finally a fully grown female drider came skittering out of the cage and pounced onto one of her handlers.  Rowan started to run forwards, but was stopped by a hand from Draith, who simply indicated he should watch."
"Instead of biting the orc with her mandibles, the creature started caressing her breasts and tethering strangely side to side. Two of the other handlers climbed onto her legs and started molesting her at the same time, which the drider seemed to enjoy."
"Once they got closer, Rowan could see now that the creature seemed to be mating with the orc she had tackled earlier and the others had joined in the fun. In-spite of the carnal display, the hero couldn't help but take note of the size of the creature and how quickly it had moved."

dra "Driders are fascinating creatures. No culture or societies and almost impossible to communicate with, but dangle the prospect of sex in front of them and they can be taught to do almost anything."

#rejoin

an "Marvelous. This creature will be of great use in our armies, I'm sure. How soon will be able to breed more?"

dra "Breeding will be out of the question until we can upgrade our facilities, but thanks to Rowan's efforts we'll have no problem completely filling up all our available cells with the site he found."
dra "The limiting factors right now are only space and supply. With the right know how and funding, Skordred will be able to help with the problem of space."
dra "As for supply, If Rowan can find more nests of the same species, we'll be able to accelerate how quickly we can raise them. I'll also be able to raise other creatures if their nests can be found, assuming we have the space for them."

show andras displeased at edgeright with dissolve

an "Very well. Rowan, once we have a few more of these things down here, I hope you can find a nice innocent village I can cut their teeth on."

show andras angry at edgeright with dissolve

an "Then we'll see first hand just how mighty these monsters are!"

#End event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drider_gets_loose:
#Drider gets loose (malediction, sex)
#Requires that there be at least one drider in the breeding pits and four orc soldiers.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with moveinright
show orc soldier neutral at edgeright with moveinright

#dra worried
dra "Rowan! Rowan! One of our driders broke away from training and escaped into the tunnels! Now she's on a raping spree and moving towards the outer tunnels!"

ro "What? How did this happen?"

#dra sad
dra "It's my fault, this particular monster was much wilder than most and didn't respond to training well. I mean, she loved having sex as much as any other drider, but she wouldn't obey anyone for it. I should have been more careful with Black Ness."

"The hero strode forward and clapped a hand onto the monster breeder's shoulder."

ro "Everyone makes mistakes and it's too late to change anything about that now."

#dra neutral
dra "Yes sir. Ness will probably escape into the forests soon and we'll never be able to catch her then. What should we do?"

menu:
    "Risk your own body as bait for a trap to recapture the female drider.":
        $ released_fix_rollback()
        jump driderSexScene

    "Send in a squad of orcs to attack and capture it.":
        $ released_fix_rollback()
        ro "Soldier, go gather a squad of orcs and bring them to the outer tunnels. Myself and Draith will go ahead and plan our attack."
        os "Yes boss!"
        scene black with fade
        "The fighting was fierce and cost the lives of several of the orc soldiers, but the escaped drider was back in the pits by the end of the day and Draith started working on devising a new way to train it."
        "The triumph ended up being quite the story among the soldiers and they frequently discussed it among their friends. While this blunder had cost the lives of several of their fellows, the orcs as a whole felt better afterwards."
        #Lose four orc soldiers, gain 3 morale.
        $ castle.buildings["barracks"].troops -= 4
        $ change_morale(3)
        #end event
        return

    "Let it escape.":
        $ released_fix_rollback()
        ro "Let it go, it isn't worth it at this point. Pull everyone out of the drider's path so we can avoid anymore damage."
        os "Wah!? Yous a coward!"
        ro "I gave you an order soldier, carry it out."
        hide orc soldier with moveoutright
        scene black with fade
        "The drider fled through the underground passages until it had stumbled its way out of the castle and into the forests surrounding Bloodmeen."
        "There was no major damage or casualties after its escape, but many of the soldiers were upset afterwards that such a beast had apparently gotten the better of them."
        #lose 1 drider, lose 5 morale.
        $ castle.buildings["pit"]._driders -= 1
        $ change_morale(-5)
        #end event
        return

label driderSexScene:

ro "You said that this drider is still very interested in sex, right?"

dra "Yeah, she's left quite a few dazed orcs in her wake."

"Rowan nodded and turned to the orc soldier that had accompanied the dark elf."

ro "Soldier, go gather a squad of orcs and bring them to the outer tunnels. Myself and Draith will go ahead and set a trap for the drider, then you will capture it."

#dra worried

os "Yes boss!"

hide orc soldier with moveoutright

dra "Wait, what do you have in mind?"

#tunnels bg
scene black with fade
show rowan necklace naked at midleft with dissolve
show draith neutral behind black

ro "Alright beasty, where are you? Hello? Ness?"

"He called out into the tunnels for the drider, trying to draw it into his trap. Surrounding the hero was a squadron of orcs with nets, handling rods, and a very worried dark elf breeder, all nestled into cracks and crevices or behind rocks."
"Rowan was quite pleased with how well he'd hidden everyone, after selecting this spot for the ambush due to how many good hiding places there were. Orcs didn't like sitting still like this, but their discipline held."

ro "Here, drider drider drider!"

dra " Rowan! That's not how you call out to a beast as noble as a drider!"

hide draith
#draith annoyed
show draith neutral at edgeright with moveinright

"The hero turned to the dark elf who'd poked his head out from behind a boulder with a look of annoyance."

ro "I'm afraid that handling monsters properly was never something I needed to learn before now, how would you suggest I proceed?"

dra "First off, stop covering your cock, make sure it's on full display! Then, make a chittering sound like this: Chita chita chit!"

"Suddenly something slapped the back of Rowan's head and he tried to wheel around to face what had attacked him. Unfortunately, this act caused him to become wrapped up in the sticky webbing that had been lobbed onto him."

ro "Oh no."

hide rowan with moveoutleft
show rowan necklace naked behind black

ro "Wahhhhhh!"

show draith neutral at center with moveinleft
show orc soldier neutral at edgeleft with moveinleft

dra "Rowan!"

scene black with fade

"The female drider caught Rowan in mid-flight and fled down the tunnels away from the ambush. He could hear Draith and the orcs calling after them and then launching into pursuit, but his captor soon outpaced them."
"With his upper body completely immobilized by the webbing, he couldn't do anything to get away from its grip, leaving him helpless in its arms as it sought out a refuge of some kind."
"Finally the drider slipped into a tiny side passage and dropped Rowan to the ground.  It darted about the hallway for a moment, then pounced onto his mostly nude body, grinding its softer underbody over his cock."

scene cg121 with fade
show rowan necklace naked behind cg121

"Like all driders, this creature appeared to be a giant spider, but with the torso, arms, and head of a pale skinned human instead of a spider head."
"The upper body wasn't entirely human, mandibles tipped with poison sprouted at the base of their jaw and the point where carapace gave way to skin."
"The lower body was mostly a black exoskeleton with hairs coming off of the legs and abdomen. At the back of said abdomen, which was almost as wide as Rowan was tall, was the drider's spinnerette which the creature had used to make the thread it had captured him with."
"Since he didn't seem the be going anywhere right now, the hero took a moment to study it's (her?) more human features. She looked to have been in her mid to late twenties, with a very fit muscled body."
"Her breasts were about average in size and there was a distinct hint of hips just before the body ended."
"Then there were the eyes, eight pools of black scattered around her head that occasionally peeked out around her soft silky white hair. At least the two main ones where eyes should be were possible to focus on to avoid being unnerved. Then Rowan retracted that thought."
"His attention was brought down to the creature's monstrous body, at the place where it was rubbing his groin. The stimulation had started to make his member grow hard, and now he could see that there was a sort of flap or slit there."

ro "(Her sex?)"

"Sure enough, once the creature realized that he was getting hard, those flaps split open and thick drops of goo started plopping out of it. Rowan only had a moment to look at the thing before the drider lowered itself down to engulf his member inside."

scene cg122 with fade
show rowan necklace naked behind cg122

"The man groaned as he was engulfed by her, sliding into a passage that was a mix of flesh and silk that clamped down onto his shaft."
"Once he was fully inside, the drider closed its eyes and made a soft chittering sound which he interpreted as a sigh of pleasure based on her body language."
"She didn't stop moving when he was completely inside her, immediately going into a steady rhythm of rising and falling on her legs. At the same time, she pressed her human arms down on his chest and leaned back with a look of contented arousal on her face."

ro "(Woah, for a vicious monster she's surprisingly cute like this.)"

"Another groan escaped the man's lips as the drider pressed herself down on him particularly hard in time with her sharply inhaling."

ro "(Did she just cum?  Already?)"

"If the drider had orgasmed, she showed no signs of being done and hardly even slowed her stride. Though now Rowan could feel his own peak approaching, given how strong and insistent her stimulation was, this wasn't surprising."
"Just as he let himself go and sent ropes of jiz into the monster's inhuman vagina, Rowan realized that he could hear the sounds of people nearby. Sensing his chance, he grabbed onto the drider's hands since they were within his reach and called out to his companions."

scene black with fade
show draith neutral behind black

"The drider realized almost immediately that it was in trouble, but was unable to disentangle itself from Rowan before the orcs got into the side passage and threw their nets over her."
"In desperation, she bit into Rowan with her lower mandibles and gave him a dose of poison to make him let go. However, she didn't get far and was subdued shortly afterwards."

dra "Sir? Rowan? Are you alright?!"

"Thankfully for Rowan the poison wasn't too bad and he hadn't gotten a big dose of it. Unfortunately he would still feel its effects for some time, along with the memory of mating with a monster."

#Rowan is injured.
$ take_damage(1)
#End scene.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
