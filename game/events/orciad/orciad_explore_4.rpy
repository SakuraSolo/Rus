init python:

    event('the_orc_slaves_fate', triggers='orciad_explore', conditions=("week >= 4", "avatar.corruption < 70",), depends=('the_unlucky_slave',), run_count=1, group='orciad_camp', priority=pr_map_res)




label the_orc_slaves_fate:

scene bg26 with fade

"Once more, Rowan found himself near the mother’s section of the camp. This afternoon, the area was mostly empty. Only a few orc mothers remained, with children no older than a year or two. The rest must have been away, training or helping with the camp chores."
"Rowan glanced over the remaining people and found his eyes drawn to one person that stuck out. A sole, pale figure sitting by one of the tents."

if emmaNotMet == True:
    "Squinting his eyes, the hero realized it was the human girl from before, the pregnant slave. The one he wanted to talk before all that… Business... with the orc matron."
    "Well, now that the orc woman wasn’t around, there was nobody stopping him."
    "Without hurry – he didn’t want to spook the girl, as he recalled doing last time – Rowan approached the tent."
    "She was sitting by the side of it, working the needle with a small smile on her face. She was sewing what appeared to be one of the camp’s war banners. Since their last meeting, her stomach had grown larger. Round and heavy, it was out in the open, not covered by her rather skimpy apparel." 
    "… Among other things." 
    show rowan necklace neutral at midleft with dissolve
    ro "…"
    "Standing next to the girl, Rowan coughed ostentatiously. The girl raised her head – and Rowan averted his gaze. From the corner of his eyes, he could see her eyes widen with fear, and her face redden with embarrassment."
    "For whatever reason, she no longer wore a shirt. Or a bra. Her enlarged breasts were now out for everyone to witness."
    show rowan necklace happy at midleft with dissolve
    ro "I apologize if I surprised you. Do you mind if I talk with you for a moment?"
    "She brought the unfinished banner to her chest, trying to cover herself. She eyed him suspiciously."
    emm "You’re… That man from before... "
    ro "Rowan. Again, I apologize for disturbing you."
    "The girl hesitated, her expression wary as she judged the man before her. Rowan offered her his best welcoming smile. It seemed to have worked, since he saw her relax ever so slightly."
    emm "It’s okay…"
    emm "I’m Emma."
    emm "And I…"
    "She forced a polite smile."
    jump emmaNotMetIntro
    
elif emmaIgnored == True:
    show rowan necklace neutral at midleft with dissolve
    "Squinting his eyes, the hero realized it was the human girl from before – the pregnant slave. That scared girl he talked about with the matron."
    "...The one that cowered before him, and tried to run away with tears in her eyes."
    show rowan necklace concerned at midleft with dissolve
    "Did he… Did he really just left without a word last time? Didn’t bother to check on her at all?"
    ro "(Goddess… What is wrong with me.)"
    show rowan necklace angry at midleft with dissolve
    "Rowan clenched his teeth and forced down the raising feeling of self-loathing. There was no point in bemoaning his earlier mistakes."
    show rowan necklace neutral at midleft with dissolve
    "His time was better spent making things right."  
    "His resolve restored, without hurry – he didn’t want to spook the girl, as he recalled doing last time – Rowan approached the tent."
    "The girl – Emma, that was her name - was sitting by the side of it, working the needle with a small smile on her face. She was sewing what appeared to be one of the camp’s war banners. Since their last meeting, her stomach grew larger. Round and heavy, it was out in the open, not covered by her rather skimpy apparel." 
    "… Among other things."
    "…"
    "Standing next to the girl, Rowan coughed ostentatiously. The girl raised her head – and Rowan averted his gaze. From the corner of his eyes, he could see her eyes widen with fear, and her face redden with embarrassment."
    "For whatever reason, she no longer wore a shirt. Or a bra. Her enlarged breasts were now out for everyone to witness."
    show rowan necklace happy at midleft with dissolve
    ro "I apologize for surprising you like that. Do you mind if I talk with you for a moment, Emma?"
    "Rowan started carefully. He really didn’t want her to panic again…"
    "And he had some success, since the girl recoiled only slightly, bringing the unfinished banner up to her chest to cover herself."
    emm "You’re… That man from before..."
    ro "Rowan. I apologize for… Leaving like that last time."
    "The girl hesitated, her expression wary as she judged the man before her. Rowan offered her his best welcoming smile."
    "It seemed to have worked, since she relaxed ever so slightly."
    emm "It’s okay…"
    jump emmaNotMetIntro
    
else:
    "Emma, the slave girl he met some weeks ago, was still present in the area. Last time they talked, the poor girl ended up sobbing in his arms. He hadn’t had the occasion to check on her since."
    "It was time to rectify that."
    "He approached the girl without hurry. Again, she was working the needle –  a small smile on her face, as she sewed what appeared to be one of the camp’s war banners." 
    "Since their last meeting, her stomach grew larger. Round and heavy, it was out in the open, not covered by her rather skimpy apparel." 
    "… Among other things." 
    show rowan necklace neutral at midleft with dissolve
    ro "…"
    "Rowan stopped beside her and coughed ostentatiously. Emma raised her head – and Rowan averted his gaze. From the corner of his eyes, he could see her blush."
    emm "Oh."
    emm " Hello…"
    "For whatever reason, Emma was sitting with her upper torso uncovered, her enlarged breasts on open display. As if unaware of that fact, she kept staring at the hero, a conflicted expression on her face."
    ro "Do you mind...?"
    emm "Huh? Oh."
    "Embarrassed, she quickly covered herself with the banner in her hands."
    emm "Sorry, just…"
    emm "I’m not supposed to… Wear anything..."
    "Her voice trailed off, and she averted her gaze, not having the courage to look him in the eyes."
    show rowan necklace happy at midleft with dissolve
    ro "It’s okay. I understand."
    "She flashed him a quick smile, but again, averted her eyes."
    emm "I…"
    emm "Uh… I don’t think I ever got your name?"
    emm "“Warbringer” doesn’t sound right."
    ro "It’s Rowan."
    "She repeated the name to herself as if savoring it. “Rowan, like the hero of Karst”..."
    "Finally, she found some courage within herself to look him in the eyes." 
    emm "Rowan, I…"
    emm "Thank you. For what you did earlier."
    "She smiled earnestly – an honest, true smile. While he could see she was still wary of him, that moment of kindness from back then really had an impact on her."
    $ change_base_stat('g', -2)
    ro "Sorry I couldn’t do more."
    emm "It’s okay."
    emm "Sorry I tried to run away."
    ro "It’s fine. You were right to be careful."
    emm "… Maybe..."
    "Her smile faltered, and again, she looked away. Silence fell between them."
    "Rowan could see Emma was fighting with herself over something. She didn’t tell him to leave, even though part of her still wasn’t all that keen on his company." 
    "He tried to think of something that would put her at ease, show her he had no ill intentions, as he already proved earlier. But before he could come up with a concrete idea, Emma came to a decision."
    "She stood up and grabbed him by the sleeve.  Gently, she pulled him with her, into her tent."
    emm "Just… For a moment… If we could…?"
    "She whispered, voice weak – almost pleading. Rowan nodded solemnly and followed her lead."
    jump emmaMain

    
label emmaNotMetIntro:

emm "I guess I should apologize as well."
emm "For how I… Reacted."
emm "Last time."

show rowan necklace neutral at midleft with dissolve

"She struggled to get the words out. She made a heroic effort to look him in the eyes, but it was obvious she’d rather be somewhere else."
"Preferably somewhere where she wouldn't be forced into slavery, but at the very least somewhere without Rowan."
"Somewhere where she wouldn't have to explain herself."

emm "I didn't..."
emm "I didn’t want anyone... To see me like… This..." 

"She placed her hand on her stomach. On her bastard half-orc child."

emm "So… Sorry."

show rowan necklace happy at midleft with dissolve

ro "It’s alright."
ro "I’d be wary of other people as well.  "

"Emma tensed at his words, her expression frozen in the polite, small smile she tried to maintain. Her eyes shot to the sides as if she was looking for someone who could come save her from this conversation."

show rowan necklace concerned at midleft with dissolve

"Rowan forced down a sight. He wanted to help the woman, somehow. He wasn't certain how, but he'd improvise something."
"At least he would if she didn't send him away."
"And for a moment it seemed like she would do just that. Tell him to go away, to stop harassing her."
"... That moment stretched out, the air heavy with uncomfortable silence."
"But as Rowan was searching his mind for any topic he could use to break the ice, the girl stood up suddenly."

emm "Do you mind… Coming inside for a moment?"

"Her tense expression slipped for a second, her voice taking on an almost pleading tone. Without thinking twice about it, Rowan nodded his head."
"She headed for her tent, and Rowan followed behind her."

jump emmaMain

label emmaMain:
    
scene bg30 with fade

"Emma’s tent was, as one would expect, largely empty. It was equipped with only the barest of necessities, and Rowan expected it to feel cold."
"Instead, it was almost… Cozy. There was not much, but what was, was enriched with various trinkets – fresh flowers, decorative cloths. Rowan saw a skull of a deer, and two dolls made out of sticks."

if woodCarverSaw == True:
    "There even was a crude, but realistic wooden figurine of a bird in flight, oddly familiar to the hero."
    
else:
    pass
    
"This tent might have been a prison, but Emma tried to do whatever she could to make it feel like home."
"Speaking of the girl, she set aside the cloth she was working on and knelt on her bedding, now covering herself with a fur blanket. She must have had nothing else to use – no shirt or anything of the kind."
"She looked up to the hero and smiled weakly." 

emm "It’s… Good to finally see a friendly face."
emm "A human face."
emm "…. Would it be too much to hope you’re here to rescue me?"

show rowan necklace concerned at midleft with dissolve

"His silence was the answer."

if delane_status == "free":
    "After he rescued Delane, Batri made sure he would lose no other slave. The guards now had strict patrol routes and inspected everyone leaving the camp."
    "Another rescue was impossible."
    
elif delane_status == "batri":
    "With the camp now under the twins boot, he could, in theory, attempt to negotiate Emma’s release.  But the whole conflict started precisely over slave ownership, and he didn’t see the orcs looking favorably at giving slaves away."
    "Perhaps he might be able to strike a deal with the warchief in the future, but for now, he didn't see a way to make it happen."
    
elif delane_status == "ulcro":
    "With the camp now under the twins boot, he could, in theory, attempt to negotiate Emma’s release.  But the whole conflict started precisely over slave ownership, and he didn’t see the orcs looking favorably at giving slaves away."
    "Perhaps he might be able to strike a deal with the warchief in the future, but for now, he didn't see a way to make it happen."

elif delane_status == "tarish":
    "With the camp now under the twins boot, he could, in theory, attempt to negotiate Emma’s release.  But the whole conflict started precisely over slave ownership, and he didn’t see the orcs looking favorably at giving slaves away."
    "Perhaps he might be able to strike a deal with the warchief in the future, but for now, he didn't see a way to make it happen."    

else:
    "With the camp still at war with itself, he could, perhaps, arrange for an escape."
    "But not now. Not when she was pregnant. She already looked weak, there was no way she had the strength to pull off a daring escape, no matter how much she desired to."

"She must have understood that much. For a moment, she just stared at him pleadingly. With a heavy heart, Rowan shook his head ever so slightly."
"She forced a smile upon her lips and moved on to other topics." 
"He expected her to be starved for human contact but that proved not to be the case. Oh, she did her best to pretend she was – she asked him about news from Rastedel, and the village she always visited for the spring carnival. She wanted to know who would be playing the six heroes this year." 

if castle.villages > 3:
    "It was one of those Rowan ordered enslaved. Heart heavy, he told her he didn’t know."
    $ change_base_stat('g', +2)    
else:
    "Rowan didn’t know, but he promised to ask if he’s ever in the vicinity."

"All pointless small talk, but Rowan indulged her. If this moment of normalcy was all he could for the girl, then at the very least he’d give her that."
"But then Emma could not maintain the pretense for long. After half an hour, her questions started coming more slowly, with bigger breaks in between."
"Finally, she fell silent altogether, and cast her eyes down." 

ro "… Emma?"

"She turned her head away, refusing to respond."
"One painfully silent minute later, Emma took a deep breath and gathered the courage to look him in the eyes once more."

emm "Rowan, I…"
emm "I have to ask."

"Her voice was heavy. Solemn."

emm "Why are you here?"
emm "As in... In this camp."
emm "You don’t… You don’t look like a bad man."
emm "Don’t seem like one."
emm "So how come you are here, among the orcs?"
emm "How did you end up working with them?"

"A fair question, and Rowan expected it to pop up at some moment."

if serveChoice == 3:
    ro "I had to make some difficult choices."
    ro "For someone very important to me. "
    emm "Was it worth it?"
    if all_actors['alexia'].relation > 30:
        ro "Despite everything that has happened..."
        show rowan necklace happy at midleft with dissolve
        ro "Yes. Always."
        "Slave or not, she was still pretty young – and every young girl dreamed of a handsome hero who sacrificed everything for the woman of his life. It was a tale all bards loved to tell."
        "Curiously, the one's Rowan heard never included a red demon trying to fuck the wife of the main character."
        "He wondered why."
        $ change_base_stat('g', -2)
        
    else:
        "His mind wandered to his wife. When was the last the time the two of them had time for one another? Held each other?"
        "Even talked honestly with one another?"
        ro "…"
        emm "Sorry, I… I shouldn’t have asked."
        ro "No, it’s… It’s not your fault."
        ro "(It’s mine.)"
        $ change_base_stat('g', +2)
        
elif serveChoice == 1:
    ro "I had to make some difficult choices. Had no other options at a time."
    "Emma nodded solemnly, understanding all too well what he was going through back then."
    
elif serveChoice == 2:
    ro "I had to make some difficult choices."
    ro "To survive."
    "A dry laugh escaped her lips."
    emm "Don’t we all... "
    
else:
    "Rowan opened his mouth – and froze."
    "So what exactly was he supposed to say to Emma? That the world was plagued by injustice and corruption, and that he had plans to make it better?"
    "By siding with orcs and demons, who thought nothing of enslaving, raping and pillaging the countryside? Who saw her as nothing but a toy or tool for their needs?"
    ro "…"
    ro "I had to make some difficult choices."
    "He swallowed heavily. Emma’s curious eyes were still on him, and he’d rather they weren’t."
    ro "For people who were dear to me. "
    "Emma nodded solemnly. She didn’t press the matter, seeing it was a difficult topic for him."
    "For that, he was thankful."
    $ change_base_stat('g', +2)
    
"Emma sat in silence for a moment, her lips moving wordlessly as she mulled over his words."

emm "“Difficult choices”, huh…"
emm "I thoughts so."
emm "I mean… I knew so!"

"She inhaled sharply, and a nervously smile crossed her face."

emm "You’re not a bad man for working with the orcs."

"She giggled to herself softly. Not a good sign."

emm "Of course you aren't!"

show rowan necklace concerned at midleft with dissolve

emm "Just as I’m not a bad woman for fucking them!"

ro "Emma?"

"He tried to politely interrupt her, but it was no use."

"The girl was no longer listening to him. She rocked herself gently, her fingers clutching the blanket at her chest with desperation, knuckles white from the strength of her grip."
"She barely even registered his presence anymore, lost in her own little world."

emm "What choice did I have?"
emm "It was either spreading my legs willingly or getting beaten up!!!"

"She shouted out, hate, anger, and pain mixed in her voice."

emm "So why should I feel bad for using my body to survive?!"
emm "Why should anyone have the right to call me a slut?!"
emm "Why do I always have to be the village slut?"
emm "Why is it wrong of me to enjoy myself a little?!"
emm "And at least the orcs know how to fuck!"

"Her face twisted in rage. She spat to the side in disgust."

emm "None of that… Three pumps and they’re done!"
emm "When the orcs fuck you, they fuck you! Really give their all! "
emm "They’re considerate like that, you know?!"
emm "Never leave you unsatisfied!"
emm "Yeah they’re a bit rough at times-"

"Her voice wavered."

emm "-all the time-"
emm "-But keep yourself wet and they always make sure you come!"

ro "Emma..."

emm "And they don’t judge you!"
emm "None of that-"

show rowan necklace shock at midleft with dissolve

emm "“I can’t believe you put in your mouth Emma!”"
emm "“Eww, in the ass, you’re so disgusting Emma!”"
emm "Well fuck you Derek, I’m glad the orcs killed you!"
emm "I bet your corpse is really disgusting now! Haha, hahaha!"
emm "Ahahahahahaa!"

show rowan necklace concerned at midleft with dissolve

ro "Emma."

"Her mad laugh broke midway, and her eyes, wet from the tears she was holding in, refocused on him again."

emm "None of this is how I wanted it to be Rowan."
emm "I never wanted to be an orc slut."
emm "But if I have to be a slut, I might as well be one to someone who appreciates it!"
emm "And they really like how I always keep myself ready for them."
emm "And how I- How I got-"

"She placed her hands on her stomach and looked away."

emm "They really like how my stomach and t-tits are all swollen."
emm "One even said he wants me to a-always look like this."
emm "That he’ll, he’ll…"
emm "Make me his s-slave-wife and will keep f-fucking me until I get pregnant with his kid this time."
emm "He’d make sure I have a warm meal every day."
emm "I wouldn’t have to worry about getting beaten up or raped…"
emm "And being pregnant is actually pretty nice…"
emm "Is it-"

"Her voice broke, and tears ran down her face."

emm "Is it wrong of me? To think it sounds pretty nice?"
emm "It doesn’t make it a bad person, right?"
emm "Right?"

ro "… "

menu:
    "Tell her it’s okay to be an orc slut.":
        $ released_fix_rollback()
        jump emmaOrcSlut
        
    "She mustn't let the abuse break her.":
        $ released_fix_rollback()
        jump emmaSurvivor
        
label emmaOrcSlut:

$ change_base_stat('g', -2)
$ change_base_stat('c', +2)
#Gain small Kharos Favour

$ emmaPure = False

ro "Emma…"
ro "You’re in a difficult position."
ro "I don’t think anybody has the right to judge you for doing what is necessary to survive."

"She held her breath, waiting for the “but” that would inevitably follow."
"..."
"It never did."

show rowan necklace happy at midleft with dissolve

"Emma exhaled slowly."

emm "R-right…"
emm "They don't."

"She offered him a small smile. A small, genuine smile."

emm "I…"
emm "Um, I apologize for…"

ro "Don’t worry about it."

show rowan necklace neutral at midleft with dissolve

ro "I’m sorry. I wish there was something more I could-"

emm "It’s alright."
emm "I…"

show rowan necklace happy at midleft with dissolve

emm "I think I’ll be fine."

"She smiled cheerfully, all the way – showing her teeth. Her smile had a few holes in it, either due to poor hygiene, or because the orcs knocked a few of her teeth out."
"She quickly hid it behind her hand, realizing what she just did. Her cheeks flushed with embarrassment, but she didn’t seem all too bothered by it."
"She could drop her guard around Rowan."
"It would take her some time to get used to this strange reality, where she didn’t have to blame herself for what she had become."
"It was best to just let her adjust. Rowan stood up and-"

emm "Wait."

"He turned his eyes to her."
"Slowly, Emma, lowered her blanked, staring straight at him as she exposed her pregnant, swollen body."
"A young woman in full bloom, she had a heavy bosom that begged to be groped, and narrow, sexy hips."
"Months of slavery made her skinny, and not in a healthy way, but any deficit in her figure was more than made up by the shy, eager look she was giving him."

if all_actors['alexia'].relation > 30:
    "She couldn’t hold a candle to Alexia – her hair did not shine as brightly, and her smile was not as pretty. But she was kneeling right before him, ready and willing to be taken."
    
else:
    "She kneeling before him, ready and willing to be taken."

emm "Do you want to, um… "
emm "Stay for a bit longer?  "
emm "It’s been a… Stressful day."
emm "I wouldn’t mind some company."

menu:
    "Stay.":
        $ released_fix_rollback()
        jump emmaSlutSex
        
    "Politely decline.":
        $ released_fix_rollback()
        if all_actors['alexia'].relation > 30:
            ro "I appreciate the offer. But I’m afraid I am a married man."
            emm "Oh?  She must be a very lucky woman then."
            "Rowan chuckled softly."
            ro "I think I’m the lucky one."
        else:
            ro "I appreciate the offer, but I’m afraid I’ll have to decline."
            emm "Ah."
            emm "Then let me just say thank you. Really."
        "Rowan smiled, and bidding Emma farewell, left the tent."
        "Not exactly the heroic job he imagined himself doing when he first joined Denara, but…"
        "Kindness came in many forms."
        return


label emmaSlutSex:

"Rowan peeked out of the tent. The orc mothers had yet to return."
"They would not be interrupted."

ro "… I guess it is a bit late."

"He closed the exit, and started to undo his belt, as Emma’s smile took on a triumphant tone."
"…"

scene black with fade

emm "You just make yourself comfortable, Rowan."
emm "I’ll handle everything."

#SlutEmma CG
scene cg234 with fade
show rowan necklace naked aroused behind cg234
pause 3

"Rowan laid naked on the tent’s bedding, as his pregnant partner climbed over him. She insisted on this position, said she didn’t want to hurt the baby."
"Rowan suspected there was another reason as well. As his gaze traveled across her swollen form, from the corner of his eyes, saw her grin lewdly at him. But the moment he looked at her again, she would once more wear that bashful smile of hers."
"She was still clinging to her nearly abandoned modesty, even if all she could afford was, at best, a token effort at keeping the masquerade."

ro "Motherhood becomes you."

"She flashed him another perverted smile, unable to stop herself. To be adored liked, desired like that – she couldn’t help but bask in this feeling."
"The tragic backstory behind her current state no longer mattered. At least not at the moment."
"Placing herself comfortably on his stomach, Emma rubbed her backside on his phallus, clearly enjoying herself a bit too much to hurry things along."
"Rowan knew all of this foreplay wasn’t needed – he felt the wetness of her nether regions on his skin, felt her eagerness on his body – but indulged her nevertheless."

ro "Taking your sweet time, aren’t you?"

emm "Can you blame me? You’re quite the treat."

ro "For a human?"

"She grinned again and reached behind her. Her finger traced along his manhood, from the base to the very top."

emm "I can see some similarities between you and the orcs."

"A weird compliment, but coming from her, it sounded like the highest of praises."
"She raised herself up with a smooth motion, and moved her hips to have the tip of his cock brush against her entrance. For a moment, she simply moved back and forth, teasing him mercilessly."
"It was only her pregnant state the prevented Rowan from turning the tables on her – grabbing her by force and pinning her under him."

ro "Nn-!"
ro "Goddess damn you Emma… Do you torment all your partners like this?"

"She giggled to herself, a devious smile dancing on her lips."

emm "Only the ones who let me."

ro "I’m starting to think I’m being too nice with you."
ro "You’re really trying my patience here.  "

emm "Mmmm..."
emm "Then I guess that’s as far as I can take it. "

"She wanted to tease him more. This feeling – this intoxicating awareness he wanted her so bad, he was barely controlling himself – was better than any alcohol she ever tried."
"She wanted to revel in it."
"But she wanted him inside her more."
"Unable and unwilling to contain her own desire, she finally positioned herself properly. Rowan gasped, as he felt the tip of his cock slowly part her lower lips."

emm "I’m sorry if I’m a bit… Loose."

"She sat down suddenly, taking him all the way in."

emm "A-ah!"

"She needn’t fear. Soaking wet, her warm insides sucked him greedily."

ro "Hnn- Damn, you’re wet."

emm "Aa-ah, thank you!"

scene cg235 with fade
show rowan necklace naked aroused behind cg235
pause 3

"Needing no encouragement from her partner, Emma started to bounce on Rowan’s cock with unbound joy, her body shaking obscenely as she did."

emm "A-Ah! Ah!"

"Her eyes never left his own. She had to cover her mouth with her hand, to conceal the lewd expression she kept breaking into."

emm "A-aaah! R-Rowan, you feel so~ Good~!"

"But it did nothing to hide her lustful moans and wanton praises. No wonder the orcs wanted her so much. She was a born slut, she just didn't know it before."

"She must have had a great deal of practice in this position – at no point did she see the need to stop and rest. Rowan watched her breasts, as they continued to sway erotically, small, white droplets forming on the end of her nipples."

menu:
    "Taste her.":
        $ released_fix_rollback()
        scene cg236 with fade
        show rowan necklace naked aroused behind cg236
        pause 3
        "He laid a hand on her thigh and held her tight. She stopped herself – her eyes following where his own were focused on."
        emm "A-aah~, if you want to…. Just let me…"
        "She opened her legs and reposition herself, allowing Rowan to sit up."
        "He reached for her tits, and squeezed them forcefully-"
        emm "A-ah!"
        "- Evoking another lustful moan from Emma. Music to his ears."
        "Not being in any hurry – a subtle revenge, from her earlier teasing - Rowan ran his tongue across her nipple, tasting the milk that started to flow freely. It was quite sweet."
        ro "Do they ever…?"
        emm "No… They don’t like it…"
        emm "But they do sometimes milk me like a cow~"
        ro "Why am I not surprised."
        scene cg237 with fade
        show rowan necklace naked aroused behind cg237
        pause 3
        "He shook his head in mocking disbelief, then finally took one of her nipples in his mouth."
        emm "A-a-ah! Please, ha-arder!"
        emm "Suck ha-a-arder!"
        "She wiggled in his arms, moaning in his ear as her milk flowed forth."
        emm "Mm-aah! Rowan, it feels so- so-!"
        emm "Goood~!"
        "And to think a while ago, she would find this behavior perverse..."
        "Rowan switched his attention to the other nipple, still pinching the first one. He allowed himself to be a bit harsher than usual, as her honeyed moans kept pushing him on."
        emm "A-aah! Y-yes! Aaah!"
        "Suddenly, her body shuddered in ecstasy. Just from having her nipples played with..."
        ro "You really are a slut, aren’t you?"
        emm "Ehehe~"
        "Not even a hint of remorse in her voice. Good heavens."
        "Rowan pinched her tit one last time, and laid back. Her puffy nipples stood proudly, a testament to his ministrations."
        ro "Weren’t you supposed to “handle everything”?"
        ro "Get back to work."
        "He needn’t tell her twice. Despite feeling sensitive, she quickly picked up the pace, once more impaling herself on his dick with wild enthusiasm."
        "After all, if there was anything the orcs required from their slaves, it was endurance."
        "It would be a long night for both of them."

    "Let her keep riding you.":
        $ released_fix_rollback()
        "Soon her movement grew more desperate, more frantic. She hadn't bothered with keeping her voice down for some time – but now, her cries grew even louder."
        emm "Rowan- ah! Rowan!"
        "She threw her head back, moaning his name, again and again. Music to his ears."
        emm "Good, so good~!"
        "She couldn’t contain herself anymore. She violently impaled herself on his dick, taking it as deep inside of her as she could. Her body quivered in pleasure, and Rowan swore he saw her eyes roll up from the ecstasy."
        ro "Good heavens…"
        ro "Such a slutty way to climax."
        emm "Ehehe…"
        emm "It’s because you’re so good, Rowan."
        ro "Filthy little liar."
        "He grabbed her by the thighs and moved her body up. Without any warning, he pushed her onto his cock again."
        emm "O-O- O-Oooooooooh!"
        ro "I bet you show that face to every orc."
        "She giggled in delight. “Guilty as charged”."
        "She might have come, but he hadn’t. And he wouldn’t be leaving this tent until he did."
        "Luckily for him, if there was one thing the orcs valued, it was endurance. Emma quickly picked up the pace, true to her earlier promise of “handling everything”."
        "It would be a long night for both of them."

scene black with fade

scene bg26 with fade
show rowan necklace neutral at midleft with dissolve

emm "Thank you, Rowan. For everything."

show rowan necklace happy at midleft with dissolve

ro "The pleasure-"

emm "-was all mine."

"Emma giggled cheerfully. She no longer bothered to cover her chest, proudly showing off her tits and belly. She even kept pushing her breasts out, whenever she saw Rowan looking in her direction."
"She really was happy like that. At first, he wasn’t certain if his advice was the right one, but after the night they spent together…"
"Honestly, he got a bit carried away there. It was a bit embarrassing."

emm "You should go now."
emm "I wouldn’t want my master-to-be to see me so me acting so chummy with a human."

ro "(“Another” human, you mean.)"
ro "Obviously. Take care, Emma."

"The shared a quick goodbye, and Rowan left her tent, spirits high."
"Perhaps everything will turn out fine for the girl."
"One way or the other."

$ emmaRowanSex = True
return

label emmaSurvivor:

$ change_base_stat('g', +2)
$ change_base_stat('c', -2)
#Gain small Solansia Favour

ro "Emma…"
ro "You’re in a difficult position."
ro "I don’t think anybody has the right to judge you for doing what is necessary to survive."
ro "But…"
ro "You know that even if you do everything the orcs want you to, and even if you pretend to enjoy doing so, they’ll never care for you."

"He saw the despair enter her eyes. Rowan’s words were like a knife to her heart, and Rowan did not hesitate to twist the blade. He had to."

ro "You’ll never be more than a toy to them." 

emm "So what?"

"She whispered, voice faint."

emm "At least a toy gets taken care of."
emm "A slave is used and discarded."

ro " … So is the toy, once the owner gets bored of it."

"It might have been cruel, to rid her of these illusions. But too often, during the war, he saw people try and bargain with demons, hoping it would allow them to retain some semblance of normalcy. That through servitude, they would be able to protect at least some parts of their now broken life."
"It never worked, and their fate was usually worse than death."

if serveChoice == 2:
    "Yet somehow he ended up doing the exact same thing, joining the twins just to save his own life."
    "For how long, he wondered, will he able to stay true to himself, defiant to all attempts at corrupting him? How much longer, until he ends like Emma?" 
    "Rowan pushed these thoughts aside. It was neither the time nor the place for them."

else:
    "A cautionary tale, given his current circumstances."
    
"Emma’s lips moved silently, failing to get her words out. She licked them and tried again."

emm "I-"
emm "I don’t-"
emm "I don’t think I have it in me to resist any longer."

if emmaMet == True:
    "Her voice broke down again. Knowing all too well how she felt, he wrapped his arms around her, just like last time."
    
else:
    "Her voice broke down again. Knowing all too well how she felt he wrapped his arms around her."
    
emm "Why- Why-"

"She broke into tears, sobbing into his arm. He did his best to whisper something encouraging into her ears, even if it was just empty words."  
"He was there for her. At least for now."
"No matter how little it meant."
"..."

emm "C-could you… S-stay the night maybe?"
emm "Just... O-one night."
emm "Please..."

ro "..."
ro "Yeah."

emm "Thank you..."

"It was a small sacrifice. The world could wait."

scene black with fade

"…"
"Night came, but it brought him no rest. Rowan stared into the darkness, a thousand thoughts denying him peace of mind."
"“You can’t protect everyone.” He knew that. Every general knew that."

if orciad_state <=1 and met_with_delane == True:
    "He might yet save Delane. It would be difficult, but possible."
    "As long as he was willing to risk Andras wrath."
    
elif delane_status == "batri":
    "That’s why he had to sell Delane to the orcs. For the greater good. As dirty as it sounded."
    
elif delane_status == "ulcro":
    "That’s why he had to sell Delane to the orcs. For the greater good. As dirty as it sounded."

elif delane_status == "tarish":
    "That’s why he had to sell Delane to the orcs. For the greater good. As dirty as it sounded."

elif delane_status == "free":
    "But at least, he was able to protect Delane. A small triumph."

elif delane_status == "dead":
    "And every general knew how failure to do so felt."
    ro "(Delane, forgive me...)"

else:
    pass
    
"So what was he going to do with this girl?"
"Emma laid beside him, dressed in his shirt – for modesty. She was pressed against his body, her hand over his chest, caressing him timidly. She couldn’t sleep either, no doubt plagued by the visions of things to come."
"She already suffered so much, and it would only get worse. So much worse."
"He turned his head to her. It was too dark to see her expression, but he saw her look up, staring into his eyes. Her fingers slowed their dance."
"She leaned in, a little. Then again, her face inching to his own, as her hand started to venture down."

menu:
    "Let her kiss you.":
        $ released_fix_rollback()
        jump emmaPureSex
    
    "Stop her.":
      $ released_fix_rollback()
      "His hand grasped her own, and Rowan shook his head. Emma sighed, and laid her head on his arm."
      jump emmaPureConclusion


label emmaPureSex:

#puresex CG
scene cg238 with fade
show rowan necklace naked aroused behind cg238
pause 3

"Tenderly, she pressed her lips against his. It was gentle, shy kiss, chaste almost. There was no passion in it, at least not the sexual one. Desire, yes. Desire for intimacy, closeness."
"For being more than an object."
"Her fingers wrapped his manhood, her small hand moving up and down his entire length, without haste, without hurry."
"She didn’t moan his name, or comment, with poorly acted out astonishment, what a big stud he is. Her breathing got a bit more hectic, and that was all. Rowan allowed her to continue without interruption, gently caressing her hair."
"He was content to let her have this. She didn’t have many opportunities to be the one in control." 
"And it wouldn’t change anytime soon." 
"Realizing he was now ready, she ran her fingers one more time along his length, and got up from her bedding. She climbed over him, her swollen stomach now resting on his own."
"He saw her remove his shirt, and for a brief moment, she continued to cover her breasts with her arm, despite the darkness."
"She exhaled slowly. With some hesitation, she moved her hand away, letting Rowan see her in her entirety."
"She might have hated that body. She might have hated what the orcs made her into. But she didn’t want it to ruin the one night she would get with Rowan."

ro "Emma…"

emm "Shh..."

"She silenced him gently, and leaned in, placing her hands on his naked chest. She ran them across his skin, having her fingers dance slowly again, as she felt the muscles underneath."
"Emma smiled to herself. So different, compared to her usual partners. Lean, strong – but not in a brutish way. There was gentleness in Rowan."

if serveChoice == 3:
    "Whoever this “very important person” of his was, they were lucky to have him."

else:
    "If he had anyone in his life, they must have been lucky to have him."

"Again, she reached for his manhood, now pressed comfortably against the valley of her backside. For someone to wait for her to get ready..."
"It was nice."
"Rowan felt the girl rise up – his manhood was suddenly denied the warmth of her body as she repositioned herself. But only for a moment."
"She lowered herself on him, her lower lips parting before him."  
"Despite all the recent abuse, her body was still that of a young woman. Rowan grunted as he felt her insides tightened around him, while Emma kept pushing him deeper in – deeper and deeper, until she could once again rest on his hips."

emm "A-ah..."

"Only her soft moaning could now be heard in the tent. Mostly. Occasionally, in the distance, a violent shout would break the silence."
"Some orc, or maybe a slave who didn’t get as lucky with their partner for the night."
"But neither of them paid any attention to the outer world. These were problems of tomorrow. They would deal with them once the sun rises."
"But not now. Not this night."

emm "Mmmh~"

"Slowly, she accustomed herself to his girth. He wasn’t the largest she had to take in…"
"And she appreciated that."

scene cg239 with fade
show rowan necklace naked aroused behind cg239
pause 3

"She raised her body gently, evoking a pleasant gasp from Rowan. She smiled to herself, and gradually lowered herself again."
"For Rowan, it was hardly a show. In the darkness, he could only see her rock her body with gentle, deliberate movement, her face hidden away."
"But every small movement of hers was done for his pleasure. Her body was his."
"In ways the orcs would never have it. "
"He didn’t hurry her on. He allowed her to slowly rack up the tempo, to start rocking her hips more aggressively, more greedily. The sounds their bodies made grew more obscene by the minute."

ro "Ah!"

emm "Mmmnn~"

scene cg239 with sshake
scene cg239 with sshake
scene cg240 with flash
pause 2
show cg241 with dissolve
show rowan necklace naked aroused behind cg240
pause 3

"Rowan was the first to reach his limit. Emma moaned softly, stopping herself as she felt him paint her insides white. A feeling she was well familiar with by now. But with Rowan..."
"It felt different."
"For a while, she just sat there, enjoying the warmth in her body."

emm "... You come a lot."

ro "… Thank you?"

"He wasn’t certain how else to answer that, but judging by the soft giggle his response provoked, Emma clearly didn’t mind it."
"After a minute or so, she pushed herself upwards, releasing his manhood."

ro "What about-"

emm "Shhhh."

"She knelt by his side, and diligently cleaned him up with her mouth. She didn't need him to prove what a stud he was to her, by finishing her off."
"She just needed him by her side."
"Once she was done, she mouthed a quiet 'thank you', and laid down by his side again." 
"Rowan said nothing, and just let her drift off."
"Soon enough, exhaustion took him as well." 
"…"

$ emmaRowanSex = True

label emmaPureConclusion:

scene bg30 with fade
show rowan necklace concerned at midleft with dissolve

emm "So I guess this is goodbye."

ro "I’m afraid so."

"Emma shuffled her feet, unsure how to continue."

ro " … If there is a way-"

emm "I know."

"She offered him a sad smile. For some reason, this time it felt like she was the one twisting a knife in his heart."

emm "It’s okay. I’ll manage."

"She lied. He knew that. She knew that."
"But she didn’t want to saddle him promises he might not be able to keep."
"Or perhaps her spirit would not take it if he did promise help, only for it to never arrive."
"She gave him a quick hug – just for a moment, to feel his warmth again."

emm "Go."

"Then she pushed him away. Rowan nodded solemnly and left her tent to resume his quest."
"He prayed he made the right call there."

return
