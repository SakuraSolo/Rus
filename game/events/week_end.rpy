# unsorted events for end of week
# story events, goals-related events
init python:

    event('turn1_end', triggers='week_end', conditions=('week==1',), run_count=1, priority=pr_story)
    #end of week 2 if village has not been captured
    event('turn2_end', triggers='week_end', conditions=('week==2',), run_count=1, depends=('not first_village_captured',), priority=pr_story)
    #end of week 3 if village has not been captured
    event('turn3_end', triggers='week_end', conditions=('week==3',), run_count=1, depends=('not first_village_captured',), priority=pr_story)
    #end of week 3 if village has been captured
    event('turn3_end_village_captured', triggers='week_end', conditions=('week==3',), run_count=1, depends=('first_village_captured',), priority=pr_story)

label turn1_end:
#end of turn 1 scene

scene white
show bg10 with fade

show jezera happy at midright with dissolve
show orc soldier neutral at edgeright with dissolve
show rowan necklace neutral at midleft with moveinleft

je "Very good. I'll take your map and reports and you can get a night's rest in your bed again. I'll be sending you out again in the morning so you can continue your work."

hide rowan necklace neutral with moveoutright
hide orc soldier neutral with moveoutright

scene black with fade

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg7 with fade

show alexia necklace concerned at midleft with dissolve

al "(Am I really going to go through with this?)"

"She took a deep breath and unconsciously fingered the blue gemstone hanging from her neck."
"Over the last week she'd spoken with Andras often and knew that his search had been fruitless thus far. Each conversation had been tinged with both dread and anticipation at the possibility of learning of Rowan's fate."
"But, also because she wanted to hear Andras's voice again. His daily visits and the kindnesses he'd shown her had touched Alexia and she genuinely felt that he had no desire to hurt her."
"Maybe, she could convince him that if he did find Rowan, that he need not end Rowan's life and that Jezera need not know Rowan had ever been found. Alexia knew that she'd need to offer a great deal for that risk...."
al "(It's for Rowan, and, being with Andras doesn't sound that bad.)"

scene black with fade

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg9 with fade

show rowan intro necklace happy at midleft with dissolve

"Rowan tested his body, lifting himself up with his arms by the bed frame.  He smiled in satisfaction; now his strength was back."
"Then he considered his options. The medallion would track his movements, but there was always the chance that Jezera simply wouldn't be paying him any attention right now. This gave him his first chance to try and find Alexia."
"Obviously he wouldn't be able to go out the door, but the windows offered an alternative. All he'd need to do is scale them to a different room and then carefully prowl the halls."
"Based on what he'd heard, Alexia was most likely being held in another of the guest rooms."
"Of course, if he was caught there was no telling what might happen to him."

if NTR == True:

    menu:
        "Sneak out and look for Alexia.":
            $ renpy.fix_rollback()
            $ AlexiaMeet = True
            ro "This risk is one I have to take."
            jump alexia_reunion


        "Don't take the chance.":
            $ renpy.fix_rollback()
            $ AlexiaMeet = False
            ro "I need to bide my time, things can always get worse for us."
            jump alexia_NTR1

else:
    "Rowan chuckled to himself."
    ro "There's no choice to be made here.  The risk is always worth it for Alexia."
    $ AlexiaMeet = True
    jump alexia_reunion

##########################################

label alexia_reunion:

$ alexiaOffer = False

scene black with fade

"Rowan slipped out of his window after quickly picking its ornate, but simple, lock."
"He carefully picked each handhold on the outside wall, never finding a false hold or slipping. Muscle memories developed from seven years prior had made climbing castle walls almost natural. Though the lack of any safety harness or net was always on the man's mind."
"Finally he reached the next room's window. This time he went for a more direct approach to get past the lock, stabbing a knife through it."

scene bg13 with fade

"Now inside the unused room, he hung low to the ground listening for any sounds of alert or danger. Hearing nothing, Rowan steps softly to the door and finds it unlocked."
"After opening the door a crack, the orc guard posted at his room was revealed to be dozing on the job. He was just leaning against the door with his helmet down over his eyes."
"Silent as a cat, the hero took his chance and darted down the hallway."

scene black with fade

"Now out in the halls, it was a simple matter for Rowan to locate the only other room under guard. It seemed that the twins were quite short staffed, as he didn't run into anyone else in the castle."
"Once again, he entered one of the neighboring rooms and slipped out the window to enter undetected."

show bg7 with fade

show alexia necklace concerned at midleft with dissolve

play sound "music/SFX/ImpactGlass.ogg"
pause 0.3
play sound "music/SFX/ImpactGlass.ogg"
pause 0.3
play sound "music/SFX/ImpactGlass.ogg"

show alexia necklace shocked at midleft with dissolve

al "*Gasp!*  Rowan...!"

"While trying to keep her voice down and heart from racing out of her chest, Alexia rushed over to the window to see her love looking at her from outside. He waved at her to stand back, then stabbed a knife through the lock on the window, snapping the flimsy metal almost immediately."

show cg19 with dissolve
pause 3

"With the path no longer barred, the woman almost tore the window open and helped her husband enter into her room. Immediately the two embraced warmly, holding each other as if they feared that the other would vanish if they let go for even an instant."
"Of course, the reality of their situation soon set in and they were forced to part."

scene bg7 with fade

show alexia necklace happy at midleft with dissolve
show rowan intro necklace happy at midright with dissolve

al "I can't believe you actually did this! Coming in through the window to rescue the princess from the tower!"

show rowan intro necklace neutral at midright with dissolve

"At this point, Rowan noticed the medallion hanging around his love's neck and his face fell. Seeing her love suddenly turn melancholy, Alexia was taken aback."

show alexia necklace concerned at midleft with dissolve

al "What is it?  Rowan, don't you have a way for us to escape? You can't have just climbed all the way up here as soon as you arrived without a plan, I know you too well for that."

ro "I arrived several months ago, this was the first chance I had to find you."

al "What kept you?"

ro "I was captured.  The demons, Jezera and Andras, threw me in their prison after I refused to help them take over the six realms."

show alexia necklace shocked at midleft with dissolve

al "Andras, he, he lied to me.  He said you never arrived, that he had gone out to find out what had happened to you."

show alexia necklace hopeful at midleft with dissolve

al "But since you're here now, that means you managed to escape, right?"

"Rowan drew Alexia's gaze to the necklace with the blue gemstone he was wearing, a twin to her own. Her face turned to the purest of snow."

show alexia necklace shocked at midleft with dissolve

al "No..."

ro " I didn't escape, I agreed to serve them."

if serveChoice == 3:
    ro "It was the only way, I needed to see you again."

elif serveChoice == 1:
    ro "Don't worry, I don't plan on actually giving them control of the six realms. For now, I have to make them believe I'll serve them."

elif serveChoice == 2:
    ro "I had to, there was no way out of there and I'd only rot away as a madman in the dungeon."

elif serveChoice == 4:
    ro "Alexia, I'm not sure the baron is much better than they would be. What difference does one master make over another?"

show rowan intro necklace angry at midright with dissolve

ro "Obviously they intend to keep a short leash on me in more ways than one. These necklaces can be used to track us and teleport us back to the castle if need be. You also can't take them off, I've tried."

show alexia necklace eyes closed at midleft with dissolve

"Alexia put her hand to her chest, trying to take in everything that had happened. How did she feel? Sadness? Despair?"
"Yes, but also frustration and a burning fury at the cocky bastard that had led her on all these months."

al "So now I'm just kept around as another chain to keep you loyal."

show alexia necklace concerned at midleft with dissolve

show rowan intro necklace neutral at midright with dissolve

al "Darling, you should have never come for me... but what's done is done. We shall have to make do as best we can. We still have one another."

if jezeraIntroSex == True:
    menu:
        "Tell Alexia you were forced to have sex with Jezera.":
            $ renpy.fix_rollback()
            ro "I agreed to bed Jezera. I don't want to tell you exactly what we did, but I have been with another woman now."
            $ admitIntroSex = True
            jump introSexYes

        "Don't mention what happened in the throne room.":
            $ renpy.fix_rollback()
            jump introSexNo

elif andrasIntroSex == True:
    menu:
        "Tell Alexia you were forced to have sex with Andras.":
            $ renpy.fix_rollback()
            ro "I offered myself to Andras. I don't think I should tell you exactly what happened, but I have been with a man now."
            $ admitIntroSex = True
            jump introSexYes

        "Don't mention what happened in the throne room.":
            $ renpy.fix_rollback()
            jump introSexNo

else:
    jump introSexNo

##########################################

label introSexYes:

ro "I'm sorry I wasn't able to be faithful to you."

al "It's okay Rowan, I don't blame you. I... I was about to offer myself to Andras so that he wouldn't hurt you if he found you."

show alexia necklace angry at midleft with dissolve

al "Those bastards are the ones who deserve the blame for forcing this on us!"

show rowan intro necklace happy at midright with dissolve

ro "Bastards they are, Jezera told me as much. Karnas's brood. Like it or not, we're stuck with them now. They'll probably throw me back in prison or worse if I don't do their bidding."

if NTR == True:

    show alexia necklace eyes closed at midleft with dissolve
    al "Then, maybe I should offer myself to him anyway? Andras will probably force himself on me at some point, and perhaps I can make things easier on us by being compliant?"

    menu:
        "Agree to let Alexia offer herself to Andras.":
            $ renpy.fix_rollback()
            ro "If you think that's best.  The time in the throne room probably wasn't the last time I'll be called on to service them.  I guess we just have to do what we can."
            $ alexiaOffer = True
            jump introSexNo

        "Dissuade her.":
            $ renpy.fix_rollback()
            ro "They want me to serve them, you are under no such obligation. Things should be fine as long as I just do what I'm told."
            show alexia necklace concerned at midleft with dissolve
            al "I hope you're right."
            $ alexiaOffer = False
            jump introSexNo

############################################

label introSexNo:

show alexia necklace neutral at midleft with dissolve
show rowan intro necklace neutral at midright with dissolve

al "Now, you should leave. Andras said he would come to visit me tonight and he'll be here soon."

ro "Alright. I probably won't be able to come and visit you again for awhile, they've been sending me on week long scouting missions."

show alexia necklace happy at midleft with dissolve

al "Don't worry, I understand. I was just happy to see you again."

show cg19 with dissolve
pause 3

"She jumped into Rowan's arms once more, then they shared a quick kiss before Rowan ducked back out into the night."

scene bg7 with fade

show alexia necklace neutral at midleft with dissolve

"Less than a minute after her husband's departure, Alexia heard the sound of footsteps approaching her room and a familiar confidant knock at the door."

play sound "music/SFX/door knock.ogg"
pause 1

al "Coming."

show andras happy at midright with moveinright

an "Alexia, how wonderful it is to see you again. I know we've always been able to talk if we wanted over the last week, but being together in person is much better."

al "Yes, it's nice to see you too."

"Her voice and stance felt stiff, but Alexia was determined to maintain her ruse."

show andras displeased at midright with dissolve

"The demon frowned for a moment, sensing something was off about the woman."

an "Is something wrong? I haven't seen you like this before."

if alexiaOffer == False:
    al "I'm just not feeling myself tonight. I just wanted to stay up to welcome you back to the castle."
    show andras happy at midright with dissolve
    an "Ah, not to worry my dear. I understand the whole situation can be quite stressful. Please, get all the rest you need and I'll come visit again soon."
    show alexia necklace happy at midleft with dissolve
    al "Thank you."
    hide andras happy at midright with moveoutright
    "..."
    show alexia necklace eyes closed at midleft with dissolve
    al "*Phew*"
    #end week
    return

else:
    al "Well, I think I've come to realize that Rowan must come here eventually. Either by your hand or on his own."
    al "I don't want him to suffer when that happens."
    an "That really depends on what he does."
    al "Yes, but, I want to do what I can. So... Andras, you want me, don't you? You've been so kind to me for so long, so you must desire my body."
    show andras displeased at midright with dissolve
    an "Now this is very unusual for you. Oddly... bold."
    al "Perhaps I should be bolder.  What if I offered myself to you for assurance of me and Rowan's safety?"
    # an shock
    "The demon shakes his head in disbelief."
    an "This is not how I thought I'd win you over. You're surprisingly conniving."
    "Skip sex scene?"
    menu:
        "Yes.":
            $ renpy.fix_rollback()
            scene black with fade
            an " I accept."
            #end week
            return

        "No.":
            $ renpy.fix_rollback()
            jump AndrasAlexiaNTR1


###########################################

label alexia_NTR1:

scene bg7 with fade

show alexia necklace eyes closed at midleft with dissolve

play sound "music/SFX/door knock.ogg"
pause 1

al "Coming."

show andras happy at midright with moveinright
show alexia necklace neutral at midleft with dissolve

an "Alexia, how wonderful it is to see you again. I know we've always been able to talk if we wanted over the last week, but being together in person is much better."

al "Yes, it's nice to see you too."

"Her voice and stance felt stiff, but Alexia was determined to follow through with her plan."
"The demon frowned for a moment, sensing something was off about the woman."

show andras displeased at midright with dissolve

an "Is something wrong? I haven't seen you like this before."

al "Well, I want to ask a favor."

show andras happy at midright with dissolve

an "Ah, of course. Is there something you require? Perhaps assistance with a project?"

al "No, I would like you to promise me that if you find Rowan, you won't hurt him."

show andras displeased at midright with dissolve

an "You are asking quite a lot of me, Alexia. You must understand that if Rowan has begun to gather the armies of the six realms then he is our enemy."

al "Yes, and I wouldn't ask this of you without giving something else in return.  I know you'd be taking a huge risk and Jezera wouldn't be happy with you for it."

show alexia necklace eyes closed at midleft with dissolve

al "That's why I'm offering my body to you.  Give me your word and I will lie with you."

show andras happy at midright with dissolve

an "Bold girl. Trying to tempt a demon with flesh."

$ alexiaUnfaithful = True
$ andras_alexia_sex = True
$ alexiaAndrasSex =+ 1


"Would you like to skip the sex scene?"

menu:
    "Yes.":
        $ renpy.fix_rollback()
        scene black with fade
        an " I accept."
        #end week
        return

    "No.":
        $ renpy.fix_rollback()
        jump AndrasAlexiaNTR1

##################################################

label AndrasAlexiaNTR1:

scene cg20 with fade
show andras happy behind cg20
show alexia necklace neutral behind cg20
pause 3

"He stepped forward and placed his hand under her chin, forcing her to look up and meet his gaze."

"The woman found herself trapped in those inhuman eyes, swimming in the power that they seemed to radiate with and finding her body seem to resonate. Andras wanted her, that much was certain."
"Alexia wondered if maybe she wanted him too."

an "This is a side of you I've never seen before.  Reminds me of my sister a bit."

show cg21 with dissolve
pause 3

"He leaned down and planted his lips on her's, pushing his tongue into her mouth and fiercely kissing her."

show cg22 with dissolve
pause 3

"The red haired woman was taken aback, but melted into the great man's lips, unable to resist his desires."
"Finally the kiss was broken and Alexia found herself short of breath in the face of the demon's raw sexuality."

scene cg20 with dissolve
pause 3

show andras smirk at midright behind cg20

an "I like it."

if alexiaOffer == False:
    an "Alright, brave Alexia, I accept. I promise that if I encounter Rowan on my travels that he will come to no harm from my hand. This will be our secret from Jezera."

else:
    an "Alright, you win Alexia. I accept."

scene bg7 with fade
show andras smirk at midright with dissolve
show alexia necklace neutral at midleft with dissolve

an "Now, relax and let me... have my fun."

"He quickly slid off his garments, then almost seemed to tear the white dress from Alexia's body."

show alexia necklace naked shocked at midleft with dissolve

al "Wha?"

an "Excuse me if I'm going a bit fast. I tend to be rough with my... partners."

label sexscene4:
$ andras_name = "Andras"

scene cg23 with fade
pause 3
show andras smirk behind cg23
show alexia necklace naked behind cg23

"Almost instantly Alexia found herself being lifted up by the powerful demon and her legs roughly pulled around his sides. Her face was pressed against his red chest, his long hair ending at her eye level."
"Desperately she looked down, trying to find the no doubt massive member of the demon. What she saw was indeed massive, veiny, and very, very, hard."
"Andras shifted his grip to line up his cock with Alexia's entrance.  As his head pushed against her womanhood, Alexia gasped as even that stretched her out more than Rowan ever had."

an "Ha ha, already so wet for me. I think you want me a bit more than you let on, don't you?"

"He relaxed his grip, allowing Alexia's own weight to bring her down further and further on his shaft. As she fell further and further, the woman involuntarily groaned in a mix of pain and pleasure."
"Half way down, Andras suddenly lifted Alexia back off of his length..."

an "Now for the real treat."

"..and slammed her back down, this time with his cock sliding into her ass!"

al "Ugah!"

an "Thanks for the lube.  I bet your husband's never taken you like this before, has he?"

"He roughly jerked her body up and down on his shaft, laughing at her obvious discomfort. Then the demon forced his tongue into her mouth, and she was powerless to resist."

show cg24 with dissolve
pause 2

"He found himself becoming more and more into the pleasure of the act. Lifting and dropping more and more frantically without a care to Alexia's wellbeing."

"Pain exploded across the red haired woman's back, as Andras's claws pierced her skin and sent trails of blood running down her form."

show cg25 with dissolve
pause 2

"Then a sudden rush of heat and jizz flowed into her bowels, signalled the demon's orgasm."

show cg25 with sshake
show cg25 with sshake
show cg26 with flash
pause 2

an "Oh, the thought of doing this to a hero's wife is so amazing.  What do you think Alexia?  How does it feel to be with a real man?  A better man?"

"Alexia said nothing. However her thoughts were not of the pleasure, but of the pain. This was Andras's true self, what he'd been showing her before was all an act."
"It was exhilarating in a way to be with such an animalistic creature that so strongly desired her, but Alexia felt no love for the demon."

show cg27 with dissolve
pause 2

"The red demon then rather unceremoniously pulled the woman off of him, flipped her over, and threw her down on the corner of her bed."

an "Time to finish what I started earlier."

"He stepped up behind her and lifted up her hips to line up his cock with her womanhood again."

an "Ready to take my seed in both holes?"

"Alexia twisted her head to the side and only just managed to breathlessly cry out"
show alexia necklace naked aroused behind black

al "Don't cum inside there!"

"Andras rolled his eyes and sighed in annoyance."

an "Fine, but that's the only concession you're getting."

show cg28 with dissolve
pause 2

"Then he pulled back and drove his cock into her passage all the way to the hilt in one thrust. This forced the breath from Alexia's lungs once more as she was stretched beyond what she ever thought was possible for her to take."
"Again and again he roughly fucked her, pistoning his cock with no regard for her comfort or pleasure. Laughing and taunting her the whole way. Alexia could do nothing but take, take, and take."

an "Oh ho! Was that you cumming I just felt?"

"Alexia just closed her eyes, trying to ignore the growing pool of her fluids on the bed. However, she could not deny that she was enjoying the feeling of being violated by such a creature."

hide cg27
show cg27 with dissolve
show cg27 with sshake
show cg27 with sshake
show cg29 with flash
pause 2

"Shortly after that she felt Andras finally pull himself out of her for the last time and spray his second load over her rear and back."

an "There, my gift to a hero's wife. I wonder if next time you'll beg me to give you a child? What do you think of that?"
an "Having a little demon filling up that belly of yours, maybe they'll even become the ruler of the six realms after me and my sister?"

show black with fade

"Laughing, the red demon casually picked up his discarded clothing and confidently walked out the door of the room without even bothering to put his garments back on."
"Alexia just lay on the bed for several moments, acutely aware of the sensations on her body as the blood and demon spunk mixed and cooled."

al "Rowan...."

$ persistent.sex_scene4 = True
$ change_actor_num_flag('alexia', 'andras_influence', 5)
#end week
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label turn2_end:
#end of week 2 if village has not been captured

scene black with fade

"Shortly after returning to the castle following Rowan's second week in service to the twins...."

show andras displeased at midleft with dissolve
show rowan necklace neutral at midright with moveinright
show orc soldier neutral at edgeright with moveinright

an "Well, well, how have you been doing Rowan? Have you been enjoying the countryside?"

ro "I-"

show andras angry at midleft with dissolve

show black with sshake
pause 0.3

an "SO MUCH SO THAT YOU'VE BEEN IGNORING ORDERS?!"

#ro worried

ro "Wha-"

play sound "music/SFX/ImpactHumanSmack.ogg"
show black with sshake
pause 0.3

"The red demon swings his hand out and slaps Rowan across the face, stunning the man and almost knocking him to the floor."

an "You were ordered to scout out the village North of the portal and help me capture it. If you cannot carry out such simple tasks, then you are of no use to me and my sister."
an "Failing again will be dealt with, harshly. Is that clear?"

show andras displeased at midleft with dissolve

an "You have one more week to occupy that village."

"Finished, Andras turned and walked away down the corridors of the castle.  Rowan was left there for a moment, before being ushered back to his room to rest."

#end week
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label turn3_end:
#end of week 3 if village has not been captured

scene white with fade
show bg10 with fade

show rowan necklace neutral at midleft
show andras angry at midright
show jezera displeased at edgeright

an "So, was this your little rebellion or are you really that spineless?"

je "This is so, disappointing hero.  All that effort to get you as our agent and now you fail so simple a task?  I had such high hopes for you too."

ro "So what happens then, am I to just go back to my cell after all?"

an "No... it's too late for that option."

show bg10 with flash
show bg10 with sshake
pause 2

if andrasIntroSex == True:
    show rowan necklace shock at midleft with dissolve
    "A flash of energy shot into Rowan's body, forcing him to the ground from incredible pain. Once again he was helpless, just like he'd been back in the village."
    ro "Wha?"
    show andras happy at midright
    an "At least you and your wife will make fine toys for me."
    show black with fade
    "And so Rowan was forced into sexual servitude to Andras, along with his wife Alexia.  He never again left his master's bedchamber."
    "Game Over - Andras' slave"
    jump gameend


elif jezeraIntroSex == True:
    show rowan necklace shock at midleft with dissolve
    "Suddenly, Rowan's body wouldn't move. Strange blue tethers of energy flowed around his form, caressing his skin and binding him place at the same time."
    "He tried to speak, but found his mouth gagged the instant his lips parted."
    je "At least I know one thing you'll be good for.  Come my hero, it's time to become my personal servant."
    hide jezera with moveoutright
    hide rowan with moveoutright
    an "Don't worry yourself about Alexia... I'll take good care of her."
    show black with fade
    "And so Rowan became Jezera's personal servant. Forced by her magic to obediently follow her wishes and be the receptacle of her desires. He never again left his mistress's bedchamber."
    "Game Over - Jezera's slave."
    jump gameend

else:
    "In a flash, Andras darted forward and jabbed his hand into Rowan's chest.  His claws quickly passed through and sunk into the man's heart."
    show rowan necklace shock at midleft with dissolve
    ro "Gha..."
    show bg10 with sshake
    show bg10 with redflash
    show black with fade
    an "Goodbye hero.  At least your wife should prove useful as a toy."
    "Game Over - Killed by Andras"

    jump gameend
    #return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label turn3_end_village_captured:
#end of week 3 if village has been captured

scene white with fade
show bg10 with fade

show jezera happy at edgeleft with dissolve
show rowan necklace neutral at midleft with dissolve

je "Well done, my hero."
je "You've accomplished much for us in these last few weeks.  It is time for you to have a very well earned reward."
je "Bring her in, brother."

#CG of Andras presenting Alexia / variant

show andras happy at edgeright with dissolve

if AlexiaMeet == False:
    show alexia necklace look away at midright with dissolve
    "Rowan's heart skipped a beat as Alexia was escorted into the room by the red demon. It was the first time he'd seen her in months."
    ro "Alexia?"
    "For some reason, she wouldn't meet his gaze and just stared at the floor."

else:
    show alexia necklace neutral at midright with dissolve
    "As Alexia was escorted into the room by the red demon, Rowan tried his best to look shocked to see her."
    ro "Alexia?"
    "She gave him a small nod, but said nothing for now."

je "Here is your wife Rowan, the one you came so far to find. We haven't done anything to her that she hasn't asked for, nor has she wanted for anything while in our care."
je "From now on, the two of you will no longer be prevented from being together while your duties allow you to be in the castle."

ro "That amulet...."

an "Yes, I must insist that Alexia remains inside the castle at all times. As insurance of your continued obedience."

show jezera neutral at edgeleft with dissolve

je " Is that really necessary, brother? Has Rowan not given us sufficient assurance yet that we need to continue forcing his wife to be our house guest?"

show andras smirk at edgeright with dissolve

an "If he isn't up to the task of his expanded duties, I'll need her on hand so that he can be properly punished."

show jezera displeased at edgeleft with dissolve

je "Andras, you're getting ahead of yourself. We'll discuss this later."

show jezera happy at edgeleft with dissolve

je "For now Rowan, you and Alexia have free range of the castle.  Please, spend some time together, catch up, and let the staff know if you need anything."
je "In the morning I'll organize any change you'd like to the sleeping arrangements."
je "Have a good night you two."

an "Yes, enjoy one another."

scene black with fade
scene bg9 with fade

if AlexiaMeet == False:
    show rowan necklace neutral at midleft with dissolve
    show alexia necklace concerned at midright with dissolve
    "Only after being shepherded into Rowan's room did Alexia finally meet her husband's gaze. Her eyes were filled with tears and when he tried to touch her she shrank away."
    ro "Alexia, what is it?"
    show alexia necklace angry at midright with dissolve
    al "He lied to me! That bastard Andras told me every day that you never came!"
    ro "Easy there, it's okay."
    al "No it isn't!  Rowan, I, I slept with him! I broke my vow to you because I thought I was protecting you. Now, now I find out he's enslaved you after keeping you in his dungeon for months!"
    al "He gloated to me about it. Told me how proud he was to trick me into offering myself to him while he was making you scout for his army and help him conquer people!"
    al "I... I...."
    show alexia necklace sad at midright with dissolve
    "Alexia's hysterics broke down into sobbing, Rowan tried desperately to comprehend what had happened to her.  He couldn't find the words, instead tears of his own started to flow."
    show rowan necklace sad at midleft with dissolve
    "Eventually he gave up, and just wrapped his arms around his wife."
    show cg19 with fade
    pause 3
    "After all that had happened, this was probably the thing that the twins had done to him that hurt the most."
    "Both of them continued crying, but clutched at one another to desperately reassure themselves that they were together again. The moment went on and on, until finally both of them ran out of tears to spill."
    if andrasIntroSex == True:
        ro "Alexia, I was forced to lie with Andras too. He is a very cruel man. There was no love in him, only a desire to satisfy his own pleasure."
    elif jezeraIntroSex == True:
        ro "They both took us; I was forced to sleep with Jezera. They're only concerned with their own pleasure, they don't love like we do."
    else:
        ro "The twins tried to force me into sleeping with one of them, I refused. I wonder if this was for revenge. Andras probably tricked you because he thought otherwise you'd do the same."
    scene bg9 with fade
    show rowan necklace neutral at midleft with dissolve
    show alexia necklace neutral at midright with dissolve
    ro "Of course, I wasn't brought here to be a toy. Andras, Jezera, they want the six realms for themselves and plan to use me to get them. When I refused the first time, they threw me into the dungeons for months."
    #al shocked
    al "Then, after all that you changed your mind?  Why did you ever agree to this horrible task?"
    if serveChoice == 3:
        ro "It was the only way, I needed to see you again."
    elif serveChoice == 1:
        ro "Don't worry, I don't plan on actually giving them control of the six realms. For now, I have to make them believe I'll serve them."
    elif serveChoice == 2:
        ro "I had to, there was no way out of there and I'd only rot away as a madman in the dungeon."
    elif serveChoice == 4:
        ro "Alexia, I'm not sure the baron is much better than they would be. What difference does one master make over another?"
    show alexia necklace eyes closed at midright with dissolve
    "Alexia fingered her necklace, the twin to the one around Rowan's neck. Andras had told her a few hours earlier what it's true function was, the first of his many horrible admissions."
    al "So now I'm just kept around as another chain to keep you loyal."
    show alexia necklace neutral at midright with dissolve
    al "Darling, you should have never come for me... but what's done is done. We shall have to make do as best we can. We still have one another."
    show cg19 with fade
    "The two embraced once more, this time much more warmly. They both understood how awful their hardship was, but it was a trial they would face together."
    scene bg9 with fade

else:
    show rowan necklace happy at midleft with dissolve
    show alexia necklace happy at midright with dissolve
    ro "I'd say that went fairly well. I don't think they realized that we'd already met."
    al "Andras may have been suspicious, but I don't think he realized it. It was hard to pretend to be shocked when he started gloating about having imprisoned you for months."
    if alexiaOffer == True:
        show rowan necklace neutral at midleft with dissolve
        show alexia necklace neutral at midright with dissolve
        ro "What about after I left? Did you... go through with it? Did he hurt you?"
        al "Yes. That bastard was very cruel in his treatment, all he cared about was satisfying his own ego and making me feel wretched."
        show rowan necklace sad at midleft with dissolve
        ro "I'm so sorry, I never should have-"
        al "Hush darling. It was my choice and I suspect that it won't be the last hardship we'll have to suffer at Andras's hands. Let us put that to the side for now."
        show rowan necklace happy at midleft with dissolve
        show alexia necklace happy at midright with dissolve
        al "The important thing is that we're together again."
        "Alexia wrapped her arms around her dear husband, which he warmly returned."
        ro "You're right. There's no use worrying about what's done now."
    else:
        pass


show rowan necklace neutral at midleft with dissolve
show alexia necklace neutral at midright with dissolve

al "Now I think we've done enough talking for the night and you look exhausted. Let's go to bed. Not a night has gone by where I didn't wish to have you at my side."
ro "Alexia, are you wanting to-"

show alexia necklace happy at midright with dissolve

al "Hush."

show cg30 with fade
pause 3

"The red haired woman helped her husband out of his equipment and lead him to the bed. Once he was settled, she disrobed and lay on top of him, breathing deeply of his familiar scent and stroking his toned form."

menu:
    "Rowan found himself growing hard under her.":
        $ renpy.fix_rollback()
        jump reunionSexScene

    "Rowan found himself drifting off to sleep under her.":
        $ renpy.fix_rollback()
        "The long thought lost comfort of Alexia with him put Rowan at ease. He felt more comfortable and safer than he had in months, to the point that he quickly drifted off."
        show black with fade
        "His dreams were of a happier time, of his home in the village, of children laughing, and of Alexia smiling brilliantly."
        #end week
        return


label reunionSexScene:

label sexscene5:

scene cg31 with fade
show rowan necklace naked behind cg31
show alexia necklace naked behind cg31
pause 2

"The long thought lost comfort of Alexia with him put Rowan at ease. He felt like he was back home again, with his wife lying on him."
"Thoughts of their old life bubbled up, then thoughts of her soft form and the joy it brought him."

al "Oh? Did I wake something up in you darling?"

"She had, Rowan's member was quickly growing to full hardness under his wife. He looked down at her and found her smiling encouragingly at him. This jump started the process of sending blood downstairs even faster."

"He started to sit up, but Alexia put her hand on his chest and pushed him back down."

al "No Rowan, you've faced many difficult days since we parted, I've been trapped in comfort, unable to do much of anything in that same time.  Let me take care of you now."

"Obediently, her husband relaxed and allowed the red haired woman to take the lead this time."

scene cg33 with fade
show rowan necklace naked behind cg33
show alexia necklace naked behind cg33
pause 2

"She climbed up and straddled herself over Rowan's waist, extracting his stiff member and letting it run against her moistening passage. Once she felt she was sufficiently wet for him, Alexia guided the shaft into her womanhood."
"As she slowly dropped down, the man underneath her let out a satisfied groan of pleasure. Just as their hips met, Rowan started running his hands over his wife's smooth legs and hips, cupping and gently pinching her."
"The red haired woman giggled slightly from the attention as she started gyrating her hips on her husband."

al "Oh Rowan, you can never keep your hands to yourself can you?  Don't stop though, I forbid it."

ro "I don't think that I could if you wanted me to."

al "And I don't think we'll ever have a chance to find out."

#Alexia laying on Rowan CG

"Alexia leaned forward and laid back down on top of Rowan's chest, this time with their bodies still linked together. As she'd settled into place, Rowan moved one arm off of her rear to her back and held her tightly against his form."
"Then he sighed in satisfaction as her hips began moving again, this time rhythmically pumping his cock in and out of her soft interior."

if alexiaOffer == True:
    ro "I'm glad I can still please you.  I was worried after-"
    al "No!  Don't talk about that.  Please, I just want to be with you and not worry about anything else."
    "She stopped for a moment, then resumed the act. "
    al "You're right.  Just focus on me."

else:
    pass

"Their breathing was becoming more and more rapid, but both of them felt incredibly happy. Even after all this time, there was a joy and a bond that ran incredibly deep between the two of them."
"It was like that first night all those years ago."

show rowan necklace naked aroused behind cg33
ro "I love you Alexia."

show alexia necklace naked aroused behind cg33
al "Oh, Rowan, I love you too. Please, fill me with your seed."

show cg33 with sshake
show cg33 with sshake
show cg34 with flash
pause 2

"As he started twitching inside her and the first spurts of his orgasm began Alexia clenched herself down as tightly as she could. At the same time she gripped him tightly and pressed herself into him as hard as she could."
"Rowan was surprised by Alexia's aggressiveness, but it wasn't anything that was going to stop the waves of pleasure and he jerked his hips under her in time with each of his pumps."
"While he was finishing, the red haired woman was just starting to shudder in her own peak. She found herself relaxing most of her body as her insides exploded with pleasure. She shuddered a couple times and then fell limp against her husband."
"Rowan softly chuckled at his wife."

show rowan necklace naked behind cg34
ro "It sounds like you might have needed that more than I did! Guess you really missed me a lot."

show alexia necklace naked behind cg34
al "Oh you jerk!"

"She leaned back and playfully jabbed a finger into his chest."

al "You don't get to turn this around on me, you're the one who came first!"

"Then both of them burst out laughing and embraced warmly once more"

al "Can we just be like this all night? I want you to stay inside me."

ro "You'll get no complaints from me."

$ persistent.sex_scene5 = True
$ renpy.end_replay()

if alexiaOffer == True:
    "After being quiet for almost a minute, Alexia spoke up one more time."
    al "Rowan, when I slept with Andras, he never came inside my womanhood. You're still the only one who can give me a child."
    "Then she was silent once more."
    "Rowan never replied to her, but did strengthen his grip on Alexia ever so slightly."

else:
    pass

scene cg32 with fade
pause 3

"Some time later, Rowan drifted off into a deep sleep."
"His dreams were of a happier time, of his home in the village, of children laughing, and of Alexia smiling brilliantly."


show black with fade

#end week
return
