init python:

    #What happened after drinking Greyhide's alcohol?
    #Greyhide's third relationship event, following either table manners or sharing people's liquor.  Likely a mission three minimum event.  Requires NTR to be turned on and that Rowan and Alexia be pure.
    event('after_drinking_greyhides_alchol', triggers="week_end",
        conditions=('NTR', 'ev_happened("greyhide_s_table_manners") or ev_happened("greyhide_shares_his_people_s_liquor")', 'avatar.corruption < 20', 'all_actors["alexia"].corruption < 20'),
        depends=('raeve_keep_visit_goal2',), group='ruler_event', run_count=1, priority=pr_ruler)


label after_drinking_greyhides_alchol:
#What happened after drinking Greyhide's alcohol?
#Greyhide's third relationship event, following either table manners or sharing people's liquor.  Likely a mission three minimum event.  Requires NTR to be turned on and that Rowan and Alexia be pure.

scene bg9 with fade
show rowan necklace neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with dissolve

ro "Alexia, please. We need to talk to him, both of us."

al "I know, I know, but..."

ro "We can hardly put it off indefinitely. Before what happened Greyhide was one of my friends among the staff.  I can't afford to let this drive a wedge between us, nor do I want to hurt him personally."

#If Alexia was the one to have sex with Greyhide
if alexia_greyhide_sex > 0:
    al "I still can hardly believe what you said I did with him. I promise I would never have done anything of the sort if I was truly myself."
    ro "I appreciate and understand that, but you're stalling again Alexia."

#Else, Rowan was the one to have sex with Greyhide
elif rowan_greyhide_sex:
    al "I haven't seen the two of you together since... what happened. How could my husband transform so much from one drink?"
    ro "I hardly can believe it myself, but it would hardly have been the only thing I couldn't remember doing while in service to our masters. However, you're stalling again Alexia."

#rejoin
"The woman let out a sigh, then square her shoulders."

al "Alright, let's go."

scene bg22 with fade
show rowan necklace neutral at center with dissolve
show alexia 2 necklace neutral at midleft with dissolve
show greyhide neutral at edgeright with dissolve

"An awkward silence pervade the room. Everyone had said their greetings, sat down, and then stopped.  Rowan cleared his throat slightly as a servant brought in a tea tray and placed it on the bench before the trio."
"Wordlessly he poured three cups from the pot then bowed and stepped back out of the room. Once again the man realized he was being distracted and tried to focus, finally breaking the silence."

ro "Well, I was hoping we could maybe talk about what happened between us. May as well cut straight to the point seeing as how we can't think of much else to talk about."

"Idly he and Alexia picked up cups for themselves and blew on the hot liquid."

gh "If you want to."

"Evidently thinking the teapot was intended for him, Greyhide picked that up between two large fingers instead of the remaining cup."

ro "I thought that there was probably something wrong with your firegrout, minotaurs don't usually get horny after drinking it, right?"

gh "No, we often have great difficulties in becoming hard enough if drunk."

al "Which wasn't the case with what happened."

gh "We only had one each, did we not?  Far too little to have that issue for myself. Normally I am not that out of sorts as I recall being either."

ro "Right, so there must have been something wrong with the drink. Did you get it from Cla-Min? Maybe she was using tainted goods."

gh "No, I made the drinks myself and can assure you the roots were good."

"Alexia let out a sigh of frustration."

al "Really? You picked it and prepared it yourself? Damn, I thought we were onto something there. Rowan suggested that-"

gh "Wait, I did not collect the roots. They can only be found in the Dragon's Tail and I have not left my forge. The mistress was kind enough to get them for me."

"The two humans exchanged a glance, then said a name together."

al "Jezera."

ro "So, my hunch may prove right after all."

"He relaxed a bit, finally letting some tension slip out of him and sipped the tea in the cup."

ro "Hmm, this is good. Thanks for asking for tea Alexia."

al "Wait, I thought you'd asked for tea Rowan?"

"The two of them looked at the minotaur for a second as he poured tea into his mouth directly from the pot, then a feeling of anger rose up in Rowan's chest and he grabbed at his amulet to commune with his mistress."

ro "Jezera! Are you watching us?"

show jezera happy at edgeleft with moveinleft

je "Oh dear, what gave it away?"

"The demoness seemed to just materialize out of the walls, much to the shock of everyone at the table. After surveying their expressions with a smirk her expression shifted to surprise and then admonishment."

je "Hmph, guess I just exposed my own hand. Oh well, are you three going to fuck soon for me?"

al "What? Why would we ever do that?"

"But even as Alexia spoke Rowan could feel the first twinges of arousal filling him. He spared a glance at the tea tray and then at both his and Alexia's cups. They had drunk Jezera's potion yet again."

je "Because it is such a fine spectacle! Come on, get those stifling clothes off and have some fun. Simply don't mind me, I will be well out of your way."

scene black with fade

"The woman seemed to melt back into the shadows as a loud clatter announced Greyhide's cuirass had struck the floor. A deep blush was showing through his cheeks as he eyed both Rowan and Alexia."

menu:
    "Both succumb to your lusts.":
        $ released_fix_rollback()
        jump .greyhideThreesome

    "Pull yourself together and resist Jezera's foul magic.":
        $ released_fix_rollback()
        "A rumbling growl escaped from Greyhide's maw as he leapt up over the table. Rowan dove to the side, catching Alexia in his arms and dragging her out of the bull's path."
        show rowan necklace neutral behind black
        ro "Alexia, come on!"
        "The two quickly ran out of the room, evading their lust addled friend."
        scene bg14 with fade
        show rowan necklace neutral at midright with dissolve
        show alexia 2 necklace neutral at midleft with dissolve
        al "Did we lose him?"
        ro "I think he stopped to take care of his problem himself a little ways back."
        show jezera neutral at edgeleft with moveinleft
        je "You two should be ashamed of yourselves! Greyhide is in such a state, he needs a friend or two to help him out."
        jump .greyhideAftermath

#####################################################################################################

label .greyhideThreesome:

"That gaze made Rowan notice just how much he'd also been affected by the tea. A glance at Alexia confirmed her own state was no better, and her somewhat loosened dress didn't help her husband keep his erection down."
"A grumbling roar erupted from Greyhide and he jumped clean over the bench they were having a calm discussion a moment before and he scooped up both the humans in each hand. Neither made any attempt to stop him or escape as he carried them to his bed."

#If Rowan had sex with Greyhide previously, then his turn comes first.  Otherwise Alexia is first.
$ event_tmp['rowans_turn'] = False
$ event_tmp['alexia_turn'] = False
$ event_tmp['threesome'] = False

if rowan_greyhide_sex > 0:
    jump .rowans_turn
else:
    jump .alexias_turn

#####################################################################################################

label .rowans_turn:
#Rowan's turn
$ rowanGaySex += 1
#CG of Rowan being hotdogged by Greyhide, Alexia watches and masterbates.
scene cg154 with fade
pause 3

"Greyhide threw Rowan onto the bed and tore his pants free, exposing his ass. The minotaur then wasted no time in gripping the much smaller figure's hips and rubbing his cock over the man's ass."
"Grunts and rubblings of animal pleasure rang out as the beast used Rowan to satisfy his lusts. Every moment the man thought that maybe he'd be impaled, a part of him anticipated it, however that never came."

#if Alexia's turn has happened
if event_tmp['alexia_turn']:
    "Like with Alexia, and in spite of already having cum once, there only seemed to be an interest in cumming by hotdogging the both of them. Perhaps Greyhide decided it wasn't worth trying to get inside either of them or perhaps some part of him still didn't want to hurt them."

#rejoin
"There was simply the thrusting onto his ass, sawing back and forth again and again. The pace never let up, the treatment never changed. Rowan spared a glance to the side and saw his wife watching, a somewhat glazed look on her smiling face while she touched herself."

show cg154 with sshake
show cg154 with sshake
show cg155 with flash
pause 3

"Then a blast of warm fluid sprayed over Rowan's back and head, filling the room with the musty smell of minotaur cum. However, if this was any indication of a reprieve of this hot animalistic sex, it was very short lived."

#Note Rowan's turn has happened.
$ event_tmp['rowans_turn'] = True
#If Alexia's turn has happened, go to both together.  Otherwise go to Alexia's turn.
if event_tmp['alexia_turn']:
    jump .both_together
else:
    menu:
        "Now it was Alexia's turn.":
            $ released_fix_rollback() 
            jump .alexias_turn
            
        "Greyhide looked for Alexia, but she'd slipped away.":
            $ released_fix_rollback()
            "Finding no other receptacle for his lusts, the minotaur simply kept going at Rowan, rubbing out another one before collapsing in a heap."
            scene bg14 with fade
            show rowan necklace neutral at midright with dissolve
            show alexia 2 necklace neutral at midleft with dissolve
            "Around half an hour later, Rowan and Alexia met back up outside the forge.."
            ro "Well, that was something."
            al "That's one way of putting it. I can't believe I just saw that happen to you."
            show jezera neutral at edgeleft with moveinleft
            je "Weren't you even a little tempted to let Greyhide have his way with you too Alexia?"
            jump .greyhideAftermath
            

#####################################################################################################

label .alexias_turn:
#Alexia's turn

#CG of Alexia being hotdogged by Greyhide, Rowan watches and masturbates.
scene cg156 with fade
pause 3

"Alexia was flipped onto the bed and hiked up her skirt.  Then he put a finger into her undergarments and tore them open to expose her womanhood. However, he wasn't interested in that."
"He growled as he fucked Alexia's buttocks, pumping his great length through her firm cheeks and pressing her down against the bed.  Each moment, Rowan feared that he would try and force himself inside, to split his wife open. It didn't happen."

#if Rowans turn has happened
if event_tmp['rowans_turn']:
    "Like with Rowan, and in spite of already having cum once, there only seemed to be an interest in cumming by hotdogging the both of them. Perhaps Greyhide decided it wasn't worth trying to get inside either of them or perhaps some part of him still didn't want to hurt them."

#rejoin
"Apparently her body was enough, her soft figure and pretty features, rubbing himself all over them was what the minotaur wanted. Alexia even seemed to be enjoying it, as she laughed and cried out excitedly as the treatment went on."

show cg156 with sshake
show cg156 with sshake
show cg157 with flash
pause 3

"To his own surprise, Rowan realized he was touching himself as he watched. An idle thought that he should stop flitted through his mind, but that disappeared under a haze of lust soon afterwards as a wave of spunk splashed over his wife."

#Note Alexia's turn has happened.
$ event_tmp['alexia_turn'] = True
#If Rowan's turn has happened, go to both together.  Otherwise go to Alexia's turn.
if event_tmp['rowans_turn']:
    jump .both_together
else:
    menu:
        "Now it was Rowan's turn.":
            $ released_fix_rollback() 
            jump .rowans_turn
            
        "Greyhide looked for Rowan, but he'd slipped away.":
            $ released_fix_rollback()
            "Finding no other receptacle for his lusts, the minotaur simply kept going at Alexia, rubbing out another one before collapsing in a heap."
            scene bg14 with fade
            show rowan necklace neutral at midright with dissolve
            show alexia 2 necklace neutral at midleft with dissolve
            "Around half an hour later, Rowan and Alexia met back up outside the forge.."
            ro "Are you alright?  I tried to help but...."
            al "Don't blame yourself, just help me get upstairs, I need a bath."
            show jezera neutral at edgeleft with moveinleft
            je "But you look so cute covered in minotaur cum.  Rowan you should really try it!"
            jump .greyhideAftermath


#####################################################################################################

label .both_together:
#both together

scene cg164 with fade
pause 3

"Now that he'd rubbed one out on both of them, Greyhide's energy finally seemed to be running out. He collapsed back onto the bed with and panted with effort. Great streams of sweat ran down his features. Yet his cock remained erect, veins pumping angrilly."
"Rowan reached out to put a hand on that shaft, only to find Alexia's moving to do the same. Together they brought their hands on the minotaur and stroked his need while settling onto the minotaur's lap."
"A groan of appreciation escaped from Greyhide's lips. He certainly still needed help, but didn't have the energy to do anything anymore. Whatever had been in that teapot, it had been strong stuff and he'd gotten an extra large dose."
"The two of them met eyes and grinned, then leaned together and kissed. Bonding over a minotaur cock was not something a human couple would normally do, though being under a demon's spell certainly made a lot of unusual things happen."

scene bg14 with fade
show rowan necklace neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with dissolve

"Around half an hour later."

ro "Well, that was something."

al "That's one way of putting it. Ugh, I need a bath."

show jezera neutral at edgeleft with moveinleft

je "Don't be ridiculous, you both look great covered in minotaur cum!"

#Note that threesome happened
$ event_tmp['threesome'] = True
$ ghThreesome = True
jump .greyhideAftermath

#####################################################################################################

label .greyhideAftermath:

menu:
    "Rowan and Alexia were furious at what Jezera had done to them.":
        $ released_fix_rollback()
        show rowan necklace angry at midright with dissolve
        show alexia 2 necklace angry at midleft with dissolve
        al "This was your fault!"
        ro "Exactly, what the hell are you trying to do to with us and our friends?"
        show jezera happy at edgeleft with dissolve
        je "You should be thanking me, I helped that friendship blossom into something so much greater!"
        al "With drugs and foul magics, that's hardly something good."
        ro "If we want to tumble with someone, that's our business."
        show jezera displeased at edgeleft with dissolve
        je "Uh, no it isn't. You are my servants, you will do as I want, and you certainly will not mouth off to me when you get your knickers in a twist."
        "She shot them one last glare, to which they responded with silence. Then Jezera turned and stomped off with an indignant huff."
        hide jezera with moveoutleft
        show jezera displeased behind bg14
        je "Ungrateful shits."
        #Lose favor with Jezera, Rowan gains influence with Alexia.
        $ change_favor('jezera', -1)
        $ change_relation('alexia', 3)
        show alexia 2 necklace neutral at midleft with dissolve


    "Avoid a confrontation with Jezera.":
        $ released_fix_rollback()
        show alexia 2 necklace angry at midleft with dissolve
        "Alexia opened her mouth, but hesitated when her husband put his hand on her arm. A look silenced her."
        "Jezera glanced back and forth at them with a curious look."
        je "Is there something you wished to say? Perhaps a thank you for a little breaking of routine?"
        ro "No mistress."
        je "Hmph, fine then. I suppose I shall see you around the castle."
        hide jezera with moveoutleft
        "The demoness looked a little disappointed, but decided against saying anything else and walked away."
        #Jezera gains a little influence on Alexia.
        $ change_actor_num_flag('alexia', 'jezera_influence', 3)
        show alexia 2 necklace neutral at midleft with dissolve


    #requires that threesome sex happened
    "They admit that they enjoyed what happened." if event_tmp['threesome']:
        $ released_fix_rollback()
        "The couple exchanged a nervous glance, which Jezera caught immediately and her smile grew an extra inch."
        show jezera happy at edgeleft with dissolve
        je "Ohoho, looks like I might have set you two up for something special. Admit it, you enjoyed our minotaur friend."
        "There wasn't exactly much point in hiding it."
        ro "Yes, mistress."
        al "I won't say that I look good covered in cum though."
        je "Oh, but the two of your are still making good progress. I think that you won't need my help from now on with Greyhide, but please send a message so I can watch next time you're planning on having some fun."
        "She mimed signalling her with the amulets, then turned with a wave over her shoulder."
        hide jezera with moveoutleft
        show jezera happy behind bg14
        je "Thank you for the show, ta darlings!"
        #Gain favor with Jezera, Jezera gains influence on Alexia, Rowan and Alexia gain a little corruption
        $ change_favor('jezera', 1)
        $ change_base_stat('c', 2)
        $ change_actor_num_flag('alexia', 'jezera_influence', 3)
        $ change_corruption_actor('alexia', 2)

"Rowan let out a long breath as the demoness turned the corner and went out of sight. Noticing Alexia was looking at him, he tried his best at a reassuring smile."

show rowan necklace happy at midright with dissolve

al "Rowan? What's going to happen between us and Greyhide?"

menu:
    "Pretend this never happened. Nothing more with Greyhide.":
        $ released_fix_rollback()
        ro "We should probably try and put this behind us. These lusts were forced on us by Jezera, we can safely say that that none of this would have happened if it weren't for her."
        "Now it was Alexia's turn to let out a long sigh of relief."

        #If table manners event was triggered
        if ev_happened("greyhide_s_table_manners"):
            al "Darling, it is so good to hear you say that. I was afraid you thought I truly lusted for Greyhide after how I behaved that night."

        #Else, people's drink event was triggered
        else:
            al "Darling, it is so good to hear you say that. I was afraid you truly lusted for Greyhide after how you behaved that night."

        #rejoin
        ro "I'll try and patch things up with my friend soon. I think he'll understand how we both feel."
        #Further sex scenes with Greyhide will not happen
        $ further_sex_scenes_with_greyhide = False
        return further_sex_scenes_with_greyhide

    "Now we have a chance to pursue a relationship on our own terms.":
        $ released_fix_rollback()
        ro "It's okay Alexia, I realize that it wasn't just Jezera's potion that lead to what happened. I find him attractive too, in a way."
        "Now it was Alexia's turn to let out a long sigh of relief, though a look of guilt lingered on her features."
        al "Rowan, if you don't think I should-"
        ro "Shh. I don't mind if you want to pursue a relationship with Greyhide if you do the same for me. I think we're past the initial shock. He's a good person."
        al "He is. But I still worry that-"
        "Once more Rowan cut her off, this time with a kiss."
        ro "No matter what happens, I love you first in my heart."
        #Further sex scenes are possible with Greyhide, probably repeat scenes can be unlocked right away.
        $ further_sex_scenes_with_greyhide = True
        return

    #requires that threesome sex happened
    "Being so lust filled was surprisingly enjoyable, especially with Greyhide." if event_tmp['threesome']:
        $ released_fix_rollback()
        ro "You felt the same way, didn't you? The rush, the lust."
        al "Yeah, and with a beast as great as Greyhide."
        ro "A part of me hates Jezera for forcing this on us and our friend, but..."
        "Alexia let out a long sigh and smiled almost in defeat to her husband."
        show alexia 2 necklace happy at midleft with dissolve
        al "She has her claws in us. How long will we last at this rate?"
        ro "At least we found someone special that we can enjoy our time with."
        al "That we have. Greyhide is a light point in this. He asked to join us together, well let's at least invite him under the covers next time."
        ro "Agreed."
        #Rowan and Alexia gain corruption.  Jezera gains influence on Alexia.  Further sex scenes are possible with Greyhide, probably repeat scenes can be unlocked right away
        $ further_sex_scenes_with_greyhide = True
        $ change_base_stat('c', 2)
        $ change_actor_num_flag('alexia', 'jezera_influence', 3)
        $ change_corruption_actor('alexia', 2)
        return

