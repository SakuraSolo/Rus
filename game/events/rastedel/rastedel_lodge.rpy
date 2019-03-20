label rastLodge:

if lodgeFirstVisit == True and eleaConvo == False and juliConvo == True:
    scene bg33 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan approached the front gate of the Grand Camellia Lodge cautiously. The tall stone structure stood in the Southwest of town, not far from the palace. It was a popular hangout spot for nobles. A place where many of the important decisions of the realm were made."
    "A place he’d normally never be welcome."
    "He looked on at the gates with a hand to his chin. It would be valuable place to gather information, but the guards at the gate didn’t seem inclined to let just anyone through. It seemed that the entire effort had been wasted."
    "Only, as he turned to leave, a familiar face passed him by."
    show juliet shocked at midright with dissolve
    juli "Rowan!"
    show juliet neutral at midright with dissolve
    juli "I had not expected to see you in the capital again so soon. I heard news of your departure."
    "Rowan smiled softly. The moment she caught his eyes, her gaze averted. It seemed not much had changed since the ball."
    show rowan necklace happy at midleft with dissolve
    ro "Quite reasonable, my lady. I only returned for the day just to look about. I’ll be back in the field soon."
    juli "You will?"
    juli "Everyone here speaks of you and your resolve. Your name gives solace whenever the topic of the conflict in the south comes up."
    juli "I will add a private prayer at weekly services for your return unharmed."
    "Rowan nodded somberly."
    ro "That’s quite kind of you, My Lady. Even knowing there are people here who wish for my safe return will make sure I don’t risk too much."
    ro "Apparently Rastedel isn’t done with my ugly face."
    juli "I wouldn’t call it ugly…"
    #show juliet confused
    juli "I suppose you’re here to get into the lodge? You’d need entry papers or a house signet ring to do that. Perhaps I could…"
    "Rowan’s heart briefly rose. Perhaps he would get some valuable information after all…"
    juli "No no. Father will know if I bring someone in. It would be best for him not to get any wrong impressions…"
    #show juli sad/embarassed
    "From what Rowan had heard, there was nothing the nobles loved to do more than talk. Even speaking together in front of the building would no doubt would have some kind of social ramifications."
    ro "I understand. If you’re worried about displeasing your father, then you can only imagine how I feel."
    "He chuckled."
    ro "I wouldn’t belong in there anyway. It’s above my station. I’ll let you go on with your day my lady."
    juli "Of course. I will no doubt see you soon."
    "An interesting conversation. It was good to have friends in the capital. The daughter of the Duke of Werden himself no less. Still, he’d probably have to break it to her that he was a married man soon."
    $ lodgeFirstVisit = False
    jump rastMenu
    
elif lodgeFirstVisit == True and eleaConvo == True:
    jump delaneLodgeSex
    
else:
    scene bg33 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan approached the front gate of the Grand Camellia Lodge cautiously. The tall stone structure stood in the Southwest of town, not far from the palace. It was a popular hangout spot for nobles. A place where many of the important decisions of the realm were made."
    "A place he’d normally never be welcome."
    "Rowan’s short visit didn’t last long. He hadn’t been allowed in last time, and he wouldn’t be allowed in this time either. His only hope was that Duke Raeve was gathering useful intelligence there."
    jump rastMenu
    
    
label delaneLodgeSex:

"Rowan approached the front gate of the Grand Camellia Lodge cautiously. The tall stone structure stood in the Southwest of town, not far from the palace. It was a popular hangout spot for nobles. A place where many of the important decisions of the realm were made."
"A place he’d normally never be welcome."
"He approached the outside, where a pair of men-at-arms whose surcoats displayed noble sigils manned the doors."

show rosarian knight neutral behind bg33

rkn "Got a permit of entry? Got a sigil ring?"

"Rowan frowned softly. That might be a problem. He didn’t have either."

show eleanor dress neutral behind bg33

ele "No. But, he’s a guest."

hide eleanor
show eleanor dress happy at midright with dissolve

"Rowan turned around to see Lady Delane standing behind him, arms folded behind her back elegantly. There was something immediately different about her." 
"In an orcish cage, everything from her poise to her aura was off. But, here she was a natural fit with the nobles strolling around the gardens."

ele "I am Lady Eleanor of House Delane. This is my signet ring."

"She flashed a ring that Rowan had never seen on her fingers before."

ele "Rowan Blackwell is my honoured guest. He has my pass of entry, and will be my responsibility."

rkn "...Rowan Blackwell…"
rkn "Yes Ma’am. Welcome back."

"The guards rushed to the sides of the gate, raising their pikes to allow Rowan and Delane through."

#show lodge bg
scene bg36 with fade

"Rowan and Delane walked briskly together through the lodge. Rowan had to pause every so often though to marvel at the interior. Magnificent pelts hung on the walls. Much of the furniture as well was made from all manner of deer and fox skin."
"It was as though the entire building was a testament to the history of luxury that the members experienced."
"The place was not too populated at this hour. But, every so often, someone would look up as they moved. No one paid too much mind though. His proximity to Lady Delane made him appear like just another guest."

show rowan necklace neutral at midleft with dissolve
show eleanor dress neutral at midright with dissolve

ele "I had little to worry about with my family. They all made it out just in time. Much of the house staff is gone, of course. "

show eleanor dress concerned at midright with dissolve

ele "Some of them I’d known my entire life."

show eleanor dress happy at midright with dissolve

ele "But, my parents and siblings all made it to the capital without too much incident. Indeed, I was the only one who was in real trouble."

"She gave him a soft smile."

ele "One cannot always expect swashbuckling heroes to rescue them from a sentence of death or worse. I got lucky, I suppose."

ro "With all due respect, my lady."

show eleanor dress happy at midright with dissolve

ro "If you could call yourself lucky, I don’t believe we would have first encountered one another in a secret Orcish prison cell."

"Delane chuckled at that. He knew from experience that the best way to keep her engaged was to stimulate her brain. She liked a verbal sparring partner."

ele "Now that I’m no longer concerned with the threat of a truly undesirable marriage, among other things, one does have to wonder…"
ele "What was the hero of Karst doing exactly at the centre of one of the largest orc tribal confederations, exactly?"

show rowan necklace neutral at midleft with dissolve

"Rowan laughed softly. Better to treat it as just a joke for the moment. He didn’t much think that she’d be too appreciative if his answer was to ally them to demon lords."

show eleanor dress neutral at midright with dissolve

"Delane paused suddenly right outside one of the doors in a long passage."

ele "This is a private room. My family has a long standing reservation on it. We will not be disturbed or overhead in here."

"Once they were inside, Delane sealed the door behind them. Rowan gave a sigh of relief."

if eleanorCaveSex == True:
    "This had been the first time they had been alone together since their escape. The first time they’d been able to enjoy each other’s company since their...encounter in the cave."
    
ele "While our chat outside was riveting, there is another reason I called you here."

show eleanor dress concerned at midright with dissolve

ele "Please be so kind as to excuse me for a moment. I’ll be in the side room."

hide eleanor with moveoutright

"Delane slipped hastily through another door at the side, leaving Rowan alone to explore the room."
"It was like anywhere else in the lodge no doubt. It was filled with tokens from the history of house Delane, some going back centuries. A medal awarded to Sir Duncan Delane by the Baron two hundred years before held the place of honour."
"But, there was only so much exploring he could do before Delane returned."

show eleanor naked aroused at midright with moveinright
show rowan necklace shock at midleft with dissolve

"She was standing in the doorway of the side room, naked as the day she was born."

ele "One must reward those who do them a kindness. It is only the polite thing to do."

"She had hungry eyes as she slinked towards Rowan. Her shapely hips rolled with each delicate step. The distance between them was closing fast."

ele "A life debt requires quite the reward. I may never be done doing so."

if eleanorCaveSex == True:
    ele "You did seem to so enjoy your first taste of it, after all."
    
menu:
    "A hero’s reward.":
        $ released_fix_rollback()
        jump DelaneLodgeSexScene
    
    "Turn her down gently.":
        $ delaneReject = True
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        "Rowan averted his gaze from her body quickly. As he looked at her naked body, a single thought had struck him like a hammer. Alexia."
        ro "My lady. I beg your forgiveness. I do. But, I can’t accept this. I’m a married man." 
        "No matter what else had happened since he’d first gone to Bloodmeen, that fact remained true."
        if eleanorCaveSex == True:
            "Delane shrunk in rejection. Her arms wrapped themselves over her bare chest. But, she still looked at Rowan with a powerful expression. Only now it showed skepticism."
            ele "Interesting. Were you mysteriously less married back in that dark cave? Or perhaps you are a newlywed?"
            "Rowan shook his head. How did he know that was how she was going to reply."
            ro "My Lady. That was a mistake. It was a stressful moment. I never should have indulged in that way. It was wrong of me. To her. And to you."
            ele "Hrmmph."
            "Having accepted his rejection less than gracefully, Delane slinked back into the side room to get dressed once more. She wasn’t about to remain naked."
        else:
            ele "I suppose this is what a lady gets for daring to hope. "
            "Rowan wanted to rise to his feet to comfort her but decided in this context it wasn’t appropriate."
            ele "Alas, you will simply have to continue to bear my efforts, even if I am willing to chalk today up as a defeat."
            ele "I will have you know that the last man I took to bed was married as well. It did not take me one try, I will assure you of that."
            ele "You underestimate me, good sir."
            show rowan necklace happy at midleft with dissolve
            "Rowan exhaled. It seemed that she had taken the rejection in stride. That was well. In a city of vipers, he needed Delane’s help."
            "Having accepted his rejection gracefully, Delane slinked back into the side room to get dressed once more. She wasn’t about to remain naked."
        show rowan necklace neutral at midleft with dissolve
        show eleanor dress neutral at midright with dissolve
        jump delaneLodgePostSex
    

label DelaneLodgeSexScene:

show rowan necklace aroused at midleft with dissolve

"Rowan watched her body in motion. She was so close now, almost pressing her naked skin against his chest. He stirred softly."

ro "It would be my honor to receive whatever favour you desire to give me."

ele "Hrmmm…"

"Their lips met. Both of their eyes closed. For a long lingering moment, he enjoyed the feeling. She was so soft. Young, beautiful, and blessed with an air of nobility that radiated from her."
"She broke the kiss, moving close enough to his ear that he could feel her warm breath."

ele "One choice. Whatever you want to do with me. Here and now."
ele "Whatever you want…"

"Rowan blinked twice. Anything he wanted. Anything he wanted. It was hard to think with their proximity. He was already riding on instinct."

ro "Have you ever been taken from the rear?"

"Delane’s eyes fluttered softly."

ele "...Never."

ro "...And you said that you would do whatever?"

ele "…"
ele "There should be some olive oil in the dresser."

#show cg1
scene black with fade
show eleanor naked aroused behind black
show rowan naked aroused behind black

"Moments later, Rowan’s clothes were discarded on the floor, and he was sitting naked on the large couch. Delane had taken a position on her knees right in front of him. Her eyes were drawn, like a moth to flame, by his erect manhood."
"She stared at it with raw lust."

ele "...Incredible."

"She reached down to the jar at her feet, and wet her hands with olive oil. Rowan found out that the contents were rather cold. He could feel it when her fingers brushed over his cock. It brought a shiver up his spine."

ro "Mmh.."

"Delane giggled. She brushed her hand up and down his shaft carefully, rubbing hard to make sure that it was well coated with oil. Among other reasons."

ele "Someone is sensitive, huh? This is what you asked for. It’s rare to expect the one to balk at such an encounter to be the man."

ro "Keep going."

ele "If you insist."

"Her hands traveled up and down his length, making sure to cover every inch of his length with the oil. A droplet dripped down his balls."

ro "You can stop now."

ele "Another moment. You’re not the one who will experience a half done job the most."

ro "And I would know what a poor job is better than you would. You’re fine, My Lady. Really."

"Delane blushed softly."

ele "So you say."

#show cg2
scene black with fade
show eleanor naked aroused behind black
show rowan naked aroused behind black

"Rowan stood up slowly. It made room for his companion to get up on the furniture, positioning herself backwards towards him with her rear raised high up in the air and one hand clutching the top of the couch."
"The other hand shot between her legs. She was already working her clit."

ro "You couldn’t wait?"

ele "Do you really believe for a moment that I don’t want to cum from this as well?"

"Rowan responded by plunging his well lubed cock towards her sphincter. It spread slowly as he worked himself inside of her."

ele "Ah!"

"Rowan grunted out too. Her rear was tight. Getting his cock even another inch in took work. But, it also meant that the sensation of her inner walls pressing on him was more intoxicating. There was something oddly beautiful about using a hole for the first time. It was like taking it for himself."
"One hand dug into her hips, holding her in place. The other found a convenient handle in her long dark hair. That way she’d be steady as she took the full force of his thrusts. His breath grew heavier."
"The sounds emitted in the process were rather loud. Rowan hoped that the room blocked sound well. After all, between the moaning, the grunting, and the sound of Delane’s fingers hungrily working her clit, there was much to overhear."

ele "This is….ah...this is...different."

"Rowan slammed himself into her with all of his strength."

ele "Ah!"

ro "Bad different?"

ele "Fuck no. More. Harder. Fuck."

ro "If you insist…"

"He took the lock of her hair that he had in hand and twisted it, Using it as a grip to slam even harder. It made the friction, already more intense from the less lubricated hole he was using, all the more overpowering."
"The effect this was all having on his partner was hard to overstate. Delane was groaning, moving, squeaking. Her finger against her clit moved with frantic abandon. This was her first time being fucked this way, and she certainly seemed to enjoy it."

ele "Oh fuck. Oh fuck."

"Her back went straight suddenly and a long groan slipped out of her lips. A moment later, her hand fell away from between her legs. She was spasming in abject pleasure."

ele "I...Oh…"

"Rowan kept up his movement. After all, just because she’d already cum didn’t mean that she wasn’t enjoying it. Besides, he was too far gone by that point. Lost in the movement of hips, the rolling of sweat, and the overwhelming tightness of her virgin passage."
"If anything he sped up the pace. No holding back for her inexperience any longer. He wanted to cum inside of her rear."

ele "Ah. Fuck. Ah."

"It did not take long for the effect to bloom. Fast moving thrusts, Delane’s tight rear, and his own lust worked in tandem. After some minutes that felt like hours, Rowan felt the little twinge of his cock that warned him what was about to happen."
"Then he let loose a load of his cum. Bliss ate his senses. He slumped over on top of her. They were both panting hard. The rise and fall of their chests almost seemed to work in tandem with one another."

#lodge bg
scene bg36 with fade
show rowan necklace naked aroused at midleft with dissolve
show eleanor naked aroused at midright with dissolve

ele "Well, my sister did tell me that it hurts."

"She groaned and chuckled."

ele "I fear you’ve left me bow legged for the foreseeable future. Such rudeness."

ro "You did say I could have whatever rewards I wanted."

ele "Which is proof you have no idea what you’re doing. Because, if you did, you’d know that I have no idea what I myself am doing."

"They both laughed and settled down on the couch, closer to how it was intended to be used. His arms were wrapped tight around her naked form. As they relaxed, a question came to his mind."

ro "If your goal was to fuck me. Why go to a building full of gossips?"

ele "Do you propose I try to bring you to my parent’s residence instead?"
ele "I have a cover story for your visit. You did save my life after all. Better to leave it as rumours then risk something worse."

ro "You are the expert."

ele "I am. Which is why you should ignore my most recent statement about not knowing what I am doing, and listen to me intently."

show rowan necklace neutral at midleft with dissolve
show eleanor dress neutral at midright with dissolve

"Some time later, they had cleaned up and gotten dressed again. As enjoyable as spending the rest of the evening naked in each other’s embrace might have been, there was a limit to how long the two could stay in the same room together with watching eyes around."

label delaneLodgePostSex:

ele "How long do you intend to stay in the capital for this time?"

"Rowan shook his head."

ro "Not long. Too much trouble awaits me in the field still. The situation, especially with the northern orcish tribes is still quite grim."

show eleanor dress concerned at midright with dissolve

ele "Oh."
ele "I had heard as much. The lives of many who have sworn loyalty to my family are at stake. I suppose I cannot fault you for your diligence."
ele "Still, you could remain in the capital if you like. No one would be shocked to see you hired as a noblewoman’s bodyguard."

if delaneReject == True:
    ele "You could even bring your wife if you so chose."

show rowan necklace concerned at midleft with dissolve

"It wasn’t like the idea wasn’t tempting. Say adieu to everything he struggled with and simply live out in Rastedel as a well paid retainer. But, the concept was absurd. Even more so considering all of the aspects of his situation she was not aware of."

ro "Would that I could, my lady. But, there are people who need. There is no escape for me."

ele "Very well."
ele "..."
ele "But, the next time you are here, we will speak further. We still have much to discuss. Much indeed. You have no choice in the matter. It’s a noble decree."

"Rowan chuckled to himself. It was an absurd proposition, especially since he wasn’t even her vassal."

ro "Yes, Ma'am."

hide eleanor with dissolve

"Rowan left the lodge shortly afterwards. True to what Delane had suggested, there was an odd glance at him, but not the kind of attention one would expect if people had been able to hear what they were up to." 
"Rowan thought of the conversation they had. Soon, he would be back here. There was no way that Jezera was finished with this place. Would he be capable of tricking Delane into aiding him? Would he be capable of convincing himself to trick her?"

if avatar.corruption < 31:
    "The concept seemed repugnant. But yet, here he was."

elif avatar.corruption > 31 and avatar.corruption < 61:
    "Rowan didn’t know the answer."
    
else:
    "The answer he suspected, to both questions, was yes."

$ lodgeFirstVisit = False
jump rastMenu