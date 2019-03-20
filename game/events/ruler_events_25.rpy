init python:
    event('more_futa_fun', triggers="week_end", conditions=('week >=4', 'futaIntrigued == True',), depends=('alexia_become_like_xzaratl',), group='ruler_event', run_count=1, priority=pr_ruler)



label more_futa_fun:

scene bg14 with fade
show alexia 2 necklace angry at midleft with dissolve
show succubus 2 neutral at midright with dissolve

al "..."

hide alexia with moveoutleft

scene bg14 with fade
show alexia 2 necklace angry at midleft with moveinright
show succubus 2 neutral at midright with moveinright

al " (Solansia’s grace…)"

"Alexia forced down a curse. What was up with these people? Was stalking her some sort of castle approved past time? A way to wind down after another daylong orgy? Or was she some sort of bizarre attraction to them, like an animal in a cage?"
"It was already bad enough that X’zaratl kept harassing her and her husband all the time, but did her succubi now also wanted in on the fun?"
"It was not unlikely, though the scantily clad succubus had yet to approach her. For the last several minutes, she kept following her without a word, eyes glued to her backside. "

show alexia 2 necklace neutral at midleft with dissolve

"Alexia shot her a short glance, knowing the demon wasn’t paying attention to anything above Alexia’s waistline. Long silver hair, outrageous bosom, curved horns… She seemed familiar…"

show alexia 2 necklace shocked at midleft with dissolve

al "(Ah!)"

show alexia 2 necklace neutral at midleft with dissolve

"She saw her before! She was one of the succubi present when X’zaratl was showing her the “joys” of having a phallus. An event Alexia was still somewhat conflicted about..."

menu:
    "See what the succubus wants from her.":
        $ released_fix_rollback()
        jump futa2sex
        
    "She’d rather not have her nether regions messed with again. Better to avoid her.":
        $ released_fix_rollback()
        "X’zaratl didn’t shy from using charms to get her way, and Alexia doubted her succubi were any different in that regard. Better to be safe than sorry."
        hide alexia with moveoutleft
        "Exploiting the castle’s twisting corridor, Alexia turned left suddenly, then bolted forward, quickly losing the succubus."
        show succubus 2 neutral at center with moveinleft
        succ2 "! ! !"
        succ2 "Aw, damn it! I got distracted by her ass!"
        scene black with fade
        show succubus 2 neutral behind black
        succ2 "Stupid, sexy rosarian redheads…"
        return
        
label futa2sex:

"No point delaying the confrontation…"

show alexia 2 necklace angry at midleft with dissolve

al "Can I help you?"

"She turned around, causing the demon to stop suddenly. Her gaze continued to linger on Alexia’s crotch for a moment, only to move up after several long seconds-"

show alexia 2 necklace concerned at midleft with dissolve

"Only to stop on her breasts."

show alexia 2 necklace angry at midleft with dissolve

succ2 "Hello~!"
succ2 "Yes, you can! Thank you for asking!"
succ2 "Sorry, I wanted to say something earlier, but I ended up staring at your ass."
succ2 "My bad~!"

"Alexia narrowed her eyes at the perpetually smiling succubus, who had yet to find her face. She recalled Rowan saying most of them weren’t exactly the sharpest tools in the shed, but she was starting to feel it was something of an understatement."

succ2 "I mean, like, you are killing it in that skirt! It really brings out your legs~~~"
succ2 "And your tits are also really nice!"

if all_actors['alexia'].corruption > 30:
    show alexia 2 necklace concerned at midleft with dissolve
    al "… Thank you?"
    al "(I guess?)"
    succ2 "You’re welcome~!"
    
else:
    show alexia 2 necklace neutral at midleft with dissolve
    "She narrowed her eyes at the succubus. And to think the church always painted the demons as soul-sucking, terrifying abominations… "
    show alexia 2 necklace concerned at midleft with dissolve
    al "(… But she has a point on the skirt. Maybe it is a bit too short…)"

show succubus 2 neutral at center with moveinleft
show alexia 2 necklace neutral at midleft with dissolve

al "Is that all? Can I go now?"

succ2 "Oh no, no! I wanted to talk to you about something important!"

"The succubus perked up, finally looking Alexia in the eyes. The simple motion made her outrageously large breasts jiggle, her one-piece doing nothing to support them."

if all_actors['alexia'].corruption > 30:
    "Knowing the demon wouldn’t mind, this time it was Alexia who took the opportunity to ogle the demon a little bit. She took a quick peek at her open cleavage, admiring her breasts."
    menu:
        "Massive tits sure look nice…":
            $ released_fix_rollback()
            $ change_corruption_actor('alexia', 2)
            
        
        "… Isn’t this a little bit too much?":
            $ released_fix_rollback()

else:
    "Alexia looked away in disgust. Were there really men who liked these sort of obscene udders?"

succ2 "It’s about Mistress X’zaratl~~~"
succ2 "You know she was suuuper excited about you and Master Rowan, right? "

if all_actors['alexia'].relation < 50 or alexiaSeparateRoom == True:
    succ2 "But recently, with you two acting all cold and distant with one another, she’s been feeling a bit down."
    show alexia 2 necklace shocked at midleft with dissolve
    if all_actors['alexia'].relation > 50:
        "Alexia blinked, surprised. Just because they’ve been sleeping in separate bedrooms didn’t mean things were bad between her and Rowan?"
    succ2 "So I was thinking – hey, maybe I should help you out a little? Get you in the mood? You can’t just keep your husband out of the marital bed!"
    succ2 "It attracts hungry succubi."
    succ2 "Like me!"
    
else:
    succ2 "I mean, not just her, we all did!"
    succ2 "The two of you are just so fun to have around! I just wish X’zaratl wasn’t so possessive of Rowan, so I could take him for a spin myself~ "

if all_actors['alexia'].corruption > 30:
    show alexia 2 necklace concerned at midleft with dissolve
    al "Keep your hands off my husband, understood?"
    
else:
    show alexia 2 necklace angry at midleft with dissolve
    al "You keep your hands away from my husband!"
    
succ2 "Ooooh, never heard this line before! Haha!"

al "..."

succ2 "I’m joking, I’m joking! Sorry~!"
succ2 "But for real, I’m not interested in your husband. At least not at the moment."

show alexia 2 necklace shocked at midleft with dissolve

succ2 "I’m here for you~!"

if all_actors['alexia'].relation > 50 or alexiaSeparateRoom == False:
    succ2 "You and Rowan are the best pairing in this whole castle! We just love watching you two experiment!"
    succ2 "But there is still so much more to explore~."
    if rowanFutaAnal == True:
        show alexia 2 necklace aroused at midleft with dissolve
        succ2 "And you know Rowan is aaaaaaaall up for it."
    succ2 "So here, let me help you~."
    
else:
    succ2 "You have to start paying more attention to your husband! How else will X’zaratl get her daily dose of threesomes?"
    succ2 "So here, let me help you~."

show alexia 2 necklace shocked at edgeleft with moveoutleft
show succubus 2 neutral at midleft with moveoutleft

show bg14 with sshake

"Without any warning the succubus jumped forward, pressing her lips against Alexia’s. She pushed Alexia’s body back, turning her to the side and pressing the woman against the wall."

if all_actors['alexia'].corruption > 30:
    show alexia 2 necklace aroused at edgeleft with dissolve
    al "Mmm-mm?"
    "Her lips were soft, and for some reason tasted like cherry~"
    show alexia 2 necklace angry at edgeleft with dissolve
    al "(Wait, what am I doing?!)"
    
else:
    show alexia 2 necklace angry at edgeleft with dissolve
    al "Mmmm!"

"She tried to push the demon away, but even though the woman was holding her with just one hand, Alexia couldn’t budge the succubus at all."
"She grabbed her arm, gathering her strength-"

succ2 "Don’t move~!"

show alexia 2 necklace aroused at edgeleft with dissolve

"Before she could react, Alexia felt the demon touch her between the legs, and suddenly experienced an overwhelming burst of heat and arousal."

al "A-ah?!"

"She recognized this feeling. She recognized this unforgivable rush of passion, of energy, -"
"- Virility."
"She looked down and watched, eyes agape, as a large, throbbing cock grew between legs, right under the succubus’ dancing fingers. It looked as if the woman was literally coaxing it straight out of her body, her mesmerizing fingers drawing Alexia’s newborn manhood into the succubus’ delicate hand."

if all_actors['alexia'].relation > 50 or alexiaSeparateRoom == False:
    if rowanFutaSuck == True or rowanFutaAnal == True:
        succ2 "You two had so much fun with it last time… So here~"
        succ2 "Enjoy!"
        
    else:
        succ2 "I’m sure in time, you’ll be able to convince your hubby to play with your cock a little."
        succ2 "You just need the right… Incentives to keep trying~"
        
else:
    succ2 "To know how to please your husband’s cock, you have to spend some time with one yourself!"
    succ2 "So here, enjoy~~~"

"They still stood in the middle of the castle hallway, and the Succubus did not appear to intent on taking their little encounter anywhere private."
"She had yet to touch her again, her hand still hovering near her nether regions, but the demon’s hot breath tickled Alexia’s ear, her heavy perfume was starting to make her feel dizzy…"

menu:
    "Push her away!":
        $ released_fix_rollback()
        show alexia 2 necklace angry at edgeleft with dissolve
        al "(D-damn it! Like hell am I going to let you do as you please!)"
        "Driven by desperation, she tried to punch to the demon in the face- "
        show succubus 2 neutral at edgeright with moveoutright
        succ2 "Oooh, you got spunk girl!"
        al "S-stay away from me!"
        succ2 "Oh! Haha, yeah, sure!"
        succ2 "I mean, duh! X’zaratl would have my head if she knew I was playing with her favorite pet without her."
        succ2 "And not in the fun “have my head between her legs” kind of-"
        al "S-shut up you dumb a-airhead!"

    "...":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 3)
        "She inhaled sharply, suddenly uncertain."
        "Was she really going to let her touch her here? Just… Allow her to assault her in the middle of the corridor, then wank her off?"
        "A long time ago, this would have been inconceivable, but now… With everything that was happening in the castle… And with this foreign body between her legs, throbbing with need, a part of her wondered…"
        "Did she really care if somebody found them?" 
        succ2 "So eager already…"
        show alexia 2 necklace shocked at edgeleft with dissolve
        show succubus 2 neutral at edgeright with moveoutright
        succ2 "Sorry! I really want to keep going, but Mistress X’zaratl would have my head if she caught me messing with you without inviting her to the party."
        al "Wha-?"
        succ2 "And not in the fun “have my head between her legs” kind of way."
        succ2 "At least I think not? I don’t think that’s really her style…"
        succ2 "Maybe she’d brainwash me into complete obedience? She’s always so cheery, I honestly don’t know what she does when she gets mad… "
        "The demon continued to babble on, but Alexia barely registered her anymore."
        
"How did she end up like this already? Attacked in the middle of the castle, now with dick between her legs, clearly visible to everyone who came across?"

show alexia 2 necklace concerned at edgeleft with dissolve

"Why did this keep happening to her?"

show alexia 2 necklace neutral at edgeleft with dissolve
        
"But she couldn’t just stand here like that. She needed to hide. She needed to get back to her room."

hide alexia with moveoutleft

"She bolted to the side, leaving the succubus behind her."

scene black with fade
show succubus 2 neutral behind black

succ2 "No need to say thank you~! Just doing God’s work!"

"… … …"
"… …"
"…"
 
if alexiaSeparateRoom == True:
    scene bg7 with fade
    show alexia 2 necklace concerned at edgeleft with moveinleft
    show bg7 with sshake
    "She slammed the door behind her."
    "Somehow, some way, she was able to get back to her room without anyone noticing her."

else:
    scene bg9 with fade
    show alexia 2 necklace concerned at edgeleft with moveinleft
    show bg9 with sshake
    "She slammed the door behind her."
    "Somehow, some way, she was able to get back to Rowan’s room without anyone noticing her."
    "Her husband wasn’t around, probably preoccupied with whatever ridiculous task the twins recently burdened him with."

al "(Solansia save me… When will this insanity end?)"

"With a tired sigh, she rested her back against the wooden door. How does she always end up in these situations?"
"None of the castle occupants, not even Andras, bothered here this much when she was first brought here. All of this only started to happen when Rowan also found himself enslaved by the twins."
"Was the knowledge he was somewhere in the castle, helpless to protect her, making this sweeter to them?"

al "(Goodness gracious…)"

if all_actors['alexia'].relation < 25:
    "None of this would be happening if her husband didn’t swear himself to the twins."
    "Or if she never married him."
    show alexia 2 necklace shocked at edgeleft with dissolve
    "The thought entered her mind like a treacherous snake, and Alexia regretted it instantly, feeling disgusted with herself."
    show alexia 2 necklace concerned at edgeleft with dissolve
    "Things weren’t perfect between them, but she couldn’t think like that. None of this was Rowan’s fault. She can’t blame him for it. She can’t."
    "She can't."
    
al "..."

show alexia 2 necklace shocked at edgeleft with dissolve

"Her cock twitched."

show alexia 2 necklace aroused at edgeleft with dissolve

al "Nn~!"

"For a moment she almost managed to forget about it - about the phallus between her legs - but the sudden pulse of desire brought her back to reality."

show alexia 2 necklace angry at edgeleft with dissolve

"What was she supposed to do with it? She could feel it throb gently. She could hear its cries for attention, sense its demand to be plunged into something."

show alexia 2 necklace neutral at edgeleft with dissolve

"But she would not see Rowan for some time, probably not until the evening."

if rowanFutaSuck == False or rowanFutaAnal == False:
    "And once she does, she doubted he would be willing to do something about it."
    
show alexia 2 necklace concerned at edgeleft with dissolve

"She breathed heavily, and rested her head. At least she could control herself, unlike what happened last time. If there was anything she could thank the succubus for, it was that she didn’t put her in a masturbatory frenzy like X’zaratl did-"
"Her cock twitched again."

if all_actors['alexia'].corruption > 30:
    show alexia 2 necklace aroused at edgeleft with dissolve
    al "O-oh!"
    
else:
    show alexia 2 necklace angry at edgeleft with dissolve
    al "Nn- stop doing that!"

"Not that she wasn’t close to it anyway. She felt like… Some sort of horny teenager…"

show alexia 2 necklace neutral at edgeleft with dissolve

"She knew spells like that were temporary, but despite that, she would likely be forced to endure her new cock for several hours… "

if all_actors['alexia'].corruption > 30:
    show alexia 2 necklace aroused at edgeleft with dissolve
    al "(If that’s the case… Maybe it wouldn’t hurt to inspect it a little?)"
    "For all the perversions she was witness to – or part of – in castle Bloodmeen, the futanari transformation was still one of the more bizarre ones. Tried as she might, she couldn’t deny a part of her was curious about it."
    "She was curious how it worked, how it felt, what it could do…"
    
else:
    al "(Why did I let X’zaratl cast that spell on me back then... And why did I talk to that succubus…)"
    "She cursed her own curiosity, and her own recklessness. Again, she found herself in a difficult position because of them. This… Thing between her legs, no matter how pleasant it might be to use, was not natural."
    show alexia 2 necklace concerned at edgeleft with dissolve
    "And yet… Despite knowing that, she could not deny a part of her was still curious about it. And if she really was stuck with it…"
    "Maybe it wouldn’t hurt to at least inspect it?" 
    "…"

"She felt her cock twitch again."

$ futaLust = 0
$ futaEventTempted = False

$ futaInspect = False
$ futaInspectTip = False
$ futaLick = False
$ fingerCheck = False
$ futaBaseCheck = False
$ futaStroke = False
$ futaIgnore = False

$ inspectAvailable = True
$ checkAvailable = True
$ tipAvailable = True
$ fingersAvailable = True
$ futaLickAvailable = True
$ strokeAvailable = True
$ keepStrokeAvailable = True

label futaMenu:

menu:
    "Inspect it." if inspectAvailable == True:
        $ released_fix_rollback()
        if futaEventTempted == True:
            $ futaEventTempted = False
        #cg1 
        scene cg284 with fade
        show alexia 2 necklace aroused behind cg284 
        pause 3
        "With a glint of unhealthy fascination in them, her eyes turned to the futanari phallus between her legs." 
        "It grew out from beneath her skirt, long and erect. It was noticeably bigger than even her husband’s, making it unnaturally long."
        "Did succubi have no sense of realistic proportions? Would it be even possible for them to fit it in without the use of magic?"
        if all_actors['alexia'].corruption > 50:
            "… Would she be able to, if she tried? "
        else:
            "Wouldn’t it hurt like hell? Or were they this elastic?"
        "… But regardless, it was a cursed tool of cursed magic. Something impure. Wrong."
        "And yet, it also seemed to fit so well between her legs. Like it belonged there…"
        $ futaLust += 1
        $ futaInspect = True
        $ inspectAvailable = False
        jump futaMenu        
        
        
    "Check the base of it." if futaInspect == True and checkAvailable == True:
        $ released_fix_rollback()
        if futaEventTempted == True:
            $ futaEventTempted = False
        al "(… How does it work?)"
        "Eyes still transfixed on the phallus, Alexia found herself moving her skirt back, her left hand reaching for the base of her new cock."
        "Her fingers brushed gently against the bottom of it, feeling it out. A pleasant tingle ran up her spine, one she tried to ignore. Hard and ready, it begged her to touch it further. To find some warm hole for it to fill."
        "Instead, her finger traveled further down."
        if futaLick == True:
            "She knew her futanari cock could produce cum – the lingering taste on her lips was proof enough. But where did it come from?"
        else:
            "She knew her futanari cock could produce cum – X’zaratl gave her a very graphic presentation on that. But where did it come from?"
        "How did it work…?"
        if alexia_ice_shard and all_actors['alexia'].corruption > 30:
            "… She should investigate further. She couldn’t rid herself of it, so why not use the opportunity to learn something new? There was still much she did not understand about magic."
            "Why discard the chance to expand her knowledge…?"
            $ futaEventTempted = True
        $ futaLust += 1
        $ futaBaseCheck = True
        $ checkAvailable = False
        jump futaMenu       

        
    "Inspect the tip." if futaInspect == True and tipAvailable == True:
        $ released_fix_rollback()
        if futaEventTempted == True:
            $ futaEventTempted = False
        "Her eyes ventured to the enlarged, red tip. Hesitatingly, she reached out to it, gently touching it with her right hand."
        "She hissed sharply. So sensitive! She never knew… Or maybe it was just the magic of the demons that made it that way."
        scene cg285 with fade
        show alexia 2 necklace aroused behind cg285 
        pause 3
        "She felt her fingers touch something wet and sticky. A few droplets of precum formed on the tip of her cock, which were now smeared across her hand."
        "… She wondered how it smelled. Would it be just like normal cum, or…"
        $ futaLust += 1
        $ futaInspectTip = True
        $ tipAvailable = False
        jump futaMenu       
        
    "Check her fingers." if futaInspectTip == True and fingersAvailable == True:
        $ released_fix_rollback()
        if futaEventTempted == True:
            $ futaEventTempted = False
        "There was no harm in checking, right?"
        "Still unsure of herself, she jerked her hand up, bringing it up to her face. She rubbed her fingers together, smearing the white substance between them."
        "Thick and sticky. Just like her cock, unnaturally so. Everything about this futanari cock of hers was just so… Overdone."
        "It was too large, the skin was too sensitive, the consistency of its cum reminded her of syrup, and the musky, heavy stench of it made her feel dizzy. And the taste of it…"
        if all_actors['alexia'].corruption > 50:
            $ futaLust += 1
            $ fingersAvailable = False
            jump futaFingerLick
        else:
            "… How did it taste?"
            $ futaLust += 1
            $ fingersAvailable = False
            $ fingerCheck = True
            jump futaMenu
            
    "Lick your fingers." if fingerCheck == True and futaLickAvailable == True:
        $ released_fix_rollback()
        label futaFingerLick:
        if futaEventTempted == True:
            $ futaEventTempted = False
        if all_actors['alexia'].corruption > 50:
            "Without thinking, she plunged her fingers between her lips."
        else:
            "Slowly, she opened her mouth, and put her fingers between her lips. A tiny part of her kept screaming this wasn’t right, but with every moment, it was growing less audible."
        al "(Salty…)"
        "As if in a trance, she licked her fingers clean, savoring the rich taste of her own precum."
        if rowanFutaSuck == True:
            "So this was what Rowan tasted…"
        else:
            "And to think Rowan didn’t want to taste it himself…"
        "It tasted amazing. She tasted amazing. Everything the demons made, was always so much more… Intense than its normal counterpart."
        "It made it so easy to drown in it…"
        "She forced herself to take her fingers out, and absentmindedly placed them around the head of her cock again. She knew she shouldn’t, but she really wanted to explore more…"
        $ futaLust += 1
        $ futaLickAvailable = False
        jump futaMenu
        
    "Stroke it." if futaBaseCheck == True and futaInspectTip == True and strokeAvailable == True:
        $ released_fix_rollback()
        if futaEventTempted == True:
            $ futaEventTempted = False
        "She moved her left hand up, along her cock, over the full length of it."
        al "A-ah!"
        "She couldn’t suppress the obscene moan. It was just her own hand, yet it felt so good to wrap it around her shaft, to stroke her throbbing manhood…"
        al "Aa-ah…"
        if rowanFutaAnal == True:
            scene black with fade 
            "And yet it paled in comparison to her husband’s ass, to the tightness of it."
            show cg147 with fade
            "The picture of him – bent in front of her, taking her futa cock up his ass, X’zaratl fucking his face-"
            "She couldn’t get it out of her mind. She couldn’t rid herself of the memory of her husband squeezing down on her cock~"
            scene black with fade
            show alexia 2 necklace aroused behind black
            al "Nn-"
            #cg1 
            scene cg285 with fade
            show alexia 2 necklace aroused behind cg285
            "A-aah! Ro-wan!"
            $ futaEventTempted = True
        else:
            "But this wasn’t enough. She wanted to experiment more with it..."
        "She wanted… She wanted something to plunge into…"
        al "..."
        "She slowed down her moments. She really… Shouldn’t be indulging herself so much…"
        $ futaStroke = True
        $ strokeAvailable = False
        $ futaLust += 1
        jump futaMenu
        
    "Keep stroking it!" if futaStroke == True and keepStrokeAvailable == True:
        $ released_fix_rollback()
        if futaEventTempted == True:
            $ futaEventTempted = False
        if all_actors['alexia'].corruption > 30:
            "She couldn’t help it. She couldn’t take her hands off it, nor could tear her eyes away. The more she explored her new dick, the less it felt like something foreign, and more like something that was a part of her."
            "A part of her that craved to be caressed, touched, sucked, used. And why should she not indulge it?"
        else:
            "It was dark magic. It was not natural. And despite that – despite that-"
            "She couldn’t deny the urge rising within her any longer. She needed to satisfy this gnawing need, and she no longer cared whether it was right or wrong."
            al "(Solansia forgive me…)"
        "She started to furiously move her hands up and down her shaft, stifling a moan as she felt a spike of pleasure spread across her body."
        if all_actors['alexia'].corruption > 30:
            "Her hips bucked forward, looking for something to plunge into. She couldn’t help it. This cock – this amazing cock – just made her feel so damn aroused~"
        else:
            "Her hips bucked forward, looking for something to plunge into. She couldn’t help it. This cock – this damned cock – just made her feel so damn aroused~"
        al "Nnn~~ aah, aaah! Aaah!"
        "But all she had was her small hands. Her small, feminine hands on her own massive, throbbing cock~"
        if all_actors['alexia'].corruption > 30:
            al "S-so good~"
        else:
            al "A-ah, why is it s-so good…"
        "She couldn’t control herself anymore, but she didn’t care. Driven my primal lust she kept fucking her palm-"
        if rowanFutaSuck or rowanFutaAnal:
            "If only Rowan were here!"
        al "AAAAH!"
        "It hit her suddenly – an unexpected spike of ecstasy –"
        "And with it, a stream of hot, white cum shot out, flying across the room, right on the room carpet. But she didn’t even notice it. She threw her head back, arched her back, and focused on this sweet, divine feeling."
        al "Aaa-aaah-aaah-aaaAAaaaH!"
        "It didn’t seem to end. A stream of constant convulsions, fueled by unnatural lust, draining her cock. Draining her. Draining her to fuel itself. More, and more, and more…"
        scene black with fade
        show alexia 2 necklace aroused behind black
        "… … …"
        "… …"
        "..."
        al "A-amazing…"
        if alexiaSeparateRoom == True:
            scene bg7 with fade
        else:
            scene bg9 with fade
        show alexia 2 necklace concerned at center with dissolve
        "Part ashamed, part fascinated, Alexia looked upon the several lines of white fluid that now decorated the floor. There was so much of it… It was almost unreal."
        "And yet, somehow, despite feeling tired, she didn’t feel satisfied. The dick in her hands still throbbed, demanding further attention from her. Already, she was ready to go again."
        if all_actors['alexia'].corruption > 30:
            "She wanted to go again… "
        else:
            "And a part of her - a part she desperately tried to deny existed - urged her to submit to this perverse pleasure. To go again, and again, and again, forget herself in the bliss of her cock..."
        $ change_corruption_actor('alexia', 5)
        jump futaEndingChoice
        
    "Try to ignore it." if futaEventTempted == False:
        $ released_fix_rollback()
        if all_actors['alexia'].corruption > 30:
            al "..."
            if futaInspectTip == True or futaBaseCheck == True:
                al "(I still want to feel it some more…)"
            elif futaInspect == True:
                al "(Just touching it a little won’t hurt…)"
            else:
                al "(Nothing wrong with looking it over..)"
            $ futaEventTempted = True
            $ futaIgnore = True
            jump futaMenu
        else:
            "She took a deep breath, and tried to think about something else than the thing between her legs. It was connected to her, yes. But it wasn’t hers. This was a curse, not a blessing."
            "She just had to occupy herself with something, and it will go away in a few hours…"
            $ futaIgnore = True
            jump futaMenu
            
    "Try to distract yourself." if futaIgnore == True and futaEventTempted == False and futaLust < 4:
        $ released_fix_rollback()
        if alexiaSeparateRoom == True:
            scene bg7 with fade
        else:
            scene bg9 with fade
        show alexia 2 necklace neutral at center with dissolve
        if futaInspectTip == False and futaBaseCheck == False:
            "Her mind set, she tore her hands away from the futanari phallus. With a determined expression, she headed for the shelf where she kept her cleaning supplies. She couldn’t wander the castle, so at least she’ll clean the place up."
        else:
            "Her mind set, she pushed herself away from the door, and headed for the shelf where she kept her cleaning supplies. She couldn’t wander the castle, so at least she’ll clean the place up."
        "Time and time again, it seemed like everyone around her conspired to make her do something she didn’t want to, force her to become someone she wasn’t."
        "And even though deep down, she couldn’t deny her fascination with this thing between her legs, she refused to let her lust control her. She had to be strong."
        scene black with fade
        "For herself, and for Rowan."
        $ change_corruption_actor('alexia', -5)
        return


        

            
            
label futaEndingChoice:

menu:
    "Go again.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 3)
        if all_actors['alexia'].corruption > 30:
            show alexia 2 necklace happy at center with dissolve
            "If it felt so good, then why should she deny herself?"
            "With a growing smile, she started to move her hands again…"
        else:
            "Even though it felt wrong – it was wrong – lust triumphed over reasons. With a feverish expression, she started to move her hands again…"
        scene black with fade
        show alexia 2 necklace aroused behind black
        al "Aaaah! Aaaah~!"
        "It didn’t take her long to come, spraying the floor white again..."
        menu:
            "Go again.":
                $ released_fix_rollback()
                al "Aaaah! Nnn-Aaaah!"
                menu:
                    "Go again.":
                        $ released_fix_rollback()
                        al "Aaa-a-a-aah!"
                        menu:
                            "Go again.":
                                $ released_fix_rollback()
                                al "Aaah~! Amazing, why does it feel so-"
                                al "Go-oood!"
                                menu:
                                    "And again.":
                                        $ released_fix_rollback()
                                        "… … …"
                                        "… …"
                                        "…"
                                        jump futaEpilogue
                                    

    "Once is enough. Restrain yourself.":
        $ released_fix_rollback()
        if all_actors['alexia'].corruption > 30:
            "With a remorseful sigh, she let go of her new toy. It was a fun thing, and with every session with it, she was gaining new appreciation for it."
            "But she wasn’t a succubus! She couldn’t spend her entire day playing with it!"
        else:
            "With a tired sigh, she took her hands off her new “present”. She didn’t want to, but she did."
            "It was a dangerous thing. It wasn’t natural – she knew that. But every time she indulged herself with it, she felt her revulsion weaken. She couldn’t let it control her. She couldn’t let it turn her into something like X’zaratl was..."
        "She adjusted her skirt – not that it did her any good, given what was between her legs – and assessed the damage her little “session” had done to the room."
        "Some of her cum landed on the stone floor, but most of it ended on the rug in the center of the room.  She eyed it dubiously."
        al "(I don’t think I’ll be able to wash that off…)"
        "With her cock still hurting and demanding attention, cleaning the room would be a headache, but she had no choice."
        if all_actors['alexia'].corruption > 30 and (rowanFutaSuck == True or rowanFutaAnal == True):
            al "(Rowan will be mad I played without him… Better to be rid of the evidence.) "
        else:
            al "(I don’t think I want Rowan to know I’ve been playing with myself…)"
        "In the end, the spell ended before Rowan visited her later that day, and her husband was none the wiser of what transpired."
        return  

label futaEpilogue:

scene bg14 with fade
show rowan necklace angry at midleft with dissolve

ro "Solansia save me, what difference does this make if the banner has spikes at the top of it or all around it…"

show rowan necklace neutral at edgeright with moveoutright

if alexiaSeparateRoom == False:
    ro "Alexia, sorry I’m-"
    scene bg9 with fade
    show alexia necklace shocked at midright with dissolve
    show rowan necklace shock at midleft with moveinleft
    
else:
    ro"Alexia, are you here?"
    show rowan necklace shock at edgeright with dissolve
    show alexia necklace neutral behind bg14
    al "J-j-just a moment!"
    show rowan necklace neutral at edgeright with dissolve
    "Her voice was strained, panicked. Without thinking twice, he barged into her room."
    scene bg7 with fade
    show alexia necklace shocked at midright with dissolve
    show rowan necklace shock at midleft with moveinleft
    
"He found his wife on the floor, scrubbing the stone surface in her nightwear. She looked as surprised with him as he was with her."

if all_actors['alexia'].corruption > 30:
    show alexia necklace happy at midright with dissolve
    al "Ah, dear, I apologize for startling you."
    al "One of X’zaratl succubi blessed me with a cock again, and I ended up playing with it the whole evening."
    al "I don’t think the staff will be able to wash the rug clean… I went a bit overboard there, ha ha."
    "She laughed in an embarrassed manner."
    "The whole room reeked of cum."
    if rowanFutaSuck or rowanFutaAnal:
        ro "Uh-huh."
        show rowan necklace happy at midleft with dissolve
        ro "You should’ve sent someone for me.  Looks like I missed all the fun."
        al "I apologize. I at first I didn’t want anyone to see me with it, at later I got a little overwhelmed by it."
        al "Next time, dear?"
        ro "Next time."
        return
    else:
        if avatar.corruption > 50:
            show rowan necklace angry at midleft with dissolve
            ro "You know I don’t want that thing anywhere near me."
            al "Oh, I know. It was mostly for practice."
            "Alexia smiled suggestively, and made a stroking motion with her hand."
            ro "Mhm."
            scene black with fade
            "He rolled his eyes. Guess he could forgive her this one time…"
            return
        else:
            show rowan necklace shock at midleft with dissolve
            ro "I- I see."
            "His wife still smiled at him, puzzled by his reaction."
            show rowan necklace concerned at midleft with dissolve
            "What was this place doing to her?"
            "(Solansia… If you still care for us, then please, look after my wife…)"
            scene black with fade
            show rowan necklace concerned behind black
            ro "… Here, let me help you with it."
            $ change_relation('alexia', -5)
            return
            
else:
    show alexia necklace concerned at midright with dissolve
    al "R-Rowan! I… I…"
    al "I-it’s not what it looks like!"
    show rowan necklace angry at midleft with dissolve
    "The whole room reeked of semen."
    if avatar.corruption > 70 and alexiaOffer == False:
        ro "What is the meaning of this Alexia. Were you fucking someone behind my back? "
        ro "Was it Andras?"
        ro "Tell me!!!"
        al "No, no! I’d never!"
    al "T-there was this succubus and she, um, she used the futanari spell on me, just like X’zaratl did a while ago-"
    al "And I, I- I couldn’t keep my hands off myself."
    "Her face was red with shame, and her eyes watered. She looked like she was on the verge of breaking down... "
    if avatar.corruption > 70:
        show rowan necklace neutral at midleft with dissolve
        ro "… I see."
        "Clean up then. And get some scented candles for this place."
        scene black with fade
        show rowan necklace neutral behind black
        ro "This entire room reeks."
        return
    else:
        show rowan necklace neutral at midleft with dissolve
        ro "… I see."
        if rowanFutaSuck or rowanFutaAnal:
            show rowan necklace neutral at midleft with dissolve
            ro "You should’ve sent someone for me.  Looks like I missed all the fun."
            "A huge wave of relief washed over Alexia, and she relaxed visibly."
            show alexia necklace happy at midright with dissolve
            al "I’m sorry. I was just so overwhelmed by this feeling… I knew I shouldn’t have, but it was hard to control myself! "
            ro "I understand. Let’s play together next time?"
            scene black with fade
            show alexia necklace happy behind black
            al "I’d love to."
        else:
            "A long silence followed. Neither knew what to say to the other."  
            "Alexia knew her husband didn’t approve of her cock. And Rowan knew she knew he didn’t approve. And yet somehow, she ended up with one again, and clearly could not resist its allure."
            show rowan necklace concerned at midleft with dissolve
            ro "(Alexia… What is this place doing to you?)"
            show rowan necklace happy at midleft with dissolve
            "Trying not to show his growing unease, he forced a pleasant smile on his face, and knelt beside her."
            scene black with fade 
            show rowan necklace happy behind black
            show alexia necklace concerned behind black
            ro "Here… let me help you clean up."
            al "… Thank you."
            $ change_relation('alexia', -5)
            return
