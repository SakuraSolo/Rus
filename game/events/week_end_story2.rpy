# unsorted events for end of week
# story events, goals-related events
init python:
    #### Fail your second mission (end of twenty-second week) ####
    # Always triggers week 22 immediately after exploration finishes if you haven't yet conquered Raeve keep or have fallen short of the required quota.
    # TODO check for real goal2
    # TODO check if Raeve Keep is conquered in the event's body
    event('goal2_fail', triggers='week_end', conditions=('week==22', 'not goal2_completed'), run_count=1, priority=pr_story)
    #### Succeed your second mission (end of twenty-second week) ####
    # Always triggers week 22 immediately after exploration finishes if you've conquered Raeve keep and have met the quotas.
    # TODO check for real goal2
    event('goal2_success', triggers='week_end', conditions=('week==22', 'goal2_completed'), run_count=1, priority=pr_story)
    event('goal_3_warning', triggers='week_end', conditions=('week==52', (('goblinRecruit == False' and 'orciad_state != 2') or 'rastFirstVisit == True')), run_count=1, priority=pr_story)

label goal2_fail:
#### Fail your second mission (end of twenty-second week) ####
# Always triggers week 22 immediately after exploration finishes if you haven't yet conquered Raeve keep or have fallen short of the required quota.

scene black with flash
show bg10 with fade
show rowan necklace neutral at midleft with dissolve
show jezera displeased at midright with dissolve
show andras angry at edgeright with dissolve

je "It would seem that you are not the man I thought you were, Rowan."

# TODO check if Raeve Keep is conquered in the event's body
#If Raeve keep has not been conquered.
if goal2_completed:
    an "What did you expect, sister? All of your schemes are falling apart, why would this one be any different?"
    #jez angry
    je "Oh, are you blameless? We wouldn't even have any kind of army if you'd just kept going as you had!"
    ro "Listen you two, the tasks you set me were-"
else:
    #If Raeve keep was conquered.
    je "While you did deliver Raeve keep to us, as requested, you failed to properly manage our finances and expansion to meet the required quota. This will cause an unacceptable delay to my plans."
    show andras happy at edgeright with dissolve
    an "What plans? The only scheme of yours that's succeeded was taking over Yael fork! You've failed your side of things worse than Rowan has."
    #jez angry
    je "Don't you start with me, brother. Remember that we are in this together, isn't that what we agreed?"
    ro "Listen, it wasn't reasonable to assume that after the assault we'd still have-"
    show andras angry at edgeright with dissolve

#re-merge
an "Silence!"

show bg10 with flash

"A bright flash of energy surrounded Rowan and a huge wave of pain shot through him."

show rowan necklace shock at midleft with dissolve

ro "Gah!"

an "Effective immediately, you have forfeited your post at Bloodmeen. We shall have to decide what must be done after this setback, but you shall play no further part."

je "I suppose that maybe we should give you as a gift to your replacement? Perhaps as a prize for actually doing what we need of them?"

#if Alexia slept with Jezera, but not Andras.
if jezNTR1 and not andras_alexia_sex:
    je "I'll be taking your wife. Perhaps I'll be able to make her more useful than you were. At least her talents won't be squandered on being a damn housewife."
#else
else:
    an "I'll settle for Alexia, that tasty redhead will soon be my personal cockslut. I wouldn't say she was worth the year we wasted on this scheme, but at least I got something out of it."

show orc soldier neutral at edgeleft with moveinleft

"Several orc soldiers stepped forward when signaled by their demonic master."

an "Men, return this failure to his cell. We'll decide what to do with him later."

hide orc soldier with moveoutleft
hide rowan with moveoutleft

scene bg8 with fade

"Game Over - Eternal prisoner."
jump gameend

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label goal2_success:
#### Succeed your second mission (end of twenty-second week) ####
# Always triggers week 22 immediately after exploration finishes if you've conquered Raeve keep and have met the quotas.

scene black with flash
show bg10 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve
show andras displeased behind bg10

je "Well, it would seem that congratulations are in order. Yael's Fork is ours, and the quota has been met. Once again, you've accomplished what was asked of you."

an "It seems that he's the only one we can rely on."

hide andras
show andras displeased at edgeright with moveinright

an "Isn't that right, sister?"

show jezera displeased at midright with dissolve

je "Why are you bringing this up now, brother?"

an "Because our best advisor should know what's happened to us."

show jezera neutral at midright with dissolve

"The demoness let out a long sigh, then turned back to Rowan."

je "My hero, there have been setbacks in both the Tundra and Ealoaen. I'd hoped to secure alliances there to assist us in a joint assault on Prothea from the base in Rosaria you built for us, but my prospects have dried up."

show rowan necklace shock at midleft with dissolve

ro "You thought to take on the holy city with what little I've managed to build up over the last few months?!"

show jezera displeased at midright with dissolve

je "Not alone! The dark elves and ogres would have joined in as well, at least if they had listened to me...."

show andras angry at edgeright with dissolve
show rowan necklace neutral at midleft with dissolve

ro "Why would they help you? Solansia help me, even if they had joined you wouldn't have stood a chance against the holy armies with Deanara at their head!"

"Silence fell in the room. Rowan looked back and forth between his masters, then feared that he'd stepped beyond his bounds and was about to be punished."

show andras happy at edgeright with dissolve

"Then Andras smiled."

an "Well Jezera, it seems that your plan was doomed from the beginning."

#jez angry
je "Shut up, it wasn't your plan to recruit the hero of Karst!"

an "True, Rowan has proven to be our greatest asset. However, now we will be doing things my way."
an "Rather than tearing out the heart of the six realms with a single stroke, we will build ourselves an army that will bring them down one by one until only Prothea remains."
an "Would you say that's a more practical plan, Rowan?"

show rowan necklace shock at midleft with dissolve

ro "It will take years to build up an army strong enough to take on the six realms directly!"

an "But you admit it could be done."

"Rowan hesitated, biting his under lip in apprehension."

an "You see sister? Our most capable servant agrees with me."

show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve

"Jezera looked to the hero for a moment, her eyes piercing Rowan's as if he might hold all the answers she needed."

an "It would seem that you and I have many plans we will need to revise. Servant, we will discuss this and brief you later."

hide andras with moveoutright
hide jezera with moveoutright

"The red demon gave a meaningful wave to his sister, who glared at him for a moment before following him out of the portal chamber, leaving Rowan behind."
"He fingered his amulet and groaned in frustration."

ro "(Those two... damn it.)"

# go to third mission
# TODO maybe some preparation for goal3
#~ return
jump goal3_start


################################################################################


label goal3_start:
#### Third mission ####
# Cla-Min and Skordred argue about titles
# goal3 is given in "new society" event

scene bg14 with fade
show clamin neutral at center with dissolve
show skordred neutral at cliohnaright with dissolve

cla "Hey Skordrey, do you think that we'll be getting titles soon for our services? I'm looking forwards to telling my kids they're all nobles."

sk "Silly girl, tha lords of Bloodmeen have always followed tha path set out by our lord Kharos; tha law of might."
sk "We do nah have hereditary titles like tha six realms, everyone must prove that they deserve their position and lose it if another shows thar better."

show clamin angry at center with dissolve
cla "That's bullshit! I deserve the peace of mind knowing that my work has secured a place for my children and their children in the new society we're building!"

show skordred angry at cliohnaright with dissolve
sk "An have this place ruled by those who happen to have been born to the right person because some time a generation ago thar ancestors put on some fancy party or was some lucky general?"
sk "No, that's lead boulders."

show alexia 2 necklace neutral at edgeleft with moveinleft
al "What are you two shouting about?"

cla "This greyskin is telling me that the twins aren't going to give out titles to anyone, even those who've earned them!"

sk "Phah, wha makes ya think ya even deserve a title? Ya should just be honored for a chance to serve the masters!"

al "Whoa, hey, calm down now. There's no need to shout, we're all adults here."

"Alexia put out her hands to hold the two small people from yelling at one another further."

al "(Ugh, I wish I hadn't said that....)"
al "Why don't you ask Andras and Jezera about this, rather than arguing about what they might say? I saw them in the throne room just a moment ago."

show clamin happy at center with dissolve

cla "An excellent suggestion, thank you Alexia. Are you coming Skordred?"

sk "I'm telling ya, yar wasten yar time...."

hide skordred with moveoutright
hide clamin with moveoutright
show alexia 2 necklace concerned at edgeleft with dissolve

al "Phew. (I'm glad it didn't come to blows.  I've never seen those two get mad at one another before.)"

if raeve_keep_rowan_claimed_helayna:
    show rowan necklace neutral at midright with moveinright
    
    ro "Hello Alexia."
    
    "His wife made no response. Thinking that maybe he should just leave, Rowan made to continue down the hall."

    show alexia 2 necklace neutral at edgeleft with dissolve

    al "Darling, wait."
    
    show rowan necklace shock at midright with dissolve
    
    al " I... I wanted to say that I'm sorry for how I acted before. With all that's happening here, it wasn't right of me to get so mad over Helayna."
    
    show rowan necklace neutral at midright with dissolve
    
    ro "Alexia... are you really sure about that?"
    
    al "You're under so much stress these days, always looking over your shoulders with two demons torturing your mind and body. Then you go and blame yourself when you have no way to protect someone but to break your vows to me."

    show alexia 2 necklace concerned at edgeleft with dissolve
    
    al "I know how you feel, darling. I said it myself, we have to do what we can, we have no choice if we want to survive this place. At least here, I can lift one weight off your shoulders."

    show alexia 2 necklace happy at edgeleft with dissolve

    al "So I just want to say, I forgive you for taking Helayna.  I may not like it and I don't think I could ever share a room with her, but I can look past it."
    
    show rowan necklace happy at midright with dissolve
    
    ro "I... thank you Alexia."
    
    "The two wrapped each other up in a warm embrace that pushed the pain away. While there was no doubt that Helayna would still strain their relationship, it alone would not break the bonds that Alexia and Rowan had for one another."
    
    show rowan necklace neutral at midright with dissolve
    
    ro "At least that's one of my worries gone.  Shame that I just learned about other problems in the castle that put a damper on our future."

else:

    show alexia 2 necklace neutral at edgeleft with dissolve
    show rowan necklace neutral at midright with moveinright

    al "Oh darling, it is good to see you again. How was the week?"

    ro "Fine... fine...."

show alexia 2 necklace concerned at edgeleft with dissolve

al "What happened while you were away?"

ro "It's not that, it's what happened after I got back that has me worried right now. I just saw the cracks in the twin's plans. Most of what Jezera apparently had in mind fell through, now it sounds like Andras is coming up with plans to conquer each of the realms one by one."
ro "And it sounds like I'm going to be at the heart of those plans."

show rowan necklace happy at midright with dissolve

ro "Something I'll need to worry about later, the bastards just had a bit of a row with one another and I doubt that they're in the mood for listening to anything else I have to say."

show alexia 2 necklace shocked at edgeleft with dissolve

al "Oh dear."

show rowan necklace neutral at midright with dissolve

ro "What?"

al "I just sent Cla-Min and Skordred to the twins about an argument they were having with one another."

ro "What were they arguing about?"

al "Whether or not the twins should give Cla-Min a title for her service, Skordred was going on about how the rulers of Bloodmeen don't do that sort of thing. I'm sorry, I didn't hear the whole thing."

ro "Well, this sounds like trouble. I'd better go see what's happening."

hide rowan with moveoutright

# go to new society: feudalism vs might
#~ return
jump new_society

################################################################################

label new_society:
#### New society: feudalism vs might ####

scene bg6 with fade
#skor angry
show skordred neutral at edgeright with dissolve
show clamin neutral at midright with dissolve
show jezera neutral at midleft with dissolve
show andras happy at edgeleft with dissolve
show rowan necklace neutral behind bg6

an "Skordred, Skordred, do you realize the irony of you professing the value of tradition for the ways of the God of Chaos?"
sk "I profess the ways that will lead to yar success!  Tha feudal ways of the six realms lead to thar near defeat in tha last war!"

ro "(I've seen enough nobility generals to know that's true enough. The competent ones often feel like lucky accidents.)"

cla "But just think about how much more loyal and hard working your people will be if they know they have a chance to become the new nobility! Why do you think the Six Realms all practise some form of feudalism?"

ro "(Because it's mandated by Solansia.  All know their place, all know peace, all know happiness.)"

show jezera happy at midleft with dissolve
je "Oh Rowan, I see you back there."

hide skordred with moveoutright
hide clamin with moveoutright
hide rowan
show rowan necklace neutral at midright with moveinright

je "Would you mind conferring with us in private? I would like your input on a problem that has arisen."

ro "... of course."

hide andras with moveoutleft
hide jezera with moveoutleft
hide rowan with moveoutleft

scene bg18 with fade
show andras displeased at edgeleft with dissolve
show jezera neutral at midleft with dissolve
show rowan necklace neutral at midright with dissolve

je "Well?"

an "I think we should make a decision on our policy going forward. As Rowan pointed out, it will be years before the Six Realms are ours and we cannot put this off indefinitely."

je "I wasn't really asking for your input just yet, brother."

ro "No, he's right. If you brush this off, it will only sow the seeds of doubt among your followers. I've dealt with this before, the worst thing you can do is absolutely nothing."

show andras happy at edgeleft with dissolve

an "You see? This isn't the time for half measures or vague promises. It is time to declare ourselves emperors!"

show rowan necklace shock at midright with dissolve
#jez shock
je "Andras?! Are you serious?"

an "Sister, sister, you said yourself that we owe nothing to the God of many masks. This is our new world, we can do as we wish in it."

je "What of those drawn to the darkness? For them, we represent a way to free themselves from the chains of this world. Do you want to throw that advantage away?"

ro "There are also your soldiers. Will they be so eager to follow a demon that adheres to feudalism?"

show andras displeased at edgeleft with dissolve
an "Ah, yes, the orcs. They're pretty much already following the way of might makes right. I hadn't considered that. Was Skordred correct in saying that they're stronger for it?"

## show jezera neutral at midleft with dissolve
show rowan necklace neutral at midright with dissolve

"Rowan hesitated, realizing the gravity of the situation and what effect his words would have in the coming months, years, possibly even centuries should the twins succeed in their bid for power."

ro "(Wait, I may very well decide what society the twins build in their new world. I need to choose my words very carefully.)"

menu:
    "Heriditary feudalism.":
        $ released_fix_rollback()
        jump .heriditaryFuedalism

    "Might makes right.":
        $ released_fix_rollback()
        jump .mightMakesRight

################################################################################

#### Supported hereditary feudalism ####
label .heriditaryFuedalism:

ro "He was right. The strength of Kharos's way would have crushed the armies of Rosaria had people like myself not stepped up to take over. I wasn't the only commoner to rise when the nobility faltered."
ro "They hated us, called us 'dirt generals', but we turned the tide."
ro "However, a realm ruled by might can hardly be called a realm. You want peace, you want prosperity, you want order? Then you must follow the laws laid down by Solansia."
ro "Might makes right may make the world yield, but you'll be ruling over a corpse while Kharos laughs in triumph."

"The two half demons watched Rowan in silence for a long moment, considering his words. Eventually Jezera spoke up."

je "I see. You're dismissed, Rowan."

"The man looked between the two of them for a moment longer, then nodded and left the room."

scene bg6 with fade

"Nearly an hour later, the twins had called up all their inner circle to the throne room to make an announcement."

#CG of Jezera and Andras standing at the throne.
show andras happy behind bg6
show jezera happy behind bg6

"The two of them stood in front of the throne and surveyed their motley crew of followers. Rowan was near the front of the small crowd with Alexia at his side, hands tightly gripped. While Alexia knew not why her husband was worried, she knew he needed her support right now."

an "Followers, favored servants, my sister and I have called you here tonight to make an announcement."

je "Yes, it has come to our attention that some of you have been hopefully of receiving recognition for your service to us. Indeed, this matter has caused some strife among the ranks."

an "Therefore we have assembled you all here to make our will known, so that there can be no further false beliefs. So you will know to punish those who descent with their masters."

je "We seek not only to make the world ours, as is our birthright, but also to remake it as we see fit... even if this goes against our father's way."

"Rowan looked up, hardly believing what he was hearing, they couldn't actually be about to do what it sounded like, could they?"

an "Know that today, marks the start of a new era, the beginning of the reigns of Emperor Andras..."

je "and Empress Jezera! Those who earn our favor will earn a place in our hierarchy, a place that will be passed on to their children, and their children's children."

#Crowd talking sound effect

"A burst of noise erupted from the assembled crowd.  Some were shocked, others dismayed, and some cheered."

show bg6 with flash
#crash sfx

"Before there was much time for any discussion, a loud crash erupted from the twins, silencing their subjects."

an "Rowan Blackwell, step forward."

"Rowan looked to Alexia for a moment and received a reassuring squeeze before releasing her hand and walked up to the dias. All eyes followed his every movement while his heart threatened to beat out of his chest."

an "Kneel."

#Show CG of Rowan kneeling and being knighted.

"He did so."

je "You have served us faithfully over the last several months. Above all our followers, you have accomplished the most, turning Bloodmeen into a player on the world stage once more. For that service, you shall be the first to receive our favor."

"The demoness drew a sword and stood in front of the kneeling man. She placed the tip of the blade on one of his shoulders, lifted it up over his head and touched the other shoulder."

je "I, Empress Jezera of Bloodmeen, dub you a knight and the champion of our new empire. In addition, I grant you the title of lord and all the associated duties and privileges. From this day forward, your family shall ever hold this."

an "Rise, Sir Rowan, rise as the champion of Bloodmeen!"

#Title name changes
$ jezera_name = 'Empress Jezera'
$ andras_name = 'Emperor Andras'
$ rowan_name = 'Sir Rowan'
$ alexia_name = 'Lady Alexia'
$ cliohna_name = 'Primate Cliohna'
$ cla_min_name = 'Lady Cla-Min'
$ skordred_name = 'Lord Skordred'

scene bg14 with fade

"Fifteen minutes after the twins made their proclamation and after several other titles had already been handed out...."

show skordred neutral at skorright with dissolve
show rowan necklace neutral at midleft with dissolve

sk "I canny believe this!  How can the masters turn on our ways like this?"

show jezera happy at edgeleft with moveinleft

je "Because we are the masters, Skordred. Do you doubt our wisdom?"

sk "Nah, ah course not, I meant that-"

je "Then you must accept our judgement on the new path that will be forged by Bloodmeen. If you cannot, you will be replaced."

sk "I, I understand."

je "Good."

hide skordred with moveoutright

"Now that the dwarf architect had left, Rowan wondered why Jezera had sought him out. However, she didn't address him, instead she looked passed him and waved to someone further down the hall."

je "Oh, lady Cla-Min? Could I have a word with you?"

"Rowan started to walk away, only for his mistress to wave at him to stay there."

show clamin happy at midright with moveinright

"A very happy goblin woman bounced up to the two of them."

cla "Yes, Jezera? Is there something I might do to help you?"

je "I see nobility suits you well. I actually thought I'd let you know on a little secret. You see, our friend here..."

"She indicated Rowan."

je "... was instrumental in convincing me to accept we needed a little change in policy going forward. If you want to thank someone for your newfound title, Rowan is your man."

hide jezera with moveoutleft

"Somehow, the short woman's grin got even bigger and she lept up into Rowan's arms to plant a big kiss on his mouth. The man looked around for any kind of help, but found that Jezera had already left."

scene bg9 with fade
show rowan necklace neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with dissolve

"After he'd finally managed to escape from the somewhat overwhelmingly affectionate goblin, Rowan retreated to his room, where he was joined by Alexia not long afterwards."
"The two sat in silence for several minutes, letting the events that had just transpired sink in."

al "Rowan, are you alright with this? I know what you said at the end of the war, has something changed?"

"Rowan didn't answer at first, but his thoughts did turn back to those months after Karnas had been defeated. He'd been born a peasant, a hunter in Arthdale and a citizen of Rosaria. However, he'd become a hero and had been instrumental in winning the war."
"This was a problem, as he represented a threat to the established order. Many people respected him far more than the nobility, many of the soldiers he'd lead would have done anything he'd asked of them."
"However, Rowan had gone back home. He'd chosen to get married and live out the life he would have lived if there'd never been a war. Deanara had told him he was a true follower of Solansia for doing that, but now he was a demon's noble."
"How did he feel about this dubious honor?"

menu:
    "Happy to finally be rewarded.":
        $ released_fix_rollback()
        ro "I never was entirely okay with just going back to Arthdale after the war ended. My only reward for everything I did was peace."
        ro "For years I've been called 'dirt general' and have been watched by nobles either afraid of me taking their power by force or hoping to use me in their own games. It didn't matter that I was a hero, only what I was born as."
        ro "I always secretly hoped that someday I might become a noble, but this wasn't how I wanted it to happen."
        show alexia 2 necklace happy at midleft with dissolve
        "Alexia let out a low chuckle and put her hand to Rowan's cheek."
        al "This isn't something you ever told me about. A part of you buried deep for the sake of others."
        "She held the gaze of her husband for a long moment."
        al "If you had become a noble, would you have come back for me?"
        "Instead of replying, the once simple man kissed her."
        #Gain a bit of corruption for this choice.
        $ change_base_stat('c', 4)

    "Mixed feelings.":
        $ released_fix_rollback()
        ro "I'm torn.  On one hand, I must admit that a part of me always wished that I'd been properly rewarded for my service to the Six Realms. On the other hand, I know that the peace and stability are thanks to the status quo being maintained."
        show alexia 2 necklace happy at midleft with dissolve
        "Alexia let out a low chuckle and put her hand to Rowan's cheek."
        al "That makes two of us. We aren't Gods, we all make mistakes."
        "The once simple man put his arms around the woman at his side and laid his head on her's."
        #no effect

    "Wish they'd never given me a title.":
        $ released_fix_rollback()
        ro "I wish that they'd never given me that title. I've never wanted anything but the life I was born to. They can't go back on that, not after publically making me their first noble."
        show alexia 2 necklace happy at midleft with dissolve
        "Alexia let out a low chuckle and put her hand to Rowan's cheek."
        al "Still the same man I fell in love with I see. Even though our life isn't what it use to be, your heart is still what it once was."
        "The once simple man looked down at the woman next to him and put a hand around her shoulder, pulling her tight against him and feeling her warmth."
        #Lose a bit of corruption for this choice.
        $ change_base_stat('c', -4)

# The twin's government style is set to feudalism.
$ society_type = 'feudalism'
#Rowan earns a point of favor with Solancia.  Rowan gains a significant relationship boost with Cla-Min.
$ change_relation('cla_min', 20)
$ change_favor('solancia', 1)
jump .thirdMission

################################################################################

#Supported might makes right
label .mightMakesRight:

ro "The nobility, by and large, was no match for Kharos's armies.  They'd only known peace and it was only ever a lucky accident when one of them was actually competent as a general."
ro "People like me, commoners forced to be great by strife, were the ones who turned the war around."
ro " Even though we were the best chance they had to win, the nobility still sought to destroy the competent common generals. They called us 'dirt generals' and spread lies about our intentions while also undermining our efforts."
ro "It was an incredibly foolish, they were so caught up in what might happen after the war was won that they nearly lost the war itself."
ro "We are weak, there's no question. If you want to win the six realms, you can't fall into the same trap that they did."

"The two half demons watched Rowan in silence for a long moment, considering his words. Eventually Jezera spoke up."

je "I see. You're dismissed, Rowan."

"The man looked between the two of them for a moment longer, then nodded and left the room."

scene bg6 with fade

"Nearly an hour later, the twins had called up all their inner circle to the throne room to make an announcement."

#CG of Jezera and Andras standing at the throne.
show andras happy behind bg6
show jezera happy behind bg6

"The two of them stood in front of the throne and surveyed their motley crew of followers. Rowan was near the front of the small crowd with Alexia at his side, hands tightly gripped. While Alexia knew not why her husband was worried, she knew he needed her support right now."

an "Followers, favored servants, my sister and I have called you here tonight to make an announcement."

je "Yes, it has come to our attention that some of you have been hopefully of receiving recognition for your service to us. Indeed, this matter has caused some strife among the ranks."

an "Therefore we have assembled you all here to make our will known, so that there can be no further false beliefs. So you will know to punish those who descent with their masters."

je "We are in the Castle Bloodmeen, traditional home of the champions of Kharos, including our father Karnas."

an "These lords have always followed one path of rule, Might Makes Right! We are no different, if you wish a place of power you must prove that you deserve it and take that power for yourself! Slaves are the only exception."

je "Everyone will have their fair chance, regardless of race, regardless of sex, regardless of birth. Remember this is not the Six Realms, you don't get special treatment just because your daddy was a good at telling people with sticks where to go."

an "This castle, no, this world, will be ours because we can make it ours. You all will hold the power that you can take. That is our birthright. Dismissed."

scene bg14 with fade

"Fifteen minutes after the twins made their proclamation...."

show rowan necklace neutral at midleft with dissolve

show clamin sad at midright with dissolve

cla "Well... crap. I guess I should have done my research. I was really hoping that I'd be able to make a good place for my family here."

show jezera happy at edgeleft with moveinleft

je "Fear not, you and yours have a place here and we can promise that your children will all have a chance in the society we're building. That's something you've never had before."

cla "True enough. I'll have to look into training and education instead."

"She bowed to both Rowan and Jezera."

cla "Good evening to you two."

hide clamin with moveoutright

je "A moment, my hero. This presents something of an opportunity to build bridges, would you come with me, please?"

scene bg6 with fade
show skordred neutral at skorright
show rowan necklace neutral at midleft with moveinleft
show jezera neutral at edgeleft with moveinleft

je "Ah Skordred, I'd like a word."

sk "Aye mistress?"

je "Our decision this evening was not as certain as you likely thought it to be. My brother was eager to proclaim himself emperor and I had already thought it was in our best interests to grant titles to our favorites."

#skor shock
"Skordred's eyes opened wide in shock."

sk "Wha?"

je "Yes, it was in fact Rowan here that convinced us of our error and to follow Kharos's path."

"The dwarf's eyes grew even larger."

je "That will be all."

#skor neutral
sk "It would seem that I was wrong about you. I... apologize for my behavior these last few weeks."

ro "What were you wrong about? I was directly involved in killing your former master."

show skordred happy at skorright

sk "Aye, but I know naw yar a true champion of chaos, deservan of my respect and loyalty. I will not farget what yav done."

"For the first time, the dwarf bowed in reverence to Rowan, leaving the man stunned at this sudden change in attitude."

scene bg9 with fade
show rowan necklace neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with dissolve

"After speaking with Skordred, Rowan retreated to his room. A few minutes later, he was joined by Alexia."
"The two sat in silence for several minutes, letting the events that had just transpired sink in."

al "Rowan, what's wrong? I can tell that this announcement bothers you, but I don't know why. It seems like this is what you should have expected the twins to do. What do you know that I don't?"

"Rowan didn't answer at first, his thoughts consumed with what might have been and what will be. He remembered what the lands that had been conquered by Kharnas's armies had been like, the brutality that he'd seen, and what exactly he'd unleashed."

ro "The twins probably weren't going to run a realm of might makes right. Then I convinced them otherwise. They were on the verge of declaring themselves emperors and making feudal subjects of their favorites."

show alexia 2 necklace concerned at midleft with dissolve
al "What? Why in Solensia's name would you not encourage that?"

menu:
    "I hoped they'd take another path.":
        $ released_fix_rollback()
        ro "I only wanted to make sure that they didn't practise feudalism. I'd hoped that they'd take a third path, rather than defaulting to Kharos's law, but what's done is done."
        ro "Alexia, I watched the Six Realms nearly burned to the ground because of privileged birth. I can't in good conscience support continuing those mistakes."
        show alexia 2 necklace happy at midleft with dissolve
        "Alexia let out a low chuckle and put her hand to Rowan's cheek."
        al "This isn't something you ever told me about. A part of you buried deep for the sake of others."
        "She held the gaze of her husband for a long moment."
        al "Thank you for being honest with me."
        #Lose a bit of corruption for this choice.
        $ change_base_stat('c', -4)

    "We won't win the war otherwise.":
        $ released_fix_rollback()
        ro "Our lives are tied to the fortunes of the twins. If they fail, we die. As horrifying as it is, I didn't think I could throw away the advantage offered by Kharos's law."
        "Alexia sighed sadly and put her hand to Rowan's cheek."
        al "We can only do what we can."
        "Rowan placed his hand on top of her's, drawing comfort from the warmth of her touch."
        #No effect

    "A part of me agrees with the philosophy of Might Makes Right.":
        $ released_fix_rollback()
        ro "As disturbing as it might be to admit, a part of me actually agrees with the philosophy of Kharos's law. Why shouldn't the people who're best for a job get that job? Why should one be privileged because of their birth?"
        "Alexia sighed sadly and put her hand to Rowan's cheek."
        al "It's for the sake of stability, so that the land can grow and won't be constantly torn by strife and war by those seeking to carve their own worlds."
        "The hero let out a his own long sigh and pressed his hand into her's, drawing some comfort from the warmth of her touch."
        ro "I know, but it was so frustrating knowing that I wouldn't have the chance to change things, either for myself or for my children."
        show alexia 2 necklace happy at midleft with dissolve
        "For an instant the woman's heart skipped a beat, but then she smiled."
        al "This isn't something you ever told me about. A part of you buried deep for the sake of others."
        "She held the gaze of her husband for a long moment."
        al "Thank you for being honest with me."
        #Gain a bit of corruption for this choice.
        $ change_base_stat('c', 4)

# The twin's government style is set to might makes right.
$ society_type = 'might'
# Rowan earns a point of favor with Kharos. Rowan gains a significant relationship boost with Skordred.
$ change_relation('skordred', 20)
$ change_favor('kharos', 1)
$ codex_add('dirt_general_starting')
jump .thirdMission

################################################################################

#Receive your third mission
label .thirdMission:

scene black with fade

"The next day."

# TODO
#Once music is being made for the game again, this is the point where the second castle theme should start being used and where it should be played for the first time.

scene bg6 with fade
show andras displeased at edgeright with dissolve
show jezera happy at midright with dissolve
show rowan necklace neutral at midleft with dissolve

je "Good morning, my hero. Yesterday was rather eventful, wasn't it?"

ro "That's one way of putting it."

an "It will likely not be the last of such turning points in both our plans and fates. However, what happened is in the past. We must look to the present and your future."

je "We've discussed the situation at length and have agreed that this is going to be a long campaign that will no doubt end in war."
je "We may yet be able to sway one, possibly two, of the Six Realms to our banner without bloodshed, but the others will take steps to prevent this once we play our hand."

an "I have my doubts on whether or not you'll be able to succeed, but the point is moot. Regardless of whether or not some kneel, we need a huge army if we hope to challenge any of the realms that would resist. Especially Prothea's legions."

"Rowan looked up at the red demon with interest."

ro "Oh?"

show andras happy at edgeright with dissolve

an "I had Cliohna brief me on the military contributions of each realm during the last war, it was... illuminating."

ro "(The old Andras never would have done that kind of research.  He's learning.)"

show andras displeased at edgeright with dissolve

je "While my brother was busy with learning about our enemies, I took a look at our own capabilities. As we suspected, there is no way our current recruitment prospects will ever meet our needs."
je "These small fry will simply not be enough. We need you to find a true army, one of a thousand soldiers or more. That may be difficult in Rosaria, but the goblins of Blackholt have been making quite the nuisance of themselves as of late for the nobles."
je "The combined force of their tribes should be enough to satisfy the first stage of my brother's new plan. Perhaps you can succeed where I failed at brokering an alliance with another of the chaotic races."


an "Agreed. You should be able to do this by the end of the year, along with more funds and forces ready for further conquests. Such territorial gains are even more important, as the more we take from one realm the weaker it shall be when it comes time to conquer it."

je "If you happen to find another suitably large army and bring it to our cause, that will also satisfy your mission."

"Jezera paused, something else was at the tip of her tongue."

je "There was one other matter I want addressed shortly. Duke Raeve will be decamping for Rastedel shortly. He will be a valuable piece in the hands of my allies in the capital."

ro "Your allies in the capital?"

"Rastedel was the capital of Rosaria. It made sense that Jezera had some sway among the most corrupt of the nobles at court. But, just how far had she penetrated into noble society?"

je "Indeed. But, I want you to go on a visit to the capital yourself. The appearance of the great hero of the realm is sure to cause a stir, and I am quite eager to see how your presence is reacted to."

je "Simply visit Rastedel when you have a chance. Arrangements will be made for the duke to join you."

"Rowan nodded slowly. Rastedel. That place of shattered dreams."

je "With that settled..."

if (society_type == 'feudalism'):
    je "We will be reserving a part of the treasury for our war chest, to only be used in the event of emergencies. I'm also increasing your salary, an appropriate rate for your new rank."

else:
    je "We will be reserving a part of the treasury for our war chest, to only be used in the event of emergencies. I'm also increasing your salary, a reward for your performance thus far."

an "That will be all."

jump .jobsIntro

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Alexia wants to help and placeable NPC tutorial

label .jobsIntro:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral behind bg14

al "Oh there you are Rowan."

hide alexia
show alexia 2 necklace neutral at midright with moveinright
show rowan necklace happy at midleft with dissolve

ro "Yes Alexia?"

show alexia 2 necklace concerned at midright with dissolve
al "Over these last months I haven't been feeling like I've been all that useful. I've been getting to know the staff and keeping an eye out for you, yes, but I think I can do more at the same time."

show rowan necklace neutral at midleft with dissolve

al "Since the castle is so understaffed, I thought that it might be a good idea to help out where I can. The smoother things go here, the easier things will be for you down the line."

"She fingered the amulet at her neck, in a way that felt uncomfortably familiar to Rowan."

al "Our fates are tied to the twins at this point."

ro "Where exactly where you thinking of helping?"

al "I can assist the staff with cleaning and cooking, I could assist Clionha in the library, or even work in the underground if it comes to it. There are lots of places to go."
al "Since you're managing the castle's affairs, I thought that it would be a good idea if you send me where you think I'm needed and I'll do what I can there."

ro "Are you sure about this?"

al " I am.  I may be a housewife, but that doesn't mean that I can't do my part to help out. I'm prepared to do what's needed..."

al "...I only ask that you not send me to the beasts below for longer than absolutely necessary."

show rowan necklace shock at midleft with dissolve

ro "Alexia...."

scene black with fade

"You may now assign Alexia to the various buildings in the castle to provide benefits every week."
"She has her own set of skills that make her suitable for some jobs more than others. Alexia will be shaped by her experiences, and the people she works with, during this time."
"A glimpse into her time working in this job will be given to you each week as well, which may have choices to be made and give you an idea of what happens to her in that time."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#goal 3 warning

label goal_3_warning:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy behind bg6

je "My hero."

hide jezera
show jezera happy at midright with dissolve

"Rowan was setting up his pack for his the week’s field work when a not entirely appreciated visitor came to see him off."

je "There was just one quick thing I wanted to mention to you before you left."
je "I gave you some objectives some time ago, and I couldn't help but notice that they are not all done yet."

if goblinRecruit == False and orciad_state != 2:
    je"I asked you to bring terms of alliance to one of the chaos races of the Rosarian plane. The orcs or the goblins. But, no such terms have yet been struck. This is not a situation that can be tolerated for long."
    if rastFirstVisit == True:
        je "Furthermore, You have yet to visit Rastedel. Your people’s poor capital must be quite lonely without its beloved champion paying a visit."
    
elif rastFirstVisit == True:
    je "You have yet to visit Rastedel. Your people’s poor capital must be quite lonely without its beloved champion paying a visit."
    
#If insufficient money and troops have been collected. (TODO)
# je "Let us not forget the matter of our troop levies and the coppers needed to keep them in the field. It would not due if we failed to be able to put a force of our own in the field. Not due at all."
                                                                                                                                        
je "The clock is ticking hero. Do not forget that."

"Rowan nodded softly."

ro "I’m working on it."

je "You best be. I do so hate to be disappointed."

"Jezera saunted away, leaving Rowan to consider her command. Her tone had been mostly innuendos, but her message was clear. Hurry it up."

return
    

