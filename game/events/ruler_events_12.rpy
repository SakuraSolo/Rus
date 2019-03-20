init python:

    #Helayna is acclimating in Rowan's room
    #If Helayna was claimed, triggers on week 30
    event('helayna_is_acclimating_in_rowans_room', triggers="week_end", conditions=('week >=30', 'raeve_keep_rowan_claimed_helayna'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Helayna is acclimating after taken by orcs
    #If Helayna wasn't claimed, triggers on week 30
    event('helayna_is_acclimating_after_orcs', triggers="week_end", conditions=('week >=30', 'not raeve_keep_rowan_claimed_helayna'), group='ruler_event', run_count=1, priority=pr_ruler_high)


label helayna_is_acclimating_in_rowans_room:
#Helayna is acclimating in Rowan's room
#If Helayna was claimed, triggers on week 30

#CG of Helayna looking out the window
scene black with fade

scene bg9 with fade
show helayna naked sad at midleft with dissolve
show rowan necklace neutral at midright with moveinright

"As Rowan entered his room, he was surprised to see that Helayna was neither sleeping or begging him to take her. Aside from taking meals, she essentially only had those two modes since she'd come here."
"Today, she was wrapped up in one of the blankets from his bed, sitting on a window bench and staring outside at the mountains visible from his room."

ro "Helayna?"

"She didn't reply at first, but the hero could tell that she had heard him due to the shift in her posture. So he approached and sat at the desk nearby her, looking out the window as well. After another minute, she finally answered with a quiver in her voice."

hel "Rowan, my love and my greatest failure. What kind of a knight am I that I couldn't control myself around you?"

ro "What happened? Did you get the band off?"

hel "No, its power is still upon me. I just can... think again. Along with that, I've gained the memories of all the sins I've committed since this curse was laid."

"A shudder ran through her body."

menu:
    "Rowan told her it wasn't her fault.":
        $ renpy.fix_rollback()
        ro "It wasn't your fault, it's Jezera's curse that did that to you."
        "Helayna laughed, turning now to look at the hero for the first time since he'd come in."
        hel "Was it?  I called out for you. Damn it, I thought that I'd finally put away that childish fantasy, but as soon as my discipline cracks my infatuation for the hero of my childhood came forth."
        jump helMergeA

    "Rowan put his arm around her.":
        $ renpy.fix_rollback()
        "Rowan stood back up and started towards Helayna. He intended to put his arm around her, but as he got close he was surprised to see the woman recoil from him in horror, now making eye contact for this first time."
        hel "No! Don't touch me! Even now I can barely keep myself in check, I'm desperately trying to stop myself from begging for you to fuck me again and again..."
        hel "Damn this childish fantasy. I thought I'd buried it years ago, but the moment my discipline cracked my infatuation for the hero of my childhood showed itself again."
        jump helMergeA

    "Rowan waited to let her finish.":
        $ renpy.fix_rollback()
        jump helMergeB


################################################################################


label helMergeA:

menu:
    "Rowan confessed he returned Helayna's love.":
        $ renpy.fix_rollback()
        ro "Helayna, I love you too. Don't call this infatuation."
        show helayna naked happy at midleft with dissolve
        if helaynaTitle == "teacher":
            "For a moment, her eyes shone with a brilliant joy that Rowan hadn't seen upon her face since the time he'd agreed to be her personal teacher. For the second time, he had touched her heart."
        else:
            "For a moment, her eyes shone with a brilliant joy. The expression was one that Rowan had never seen on her face before, there was no doubt that his words had touched her heart."
        show helayna naked sad at midleft with dissolve
        "Then her expression fell and tears streamed down the noblewoman's face at Rowan's confession."
        hel "Love that should never have been consummated. You were forced to break your vows to Alexia, I was forced to break the honor of my household. Nobility and peasants should never mix."
        "Another shudder ran through her."
        hel "The thing that scares me the most is how much I liked it. Even as a girl I had fantasies of having you as a lover. I knew and accepted that you were already married to Alexia and I would marry a nobleman, but I wanted that love in-spite of Solansia's laws."
        hel "Now, it's all I can do to resist the power of my heart and the band.  Two halves of me tear at one another, please help me! I need to escape from this place, I need to be away from you, before both of us fall deeper into this curse!"

        menu:
            "Rowan kissed her.":
                $ renpy.fix_rollback()
                show helayna naked aroused at midleft with dissolve
                "Instead of answering the woman, Rowan moved forward and pulled her into a deep kiss. She melted into his arms and eagerly returned his affections, the reservations of the conversation vanishing in an instant."
                ro "Our love isn't evil, it's something Jezera could never have created."
                "The blankets she'd been wearing fell away, revealing her nude form which quivered with arousal. The former knight pulled back from her keeper for a moment to brush away the tears from her eyes. As she did so, a somewhat melancholy tune escaped her lips."
                hel "Here we two lovers lie, under a blackened sky."
                hel "Until now our love was forbidden, but dark has revealed what was hidden."
                "Then her expression shifted from whimsical to hungry and she rushed forward into Rowan's arms for another deep kiss."
                jump helAcclimitedSex

            "Rowan resolved to help Helayna escape.":
                $ renpy.fix_rollback()
                jump helMergeC

            "It would be too dangerous to help her, for both of them.":
                $ renpy.fix_rollback()
                jump helMergeD

    "Rowan waited to let her finish.":
        $ renpy.fix_rollback()
        jump helMergeB


################################################################################


label helMergeB:

"Rowan didn't say anything, letting the former knight continue at her own pace."

show helayna naked sad at midleft with dissolve
hel "I only hope that I can redeem myself, in at least my own eyes if not Solansia's."

"Now her face fell downward, both embarrassed and oddly shy."

hel "Rowan, great hero of Rosaria, I beg you to help me get away from this place. I need to escape, to be away from you. If I don't, I fear that my love and lust for you will overcome what remains of my discipline and I will fall to corruption."

menu:
    "Rowan resolved to help Helayna escape.":
        $ renpy.fix_rollback()
        jump helMergeC

    "It would be too dangerous to help her, for both of them.":
        $ renpy.fix_rollback()
        jump helMergeD


################################################################################


label helMergeC:

ro "Alright.  I'll find a way to get you out of here. There's no way I'll be able to sneak you out the portals, so you'll have to brave the Rakshan Wastes. I don't know how you'll make the journey. But the safer route will be to the Empire of Sand-"

show helayna naked neutral at midleft with dissolve

hel "No, I'm not going to run away. I can't stay here, but I need to do something to help you."

ro "Are you certain? Helping me means helping demons who're trying to conquer the Six Realms."

#hel embarassed
hel "I can remember you telling me about what's happened here. Between you, uh, satisfying my needs, your confessions didn't fall on deaf ears. Perhaps with time we can bring them down from within or at least soften the damage they will do."

ro "I appreciate your confidence, but what you're suggesting seems incredibly risky. There are many creatures in the Wastes that could take advantage of that curse to do horrible things to you. Even a simple crossing will be a difficult task."

hel "Just get me armor, a weapon, and away from these walls. I'll handle the rest."

ro "Alright, if you're certain, best we start our plans as soon as possible. It might take weeks before I can get you out of here."

show helayna naked happy at midleft with dissolve
hel "I appreciate it, [helaynaTitle].  I know that you're taking a big risk here, I doubt your masters will be happy to learn I'm gone.  If I can ask one final thing, please help me keep my lusts in check while I remain in your care."

ro "Of course, I promise."

#Rowan will attempt to help Helayna escape in 5 weeks (TODO)
$ helayna_escape_method = 'rowan'
return


################################################################################


label helMergeD:

ro "No, it's too dangerous, for both of us. Not only will my masters be upset with me helping you escape, but what would you do? I can't get you through the portals, so you'd be braving the Rakshan Wastes to return to the Six Realms."

show helayna naked neutral at midleft with dissolve
hel "Please, you don't understand, I must, I need..."

show helayna naked sad at midleft with dissolve
ro "I'm sorry Helayna."

#Helayna will escape without Rowan's help in 5 weeks
$ helayna_escape_method = 'without rowan'
return


################################################################################


label helAcclimitedSex:

#naked Helayna stradling clothed Rowan's lap on the windowsill CG
scene cg136 with fade
show rowan necklace naked behind cg136
show helayna naked aroused behind cg136
pause 3

"The lustful woman held his lips for a long moment, at the same time her arms ran all over his back while she grinded her sloppy sex on his legs."
"To help her along, Rowan tried to work his hands underneath her. While he was trying to get at his trouser buckle, Helayna decided that his fingers made a far better source of stimulation and switched to rubbing herself all over them."
"The hero decided to humor her by working his digits into her snatch, causing her to moan loudly into his mouth. Evidently she'd really been holding herself back during their conversation, as that moan was accompanied by a big splash of her juices."
"Helayna broke off the kiss abruptly with an embarrassed look on her face."

ro "Wow, already? I didn't realize you liked my fingers so much, just look at the mess you made of me."

"She broke eye contact and gasped out a reply."

hel "I, ha, can, hah, keep going."

"Then her eyes darted down and saw her lover's bulge straining against his sodden garments. Apparently acting on instinct now, she worked his erection free and readjusted so she was kneeling in front of him on the bench."

scene cg125 with fade
show rowan necklace neutral behind cg125
show helayna naked aroused behind cg125
pause 3

"Almost as soon as Rowan felt the cool air of his room upon his erection, it was replaced by the warm interior of a woman's mouth."

ro "Gha, oh Helayna!?"

"She was vigorously sucking down on his member, taking it in as deeply as it would go while also running her tongue over every inch she could reach. Ever since she'd been brought to his room, Helayna had never given head before, always being completely passive in bed."
"Finding the current situation a little overstimulating, Rowan put a hand on his lover's head. Instantly she reacted to his touch, adjusting her pace and depth at the slightest pressure to match what he wanted."
"Rowan was impressed at her performance, while he had little doubt that she'd never done something like this before, already Helayna seemed to be an expert at giving blowjobs. He wondered how well she'd perform in bed now that she'd regained her wits?"
"The combined current stimulation, aroused state, and lewd thoughts that were racing through his head quickly brought the man to his peak and he used his hand to push his lover's face all the way down to the hilt."
"Helayna swallowed him eagerly and without gagging. With his lower head in her throat, he painted her throat white as she gulped down around him, humming pleasantly at the same time and stroking his thigh in appreciation."

scene cg126 with fade
show rowan necklace neutral behind cg126
show helayna naked aroused behind cg126
pause 3

"A moment later she popped off of him with a small flick of her head, and showed him her mouth. On her tongue was a small drop of his cum, which she swallowed a moment later."

hel "Thank you so much, [helaynaTitle]. It felt really good to make you feel good, and you taste wonderful."

"Rowan started to stroke her hair and was about to say something when Helayna abruptly threw her arms around his shoulders and whispered in his ear."

hel "I'm sorry about what I said earlier. I promise I won't try to push you away again. I love you, my hero."

scene bg9 with fade
show rowan necklace neutral at midright with dissolve
show helayna 2 happy at midleft with dissolve

ro "You sure you're alright?"

hel "Yeah, I'm pretty sure I can control the urges from this ring now. I can probably even move out of your room if you want to share it with another girl, I don't mind."

show helayna 2 aroused at midleft with dissolve

hel "At least, as long as I get a fair share of time with that wonderful sword of yours, I'm happy."

#Helayna will not attempt to escape. However, she can now be swapped out with other lovers if desired.
$ helayna_escape_method = 'no escape'
$ helayna_moveable = True
# TODO
#Helayna is added as an asset to the castle, raising military score slightly (~20-30) but cannot be used to help conquer map items.
#Rowan gains a little corruption.
$ change_base_stat('c', 2)
return


##########################################################################################################################
##########################################################################################################################
##########################################################################################################################


label helayna_is_acclimating_after_orcs:
#Helayna is acclimating after taken by orcs
#If Helayna wasn't claimed, triggers on week 30

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

wom "My lord, may I speak to you for a moment?"

"Rowan looked up, then did a double take in surprise to see one of the castle's maids addressing him. This was very rare, the staff almost never spoke to him."

ro "Yes, uh, go right ahead."

wom "Helayna has been asking to see you. If it would not be too much trouble, could you come and speak to her?"

if society_type == "might":
    "It felt strange having someone act like this to him, like they were addressing a noble. The girl must have been from one of the six realms and hadn't left her behavior behind."

else:
    "It felt strange having someone act like this to him, like they were addressing a noble. Which Rowan supposed now he was, he'd have to get use to that."

ro " I'm not sure I really should be seeing her, I'd rather not-"

"A frantic look crossed her and she suddenly darted forward to grab one of Rowan's hands."

wom "Begging your pardon, but she's acting very unusual right now. Please, she won't let me feed her anymore."

ro "Alright, let's go see Helayna."

wom "Thank you ever so much!  I pray that I will be able to repay this kindness."

ro "That's enough, please. We'll discuss it after I see what's happened with Helayna."

scene black with fade

"The maid lead Rowan to one of the spare rooms nearby the kitchens. He thought that surely Helayna wasn't staying in here if she'd been made into a pleasure slave and staff like he'd thought."

#CG of Helayna looking out window with alt interior.
scene black with fade
show rowan necklace neutral behind black
show helayna naked neutral behind black


"Sure enough, the red haired woman was inside. She was wrapped up in a blanket and staring out the window."

ro "Helayna?"

"At the sound of his voice, a small smile crept up on her lips. Letting her take her time to respond, Rowan stepped into the room and sat down nearby. The maid nervously stayed at the door and just watched the two of them."
"A few minutes passed in silence, then Helayna spoke."

hel "Rowan, my [helaynaTitle], I feel like I've woken from a horrible nightmare. Dark dreams have troubled me, dreams I cannot forget from what happened at the keep. I saw how those demons treat you, you saw how they treated me."
hel "I feel dirty, even now my curse threatens to overtake me, but my mind is mine again."

"Sunlight reflected off the tears that glistened in her eyes for a moment as she met his gaze for the first time. That smile was genuine, but bittersweet."

scene bg7 with fade
show rowan necklace neutral at midright with dissolve
show helayna naked happy at midleft with dissolve

ro "What happened to you? Was it Jezera who broke her promise, or was bringing you here Andras' idea?"

"She shook her head, making her hair form a pink halo around her head for a moment."

show helayna naked neutral at midleft with dissolve

hel "They didn't touch me then, it wasn't until I was rescued by her that the demons touched me."

"Rowan turned to face the maid who'd fetched him."

ro "Well, what's this about?"

wom "I... I found her in the barracks, secreted in one of the back rooms and covered in the dried orc fluids of all kinds. I thought it would be better if she was up here on the staff rather than an orc's toy, but... mistress found her."

ro "What did Jezera have to say?"

wom "{i}Oh well, she's here now we can put her to use as a fun little slut.{/i}"

"A loud sigh escaped from Rowan's lips. Really though, now that he was thinking about, how much better would it have been if Helayna had gone wandering off in her state or just sat there in the courtyard after what had happened."

ro "Regardless of how it happened, it is good to see you yourself again, Helayna. Since you told me what happened to you, I at least owe you the full story of what happened to me."

scene black with fade
scene bg7 with fade
show rowan necklace neutral at midright with dissolve
show helayna naked neutral at midleft with dissolve

"Rowan finished off the story by explaining the amulets that he and Alexia were now cursed with, like Helayna was locked to her ring. He noticed then that she was staring at it around his neck."

hel "Can she listen in at any time?"

ro "I don't think so, there's a special thing I need to do to talk to her and if she can, she's hidden it very well."

hel "Then, you can help me escape."

ro "Helayna? Are you certain? Where would you go, we're on the edge of the Rakshan Wastes here. There's no way I could sneak you through the portals, Jezera controls that."

hel "The orcs didn't just take me, they took my armor too. With that, I can take care of myself on the road, if you can get me that and find a way to smuggle me and some supplies away."

#hel embarrassed
hel "Rowan, I can't stay here. I told you, my desires are always about to overcome me. Those demons, they will break me. I need to escape. Please, you have to."

menu:
    "Rowan resolved to help Helayna escape.":
        $ renpy.fix_rollback()
        ro "Alright. I'll see what I can do."
        show helayna naked happy at midleft with dissolve
        hel "Thank you, [helaynaTitle]."
        wom " I'll help to. Just tell me what to do."
        ro "This isn't something that can be put together in just a few days and I only get one day a week in the castle. However, I think I have a plan...."
        #Rowan has resolved to help Helayna.
        $ helayna_escape_method = 'rowan'
        # TODO
        return

    "It would be too dangerous to help her, for both of them.":
        $ renpy.fix_rollback()
        ro "I'm sorry Helayna, it's too dangerous."
        #hel naked cry
        show helayna naked sad at midleft with dissolve
        hel "No! Please, you must reconsider!"
        ro "I can't bear thinking I'm sending you to your death and it could mean that the twins take out their anger on me and Alexia."
        hel "Rowan, what kind of a hero are you?"
        ro "One that's been forced to serve demons. I... have to be pragmatic. I'm sorry."
        "Without letting the two women say anything else, Rowan stood up and left the room."
        #helayna will escape without Rowan's help
        $ helayna_escape_method = 'without rowan'
        #gain a small amount of guilt
        $ change_base_stat('g', 2)
        return
