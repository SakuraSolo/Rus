init python:

    #Alexia visits with Cla-Min
    event('alexia_visits_with_cla_min', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #X'zaratl's Guilt Solution
    #Requires Dark Sanctum built, Guilt higher than x (to do),  'X'zaratl's advances' event already triggered
    event('xzaratl_guilt_solution', triggers="week_end", conditions=('week >=4',
        "castle.buildings['sanctum'].lvl >= 1", 'avatar.guilt > 10'), depends=('xzaratl_s_advances',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Andras' Challenge
    #Requires: Arena built, at least 15 orcs
    event('andras_chanllenge', triggers="week_end", conditions=('week >=4', "castle.buildings['arena'].lvl >= 1", "castle.buildings['barracks'].troops >= 15"), group='ruler_event', run_count=1, priority=pr_ruler)
    #Orc Deserters
    #Low morale event. Requires at least 15 orcs
    event('orc_deserters', triggers="week_end", conditions=('week >=4', "castle.buildings['barracks'].troops >= 15", 'castle.morale < 20'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Alexia visits with Skordred
    #No requirements, but will appear at some point during the second mission in the NPC slot eventually.
    # TODO NPC slot
    # TODO check for real goal2 being active
    event('alexia_visits_with_skordred', triggers="week_end", conditions=('week >=4', 'not goal2_completed'), depends=('first_village_captured',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Rowan is feeling guilty
    #Requires Rowan have enough guilt to trigger low guilt after decay.  High priority event.  Note that conquering Raeve Keep should give enough guilt on its own to trigger this event.
    event('rowan_is_feeling_guilty', triggers="week_end", conditions=('week >=4', 'avatar.guilt > 15'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Disease outbreak
    #Req at least 10 soldiers.
    event('disease_outbreak', triggers="week_end", conditions=('week >=4', "castle.buildings['barracks'].troops >= 10"), group='ruler_event', run_count=1, priority=pr_ruler)
    #Pure morning with Alexia
    #Requires Rowan and Alexia be sharing a room and that Alexia be pure.
    event('pure_morning_with_alexia', triggers="week_end", conditions=('week >=4', "not alexiaSeparateRoom", "all_actors['alexia'].corruption < 5"), group='ruler_event', run_count=1, priority=pr_ruler)
    #Jezera's alliance making skills
    #Requires after week sixteen, high priority event after week eighteen.
    event('jezera_s_alliance_making_skills', triggers="week_end", conditions=('week >=16',), only=True, group='ruler_event', run_count=1, priority='pr_ruler_high if week > 18 else pr_ruler')
    #Drinking buddies
    #Can trigger three weeks after the forge is built.  Requires that the tavern exist. (Activated in "forge_purchased")
    event('drinking_buddies', triggers="week_end", conditions=('week >=4', "castle.buildings['tavern'].lvl >= 1"), active=False,
        group='ruler_event', run_count=1, priority=pr_ruler)


label alexia_visits_with_cla_min:
#Alexia visits with Cla-Min

scene bg14 with fade
show clamin neutral pipe at midright with dissolve
show alexia 2 necklace happy at midleft with moveinleft

al "Good afternoon Cla-Min. I saw you'd stepped away from work and was hoping to catch a word with you."

cla "Alexia."

"The goblin woman tapped out her pipe and looked passed the woman for a moment at her family bringing in supplies from the portal chamber.  She sighed, then stowed the pipe."

show clamin neutral at midright with dissolve

cla "Yes, I suppose I can spare a minute. I don't suppose you're looking to offload some money you stumbled on?"

al "Uh, no."

cla "Pity. Alright, what is it?"

show alexia 2 necklace neutral at midleft with dissolve

al "You and your family aren't like most of the people here in the castle. Goblin caravans aren't really Karnas supporters, regardless of what rumors often say. What brought you to this castle? Was it the promise of Jezera's portals?"

show clamin happy at midright with dissolve

cla "I'm afraid that information doesn't come free, at least not for you. One good turn deserves another, if you catch my drift."

al "Are you asking for information or a favor?"

cla "A favor, just a small thing, I assure you."

al "I can't do much for you, but alright."

cla "Wonderful! Then I'd be happy to tell you a bit about my history with the twins."

show clamin neutral at midright with dissolve

cla " It was by chance we joined the twins, but probably not when you suspect. My caravan met up with them on the road before they'd taken up residence in this castle. They needed to bring people and supplies across the wastes, we needed their coin."

al "How long ago was that?"

cla "About two and a half years."

al "What were the twins like back then?"

cla "Less entitled, but we didn't talk much since I kept me and mine away from them. A good mother doesn't let demons mess with her family."

al "So why did you take the job if you didn't trust them?"

cla "Jobs like that are few and far between for goblins, so we usually take what we can get. That said, after the third trip over the wastes for more stuff, I was thinking it was time to call it quits. After all, I have to look out for my family and endless barrans are no place to raise children."
cla "However, it was then that things changed, as Jezera told me she'd managed to get that portal open and was in the process of opening up other gates around the whole of the Six Realms!"

"The goblin tapped a finger to her nose knowingly."

cla "Now I could see the way the wind was blowing if these two could go anywhere in the world at any time. If we agreed, gone would be the days of runs through dirt and sand, now we could go see woods, plains, or the sea whenever we wanted!"
cla "Even if the twin's plans don't pan out, this job has probably already made Cla the richest goblin caravan in the world and since things just keep getting better here, I have every intention of sticking around until the town bells are ringing."

al "Thank you very much for the story."

cla "If you're truly grateful, then I'll ask one simple thing of you."

al "Certainly."

cla "Don't get too fussed up if I or someone from my family makes a move on your husband. Thanks darling."

hide clamin with moveoutright

"Alexia was left speechless as the goblin matriarch headed off to rejoin the rest of her family who'd just finished unloading supplies. By the time she collected herself and followed after Cla-Min, they'd all left back through the portal."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label xzaratl_guilt_solution:
#X'zaratl's Guilt Solution
#Requires Dark Sanctum built, Guilt higher than x (to do),  'X'zaratl's advances' event already triggered

$ released_block_rollback()
scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show xzaratl neutral behind bg14

xz "Oh, Rowan..."

"The succubi's teasing, lilting voice echoed down the corridor, each syllable seeming to trail off into a disarming, intimate whisper."

#if fucked
if xzaratl_s_advances_rowan_sex:
    "Rowan tensed, his thoughts helplessly turning back to the unspeakable pleasures the creature subjected him and his wife to last time it caught them alone."

#else
else:
    "Rowan tensed, what new tricks was the creature going to try out on him this time?"

#remerge
ro "What do you want?"

#if fucked and R has high corruption # skipped corruption check because of subchecks for corruption
if xzaratl_s_advances_rowan_sex:

    xz "To make you happy. You and your delightful wife. Didn't I make you happy last time? Wasn't it so good for you, once you abandoned your frigidity and etiquette and allowed me to open up a few new vistas of ecstasy to you?"

    #if R has high corruption
    if avatar.corruption > 15:
        ro "Yes... it was wonderful."

        hide xzaratl
        show xzaratl neutral at cliohnaright with dissolve

        "X'zaratl appeared in front of him, a voluptuous blooming of flawless flesh out of thin air."

        xz "And yet... I can sense you still aren't truly happy. I can taste your thoughts, bitter and fibrous with the regret that war inevitably brings."
        xz "They will poison you in time, those thoughts; they will line that handsome face of yours and make you do unhappy things, blackening and burying the pleasure that would otherwise be yours to savour."

        ro "What are you getting at?"

        xz "I can alleviate those thoughts. In a most delicious, delightful way. It will involve you, your wife... Let me show you something new."

        #go to alright / no menu
#~         jump .alright_no_menu

    #else
    elif avatar.corruption > 10:
    #if R has medium corruption
        ro "W-well, I'm perfectly happy right now, thank you."

    #if R has low corruption
    else:
        ro "I remember you raping us, certainly. I am most definitely happier without interventions of your kind."

    #remerge

    xz "But you aren't. I can taste your thoughts, bitter and fibrous with the regret that war inevitably brings."
    xz "They will poison you in time, those thoughts; they will line that handsome face of yours and make you do unhappy things, blackening and burying the pleasure that would otherwise be yours to savour."

    ro "What are you getting at?"

    xz "I can help you. I can alleviate those thoughts, in a most delicious, delightful way. It will involve you and your wife, but I promise I won't have my way with her. Let me show you something new."

    #go to alright / no menu
#~     jump .alright_no_menu

#~ label .alright_no_menu:
    menu:
        "Alright.":
            $ released_fix_rollback()
            jump .xzaratlGuiltScene

        "No.":
            $ released_fix_rollback()
            ro "Stay away from me and Alexia. And keep out of my head in future, if you don't want banishing back from whence you came. My thoughts are my own."
            xz "Going to start playing hard to get, are we? Mmm, I like that - particularly since you've already let me sample the goods."
            xz "Keep carrying those glum, horrible thoughts around with you then, and take care for now... you and your wife."
            "The succubus slipped out of existence as quickly as she had appeared. Rowan walked on, resolving to put the sexual predator out of mind."
            return
else:
#if not fucked
    if xzaratl_s_advances_used_favor:
    #else if R and A used favour to get rid of her
        xz "For you to stop avoiding me. You and your blushing wife. I know that it hurts you to do it - that you cut unfair deals with our benefactors to restrain me."
        xz "I can sense your thoughts - it hurts me that you hurt yourself, particularly when all I want is to grant you great pleasure."
    else:
    #if R and A avoided X'zaratl
        xz "For you to stop avoiding me. You and your blushing wife. I know that it hurts you to do it - that you lose sleep and wear yourself down to keep away."
        xz "I can sense your thoughts - it hurts me that you hurt yourself, particularly when all I want is to grant you great pleasure."

    #remerge

    ro "Here's a solution, then - stop bothering me."

    hide xzaratl
    show xzaratl neutral at cliohnaright with dissolve

    "He started as X'zaratl appeared in front of him, a voluptuous blooming of flawless flesh out of thin air."

    xz "But even if I did that, you'd still have dark thoughts weighing you down. Bitter and fibrous with the regret that war inevitably spawns, they are."
    xz "They will poison you in time, those thoughts; they will line that handsome face of yours and make you do unhappy things. I would laugh if it wasn't so sad, for you see: it would be simplicity itself for me to help you."

    ro "What are getting at?"

    xz "I can make you feel less guilty - in a most delicious, delightful way. It will involve you and your wife. But you have my solemn vow that I won't have my way with her. I am your servant; I want to help."
    xz "Come on, Rowan. Let me show you something new."

    menu:
        "Alright.":
            $ released_fix_rollback()
            jump .xzaratlGuiltScene

        "No.":
            $ released_fix_rollback()
            ro "Stay away from me and Alexia. And keep out of my head in future, if you don't want to be banished from whence you came. My thoughts are my own."
            xz "Still playing hard to get, are we? Mmm, that's precious - until it starts getting tiresome."
            xz "And once I lose interest, you will have to carry those glum, horrible regrets around with you for the rest of your life. Take care for now, then... you and your wife."
            "The succubus slipped out of existence as quickly as she had appeared. Rowan walked on, resolving to put the sexual predator out of mind."
            return

label .xzaratlGuiltScene:

"Rowan took a deep breath. No doubt the succubus had her own lecherous agenda here... but to be free of that gnawing guilt. The weight of the terrible things he was being forced to do at the behest of the demons. Yes, that would be worth almost anything."

ro "Alright then. Show me."

xz "Excellent. It tastes so much better when you submit of your own accord. Let's go find that toothsome wifey of yours, shall we?"

#if alexia is in rowan's room
if not alexiaSeparateRoom:
    scene bg9 with fade
else:
#if alexia is in guest room
    scene bg7 with fade

#remerge
show alexia necklace concerned at edgeleft with dissolve

"Alexia froze, fingers tense on the book in her hands when Rowan and X'zaratl entered the room."

show rowan necklace neutral at midleft with moveinright
show xzaratl neutral at cliohnaright with moveinright

ro "Relax, dear. She is here on my invitation. She says she can help me with my... my piece of mind."

#if fucked
if xzaratl_s_advances_rowan_sex:
    al "I- I don't understand. Surely you remember last time? She's {i}evil{/i}, Rowan."
#else
else:
    al "I- I don't understand. Weren't we doing our best to avoid her? She's {i}evil{/i}, Rowan."

#remerge

ro "We can't avoid her for the rest of our lives, Alexia. And this I know to be true - she is more helpful to us as an ally than an enemy."

xz "Yes, timid, fair-skinned little succulent. Do relax."

"X'zaratl took Alexia's head in her hands - she barely seemed to move over to her - and hushed the words whilst moving her fingers across her brow."
"Alexia's eyes unfocused as the sharp edges of the world around her disappeared - replaced by deep sensual impression and purpose."

show alexia necklace happy at edgeleft with dissolve

al "Yes, madam - I... I am yours."

"The succubus grinned, rewarding Alexia's descent in submission with another pass of her fingers, this time across the woman's breasts. Alexia's lips opened, a long exhalation flowing out as heat spread through her body, coursing inexorably down to her sex."

ro "What are you doing to her?"

xz "You don't talk now, unless I demand it. You and I both know you've been a bad boy, and you are going to feel true penance for the things you've done. Take off your clothes, worm, and kneel there."

scene black with fade
show xzaratl neutral behind black
show alexia necklace aroused behind black

"Rowan felt no magical impulsion to do as the succubus ordered - she left it to be his choice, as it had been to bring the demon here in the first place."
"He could, maybe, refuse, drive her out... and yet. The weight of his conscience. He {i}had{/i} been bad. Even worse, for involving his innocent wife in this. He deserved this."
"Slowly he did as X'zaratl ordered, stripping away his armor and garments until his skin was bare to the chill of the flags beneath his feet and knees."
"Already he felt a certain lightness - losing his will to a harsh mistress's demands, readying himself for a punishment he so clearly required..."
"The succubus watched with a grin, stroking her clit-cock openly at the sight of the penitent man, brawny ass bared."
"She pushed her growing erection and plush breasts into Alexia's back, leading her forwards, hot breath in her ear as she fondled the human's own tit with one hand, other tracing a line down her arm."
"A bullwhip appeared in Alexia's grip; an extension of the demon creature's will."

xz "Here he kneels before you, Alexia. Your husband. You thought he'd come to rescue you, but instead he jumps to your captors' every wish. Doesn't that fill you with rage?"
xz "Doesn't he deserve to be punished for it?"

scene cg117 with fade
show xzaratl neutral behind cg117

"Flames of anger leapt in the dark of Alexia's mind. She loved Rowan, yes she did, but gods-damned did he deserve to pay for this horrible situation he had landed them in!"
"Without thinking, allowing the rage and passion to direct her entirely, she raised the whip and slashed its tip across her husband's back."
"Rowan gasped and twitched as white hot pain was striped across his naked flesh."

xz "Good boys do not flinch! Alexia, hit him again. He must learn."

"Face flushed, Alexia did so, swinging the whip in the air a few times in order to give the lash a hefty swing."
"Rowan gritted his teeth as the blow landed with a juicy THWACK, a burning red cross painted over his back, doing everything in his power not to flinch from it."
"The agony had to be accepted. Welcomed."

xz "Better. Now, Alexia, understand that your hubbie knows that he's done wrong. If only you knew half the things he has done in the demons' service; the many black, sinful deeds he has not told you about!"
xz "That is why he is on his knees before you - to receive just punishment for his failings, from the one person he can trust to only spare the lash once he has been truly forgiven."
xz "Beat him, and then beat him some more, until your heart is light."

scene cg118 with fade
show xzaratl neutral behind cg118
show alexia necklace aroused behind cg118

"Alexia was giddy. Whether by X'zaratl's design or from some long dormant desire, every time she lifted the whip and brought it down with a satisfying crack on Rowan's back and buttocks she felt a surge of lusty glee."
"By the fifth stroke her underwear was quite wet with it and she'd almost forgotten the presence of the succubus. Whipping her husband was a release to a tension so pervasive she hadn't even noticed it was there."
"For his part Rowan summoned to mind all the tawdry and evil events of the past weeks; the ruthless decisions made, the awful actions he had set into motion."
"With each agonising slash of the rope across his backside, every telling mark left upon his skin, he felt a certain salvation; a wrong of his righted."
"That rationally it made no sense made no difference. The excoriating sensation of atonement consumed all."

al "Hah!... Hah... whew…"

"It was only after the sixteenth stroke that Alexia came back to herself. Chest heaving, she raised the whip again, this time to gaze at it, and the red, arcing welts she had left on Rowan's back, with a kind of wonder. Warm fingers stroked the line of her jaw."

#if alexia is in rowan's room
if not alexiaSeparateRoom:
    scene bg9 with fade
#if alexia is in guest room
else:
    scene bg7 with fade

#remerge

show alexia necklace happy at edgeleft with dissolve
show rowan necklace naked at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve

xz "Are you done, dear?"

al "I... yes…"

xz "You enjoyed that, didn't you! I knew we wouldn't have to dig too deep under that plain surface of yours to find some spicy thoughts and desires."
xz "Oh, we're going to have such {i}fun{/i}, the three of us. Here, help your husband up and hold him. Let him know he did well, and has been absolved of his sins - for now."

scene cg313 with fade
show alexia necklace happy behind cg313
show rowan necklace naked behind cg313
show xzaratl neutral behind cg313
pause 3

"With a certain amount of shakiness, Alexia dropped the whip and pulled Rowan up, hand running across the burning ridges that ran right down his back and ass. Was it really her who had put them there?"
"It seemed impossible... but her heart leapt as the memory of the thrill, the release... she buried her head into Rowan's chest to escape dotting the 'i's and crossing the 't's of those exciting thoughts."

xz "Thank your wife for punishing you."

ro "Th-thank you, Alexia."

"It felt inescapably warm and wonderful to be hugged by his whipper, the rightful end to this painful yet incredibly gratifying experience."
"Although he was going to carry the marks of this encounter for many a day to come, he hadn't felt this light and carefree in weeks. X'zaratl's arms and soft breasts pressed upon them, and neither cringed away."

if not alexiaSeparateRoom:
    scene bg9 with fade
#if alexia is in guest room
else:
    scene bg7 with fade

show alexia necklace happy at edgeleft with dissolve
show rowan necklace naked at midleft with dissolve
show xzaratl neutral at cliohnaright with dissolve


xz "Didn't I tell you? You may have to make hard decisions in Andras and Jezera's employ, yes - but that simply opens the doorway to yet greater pleasures for the two of you to enjoy, and become closer than ever before."
xz "Trust in X'zaratl, and every day will be a new exploration of pain and pleasure."

hide xzaratl with moveoutright

al "Are you alright, love? I can't believe I hurt you like that. I- I couldn't stop..."

ro "Let go of your anxiety, Lex. You did exactly what I wanted - what I needed. It felt wonderful."

"He kissed her softly, and then slowly redressed, wincing as cool cloth fell over the welts. He would be moving tenderly for a while, yes - but the absolution of his guilt by way of the masochistic ritual was surely worth more."

#Corruption up, +1 Wounds, Guilt way down
$ change_base_stat('c', 2)
$ change_base_stat('g', -2)
$ take_damage(1)
$ alexiaWhippedRowan = True
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label andras_chanllenge:
#Andras' Challenge
#Requires: Arena built, at least 15 orcs

$ released_block_rollback()
scene black with fade
show rowan necklace neutral behind black
show andras happy behind black

"Near to the muffled roar and hubbub of the castle's arena, Rowan ran into Andras."
"The male demon was leaning against a wall with an air of casualness, but it was obvious that he had been waiting specifically for the human to happen along, most notably by the malicious grin that spread across his face when he saw him coming."

an "Rowan! Has the Lord Commander come to review the arena?"

ro "Not specifically."

an "Let's put in a visit, shall we? There's a big fight on now, and it will do the troops good to see us both taking it in."

"Rowan knew it would be pointless to argue. He nodded and allowed the demon to steer him towards the small coliseum."

scene bg29 with fade
show rowan necklace neutral at midleft with dissolve
show andras smirk at midright with dissolve

"Inside the thronged arena, soldiers quickly made space so that Andras and Rowan had prime seats, halfway up a terrace near the centre. On the sand below, two helmeted orc gladiators clashed furiously with sword and shield."
"The mob roared and oohed each time a blow found its mark; around him, Rowan saw tokens exchanging hands, beer being swilled and other would-be competitors readying themselves."

an "You can see why this is popular, eh Rowan? Even a milquetoast human such as yourself can appreciate the rush and glory of one-on-one combat!"

"Several orcs nearby sniggered, throwing sidelong gazes at Rowan. His skin crawled as Andras raised his voice."

an "But not to worry. You're safely ensconced up here - as my little pet. You wouldn't last five seconds in the ring, and nobody would expect you to. Your talents run elsewhere, after all..."

#if Rowan has had sex with andras
if andrasIntroSex:
    "With a vindictive quirk of the lip, the demon leant back and slid his hand meaningfully down his abdomen, tracing the outline of his hardening cock."
#else
else:
    an "Studying books, being at the beck and call of my sister, that's more your thing!"

#remerge

"The crowd of orcs surrounding them guffawed, turning delighted eyes back to Rowan for the response."

menu:
    "Rise to the challenge.":
        $ released_fix_rollback()
        ro "You're pathetic. I could best any one of these orcs in combat, and you know it."
        an "Prove it!"
        "Down below, the fight came to an end - the bigger orc smashed his opponent's blade out of his hand, and the latter quickly yielded, knee on sand. The crowd roared their approval, getting even more raucous when Andras himself strode out and thrust the winner's hand to the sky."
        scene black with fade
        show andras smirk behind black
        an "And now, my dogs of war, my blood-drunk sons and daughters: a special treat. Our very own commander, Lord Rowan himself, will now step into the arena to take on your champion!"
        "By the time Rowan had stripped down to the waist, taken up helmet, blunted sword and shield and was striding into the arena, the murmuring around the terraces had built into a full-throated roar of excitement."
        scene bg28 with fade
        show rowan necklace neutral at midleft with dissolve
        "He could feel it vibrating through the sand as he took up stance opposite his opponent; all of the orcs, predictably, were bellowing the name of their champion. The big, sweat-streaked orc gave him a big, unfriendly grin."
        show wild orc neutral at midright with dissolve
        wo "I can't believe you agreed to this, hoo-man. I will crush you, and once I do, I will be Warlord!"

        #combat check dc 15
        # TODO change when combat will be defined
        #fail
        if not dice(20) > 15:
            "The sound of steel clanging and barking against itself punctuated the crowd's throbbing roar, Rowan and the orc stepping backward and forward across the muddled sand, blocking, feinting and parrying furiously."
            "At first Rowan thought he had the advantage - he forced the big greenskin back numerous times with his quicker blows - but his opponent had seemingly limitless endurance, and Rowan's limbs began to ache as the battle dragged on."
            "The orc suddenly stepped in behind Rowan's failing guard and smashed the pommel of his sword into his face. Nose bloodied and pain ringing in his ears, Rowan fell to the ground. Cheers and jeers spiralled to the spin of the sky above."
            show andras happy behind bg28
            an "Enough! Well fought, champion, you retain your belt. You and yours should be proud this day."
            wo "Pshaw! Retain my belt? His crown should be mine! Why do we take orders from this weakling anyway?"
            an "Because we are conquering a human world, not an orcish one. He is useful to us in ways you will never be. Revel in your victory today, but always remember that."
            "The Orc snorted in contempt at Rowan, before lifting both of his trunk-like arms to the crowd, who howled their approval at him."
            "With the receding of pain came the burn of humiliation, but Rowan knew better than to scurry away; he lifted his head, applauded the tusked warrior, and then walked away with his head held high."
            hide wild orc with moveoutright
            show andras smirk behind black
            an "You are braver than I thought - and more foolish, human. Brawling with orcs! At least you entertained them. And me."
            ro "Please do shut up and leave me alone."
            "The sadistic demon slapped him on the shoulder merrily."
            an "Get that nose of yours looked at, at least. You'll have to come up with some way of redeeming yourself, you know. The orcs won't forget you getting your ass handed to you easily."
            #gain 10 xp, a wound, and lose morale
            $ add_exp(10)
            $ take_damage(1)
            $ change_morale(-5)
            return
        #pass
        else:
            "The clang and shriek of steel punctuated the crowd's throbbing roar, Rowan and the orc circling backwards and forwards across the muddled sand, blocking, feinting and parrying furiously."
            "The big brute fought ferociously, with what seemed like limitless endurance, but Rowan was by far the more skilful and level-headed swordsman."
            "He allowed the orc to waste his huge haymakers on thin air whilst stinging him again and again with telling drives of his blade, until the orc's chest was heaving and creaking with exhaustion."
            wo "Stand... still!"
            ro "If you insist."
            "He stopped circling suddenly and stepped in, smashing his opponent with the blunt edge of his sword hard enough to send a bloody tusk flying. The orc collapsed to the deck, weapon falling out of his hand."
            "The crowd fell quiet, watching dumbstruck as Andras strode back out, grasped Rowan's wrist, and thrust it to the side."
            show andras happy behind bg28
            an "Your victor, your commander - Lord Rowan!"
            "A hushed murmur shuffled around the terraces, before growing slowly into a clamor. After a few seconds, all present were bellowing two syllables."
            cro "Ro-wan! Ro-wan! RO-WAN!"
            scene bg14 with fade
            show rowan necklace neutral at midleft with dissolve
            show andras happy at midright with dissolve
            an "Well fought, champion. I must admit that I didn't think you would be brave enough to pick up the gauntlet."
            ro "You just hoped to humiliate me, then?"
            an "One way or another: our troops were entertained. This way though, you demonstrated their leader's strength and steel. You grabbed the situation and made it your own! I liked that."
            "He gave Rowan a lingering eye before swaggering off with a smirk, completely unabashed. The demon was right about one thing, though; Rowan heard chatter echo throughout the fortress about his famous victory in the arena for many days to come."
            #gain 25xp, morale, and andras' favour
            $ add_exp(25)
            $ change_morale(5)
            $ change_favor('andras', 1)
            return

    "Try and provoke him back into fighting in the arena instead.":
        $ released_fix_rollback()
        ro " Seems to me that the being that spends most of his time bragging about how mighty his race is should be the one to prove his mettle in the ring."
        ro "But nobody expects that of you, Andras. Your talents run towards bragging about the size of your dick and hanging around the castle doing precisely nothing."

        #diplomacy check dc12
        #fail
        if not check_skill(12, 'diplomacy')[0]:
            an "Hah! I knew you would try and weasel out of fighting somehow. Don't shiver in your socks about it, Rowan - as I said, nobody would expect a human to risk his soft, clean skin in honorable combat."
            an "You stick to what your people are good at. Weaselling."
            "The soldiers around them sniggered, but when Rowan didn't dignify Andras' words with a response they turned back to the action down on the sand."
            "The fight ended soon after, and the male demon headed down to thrust the victor's hand up to the sky. Rowan slipped away quietly in the exultant clamor."
            return
        #pass
        else:
            "The orcs surrounding them ooh'ed, the human and demon's verbal jousting tickling their limited minds in ways the battles could not. Andras's face darkened."
            an "You dare question MY prowess? I'll show you how a true warrior fights, worm!"
            "Down below, the fight came to an end - the bigger orc smashed his opponent's blade out of his hand, and the latter quickly yielded, knee on sand."
            scene bg28 with fade
            show andras displeased behind bg28
            show rowan necklace neutral behind bg28
            "The crowd roared their approval, getting even more raucous when Andras himself strode out and held the winner's hand up to the air."
            an "And now, my dogs of war, my blood-drunk sons and daughters: a special treat. Your leader, red knight Andras the Immolator, shall battle your champion!"
            an "No magic, sword vs sword - honorable combat, so you may be reminded why you would follow him unto hell's gates themselves!"
            "The murmuring around the terraces had built into a full-throated roar of excitement by the time he had finished, the crowd lapping up the bold demon's words."
            "Rowan could feel it vibrating through the stone as he watched Andras took up stance opposite the burly orc champion, foregoing armor but taking up the blunt sword and shield the previous contestant had used."
            "The orc surprised Rowan by lasting longer than he expected. He weathered several of Andras's blows and then got a good one in himself, slashing the demon across his chest and forcing him back with a startled bark."
            "After that though, the devil-may-care smirk dropped off Andras's face and he came at his opponent like a berserk hummingbird."
            "The lumbering orc was struck with vicious precision again and again, barely even able to bring his shield up before he was attacked from yet another angle."
            "When at last the big brute collapsed to the sand, holding his hand up for mercy, Andras smashed him across the face, knocking out a tusk and laying him out cold."
            "He turned to the terraces and raised his arms, chest heaving, drinking in the cheers that rained down."
            cro "AND-RAS! AND-RAS! AND-RAS!"
            an "What do you think about that, worm?"
            ro "Oh, you certainly showed me about how honorable combat should be fought, demon. Particularly the bit where you hit your opponent after he surrendered."
            "Andras sneered at Rowan, but drunk upon his own victory and the jostling knot of backslapping orcs around him, he went no further with it."
            "In retrospect, Rowan realised as he listened in on the conversation of his guards in the days to come, the incident at the arena had worked out well."
            "The garrison had been reminded not only of their demon leader's ruthlessness and battle prowess, but their human leader's slyness and way with words."
            "Their expectations had been met; their world view affirmed."
            #gain morale (less than gain from rowan winning in arena), 10xp
            $ add_exp(10)
            $ change_morale(3)
            return

    "Don't take the bait.":
        $ released_fix_rollback()
        ro "Whatever."
        "Andras tried needling Rowan a couple more times, but both he and the orcs around them grew bored when Rowan refused to respond, and their attention drifted back to the battle."
        "The incident was completely forgotten by the following day."
        return

    "Respond submissively.":
        $ released_fix_rollback()
        $ rowanAndrasSex =+ 1
        $ rowanGaySex += 1
        ro "You are right, sir. I am your pet."
        an "Hell-damned right."
        "He reached out and pulled Rowan into his brawny side, flagrantly groping the human's flank and chest."
        "Rowan felt himself grow hot underneath the contemptuous eyes of the surrounding soldiers; where the burn of humiliation ended and the helpless lust he felt underneath Andras's rough touch."
        "The decadence of demons and the spinelessness of humans affirmed, the orcs lost interest and turn their attention back to the battle."
        "Andras though grew more and more bold with his gropes and caresses, his lust to dominate utterly interchangeable from that he felt watching blood spill and blade clash below."
        scene cg129 with fade
        pause 2
        show cg130
        show andras smirk behind cg130
        pause 2
        "His livid gaze fixed on a particularly fierce and savage wrestling match, he snatched Rowan's hardening penis and began to jerk it hard, making the human gasp to the helpless arousal pulsing up his spine and tightening his balls."
        "Andras suddenly stood up and pushed Rowan out of his seat."
        an "The chambers below. Now."
        scene cg62 with fade
        show andras smirk behind cg62
        pause 2
        "The sound of the crowd and clang of sword against shield was muffled in the sandy cell where Rowan got on his knees, coiled his hand around the base and spread his lips over the musky head of Andras's thick erection."
        "Drunk on violence and Rowan's willing submission, Andras had no interest in formalities; he grabbed the human by the hair and roughly pumped his cock past his lips, utterly unheeding to the splutters and gulps this precipitated."
        an "Ungh... tighten up and suck it up, whore! I know you can, it's what you're good for... that's it!"
        "Rowan hollowed his cheeks around the exacting thrust of his master's bulging erection, earning himself a groan of approval and a tightening of the grip on his hair."
        "Andras worked his muscular hips, filling Rowan's mouth with hard, delicious meat again and again, practically using him as a masturbation toy to reach a delicious high."
        show cg62 with sshake
        show cg62 with sshake
        scene cg63 with flash
        show andras smirk behind cg63
        pause 2
        "Rowan's cheeks swelled with hot demon cum as Andras found release with an ecstatic gasp. He swallowed it down only to receive another mouthful, and another, and another."
        "At last Andras released his cruel grasp and withdrew his wilting member, drool and thick seed trailing after it. He even went as far as to stroke Rowan along the line of his jaw."
        an "A prime seat at the entertainment, crowned by fifteen luscious minutes with my pet cock-polisher. Ah, this is the life I was born to lead!"
        "Did Rowan think of the tyrannical demon as 'master' during all of that? He shuffled the thought away as hurriedly as he got back to his feet and strode away from the arena. He could not deny the tiny shiver of pleasure it gave him, though."
        #gain corruption, gain andras' favour
        $ change_base_stat('c', 2)
        $ change_favor('andras', 1)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label orc_deserters:
#Orc Deserters
#Low morale event. Requires at least 15 orcs

show bg6 with fade
show rowan necklace neutral at midright with dissolve

"Lost in his own thoughts, Rowan was slightly startled by the burly sergeant striding into the throne room. He and two other soldiers frog-marched five orcs in chains in. The prisoners looked ragged and resentful."

show orc soldier neutral at midleft with moveinleft
show wild orc neutral at edgeleft with moveinleft

os "These vermin tried to run away whilst out on patrol! Took us a day and a half to track 'em down and drag 'em back here."

wo "There's nuthin but piss and misery in this y'ere place! Takin orders from a weakling yuman who's got shit all clue what he's doin. You can stuff it up your bung'ole!"

os "Silence, coward! What do you want doing with 'em, lord?"

"Rowan knew the mood in the barracks had been low recently, but he had not been aware that it had gotten this bad."

show andras smirk at edgeright with moveinright

an "If I were you, I'd have them executed."

ro "Oh. You're skulking around here, are you?"

an "Naturally. You need all the advice you can get. I'll give you it again: Execute them. Orcs respond to hard discipline and blood-displays. Turn a problem into a boon!"

menu:
    "Put them in the stockade for a week.":
        $ released_fix_rollback()
        ro "No. We need every healthy soldier we can get. Spare them, and stick them in the stockade on half rations for the week. When they come out they can show their gratitude by following every order to the letter from now on."
        os "As you say... sir."
        an "*snort* What a fool you are! Do you think you're running a cake shop here? If they didn't think you were a weakling before, they certainly will now!"
        "Andras was right - once word got around that Rowan had spared the lives of the deserters, the mood in the barracks turned downright mutinous."
        "Still, after the orcs were released they agreed to continue serving, and Rowan walked with his back a little straighter for not having resorted to brute displays of power."
        #Military Strength unchanged, Morale down, Corruption down
        $ change_morale(-5)
        $ change_base_stat('c', -2)
        return

    "Execute them.":
        $ released_fix_rollback()
        ro "Desertion cannot be tolerated. Take them to the yard, gather the garrison and have them executed."
        os "Right away, sir!"
        hide wild orc with moveoutleft
        hide orc soldier with moveoutleft
        an "Good man. There is nothing weak about listening to experience, you know."
        "Andras was right - the garrison watched the beheadings in stunned silence, but it was noticeable afterwards how the orcs went about their tasks and snapped to attention when Rowan approached with considerably more vim."
        "Still, the certain knowledge that the old hero of Rosaria would never have stooped to executing his own men to keep them in line plagued Rowan's mind."
        #Military Strength down, Morale up a lot, Corruption up
        $ castle.buildings['barracks'].troops -= 5
        $ change_morale(10)
        $ change_base_stat('c', 2)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_visits_with_skordred:
#Alexia visits with Skordred
#No requirements, but will appear at some point during the second mission in the NPC slot eventually.

#workshop bg
scene bg14 with fade
show alexia 2 necklace happy at midleft with moveinleft

al "Hello? Anyone in here? I hope I'm not interrupting anything."

show skordred happy at cliohnaright with moveinright

"Alexia spotted the dwarf working on something at a workbench right after she spoke, but he was already in the process of setting down his work and approached her with a smile on his face."

sk "Is no problem, nothin urgent. I don believe we've been intradused. I am Skordred, master builder, at yar service."

al "Alexia Blackwell, uh, housewife. It's nice to meet you. My husband warned me you might be a bit rough around the edges...."

sk "If I'm nah mistaken, you're the honored guest of my masters."

al "It's not exactly by choice."

sk "A regrettable state of affairs.  I'm very sorry that one such as yarself was unfortunate enough to fall in love with a regicide. However, know that I donna blame ya far the actions of yar husband. Yar always welcome in my shop."

"He held out his hands and, after a moment's hesitation, Alexia placed one of hers in them. The dwarf kissed her hand through his beard and then released it."

sk "Naw, tell me what brings ya here today?"

al "I was hoping you could tell me a bit about this castle, I really don't know anything about this place and it looks like I'll be calling it home for the foreseeable future."

sk "Is no problem at all.  If I may be permitted a moment of pride, I would call Bloodmeen my greatest creation."
sk "The castle is a sorry sight now, but just imagine what it looked like when the mortar was fresh and master Karnas was marching through the gate far the first time."

"The man was lost in memory for a moment before continuing."

sk "Bloodmeen actually refers to an entire series of castles, each serving as the seat of power for Kharos's holy vessel. My order of master builders exists to make certain that a proper fortress from which to liberate the world awaits each of them."
sk "Would you like to know the histories of the previous castles or thar lords?"

al "That's okay. Thank you for your help, master builder, it was very interesting hearing about the castle."

sk "It was my pleasure. Have a enjoyable day Alexia."

hide alexia with moveoutleft
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label rowan_is_feeling_guilty:
#Rowan is feeling guilty
#Requires Rowan have enough guilt to trigger low guilt after decay.  High priority event.  Note that conquering Raeve Keep should give enough guilt on its own to trigger this event.

scene bg4 with fade

"There were screams, blood flew in the air, figures pointed, and someone laughed."
"Rowan was walking forward, towards someone unarmed who begged for him to stop, to leave them alone."
"Then he raised his hand, a hand holding a sword, and brought it down on the defenseless person! Somehow now he knew that he was the one laughing."

scene black with fade

#if alexia is sharing a room with Rowan
if not alexiaSeparateRoom:
    show alexia necklace naked shocked behind black

    al "Rowan, Rowan!"

    scene bg9 with fade
    show alexia necklace naked shocked at center with dissolve
    #neutral
    show rowan necklace naked concerned behind bg9

    ro "Wha? Alexia, where?"

    show alexia necklace naked at center with dissolve

    al "Good.  You were tossing and crying out in your sleep. Saying no over and over to yourself."

    show alexia necklace naked at midright with moveoutright
    hide rowan
    show rowan necklace naked sad at midleft with dissolve

    ro "Oh, it was just a dream."

    al "A nightmare. I've never seen you like this before, it was nothing like the war terrors you sometimes had."

    "Rowan covered his face with his hands, feeling the cold tears on his face that had been brought forth from the horrific images in his mind."

    ro "It's getting to me. The guilt for the things I've done for the twins, the people I'm killing and enslaving...."

    al "Hey, take it easy.  You're not doing any of that right now, you're with me."

    "She wrapped her arms around him and tried to comfort her husband. The soft embrace brought forth both tears of guilt and gratitude. The hero cried against his wife, cried for the evil he'd done and for what he would still have to do for the two of them to survive."
    "After some time had passed, Rowan's tears finally stopped flowing and he pulled back."

    show rowan necklace naked concerned at midleft with dissolve

    al "Feeling better now?"

    ro "Not really, but I think I can bear it."

    al "Are you worried this is going to affect your work?"

    ro "No, this guilt definitely is going to hamper me a little. I can probably take some more before it seriously slows me down, but eventually I'll be crippled by it."

    al "You're a good man. Even after all that's happened, you're still a good man. Try to take it easy, we'll manage if you put off doing bad things while your consciousness is getting to you."

    show rowan necklace naked at midleft with dissolve
    "A wry chuckle escaped his lips, seeking a break from the morbidity of the discussion."

    ro "Yeah, try to balance the evil so I don't feel quite so bad about it. Great advice."

    #alexia necklace naked concerned
    al "Rowan?"

    show rowan necklace naked concerned at midleft with dissolve
    ro "I'm fine, I'm... fine."

    return

#else
else:

    show rowan necklace naked concerned behind black

    ro "No! No! Please!"

    "Rowan shook, his body was covered in cold sweat and he could feel tears on his face."

    ro "Where?"

    scene bg9 with fade
    show rowan necklace naked sad at midleft with dissolve

    ro "Oh, it was just a dream."

    scene bg14 with fade
    show rowan necklace neutral at midleft with dissolve
    show alexia 2 necklace concerned at midright with dissolve

    al "Rowan! You look awful, what happened?!"

    ro "Oh, hello Alexia, I had a bad night."

    al "Bad?  From the looks of things it was truly awful. Did you have another night terror from the war? No, wait, this looks much worse."

    "Rowan covered his face for a long moment, recalling the images that he'd seen and what was clawing at his insides."

    ro "It's getting to me. The guilt for the things I've done for the twins, the people I'm killing and enslaving...."

    show alexia 2 necklace happy at midright with dissolve

    al "Hey, take it easy.  You're not doing any of that right now, you're with me."

    show rowan necklace sad at midleft with dissolve
    "She wrapped her arms around him and tried to comfort her husband. The soft embrace brought forth both tears of guilt and gratitude. The hero cried against his wife, cried for the evil he'd done and for what he would still have to do for the two of them to survive."
    "After some time had passed, Rowan's tears finally stopped flowing and he pulled back."

    show rowan necklace neutral at midleft with dissolve

    al "Feeling better now?"

    ro "Not really, but I think I can bear it."

    al "Are you worried this is going to affect your work?"

    ro "No, this guilt definitely is going to hamper me a little. I can probably take some more before it seriously slows me down, but eventually I'll be crippled by it."

    al "You're a good man. Even after all that's happened, you're still a good man. Try to take it easy, we'll manage if you put off doing bad things while your consciousness is getting to you."

    show rowan necklace happy at midleft with dissolve
    "A wry chuckle escaped his lips, seeking a break from the morbidity of the discussion."

    ro "Yeah, try to balance the evil so I don't feel quite so bad about it. Great advice."

    show alexia 2 necklace concerned at midright with dissolve
    al "Rowan?"

    show rowan necklace neutral at midleft with dissolve
    ro "I'm fine, I'm... fine."
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label disease_outbreak:
#Disease outbreak
#Req at least 10 soldiers.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with moveinright
show andras angry at edgeright with moveinright

"That morning, shortly after Rowan had gotten to work he was approached by Andras and an orc soldier."

ro "Yes, how can I help?"

an "Show him."

"The demon motioned to the soldier with him, who promptly stripped down and revealed a large rash that was spreading across his abdomen."

an "This damn rash has spread to a bunch of our troops and it's making them weak."

show rowan necklace angry at midleft with dissolve

"Rowan gritted his teeth and cursed."

ro "Damn, that's bloodren pox. It's a very dangerous disease that usually either kills those it infects within a few days or clears out after a week. Tends to spread fast too, very dangerous to people closely packed together, like soldiers in a barracks."

an "Gheh, can we stop its spread by killing the infected?"

ro "We don't need to kill them, just isolate them. If you survive this, you're pretty much immune afterwards. Come on, we need to start moving the infected away from the barracks into the tunnels."
ro "That should at least slow the rate of infection, I hope."

show black with fade

"The two of them headed down to the barracks and organized Rowan's suggested quarantine. There did seem to be fewer new cases afterwards, but the hero wasn't sure if that was because the outbreak had already died down or because of his efforts."
"Many of the soldiers that had already come down with bloodren pox would be dead by the end of the week when Rowan returned from his exploration."

#Randomly lose between 5 and 20 soldiers, but not more than 50% of your total.
$ castle.buildings['barracks'].troops -= min(castle.buildings['barracks'].troops / 2, 4 + dice(16))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label pure_morning_with_alexia:
#Pure morning with Alexia
#Requires Rowan and Alexia be sharing a room and that Alexia be pure.

scene cg30 with fade

"Rowan awoke to the feeling of his wife laying on him.  Since she still seemed to be asleep, he decided to just enjoy her soft warm skin against his rather than waking her up."

show alexia necklace naked behind cg30

al "Good morning darling."

scene cg31 with fade
show alexia necklace naked behind cg31
show rowan necklace naked behind cg31

ro "Heh, it isn't often that you wake up before me. What gave it away?"

"Alexia slipped her hand under the sheets and brushed it over her husband's cock, which had grown hard next to her leg."

ro "Should I apologize for thinking you're beautiful?"

"They both grinned."

al "Never."

menu:
    "Time to get up.":
        $ released_fix_rollback()
        "The two of them shared a long kiss, then the hero climbed out of bed to start another day in glorious service to the twins."
        return

    "Flip over onto Alexia and make love to her.":
        $ released_fix_rollback()
        jump .alexiaPureMorning

label .alexiaPureMorning:

#CG of Rowan kissing Alexia while laying on top of her.
scene cg202 with fade
show rowan necklace naked behind cg202
show alexia necklace naked behind cg202
pause 3

"He rolled over, putting himself on top of Alexia and kissing her deeply. She welcomed him into her mouth and wrapped her arms around his head to keep him against her for several moments longer than Rowan had originally intended."
"When he was finally able to break the kiss, he had to take several deep breaths to recover."

ro "I knew you liked kisses, but I wasn't aware you liked to kiss my breath away."

al "If you're allowed to have surprises, so am I."

#CG of Rowan licking Alexia's nipple.


"As payback, Rowan shuffled a little ways down so that he could run his tongue around Alexia's nipple, as well as give it a playful nibble."
"This brought a sharp gasp to her lips, just as the man had hoped."

al "Ah! What's that for?"

ro "Just trying to steal your breath away."

al "I'm not sure you quite managed that, think you can try again?"

scene cg83 with fade
show rowan necklace naked behind cg83
show alexia necklace naked behind cg83
pause 3

"Instead of accepting that invitation, Rowan shifted once more to abruptly push himself inside Alexia's passage. She let out another gasp of surprise that quickly turned into a moan of pleasure."

ro "Nah, let's keep the train of surprises going."

al "Oh darling, you brute!"

"Her moans of pleasure between her words signaled that she was far from upset at this penetration. The feeling of her walls rippling around Rowan's cock, slick with the fluids of her arousal, added further evidence to that conclusion."
"Rowan began to slowly rock his hips forwards and back, his arms firmly planted on the bed on either side of Alexia's head for balance. His wife was content to let him take her, since he'd gotten lots of practise at learning the perfect pace to take their lovemaking."
"Gradually he increased his thrusts, timing them with Alexia's gasps and appreciative moans. Finally his own lusts caused him to lose control and he abandoned himself to them.  Sensing the change in her husband, the woman could only smile and whisper to herself."

al "Yes, Rowan please, please fill me!"

show cg83 with sshake
show cg83 with sshake
scene cg84 with flash
show rowan necklace naked behind cg84
show alexia necklace naked behind cg84
pause 3

"Rowan came, spurting deep into Alexia's hot passage and triggering her own orgasm in response. Still spurting more of his cum inside her, the man collapsed on top of his wife, weakened by the now finished sex."
"The woman wrapped her arms around her husband and kissed his neck while continuing to relish the feeling of him filling her. It was in these moments together without an audience that she was her happiest."
"After catching his breath and rolling off of Alexia, Rowan spoke again."

ro "Well, was your breath taken away?"

al "I don't know, you'd better try again to make sure."

"Both grinned at each other once more."

ro "How about tomorrow or next week?"

al "I'll see if I can fit you into my schedule."

ro "If you can't find the space, I'll be sure to work my way in anyway."

al "Ha. Darling, I think that's enough innuendoes for one morning."

"The two of them shared a long kiss.  Then, still smiling, the hero climbed out of bed to start another day in glorious service to the twins."

#Rowan loses some corruption
$ change_base_stat('c', -2)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_s_alliance_making_skills:
#Jezera's alliance making skills
#Requires after week sixteen, high priority event after week eighteen.

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

je "There you are, my hero. I need to ask a favor of you, I'm going to be meeting with a woman of status shortly and I'd like to present you as my sex toy to demonstrate my power."

ro " Mistress. It isn't like you to give me a choice in the matter, is there a catch?"

je "Only if you mind wearing a collar and filling your mouth with pussy while two lovely ladies discuss politics and possibly being dominated by another woman than myself. I want you to pretend to be absolutely obedient on this excursion."
je "Oh, we will both have blue skin, if that happens to factor into your decision."

menu:
    "Join her on her trip and pretend to be Jezera's sex slave.":
        $ released_fix_rollback()
        jump .jezSexSlave

    "Refuse to join her.":
        $ released_fix_rollback()
        "Rowan shook his head."
        ro "Sorry, I don't think I'd be comfortable pretending to be your slave."
        show jezera neutral at midright with dissolve
        je "I feared as much, but it's fine. I should be able to put together this alliance anyway. Have a good day, my hero."
        hide jezera with moveoutright
        scene black with fade
        "Later that day, Jezera returned from her meeting. While she'd negotiated an alliance successfully without Rowan's help, the terms her new ally demanded for such a relationship had angered her greatly."
        #CG of Jezera holding up the dark elf queen with her ribbons.
        "To the point that she'd called the whole thing off by beheading her potential partner."
        play sound "music/SFX/BodyfallDirt.ogg"
        #CG variation with queen gone.
        "The whole episode had worried Rowan greatly, as it was the first time he'd learned something of Jezera's activities away from the castle. If this was how she conducted all her negotiations, there could be dire consequences."
        $ codex_add('dancer_s_whips')
        return

label .jezSexSlave:

$ rowanJezSex =+ 1

ro "Alright, I'll do it."

je "Wonderful! Come, let's get you dressed up and then we'll be on our way."

scene black with fade

"In addition to a collar, the demoness also had the hero change out of his clothes into something quite similar to the prisoner garb he'd been forced to wear a few months prior."
"The ensemble clashed severely with the elaborate sapphire necklace, but Jezera made no move to remove it."

scene bg3 with fade
show jezera neutral at midleft with dissolve

"After that, the two left through the portal to a forested area nearby mountains that Rowan wasn't familiar with. If he had to guess, he'd say they were somewhere in the forests of Ealoaen, home of the elves."

#cave bg
scene black with fade
show jezera neutral at midleft with dissolve

"Jezera led him to a nearby rock formation and opened up a hidden path down into a cave. She obviously knew where she was going, as she picked her way through a very specific path from tunnel to tunnel, ever downwards."
"Occasionally she'd use magical ribbons of energy to carry herself and Rowan down sheer cliffs or over difficult terrain. That particular spell seemed to be Jezera's magic of choice as she was very good at manipulating the energies and she always used it when she could."
"Eventually they reached caverns that had been worked by intelligent hands. Here was where the show would begin, so a lease was taken up and a hood placed over the hero's head."

scene black with fade
show jezera happy behind black

"Rowan would have to trust his mistress to lead him through the caves. Even without his eyes covered the man would have had a hard time making his way through here as the demoness no longer bothered to use lights and there was no other sources the man could make out."
"Voices whispered about them and the soft pattering of feet other than their own was audible, but Rowan had no idea who they belonged to."
"Eventually they arrived at an underground building of some kind and were lead inside after Jezera conversed with another woman in a language that Rowan finally realized to be dark elvish. He didn't know what they were saying, but it did tell him where they were."
"The realization made him smile behind the hood, understanding now why Jezera had said that he would be seeing another blue woman."
"Inside Rowan finally could see something again, as glinting lights would occasionally wink at him through the lines in the fabric covering his head. They were lead to a chamber deep inside the structure before someone spoke again."

wom "Well now Jezera, let's see the great hero my attendant tells me you've brought."

"She spoke in the common tongue, either because it was Rowan's or Jezera's native language. Regardless of the reason, it meant that the man could understand it."

je "Of course."

"Now Jezera roughly dragged Rowan forward and pushed him to his knees before pulling the hood up off his head."

je "May I present, the great hero of Karst and one of Deanara’s band to defeat Karnas, Rowan Blackwell."

#CG of dark elf queen sitting in a chair.

"Thanks to the light given off by some nearby crystals, Rowan could clearly see the regal dark elf woman that he'd been presented to. She was a lithe woman, dressed in an expensive silk gown that clung tightly to her body and accentuated her womanly features."
"They were inside what appeared to be a private sitting room, with the dark elf seated in a chair at a small table against the wall."
"She stood up, revealing herself to be nearly a head taller than Rowan, and took a step forward to get a closer look at the man. A wicked smile graced her lips and the hero felt a flash of recognition that mirrored the expression on the woman's face."
"He knew this woman, but why?"

wom "Hahaha! It is him! Well now Jezera, you've well and truly impressed me. Let's see how well he licks."

je "I'd be happy to."

"The two women sat down together at the table and Jezera pulled on Rowan's leash until he crawled up to her legs. While he wrapped his arms around her and lifted the fabric of her dress out of the way he continued to wonder where he'd seen this dark elf before."

scene cg67 with fade
show jezera happy behind cg67
pause 2

"He could feel the gaze of the lady from behind as he started his work on his mistress. First he kissed the insides of her legs and gently drew his fingers over the crevice of her skin where leg met hips. Then brushed his tongue over labia, nibbling slightly when he touched the other side."

wom "He's quite the romantic, isn't he?"

je "Yes, did you know that after the war he went back to his home village and married his peasant sweetheart?"

wom "Huh, no kidding? I admit, married men are among my favorites to make my own."

"Rowan extended his tongue and ran it up the inside of the lower lips, then flicked it ever so slightly over Jezera's clit, causing her to twitch once. She inhaled sharply as his tongue plunged deep into her passage several times in succession."

wom "It would sound like you're having a good time. Would you mind giving me a chance to enjoy him afterwards? The thought of having a hero of men between my legs is... appealing."

"A hand was placed on the back of Rowan's head as he continued to toy and tease. Then it pushed him against Jezera's sex as her thighs tightened up around his head. Taking the hint, he switched to a much more direct method of eating and licking as fast as he could."

"The effect was almost immediate. Gasps and moans of pleasure now emanated in response to his ministrations. Jezera exalted in this act and was soon leaking out her fluids all over Rowan's face in orgasm."

je "Hah, hah, I would say that he's probably good for a second round, aren't you pet?"

"She ran her fingers through his hair and smirked down at the man still between her legs."

je "You just love pussy, don't you? Go get more!"

scene cg231 with fade
show jezera happy behind cg231
pause 3

"Jezera relaxed her legs and directed Rowan towards the dark elf. He shuffled on the ground the short distance to the other woman, keeping his head down to avoid drawing too much attention."

"The unfamiliar lady uncrossed her legs and rolled up her gown to reveal an elven vagina. Her folds were thinner than Jezera's, fitting right in with her lithe frame. It was also already very wet, evidence of just how much the previous display had turned her on."

#CG of dark elf queen with Rowan eating her out.

wom "Like what you see? Good, drink up slave!"

"She lifted up her legs and wrapped them around Rowan's head, forcing him in without any setup or foreplay. Obediently, he started licking, hard."

wom "Oh yes. More, more."

"While the man redoubled his efforts, he felt a long finger brush over his face. Suddenly there was a sharp pain as the woman opened a small cut on his cheek which made him cry out."

wom "Uh, uh, uh, keep eating or it will get worse."

"He did so, licking and plunging and drinking from the dark elf. At the same time, she caught a few drops of his blood on a finger and brought it up to her lips. Rowan could just barely see her licking the finger sensually before she let out one long gasp that signalled her orgasm."
"Shortly after coming down from her high, the dark elf woman casually released the man from her grip and pushed him to the side so she could sit at the small table properly again."

wom "I'm quite satisfied. Shall we talk business, Jezera?"

je "Yes, let's."

scene black with fade
show jezera happy behind cg231

"The two of them pointedly ignored Rowan as he crawled away until the leash was taught and then sat down cross legged to watch their conversation. Well, he mostly listened since he didn't want to take the chance of making eye contact with the woman."
"They discussed an alliance between the woman and Bloodmeen castle, which Jezera seemed to claim to be the sole ruler of. Made sense, dark elf society was a matriarchy and wasn't exactly known for respecting men at all."
"While he tried to pay attention to what was being said, Rowan constantly found himself distracted by old memories, trying to conjure up why the woman was so familiar. However, his attention was arrested again when he noticed that Jezera was becoming visibly irritated."

je "Being a vassal of the new rising of Bloodmeen and a lord of one of our provinces should be an honor for you and I've already given you generous gifts, why do you keep pushing for more?!"

"The dark elf woman laughed at the sudden outburst."

wom "Oh child, you're not very good at diplomacy are you? If I recall, you started this whole discourse claiming we were equals. Now you think to gain my services by claiming to be greater?"

"Still smiling, she leaned forwards in her chair."

wom "I've done my homework, I know your power. I'm the one with the armies, you need my help. If this alliance is to happen, you need to offer me something far better than being just another subject."
wom "I will join you, but as an equal partner, not a vassal. The price of helping you take the world will be half of it, that's fair is it not?"

"This was evidently the last straw for the demoness, as she suddenly stood up and tossed the lead of Rowan's leash aside. Ribbons of magic blazed to life around her."

wom "Sit down girl, you're not impressing anyone by -urk!"

#CG of Jezera holding the dark elf queen up by her ribbons.

"One of Jezera's cords of magic snapped around the dark elf woman's neck, cutting off her words and causing her to struggle for breath!"

je "I'll show you! If you won't serve me, then I'll find another who will!"

"Genuine fear was plain on the elven woman's face for the first time. She tried to signal something as her body was lifted up into the air by her neck. As moments passed, more and more tethers latched on until the combined force tore all the way through, beheading the dark elf."

play sound "music/SFX/BodyfallDirt.ogg"
#variation of Jezera's ribbons with the dark elf queen gone.

"This sudden reaction from Jezera had caught Rowan completely off guard and he didn't even have time to think about how he should respond in the scant few seconds between when his mistress launched her attack and when the body fell to the floor."

je "We're leaving."

"She addressed Rowan, but didn't bother to wait for a response before teleporting the two of them back to the castle."

scene bg10 with flash
show rowan necklace neutral at midleft with dissolve
show jezera displeased at midright with dissolve

je "Grr, I'm going to have a bath. You're dismissed Rowan."

show jezera displeased at edgeright with moveoutright

"She started to walk away, then turned back and offered a smile to the man who was still sitting on the ground."

show jezera happy at edgeright with dissolve

je "At least I can count on you, my hero."

hide jezera with moveoutright

"This whole episode worried Rowan greatly, as it was the first time he'd learned something of Jezera's activities away from the castle. If this was how she conducted all her negotiations, there could be dire consequences."
"Plus he still wasn't sure who the woman had been. It was clear that she had been someone of great power within the dark elf hierarchy, a general perhaps? He didn't know and it wasn't worth the risk of asking Jezera right now."

#gain corruption
#gain favour with jezera
$ change_base_stat('c', 3)
$ change_favor('jezera', 1)
$ codex_add('dancer_s_whips')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drinking_buddies:
#Drinking buddies
#Can trigger three weeks after the forge is built.  Requires that the tavern exist.

show bg10 with fade
show rowan necklace neutral at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

gh "Hold, why are we here?"

ro "I figured you'd rather hang out somewhere a bit less intimidating than the castle."

"Rowan placed his hand on the blue jewel hanging around his neck."

ro "Two to the tavern, if it pleases you."

show jezera neutral behind bg10

je "Alright, enjoy yourself."

show bg10 with flash

ro "Come on, the portal's open now."

gh "...  Very well."

show bg10 with flash

scene bg21 with fade
show indarah neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Hey there, is our room ready?"

ind "It is, where is your companion?"

ro "Around the back, didn't want to disturb the other guests. I'll just take the drinks and let him in."

ind "Is a bottle of wine good?"

ro "Better make that three to start with, we'll see where we are after that."

show indarah shock at midright with dissolve
ind "Just who is your companion?"

ro "A really big guy. Thanks Indarah."

hide rowan with moveoutleft

#tavern back room
scene black with fade
show rowan necklace neutral at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

ro "Tell me Greyhide, have you ever had Rosarian wine before?"

gh "I have not."

ro "Then I hope you enjoy it. This wine is the speciality of my home country."

"The minotaur took the tankard that Rowan had filled and drank the whole thing in one swig. He was silent for a moment, then smiled down at the man and allowed Rowan to refill his cup."

show greyhide neutral at cliohnaright with dissolve

gh "Tell me about your homeland."

show rowan necklace happy at midleft with dissolve

ro "Rosaria is a land of great plains of grass and crop fields, with pleasant forests and rolling hills. The most wonderful place there for me was always my home village."

"While sipping his own glass, Rowan leaned back in his chair and closed his eyes, picturing his home as he described it."

ro "A lazy morning filled with the laughter of children and the smell of fresh baking, smiling faces and good mornings from the others that you'd lived your whole life with. Then, of course, coming home to the woman I love with all my heart."

gh "I like the sound of your home. So different from mine."

"The elder man picked up the second bottle and used his teeth to pull out the cork. He spat it onto the floor and took a big swig, nearly emptying the whole thing again."

gh "My home was on harsh mountains and caves where we ate moss and tough bushes. Every day was a struggle with another pack mate who wanted be boss or posture for mating power."

show greyhide sad at cliohnaright with dissolve

gh "For a time, there was a woman that I and she had earned our rights to. I defeated all rivals for her, she all for me. Then... she died. An ugly shrew thought herself worthy of me by throwing my love off a cliff."

"He popped open the third bottle and this time he did down the whole thing."

gh "I didn't care to fight for women after that. Nor did I enjoy them fighting for me. It felt so... hollow. Why fight for love? Why cause pain for others so you can feel pleasure?"

"Rowan looked at the last bottle, still half full and handed it to the minotaur as tears started to run down his long face."

ro "I'll be right back with a full barrel of wine."

scene black with fade

"A few hours later."

#tavern back room
scene black with fade
show rowan necklace neutral at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

gh "I may have lived more years than you, but you've seen more pain and battle than three of my lifetimes. I do not envy your scars. I do envy the softness you enjoy with your wife."
gh "Minotaur women are nothing like that, even my love was a passionate beast."

menu:
    "Have you considered trying men?":
        $ released_fix_rollback()
        ro "Have you considered trying men?"
        "The minotaur stared at Rowan for several moments, silent confusion playing over his visage at the suggestion. Then his eyes went wide and he downed two full tankards in a row."
        gh "I shall think about your suggestion."
        #Note that further Greyhide scenes will favor sex with Rowan.
        $ drinking_buddies_suggestion = 'men'
        return

    "Alexia lives at the castle, would you like to meet her?":
        $ released_fix_rollback()
        ro "Alexia lives at the castle, would you like to meet her?"
        gh "I think so. It will be nice to meet your family and learn more of your ways."
        $ drinking_buddies_introduce_alexia = True
        #Note that further Greyhide scenes will favor sex with Alexia or a threesome with her and Rowan.
        return

    "Does having a friend help?":
        $ released_fix_rollback()
        ro "Does having a friend help?"
        show greyhide neutral at cliohnaright with dissolve
        "The minotaur took another drink, looked at his tankard, then up at Rowan.  After a few moments a smile graced his worn visage."
        gh "It does. You may be the first one I've known that understands me."
        #Note that further Greyhide sex scenes should not trigger.
        $ drinking_buddies_suggestion = 'friend'
        return
