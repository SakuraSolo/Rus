label blameAlexiaOutcome:

#rowan should lose a decent amount of influence with alexia for telling on her
$ change_relation('alexia', -20)

ro "It... it..."

je "Yes?"

ro "Ah... Ah..."

an "Spit it out boy!"

ro "Alexia."

"The twins were silent for several long moments. Then Andras rubbed his hands together as a huge grin spread across his face."

show andras smirk at edgeright with dissolve

an "Oh, that’s rich. That’s just too rich. She let the little bird out of the cage, and her husband sang on her."

#jez angry
show jezera displeased at midright with dissolve

"Jezera glared silently at Rowan from her throne."

an "The real question is what to do about it. Obviously, with tattle-tale over here, we can’t truly harm her. But, mischief like this deserves an...answer…"

je "I don’t really care what you do. Leave me out of this."

an "Hrmm. Too many options can be harder than too few."
an "Well for starters…"

show rowan necklace concerned at midleft with dissolve

"Andras spent the next few minutes listing out a series of increasingly horrible punishments to subject Alexia too. Rowan’s hands shook softly, but otherwise he remained silent."
"As the demon was winding down on his punishments, it sounded like he might have made a decision. Rowan wasn't exactly sure what Andras intended, but he heard the words, 'long', 'slimy' and 'sexually voracious'."
"Knowing Andras, there was probably a way to convince him to let Rowan choose the punishment. Something quick and that Alexia could take. It took a minute for him to figure out such an offer."
"Perhaps he could offer to be the one to punish her himself? But, if he did that, would Alexia see that his goal was to protect her, or would she be angry at him for his more obvious role in her fate?"

menu:
    "Let Andras subject her to his plans.":
        $ released_fix_rollback()
        "He couldn’t do it. None of those punishments sounded half as bad the knowledge that he was the one hurting her."
        "Jezera had clearly had enough of this. She left, but not without leaving the silent hero a few words."
        je "What in the hells was that? Are you truly that terrified of my brother that you'd sell out your wife to him?"
        "Rowan didn't look at her. He felt numb, still hardly believing he'd actually done what he did himself. Since he hadn't reacted, she grabbed his chin and forced him to look at her in the eyes."
        je "You stupid coward. There are better ways you could have handled that. Actually come up with a plan next time something like this happens."
        hide jezera with moveoutright
        "After roughly shoving him back, the demoness turned around and marched away with an annoyed huff."
        show andras happy at edgeright with dissolve
        an "I have some things to care of. Don’t expect to see your little wife for awhile. But, don’t worry, she’ll still be intact when I’m done with her."
        hide andras with moveoutright
        "Rowan was left in the throne room, wondering how he’d ever tell Alexia…"
        #Alexia is removed from Rowan's room if she was in there and is unavailable in the guest rooms or for NPC placement for the next four weeks. She gains significant corruption and Andras influence.
        $ alexia_away_weeks = 5
        $ alexia_cant_work_weeks = 5
        $ all_actors['alexia'].job_state.job = None
        $ all_actors['alexia'].flags['andras_influence'] += 4
        $ change_corruption_actor('alexia', 4)
        #Rowan gains significant guilt.
        $ change_base_stat('g', 6)
        #Gain a favor with Andras, lose a favor with Jezera.
        $ change_favor('andras', 1)
        $ change_favor('jezera', -1)
        #Activate wulump event path
        # currently "Alexia in dungeon" is controlled via "alexia_away_weeks"
        return

    "Punish her yourself.":
       $ released_fix_rollback()
       $ change_base_stat('g', 6)
       jump rowanPunishment

################################################################################

label rowanPunishment:

ro "What if I punished her?"

an "What..if…"

show jezera neutral at midright with dissolve

"Jezera perked up in her chair. For a moment, she even seemed to forget her glare at him."

ro "She’s my wife. The castle security was my responsibility. All things considered, I should be the one to administer the punishment."

show andras displeased at edgeright with dissolve

"Andras narrowed his eyes. It was like the bolts in his brain were coming together on the subject."

an "You don’t have the stones, boy."

ro "I do. I’ll personally deliver twenty five lashes to her with an instrument of your choosing."

"Jezera was frantic with energy. She leaned over to her brother’s ear and began whispering something in a hushed tone. Andras just remained stone-faced."

an "How do we know that you won’t try to wuss out? Just pretend to hurt her?"

ro "Because I can do it in the public courtyard. You’ll be able to watch for yourself."

je "Oh, I hardly think that will be-"

show andras smirk at edgeright with dissolve

an "I like it! Having you be the one to hurt her yourself after ratting her out? The betrayal of it all? That’s an opportunity I can’t miss out."
an "But, if I get a whiff you’re going soft, then she’s going to go through a hell of a lot worse than a few lashes."

show jezera displeased at midright with dissolve

je "You’re insatiable, brother."

show jezera happy at midright with dissolve

je "Very well. Bring your wife to the courtyard in four hours time. There will be a punishment scaffold waiting."

hide andras with moveoutright

"With the work of the day concluded, Andras went off about his business. Meanwhile, Jezera stopped in front of Rowan."

je "Pain isn’t really my modus operandi. In truth, I find it rather distasteful. Thankfully, there is a way to go all out with the lashing, but not hurt your wife."

"Jezera reached into her bag and pulled out a small glass vial filled with a bubbly purple mixture. She placed it in Rowan’s hand with a wink."

je "If you apply this on to her skin before the whipping, she should have a much more pleasurable experience while still appearing to Andras like you’re truly hurting her."

"With that, Jezera turned and stalked off, leaving Rowan wondering if he could ever trust a strange vial put into his hand by that woman."

hide jezera with moveoutright

scene black with fade
scene bg9 with fade
show rowan necklace sad at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

al "Rowan! You’re back! What happened?"

ro "…"
ro "They threatened the staff with reprisals unless I told them who did it. I didn’t want to do it, but Andras would have killed the maids just to prove the point."

#if Alexia has at least 5 Andras influence and is higher than Jez influence
if get_actor_flag('alexia', 'andras_influence') >= 5 and get_actor_flag('alexia', 'andras_influence') > get_actor_flag('alexia', 'jezera_influence'):
    al "Are you sure Andras wasn’t just trying to scare you? He’s kinder than he acts."

#else if Alexia has at least 5 Jezera influence and is higher than Andras influence
elif get_actor_flag('alexia', 'jezera_influence') >= 5 and get_actor_flag('alexia', 'jezera_influence') > get_actor_flag('alexia', 'andras_influence'):
    al "Maybe he might have done that, but surely Lady Jezera would have stayed his hand…"

#rejoin

ro "I had no choice. I had to tell them that you did it."

show alexia 2 necklace look away at midright with dissolve

if all_actors['alexia'].relation < 20:

    "Alexia looked off to the side in silent reflection. She wouldn’t meet her husband’s eyes."

    al "You really told them what I did. Huh. The old Rowan never would have done something like that. So what’s going to happen to me?"

    ro "..."
    ro "Four hours from now I’m to take you to the courtyard and whip you in front of them. It was my suggestion. Andras was trying to decide on a punishment and I offered it as a solution."

    al "I see…"

    "Alexia went silent. She chewed her lips, as though there was something she wanted to say but couldn’t find the right words for."

#If Rowan Alexia Influence is above 5
else:

    al "I...I suppose you had no choice. If he was threatening the staff, I don’t know what I would do in that situation either."

    "She looked off to the side, struggling to meet his eyes."

    al "So what will happen to me then?"

    ro "Andras started talking punishments. I couldn’t let him do the things he planned to do. I couldn’t. So I intervened and suggested I punish you instead."
    ro "I am to take you down to the courtyard and whip you in front of them."

    al "Oh."

    show alexia 2 necklace concerned at midright with dissolve

    "She sighed deeply, but still found the courage to meet his concerned look."

    al "I suppose I don’t really have a choice do I? I just have to…"
    al "…"
    al "Can you hold me? I’m scared."

    "There was barely a need to ask. Her husband stepped forward and took her into his arms. She felt soft, even vulnerable, in his arms. This was going to be a hard thing to do."

#rejoin
show rowan necklace neutral at midleft with dissolve

"In the silence of the room, Rowan finally had the ability to contemplate what he was going to tell her the plan was."
"He had a few options. The simplest, and most harmful to her, would be to simply go ahead with the lashings. The second option was to try to fake a more severe punishment. That would be better for her...if he could pull it off."
"The final option was to try to use whatever the potion Jezera had given him was. It might indeed ease her suffering. Jezera liked power but didn’t hunger for pain. But, could he really trust her not to have anything planned?"

$ event_tmp['rowan_can_punish'] = True
$ event_tmp['fake_punishment'] = False
$ event_tmp['jezera_potion'] = False

menu rowanPunishment_menu1:
    "Punish her for lying." if event_tmp['rowan_can_punish']:
        $ released_fix_rollback()
        jump alexiaPunishOption

    "Fake Her Punishment.":
        $ released_fix_rollback()
        ro "I’m not going to let anything bad happen to you, though. I’m the one holding the whip. I’ll go easy on you."
        al "The twins won’t be happy about that."
        ro "No, they won’t be. I don’t know what Jezera will do if she thinks I’m holding back, but Andras would definitely be very angry. We’re going to need to put on a convincing show."
        show alexia 2 necklace concerned at midright with dissolve
        al "But, what if they find out? Then-"
        "Rowan put a finger on her lips, and looked her in the eyes. In truth, the prospect terrified him too, but he couldn’t show her that."
        ro "They. Won’t. Find. Out."
        ro "You’re going to need to listen to me very carefully. This is what we need to do…"
        $ event_tmp['fake_punishment'] = True
        jump punishmentCourtyardFake

    "Use Jezera’s Potion":
        $ released_fix_rollback()
        $ whipJezPotion = True
        "Rowan reached into his pocket and held out the vial. Of course, it was always a risk trusting Jezera with anything. But, she actively didn’t want to see Alexia hurt either."
        "Still, the prospect of some kind of side effect loomed large."
        "Rowan sighed to himself. There really was no better option."
        ro "There’s one other thing. Before I left, Jezera gave me this."
        "He held up the potion."
        ro "From the way she said it, it’s supposed to be some kind of way of dulling the pain. But, the way she talked about it also made it seem like it increased sensitivity in other ways."
        ro "She always has some plan going. I don’t trust her, but this might be the only option we have for fooling Andras."
        #If Jezera Alexia influence is above
        if get_actor_flag('alexia', 'jezera_influence') >= 5:
            al "If Mistress Jezera wants me to use it, then I should. I doubt she’d really let me get hurt."
            "Rowan almost winced at that. The half-demoness had really sunken her talons into Alexia."
        #else
        else:
            al " I don’t trust her either. But, unless you know of any other tonics that can stop the pain in the next few hours, it might be our best bet."
        #rejoin
        ro "I should get ready then. An hour before the whipping is supposed to begin, I’ll apply it to your skin. In the meantime, just take care of yourself. Bathe, relax, anything that might dull the impact."
        "Rowan gave his wife a quick but powerful hug. He wouldn’t let anyone hurt her. Not even himself."
        $ event_tmp['jezera_potion'] = True
        jump punishmentCourtyardPotion

################################################################################

label alexiaPunishOption:

#should require rowan to have lost some alexia influence, but not too much to make it very hard to get - maybe amount lost from blaming alexia plus a few points lost for another event?
if all_actors['alexia'].relation < 45:

    ro "(What else is there to do? I have to go through with the punishment. It’s not worth risking anything else.)"
    "For some reason, Rowan didn’t even feel the need to mention the potion."
    "Of late the two had been drifting apart so far. How else could his own wife had done this without telling him?"

    show rowan necklace angry at midleft with dissolve

    "The idea of adding one more to the list of ways that the two had taken power over his wife was sickening. It made him feel impotent. She was his wife. His, damnit!"

    show alexia 2 necklace angry at midright with dissolve

    al "So that’s it then? My safety wasn’t worth starting a fight with them?"

    ro "I came to this castle to save you? Didn’t I? I went through all of that. And you keep lying to me. Doing things like...like...freeing Helayna behind my back."

    al "I freed Helayna because you wouldn’t. You’re too weak. Too weak to defy the twins. Too weak to help anyone."

    "Rowan balled his hand into a fist. He almost slammed the bed in anger. His own anger freaked him out. When had he ever got this mad about anything?"

    al "Oh yeah, because you’re to doing so much defiance nowadays, huh?"

    #If Jezera has the most Alexia influence
    if get_actor_flag('alexia', 'jezera_influence') > get_actor_flag('alexia', 'andras_influence'):
        ro "Don’t think for a second I haven’t seen the way that you jump to do whatever it is Jezera tells you to do."

    #If Andras has the most Alexia influence
    else:
        ro "Don’t think for a second I haven’t seen the way you make eyes at Andras whenever you’re in the same room with him."

    #rejoin
    ro "Maybe I am weak. Maybe. We’ll see in the courtyard in a few hours."

    hide rowan with moveoutleft

    "He stormed out of the room, pausing to silently lean against the door, once he was out of sight of Alexia. He was going to punish Alexia for her lack of devotion to him. That should have made him feel powerful, right?"
    "But, it didn’t…"

    jump punishmentCourtyard

else:
#else
    "For the briefest of moments, Rowan actually considered going through with the punishment as intended without even using Jezera’s potion. But, the thought of Alexia’s brutal screams ended any such notion."
    "He simply didn’t have the heart to do it."
    #Player is taken back to the previous menu, but with “Punish Her” option now unavailable.
    $ event_tmp['rowan_can_punish'] = False
    jump rowanPunishment_menu1

################################################################################

label punishmentCourtyard:

# Alexia Whipping CG1 Variant 1
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked angry behind black

"Rowan approached the scaffold. Jezera and Andras were already waiting on a hastily constructed set of bleachers placed to the side. Some of the other residents around camp had all come to look at the cause of the commotion."
"It wasn’t hard to see why. Alexia was stripped naked and strapped into an X-cross on the stage. Rowan walked soberly to the stage and picked up a bullwhip prepared for him."
"Rowan was no expert with the lash, but with all his combat training it only took a few practice swings to get a handle on the punishment device."
"Andras had a hand over his face, but watched intently. No doubt to cover his smirk. Jezera was slumped sideways in her seat with her arms crossed."

ro "Look, I’m sorry about earlier. I just-"

al "Just do it already, asshole."

"Rowan stuttered. Why was she angry at him? She’d been the one to free Helayna? Didn’t she know that she was responsible for all of this?"

ro "Fine."
ro "You will count out loud after each lash. We clear?"

al "...yes."

#Alexia Whipping CG1 Variant 2
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked angry behind black

"Rowan breathed in and then swung forward, landing a shockingly hard blow on her back. The air crackled, and Alexia grunted."

al "One."

"He pulled back and brought another blow crashing against her shoulder blades. His time he could see the effect on her. She practically squirmed, trying to dodge a blow that there was no way to escape from."

al "Two."

"Now he was starting to get into it. Every time the lash struck, he got a strange sense of euphoria. The whip became an extension of his hand. Alexia, on the other hand, was definitely not getting into it."

show alexia necklace naked sad behind black

al "Three...uh...Four…"

"Tears formed in her eyes. She chanced a glance backwards with betrayal."
"More whip strikes soon followed. He placed his anger at her in them, his frustration with his situation, and with her distance. They added fuel to his arm."

al "Five. Ahhh. Ahhh. Six. Seven."

"Andras was leaning forward in his seat now. His eyes shone brightly. This contrasted Jezera, who was starting to turn away each time she saw the whir of leather in motion."
"Alexia’s body was really starting to show the signs of the pain now. Deep red welts were etched into her back, marking each lash. She was shivering. Whimpering. It was a pathetic sight."

#if rowan corruption is lower than 20
if avatar.corruption < 20:
    "Andras was leaning forward in his seat now. His eyes shone brightly. This contrasted Jezera, who was starting to turn away each time she saw the whir of leather in motion."
    "Alexia’s body was really starting to show the signs of the pain now. Deep red welts were etched into her back, marking each lash. She was shivering. Whimpering. It was a pathetic sight."

#rejoin

#Show Alexia Whipping CG Variant 3
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked sad behind black
show andras displeased behind black
show jezera displeased behind black

"The numbers rose higher and higher. It was easy to get lost in the rhythm of the whip. It was easy to forget that each time he struck, Alexia’s back must have been shooting with pain."

al "Fourteen. Fifteen. Ahh. Sixteen."

"Rowan’s mind searched for excuses for his actions. She was a bad wife. She was a traitor. She was the reason why he was in this situation. Yet, he could not arrive at the word that he really meant. Unfaithful."

al "Please. Just...just stop. For a second. I can’t…"

ro "You’re not at twenty five yet."

al "Please...Rowan…"

#if rowan corruption is lower than 49
if avatar.corruption < 49:
    "That got his attention. Seeing her squirming and crying was too much. How could he keep doing this? He was a hero. He came to rescue her. His arm lowered."

    an "You made a promise, Rowan. You have to see it through."

    "Rowan sighed. Andras was cracking his knuckles. This was his punishment as much as Alexia’s now. There would be no escape. Alexia pleaded at him with her eyes, but to no avail. Rowan whipped her once more."

#else
else:
    "Rowan stopped for a second, looking at the pathetic whimpering form of his wife. Is this why he’d gone through all of this? To save her of all people? He seethes quietly."

    ro "No. You’ll rest when I’m done."

    "Alexia turned her eyes from him. Then he lashed out with the whip again, making her arch in her back in pain."

#rejoin

al "Ahhh. Seventeen. Seventeen."

"Strike."

al "Eighteen."

"Strike."

al "Nineteen."

"By the final few, even Rowan’s stamina was starting to yield. There was only so much pain he could cause before this little revenge became hollow. Certainly he hadn’t done any lasting damage. But, the pain was starting to get to him too."

al "Please, twenty five. I’m done now. Please. It’s over right? Twenty five?"

"Rowan sighed, lowering the whip. He almost dropped to his knees. Every moment, more and more of his euphoria was replaced with shame."

je "Someone get a towel on her and take her to the cellar."

"Rowan watched in silence. He would just need to go down and see her soon. If she just listened to him, then it would all be back to normal soon."

#rowan loses influence over alexia
$ helAlexiaWhip = True
$ change_relation('alexia', -5)

jump NTRaftercare

################################################################################

label punishmentCourtyardFake:

#Alexia Whipping CG1 Variant 1
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked concerned behind black


"Rowan approached the scaffold. Jezera and Andras already were waiting on a hastily constructed set of bleachers placed to the side. Some of the other residents around camp had all come to look at the cause of the commotion."
"It wasn’t hard to see why. Alexia was stripped naked and strapped into an X-cross on the stage. Rowan walked soberly to the stage and picked up a bullwhip prepared for him."
"He walked over, slightly brushing his hand over her rear. She leaned back to look into his eyes. It was the agreed upon signal that all way set for the plan."
"Rowan was no expert with the lash, but with all his combat training it only took a few practice swings to get a handle on the punishment device. He wasn’t totally certain how much force he could take out of the blow while still making it look read. He just hoped it would be enough."
"Andras had a hand over his face, but watched intently. No doubt to cover his smirk. Jezera was slumped sideways in her seat with her arms crossed."
"Rowan whispered to her in a hushed tone."

ro " Remember. It has to look real."

al "I’ll do my best."

"He took a step back and raised his voice loud so that the rapidly swelling audience could hear him."

ro "You will count out loud after each lash. We clear?"

al "...yes."

#Alexia Whipping CG1 Variant 2
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked concerned behind black

"Rowan breathed in and then swung forward, landing a shocking hard blow on her back. At the last moment, he took some of the force from the blow, so it would only mostly look hard. Alexia grunted still."

al "One."

"He pulled back and brought another blow seemingly crashing against her shoulder blades. She made a point of trying to squirm in reaction to blow. Though, certainly some of her reaction was real pain."

al "Two."

"Every so often, he’d check back at the demons. Were they buying it? The longer it went on, the more paranoid he started to get."

show alexia necklace naked sad behind black

al "Three...uh...Four…"

"Tears formed in her eyes. She wasn’t bad at this."
"More whip strikes soon followed. He tried to lesson the impact of each blow, but in truth, some still landed with something resembling strength. Certainly the welts on her back that were developing, while shallow, were proof she wasn’t escaping without any pain."

al "Five. Ahhh. Ahhh. Six. Seven."

"Andras was leaning forward in his seat now. His eyes shone brightly. Watching them. This contrasted Jezera, who was starting to turn away each time she saw the whir of leather in motion. She, at least, certainly seemed to buy it."
"Alexia’s body was really starting to show the signs of the pain now. Red welts were sewn into her back, marking each lash. She was whimpering. It was so real that it seemed impossible that she was faking it."

#Alexia Whipping CG Variant 3
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked sad behind black
show jezera displeased behind black

"The numbers rose higher and higher. It was easy to get lost in the rhythm of the whip. A few times, her groan of pain seemed to tell he’d gotten too lost in it."

al "Fourteen. Fifteen. Ahh. Sixteen."

"Alexia was shivering now. Squirming even when the whip wasn’t lashing out at her back. Now, she launched into her boldest play yet...If it was still a play that is..."

al "Please. Just...just stop. For a second. I can’t…"

ro "You’re not at twenty five yet."

al "Please...Rowan…"

"Rowan sighed. That one felt real. A part of his heart panged. But, he knew he needed to keep up his stern demeanor. Much worse things would happen to her if he faltered now."

ro "No. You’re done when you’re done."

"He brought the whip back behind his back and struck once more. Andras’ eyes twinkled."

al "Ahhh. Seventeen. Seventeen."

"Strike."

al "Eighteen."

"Strike."

al "Nineteen."

"By the final few, even Rowan’s stamina was starting to yield. It was not easy giving this kind of treatment to a loved one. But, it was actually harder to make the blows land without hurting her."
"Even as his skill rose, his exhaustion made each blow a little bit more wild. A bit more likely to make her go up on her tiptoes and cry out."

al "Please, twenty five. I’m done now. Please. It’s over right? Twenty five?"

"Rowan sighed, lowering the whip. He almost dropped to his knees. It was done. Now the question was the results. Would they buy it?"
"He looked back towards the twins."

$ event_tmp['punishment_deception_passed'] = False

#deception check DC12
if check_skill(12, 'deceive')[0]:
#pass
    "Andras was leaning back in his chair with a satisfying grin. He even seemed to notice Rowan looking at him, and gave a nod of approval. Surely a sign that the ruse had worked?"
    #mark as passed
    $ event_tmp['punishment_deception_passed'] = True

#fail
else:
    "Andras was looking on stone faced. Every few seconds he or Jezera would turn to one another and whisper something. Rowan almost shivered. Surely that wasn’t a good sign."
    #mark as failed

#rejoin

je "Someone get a towel on her and take her to the cellar."

"Rowan leaned over and gave Alexia’s hand a squeeze before she was taken off. He just hoped that he’d managed to dilute the blows enough that her aftercare would go smoothly."

#Rowan gains some influence with Alexia, however not enough to overcome the loss for selling her out in the first place.
$ change_relation('alexia', 7)

#if rowan influnce on alexia is highest
if all_actors['alexia'].relation > get_actor_flag('alexia', 'andras_influence') and all_actors['alexia'].relation > get_actor_flag('alexia', 'jezera_influence'):
    jump alexiaAftercare

#else
else:
    jump NTRaftercare

################################################################################

label punishmentCourtyardPotion:

#Alexia Whipping CG1 Variant 1
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked concerned behind black

"Rowan approached the scaffold. Jezera and Andras are already waiting on a hastily constructed set of bleachers placed to the side. Some of the other residents around camp had all come to look at the cause of the commotion."
"It wasn’t hard to see why. Alexia was stripped naked and strapped into an X-cross on the stage. She shivered lightly in the morning. Rowan walked soberly to the stage and picked up a bullwhip prepared for him."
"Rowan was no expert with the lash, but with all his combat training it only took a few practice swings to get a handle on the punishment device."
"Andras had a mouth over his face, but watched intently. No doubt to cover his smirk. Jezera was slumped sideways in her seat with her arms crossed. Though, her eyes were fixed very intently on the proceedings."

ro "How does it feel? Are you alright?"

al "I don’t know. So far it’s just a faint tingling."

"Rowan nodded. Jezera had said that the experience she would feel would be pleasurable. But, what had she meant by that? Surely there was some kind of double entendre to her words."
"He turned back slightly and raised his voice so that the audience, especially its two more important members, could hear."

ro "You will count out loud after each lash. We clear?"

al "...yes."

#Alexia Whipping CG1 Variant 2
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked concerned behind black

"Rowan breathed in and then swung forward, landing a shockingly hard blow on her back. The air crackled, and Alexia gasped in shock. In moments, she was wiggling in her bonds."

al "O-one."

"Rowan paused briefly. That sure didn’t sound like pain. It sounded more like their alone time. He glanced back at Jezera who flashed a tiny grin."
"Still, he had to continue. He pulled back and brought another blow crashing against her shoulder blades. She practically squirmed, as much trying to dodge the blow and lean into it."

al "Two..."

"That time he could almost feel her excitement. Every time the lash struck, he got a strange sense of euphoria. It was certainly hurting her still, but he was getting mixed signals. Pain and pleasure coming out at once. It was kind...enjoyable..."

show alexia necklace naked aroused behind black

al "Three...oh...Four…"

"She was gasping now with every blow. She chanced a glance backwards with needful eyes."
"More whip strikes soon followed. He placed his lust into it. He placed his strange, sexual even, high into every blow. It guided his arm, and made much of the rest of the world, even the twins, fade away."

al "Five. ugh. Six. Seven."

"Jezera was leaning forward just as heavily as Andras was now. She flashed her teeth in a deep grin."
"Alexia’s body was really starting to show the signs of the lash, even if her actual reactions were mostly lustful. Deep red welts were etched into her back, marking each lash. She was shivering...Whimpering…"
"..Wet."

#if rowan's corruption is less than 20
if avatar.corruption < 20:
    "It was a strange thing, watching his wife grow so aroused from something that was supposed to hurt her. When she looked back at him, her eyes were pleading for more delicious pain."
    "He knew that the cause was Jezera’s potion. It must have been mixing up her sensations. It must have been. But, the question that Rowan had to ask himself was why he was enjoying giving her that pain? Why did he love the way she shivered and shook with each crack of the whip?"
    "Rowan swallowed. He shouldn’t think about that."

#if rowan's corruption is 20-49
elif avatar.corruption < 49:
    "There was no mistaking what the potion had done. Jezera had made her a masochist, at least for the moment. Every time he cracked the whip across her back, He could see the mix of signals in her eyes. Pain turning to pleasure. Pleasure turning to pain. It was oddly…"
    "It was oddly enticing. Rowan paused if only for a brief moment. His fingers traced her back, and the welts on it lightly. She shivered under his touch. He hadn’t known he had the capacity to be such a sadist. But, this was a rather unusual situation…"

#else
else:
    "The squeals of pleasure and pain were unmistakable."
    "Jezera’s potion had turned Alexia into a painslut, eagerly drinking in the power of each blow. Her body wiggled back afterwards each time, eager for more and more of that sweet feeling. It was obvious from every last whimper and groan."
    "Rowan didn’t mind of course. This was all still new to him, but he found he actually liked her reactions. He liked the mix of pleasure and pain in her every cry. There was a slight wicked thrill in the idea that he might be a sadist himself."
    "Clearly this had been Jezera’s plot all along. But, was that such a bad thing?"

#rejoin

#Alexia Whipping CG1 Variant 4 (aroused)
scene black with fade
show rowan necklace neutral behind black
show alexia necklace naked aroused behind black
show andras displeased behind black
show jezera happy behind black

"The numbers rose higher and higher. It was easy to get lost in the rhythm of the whip. It was easy to get lost in her little gasps and moans. It was easy to get lost way she seemed to dance in place each time the lash struck. The flow of the moment."

al "Fourteen. Fifteen. Oh. Sixteen."

"Rowan’s eyes were drawn to the trail of wetness going down her thigh. It wasn’t hard to see the way she was sticking her ass out towards him either. It was almost like she was asking him to fuck her right here on stage. Just how powerful was the potion?"

al "I. oh. I can’t...I can’t think right now. Maybe. Ha. Maybe give me a second?"

ro "You’re not at twenty five yet."

al "Please...Rowan…"

#if corruption is less than 50
if avatar.corruption < 50:
    "Rowan paused for a moment, running his hands down the curve of her back. He could feel the many throbbing welts. He suspected she’d be a little less keen on those once the potion wore off. She wiggled softly underneath his hand."
    "His hand drifted lower. Of course, her lower lips were soaked. He toyed with them lightly for a moment. Alexia, of course, could do little in her blissed out state besides moan."

    an "You’re here to whip her, not fuck her. Get on with it."

    je "You have no sense of fun, brother."

    "Rowan took a step back. Even that one moment of rest seemed to have restored a little bit of her vigor. She even nodded back to him slightly. No need to be told twice. He struck her with the whip once more."

#else
else:
    "Rowan stopped for a moment, looking down at her shivering form. She was pleading for a brief respite. Yet, he knew that Andras was still watching him to ensure he didn’t falter. Besides...he didn’t want to stop."
    "With barely any hesitation, he brought the whip back and struck out in another lashing blow. It was enough to make her scream."

#rejoin
al "Ohhh fuck. Seventeen! Seventeen!"

"Strike."

al "Eighteen!"

"Strike."

al "Nineteen!"

"By the final few, even Rowan’s stamina was starting to yield. Even driven by a newfound sense of sadism, there was only so long an untrained whip master could keep going at full."
"Yet, her body was still only growing hotter and hotter. She was practically screaming now with each blow. Was it possible to make her cum from pain alone?"

al "Twenty five. I’m at twenty five now, right? Fuck."

"Rowan sighed, lowering the whip. Part of him wanted to continue. But, he knew that the game had already gone far enough. Alexia was shivering in her bonds."
"Andras and Jezera, of course, were whispering to each other. There was no way he wouldn’t notice how much she’d enjoyed that. But, no doubt Jezera would talk him out of too harsh a reaction."

je "Someone get a towel on her and take her to the cellar."

"Rowan watched sympathetically. She’d need close care. She may have enjoyed herself, but the toll it had taken on her body was clear to see. Besides, after such an intense experience, she probably had needs she wanted to fulfill. And perhaps, so did he."

#Alexia gains corruption and a little Jezera influence.
$ change_corruption_actor('alexia', 5)
$ change_actor_num_flag('alexia', 'jezera_influence', 3)

#if rowan influnce on alexia is highest
if all_actors['alexia'].relation > get_actor_flag('alexia', 'andras_influence') and all_actors['alexia'].relation > get_actor_flag('alexia', 'jezera_influence'):
    jump alexiaAftercare

#else
else:
    jump NTRaftercare

################################################################################

label NTRaftercare:

scene bg14 with fade
show rowan necklace neutral at midleft with moveinleft

"Rowan walked quietly through the corridors underneath the castle. The room they’d taken Alexia to recover was this way. After a lashing of that sort, she’d need time to recover."

show orc soldier neutral at midright with moveinright

"Rowan’s mind was still tossing and turning over what had transpired, how to even discuss the events in the courtyard, before he was stopped by the surprise appearance of an orc guard outside her room."

os "Stop. Said no puny human Rowan come this way."

show rowan necklace angry at midleft with dissolve

ro "Who said that?"

os "Human female with fire hair. Said no Rowan."

"Rowan’s eyebrows narrowed. Alexia had told him not to see her right now. In her moment of need she didn’t want to see him?"

ro "Fine."

"Rowan stormed away fuming. He wondered how she didn’t understand that the entire reason he’d went through all of that was for her sake. So they wouldn’t be the ones to punish her."

hide rowan with moveoutleft
hide orc soldier with moveoutright

scene black with fade
show alexia necklace naked aroused behind black

al "Oh. That feels….that feels good."

"Alexia gasped softly. Hands softly roamed her body. They were applying lotion, but they were also engaged in...other tasks..."
"Her mouth let out soft gasps every few seconds. It let her escape from the throbbing pain that consumed her back."

#If Jezera Influence is higher then Andras Influence
if get_actor_flag('alexia', 'jezera_influence') > get_actor_flag('alexia', 'andras_influence'):
    show jezera happy behind black

    je "That’s right, girl. Just relax into my hand. It feels good doesn’t it? Nothing to cure a bit of back of back pain a woman’s touch…"

    "The soft feminine hand exploring her folds dug deeper and deeper. The sensation of it drove the thoughts out of her head. Thoughts of her punishment. Thoughts of Rowan..."

    al "Oh lords. Yes...Mistress..."

    #Alexia gains some Jezera influence.
    $ change_actor_num_flag('alexia', 'jezera_influence', 3)

#If Andras Influence is higher then Jezera Influence
else:
    show andras smirk behind black

    an "Oh stop pretending you don’t like where my hand is. You can’t hide from me how badly you want it. Admit it."

    "The powerful masculine hand exploring her folds dug deeper and deeper. The sensation of it drove the thoughts out of her head. Thoughts of her punishment. Thoughts of Rowan..."

    al "Oh fuck. Fuck. More. Please. More... "

    #Alexia gains some Andras influence.
    $ change_actor_num_flag('alexia', 'andras_influence', 3)
#rejoin
return

################################################################################

label alexiaAftercare:

scene bg14 with fade
show rowan necklace neutral at midleft with moveinleft

"Rowan walked quietly through the corridors underneath the castle. The room they’d taken Alexia to recover was this way. After that kind of session, she’d need time to recover."

show orc soldier neutral at midright with moveinright

"Rowan’s mind was still tossing and turning over what had transpired, how to even discuss the events in the courtyard, before he was stopped by the surprise appearance of an orc guard outside her room."

ro "Alexia is in there?"

"The orc nodded. And stepped aside."

scene bg11 with fade
show rowan necklace neutral at midleft with moveinleft

ro "Alexia? Alexia?"

show alexia necklace naked sad at midright with moveinright

"Alexia was laying naked on her back, tears running down her cheeks. Even with all the steps he’d taken to prevent her from being harmed, there were still dark welts on her back where the lash had struck."

ro "Hey there. Move over a little bit, please. Let me sit with you."

"Alexia groaned and nodded. She made a bit of space for her husband to sit with her. There was a bowl next to the table with some kind of cream. It was probably to help with marks."
"Rowan put some of the cream on his hand and started rubbing it into Alexia’s back. She sighed weakly. Everywhere that showed signs of the lash’s bite was throbbing with heat."

ro "How did it feel? Are you alright?"

#if fake punishment was selected
if event_tmp['fake_punishment']:
    "Alexia leaned into his touch, but otherwise remained silent for a time. She was struggling to find the will to speak."

    al "Well it hurt. Badly."

    #alexia necklace naked happy

    al "But, it could have hurt a lot more."

    show rowan necklace happy at midleft with dissolve

    "She smiled at him and he smiled back. For a moment, it seemed like all of the unpleasantness of earlier was gone and they were back to just being who they always had been with one another."

    al "Think we fooled them?"

    ro "I hope so. At least, Andras didn’t seem to know back in the courtyard. And I don’t know if Jezera would care even if I did fake it."
    ro "Still, We’ll find out soon enough. So long as we don’t hear anything from them, we can assume the answer is they bought it."

    "Alexia pressed herself closer to him. She was shivering lightly. It was strange. Her back was all heat, but she seemed like she was freezing. All he could do was press the blanket closer to her and massage more soothing cream on her back."

#If Use Jezera’s Potion was Selected
elif event_tmp['jezera_potion']:
    "Alexia leaned into his touch, but was struggling to find the will to speak. Every so often, she let out a soft gasp. A likely remnant of the potion’s fading effects."

    al "It was so weird. It still hurt. It hurt badly. But, I didn’t quite realize that pain could feel so good."

    show alexia necklace naked aroused at midright with dissolve

    al "By the end of it I was so worked up I could have…"
    al "Well, I was pretty worked up is what I’m saying."
    al "How about you? Did you...did you like it?"

    "Rowan paused to collect his thoughts. He thought back to how he felt in the courtyard. He remembered the rising heat as each blow sang out."

    #if rowan corruption is less than 50
    if avatar.corruption < 50:
        show rowan necklace aroused at midleft with dissolve

        ro "It was really strange, but I think I did. You were getting so worked up by it, how could I not?"

        "Still tired, all his wife could muster was a soft smile."

    #else
    else:
    #rowan smirk
        show rowan necklace aroused at midleft with dissolve

        ro "With the way you were moaning like a slut back there, how could I not?"

        "Maybe when I want to work you up some other time, I’ll take you back down there."
        "Alexia blushed softly, but otherwise didn’t muster a reply beyond a soft whimper."

    #rejoin (from corruption split)
    "She leaned in closer to his touch. From this vantage point he could see the remaining glisten on her thighs. Just how much of the reaction the potion had brought out had been there before without either of them know? Rowan didn’t want to think about that."

#rejoin (from fake punishment / potion split)

show rowan necklace neutral at midleft with dissolve
show alexia necklace naked aroused at midright with dissolve

"The two remained with bodies pressed against each other for a time. It wasn’t long before Alexia’s shivering had gone down to almost nothing, and the strength was starting to come back to her."

al "If you want, you can use your hands…on me."
al "My back is too sore for anything more intensive. But, if it’s just hands, I’d like that."

#If Use Jezera’s Potion was Selected
if event_tmp['jezera_potion']:

    al "I played with myself before you came in. After how worked up I got, I couldn’t help myself. But, it wasn’t enough."

#rejoin
ro "I think after all we’ve been through today, I don’t think I could do more than use my hands myself."

#Rowan Alexia Aftercare CG
scene black with fade
show alexia necklace naked aroused behind black
show rowan necklace aroused behind black

"Rowan slid a hand to her thigh. He rubbed her skin softly, feeling its texture. His wife responded by parting her legs slightly. It was a welcome to go further."
"So, Rowan slid a single finger inside her lower lips slowly."

al "Oh."

#if the player previously selected Fake Her Punishment
if event_tmp['fake_punishment']:
    "Her sex was already damp, at least slightly, from the closeness and having him rub her back. But, with his finger steadily teasing her more and more, it wasn’t long at all before Alexia’s pussy started to get wetter and wetter."
    "Soon, she was positively drenched. Juices were beginning to collect on his hand and her thighs. All clear signs she was ready for more."

#else
else:
    "From the moment he entered her, it was clear that Alexia hadn’t lied about having already touched herself. Her pussy was already drenched. He found no trouble at all working his finger inside of her, no trouble exploring her sensitive passage."
    "He’d only been subjecting her to his touch between her legs for mere moments and her body was already begging him for more."

#rejoin
"Rowan kept a slow steady pace with his fingers. Nothing too fast or brutal, with her body in the state it was in. Still, he did take the time to slide a second finger in. His every motion was intended for the purpose of causing a feeling to rise inside of her."
"To make a need rise in her like a tide."
"There’s a strange gentle quality to it. It’s not a furious act of lovemaking, or a warm up to a more intense fucking. It’s just a husband and wife in a bed together with his hands softly bringing her body pleasure."
"In the glow of the moment it’s almost easy to forget the events that brought them here."

al "Oh. That feels...that feels...oh."

"The longer he continued pumping his fingers inside of her, the harder it got for her to remain still. She squirmed, arching her back and curling her toes. Every so often she tried to mouth a word, but was too tired to even form the words."
"When Alexia finally came against her hands, she did it without a scream. She just bucked her hips and let out a broken gasp. A soft orgasm for a soft moment."
"In the afterglow of it, her eyes were fluttering. She was barely even able to get a word out."

al "I know...I know you did what you had to do. Telling them, I mean. I forgive you, Rowan."

"That was all she said before she went to sleep. Rowan curled up next to her, but even though he too was tired, he just couldn’t sleep. Not with all of the thoughts racing through his head."

#Rowan gains a little Alexia influence, combined with faking the punishment this should not be enough to overcome the loss for selling her out in the first place.
$ change_relation('alexia', 3)

#If Fake Her Punishment was selected, and the roll was a success, half of the guilt gained for selling Alexia out is lost.
if event_tmp['fake_punishment'] and event_tmp['punishment_deception_passed']:
    $ change_base_stat('g', -3)
#End Scene (If Fake Her Punishment was selected, and the deception roll was a failure, jump to andrasFailure below instead)
if event_tmp['fake_punishment'] and not event_tmp['punishment_deception_passed']:
    jump andrasFailure
else:
    return

################################################################################

label andrasFailure:

scene bg6 with fade
show andras displeased at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "You wished to see me?"

an "Yes, I did."

show andras angry at midright with dissolve

"His face radiated menace. Clearly, this was not going to be a fun conversation."

an "That was a good show out there, but do you actually think I don’t know what a woman in pain really sounds like?"

show rowan necklace concerned at midleft with dissolve
ro "…"

an "I’m not mad. If anything, it showed me that I was right. I couldn’t trust you to be a man and hurt her. "
an "Have no worries. She’s not going to be harmed too much for this. But, she will have to go through the original intended punishment. I’ll give her back, no worse for wear, in about a month or so."

"Rowan clenched his face, but otherwise remained silent."

an "Nothing to say? That’s the spirit, servant. Learn to act a bit better next time. You might even fool me."

#Alexia is removed from Rowan's room if she was in there and is unavailable in the guest rooms or for NPC placement for the next four weeks. She gains significant corruption and Andras influence.
$ alexia_away_weeks = 5
$ alexia_cant_work_weeks = 5
$ all_actors['alexia'].job_state.job = None
$ all_actors['alexia'].flags['andras_influence'] += 4
$ change_corruption_actor('alexia', 4)
#Rowan gains smallt guilt.
$ change_base_stat('g', 2)
#lose a favor with Andras.
$ change_favor('andras', -1)
#Activate wulump event path
return
