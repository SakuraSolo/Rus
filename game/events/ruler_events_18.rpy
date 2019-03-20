init python:

    #Helayna's Day Off
    #Triggers on week 35 as a Ruler Event provided they accepted Helayna’s love confession (Helayna didn't escape)
    event('helaynas_day_off', triggers="week_end", conditions=('week >=35', 'helayna_escape_method == "no escape"'),
        group='ruler_event', run_count=1, priority=pr_ruler_high)


label helaynas_day_off:
#Helayna's Day Off
#Triggers on week 35 as a Ruler Event provided they accepted Helayna’s love confession (Helayna didn't escape)
$ halaynas_day_off = True
scene bg9 with fade
show rowan necklace happy at midleft with dissolve
show helayna neutral behind bg9

"The sounds emerging from Rowan’s room the night before had surely annoyed those nearby. Helayna, of late, had taken to increasingly loud displays of lust."
"After the past week in the field, being able to relax with his lover meant that making a bit of a disturbance was not at the front of his mind."
"In the morning his eyes flickered open to the rise of the sun. There was an emptiness next to him. A depression where there should be a body. His eyes were still hazy from sleep, but he could make the faint outline of Helayana already up and about."

ro "Helayna."

hel "My love, I had not realized you were were awake."

hide helayna
show helayna happy at midright with dissolve

"Rowan blinked twice. His eyes slowly adjusted. Helayana was looking at him sympathetically. Yet, he couldn’t help but notice that she was standing near the closet fiddling with the straps of her old breast plate. How long had it been since he’d seen her wear it? Raeve Keep?"

ro "And I had not realized you were back to training?"

show helayna neutral at midright with dissolve
pause 1
show helayna aroused at midright with dissolve

hel "It’s not something that needs concern you. If you like I can distract you with..."

"She started walking back towards him, swaying her hips and leaving the breastplate to the side. Her eyes were drawn, as they so often were, to the faint outline of his cock poking from beneath the sheet."

ro "No no. That’s alright. Maybe a bit later."

"She averted her eyes. That she managed to even do so once her mind had drifted to sex was a major step up from where she had been even weeks before."

show rowan necklace neutral at midleft with dissolve
show helayna neutral at midright with dissolve

ro "You don’t have to go back to training if you don’t want to. Raeve Keep is fallen. And around here I will protect you. You’re mine now."

show helayna sad at midright with dissolve

hel "…"

"The turn in the topic managed to draw his lover back into the conversation. The lust faded slowly from her eyes."

hel "Rowan, why are you doing all of this? What are you fighting still?"

ro "What? I’ve told you plenty of times before? They took Alexia and…"

show helayna angry at midright with dissolve

hel "...and now you share your bed with me instead. Don’t say because the twins have power over you either. May I live long enough to see Jezera on her knees before it."
hel "The two of us could teach that purple a bitch a lesson in…"

ro "Don’t talk about that. Not here. The walls have ears."

show helayna neutral at midright with dissolve

"Helayana averted her eyes and flashed a blush."

hel "But still, why do you still fight now?"

#if corruption lower than 20
if avatar.corruption < 20:
    ro "The demon’s war will continue even if I leave. They’re surprisingly adept. With a decent person at helm, someone is looking out for the good folk. Without me, can you imagine what they would have done to them by now? How horrible this war would be?"

#if corruption is 20-49
elif avatar.corruption <= 49:
    ro "I still ask myself that question constantly. My actions make the demons more powerful, yet the enemies they fight are no innocents either. If I comply, people suffer. If I don’t comply, people suffer."
    ro "I don’t fight for Andras and Jezera’s sake...but at this moment, I have no brighter path worth risking my life to seek."

#if corruption is over 49
else:
    ro "Well why shouldn’t I? So the Baron can lord around in his castle still? So the same old cycle can continue forever? I don’t know. The Twins are probably wrong. Who knows? I’m sorry about all the deaths in the war, but I’m not tearing down anything worth keeping."

#rejoin
#if rowan's influence over alexia is still high
if all_actors['alexia'].relation > 20:
    ro "Besides, they still have Alexia. She’s still my wife. You are my love Helayna. You needn’t doubt that for a moment. But, I cannot leave Alexia to them."

#rejoin
"Rowan’s lover sighed, reaching down to pick up her breastplate."

hel "Even after my mind returned, it took me awhile to want to train again. My family has fallen. I have no legacy or small folks to defend. I didn’t train anymore, because what was the point?"
hel "But, I was being silly. I have a cause."

"She took another step closer. Without warning she knelt at the foot of bed, lowering her head."

hel "You have the power to make the world a better place, my love. It’s so obvious to me. You are the most important player in this entire conflict. The most important player to me. Let me give everything I have to aiding you."
hel "Let me fight by your side. Let me swear my service to you."

ro "Helayna…"

"He reached out and placed a hand on her shoulder. How long had she felt this way? Had he really not noticed?"

ro "I can’t tell you how much you help me already just by remaining safe here."

hel "I don’t want to be safe. I want to be useful. Please…"

"Rowan sighed. There was no denying that Helayna was a great fighter. Or at least that she once was. With her at the head of a chaos army, few in the realm would even bother to take the field. Still, the head of an army was the most dangerous spot for her to be."

ro "We can discuss this again at a later point. I probably need to head out for my daily tasks soon."

"Helayna hung her head, but nodded her acquiescence. "

show helayna sad at midright with dissolve

hel "I understand. You have a lot of things on your mind in these cruel days. Just...please. Consider it further, my love. For me..."

"Rowan placed a hand on her cheek. Helayna was a good warrior. He was scared for her, but surely she could handle herself, right? He would need to see how she was doing as a warrior. He needed to see how much she’d lost because of the ring."
"It was still on his mind as he left for his daily tasks. Helayna hadn’t mentioned it again, but he saw the same lingering question in her eyes every time the two exchanged words."
"She was right when she said he had much on his mind. He simply couldn’t focus on the question now when he had a troop review to do today."
"Rowan left, and when he did the only two occupants of the room were Helayna and her doubts. Today was going to be a long day for her."

hide rowan with moveoutleft

"Her eyes hungrily traced the arch of his back as it walked away from her. Even during the earlier conversation she had been forced to struggle to even so much as focus on the topic at hand. She wanted him."
"She wanted him in the morning. She wanted him at night. She had wanted him during that conversation. She even wanted him when…"
"Helayna sighed. She felt better for having told him most of it, but the one thing she hadn’t mentioned lingered heavy on her thoughts."

scene bg14 with fade
show helayna neutral at midleft with moveinleft

"Helayna began this morning much the same as many others with Rowan in the field. Once she had fit into her armor, she marched down the hallway to the training barracks."

show alexia 2 necklace neutral at midright with moveinright

"Unfortunately, today it was the same hallway that Alexia chose to take on her own morning routines. Rowan’s wife saw her husband’s lover and stopped in place."

al "Oh."

show alexia 2 necklace concerned at midright with dissolve

"At the sight of her, Helayana blushed and looked away. The two had not had a proper conversation in...well, they’d actually never had one so far. Helayna prefered it that way."

show helayna aroused at midleft with dissolve

"A stray thought came to the knight. One of Alexia and Rowan in bed together while she…."
"Helayna was forced to focus in order to push down the fantasy. Now was not the time."

show helayna neutral at midleft with dissolve

"Both women tried continuing on their way, but that proved fruitless. A few few feet later it was apparent they were heading in the same general direction. Eventually, Alexia broke the silence in a soft voice."

al "I see you came from my husband’s room."

hel "…"

al "How was his mood this morning?"

"Her face was inscrutable."

hel "…"
hel "He’s stressed Lady Alexia. With the war and all of its intricacies and implications even when I speak to him, he normally isn’t truly there."

#low rowan alexia influence
if all_actors['alexia'].relation < 20:
    show alexia 2 necklace angry at midright with dissolve

    al "So, you’ve taken my husband and yet you don’t even truly have him. I hope you’re happy, Helayna."
else:
#else
    al "For a moment when you said that he doesn’t truly confide in you, I was happy. But, only for a moment."

    "Alexia stopped in the hallway momentarily. She visibly digested each word."

    show alexia 2 necklace neutral at midright with dissolve

    al "I don’t hate you, Helayna. Not truly. My husband suffers the weight of the world on his shoulders. Had he not taken you in, I don’t know what would have happened to you. Now you’re better, and I cannot say for certain what dangers he protects you from."

    "She let out a long sigh."

    al "I don’t intend to cede you Rowan. Not, for a moment. But, if you can lighten his load while he’s in your company, even if for a moment, I cannot hate you."

#rejoin
"Alexia didn’t follow up the thought. There wasn’t even a chance for Helayna to respond. She turned and marched off in a separate hallway, leaving Helayna contemplating the ethics of her choices."

#courtyard
scene black with fade
show helayna neutral at midleft with dissolve

"The ringing of swords in the practice field announced that Helayna had set to work. She started with her stances before moving on to working with a wooden dummy."
"The only other residents of the field were a few of the brighter orcs and an androgynous man in leather armor whose true species was a mystery."
"Helayna swung out again and again. Much of this was second nature to her. Months had passed, but her instincts were still there. No, the real problem was the changes in her own mind. The nagging little thoughts that interfered with her rhythm."
"A few days earlier she’d been sparring with an orc male. Before, she might have bested him with ease. But, she’d been distracted repeatedly by the sheen of sweat on his muscles before being knocked to the dirt."

show helayna aroused at midleft with dissolve

"Even now she could feel it. As she tried to focus on striking the precise spots on the dummy meant to reflect gaps in the armor, her glance kept on being stolen by just how tight the leather was pressed against the skin of the androgynous man."

show helayna neutral at midleft with dissolve

hel "No. I need to train. I need to focus."

"She redoubled her work. Neck. Under arms. Strike parallel. Bring the blade down from that angle so it wouldn’t be deflected by the armor."

show helayna aroused at midleft with dissolve

"But, it was no use. Helayna was falling. Her thoughts grew cloudier by the moment. She hadn’t even gotten sex in the morning after all. Eventually, still standing in the middle of the training field, she fogged up entirely. She got lost in it..."

#throne room cg
scene cg171 with fade
pause 3 

"In her fantasy, Helayna was masturbating. The throne room made schlicking sounds to match the stroke of her fingers. Though, that was matched by the gasping sound of another woman going down on a man’s thick cock."
"Rowan."

scene cg172 with fade
show helayna naked aroused behind cg172
show rowan necklace naked aroused behind cg172
show jezera naked behind cg172
pause 3

"And he was sitting in her uncle’s old throne. Of course, she was right beside him, perched on one of the arm rests."

hel "Uh. Harder. It would be so hot if you fucked her harder, my love."

"The woman in chains was gasping desperately, trying to pull her head up from the manhood that filled her throat. It was to no avail. This powerful figure of a man easily kept her cock in mouth with the mere presence of a single hand."

ro "You’re not done yet."

je "Please...I…."

"Again she tries to escape, but again her head is forced back down. There is no escape for the prisoner. No escaping his power or domination. "
"The thought alone is enough to make Helayna gasp lewdly into the air and lean towards him. How could she resist the sight of her love using this captive woman so brazenly?"

ro "You’re not done yet."

"There was no escape for her now. His captive surely knew it. She forced herself down on his manhood, slobbering and gagging every time she brought her head down. It was music to her ears."
"Helayna could see the desperate spasming of her bound body and the way she tried to suck in air around his cock."
"It was all too much. She reached out with a damp hand ran it over his chest Her other fingers eagerly explored her own passage. He looked so strong like this. So virile. It was all too much."

scene cg172 with sshake
scene cg172 with sshake
show cg173 with flash
pause 3

"It was all too..."

#courtyard
scene black with fade
show helayna aroused at midleft with dissolve

"....good to be true. She was sitting on the floor of the training ring. A dampness between her legs told her what happened. She’d spaced out. Again."
"She looked around. The only one who seemed to have even noticed that she’d been staring into space was the androgynous man. He flashed her a smirk. She sighed. Even if she wanted to train, it just wouldn’t be possible like this."
"With a defeated sigh she went back to the weapon shed to put back her training sword."
"Or at least that was her intent. She paused at the empty weapon rack. No one else could look into the shed. She was all alone. Her fingers ran over the sword’s hilt. It was very stiff. Very hard."
"But, no. It would probably never work for the idea that was rapidly clouding over her brain. Too rigid. She’d hurt herself, and then might not be able to fuck her beloved for weeks. Something softer and more yielding."
"Helayna’s eyes were drawn to a battleaxe along the wall. Had she seen a similar object in the forge a few weeks back?"
"Regardless, when she put her finger to the handle the flexibility of the wood was apparent. It needed it to not snap under the weight of the head. And the surface was polished and wax sealed. No risk of splinters where they were unwanted."

#axe cg
scene cg306 with fade
show helayna aroused behind cg306
pause 3

"She took the axe from the wall and positioned it with the head on the ground. That way the weight of the head could be used as an anchor point."
"There wasn’t too much foreplay needed. A bit of wiping her juices on the handle. Afterall, she was still quite lubricated from her fantasy. After that it was just a matter of removing any apparel that might be in the way."
"Helayna gasped softly as the wooden shaft slide into her body. It was long and hard. With the way it filled her, it became so simple and easy to just let herself rock and up down, taking more and more of it into her each time she thrusted down."

hel "mmmm…."

"Of course, such a thing was not what she truly wanted. Helayna wanted him. She wanted him.  Every waking moment she wanted Rowan’s cock inside of her. Whenever she fucked herself with anything...this...her fingers...she couldn’t help but imagine it as being his."
"It was like every day she was here, her body became more fitted to his unique shape."
"She pushed her body down faster and father. The rhythm picked up a greater, more desperate, urgency with each movement of her body. This was not the tepid clit flicking of a virgin, but the hip shaking self-fucking of a complete slut. She wanted it. She wanted him."

hel "...Rowan…"

"Thinking of him made the tide rise higher."
"At any moment anyone could walk in. The stray thought that a giant orc could walk in and see her like this wasn’t absent to her mind. Her sexuality was wired to Rowan, but as she was now, there was still something sexy about the idea of being caught, helpless, in a position like that."
"Thinking of that made the tide rise higher and higher."
"Her hips rolled faster and faster. The handle of the axe bent slightly against her shape. It was flexible, flexible enough to feel good at least. A nice stand in for the cock that Helayna so desperately needed."
"The tide of pleasure was almost there. It built up inside of her, threatening to explode. Her gyrating thrusting against the weapon only made that rise steady."
"Each moment she let herself be lost in the sensation the tide was getting higher. Almost to the the point of tipping over the edge. To the point she was right about to explode."
"Helayna gasped softly and then she came."
"She had to stop herself from screaming. She certainly failed to stop herself from making a mess of the floor. She wasn’t even thinking of that, when she was far more concerned with melting into puddle."
"Helayna sat on the floor of the armory panting. The glow of the orgasm still hung over her, along with the scent of feminine lust. Helayna closed her eyes. But, when she did she felt...somehow gloomy."

hel "I can’t do it. No, matter how hard I try, I can’t do it. I’ll never...I’ll never be me again."

scene bg14 with fade
show helayna angry at midleft with moveinleft
show jezera happy behind bg14

"When she recovered, Helayna knew where she needed to go. She couldn’t train under the effects of the ring. There was only one person who knew enough about the ring to help her. And she was the one person Helayna wanted to speak to least."
"She approached the woman’s chamber and rapt on the door loudly with her gauntlet."

je "Who is it~?"

hel "It is I, Lady Helayna Raeve."

"A silence hung in the air. Helayna took in a deep breath. Would the demoness even consent to a conversation?"

je "Oh, Rowan’s little pet. Enter."

scene cg181 with fade
show jezera naked happy behind cg181
show helayna neutral behind cg181 
pause 3

"Helayna opened the door, and soon found herself gaping in awe. Jezera was not alone. Another woman sat in the front of the room painting a regal portrait of her. Only, most regal portraits for women aren’t done in the nude...or with a naked woman licking your feet."
"For a moment, Helayna’s eyes were captured by the obscene display. The girl, no older than her twenties, had a clear dignity to her posture and lacked the scars and cracks you’d find in a peasant girl. She must have been a noblewoman that Jezera had converted into a pet."
"She gulped loudly, trying not to stare at the way that the pet’s tongue danced on the top of Jezera’s naked feet."

je "Yes yes. Out with it."

scene cg182 with fade
show jezera naked happy behind cg182
show helayna neutral behind cg182 
pause 3

"Helayna almost jumped. Jezera was looking right at her with an amused expression. A silent swear ran through her head. Did the demoness know where she was looking. Or how hard it would be to tear her eyes from Jezera's exposed bosom if it got caught there?"
"Surely the latter at least."
"Helayna coughed and straightened her back. It was a challenge to keep her eyes focused on the demoness’ face."

hel "It’s the ring. I want it off."

je "Aww, isn’t that cute. I’m sure you do. Must be quite hard to manage."

"Jezera giggled. The pet at her feet arched her back, only to earn a swift discipline from her mistress in the form of a domineering tap on the head with her other foot."

je "Hold still, girl."

"Helayna coughed. She couldn’t keep looking at Jezera. Her eyes were going to wander lower. Instead, she turned her head away. How good would it feel to run her sword through this witch one day?"

hel "Look. I’m trying to train to be Rowan’s field commander. You don’t want him dead, right? Especially after all of your work to force him to do your bidding. I’m not going to run off or fight you..."

je "Probably for the best. My brother would be quite displeased if you did."

hel "But, you actually want me leading your troops, right? I can’t think str- I mean I can’t fight as well with it on."

"Jezera smirked, leaning over the railing of her throne. The artist painting he made a tsk sound. Surely there were less demanding clients to paint."

je "I suppose that is a a good point. You’ve almost even convinced me."
je "And...whatever her name was...over here can tell you how hard a task that can be. Can’t you girl?"

"She placed one of her feet on top of the girl’s head forcing it to the ground. Naked and on all fours, all she could do was let out a pathetic mewling sound."

je "She showed up the other day asking for the release of her brother, a knight we took captive. An experience I’m sure you’d know nothing about. Still, isn't she just precious?"
je "Still, as much as I’d like to help you Helayna, there is sadly one tiny problem. I have no idea how to remove it."

"Helayna almost scowled. She had to calm herself and remember that perhaps she should not further antagonize the person who did this to her. That said, she didn’t believe that excuse for a second."

hel "How do you not know?"

je "As I said, it’s not my invention. If anything, I’m not even totally sure I understand the mechanics myself. We can perhaps take a look at it together. Though some other time."
je "I do have current engagements, after all."

"The pet at her feet let off a soft whimper. Helayna really did not want to think about what was going to happen to the girl once she and the painter left."

je "So, you’re just going to have to make do with it on, dear."

scene cg183 with fade
show jezera naked happy behind cg183
pause 3

"She wanted to look up at glare into Jezera's eyes. If anyone could be said to be her captor, it was Jezera. And at that moment, she was so afraid of looking up and being caught on her body, or worse whatever depraved game she was playing with her captive, left her unable to meet her eye."
"Helayna nodded as politely as she could muster and almost ducked out of the room. Maybe she could try her hand at training again? Already though, she knew how it would end..."

je "One might almost think I was having an effect on her…"

scene black with fade

"Helayna would spend the rest of her day locked on the singular task of honing her skills. Afterall, without Rowan around, what was there to do but try to focus on her rusted skills as much as circumstances allowed."

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve
show jezera neutral at midright with dissolve

"Rowan walked into the empty throne room, cracking his neck. He’d been ordered to come right after he finished with the day’s war preparations."

ro "You wanted to see me, Jezera?"

je "Yes, yes, come in. It’s about your strumpet. She came and visited me today."

ro "Helayna?"

"Rowan’s eyebrow raised. Jezera talking to or talking about Helayna was bad news."

je "Indeed. You are aware that she’s been trouncing around in armor trying to restore her sword arm, yes?"

show jezera happy at midright with dissolve

#if Jezera influence on Alexia is higher than Rowans
if all_actors['alexia'].flags['jezera_influence'] > all_actors['alexia'].relation:
    je "One has to keep track of what their loved ones are doing and who they’re doing it with."

#rejoin
show jezera neutral at midright with dissolve

"Rowan guarded his tongue. It was clear that she had something of import to say, but if he let her question him as she wished, he’d probably never hear it."

ro "I’m aware as of this morning. Did she tell you why she came to visit you?"

je "Besides my charming personality? She’s been having trouble with her ring apparently."

"Jezera went into detail explaining what had happened before. Of course, she hadn’t spared the detail about the pet at her feet. But, at this point it hardly shocked Rowan. For better or for worse her usual antics had lost much of their power to surprise him."
"Still...Helayna was having problems training while wearing the ring. Why hadn’t she told him in the morning?"

je "There’s one other thing. That girl of yours spent an awful lot of time staring at the waif at my feet. Longer than mere curiosity would dictate."

"He sighed. So this was the reason she wanted to speak to him..."

ro "Wouldn’t that just be an effect of the ring? Anything remotely erotic gets her in a state."

je "Well, it was certainly a factor. But, lust and submissive inclinations are not the same thing. If it was just the lust she would have responded more strongly at different moments. You should trust me on this one. I’m good at picking these things out."

ro "I don’t doubt your experience."

"He held his tongue. Surely, this wasn’t going where he thought this was going..."

show jezera happy at midright with dissolve

je "Rowan, Rowan, Rowan. I can’t believe you don’t see these things the way I do."
je "That girl pines to be a submissive, even if she doesn’t know it yet."

"His eyebrows narrowed into a glare. A rare show of backbone."

show rowan necklace angry at midleft with dissolve

ro "we have our pact, demon. I will serve as you wish. But, you’ve already done enough to Helaya. I won’t remain silent if you choose to do anything else to her. Consider how far I’ve proven willing to go for Alexia."

"As if to further emphasize the point, he put his hand on his sword handle. Though he kept his head bowed somewhat."

je "Always the hero, huh? Well don’t worry. I’m just a friendly helper. I won’t do anything to her at all."
je "After all, you will."

show rowan necklace neutral at midleft with dissolve

"He raised his head, looking at her eye to eye. Did she intend to force him into playing one of Jezera’s little games with her?"

ro "I will?"

je "Consider this."
je "You have this girl, pretty thing that she is, and you’re her universe. Right now, she eats, sleeps, and breathes Rowan. Sucks too, I suppose. Throwing herself at her training? Submissive tendencies emerging?"

"She looked off into the middle distance. It was almost wistful."

je "You can make Helayna into anything you’d like. Anything at all. She’d only love you all the more for it."
je "Make her your slave? Your fanatic? Your personal footstool? Maybe give her to Alexia as a present?"
je "If I was in your place, I’d already have a training regiment prepared for her."

"In his head, he retorted that this was because he was not her. He was, however, wise enough not to vocalize it in this context."

ro "Thank you for bringing this to my attention. I’ll keep that in mind."

je "Don’t do it for my sake. Or even yours. Do it for hers!"
je "She doesn’t have the focus to be the knight she was before. She’s desperate to be useful to you. The only way you can make her happy is making her your slave."

"Rowan pondered this as he returned to his room. He hadn’t seen Helayna in the field. Perhaps this was all nonsense. Perhaps, he should visit her while she trains? But...what if Jezera was right?"

scene bg9 with fade
show rowan necklace neutral at midleft with dissolve
show helayna 2 happy at midright with dissolve

"The castle was dark now. When Rowan arrived, he found Helayna curled up under the sheets, vergining on sleep. She groggily turned to him, rubbing her eyes."

hel "My love, you’re back. It was later than I expected."
hel "Is something wrong?"

"He sat down on the bed and removed his clothing, piece by piece."

show rowan necklace naked at midleft with dissolve

ro "Not a thing, Beautiful. Not a thing."
ro "How was training?"

hel "It went very well. I’ll be back to fighting shape in no time. You will see."

"Rowan nodded and laid down. He felt a pair of soft hands working their way around his bare midriff into a soft hug."

ro "I will. Someday soon, I’ll join you out on the training field. We can spar together."

#f Rowan/Helayna backstory was her teacher
if helaynaRelationship == 0:
    ro "Just like old times."

#rejoin
hel "Oh. I...I look forward to it. Greatly."

show rowan necklace naked concerned at midleft with dissolve

"His ears perked up. Was there a hint of fear in her voice?"

show helayna 2 aroused at midright with dissolve

"That thought was banished by a more pressing reality. She was exploring his body, letting her digits pour over his chiseled chest. There was no mistaking what she wanted. It was what she wanted every night she could get it."

hel "My love...do you want to…?"

scene black with fade

"Rowan made love to her before they slept. The sounds of their bodies echoed down the hall, no matter how much he tried to keep quiet. In his arms she felt so...malleable..."

return
