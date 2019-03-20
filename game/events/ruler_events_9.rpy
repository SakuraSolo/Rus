init python:

    #Dinner is Served
    #high priority week from 4 weeks after Raeve Keep capture, requries that Helayna was not claimed
    event('dinner_is_served', triggers="week_end", conditions=('week >=4',), group='ruler_event', active=False, run_count=1, priority=pr_ruler_high)
    #Repeat sex with Acclimated Helayna
    #Repeatable.  Requires that Helayna accept her place in the castle.  Helayna must be in Rowan's room.
    #Helyana has been corrupted, and now has a somewhat negative influence on Rowan as long as she remains in his room.  That is, if corrupting him isn't the player's desired goal.
    #Should probably have some sort of counter to reduce chance of it happening too much
    event('repeat_sex_with_acclimated_helayna', triggers="week_end", conditions=('week >=4', 'rowan_shares_room_with_helayna'), group='ruler_event', priority=pr_ruler)
    #Alexia become like X'zaratl
    #Requires that initial X'zaratl's advances event have happened.
    event('alexia_become_like_xzaratl', triggers="week_end", conditions=('week >=4',), depends=('xzaratl_s_advances',), group='ruler_event', run_count=1, priority=pr_ruler)
    #The Demonic Tome
    #4-6 weeks after A Trip to the Library #(activated in "trip_to_library")
    event('the_demonic_tome', triggers="week_end", conditions=('week >=4',), group='ruler_event', active=False, run_count=1, priority=pr_ruler_high)


label dinner_is_served:
#Dinner is Served
#high priority week from 4 weeks after Raeve Keep capture, requries that Helayna was not claimed

scene bg9 with fade

if alexiaSeparateRoom == True:
    show rowan necklace neutral at midleft with dissolve
    show orc soldier neutral at midright with moveinright
    os "Oi, ‘uman. Masters request your presence in ballroom for dinner when seventh bell rings."
    os "Don’t be late, or else."
    hide orc sodier with moveoutright
    ro "Dinner? I wonder what those two are up to now."

else:
    show rowan necklace neutral at midleft with dissolve
    show alexia necklace neutral at midright with dissolve
    show orc soldier neutral at edgeright with moveinright
    os "Oi, ‘uman. Masters request your presence in ballroom for dinner when seventh bell rings. Both of yous."
    os "Don’t be late, or else."
    hide orc sodier with moveoutright
    ro "Well, he was about as charming as usual. What do you suppose this is all about?"
    al "It is strange, we’ve been here for months now, and there’s never been any sort of dinner. And in the ballroom as well?"
    ro "They were pleased when I managed to take the keep from the Duke, maybe they want to celebrate that victory together."
    al "That was weeks ago though. I don’t know, I just don’t trust them."
    ro "Neither do I darling, we will just have to be careful."
    ro "Anyway, I had better head out, I still have work to do before dinner. Try not to worry, okay?"
    show rowan necklace happy at midleft with dissolve
    al "Okay. Be careful, my love."
    ro "I always am."
    hide rowan with moveoutright

scene bg27 with fade

if alexiaSeparateRoom == True:
    show rowan necklace neutral at midleft with dissolve
    show alexia 2 necklace neutral at edgeleft with moveinleft
    ro "Alexia? They made you come here as well?"
    al "Yes, an orc showed up in my room this morning and informed me that attendance was mandatory."
    ro "I don’t think there’s an orc alive who knows the words attendance or mandatory."
    al "Well, those weren’t the exact words he used, my love."
    ro  "What do you suppose this is all about?"
    al "It is strange, we’ve been here for months now, and there’s never been any sort of dinner. And in the ballroom as well?"
    ro "They were pleased when I managed to take the keep from the Duke, maybe they want to celebrate that victory together."
    al "That was weeks ago though. I don’t know, I just don’t trust them."
    ro "Neither do I. Shhh, here they are now."

else:
    show rowan necklace neutral at midleft with dissolve
    show alexia 2 necklace neutral at edgeleft with dissolve
    al "I don’t see them."
    ro "We are a little early I suppose."
    al "Oh, here they are now."

show andras happy at edgeright with moveinright
show jezera happy at midright with moveinright

"The twins entered from the doorway at the opposite side of the room, and walked over to the long table at the other end. It was far too big for just the four of them, but this sort of over the top opulence was what Rowan had come to expect from the demons."
"At the top of the table, near to where Jezera and Andras now stood, four places had been set, and the surrounding part of the table had been furnished with fresh flowers and more extravagant ornaments."

an "Ah there you two are you are. Well, don’t stand there all day gawping, come and join us."

je "Yes, please do. We won’t bite."

"The demon flashed a cheeky grin the pair had seen many times before."

je "Unless you ask us to, that is."

scene bg27 with fade
show rowan necklace neutral at edgeleft with dissolve
show alexia 2 necklace neutral at edgeright with dissolve
show jezera happy at midleft with dissolve
show andras happy at midright with dissolve

"The hero and his wife did as they were told, joining the demons at the far end of the table. Andras and Jezera took the two places that had been set at the head, the usual seat of power being divided into two equal ones."
"Rowan had been positioned to their right, and Alexia to their left, separating the two. Alexia, who would have much rather have been seated by her husband’s side, could only look across the width of the table at him."

je "Now, that’s much better isn’t it? I hope you two are hungry, the chefs have been busy in the kitchens all day."

an "I could eat a horse."

je "You probably {i}have{/i} eaten a horse."

show andras displeased at midright with dissolve

"The demon, unhappy at the joke made by his sister at his expense, threw a snarl in her direction, to which she responded by rolling her eyes."

je "Oh behave brother, we have company."

"Turning away from him, she addressed the others at the table."

je "Anyway, we just wanted to do something to show you that we appreciate the hard work you both have been doing. As I told you initially, there is no need for us to be enemies."

show andras happy at midright with dissolve
an "Indeed. As long as you do as you are told, and perform your tasks well, you will be rewarded."

#if you captured the keep using force

an "Even I admit I was a little impressed with the way you captured Raeve Keep."

je "I may find the whole thing barbaric, but I suppose I cannot argue with result. It was a job well done."

#if you captured the keep using spies

je "The way you infiltrated the keep was masterful, you are clearly a man after my own heart, my hero."

an "My sister’s cowardly methods may disgust me, but you captured the keep, and I must admit, that was the important thing."

#rejoin

je "Oh, where are my manners? Your glasses are empty, would you like something to drink?"

"Alexia, not wanting to offend their hosts, politely affirmed, as did her husband who had noticed her slight unease."

al "Yes, please. If it isn’t too much trouble."

ro "And I am a little thirsty myself to tell the truth."

je "Trouble? What sort of a hostess would I be if it were any trouble. No. Slave? Bring our guests some wine before they die of thirst."

#cg of naked Helayna entering, carrying a pitcher of wine
scene black with fade
show rowan necklace neutral behind black
#helayna naked
show helayna naked aroused behind black
show jezera happy behind black

"Rowan’s jaw almost hit the floor when he saw that the slave to whom Jezera referred was the knight from Raeve Keep. He hadn’t seen her since the day the keep had fallen, and had, perhaps naively, believed that she had been freed as the demoness said she would be. "
"He broke his gaze to glance across the table at his wife, who was giving him a worried look. “Helayna”, he mouthed, and her mouth crinkled into a furtive frown."

ro "Helayna.. I thought…"

hel "Hello [helaynaTitle]…"

"The woman did her best to smile, despite the awkwardness of the situation."

je "Are you going to stand there all day yapping, or are you going to do your job?"

hel "Oh! Sorry mistress."

"Remembering her place, the servant made her way over to the table and filled Rowan and Alexia’s goblet as ordered."
"Once done, she looked over at Jezera, who indicated for her to fill the demons’ as well. As she leaned over to fill Jezera’s, the demoness gave her firm derriere a hard spank."

hel "Unnn…"

"The woman shuddered, and let out a soft moan. Her tormentor grinned in approval."

je "I think I’m going to have to discipline you some more, you are hardly giving our dinner guests a good impression with service like that."

hel "Yes, mistress…"

#cg of Jezera fingering Helayna’s cunt
scene black with fade
show rowan necklace neutral behind black
show helayna naked aroused behind black
show jezera happy behind black
show andras happy behind black

"The demoness slid her hand down from the former knight’s ass, and placed it instead between her legs. Helayna inhaled sharply as one finger, and then another, penetrated her tight pink pussy."

je "If you cannot provide a good service, I suppose you can at least provide some entertainment."

hel "Yesssss…"

"Any embarrassment or shame she may have felt about the situation melted away as quick as the expression on her face, and she gave in to her baser instincts, amplified by the ring."
"Jezera continued to frig her sodden cunt, as Helayna moved against her fingers, her moans increasing in intensity."
"Alexia turned away, unable to watch the debasement of the poor girl by their captors, while Rowan looked on, his horror tinged with arousal."
"The other demon chuckled at the display."

an "Not bad, sister. Perhaps we should have this slut provide the entertainment at every meal."

"Helayna either didn’t hear Andras’ crude comment, or didn’t care as she bucked against Jezera’s hand, her rapid breathing signally her approach to orgasm."
"Before she could get there, however, the demoness pulled her hand away, and Helayna whined like a small child deprived of her favourite toy."

je "No, slave. After today’s poor performance, you don’t deserve to cum."

"Between pants, the woman managed to get her pleading out."

hel "But I… I…"

"She glanced at the hero with a look that was half crushing disappointment, and half pure animal lust."

je "Get to the kitchens. The food must almost be ready by now."

scene bg27 with fade
show andras happy behind bg27
show jezera happy behind bg27
show helayna naked aroused behind bg27

"Helayna exited the room, leaving Rowan and Alexia alone with the demons. Andras said very little, while Jezera made small talk about her interests, and the day to day life of the castle like nothing had happened."
"After fifteen very awkward minutes, Helayna returned. She was doing her best to balance the tray of food, but was obviously still feeling the effects of Jezera’s assault."
"She trembled from the ring’s amplified arousal, and the juices from her sodden cunt ran down her leg."
"With some effort she carried the tray over to the table and placed it down in the middle. Lifting the cloche, she revealed a cooked bird, large enough to easily feed the four of them."

an "Shall I carve it, sister?"

je "If you want, but use a knife, and not your claws, at least."

"Ignoring her insult, the demon carved four large portions for each of the four sat at the table. The two humans ate cautiously as Jezera picked at her food, and Andras tore into it as one would expect of a demon."

hel "Will that be all, masters?"

an "Not so fast, slut. I have other {i}appetites{/i} that have yet to be sated."

"He pushed aside the cloth covering his lower half to reveal his thick red cock, half erect, presumably from his sister’s show earlier. The servant ogled it hungrily, unable to tear herself away."

hel "Would you like me to… take care of that, my lord?"

menu:
    "Object.":
        $ released_fix_rollback()
        show rowan necklace angry behind black
        ro "That's enough!"
        je "Hmmm?"
        ro "You might find this display amusing, but I'll have no part in it. Come on Alexia, we are leaving."
        je "How rude."
        "The pair left the twins, the rest of their meals, and this whole charade behind. As they exited the room, a cacaphony of moans and other sex noises, and laughter could be heard in the distance."
        return

    "Say nothing.":
        $ released_fix_rollback()
        jump dinnerSex

label dinnerSex:

scene cg102 with fade
show helayna naked aroused behind cg102
show jezera happy behind cg102
show andras happy behind cg102
show rowan necklace neutral behind cg102
show alexia 2 necklace concerned behind cg102
pause 3

"The demon gave his answer in the form of an action, pulling her down on top of him, so that her back was against his chest. Thankfully she was still sopping wet from her earlier encounter, as Andras unceremoniously forced his fat cock inside her."

hel "Unnnnnnnn!!!"

"Helayna didn’t seem to mind, she began to ride without needing any further instruction. Her pert tits bounced up and down as she grinded on the demon’s huge dick, taking it to the edge of her cunt, then pushing down to force it as deep as she could take it."
"Her expression was one of pure animal lust; she was lost to the world, concerned with only one thing."

je "So, Rowan, with all the work that Skordred has been doing around the place, is it start to look like the Bloodmeen that you remember?"

ro "Errr…Well, yes. Back when your father-"

hel "Fuck me! Fuck me! Fuck me!"

ro "-inhabited it, it was a lot more impressive. Obviously the war and the years-"

hel "So biiiiiiiiiig!"

ro "-have taken their toll, but it is starting to get there."

hel "...fucking deep, unnnnnn!"

je "And Alexia, I hope you don’t find your quarters too drab. There aren’t that many rooms in the castle suitable for we ladies I’m afraid."

al "Oh no, it is uh…"

#if alexia had sex with andras in the intro
if andras_alexia_sex:
    scene cg103 with fade
    show helayna naked aroused behind cg103
    show jezera happy behind cg103
    show andras happy behind cg103
    show rowan necklace neutral behind cg103
    show alexia 2 necklace concerned behind cg103
    pause 3
    "She glanced over at Helayna and saw the look of pure bliss on her face. As she remembered what it felt like that have that thing inside of her, her body shivered."
    "But was it the tremble of the mind recalling an unwanted memory, or the subconscious response to a past sensation of pleasure?"
#else
else:
    "She glanced over and saw the expression on Helayna’s face. She looked like a woman who was completely lost, and Alexia felt sorry for her. She could only turn away."

#rejoin

al "-perfectly fine. I don’t really need a lot of space, and to be fair, it is nearly as big as our entire house."

je "Excellent, if you have any issues, just let me know."

"As they continued their small talk, Andras’ fun began to reach its climax."

an "Ready for my load, whore?"

hel "Yessss! Give it to me!"

if andras_alexia_sex:
    show cg103 with sshake
    show cg103 with sshake
    scene cg104 with flash
    show helayna naked aroused behind cg104
    show jezera happy behind cg104
    show andras happy behind cg104
    show rowan necklace neutral behind cg104
    show alexia 2 necklace concerned behind cg104
    pause 3

else:
    show cg102 with sshake
    show cg102 with sshake
    scene cg104 with flash
    show helayna naked aroused behind cg104
    show jezera happy behind cg104
    show andras happy behind cg104
    show rowan necklace neutral behind cg104
    show alexia 2 necklace concerned behind cg104
    pause 3

"The demon laughed as he came deep within her. The woman screaming in orgasm, and then collapsed against his chest, savouring the warm, gooey sensation now within her loins."

an "That’ll be all, you can go now, slave."

"When she stood, her legs were so weak that she almost collapsed onto the hard stone floor. She steadied herself using the table, as cum dripped from her well fucked snatch."

an "Aren’t you forgetting something?"

hel "Uhhh… thank you master…"

"She left without even looking at Rowan, unable to face him after the shame of what had just occurred. This didn’t help assuage any of the guilt he was feeling from yet another good person being dragged into the orbit of the twins because of him."
"The rest of the dinner continued with a mixture of forced small talk and awkward lulls into silence. Helayna was not seen again, as another serving girl brought out the other courses."
"As soon as it was possible for them to do so without it being perceived as rudeness, the human pair made their excuses to leave, both perturbed by the evening’s events."

#rowan gains a small amount of guilt
#if alexia had sex with andras in the intro, she gains a small amount of corruption
$ change_base_stat('g', 2)
if andras_alexia_sex:
    $ change_corruption_actor('alexia', 2)
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label repeat_sex_with_acclimated_helayna:
#Repeat sex with Acclimated Helayna
#Repeatable.  Requires that Helayna accept her place in the castle.  Helayna must be in Rowan's room.
#Helyana has been corrupted, and now has a somewhat negative influence on Rowan as long as she remains in his room.  That is, if corrupting him isn't the player's desired goal.
#Should probably have some sort of counter to reduce chance of it happening too much

scene bg9 with fade
show helayna naked aroused at center with dissolve
show rowan necklace happy at edgeleft with moveinleft

"When Rowan entered his room, he discovered that Helayna was waiting for him on the windowsill, a come hither look on her face."

ro "My Helayna, if I wasn't mistaken, I would say you're trying to seduce me."

hel "Why, I'd never do such a thing. I am a knight after all. However, if someone had certain duties to fulfill, I might be inclined to seek an appropriate setting."

"After taking a seat next to her, Rowan replied to her comment."

ro "And what duties might those be?"

#Helayna giving blowjob CG.
scene black with fade
show rowan necklace happy behind black
show helayna naked aroused behind black

"Instead of answering his question, his mistress deftly removed her dress and pulled open her lover's pants. Then she dove down and engulfed his growing length into her mouth."

ro "Wow. Where did you learn to give head like that?"

"Given the current obstruction, there was no way that Helayna could meaningfully answer him. That didn't stop her from doing it anyway, taking full advantage of the act to add to her blowjob."

ro "Hahah, you really have a way with words."

"With an audible plop, she removed his now very stiff length from her maw and grinned at Rowan."

hel "Thanks. Think you could maybe help me fill up my lower lips? They're feeling so achingly, painfully, empty."

#CG of Rowan fucking Helayna missionary.
scene black with fade
show rowan necklace happy behind black
show helayna naked aroused behind black

"As she said that, she jumped up and flipped over onto the bed.  With two fingers, the pink haired woman pushed her slit open and presented herself to the hero. All too eager to comply with her invitation, Rowan pounced on the woman and pushed himself inside her in one smooth motion."

hel "Hmmm, thanks lover. It feels so good to soothe my burning loins with your sword."

"In-spite of her recovered faculties, Helayna still wanted to be fucked hard and fast, so Rowan did exactly that. Her lusts remained, they just didn't consume her anymore."

ro "What can I say? You've got a great sheath."

"That passage was slick with arousal, as it always was. That wasn't to say that it's owner was the same every time Rowan took her, she always had a few new moves and liked to play with the way she squeezed down on him to surprise him along the way."

hel "Tell all the girls you take that. I wanna hear about lots of other conquests."

"This was a newfound kink that had caught Rowan off-guard. He wasn't sure if it was the band who'd caused it, like Helayna's strange oral skills, or if it was something she'd always had beforehand."

ro "Sounds like you're being a bit of a bad influence on me."

"She laughed, since their confession of love, Helayna had fully embraced the lusts that had been forced upon her. Along with that, and her love of Rowan, she'd started to get a rather dirty mind and liked to encourage Rowan in rather naughty things."

hel "Hrmm, can't be a bad influence if it makes you feel good, can it? I think you taught me that one."

"Both stopped the conversation as their peaks approached. This was the point where Rowan's strength finally gave out and Helayna lent hers to help him."
"Wrapping her legs about his hips, she pulled him tightly against her and made certain he was as deep as possible as he filled her up with his white seed. Shortly afterwards, the man fell forwards onto his lover, who embraced him gratefully for helping her fulfill her needs."
"The two simply lay there for several minutes. Helayna had no intention of letting her love slip from inside her for some time and Rowan was content to remain and recover from the sex that inevitably robbed him of breath."

#Rowan gains a little corruption.
$ change_base_stat('c', 2)
# set timer on this event, so it will not happen before 3 weeks will pass
$ set_event_timer('repeat_sex_with_acclimated_helayna', 'delay', 3)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_become_like_xzaratl:
#Alexia become like X'zaratl
#Requires that initial X'zaratl's advances event have happened.

scene bg14 with fade

show alexia 2 necklace neutral at midleft with moveinleft

al "Hm?"

show xzaratl neutral at edgeright with dissolve
pause 1
hide xzaratl with dissolve

show xzaratl neutral behind bg14

xz "Alexia, oh Alexia?"

show alexia 2 necklace angry at midleft with dissolve

al "You! What do you want?"

"The demoness flitted in and around her, speaking directly into her mind making it hard to tell if the beast was real or not."

xz "Have you ever wondered what it would be like to be someone like me?"

al "You mean a monster? Hardly."

hide xzaratl
show xzaratl neutral at edgeright with dissolve

xz "Oh ha, no not like a demon, I mean one who is of two kinds. A woman who knows what it's like to be a man as well."

show alexia 2 necklace neutral at midleft with dissolve

al "What are you getting at?"

xz "My darling pet, would you like to try having a cock for a day? To feel what it's like for your husband?"

show alexia 2 necklace shocked at midleft with dissolve

al "What?"

menu:
    "The idea of having a penis intrigued Alexia.":
        $ released_fix_rollback()
        $ futaIntrigued = True
        jump alexiaFuta

    "Without hesitation, Alexia refused.":
        $ released_fix_rollback()
        show alexia 2 necklace angry at midleft with dissolve
        al "No! Why would you even suggest something so vulgar to a lady!"
        #xzaratl disappointed
        xz "That's such a shame. Not even an inkling? Hmm, guess I'll have to think of something else for next time."
        hide xzaratl with dissolve
        "Then, as quickly as she'd appeared, the succubus vanished."
        show alexia 2 necklace neutral at midleft with dissolve
        "Alexia let out a sigh of relief, glad to be done with that."
        return

label alexiaFuta:

"Alexia froze up, unsure how she felt about what was going on. X'zaratl didn't give her the chance to think about it, she just stepped in closer and brazenly fondled the red haired woman."

show alexia 2 necklace aroused at midleft with dissolve

"The succubus's hand seemed to pass right through the fabric of her dress and brush up over the folds of Alexia's womanhood, going further up and pinching the hood of her clit."

al "Wha...?  Wait, stop, no...."

xz "Yes... you want this, admit it. Just let it happen."

"A loud moan escaped Alexia's lips as she felt a strange erotic rush..."

scene black with fade
show xzaratl neutral behind black

xz "Let's go back to my place and I'll get your husband to come see just how beautiful you are like this!"

"About fifteen minutes later..."

scene bg23 with fade

show rowan necklace neutral at midleft with moveinleft

ro "X'zaratl? You wanted to see me?"

"He was rather surprised to see that the head of the sanctum wasn't at the entrance to meet him after she'd called him down here. A loud sigh escaped his lips, this was probably another of her games."
"Already the sound of feminine moans drifted to his ears from across the room. Wary of an ambush, Rowan made his way across the chamber to X'zaratl's personal room and drew the curtain aside."

scene cg99 with fade
pause 3

"It wasn't X'zaratl that Rowan saw inside, nor one of the castle's cubi.  It was his wife, naked, and masturbating a rather sizable cock with her hand!"

show rowan necklace shock behind cg99

ro "Alexia? What happened to you?"

"Oblivious to his arrival, the red haired woman continued to rapidly pump her new meat, up and down, while gasping in pleasure at the same time."
"A wave of arousal overcame Rowan when he stepped into the room. He tried to resist, but his wife working her shaft caught his attention, then mesmerized him."
"That soft flesh, emerging from above her womanhood and proudly proclaiming her arousal. The way the flesh pulled onto and off of her glans, that it looked to be just a touch bigger than his. Was it twitching?"

show cg99 with sshake
show cg99 with sshake
scene cg100 with flash
pause 3

"Alexia grunted with apparent effort, bucked her hips, and let loose a big thick stream of cum in an arc from her shaft. It made quite the puddle."
"Such a shocking display managed to shake Rowan out of his reverie, giving him some lucidity again. First item of note for him was to reaffirm that his wife did indeed have a cock. Second, was that his own strained against his pants and already had formed a wet spot around the tip."


"Lastly was that Alexia seemed to have finally taken note of his arrival and had locked eyes with him."

show alexia necklace naked aroused behind cg100

al "Oh Rowan, I had no idea how wonderful it was to be a man! What do you think of my new sword?"

"A coy look crossed her face."

al "Darling, how about you give it a little kiss?"

menu:
    "As per her request, he gave her a blowjob.":
        $ released_fix_rollback()
        $ rowanFutaSuck = True
        #CG of Rowan giving Alexia a blowjob with her hands on the back of his head.
        scene cg101 with fade
        pause 3
        "Rowan knelt down in front of Alexia and placed a kiss on the purple head."
        show alexia necklace naked aroused behind cg101
        al "Hmm, keep going."
        show rowan necklace happy behind cg101
        ro "Like this?"
        "Rowan started to run his tongue around the glans, then ran it all the way down her length. She melted under his ministrations, putting her hands on his head in a desperate attempt to stay on her feet."
        ro "Hhhgmmm!"
        "In-spite of being on the verge of toppling over, the woman started pistoning her hips forwards and backwards, fucking her husband's face at a rapid pace while he continued working on her."
        al "That feels so good..."
        ro "Hmmph!"
        "This reversal of roles excited the man and he enthusiastically tried to suck down this alien cock in his mouth as well as he could, slurping and licking it on each pass in and out."
        al "Oh, darling, take it! Take all of me!"
        "Roughly she plunged her length down his throat! Rowan tried to gag, but couldn't do anything but feel the rush of liquid pass through Alexia's cock and be deposited straight into his stomach."
        al "Yes! Yes. My husband...."
        "She held him there, choking on her for a moment after her orgasm had stopped, then her legs gave out and the resulting tumble popped her free."
        "Finally able to breath again, Rowan gasped and coughed in desperation for several seconds before he noticed the succubus who was standing nearby, evidently a close observer of the recent event."
        #Note blowjob happened for later in scene.  Increase X'zaratl scene count by 1.  Rowan and Alexia gain some corruption.  Rowan's influence over Alexia increases.
        $ event_tmp['blowjob'] = True
        $ change_base_stat('c', 2)
        $ change_corruption_actor('alexia', 2)
        $ set_actor_flag('alexia', 'rowan_influence', get_actor_flag('alexia', 'rowan_influence') + 2)
        $ xzaratl_scene_count += 1

    "Put a stop to this.":
        $ released_fix_rollback()
        $ event_tmp['blowjob'] = False
        show rowan necklace neutral behind black
        ro "No, stop.  Alexia, do you realize what you're saying? This isn't your body, these aren't your thoughts. This has to be some trick or lie."
        show xzaratl neutral behind black
        xz "Hmph. Silly pet, that is an authentic cock! She's just a little overwhelmed by the new sensations."
        "Rowan turned to the source of the voice and saw the succubus lurking in the corner of the room."

scene bg23 with fade
show rowan necklace angry behind bg23
show xzaratl neutral behind bg23

ro "X'zaratl? This is your doing, isn't it? You did this to Alexia."

xz "So much anger. Are you thinking I went tampering with your love? Worry not, this change is not permanent."

"A soft click clack sounded through the suddenly silent room as X'zaratl walked next to Alexia, then outstretched her hand to run it over the still hard flesh protruding unnaturally from Rowan's wife."

xz "I've given both of you a gift, a chance to see what it's like for each other. This understanding helps lovers stay together, for their love to grow stronger than ever. Not to mention that such a lovely couple as yourselves could use a little spicing up in the bedroom too."

#If Rowan has refused all previous sex scenes with X'zaratl.
if xzaratl_scene_count == 0:
    ro "How hard is it to realize that we don't want anything you have to offer?"

    xz "Maybe you don't, but your wife has realized the pleasures and joys I can give both of you."

#If Rowan previously had sex with X'zaratl penetrating him.
else:
    xz "You've already shown that you love the thought of a girl's cock up your ass, what about the chance at your wife's now? Hmmhmm, I knew that'd get a rise out of you."

"The second of X'zaratl's right hands came up to stroke Alexia's shaft as well."

xz "To help you savor this gift, I've also poured my endurance into Alexia. She can go as many times as you want, without fear of growing soft. Now pets, ready to experience the real treat?"
xz "Pucker up Rowan, time to be the woman to Alexia's shaft with your ass. Oh, and don't mind me taking your face, I promise I'll be gentler than your wife will probably be in that state. She does look a bit hungry."

menu:
    "The succubus's power was too much to resist.":
        $ released_fix_rollback()
        jump alexiaFuta2

    "Rowan wanted no part of what X'zaratl had in mind.":
        $ released_fix_rollback()
        "Enough was enough, Rowan wanted no part in what was being offered and he managed to throw off X'zaratl's lusts this time."
        ro "You witch, stop forcing your sick fantasies on us! Just let us be!"
        xz "I don't think so, you see Alexia still wants this, so if you're not willing to cooperate I guess I'll just have to force you to accept it."
        ro "Are you sure about that?"
        xz "Hmm? Oh Kharos take you!"
        scene bg23 with fade
        show rowan necklace neutral at edgeleft with dissolve
        show alexia necklace naked at center with dissolve
        #xzaratl mad
        show xzaratl neutral at edgeright with dissolve
        "The succubus had turned and noticed that the cock that Alexia had been given was retreating back into her flesh! A moment later, it was completely gone."
        xz "Just why are you rejecting me now of all times?"
        "The red haired woman's voice was barely a whisper that almost couldn't be made out."
        al "I... I won't hurt Rowan."
        ro "You see? This game of yours is over!"
        xz "Fine, leave! I can't force this on Alexia anyway. Looks like I'm going to have to figure out something else for next time."
        "After grabbing one of the blankets scattered about and draping it over his wife, the man helped her leave the room."
        ro "Darling, let's go."
        hide rowan with moveoutleft
        hide alexia with moveoutleft
        return

label alexiaFuta2:

$ rowanFutaAnal = True

"Once more, the unnatural lust overwhelmed Rowan and he willingly got on his hands and knees, removed his trousers, and presented his ass to his wife."

#CG of futa Alexia on Rowan doggie style.
scene black with fade
show xzaratl neutral behind black

"The obvious invitation made her let out a little squeal of excitement and Alexia lept forward to accept."

xz "Oh you two are just so adorable together!"

"In her lust addled state, the woman made no attempt to prepare her husband or lubricate him. Instead she forced herself inside, with only her cum to help her girlcock's passage. Immediately she wrapped her arms around Rowan's chest and hugged him tightly."
"The rough penetration elicited a grunt of shock and pleasure mixed together from Rowan as his insides were forced apart to accommodate the new intruder inside him."

show alexia necklace naked aroused behind black
show rowan necklace naked aroused behind black

al "Darling, you're really tight. It feels so good to be inside you."

ro "My love... wow."

"After savoring the sensations for a moment, Alexia began bucking against her husband in earnest. Her movements were awkward and unfamiliar, but very enthusiastic."
"With so powerful of sensations emanating from his ass from the rough fucking, the hero was forced to grit his teeth and clench his eyes shut. This act also made Alexia even more excited, since he'd clenched his sphincter down on her as well."

xz "Since you two seem to be well on your way, I think I'll just invite myself to join in."

"Rowan managed to open his eyes and saw X'zaratl squatting down in front of him, her lower garments already removed and erect cock staring him in the face. She lovingly cupped his head with her upper arms, while the lower ones lined her sex up with him."

scene cg147 with fade
show rowan necklace naked aroused behind cg147
show xzaratl neutral behind cg147

pause 3

"Some more of her magic flowed into the man's mind, giving him an uncontrollable desire to open his mouth and suck her cock down. So he did so, accepting her willingly."
"Now there were two dick equipped women using Rowan to sate their lusts, one in front and one in the back."
"A warm hazy pleasure had replaced the earlier pain from his rear, so now Rowan was able to enjoy the experience at least somewhat, though he was unable to vocalize it."

xz "That's right Rowan, learn your love, understand why she loves your manhood by accepting hers."

ro "Hmmgh."

scene cg148 with fade
show alexia necklace naked aroused behind cg148
show xzaratl neutral behind cg148
pause 3

"The succubus's upper hands continued to caress his hair and face, while her lower ones now held onto his neck and stopped him from making any attempt to escape from her. Though it wasn't her treatment that was affecting him the most, that was his wife's."

al "Rowan, oh Rowan, I think I'm about to cum! Please, let me fill you, let me show you how wonderful it is when you fill me!"

"There wasn't anything he could do about it, whether he wanted to or not. If Alexia wanted to fill his ass with her false seed, she would soon be doing exactly that."
"Apparently X'zaratl could read his thoughts or at least sensed what he was feeling, as she addressed him even while she continued fucking his face."

xz "Don't be so hesitant my pet. Embrace it. Someday there may be more, but today there are no consequences to fear, nothing to lose, enjoy this gift."

"Those gasps of pleasure that Alexia had been letting out were quickly growing shorter and of a higher pitch. There was no doubt that her orgasm was approaching. Apparently Rowan's gagged gasps and mouth were also having an effect on X'zaratl."
"Or perhaps she intentionally was timing her pleasures to Alexia's."
"Regardless of the reason, both of their orgasms arrived simultaneously."

show cg148 with sshake
show cg148 with sshake
scene cg149 with flash
pause 3

"At the same time as he tasted the salty goo in his mouth from X'zaratl, the sensation of hot fluid filled his ass. Surprisingly, while the succubus gave him about a mouthful of her seed, his wife's gift seemed to go on and on, filling him more and more. Soon he felt rather bloated."
"After forcing him to swallow her gift, X'zaratl finally pulled away from the man's face and allowed him some degree of freedom again."
"Alexia made no move to pull out of him, in fact she had once again lost herself to the pleasure and hung onto him tightly for some semblance of stability. She kept her arms wrapped around his chest and cock deeply entrenched."

scene black with fade
show rowan necklace naked behind black

ro "*cough* Um, Alexia? Are you going to let go?"

"She didn't respond, only rubbing her breasts on his back while cooing and sighing contentedly. Rowan looked around the room, only to find that apparently X'zaratl had abandoned him to his wife."
"Soon after that thought he noticed that at some point during the event, he'd cum as well. There was a small puddle underneath him."
"It wasn't until around half an hour later when Alexia's cock retreated back to the place it had come from did she finally release her husband from her grip."

#If blowjob did not happen, increase X'zaratl scene count by one.  Rowan and Alexia gain corruption.  Rowan influence with Alexia increases.
if not event_tmp['blowjob']:
    $ xzaratl_scene_count += 1
$ change_base_stat('c', 2)
$ change_corruption_actor('alexia', 2)
$ set_actor_flag('alexia', 'rowan_influence', get_actor_flag('alexia', 'rowan_influence') + 2)
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_demonic_tome:
#The Demonic Tome
#4-6 weeks after A Trip to the Library

scene bg9 with fade

if alexiaSeparateRoom == True:
    show rowan necklace neutral at midleft with dissolve
    show alexia 2 necklace concerned at midright with moveinright

else:
    show alexia 2 necklace concerned at midright with dissolve
    show rowan necklace neutral at midleft with moveinleft

al "Rowan…"

ro "Yes, my love?"

"The hero noticed the nervousness in his wife’s tone. Her arms were wrapped around a large bound book that he had never seen before."

ro "What’s that you have there?"

al "It’s a book I found in the library."

ro "Oh?"

al "Truth is, I’ve had it for a few weeks, but I’ve been hiding it…"

show rowan necklace happy at midleft with dissolve

ro "You didn’t need to hide it darling."

al "I know, I just didn’t know what to do with it."

"She held the book out and opened it, to show her husband the strange language and illustrated chaos within."

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

al "I think it might contain some information that could help us, but I’ve not been able to make any sense of it. I even tried to find other books in the library that might be helpful, but had no luck."

ro "What do you think it is?"

al "Some sort of history of demons, perhaps? Whatever it is, it might be something we could use against the twins."

if NTR == True:

    menu:
        "Suggest she ask Andras for help.":
            $ released_fix_rollback()
            ro "Perhaps Andras would help you, you did say he was quite pleasant with you when you here as their hostage."
            al "I guess, he did suggest the book in the first place when I was in the library. I don’t trust him though."
            ro "I don’t trust him either, but I don’t think he’d hurt you."
            al "I agree, the twins still want to use me as leverage against you."
            al "I guess it is settled then."
            ro "Okay, but just be careful."
            show alexia 2 necklace happy at midright with dissolve
            "The woman gave her husband a kiss, and a smile."
            al " Don’t worry, if I feel things are starting to take a turn for the worse, I’ll just leave. You just go about your day as normal so the demons won’t suspect anything."
            ro "Okay, I’ll see you later. Love you."
            al "Love you too, husband."
            $ alexia_and_her_demon_book = 2
            hide rowan with moveoutleft
            jump andrasHelp


        "Suggest she ask Jezera for help":
            $ released_fix_rollback()
            ro "You could try asking Jezera for help. While she may be our captor, she seems a lot more reasonable than her brother."
            ro "If she thinks helping you might view her and her cause in a more favourable light, she might be willing to tell you about the book."
            al "I guess, she seems nicer, but it feels a little… I guess, cold? Calculated? I think there’s someone else hiding under that facade. I don’t trust her."
            ro "I don’t trust her either, but I don’t think she’d hurt you."
            al "I agree, the twins still want to use me as leverage against you."
            al "I guess it is settled then."
            ro "Okay, but just be careful."
            show alexia 2 necklace happy at midright with dissolve
            "The woman gave her husband a kiss, and a smile."
            al " Don’t worry, if I feel things are starting to take a turn for the worse, I’ll just leave. You just go about your day as normal so the demons won’t suspect anything."
            ro "Okay, I’ll see you later. Love you."
            al "Love you too, husband."
            $ alexia_and_her_demon_book = 3
            hide rowan with moveoutleft
            jump jezeraHelp


        "Tell her it is too risky.":
            $ released_fix_rollback()
            ro "I appreciate your wanting to help, my love, I really do, but it is too risky."
            al "I could be careful."
            ro "I know you could, but we don’t know what we are dealing with. They already kidnapped you, we have no idea what else they have planned."
            al "Andras was the one who originally suggested the book to me in library."
            ro "That alone is suspicious, this whole thing could be a trap. We just don’t know."
            al "I suppose you are right…"
            show rowan necklace happy at midleft with dissolve
            "The man took her by the hand, and smiled at her."
            ro "I’m sure there’ll be plenty of ways for you to help in the future darling, but we can’t take any dangerous chances. I don’t know what I’d do if anything happened to you."
            al "I understand. I just hate being stuck here while you are out there, doing nothing. I feel so useless."
            ro "Alexia..."
            al "You’d better go, I’ll return this book to the library, and then we can forget all about it."
            ro "Okay, I’ll see you later. Love you."
            al "Love you too, husband."
            hide rowan with moveoutleft
            return

else:

            ro "I appreciate your wanting to help, my love, I really do, but it is too risky."
            al "I could be careful."
            ro "I know you could, but we don’t know what we are dealing with. They already kidnapped you, we have no idea what else they have planned."
            al "Andras was the one who originally suggested the book to me in library."
            ro "That alone is suspicious, this whole thing could be a trap. We just don’t know."
            al "I suppose you are right…"
            show rowan necklace happy at midleft with dissolve
            "The man took her by the hand, and smiled at her."
            ro "I’m sure there’ll be plenty of ways for you to help in the future darling, but we can’t take any dangerous chances. I don’t know what I’d do if anything happened to you."
            al "I understand. I just hate being stuck here while you are out there, doing nothing. I feel so useless."
            ro "Alexia..."
            al "You’d better go, I’ll return this book to the library, and then we can forget all about it."
            ro "Okay, I’ll see you later. Love you."
            al "Love you too, husband."
            $ alexia_and_her_demon_book = 1
            hide rowan with moveoutleft
            return

############################

label andrasHelp:

scene bg7 with fade
show alexia 2 necklace neutral at midleft with dissolve
play sound "music/SFX/door knock.ogg"
pause 1

al "Come in."

show andras happy at midright with moveinright

an "Hello Alexia. I believe that you were trying to find me?"

al "Yes..."
al "I looked around but I had no luck. I suppose one of your orcs told you?"

an "You guessed right. Sometimes I have to leave the castle on business too, your husband isn’t the only person around here that has thing he needs to do."

al "I wasn’t trying to say-"

an " Don’t worry your pretty face, I wasn’t suggesting that you meant anything by it. Just know that both my sister and I are working just as hard as Rowan towards our goals."

al "(Now might be a good time to try and get some information)"
al "What sort of business, if you don’t mind me asking?"

an "Not at all. I often have to go out to Rosaria to check on our orc soldiers, they are a very undisciplined bunch unfortunately, and have to be shown a firm hand."

al "I see, I never really thought about the orcs outside of the castle, I must admit."

an "And why would you? Things like these aren’t really the concern of sweet girls like yourself. I also try to keep an eye on the enemy forces, to see if there’s any unusual activity."

al "Like?"

an "Reinforcing certain locations, mustering, patrols that might serve problematic; that sort of thing."

al "And your sister?"

an "She has different concerns. Her agents are scattered across the six realms, and it makes more sense for her to visit them than for them to travel here. In disguise, of course."

al "Of course."

an "And then there’s her most important concern."

al "(This could be good…)"

"The demon pointed at the outfit that the redheaded woman was wearing."

an "Shopping! Where do you think all these dresses come from?"

show alexia 2 necklace happy at midleft with dissolve

"Despite the disappointment of not learning anything useful as she expected, Alexia couldn’t help but giggle at the thought of the demoness shopping."

al "I just assumed she made them herself."

an "My sister? Sew? It’ll be a bright day in the Outer Dark before that ever happens."

"The demon let out a chuckle of his own."

an "The castle coffers would be a lot better off for it as well, trust me. Don’t tell her I told you though, she likes people to think she made them."

al "I won’t."

an "Anyway, I’m sure of all this talk of what my sister and I get up to when working is boring you."

al "Not at all. I’ve been cooped up here for so long now, it is nice to hear about what is going on in the outside world."

an "I apologize, this has all been unfair for you, and I didn’t mean to be insensitive."

show alexia 2 necklace neutral at midleft with dissolve

al "It is fine. Having free reign in the castle is one thing, but it is hard not to forget that I am still your prisoner. How long for, I have no idea."
al "Perhaps even forever."

an "It won’t come to that, I’m certain. Once your husband does what he agreed to do, you will be free to stay or go as you please."

al "I guess…"

an "Here’s an idea, how about I take you out somewhere? My sister couldn’t object, such a beautiful thing shouldn’t be kept in a gilded cage. Would you like that?"

menu:
    "I’d like that very much.":
        $ released_fix_rollback()
        show alexia 2 necklace happy at midleft with dissolve
        al "I’d like that very much. I’d feel a lot better after some fresh air I think."
        an "Then it shall be arranged. But I forget myself, there was a reason you wanted to see my today?"
        #record that Alexia has agreed to go outside the castle with Andras
        # TODO:

    "It’s fine, really.":
        $ released_fix_rollback()
        show alexia 2 necklace happy at midleft with dissolve
        al "It is fine, really. Truth be told, I’ve gotten used to it."
        an "If you change your mind, let me know. It would be no imposition. But I forget myself, there was a reason you wanted to see my today?"

al "Oh, yes!"

"Alexia rummaged around under the bed for a few moments, and then pulled out the demonic tome from underneath."

al "It is about this book..."

an "Oh, still have that do you?"

show alexia 2 necklace neutral at midleft with dissolve

al "Yes, but to be honest, I haven’t really been able to make much sense of it."

an "I’m not surprised, it is written in a regional dialect of a very old language so obscure few would ever bother to translate."

al "I looked in the library for anything that’d help, but had no luck finding any other books that might be useful."
al "I was hoping maybe you would be willing to help?"

an "Oh, you were? And what, pray tell, would be in it for me?"

al "What do you mean?"

an "Well, I already helped you once didn’t I? You were never have found the book, had I not been in the library."

al "True…"

"The demon pawed at the dormant beast hidden beneath his kilt."

an "You’re such a beautiful woman Alexia, I can’t help the effect you have on me. If you help take care of my needs, I’ll translate whatever you want in the book."

menu:
    "Agree to his demand to get the information.":
        $ released_fix_rollback()
        jump NTRScene3

    "Scold him and storm out.":
        $ released_fix_rollback()
        show alexia 2 necklace angry at midleft with dissolve
        al "I should have know you’d try something like this. Despite all your niceties, your true self is always lurking underneath."
        al "Here!"
        "The woman threw the book at him, it bounced off his muscular frame with a dull thump."
        al "You can keep your book and whatever the hells it has to say inside of it, I am a married woman!"
        hide alexia with moveoutleft
        "Before he had a chance to respond,  the woman stormed out of the room, slamming the door behind her."
        return

#########################

label NTRScene3:

show alexia 2 necklace angry at midleft with dissolve

al "Okay then, let’s get this over with, but I won’t let you touch me."

an "That’s fine, sweet Alexia, I just need you to touch me."

"He sat down on the bed and gave his kilt a downward tug, causing his now semi-erect cock to pop free from below the waistband."

an "Come over here, it won’t bite."

#cg1 - jerking
scene cg85 with fade
show andras happy behind cg85
show alexia 2 necklace angry behind cg85
pause 3

"Without saying a word, Alexia sat down next to him and tentatively placed her hand on the demon’s dick."

an "You’ll have to get a firmer grip on it than that, don’t you do this with your husband?"

al "Rowan isn’t a pervert like you, demon."

"As annoyed as she was at Andras, she just wanted it to be over, so she gripped it tighter as he demanded."

an "That’s more like it, now start to move it up and down."

"The woman did as she was told, starting slowly, before settling into a steady rhythm. Clearly enjoying himself, the demon lay back as she worked."

an "You have another hand, you know."

al "Meaning?"

an "A good woman never neglects the balls."

"Alexia reluctantly cupped his red balls as she worked the shaft with her other hand."

an "Ahhhh… That’s more like it…"

"For a few minutes the demon lay back, enjoyed the sensation as Alexia jerked his big dick while fondling his balls. Then, a wicked smile crossed his face."

show andras smirk behind black

an "Oh Alexia..."

al "What?"

an "As lovely as this is, it is going to take a bit more than this to get me off."

al "I told you, I won’t let you touch me."

an "Who said anything about me touching you, but maybe if you used your soft breasts..."

al "My breasts?"

an "You want to know what is in the book, right?"

al "Fine!"

#cg2 - titjob
scene cg86 with fade
show andras happy behind cg86
show alexia 2 necklace angry behind cg86
pause 3

"Alexia pulled the straps of her dress down, freeing her breasts for below. Kneeling at the foot of the bed before Andras, she positioned her chest so she could place his cock between her tits."
"Pushing them together, she began to move up and down."

an "That’s it, but it needs a little more lubrication. Spit on it."

al "Eww, that’s disgusting."

an "You can always leave, but then you’ll find out nothing..."

al "..."

#cg2 - titjob (spit variant)
scene cg87 with fade
show andras happy behind cg87
show alexia 2 necklace angry behind cg87
pause 3

"Not wanting the shameful situation to be for naught, she did as the demon asked, spitting on his cock as it sat between her perky breasts. A line of drool dribbled from her lips down onto the fat head of the cock below."

an "Perfect, now put some effort into it and make me cum!"

"Wanting it all to be over, Alexia started to move her chest up and down quite vigourously."
"Now well lubed, the cock slid back and forth between her tits with ease, especially when the demon started to move with her, pistoning his hips back and forth. It wasn’t long before he was close to climax."

an "Ohhh... Fuck..."

#cg2 - titjob (cum variant)
scene cg87 with sshake
scene cg87 with sshake
scene cg88 with flash
show andras happy behind cg88
show alexia 2 necklace angry behind cg88
pause 3

"With one final thrust upwards of his hips, Andras exploded, sending goosy spurts of cum upwards."
"A look of surprise was on Alexia’s face as jizz splattered it, some even landing inside her half open mouth. A moment passed before the expression shifted to rage."

scene bg7 with fade
show alexia 2 necklace angry at midleft with dissolve
show andras smirk at midright with dissolve

al "You got it all over me, you idiot!"

an "What can I say? You were doing such a good job, I couldn’t contain myself."

al "Ughhh... I need to go clean this off before Rowan gets back. You better keep your word, demon!"

an "Never fear sweet Alexia, I’ll send some notes to your room later which will tell you everything you need to know."

al "You better."

hide alexia with moveoutleft

#Alexia gains some corruption
$ alexiaUnfaithful = True
$ alexiaAndrasSex =+ 1
$ change_corruption_actor('alexia', 2)
#Andras’ influence over Alexia increases
$ change_actor_num_flag('alexia', 'andras_influence', 3)
# TODO:
#gain 1 demonic knowledge
return

###################################

label jezeraHelp:

scene bg18 with fade
show jezera neutral at midleft with dissolve
play sound "music/SFX/door knock.ogg"
pause 1

je "Please enter Alexia, the door is now unlocked."

show alexia 2 necklace neutral at midright with moveinright

"The red haired woman entered into a very lavishly decorated room filled with soft cushions and elaborate tapestries."
"It was a lady's room, albeit one that enjoyed sexual imagery. Its owner sat in one of two armchairs nearby a small tea table in one of the corners."

al "Hello Jezera. I came to ask you about this book…"

show jezera happy at midleft

"She held it out before her, so the demoness could see it. Jezera flashed her a grin."

je "I was wondering when you would come to see me about that."

al "You weren't expecting anyone else than?"

je "No, just us, but I'm sure that Rowan told you that when I concentrate I can tell where you and he are thanks to those amulets."

"Alexia took the other seat at the table somewhat nervously. She watched her host dipping tea leaves into a silver teapot decorated somewhat explicitly with fornicating demons for several moments."

al "So, is it your magic that's on these then?"

"She fingered the blue stone dangling from her neck."

je "The magic, cutting, and metalworking. I actually apprenticed as a jeweler for a short time, since I always had a fondness for such trinkets as a child. Those skills have lent themselves well to my enchanting."

"The demoness ended her dipping and expertly poured out two cups of tea."

je "Warping dimensions and imbuing artifacts with new properties are my natural talents. Well, that and the shapeshifting I demonstrated to you before, though my brother has some talent in that as well."

"She picked up one of the cups along with its saucer and passed it to Alexia."

je "Between the two of us, teleporting and enchanting are my skills alone."

"Then Jezera brought the cup to her lips and took a deep sip. Trying not to be rude, Alexia also took a sip from the cup as well."
"A shiver ran down her body as the liquid touched her tongue; not because it was cold, the tea was quite a pleasant warmth, but because of the things it seemed to make her feel."
"Alexia tried to push those feelings away for now, and instead concentrated on being a good conversation partner."

al "I can't really say that I've got any special talents like that myself. I never imagined myself as being anything but Rowan's wife when growing up."
al "I honed my skills at homemaking during the war and thought of the times I'd spent with Rowan in happier days."

show jezera displeased at midleft with dissolve

"Jezera placed her cup back on the saucer and tapped a finger on the brim with a slight look of annoyance in her eyes."

je "Surely you had some ambition beyond being a simple peasant wife?"

"The demoness's mismatched eyes locked with Alexia's, seeming to search deep within her."

# Blurry CG of Alexia dancing?  Variation for her being in Jezera's bedroom with Jezera watching?

scene black with fade
show alexia 2 necklace neutral behind black
show jezera displeased behind black

"A faint memory stirred, then grew and grew. Alexia was spinning while people clapped and cheered around her. A teenage Rowan watched her with a look of amazement in his eyes."

al "Actually, I do remember dancing during a spring festival just before the start of the war. It felt so natural, but no one stopped talking about how amazing it was until Karnas appeared."

"The red haired woman felt herself blush and she looked down, breaking Jezera's gaze."

al "That night was the first time that Rowan and I... we...."

"Alexia trailed off, thoughts of the first night with Rowan now making her feel very aroused and making it difficult to concentrate when combined with the strange effect the tea was having on her."

scene bg18 with fade
show jezera happy at midleft with dissolve
show alexia 2 necklace aroused at midright with dissolve

je "Hmmhmm, I knew that you were destined for something greater."
je "A dancer whose movements, body, and face would have drawn spectators from all over the six realms. Please, show me."

"Without thinking about it, Alexia stood up and started spinning in the middle of the demonesses room. It was exhilarating to dance again."

if NTR == False:
    "No, this was wrong. She felt funny, and she’d promised Rowan she would leave if things started to go badly, even if it meant learning nothing about the book."
    "Her movements slowed, then stopped. She shook her head, clearing the fog that had stopped her from thinking."
    "Jezera nodded when Alexia looked at her with clear eyes, seemingly satisfied. She stood up and smiled to the human woman."
    je "Thank you for joining me today Alexia, I enjoyed our time together and hope that we will have another chance in the future."
    al "Yes, thank you for the tea. I should get back to Rowan now."
    return

else:


    menu:
        "Forget about the book and leave before it goes any further.":
            $ released_fix_rollback()
            "No, this was wrong. She felt funny, and she’d promised Rowan she would leave if things started to go badly, even if it meant learning nothing about the book."
            "Her movements slowed, then stopped. She shook her head, clearing the fog that had stopped her from thinking."
            "Jezera nodded when Alexia looked at her with clear eyes, seemingly satisfied. She stood up and smiled to the human woman."
            je "Thank you for joining me today Alexia, I enjoyed our time together and hope that we will have another chance in the future."
            al "Yes, thank you for the tea. I should get back to Rowan now."
            return


        "Stay in the hope of learning about the book.":
            $ released_fix_rollback()
            "Thoughts of Rowan seemed to melt away, replaced with images of crowds of people watching her. Then of the upper echelons of nobility. Finally, an image of dancing before a great queen filled Alexia's mind."
            "Without really knowing what had happened, Alexia discovered that she was naked and sitting on a delicate leg while a pair of warm breasts pushed into her back."
            "Soft lips kissed her neck while two fingers pushed the folds of her womanhood apart."
            scene cg106 with fade
            show jezera happy behind cg106
            show alexia 2 necklace aroused behind cg106
            pause 3
            al "Oh my."
            "Those fingers pushed into her, penetrating her gently and teasing her passage and clit without seeming to violate her."
            "Alexia was being toyed and played with, not fucked. It was so surreal to have sex like this, completely unlike being with a man."
            "She moaned and seemed to settle deeply into Jezera's grip. The demoness giggled, then squeezed her plaything possessively for a moment before resuming her teasing again."
            "A hand ran up and down Alexia's skin while another curled inside her passage. A soft pinch occurred on her clit, then slow circles were being drawn around her again."
            "Words were whispered in her ear, promising sweet release and joy."
            al "Ahh...."
            "Alexia looked forward and saw a hand presented to her, covered in fluids. Her fluids."
            je "You're so fun to play with, lovely Alexia. Please come with me, let's relax on my bed."
            "Still in a daze, Alexia allowed herself to be led across the room and layed down on the bed. To her slight surprise, Jezera opted to lay down on top of her with her pussy lips on top of her face in a sixty nine position."
            scene cg50 with fade
            pause 2
            "The flame haired woman felt a tongue pressed into her passage and then found herself willingly opening her mouth to accept the womanhood above her face as it pushed down onto her."
            "She drank deeply of the fluids that dripped down her throat while also trying to tease more forth. Her efforts were nothing compared to that of the blue skinned demonesses' work."
            "That expert tongue both filled her and didn't, making her lower half feel warm and soft."
            "Once more, she didn't feel violated, only satisfied. Jezera seemed to be able to perform in a way that men couldn't. Alexia wanted to just surrender herself and feel more joy."
            "In turn, she wanted to give everything she could to try and make her partner feel half the pleasure she did."
            "..."
            scene bg18 with fade
            show jezera naked happy at midleft with dissolve
            show alexia necklace naked aroused at midright with dissolve
            je "Thank you for joining me today Alexia. I enjoyed our time together and feel like I gained a great deal from the experience."
            je "I hope you found it just as fulfilling."
            al "Ah, ha. I... I should get back to Rowan. Thank you for the... tea."
            je "You are welcome, my sweet girl. I’ll send some notes to your room later that will help with the book, for when you can think straight again."
            # TODO:
            #gain 1 demonic knowledge (new variable)
            #gain jezera favour (to do)
            $ alexiaUnfaithful = True
            $ alexiaJezeraSex =+ 1
            $ alexia_has_sex_with_jezera_during_demon_book = True
            $ change_relation('jezera', 3)
            return
