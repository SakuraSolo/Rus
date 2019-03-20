init python:

    event('shayas_gift', triggers="week_end", conditions=('castle.buildings["brothel"].lvl >= 1', 'week >=4'), group='ruler_event', run_count=1, priority=pr_ruler)
    event('threes_company', triggers="week_end", conditions=('liurialSex == True',),  group='ruler_event', run_count=1, priority=pr_ruler)
    event('the_demons_hobby', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)

label shayas_gift:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan stood in the throne room staring at the portal. He had to leave on his weekly field work. Once more the weekend had passed by in a drifting haze. At one point he had thought back on the lazy days in the immediate aftermath of the war. Where had that time gone?"
"In his thoughts, he didn’t notice for some time that he wasn’t alone. Though, this particular visitor seemed to have a talent for making herself not draw attention."

show shaya neutral at midright with moveinright

ro "Shaya?"

"The brothel's madam was waiting in the doorway, watching him silently. When he turned to her to address her, she adopted a lower posture. Head downcast, palms facing upwards, shoulders slouched."

sha "Sir Rowan. I’m sorry if I am intruding."

ro "No no. It’s alright. I still have a minute. Is there something you wanted to speak to me about?"

"Shaya nodded softly."
"She padded forward, barefoot against the stone floor, until she was quite close to him. He could smell the floral scent of whatever perfume she’d put on, and had to force himself not to stare at her exposed body with how close it was to him."

sha "I have a note, may I give it to you?"

"Rowan extended his hand, and Shaya handed over a small rolled up piece of parchment. It had the details of where a small caravan would be going through and where it would be unguarded the longest."

ro "What is this?"

sha "One of my girls managed to find herself in bed with a drunk nobleman. He had loose lips about a shipment of minerals being transported from the eastern mines. I had hoped that you would know what to do with it."

"Rowan looked over the note. It would be simple enough to arrange an ambush and capture the minerals for Bloodmeen. He could arrange for that in a matter of minutes. Rowan gave the shy woman an encouraging smile."

ro "This is most useful. You’ve proven yourself of great service today."

show shaya happy at midright with dissolve

"Shaya brightened up visibly. Beneath her veil, her eyes sparkled happily at the compliment."

sha "Really? I’m happy to hear you say that. I’ll be sure to return if I can bring out any more useful information."

"Shaya started back around to leave Rowan to his work. But, before she reached the doorway, she stopped and bowed slightly."

sha "I’ll leave you to your work, Sir Rowan. But, I do put on shows quite frequently at the brothel. I’d be very happy if you decided to graced me with your presence at some point. You don’t know how much it means."

ro "I’ll consider it."

"Shaya nodded softly, and almost skipped out. She seemed to have liked that answer. Rowan scratched his head slightly. That was the person Jezera had helping her manage the castle’s spy network?"
"He decided better of continuing to question it. The portal loomed large and he had a job to do."

$ shayaShow = True
$ change_treasury(+30)
return


###############################################################################################################
###############################################################################################################
###############################################################################################################

label threes_company:

#TO DO - Trigger percentage should start low, but rise as the game goes on until it’s very likely to have happened by week 70. 
#TO DO - Should stop being available if Alexia arrives at any option other than Pure Housewife.

scene bg9 with fade
show rowan necklace naked aroused at midleft with dissolve
show alexia necklace naked aroused at midright with dissolve

"Rowan had just returned from the field, and had returned to his corridors to do the first thing he’d wanted to do when he came back."

al "Harder. Fuck. Harder."

"He and Alexia were in bed together, deep in the throes of passion. The bed creaked loudly every time he slammed into her." 
"Which, of course, was right when the door opened."

scene bg9 with fade
show rowan necklace naked aroused at edgeleft with dissolve
show alexia necklace naked aroused at midleft with dissolve
show liurial neutral at midright with moveinright

liur "Lord Rowan. I wanted to discuss the…"

"Liurial burst through the door, looking down at a stack of documents in her hands. She looked up, only to meet eyes with Rowan midway through plowing his wife. Her eyes went wide and she dropped her papers in surprise."

liur "Oh."
liur "I’m so sorry."

"Liurial scrambled down for her papers, dropping her gaze in the process. With a groan, Rowan rolled over off of Alexia. She moaned softly at the sensation of his cock pulling out of her."

show rowan necklace naked at edgeleft with dissolve

ro "No no. It’s alright."

show alexia necklace naked at midleft with dissolve

"He walked over to the doorway to help the flustered elf with her documents. Alexia pulled the covers over her nakedness and giggled softly."

ro "Alexia. Liurial."
ro "Liurial. Alexia."

"Liurial, for her part looked half panicked. Rowan empathized with the poor girl. This was not the ideal way to meet the wife of the man you’re sleeping with. She froze up, as though not merely embarrassed, but terrified of the other woman."

liur "You must be his...uh...wife."

"He turned back Alexia."

ro "We’ve talked about her before. She was the one who asked me to protect her from a mercenary with grabby hands."

"Liurial shot Alexia a nervous look, but dodged back into a downcast when it seemed Alexia had noticed."

al "I recall. A heroic endeavour. I hope my husband is treating you well."

"There was a brief pause. Liurial was struggling to so much as formulate a reply. It made alarm bells go off in his brain. After all, he and Alexia hadn’t quite had the conversation he’d wanted about Liurial."

liur "Oh yes, Lord Rowan is most kind."

al "I see…"

show alexia necklace naked concerned at midleft with dissolve

"Alexia looked back and forth between her naked husband and the blushing girl collecting the dropped papers. It was like fire had just been lit in her brain."

al "Rowan, join me in private for a moment."

show rowan necklace naked concerned at edgeleft with dissolve

"Rowan knew at once that something was wrong. Her expression had hardened into the face she made when something was serious."

hide liurial with dissolve

"Alexia covered herself with the blanket still and walked into the closet. Rowan followed, closing the door behind him so that Liurial couldn’t overhear. The last he saw of Liurial before closing the door was the elf standing in place with a sunken expression."
"Once inside, the first thing Alexia did was throw on her nightie."

show alexia necklace concerned at midleft with dissolve

al "There’s something about her behaviour. She’s so stiff. Yeah, she caught us in an awkward position, but in this place, finding people having sex is basically common."
al "I can’t quite put my finger on what’s wrong, but…"

"She paused, as if chewing over her words."

al "I think that the awkward part is me."
al "You haven’t slept with her, have you?"

menu:
    "Claim you never slept with her.":
        $ released_fix_rollback()
        $ rowanLiurialLie = True
        if raeve_keep_rowan_claimed_helayna == True:
            "Rowan almost felt a bead of sweat drip down his forehead. How could he tell Alexia to her face that he’d strayed from his marriage vows with Liurial?"
        else:
            "Rowan almost felt a bead of sweat drip down his forehead. How could he tell Alexia he was sleeping with another woman? Especially considering how upset she’d been when she learned about Helayna."
        ro "Slept with her? No, of course not."
        "He put a hand on her shoulder to reassure her."
        ro "She’s my secretary. She helps me with the books. That’s all. Why did you jump to that first?"
        al "I...you’re right. I just had this strange feeling, that something was wrong. I guess I’m just being paranoid."
        "Rowan’s heartpanged. There was something horribly sad about her expression. She had been right. He and Liurial were actually sleeping together. All he’d done was make his own wife feel bad for her very real suspicions."             
        "Or at least maybe make her feel bad. Even as the two walked back out to continue talking to Liurial, Alexia was still glancing back and forth between Rowan and Liurial."
        $ change_base_stat('g', +2)
        jump alexiaLiurialThreesome

    "Tell Her The Truth.":
        $ released_fix_rollback()
        ro "…"
        "Rowan paused, trying to put together the words. He’d meant to speak to Alexia about it before. After all, surely if he explained the situation, she’d understand why he was sleeping with Liurial, and how little it meant about their relationship."
        "He took a deep breath."
        ro "Yes, I have."
        "Alexia’s face darkened in the shadows of the closet."
        al "I suppose I’ve said that you could do what you had to do."
        "Then she looked up at him, looking into his eyes. There was real anger in them."
        al "Still, why was this something you had to do? Sleeping with someone because you had to is different then doing it for fun. We still have vows."
        if all_actors['alexia'].relation < 30 and alexiaUnfaithful == True:
            "Yet, her face softened as soon as she said it. Hesitation snuck into her voice. It was like she was reconsidering her words even as she said it. Rowan raised an eyebrow, unnerved by her sudden mellowing."
        else:
            pass
        jump ALThreesomeConvo
        

label ALThreesomeConvo:

menu:
    "You can use her too if you like.":
        $ released_fix_rollback()
        "Rowan sighed. He needed to help Alexia see the upsides to having Liurial around."
        ro "Look, the girl threw herself at me. She basically placed herself at my feet. She’s skilled. She’s intelligent. And she swore she belonged to me."
        ro "You’re not looking at this with clear eyes. She’s not your competition. By her own choice, she’s more of a possession."
        ro "But, you’re my wife. What’s mine is yours. That means she as much yours as she is mine. Heck, if you’d like to try sleeping with her too, I can hardly protest."
        if all_actors['alexia'].corruption > 50:
            "Alexia looked down in contemplation, sneaking a glance up at Rowan here and there."
            al "…"
            "But, it was clear by now that neither of them were the same people they’d been when they’d first come to this place. They’d changed." 
            show alexia necklace happy at midleft with dissolve
            "A mischievous little smirk appeared on her face."
            show alexia necklace neutral at midleft with dissolve
            ro "Once you might have said that you’ve never had sex with another woman before."
            al "Once."
            al "I’m not mad at you about her. If she’s loyal to you, then you might need someone like her. But, in the future, if you’re sleeping with some secretary, you tell me."
            ro "I’ll try."
            ro "Thank you."
            if (all_actors['jezera'].favors + all_actors['andras'].favors) < 5:
                "Alexia planted a soft kiss on his lips. It was almost a thank you for the new toy that he’d basically given her."
            else:
                pass
            "Rowan and Alexia walked out of the closet together. Liurial had been waiting for them, chewing on her lips, but her expression softened when she saw that neither of them looked particularly upset with her."
            $ change_relation('alexia', +5)
            jump alexiaLiurialThreesome
            
        else:
            "Alexia stared at Rowan with something approaching horror. It seemed he’d totally misjudged how she’d react to what he said."
            show alexia necklace angry at midleft with dissolve
            al "What’s mine is yours? Are you kidding me right now?"
            "Her face reddened with anger."
            al "I don’t want to fuck your secretary. What is this place doing to you?"
            "Before Rowan could get in another word, Alexia stormed out of the closet."
            $ change_relation('alexia', -5)
            $ change_base_stat('g', +2)
            jump alexiaLiurialStormout
            
    "I need to keep her loyal.":
        $ released_fix_rollback()
        ro "You’re right. You’re absolutely right. I should have told you about her. I was just trying to spare you from having to know about what I have to do every day."
        ro "But, she’s my secretary. One of the few people in this place who is loyal to me and not to the twins."
        ro "Having her look to me as more than just a boss is vital. It certainly makes it less likely Jezera will sink her talons into her."
        ro "I can’t have her whispering behind my back, and in this world, sleeping with her helps ensure her loyalty."
        "He put a hand on her shoulder."
        ro "It’s unfortunate, but these is the rules of the game we have to play by."
        if all_actors['alexia'].corruption > 30:
            "Alexia paused to think. Rowan was left on egg shells the entire time. Would she really accept that explanation? Or would she have insisted it wasn’t necessary. This was the moment he’d worried about for so long."
            "Then she finally nodded her head and responded softly."
            al "Jezera is sleeping with half of the castle. And she has spies everywhere."
            al "I suppose if it works for her, it could work for us too."
            al "Though, I’m less than comfortable about my hero being reduced to those kinds of tactics."
            "He exhaled. She did understand after all. Rowan could only imagine she was just as aware of the compromises life in the castle entailed as he was."
            if all_actors['alexia'].relation > 30:
                al "Just please be careful, all right? And don’t engage in this sort of behaviour more than you have to."
                "She pressed herself close to him. Her naked bosom met his chest."
                ro "No more then I have to. I promise."
            else:
                "She looked off to the side, almost apprehensive in her expression."
                "We all have things that we have to do. It may not be pleasant, but sometimes we have to let ourselves be involved in things we might not otherwise have ever seen ourselves doing."
            "There was a brief pause, made all the more awkward by the fact that Liurial was no doubt still waiting for them to emerge from the closet."
            al "…"
            al "Is she good though? You know, in bed?"
            "Rowan sputtered. He hadn’t expected to hear that from her. Especially without prompting. Was she interested in Liurial? Or just being jealous?"
            "He decided to try to find out."
            ro "You could find out if you want. She’s sworn herself to me. And you’re my wife. The most important woman in my life. I have no doubt she’d serve you as well."
            "Alexia blushed hard but nodded softly. Evidently she was actually thinking about it."
            "Rowan and Alexia walked out of the closet together. Liurial had been waiting for them, chewing on her lips, but her expression softened when she saw that neither of them looked particularly upset with her."
            if avatar.corruption < 49:
                $ change_corruption_actor('alexia', 3)
            else:
                pass
            jump alexiaLiurialThreesome
        else:
            "Alexia paused to think. Rowan was left on egg shells the entire time. Would she really accept that explanation? Or would she have insisted it wasn’t necessary. This was the moment he’d worried about for so long."
            show alexia necklace angry at midleft with dissolve
            "Finally she looked up at him and shook her head in disgust."
            al "There are things we have to do and there are things we don’t have to do."
            al "It might be useful to fuck some elf secretary. But you never had to do anything of the sort. Don’t give me that."
            if alexiaUnfaithful == False:
                "Without a further word, Alexia turned away in a huff and stormed out of the closet."
                $ change_relation('alexia', -5)
                jump alexiaLiurialStormout
            else:
                show alexia necklace sad at midleft with dissolve
                "But, before she could get too worked up with rage, something invisible seemed to stop her. She ducked her head down with shame."
                al "Still, I suppose we all make mistakes. And this place...this place is always so sexual. So forward. Sometimes it’s hard to know right from wrong."
                al "Sometimes mistakes are made."
                al "So I can forgive you. Just...don’t do it again, alright?"
                "She pressed her head to his chest, and he responded by wrapping his wife in his arms. There was an unspoken sadness between them. Like a cloud hanging above both their heads."
                ro "Alright."
                "Rowan and Alexia walked out of the closet together. Liurial had been waiting for them, chewing on her lips, but her expression softened when she saw that neither of them looked particularly upset with her."
                jump alexiaLiurialThreesome

    "She was in trouble and needed protection.":
        $ released_fix_rollback()
        ro "Liurial came to me looking for a protector. Jezera had been harassing her. She was probably was considering her as a candidate for her latest pet."
        ro "She begged me for my help."
        "Alexia shook her head. She wasn’t buying it."
        al "That’s noble of you, I suppose. But, why did you have to have sex with her? Can’t you take her under your protection without making her your latest…"
        al "...Conquest?"
        "Rowan put a hand on her shoulder."
        ro "I wish I could. But, you know that no one would respect that. I’m not strong enough to keep her out of harm's way if she’s just a subordinate. But, even Jezera has enough restraint to know not to sleep with with my woman."
        if alexiaJezeraSex > 0:
            "Alexia blushed softly, and didn’t meet his gaze. Rowan tilted his head slightly at her reaction. Was there something wrong?"
        elif all_actors['alexia'].corruption > 30:
            "She nodded softly, placing one hand on top of Rowan’s."
            al "I understand. You don’t have to say more than that. We’re prisoners in this place and sometimes that takes unseemly actions if one wants to keep their soul."
            al "If this is what you have to do then it is what you have to do."
            "Then she looked him in the eyes, giving him a surprisingly forceful look."
            al "But, I’m your wife. If you want this girl on the side, that’s fine. She needs to be aware that I come first."
            ro "I assure you. She knows."
            "Rowan and Alexia walked out of the closet together. Liurial had been waiting for them, chewing on her lips, but her expression softened when she saw that neither of them looked particularly upset with her."
            jump alexiaLiurialThreesome
        elif all_actors['alexia'].corruption < 30 and alexiaUnfaithful == True:
            al "I…"
            al "I…"
            "Alexia went silent, placing a hand a hand on her head. She was right about to start to speak before thinking better of it. It was as though there were words sitting on her tongue that she just couldn’t get out."
            al " Fine. I’m not happy about this. But, I understand. There was an attractive woman throwing herself at you. You wanted to help her out. These things happen."
            "She looked down darkly."
            al "Thank you for telling me."
            al "I forgive you. It’s okay for you to help this girl. Be with this girl as much as you need to be."
            al "But, I’m your wife. I want to come first. You can’t forget who you said your vows too."
            ro "Never. I would never forget. You come before anyone else. Always."
            "She pressed herself to his chest. They gripped each other, as much for the sake of clinging to their spouse as themselves."
            "Rowan and Alexia walked out of the closet together. Liurial had been waiting for them, chewing on her lips, but her expression softened when she saw that neither of them looked particularly upset with her."
            jump alexiaLiurialThreesome
        else:
            al "I…"
            "Alexia went silent, placing a hand a hand on her head. But, this didn’t take long at all. She soon looked up at him with a red hot glare."
            al "No."
            al "No."
            al "I understand how this place works. I really do. But, this is not okay. I’m your wife. She’s some girl who threw herself at you."
            "She took a step back from him, leaving Rowan standing there with a gaping jaw. If anything was going to calm her rage, it would have been that appeal to heroism. But, there was simply no way that she’d be happy about him breaking his vows this way."
            al "I suppose in this situation I can’t stop you. But, if you think I’m okay with this, you’re dead wrong. Dead wrong. She needs to leave right now."
            "Rowan started to stammer."
            ro "I..."
            "Before Rowan could get in another word, Alexia stormed out of the closet."
            $ change_relation('alexia', -3)
            $ change_base_stat('g', +1)
            jump alexiaLiurialStormout  


label alexiaLiurialStormout:
show liurial neutral at midright with dissolve    

liur "Lady Alexia?"

show alexia necklace angry at midleft with dissolve
"Liurial attempted to approach Alexia. She adopted a small slouched posture. An attempt to reduce the red head’s fury that found no success."

al "Get out."
al "Just get out."

"Liurial stammed to get a word in, amidst the oppressive glare radiating from Alexia."

liur "I…"

al "Out!"

show bg9 with sshake

hide liurial with moveoutright

"Alexia screamed at the surprised elf. The message certainly seemed to have gotten across. Liurial scrambled out the door, leaving Rowan slowly trying to approach his riled up wife. Alexia stood in the middle of the room fuming."
"Rowan tried to reason with her, but she was too mad to speak. It took a full half hour before she calmed down enough to sit back down with him. It took further finagling not to get her to try to kick him out of his own room."

show alexia necklace sad at midleft with dissolve

"When it was over, and she settled down, the two were sitting by the windowsill. For all her anger, Alexia was not the hysterical type. With her shoulders slouched and her slumped over expression, she just seemed sad."

al "What is this place doing to you? What is this place doing to us?"

"Rowan didn’t know what else to do except hug her. She accepted with a sigh."

$ alexiaThreesomeStormout = True
return

label alexiaLiurialThreesome:
scene bg9 with fade
show liurial neutral at midright with dissolve
show rowan necklace naked at edgeleft with dissolve
show alexia necklace happy at midleft with dissolve

"Alexia stopped in front of Liurial. The elf was standing straight, almost on edge. Alexia smiled at her softly."

al "I apologize for the wait. That was so rude of me. There was just something that me and Rowan needed to talk about urgently."
al "It’s good to finally meet you, Liurial."

show liurial happy at midright with dissolve

"Rowan took a seat on the bed, and the other two sat cross legged on the floor. The two talked, mostly about the kind of work Liurial did and about him. Rowan blushed and laughed playfully when they both shared embarrassing stories about him."
"But, after the initial concern, the two seemed to get along with one another. For all their differences, as a Rosarian peasant housewife and a refugee elf, the two found commonality in their civility, their diligent demeanor..."
"...And most of all, their mutual experience being gawked at by every hungry eyed cretin in an entire castle full of hungry eyed cretins."
"Before long, Liurial visibly started to relax. Her shoulders slumped and her posture shifted forward. Spending time talking to Alexia seemed to dissipate the tense air all by itself."

if all_actors['alexia'].corruption < 30:
    if rowanLiurialLie == True:
        "Yet, a pleasant conversation seemed to be all it was. Alexia looked on Liurial with genuine sympathy and friendliness, but there was a certain coolness about it, no matter how hospitable."
        "For scant moments, Rowan fantasized about the possibility that this might lead to more. The thought of Alexia and Liurial both naked and pressed close to one another certainly had a nice texture to it."
        "He still indulged slightly in that fantasy even as Alexia walked Liurial to the door. It seemed her little visit was at an end."
        return
    elif avatar.corruption < 30:
        "Yet, a pleasant conversation seemed to be all it was. Alexia looked on Liurial with genuine sympathy and friendliness, but there was a certain coolness about it, no matter how hospitable."
        "For scant moments, Rowan fantasized about the possibility that this might lead to more. The thought of Alexia and Liurial both naked and pressed close to one another certainly had a nice texture to it."
        "He still indulged slightly in that fantasy even as Alexia walked Liurial to the door. It seemed her little visit was at an end."
        return
    elif avatar.corruption > 30 and alexiaUnfaithful ==True:
        "A moment to take it further arrived out of the blue. A pause set in over the room. Liurial gave Alexia and Rowan a shy glance. It gave Rowan an idea."
        ro "Liurial, I don’t believe I’ve ever asked you, but is attraction to both males and females common in elven society?"
        "Liurial nodded softly, though Rowan caught her eyes briefly fall on Alexia."
        liur "In Elven society it is tolerated but not encouraged. Our long lives make temporary couplings by non-breeding pairs less uncommon."
        liur "In truth, when I was first coming into maturity, I had a partnership of a few years with a female."
        "Alexia leaned in slightly."
        al "I see."
        "A soft grin played on Rowan’s face."
        ro "So do you find Alexia attractive?"
        show alexia necklace aroused at midleft with dissolve
        show liurial aroused at midright with dissolve
        "Alexia and Liurial both seemed to flush at once. For the briefest moment, a glance bridged their eyes. Then Liurial spoke up."
        liur "Yes. Very."
        "Rowan slipped off the bed and sat on the floor. After all, here could take a closer look."
        ro "Would it be okay with you, Alexia, if Liurial kissed you?"
        "Alexia put her hands to her mouth and looked back and forth between Rowan and Liurial. The sheepish elf certainly was aggressive, but the blush and soft eyes she was making suggested she was a willing participant."
        "Liurial took off her hat and put it to her side."
        "Alexia raised an eyebrow to Rowan. But, that was the last of her reluctance. She locked eyes with Liurial and developed a blush to match the elf."
        al "Yes, I wouldn’t mind that."
        #elfsome cg1
        scene black with fade
        show rowan necklace naked aroused behind black
        show liurial aroused behind black
        show alexia necklace aroused behind black
        "Liurial leaned in and closed her eyes. A heartbeat passed. Then, Alexia followed suit. Rowan watched eagerly as their lips touched one another." 
        "At first it was a timid contact. No tongues. Not much movement of their bodies. Liurial was naturally reluctant to be aggressive with her protector’s wife. Alexia, meanwhile, was almost certainly not very used to the soft lips of a woman."
        "But, no matter what reluctance she brought in, Alexia clearly had a taste for Liurial. Her head surfed forward, and the kiss grew deeper. Liurial tilted her head backwards and accepted as Alexia took lead."
        $ change_corruption_actor('alexia', 3)
    else:
        "But, before Rowan could even consider how he might take this situation further, he saw a mischievous glint in Alexia’s eye."
        al "Liurial, you’ve been with my husband, right?"
        "Liurial blinked twice."
        liur "Excuse me, Ma’am?"
        "Alexia leaned closer. Their respective postures left Alexia positioned above Liurial."
        al "Carnally. You’ve been with him, right?"
        show liurial neutral at midright with dissolve
        "Liurial shot a surprisingly obvious look up to Rowan. He nodded softly and then lowered himself to the floor. That was all Liurial needed."
        show liurial aroused at midright with dissolve
        liur "I have."
        show alexia necklace aroused at midleft with dissolve
        "Despite the fact that Alexia was in the driver’s seat here, she still seemed rather flushed. Rowan watched closely."
        al "And if you consider yourself his woman, and I am his wife, does that make you my woman as well?"
        "Liurial slowly nodded, now incapable of looking away from Alexia. Their lips were only a few inches from one another."
        al "What if I wanted to kiss you. Just to see what it feels like?"
        al "I’ve never kissed an Elf before. Few human girls have."
        liur "I wouldn’t mind that, Ma’am."
        "Liurial pulled the hat off her head without breaking eye contact with Alexia."
        liur "I wouldn’t mind that at all."
        #elfsome cg1
        scene black with fade
        show rowan necklace naked aroused behind black
        show liurial aroused behind black
        show alexia necklace aroused behind black
        "Alexia leaned forward, and pressed her lips to Liuiral’s. There was little build up needed. Alexia was clearly eager, and while Liurial’s timidity left her movements initially stiff, desire put more energy into her movements."
        "Their respective positions said it all. They leaned forward with their eyes closed, but Alexia was leaning forward and had positioned her head slightly above Liurials. It left the elf leaning back, letting Alexia take the lead."
        "Rowan watched the unfolding scene with rapt attention. How had it all turned out so well?"

"Rowan leaned closer. Of course neither of them minded his greater attention. Though any thought that this might be a show for him was dispelled by how quickly Alexia had become riled up. The moans and shallow gasps that escaped the kiss were very real."
"Liurial's hands went up to her shoulders. The willowy fabric that made up her dress offered no resistance as she pulled it to the sides. The kiss broke so Liurial could finish working her dress off of her body."

al "What are you…"

"But, Alexia paused mid sentence at the sight of Liurial’s willowy petite form. Her eyes traced Liurial nape to pussy. Without a further word Alexia’s hands went to her own nightie. It joined Liurial’s dress in a pool at their knees."
"When the kiss rejoined, their entire bodies pressed against one another. Soft hands explored soft bodies. Liurial almost seemed to be absorbed in Alexia’s modest but still far larger bossom. Lips meetings lips. Body meeting body."

show alexia necklace naked aroused behind black

if avatar.corruption > 30:
    "Alexia broke the kiss, though her hands continued to explore Liurial’s body. Liurial rolled her head back and let out a groan. But, Alexia was looking at Rowan with lustful eyes."
    al "What are you waiting for? Going to join us?"
    "Rowan nodded slowly, enraptured by the sight in front of him. With no clothes to remove, he crawled over to the two women and joined his body with theirs."

else:
    "Rowan scooted closer to the two women, putting one hand on each of their backs. Alexia broke the kiss with a gasp, but neither of them seemed to much mind his intrusion. They were both used to his touch."
    ro "Room for one more?"
    "Alexia giggled and shot Liurial a grin."
    al "What do you think?"
    "Liurial breath was coming out heavy, but she managed a dainty giggle."
    liur "How could I refuse?"
    "And just like that, two became three."
    
"Rowan leaned down on Liurial, planting a strong kiss. His secretary was all too happy to receive the attention, pressing her hands to his chest. Alexia was not to be denied, and she in turn leaned on his neck to suckle on it. Her breasts jutted into his side."
"All three of them softly ground their hips against each other’s bodies. Dry humping and generally basking in the the warmth and physicality."

al "I have an idea."

#elfsome cg2
scene cg242 with fade
pause 3

"Alexia took a position behind Liurial. Her arms wrapped around the elf’s body and her bosom teased the blond by pressing into her back. Before Liurial could even ask what was happening, Alexia’s hands grasped Liurial’s nipples and toyed with them." 
"Liurial’s eyes sealed shut and she let out a long low moan. Just the opportunity for Alexia to take possession of her lips once again. But, Rowan wasn’t focused on that. He was focused on the fact that Liurial’s legs seemed to spread all on their own."
"Her thighs glistened. No need for further lubrication. Her body was practically calling out to him with a need to be fucked."

#elfsome cg2 variant 2
scene cg243 with fade
show rowan necklace naked aroused behind cg243

"Rowan took the opportunity to slide his nearly painfully erect cock inside of her. At the feeling of his head pressing into her Liurial let out a loud sound muffled by Alexia’s lips. She gave a short little spasm as his shaft worked its entire way in."
"The body of three people in motion is not the same as two. Every time he would piston forward into Liurial’s welcoming body, the force of it would grind into Alexia. And when Alexia would push her own body in response to Rowan’s it would push Liurial’s with it."
"In this way three bodies acted almost like two. Rowan would thrust, Alexia counter-thrust. And in the process they used Liurial’s squirming body almost like a ragdoll. Alexia was fucking him using Liruial as a puppet."
"Though if the elf even had the clarity of thought left to protest, or the will to do so, it was absolutely silenced by the shallow desperate kisses she exchanged with Alexia."
"The rhythm of their hips grew faster. The friction of her tightness against him drove him all the closer to eruption. Their bodies made a strange music in their motion. Slapping sounds, wetness, sounds, moan and groans of all sorts. All of it his a temporary crescendo at once."

ro "Ugh!"

"He felt a powerful burst of pleasure, and then a load of his seed shot into Liurial’s pussy. Whiteness leaked out, in whatever space his cock allowed. And yet, even as the motion ground to a stop, he could feel the beginnings of another round starting to stir."

#elfsome cg3
scene black with fade
show liurial naked aroused behind black
show alexia necklace naked aroused behind black

"After a break of a minute, spent mostly panting and hyperventilating as opposed to speaking, the positions shifted again. Liurial was laid back with her legs spread. Rowan’s cum had formed a pool in her pussy. Which is why Alexia was on all fours, with her face mere inches away."
"All that cum would only be seasoning for her pussy’s taste."
"Rowan took position behind her, still grunting softly. Already his cock was nearly back to full stiffness. Certainly stiff enough to elicit a groan of pleasure from the force of its penetration into his wife. An easy thing to accomplish with her body so wet and eager for him."

al "Just like that. Just like that."

"Liurial watched on, wide eyed, as Alexia’s entire body shook under him. But, she didn’t have long to breathlessly gawk. Alexia lowered her head, and soon had the elf squirming and gasping at the sensation of her tongue lapping at Liurial’s soiled insides."
"From Rowan’s vantage point, he couldn’t see Alexia’s face. He could only imagine the drip of his cum down Alexia’s tongue back into Liurial’s pussy. But, he didn’t have to imagineLiurial’s reaction. The way she rolled her head back and let out a long groan was so sexy."
"The sight of it all pushed him forward even as the first hints of exhaustion started to settle in. How could he stop when Liurial’s face and his wife’s body looked like that?"

liur "My Lady…"

if alexiaJezeraSex > 0:
    "Her lips twisted and contorted in pleasure. Alexia, it seemed, was surprisingly skilled at handling a woman’s body."
    
else:
    pass
    
"And so it went. Thrusting and licking. Gasping and moaning. Like with the prior position, the movement of one affected all three." 
"Every time that Liurial would shiver it would reverberate back through Alexia to him. Every time he’d slam his hips into Alexia, it would drive her tongue deeper into Liurial’s sex."

liur "Oh!"

"Liurial let out a small shocked sound, almost a squeal. Then she convulsed. Already on edge from from her earlier fucking, she was the first to cum. But, Alexia followed soon afterwards. Rowan gasped out loud at the sensation of her insides clamping down on him."
"Rowan lasted another minute, but he too was ready to blow. Indeed, his stamina was partially just the result of having already came once. He groaned out and let loose a matching load inside of Alexia. Now she and Liurial matched."
"All three half fell into a heap on the floor, panting and recovering their breath. Alexia glanced at Rowan and smiled. She had a stream of white semen from Liurial’s soiled pussy running down her face."

scene bg9 with fade
show liurial naked happy at midright with dissolve
show rowan necklace naked at edgeleft with dissolve
show alexia necklace naked at midleft with dissolve

"A quiet set into the room. It matched the musk of sex that hung heavy in the air. Liurial turned to Alexia."

liur "Thank you for that. I was worried that you wouldn’t approve of…"

al "The fact that you’re sleeping with my husband?"

"Liurial nodded softly."

al "I don’t know if I’d say I approve or not. But, I can tolerate it considering the circumstances."

liur "You’ve already been so generous today though..."

ro "Indeed. Though I can’t imagine it’s all generosity. You swore yourself to be my woman. And since she’s my wife, what’s mine is hers."

"Liurial and Alexia exchanged a brief glance."

liur "Being Alexia’s woman? One can imagine worse fates then that."

al "In this castle? Clearly not. I’m the fiercest predator around."

"A sad little laugh went over the circle. One forged in the mutual experience of bloodmeen and the world they lived in."

return

###############################################################################################################
###############################################################################################################
###############################################################################################################

label the_demons_hobby:

scene bg8 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan was down in the dungeons questioning a prisoner who fell into the hands of one of their orc bands. An entire small caravan had been found alongside him. In truth, this man wasn’t connected to much of anything, so Rowan wasn’t sure what to even do with him."
"The man offered what little he knew about the military situation. He’d passed a checkpoint the army had set up in the North. But, just as Rowan was about to call it a day, who should walk in but Andras himself."

show andras displeased at midright with moveinright

an "One of the prisoners?"

ro "Indeed Master. I was just questioning him."

"The man went pale at the sight of a demon lord standing in all his glory in the middle of the room."
"Andras yawned, clearly bored. After all, this was just a band of small merchants of artisans, not some group of fighters. But, then something made his eyebrow rise."

show andras happy at midright with dissolve

an "Your hand moved just now. You have very precise motor skills."

pris "Ah. Yes."

an "You’re a craftsman, aren’t you?"

"The man nodded frantically."

pris "A clockmaker, my lord. One of the finest in the realm. Or at least, so I’ve been told."

"Andras took a step closer. His shadow engulfed the prisoner."

pris "Please, Sir. I have a family."

"Andras raised a hand."

an "Tell me about this craft. Clock making. What does it require? What is the process?"

show rowan necklace shock at midleft with dissolve

"Now it was Rowan’s turn to look surprised. Andras soon grabbed a seat and began to question the man in detail about the mechanics of the clockmaking trade." 
"The prisoner sat on edge. Sweat dripped down the side of his head. Yet, he did his best to answer every question Andras asked, sensitive not to get bogged down too hard in specifics."
"Yet, every time he tried to dumb down his answers, Andras seemed to grow more annoyed. He was genuinely interested in the man’s explanation of his work. This was not the first time Rowan had seen Andras get so worked up over a minor matter, but it was still a surprise."
"After what felt like an hour. Andras rose from his seat."

an "It is settled then. You will remain here and work on a design of my specification. I will have my request brought to you in writing. If you accomplish that then I will make sure you have fine lodgings."

pris "Of course. It will be a work worthy of your glory."

"Rowan interjected quietly."

show rowan necklace neutral at midleft with dissolve

ro "Is there anything you want me to do with the other prisoners?"

an "No strong fighters or attractive women? Nah, do whatever you want with them. I don’t care."

"The prisoner gulped, but clearly didn’t feel up to challenging the man who’d just given him a reprieve."

if serveChoice == 2:
    show rowan necklace concerned at midleft with dissolve
    "It was an emotional state Rowan knew well."
    show rowan necklace neutral at midleft with dissolve

show andras displeased at midright with dissolve

"Right as Andras reached the doorway, he turned back towards the man. His expression, which had been so uncharacteristically reasonable until now, suddenly filled with demonic menace."

an "I needn’t have to tell you what will happen if I am disappointed in your work."

"Before he could even get a reply Andras turned and walked out, leaving Rowan alone with the clockmaker. It was impossible to tell from his expression whether he felt more secure before or after his visit with a demon. Rowan resumed the interrogation."

$ change_prisoners(6)
return


