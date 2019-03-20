init python:

    #rastedel not complete TODO
    event('claMin_brings_in_boy', triggers="week_end", conditions=('week >=10', 'castle.villages > 1',), group='ruler_event', run_count=1, priority=pr_ruler)


label claMin_brings_in_boy:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show clamin happy at midright with dissolve

cla "Rowan, dear. I have with me someone who was quite insistent on meeting you."

"The thrifty goblin had an unfamiliar young man with her. A tall, lanky man, barely past the age of adulthood, if Rowan had to guess. With short, curly hair, a face marred with zits, and a strained, nervous expression."
"His dirty clothes betrayed peasant origins, though the glint in his eyes, the way he studied his surrounding, and the respectful pose he took immediately upon standing before the throne, all hinted at some degree of wit."

ro "Is that so? And why is that?"

cla "He has great aspirations! And I think he might be of use to you."

ro "I take it you didn’t just trip over him?"

cla "No, but he is the one who found me rather than the other way around! Approached me during my visit to one of the Rosaria villages you struck a deal with."

show rowan necklace shock at midleft with dissolve

cla "He threatened to have me hanged if I don’t do exactly as he says, the little charmer!"

young "T-that’s… A bit of an exaggeration, Miss Cla-Min."

cla "Is it? Is it really?"

show rowan necklace neutral at midleft with dissolve

"The peasant boy grew increasingly nervous, while the goblin mistress chuckled to herself, clearly having the time of her life. Rowan tapped the throne impatiently, urging them to move on with this."

cla "Come on, tell him the full story!"

"She urged the boy on, not bothering to acknowledge Rowan’s not so subtle signals. The aspiring youth, on the hand, was much more attentive. He had the courtesy to at least lower his head apologetically, before following Cla-Min’s orders."

young "I do not believe you recall me, my Lord, but as Miss Cla-Min said, I am from one of the villages you visited a while ago. I… Help the village elder, mostly by tending to administrative matters."
young "And it fell to me to oversee the matters concerning our weekly deliveries to your caravan. I often handled the negotiations, and as such spent much time near the goblin carts."
young "Over time, I started noticing… Oddities. Peculiar patterns. Caravans from the south had products often found in the north, and the other way around."
young "Other had fruits that should have perished in the journey, yet remained fresh. And if a local carpenter or herbalist found themselves in need of an obscure product, the caravan in the following week often just so happened to carry it."
young "It became clear to me something was up. At first I suspected they were going through Blackholt Forest, and-"

ro "I think I get the gist of it. So what did you do once you figured out our Caravans weren’t what they seemed to be?"

young "Well, I…"
young "I approached miss Cla-Min and expressed my desire to be part of her venture."
young "… I might have offhandedly mentioned I’ll report them to the baron if they don’t do as I say, who would indubitably have them hanged for tax evasion."

if rastFirstVisit == False:
    ro "You never met the guy, have you?"
    young "Sir?"
    ro "No matter."

"Rowan tapped his throne, lost in thought. Cla-Min was one of the more sneaky of the twin’s supporters. She spent many months operating the castle supply lines, and people had yet to catch whiff of the true purpose of her caravans, and the way they remained profitable."
"The fact the aspiring boy figured it out, at least partially, was promising. The planning and execution of his get rich scheme… Left much to desire, but at least it did manage to get Cla-Min interested…"

show rowan necklace happy at midleft with dissolve

ro "So the guy tries to blackmail his way into your business, and your first instinct is to introduce him to your employer?"

cla "Of course! You know I just adore smart people with ambition."
cla "He was wasting away in the countryside! Rather than let a good protégé go to waste, I had a little talk with him, gauged the extent of his commitment, and then thought I’ll introduce you to him!"
cla "So what do you think?"

"Rowan turned his attention to the young man again. Despite finding himself a thousand miles away from home, at the mercy of people who were literally bound to demons, he seemed to be handling himself remarkably well."
"But it wouldn’t be enough. A quick mind was a blessing, but it didn’t guarantee being useful or successful. Especially not in Castle Bloodmeen."

ro "So besides having a sharp eye and poorly disguised suicidal tendencies, what skills do you bring to the table?"

young "I can write and read sir. I know arithmetic, I am familiar with many medicinal herbs, and understand the basics of magical theory."

ro "That’s quite a lot for a peasant. Have you studied in one of the local abbeys?"

young "Yes, for two years. I lied about my lineage to get there. They kicked me out once they learned of it."

ro "So you’re telling me you lied about your credentials to get your last job?"

young "When you put it that way, my lord…"

if society_type == "might":
    ro "Can’t say I blame you. Rosarian caste practices are awfully outdated."
    show rowan necklace happy at midleft with dissolve
    show clamin sad at midright with dissolve
    ro "You will find that we don’t employ them here."
    young "I am grateful to hear that, my lord."
    show clamin happy at midright with dissolve
elif society_type == "feudalism":
    show rowan necklace angry at midleft with dissolve
    ro "Good grief… People always trying to do whatever they can to rise above their station."
    show rowan necklace neutral at midleft with dissolve
    cla "Complained the son of a hunter to a goblin outcast turned Lady."
    ro "… I suppose."
else:
    "Rowan drummed his fingers on the throne’s arm. Only people born into the church of Solansia could climb its ranks. Hardly a fair practice, but it did promote unity among the clergy…"
    "He cast aside thoughts of Rosarian social system. There would be time to consider it later."

show rowan necklace neutral at midleft with dissolve

"He threw the ambitious boy another appraising look. Truth be told, the castle was horribly understaffed on every possible front. The twins had a knack for acquiring exceptional individuals, but there was only so much one person could do."
"Almost everywhere, he needed secretaries, assistants, attendants and simple help. The fact Cla-Min vouched for him was probably enough of a recommendation… Though he could ask for a more… Personal proof of loyalty."

if avatar.corruption < 50:
    "If he even wanted him here. Ambitious or not, the boy looked barely past eighteen... He had no idea what he was getting himself into. Maybe he could still send him away, if Cla-Min didn’t tell him too much about their operation…"

$ aspirantKeep = False
$ aspirantSucked = False

label aspirantMenu:

menu:
    "Send him to help Cliohna with research.":
        $ released_fix_rollback()
        $ change_relation('cliohna', 5)
        #increase research (TODO)
        ro "I accept your service. You will work in the castle library, under Cliohna. Find her, tell her I sent you."
        young "As you command, my lord."
        ro "Your fate is now in her hands."
        jump claminComplaining
        
    "Send him to Skodred.":
        $ released_fix_rollback()
        $ change_relation('skordred', 5)
        #increase income (TODO)
        ro "I accept your service. You will work with the head builder, a dwarf by the name of Skordred. Find him, tell him I sent you."
        young "As you command, my lord."
        ro "Your fate is now in his hands."
        jump claminComplaining
    
    "Let Cla-Min keep him.":
        $ released_fix_rollback()
        ro "It seems to me you already have a good rappport with Cla-Min."
        show rowan necklace happy at midleft with dissolve
        ro "Surely you would have use of him?"
        cla "Having human intermediaries is useful in some cities. But are you sure you don’t want to place him with someone else?"
        if check_skill(15, 'spot')[0]:
            ro "So that I would feel indebted to you?"
            ro "No, I think I’ll be alright."
            cla "Am I this transparent, love?"
            ro "Less than some. Don’t worry about it."
            $ change_relation('cla_min', 5)
        else:
            ro "Your business is the backbone of this operation. Is it really that surprising I’m committing resources to it?"
            cla "Of course not. It’s good to be appreciated."
            cla "But you know what it is that I really want…"
            "She flashed him a cheeky smile, and placed her hand on her belly. That woman did not give up…"
        
        "He turned his attention to the young man, who bowed in gratitude. Perhaps it was an outcome he was hoping for?"
        ro "Work hard and remember where your loyalties lie. Understood?"
        young "Of course, my lord."
        $ change_relation('cla_min', 5)
        #increase weekly income (TODO)
        return
        
    "Demand he first proves his loyalty. By servicing you. Sexually." if aspirantSucked == False:
        $ released_fix_rollback()
        $ rowanGaySex += 1
        ro "Tell me, young man, how far are you willing to go? What are you willing to do, to prove your loyalty, and usefulness, to us?"
        show rowan necklace happy at midleft with dissolve
        "Rowan reclined on his throne, spreading his legs casually, and waited for the man’s response. He rarely got to play lord like that. There was always some problem that needed to be solved… No time to enjoy the perks of the job."
        "The young man eyed Cla-Min from the corner of his eyes. The goblin mistress smiled and nodded, urging him to proceed."
        ro "Already hesitating? That’s-"
        show rowan necklace neutral at midleft with dissolve
        young "I’ll do it!"
        show rowan necklace happy at midleft with dissolve
        young "I mean- I’ll do it. Whatever it is you demand of me, my Lord. I’ll do it. My heart and soul belongs to Castle Bloodmeen, to the twins, and to you."
        show rowan necklace neutral at midleft with dissolve
        ro "Of the former I am certain. The latter I know is only a matter of time. But neither of them I require at the moment."
        show rowan necklace happy at midleft with dissolve
        ro "Come closer."
        show rowan necklace happy at center with moveinleft
        hide clamin with dissolve
        "He did as he was told, hiding his nervousness. Rowan mentally commended him for it. Enthusiasm was preferable, but when faced with a lack of it, quiet obedience was the next best thing."
        young "Then what it is that you require of me, my Lord?"
        show rowan necklace neutral at center with dissolve
        ro "What do you think? You showed such extraordinary investigative skills with our caravans. Put them to use here."
        show rowan necklace happy at center with dissolve
        "The boy’s head jerked almost unnoticeably, betraying his intention to again look to Cla-Min for guidance. He stopped himself though, knowing doing so would fail whatever test Rowan was putting him up to."
        "Instead, his eyes turned to the man on the throne. The smiling master of the castle, lazily leaning away on his throne, his legs open…" 
        "Rowan could almost hear him swallowing heavily." 
        young "I am willing to serve with all my heart, my mind, my soul… And my body."
        show rowan necklace neutral at center with dissolve
        "The hero nodded solemnly, acknowledging the seriousness of the pledge, but showing no indication the man guessed correctly. The man would have to decide himself if he wished to continue this course of action, knowing one bad move could spell the end of his ambitions…"
        if avatar.corruption > 50:
            show rowan necklace happy at center with dissolve
            "It was intoxicating, freely using his influence like that. If only he didn’t have to answer to the twins…"
        else:
            show rowan necklace concerned at center with dissolve
            "It was dangerously thrilling, using his power like that, realizing and ending dreams on a whim. Maybe that’s why the twins allowed him so much freedom in the matters of the state. So he would learn to enjoy the power he held over people…"
            ro "(Better not think about it now…)"
        show rowan necklace neutral at center with dissolve
        ro "Well then?"
        "He watched as the boy’s expression grew stern, more determined. He came to a decision."
        "And that decision was, to walk up the throne’s steps and kneel before Rowan, placing his hands on the hero’s knees."  
        show rowan necklace happy at center with dissolve
        "Rowan barely stifled a chuckle. He was being so serious about it! Hardly surprising, given the situation… And in part, he admired the commitment. Focused, persistent. He understood what Cla-Min saw in him."
        show rowan necklace happy at midleft with moveoutleft
        show clamin happy at midright with dissolve
        "And speaking of the goblins mistress… She was still in the hall, watching as her protégé started to unbuckle her boss. A devious smirk danced on her lips, that quickly turned to her usual shining smile the moment she noticed she attracted Rowan’s attention once more."
        menu:
            "Let her watch.":
                $ released_fix_rollback()
                $ aspirantClaPresent = True
                ro "Developing a bit of a voyeuristic streak, are we?"
                cla "Oh, “voyeuristic” already. Is it so wrong of me to look after my investments?"
                ro "And you’re referring to which one of us here?"
                "The goblin flashed her teeth in a coy smile, refusing to answer."
                hide clamin with dissolve
                show rowan necklace happy at center with moveinleft
                ro "(What a hopeless woman…)"
                jump aspirantSexScene
                
            "Tell her to wait outside.":
                $ released_fix_rollback()
                $ aspirantClaPresent = False
                ro "Developing a bit of a voyeuristic streak, are we?"
                cla "Oh, “voyeuristic” already. Is it so wrong of me to look after my investments?"
                ro " In this case? Yes. A bit of privacy would be welcomed."
                cla "Your wish is my command, love."
                hide clamin with moveoutright
                show rowan necklace happy at center with moveinleft
                "She flashed him a coy smile, then hurried out of the chamber."
                jump aspirantSexScene

    "Cla-Min be damned, this guy is suspicious. Enslave him." if aspirantKeep == False:
        $ released_fix_rollback()
        ro "I take it you vetted him extensively?"
        if castle.buildings['tavern'].lvl >= 1 or castle.buildings['pit'].lvl >= 1:
            ro "I wish Andras shared your thoroughness."
            show rowan necklace angry at midleft with dissolve
            show clamin neutral at midright with dissolve
            ro "Regardless, I would rather his hobby of picking random people to serve as castle staff did not become a common practice we all indulge in."
        else:
            show rowan necklace angry at midleft with dissolve
            show clamin neutral at midright with dissolve
            ro "And yet I can’t help but feel distressed by the fact he’s even here. Since when do we practice picking up strays like some damned orphanage?"
        cla "Rowan? Love? What are you saying?"
        show rowan necklace neutral at midleft with dissolve
        if aspirantSucked == True:
            ro "I’m saying that for all his intellectual assets and mediocre cock sucking skills, this boy cannot be trusted. And I have no intention of letting him walk out of castle Bloodmeen freely."
        else:
            ro "I’m saying that for all his intellectual assets, this boy cannot be trusted. And I have no intention of letting him walk out of castle Bloodmeen freely."
        ro "Guards!"
        show clamin neutral at center with moveinleft
        show orc soldier neutral at edgeright with dissolve
        "Orcs poured into the chamber. At Rowan’s orders, they grabbed the man, quickly gagging him. Rowan saw his expression turn from shock to despair. Foolish boy. He never should’ve come to Castle Bloodmeen."
        cla "Rowan this is-"
        "He raised his finger, and the goblin merchant instantly fell silent. He stood up from his throne, and approached her with a somber expression on his face, while the orcs dragged the aspirant out of the hall."
        hide orc soldier with moveoutright
        show clamin neutral at midright with moveoutright
        ro "Cla-Min this entire operation relies on us maintaining secrecy. One bad ally, one untrustworthy recruit, and this entire thing falls apart, and both of us end up dead."
        if serveChoice == 1 or serveChoice == 3:
            scene black with fade
            show rowan behind black
            ro "(Which would be a small price to pay for seeing the twins fall… But I need to get Alexia to safety first.)"
            scene bg6 with fade
            show rowan necklace neutral at midleft with dissolve
            show clamin neutral at midright with dissolve
        ro "So you will forgive me if I do not wish to compromise our security just because you found yourself a pet capable of a few tricks."
        show clamin happy at midright with dissolve
        cla "… Of course. I’m sorry. I should’ve consulted with you first."
        ro "Yes, you should’ve."
        if check_skill(15, 'spot')[0]:
            show rowan necklace angry at midleft with dissolve
            show clamin neutral at midright with dissolve
            ro "And I ask you to refrain from trying to stack the castle staff with people indebted to yourself."
            ro "It’s a dangerous game you’re playing here."
            show clamin happy at midright with dissolve
            cla "Ah, love, it’s so sweet of you to worry about me."
            show clamin neutral at midright with dissolve
            cla "I shall take your advice to heart."
            $ change_relation('cla_min', 5)
        else:
            show rowan necklace concerned at midleft with dissolve
            ro "I appreciate the initiative, but next time, inform me first?"
            cla "Of course, love."
            show clamin neutral at midright with dissolve
        show rowan necklace neutral at midleft with dissolve 
        ro "You can go now."
        hide clamin with moveoutleft
        "The Goblin bowed before him, then quickly took her leave, clearly in no mood to pester Rowan further. He was left pondering whether or not he was being too paranoid about the whole ordeal…"    
        $ change_relation('cla_min', -5)
        $ change_prisoners(1)
        $ change_favor('jezera', 1)
        return
       
    "This place will eat him alive. Send him away, for his own good." if avatar.corruption < 50 and aspirantSucked == False:
        $ released_fix_rollback()
        ro "Boy, come here for a moment."
        hide clamin with moveoutright
        show rowan necklace neutral at center with moveinleft
        "He urged the boy to step forward, all the way onto the steps of the throne. Once he was right in front of him, Rowan leaned in, and lowered his voice so Cla-Min wouldn’t hear them."
        ro "How much have you been told about this castle? About me? About the twins?"
        young "Not that much sir. I understand the castle belonged to the previous demon lord? And that the current occupants are his descendants?"
        ro "And what about me?"
        "The boy hesitated, eyeing Rowan dubiously. Finally, he lowered his head, and answered:"
        young "Miss Cla-Min told me you’re the Great Trickster, and that you responsible for the twins’ success. She added that if I want to get anywhere here, I have to my best not to anger the twins, but it’s you I should seek to please. "
        ro "Lovely."
        ro " (He doesn’t seem to recognize me… He’s too young for that. This makes things easier)."
        ro "Listen… Whatever Cla-Min told you about this place, she was sugarcoating things, okay? This castle will eat you alive. And not in the fun, sexy way."
        ro "You value your life? Forget your ambitions, and run away. Run away as fast as you can. Forget this place, forget me, forget Cla-Min, and just run. Return to your village, and live a happy, long live, away from all of this."
        ro "You understand?"
        "The boy hesitated, uncertain. Rowan could see his trip to the castle didn’t go as he thought it would."
        ro "(Welcome to the club kid.)"
        "Finally, he gave a reluctant nod, understanding that without Rowan’s backing, he was a small fish in a sea full of sharks.  Rowan signaled him to walk away, then turned to Cla-Min. The thrifty goblin kept watching them, silent, but attentive."
        show rowan necklace neutral at midleft with moveoutleft
        show clamin neutral at midright with moveinright
        ro "Cla-Min, I want you to escort this young man to the village you first found him in. He will be of more use to us as a spy, than servant."
        if check_skill(5, 'deceive')[0]:
            pass
        else:
            show clamin sad at midright with dissolve
            cla "..."
            $ change_relation('cla_min', -5)
        show clamin happy at midright with dissolve
        cla "Of course. I’ll handle everything."
        ro "Good. Dismissed."
        hide clamin with moveoutright
        "He only hoped Jezera wouldn’t catch wind of this…"
        $ change_favor('jezera', -1)
        $ change_base_stat('c', -5)
        return
       

label claminComplaining:

cla "Aw, I was hoping you’d let me keep him."

if check_skill(15, 'spot')[0]:
    show rowan necklace angry at midleft with dissolve
    show clamin neutral at midright with dissolve
    ro "No, you weren’t. You wanted me to assign him somewhere, hoping I would feel indebted to you."
    show clamin happy at midright with dissolve
    cla "Am I this transparent?"
    show rowan necklace neutral at midleft with dissolve
    ro "Less than some. Don’t worry, you’re not losing your edge."
    $ change_relation('cla_min', 5)
    
else:
    ro "If he’s really as smart as you’re selling him here, then I’ll need him elsewhere. We’re more or less shorthanded on all fronts, all the time."
    cla "I understand. Perhaps the next one then?"
    ro "Perhaps."
    
ro "The matter is settled then. Good luck…"

scene black with fade

"Huh, he never asked for his name."
    
return

label aspirantSexScene:

"Paying no attention to his discussion with Cla-Min, the boy finally undid Rowan’s trousers, and was met with his half-erect cock. He recoiled a little, as if surprised by the size."

ro "Have you done anything like that before?"

young "No… My lord."

ro "Then I hope you learn quickly."

#blurred cg1
scene black with fade
show rowan necklace happy behind black

"Magnanimously, Rowan ran his fingers through the boy’s curls, lightly pushing him towards his cock while the young man awkwardly wrapped his fingers around his phallus."
"He stroked it gently, his gaze focused on the tip, with resolve that continued to bring a smile to Rowan’s face. So nice to see people willing to give it their all…"
"Again, he pushed his head forward, reminding him not to waste too much time on the foreplay. The large tip of his dick brushed against the young man’s cheek, leaving a small, white stain on his skin."

if avatar.corruption > 50:
    ro "Come on, show your new master what you’re capable of."

else:
    ro "Come on, show your new lord what you’re capable of."

#cg1
scene black with fade
show rowan necklace happy behind black
show clamin happy behind black

"The boy nodded, and his mouth parted, welcoming Rowan’s cock."

young "Mmm-mmm!"

"Rowan was free to marvel at the embarrassed expression that graced the boy’s face. He really must have been new to this… Maybe even his cock was the first he ever tasted."
"It would seem so, as he did not seem to be capable of taking him any further in, gagging when he first tried. Instead, he focused all his attention on the tip of his cock, his wet tongue dutifully circling around the sensitive head."

ro "Hmm…"

"He had to admit the boy was trying his best here, but his inexperience was… Vexing. He needed more training. Guidance."
"Or breaking in."

menu:
    "A disappointing performance. Use his head to get yourself off.":
        $ released_fix_rollback()
        $ change_base_stat('c', 3)
        ro "Admirable attempt, but…"
        ro "You should’ve come more prepared. In a castle full of sex demons, this is hardly enough."
        young "Mm-mmm?"
        ro "No, no, no need to worry, just… Open wide. And mind your teeth."
        "With only this scant words of warning, he gripped the boy firmly, and shoved his head all the way to the base of his dick. The poor sod gurgled something in protest, but Rowan paid no mind to it."
        if aspirantClaPresent == True:
            cla "Don’t struggle! Relax your head, let it slide all the way in!"
            ro "Couldn’t explain it better."
        "He continued to thrust his head up and down his cock, using the man as a simple relief toy for his lust. It didn’t take long for the boy to accept his place. Accept his role."
        "He relaxed his posture, adjusting his pose so that Rowan’s cock could reach deeper – deeper, all the way to the back of his throat-"
        young "Ghrl!"
        ro "Hmph, we’ll have to rid you of that gag reflex."
        "- despite Rowan doing nothing to make the harsh facefucking in any way bearable. He wanted to test him. See how well suited he was for the role he would no doubt take in castle Bloodmeen if he lacks the spine to stand up for himself."
        "That of a bottom bitch."
        "And he was pleased to see the boy learned quickly, and soon bobbed his head rapidly on Rowan’s dick, no longer requiring the hero force him in any way. His expression grew less tense, his cheeks red, and his eyes even rolled back a little."

    "Offer some advice.":
        $ released_fix_rollback()
        ro "Admirable attempt, but…"
        ro "You should’ve come more prepared. In a castle full of sex demons, this is hardly enough."
        young "Mm-mmm?"
        "He ran fingers through his hair gently, looking him in the eyes as the man gently sucked his tip."
        ro "You have to learn how to take a cock all the way in. All the way to the base."
        ro "If you can’t do it now… Guess I’ll have to forgive that, but you better start practicing."
        "The man continued his ministrations for a moment, eyes focused on Rowan. His mind, if Rowan had to guess, racing."
        "Finally, he opened his mouth wider, and again tried to take more of Rowan in. Tried to force him deeper, past his tongue, which still continued to lick dutifully, lubricating Rowan’s cock, coating it with saliva."
        "Saliva that now lewdly dripped down his chin, creating quite the pretty picture."
        young "MM-mm! Ack!!"
        if aspirantClaPresent == True:
            cla "You have to relax your throat! Don’t struggle, and just let it slide in!"
            young "Mmm-mmm…"
            "The hero saw the goblin flash him a knowing smile from the sidelines, and Rowan raised his hands in defeat."
            ro "I concede, he is a fast learner…"
            cla "Told you!"
        else:
            ro "Relax your throat. Stop struggling so much."
            young "Mmmmm… Mmm."
            "It took him a while, but several attempts later, Rowan’s cock finally pierced all the way to down his throat. "
            ro "Well done… Keep going."
        "Growing more comfortable with Rowan’s dick by the minute, the young man increased his speed, increased the tempo."
        "As if relishing in his newfound deepthroating talent, he now freely pistoned his face on Rowan’s dick, taking him all the way in, up and down, just as Rowan wanted him to."
        "He was almost fucking himself on Rowan’s cock, so great was his enthusiasm... His eyes even start to roll back a little!"

ro "So you enjoy being at the bottom after all. "

young "Mm, mmm…"

"Rowan stroked his hair affectionately, pleased with this development. Heart, soul and body indeed… He didn’t know about mind yet, but a willing body often preceded a pliant mind."
"This continued for several minutes, and soon enough, Rowan felt himself nearing the end, felt the pressure rising."
"He grabbed the boy’s head more firmly, and again, pulled him all the way to the base of his dick, the tip of his cock buried deep inside his throat, as he started to climax."

ro "Ah!"

young "Mmm!"

"Load after load, deposited directly into his stomach. Thick, warm cum, courtesy of the master of Castle Bloodmeen."

young "MMm! Mmm… Mmm- ah! Aaah… Ahhh…"

scene bg6 with fade
show rowan necklace neutral at center with dissolve

ro "What do you say?"

young "T-thank you… My lord…"

show rowan necklace happy at center with dissolve

"Well done. Now clean yourself up."

if aspirantClaPresent == False:
    ro "Cla-Min! You can come back now."

show rowan necklace happy at midleft with moveoutleft
show clamin happy at midright with dissolve

cla "Happy with his performance?"

menu:
    "Yes. Cla-Min did well bringing him to the castle.":
        $ released_fix_rollback()
        ro "Yes, and you did well bringing him here. He’s certainly going to adapt to Castle Bloodmeen well."
        cla "He already got the most important lesson down!"
        cla "So where are you going to assign him?"
        $ change_relation('cla_min', 3)
        $ aspirantKeep = True
        
    "You still have some doubts about him.":
       $ released_fix_rollback()
       show rowan necklace neutral at midleft with dissolve
       show clamin neutral at midright with dissolve
       ro "… It was acceptable."
       "He let the matter in the air, drawing a concerned looks from both Cla-Min and her hopeful protégé."
       
$ aspirantSucked = True

jump aspirantMenu

