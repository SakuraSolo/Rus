label greyhideBatriHelp:

scene bg22 with fade
show rowan necklace neutral at midleft with dissolve
show greyhide neutral at cliohnaright with dissolve


if ghBatriLater == True:

    gh "Rowan. Have you decided the size of Batri’s 'care package'?"

    ro "Hmmmm."

    jump ghBatriHelpMenu

else:
    pass


"Rowan found Greyhide with a freshly finished waraxe in hand. The minotaur kept staring at his creation, apparently lost in thought."

show rowan necklace concerned at midleft with dissolve

ro "Is something on your mind, Greyhide?"

"With a sigh, the minotaur put the axe away, next to a dozen similarly made weapons."

gh "No."
gh "Yes..."
gh "The usual. Working the forge can be… Tedious."

"The minotaur smiled at him, in this weird way only a creature with a muzzle could."

if alexiaForgeIntro == True:
    gh "But you and Alexia are always a pleasant distraction from the usual drudgery."
    
else:
    gh "But your rare visits are always a pleasant distraction from the usual drudgery."
    
gh "What do you need, Rowan?"

ro " ..."
ro "I need you to make even more weapons."

gh "..."

"The minotaur gave him the thousand yard stare."

show rowan necklace happy at midleft with dissolve

"Rowan smiled apologetically."

gh "Of course. That is why I’m here. "
gh "What exactly do you need?"

show rowan necklace neutral at midleft with dissolve

ro "Not the usual stuff we give to our troops. This time, quality and practically are secondary."
ro "What I need are axes that first and foremost look impressive."
ro "I want every orc who sees them green with jealousy."

gh "As opposed to their usual shade of green?"

show rowan necklace happy at midleft with dissolve

ro "… Yes."

show rowan necklace neutral at midleft with dissolve

ro "I need them awed by them. I need them to think ”This is what I'll be able to get if I join Batri”."
                                                                   
gh "Simple enough. Our forge is more than capable of making equipment like that, and so am I."
gh "You only need to tell me how many do you need."

"Now that was an interesting question."

if batri_power < 4:
    "Batri still needed a lot of support. Even if Rowan ordered Greyhide to work on this full time for several weeks, it won’t be enough to give the orc the boost he needed."
    
elif batri_power > 3 and batri_power < 6:
    "Batri’s support has already grown considerably. Should he order Greyhide to work on this full time for several weeks, they will likely get close to full support by the end of the month."
    
elif batri_power > 5 and batri_power < 8:
    "Batri was almost ready. If Greyhide works on this full time, the weapons will most certainly give him the final push he needed. They can probably settle for a medium delivery."
    
else:
    "Batri was almost ready. Rowan only needed some equipment to give Batri the final push he needed, so a small delivery would be enough."


"For logistic reasons, it was better to make it a onetime deal. Besides, if this became a regular occurrence, Batri could get the wrong message – he could be tempted to delay the raid so he could con Rowan out of more free equipment."
"Well, free for him. For Rowan, this entire project would be a considerable drain on the castle’s iron reserves. But if compared to the raids, it was a much more reliable way of boosting Batri’s powerbase."
"What package should he send him then?"

label ghBatriHelpMenu:

menu:
    "Small package." if castle.iron_per_week > 2:
        $ released_fix_rollback()
        $ castle._iron -= 3
        $ batri_power += 1
        jump ghBatriConclusion

    "Medium package." if castle.iron_per_week > 5:
        $ released_fix_rollback()
        $ castle._iron -= 6
        $ batri_power += 2
        jump ghBatriConclusion
        
    "Large package." if castle.iron_per_week > 8:
        $ released_fix_rollback()
        $ castle._iron -= 9
        $ batri_power += 3
        jump ghBatriConclusion
        
    "Full package." if castle.iron_per_week > 11:
        $ released_fix_rollback()
        $ castle._iron -= 12
        $ batri_power += 4
        jump ghBatriConclusion
        
    "Decide later.":
        $ released_fix_rollback()
        $ ghBatriLater = True
        gh "Alright, once you make up your mind, you know where to find me."
        return

label ghBatriConclusion:

gh "Very well, I’ll see that it’s done."
gh "Give me the camp location, I’ll tell the orcs to bring the package over once it’s ready for delivery."

show rowan necklace happy at midleft with dissolve

ro "How often do I tell you’re a joy to work with Greyhide?"

gh "Not often enough."

$ ghBatriHelp = "got"
$ journal.complete_quest_note('orciad', 'note9')

return


###########################################################################
###########################################################################
###########################################################################

label jezeraDelaneHelp:

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan didn’t exactly like asking the twins for help."

if serveChoice == 4:
    "A foolish sentiment, perhaps. They were in this battle together, and only by supporting one another would victory be assured."
    "It would be nice if the twins finally acknowledged that. They were a nuisance as often as they were of help to him."

else:
    "He was held captive, chained with a cursed amulet and forced to commit countless atrocities in order to protect himself and his wife."
    "Asking his torments for favors felt... Wrong."

"However, he had to acknowledge that when it came to finding gifts for a noblewoman there was but one expert in the whole castle he could rely on."
"And he was now knocking on her doors."

show jezera neutral behind bg14

je "Enter!"

scene bg18 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with moveinright

"For once, she was fully clothed, and she seemed to be in a good mod. Praise the Goddess."

je "Rowan, my hero! What brings you to my chambers? "

show rowan necklace happy at midleft with dissolve

ro "Mistress Jezera. I have a favor to ask of you."

je "Oh? Now that’s new. Do tell."

show rowan necklace neutral at midleft with dissolve

ro "Are you familiar with the orc camp in the northern regions of Rosaria?"

je "The one locked in a duel over some minor noblewoman? Yes, Andras filled me in."

ro " I managed to gain the favor of one of the warchiefs, Ulcro. But he won’t join us unless I provide him with suitable gifts for Delane- the noblewoman, I mean."

show rowan necklace happy at midleft with dissolve

ro "So I was wondering if you have any jewelry you would be willing to part with. Some things you are no longer fond of, perhaps?"

if (all_actors['jezera'].favors + all_actors['andras'].favors) < 3:
    show jezera neutral at midright with dissolve
    je "Oh, Rowan I’m not sure how to tell you this."
    je "I talked with Andras about it earlier, and…"
    je " He believes either Batri or Tarish would make for better leaders. Ulcro is, and I quote here, “A coward and delusional fool.”"
    show rowan necklace angry at midleft with dissolve
    je "I fear my hands are tied. Everything relating to orcs is his responsibility."
    ro "Is that so?"
    show jezera happy at midright with dissolve
    "Jezera sent him an innocent smile. Now he was sure she was messing with him."
    show rowan necklace neutral at midleft with dissolve
    "But there was no way he could pressure her into helping. He hadn't been playing nice with them either."
    ro "… I’ll reconsider my position then. I apologize for taking your time, Mistress."
    je "Oh no, I apologize for not being of any use. After taking the time to visit me..."
    je "You know... Maybe I could dig something up. But I wouldn't want to encroach on my brother's territory."
    show rowan necklace angry at midleft with dissolve
    je "But If I were to tell him you literally begged me for help, I am sure he would be more understanding of my actions."

    menu:
        "Beg for help.":
            $ released_fix_rollback()
            show rowan necklace neutral at midleft with dissolve
            ro "..."
            je "So? What will it be?"
            je "Will you crawl at my feet, just to get a couple of old trinkets, or will you leave empty-handed?"
            "In a true display of heroic willpower, Rowan stopped himself from visibly scowling."
            "Compared to Batri and Tarish, Ulcro was the lesser evil. If he had to humiliate himself to ensure his support..."
            "Then so be it."
            hide rowan
            show rowan necklace neutral behind bg18
            show jezera happy at center with moveinright
            "With some hesitation, Rowan knelt before Jezera. The half-demoness grinned from ear to ear, basking in his submission."
            ro "Please... Mistress Jezera..."
            ro "I really need those gifts..."
            "Gritting his teeth, he pressed his forehead to the cold floor."
            "... Something tapped his head gently."
            "He raised his head slightly. Jezera's black boot was right before his eyes."
            je "Kiss it."
            
            menu:
                "Do it.":
                    $ released_fix_rollback()
                    "Trying not to think about his own actions, Rowan leaned in, pressing his mouth against the black leather."
                    "Jezera was almost giddy with excitement, and she actually knelt before him, so she could pat him on the head in a condescending manner."
                    je "Oh Rowan, if only you did as you were told when in the field."
                    je "I'd love to take this a step further, but I fear other responsibilities call us both."
                    je "But I do hope this small display heralds a change in your behavior."
                    "She ran her fingers through his hair. Rowan kept his eyes down."
                    je "You will find servility... Rewarding."
                    "She rose up abruptly."
                    je "I will get you the jewelry."
                    je "Consider yourself dismissed."
                    jump jezDelaneLarge
                    
                "Don't.":
                   $ released_fix_rollback() 
                   "Rowan couldn't force himself to do it."
                   je "Aww... And you were doing so well!"
                   je "But I will recognize the effort."
                   je "I will get you your jewelry, but I hope you will rethink your behavior from now on."
                   je "Think will be so much easier for you if you just do as you are told."
                   "Still on his knees, Rowan said nothing."
                   je "Consider yourself dismissed, Rowan."
                   jump jezDelaneSmall
                   
        "You'll manage.":
            $ released_fix_rollback()
            ro "I wouldn't want to drive a wedge between you and your brother. I'll think of something."
            je "Of course. You are nothing if not resourceful."
            ro "That's why I'm here."
            "Rowan bowed his head stiffly and headed out, holding in his anger."
            $ jezDelaneHelp = "got"
            return
            
else:
    je "Hmm…"
    je "I might have something laying around. Give me some time to look things over."
    ro "Of course, Mistress."
    "Promising. He’ll see what Jezera was willing to part with."
    


if (all_actors['jezera'].favors + all_actors['andras'].favors) < 5:
    label jezDelaneSmall:
    scene bg9 with fade
    "In the evening, he found a small case in his room." 
    "Rings, bracelets, necklaces. Nothing too fancy, but fine gifts nevertheless."
    $ delane_gifts +=10
    $ jezDelaneHelp = "got"
    $ journal.complete_quest_note('orciad', 'note18')
    return
    
else:
    label jezDelaneLarge:
    scene bg9 with fade
    "In the evening, he found a small, open box in his room."
    "Rings, bracelets, necklaces, books, poems…"
    "Fresh, comfortable underwear?"
    "Now that he thought of it, Delane probably could use some..."
    "Surprisingly considerate of Jezera. Delane will be pleased with it."
    $ delane_gifts +=20
    $ jezDelaneHelp = "got"
    $ journal.complete_quest_note('orciad', 'note18')
    return    

###########################################################################
###########################################################################
###########################################################################

label cliohnaDelaneHelp:

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve

ro "Cliohna, do you have a moment?"

show cliohna neutral at cliohnaright with dissolve

"The sorceress looked away from her books and narrowed her eyes, obviously displeased at being interrupted."

cl "A short one."

ro "I need some books that could be of interest to a noblewoman. Do you have anything that fits the profile, that you might be willing to part with?"

if castle.researches['history_of_rosaria'].completed:
    cl "Yes. My assistant will point you towards nonessential tomes. Take as many as you need."

    ro "Excellent."

    hide rowan
    hide cliohna

    "Having already studied and cataloged all of them, it was easy to pick some of the more interesting books for Delane."
    "She should be quite pleased with them."

    $ delane_gifts +=15
    $ cliohnaDelaneHelp = "got"
    return

elif castle._current_research == 'history_of_rosaria':
    
    cl "As you know, I am currently studying the tomes pertaining to Rosaria nobility."
    cl "I will determine what is nonessential to my research, and have it delivered to your room by the end of the week."
    ro "Ah, excellent."

    hide rowan
    hide cliohna

    "Rowan doubted anything in Cliohna's library would prove to be particularly interesting, but even boring books will help Delane pass the time."

    $ delane_gifts +=10
    $ cliohnaDelaneHelp = "got"
    return

else:
    cl "I have yet to study the tomes pertaining to Rosaria nobility."
    cl "But I will have to do so at some point anyway, so if you want to, I can spend the next week sifting through them. Find some that will be of no use to us."

    show rowan necklace concerned at midleft with dissolve

    ro "But it will take you away from your current research."

    cl "Precisely."

    show rowan necklace neutral at midleft with dissolve

    ro "Hm…"

    "Should he tell Cliohna to look through the tomes?"

    menu:
        "Yes.":
            $ released_fix_rollback()
            ro "Do so. Have the books delivered to my room by the end of next week."
            cl "Very well."
            hide rowan
            hide cliohna
            "Rowan doubted anything in Cliohna's library would prove to be particularly interesting, but even boring books will help Delane pass the time."
            $ castle.rp -= 10
            $ delane_gifts +=10
            $ cliohnaDelaneHelp = "got"
            $ journal.complete_quest_note('orciad', 'note17')
            return

        "No.":
            $ released_fix_rollback()
            ro "No. I need you focused on the task at hand."
            cl "Very well."
            "Cliohna's research was too important, he'd have to find another way to gather the gifts he needed to persuade Delane to choose Ulcro."
            $ cliohnaDelaneHelp = "got"
            return

###########################################################################
###########################################################################
###########################################################################

label shaya_Show:

scene bg24 with fade
show rowan necklace neutral at midleft with dissolve
show shaya neutral at midright with dissolve

"Rowan decided to take a break from work and check out a show that Shaya was putting on in the brothel. One of the most important responsibilities of Shaya and the other whores at the brothel was keeping the mercenaries entertained."
"Besides, she had asked him to come down at some point."
"He took a seat near the back next to a large orc who was paying slightly more attention to the dancing human then would be socially acceptable in any other circumstance."
"Rowan could not see Shaya’s mouth behind her veil, but her eyes locked onto his a moment after he took a seat. He had to imagine she was smiling underneath."
"The dance she was engaging in was certainly provocative. She rolled her hips and belly to the sound of a drums. Her bosom shook, and with it the little bells sewn into her scant clothing. It all emphasized the shaking and rolling of her body."
"She was confident and expressive. Throwing little winks into the audience and throwing herself into provocative positions that made one want just a little bit more. It was a teasing game, one that felt strangely at odds with her demeanor about the castle."
"But, the dance was just a warm up. Rowan’s lips parted softly when he saw her draw out a large black onyx prop and place it on the ground. It was nearly two feet tall and jutted out of the center of the stage. No one could miss how it was shaped. It looked like a cock."

if shayaShowFirst == True:
    "Was this too a traditional dance of Qerazel? With the rumors about the place that filtered back to Rosaria, Rowan wouldn’t doubt it."
    
else:
    pass
    
#shaya dance CG
scene cg219 with fade
pause 3

"A cheer roared out amongst the crowd. Shaya lowered herself into a squat behind the onyx cock and rubbed her crotch from base to head, in a rhythmic motion, steadying herself with her right hand."

show cg220 with dissolve
pause 2

"It was a dance, and the cock was her partner. She shifted position, dancing around it. At one point leaning over so the entire audience could stare down her top while rubbing her behind against the fake cock’s surface."

show cg221 with dissolve
pause 2

"This posture, positioned as if she was being taken from behind, was the one she settled into. What followed was the most provocative display of all. She rolled her hips up and down and even let out a long low moan."

show cg222 with dissolve
pause 2

"At first it was slow, She rolled her head in a circle and faked a long moan. But, as she went the dance became more frantic, almost leaping in place."
"She concluded the dance by jumping, a simulation of an orgasmic spasm, and spinning in a circle to wrap her arms around the prop. When she came to a stop, it was with her arms wrapped around her onyx co-performer and body pressed to it like a lover."

show cg223 with dissolve
pause 1
show cg224 with dissolve
pause 3

scene bg24 with fade
show rowan necklace aroused at midleft with dissolve
show shaya happy at midright with dissolve

"When the music came to a halt, a cheer went through the crowd. How could they not love a performance like that? Roman himself could attest to its effectiveness."

if shayaShowFirst == True:
    "This Shaya he’d never seen before, this vixen on stage, let out an appreciative purr. She basked in the attention of the crowd. "
    
else:
    pass

"But, Rowan didn’t bother to approach the stage or try to talk to her. Shaya was working. As soon as the performance was done, men were calling out from the seats asking to be first in line. Shaya walked into the crowd and threw herself into the arms of a hungry looking mercenary."
"Rowan stood up and made for the exit. But, even as he did, he looked back at Shaya in the moment before she disappeared into the silks of the back rooms. She was eyeing him as well. Once more he could only suppose she was smiling."

$ shayaShowFirst = False
return


