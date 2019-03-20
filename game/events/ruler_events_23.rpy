init python:

    event('rowan_picnic', triggers="week_end", conditions=('goal2_completed', "all_actors['alexia'].relation > 50"), group='ruler_event', run_count=1, priority=pr_ruler)
    event('a_visit_to_Cliohna', triggers="week_end", conditions=('cliohnaHJ',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('alexia_and_the_rude_workers', triggers="week_end", conditions=('week >= 42',), group='ruler_event', run_count=1, priority=pr_ruler_high)
    event('helaynas_help', triggers="week_end", conditions=('week > 42', 'helayna_escape_method == "no escape"',), group='ruler_event', run_count=1, priority=pr_ruler)
    



label alexia_and_the_rude_workers:

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve

"In just a few more hours, the sun would set, and Rowan would return to Castle Bloodmeen once again."

if alexiaWulump == True or helAlexiaWhip == True:
    "She used to eagerly await his arrival. Used to count every hour, yearning - yearning so much! - to see his face, hear his voice."
    "But now… After everything that happened after Lady Helayna’s escape…"

    show alexia 2 necklace angry at midleft with dissolve

    if alexiaWulump == True:
        "After he allowed Andras to turn her into a tentacle fuck toy..."
        
    else:
        "After he mercilessly whipped her in front of everyone…"
        
    show alexia 2 necklace concerned at midleft with dissolve
    "… Was this still the same man she married all these years ago? This kind, courageous man, who did everything in his power to make things right?"
    
    al "(Oh Rowan…)"

    "… She didn’t know what would become of them."
    "She didn’t know if their marriage will hold in these turbulent times. If it can somehow endure this growing divide between them."

    if all_actors['alexia'].flags['andras_influence'] > 4 or all_actors['alexia'].flags['jezera_influence'] > 4:
        "And worse of all…"
        "She didn’t know if she even wanted it to endure..."
    else:
        pass
        
else:
    "For over half a year now, she’s been counting every day, every hour, every minute sometimes, looking forward to the moment when Rowan would step through the portal, and return to castle Bloodmeen."
    "… And return to her, if only briefly. With everything the twins expected of him, the two of them could rarely scrape more than a few hours together."
    "To see her marriage reduced to this…"

    if raeve_keep_rowan_claimed_helayna:
        show alexia 2 necklace angry at midleft with dissolve
        "With her husband sharing his room with a woman other than her."
        show alexia 2 necklace concerned at midleft with dissolve
        "How could she not despair?"
        al "(Oh Rowan…)"
        
    else:
        "How could she not despair?"
        
show alexia 2 necklace neutral at midleft with dissolve

"She sighed to herself, and tried – as always, failing to – to banish the dark thoughts that plagued her."

if all_actors['alexia'].job_state.job == None:
    "She really wished Rowan would let her work, as she requested earlier. All that free time on her hands did nothing to put her mind at ease."
    "With nothing better to do, she usually ended up browsing the various books at the library, or - just as she was doing right now - wandering the castle, with no goal or destination in mind."

else:
    "At least now she had something to occupy herself with. But with her job done for the week, and with no plans until Rowan got to the castle, she took the time to wander through its halls, without a particular destination in mind."

"A dangerous past-time, mayhap given how one never knew what the many, destroyed rooms and tunnels of Castle Bloodmeen hid from the world."

#tunnels
scene black with fade
show alexia 2 necklace shocked at midleft with dissolve

larry "-like big, round pillows!"

omar "Man, if I could just stick my dick-"

"It was from one of the said ruined tunnels, that Alexia heard a pair of unfamiliar voices."

show alexia 2 necklace neutral at midleft with dissolve

"Odd. Could these belong to Skordred’s workers, taking a break? Judging from the faint, but unmistakably drunken, laughter, it seemed unlikely."
"Skordred wasn’t one to let his workers drink on the job, but she hadn’t seen him for the last few days… Maybe he was taking care of something away from the castle?"

hide alexia with moveoutright

"Curiosity got the better of her, and she ended up heading into the ruined tunnels, following the lively discussion that took place."

scene black with fade
show alexia 2 necklace neutral behind black

"Discussion that, as she learned, revolved around Cla-Min’s rather… Rich attributes."

al "(Goodness gracious…)"

#tunnels
scene black with fade

larry "And that blonde stripper chick. Man, I’d tap that sweet ass so hard."

show alexia 2 necklace neutral at edgeleft with moveinleft

omar "What, the sorceress?"

larry "Fuck no, that bitch is ice cold. The elf, Omar, the elf!"

show alexia 2 necklace neutral at midleft with moveinleft

"She eventually stumbled upon the two workers, who remained oblivious to her presence. They appeared to be relatively young. One was light skinned, with short, blond hair, likely from Rosaria."
"The other was dark skinned and spoke with a thick Qerazel accent. He was currently drinking from a bottle half full, and Alexia could bet the clear liquid was not water."

$ omarName = "Omar"
$ larryName = "Larry"

omar "They’re both elves Larry! And you don’t stand a chance with either. Everybody knows misses “high and mighty pointy ears” don’t mingle with us, flat eared mortals."

show alexia 2 necklace concerned at midleft with dissolve

larry "Then you’re out of luck sir, but I, I’d like to remind you, am part elf."

omar "For the last time, your grandfather was not an elf!"

larry "He was! How else will you explain my magical abilities!"
larry "With the help of a simple potion, I can enter a deep, meditative trance, for 12 hours straight! Just like an elf!"

show alexia 2 necklace happy at midleft with dissolve

omar "For the last time Larry, {i}vodka{/i} is {i}not{/i} a magical potion!"

larry "It’s a base for all alchemical potions, so yes it is!"

"Shaking her head in disapproval, Alexia took the opportunity to step forth, revealing herself to the two workers."

show alexia 2 necklace neutral at center with moveinleft 

al "Excuse me, but… What are you two doing?"

"In an instant, the jovial, lighthearted atmosphere disappeared without a trace. The two men turned their attention to her, an unpleasant look in their eyes."

show alexia 2 necklace concerned at center with dissolve

larry "And what does it look like we’re doing, you airhead?"
larry "We’re taking a well-earned break."

show alexia 2 necklace neutral at center with dissolve

al "I can see that. But I don’t think you’re allowed to drink during breaks."

show alexia 2 necklace shocked at center with dissolve

omar "Then you shouldn’t be doing much thinking, slut, because you’re not very good at it."

larry "Rude."

show alexia 2 necklace angry at center with dissolve

omar "Yeah, she is."

al "What did you just-"

"The Rosarian man cut her off, unconcerned with her protests."

larry "Hey, is she one of Mistress Jezera's maids? I don’t think I saw her earlier."

omar "I don’t know man. But in this fucking castle, the women are either maids, whores or slaves."

show alexia 2 necklace shocked at center with dissolve

omar "Hey slut, which one is it?! Do you eat pussy, suck dick, or suck dick for money?"

show alexia 2 necklace angry at center with dissolve

larry "Does that really narrow it down?"

omar "I dunno."

"Fuming with anger, Alexia took a deep breath, and narrowed her eyes ever so slightly at the two men."
"This wasn’t the first time she’s been dealing with impolite drunks, but these two were slowly moving to the top her of “most infuriating assholes” list."

al "... You must be new around here."

larry "Hey, she has spunk."

omar "She’d be better guzzling on spunk."

larry "Preach, man."

al "Unbelievable."

show alexia 2 necklace neutral at center with dissolve

al "I simply must ask. Are you two even aware what castle are you in?"

"Omar simply sneered at her, but Larry was kind enough to offer a response, after rolling his eyes very ostentatiously."

larry "Castle Bloodmeen, obviously."

al "And do you happen to be aware who exactly is ruling this castle?"

larry "Ah, I see what you’re getting at!"
larry "Granted, Mistress Jezera and Master Andras are plenty scary, but…"

"He tossed the almost empty bottle to his friend."

omar "Everybody knows it’s this Rowan guy who’s running things."

show alexia 2 necklace angry at center with dissolve

larry "And everybody also knows he’s a massive pussy, so we can do whatever the fuck we want! Isn’t that great?"

show alexia 2 necklace shocked at center with dissolve

omar  "I heard he’s letting Andras fuck his wife."

if alexiaSeparateRoom == False:
    larry "Do you think they’re using his bed while he’s away?"
    omar "Obviously."
    
else:
    larry "Obviously! Why else would she sleep in her own room?"
    
if alexiaAndrasSex > 0:
    "Alexia turned red in embarrassment, humiliated beyond imagination. Did the staff really gossip about her and Andras?"
    
else:
    "Alexia turned red in anger. To think the staff would spread such filthy, slanderous allegations!"
    
"Larry turned to her with a shit-eating grin on his face, still unaware of who he was talking to."

larry "So as long as Skordred ain’t around, we can laze around all day, and Rowan will get all the blame anyway. Best fucking job we ever had."

omar "By far."

larry "Yeah, yeah."
larry "Hey Omar, do you think Master Andras shares his wife around?"

omar "Rowan’s? Probably. I don’t think I’d use her, though."

larry "Yeah, I bet that bitch is all loose by now."

if greyhideMet == True:

    larry "Who else do you think she fucks?"
    omar "The minotaur?"
    larry "No way, have you seen a minotaur’s dick? That thing would split her apart."
    omar "Shit, that bad?"
    omar "Hold on- How would I know how big a minotaur dick is?"
    omar "How would YOU know how big it is?!"
    larry "I m-mean, it’s just common knowledge-!"
    omar "How is this- Oh Solansia’s tits, the cheese festival!"
    
else:
    pass
    
show alexia 2 necklace angry at center with dissolve

"The conversation continued, but Alexia couldn’t follow it anymore. Their voices were drowned out by all the blood currently rushing to her head."

if helAlexiaWhip:
    "Never before, in her entire life – barring the time Rowan punished her on the castle courtyard – had she been so humiliated. Straight to her face even!"
    
elif raeve_keep_rowan_claimed_helayna:
    "Never before – barring her husband fucking Helayna – Had she been so humiliated. Straight to her face even!"
    
else:
    "Never before had she been so humiliated. Straight to her face even!"

"She couldn’t get herself together. She didn’t know if she should break into tears, scream in frustration, or just slap both of them, preferably with a steel gauntlet."

show alexia 2 necklace happy at center with dissolve
pause 1
hide alexia with moveoutleft

"So instead, she defaulted to her usual behavior – letting somebody else deal with the issue."

scene bg14 with fade
show alexia 2 necklace happy at center with dissolve

"Skordred wasn’t around, and these two were slacking off. Drinking on the job, even! Somebody had to do something!"
"It had nothing to do with them being insulting, rude assholes!"
"No, she was just keeping the castle running! That’s right!"
"Now…"

show alexia 2 necklace neutral at center with dissolve

if alexiaWulump == True or helAlexiaWhip == True:
    jump informJezeraNow
    
else:
    "While she had no doubt Rowan would simply love to hear all about this, he would not return to Castle Bloodmeen in several more hours. Perhaps…"
    menu:
        "Inform Jezera now.":
            $ released_fix_rollback()
            jump informJezeraNow
            
        "Tell Rowan everything in the evening.":
            $ released_fix_rollback()
            jump tellRowanEvening

label informJezeraNow:

"… She did see Mistress Jezera earlier today, so she was certainly somewhere in the castle."
"And she would not take kindly to Skordred's workers drinking on the job. She was certain she would resolve the matter…"

show alexia 2 necklace happy at center with dissolve

"To her satisfaction."

hide alexia with moveoutright
scene black with fade

"......…"
"...…"
"…"

$ change_corruption_actor('alexia', 3)
$ all_actors['alexia'].flags['jezera_influence'] += 3
$ change_relation('alexia', -5)
jump rudeJezeraBranch

label tellRowanEvening:

al "(Hmph, better not involve Jezera unless I have to.)"

"Besides, she was certain Rowan would just love to know what the staff was saying about the two of them. This would be a nice opportunity to instill some discipline in these people."

show alexia 2 necklace happy at center with dissolve

"But she just couldn’t wait…"

hide alexia with moveoutright
scene black with fade

"......…"
"...…"
"…"

$ change_relation('alexia', 5)
jump rudeRowanBranch


label rudeJezeraBranch:

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve
show jezera happy behind bg14

je "Ah, there you are."

hide jezera
show jezera happy at midright with moveinright

al "Mistress Jezera?"

je "I was looking for you. I wanted to thank you for your very… Detailed report on everything you were witness to earlier this day."

show alexia 2 necklace concerned at midleft with dissolve

"After the events at the tunnel, she ended up finding Mistress Jezera quite quickly. Blind with rage, for better or for worse, she ended up telling the demoness everything, not holding her tongue at all."
"Which she was slowly starting to regret. Now that her anger subsided, she was starting to realize what fate did she'd bring to the two young men."
"Yes, they were rude and foolish, but so were many their age, before life wizened them up. Today’s event would no doubt lead to a valuable lesson they would carry for life… If Jezera did not see fit to end that life early."

scene bg18 with fade
#jez angry
show jezera displeased at center with dissolve

"And judging from the dark look the demoness wore the last time Alexia saw her…"

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

al "Yes… About that..."

show jezera happy at center with moveinright

"But the demoness would not let her finish."

je "A-a-a! Don’t say anything, just follow me for now."

hide jezera with moveoutleft

"… She didn’t like where this was going, but she couldn’t oppose Jezera."

hide alexia with moveoutleft

"Meekly, she followed after her, in the direction of the castle dungeons."

scene bg8 with fade
show jezera happy at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

je "You know me Alexia. I like to run a tight ship. I like it when the Castle works like a dwarven clock."

show jezera displeased at midleft with dissolve

je "It isn’t often somebody fails me. At least not as glaringly as these two did today."

show jezera happy at midleft with dissolve

je "But I’m almost thankful for it."

show jezera neutral at midleft with dissolve

je "You see, normally I’d be all for settling for my usual routine-"

show jezera happy at midleft with dissolve

je "I’ll spare you the details -"

show jezera displeased at midleft with dissolve

je "But when you told me about all the things they said about you..."

show jezera happy at midleft with dissolve

je "I thought that perhaps a lesson would be prudent."
je "The first one was properly apologetic. The other…"

show jezera neutral at midleft with dissolve

je "Not so."

show jezera neutral at edgeright with moveoutright

"They finally reached the cell Jezera was leading them to. The castle mistress put a finger to her mouth, then pointed to the inside of it."

show alexia 2 necklace shocked at edgeleft with dissolve

"In the half-dark of the dungeon cell, Alexia saw the man she recalled was called Omar. Blindfolded and chained to the wall, he was stripped from the waist up – but Alexia saw no marks from torture on his skin."

show alexia 2 necklace neutral at edgeleft with dissolve

"It was surprising, to say the least. The last person she saw leave the Bloodmeen dungeons was her husband, and despite the twin’s quite tame treatment of him, his body was still plenty bruised. Omar didn’t have as much as a cut on him yet."

show jezera happy at edgeright with dissolve

"Alexia turned her eyes to the demoness, confused, but mindful of the earlier order to stay silent. Jezera flashed her another predatory grin, then took the dungeon keyring out. Soon all would be clear."

je "Ooooooh Ooooomaaaaar!"

"The demoness ostentatiously jiggled the cell keys, causing the man to perk up in an instant."

omar "M-mistress Jezera, is that y-you?!"

"Despite the lack of visible scars, Alexia noticed the man lost all of his earlier nonchalance. His voice was raspy, and he kept jerking his head, yanking the chains that held his wrists."

show alexia 2 necklace concerned at edgeleft with dissolve

"Alexia guessed it did not require physical torture to break a man."

show alexia 2 necklace shocked at edgeleft with dissolve

omar "Did- Did you find that red-haired bitch? D-did she confess?"

je "I did. And she did."

"Again, Jezera signaled for her to be silent, but Alexia was too shocked to speak up anyway. Did he really…?"

je "You were right. About everything."

"The demoness opened the cell door, and approached the man. Gently, she placed her hand on his face, and caressed it soothingly."

je "Just as you said, she was lying about you and Larry drinking."

show alexia 2 necklace angry at edgeleft with dissolve

je "She confessed she was jealous you spurned her advances, and that she made the whole thing up to spite you."

"Surprised shock passed through the man’s face, but he quickly switched it to a smug expression of victory. He tried to be suave, but neither of the women missed him slipping in his act."
"Jezera was clearly having the time of her life, but Alexia…"
"Felt her blood boil again."

omar "O-of course!"
omar "Dumb bitch thought she could get away with it!"
omar "But nothing escapes your eyes, Mistress Jezera!"

je " Hmmmm, it’s true, I do think myself quite perceptive."

"A devious smirk crept on Jezera’s lips, and she turned her head around. She answered him, but Alexia knew it was her she was addressing."

show alexia 2 necklace neutral at edgeleft with dissolve

je "But now I’m at a loss…"
je "What should I do with this dishonest little rat?"

show alexia 2 necklace shocked at edgeleft with dissolve

omar "You should throw her to the orcs!"

show alexia 2 necklace angry at edgeleft with dissolve

omar "Have them rape the dumb bitch. That will teach her a lesson!"
omar "A-and cut her tongue out, so she doesn’t tell any more lies!"

je "Ooooooh, should I also cut her hands and feet? Turn her limbs into cute little stumps?"

omar "Y-yes!"
omar "Reduce her to a crippled cumbucket for the orcs!"
omar "Lying- Spreading lies about your l-loyal servants! I can’t – You can’t let people show such disrespect to you, Mistress Jezera!"

je "My, my. How considerate of you. You really are something."
je "I am so glad Alexia allowed me to meet you."

show alexia 2 necklace shocked at edgeleft with dissolve

"Jezera chuckled to herself, and snapped her fingers. A gag appeared in the man’s mouth, straight out of thin air."

show alexia 2 necklace neutral at edgeleft with dissolve

je "And while I could listen to this all day, I think it’s time to move this thing along."

"She took his blindfold off. Confused by the sudden appearance of the gag, his eyes ended up darting across the room, trying to figure out what the hell was going on."
"They found Alexia quickly."
"Never before has she seen a man so quickly transition from hopeful elevation, to absolute, crushing despair and terror. A strange sense of euphoria took over her, as the man who so casually belittled and insulted her, now froze in dread at the sight of her."

show alexia 2 necklace happy at edgeleft with dissolve

"It might have been wrong, but she couldn’t help but smile a little, as she saw him start to flail in his bondage, screaming into the gag. Normally, she would find the sight disconcerting, but now…"

show alexia 2 necklace happy at midright with moveoutright

je "Oh, Alexia, my sweet, pure Alexia."

"The demoness moved behind her, wrapping a single hand around her, in a friendly gesture."

je "I noticed your expression earlier, before we came here."

"She leaned in, whispering in Alexia’s ear."

je "You felt sorry for them, didn’t you? For what you thought I would do to them."

show alexia 2 necklace happy at center with moveoutleft

"The demoness pushed her gently into the cell. Eyes still fixated on the trashing man, as if spellbound, Alexia did not resist."

hide jezera with moveoutleft

show jezera happy behind bg8

je "But you should know by now…"

hide jezera

show jezera happy at center with moveinleft
show jezera happy at midleft with moveoutleft

je "Some people do not deserve your compassion."

"Alexia felt something being placed in her hand. A handle of sort."

je "They deserve…"

"She looked down -"

je "Something else."

"And saw a whip."

menu:
    "...":
        $ released_fix_rollback()
        "The whip felt cold, but as it touched her fingers, a warm feeling spread up her hand. It carried with it promises of things to come, of delights yet unknown to her."
        "Of pleasures far darker, far more violent anything she ever tried."
        "She saw it unfurl, watched, with unhealthy fascination, as it reached the ground. Her breath grew heavy, her heart beat faster."
        "No, it already beating faster earlier – it was now hammering in her chest. She just didn’t notice, with all the deafening sound of blood rushing through her head."
        je "He called you a slut."
        "Jezera’s grabbed her shoulders gently, and leaned in to whisper in her ear. Her soft breath somehow pierced through Alexia’s growing bloodlust, tickling her skin."
        je "He lied about everything, and would see you crippled, maimed and raped day and night, just so he could escape punishment."
        show jezera happy at edgeleft with moveoutleft
        je "And he’s not even sorry about it. Not yet."
        je "{b}Make him{/b}."
        "Her words spread like fire through her body. All her anger, all her fury, rose to the top, swallowing her whole. Until now, had it all laid just beneath the surface, or did Jezera do something to awaken it?"
        "She didn’t know, and now… She no longer cared."
        show bg8 with smallshake
        show bg8 with redflash
        "Her hand shot forward, and the whip struck the man’s chest. A muffled scream escaped his lips, and his body arched in agony."
        if helAlexiaWhip:
            "She knew how he felt, but she felt no sympathy for him. This worm deserved none of it."
        elif alexiaWhippedRowan:
            "So different was his reaction to Rowan’s. But what she did back then was out of love, and this… Carried with itself a different feeling."
        else:
            "Did it really hurt so much? She hoped so. He deserved everything that was coming for him."
        "Her hand moved again, making the whip slash the air and strike Omar’s flesh, drawing blood. The unmistakable scent of iron reached her nose, and a strange thrill came over her. More. She had to punish him more!"
        
        $ tempRound = 0
        $ tempBlame = 0
        $ tempWhip = 0
        $ tempRest = 0
        
        if rowanBlameAlexia:
            $ tempBlame += 1
            
        else:
            pass
        
        show alexia 2 necklace angry at center with dissolve
        jump alexiaWhipMenu

    
    "Throw it away, quickly.":
        $ released_fix_rollback()
        "The whip felt cold, but as it touched her fingers, a warm feeling spread up her hand. It carried with it promises of things to come, of delights yet unknown to her."
        "Of pleasures far darker, far more violent anything she ever tried."
        show alexia 2 necklace shocked at center with dissolve
        show alexia 2 necklace shocked at edgeleft with moveoutleft
        #jez angry
        show jezera displeased at midleft with dissolve
        "Struck with panic, she threw the thing away from her as far as she could."
        al "What- What was this- What were you-"
        show jezera happy at midleft with dissolve
        je "Oh, I was just thinking-"
        #jez angry
        show jezera displeased at midleft with dissolve
        al "No, this-"
        al "This isn’t-"
        al "I have to go."
        hide alexia with moveoutleft
        "Her entire body shaking, Alexia threw herself at the cell door. She felt Jezera’s glare on her back, watching her go."
        "Whatever plans the demoness had for her and Omar, she wanted no part in them."
        $ change_corruption_actor('alexia', -3)
        $ all_actors['alexia'].flags['jezera_influence'] -= 3
        return

    
label alexiaWhipMenu:

$ tempRound = tempWhip + tempRest

if tempWhip == 1:
    "Omar squirmed in his bondage, desperately trying to avoid the incoming blows."
    "To no avail."
    
elif tempWhip == 2:
    "Muffled screams left his mouth, as the gag prevented Omar from crying out. No matter."
    "His panicked eyes told her everything she needed to know."

elif tempWhip == 3:
    "The man shook his head desperately, hoping to dissuade her from striking again. But why should she hold back?"
    "He deserved everything coming his way, no matter the reason for it."

elif tempWhip == 4:
    "Strike after strike, new marks decorated his body, a tapestry of blood her bruiser."
    "More, she wanted to see it grow more!"

elif tempWhip == 5:
    "His muffled screams grew weaker, his desperate moves slower."
    "Good, he was easier to hit this way."

elif tempWhip == 6:
    "Tears ran down Omar’s face, but Alexia paid no attention to them."

elif tempWhip == 7:
    "The man no longer screamed, no longer dodged. His head hanged low, as strength escaped his body."

elif tempWhip > 7:
    "Hanging by the chains on his wrists, the man could only twitch in agony as her whip kept striking his body."

else:
    pass
    

menu:
    "Punish him for lying.":
        $ released_fix_rollback()
        $ tempWhip += 1
        show bg8 with smallshake
        show bg8 with redflash
        al "Lying… Bastard!"
        "Her entire body tingled as she felt the whip find its target, two new marks appearing over his chest."
        "He could’ve avoided this. He could’ve come clean. Maybe then Jezera would show him mercy."
        "But he chose to lie…"
        "And now Alexia would show him none."
        jump alexiaWhipMenu
        
    "Punish him for endangering her husband and herself.":
        $ released_fix_rollback()
        $ tempWhip += 1
        show bg8 with smallshake
        show bg8 with redflash
        al "Selfish… Bum!"
        "With every hateful, venom dripping word, the whip would strike his body. Alexia watched with growing smile as the marks increased in numbers."
        "He could’ve just done his job. But no, he’d rather she and Rowan suffered for his laziness!"
        "And now he was paying the price."
        jump alexiaWhipMenu
                                         
    "Punish him for calling her a slut.":
        $ released_fix_rollback()
        $ tempWhip += 1
        show bg8 with smallshake
        show bg8 with redflash
        "Her whip whizzed through the air, striking true. Omar left another muffled scream. It was almost a shame she couldn’t hear him cry out."
        "“Slut”. “Whore”. “Bitch”. Such vile words. She had better for him."
        show bg8 with smallshake
        show bg8 with redflash
        al "Pig! … Dickless… Ape!"
        "And each carried with itself another strike of her whip."
        jump alexiaWhipMenu
        
    "Punish him for Cla-Min trying to steal her husband away from her." if tempBlame < 1:
        $ released_fix_rollback()
        $ tempWhip += 1
        "Cla-Min’s cocky grin flashed before her eyes."
        "“Don't get fussed up if I make a move on your husband, darling.”"
        "The nerve on this woman!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Stupid... Goblin... Slut!"
        "How she wished it was her chained to the wall!"
        jump alexiaWhipMenu
        
    "Punish him for Greyhide taking advantage of her." if alexia_greyhide_sex:
        $ released_fix_rollback()
        $ tempWhip += 1
        "Despite his table manners, she thought he was nice. She really did."
        show bg8 with smallshake
        show bg8 with redflash
        al "Drugged… Grout… My… Ass!"
        "She screamed in frustration, striking the man in front of her without mercy."
        "Nobody in this castle could be trusted. She learned that the hard way."
        jump alexiaWhipMenu

    "Punish him for her husband letting Greyhide fuck him." if (rowan_greyhide_sex > 0 and all_actors['alexia'].relation < 50) or (rowan_greyhide_sex > 0 and tempBlame > 1):
        $ released_fix_rollback()
        $ tempWhip += 1
        $ tempBlame += 1
        "Drugged firegrout! Magic charms!"
        "Just how bloody difficult could it be to stay away from minotaur dick?!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Cheating… Bastard!"
        jump alexiaWhipMenu
        
    "Punish him for Greyhide taking advantage of her husband" if (rowan_greyhide_sex > 0 and all_actors['alexia'].relation > 50) or (rowan_greyhide_sex > 0 and tempBlame > 1):
        $ released_fix_rollback()
        $ tempWhip += 1
        "Drugging her husband… And taking advantage of him! Unbelievable!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Dumb… Cow!"
        "She wished it was Greyhide chained to the wall. But Omar would take the strikes meant for him."
        jump alexiaWhipMenu
        
    "Punish him for her own husband selling her out to the twins." if rowanBlameAlexia:
        $ released_fix_rollback()
        $ tempWhip += 1
        $ tempBlame += 1
        if helAlexiaWhip:
            "“I Forgive you.”"
            "What bullshit!"
            "Tears in her eyes, she wailed on the man. Her own husband - Her own husband! - whipped her, because she decided to save the woman who thought the life of him."
            show bg8 with smallshake
            show bg8 with redflash
            al "Hate… You… Hate... You!"
        else:
            show bg8 with smallshake
            show bg8 with redflash
            al "Fucking… Coward!"
            "Rowan, the hero of Karst, the man who killed the living embodiment of Chaos."
            "Somehow couldn’t find the balls to protect his own wife from the people who owed all their success to him."
            show bg8 with smallshake
            show bg8 with redflash
            al "Spineless… Piece of… Shit!"
            "Tears in her eyes, she wailed on the man, barely seeing where the strikes landed."
        jump alexiaWhipMenu
        
    "Punish him for Andras constantly harassing her.":
        $ released_fix_rollback()
        $ tempWhip += 1
        show bg8 with smallshake
        show bg8 with redflash
        al "Stupid... Demon!"
        "She struck with all her might, drawing blood and another scream. Weak. Weak."
        "She must hit him stronger. Far stronger!"
        "If it was Andras, he wouldn’t be hurt by something like this!"
        jump alexiaWhipMenu
        
    "Punish him for Jezera constantly harassing her on the job." if get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') > 1:
        $ released_fix_rollback()
        $ tempWhip += 1
        "Always touching her… Always groping her-!"
        "Did the demoness have no notion of personal space?!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Hands… Off… Me!"
        "She struck the man, almost feeling Jezera’s perfume still near her."
        jump alexiaWhipMenu
        
    "Punish him for her husband fucking Helayna." if raeve_keep_rowan_claimed_helayna:
        $ released_fix_rollback()
        $ tempWhip += 1
        $ tempBlame += 1
        "“Under so much stress”. “I know how you feel”. “I forgive you”."
        "What a joke!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Bastard!"
        "How many more women will her husband fuck to “save” from the twins?!"
        if helayna_escape_method == "rowan" or helayna_escape_method == "no escape":
            $ tempBlame += 1
            "And why did saving them meant keeping them in his bedroom?"
            "He was concerned enough to fuck her, but not concerned enough to help her escape!"
            show bg8 with smallshake
            show bg8 with redflash
            al "Stupid… Hypocrite!"
        else:
            "And how come they are saved before she is?!"
            show bg8 with smallshake
            show bg8 with redflash
            al "Should’ve... Been... Me!"
            
        jump alexiaWhipMenu
        
    "Punish him for her husband fucking his secretary." if alexiaThreesomeStormout:
        $ released_fix_rollback()
        $ tempWhip += 1
        $ tempBlame += 1
        show bg8 with smallshake
        show bg8 with redflash
        "She struck at the man with abandon. He and Larry weren’t the only people who liked Liuriel’s “sweet ass”."
        show bg8 with smallshake
        show bg8 with redflash
        al "Stealing… My… Husband!"
        jump alexiaWhipMenu
        
    "Punish him for her husband servicing the twins the moment he joined them." if (jezeraIntroSex == True and admitIntroSex == True)  or (andrasIntroSex == True and admitIntroSex == True):
        $ released_fix_rollback()
        $ tempWhip += 1
        $ tempBlame += 1
        show bg8 with smallshake
        show bg8 with redflash
        al "Day… One! Day… One!"
        "On day one."
        "… That’s how quickly Rowan tossed their wedding vows aside. The moment he agreed to serve the twins, he no longer saw fit to remain faithful."
        "They wanted to test his loyalty to them…"
        "But what about his loyalty to her?"
        if alexiaOffer:
            $ tempWhip += 1
            $ tempBlame += 1
            "What about her loyalty to him?"
            show bg8 with smallshake
            show bg8 with redflash
            "Sold… Me… Away!"
            if jezeraIntroSex:
                "“Hey honey, I fucked a girl, but it’s okay, you can fuck her brother in return”?!"
            else:
                "Hey honey, I fucked a guy, but it’s okay, you can fuck him too”?!"
            show bg8 with smallshake
            show bg8 with redflash        
            al "Spineless… Asshole!"
        jump alexiaWhipMenu

    "Punish him because she feels powerless.":
        $ released_fix_rollback()
        $ tempWhip += 1
        show bg8 with smallshake
        show bg8 with redflash
        al "How... Does it… Feel…!"
        "Strike after strike, she mangled his half-naked body. Finally, someone who understood how she felt."
        "How it felt to be powerless, worthless, at the mercy of people who couldn’t care less about you. One bad move from her husband, and she ends just as he did – chained to the wall, with no hope in sight."
        "But not this time. This time she held the whip."
        "And she didn’t want to let go of it."
        jump alexiaWhipMenu
        
    "Punish him, because her husband barely pays attention to her anymore." if all_actors['alexia'].relation < 50:
        $ released_fix_rollback()
        $ tempWhip += 1
        $ tempBlame += 1
        show bg8 with smallshake
        show bg8 with redflash
        al "Why… Why?!"
        "Did she really want so much from him? For him to spend some time with her, to take her side every once in a while, to put her, and her only, first, at least from time to time?"
        "Was it too much for her to want her husband to show he still loved her?!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Just… A little…"
        "… She whispered to herself, as her vision went blurry."
        jump alexiaWhipMenu
        
    "Rest her hand for a moment." if tempRound > 2 and tempRest < 3:
        $ released_fix_rollback()
        if tempRest == 0:
            show alexia 2 necklace concerned at center with dissolve
            al "Ah… Ah..."
            "She felt dizzy. She lowered the whip, and steadied herself. She could barely see anything, with red mist over her eyes."
            show alexia 2 necklace neutral at center with dissolve
            "And yet… And yet!"
            show alexia 2 necklace angry at center with dissolve
            "This wasn’t nearly enough punishment!"
        else:
            al "Nnngh!"
            "She grabbed her head in pain. Her entire body ached from exhaustion, and her hand grew heavy as lead."
            "Despite that… She still felt like she needed to continue."
        $ tempRest += 1
        jump alexiaWhipMenu
        
    "Let go off the whip." if tempRest == 2 and tempBlame < 5 and tempWhip < 7:
        $ released_fix_rollback()
        show alexia 2 necklace concerned at center with dissolve
        "The whole room swayed from one side to the other. Or was she the one swaying? She wasn’t certain. Somehow, it was… Difficult to discern what was and what wasn’t."
        "What she knew was real, was the bloodied body in front of her."
        "And the fact she was the one responsible for the man’s state."
        show alexia 2 necklace shocked at center with dissolve
        al "No…."
        al "No!"
        "She tried to throw the whip away, but as the adrenaline left her body, she barely had the strength to unclench her fingers. The whip fell to the dungeon floor, like a harmless toy it wasn’t."
        show jezera displeased at edgeleft with moveinleft
        "She turned around, suddenly aware the demoness never left the room."
        al "You..."
        je "It was..."
        je "Shh..."
        show jezera displeased at center with moveinleft
        show alexia 2 necklace shocked at edgeright with moveoutright
        "Jezera tried to take hold of her, but the woman stumbled back."
        jump whipRunningAway
        
    "Punish him, because it feels good." if tempWhip > 4:
        $ released_fix_rollback()
        $ tempWhip += 3
        show alexia 2 necklace happy at center with dissolve
        show bg8 with smallshake
        show bg8 with redflash
        "How long had she been hitting him? She lost count. And she didn’t care."
        "The thrill was simply too much. The piercing snap of the whip, the muffled screams, the sight of his blood-!"
        show bg8 with smallshake
        show bg8 with redflash
        al "Ha… Ha… Ha- Ha!"
        show bg8 with smallshake
        show bg8 with redflash
        "Her voice broke midway through her half-deranged laugh. It wasn’t like her. She knew it. But at the moment she didn’t care."
        "She just wanted someone to hurt just as she hurt."
        show alexia 2 necklace shocked at center with dissolve
        al "Ha… Ha?"
        "But as a numbing feeling set of her arm, and as the sweat started to get into her eyes, she noticed the man was no longer moving."
        "Did… Did she just…?"
        show jezera happy behind bg8
        je "Relax… He’s fine."
        hide jezera
        show jezera happy at midleft with moveinleft
        show alexia 2 necklace shocked at center with dissolve
        "The demoness embraced her from behind, hugging her gently. Affectionately. Reaching for her chin, she forced Alexia to look away from them man, and into her eyes."
        je "You didn’t do anything wrong."
        je "There’s no reason for you to feel guilty."
        je "About anything."
        "Weakly, Alexia untangled herself from her."
        al "No… This isn’t..."
        jump omarWhippingAftermath
        
    "Punish him, because her marriage is a fucking joke." if tempBlame > 2:
        $ released_fix_rollback()
        $ tempBlame += 2
        show alexia 2 necklace concerned at center with dissolve
        show bg8 with smallshake
        show bg8 with redflash
        al "Take… That… Take… That!"
        "How long has she been hitting him? She lost count. But it wasn’t enough. It could have been a thousand strikes, and it still wouldn’t be enough."
        show bg8 with smallshake
        show bg8 with redflash
        "She needed him. It was his fault she was here. All of this was his fault."
        "And he abandoned her."
        al "Why… Why…"
        "She couldn’t feel her arm anymore. And the man before her wasn’t moving either."
        "And he wasn’t Rowan."
        "But how she wished he was..."
        "She felt the tears running down her face. She didn’t have the strength to wipe them."
        show jezera happy at midleft with moveinleft
        je "There, there…"
        "The demoness hands cupped her cheeks gently, her thumbs wiping the tears away. Alexia forgot about her. Forgot she was here."
        je "Didn’t it feel good?"
        je "To finally let go?"
        "Alexia looked at her with unseeing eyes."
        al "Not..."
        jump omarWhippingAftermath
        
label omarWhippingAftermath:

al "This isn’t… Me…"
al "You did something…"

je "Shh…"

"Jezera placed a finger on her mouth. Her other hand started to caress her cheek soothingly. For the first in what felt like forever, Alexia saw no smugness, no mockery in her eyes."
"Only compassion."

je "No, it isn’t you. And it doesn’t have to be you."
je "But the “you” you are now…"
je "Doesn’t have to be you either."

"The demoness offered her a kind smile. A smile Alexia didn’t think she was capable of."

je "You don’t have to be the quiet, servile girl who just… Takes everything thrown at her and always shows the other cheek."
je "Let go of that. Unchain yourself from everything that holds you back."
je "Let me help you free yourself from all that pain in your heart."
je "Let me help you embrace your desires."

"Her hand reached behind Alexia’s head, and the demoness slowly drew her in."

menu:
    "Let her kiss you." if NTR == True:
        $ released_fix_rollback()
        jump omarWhipSex
        
    "Push her away.":
        $ released_fix_rollback()
        show jezera displeased at center with moveinleft
        show alexia 2 necklace shocked at edgeright with moveoutright
        jump whipRunningAway


label whipRunningAway:
$ tempWhip -= 2
$ whipCor = tempWhip * 3
$ change_corruption_actor('alexia', + whipCor)
$ blameRelation = tempBlame * 5
$ change_relation('alexia', - blameRelation)

al "No… No!"
al "… Isn’t… Me…"

je "Alexia…"

show alexia 2 necklace shocked at edgeleft with moveoutleft

"She didn’t listen to what she had to say. Panicking, she rushed past her. Almost delirious, she stumbled into the cell bars, before almost falling through the cell open doors."

hide alexia with moveoutleft

"She ran out of the dungeon, leaving the demoness behind."

scene bg14 with fade
show alexia 2 necklace concerned at center with moveinleft

"And she was going mad as well."

if all_actors['alexia'].relation < 40:
    "Rowan was supposed to be her anchor. Without him, she was drifting without direction."
    "And all around her, dangerous waters loomed."
    al "(Someone… Anyone…)"
    al "(Save me.)"
    
else:
    "Rowan was the last thing that held her sanity together. If he ever falls of the deep end…"
    "She feared what will become of her."
return

label omarWhipSex:

$ whipCor = tempWhip * 3
$ change_corruption_actor('alexia', + whipCor)
$ blameRelation = tempBlame * 5
$ change_relation('alexia', - blameRelation)
$ all_actors['alexia'].flags['jezera_influence'] += 3



show alexia 2 necklace aroused at edgeleft with moveoutleft
show jezera happy at midleft with moveoutleft

"She allowed Jezera to find her lips, the down sharing a kiss that started chaste, but grew more passionate by the moment, spreading warmth all across her body. She didn’t even realize how cold she felt until now."
"Maybe Jezera was right. Maybe there was more to her. Maybe there were parts of her that just waited to be unleashed upon the world. Parts she could come to accept, and even enjoy."
"Alexia didn’t know. She didn’t want to think anymore. She just wanted to forget about everything, even if only for a moment."

if alexiaJezeraSex > 0:
    "Even it meant, again, giving herself to the woman responsible for her predicament."
else:
    "Even it meant giving herself to the woman responsible for her predicament."

scene cg259 with fade
show jezera happy behind cg259
show alexia 2 necklace aroused behind cg259
pause 3

"She felt the demoness hand reach underneath her skirt. She didn’t protest. Let her do whatever she wanted. Maybe it really would be easier this way..."

al "A-ah!"

"Jezera chuckled to herself, Alexia’s sweet moans being true music to her ears."
"So much potential in this simple peasant girl..."
"Jezera would mold her according to her own desires. She just needed to break all these silly preconceptions of “morality” Alexia so desperately still clung to."

if get_actor_flag('alexia', 'jezera_influence') < get_actor_flag('alexia', 'andras_influence'):
    "And this was an important step to make that ambition of hers a reality. Alexia was spending too much time with her brother. She couldn’t let that brute taint such a beautiful gem."
    
else:
    "She would destroy all that helped Alexia stay afloat, and when the woman finds herself drowning… She’ll be there to pull her out of the water, and into her arms."


scene cg260 with fade
show jezera happy behind cg260
show alexia 2 necklace aroused behind cg260
pause 3

"Jezera’s hand finally reached its target, her fingers worming her way inside Alexia’s panties."
"And she loved what she found."

al "M-mistress Jezera…"

je "Shh…"

"The demoness pushed her forward, gently forcing her back to the cold, stone wall of the dungeon. Alexia saw Omar in the corner of her eye, and had to turn her head away."

je "Just close your eyes, Alexia."
je "Close your eyes, and focus on my voice."

"She did as the castle Mistress commanded, resting her head on the hard surface behind her."

al "A-Ah!"

"A single finger found it’s way inside her, exploring her wet, overflowing lips. Did she really get so wet from something so wro-"

je "Shh…"
je "You’re thinking about stupid things again, I can see it. Stop. Stop thinking about all that causes you pain."
je "Focus on this."

al "Ah!"

"Another finger was thrust inside of her, this time much more forcefully. Alexia stifled a moan, unable to fight off the growing heat in her nether regions."

je "There. Isn’t this better?"

"Alexia felt the demoness press her body against her own, her soft breasts squashing hers. The smell of her perfume banished the scent of blood, overpowering Alexia’s senses. She welcomed it, like never before."

je "Isn’t it better to let yourself be carried away by this feeling?"

"Her world was reduced to Mistress Jezera’s sweet perfume, her warm body, her seductive words, and her forceful fingers. Once, she would find it oppressing. But now… Somehow, it was just the opposite of it."

al "Ah! Nn-ah!"

scene cg261 with fade
show jezera happy behind cg261
show alexia 2 necklace aroused behind cg261
pause 3

"Her back arched, as her body sought to give Jezera easier access to her needy hole. Jezera welcomed the invitation, sneaking another finger inside."

al "Hah…. A-a-ah!"

je "Alexia, my sweet Alexia."

"The demoness lips brushed gently against the skin of her neck, of her cheek, teasing her."

je "You are still holding back."

je "Let go. Forget about everything, and focus on what you’re feeling."

"Her fingers plunged deeper."

al "AH! HAA- AH!"
al "Aaaah! Nn-Aa-Aaaah!"

je "Louder."

"Jezera blew gently into her ear, as her hand mercilessly abused her lower region, pushing in and out of her pussy."

al "Aaaaaah!"

je "Louder!"

al "AAAH! A-AH! NNNH-AAAAH! AAAAH! … AAAH!!"

"She couldn’t hold it in. She knew she was being shameless, screaming at top of her lungs as Jezera played with her body without as much a sliver of resistance from herself."
"But she just couldn’t resist the temptation. She couldn’t resist the sweet oblivion that came with following Jezera’s lead."
"“Don’t think. Focus on the pleasure.”"

al "AAAAH! A-A-AAAAH! … HAAAH-NN-AAAH!"

je "Good girl."
je "Just focus on my fingers. Focus on my voice."
je "And scream your lungs out."

"Throwing her head back, she did just that. Each moan, each scream, a declaration of her submission. Each and every single one, rewarded by the demoness."
"With every moan, Jezera would bestow onto her a new pleasure. Her lips caressed her skin, licking and kissing, conquering. Her free hand explored her bosom, pinching and kissing, claiming."
"For a single moment, in the darkest dungeons of Castle Bloodmeen, the concept of right and wrong stopped existing. There was only pleasure."
"And the mistress in control of it."

al "A-AAH! Ooooh-Nn! Aaah!"

"..."

al "Aaaah! M-more! Aaah!"

"..."

al "P-please! M-mistess Je-zera!"

"... ... ..."

"Alexia lost track of time, endlessly coming on Jezera’s fingers. She had long since stop paying attention to the things the demoness kept whispering to her ear. Seductive little promises, of things to come."
"As long as she put her trust in Mistress Jezera."

je "Alexia."
je "Open your eyes."

al "Mmm..."

"Groggily, she gazed upon her mistress."
"Mere inches away from her face, she saw Jezera’s victorious smirk. Her eyes shone in the dark, betraying just how greatly the demoness relished in Alexia’s submission."
"Reason started to return to her, as strength started to leave her body."
"Was this a mistake? Letting Jezera do whatever she wanted with her… Was this really a good idea?"

je "Now…"

"Jezera’s hand entered Alexia’s vision. The same one she used to finger-fuck her for the last… Several hours?"
"It was soaking wet with her juices, glistening lightly in the half-dark of the cell."

je "Open up."

$ alexiaUnfaithful = True
$ alexiaJezeraSex += 1

menu:
    "Obey.":
        $ released_fix_rollback()
        "Maybe it was the exhaustion. Maybe it was the lingering pleasure between her legs."
        "Or maybe part of her wanted to do everything Jezera ordered, without thinking too hard about it. Or anything."
        "She opened her mouth, and leaned in lick her juices of the demoness fingers, slowly cleaning every single one with her tongue, much to Jezera’s delight."
        je "Good girl."
        je "Just keep doing as I say, and trust me…"
        je "I will open before you a world you never knew…"
        "… If Jezera had more to add, she didn’t register it. The whipping, the finger-fucking, all of that proved too much to her."
        "Her body gave way, and midway through the fourth finger, she found herself slipping into a deep slumber."
        "She felt Jezera catch her, the demoness low chuckle following her into sleep…"
        "..."
        if recruitDaz:
            jump whipDazEpilogue
        else:
            return
            
    "Turn your head away.":
        $ released_fix_rollback()
        "An inkling of fear crept into her heart, as she slowly came to recall everything the demoness forced to go through this day."
        "Just how much control did she allow the demoness to have over her? Not just over her body, but also over her thoughts, her emotions?"
        "... Too much. She sought to escape the filthy fingers, turning her head away, despite knowing Jezera would not be happy with it."
        "But the demoness didn’t mind her meek resistance in the very least."
        je "Oh, Alexia…"
        je "Isn’t it a bit too late to play squeamish?"
        "Alexia shuddered as Jezera touched her cheek, trailing a heart made of her own juices across her skin."
        je "Did I do wrong by you today?"
        je "Alexia…"
        je "Don’t fight me."        
        "She leaned in, with the tip of her tongue licked the wet spot she just made."
        je "Trust in me."
        je "And I’ll show you a world you never knew…"
        "All of this – the pressure, the whipping, the finger-fucking, proved to be much for her."
        "She found herself slipping away, into the embrace of darkness, and into Jezera’s arms."
        "… …"
        "The demoness' low chuckle following her into sleep..."
        "..."
        if recruitDaz:
            jump whipDazEpilogue
        else:
            return

label whipDazEpilogue:

"… …"
"… … ..."

scene bg8 with fade
show jezera happy at edgeright with moveinleft

je "Hm hm hm…"
je "There you go!"

show jezera happy at midleft with moveoutleft

je "I must say, it’s been a true pleasure working with you."

show dazzanath neutral at midright with moveinright

daz "Mmmm, I assure you the pleasure was all mine."
daz "It was quite the show, after all."

je "Oh, you flatterer. I Know - I’m the best."
je "But I will say, It’s so nice to finally meet someone who genuinely appreciates my schemes."

show jezera displeased at midleft with dissolve

je "My brother is always like-"
je "“Ooh, Jezera, this is waaay too complex!”"
je "“Wouldn’t it be easier to just torch everything to the ground?”"

daz "Mmmm, he is simple like that..."
daz "I don’t think he wholly understands true art takes both time and effort."
daz "You can’t just rush a proper corruption."

show jezera happy at midleft with dissolve

je "Exactly! Finally someone who gets it!"
je "I appreciate you volunteering for this. I hope Alexia didn’t overdo it too much."

daz "Oh, she did not hold back. But as they say…"
daz "A true artist must be willing to make sacrifices in the name of his craft."

je "Oh, where did Rowan find you, you wonderful gem of a man~."

daz "In a makeshift dungeon."
daz "Chained to a wall."

je "Ha!"
je "..."
je "Say, want to go for round two?"

daz "It would be my honor, Mistress Jezera."

je "Good boy."

scene black with fade
pause 1
return


label rudeRowanBranch:

scene bg6 with fade
show rowan necklace angry at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

omar "-really sorry! It’s just, the alcohol, and the-"

larry "Yeah, it’s the alcohol, we really didn’t want to call your wife a slu-"

omar "Solansia Tits shut the fuck up you’re going to get us both killed!"

ro "Oh no, don’t blame him, you’re both doing an equally excellent job at getting yourself in trouble."

"His harsh voice put and end to the discussion, cutting the two men off midway through their inept apology. Rowan knew what they did, and would not listen to this bull-crap."
"Alexia basically ambushed him the moment he stepped through the portal. Still fuming with rage, she described everything that transpired earlier this evening, sometimes in greater detail than was required."
"Suffice to say, her husband was none too pleased by the news."

if avatar.corruption > 59:
    scene black with fade
    show rowan necklace angry at center with dissolve
    "She saw his expression darken with ever insult she recalled, about both him and her. His jaw tightened, and a cold look entered his eyes."
    "Not a very common sight, as far as Alexia was concerned. She rarely saw her husband get mad, and even when he did, he never was so… Hateful."
    "Yet ever since the two of them found themselves in the twins thrall, she’s been noticing this expression increasingly more often."
    scene bg6 with fade
    show rowan necklace angry at midleft with dissolve
    show alexia 2 necklace neutral at edgeleft with dissolve
    "She wasn’t certain what to think of all of this."
    
else:
    "And judging by how she saw him scowl, his eyebrows furrowed in displeasure, he found the whole debacle both ridiculous and distasteful."
    
ro "Gag them. I’ve heard enough."

"The men tried to protest, but did not resist, as the two orcs who earlier dragged them into the throne hall brought out cloths and violently shoved them in their mouths."
"Alexia saw her husband rise his eyes to the ceiling and shake his head ever so slightly."

if avatar.corruption > 59:
    "There was no reason to literally choke them- tying the cloths behind the back of their head worked just as well."
    "Regardless, he said nothing of it."

else:
    ro "Just tie the cloths behind the heads next time. Goddess..."
    "He offhandedly reprimanded the orcs, then signaled for them to step back."
    
show rowan necklace angry at center with moveinleft

ro "So let me get this straight."

if avatar.corruption > 79 or all_actors['alexia'].relation < 50:
    ro "You showed blatant contempt for myself, despite knowing I’m quite literally the boss of your boss."
    ro "Several times you disrespected my wife, calling her a slut, and a whore."
    
else:
    ro "Several times you disrespected my wife, calling her unspeakable things."
    ro "You showed blatant contempt for myself, despite knowing I’m quite literally the boss of your boss."
    
if serveChoice == 4:
    ro "You ignored your duties, potentially delaying our subjugation of Rosaria."
    
else:
    ro "You ignored your duties, knowing fully well what consequences there might be to both me and my wife."

if alexiaAndrasSex > 0:

    if alexiaOffer:
        pass
        
    else:
        show alexia 2 necklace concerned at edgeleft with dissolve
        ro "You spread slanderous lies about my wife sleeping behind my back."
        show alexia 2 necklace neutral at edgeleft with dissolve
        al "Absolutely abominable!"
        
else:
    "You spread slanderous lies about my wife sleeping behind my back."
    
ro "And you were still drinking when my orcs found you!"
ro "I understand castle Bloodmeen isn’t exactly stormed by highly qualified help, but is this really who I have to work with now?"
ro "You?!"

show rowan necklace concerned at center with dissolve

ro "I should have you executed for this."

show rowan necklace neutral at center with dissolve

ro "But I won’t."


if avatar.corruption > 69 or (avatar.corruption > 59 and all_actors['alexia'].relation > 59) or (avatar.corruption > 49 and serveChoice == 2):
    jump rudeRowanBranchCor
    
else:
    jump rudeRowanBranchPure
    
label rudeRowanBranchCor:

$ rowanTwoWorkers = 'harsh'

"A wave of relief washed over the workers, but Alexia knew a false hope spot when she saw one."

if all_actors['andras'].relation < 30:
    ro "I’m not Andras for fucks sake."

else: 
    pass
    
show rowan necklace happy at center with dissolve

ro "No, instead, I sentence you to mine duty."

show rowan necklace angry at center with dissolve

ro "For life."

show rowan necklace happy at center with dissolve

ro "I hope you two took a good look at the sun this morning, because you are not going to see it again."

show rowan necklace angry at center with dissolve

ro "Ever again."

omar "..."

larry "..."

"For a moment, everyone gathered just stared at one another silently."

omar "Mmm! MMMM! Mmmm!"

"Omar threw himself forward, only to be violently thrown to the ground by the orc guarding him. Larry was smart enough not to try anything like that – if or too shocked to move."
"Alexia swallowed heavily as she watched the unfolding scene. This seemed… Harsher than she expected."
"Was this really an appropriate punishment?"

menu:
    "Yes. They deserve this.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +10)
        $ omarLarryOutcome = "mines"
        "Alexia steeled her heart, and quelled any remaining embers of sympathy she had for the men. They should’ve been more polite."
        show alexia 2 necklace happy at edgeleft with dissolve
        "It fact, it felt nice, to see Rowan defend her honor so decisively. He usually opted for more reserved solutions, rather than this, perhaps somewhat crude, but very direct display of his power and authority."
        "Maybe something good will come out of this whole “slaves to the demons” situation after all."
        ro "Take them away."
        "The two workers, bound and gagged, stood no chance against the orcs. Their fates were sealed."
        "The orcs dragged them outside, their muffled screams slowly dying out in the halls of the castle."
        al "Thank you, Rowan."
        show rowan necklace happy at center with dissolve
        ro "You’re welcome."
        jump rowanKinkyFollowup
        
    "No. Rowan is being needlessly cruel.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', -3)
        show alexia 2 necklace concerned at edgeleft with dissolve
        al "Rowan…"
        show alexia 2 necklace concerned at midleft with moveinleft
        al "Don’t you think this is a little…"
        al "Excessive?"
        ro "Excessive?"
        "She caught a glimpse of his face. His anger did not die out – in fact, she wondered whether or not it was directed at her now."
        show alexia 2 necklace concerned at edgeleft with moveoutleft
        ro "Really, Alexia?"
        ro "They called you a whore."
        ro "A slut."
        ro "Insulted both you and me, and placed us both in danger."
        ro "Do you really think I should be lenient with them?"
        
        menu:
            "Yes.":
                $ released_fix_rollback()
                $ change_corruption_actor('alexia', -3)
                show alexia 2 necklace neutral at midleft with moveinleft
                "Steeling herself, Alexia looked up to her husband a took a step forward. It wasn’t often she stood against him."
                "But she couldn’t let him continue on this path."
                show rowan necklace shock at center with dissolve
                ro "Yes."
                show alexia 2 necklace concerned at midleft with dissolve
                show rowan necklace neutral at center with dissolve
                al "I was… Angry with what they said before. Furious, even."
                show alexia 2 necklace neutral at midleft with dissolve
                al "But this…"
                al "This is going too far."
                al "Please, Rowan."
                al "I forgive them. Can’t you just… Tell them to brush the barrack cobblestones for the next two months? Or something like that?"
                show alexia 2 necklace happy at midleft with dissolve
                al "Wouldn’t that be punishment enough?"
                if avatar.corruption > 79 or all_actors['alexia'].relation < 30:
                    ro "..."
                    show rowan necklace angry at center with dissolve
                    show alexia 2 necklace shocked at midleft with dissolve
                    ro "No."
                    al "Rowan, I-"
                    al "No, Alexia, this isn’t up to debate."
                    ro "Their actions threaten both of us. And I cannot overlook such brazen show of disrespect."
                    show rowan necklace concerned at center with dissolve
                    ro "I’m doing this for us."
                    show rowan necklace neutral at center with dissolve
                    ro "So be quiet for one minute and let me do my job here."
                    "She watched, stunned, as he turned his back on her, and address the orcs."
                    ro "You have your orders. Take them away."
                    omar "Mmm! Mmm!" 
                    "Again, Omar tried to break free, only to be punched in the face by the guard restraining him, rendered unconscious on the spot. Alexia could only watch in horror as the orcs dragged them away."
                    al "..."
                    al "..."
                    show alexia 2 necklace concerned at midleft with dissolve
                    al "You’re just like them."
                    show rowan necklace angry at center with dissolve
                    al "You’re just like the twins."
                    ro "I am nothing like them!"
                    show rowan necklace concerned at center with dissolve
                    ro "Look, listen to me for a moment-"
                    show rowan necklace concerned at midleft with moveoutleft
                    show alexia 2 necklace concerned at edgeleft with moveoutleft
                    al "Don’t touch me."
                    "She stumbled backward, grasping the wall to stop herself from falling."
                    "She had to go."
                    hide alexia with moveoutleft
                    "She had to get away from all of this."
                    show rowan necklace angry at midleft with dissolve
                    ro "Alexia!"
                    scene black with fade
                    show rowan necklace angry behind black
                    ro "You get back here right now!"
                    ro "Alexia!"
                    "... ... ..."
                    "... ..."
                    "..."
                    $ omarLarryOutcome = "mines"
                    $ change_relation('alexia', -25)
                    $ alexia_away_weeks = 1
                    $ alexia_cant_work_weeks = 1
                    $ all_actors['alexia'].job_state.job = None
                    jump rudeApology
                   
                    
                else:
                    ro "..."
                    "Her husband sighed wearily."
                    ro "Alexia… It’s not that simple."
                    ro "I can’t have the staff sabotaging me."
                    show rowan necklace angry at center with dissolve
                    ro "This job is difficult with the twins being… The twins."
                    ro "I don’t need this… Circus show rocking the boat."
                    al " I know Rowan, I know."
                    show rowan necklace concerned at center with dissolve
                    "She grabbed his face gently, a kind smile on her face."
                    show alexia 2 necklace neutral at midleft with dissolve
                    al "But this isn’t like you."
                    show alexia 2 necklace concerned at midleft with dissolve
                    al "Don’t let this place turn you into somebody I no longer recognize."
                    ro "..."
                    show rowan necklace angry at center with dissolve
                    "Without another word, he grabbed her by the hands and pushed her away."
                    "His cold gaze turned to the workers once more."
                    show alexia 2 necklace concerned at edgeleft with moveoutleft
                    show rowan necklace angry at edgeright with moveoutright
                    ro "Three months of cleaning the barracks, and if I ever see any of you two idiots again, you’ll end as Cliohna’s experiments. Have I made myself perfectly fucking clear here?"
                    larry "Mmm!"
                    omar "Mmmm!"
                    show rowan necklace neutral at edgeright with dissolve
                    ro "Good. Take them away."
                    "..."
                    al "… Do you want to talk about this?"
                    ro "..."
                    ro "Let’s see what’s for dinner."
                    hide rowan with moveoutright
                    "He left without another world. His wife, after a moment of hesitation, hurrying after him."
                    $ omarLarryOutcome = "barracks"
                    $ change_base_stat('c', -10)
                    $ change_relation('alexia', -5)
                    return
                
            "Perhaps not...":
                $ released_fix_rollback()
                $ change_corruption_actor('alexia', -5)
                al "..."
                al "Well, maybe not, but…"
                show rowan necklace happy at center with dissolve
                ro "Good."
                "He didn’t wait for her to finish. The matter was resolved."
                show rowan necklace neutral at center with dissolve
                ro "Take them away."
                "The two workers, bound and gagged, stood no chance against the orcs. The Bloodmeen guards dragged out of the chamber, with Omar’s muffled screams slowly dying out in the halls of the castle."
                "Alexia pretended she didn’t hear it. It was easier that way."
                show rowan necklace neutral at midleft with moveoutleft
                ro "Alexia, look."
                show rowan necklace concerned at midleft with dissolve
                ro "I understand things haven’t been… Easy for you."
                ro "But that is exactly why I need you strong."
                "He held her close, kissing her softly on the forehead."
                if all_actors['alexia'].corruption > 50:
                    "She nodded solemnly. She understood why Rowan needed to be harsh, but still…"
                    "It left a bitter aftertaste in her mouth."
                    show rowan necklace happy at midleft with dissolve
                else:
                    "She said nothing. Her husband waited for her to respond, before sighing and letting go."
                ro "Alright, let’s grab something to eat. I’m starving."
                al "… Of course."
                return


label rudeRowanBranchPure:

$ rowanTwoWorkers = 'kind'

ro "Stupidity is not a crime, as much as I’d want it to be."

show rowan necklace neutral at center with dissolve

ro "One month of cleaning the orc barracks. And I’m being lenient here."
ro "Consider yourself lucky, that Alexia came with this to me, and not Jezera or Andras. None of them would be anywhere near as understanding here."
ro "So clean up your act before the twins catch wind of your antics. Have I made myself clear?"

larry "Mmm!"
omar "Mmmm!"

ro "Good."

"The two workers nodded their head, not believing their own luck. Any noble, after having their wife insulted as Rowan had, would have their heads on a plate."
"Few people had Rowan’s compassion, and it was that very kind heart that made Alexia marry him."
"… Still, a part of her now wondered if he wasn’t being too kind. Oh, she understood they were just two incredibly stupid assholes. Not exactly grounds for execution."
"But after the things they said about her…"
 
menu:
    "Rowan is being too kind.":
        $ released_fix_rollback()
        show alexia 2 necklace angry at edgeleft with dissolve
        "… They really didn’t deserve any mercy."
        al "… Is that it?"
        ro "Excuse me?"
        al "Is that all they get?"
        al "One month of cleaning duty?"
        al "For calling your wife a whore, a slut, and an airhead?"
        if all_actors['alexia'].relation > 50:
            show rowan necklace concerned at center with dissolve
            "She didn’t hide the disappointment in her voice, and she saw that every word was like a dagger to Rowan’s chest."
            "Good. He should find this painful. Just as she did."
        else:
            "She didn’t hide the disappointment in her voice, but Rowan’s face remained impassive."
            "… Did he really care so little for it?"
        ro "Then what would you have me do?"
        ro "Toss them into the blackest abyss, just for being rude to my wife?"
        al "..."
        
        menu:
            "Yes, that’s precisely what he should do!":
                $ released_fix_rollback()
                $ change_corruption_actor('alexia', +5)
                al "Yes! Exactly that!"
                show alexia 2 necklace concerned at edgeleft with dissolve
                al "Or do you not care what they all say about me when you’re gone?"
                al "Is being locked in this castle not enough for me? Do you also want me to listen to people mocking me and belittling me on every corner?"
                show alexia 2 necklace neutral at edgeleft with dissolve
                al "Is it too much, to ask that you protect my dignity and good name, as a husband should?"
                show rowan necklace neutral at center with dissolve
                "This must have hit a spot, as she saw his features hardened. Perhaps it wasn’t exactly fair of her here, but after being married for so long, one learned what buttons to push."
                "Rowan turned his eyes to the two workers who now squirmed in their bondage as the two orcs held them, shaking their heads as the begged Rowan to ignore his wife’s counsel."
                show alexia 2 necklace angry at edgeleft with dissolve
                "Alexia turned her gaze at them as well, casting them a venomous look. They shriveled under it, much to her satisfaction."
                if avatar.corruption > 20 or all_actors['alexia'].relation < 50:
                    ro "..."
                    show alexia 2 necklace shocked at edgeleft with dissolve
                    ro "No."
                    ro "No, this is not right. I’m not going to kill them or do something equally as bad, just because they insulted you."
                    show rowan necklace concerned at center with dissolve
                    ro "Alexia, I understand you feel-"
                    show alexia 2 necklace angry at edgeleft with dissolve
                    al "Oh, spare me. I don’t want to listen to his."
                    ro "Alexia-"
                    al "I should’ve known you wouldn’t have the guts to stand up for me."
                    if all_actors['alexia'].flags['andras_influence'] > 5:
                        al "Andras wouldn’t think twice about this."
                    elif all_actors['alexia'].flags['jezera_influence'] > 2:
                        al "I should’ve asked Jezera to deal with them. She wouldn’t think twice about this."
                    else:
                        al "Spineless wimp."
                    ro "Alexia!"
                    hide alexia moveoutleft
                    "She couldn’t stand his presence anymore. She couldn’t believe she married this cowardly pile of self-righteous delusions."
                    scene black with fade
                    "She stormed off, without looking back even once."
                    $ omarLarryOutcome = "barracks"
                    $ change_relation('alexia', -10)
                    jump rudeApology
                    
                else:
                    ro "..."
                    show alexia 2 necklace happy at edgeleft with dissolve
                    ro "You’re right."
                    "Her husband sighed to himself, a tortured look crossing his face."
                    al "(Oh sweet Rowan… Always trying to do the right thing.)"
                    "This time, it meant listening to her."
                    "Still, she was not unsympathetic to his plight. She walked up to him and hugged him gently, hoping it would ease his burden just a little bit."
                    ro "Mining duty. Throw them into the deepest tunnels you find. I don’t want to see them in the castle ever again."
                    omar "Mmm! MMMM! Mmmm!"
                    "Omar threw himself forward, only to be violently thrown to the ground by the orc guarding him. Larry was smart enough not to try anything like that – if or too shocked to move."
                    "To have their fortune overturned so suddenly…"
                    "Alexia saw the regret on their face as the orcs dragged them away. Good. This should make people think twice before insulting her again."
                    al "Thank you, Rowan. I know it wasn’t easy."
                    al "But I feel better knowing I can rely on you."
                    ro "..."
                    ro "Let’s see what’s for dinner."
                    hide alexia with moveoutleft
                    hide rowan with moveoutleft
                    "He turned away without another word. Alexia followed, a soft smile on her lips as she went."
                    $ omarLarryOutcome = "mines"
                    $ change_base_stat('c', 5)
                    $ change_relation('alexia', -5)
                    return

            
            "Maybe not.":
                $ released_fix_rollback()
                show alexia 2 necklace concerned at edgeleft with dissolve
                $ omarLarryOutcome = "barracks"
                "Alexia scowled softly. This whole debacle was leaving a bad taste in her mouth."
                al "I guess not…"
                show rowan necklace happy at center with dissolve
                ro "I understand this isn’t easy for you."
                show rowan necklace angry at center with dissolve
                ro "Believe me, I heard my share of insults when they made me general. From people who definitely should know better than to disrespect their superior officer."
                show rowan necklace concerned at center with dissolve
                ro "But If I had every soldier decapitated just for being stupid or narrow-minded, I’d be killing a lot of people who could still do good…"
                ro "… With proper guidance."
                show rowan necklace neutral at center with dissolve
                "He signaled for the two orcs, and the castle guards pulled the men upwards."
                ro "I hope this will be a lesson for you. I expect you to be at your best behavior from now on."
                larry "Mmm!"
                omar "Mmm-mm!"
                ro " … I’ll assume that was “Yes” and “Yes sir!” subsequently."
                ro "Take them away."
                "The orcs dragged them out, while Alexia rubbed her arms, not sure where to look."
                show rowan necklace concerned at center with dissolve
                ro "Alexia…"
                show rowan necklace concerned at midleft with moveoutleft
                ro "How are you holding up? Are you okay?"
                al "I’m fine."
                "Such an obvious lie. Rowan saw right through it and moved in to hug her close to his chest. The warmth of his body, and the beating of his heart, brought a strange sense of calmness to her."
                "This place was getting to her. Turning her into someone she didn’t recognize anymore. She was glad she still had Rowan with her. He was her anchor. Her lighthouse guiding her to the shore in these dark waters."
                "She feared what could happen if someone ever snuffed that fire out."
                $ change_corruption_actor('alexia', -5)
                return

        
    "Rowan is right.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', -5)
        show alexia 2 necklace concerned at edgeleft with dissolve
        al "..."
        "… Guess she shouldn’t let her emotions get the better of her. Everybody deserved a second chance, even these two."
        ro "Alright, take them away."
        $ omarLarryOutcome = "barracks"
        jump rowanKinkyFollowup


label rowanKinkyFollowup:

show alexia 2 necklace happy at edgeleft with dissolve
show rowan necklace happy at midleft with moveoutleft

ro "Well, that was a wonderful way to start the weekend."
ro "Do we have another crisis for me to look over?"
ro "Are Cla-Min and Skordred arguing about societal ideas again?"
ro "Or maybe Andras killed a bunch of orcs and now cannot comprehend why morale is low?"
ro "Because I swear by the Goddess, there’s something new every week. Maybe I should just start holding two audiences at once!"

"A forced attempt to lighten up the mood, albeit a successful one. They had so little time for one another, neither really wished to discuss the matter any further."
"But she did feel a little bad about forcing Rowan to deal with it…"

show alexia 2 necklace concerned at edgeleft with dissolve

al " I’m sorry for adding to your problems, but I didn’t want to go to Jezera with it…"

show alexia 2 necklace happy at edgeleft with dissolve

ro "It’s fine, Alexia. The matter is resolved, no point dwelling on it."

show rowan necklace neutral at midleft with dissolve

ro "Hmmm… Although…"

show alexia 2 necklace shocked at edgeleft with dissolve

"He placed his hands on her hips, and hugged her close. A devious smile danced on his lips as his hands slowly roamed over her curves, making their way to her backside."

show alexia 2 necklace happy at edgeleft with dissolve

ro "Maybe I am a little mad about all of this."
ro "Most wives great their husbands with a warm meal on their return."
ro "And what do I get?"
ro "Two drunk clowns?"

"She giggled to herself. Right, guess this wasn’t how her husband imagined their weekly reunion would start like."
"Well, if that’s the case…"

menu:
    "Take the lead - “Compensate” him for all the hard work.":
        $ released_fix_rollback()
        $ kinkylead = "alexia"
        "Her hand playfully danced down his chest, as she looked him deep in the eyes. It did not escape her how he was undressing her with them, his desire for her growing more apparent by the second, as her fingers ventured further and further down."
        al " I’m terrible sorry Rowan. I must be a pretty horrible wife, since I also appear to have forgotten to set up the stove."
        al "But I think I can get you something warm for the evening..."
        "She grabbed him by the groin, feeling his rock-hard erection, thoroughly enjoying the soft grunt it got out of her husband."
        "His office was just behind the corner. It would serve well for what she had planned…"
        jump rowanKinkyFollowupSex

        
    "Tease him a bit, and see where it goes.":
        $ released_fix_rollback()
        $ kinkylead = "rowan"
        al "Guess I’m a pretty bad wife."
        al "Thinking about punishing me?"
        if whipJezPotion:
            al "Should I bring the whip?"
            ro "Not this time."
        else:
            pass
        "He grabbed her backside possessively and forced her hips into his groin, making Alexia feel the result of their week-long separation."
        al "Oh!"
        if raeve_keep_rowan_claimed_helayna or alexiaThreesomeStormout:
            "It was incredibly satisfying, knowing that despite the many women that showed interest in Rowan, some of them much younger than her, she still had this sort of an effect on her husband."
        else:
            "It was nice knowing, that despite the many years of their marriage, she could still have this sort of effect on her husband."
        al "I guess it’s not a meal you’re hungry for."
        ro "You guessed right. Now get moving."
        show alexia 2 necklace shocked at edgeleft with dissolve
        "He slapped her on the ass, and pushed her in the direction of his office…"
        jump rowanKinkyFollowupSex
            
    "Enough emotions for today. Grab dinner together and call it a day.":
        $ released_fix_rollback()
        "She put her hand on his chest and playfully pushed herself away."
        al "Let’s see about that warm meal first, shall we?"
        al "Then we can think about other things."
        ro "Tease."
        "She flashed him a coy smile and grabbed him by the hand, leading him to the castle kitchen."
        "They’d play another day."
        return
        

label rowanKinkyFollowupSex:

scene black with fade
show rowan necklace aroused behind black
show alexia 2 necklace aroused behind black

if kinkylead == "rowan":
    al "Mmm-!"
    ro "Open wide!"
    #cg 1
    scene cg286 with fade
    show rowan necklace aroused behind cg286
    show alexia 2 necklace aroused behind cg286
    pause 3
    "His patience has long since expired. The moment they reached his office, he dragged her in front of his chair, and forced her to her knees. A few hectic movements later, his cock was free for Alexia to admire-"
    "Only for Rowan to grab her by the head and instantly jam it down her throat."
    al "! ! !"
    al "(S-so forceful!)"
    if rowanTwoWorkers == 'harsh':
        "He paid no attention to her grunts of discomfort, and yanked her by the hair to make her adjust her position. She scrambled to follow his directions, knowing he expected her to keep up."
    else:
        "Seeing her discomfort, Rowan lessened his grip a little, as to not to hurt her. But there would be no denying his pent-up lust."
        "He gave her a short moment to adjust her position, which Alexia gratefully welcomed. But only a moment."
    al "MMM!!"
    "He pulled her head deep onto his cock, all the way in. A familiar warmth filled her mouth, one she was used to – but perhaps not to taking it so forcefully. He must have really missed her…"
    al "(Aah… Rowan..)"
    "His musky odor assaulted her nose. He didn’t even get to wash, so great was his desire."
    "Somehow, it served to only turn her on. From the moment he stepped through the portal, all he must’ve been thinking about was finding and making love- no, fucking his wife. He didn’t care for everything else."
    if raeve_keep_rowan_claimed_helayna or alexiaThreesomeStormout:
        "Not even for other women. She was the one he wanted most. His loving, obedient wife."
    else:
        pass
    al "(A-ah…)"
    "She obediently ran her tongue across his length, as much as she could – it was far too deep for her to appreciate it properly, or, for that record – breathe properly."
    "Obviously, that would not be enough to please her husband, and she soon felt his hold of her lessen."
    "She understood what he wanted of her. She pulled back a little, sucking on the tip of his tool, before willingly taking him all the way in again."
    ro "Very good Alexia… Keep doing that."
    "If he wanted her to face-fuck herself on his dick… Who she was to refuse?"
    if avatar.corruption > 60:
        "A predatory smile danced upon his lips, his eyes devouring her form, making a pleasant tingle run down her spine. These eyes too, she’s been seeing more often recently."
        "Hungry eyes, filled with primal, animalistic desire."
        "She didn’t mind. At least not now, when she was sucking his cock with such abandon."
    else:
        "A confident, cocky smile danced upon his lips, as he appreciated her kneeling form. He always was enjoying himself a little too much when she agreed to humor him like that."
        "Oh, but she didn’t mind. Did not mind at all."
    al "Mmm-mmm… Mmm… Mm!"
    "She increased her effort, sucking him greedily, her mouth making increasingly more obscene noises. Her muffled moans and lewd slurping filled the room, and she heard husband chuckle at it."
    ro "Good heavens Alexia."
    if rowanTwoWorkers == 'harsh':
        ro "For someone who got so prissy about some two guys calling her a slut..."
        ro "You’re acting pretty slutty right now."
    else:
        ro "I’m starting to think I was being too hard on Larry and Omar."
        ro "You’re acting quite.... Liberal today."
        al "(Slutty. You wanted to say slutty.)"
    "Her cheeks turned crimson in embarrassment, and she felt her shame only added to Rowan’s arousal."
    menu:
        "Maybe she is a bit of a slut…" if alexiaUnfaithful:
            $ released_fix_rollback()
            "… Maybe he was onto something. She hasn’t been exactly acting like the very picture of a Rosarian wife in recent months, but surely Rowan couldn’t complain about the results, right?"
            $ change_corruption_actor('alexia', 5)
            
        "Only for him.":
            $ released_fix_rollback()
            "Surely there was nothing wrong with servicing her husband with a little more enthusiasm than the church of Solansia advocated for, right?"
            $ change_relation('alexia', 5)
            
        "It’s not like that…" if all_actors['alexia'].corruption < 50:
            $ released_fix_rollback()
            al "(I just…)"
            "She tried to think of an excuse, but it was hard to defend her dignity with a cock in her mouth."
            $ change_corruption_actor('alexia', -5)
            
    "She wouldn’t be allowed to consider the matter further, as her apparent embarrassment was exactly what pushed her husband over the breaking point."
    show cg286 with sshake
    show cg286 with sshake
    show cg286 with flash
    if rowanTwoWorkers == 'harsh':
        "His hand, until now content to caress her hair, now grabbed her by the back of the head and forced her to take his cock all the way in, allowing Rowan to deposit his seed directly into her stomach."
        "She had nothing to say on the matter. She gagged lightly, as she felt his thick cum pour down her throat."
    else:
        "His hand, until now content to caress her hair, now gripped it again, forcing Alexia in place as her husband came in her mouth."
        "Obediently, she drank all of it, enjoying the tart taste of her beloved."
    ro "Nnn- aah!"
    ro "Damn… You have no idea how much I wanted to see you like this."
    "He freed her mouth, causing her to gasp loudly. Oh, she had a pretty good idea…"
    al "(… Hah…)"
    "Guess in the end, one of the got their warm meal after all..."
    return
        
else:
    al "Mmmm…"
    ro "Mmm- A-Alexia!"
    "In a rare display of initiative, she pushed her husband into his office, throwing him into his chair with surprising forcefulness."
    "It’s been only a week, but damn, she missed him."
    al "Just relax, my beloved…"
    "She pressed into him, locking their lips in a long, passionate kiss, born of prolonged separation."
    "She wanted him, and she wanted him to know that."
    al "Aah..."
    al "I’ll show you I take my wifely duties very seriously."
    "She didn’t rush into things. Not at first. Standing over him, she made a show of kneeling down, running her hands under his shirt, feeling his chiseled chest."
    "Her eyes never left his, and she watched, with sweet satisfaction, as his breathing grew heavy, his arousal more apparent by the second."
    "He allowed himself to be subjected to this sweet torture, waiting for Alexia to finally reach the thing that needed her touch most."
    if rowanTwoWorkers == 'harsh':
        "It always fascinated her, how he could be so… Domineering in day to day matters, but once she got him in bed, he was often willing to give up control with but token resistance."
        "She never really explored that part of him before, at least not in depth…"
        "But she didn’t mind it."
    else:
        "He was always so considerate of others. So understanding. Took lead because he had to, not because he wanted to."
        "So this one time, Alexia was more than happy to take the burden of leading off his shoulders."
    "Slowly – agonizingly slowly – she got to her knees, the coy smile never leaving her lips."
    al "Have you been thinking about me during your journeys? About me kneeling before you like that…"
    "Her fingers deftly undid his buckle, and the swollen tip of his manhood proudly poked through his pants."
    al "About me putting your cock between my lips…"
    "She blew at it gently, and placed a chaste kiss at the very tip of it. Then another, further down."
    al "About me sucking you dry?"
    "And another, and another. The musky, familiar scent of his cock filled her nostrils, making her smile."
    ro "A-ah!"
    "She chuckled to herself, seeing his growing frustration. Was she being inconsiderate? Teasing him so, after everything he had to go through today, because of her?"
    "Maybe a little. But she was going to make up for all of it."
    #cg 2
    scene black with fade
    show rowan necklace aroused behind black
    show alexia 2 necklace aroused behind black
    "She ran her tongue along his shaft, from the base, to the swollen tip. Then again, along the side of it."
    "And again, along the other."
    if rowanTwoWorkers == 'harsh':
        ro "Nn-! Alexia…"
        "He growled at her, his hands clenching. Scary, scary… Yet still, he let her do as she pleased."
    else:
        ro "A-Alexia…"
        "He moaned her name out. Ah, how she loved when he did that!"
    "She felt her loins stir, and for a moment, she felt tempted to sneak a hand down to her crotch. But she resisted the temptation."
    "All of this… It wasn’t about her. It was about her showing him how much she appreciated all he kept doing for both of them."
    if all_actors['alexia'].relation < 50:
        "Even if they weren’t always on the same page."
    else:
        pass
    "A droplet of precum formed at the tip of his cock. She pressed her cheek against it, smearing it over her face, well aware of the effect it will have on him."
    al "Won’t you say it suits me?"
    ro "It def –ngh!- initely does."
    "She flashed him a cheeky grin. Exactly what she was hoping for."
    "Finally, she decided to put an end to his suffering. She opened wide, giving Rowan a good look at her face -"
    "Then dived straight into his cock, taking it all the way in."
    al "Mmm!"
    ro " Aah!"
    "She was going to milk him dry..."
    if helayna_escape_method == 'no escape' and alexiaThreesomeStormout:
        "Once she’s done with him, there’s no way he’ll have any strength left for either of the two floozies that kept trying to seduce him away from her."
    elif alexiaThreesomeStormout:
        "Once she’s done with him, there’s no way he’ll even want to look at that skinny elf floozy of his."
    elif helayna_escape_method == 'no escape':
        "Once she’s done with him, there’s no way he’ll have any strength left for Helayna. Guess she’ll have to find another way to satiate her lusts."
        "Poor her."
    else:
        pass
    ro "D-amn Alexia, that’s- Ah!"
    "She silenced him by wrapping her fingers around his balls, massaging them with care as she rocked her head on his cock, her tongue working his shaft diligently."
    "Up and down, up and down, his cock hitting the back of her throat. Up and down, up and down."
    al "(Let your wife take care of all that pent-up lust, my beloved…)"
    ro "NN- Ahh! Aaah! Aaa!"
    "His moans filled the office, joined by the obscene, slurping noises she was starting to make."
    "If someone entered the room now, what would they think? With her sucking her husband’s cock, right after he got back to the castle?"
    "Ha… Despite her earlier anger today…"
    "Maybe there was something to Omar and Larry’s words after all."
    menu:
        "Nothing wrong with enjoying herself a little." if all_actors['alexia'].corruption > 50:
            $ released_fix_rollback()
            "So what if in recent months she started to behave a bit more… Slutty."
            "There was nothing wrong with that."
            "Still didn’t change the fact they should’ve watched their words."
            $ change_corruption_actor('alexia', 5)
            
        "This was just for her husband. Nothing more.":
            $ released_fix_rollback()
            "Though really, her taking care of her husband was hardly “immoral”."
            "She was just doing her wifely duties. That’s all."
    "But she didn’t have the time to ponder the matter further. At last, her ministrations were rewarded, and she felt Rowan’s cock twitch."
    al "! !"
    ro "AH!"
    "She felt his hot cum fill her mouth, and she intensified her sucking, drinking his seed greedily. Her fingers never stopped massaging his balls, pushing more and more of him into her mouth."
    "Milk. Him. Dry."
    al "Ah! Ha…"
    "Finally, she released his cock, and immediately, went on to clean it up of any remaining cum, looking him in the eyes as she did."
    "Out of the two, she might have been the one who ended with a warm treat in her stomach…"
    "But she didn’t think he would complain."
    return

label rudeApology:

scene black with fade

"... ... ..."
"... ..."
"..."

scene bg14 with fade
show rowan necklace angry at midleft with dissolve

ro "(Solansia’s tits…)"

"Rowan mulled a curse in his mouth. For the entire weekend, his wife has been avoiding him. She wouldn’t even let him say goodbye as he headed for the portal."

if rowanTwoWorkers == 'harsh':
    "Just what he needed – his wife causing him troubles. As if the job wasn’t already difficult…"
else:
    show rowan necklace concerned at midleft with dissolve
    "He was growing concerned with all the mental strain she’s been under. He understood life in castle Bloodmeen wasn’t easy, but for her to react so violently to his opposition…."
    
"He wasn’t certain what to think about all of this."

show alexia 2 necklace concerned at midright with moveinright
show rowan necklace shock at midleft with dissolve

"But he would have to make up his mind soon."

al "Rowan."

show rowan necklace neutral at midleft with dissolve

ro "Alexia."

al "I..."
al "I wanted to apologize."
al "For what happened two days ago."
al "In the heat of the moment, I said some hurtful things I didn’t mean."

if rowanTwoWorkers == 'harsh':
    $ change_corruption_actor('alexia', 3)
    al "Rowan, you always took the high road, and it was painful for me to see you act so… In my eyes, callously."
    al "But I understand you have to make some compromises to survive, for us both."
    al "And I shouldn’t have been so hard on you for it."
    
else:
    $ change_corruption_actor('alexia', -3)
    al "Rowan, you always took the high road, and it was one of the many things that made me fall in love with you."
    al "But being here… I…"
    al "I guess I started to forget what it meant to be considerate of other people failings."
    al "And I… Lashed out when I shouldn’t have."
    
al "So… I just wanted to say I’m sorry."
al "And that I love you."

ro "..."

menu:
    "“I love you too, and I’m sorry as well.”":
        $ released_fix_rollback()
        label alBluffCheck:
        $ change_relation('alexia', 10)
        ro "I should’ve been more understanding of your anger. You’re trapped with these people the entire week…"
        ro "When your only crime is being the wife of a hero."
        show alexia 2 necklace happy at midright with dissolve
        ro "I’m sorry, for everything."
        if rowanTwoWorkers == 'harsh':
            $ change_corruption_actor('alexia', 3)
            ro "I’ve been making difficult choices my entire life. I’ve grown…"
            show alexia 2 necklace neutral at midright with dissolve
            ro "Desensitized, I guess."
            ro "I shouldn’t have shouted at you. I’m sorry."
            show alexia 2 necklace happy at midright with dissolve
            al "It’s okay. I forgive you."
            ro "Thank you."
            ro "I’m sorry, for everything."
        else:
            pass
        "He hugged her close, giving her a quick kiss."
        ro "And I love you. Stay safe."
        al "You be careful as well, my beloved."
        return
        
        
    "“I understand, but you need to be better than this.”":
        $ released_fix_rollback()
        $ change_relation('alexia', -5)
        ro "I understand, but…"
        ro "Alexia, I can’t have you causing me trouble, alright?"
        if rowanTwoWorkers == 'kind':
            show rowan necklace concerned at midleft with dissolve
            ro "I understand you had your reasons to be mad at these two guys, but you can’t… Lash out like that."
            $ change_corruption_actor('alexia', -3)
            show rowan necklace neutral at midleft with dissolve
        else:
            ro "I understand you’re not… Properly accustomed to the realities of this place, but you need to accept the fact we’re not in Rosaria anymore."
            ro "I can’t be lenient on these people, and neither can you."
            $ change_corruption_actor('alexia', 3)
        ro "Will you try to keep your emotions under control?"
        if rowanTwoWorkers == 'kind':
            show alexia 2 necklace angry at midright with dissolve
        else:
            show alexia 2 necklace concerned at midright with dissolve
        "This wasn’t what she wanted to hear, but he didn’t have the time to sugarcoat things."
        show alexia 2 necklace neutral at midright with dissolve
        al "… Yes, I will."
        "He could only hope she actually meant it."
        ro "Alright. I have to go now."
        ro "Let’s just… Pretend this never happened."
        hide rowan with moveoutright
        al "Stay safe, my beloved."
        return
        
    "You don’t have time for this. Just pretend and tell her what she wants to hear." if all_actors['alexia'].relation < 50:
        $ released_fix_rollback()
        $ change_base_stat('c', 5)
        show rowan necklace angry at midleft with dissolve
        "Rowan barely stopped himself from rolling his eyes. NOW she’s remorseful..."
        show rowan necklace neutral at midleft with dissolve
        "He didn’t have time for this."
        if rowan_shares_room_with_helayna:
            "Helayna was never giving him so much trouble, and his wife wondered why he preferred her company."
        else:
            pass
        "He’ll just say what she wanted to hear, and be done with the topic."
        if check_skill(8, 'bluff')[0]:
            jump alBluffCheck
        else:
            $ change_relation('alexia', -10)
            ro "I should’ve been more understanding of your anger. You’re trapped with these people the entire week…"
            ro "When your only crime is being the wife of a hero."
            show alexia 2 necklace concerned at midright with dissolve
            ro "I’m sorry, for everything."
            if rowanTwoWorkers == 'harsh':
                ro "I’ve been making difficult choices my entire life. I’ve grown…"
                show alexia 2 necklace neutral at midright with dissolve
                ro "Desensitized, I guess."
                ro "I shouldn’t have shouted at you. I’m sorry."
                show alexia 2 necklace concerned at midright with dissolve
                al "It’s okay. I forgive you."
                ro "Thank you."
                ro "I’m sorry, for everything."
            else:
                pass
            "He hugged her close, giving her a quick kiss."
            "She didn’t return it."
            ro "And I love you. Stay safe."
            al "..."
            al "You be careful as well, my beloved."
            return
        
        
##########################################################################################################
##########################################################################################################
##########################################################################################################

label a_visit_to_Cliohna:

#cliohna lab bg
scene black with fade
show rowan necklace neutral at midleft with moveinleft

"Rowan entered one of the side rooms off of the library. It was one of the lab spaces, but Cliohna had partially converted it into a bedroom, having one of the barracks bunks installed as well as her personal furnishings."
"The room was a study in contrasts, plain bedding and linens on one side, magical apparatuses on the other, and in the middle Cliohna and her matching dresser and dressing table.  It certainly made some of her personal priorities rather clear."

show cliohna neutral at cliohnaright with dissolve

cl "Ah Rowan, how nice of you to join me this evening."

ro "It was an unusual request, one would almost think you were trying to seduce me."

cl "Why would I ever be required to do that? No, no, you're here for some experimenting but some physical fun is not entirely off the table either."

"She waved him inside, so Rowan took a few steps forwards and closed the door behind him. Normally a dangerous move, but it wasn't like running would have been terribly productive with a powerful magic user like Cliohna."

ro "Exactly what kind of experiment did you want to do on me this time?"

cl "During our last session you proved that you had the capacity to remove my influence from your mind and regain yourself. I wish to test the limits of that and learn how you manage it. Such a skill is rare and I wish not to miss this opportunity to study it."

menu:
    "I'd really rather not give away the one defence I've got against magic users.":
        $ released_fix_rollback()
        cl "A pity, I won't be able to force that information out of you either. Though... I cannot fault you for your prudence. I shall simply have to be patient and observe rather than experiment."
        ro "So I'm still an experiment subject to you then?"
        cl "Most people are. That will be all for this evening, please leave my chambers."
        return
        
    "Alright. I don't really understand it, I just do it by instinct.":
       $ released_fix_rollback() 
       pass

#cliohna lab bg
show black with flash

cl "Wonderful. {i}Strip{/i}."

show rowan necklace naked at midleft with dissolve

"Her voice wasn't just spoken, it was forced into his head as she employed magic to enforce her will once again. Like before, it overcame him in an instant and Rowan was compelled to obey."
"Somewhat stiffly, he removed his clothing, then stood there unable to act without Cliohna's orders."

cl "No resistance, no hesitation. I had thought that perhaps I had missed it, but no, you truly are in my power."
cl "You are a very handsome man Rowan. How fortunate for me that someone like you proved to be an interesting study after all."

"With her full attention on him, there was no way for Rowan to slip out of her control. He simply stood there, listening."

#CG of Cliohna kissing Rowan.
scene black with fade
show cliohna neutral behind black
show rowan necklace naked behind black

"To his surprise, Cliohna suddenly leaned forward and planted a kiss on his lips!  He still couldn't move, but a part of his mind could still think for itself."
"After a moment she removed her lips and instead wrapped her arms around him and pressed her exposed skin and modest breasts to his chest, snuggling in and laying several more kisses on his neck."

cl "Nothing?"

"The sorceress sounded disappointed, but not in the way that Rowan would have expected. It wasn't the same clinical disappointment that she used when her experiments failed to yield results, was is that she thought he didn't find her attractive or enjoy her attention?"

cl "Oh, it would seem I spoke too soon."

#Cliohna smiling CG variation.
scene black with fade
show cliohna neutral behind black
show rowan necklace naked behind black

"Leaning back into his vision so she could meet his eyes, Rowan saw that Cliohna was smiling now, then felt one of her hands run over his cock which had managed to become semi-erect even while he was under her power."

cl "You do find my form beautiful. You enjoy the touch of my smooth skin. The feeling of my lips upon you. Good."

"The last word was almost a purr as she once more leaned forwards and possessively wrapped her arms around him. A moment later her words hit him like a massive wave as her second command struck him."

cl "*Return my embrace.*"

"With no way to do otherwise, he mechanically hugged her. It was strange, like he was wearing clothing that had a mind of its own. He could feel Cliohna just fine, but couldn't shift his arms at all."

cl "Hmm, I can feel the edge of you sliding around my will. Trying to do more than what I have given you permission to do."

"A soft shiver ran through her form."

cl "You want me so much. You desire me, desire to be inside me. Yes... yes you should desire me. No man wouldn't."

"A drop of some liquid fell on Rowan's foot. He found he could cast his eyes down, but couldn't see what had happened because Cliohna was in the way. Instead he saw her hair and was reminded that his arms were currently wrapped about her."
"To his surprise, he realized that he had also started lightly brushing his fingers up and down her back, rubbing her as part of the hug. He stopped in surprise, which made Cliohna look up at him and note the direction of his eyes."

cl "I have allowed myself to become distracted, and without even realizing it that in turn allowed you the chance to slip out from under me."

"Another drop struck his foot while the sorceress studied him."

cl "It mattered not that you were enthralled by my beauty, or perhaps it was that enthrallment that allowed you to throw off my other influence?"

"A surprisingly giddy smile lit up her face now as she pushed Rowan away from her and took a few steps away. Now the man could see that at some point she'd unclasped her lower garments, leaving her nether lips bare which glistened with the moisture of arousal."

cl "Oh Rowan, you're so hard now! How about we complete this session with something more physical. I apologize that I won't be allowing you to do as you wish to me, but you will experience what we both desire now."

#CG of Cliohna standing fucking with Rowan.
scene black with fade
show cliohna neutral behind black

"Once more approaching him, she lifted up a knee, extended her leg, and rested it on his shoulder. Then she settled herself down onto his shaft, enveloping his length in her overaroused interior."

cl "Fucking... hero."

"In a moment her passage was quivering around him, accompanied by a sudden rush of fluids down the passage."

cl "Come on, cum!"

"She jerked her hips several times, trying to get Rowan off.  Then a moment later he felt her will reassert itself on him."

cl "*Cum damn it!*"

#CG cumshot variant
scene black with fade
show cliohna neutral behind black

"The command was shaky, but still strong enough to force Rowan to let loose into her almost spent passage. Afterwards however, the hero found that his will and body where once again his own, even as his forced orgasm let out its final spurt."

cl "Hah, you are very formidable."

"She was struggling to catch her breath as she lowered her leg and stepped away. The giddiness and unusual agitation was still there, but were quickly evaporating back into the normal cool reserved librarian."

scene black with fade
show cliohna neutral behind black

cl "It would seem that I allowed myself to become somewhat over excited by the experimentation. We shall have to continue this at another time, but rest assured that I very much want to see the extent of your desire once again when our masters do not have need of you."

return


##########################################################################################################
##########################################################################################################
##########################################################################################################

label rowan_picnic:

#Cg 1- Rowan and Alexia in the woods
show bg3 with fade
show rowan necklace happy at midleft with dissolve
show alexia 2 necklace happy at midright with dissolve

al "It's been so long since we went into the Western forest for a picnic."

ro "It has, nice to finally relax and just enjoy one another like this."

"The two of them were in the forest outside Bloodmeen, hand in hand with a picnic basket under Alexia's arm. Jezera had allowed them a chance to spend a few hours outside together, so they were going to make the most of it."
"Rowan's inner tracker made it painfully obvious that this place was nothing like the Western Forest he'd grown up in and only reminded him of the end of the war.  However, he was glad that Alexia could appreciate the place for him."

if avatar.corruption < 31:
    "Oh, Solansia it felt nice to have her at his side for something so innocent and loving as a picnic. He might not feel familiar in this place, but the way they held one another and their intentions reminded him of being two young love birds again."
    
else:
    pass
    
"They slowed momentarily, allowing Alexia to lean against her lover and then press into him. Rowan responded to her affections by drawing her into a hug and brushing his hand over her hair several times."

al "Oh my beloved, I love you."

"He kissed the top of her head, then glanced about the small clearing they'd stopped in. There was some soft grass underfoot with wildflowers blooming between the blades."

ro "You have a good sense for picnic places. Shall I help you with the spread?"

al "How about you make sure no one is going to peak in on us instead? I think I can manage here."

if society_type == "feudal":
    ro "Of course, my lady."
    
else:
    ro "I'll see what I can do, my love."

"He slipped back into the woods while Alexia busied herself with laying down a blanket and extracting their food and drink from the basket."
"A few minutes later of making sure no demons or gossipers had decided to crash their picnic or snoop on them, Rowan returned and seated himself next to Alexia. Together they looked out on the meadow for several seconds before Alexia broke the silence."

al "So, shall we eat?"

#cg2 - rowan and alexia eating

"Alexia had packed them muffins, cheese, and some wine. As Rowan took his first bite, it was quite the rush of nostalgia."

ro "Oh my, it's been so long since you made these. You use to make them all the time."

al "With mother and father at the bakery. I made them so often that when I married you I vowed never to have to do it again. I remembered the other day how much you loved it when I gave you one, so I thought I should make them again for this special day."

ro "I wouldn't want you to make something like this on my behalf if you hate doing it-"

al "Hush darling. That was after making the same muffins every other day for nearly twenty years. It's been so long I missed doing it too, this was as much a treat for you as it was for me."

"She laid her hand on his, then brought up her glass for a toast."

al "To happy memories."

ro "To happy memories."

"He agreed and they drank."
"Rowan closed his eyes and leaned against Alexia while the warm sun shone down on him through a gap in the trees. His mind swam with those happy memories, thinking of all the joy he'd had with the woman next to him."

menu:
    "Kiss her.":
        $ released_fix_rollback()
        jump rowanPicnicSex
        
    "Just enjoy Alexia's company.":
        $ released_fix_rollback()
        "This moment was something to be treasured. A moment they would recall as a happy memory as well. There were precious few of them these days."
        $ change_base_stat('c', -5)
        $ change_corruption_actor('alexia', -5)
        $ change_relation('alexia', 10)
        return

label rowanPicnicSex:

"He shifted, opening his eyes and looking down to see that his wife was glancing in his direction too. That beautiful face, leaning down, their eyes closed again as their lips met in a kiss."
"At first it was simply a brush of the lips, then another, and soon both had their tongues inside each others mouths. Passions flared for both of them as they embraced and gripped one another, exploring both their bodies and finding both wanted what would come next."
"Rowan slipped free of his wife's lips, going down and kissing her neck, then her collar.  After a moment's fumbling, Alexia managed to get her hand on his growing arousal, fondling him through his pants."

al "Rowan, my beloved, I feel like it's the spring festival all over again."

"Continuing his journey downwards, momentarily flicking the amulet around behind Alexia in annoyance, allowing him to get down unimpeded. Alexia helped him along by slipping her dress off her shoulders and letting him get down to her breasts."
"Upon reaching her nipples and laying a kiss upon them, Alexia let out a small groan of both pleasure and frustration, as Rowan's cock had now slipped beyond her reach. Fortunately she managed to solve that problem with her knee after squirming around for a bit."

ro "Getting a bit creative now? Careful you don't hurt me like that."

al "I'll try... eh!"

"The cry of surprise came as Rowan nibbled on her, causing a jolt to go through her and very nearly jamming her knee into Rowan's stomach. Mocking pain, Rowan once again looked up at Alexia with a smile."

ro "Ouch, that hurt!"

al "Hey! You can't be doing that to me and expect I can control myself!"

ro "What, this?"

"He nibbled her again, prompting another jolt and this time Alexia kneed him in the belly intentionally."

ro "Oof."

al "Ouch!"

"Unfortunately she ended up hitting one of his belt buckles, doing more damage to herself than Rowan. They both looked at one another in surprise for a beat, then burst out laughing."

al "Look at us, the most romantic of all couples!"

ro "Honestly, would you have it any other way?"

"She drew him against her bare chest, cradling her husband's head against her breasts for a moment before answering."

al "No. You're perfect just the way you are my darling."

if alexiaAndrasSex > 0 or alexiaJezeraSex > 0:
    "She meant it. In spite of her breaking her vows with their captors, Alexia did truly love Rowan as he was more than anything else."
else:
    pass
    
#sex cg
scene cg271 with fade
show rowan necklace naked aroused behind cg271
show alexia necklace naked aroused behind cg271
pause 3

"She shifted under him, leaning backwards on the blanket and lifting her legs up to present herself to her beloved husband. Well that was a pretty clear sign that the foreplay was over."
"It only took another moment to free his cock and shift Alexia's panties aside so that he could press himself inside her womanhood."

scene cg272 with dissolve
pause 1
scene cg271 with dissolve
pause 1
scene cg272 with dissolve
pause 1
scene cg273 with dissolve
show rowan necklace naked aroused behind cg273
show alexia necklace naked aroused behind cg273
pause 2

"As one they let out a long breath of relief and extacy.  Rowan dove in and out, falling into a well known and well practised rhythm, just as fast as he knew Alexia wanted and the best pace for him to enjoy the lovemaking as just that."

al "There's one thing that you've gotten a lot better at from all those years ago."

"A blush went to Rowan's cheeks. That was one part of that night he didn't like to think about."

ro "I should hope so!"

scene cg274 with dissolve
pause 1
scene cg275 with dissolve
show rowan necklace naked aroused behind cg275
show alexia necklace naked aroused behind cg275
pause 2

"He focused instead on the feeling of Alexia's walls squeezing down around his shaft and the way her breasts rolled with each steady thrust inward. Warmth filled him as he felt his climax arrive. Luckily Alexia also followed him soon after, before his orgasm completely finished."

al "Good enough we can cum together... I love you Rowan."

ro "I love you too Alexia."

scene cg276 with dissolve
show rowan necklace naked aroused behind cg276
show alexia necklace naked aroused behind cg276
pause 3

"They kissed once more, Rowan still leaning over her."

al "Oof, I think I need to set my legs down now."

scene cg277 with dissolve
show rowan necklace naked aroused behind cg277
show alexia necklace naked aroused behind cg277
pause 3

ro "Oh sorry. There you go."

al "Thanks darling."

"Now sitting, she kissed him again to make up for cutting off the one while they were linked."

ro "After that workout, I think I could do with another muffin."

al "Here you are, there's plenty left."

$ change_base_stat('c', -3)
$ change_corruption_actor('alexia', -3)
$ change_relation('alexia', 10)
return

##########################################################################################################
##########################################################################################################
##########################################################################################################

label helaynas_help:
    
scene bg9 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan sat hunched over a map. Some orcs had gotten into an engagement the week before, and unless they retreated a second fight was likely. Some of the other local commanders had offered suggestions earlier.  They weren’t much good."
"He’d asked them to leave to consider it alone. Sometimes Rowan felt like he was the only one in the entire castle who understood tactics."
"Click."
"Rowan turned around. The door opened. But, when he saw who was in the door frame his expression softened."

if helPath == "bedslave":
    #hel collar happy
    show helayna collar neutral at midright with moveinright
    
else:
    show helayna 2 happy at midright with moveinright
    
hel "My love? You’ve been cramped up in here all day. I wanted to bring you some tea. You can’t plan on no food or drink."

show rowan necklace happy at midleft with dissolve

"Rowan leaned back in his chair, and welcomed her to his side. Perhaps a bit less stress might help with the work. When his lover approached, he planted a small peck on her cheek."

hel "What is that?"

ro "The week’s campaign map. A band of raiders got caught by the local forces on a raiding mission. I’ve been deciding whether to pull them out via portal or try to make a stand with them."

"Helayna squinted hard. Rowan took a sip of the tea she prepared. Helayna was not much of a domestic, but the tea was serviceable."

hel "Here."

"She suddenly pressed her finger to a spot on the map. Heavy elevation and a tree line."

hel "You don’t have to pull them out or make stand. I was never much of a tactician, but I knew you don’t charge lightly equipped orcs on a high ground with footmen weighed down by heavy armor."
hel "If you move them here, there’s a good chance the commander doesn’t bother making the attack. He might win, but he’d lose two men for every orc killed. He’d just back off."

"Rowan studied the position. Was she right?" 
"He was still focusing on it when he felt a kiss on his cheek. Helayna’s heart shaped rear swayed gently as she walked out of the room. Rowan found it impossible not to look. "

hel "Good luck with the planning, my love. You know where to find me...when you’re done…"

"She smirked at him and then vanished."

hide helayna with moveoutright

"Rowan focused back on the map. He didn’t have any better ideas, and his lover did make a point. When Rowan sent out his orders an hour later, he directed the band to take the position Helayna had suggested."
"No use taking much longer to decide. It would be a shame to keep a good commander waiting."

$ change_recruitment_bonus('barracks', 2)
return


