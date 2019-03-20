# temporary dict to store event's variables
# should only be used to save vars in event scope
default event_tmp = {}

label rowan_intro:
    python:
        # timestamp in weeks
        week = 0
        # adult mode (NSFW)
        adult = True
        # create avatar Rowan
        avatar = Avatar('Rowan')
        # set variable to show events that this scenario is Rowan's
        Rowan_sc = True
        # add some items to backpack
        avatar.inventory.add_items(('iron_sword', 'leather_straps'))
        # equip 'sword' to main hand
        avatar.inventory.equip('iron_sword')
        avatar.inventory.equip('leather_straps')
        avatar.gold = 100
        avatar.base_strength = 10
        avatar.base_vitality = 10
        avatar.base_reflexes = 5
        avatar.base_intelligence = 5
        avatar.base_luck = 5
        avatar.heal()
        # create castle
        castle = Castle()
        # hide temporary uid
    python hide:
        # create starting buildings
        for uid in starting_buildings:
            castle.buildings[uid].build()
        # unlock first level of some buildings - they are available without research
        castle.buildings['tavern'].max_lvl = 1
        castle.buildings['sanctum'].max_lvl = 1
        castle.buildings['forge'].max_lvl = 1
        castle.buildings['arena'].max_lvl = 1
    python:
        castle.treasury = 200
        castle.morale = 50
        castle.military = 10
        castle.tech = 10
        castle.rp = 10
        castle.buildings['barracks'].troops =2
        # create outer lands
        lands = Lands(all_realms, all_locs)
        # enable one loc for debug
        # lands['rosaria']['rastedel'].visible = True
        # lands['rosaria']['rastedel'].accessible = True
        lands['prothea'].accessible = False
        lands['tundra'].accessible = False
        lands['forest'].accessible = False
        lands['dragons_tail'].accessible = False
        lands['empire'].accessible = False
        lands['rosaria'].accessible = False
        askcellmate = False
        # disable some parts of the game (only controls are disabled)
        systems = Systems()
        # create first map
        world = World()
        m = create_map_from_file("maps/rosaria map.json")
        world.maps[m.uid] = m
        del m
        # create the trader of the castle shop
        castle_shop_trader = Avatar('Cla-Min')
        castle_shop_trader.gold = 10000
        castle_shop_trader.inventory.add_items(('leather_jerkin', 'studded_coat', 'robe', 'cloth_hat', 'gloves', 'shoes', 'studded_coat', 'leather_helm', 'studded_helm', 'leather_gloves',
            'studded_gloves', 'leather_boots',
            # temp weapons/shields
            'iron_rapier', 'bastard_sword', 'zweihander', 'wooden_shield', 'buckler', 'knights_shield'))
        # create NPC actors
        jezera = Actor('jezera', 'Jezera')
        andras = Actor('andras', 'Andras')
        jezera.inf_corruption = True
        andras.inf_corruption = True
        Actor('alexia', 'Alexia')
        all_actors['alexia'].relation = 70
        Actor('cla_min', 'Cla-Min')
        Actor('solancia', 'Solancia')
        Actor('skordred', 'Skordred')
        Actor('kharos', 'Kharos')
        Actor('fey', 'Fey')
        Actor('draith', 'Draith')
        Actor('cliohna', 'Cliohna')
        Actor('xzaratl', 'X’zaratl')
        Actor('tamir', 'Tamir')
    # create rumors
    call create_rumors from _call_create_rumors
    # init journal
    python:
        journal = Journal()
        # hide journal in the prologue
        journal.hide()
        for entry in ['checks_start', 'checks_partial', 'corruption_start', 'corruption_increasing', 'gold_start', 'intelligence_start',
            'luck_start', 'primary_statistics', 'reflexes', 'skills', 'strength', 'vitality']:
            journal.glossary_add(entry)
        for entry in ['rowan_starting', 'alexia_starting', 'village_elder_starting', 'karnas_starting', 'deanara_starting', 'jezera_starting',
            'andras_starting', 'arthdale_starting', 'bloodmeen_starting', 'punishment', 'solansia_starting', 'kharos_starting', 'six_realms_starting',
            'solance_starting']:
            journal.codex_add(entry)


if (persistent.prologue_complete == True):

    scene black

    "Would you like to skip the prologue?"

    menu:
        "Yes":
            $ renpy.block_rollback()
            $ prologueSkip = True
            jump rowangamestart

        "No":
            $ renpy.block_rollback()
            $ prologueSkip = False
            jump rowanprologuestart

else:
    $ prologueSkip = False
    jump rowanprologuestart

label rowanprologuestart:

play music "music/village loop.ogg" fadein 2.0
show bg1 with fade

pause 1


"Our story begins in the village of Arthdale, a small hamlet in the Rosarian Valley. The village itself, to a person who did not know better, would seem like any other small peasant village in Rosaria."
"During the day the sounds of the clang of a blacksmith’s hammer and children at play fill the air, while the villagers go about their daily business. At night the local tavern is home to farmers returning from long days at work in the field. The village inn has very few visitors."
"It would be truly unremarkable if it were not for the fact that one of its inhabitants had played a major part in the victory against the last Demon Lord. Rowan Blackwell, along with his companions, had defeated Karnas and saved the Six Realms from eternal darkness."
"Seven years had passed since that fateful day, and our hero now lived out his days in the peace of uneventful village life with his childhood sweetheart and wife, Alexia."

show village elder happy at midright with dissolve

el "Ah, Rowan, there you are. Back from your morning patrol, already?"

show rowan intro happy at midleft with moveinleft

ro "I like to set out early while Alexia is still asleep, that way I avoid disturbing her. Even after all these years, I still have trouble sleeping past sunrise."

el "I often find myself wondering why you still do them, we’ve never had much trouble around here. Even during the war, the fighting never made it this far South."

menu:
    "We must remain vigilant.":
       $ renpy.fix_rollback()
       $ patrol = 1
       show rowan intro neutral at midleft with dissolve
       ro "The price of peace is eternal vigilance. Karnas was not the first Demon Lord and he won’t be the last. One always rises to take the place of the fallen, and it is in complacency that corruption springs anew."
       jump vigilant

    "Old Habits die hard.":
        $ renpy.fix_rollback()
        $ patrol = 0
        $ bandits = 0
        ro "Old habits die hard, I suppose. I spent so much time in the field scouting during the war that I got used to being alone in the wild. I like the solitude, it gives me time to clear my head."
        jump habits

    "Exercise is important.":
        $ renpy.fix_rollback()
        $ patrol = 0
        $ bandits = 0
        ro "The long walks are good exercise and without the fighting to keep me fit, I need something to stop me from putting on weight. And you know what my wife’s cooking is like, she could feed the entire village. I swear the woman is trying to fatten me up like a cow."
        jump exercise

label vigilant:

el "The process usually takes a long time, my young friend, and I fear your patrols may be a few hundred years too early."

ro "Perhaps, but it never hurts to be careful, especially with the rumours that bandits have been seen near the western Woods."

el "The bandits will not bother us, they know better than to attack the town where the hero of the siege of Karst lives."

ro "I fear my name no longer carries the weight you ascribe to it, but even so. Desperate times often make men foolhardy, and without the chaos of war, bandits find themselves with lean pickings. Even a village as small as ours begins to look like a ripe target."

el "You’ll have to forgive an old man his optimism, Rowan. When you are as ancient as me, you might also find yourself pushing away the dark thoughts."
el "Did you see any such signs of trouble on your travels?"

menu:
    "Yes.":
       $ renpy.fix_rollback()
       $ bandits = 1
       ro "I did not venture far into the western woods, but even at the edge of the forest I could see signs that someone had passed through the woods recently. Judging from the tracks and the broken low boughs, I would say at least half a dozen men, with a cart trailing."
       el "We will just have to hope that they keep to the forest and leave us be."
       show rowan intro happy at midleft with dissolve
       ro "I had best be getting home, Alexia will be waiting for me, and I would not want to worry her."
       el "Yes, you’d better go before I get into trouble for keeping you so long. Give her my regards."
       ro "I will. See you soon, my friend."

    "No.":
        $ renpy.fix_rollback()
        $ bandits = 0
        show rowan intro happy at midleft with dissolve
        ro "The only trouble I saw was the Longwater twins on my way back into town, up to no good as usual. They were playing crusade again, and little Allie was pretending to be Karnas. The faces she pulls are almost as terrifying as the real thing."
        el "You would know, Rowan."
        ro "I had best be getting home, Alexia will be waiting for me, and I would not want to worry her."
        el "Yes, you’d better go before I get into trouble for keeping you so long. Give her my regards."
        ro "I will. See you soon, my friend."



jump scene1end

label habits:

el "I used to take a lot of long walks myself, back when I was a younger man. It never hurts to get away from it all for a little while. It has been a long time since I last left the village though. Too much trouble for these old bones these days, I’m afraid."

ro "You are not that long in the tooth just yet, old man."

el "Do not fret, my child. None but the gods live forever, and the Goddess has blessed me to live this long."

ro "You should not talk like that. I am sure you will be here for many more years to lecture us about the good old days."

el "I truly hope so, Rowan, but I have had a good life. I got to spend nearly fifty years with the woman I loved, and while we never had any children, seeing you, Alexia, and the rest of the village’s children grow gave us such joy."
el "When the time comes to join my Maris is the world that lies beyond this one, I shall do so without regrets."

ro "Come now, my old friend, it is too nice a day for all this talk of death. We should leave such dark subjects for drearier times."

el "Indeed, and you have a beautiful wife that you had best be getting home to instead of spending time with an old fool."

ro "I’ll give her your regards, my friend. Take care of yourself."

el "You too, Rowan."


jump scene1end

label exercise:

el "You should not complain too much, Rowan. Nearly fifty years I spent married to a woman, the Goddess rest her soul, who could not cook to save her life."

ro "Maris’ cooking was not that bad, surely?"

el "You try eating meat as tough as an old boot seven nights a week, that is the mark of true love. And now she has gone, would you believe I miss it?"

ro "I’m sure she is looking on, from the world beyond, and waiting for the day that you will be together again."

el "If she is, she is probably cursing me for bad mouthing her cooking. Another week of back pain!"

ro "Speaking of being cursed by wives, I should get home. Mine is probably wondering where I am by now."

el "Give Alexia my best, and thank her for the food she sent over for a poor old widow."

ro "I will. Try not to get into too much trouble between now and when next I see you."

el "I’m not making any promises."




jump scene1end

label scene1end:

hide village elder happy at midright with dissolve
hide rowan intro happy at midleft with moveoutright


scene bg2 with fade

pause 0.5

show rowan intro happy behind bg2 with dissolve


ro "Alexia? Are you home, my love?"

show alexia intro neutral at midleft with dissolve

al "I’m just in the kitchen cleaning up the mess I made making dinner. How was your walk?"


if (patrol == 1) & (bandits == 1):
    menu:
        "Tell her about the bandits.":
            $ renpy.fix_rollback()
            ro "I noticed some signs of life in the western woods; bandits, I suspect. I am not too worried, it is probably nothing, but I’ll have to be extra cautious for the next few days. Better safe than sorry, after all."
            show alexia intro concerned at midleft with dissolve
            al "Please be careful, Rowan. I spent so many nights worrying about something happening to you the years you spent away during the war, and I could not stand the thought of losing you now to some common bandits."
            ro "I always am, darling. Do not fret over me, I will just keep an eye on the situation in case they aim to attack the village. Anything other than that, I will leave it to the Duke’s men to deal with."
            show alexia intro neutral at midleft with dissolve
            al "Good. You spent enough years away playing the hero, and while the rest of the Six Realms may not feel the same, I much prefer you here to play husband."

            menu:
                "Molest her from behind.":
                    $ renpy.fix_rollback()
                    ro "You do, do you? Well, how about I play a little husband for you right now?"
                    jump sexscene1

                "Leave her be":
                    $ renpy.fix_rollback()
                    jump intronosex



        "Avoid worrying her by lying.":
            $ renpy.fix_rollback()
            ro "I took my usual route and found that there is nothing to worry about, darling. We have not had any trouble for the past seven years, and I doubt we will see any anytime soon."
            al "I’m glad to hear that. It has been so peaceful since you returned from the war, those years you were away feel more like a bad dream than actual reality."
            ro "I try not to think about them myself, it is a life I’m not eager to go back to. As far as I can help it, I will not leaving again, I have done enough travelling for one lifetime."
            al "You had better not be planning on going anywhere, or you will be in real trouble, mister hero."

            menu:
                "Molest her from behind.":
                    $ renpy.fix_rollback()
                    ro "Would I now? And what sort of trouble would that be, pray tell? This kind, perhaps?"
                    jump sexscene1

                "Leave her be":
                    $ renpy.fix_rollback()
                    jump intronosex

elif (patrol == 1) & (bandits == 0):
    ro "Well, I guess that would depend on your feelings about the Longwater twins, the pair were up to their usual mischief. Other than that, it was uneventful, as always."
    al "You leave those poor children alone, they are just trying to have some fun. You forget that I remember when you were their age, and all the trouble you used to get into."
    ro "Me? Trouble? I was a little angel."
    al "A devil more like, it is surprising you did not side with Karnas instead of the forces of Light."

    menu:
                "Molest her from behind.":
                    $ renpy.fix_rollback()
                    ro "A devil am I? Well, if I am going to be accused of being a devil, I may as well act like one."
                    jump sexscene1

                "Leave her be":
                    $ renpy.fix_rollback()
                    jump intronosex

elif (patrol == 0) & (bandits == 0):
    ro "Uneventful, thankfully. There’s few travellers on the road to Rastedel, and the western woods seems quiet. Most of the people I saw were farmers off to work the fields, it looks like they will have a good harvest this year."
    al "I’ve heard the same from some of the women in the village. There is already talk of a feast to be held in honour of Diannan, to give thanks for her blessing."
    ro "Which we will have to attend, no doubt? I bet you have already told them we will be there. It was bad enough with all the parades after the war, and now the village is starting to follow suit."
    al "I know you hate these things, but it would be terribly bad manners not to attend. Whether you like it or not, you are an important person around here."
    al "Plus, it would probably not hurt to stay on the good side of a goddess, you know."

    menu:
        "Molest her from behind.":
            $ renpy.fix_rollback()
            ro "Very well, I suppose I will have to go with you then. But if I do this for you, I think it is only fair that you do a little something for me in return."
            jump sexscene1

        "Leave her be":
            $ renpy.fix_rollback()
            jump intronosex


label sexscene1:


show cg1 with dissolve
pause 2

show alexia intro neutral behind cg1 with dissolve
show rowan intro happy behind cg1 with dissolve

"Quickly, without making a sound, Rowan slid up behind his unsuspecting wife as she was washing the dishes and grabbed her by the hips, pulling her ass to his crotch."
"With both of her hands busy with the task, she was left defenseless as he began to gently kiss the pale, exposed flesh of the nape of her neck."

voice "music/Voice/Alexia_light_breath_1.ogg"
al "Uhhhh... I am trying to wash the dishes here, husband, and you are not exactly helping."

show rowan intro smug behind cg1

ro "What? I am not stopping you, am I? Your hands are perfectly free to continue doing what they are doing."

"As Rowan continued to plant soft kisses down the length of her unguarded neck, Alexia’s breaths grew both shorter and shallower, and her skin more flush."

show alexia intro aroused behind cg1 with dissolve

voice "music/Voice/Alexia_light_breath_2.ogg"
al "You might not be stopping me, dear heart, but you are making it awfully difficult for me to concentrate on cleaning these plates."

ro "I’m sorry, I did not realize that you found it so distracting. I suppose if I were to do this, it would not help?"

"While he continued his assault on her neck, Rowan slid one hand down to caress her thigh."

voice "music/Voice/Alexia_very_light_moan_2.ogg"
al "No, husband, that definitely does not help."

ro "How about this?"

"With a grin, he moved his other hand from her hip, slowly up her stomach until he found her left breast. Placing his hand over her tit, he lightly grazed her erect nipple, eliciting a soft, low moan."

voice "music/Voice/Alexia_light_moan_2.ogg"
al "Nnnnnn... What do you think?"

ro "I don’t know, that is why I am asking you."

menu:
    "Threaten to stop.":
        $ renpy.fix_rollback()
        ro "I guess I had better stop then. I would not want you telling the villagers about how I keep you from doing your work at home."
        "Taking his hands from her body, he places them on the counter at either side, and arcs backwards so they are no longer touching."
        al "Did I tell you to stop, darling?"
        ro "I thought your husband was being naughty and distracting you?"
        al "He is, but I never said that it was a bad thing."
        ro "Oh really?"
        jump alexia_foreplay_beg

    "Tease her harder.":
        $ renpy.fix_rollback()
        show rowan intro aroused behind cg1
        ro "In that case, I guess I will just have to keep touching you until you give me a proper answer then."
        "With that, Rowan began to massage her thigh while using the other hand to grope her tit roughly."
        voice "music/Voice/Alexia_light_moan_2.ogg"
        al "Uhhhh...."
        voice sustain
        "Sliding the hand on her thigh under her dress, he pressed it against her underwear and gently rubbed her wet pussy."
        voice "music/Voice/Alexia_medium_moan_2.ogg"
        al "Ohhh yessssss...."
        voice sustain
        ro "Somebody is practically sodden down there."
        al "What do you expect when you are fondling me like that, dear?"
        jump alexia_bj_intro

label alexia_foreplay_beg:
menu:
    "Resume foreplay.":
        $ renpy.fix_rollback()
        show rowan intro aroused behind cg1
        "Rowan resumed what he was doing, groping one breast, while he slid the other under her dress to massage her clit."
        voice "music/Voice/Alexia_medium_moan_1.ogg"
        al "Ohhh yessssss...."
        jump alexia_bj_intro

    "Make her beg.":
        $ renpy.fix_rollback()
        ro "If you want me to restart, you are going to have to tell me what you want me to do to you."
        al "I want you.... to touch me..."
        ro "You are going to have to be a lot more specific than that."
        al "I want you to grope my breasts..."
        show rowan intro aroused behind cg1
        "Rowan placed one hand back on her breast, squeezing the nipple hard."
        ro "Like this? And what else?"
        voice "music/Voice/Alexia_heavier_breath_2.ogg"
        al "Uhhuhhh... and stroke my..."
        ro "Stroke your what?"
        voice "music/Voice/Alexia_medium_moan_1.ogg"
        al "Ohhhhh... my pussy, you bastard."
        ro "No need for the name calling, all you have to do is ask."
        "He moved his hand beneath her dress and under the panties, sliding two fingers between her wet cunt lips."
        jump alexia_bj_intro

label alexia_bj_intro:

ro "Since I have made you feel good, how about you do the same for me?"

voice "music/Voice/Alexia_light_moan_1.ogg"
al "Mmmmm.. What did you have in mind?"
voice sustain
ro "I can think of a few things."
"Emphasizing his point, he pressed his hard cock against her ass."

al " I take it that is not your sword?"

ro "Nope."

al "And what exactly would you like me to do with that?"

menu:
    "Ask her to blow you.":
        $ renpy.fix_rollback()
        ro "How about you give it a little kiss?"
        show cg2 with dissolve
        pause 2
        voice "music/Voice/Alexia_light_sucking_1.ogg"
        "Alexia knelt down in front of Rowan and pulled his hard cock free from his trousers. Grabbing it at the base, she placed a soft kiss on the shiny, purple head."
        voice sustain
        al "Like this?"
        voice sustain
        "With a grin, Alexia started to run her tongue along the head of her husband’s cock with long, slow licks, while she gently worked the shaft with her hand."
        voice sustain
        ro "That’s it..."
        voice sustain
        "Taking the head of his cock into her mouth, she sucked on it lightly while continuing to stroke the shaft."
        "As she sucked, she started to swirl her tongue, licking the sensitive tip, causing Rowan to let out a low moan."
        voice "music/Voice/Alexia_light_sucking_2.ogg"
        "Enthused by his reaction, Alexia bobbed her head back and forth, her soft lips rubbing up and down the length of his throbbing cock."
        voice sustain
        "Rowan began to subconsciously move with her, slowly moving his hips back and forth."
        voice sustain
        ro "That feels so good..."
        al "Mmmmmfff!"
        voice "music/Voice/Alexia_sloppy_sucking_3.ogg"
        "She continued to work his dick at the base with her hand, while sucking on the head and the shaft in a slow, deliberate manner."
        voice sustain
        "Before long, Rowan’s dick was covered in spit and every movement of her head was accompanied by a sloppy squelch."
        voice sustain
        "Rowan placed his hand on her head and braced against the window frame to steady himself, as climax was starting to rise within him."
        "Feeling him begin to shudder, Alexia stopped sucking on his dick and grabs it by the base."
        ro "I’m so close...."
        "Keeping a tight grip, she backws off until his cock was no longer inside her mouth, and grinned up at him."
        al "Not yet, husband, I have somewhere else that I would like you to put it before you finish."
        jump alexia_rowan_bedroom


    "Push her head down.":
        $ renpy.fix_rollback()
        show cg2 with dissolve
        pause 2
        "Without a word, Rowan pushed Alexia’s head down to his crotch while freeing his hard dick from his trousers with his other hand."
        "Before she could utter a word of protest, he shoved his cock into her mouth, a wide o of shock from the rough behaviour."
        al "Mmmmffffph!"
        voice "music/Voice/Alexia_sloppy_sucking_1.ogg"
        "With her lips now wrapped around his cock, Rowan moved his hips back and forth, gently, to simulate fucking her, enjoying the wet, warm sensation he felt as it slides in and out of her mouth."
        voice sustain
        "On her knees, and in a position in which she felt powerless, all Alexia could do was accommodate his manhood as best as she could, sucking on it as he pistoned his hips back and forth."
        voice sustain
        "Bracing himself against the under ledge of the window, Rowan placed his hand on her hair and stroked it as he fucked her mouth to a symphony of squelching sounds."
        voice "music/Voice/Alexia_heavier_slurping_3.ogg"
        "His wife was enthusiastically slurping away as he bucked his hips to a steady rhythm, doing her best to deliver a good, sloppy blowjob."
        voice sustain
        "Rowan pulled his dick from her mouth, glistening in the sun from being covered with all of the excess saliva."
        voice sustain
        ro "Ready to take it deeper, baby?"
        voice "music/Voice/Alexia_light_moan_1.ogg"
        al "Ohhhh.... Uhhuhh..."
        voice "music/Voice/Alexia_glug_glug_3.ogg"
        "Smirking, Rowan pushed his cock back between her soft lips, and began to move his hips once more, faster and rougher."
        voice sustain
        "Alexia tried her best to avoid gagging by breathing through her nose as her husband’s fat cock slid in and out of her throat."
        voice sustain
        "The room was filled with the glug glug glug sound of her gag reflex, and the slapping noise produced by the meeting of Rowan’s ass and the window ledge."
        ro "Unnnn... you are amazing..."

        menu:
            "Make her deepthroat you.":
                $ renpy.fix_rollback()
                ro "I am going to put it in all the way now, okay?"
                voice "music/Voice/Alexia_light_gagging_3.ogg"
                al "Glggf!"
                voice sustain
                "With one last thrust, Rowan pulled her head against his crotch, forcing her to take it all in her throat."
                voice sustain
                "Alexia did her best to take the entire length without gagging, deepthroating it admirably. She could feel it quiver as it pressed against her lips, so close to cumming."
                "Before that happened, however, Rowan pulled it free, now dripping with spit, and grabbed it by the base, prolonging the orgasm. His wife looked up at him in surprise."
                jump alexia_rowan_bedroom

            "Take it to the bedroom.":
                $ renpy.fix_rollback()
                "Taking his cock from her mouth, Rowan reached down to offer his hand and aid his wife in rising."
                jump alexia_rowan_bedroom

label alexia_rowan_bedroom:

ro "Are you ready to move this to the bedroom, darling?"
voice "music/Voice/Alexia_very_light_moan_3.ogg"
al "Mmmmhmmmm..."

show cg3 with dissolve
pause 2

show alexia intro aroused naked behind cg3 with dissolve
show rowan intro aroused naked behind cg3 with dissolve

"The pair moved the action to the bedroom, where Alexia led on her side to allow Rowan to take her from behind."
voice "music/Voice/Alexia_light_moan_3.ogg"
"Rowan led beside her and lifted her leg slightly to position himself between her wet and willing pussy lips. As he slid his cock between them, Alexia let out a long, loud moan."
voice sustain
"Rowan placed his arm around her waist and with a grunt started to move against her, taking care at first to move slowly."
voice "music/Voice/Alexia_medium_moan_3.ogg"
"With gentle thrusts of his hips, his dick slid in and out of her cunt, which caused her to cry out in pleasure."
voice sustain
"The friction from her well lubricated labia felt so good that his manhood pulsed from the sensation with each and every thrust."
voice sustain
"He leaned in to place soft kisses on her neck as he continued to buck his hips, his flat stomach slapping away against her pert, round ass."
"As he continued to pound away on her pussy with care, he leaned forward to whisper in her ear."

ro "Are you okay, darling?"

voice "music/Voice/Alexia_light_moan_1.ogg"
al "Uhhhuhhhh... Don’t stop..."

menu:
    "Keep going at the same speed.":
        $ renpy.fix_rollback()
        "Rowan continued to move against her, while softly kissing her neck. Her breaths grew shallower, and her moans louder as he brought her closer and closer to climax."
        voice "music/Voice/Alexia_heavier_moan_2.ogg"
        "Sliding his hand down from her waist, he softly rubbed her clit as he fucks her lovingly, causing her to cry out."
        voice sustain
        ro "I’m close, honey..."
        voice sustain
        al "Ohhhh... me tooo..."
        ro "Let’s come together..."
        voice "music/Voice/Alexia_heavier_moan_1.ogg"
        al "Yessssss..."
        voice sustain
        "He moved his arm back up to clinch her waist and gave it one last hard, deep thrust."
        voice "music/Voice/Alexia_climax_2.ogg"
        show cg3 with sshake
        show cg3 with sshake
        show cg4 with flash
        pause 2

        "Alexia orgasmed loud and incoherently as he flooded her sodden pussy with his cum, and then collapsed beside her, still inside of her."
        voice sustain
        "She pushed back against him as he spooned her, snuggling against his neck."
        al "Mmmm... Love you."
        "Rowan planted a soft kiss on the crown of her head."
        ro "Love you more."
        al "You have worn me out now, and I have so many things to do today."
        jump intro_scene3

    "Be rough with her.":
        $ renpy.fix_rollback()
        "Using the arm wrapped around Alexia’s waist for leverage, Rowan began to fuck her harder, pounding his dick against her wet pussy."
        voice "music/Voice/Alexia_heavier_moan_1.ogg"
        "The sudden change in pace caused her to cry out in surprise."
        voice sustain
        ro "You love it rough, don’t you slut?"
        voice sustain
        al "Nnnnn... I’m not... a...."
        "Unimpressed by the answer, Rowan gave her hair a sharp tug."
        ro "What was that, slut?"
        voice "music/Voice/Alexia_heavier_moan_3.ogg"
        al "Yesssss!!"
        voice sustain
        ro "That is what I thought."
        voice sustain
        "Close to climax, he leaned in to bite her neck as he made one last forceful thrust, pushing his cock deep inside her."
        voice "music/Voice/Alexia_climax_1.ogg"
        show cg3 with sshake
        show cg3 with sshake
        show cg4 with flash
        pause 2
        voice sustain
        "Alexia screamed loud in orgasm as her husband filled her pussy with his warm, sticky seed."
        "Rowan pulled his cock out with a satisfying pop as she led there, blissfully cooing, while cum leaked from her cunt."
        al "Gods, husband, where did that come from?"
        ro "Enjoyed that, did you?"
        al "I am not complaining, but my legs feel like they are made from jelly."
        jump intro_scene3

label intro_scene3:

# mark sex_scene1 completed and ready for replay
$ persistent.sex_scene1 = True
# end of sex_scene1 replay
$ renpy.end_replay()

show alexia intro naked behind cg4 with dissolve
show rowan intro naked behind cg4 with dissolve

al "Dinner is going to be ruined, you know."

ro "I think I can live with that, darling."

al "I suppose I should just be thankful the house did not burn down as a result of your horniness. Goddess fend."

ro "I have not the faintest idea what you mean, my love. If anything, it is your fault for being so beautiful."
ro "I would have to have the willpower of a god to resist, and I am just a man, after all."

"Alexia leaned in close and gives him a long, deep kiss before sitting up and sliding her legs off the bed."

al "Flattery will get you everywhere, husband."
al "I better go and see if there is anything left in the kitchen for me to salvage. I’m sure you’ve worked up an appetite after that."

"As she tried to stand, she collapsed back onto the bed, and started to giggle uncontrollably."

show alexia intro naked laugh behind cg4 with dissolve
al "I think my legs may need a few more minutes."

"Her giggle proved infectious, as Rowan joined in with the laughter. As the pair sat on the bed, lost in the joy of each other’s company, they were soon interrupted by an unexpected arrival."

stop music
pause 0.5
play sound "music/SFX/door knock.ogg"
pause 1

show rowan intro neutral naked behind cg4 with dissolve
show alexia intro concerned naked behind cg4 with dissolve

ro "Are you expecting anyone?"

al "Only Nemma, but she is not due until after her husband comes home."
al "She is teaching the children today, so it is very unlikely that it will be her."

play sound "music/SFX/door knock.ogg"
pause 1

al "Whoever it is, it sounds urgent. It could be someone in trouble."

ro "Wait here, I will go and see who it is."

al "Be careful."

show rowan intro naked behind cg4 with dissolve

ro "I always am."

play sound "music/SFX/door knock.ogg"
hide alexia intro neutral with dissolve
pause 1

scene bg2 with fade
show rowan intro neutral at midright with dissolve

jump jezarrives


label intronosex:

stop music
pause 0.5
play sound "music/SFX/door knock.ogg"
pause 1

scene bg2

show alexia intro concerned at midleft with dissolve
show rowan intro neutral at midright with dissolve


ro "Are you expecting anyone?"

al "Only Nemma, but she is not due until after her husband comes home."
al "She is teaching the children today, so it is very unlikely that it will be her."

play sound "music/SFX/door knock.ogg"
pause 1

al "Whoever it is, it sounds urgent. It could be someone in trouble."

ro "Go and wait in the other room, I will see who it is."

al "Be careful."

ro "I always am."

play sound "music/SFX/door knock.ogg"
hide alexia intro neutral with dissolve
pause 1

jump jezarrives


label jezarrives:

ro "One moment, I am coming."

show cg5 with dissolve
play music "music/Jezera 1 loop.ogg" fadein 1.0
pause 2
show jezera disguised hood worried behind cg5

"Rowan opens the door to discover, standing before him, a beautiful young woman. Drawn around her is a red cloak, the hood pulled up to conceal her pale silver hair."
"Her attractive face wears a look of extreme worry, something is clearly very wrong."

$ jezera_name = '???'

je "Thank Solansia you are home, Hero, I need your help. It is my daughter, she’s... she’s..."

"Before she can get the rest of her sentence out, the woman bursts into tears."

ro "Please, come sit down. Let me find you something to wipe your eyes. Just try and breathe."

hide jezera disguised hood worried
hide rowan intro neutral
hide cg5
show jezera disguised hood crying at midleft with dissolve

"Rowan roots around the room until he finds a small scrap of cotton from his wife’s sewing materials, suitable for use as a makeshift handkerchief."

show rowan intro neutral at midright with dissolve

ro "Here, take this."

"He hands it to the distressed young lady, who uses it to dry the tears falling from her striking gold eyes, as she sniffles."

show jezera disguised hood worried at midleft with dissolve

je "Thank you."

show rowan intro happy at midright with dissolve

"Awkwardly, she tries to return the handkerchief, but Rowan just smiles as he motions for her to keep it."

ro "Now, let us start with something easy - What is your name?"

$ jezera_name = 'Mariel'

show jezera disguised worried at midleft with dissolve

je "Oh, Goddess fend, where are my manners? My name is Mariel. "

"With that, she bows her head slightly and offers her hand. Rowan takes it briefly, recalling the many women he had met at all of the balls following the triumph of the crusade. High born this one, he thinks."

ro "Nice to meet you Mariel. I am Rowan. Now what’s all this about your daughter?"

je "I know who you are hero, that is why I came here. Please help me, my daughter—"
je "Oh, gods, it’s terrible!"

show jezera disguised crying at midleft with dissolve
show alexia intro concerned at edgeright with dissolve

"With a cry, Mariel slumps down in the seat, covering her face with her hands. At that moment, Alexia reenters from the other room, having heard a woman's voice."

al "Is she alright?"

show rowan intro neutral at midright with dissolve

ro "Seems there has been some sort of trouble with her daughter, truth be told I am having a hard time getting it out of her."

al "What is her name?"

ro "Mariel."

al "Okay. Let me try a softer approach, darling."

show rowan intro happy at midright with dissolve

ro "You do have your ways."

show alexia intro neutral at edgeright with dissolve

"Alexia goes over to the side of the room where the other woman is sat, weeping, and places her arm around her in a delicate manner as not to startle her."

al "Come now, Mariel, everything will be fine, I am sure. My name is Alexia, I am Rowan’s wife. You just try to tell Rowan what the problem is, and I will make you something hot to drink."

show jezera disguised neutral at midleft with dissolve

"The simple act of kindness seems to have helped Mariel regain her composure, as she sat up straight, removing her hands from her face."

je "Yes. Thank you, that is very kind."

hide alexia intro neutral at edgeright with dissolve

ro "Try to stay calm, and tell me about what has happened as best you can, starting at the beginning."

je "We are returning to Prothea from Uvarth, where we had been visiting family. We had hoped to return earlier in the year, but heavy snowfalls had made the mountains impossible to traverse."
je "When the first thaws came, we left for home with two knights of the house of Aurald as protection, owing to rumours of ogre sightings, believed to be hiding out in caves up in the passes."

show alexia intro neutral at edgeright with dissolve

"Alexia returns with a cup and hands it to her."

je "Thank you, Alexia."
je "The journey was uneventful though. Once we left the mountains behind, the knights took their leave to return to Uvarth, believing Rosaria to be peaceful enough for us to travel on alone."

ro "Not an unfair assumption, there is very little trouble about these days. Travellers are generally very safe as long as they stick to the trader roads."

je "That was also my thought, so I had no objection to the knights returning home. And everything was peaceful, until yesterday."

al "Was that when something happened to your daughter?"

je "Yes. We were camped in the fields not far from here, hoping to make our way to Rastedel today."
show jezera disguised worried at midleft with dissolve
je "But when I woke this morning, my Nera was nowhere to be found. "
je "I searched the fields all morning, asking farmers and other travellers if they had seen her, but nobody had. I can only think that she somehow has ended up in the western woods."
je "If something has happened to her, I do not know what I will do. I can’t lose her... I..."

show jezera disguised crying at midleft with dissolve

"The thought that something may have happened to her child is too much for Mariel to bear, and she begins to sob uncontrollably again."

menu:
    "Be honest.":
        $ renpy.fix_rollback()
        ro "If she vanished in the night, it is unlikely that she wandered off by herself."
        if (patrol == 1) & (bandits == 1):
            ro "I noticed signs of bandits in the area earlier this morning, and they may have taken her to ransom or to sell to slavers."
            ro "They will not of harmed her, they would not want to decrease the value of the ”merchandise”. Do not worry, I will find them and return her to you, I swear."
            jump marielthank

        else:
            ro "Someone, or even something, probably took her, but do not worry, whatever has happened, I will find her."
            jump marielthank

    "Console her.":
        $ renpy.fix_rollback()
        ro "I am sure she is perfectly fine. You know what children are like, she probably got curious and wandered off in the night. I bet she is just lost, and I am good at finding lost things. I will find her, I promise you."
        jump marielthank

label marielthank:

show jezera disguised happy at midleft with dissolve

je "You will? Oh thank you, thank you so much! I do not know how I will ever be able to repay you."

show jezera disguised neutral at midleft with dissolve

ro "There is no need for any repayment, Mariel. Kindness costs nothing, and  the Goddess teaches us that we should always help those that are in need."
ro "I will get my things and leave immediately, we do not want her out there after the sun goes down."

hide rowan intro happy with dissolve

"Rowan leaves the pair to recover his equipment, kept in storage for the better part of the last seven years."
"He had taken the blade out every now and then to oil it, a process that had been drilled into him during his military years, but other than that, it had laid untouched."

show rowan happy at midright with dissolve

"When he returned he found the pair chatting away and laughing, and he marveled at his wife’s ability to put other people at ease."
"Her warmth, and her willingness to share it with others was just one of many reasons he had fallen in love with her."

al "I hoped I would never have to see those things again, husband"

ro "And I had hoped I would never have to wear them, but on the bright side, at least they still fit me."

al "It is not exactly the best time for your sense of humour."

ro "Everything will be fine, I am only taking my sword as a precaution. I will be back before you know it. You just keep Mariel company and try to stop her worrying so much."

al "Okay, I will. Be safe."

show jezera disguised worried at midleft with dissolve

je "Please be careful, Rowan. I would hate for something to happen to you when you are trying to help me..."

ro "Do not worry about me, I am tougher than I look."

hide rowan happy with dissolve

"With a wink, Rowan leaves the pair to search for the child."

show jezera disguised neutral at midleft with dissolve

al "Now, tell me all about life in the Holy City."

stop music fadeout 1.0

scene bg1 with fade
play music "music/village loop.ogg" fadein 1.0

show village elder happy at midright with dissolve
show rowan neutral at midleft with moveinleft

el "This does not look good."

ro "A traveller’s child is missing, she may have just wandered off, but likely there is something more sinister involved."

el "Do you think she has been abducted?"

ro "Perhaps, I am heading to the western woods now, the mother thinks that is where she might be."

el "I will send Tobias to Rastedel to inform the Duke. We pay our tithes like everyone else, and are entitled to his protection."

ro "Even so, the Duke’s men would not get here until the morning. It is not a bad idea though, at the very least they could escort the lady and her child on, if they are not needed."

el "I will not delay you any longer. Take care, my friend."

hide rowan neutral at midleft with moveoutleft
stop music fadeout 1.0

scene bg3 with fade
play music "music/songbirds.ogg" fadein 1.0

"A few hours later..."

show rowan neutral at midleft with dissolve

"Rowan had found a trail at the edge of the woods, and followed it into the interior. At a glade, somewhere deep inside, he kneels to inspect the ground."

ro "These footprints must be hers, they are too small to be those of an adult, but they just seem to vanish into thin air."

"Rowan looks up into the canopy above him, perhaps she had climbed a tree in order to get her bearings from a higher vantage point, or even to avoid danger?"

"Returning to his feet, he surveys the landscape around him."

ro "Nothing else has passed through to disturb the soil, and there is no water nearby either to mask her tracks, this one is a real mystery."
ro "Hmmm?"

stop music
play sound "music/SFX/arrow_tree_thud.ogg"
pause 2
play music "music/Orc Ambush loop.ogg" fadein 1.0

"From somewhere within the thick brush, an unseen assailant looses an arrow. Luckily for Rowan, it misses its mark, flying harmlessly past him and embedding itself in a nearby tree."

show rowan shock at midleft with dissolve

ro "An attack?!"

show wild orc neutral at orcright with dissolve
show rowan neutral at midleft with dissolve

"Half a dozen orcs emerge from the trees around him, surrounding him. Rowan could see no way out except through them. The largest one, their leader he reasoned, stepped forward. Confident in the odds, no doubt."

ro "Where is the girl?"

wo "Is no girl."

ro "What do you mean?"

wo "Is no girl. Never was. Is trap. You stupid human, fall for trap like all other stupid humans."

"The realization hit Rowan like the twist of a knife in his stomach - if this was a plan to trap him all along, then Alexia and the rest of the village were in even more danger than he was."

show rowan attack at midleft with dissolve

pause 1

"He had to get back there. He fingers the grip of his sword and eyes the orcs before him. The only way out is through."

wo "I know what you thinkin’, don’t be stupid human, be smart human for change. Just put weapon down, don’t make fuss."

ro "Can’t do that, I’m afraid."

wo "Shame, we haveta kill you then. Boss won’t be pleased."

menu:
    "Attack.":
        $ renpy.fix_rollback()
        ro "You are certainly welcome to try."
        jump wildorcfight

    "Try to reason with him.":
        $ renpy.fix_rollback()
        ro "It is not too late, we could all still walk away from this."
        wo "Only ones walking away from this be orcs. Orders is orders, human."
        ro "So be it."
        jump wildorcfight

label wildorcfight:
play sound "music/SFX/sword_draw.ogg"
pause 1
play sound "music/SFX/orc_attack.ogg"
pause 1.5
play sound "music/SFX/sword_hit_1.ogg"
show bg3 with sshake
pause 0.3
play sound "music/SFX/sword_hit_2.ogg"
show bg3 with sshake
pause 0.3
play sound "music/SFX/sword_hit_3.ogg"
show bg3 with sshake
pause 0.3

show cg6 with flash
pause 2

"In a flash, Rowan draws his sword from its sheath just as the first orc rushes towards him. Bringing his blade up to meet the incoming axe, the sound of steel clashing against steel rings throughout the otherwise tranquil woods."
"The orc is strong, but like the rest of his kind, sluggish, and no match for a swordsman of Rowan’s skill. Even with a few years of rust, he turns the axe away with a twist of the wrist, and sinks the riposte deep into the orc’s chest with ease."
"Bracing his foot against the slumped orc, Rowan pulls his blade clear just in time to meet the next enemy’s blade. He still had his work cut out for him if he was to get out of these woods alive."

stop music fadeout 1.0

scene bg2 with fade
play music "music/village loop.ogg" fadein 2.0

show alexia intro neutral at midleft with dissolve
show jezera disguised neutral at midright with dissolve

je "...And in the summer, it is really beautiful. They have processions through the city to the Cathedral of Light in honour of Solansia."
je "Everyone wears the most wonderful outfits, it is so colourful and lively. I cannot wait to return after a few months in Uvarth, it will be a most welcome change of scenery."

al "Is Uvarth really so bad? I have heard tales of cold deep enough to splinter bones, but I confess I have always doubted their veracity."

je "They are true enough, I am afraid. If you were to get caught up on the tundra in the dead of winter, at best you’d survive with bitter frostbite, should you survive at all."
je "It is not just the cold though, the whole city is so solemn. The Lords lock themselves away and bicker with each other. It is almost as if the place became a tomb the day their ancestors swore an oath to guard Araug’s Fall"

al "And the chasm? Did you see it?"

je "Only from the walls of the city. Even from a distance it seems impossibly deep, and the land around it is blackened like the northern wastes. Nothing grows there, even the snows seems to avoid it."
je "I do not know if the Fel Dragon truly does slumber, imprisoned, somewhere at the heart of it, but the Lords certainly believe it to be true. The sense of foreboding I felt when looking at that hole makes me think they might not be entirely wrong."

show alexia intro concerned at midleft with dissolve

al "Speaking of a sense of foreboding..."

"Alexia rises from her chair and walks to the window, hoping to catch a glance of her husband returning down the lane to their cottage. To her despair, she sees nothing but the sun sinking lower to meet the horizon."

al "It is getting late, and there is still no sign of Rowan. He should have been back by now if he was only searching the western woods."
al "I have to admit, I am starting to get a little worried, hopefully he will not be much longer in returning."

je "Oh, I think he might be a while longer yet, my sweet girl."

al "What do you mean by that?"

stop music fadeout 1.0
pause 1
play music "music/Jezera 2 loop.ogg" fadein 2.0

je "By now he will have encountered the little trap I left waiting for him in the woods, and the orcs will be keeping him busy."

al "Orcs?!"

show jezera disguised smirk at midright with dissolve

"Mariel rose from her chair, and the smile on her face morphed into an evil smirk. The change was so severe it was if a veil had lifted, and the woman was now someone else completely."

je "Do not worry your pretty face, Alexia. It is nothing your husband cannot handle, they will just keep him busy for a little while until we’ve had our fun."

al "We? Who else is with you and why are you doing this?"

je "All in due time, my dear. I suppose this ruse has gone on long enough. I do enjoy a good charade, but all good things must come to an end, as they say. "

play sound "music/SFX/spell_reveal.ogg"
show cg7 with flash
pause 2

"With that, Mariel waves her hand and a hot white light pulses through the room, sending Alexia tumbling backwards onto the hard wood floor."
"When the blinding brightness cleared from her eyes and she could see again, where the white haired girl had been stood was now a beautiful blue hued woman, clearly not human, and naked as the day she was born."

$ jezera_name = '???'
show jezera naked happy behind cg7

al "You’re a... a.... demon!"

je "Aren’t you quick to catch on. This will not do though, I’ll catch my death of a cold."

"With another wave of her hand, the demon summoned herself a revealing outfit; a low cut red and gold dress to emphasize her ample cleavage, accompanied by a pair of long black leather gloves."

show jezera happy behind cg7

je "That is much better. Now, what am I going to do with you?"

stop music fadeout 1.0

scene bg3 with fade
play music "music/Orc Ambush loop.ogg" fadein 1.0

show wild orc neutral at orcright with dissolve
show rowan neutral at midleft with dissolve

"Meanwhile, back in the western woods, Rowan had managed to slay most of the orcs, Now all that stood in his way to returning to his home was the one who had spoken to him when the trap had been sprung."

wo "Stupid human, why you no give up? You can’t win, we too strong."

ro "Look around you, I think the odds are swinging firmly in my favour."

"The orc’s sword had shattered from an earlier parry, and he now came at Rowan, swinging a crudely made axe wildly."

show rowan attack at midleft with dissolve

play sound "music/SFX/sword_hit_1.ogg"
show bg3 with sshake
pause 0.3

"Powerful, but slow and deliberate, the hero thinks as he bats another blow away. At this rate, it will not be long before he tires himself."

wo "Haha, see, this why you stupid, human. Me’s not talkin’ about orcs, me’s talkin’ about orcs’ masters. Kill me, kill lotsa orcs, don’t matta."

ro "And just who are these so called masters?"

wo "Me’s not telling, you find out soon enough. Orcs’a not s’posed ta spoil the surprise."

play sound "music/SFX/sword_hit_1.ogg"
show bg3 with sshake
pause 0.3
play sound "music/SFX/sword_hit_2.ogg"
show bg3 with sshake
pause 0.3
play sound "music/SFX/sword_hit_3.ogg"
show bg3 with sshake
pause 0.3

"The two clash again and again, the orc attempting to use his superior strength to force the advantage when their weapons lock. His smaller opponent, not foolish enough to engage in a contest of strength, opts to pirouette, sending the orc tumbling past him."
"As he spins, he brings his sword back around, scoring a hit. The long bloody slash down the monster’s back causes the beast to cry out in rage."

ro "What have they done to my village?"

wo "You’s find out soon enough, but it be too late already."

play sound "music/SFX/orc_attack.ogg"
"With a final cry of rage, the orc charges Rowan one last time, intent on killing his foe. Tired and wounded, dodging it is no challenge for Rowan, who side steps and hacks one last time at the orc champion’s midsection."
"The blade finds its target and bites deep. The orc sinks to the ground, finally defeated."

hide wild orc neutral with dissolve
show rowan neutral at midleft with dissolve

ro "Maybe he was wrong, maybe it isn’t too late. I have to get back. Goddess, protect the village, and hold on Alexia, I’m coming."

hide rowan neutral with moveoutleft

stop music fadeout 1.0
pause 0.5
play music "music/songbirds.ogg" fadein 1.0

pause 4

"Sometime after Rowan leaves, the orc rises from the floor. He had only been playing dead all along, and though wounded severely, he is able to stand under his own power."

show wild orc wounded at orcright with dissolve

wo "See? Knew human was stupid, can’t kill me’s, me’s strongest of all orcs!"

"As if responding to the orc’s claim, the shadows in the glade begin to lengthen until they cross at the center. From the dark ground, as if stepping out through the very shadows themselves, appears a demon; blood red in colour, covered in black markings."
"He looks thoroughly displeased."

$ andras_name = '???'
show andras displeased at midleft with dissolve

an "If you were the strongest, surely you would not have been defeated by a lowly human."

wo "Human was strong, big hero. An’ your sista said—"

an "You dare defy me?"

wo "No defy, just do as ordered."


an "Weakness will not be tolerated. If you do not have the strength to even defeat a human, what use are you?"

"With lightning quickness, the demon plunges his clawed hand deep into the orc’s chest, piercing his heart. The orc drops to the floor, and this time it was certain he would not be rising again."

play sound "music/SFX/orc_attack.ogg"

hide wild orc with redflash
pause 1.5
show andras displeased hands at midleft with dissolve

an "Pathetic."

stop music fadeout 1.0

scene bg4 with fade
play music "music/burning village loop.ogg" fadein 1.0

"A few hours later, Rowan arrives back at the village to find it engulfed in flames. He had seen the smoke from the distance and feared the worst, and now those fears had been confirmed by the inferno that raged before him."
"There was no hope that a blaze this size could be quelled, Arthdale was doomed."
"Forcing his way through the acrid, black smoke he searches for survivors, but can find no trace of any of the villagers. Praying to Solansia that this is because they all fled to safety, and not because they had been consumed by flame, he pushes on towards his home in search of his wife."

show rowan neutral at midleft with moveinleft

ro "ALEXIA?"
ro "ALEXIA?"
ro "ANYBODY?"

"His cries return no reply, but whether it is because nobody is able to hear over the roaring of the flames, or simply that there is no one around, he cannot tell."
"The air begins to sting Rowan’s eyes, and the more he breathes in, the more he feels his lungs filling with smoke. He pushes on, letting out a hacking cough as he continues his search. At this rate, it wouldn’t be long until he collapsed, he realizes."
"Just as he is about to turn back, he sees his wife in the village square, but she is not alone."

show cg8 with dissolve
pause 2

"She kneels on the stone ground, surrounded by the flickering flames engulfing the village, her head held up by a shapely blue-skinned female demon."
"Beside her stands a more menacing figure, also a demon, but this one male, and with crimson hued skin, crossed with black markings."

scene bg4 with dissolve

show rowan neutral at roleft with dissolve
show jezera neutral at midright with dissolve

je "Glad that you have finally joined us, I was beginning to think this whole village would burn to ground before you got here."

"Rowan ignored the female demon, focusing instead on his wife, Alexia, who had yet to look at him. Her head was just hanging, almost lifeless, as she looked towards the ground."

ro "If you’ve hurt her in anyway, I’ll—"

show andras angry at orcright with dissolve

an "Yes, that is the spirit!"

show andras displeased at orcright with dissolve

je "Now, now, boys, she is perfectly fine. Just a little magic to make her a bit more agreeable, it will wear off eventually. Couldn’t have her running off, could we?"
je "She is of no use to me damaged, and I’ve certainly no intention of harming her."


show andras smirk at orcright with dissolve

an "I might, hero, if you make me."

"The male demon was clearly trying to provoke him, Rowan knew, but it would be foolish for him to attack, especially while one of them had Alexia as a hostage."
"Two demons were enough of a challenge on their own, and the thick smoke that surrounded them made it impossible for him to know if they were alone."
"They had others willing to serve them, he had learned that in the encounter back in the western woods, and that made it all too risky."

je "You will have to excuse my brother, Andras, he is somewhat overdramatic. This—"
"The female demon waves her hand, nonchalantly, to gesture at the flames still roaring around them."
je "—was all his doing. I find it a little over the top myself, but I do suppose it lends a sort of gravitas to the situation. Don’t you agree?"

$ andras_name = 'Andras'

show andras displeased at orcright with dissolve

an "And what would you have had me do, Jezera, send him a harshly worded letter?"

$ jezera_name = 'Jezera'

"Ignoring his remark, Jezera continues to address Rowan."

show jezera happy at midright with dissolve

je "My brother, you see, has always been of the wrong impression that force is the only way to get what you want."

show jezera hands happy at midright with dissolve

je "We women know that you catch a lot more flies with honey."
je "If he had his way, you would already be dead, but I find violence utterly boorish. I have a much more enticing proposition for you, hero."

"The smoke was beginning to rise, and Rowan could see no other people in the square - orc or villager."
"With only the two opponents, perhaps, if he chose him moment just right, he could get to Alexia before they realized and spirit her away from here."

ro "Get on with it then."

show jezera neutral at midright with dissolve

je "So impatient, just like the rest of your sex. No, not here, I don’t like to make it that easy."
je "Come to the site of your final battle against Karnas, I am sure you have not forgotten where that was, and we shall discuss it there."
je "We will have to take your wife with us, you understand. We need some way of ensuring your attendance after all."

an "Come alone, human, and do not even think about bringing along some of your little friends like last time. You won’t like what happens if you do."

"Bastards. He’d be damned if he was going to allow them to leave with Alexia. Just a little bit longer..."

show jezera happy at midright with dissolve

je "Time for us to make our grand exit. See you soon, Rowan."
je "And don’t take too long, you know it’s rude to keep a lady waiting."

"As Jezera bends to lift Alexia from the ground, her attention elsewhere, Rowan sees his moment appear."

show rowan attack at roleft with dissolve
"Seizing the opportunity he launches himself forward, pulling his sword clear from its scabbard and—"

play sound "music/SFX/spell_andras.ogg"
show cg9 with redflash
show cg9 with sshake
pause 2

"The red flash of demonic magic sparks through the air, as the full force of a spell evoked by Andras knocks him from his feet."
"Pain arcs throughout his body as the magic drives him onto his knees."
"Despite his best efforts, Rowan cannot rise. He can’t even move, and now finds himself, like his wife, at the mercy of the demonic siblings."

show rowan shock at roleft with dissolve

ro "Ugh..."

je "How disappointing, I was hoping you were different, but like all men you are so quick to resort to barbarianism. Such a pity."

an "Should I put the pathetic creature out of his misery?"

je "Not yet. If he survives the night he can come and find us at Castle Bloodmeen, and if not... Well, then he will not be a problem anyway."
je "I’ll be waiting, hero."

"Rowan can only look on in despair as the demons disappear into the thick smoke, Andras carrying his wife."
"Though no longer held in place by Andras’ dark magic, it has sapped all the strength from his body, and he is unable to move as the flames rage around him."
"Had he come this far in life only to die here in his home town? The thought was the last to occupy his mind as he drifted out of consciousness."

scene black with fade
pause 2

"Row..."
"Rowan ... you ... me"
"We need ... get out ... here"

show bg4 with dissolve

show village elder wounded at midright with dissolve

el "Get up Rowan, we need to get out of here. The fire is still spreading."

"Rowan opened his eyes to see the village elder standing above him."

show rowan neutral behind bg4

ro "There’s blood on you, are you okay?"

el "I was looking for survivors when someone attacked me from behind. But don’t worry, it will take more than that to kill me."

ro "The other villagers?"

el "All safe, most managed to escape early when the fire started. There was only you and Alexia unaccounted for."

ro "Alexia... They took her."

el "We’ll worry about that later, first we have to get out of here before we burn to death."

"Helping Rowan up, the elder placed the younger man’s arm around his own neck so he could help support him."
"Though clearly quite injured himself, the elder guided Rowan through the village until they were both clear of the fire in a field occupied by the other distraught villagers."
"Rowan could feel the cool grass press against the flesh of his neck when the elder placed him back on the ground, a welcome change of sensation from the pain that wracked his body."
"As he looked up at the stars in the night sky, just about visible through the thick smoke that still rose high into the air, he faded out of consciousness once more."

stop music fadeout 1.0
scene black with fade
play music "music/SFX/DroneVortex.ogg" fadein 1.0

"While sleep came easy to Rowan, it was anything but comfortable, as he tossed and turned on the cold, hard earth. His dreams were haunted by images that seems to shift away from him, as if he was glancing at them in the glass of a warped mirror. "
"With some degree of lucidity, he was able to discern among the shifting landscape of his dreams things that were in the conscious layer of his mind; the demon twins, twisting flames, the shadow of that castle he had not seen in years."
"Bloodmeen."
"He tried to will himself in the dream to go towards it, as he knew he must in real life, but he kept getting turned around, until he found himself lost in a place unknown to him."
"A labyrinth of stone. Heat assaulted him from all sides as if he were in a kiln of earth, was this place underground?"
"No longer in control of the dream’s actor, he rode the dream like a passenger as dream-Rowan began to stalk the maze like passages of this foreign place."
"Every now and then, upon rounding a corner, he could see someone walking ahead in the distance. A man or a woman? Human even?"
"He could not tell. Like many of the other things he had seen in the dream, the figure seemed to shift before him. The more he tried to focus, the more the shape seemed to escape perception."
"The dream continued this way for what, to Rowan, felt like an eternity, but he was sure each time they turned a corner, they were getting marginally closer to the figure who led them."
"If it continued this way, at some point, they would catch up. Then he would discover just who, or what, this stranger was."
"Eventually, his dream self reached the heart of a labyrinth."
"He found himself in a huge, cavernous room. The grandest space he had ever seen, the Cathedral of Light, paled in comparison. Towards the centre of the room, in the distance, he could see the shadowy figure stood at the edge of a pit."
"From his current vantage point, it was impossible for Rowan to see what was in the pit, but the other figure was certainly interested in what lay beneath them."
"Feeling control return to him once more, he willed himself to walk forward toward the pit. First, the left leg, and then the right. With each step, the world seemed to get more white, until it seemed blidingly so. And then..."

play music "music/destroyed village loop.ogg" fadein 1.0
scene bg5 with fade

show village elder happy at midright with dissolve

el "Finally awake are you? I was beginning to wonder if you were going to sleep all day."

"Awake. And before he had seen what was in the pit."
"In the bright light of day, he couldn’t shake the feeling that it had been more than just a dream. Nothing he could do about that now though."

show rowan neutral at midleft with dissolve

ro "How long have I been out?"

el "Nearly fifteen hours. I was going to wake you, but I thought you might need the rest."
el "Yesterday was an eventful day, and you have a long journey ahead of you now, my child."

"Rowan blinks a few times, heavily, freeing himself of the last vestiges of sleep. In the light of day he could see the full extent of the damage the fire had inflicted on the village, and it was not pretty."
"The absence of the other villagers stung keenly, like an old wound on a cold day, and it felt odd to him that the two of them should be there alone, surrounded by such an uneasy quiet."

el "You look a little out of sorts, Rowan. Is something the matter?"

menu:
    "Tell him about the dream.":
        $ renpy.fix_rollback()
        ro "I had a strange dream unlike any I have ever had before. It felt... different, almost real even."
        ro "I was in a maze with stone walls following a strange figure. I had no control over my actions, so I just had to keep following it down all the passage ways."
        el "A strange figure and a maze? That is certainly odd. It is not like anything I have heard of in all my years, I must admit."
        ro "It gets even weirder."
        ro "Eventually, I reached the centre and the figure was standing over a huge pit. I wanted to see what was in it, but I woke before I got the chance, unfortunately."
        ro "Even now, I just cannot shake the feeling that whatever was in the pit, it was important."
        el "I don’t recall any stories about pits in the centre of labyrinths, but it does sound rather ominous."
        el "Perhaps it was just the product of your imagination, you have had a rather rough time yesterday, after all."
        el "Then again, it may be something more. There are myths in which the gods speaking to mortals through dreams. If that is the case, you had have to seek out someone better versed in these things, I am no scholar or seer."
        ro "If only I had the time, but I have to get to Castle Bloodmeen. Solansia only knows what they might do to Alexia if I do not arrive soon enough."
        jump safealone


    "Change the subject and ask about the villagers.":
        $ renpy.fix_rollback()
        ro "I’m fine, it has just been a rough night. Where are the rest of the villagers?"
        el "The guards from Rastedel we sent for yesterday arrived earlier, and I asked them to escort the villagers back to town. They can’t exactly stay here at the moment with the village the way it is."
        el "I didn’t want to leave you, so I stayed behind. I may be old, but I can still walk to Rastedel by myself, you know."
        ro "Better safe than sorry. I doubt the demons will return, they want me after all, but why take any unnecessary chances?"
        ro "This place just seems so... wrong without anybody here, though. The lack of noise in unnerving."
        el "I know how you feel. In all the decades I have lived in this village, I have never known it be so quiet. This place the only home I have ever known, and I fear I will not live to see it restored."
        ro "It can be rebuilt, old friend, and I will help you. But first I have to get to Castle Bloodmeen. Solansia only knows what they might do to Alexia if I do not arrive soon enough."
        jump safealone

label safealone:
el "Do you really think it is safe to go alone?"

menu:
    "I have to do this by myself.":
        $ renpy.fix_rollback()
        ro "No, but I have to do this by myself. They came for me after all, and I cannot risk anybody else getting hurt because of me."



    "I was told to come alone.":
        $ renpy.fix_rollback()
        ro "No, but I have to. The male demon, Andras I think she called him, said that they would hurt Alexia if I didn’t, and I cannot risk it."

el "I understand. I wish it did not have to be this way, that you have to walk into what is no doubt a trap by yourself, but your desire to protect others is noble as always."
el "Whatever happens, know that I am proud of you, and your parents would be too if they were still with us."

show rowan happy at midleft with dissolve
ro "Now, now, old man, don’t be planning my funeral just yet. I have still got a few tricks up my sleeve."
ro "Anyway, I had better set off while the sun is still high. I have a lot of preparation for the journey, and I’ll need to book passage from Prothea."
ro "Are you sure you are fine travelling to Rastedel by yourself?"

el "Don’t you worry about me, the roads are safe enough. The Duke even ordered extra patrols when he heard about yesterday’s trouble."
el "And you don’t need an old man like me slowing you down, you have got a wife to save."

ro "Nonsense, if you were any younger I’d be taking you with me!"
ro "May Solansia watch over you and keep you until I return."

el "And you too Rowan. We will all be praying for you, and Alexia’s safe return."

stop music fadeout 1.0
scene black with fade

"The two exchanged tense good-byes, both unsure if they would see the other again. Rowan tried to remember how he felt the last time he had left the village, all those years ago, unknowingly on the path to Castle Bloodmeen."
"Had he felt excitement? Fear? Sorrow?"
"No matter, he did not have the luxury of nostalgia now. The journey ahead was long and arduous, as he knew from experience, and it would be months before he reached his destination."
"He could only hope they would not hurt Alexia in the meantime."

"Four months later..."

scene cg10 with fade
play music "music/before the gates loop.ogg" fadein 1.0
pause 3

"Rowan had crossed seas, the desert, and finally the black jaws themselves; a difficult journey that had taken the best part of four months, to stand where he now stood."
"Last time he crossed the bridge, they had to battle for every step. The fighting had been heavy here at the last bastion of Karnas’ defence. How many men, he wonders, had lost their lives for even an inch?"
"It all seemed so long ago now, he thinks, as he now crosses the span unchallenged. Even the tall iron gates that had barred them from entering the courtyard now waited for him, uncontested."

scene black with fade
"He retraces his steps as if he were almost reliving a memory. First, through the courtyard, and then into the castle proper. The vestibule was eerily quiet, he had at least expected a few guards, but there were none to be found anywhere."
"Pressing on, he makes his way down the main corridor towards the throne room, where he and his friends had fought, and defeated, Karnas. The doors stood open, as if they were inviting him in."

scene bg6 with fade

"He steps into the throne room to find it larger than he remembered. The long walk to the dais, flanked on either side by pillars of obsidian, and then, up those stairs, the throne."
"What little light there was in the room was reflected off the black stone of the seat of power - obsidian, perhaps? - making the imposing center piece even more so."
"Twisted with long appendages, like tentacles, it seemed to him a very real manifestation of chaos itself."
"And sat upon it, Jezera."

show jezera happy at edgeright with dissolve

je "Welcome to Castle Bloodmeen, hero. So nice of you to finally join us."

show rowan neutral at midleft with dissolve

ro "Where’s Alexia? What have you done with my wife?"

je "Oh don’t be so dramatic, Rowan, she is safe and sound as promised. You came alone, and so we have held up our end of the bargain."

ro "And I am just supposed to trust you on that, am I?"

je "Well, you know what they say about demons and deals."

ro "I thought that usually involved some poor fool’s soul."

je "You humans are always so pedantic, doesn’t it ever get tiring? No wonder you are always killing each other."
je "It would not hurt you to lighten up a little, you know, hero."

show jezera displeased at edgeright with dissolve

"Jezera is clearly becoming visibly annoyed by Rowan’s unfriendly demeanor, and gives an audible sigh, more for show than from any genuine tiredness."

je "As I have already said, Alexia is fine. My brother is with her now."

ro "In some dank cell, somewhere beneath this castle, no doubt."

je "In the guest wing actually, attended to by servants. A lot nicer than your hovel back in that peasant village, in fact."

"Rowan begins to open his mouth to speak, but Jezera, having had enough by the point, cuts him off before he can even start."

je "You can see her shortly, and then that will be your proof that I am good for my word."

show jezera happy at edgeright with dissolve

"Rising from the throne to her feet, the annoyance melts for her face as she looks down at Rowan from the dais, replaced by a familiar, knowing smile."

je "Now, with that behind us, let us get to the business at hand."

scene black with fade
stop music fadeout 1.0

"Meanwhile..."

scene bg7 with fade

"It had been four months since Alexia had been kidnapped by the demons and brought to live in the castle. She could remember that night like it was yesterday: Jezera’s transformation, the fire, her fear when Andras cast his spell on her husband."
"When they had brought her through the portal to Bloodmeen, she was almost catatonic from shock, certain she would be thrown into a cell where no one would ever find her, and left to rot."
"But, much to her surprise, that was not what happened. Once they had arrived in the castle, she was carried to the room where she now found herself, a spacious, well furnished room in the guest wing, and fed and bathed by female servants."
"Fresh clothes were lain on the bed, and she was left alone to sleep. She did not get much rest that first night, too afraid to drift off in case something happened to her, but nothing did."
"Her captors were always courteous toward her, and would often visit to exchange pleasantries. Nothing was asked or expected of her, and despite her status of prisoner, was also not confined solely to her room."
"She was allowed free reign of most of the castle if she wished, and often took the opportunity to visit the vast library."
"As prisons went, it was far from the worst that she could imagine, but she missed her husband desperately. Although, even these feelings were a cause for contradiction."
"She wanted nothing more for him to walk through the door right this minute, but she knew if he did, he would have walked right into the demon’s trap."
"As she sits, weighing the implications of her conflicting desires, she hears a knock on her door."

play sound "music/SFX/wood_door_knock_01.ogg"
pause 0.5

show alexia white neutral at midleft with dissolve

al "Who’s there?"

an "Andras. I hope this isn’t an inconvenient time?"

al "No, please, come in."

"The demon opened the door and stepped into the room, with the  air of hesitation he displayed every time that he visited. She always found it funny considering it was his castle, after all."

show andras happy at midright with dissolve

al "Good day, Andras. Any news of my husband?"

"She asked the same question whenever she saw either of the demon siblings, never quite sure if she wanted the answer to be yes or no."

an "Nothing as of yet, I’m afraid. I would not worry though, the journey from Rosaria takes time."

al "And is fraught with danger."

an "Nothing Rowan has not faced before, and last time, there had been an army in the way."

show alexia white happy at midleft with dissolve

"She smiled at his kind reply. She knew that he was just trying to make her feel better, but in the back of her mind as always was the knowledge that no matter how nice he and his sister acted towards her, she was still their captive."

al "Thank you, I pray for his safety daily."

"The truth, but she omitted that part of her prayed that he would stay safe by never coming to the castle."

an "I am told you have been spending a lot of time in the library."

al "I have, it is amazing. I’ve never seen so many books. In Arthdale, you could sometimes get them from traders passing through, but there were never a great deal to read."

an "My sister tells me it rivals the church’s archives in Prothea, but I have never been a big reader myself."

al "You are missing out, I have found so many books I have never ever heard of before, and all on different topics."
al "I am learning so much, but... I don’t think Cliohna likes me very much."

an "Well, I will let you into a secret - I don’t think Cliohna likes anybody that much. It wouldn’t surprise me if those books were the only friends that she had."

"Alexia let out a laugh, and then felt a little ashamed she’d laughed at a joke that was a little mean spirited."

al "That was a little unkind, Andras."

an "You were the one who laughed."
an "Anyway, I shall let you return to your books, I just wanted to make sure you had everything that you needed."

al "Thank you for your concern, but the servants have made sure of that."

an "In that case, I shall take my leave. Good day, Alexia."

al "Goodbye."

"As he steps into the doorway, she feels a pang of loneliness, accompanied by a tinge of guilt."

show andras happy at orcright with dissolve

show alexia white concerned at midleft with dissolve

al "Andras?"

an "Yes, Alexia?"

al "Come visit me again, soon?"

an "Of course."

show andras smirk at orcright with dissolve

pause 0.5

hide andras smirk with moveoutright

show alexia white happy at midleft with dissolve
pause 2

scene bg6 with fade
play music "music/before the gates loop.ogg" fadein 1.0
show jezera happy at edgeright with dissolve

je "Do you remember the last time you stood in this hall, hero?"

show rowan neutral at midleft with dissolve

ro "Of course I do, seven years ago when Karnas sat in that throne instead of you."

je "And?"

ro "You know the story, everybody knows the story thanks to the Church."

je "I want to hear it from you."

ro "Fine. We fought our way through the castle to the throne room and found Karnas waiting for us. He was unwilling to yield, and quite angry that the war was lost."
ro "He attacked ferociously, without warning. He was huge, and his strength inhuman, I have still never seen anything like it."
ro "Before we knew it, he had almost killed Valyr, who barely dodged the blow meant to find his heart. But we had not come unprepared."
ro "While Valyr, N’mala, and I did our best to fend him off, Al-Serah sang the Lay of Llyr, and Deanara brought forth into our world a manifestation of the power of Solansia."
ro "To see a living saint perform a miracle before you eyes, words cannot express it. When the dust cleared, Karnas was gone. We had won."

je "And that, Rowan, is how you killed our father."

show rowan shock at midleft with dissolve

ro "Father?!"

show rowan neutral at midleft with dissolve

je "Now it is my turn to tell you a story. Just as there are those who are instinctively drawn to light, like you and your friends, there are those drawn to darkness."
je "Our mother was one such person. She was nobody special, just a northern village girl, but she was beautiful."
je "In the early days of the war, Karnas conquered her village, and she fell in love with him at first sight. So much power, she saw him as a god."
je "She gave herself to him body and soul, the pleasure was unlike anything she had ever felt before or did after."
je "The other villagers called her all sorts of names, spat at her in the street, but she was proud to be one of ‘Karnas’ whores’."
je "Eventually, he moved on; he had a war to win after all. But he left our mother with a little something."
je "A few months later, Andras and I were born."

ro "And that is what this is all about, revenge?"

je "Revenge? Oh no, you misunderstand me, Rowan. Why would a person want revenge for someone they have never met?"
je "No, hero, what I want from you is for you to give back the thing that you stole from us."
je "Our birthright."

ro "What is that supposed to mean?"

je "Our father should have ruled this world, and when his time was over, it should have passed to us."
je "You will serve us and help us recover what is rightfully ours. You will help us conquer the Six Realms."

show rowan attack at midleft with dissolve

ro "Betray my friends? I’d rather die first. Do your worst, demon."

je "I’m disappointed in you, hero. I had hoped that you were more flexible than the rest of your kind, but alas."
je "We shall do it my brother’s way then, do not say I did not try to warn you."

stop music
play sound "music/SFX/metal_lever_movement_03.ogg"
pause 0.5
scene black with fade

"The click of a mechanism, and before Rowan could so much as blink, the floor beneath him gives way. A trapdoor hidden beneath the castle’s regal carpet."
"As he falls, he reaches out in vain to try and grab the edge, but can only watch it shrink smaller and smaller and he falls deeper into the darkness below."

play sound "music/SFX/BodyfallDirt.ogg"

"A few seconds later, Rowan discovers the depth of the pit, colliding with the hard dirt at the bottom. He hears the sickening crack of bone, as searing agony shoots up his leg."
"Broken leg, he thinks, and with the bone probably protruding from his shin to boot. He grits his teeth and tries to suppress the sensation, but the pain is too much to bear, and it is not long until he passes out."
pause 2

play music "music/Dungeon Ambience.ogg" fadein 1.0
"How long he lies unconscious in the pit he has no idea, but when he does wake sometime later, he feels cool stone pressed against his cheek, and dry straw scratching the bare skin of his side."
"Metal digs into his wrists, his hands had been shackled together, while the pain in his leg is completely gone. Whoever had bound him must have used magic to mend it while he was unconscious."
"Rolling over onto his back, he tries to open his eyes, only to be blinded by light coming in from above."

show white with fade
ro "Ugh... Where am I?"

show bg8 with fade

"As his eyes become accustomed to the light in the room, Rowan is able to see where he is; a cell in the castle dungeons."
"As he strains against the manacles, trying to force them apart and free his hands, a man’s voice rings out from the other side of the wall."

cm "What? Can you not tell from the luxury accommodations, fine dining, and the varied assortment of beautiful women?"
cm "You obviously must be in the finest brothel in Qerazel."

show rowan jail neutral at midleft with dissolve

ro "Hello? Is there somebody else down here?"

cm "No, you are all alone, and it is just your own mind talking to itself, making sarcastic comments."

ro "There’s no need to be like that."

cm "Try spending a few years in this place, and then see how much you enjoy strangers asking you stupid questions."

"A dry cackle came from the other side of the wall, almost half-laugh, half-cough. Despite his best efforts, Rowan was having no luck in escaping from the manacles."
"For the time being, he would have to remain bound."

ro "I am sorry, I just did not expect for there to be anyone else down here. My name is Rowan."

cm "Used to have one myself, maybe I forgot it, maybe I don’t care to remember."
cm "Language ain’t much use to a man left to his own devices, and what good’s a word if no ever says it anyway?"

"Rowan stands and inspects his surroundings. The wooden door was no doubt locked, and looked as sturdy as the stone walls of the cell."
"Light was coming in from somewhere high above, but the walls were smooth and would offer no purchase, should he try to climb. At least, he thinks, the cell is not too cramped."

ro "How long have you been imprisoned down here?"

cm "Weeks? Months? Years? Does it matter? The thing about time is, after a certain point it all just starts to bleed together."
cm "Do you think the mayfly, or the animal in the field, or even the gods obsess about every little passing moment?"

"It was fast becoming clear that however long the man had spent locked in the dungeons, it had frayed the edges of his sanity."
"Not only was Rowan trapped down here, he was sharing his captivity with a mad man."

cm "Better to say 'No!' To cast off the tyranny of time, and free yourself from the chains of temporality."

ro "I am more concerned with freeing myself of chains of a more physical manner at the moment. Any ideas about getting out of here?"

cm "Escape? I wouldn’t bother. And if you did get out, what would be the point? Out there is as much a prison as in here."
cm "In here, at least you can see the bars."

"Clearly, the other man was going to be no help, leaving Rowan to consider his options."

$ door_escape = 0
$ climb_escape = 0
$ guard_escape = 0

label escape_options:

if (door_escape == 1) & (climb_escape == 1) & (guard_escape == 1):

    menu:
        "Try the door.":
            $ renpy.fix_rollback()
            if (door_escape == 1):
                "Still locked, Rowan will have to find another way out."
                jump escape_options
            else:
                "Rowan tries the door, and his hopes that it might have accidently been left open soon melt away. He gives it a push, but it sits solidly in the frame, and does not budge."
                cm "I wouldn't get any ideas, if I were you."
                "Unwilling to be defeated by the wooden obstacle that stands in his way, Rowan takes a couple of steps back, braces himself, and charges the door shoulder first."
                show bg8 with sshake
                "Unfortunately, the door has been reinforced with something stronger than just wood, and a magic barrier sends Rowan flying back across the room."
                "He slams against the wall and slumps down to the stone floor, his shoulder lancing with pain. He will not be trying that particular method of egress again."
                cm "Always a shame to say I told you so."
                $ door_escape = 1
                jump escape_options

        "Try to climb up.":
            $ renpy.fix_rollback()
            if (climb_escape == 1):
                "Nope, still too slippery to climb."
                jump escape_options
            else:
                "If light is coming from somewhere above, Rowan thinks, that must mean there is a way out. While the walls were too slippery to climb, he could see one chain above him, low enough to grab."
                "Rowan reaches up and tries to hoist himself from the ground using the chain as leverage, but it is old and rusted by years of exposure to the moist dungeon atmosphere, and the links split from the strain."
                show bg8 with sshake
                "Rowan falls down, arse first, against the cell floor. Climbing out was a non-option, and he has nothing to show for his escape attempt other than embarassment and a numb behind."
                $ climb_escape = 1
                jump escape_options

        "Call out to the guard.":
            $ renpy.fix_rollback()
            if (guard_escape == 1):
                "Still no reply."
                jump escape_options
            else:
                "Perhaps, Rowan thinks, someone will come if he pretends to be injured. He calls out at the top of his voice that he is bleeding, but his appeal for help brings no response."
                cm "You are wasting your breath, no one is coming. Nothing can hear you down here except for me and the rats."
                $ guard_escape = 1
                jump escape_options

        "Give up":
            $ renpy.fix_rollback()
            jump jailgiveup

else:

    menu:
        "Try the door.":
            $ renpy.fix_rollback()
            if (door_escape == 1):
                "Still locked, Rowan will have to find another way out."
                jump escape_options
            else:
                "Rowan tries the door, and his hopes that it might have accidently been left open soon melt away. He gives it a push, but it sits solidly in the frame, and does not budge."
                cm "I wouldn't get any ideas, if I were you."
                "Unwilling to be defeated by the wooden obstacle that stands in his way, Rowan takes a couple of steps back, braces himself, and charges the door shoulder first."
                show bg8 with sshake
                "Unfortunately, the door has been reinforced with something stronger than just a wood, and a magic barrier sends Rowan flying back across the room."
                "He slams against the wall and slumps down to the stone floor, his shoulder lancing with pain. He will not be trying that particular method of egress again."
                cm "Always a shame to say I told you so."
                $ door_escape = 1
                jump escape_options

        "Try to climb up.":
            $ renpy.fix_rollback()
            if (climb_escape == 1):
                "Nope, still too slippery to climb."
                jump escape_options
            else:
                "If light is coming from somewhere above, Rowan thinks, that must mean there is a way out. While the walls were too slippery to climb, he could see one chain above him, low enough to grab."
                "Rowan reaches up and tries to hoist himself from the ground using the chain as leverage, but it is old and rusted by years of exposure to the moist dungeon atmosphere, and the links split from the strain."
                show bg8 with sshake
                "Rowan falls down, arse first, against the cell floor. Climbing out was a non-option, and he has nothing to show for his escape attempt other than embarassment and a numb behind."
                $ climb_escape = 1
                jump escape_options

        "Call out to the guard.":
            $ renpy.fix_rollback()
            if (guard_escape == 1):
                "Still no reply."
                jump escape_options
            else:
                "Perhaps, Rowan thinks, someone will come if he pretends to be injured. He calls out at the top of his voice that he is bleeding, but his appeal for help brings no response."
                cm "You are wasting your breath, no one is coming. Nothing can hear you down here except for me and the rats."
                $ guard_escape = 1
                jump escape_options

label jailgiveup:

"All avenues of escape exhausted, Rowan slumps against the nearest wall, sitting back down on the straw near to where he awoke."
"There was no way he was going to get out of here by himself, and the only other person who knew he was here was the elder, and he’d told him not to send help."

cm "Told you. Better to just give up. You’ve more chance of touching the stars than you have escaping from here, and hope?"
cm "Hope’ll quickly become the millstone around your neck."

hide rowan jail neutral with dissolve

"Time passed. At first, Rowan scored the passing of days on the wall, using the rising and the setting of the sun for guidance."
"After a while, it became an exercise of no real meaning other than repetition, a symbolic mechanical exercise, and he abandoned it completely."
"The guards would bring three square meals a day, and the food was not too terrible considering the position he currently found himself in. They would also occasionally visit for less friendly reasons, the timing of which seemed to have no rhyme or reason."
"These little meetings became random punctations of violence in an otherwise monotonous existence consisting of prison boredom and his prison mate’s rants."

"Months pass..."

cm "Someone’s coming."

show rowan jail hurt at midleft with dissolve

ro "A guard?"

"It isn’t time for them to eat, Rowan thinks, so probably another impromptu beating."

cm "No clinking of armour, or heavy footsteps. Something much lighter than an orc."

"Soft footsteps echo down the dungeon hallway, until the visitor stops outside the door to Rowan’s cell. The door swings open to reveal none other than Jezera."

show jezera neutral at right with dissolve

je "Hello hero, it has been a while."

ro "Demon."

je "I see my brother has been sending his goons to see you. I apologize, but I did warn you."

ro "Is that why you came down here? To tell me ‘I told you so’?"

je "No, I came down here to try and talk some sense into you."

ro "And I’m sure I can guess what it is that you consider ‘sense’."

je "Oh, for Fiuren’s sake, Rowan. No one is coming, and there’s no way out, haven’t you figured that out yet?"
je "Are you really so stubborn that you would rather rot to death in this cell?"

ro "Compared to the alternative, enslaving the whole of the Six Realms, rotting is preferable."

je "The truth is, hero, the Six Realms are already enslaved. The peasants live on land parceled by the aristocracy, grateful for their meagre existence."
je "Those aristocrats kowtow the monarchs for favour, and have their petty wars. Meanwhile the Church collects its tithes, and the gods?"
je "They are the worst masters of them all. So much suffering, and what do they do?"
je "Nothing."

ro "You’d simply have us exchange one master for another, then? Why not just get rid of masters altogether instead?"

je "The thing about people is they need masters. They need someone to look up to, to tell them what to do, to blame when everything goes wrong."
je "They talk about freedom, but it is the last thing in the world that they truly want."
je "If they got it, they’d have to face up to the fact they are the ones ultimately responsible for everything that happens to them."
je "No man wants that burden."

ro "So what? You’d have us worship the One of Many Masks?"

je "Gods no, I am not insane, hero. Unlike most of you humans, I have seen beyond the veil into the Outer Dark, and the horror that Kharos presides over."
je "Chaos is capricious and fickle, only a fool would worship it."

ro "You and your brother then?"

je "Would it really be so bad? There would be no more petty wars, and no bleeding the peasants for the little that they have; we have no interest in human wealth."
je "Freed from your pointless laws, and the prudish notions of the faith, people would be able to indulge in their basest desires."

ro "Like animals, you mean?"

"Jezera sighs, once again growing tired of having the same argument."

je "Listen, just promise me you will think about it. A time will come soon when you’ll have to decide once and for all, and I won’t be able to protect you."

ro "Very well, I shall give it some thought."

show jezera happy at right with dissolve

je "Thank you. In the meantime, I’ll stop those little visits from the guards. Anyone who touches you from now on will lose his head."
je "Until we meet again, hero."

hide jezera happy with dissolve
"Jezera opens the door and goes back out into the hallway, leaving Rowan alone with his thoughts."

cm "I would listen to the woman if I were you, you don’t want to end up like me."

"The sinister cackle of his anonymous jail mate filled the room. Rowan feels an involuntary shudder go all the way through him, and hopes that would not be his fate."

hide rowan jail hurt with dissolve

"A few weeks later..."

"Rowan is woken up by the feel of a sharp jab in his ribs. He opens his eyes to see an orc towering above him, his metal boot pressed into his side."

show orc soldier neutral at orcright with dissolve

os "Get up human, is time to go."

"Rowan rises to his feet, and attempts to shake of the vestigial remnants of sleep."

show rowan jail dirty at midleft with dissolve

ro "Where am I going?"

os "No questions, go."

"The orc gives Rowan a solid shove in the direction of the door, and the human walks ahead of him out of the cell and into the corridor."

stop music
scene black with fade

"As he passes the next cell, he looks through the bars to find it empty. The other inhabitant of the dungeon seemingly vanished without a trace."
"The guard leads him back upstairs to the first floor, and he is taken into a small chamber, where servants clean the dirt from his body, and shave his face."
"Once they are finished, his escort resumes, and he finds himself once again entering the throne room."

label badend1return:

show bg6
play music "music/before the gates loop.ogg" fadein 1.0

"When they reach the dais, the orc removes the manacles from his wrists, and leaves Rowan with the other two people present in the room, Andras and Jezera."

show andras smirk at right with dissolve

an "Greetings human, I trust you are enjoying the accommodation."

show rowan jail neutral at midleft with dissolve

ro "If you have just brought me here to insult me, I’d rather waste away in my cell."

show jezera neutral at midright with dissolve

je "That is enough, brother."

show andras displeased at right with dissolve

an "You are decidedly no fun, sister."

ro "I could come back later, if you would like."

je "I am glad to see your sojourn in the dungeon has not harmed your sense of humour."

an "Very well. The reason we have summoned you, human, is because my sister has convinced me to give you another chance."
an "Has some time alone in that cell brought you to your senses?"

label introservechoice:

menu:
    "Agree to serve them while biding your time.":
        $ renpy.fix_rollback()
        $ serveChoice = 1
        jump introserve

    "Agree to serve them so you don't turn out like the other prisoner.":
        $ renpy.fix_rollback()
        $ serveChoice = 2
        jump introserve

    "Agree to serve them so you can see Alexia again.":
        $ renpy.fix_rollback()
        $ serveChoice = 3
        jump introserve

    "Agree to serve them because Jezera was convincing.":
        $ renpy.fix_rollback()
        $ serveChoice = 4
        jump introserve

    "Refuse.":
        $ renpy.fix_rollback()
        ro "I'd rather die than serve you."
        jump introrefuse2


label introrefuse2:

je "Are you sure, Rowan? This is your last chance, I won't be able to protect you after this."

menu:
    "Rethink your decision.":
        $ renpy.fix_rollback()
        jump introservechoice

    "Stand by your principles.":
        $ renpy.fix_rollback()
        ro "Do your worst."
        jump jailbadend

label jailbadend:

je "That is very disappointing, hero. But I suppose it cannot be helped."
je "Goodbye Rowan, this is the last we'll be seeing of each other, I'm afraid."

"The guard returns and takes Rowan back to his cell."

play music "music/Dungeon Ambience.ogg" fadein 1.0
scene bg8 with fade

"Years pass. The guards continue to bring food, but neither Jezera nor anyone else ever visits again. With escape beyond him, and no news of his wife or the outside world, Rowan's fate is sealed."

scene black with fade

"Bad End #1 - The Prisoner"

menu:
    "Return to last scene.":
        $ renpy.fix_rollback()
        jump badend1return

    "End game.":
        $ renpy.fix_rollback()
        jump gameend


label introserve:

je "Excellent, I knew you would come to your senses eventually."

an "Do you swear to serve us then, human, and do whatever we ask of you?"

ro "Yes..."

show andras smirk at right with dissolve

"Andras smirks, as a new idea forms in his mind."

an "I have an idea on how you can prove that."

show jezera happy at midright with dissolve

je "I think I know where you are going with this, brother."

an "Why don’t you show us how willing you are to ‘serve’?"

"The pair were hardly being subtle, it was clear he would have to serve one of them sexually, and it was up to him to decide."

menu:

    "Jezera.":
        $ renpy.fix_rollback()
        $ jezeraIntroSex = True
        $ andrasIntroSex = False
        $ rowanJezSex =+ 1
        "If I have to have sex with one of them, Rowan thinks, I would prefer it to be the beautiful woman."
        ro "Jezera."
        je "Mmm, I was hoping you would say that."
        jump sexscene2

    "Andras.":
        $ renpy.fix_rollback()
        $ andrasIntroSex = True
        $ jezeraIntroSex = False
        $ rowanAndrasSex =+ 1
        "Something about the male demon, perhaps his toned body, or even his cocky attitude, drew Rowan to him."
        ro "Andras."
        an "Want to get fucked by a real man, do you hero?"
        $ rowanGaySex += 1
        jump sexscene3

    "Refuse.":
        $ renpy.fix_rollback()
        $ andrasIntroSex = False
        $ jezeraIntroSex = False
        ro "I've no interest in doing any of that with you demons, I'm a married man."
        show jezera displeased at midright with dissolve
        je "Disappointing, though it would do no good to force you. Your promise of loyalty will have to suffice for the time being."
        $ introserve = 0
        jump prologueend

label sexscene2:

scene cg11 with fade
show jezera naked happy behind cg11
show rowan aroused behind cg11
pause 2

$ jezera_name = 'Jezera'


"The demon slides her dress down to reveal her shapely body, curvaceous, with a pert pair of large breasts."
"Unlike his wife, the area above her cunt had been completely shaved, leaving nothing to the imagination."
"She turned and walked towards the throne, sitting on it, and spread her legs wide. With one finger, she beckoned Rowan to her."

je "Come here, hero."

"Gingerly, Rowan climbed the few steps between them until he stood before her."

je "Now, take off those pants, and kneel."

"Rowan did as he was told, removing the clothing on his lower body, and kneeling at her feet."
"Without saying a word, she lightly grabbed him by the hair and pulled his face forward toward her crotch."
"Clear on what is expected, Rowan began to tongue her pussy gently, causing her to let out a little moan."

je "Unnn... That’s it."

"He continued, running his tongue against her pussy lips, until he reached the clitoris, which he flicked lightly with the tip, causing her to let out another louder moan."

je "Someone has done this before."

"Rowan continued to lick her clit, and then began to suck on it gently, eliciting a shiver from Jezera."
"With a gentle shove, she moved his head down to her cunt hole, now sticky with her juices. Rowan gave it a probing lick, tasting her sweetness, before sliding his tongue deep inside."

je "Ohhhh..... Yessss....."

"The demon began to buck her hips against him as he moved his tongue inside her, while rubbing his nose against her clit."
"As she rose to orgasm, she grabbed his hair roughly and forced his face against her cunt as she locked her legs around him. As he struggled to breathe, Jezera came all over his face."

je "Uhhhhhhhh!!!"

"Jezera released her hold on Rowan, and he fell back onto the soft carpet of the throne room."

ro "Can’t... Breathe..."

"Still in post-orgasmic bliss, Jezera slid a hand down to stroke her pussy."

je "Not bad, hero. Mmmm... I’m going to have a lot of fun with you."

show cg12 with fade
pause 2


"She rose from the throne and steped behind Rowan, who had now sat up. She placed one arm around him, and with surprising strength, lifted him so that she was beneath him, with her back against the carpet."
"With her free hand, she gestured down toward his cock, now hard and glistening with precum."

je "Despite all the protestation, someone is clearly enjoying himself."

"Rowan burned with shame as she spat on her hand and grabbed his cock at the root. With a gently touch, she began to lightly jerk it up and down, with long soft strokes."
"As his cock started to throb in her hand, she moved to the top, and lightly traced her wet fingers around the sensitive purple tip."

je "Do you like that, Rowan?"

ro "Unnnn...."

"With a grin, she grabbed his cock at the root again, harder now, and began to jerk it firmly. Rowan let out a louder moan as her hand moved up and down, lubricated by her spit. "
"She moved faster as she licked and kissed his neck, causing him to grunt loudly. As he moved closer to orgasm, she can feel his manhood begin to throb harder and harder."

je "Do you want to cum, hero?"

"Close to orgasm and robbed of his senses, Rowan could only moan in response."

ro "Yessssss....."

je "Too bad."

"Smirking, the demon once again grabbed his dick again at the base, but this time, she did so so tightly, that it robbed him of climax."
"The cock throbed wildly in her grip, but could find no release. Rowan could only whimper as she held it firm until the moment had passed."

je "Don’t be too disappointed Rowan, I just didn’t want to waste all that lovely cum."
je "There’s a much better place for you to put it. Now, go and sit on that throne."

show cg13 with fade
pause 2


"Doing as he was told, Rowan stood and went over to sit on the throne. Jezera soon followed, mounting his cock, still rock hard from ruined orgasm, reverse cowgirl."
"Her pussy, tight and sodden from the foreplay, felt incredible against his dick. She leaned forward and began to move against him very slowly, moving her ass up and down on his member."

je "Mmmmm... Now this is more like it."

"Already sensitive from earlier, Rowan did his best to concentrate on not cumming as the beautiful demon moaned loudly while riding him."
"With each stroke, she rises higher and takes him deeper, the sensation becoming almost too much for him to bear."

je "So, are you enjoying serving me?"

"She moved faster then, bucking her hips and driving him toward climax."

ro "Uhhuhhh...."

je "And do you want to cum deep inside me?"

show cg13 with sshake
show cg13 with sshake
show cg14 with flash
pause 2

"The question was more than Rowan could bear as she dropped her hips to take all his manhood inside her cunt. He convulsed wildly as he shot his load deep within her."
"Jezera shuddered as she came one more time on his dick, letting out a long, loud moan of orgasmic bliss."
"Rowan sagged back on the throne spent, as Jezera lifted herself from him and stood, cum still oozing from her well fucked hole. She flashed him a cheeky wink, as she put her dress back on."

$ persistent.sex_scene2 = True
$ renpy.end_replay()

$ introserve = 1
jump prologueend

label sexscene3:

scene cg15 with fade
show rowan aroused behind cg15
show andras smirk behind cg15
pause 2

$ andras_name = 'Andras'

"With a smirk, the demon disrobed to reveal a cock far larger than anything Rowan had ever seen before. Thick, red, and veiny, he felt his own begin to stir at the sight of it."

an "Now get over here, and suck my cock."

"Rowan removed his clothes and knelt before Andras, who stood over him, making it perfectly clear who had all the power. The smell of his cock was overpowering to Rowan as he looked up at it from below."

an "By the time I’m done you’ll beg me to fuck you. Now start sucking."

"Inexperienced, but curious, Rowan started to lick the cock above him lightly, running his tongue from the base to the tip."

an "If you do a good job, maybe I’ll let you be my personal cocksucker."

"Finding the act arousing, Rowan began to grow more confident, licking the cock harder and faster. Upon reaching its strangely crimson head, he swirled his tongue around it."
"Once it was glistening with his spit, he slid it into his mouth and sucked on it softly. Using a free hand, he jerked the shaft while alternatively sucking and licking the head."
"The demon looked down to see Rowan’s dick is now rock hard and covered in precum, which made him chuckle."

an "Looks like somebody is enjoying himself, but remember, a good slut doesn’t forget to take care of the balls."

"Rowan burned with shame from the demon’s lewd suggestion, but that did not stop him from obeying it. He slid the tip of his tongue all the way down the length of the shaft, until he reached the balls."

an "You are good at following orders, which comes as a pleasant surprise following your earlier defiance."
an "Now, take me in your mouth."

"Rowan did as he was told, taking as much of the huge cock as would fit. Andras began to move his hips back and forward, as Rowan sucked it as best as he can."
"He also moved his head with Andras’ rhythm, accommodating as much of the massive member as possible."

an "Unnnn... Take it all!"

"Andras grabbed his throat with both hands and forced his cock as deep as he could, causing Rowan to gag."

ro "Mmmmfff!"

"The demon pulled his cock out of the smaller man’s throat and laughed. While Rowan coughed, he gave him a little slap on the face with his dick."

an "Don’t worry, with a little practice you will be deepthroating it in no time like a Qerazeli whore."
an "Now stand."

show cg16 with fade
pause 2

"Rowan rose, as the demon came up behind him and placed his hand over his mouth. Without warning, he spat on his hand and slid a finger into the human's tight hole."

an "If you are going to take my dick, I’m going to have to open up this tight little virgin asshole a little first."

"Rowan let out a muffled moan as Andras probed his ass, first with one finger, and then with a second. He began to slide the fingers in and out of his hole, opening it up a little more each time he penetrated it."

an "Now we are starting to get somewhere."

"Andras continued what he was doing, but started to slide his fingers in and out faster, causing Rowan muffled moans to grow more intense."
"He smirked as he looked down to see the human’s cock throb and twitch from arousal."

an "Remember when I said you’d beg me to fuck you?"

"He forced the two fingers in as deep as they’d go, and started to make a come hither movement with them, stroking Rowan’s g-spot. Rowan let out a low, loud muffled moan."

an "Do you want me to fuck you?"

"Rowan nodded enthusiastically as Andras continued to move his fingers inside him. He removed the hand that was covering his mouth."

an "I want you to say it."

ro "Please..."

"The demon smirked."

an "Please what?"

ro "Please.. Fuck me..."

show cg17 with fade
pause 2

"Andras laughed as he removed his fingers from Rowan’s ass. Sitting on the throne, he gestured for the other man to come and mount his huge cock."
"Without needing to be asked twice, Rowan lifted himself above the demon and slid the still lubricated dick as deep as he could."

ro "Unnnnn!!"

"The human began to move, greedily taking the cock into his willing asshole. Andras looked at the man and grinned."
"A great hero of good, who had been so defiant only a few months ago, was now riding up and down on his cock with aplomb."

an "Do you like having my cock in your ass, hero?"

"Rowan let out a moan of affirmation, which made the demon smile. He was going to have some fun breaking in this one."
"Placing one hand on his neck, and the other below his leg, he used his strength to help Rowan’s momentum, forcing him to take more of the huge cock in his ass."
"Before long, the rough movement, combined with tightness of Rowan’s hole, brought him close to climax."

an "Get ready for my load, slut."

"The thought was too much for Rowan, who let out a guttural grunt of orgasm, and shot ropey lengths of jizz on the demon’s stomach and chest."

show cg17 with sshake
show cg17 with sshake
show cg18 with flash
pause 2

"With one last pull, Andras brought the man down on his cock and came in his ass. Rowan collapsed against his chest, as a warm feeling filled him deep inside his hole. Andras let out a loud laugh."

an "If the Goddess of Light could see you now, with an ass full of demon cum."

"The human bristled at the comment, but made no attempt to remove the huge cock from his ass."

an "Go on, get up. If you serve us well, I might let you do this again."

"Rowan got off the throne and put his pants back on, while the demon did the same."

$ persistent.sex_scene3 = True
$ renpy.end_replay()

$ introserve = 1
jump prologueend


label prologueend:

if (introserve == 1):
    scene bg6 with fade
    show jezera happy at midright with dissolve
    je "Not bad hero, keep that up and you'll do very well around here, won't he brother?"
    show andras smirk at right with dissolve
    an "Indeed."

else:
    je "We will only tolerate this stubborness for so long though, hero. It would be wise to become a little more flexible now you are under our employ."



je "In the meantime, we have prepared a room for you. The guard will show you there now. Get some rest, hero, tomorrow is the first day of your new life."

scene black with fade

$ persistent.prologue_complete = True

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label rowangamestart:

stop music fadeout 1.0


if prologueSkip == True:

    "Why did Rowan agree to serve the twins?"

    menu:
        "To bide his time.":
            $ renpy.fix_rollback()
            $ serveChoice = 1

        "To avoid turning out like the other prisoner.":
            $ renpy.fix_rollback()
            $ serveChoice = 2

        "To see Alexia again.":
            $ renpy.fix_rollback()
            $ serveChoice = 3

        "Because Jezera was convincing.":
            $ renpy.fix_rollback()
            $ serveChoice = 4


    "Who did Rowan agree to serve?"

    menu:

        "Jezera.":
            $ renpy.fix_rollback()
            $ jezeraIntroSex = True
            $ andrasIntroSex = False


        "Andras.":
            $ renpy.fix_rollback()
            $ andrasIntroSex = True
            $ jezeraIntroSex = False
            $ rowanGaySex += 1


        "Neither.":
            $ renpy.fix_rollback()
            $ jezeraIntroSex = False
            $ andrasIntroSex = False
            $ introserve = 0


else:
    pass


"Would you like to see the game's netorare content?"
"If NTR is turned off, any options that you could make that would lead to NTR content will be blocked off. Generally, these are any scenes that would lead to Rowan's wife having sex with someone else, not including group sex involving Rowan. The story is otherwise unchanged."

menu:
    "Yes, I would like to see NTR content.":
        $ renpy.fix_rollback()
        $ NTR = True

    "No, I do not want to see NTR content.":
        $ renpy.fix_rollback()
        $ NTR = False

$ jezera_name = 'Jezera'
$ andras_name = 'Andras'


# choice to skip remaining part of intro
if config.developer:
    menu:
        'Dev mode choice - skip intro?'

        'Jump to map, week 1':
            jump end_of_intro

        'Jump to castle, week 4':
            # TODO: maybe set variables to defaults here
            $ week = 3
            $ journal.show()
            jump week_start

        'Continue':
            pass

"The orc guards escorted Rowan away from the throne room and towards the guest wing of the castle. They brought him to one of the rooms, then ushered him inside before closing the door behind him."
"Rowan chuckled somewhat wryly after hearing the sound of his door being locked and that one of the guards hadn't left with the others. He may have had better accommodations now, but he was still a prisoner."

scene bg9 with fade

"He surveyed his surroundings, immediately spotting his equipment laying on the bed. Gear that had been taken away from him when he'd been captured all those months ago."
"He picked up the blade, wincing in pain from the effort thanks to the stiffness in his arms."
"Instead of continuing, Rowan went through a simple warm up routine, trying to get his body into shape after being confined and beaten for so long."
"Soon he found himself too tired to continue on and slipped into the bed. Compared to his previous accommodations, the mattress and sheets felt heavenly and Rowan fell asleep almost immediately."
"The last thought that went through his mind was that of Alexia."

scene black with fade

"That night, Rowan's sleep was blissfully dreamless."
"Nearby, shortly after Rowan had fallen asleep..."

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

scene bg7 with fade
show alexia white neutral at midleft with dissolve
play sound "music/SFX/door knock.ogg"
pause 1

al "Coming."

show andras happy at midright with moveinright

al "Ah, I wasn't expecting you Andras, you don't usually visit this late."

an "That's because I'm afraid I won't be able to visit you as often anymore. I'm going to be leaving the castle soon."

show alexia white concerned at midleft with dissolve

al "Why, what's happened?"

an "Rowan is taking longer than he should have to arrive. Me and my sister need to know if he's decided not to come or if..."

"The red demon left that thought hanging in the air for a moment before holding out a strange necklace with a single blue gemstone to Alexia."

an "I wanted to give you this before I left, it will let us talk to one another over great distances so that I can keep you company even after I leave."

al "Thank you."

"Stepping forward, Andras placed the chain over Alexia's head and pulled her hair up over it.  He then demonstrated how to touch the gemstone and focus to communicate."

show cg20 with fade

"Just before stepping away, the demonic twin placed a finger under Alexia's chin and tipped her face up to look him in the eyes. He smiled to her and then kissed her on the forehead before taking his leave."

scene bg7 with fade

show alexia necklace concerned at midleft with dissolve
hide andras happy with moveoutright

"Alexia touched her forehead, her mind awash with thoughts of both her husband and the demon who was now going to be hunting him."

scene black with fade

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


scene bg9 with fade
pause 1
play sound "music/SFX/door knock.ogg"
pause 1
play music "music/Jezera 1 loop.ogg" fadein 1.0

show jezera neutral at midright with moveinright

je "Good morning hero, how was it sleeping in a bed again? Better than a dungeon cell?"

show rowan neutral at midleft with dissolve

ro "Yes, very nice."

"The blue skinned woman stepped to the side as a maid enters and placed a tray of food on the desk. She bowed to the demoness and then stepped back out."

je "I'm glad to hear that you appreciate my accomodations much better than my brother's. Though he still insists that we keep you under guard for the time being."
je "Should you prove yourself useful in the coming weeks, I'm sure that I can arrange for the end to that."

show jezera happy at midright with dissolve

"The demoness smiled sweetly to Rowan, suggesting that there would be much more than that for his good behavior."

ro "But only if I'm useful."

show jezera neutral at midright with dissolve

je "Why must you always focus on the negatives? Very well."
je "Now we come to your new life. You are going to be me and my brother's eyes and ears in the world. The one who will survey lands for our conquest and will coordinate our armies."
je "Your status as one of the heroes from the last war will give you safe passage to travel where you want and your experiences from that time make you the perfect scout and military adviser."
je "I have created a network of portals across the six realms that you will use to quickly travel between each and spread our influence before they have a chance to coordinate against us."

ro "Wait, you can transport anyone anywhere in the six realms undetected?!"

show jezera happy at midright with dissolve

je "Well, I can't open one just anywhere, but my reach is vast. This will be the trump card for our take over. My brother thinks of it as being the perfect way to launch surprise attacks."
je " I believe he should be more broad in his plans."

"Rowan had the impression that Jezera was referring to him with that statement."

show jezera neutral at midright with dissolve

je "Since you are most familiar with Rosaria, it is there that our reign will begin. We need to first secure a foothold, and that means the end of the baron's rule in the duchy surrounding my portal."
je "But first, familiarize yourself with the immediate area, and learn what you can about what has happened since you left. Report back your findings."

stop music fadeout 1.0

show jezera displeased at midright with dissolve

je "One more thing. Andras has left to begin mustering soldiers again and wants to test his forces. There was a village to the North of the portal that we passed by when we went to see you the first time, you are going to help him occupy it."

play music "music/Jezera 2 loop.ogg" fadein 1.0

show jezera happy at midright with dissolve

je "Tell the guard when you're ready to leave. I do hope you are a great asset to us Rowan. Enjoy your breakfast."

hide jezera happy with moveoutright

"Rowan was silent for several moments after the demonic twin left. Then he slammed his hand against the wall in anger."

ro "Damn it!"

stop music fadeout 1.0
scene black with fade

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

"Half an hour later."

scene bg10 with fade

show jezera neutral at midleft with dissolve
show rowan neutral at midright with moveinright
show orc soldier neutral at edgeright with moveinright

ro "So, this is the portal?"

je "Yes. Now Rowan, there's one last thing that we need to quickly take care of before you leave."

"She holds out a necklace to him with a single blue stone. Rowan takes it from her."

ro "I'm assuming this has some magical properties to it?"

je "It will allow you to communicate with me and my brother. It will also allow me to track your movements and transport you back to the castle. You won't be able to take it back off, but I must insist that you wear it while in our employ."

"\"Another prison.\"  Rowan thinks to himself as he places the medallion over his head and is instructed in its use."

show rowan necklace neutral at midright with dissolve

je "I'm going to send you out for a week now, then bring you back to the castle. Report anything important directly to us. Write detailed maps for everything else."

show jezera happy at midleft with dissolve

je "Good luck, my hero."

hide jezera happy with moveoutleft

scene white with fade


label end_of_intro:
# start to explore first map
$ week = 1
$ journal.show()
call map_exploration ('rosaria_map') from _call_mapExploration_1
jump before_week_end

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label gameend:

"To be continued...."

"Thanks for playing and taking your first steps in the world of Seeds of Chaos. If you have enjoyed what you have seen please consider supporting the Patreon and/or spreading the word."

# clear return stack and return to main menu
$ renpy.set_return_stack([])
return
