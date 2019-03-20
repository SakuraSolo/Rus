init python:

    # Greyhide's first gift
    # Req: Forge, should happen within 6 weeks after building
    # activated in "forge_purchased" with timer=dice(5)
    event('greyhide_s_first_gift', triggers="week_end", conditions=("castle.buildings['forge'].lvl >= 1", 'week >=4'), group='ruler_event', active=False, run_count=1, priority=pr_ruler_high)
    #Unwanted room guest
    #Req: Poisoned event
    event('unwanted_room_guest', triggers="week_end", conditions=('week >=4',), depends=('poisoned',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Indarah's first gift
    #Req: Requires Tavern, should happen within 6 weeks after building
    # activated in "tavern_purchased" with timer=dice(5)
    event('indarah_s_first_gift', triggers="week_end", conditions=("castle.buildings['tavern'].lvl >= 1", 'week >=4'), group='ruler_event', active=False, run_count=1, priority=pr_ruler_high)
    #Orcish Occupational Savagery
    event('orcish_occupational_savagery', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Champion statue sculpting
    #Req: After week 8
    event('champion_statue_sculpting', triggers="week_end", conditions=('week > 15',), depends=('wall_inspection',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Cliohna's hero studies
    #Req: After week 6, high priority after week 14
    event('cliohna_s_hero_studies', triggers="week_end", conditions=('week > 6',), group='ruler_event', run_count=1, priority='pr_ruler_high if week > 14 else pr_ruler')



label greyhide_s_first_gift:
#Greyhide's first gift
#Req: Forge, should happen within 6 weeks after building

scene bg6 with fade
show rowan necklace neutral at edgeleft with dissolve
show greyhide neutral at center with moveinright
show jezera happy at edgeright with moveinright

je "Here you are."

gh "Oh, thank you."

ro "Wait, what's going on?"

je "I found this big guy wandering around the halls. Turns out he was looking for you."

"She winked and waved before leaving."

je "Have fun you two, oh and Rowan, please be a dear and help your friend find his way back after you finish."

hide jezera with moveoutright

"After the woman left, Rowan turned his full attention to the minotaur. He quickly noticed that the old warrior was carrying something, maybe a flask?"

ro "Hello Greyhide. What brings you up to see me?"

gh "I've learned that you travel the world, that you seek enemies for the brat to send his soldiers to fight. I don't want you to die out there."

ro "I appreciate the sentiment. Did you bring me something to help me survive?"

gh "Yes."

"He held out the item that man had noticed him holding. It seemed to be a leather waterskin, probably what minotaurs usually used to hold liquids. Rowan accepted it, finding that it still held a trickle of something."

gh "Drink it. It makes warriors stronger for fights and long journeys, it's my last dose."

"The man made eye contact with the minotaur and considered him. There was a strange kinship there, something that Rowan could trust. Greyhide wouldn't try to hurt him, so he drank."
"It burnt his tongue, so he swallowed it as soon as he could. Immediately Rowan recognized the effects of a magical potion gripping his body. A jolt of energy rushed through him shortly aftewards, filling him with strength."
"Rowan smiled to Greyhide, which was returned by a nod."

ro "Thank you. I won't forget this."

gh " If I get more warrior's blood, I will share it with you."

"Silence for a moment, then the minotaur looked side to side before turning back to Rowan."

gh "I fear that the woman was right. Could you please show me the way back to my forge?"

ro "It's the least I can do."

#gain temporary boost to strength for three weeks
$ add_effect(MultiEffect("\"Warrior's blood\"", 'pos', (('strength', 2),), 3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label unwanted_room_guest:
#Unwanted room guest
#Req: Poisoned event

scene bg9 with fade
show rowan necklace neutral behind bg9
show jezera neutral behind bg9

"Rowan decided to retire to his room shortly after lunch for a little time to himself. Most of his breaks were spent walking around the castle or on brief excursions outside. He wasn't one who sought to meditate by sitting still often."
"Suddenly there was a noise, to which the ever vigilant hero immediately responded. His eyes snapped open and quickly surveyed his surroundings. Everything seemed normal, except for...."
"He dove to the side as a shadow shot out from under his bed towards him, iron glinted in the sunlight when the figure passed in front of his window. The assailant was too slow to respond and their blade scored only a grazing hit."
"Rowan rolled easily and came up with with his sword. With two quick motions he'd pulled it free from its scabbard and was ready to fight. Now he had a chance to study his opponent, who proved to be a humanoid wrapped in a full body suit of leather armour."
"They were thin and lithe, a little shorter than he was. That suggested either a human woman or an elf, but with the mask he couldn't tell for certain."
"His attacker didn't come at him again, instead they seemed to hesitate and look back and forth in the room. Rowan tensed to launch an attack of his own, but as he began to move forward the other evidently came to a decision and turned to run away."
"The would-be assassin jumped straight into Rowan's window, which shattered under their weight. A curse escaped Rowan's lips when he looked out the window and saw the figure use some kind of magic to hover down and away from the castle towards the forest below."
"After retrieving his bow from a closet, he attempted to shoot whoever his attacker was, but they were too far away by then for him to make an accurate shot and the two arrows he loosed flew wide. Rowan lowered the weapon and placed a hand on his necklace."

ro "Someone just tried to attack me in my room. They fled out my window using some kind of levitation magic."

je "This is troubling. That's the second time someone's tried to kill you now. Do you know who wants you dead?"

ro "I was hoping you might be able to tell me. Any chance you or maybe Cliohna could use magic to follow them? I can't exactly track someone who flies."

je "Not unless one of us was there right now or whoever it was decides to stick around and keep using magic. I'm on my way over now, we'll see if there's anything to be done when I arrive."

"Rowan nodded, heedless that that wouldn't get sent through the amulet. He released the sapphire stone and looked down over the forest again as the leather clad figure vanished into the trees. This wasn't over yet."

"A glance to his wound revealed what he'd feared: the blade had been poisoned."

#int injury
$ add_effect(Injury('Poison', 'intelligence', -2))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################



label indarah_s_first_gift:
#Indarah's first gift
#Req: Requires Tavern, should happen within 6 weeks after building

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show indarah neutral at midright with moveinright

ro "Good morning Indarah, it's unusual to see you in the castle."

ind "Also not my usual wake up time. Jezera wanted to meet with me, so here I am."

ro "On your way in or out then?"

ind "Out, but I figured I'd drop by and say hi before I left."

"The dark skinned woman looked away from Rowan, fidgeting for a moment before meeting his gaze again."

ind "I wanted to apologize for being so terse with you when we met, you were just looking out for me in your way. As well as to thank you."

ro "No thank you is needed, our situations are different so it isn't fair to-"

ind "No, I mean for my tavern. Jezera told me you're the one who decides what money gets spent on, so I wanted to thank you for building it for me."

ro "Oh, well, I guess you're welcome. Though honestly I can't claim that I meant for you to get it afterwards."

ind "It doesn't matter."

"She pulled a small charm out of her silks and held it out to Rowan."

ind "You played a part, so I would like you to have this."

"The gift turned out to be a fairly simple copper plate with a symbol carved into it. It wasn't something that the hero immediately recognized but it did seem familiar."

show rowan necklace happy at midleft with dissolve

ro "Well thank you for the gift."

ind "It is a gift of fortune, meant to help sailors on voyages. Remember that the magic won't last, but for a time you may find that the world favours you."

"He pocketed the metal piece and gave a warm smile to the woman."

ro "I don't believe that I wished you good fortune yourself, so let me take the opportunity to do so now."

ind "It is appreciated. Good morning to you, hero Rowan."

hide indarah with moveoutright

"She curtsied to him, which Rowan returned with a sweeping bow.  Indarah made her way out of the throne room, but came back a moment later."

show indarah neutral at midright with moveinright

ind "When exactly did you learn about the customs of the Dragon's Tail?"

ro "Picked it up during the war. Turns out knowing how to make a good first impression with everyone was a pretty useful trick. I made a point of learning the basics for all Six Realms and for any other races I happened to deal with."

"That got Rowan a nod of both approval and respect."

ind "Now there's something impressive. You should give me a rundown sometime, I think I'll find a use for them."

ro "I'd be happy to."

hide indarah with moveoutright

#gain temporary boost to luck for three weeks
$ add_effect(MultiEffect("\"Sailor's charm\"", 'pos', (('luck', 2),), 3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label orcish_occupational_savagery:
#Orcish Occupational Savagery
#No prereqs

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at cliohnaright with dissolve

"As much as he'd wished that he could avoid knowing about this issue, Rowan knew at the back of his mind that he'd eventually have to deal with the orcs in the service of the twins taking advantage of their charges."
"In fact, it was a bit of a blessing that it had taken this long to actually become a problem."
"A report detailing the practise of rape gangs in an occupied village lay on his desk. It was incredibly blase about the event, mentioning it only as an afterthought. However, that detail was the only real one of note in the report."
"Rowan always wished that this simply wouldn't happen, but now that it had he would have to make a decision. If he did nothing, the problem would only get worse. That would mean more stories and more refugees fleeing from the twin's armies, to say nothing of his consciousness."
"However, this was something that orcs expected as a perk when they agreed to join Andras. An official move to stop the practise would greatly upset the orcish troops, even those who weren't even in a position to participate."

os "Is dat all boss?"

menu:
    "Stop the rape gangs":
        $ released_fix_rollback()
        ro "Send a message to your commander, the rape gangs are to stop immediately."
        os "What?!"
        ro "There will be no raping or violating of any people in our service, is that understood?"
        "The orc's response was to spit on the floor."
        ro "That is an order, soldier."
        "A hand went for his sword, though a fierce and steady gaze from the hero made him pull it back. The tension in his stance remained, however."
        "Satisfied for the moment that a fight wasn't going to start, Rowan wrote an official order and handed it to the messenger. Without saying a word, the soldier snatched up the document and stomped out of the room towards the portal chamber."
        ro "Hah, that isn't going to be the end of this. I'm going to have to follow up to actually get them to stop."
        ro "(And they're going to be fighting me every step of the way....)"
        #Lose a lot of morale.
        $ change_morale(-20)
        return

    "Turn a blind eye.":
        $ released_fix_rollback()
        ro "Yes, that's all. You may leave, soldier."
        "He saluted and marched out of the room towards the portal chamber."
        "Rowan only covered his face and offered up a silent prayer for both himself, and those he'd abandoned to the orcs's lusts."
        #gain infamy, guilt, and corruption
#~         $ avatar.base_infamy += 2
#~         $ avatar.base_guilt += 2
#~         $ avatar.base_corruption += 2
        $ change_base_stat('f', 2)
        $ change_base_stat('g', 2)
        $ change_base_stat('c', 2)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label champion_statue_sculpting:
#Champion statue sculpting
#Req: After week 8


scene bg20 with fade
show skordred neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "What is it, Skordred? Calling me in here is very unusual for you."

"The dwarf continued to work on something at one of the benches, pointedly ignoring the new arrival. Even though he'd been invited, Rowan realized that there wasn't going to be any courtesies extended to him."
"After a moment's wait, the master builder stood up and faced the hero."

sk "You may be one of the sinners who killed the world's proper ruler, but ya are nah a champion of chaos in service to the lords of Bloodmeen."

"Rowan decided not to say anything, preferring not to discuss this topic himself."

sk "For those occupying such a post, I grant the honor of carving their likeness into stone to join the castle's silent guard."

ro "That's fine, you don't need to trouble yourself about making any statues of me."

sk "This act brings great satisfaction to me, it is one of my few joys beyond my duties. I would not have called ya here had I not concluded that I genuinely wished to do it. Even with ya as the subject."

ro "Ah, well, I suppose it would be a bit rude to turn you down. What did you need from me then?"

sk "I require detailed measurements of yar body as well as to record the likeness of yar features. My sculpture shall be as close as possible to yar true appearance."

ro "Alright. Do you want to do that right now?"

sk "Aye. Strip naked and get yar prick erect."

ro "... Wait, what?"

sk "I said, strip! An if ya canna get hard on your own, I'll help you."

menu:
    "Strip naked for Skordred":
        $ released_fix_rollback()
        jump .skorStrip

    "Don't strip":
        $ released_fix_rollback()
        ro "Is this really necessary for your sculpture?"
        sk "Ah course, yar cock is of the utmost importance to preserve in stone.  Ifin ya cannot let me study yar form naked, then ay can ferget the whole thing."
        menu:
            "Strip for Skordred":
                $ released_fix_rollback()
                jump .skorStrip
            "Refuse again.":
                $ released_fix_rollback()
                ro "The answer is no then."
                sk "Then get out of my workshop until yar duties require it."
                return

label .skorStrip:

#CG of Rowan awkwardly stripping with Skordred nearby holding a tape measure.
scene black with fade
show rowan necklace naked behind black
show skordred neutral behind black

"While Rowan began to remove his garments, the dwarf gathered several supplies. These included a workbook, a tape measure, and a sketchpad."

ro "So, you've been doing this for awhile now as a hobby?"

sk "Of a sort."

"The dwarf placed his things on a nearby table, then unrolled the measuring tape."

sk "Hold out yar arms."

"Somewhat reluctantly, the human held his arms out from his body. This revealed his member to the dwarf, though it seemed that Skordred wasn't interested in that yet."
"Instead he measured various parts of Rowan's body, such as the length of his arms, legs, and torso, or the circumference of his waist, chest, and shoulders. There were also some more awkward places than others, such a large number of measurements of his ass."
"Having the grey skinned man so close to his nude form was rather disconcerting for the hero. Even still clothed, there was a very strong sensation of heat coming off of the dwarf, his body no doubt tended to stay at a higher temperature than humans did."
"Those hot rough hands crawling over his body was unsettling, making the situation more intimidating than the smaller man would normally seem. Especially considering the difficulty Skordred sometimes had in reaching what he was meaning to measure."
"All the physical information about the subject, Rowan, was recorded in the notebook. All save those needed of his sex."

scene cg267 with fade
show rowan necklace naked behind cg267
show skordred neutral behind cg267
pause 3

sk "Still not hard I see."

ro "Yeah, I was thinking that- eh?!"

"The dwarf surpised Rowan by starting to move even closer to his crotch."

menu:
    "Allow him to continue.":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        jump skordredBJ

    "Stop the dwarf.":
        $ released_fix_rollback()
        "Uncomfortable with what he was doing, Rowan made it very clear that he wanted Skordred to back off."
        sk "Fine, get hard by yerself then, but hurry it up."
        "Rowan sheepishly stoked his cock until it stood erect, and the sculptor made all the necessary notes and measurements, before sending a perplexed Rowan on his way."
        return

label skordredBJ:

$ skordred_bj = True

scene cg268 with fade
show rowan necklace naked behind cg268
show skordred neutral behind cg268
pause 3

"Without bothering to wait for Rowan to finish, the dwarf opened his mouth wide and promptly put it around the man's shaft!"

ro "What are you doing?"

"Skodred didn't answer, he just started blowing his subject. Right away Rowan noted the strange sensation of the dwarf's beard pressed against his crotch, then at the rising pleasure from the somewhat blunt methods employed on his shaft."
"There was no finesse, just a practical attempt to get him hard as fast as possible. Starting with several fast tongue licks on an engulfed shaft, switching into a rapid head bob as soon as there was enough firmness to allow it."
"After about half a minute, the dwarf popped back off of Rowan and considered his length. Apparently unsatisfied, he once again dropped his head back down and bobbed again several times. Skodred even took it on himself to deepthroat him, twice."

#CG variation with Rowan's cock erect and a line of spit going from it to Skordred's mouth
scene cg269 with fade
show skordred neutral behind cg269
pause 3

"The taller man groaned in pleasure, then in confusion as the shorter one pulled all the way off again."

sk "Good. Ya have a respectable size for a champion of chaos."

#first CG again, with Rowan erect variation.
scene black with fade
show rowan necklace naked behind black
show skordred neutral behind black

"He once again extracted his tape measure, then took detailed dimensions of both Rowan's cock and his balls, cupping those orbs in his hot hands for what felt like slightly too long during the process."

sk "Naw I need a pose. Try putting one leg up on that stool and mime pointing your sword forward in challenge."

"Feeling a bit put off from having been brought to the edge, but not pushed over, Rowan tried doing as he was instructed."

sk "Nah, nah, bring your arm higher!"

ro "But that position would leave me open to a surprise attack."

sk "Doesn matter, the important part is the power of the pose. Try putting both feet on the ground with your sword arm down... hey! You're getting soft!"

#CG of Skordred over Rowan's cock again.
scene cg268 with fade
show rowan necklace naked behind cg268
show skordred neutral behind cg268
pause 3

"The dwarf rushed forward and dropped his head back down on Rowan's shaft, bringing him back to the edge again."

#CG of cock with spit coming off.
scene cg269 with fade
show skordred neutral behind cg269
pause 3

sk "Try thinking of our masters, maybe that will keep you hard long enough to finish this."

#Transition to same image.
scene cg269 with fade
pause 3

"Sometime later, and after several more edging blowjobs, Skordred finally settled on a pose he liked. Rowan felt both relieved and incredibly frustrated as the constant edging had made his balls start to feel rather sore."

#CG of Skordred over Rowan's cock again.
scene cg268 with fade
pause 3

"The dwarf seemed to sense something like this, so he dropped his head again and deep throated his subject again, burying his thick nose into the bush above the shaft as well as his beard onto the man's balls."
"Finally, the peak of orgasm coming and Rowan was fairly sure he wasn't going to be forced to endure without any longer. Skordred's mouth and throat, hot and wet, rippled around him as thick grey fingers once again cupped and fondled his nuts."
"The man grunted, felt his insides clench, then poured his seed down the dark dwarf's throat in a well needed release. The last hour's work had not made this experience more pleasurable than normal, in fact it did the opposite, but it was incredibly relieving to finally cum."

#CG of Skordred off of Rowan's soft cock with some cum in his beard.
scene cg268 with sshake
scene cg268 with sshake
scene cg270 with flash 
pause 3

"When the last of Rowan's spurts ended, the dwarf let the man's softening shaft slip free of his maw. He looked at that member for several moments silently and face unreadable. Rowan did notice at least one drop of his cum running over the dark one's beard."

#CG of Skordred sketching Rowan's face.  Both are sitting on stools, Rowan is still naked, his face is flush and he's sweating.
scene cg312 with fade
show rowan necklace naked behind cg312
show skordred neutral behind cg312
pause 3

"Abruptly Skordred straightened and grabbed the sketchpad. He directed Rowan to take a seat, then took the other one."

sk "The last thing I need is a sketch of yar face with the proper expression."

ro "Ah, what would that be?"

sk "The one ya were doing for the pose!"

ro "Oh, right. Do you mind if I get dressed for this?"

sk "I won be long, stay where y'are."

ro "Hmm, fine."

scene bg20 with fade
show rowan necklace neutral at midleft with dissolve
show skordred neutral at cliohnaright with dissolve

sk "That'll be all. Ya may leave."

ro "Right, I guess I'll check in when you finish."

sk "That may take some time, I still need to get the right stone to carve after all. However your part is now done."

ro "I see. Farewell Skordred."

"The dwarf declined to say goodbye."

hide rowan with moveoutleft

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

ro "(Well that just happened.  Who'd have thought that before even giving the courtesy of a hello or goodbye, he'd give me a blowjob?)"
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label cliohna_s_hero_studies:
#Cliohna's hero studies
#Req: After week 6, high priority after week 14

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

ro "You wanted to see me, Cliohna?"

cl "Yes, you are quite a remarkable individual. I find it hard to believe that you haven't accomplished all that you did without some magical assistance."

ro "I've been tested for-"

cl "I know. I wish to check for myself, quite thoroughly."
cl "To that end, I require your seed, freshly extracted. Preferably by my hand, but if you are not willing to let me touch you I will accept the result of self pleasure."

show rowan necklace shock at midleft with dissolve

ro "Wait, are you asking me for my cum?"

"The woman nodded."

ro "And you're going to give me a handjob to get it?"

"She nodded again."

ro "And there's no hidden cost to this or anything like that?"

#cliohna smile
cl "Nothing that will last. I may get some pleasure for myself once you're finished, but you need not fear my influence lasting past the hour."

show cliohna neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve

cl "At least so long as you do not attempt to leave this room without providing me with your seed to test for magical potential. Just so we're clear, the only choice you have to make is how I will get what I desire."

#rowan wry
ro "(Wonderful, I just love it when powerful magic users dictate what I'm allowed to do.)"

menu:
    "Receive a handjob and whatever else Cliohna has in mind.":
        $ cliohnaHJ = True
        $ released_fix_rollback()
        jump .cliohnaHJ

    "Masturbate to get the cum she wants.":
        $ released_fix_rollback()
        ro "I'll just get your seed behind that bookcase, is that fine?"
        "The woman sighs, clearly somewhat disappointed but only motions towards a flask on a nearby table."
        cl "That will do. If you would be so kind, please put it in there."
        "The hero nodded and took the flask."
        hide rowan with moveoutleft
        scene black with fade
        show bg12 with fade
        show cliohna neutral at cliohnaright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        "A couple minutes later he returned and handed the flask to Cliohna. She looked at its contents for a moment, then nodded and waved a hand dismissively to Rowan."
        cl "You may leave now."
        "Knowing it was best not to push or comment on things any further, he simply left while wondering if anything would come of this."
        return

label .cliohnaHJ:

ro "Do whatever you want, I'll bear through it."

#cliohna smile
"The witch actually smiled at this! She seemed almost pleasantly surprised at his choice."

cl "Wonderful. Kindly extract your male sex from your garments, I will get to work at once."

scene cg186 with fade
#cliohna smile
show cliohna neutral behind cg186
pause 3

"The witch wasted no time in grabbing ahold of his shaft the instant he'd taken it out, her long smooth digits soon getting him to full hardness."
"The telltale tingle of magic sent a small jolt through Rowan's body and he could feel himself relaxing immediately afterwards."
"Instincts honed from years of practise took over, pushing against Cliohna's influence over the man's mind. Instead of growing more pliant as she stroked his shaft, Rowan's posture stiffened and he grew more alert under her touch."

cl "Hmm, you're surprisingly resilient to magical influence. I wonder what will happen if I bring things up to a higher level?"

"Suddenly it felt like a mountain was pushing him down. For a moment the man was able to hold out, but the sensation of soft cool fingers gliding over his cock with increasing speed soon knocked a hole in his defenses and swept him under the wave of magic."
"It was against the undirected assault on an army trying to break its morale or an enemy spellcaster trying to confuse or frighten that the veteran soldier had learned to resist, not the focused efforts of an undistracted sorceror of Cliohna's caliber."
"Rowan felt dazed. He couldn't help but relax under the witch's grip and enjoy the sensation of her stroking his shaft. Up and down, smooth and enjoyable. A groan of pleasure escaped his lips."

cl "Even with my full weight behind it you managed to hold back for an instant. There can be no question that there is something special about you, hero of men."

"She continued to muse out loud above him, but Rowan hardly paid any attention. No commands had been given, so he simply waited and enjoyed her ministrations on him. Stroke by stroke, fingers continuing to bring him closer and closer."

"With a wave of her free hand, a small flask sitting on the nearby table floated over to Cliohna, which she pressed against the head of Rowan's cock in preperation to collect his seed. At the same time, a new sensation spread through him. Some other magic?"

cl "Now cum for me, Rowan. If you would be so kind."

scene cg186 with sshake
show cg186 with sshake
show cg187 with flash
#cliohna smile
show cliohna neutral behind cg187
pause 3

"An order had been received, the man would obey. Instantly he reached his peak and leaned backwards slightly as ropes of cum sprayed out into the waiting flask. He spurted a couple more times, then once again resumed his relaxed pose, waiting for another command."

cl "Very good. Seems to be about a normal orgasm for a human man, though that was as expected."

scene black with fade
show cliohna neutral behind black

"The witch replaced the flask on the table in some sort of apparatus, then pulled Rowan in front of her at the table. She pushed down on his head, directing him to kneel on the ground, leaving his head at the height of her groin."
"There was a soft click as the band of strange material covering Cliohna's womanly parts fell to the side. Whether by the act of stroking him or controlling him, it seemed that the witch had grown aroused as moisture glistened on her parted folds."

cl "Use your tongue to pleasure me while I work on your seed."

"Rowan hesitated for an instant, the desire to do as he was told clashing with a part of his mind that was struggling to regain control."

cl "Now."

scene cg80 with fade
show cliohna neutral behind cg80
pause 3

"A blast of magic against his mind forced the man back into compliance and he opened his mouth to lick the lips of Cliohna's labia."

cl "Ghmm, you're just full of surprises. Perhaps you'll be able to give me one more?"

"As he'd been instructed, Rowan licked and licked. He traced up and down the sides of her sex, then plunged into its depths. Drinking deeply of her fluids and coaxing more of them forth with each motion."
"Rowan continued to eat the woman out, but with each passing moment he felt his faculties grow more and more under his own control again. However he did not slow in his efforts to please the woman who'd dominated him, hiding his ability to throw her influence off."
"Cliohna was powerful, yes. Very powerful and very experienced, though not terribly skilled at controlling others. She relied on brute force to charm through magic, which allowed the man to break free shortly after her concentration was broken."
"With a small shock, Rowan realized that he'd probably broken free from her control due to his ministrations on her womanhood. The normally calm and disdainful witch was breathing heavily and occasionally shuddering as his tongue brought her closer and closer to orgasm."

cl "Deeper, deeper, yes! Just like that!"

"A final tremor rushed through her body and the witch let out a soft moan, her first of the experience. Cliohna's passage rippled and squeezed in time with her peak, which was soon followed by a final stream of fluids."

cl "Good, stop. You may come up now."

"The witch wiped her hand over her sex, brushing away some stray drops and then refastened her thong."

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

"Shortly afterwards Rowan emerged from under the table as well, straightening up and looking at the woman he'd just eaten out. The two studied one another for a moment before Cliohna broke the silence."

cl "You've thrown off my control, haven't you?"

show rowan necklace happy at midleft with dissolve

"Arms spread wide and a shrug of the shoulders was the hero's response."

cl "Interesting. We shall see if that's an indication of hidden talent. You may leave now."

"Knowing it was best not to push or comment on things any further, he simply left while wondering if anything would come of this."
return
