init python:
    #Back for Seconds
    #Requirements: after week 16, Jezera Influence is at least 5
    event('back_for_seconds', triggers='week_end', conditions=('week>=16', 'week<=34'), group='ruler_event', run_count=1, priority=pr_ruler)

label back_for_seconds:
#Back for Seconds
#Requirements: after week 16, Jezera Influence is at least 5

#if alexia is in rowan's room
if alexiaSeparateRoom:
    scene bg7 with fade
else:
    scene bg9 with fade

#rejoin
show alexia necklace naked neutral at midleft with dissolve

"Alexia was rummaging through her closet, searching for the day’s outfit, when she was surprised by the sudden appearance of a maid in the doorway. When had she even gotten in? The maid was a meek girl with braided red hair and freckles."
"Alexia threw her hands over her body, covering her nakedness."

show alexia necklace naked shock at midleft with dissolve

maid "Mistress Jezera would like you to join her in the parlor for a lunchtime tea shortly."

"The girl didn’t even look at her creamy nudity before turning and starting down the hallway. She left the housewife to close the door after her. "

show alexia necklace naked concerned at midleft with dissolve

"Alexia, shivered slightly. The prospect of a teatime chat with Jezera could be...dangerous."

#if visiting Jezera was chosen during the Demon Tome event
if alexia_and_her_demon_book == 3:
    "Alexia still remembered the last time she’d sat with Jezera for tea. Or at least she remembered part of it. Hazy visions of her body dancing and swaying in the air under Jezera’s hungry watchful eyes."
    if alexia_has_sex_with_jezera_during_demon_book:
        "Then what came afterwards. Soft feminine fingers exploring her. A tongue against her slit. Her tongue against another slit. Things she should never have enjoyed."
    else:
        "It had been providence that she’d had the willpower to leave before anything...untoward happened. Still, the thought of what the demoness might have done to her still lingered in the back of her mind."
        "And Jezera wanted her company once again..."
else:
    "For all the interest the demoness had shown in her in the past, she’d never once been called to tea before. While perhaps it was just an innocent lunch date, Alexia would have to be a fool at this point to trust the demoness not to take advantage of the situation."
    "The question was, if Alexia went along with it, would she have the willpower to prevent said advantage being taken…"

#rejoin (from demon tome if/else)
"Alexia sighed, rifling quickly through the closet to find something to cover herself with. Then she rushed down the hall, seeking to catch up to the redheaded maid."

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

al "I have a message that I want you to bring back to Lady Jezera."

menu:
    "Make an excuse.":
        $ released_fix_rollback()
        al "Please tell the lady that I deeply apologize, but I will not be able to attend today. I have urgent business that I need to focus on, and I beg her leave to allow me to complete my needed tasks, for the good of the war effort."
        "Jezera wasn’t going to be happy about this, but so long as it was sugar coated properly, Alexia hoped that she wouldn’t earn the woman’s wrath."
        maid "Ar...are you certain about this? The mistress will not be pleased."
        "The look in the girl’s eyes told Alexia that this displeasure was very likely to affect the girl personally. Still, she had to remain resolute. "
        al "I am certain. It really cannot work today with the current schedule. Please give her my fondest regards."
        "The maid nodded and left to deliver the message. Clearly it must have worked, since Alexia heard nothing more of the manner for the rest of the day. No angry rants, no further insistence on her attendance, not even a passive aggressive reply."
        "Still there was a moment where she was almost certain she heard Jezera fuming from her room as she passed by. Alexia felt a strange stirring of pride at that."
        #Alexia loses 2 Jezera influence
        $ change_relation('jezera', -2)
        return

    "Accept the command.":
        $ released_fix_rollback()
        al "Please tell her that I humbly accept her invitation and will be along in a timely manner."
        "The maid smiled softly. She looked almost relieved."
        maid "Of course, madam Alexia. I will tell the mistress to expect you. She will be most pleased to hear of your attendance. I believe she was looking forward to it."
        "The maid returned to Jezera’s room, leaving Alexia to wonder if she’d made the right choice."
        #if rowan's influence on Alexia is 10 more than Jezera's
        if  all_actors['alexia'].relation - all_actors['alexia'].flags['jezera_influence'] > 10:
            "She brought a hand to the amulet around her neck softly."
            al "This would be much easier if you were here today, Rowan. I never know what to do around those two…"
        else:
            "She tried to think about her husband and her vows to him, but the longer she thought about her upcoming visit, the harder it was to stop from blushing."
        #rejoin
        jump secondsTea

label secondsTea:

scene bg18 with fade
show jezera happy at midright with dissolve
show alexia 2 necklace concerned at midleft with moveinleft

"Alexia walked into Jezera’s room and found the blue woman sitting on a small wooden chair at a low table. Jezera happily waved to her as soon as she arrived, as if the two were a pair of friends having a casual sit in."
"She also noted that the red haired maid from earlier was still hovering around, still maintaining her eyes to the ground. Only now she had a unmistakeable soft pinkish hew to her cheeks."
"Then Alexia noticed an issue."

al "Is there nowhere for me to sit, my lady?"

"There wasn’t another chair in the entire room. Well, a large one near the back, but it was obviously unsuited for this kind of lunchtime nicety."

je "Nowhere to...Oh. Oh, of course. How silly. I must have forgotten to bring up something as simple as another chair in all my excitement."

#if rowan's influence on Alexia is 10 more than Jezera's
if all_actors['alexia'].relation - all_actors['alexia'].flags['jezera_influence'] > 10:
    "Alexia furrowed her brow softly. This had to be some sort of trick or power play. She didn’t trust it for the moment. Still, there was little to be done in the situation."
    "She had a sneaking suspicion that if she tried to insist on a chair be brought, that Jezera would wave her concern off."
else:
    show alexia 2 necklace aroused at midleft with dissolve
    "Alexia instantly turned a shade pinker. She had no illusions that this was actually an accident. It was no doubt meant to force Alexia to sit at the other woman’s feet. The mental image was...effecting."
#rejoin
je "We must have somewhere for our poor darling guest to sit. It would be so rude otherwise."
je "I’ve got it!"
je "Would you be a dear and get some of the cushions from the armoire? The red velvet ones. If I lack a chair for the poor girl, the least I can do is provide somewhere comfortable for her to recline."

maid "Of course, Mistress."

"Alexia eyed the cushions wearily, but had little choice but to kneel down on them. Trying her best to maintain enough height to come close to matching her host at the table."

#CG 1 Variation 1
scene black with fade
show jezera happy behind black
show alexia 2 necklace neutral behind black

"In this position, if she stopped forcing herself up towards the table for a second, then she’d be practically kneeling at Jezera’s feet."
"The maid, Amelia, soon came around with tea. Of course, it tasted delicious. A fine black that must have come from the twins’ private stores directly."
"Alexia sipped the drink down and laughed along at the conversation. She couldn’t show her discomfort with the situation."
"Alexia would occasionally catch a glimpse of Jezera putting a hand on Amelia’s thigh, or otherwise catching a glance at the girl’s behind whenever her skirt would ride up from some action. However, she just couldn’t connect the dots of their relationship."
"Eventually the conversation turned, of all things, to stories from their hometowns."

je "So, there was this old woman in my hometown who I’d talk to sometimes. She was quite wealthy, so it quite literally paid to be in her favour. And she had this majestic story."
je "See, she was born a commoner."

"Alexia felt the weight of Jezera’s gaze on her."

je "She eventually married this merchant. From an entire family of merchants. They ran all sorts of trade ships running to and from Travelers Rest. Nice enough man, I was told. She said they were happy together."
je "Then he died. Pirates, I think? Perhaps minotaurs. It was some time, and you humans are all so fragile."
je "Anyway, she was to be left with his entire fortune. It was riches to last many a mortal lifetime. Only there was a problem. His older brother was also a merchant, and he laid claim to the fortune as well."

"Alexia almost unconsciously lowered back into her cushion, temporarily distracted from Jezera’s power plays by the story."

je "She couldn’t fight him for influence with his own family as the judge. She couldn’t run away with the money, since so much of it was tied to property and that paper nonsense you humans use."
je "So she...actually, no. Let’s play a little game first. Fun, no? What would you do in that situation? How would you protect your newly acquired wealth?"

"Alexia paused. What would she do in that situation? Alexia had never dealt with matters of inheritance and intrigue before she’d come to Bloodmeen. She was a housewife, damnit."

al "May I think about that for a moment, m’lady?"

je "Why of course. I want to see the little gears in your mind turn."

"Jezera leaned back into her seat, taking a sip of tea and letting out a sigh."

je "Though, perhaps you’d be kind enough to help me something. These boots are just murder on my feet. Heels are a curse I have to bear too often."
je "Would you be a good girl and take them off for me?"

"Alexia blushed softly, briefly broken from her line of thought."
"The optics of such a request were...less than benign. She glanced backwards to where Amelia stoically stood. Still, she had no grounds to refuse. And it was an innocuous request."

al "Oh. Um, of course."

#CG 1 Variation 2
scene black with fade
show jezera happy behind black
show alexia 2 necklace neutral behind black

"Jezera crossed her legs, placing her right leg close to Alexia. For the first time, Alexia noticed that her head was nearly level with the other woman’s raised foot. It was humbling."
"Wordlessly, she took the foot and undid the laces, letting the boot fall to the ground at her side."
"Jezera re-crossed her legs, giving Alexia the other boot to remove. Alexia’s fingers trembled as she undid the laces and removed the boot. For the briefest second, her hands touched the sole of Jezera’s foot. It was hard not to dwell on..."

je "So did you arrive at an answer to what you would do about the inheritance."

"She snapped to get Alexia’s attention. Alexia looked up, almost gasping. How had she gotten so distracted?"

al "I believe so."

"She breathed in and rose slightly to face Jezera on a more even level. "

al "I think I would fight for what was mine. I’m not Rowan, and I’m not much of a soldier. But, if I had money, I could pay for someone who was. Force them to back down."

je "Not a bad answer, I suppose. Certainly more ambitious than I’d expect from a human girl with less...potential. But it has a problem. "
je "You’d only have your own money to hire sellswords with. He could go to your same sellswords and offer then whatever you were paying them plus extra."
je "That’s the problem with sell swords. You can never trust them. Liars, cheats, and backstabbers, the lot of them. Though, they can be useful in the right circumstance."

al "Then what did the woman do?"

je "Simple. She married the brother."

al "She...married him?"

je "Exactly. She was still young and pretty. He didn’t have a wife. So the minute he put in his claim, she offered to make it easy by tying the knot."
je "Of course, she poisoned him a year later. She couldn’t just take his earlier disrespect lying down, so to speak. However, once he was gone, she had the wisdom to secure both brothers fortunes before anyone else could lay a claim."
je "Once you expand the possibilities, you’d be astonished what power a woman of intelligence and beauty can amass."
je "My foot still aches. Be a dear and massage it for me, won’t you darling?"

"Alexia felt the urge to protest rise, but it was silenced by a leering glance from Jezera. She was in control here. Alexia mumbled softly to herself, but grabbed the foot that was offered it, and softly rubbed all over it."
"It was strangely soft. Feminine. She noted to herself just how little it felt like her husband’s foot."

je "Still, your idea, the mercenaries, had potential. Perhaps he might have been able to pay higher then you, but there is always a counterplay to that move."

al "A counter?"

je "Of course! Just, fuck the mercenary captain. Then it doesn’t matter how much more he offers. So long as one of his subordinates doesn’t off him. Haha."

"Alexia gasped. The idea was so lewd. Still, it brought back memories of the way she might perk up her breasts when making a request from one of the local men in town, and of course of all the eyes on her when she’d dance by the firelight."
"Once more, conversation with Jezera had distracted her. Without focusing on keeping control of herself, she’d been getting steadily more absorbed with rubbing the other woman’s foot. Her fingers and thumbs lavished attention into her skin."
"There was a brief pause in the conversation. Alexia’s eyes slipped lower to the bare foot in front of her. Her lips parted slightly. A passing thought ran through her head. A vague curiosity that she’d never thought herself capable of."
"What did Jezera’s foot taste like?"

je "You’re staring, darling."

"Alexia started to gasp out some kind reply, but Jezera simple leaned down, covering her mouth with a single finger."

je "You almost look like you want to give them a kiss. There’s no shame in that. You’re not the first girl whose wanted that. Why don’t you give my foot a small peck. Try it."
je "Maybe. Just maybe. You’ll like it."

"Alexia still couldn’t muster the words to speak. Jezera was right. Alexia knew it. She did want to try it. She did want to lean down and kiss her foot."
"Rowan’s words rang in her temples. She shouldn’t trust the twins. They were always up to something. What would he say if she knew she was so much as considering this?"

#if alexia had sex with Jezera in the Demon Tome update
if alexia_has_sex_with_jezera_during_demon_book:
    "Dark images clouded her mind once more. The night she’d taken tea with Jezera. The time she’d tasted the other woman’s pussy. Kneeling here, in this moment, she could almost taste it again on the tip of her tongue."
else:
    pass

#rejoin
menu:
    "Get out of there.":
        $ released_fix_rollback()
        scene bg18 with fade
        show jezera happy at midright with dissolve
        show alexia 2 necklace concerned at midleft with dissolve
        al "I…"
        je "That’s right. There’s nothing wrong with you wanting to…"
        al "I...I have to go."
        "Without warning Alexia rose to her feet. Her cheeks were burning bright bright red. Jezera tried to calm her down. Told her everything was alright. None of it had any effect. Alexia stormed to the door, now nearly bursting with tears."
        "She slammed the door shut behind her as she left. In the process, she left a slightly shocked Jezera sighing in her chair."
        hide alexia with moveoutleft
        je "And I was so close this time too…"
        je "I suppose this is my punishment for getting overconfident. Isn’t that right Amelia?"
        ame "Yes, mistress. Anything you say, mistress."
        je "Exactly. Now then, join me girl. I have some frustrations to relieve…"
        #if alexia is not in rowan's room
        if alexiaSeparateRoom:
            scene bg7 with fade
        else:
            scene bg9 with fade
        #rejoin
        show alexia 2 necklace concerned at midleft with dissolve
        "Alexia jumped on her bed, nearly sobbing. It wasn’t anything that she’d actually done. It wasn’t the temptress’ words. It was the fact that for one brief moment there, she’d considered going along with what Jezera said."
        "In that moment, just turning off her mind for one brief second and doing what the other woman said had seemed so easy."
        "If she didn’t watch herself around Jezera, next time would she have done what Jezera wanted? What would Rowan say if he found out? Alexia definitely didn’t want to think about that bit."
        return

    "Give in." if NTR == True:
        $ released_fix_rollback()
        jump secondsSex

label secondsSex:

#CG 1 Variation 3
scene black with fade
show jezera happy behind black
show alexia 2 necklace neutral behind black

"Alexia leaned down, barely even able to construct a coherent thought. There was something almost sweet smelling about Jezera’s blue skin. Was it because of her demonic powers? "
"Then she gave Jezera’s foot a soft peck. It was tepid. But, without even being prompted further, it was followed by another. And another. Just like that, Alexia was lost in a cloudy haze, kneeling beneath Jezera and kissing her feet."
"She told herself earlier that she’d be stronger then this. And yet, here she was. Her cheeks burned with shame, but she didn’t stop kissing."
"Jezera leaned back in her chair and turned her attention to her tea. It was almost as if Alexia was too beneath her notice to hold a conversation like this."
"Once more, the dynamic continued until what had first been unthinkable had again become routine. Her soft pecks turned to fuller deeper kisses. It was like the smaller, weaker, kisses wouldn’t satisfy her anymore."
"But, it didn’t stop there either."

je "Aww, did you just lick my foot? I didn’t even tell you to do that, girl."

"Alexia noticed what had happened. Jezera was right. Without even thinking about it, she’d just run her tongue not just over the dominant woman’s foot, but even part of the way up her leg."
"She lowered her eyes. She felt weak. Pathetic. Why was she doing this?"

je "I didn’t tell you to stop now, did I? Keep going?"

"And just like that, she was back at it. Only this time there was nothing tepid or even restrained about it. Now framed as an order, there was a net for Alexia to fall back on."
"She wasn’t furiously tounging this other woman’s leg because she wanted to. Because she was too weak to resist. She didn’t have a choice. It was so easy to just give in and obey when given that lifeline."
"Her tongue worked hard, lapping at Jezera’s heels like a dog. Her nose was assaulted by a scent coming from between Jezera’s legs."
"Among the few thoughts that pierced the vale was another step of curiosity. What would it taste like if she raised her head ever so slightly."
"She barely paid attention to the fact that she had an audience. That Amelia, the maid, was watching her from her corner silently. If she’d bothered to pay attention, she might even notice the girl’s breath starting to grow shallower."
"Jezera though? It seemed like Jezera was paying less attention than anyone. She moved her feet around with seemingly no regard for where it would be comfortable for Alexia."
"It forced her to crane her neck up and down to follow along Jezera’s foot."
"There was something strange about the woman’s indifference. It made her heart beat faster. It made Alexia want to lick and lick until Jezera noticed her. It made her want to lick until she was worth being noticed."
"It must have been more then ten minutes before Alexia worked up the heart to do what she really wanted. What her body was aching for."
"She ran her tongue along Jezera’s foot, only instead of stopping below her knee, she kept on going, this time rising closer to Jezera’s inner thigh."
"She was running entirely on instinct now."
"Only, Jezera didn’t let her. Alexia was stopped, within mere inches of the other woman’s sex, by Jezera’s hand on her head. She almost whined."

je "Uh uh uh. I didn’t say you could go that far now, did I?"

"Alexia flushed crimson. She tried to mumble out some kind of apology, but she was far too mortified to even speak."

je "Though...I think I have an idea."

"Jezera leaned back in her chair. She was flashing an evil smirk. Like a predator who her prey right where she wanted it."
"If Alexia could even think properly, she’d be forced to admit there was something intoxicating about being viewed under those eyes."

je "I want you too...hrm...let’s see. I want you to take off your dress, and then kneel straight up with your legs spread and your hands behind your head."

"She snapped her fingers."

"Alexia gasped softly, a moment of sanity returning. Was she really doing this? Had she really almost done that? Maybe, she should just go now?"

scene cg203 with fade
show jezera happy behind cg203
show alexia necklace naked aroused behind cg203
pause 3

"As she thought all that, her hands were shakily undoing her dress, letting it fall off her body and exposing her undergarments to the temptress. Jezera smiled, especially when she caught sight of the dark patch on the front of Alexia’s panties."
"Alexia straightened her back, adopting the posture Jezera had specified. Hands on the back of her head, kneeling, but with her knees spread apart. Raised from the ground. It was humiliating, like a display position. That meant it was arousing too."
"And that was before, Jezera raised her leg, placing it between Alexia’s spread thighs. Her foot just hovered there. Inches from Alexia’s crotch. It was as though it was bathing in the warmth of it. Alexia whimpered softly."

je "Oh, you’re adorable. You’re practically shivering. Isn’t it cute, Amelia?"

"The maid didn’t respond. She merely kept her eyes on the ground, blushing dark red."

je "I bet your body is just...aching...for me to raise my foot just a bit. Only a little bit. To let you rub that dripping pussy all over it. You can’t hide it from me."

"She couldn't. Her body was practically squirming with need. Squirming with helplessness."

je "Beg for me for it. Maybe if you ask me nicely, I’ll let you grind that greedy little cunt of yours all over my foot."

menu:
    "Debase herself":
        $ released_fix_rollback()
        "There was no hesitation left in Alexia. All of her caution, all of her shame, all of her dignity had dripped out between her legs. When her voice raised, it was hoarse with desperation."
        al "Please. I. Please, I need it. Please let me rub myself against you…"
        "Jezera grinned wide, flashing her teeth. But, she simply raised her finger, ticking it back and forth in a disappointed gesture."
        je "One more time. It’s “Mistress Jezera”."
        "Alexia squealed pathetically, but otherwise offered no further resistance."
        al "Please please please, Mistress Jezera. Please let me rub myself against you..."

    "Try to fight it.":
        $ released_fix_rollback()
        "Alexia still had a lingering sense of hesitation. A feeling that this wasn’t right. She was still whimpering and squirming. She didn’t even change her posture. Yet, part of her was still fighting."
        al "I. Please. I’m not going...I can’t…"
        "Jezera leaned down, looking her dead in the eyes. Naked, submissive, helpless. It was so hard for Alexia to match her gaze for even a second."
        je "I think you can. I think you will."
        al "Please...no….I…."
        je "Or, perhaps I should tease you more and more and more, until you break. Until your little cunny can’t stand it anymore. You can’t resist me."
        "She smirked softly."
        je "You’re going to beg, Alexia. The question is, are you going to do this the easy way, or the hard way?"
        "Alexia gasped, but otherwise didn’t respond. She knew what Jezera said was the truth. She couldn’t resist her. Not now. Not like this."
        al "Please. I. Please, I need it. Please let me rub myself against you…"
        "Jezera grinned wide, flashing her teeth. But, she simply raised her finger, ticking it back and forth in a disappointed gesture."
        je "One more time. It’s “Mistress Jezera”."
        "Alexia squealed pathetically, but otherwise offered no further resistance."
        al "Please please please, Mistress Jezera. Please let me rub myself against you..."

je "Well there we go. Wasn’t that easy?"


scene cg204 with fade
pause 3

"Before Alexia could respond, Jezera pushed her foot up ever so slightly. Now it was digging into her pussy, making it ever so easy for Alexia to grind into it. To rub into it. To throw her pussy against as though she were an animal in heat trying to get off."
"Alexia gasped loudly at the sensation. Jezera’s foot was so soft. She’d never even considered doing something like this before. Fucking another person’s foot. Another woman’s foot. It was so shameful. So degrading. But, why did it feel so good."
"Jezera didn’t even work. She didn’t move her foot. It was as though any further effort on her part was beneath her. She regarded Alexia, in all her open sluttyness, with something between amusement and disgust. A potent emotional hammer."
"Alexia ground and ground until she was lost in the motion. Her hips pumped and thrusted, trying to eek out every last drop of stimulation it could get from contact with the other woman."
"The bottom of her panties were brushed to the side by the motion, just so she could a little more stimulation. Drops of wetness, Alexia’s juices, dripped down the side of Jezera’s foot, pooling at her heel. They made a tiny dripping sound when they hit the cushion."

scene cg205 with dissolve
pause 3

"Time seemed to lose meaning. The passing from moment to moment was defined first and foremost by the rise of pressure between her legs. Like a tide rolling in and receding, but coming in higher each time. The tide rose and rose with each mewl from her lips and each desperate buck of her hips."
"It seemed to go on forever. Part of Alexia wanted it to go on forever."
"Of course, it ended how these things so often do. There was a flash of pleasure and then a plateau of powerful waves coursing throughout her body. Alexia squealed loudly into the air as she came just from riding Jezera’s stationary foot."
"Jezera smiled."
"Exhausted, she fell to the ground, nearly curling up at the foot of Jezera’s chair. She whimpered softly. That had been draining. Physically yes, but emotionally more than anything."

scene bg18 with fade
show jezera happy at midright with dissolve
show alexia necklace naked concerned at midleft with moveinleft

"Which is why it felt so strange when her hair was parted by the brush of a hand through it. Was Jezera...petting her? And if so, why did it feel good? Why did it make her feel, if anything, somewhat comforted."
"Alexia groaned softly. This was wrong. Everything was wrong. She was a married woman. Rowan’s wife. What was she doing, cooing at the feet of this woman half naked like some pet?"

je "Adorable. Simply the cutest. I knew you had that in you. "

#if alexia and jezera had sex during the demon tome event
if alexia_has_sex_with_jezera_during_demon_book:
    je "Of course, there was that earlier, incident. But, I think it’s oh so much more an interesting experience when you’re not half a zombie. "
else:
    pass

#rejoin
je "I think that works wonders as a start to the afternoon, but I was intending for more amusements then that."

"She scritched Alexia’s scalp softly."

je "If you want, you can stay. You did so seem to want to taste me earlier, after all…"

"Alexia, slowly backed away, still crawling on the ground. Jezera’s hand reached out slightly as the girl pulled from her grasp."
"She gasped loudly, trying to catch her breath. Trying to catch her thoughts. She’d just...she’d just...Alexia’s cheeks burned."

al "No...I, uh...I can’t, uh…"

je "Sure you can. Can you really tell me that it wouldn’t be oh so much fun? Just spending the day as my little playtoy? If you hate the idea so much, then what was that a moment ago?"

"Alexia backed to the door slowly. Jezera, perhaps, could have easily stopped her. Yet, the demoness held back. She almost seemed satisfied with the day’s progress."

al "Please. I. Uh…."

"Without even managing the illusion of polite niceties, Alexia burst through the door of the room, forcing herself back into her dress as she ran down the hallway. She was trying to get anywhere, anywhere at all, if it meant being out of that room."

hide alexia with moveoutleft

"The smile never left Jezera’s face for a moment."

je "A pity. She’s going to miss the best part. Ah well. There is always next time after all."

"She beckoned to Amelia."

je "Over here, doll. I think I have a few urges to relieve."

#alexia gains 3 jezera influence
$ change_relation('jezera', 3)
$ alexiaUnfaithful = True
$ alexiaJezeraSex =+ 1

return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

init python:
    #Resistance. Futile?
    # If serveChoice = 4, it should happen in week 6-9, else week 10-14
    event('resistance_futile', triggers='week_end', conditions=('week>=6', 'week<=9', 'serveChoice==4'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    event('resistance_futile', triggers='week_end', conditions=('week>=14', 'week<=16'), group='ruler_event', run_count=1, priority=pr_ruler_high)

label resistance_futile:

#rowan's chambers night
scene bg9 with fade
show rowan necklace neutral at midleft with dissolve

"Of late, sleep had often not come to Rowan easily. With so many matters on his mind, and so many of his ideals being challenged, he was frequently left tossing and turning."
"Today, the subject on his restless mind was an event from earlier. He’d been down in the cellars speaking to the goblin that runs them, a surely creature older than half the vintages, when Jezera interjected asking for him to bring up a bottle."
"Once more his attempts to catalog supplies had been thwarted by alcoholism."
"Putting aside his feelings towards her less than diligent management, it left him with a nagging question. Just what exactly was the amulet she had forced him to to wear, and what did it do?"
"Clearly Jezera was able to communicate with him through the amulet, as demonstrated by her earlier... interruption."
"It was also able to cause pain at times. Less than a day after being forced to wear it, he’d tried to take it off. Not only did he find himself strangely incapable of it, but within seconds he was writhing in agony."
"Andras had come up to check afterwards, though probably mainly to laugh at him."
"He lightly brushed the magical artifact with his finger. What had really piqued his interest today was the fact that she’d known he was down in the cellars at all. He hadn’t told anyone he was going down and hadn’t been spotted on his way down."
"At least he didn't think so."
"Did that mean she could locate him anywhere, or at least anywhere in the castle?"
"If so, Rowan considered what else could it do? She hadn’t seemed to know what had been going on in the conversation with the surely old cellar keeper, but the idea that she might be able to overhear him whenever she wanted gave Rowan pause."
"Jezera’s busybody ears listening into his private moments with Alexia…."
"His musing was broken up by a knock on the door. It was a maid coming to check in on him for the night. Rowan almost shooed her away before an idea struck him."
"It might be risky, but there was one very simple way to test if Jezera was able to listen in on him. A way to ease that little drumbeat of paranoia. Attempt some kind of obvious scheme and see if she knew about it."
"If she did know, then he’d have proof she could use the amulet to overhear him. If she didn’t, well that was one step closer to his eventual freedom. Still, there was all kinds of risks involved. What would the twins do when they did find it out?"
"He coughed loudly."

maid "Did you need something from me, sir?"

menu:
    "Test the amulet’s power.":
        $ released_fix_rollback()
        ro "Actually yes, stay and talk for a moment."
        show rowan necklace happy at midleft with dissolve
        "The maid shifted her glance sideways, but otherwise obeyed without complaint."
        maid "Yes, sir."
        ro "You’re Rosarian, aren't you? The red hair gives it away."
        maid "Rastadel itself, sir. Spent most of my life there. The sky outside town was so vividly blue. I think I’ve almost forgotten it by now."
        ro "It really is quite lovely. But, how did  you end up this far north? You were taken as a prisoner, I assume?"
        "The maid went into a fairly long story about how she was taken from her village. Her name was Amelia and she’d been taken on an orcish raid. Rowan’s heart ached."
        "Still, he sensed a bit of easing in her posture. Shoulders relaxing, arms uncrossing. It was working."
        "After awhile, she joined him on the bed. There was still a discomfort there. Perhaps she thought he meant to take her to bed? Regardless, over the next forty minutes or so the two got well acquainted."
        ro "Do you work in a specific wing?"
        maid "No no, all over the castle, sir."
        ro "Even Jezera’s chambers?"
        "She blushed softly."
        maid "Mistress Jezera is very particular about who is allowed to clean up her room. Far more so than Master Andras."
        ro "So you aren’t allowed in?"
        maid "No, I am. I’m one of the ones she likes, I suppose."
        "She didn’t quite meet his gaze. Almost as if there was something she wasn’t saying."
        ro "What do you think of her?"
        "He was testing, probing. Seeing if she could be trusted. There were some things she was holding back, a consequence of living in a castle like this. But, there was a genuine connection."
        maid "If I told you, would you promise not to take it to the mistress?"
        ro "I see. We needn’t talk about anything that might get you in trouble. That said, I’m pretty curious about her myself. In fact, I suspect that if I learn more about her, it might be the key to returning to that Rosarian sky that was so blue."
        "The maid nodded."
        ro "So if you ever hear anything around her or see any documents in her room then perhaps it might not be such a bad thing for me to hear about it. After all, I don’t plan to go home alone."
        "The maid nodded softly, but otherwise didn’t reply. Still, all estimations seemed to suggest that she was answering in the affirmative. She really did seem to dislike, perhaps even hate, the purple demoness."
        "A short while later, the girl left to continue her duties. Rowan sat back down in bed, continuing to fail to sleep. If Jezera really could overhear conversations, there would be no way she’d take an action like that lying down."
        "And if she couldn’t? Well, then he might have just gained an informant with access to her room. All in all a win-win situation."
        "He smiled softly."
        scene bg6 with fade
        show rowan necklace neutral at midleft with dissolve
        show jezera displeased at midright with dissolve
        "Rowan couldn’t be surprised when less then two hours later he was called to the throne room. He also couldn’t be surprised to see his mistress sitting on the throne looking pretty livid."
        "But, what he was pretty surprised about was that the maid from before, Amelia, was naked and curled up around Jezera’s foot."
        "She got right to the point."
        je "Rowan, did you seriously try to set up one of the castle maids to spy on me? Without even bribing her? Without even fucking bribing her? Just how stupid are you?"
        "Rowan had to force himself not to smile. This next part wasn’t going to be fun."
        ro "I think it would be pretty stupid of me to try to spy on you in this place. You own this castle."
        je "Don’t play dumb with me, boy. I know what you did."
        "Jezera stared daggers at him."
        je "The first thing the little slut did after leaving your room is come right to me and tell me what you did. Are you really this stupid?"
        show rowan necklace shock at midleft with dissolve
        "Rowan opened his mouth to speak and then fell silent. Well, that plan had just gone down the drain. If she knew without even having to use the amulet, then this proved nothing. The whole plan was a wash."
        "Suffice to say, Rowan had never actually counted court politics as one of his foremost skill sets."
        je "Here’s the part I don’t get. Why would you ever think such an amateur scheme would work? Do you really think that I don’t vet the people who have access to my room?"
        je "Vet very extensively."
        "Rowan glanced at the naked girl. Suddenly, he has a sneaking suspicion what exactly about Jezera it was that Amelia had been so reluctant to talk about earlier."
        ro "I see. I suppose I didn’t trust my confidant carefully enough. I submit to whatever punishment you think is worthwhile."
        "He lowered his head slightly. The throne room was silent for a moment. Then, of all things, Jezera started to laugh."
        show jezera happy at midright with dissolve
        je "Frankly, I don’t know whether I should send you to the dungeons, or give you pointers for how to make less of an ass of yourself when scheming."
        je "First of all, you take your time and spy on potential informants. You don’t trust people who you don’t have under your thumb. Didn’t you even think about getting blackmail material or something?"
        "She sighed, and straightened her face."
        show jezera displeased at midright with dissolve
        je "Look, just this one time I will be lenient. Frankly, if I were in your unfortunate boots, I’d probably have tried some nonsense like that too. Only, better, of course."
        je "This time you’re leaving with a warning. If I hear that you’ve been trying to get the help to spy on me again, I will not hesitate to refer the matter to my brother. He is less inclined to chuckle at sedition then I am. We clear?"
        ro "Yes mistress."
        je "Good, good. Off with you."
        "Jezera rose from her throne and walked towards the door. She yawned loudly the entire time. Rowan, meanwhile, stood in place for a few moments processing. Perhaps it might have been smarter to let that particular plot bake for a little bit longer."
        hide jezera with moveoutright
        scene black with fade
        "Still, despite the fact that he’d learned nothing of note about the amulet, he’d gained valuable insight about the bonds that kept him here."
        "He sighed inwardly and made the way through the darkened corridors of the castle back to his room. He wouldn’t be a prisoner forever. Not if he could help it."
        return


    "It’s too risky for now.":
        $ released_fix_rollback()
        ro "No no, my head is in the clouds is all."
        show rowan necklace happy at midleft with dissolve
        "Rowan faked a smile. As quickly as his resistant flight of fancy had appeared, it ended."
        "The consequences of getting in trouble were too dire. The benefits too marginal. Perhaps he might try to fight the twins’ influence one day. But if he did, it would need to be a better thought out plan."
        maid "I understand, sir. Thinking of home is an easy trap. I can’t say I haven’t fallen into it myself of late."
        show rowan necklace neutral at midleft with dissolve
        "The maid departed soon. Rowan’s brow sunk again the moment she left. Once more he was left alone with naught but his thoughts. Would he ever be free again?"
        return
