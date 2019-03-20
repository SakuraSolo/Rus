init python:
    
    event('snitches_get_stitches', triggers="week_end", conditions=('week >=30', 'all_actors["alexia"].relation > 60',), depends=('resistance_futile',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('village_argument', triggers="week_end", conditions=('week >=30', 'castle.villages > 1', 'society_type !="none"',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('bathing_andras', triggers="week_end", conditions=('week >=30', 'all_actors["alexia"].job_state.job != "none"', 'NTR == True', "castle.buildings['arena'].lvl >= 1",), group='ruler_event', run_count=1, priority=pr_ruler)


label snitches_get_stitches:

scene bg9 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

"Alexia crossed her arms over her chest, and looked over the documents that Rowan had placed on the table. Rowan furrowed his brow, wondering what might be going through her head."

al "What’s...What is all of this?"

"She kept her voice low. The danger to her was obvious."
"Rowan etched his hand over a map drawn with mediocre penmanship." 

ro "Documents. Part of my job is to manage supplies and information for the army. They don’t trust me with everything. But, they have to tell me all about supply, troop counts, and intelligence reports from field agents and spies that are directly important."
ro "Most of the documents are one of a kind. People might realize if they went missing."
ro "But, there's probably not a way to stop someone with direct access from copying their information."

"He slumped down on the bed next to her. Alexia folder her legs to the side to make room for him."

ro "There is only so much that I should ever keep. Any more wouldn’t be feasible…"
ro "...Or safe."

"Alexia stared at one of the pages on the table. It was a request form down to the merchants for helmets. Numbers, costs, materials. Rowan knew that in the hands of a Prothean general, this could help turn the tide of entire battles."

al "This is...I hadn’t imagined that you’d been doing such things. You know what the Twins would do to you if they discovered this stash. Your life is on this table, Rowan."
al "What do you intend to do with it?"

show rowan necklace concerned at midleft with dissolve

ro "For the moment? What can I do?"

"He let his head sink slightly into his hands. Alexia was touching his shoulder, looking at him sympathetically."

ro "If I give this to the other side without knowing my role here and how I got into that position, all of it will go to waste. They need to trust it."
ro "I can’t sneak it over to the other side without an ally who can get them to listen."
ro "I can’t really blackmail them with it either. Not when they can turn either of us into a blood stain on a whim."
ro "So for the moment, I’m just holding on to them. Someday, I might have an opportunity to use them as a weapon against them."

if avatar.corruption < 30:
    ro "...It can be my atonement..."
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "I’m going to make those bastards pay for everything they’ve done."
    
show rowan necklace neutral at midleft with dissolve

"Alexia rubbed her hand on his shoulders softly. There was so much tension in them. They were used to carrying so much weight."

ro "I wanted you to know where I kept the stash of it, so that way in case something ever happens to me..."

al "Don’t talk like that. I mean it. Don’t. You never used to talk like that even when you were in the army."

"Rowan gave her a weak smile."

ro "The question then is how to store them in a way where they’d be safe. Jezera can probably see anywhere in the castle that she really wants using her dark magic. But, maybe if there is somewhere that she doesn’t know abou-"

show rowan necklace angry at midleft with dissolve
show alexia 2 necklace shocked at midright with dissolve

"The door swung open."
"Inside walked a balding servant carrying a tray of food. Rowan’s hair stood on end."

serv "Sir Rowan? I’ve come to bring you-"

"He looked around the room. Then his eyes widened. He was looking right at the map on the table. Did he know?"

ro "Why didn’t you knock?"

"The servant bowed his head, still eyeing the table. Rowan put a hand on the hilt of his sword."

serv "I apologize. My mistake. I will have the tea brought up at another time."

"The servant hurriedly returned to the hallway, and slammed the door shut with a thud."

show rowan necklace concerned at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

"At once, both Rowan and Alexia exchanged a worried glance."

al "He saw the papers."

ro "I locked that door, didn’t I? Did he know we were talking in secret?"

"The danger that had been a phantom spectre moments before was now tangible."

al "I think I know that man, though. I have contacts among the servants."

"Rowan rose from the bed and started tapping his feet. They would have to act fast. There was no telling how soon he could tell Jezera what he saw."

ro "He didn’t get that good a look, so he probably won’t be able to speak to her immediately. Probably. We have a chance to get to him first, just to make sure."
ro "He might even really have just wandered in accidentally."

"Alexia rose to her feet as well."

al "I’m going to try to find out where he’s working. We can meet back up in an hour."

"Rowan ducked down to the table and swept the documents into a nondescript sack. No good having someone see them while they were out."

al "I love you."

ro "Love you too."

hide alexia with moveoutright

scene bg8 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan paced the dark cell that he had chosen as the meet up point. Alexia was supposed to be down here at least five minutes ago. What was taking her so long?"
"Had the man already gone to Jezera? The thought created a pit in his stomach."
"That was when the door to the cell opened. Rowan’s muscles tensed."

show alexia 2 necklace concerned at midright with dissolve

"All of his idle speculation came to a stop. It was Alexia, and with her was the man who had entered the room the hour before. He was half quivering in his boots."
"For the first time, Rowan actually got a look at the man. He was perhaps in his 40s, with aging features that showed it. Most prominent was his pattern baldness, that left dark hair at his temples, but not the top of his head."
"There was a certain slobbishness to him. Even his outfit, while dignified by the other servants, was ever so slightly disheveled. Rowan could almost imagine how he got here. Probably a failed business venture, or a disgraced reputation in his former home."

show rowan necklace angry at midleft with dissolve

"But, Rowan didn’t want to imagine this man’s story. Not at this moment."

serv "I’m so sorry. Really. I am. I didn’t mean to barge in like that. I wasn’t thinking. I just went to check on you and the papers were right thereinsightandI-"

"Rowan crossed his arms and gave the man a dark glare."

ro "Calm down. Go back a step. You just walked in? The door wasn’t locked?"

serv "Well, just opened the door and…"

ro "The door was locked."

serv "I don’t know. I don’t know…"
serv "Actually...when I was opening the door, my hand bumped into this little latch thing at the bottom of the handle frame. I thought that was kind of weird. Maybe that did it?"

al "A little latch?"

"Rowan put a hand to his chin. It was possible the man was telling the truth. It would be in character of Jezera to include some secret way to bypass the lock on the door. Though, it was far more likely he had a key and was just lying. He’d need to check the door later."

ro "Let’s get right to the point."
ro "You said yourself that you saw documents. What did you see? Tell me everything that you remember."

serv "I...I...I…"

ro "Relax. Just tell me."

serv "Look, I didn’t mean to see anything. I just, looked around and I saw a map on the table. It looked like Rosaria. And it seemed odd, because why would you be talking to your wife about military matters like that."
serv "Then, when I walked in, you looked so defensive. And you were grabbing your sword. I didn’t mean to see anything. I swear."
serv "I won’t say a word about this to anyone. Not a word. I’ll pretend like I never saw anything."
serv "Please. I don’t want to get involved in fights among the big guys."
jont "My name is...My name is Jon. Jon Thusia. I don’t want to be involved in anything."

"Rowan watched the display Jon was making with pitying eyes. He really did seem over his head." 
"Though, the fact he was showing this much fear was slightly odd. Yes, there was the implicit threat of violence, but Rowan didn’t have a reputation for violence against subordinates. Besides, he wasn’t really a “big guy”. Not in Bloodmeen."

ro "Don’t move at all."

"Rowan led Alexia into a corner far away from Jon, but where he was still in Rowan’s peripheral vision."

show rowan necklace concerned at midleft with dissolve

ro "This is really bad. He seems like a nobody."

"Alexia looked to the side and crossed her arms over her chest."

al "Then what do we do with him?"

"Rowan looked back over his shoulder."

ro "There is no way we can know for certain whether or not he’s one of Jezera’s spies. But, there really is a good chance that he is just unlucky."

al "And if he isn’t?"

ro "I don’t know. I don’t."

"They stood in silence for a moment. The answer in this situation was obvious, but there was a barrier, born from years of life, standing in the way."

if all_actors['alexia'].corruption > avatar.corruption:
    "Alexia broke it first."
    al "If we did have to do something about it, would it be hard to cover it up?"
    "Rowan shook his head."
    ro "I was thinking about it while waiting for you. The caverns beneath the castle are really large. Huge segments of it are unused. If we left a body there no one would find it."
    ro "I doubt anyone would make too big a stink about his disappearance. Even if he’s one of Jezera’s informants, he’s a nobody. She has tons of informants and the castle has tons of servants. Probably no one would care."
    ro "...No one would care at all…"
    
else:
    "Rowan broke it first."
    ro "I was thinking about how we’d do it if we needed to while waiting for you. The caverns beneath the castle are really large. Huge segments of it are unused. If we left a body there no one would find it."
    ro "I doubt anyone would make too big a stink about his disappearance. Even if he’s one of Jezera’s informants, he’s a nobody. She has tons of informants and the castle has tons of servants. Probably no one would care."
    al "That’s kind of sad when you think about it."
    ro "Yeah. Yeah it is."
    
"They both took a moment to clear their throats."

al "What do you want to do, Rowan? I trust you. It’s your decision to make, either way."

menu:
    "Kill Jon.":
        $ released_fix_rollback()
        "Rowan sighed inwardly and closed his eyes."
        ro "During the war, it wasn’t just orcs I killed. There were humans too. Those who took to the dark banner."
        ro "I don’t know this man’s story. But, he is a servant of the Twins. We don’t have the power to compel his silence if he wanted to talk to them. There is only one choice we can make here."
        if avatar.corruption < 30:
            ro "No matter how unpleasant a choice it is."
        "Alexia didn’t say anything for a short period of time. When she spoke again, it was with resignation."
        al "We have to do what we have to do."
        hide alexia with dissolve
        "Alexia turned her back away from Jon. She was not used to watching people die."
        "Jon shook slightly as Rowan approached. The conversation in the corner had no doubt lasted for an uncomfortable period of time. "
        show rowan necklace neutral at midleft with dissolve
        "There were no further words that passed. No warning Jon was given. In one swift motion, Rowan shoved his sword through Jon’s heart."
        show bg8 with redflash
        jont "Ack!"
        if avatar.corruption < 30:
            ro "I'm sorry."
        "Jon slumped over immediately. Stabbing some parts of the body cause a slow, drawn out death, and others kill a man fast. Rowan had made it quick."
        "When it was done, he stood over the crumpled form, sword and outfit stained with blood. Alexia turned around to see it, putting her hands on her face."
        show rowan necklace concerned at midleft with dissolve
        show alexia 2 necklace shocked at midright with dissolve
        al "...Solansia…"
        "Rowan looked down at the body. He knew was going to be a long night carrying it down into the depths. "
        ro "This won’t be the last time, you know. Our enemies own this castle. They own us. We’re probably going to need to kill again. We need to be ready for it."
        show alexia 2 necklace concerned at midright with dissolve
        "Her face went slightly white, her eyes glued on the corpse."
        al "I’ll..I’ll try."
        "After that, Alexia went back up to their room, leaving Rowan with his grisly work. He had been correct in his assessment. It was a long night. Jon’s face was frozen in his final look of terror the entire time."
        $ change_corruption_actor('alexia', +5)
        $ change_base_stat('c', +5)
        return
        
    "Spare Jon.":
        $ released_fix_rollback()
        "Rowan sighed inwardly. He’d seen all the dangers that lay ahead in his nightmares. It wasn’t that he didn’t understand the situation…"
        ro "No. I don’t think we should do it."
        ro "I know. Killing him by far the safer thing to do. But, when I considered it, there was just one fact that I couldn’t put aside."
        al "What was it?"
        ro "Killing him was what Jezera would do. It’s what she would want us to do. If we give in and kill him, then she still wins."
        ro "I don’t think she’d kill us over the maps even if she found out. It’s not worth the risk of killing an innocent man over."
        if avatar.corruption > 30:
            "Even as he said that out loud, a small voice in the back of his head still chided his naivety. He knew this was stupid. He knew it was sentimental. Everything he’d learned here had taught him that."
        "Alexia glanced back at Jon. She still looked doubtful."
        al "I...I’m afraid to risk it."
        ro "I know…"
        al "But, if you think that’s right, then I’m sure this is the right decision."
        if all_actors['alexia'].corruption > 30:
            "There was a strange look in her eyes even as she said that. Rowan felt a small chill down his spine. She was lying. She was judging him this very second."
        "Rowan returned to Jon and laid out the rules. This conversation had not happened. Walking in on the room had not happened. If word reached them that Jon was talking, he would have to answer to Rowan directly."
        "Jon certainly seemed scared by the prospect. He enthusiastically agreed to keep his mouth shut, and scurried off the moment Rowan gave him leave to go."
        "Rowan hoped it worked…"
        $ sabotage_route -= 1
        $ overlord_route -= 1
        return
        
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

label village_argument:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

ro "And what is this about?"

os "Humi greedy! Wants wat not his!"

merc "Lord Rowan, with all due respect for my brother in arms here, his words are, to put it mildly, a gross misrepresentation of the truth. I have merely come to explain- "

os "GREEDY LITTLE PIG!"

merc "- that I believe there would be tangible benefits to leaving Cheshire Burrows in my care, as I have-"
        
show rowan necklace angry at midleft with dissolve

os "MY VILLAGE!"

merc "-several valuable-"

os "NOT YOUS!"

merc "Oh can you SHUT UP FOR ONE-!"

ro "ENOUGH!"

if avatar.corruption > 50:
    ro "Both of you, stay your tongue or I’ll have them cut, cooked and served to the dogs."
    ro "Explain the situation, one at a time."

else:
    ro "Both of you, be quiet, and explain the situation. Wait your turn, and let the other speak in peace."
    
scene bg6 with fade

"The problem they approached him about, once explained in full, proved to be a simple one."
"The man before him, one of the many human mercenaries the twins employed as auxiliary forces to the orc army, was previously a Rosarian peasant, who just so happened to be born in Cheshire Burrows, one of the villages Rowan had conquered in Rosaria."
"As the man was native to the place and knew the people living there, he wanted to oversee the area. He argued the place would be better off if left in his care, and that it wasn’t “right” to have orcs, who had no concept of agriculture and weren’t even native to the area, overseeing human settlements."
"Though Rowan doubted the man in front of him had any farming experience himself. After the war, there was no small number of farmlands that lost their owners to the demons, and village elders often gave local land away for free."
"The people who ended up serving the twins never had any interest in a tending to the fields to begin with."
"The orc’s argument, on the other hand, was thus: He was on the vanguard of their force when they took Cheshire Burrows and by right of conquest the place was his to rule.  Or at least oversee it in the Twin’s name."

show rowan necklace neutral at center with dissolve

"And now it fell to Rowan to decide who he wanted to have on the ground in Cheshire Burrows."

menu:
    "Orc support is crucial to the war effort. Let him keep the land.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with moveoutleft
        show orc soldier neutral at midright with dissolve
        ro "Rosarian settlements are our primary source of income. I need them subjugated, and orc presence prevents the peasants from getting any stupid ideas."
        "He nodded at the orc, giving him his blessing in all of this."
        ro "Keep them pacified-"
        os "Uh?"
        show rowan necklace concerned at midleft with dissolve
        ro "… Keep them afraid."
        show rowan necklace neutral at midleft with dissolve
        ro "But don’t forget about the grain and the gold. We need the weekly supplies to keep coming. Am I clear on this?"
        "The orc nodded his head enthusiastically, his mouth widening in a grotesque parody of a triumphant smile as he regarded the human mercenary next to him."
        "The man in question was, predictably less than pleased by this development."
        ro "Is there something you wish to add?"
        if society_type == "might":
            "The mercenary hesitated, then bowed graciously, knowing fully well it was unwise to make an enemy out of Rowan."
            merc "No, Lord Rowan. I only ask that you not forget there are people who contribute to the war effort in ways other than standing on the front lines."
            ro "I assure you I am well aware of that. Anything, else?"
            merc "No, Lord Rowan."
        else:
            show rowan necklace angry at midleft with dissolve
            merc "… Yes, if I may."            
            show rowan necklace neutral at midleft with dissolve
            merc "Lord Rowan, I must ask: Is this a temporary solution or should we presume Cheshire Burrows is therefore granted to the orcs?"
            merc "When Empress Jezera named you a Lord and granted noble titles to some of the other people in the castle, many of us were hoping this would mean that our commitment to the cause would soon be rewarded as well."
            merc "But I see the orcs take priority."
            "There was a not so subtle note of resentment in his voice, and Rowan knew all too well how easily it could turn into widespread dissent."
            ro "(I can’t deal with this right now. Last thing I need is people banging at my doors, demanding titles and fiefs.)"
            if check_skill(10, 'diplomacy')[0]:
                show rowan necklace happy at midleft with dissolve
                ro "I assure you your continuous service is much appreciated by both the twins and myself."
                show rowan necklace neutral at midleft with dissolve
                ro "Consider this a temporary solution, as there is simply no point in counting chicken before they’re hatched. We cannot guarantee any of the currently subjugated villages will remain in our hands in the years to come."
                ro "For now, the focus is on keeping order and gathering resources. We will split the territory later."
                ro "You will all get what you deserve – when the time is right."
                merc "… That is all we ask for, Lord Rowan."
                "The man didn’t appear all that convinced, but his concerns were adequately alleviated, for the time being."
            else:
                show rowan necklace angry at midleft with dissolve
                ro "Do you honestly intend to waste my time with childish accusations of favoritism?"
                ro "Or are you just disappointed you would not be getting your slice of the pie as quickly as you had been expecting?"
                merc "Lord Rowan, I-"
                ro "Do not interrupt me."
                show rowan necklace neutral at midleft with dissolve
                ro "You will all get what you deserve, when the time is right. In the meantime, stop being so greedy, and cooperate."
                ro "Am I being clear here?"
                merc "Of course, Lord Rowan. My apologies for speaking out of place."
                "His voice was stiff, and for a moment, Rowan wondered if it wouldn’t be better to make an example out of him."
                "But he couldn’t be chasing after every single display of dissent. He memorized his face and made a mental note to deal with him quickly if he ever causes problems again."
                $ castle.morale -= 5
            ro "Then the matter is settled. You are dismissed."
            $ castle.morale += 5
            return
            
    "Cheshire Burrows will be better off with a human supervisor.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with moveoutleft
        show orc soldier neutral at midright with dissolve
        ro "Every gold coin and every sheaf of grain is important to us. I need the villages as productive as possible."
        "He nodded at the human, given him his blessing in all of this."
        ro "You will oversee Cheshire Burrows from now on. If I hear of any problems there, you know what will happen."
        "The mercenary bowed deeply, praising Rowan’s wisdom. The orc, on the other hand, was less than pleased with this development."
        if society_type == "might":
            os "Dis wos not wat masta’ Andras promised! "
            os "We took da village! It should be ou’s!"
            show rowan necklace angry at midleft with dissolve
            os "“Might makes right”!"
            show rowan necklace neutral at midleft with moveoutleft
            "Rowan suppressed a sigh, silently cursing Andras for the grandeur speech he made on the whole thing a while ago. It really didn’t explain all that well what they were going for." 
            "Meritocracy meant rule of the most competent, not the strongest… Not that orcs ever saw value in skills concerning matters other than warfare."
            if check_skill(15, 'intimidate')[0]:
                show rowan necklace angry at midleft with dissolve
                ro "(I don’t have time for this…)"
                "The orcs only really understood one language – the language of power. So he raised from his throne, and took a step towards the impertinent soldier."
                show rowan necklace angry at center with moveinright
                ro "“Might makes right” indeed."
                ro "And I’m saying this land does not belong to you."
                ro "Do you wish to contest this decision?"
                os "……………….. No, masta Rowan."
                show rowan necklace happy at midleft with moveoutleft
                ro "Good."
                show rowan necklace neutral at midleft with dissolve
            else:
                show rowan necklace angry at midleft with dissolve
                ro "Ignoring for a moment that I really don’t have to explain myself to you people, shut up and listen."
                ro "“Might makes right” does not mean rule of the strongest, but the most competent. And in this case, this man is better qualified for the job."
                ro "Have I made myself clear?"
                "The orc was hardly happy with this resolution, but it didn’t matter. They would fall in line.  They always did."
                #permantly lower morale by 2 (to do)
                $ castle.morale -= 2
        else:
            "He grumbled something under his breath about human favoritism, but didn’t dare to meet Rowan’s eyes. Ever since Jezera named Rowan Lord, many of them quickly realized where their place was in the new pecking order."
        ro "Then the matter is settled. You are dismissed."
        #permantly lower morale by 3 (to do)
        $ castle.morale -= 3
        #increase weekly income a little (to do)
        $ castle.treasury += 100
        return
            
    "Cla-Min’s clan needs some fiefs." if society_type == "feudalism":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with moveoutleft
        show orc soldier neutral at midright with dissolve
        ro "Neither of you deserve these lands."
        ro "I will assign a goblin supervisor to the Cheshire Burrows. Someone who actually handles supply and administrative matters, rather than a solder with no stewardship experience."
        show rowan necklace angry at midleft with dissolve
        "The orc gawked at him in surprise, his expression slowly turning that into absolute fury. But one angry glance from Rowan was enough to have him back down. Ever since Jezera named him and Cla-Min nobles, many of them were quick to realize their place in the new pecking order."
        show rowan necklace neutral at midleft with dissolve
        "The human, on the other hand, would not be dissuaded so easily."
        merc "Lord Rowan, would you reconsider? When Empress Jezera declared a new order on Solanse, we thought this would mean adequate rewards for everyone – especially us. Many of us took a massive risk by betraying our nations and joining the twins."
        merc "The pay and the slaves are all nice, but when you and Lady Cla-Min are rewarded with noble titles… It seems to us like we’re getting the short end of the stick here."
        if check_skill(15, 'diplomacy')[0]:
            ro "(What a load of crap…)"
            ro "Do not worry, you will get your just reward – in due time."
            ro "But for the time being, our resources are sparse, and enemies plenty. You’re warriors, and I need you on the field. Both of you."
            ro "But I guarantee you, when the time is right, you will not regret having joined us."
            merc "… If you say so, Lord Rowan."
            "The man was not convinced, but this reassurance was all he would get. Rowan couldn’t bend to petty complaints. Doing so would cascade into an avalanche of pretensions he’d never dig himself out of."
        else:
            show rowan necklace angry at midleft with dissolve
            ro "What a load of crap."
            merc "… Lord Rowan?"
            ro "All of you are renegades to your home nations. Don’t pretend pledging yourself to castle Bloodmeen was some heroic self-sacrifice on your part."
            ro "You will get your just reward – when the time is right. And no sooner."
            ro "Now, need I tell what will happen if I hear you spreading dissent again?"
            merc "I-"
            merc "No, Lord Rowan. And please, forgive me from speaking out of place."
            ro "I will. This one time."
            #permantly lower morale by 2 (to do)
            $ castle.morale -= 5
        hide orc soldier with moveoutright
        "With the mercenary dealt with, his ruling would soon become law. He only needed to inform Cla-Min to select one of her more sensible offsprings to head for Cheshire Burrows. She will certainly be happy with his decision."
        "Even if the orcs weren’t."
        #permantly lower morale by 5 (to do)
        $ castle.morale -= 10
        #increase weekly income a little (to do)
        $ castle.treasury += 100
        $ change_relation('cla_min', 10)
        return

    "Let them fight." if society_type == "might":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with moveoutleft
        show orc soldier neutral at midright with dissolve
        ro "A simple problem, I suppose. And the solution to it is also simple."
        ro "You."
        merc "Yes, Lord Rowan?"
        ro "You claim to be more competent, and that you will be able to take better care of Cheshire Burrows. Are you willing to back your words with steel?"
        "The man hesitated for a moment, then nodded his head. Rowan never had a high opinion of the mercenaries under their employment, but they certainly were not afraid to fight for what they thought belonged to them."
        ro "Well then, get to it. I don’t have all day."
        hide orc soldier with moveoutright
        "Rowan pointed to two columns on the opposite sides the throne room, ordering the men to prepare themselves. Both came armed. Perhaps they anticipated things would turn out this way. This was the order of things in castle Bloodmeen, after all."
        "“Might makes right”."
        "They took their respective position and brandished their weapons. The mercenary wielded a short sword and a round wooden shield, and dressed in light, leather armor. The orc was similarly clad, but carried a massive, two handed axe in his hands."
        ro "Begin!"
        if castle.morale > 80:
            "The ensuing battle was a quick one. The orc charged the Human mercenary, swinging his axe in a vertical arc. A predictable attack, and the mercenary had no trouble dodging it."
            "Or the next one. And the one after that. And, to give him credit, the several that followed next."  
            "But the orc warrior was relentless, fighting with ferocity Rowan was well used by now. It did not take long for the man to tire himself, and then – for him to start making mistakes."
            show bg6 with sshake
            merc "Aaaarg!"
            "The tip of the orc’s axe brushed against his arm and the man stumbled."
            show bg6 with redflash
            "Then his head flew across the room, separated from his body. He didn’t even get to scream in horror again."
            show orc soldier neutral at midright with dissolve
            ro "This settles things then."
            ro "Make sure Cheshire Burrows meets the weekly quota. Understood?"
            os "Yes, Masta’ Rowan."
            $ castle.morale += 10
            return
        else:
            "The ensuing battle ended up dragging on, much to Rowan’s annoyance."
            "The orc charged the Human mercenary, swinging his axe in a vertical arc. A predictable attack, and the mercenary had no trouble dodging it. Or the one that came after. And the one after that one."
            merc "Is this your best shot? I knew nuns who used the hoe better than you are swinging that axe!"
            os "SHUT UP!"
            "Infuriated by the man’s words and his inability to hit him, the orc quickly lost patience. He started to swing his axe more erratically, with far too much force than necessary."
            "The man was tiring him out, waiting for the orc to make a mistake. If he was not blinded by fury, then perhaps the green warrior would figure out what was happening. Or perhaps not."
            "Regardless, several minutes later, the orc finally exposed himself, and the mercenary quickly pushed his sword into his heart, killing him on the spot. A rather anticlimactic ending, but one Rowan welcomed with open arms. He had other responsibilities to attend to."
            ro "Well, that settles it."
            ro "Cheshire Burrows is now yours to oversee. Keep in mind, your payment will be determined on how it performs."
            merc "You will not be disappointed in me, Master Rowan."
            ro "Pray I am not."        
            #increase weekly income a little (to do)
            $ castle.treasury += 100
            return

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

label bathing_andras:

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve
show andras happy behind bg14

al "(How troublesome…)"

if all_actors['alexia'].job_state.job == 'maid':
    "Her shift was already over, but before she could head back to her room, one of the head maids caught her, and asked for a small favor."
    "Jezera suddenly decided she wants an impromptu party on the morrow, they needed more maids working the kitchen. Alexia would take the early shift in the morning, but before that, she had to call back some of the maids currently cleaning the arena. "

elif all_actors['alexia'].job_state.job == 'research_assistant':
    "Her shift was already over, but before she could head back to her room, one of Cliohna’s apprentices asked her to go to the arena to remind a colleague of theirs that as much as they all loved sweaty, muscular, half-naked orcs-"
    "-a turn of phrase Alexia found oddly specific, especially coming from a scrawny bespectacled teenager-"
    "-somebody had to transcript the “Ancient Theurgs and why they failed”, before the old tome turns to dust and that it fell to him, as he was the one who drew the short stick last week."
    
elif all_actors['alexia'].job_state.job == 'barmaid':
    "Her shift was already over, but as a messenger from the castle informed Indarah, the arena was all out of wine, and something had to be done about it."
    "Usually, it would be up to Cla-Min to provide the necessary supplies, with the industrious goblin apparently being busy elsewhere, it fell to the tavern mistress to share some of their stock, and for Alexia to make the delivery."

elif all_actors['alexia'].job_state.job == 'breeding':
    "Her shift was already over, but Draith wanted her to make a short trip to the Arena before she could retire for the evening."
    "He wanted her to ask its master if the Arena could accommodate a particularly nasty creature he read about a few days ago, which apparently was capable of easily traversing even oil covered walls."
    "The overseer’s response was, quote: “We’ll need more spikes”, unquote."
    "If Rowan was around, he’d probably lambast them for trying to solve all their logistic problems with spikes. Alexia, on the other hand, chose to keep her mouth shut. She didn’t approve of the place anyway."

else:
    "Her shift was already over, but before she could head home, Greyhide politely asked her to do one last thing for him that day – deliver some swords to the castle gladiators, and tell tomorrow what their opinion on them was."
    "Apparently, they didn’t have enough spikes."
    al "(Go figure…)"


"Her task now finished, she was free to rest for the evening."
"But as she went out of the arena inner chambers, and passed the stairs that led to the audience lodge, she heard sounds of battle, and with it, a very familiar voice."

an "Hahaha, is that all you got, you sissies?! Hit me with all you got!!!"

"Looked like Andras was having fun…"

menu:
    "Check what’s going on.":
        $ released_fix_rollback()
        pass
        
    "Avoid him like the plague that he is.":
        $ released_fix_rollback()
        hide alexia with moveoutleft
        "Alexia paid no attention to the demon, and continued on her way, Andras' shouting accompanying her for some distance."
        scene black with fade
        show andras smirk behind black
        an "Come on, keep trying! You have to draw blood on me…"
        return
        
"Checking on the twins’ activities was one of the primary ways she could be of assistance to Rowan. After a brief consideration, she headed up the stairs, to see what the red demon was up to."

hide alexia with moveoutleft

scene bg28 with fade
show andras happy at center with dissolve
show orc soldier neutral at edgeleft with dissolve
show wild orc neutral at edgeright with dissolve

an "Come on, keep trying! You have yet to draw blood on me, chief Razzak!"

"Surrounded by orcs on all side, Andras spread his arms open, inviting them to attack him."
"Alexia wasn’t exactly familiar with the forces that made the twin’s army, but the blue tattoos on their backs – some odd bird creature, of sorts? -  were unknown to her, and the poor quality of their equipment hinted they were fresh recruits."

an "Or should I call you chief “Chickensquawk”?"

show andras angry at center with dissolve

if society_type == "feudalism":
    an "I think the name will be quite fitting, once I feed you your own testicles for thinking you can demand that I-"
    an "EMPEROR OF CASTLE BLOODMEEN AND THE RIGHTFUL HEIR TO THE DEMON LORD KARNAS!"
    an "-should prove myself to YOU. "
    
else:
    an "I think the name will be quite fitting, once I feed you your own testicles for thinking you can demand that I should prove myself to YOU."
    
show andras happy at center with dissolve

"The orcs growled in fury, though even at a distance, Alexia could see their confidence crumble. At least one orc was checking the blade of his axe in disbelief, shaking it angrily. Was it not able to harm the half-demon?"

wo "You no demon boss. Who you fatha was means nuthin’"

"The chief tried to keep the morale of his men up, but what little he gained with that speech, Andras erased in an instant. He let out a roaring laugh, that carried across the arena."

an "Oh, you poor fool. Who my father was means everything."
an "For example, it allows me to do… THIS!"

show bg28 with sshake
show bg28 with redflash
show alexia 2 necklace shocked behind bg28

al "! ! !"

show bg28 with redflash

"She barely saw him move. One moment he was standing at the center of the arena. Another, he was right in front of the orc warchief, his hand buried deep into the orc’s chest."

an "I’m glad to know your heart beats for our cause."

"With a single motion, he tore his hand out-"

show bg28 with redflash

"Holding the orc’s heart in it."

an "And that you are willing to give up so much for us."

"Nobody dared to move. For a brief moment, the orc chieftain stared at his still beating heart, until reality caught up to him."
"He fell to the ground, dead."

hide wild orc with redflash

an "WHO DO YOU SERVE!"

orcs "ANDRAS! ANDRAS! ANDRAS! ANDRAS! ANDRAS!"

"Alexia watched as Andras raised the chieftain’s heart high, proof of his profess. The dozen orcs that made the now fallen tribe already forgot about their old leader, and now chanted the demon’s name in fervor."

al "(How quickly they accepted him…)"
al "! ! !"

show bg28 with redflash

"Unexpectedly, Andras crushed the heart in his hand, showering himself and the surrounding orcs in blood. Alexia felt a wave of nausea take her, while the orcs – only screamed louder in ecstasy…"   

scene bg29 with fade
show alexia 2 necklace shocked at center with dissolve

al "(Disgusting…) "

show andras smirk behind bg29

an "Have you enjoyed the show, Alexia?"

hide andras
show andras happy at edgeright with moveinright
show alexia 2 necklace concerned at center with dissolve

"She saw his hands gripping the edge in front of her. Easily seizing the arena wall, Andras pulled himself up in front of her."

show alexia 2 necklace concerned at midleft with moveoutleft

"He smelled of blood. She could see it – just barely – on the ferocious red of his skin."

an "So?"

al "It was a bit… Graphic?"

an "Hah! Women and their delicate sensibilities…"

show alexia 2 necklace concerned at edgeleft with moveoutleft
show andras happy at midright with moveinright

"He took a step forward. Instinctively she backed away from him, and immediately she realized it was something she should never have done."

show alexia 2 necklace neutral at edgeleft with dissolve
show andras smirk at midright with dissolve

an "Really, Alexia? A little bit of blood and gore and you’re already fainting? No… That won’t do."

show alexia 2 necklace concerned at edgeleft with dissolve

al "Fainting? I feel fine, it’s just-"

an "No, no, you obviously aren’t. And you have my apologies for that!"

show alexia 2 necklace shocked at edgeleft with dissolve

"He spread his arms wide again, presenting himself in all his bloodied glory to the woman."

show andras smirk at center with moveinright

an "You’re our esteemed guest! I should present myself properly."

show andras smirk at midleft with moveinright

an "After all, I wouldn’t want anyone to feel uncomfortable in my company."
an "Come, help me make myself presentable to everyone."

"He pointed with his head to the side, the devious smirk never leaving his lips. Racking her brain, Alexia tried to unravel the meaning behind his words."
"Finally, she realized he was pointing in the direction of the castle baths. Had to make himself presentable…"

$ bath_refuse = 0

menu:
    "Follow him into the baths. His request is innocent enough.":
        $ released_fix_rollback()
        show alexia 2 necklace neutral at edgeleft with dissolve
        show andras happy at midleft with dissolve
        $ change_actor_num_flag('alexia', 'andras_influence', 1)
        al "… If you need my help cleaning yourself, then I suppose I can be of assistance."
        an "Of course."
        scene black with fade
        show andras happy behind black
        an "You know I would never ask you to do anything you wouldn’t want to…"
        jump bathTime
        
    "He’s scheming something. Try to make up an excuse.":
        $ released_fix_rollback()
        $ bath_refuse += 1
        show alexia 2 necklace neutral at edgeleft with dissolve
        al "Lord Andras, I remain at your disposal, but it is getting late, and I-"
        show andras displeased at midleft with dissolve
        an "Alexia."
        show alexia 2 necklace concerned at edgeleft with dissolve
        show andras happy at midleft with dissolve
        an "I’m in a good mood."
        show andras angry at midleft with dissolve
        an "You do not want to ruin it."
        menu:
            "Reluctantly agree.":
                $ released_fix_rollback()
                show alexia 2 necklace neutral at edgeleft with dissolve
                show andras happy at midleft with dissolve
                al "… I guess I can spare an hour."
                an "Excellent."
                show alexia 2 necklace neutral at midleft with moveinleft
                show andras happy at edgeleft with moveoutleft
                an "Now follow me! And smile, we just gained a new tribe of orcs!"
                scene black with fade
                show andras happy behind black
                an "Aren’t you happy to be a part of all of this?"
                jump bathTime
                
            "Refuse.":
                $ released_fix_rollback()
                show alexia 2 necklace neutral at edgeleft with dissolve
                show andras happy at midleft with dissolve
                al "… No, I do not."
                show andras angry at midleft with dissolve
                al "But neither do I want to neglect my castle responsibilities, and tomorrow I have a long day ahead of me."
                al "I’m afraid I will have to ask to be exempt from bath duty, so I can focus on what Rowan, my husband and your faithful servant, asked me to do."
                "The joyous atmosphere that filled the arena a minute ago was now nowhere to be found. She watched, sweating, as Andras performed his usual emotional journey at being denied."
                "First, utter disbelief. Then, furious anger. And finally – cold hatred."
                an "Very well, continue on then."
                an "But you would be wise to reevaluate your priorities in the future."
                an "Or else I’ll find a way to remind you of them myself."
                "The unsubtle threat was left unspoken, but despite the rising panic, she held firm."
                if alexiaOffer == True:
                    "Perhaps it was foolish of her to make a stand here, after her husband openly said they will have to do some unsavory things to survive, but she couldn’t just let Andras do whatever he wanted with her." 
                    "She had to take a stand somewhere."
                else:
                    "She couldn’t allow Andras to do as he pleased with her. She had to take a stand somewhere. Anywhere."
                al "I will keep that in mind, Lord Andras. And now, if you excuse me, I bid you farewell."
                hide alexia with moveoutleft
                "Feeling his eyes drilling a hole in her skull, she bowed before her tormentor and quickly left the lodge."
                $ andrasPunishmentCounter += 2
                return
                
label bathTime:

#baths BG 
scene black with fade

"The castle baths ran underneath the castle, fueled by underground hot waters. From what Alexia learned from the castle gossip, they were built by some early Demon Lord, to accommodate for his taste in nymphs and mermaids." 
"The baths themselves had one single, massive pool in the middle of it, usually used by the servants, and a series of smaller chambers, with smaller baths in them, often referred to as “fuck rooms”, for obvious reasons."

show alexia 2 necklace neutral at midleft with dissolve
show andras happy at center with dissolve

an "You there! Prepare a chamber for us, and get the water ready."

"Two servants quickly hurried to get one of those ready. The fact that for all his earlier monologuing about Alexia helping him bathe, it was not her he sent to do this, was already raising red flags."

al "The main hall would be quicker."

an "I’m in no hurry."

al "Are you sure you don’t want to use your usual servants?"

show andras displeased at center with dissolve

an "And where would be fun in that?"

show andras happy at center with dissolve

if alexiaAndrasSex > 0:
    show alexia 2 necklace aroused at midleft with dissolve
    an "You should understand by now, that trying new things can be… Exhilarating."

else:
    an "It’s good to try something new every once in a while."
    show alexia 2 necklace angry at midleft with dissolve
    al "{b}Someone{/b} new."

show alexia 2 necklace neutral at midleft with dissolve
hide andras with moveoutright
hide alexia with moveoutright

"Luckily for her, the servants didn’t want to be a target of Andras’ wrath either and they quickly completed their preparations. The red demon went in first, then urged her to follow."

show alexia 2 necklace neutral at midleft with dissolve
show andras happy at midright with dissolve

"Their room was fairly simple one. A large bathtub was built into the floor on the center of it. It was slightly elevated, with two sets of stone circles surrounding it, doubling as short stairs."
"A nearby shelf held all the required soaps, sponges and herbs, everything anybody might need for a pleasant bathing experience. Nearby walls were decorated with faded frescos of various sea creatures, some in very obscene poses."
"Never one to be abashed by Alexia’s company – or anyone’s as far as she was concerned - Andras wasted no time discarding his loincloth."

if all_actors['alexia'].flags['andras_influence'] > 5:
    show alexia 2 necklace aroused at midleft with dissolve
    "She found herself quickly stealing a glance at what was between his legs. Even when not erect, his massive cock intimidated her with its length. To think she found a man even larger than her husband-"
    "Her thoughts started going in a weird direction. She lambasted herself for such lack of self-control and looked away."   
    al "(Damn it Alexia… Get your head out of the gutter.)"
    show alexia 2 necklace neutral at midleft with dissolve

else:
    "She turned her head away. As always, Andras had no sense of propriety."

"From the corner of her eye, she saw him crack his neck, then slowly flex his impressive muscles. An obvious show, no doubt for her to feast her eyes."

hide andras with moveoutright

"She said nothing of it, and after a moment, much to her relief, she noticed him lowering himself into the bath."

show alexia 2 necklace neutral at center with dissolve

if all_actors['alexia'].flags['andras_influence'] > 5:
    "Quickly, she grabbed the prepared bucket of hot water, as well as one of the sponges, and hurried to her captor."

else:
    "His back was now turned to her, open and defenseless. She looked over the nearby shelves foolishly hoping to find a dagger, or perhaps something sharp, a spike maybe…"
    "She knew she would not dare to raise a hand against him, and yet she could not stop herself from indulging in this little act of mental rebellion. A part of her still longed for an opportunity to bite back against her tormentors, no matter the consequences."
    "But the shelves hid nothing of any use. No weapon, nor metal tool. Stifling a frustrated sigh, she grabbed the prepared bucket of hot water, as well as one of the sponges, and hurried to the red demon."

hide alexia with moveoutright

#blurred bath BG
scene black with fade

if all_actors['alexia'].flags['andras_influence'] > 5 or all_actors['alexia'].corruption > 30:
    "Slowly, she started washing his body of all the blood, dirt and sweat."
    "The servants from earlier filled the bath with relaxing herbs, and thanks to them, the chamber was now filled with a pleasant, calming scent. The thick walls separated them both from the usual insanity of castle Bloodmeen, drowning out the shouts of orcs and screams of prisoners."
    "Despite herself, she found herself relaxing a little, slowly moving her hand across his body. The sponge in her fingers slowly traversed across his skin, cleaning his tattooed, powerful torso."
    "Her eyes fell to the odd markings that covered his whole upper body. What did they mean…?"
    if all_actors['alexia'].flags['andras_influence'] > 5 and all_actors['alexia'].corruption > 30: 
        "She trailed a single finger across the dark lines, unable to contain her fascination with them. She marveled at the intricate, seemingly chaotic lines."
        "… And she marveled at the rock-hard muscles she felt beneath her fingers, though that she dared not to admit, even to herself."
    else:
        "But she dared not to touch his skin, nor to ask about them."
        
else:
    "Slowly, she washed his body of all the blood, dirt and sweat, being extra careful to do it as mechanically as possible."
    "Between the heavy, pleasant air in the room, and the silence that accompanied them, it would be easy to relax, to drop her guard. But she could not forget who she had before her eyes. What this man was responsible for."

#bath BG
scene black with fade
show andras happy behind black

an "This would be a lot easier if you entered the bath with me."

if all_actors['alexia'].flags['andras_influence'] > 5 or all_actors['alexia'].corruption > 30:
    show alexia 2 necklace aroused behind black
    al "A-ah…"
    al " I… I don’t think that’s how baths work, Lord Andras."
    show alexia 2 necklace neutral behind black

else:
    show alexia 2 necklace aroused behind black
    al "I don’t think that’s how baths work, Lord Andras."
    show alexia 2 necklace neutral behind black

if bath_refuse > 0:
    "He showed his teeth in a predatory smile, this time more amused than angered by her defiance."

else:
    "He showed his teeth in a predatory smile, amused by her defiance. "

an "Then at least take off your dress. It’ll get dirty otherwise."

al "I need to have it washed anyway. It’s been a long day."

an "Ah yes, you’ve been busy with work. I understand. I understand all too well!"

"He raised his voice, magnanimously “forgiving” her."
"…He was being far too understanding now. It wasn’t like him not to pressure her.  "

an "Conquering the world is hard work. All the pillaging, and murdering…"

"-His fingers briefly brushed against her cheek-"

an "-And raping…"

if all_actors['alexia'].corruption < 30:
    al "(Disgusting…)"

an "Occupies me and my orcs heavily. But I am lucky today."
an "I feared I would have to take a break, wait for our forces to replenish. Lost some of my orcs a week ago, and it takes time to attract new ones."
an "But thanks to Warchief Chickensquawk, I will be able to return to the field tomorrow! Isn’t it wonderful, my dear Alexia?"

"His pleasant demeanor was rising all the red flags. He was up to something…"

al "I thought Rowan was handling our forces?"

an "Most of them, yes. But do you think all I do is languish in my chambers, surrounded by women?"

if castle.villages > 1 or castle.buildings['dungeon'].prisoners > 4:
    an "Your husband is doing a commendable job ensuring we have a steady supply of slaves, but as it happens I found a most scenic little village last week, ripe and ready for harvest."

else:
    "Since your husband doesn’t have the balls to raid human settlements, it falls to me to pick up the slack. And as it happens, I found a most scenic little village last week, ripe and ready for harvest."
    
an "And just cannot wait to sack it-"

show alexia 2 necklace shocked behind black

al "! ! !"

an "-Enslave everybody there, then burn it to the ground!"

scene black with fade
show alexia 2 necklace concerned behind black

al "…"

scene bg4 with fade

"…"
"… …"
"… … …"

scene black with fade
show alexia 2 necklace concerned behind black

al "… What would it take?"


#baths CG
scene black with fade
show andras happy behind black
show alexia 2 necklace neutral behind black

an "Oh? Excuse me? You must speak louder woman."

"Her hand still traveled across his body, across his bloodied torso. The water took a soft, red tint to it."

if all_actors['alexia'].flags['andras_influence'] < 5:
    "As always, Andras tainted everything he touched."

al "What would it take for you to assign these orcs to Rowan?"
al "He’s your general, is he not? I believe he could use the fresh recruits."

an "That much is true…"

"She watched him stroke his cheek, as if in deep thought. Pretending to hesitate… As if they both didn’t know what all of this was coming to…"

an "But if I did give away these orcs, what would I be doing the entire week? "

"He leaned in, gently cupping her chin."

an "You?"

al "I..."

if all_actors['alexia'].flags['andras_influence'] > 5:
    "Unwanted images of their past liaisons assaulted her imagination, and she it took every ounce of her self-control not to turn crimson from embarrassment. If that was what it would take…"
    
elif all_actors['alexia'].flags['andras_influence'] > 3:
    "Unwanted images assaulted her imagination. All the time, he kept pressuring her into breaking her marital vows…"
    "Was she to break them here?"

"But unexpectedly, he waved his hand dismissively and shook his head."

an "No, no… that would be unreasonable. You do have your own duties after all."
an " But now that you mention it… Maybe I should consult with Rowan first… He might indeed have more use of them… Assuming he is as “thorough” in his duties as you are…"

"He spread his legs open, drawing her attention to the familiar phallic shape that lurked beneath the surface"

an "If I knew both of you are willing to go beyond of what is expected… Then perhaps I wouldn’t mind trusting him with today’s tribe."

if all_actors['alexia'].corruption < 30:
    "She turned her gaze away, fighting a grimace. A seed of doubt blossomed in her heart at the thought of what he was asking her to do." 
    "But could she afford to be squeamish? When lives were at risks?"
    
menu:
    "Give him the full service.":
        $ released_fix_rollback()
        jump bathsFullService
        
    "Refuse. She will not debase herself before him – people of Rosaria be damned." if all_actors['alexia'].corruption > 30:
        $ released_fix_rollback()
        "She eyed Andras’ disgusting dick with repulsion. The events of Arthdale still haunted her, but-"
        "… But to hell with this! Washing her captor was humiliating enough, she didn’t have to go out of her way to-"
        "To do what, exactly? Look for excuses to cheat on her husband? It wasn’t her responsibility to look after the people of Rosaria. Neither was it her husband’s. If the lords did their job properly, none of this would be happening."
        "Her responsibility was to stay loyal to Rowan. No more, no less."
        jump bathsRefuse
        
    "Refuse. She will not bend to his will." if all_actors['alexia'].corruption < 31:
        $ released_fix_rollback()
        "She swallowed heavily. There was no guarantee Andras would really grant Rowan these orcs. Or that he wouldn’t resume raiding the week afterwards."
        "Regardless of what happened in Arthdale… She shouldn’t be treating her fidelity like something to be traded away. Even for the lives of others."
        jump bathsRefuse

        
label bathsFullService:

"She didn’t say a word, but behavior signaled her submission. She repositioned herself a bit, laid down, so her hand would be able to reach further – further down, under the water, and between his legs…"   
"And it was all Andras needed to see."

an "Ah… Aren’t you the perfect companion? Setting such a sterling example for your husband!"

if all_actors['alexia'].flags['andras_influence'] > 5: 
    al "Please… Don’t talk about Rowan anymore…"
    "Her hand traveled south, and with every inch, his grin grew wider. She tried her best to hide her embarrassment, but failed to do so."
    
else:
    "Her hand traveled south, and with every inch, his grin grew wider. This was what she despised most about him – the pleasure he took from bending her to his will. What a despicable man…"
    al "(I am doing this for the people of Rosaria… And only for them.)"

an "You know we could’ve skipped all of that, right? If you joined me in the bath from the start… I would’ve agreed to your request without thinking twice!"

if all_actors['alexia'].flags['andras_influence'] > 5: 
    al "..."
    
else:
    al "(Keep dreaming you bastard…)"
    
"Finally, her hand reached his nether regions. Slowly, hesitantly, the sponge in her fingers brushed against his erect tool…"

if all_actors['alexia'].flags['andras_influence'] > 5: 
    al " (So big…)"

else:
    al "(Remember why you’re doing it…)"


scene black with fade
show alexia 2 necklace shocked behind black

al "! ! !"

"Andras pushed himself up suddenly, and sat at the edge of the bath. His erect phallus, previously under the water, now stood proudly right in front of her eyes."

#handjob CG
scene cg307 with fade
show andras smirk behind cg307
show alexia 2 necklace neutral behind cg307
pause 3

an "To make it easier for you."

if all_actors['alexia'].flags['andras_influence'] > 5:
    al "O-of course…"

else:
    "She bit back a snarky remark. Bastard…"

an "And ditch the sponge."

"She took a careful glance at his face, trying to judge how much of a request it was. She saw his eyes narrow. An order, then."

if all_actors['alexia'].corruption > 30:
    "She did as he told, and faced the cock in front of her, her hand on his thighs. She tried not to marvel at its size, but failed horribly."
    "To think Andras always concealed this monster with only a skimpy loincloth… How did it not show constantly…"     
    "… Maybe it did?"
    "Maybe if she started paying attention, she’d be seeing it more often. See its shape press against the material, catch a glimpse of its enlarged head peeking from behind the cloth…"

else:
    "She did as he told, and faced the cock in front of her, her hand on his thighs. She tried not to think about how much bigger it was than her husband’s. Some women would welcome having a man like Andras shower them with such attention."
    "Foolish women, that is."

an "Come on slut, hurry up."

if all_actors['alexia'].flags['andras_influence'] > 5:
    al "Y-yes… I apologize…"

else:
    al "..."
    
"She wrapped her fingers around his shaft. It was still wet. Slippery. Her hand slid down with ease, then moved up, the entire length. Again, and again."

an "That’s right… Clean it real thorough…"

if all_actors['alexia'].flags['andras_influence'] > 5:
    al "A-ah… Yes…"
    "Aiming to please, she didn’t hurry things along. She wanted him satisfied, since only then would he look favorably at her request. This hard, erect phallus in her hand was the key to so many things…"
    "She had to get used to it. She started working in the castle to take some weight off Rowan’s shoulders. But this… This way she could also be of use to him…"
    "By stroking Andras’ cock… By working her hand along it, she was also helping her husband. This also… Was something she did for Rowan…"

else:
    al "(Think about the people of Rosaria Alexia… Be strong.)"
    "She tried to be mechanical. Tried not to act overly sexual. It was difficult, when one had a dick in their hand…"
    "She knew she needed him satisfied. She needed him happy, so that he would look favorably at her request. But she couldn’t force herself to put her heart into it. This was wrong. All of this was wrong."
    "Stroking Andras’ cock… Feeling its warm, hard flesh… It didn’t feel right."  
    "And she hoped it would always stay this way."

an "Don’t forget the tip."

"She gently pulled back the foreskin…"

an "And use your tongue, slut."

if all_actors['alexia'].flags['andras_influence'] > 5:
    "Without thinking, she caught herself opening her mouth, leaning in to fulfill Andras’ demands…"
    scene black with fade
    show andras displeased behind black
    "She turned her head away quickly."
    "This was going too far. Lives were on the line, but readily following his orders like that… "
    an "Hmm… Fine, I’ll give you a pass this one time…"
    "She felt him touch her cheek. He forced her to turn her head again, to again face the cock in front of her."
    an "But look at my dick as you clean it. Marvel at it."
    "She was doing this for Rowan. For the people of Rosaria. It would be unwise to antagonize him further… So she did as ordered."
    #bath handjob cg
    scene cg307 with fade
    show andras smirk behind cg307
    show alexia 2 necklace neutral behind cg307
    pause 1
    "Again, Andras massive phallus taunted her, its erect form dominating her field of view. From the corner of her eyes, she saw Andras face, as always in situations such as these – smiling triumphantly..."
    
else:
    al "Stop calling me-ack!"
    scene black with fade
    show andras angry at center with dissolve
    "He seized her by the face, his grip – iron. He forced her to look up into his eyes, to see the anger kindling in them."
    an "I will call you whatever I want, and if you don’t want to use your tongue, then I would advise you to at the very least watch it."
    an "Remember what’s on the line here. And that it was you who wanted it."
    scene black with fade
    "Her heart skipped a beat. Always – always, the very moment she forgets her place, Andras was there to remind her of it. He would always find some way to make her to his bidding…"
    "… At least as long as he was cruel, she didn’t have to worry she would ever grow accustomed to servicing him… She hoped."
    #blurred bg
    scene black with fade
    show andras displeased behind black
    show alexia 2 necklace neutral behind black
    al "… I apologize, Lord Andras."
    an "Hmph. Let it be the last time, slut."
    #bath handjob cg
    scene cg307 with fade
    show andras smirk behind cg307
    show alexia 2 necklace neutral behind cg307
    pause 1
    "He released her, and again, she found herself staring at his massive phallus, its erect form dominating her view."
    al "(Let’s just get this over with…)"

"For the next several minutes, her hand caressed his cock, guided by his commands."

an "Touch it more firmly. Worship it."

al "Yes, Lord Andras."

"His cock was warm, throbbing. Eager for more than just her fingers. Quickly, she saw white droplets at the tip of it, a familiar scent reaching her nostrils."

if all_actors['alexia'].flags['andras_influence'] > 5:
    "And with it, a familiar warmth started spreading from between her legs."
    al "(Why does he make me feel like this…?)"
    "When did her feelings start being so bungled up? When did she stop feeling only pure revulsion for this man?"
    "She couldn’t tell. All she knew, was that no matter what these feelings were, she had to bury them deep inside, lest one day she starts acting on them…"

else:
    "She fought back her revulsion. As time went by, she started feeling… Numb. She stopped thinking about what she was doing. About what her hand was doing."
    "Frankly, it could’ve been anybody’s hand. Anybody could be stroking Andras’ right now dick. Her hand doing it… It didn’t mean anything. None of this meant anything…"
    al "(I’m doing this for Rowan… I’m doing this for Rowan… And for the people of Rosaria…)"
    
an "And don’t forget about what’s under."

al "Yes, Lord Andras."

"Her hand reached down, closing around his balls. Feeling their weight. Their warmth."

an "You’re going to clean their insides as well. Understood, slut?"

al "… Yes, Lord Andras."

an "Good, then keep going. And don’t you dare to move your face away."

al "Yes, Lord Andras."

"She saw it coming. She felt his balls churn, saw his cock stiffen, saw him thrust his hips. She hurried her hand, and soon-"

an "Nn-Aaah!"

show cg307 with sshake
show cg307 with sshake
scene cg308 with flash
pause 3

"A stream of white hit her face, his thick cum spraying her. Her eyes, her mouth, her hair – all of it, covered in his seed."

an "Now that’s a pretty picture~"

"Shameful. How horribly shameful all of this was… Covered in white, sticky cum, of a man other than her husband…"

if all_actors['alexia'].corruption > 30:
    "Guess that’s just how things would be from now on…"

else:
    al "(I’m sorry Rowan…)"
    
"She felt his fingers on her skin - caressing her face, spreading the cum across her cheeks, across her lips.  She looked up, and again, saw this mocking grin of his, these laughing eyes…"

an "Ah… How sloppy of me… I got my hand dirty."

"He held his fingers in front of her, now dripping with semen. Her heart sunk, as she heard the words:"

an "Clean them. Thoroughly."
an "And use your tongue, slut."

menu:
    "Do it.":
        $ released_fix_rollback()
        "She was this close… No point in playing rebellious now…"
        al "Mm-m! Mmm…"
        "Averting her gaze – she didn’t want to see his expression as she debased herself further – she lolled out her tongue, and obediently started sucking, licking the sperm off his fingers."
        "She was painfully aware her own face was still coated in his seed. She felt its warmth, felt it slowly trickle down her chin, while her tongue prevented the same from happening to the cum on her tormentor’s fingers."
        "With the tip of her tongue, she scooped up every drop. Every salty, white drop…"
        if all_actors['alexia'].corruption > 30:
            al "(Doesn’t taste… That bad…)"
        else:
            al "(Disgusting…)"
        "Finally, when his hand was clean, and her mouth fully, she made a loud, gulping sounds, knowing it would please him."
        if all_actors['alexia'].corruption < 31:
            "She didn’t want to do that either, but she went so far already…"
        an "Good… Good…"
        
    "Try to refuse.":
        $ released_fix_rollback()
        al "(…)"
        "She already allowed herself to be debased so much… Maybe it was idiotic of her to rebel now, potentially undoing all of her work, but she had to try."
        "Rather than lean in, she slowly reached for the cloth, and started to bring it closer to his fingers."
        "She could see it in his eyes, on his face – the metaphorical coin flip. What will it be this time? Outrage, or amusement?"
        an "Ha ha ha… Still trying to be modest? With all that cum on your face? Oh, you dumb, deluded slut…"
        "She breathed a sigh of relief, and started cleaning his fingers. Safe…"
        al "You’re clean… Are you not?"
        an "The same can’t be said about you…"
        an "I told you to strip, did I not?"
        al "..."
        
"His hand reached for her hair, and firmly pushed her down – making her face reflect on the surface of the water."

#baths BG
scene black with fade
show alexia 2 necklace aroused at center with dissolve

"Making her look at her cum stained, embarrassed expression…"

show andras smirk at midright with dissolve

an "Exemplary service Alexia.  I’ll inform Rowan he will be receiving additional orcs this week."
an "I hope you’re proud of yourself, haha!"

hide andras with moveoutright

"His laughter was the last thing she heard from him."
"She only hoped it was all worth it…"
$ castle.buildings['barracks'].troops += 10
$ change_actor_num_flag('alexia', 'andras_influence', 3)
$ change_corruption_actor('alexia', +5)
$ andrasBathHandjob = True
return


label bathsRefuse:

al "… I think this part you can handle yourself."

an "Are you certain? The village-"

al "I’m certain."

"She cut him off midway, voice cold. In an instant, her disobedience was answered with a furious scowl. Andras lifted himself out of the bath abruptly, splashing her with the bloodstained water."

#baths CG
scene black with fade
show alexia 2 necklace neutral at midleft with dissolve
show andras displeased at midright with dissolve

an "Have it your fucking way then."
an "I will take great pleasure raping every single woman living in that fucking village."
an "I hope you’ll be sleeping comfortably today knowing this."

show alexia 2 necklace concerned at midleft with dissolve

al "…"

show andras angry at midright with dissolve

an "What are you standing here for? We’re fucking finished. Get out you dumb slut."

"She bowed deeply, and hastily left the chamber.  "

hide alexia with moveoutleft
show andras angry at center with moveinright

an "What a fucking waste of time…"

$ andrasPunishmentCounter += 1    
$ andrasBathHandjob = False
return
