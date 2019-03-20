init python:

    #Corrupted Abbey - Dazzanath
    #Requirement: Dark sanctum
    event('corrupted_abbey_dazzanath', triggers='map_res_19', conditions=('castle.buildings["sanctum"].lvl > 0', 'castle.buildings["brothel"].lvl > 0',),
        group='map_res_abbey', run_count=1, priority=pr_map_res)
    #dazzanath arrives event
    #//Quick message after 4 weeks when Dazzanath arrives at the castle. Occurs at end of week, in addition to any other events.
    event('dazzanath_arrives', triggers="week_end", active=False, group='ruler_event', run_count=1, priority=pr_ruler_high)


label corrupted_abbey_dazzanath:
#Corrupted Abbey - Dazzanath
#Requirement: Dark sanctum

scene black with fade
show rowan necklace neutral behind black

#if corruption is higher than 49
if avatar.corruption > 49:
    "Usually, Rowan never checked individual Abbeys before ordering his orcs in. It was inefficient, scouting every single location that he would inevitably order to be burned to the ground."
else:
#else
    "Usually, Rowan never checked individual Abbeys before ordering his orcs in."
    "It was easier that way. He didn't want to see the faces of people that would soon die or be enslaved by his orders."

#rejoin
"But this time, things were different, as the abbey before him laid in an area he was told to pay specific attention to."

show xzaratl neutral at center with dissolve

xz "If you want to, that is. You might find something… Interesting there."

hide xzaratl with dissolve

"Would it be too much to wish that the people he was supposed to be working with would kindly stop being so infuriatingly cryptic half of the time?"
"Probably yes."

#abbey bg
scene black with fade
show rowan necklace neutral behind black

"Regardless, whatever X’zaratl was referring to, Rowan knew it would be unwise to simply ignore her words. That's why this time, after scouting the abbey, he didn't call the castle and instead went to pay the clergy a visit."
"Thus far, he didn't find anything odd about the place. The building itself wasn't any different than all the other temples of Solansia. It was a small, octagonal structure, with large windows on the side of it."
"Rowan approached the main gate and knocked twice. After a short while, a pair of acolytes opened it up and inquired about the nature of his visit."
"He introduced himself, giving his full name but not mentioning his past as the Hero of Karst, and explained he was merely passing by. He told them he wished to pay his respects to Solansia and rest a while before continuing his journey."
"A simple cover, that would serve his needs for the time."
"But the acolytes weren't all too keen on letting him inside, he saw that much from their expressions. They eyed him suspiciously and kept exchanging glances, as if both of them expected the other to come up with an excuse to send the visitor away."
"But they found none, and with some reluctance, led him inside, into the large, also octagonal, hall that made the center of the abbey."
"Rowan looked up at the statue of Solansia and knelt before it to offer a quick prayer. But just as he was about to start, a pleasant voice called out to him."

aga "Rowan Blackwell?"
aga "Is that you?"

"A short, plump nun entered the hall from one of the side rooms. She looked no older than her early forties if Rowan were to judge from the small wrinkles around her mouth."
"She approached him with a kind smile on her lips and a bright sparkle in her eyes, and bowed her head in respect."

#if guilt higher than 49
if avatar.guilt > 49:
    "Rowan returned the greeting with a hollow smile."
else:
#else
    "Rowan returned the greeting with a polite smile."

#rejoin
ro "In the flesh. Have we met?"

$ agathaName = "Reverend Agatha"

aga "Reverend Agatha, the Abbess. And no. Not exactly."
aga "But I saw you once. A long time ago. After the battle of Seeley Fields."

"Her smile turned melancholic and a painful shadow crossed her face."

aga "I was one of the nurses that took care of the wounded. You visited the infirmary, to send off an old friend."

"Rowan grimaced despite himself. He remembered the battle, and what transpired after it."
"Sir Raignald, one of the few nobles who openly expressed his support for Rowan being named General, received a grievous wound on Seely Fields. He died soon after, in his final words begging Rowan to create a world where his daughters could live happily."

#if corruption is higher than 49
if avatar.corruption > 49:
    "Rowan hadn't thought about the old knight for a long time now and was none too pleased with the nun for reminding him of the promises he made that day."
    "But he couldn't reveal just how far he strayed from the path he vowed to follow."
else:
#else
    "Rowan still thought about the old knight from time to time. A joyous fellow, he always bragged about his younger child being the jewel of the realm."
    "If he knew how far had Rowan strayed from the path he once vowed to follow, he would not doubt punch him in the face in an attempt to straighten him up."
    "It wasn't a pleasant thought, but Rowan couldn't help but smile at the memory of his old companion. The realms suffered a great loss when Raignald left them."

#rejoin

ro "Sir Raignald. He was a good man."

aga "So he was. I remember he spoke of his daughters in his final moments. Said he hoped they would one day find a husband as noble as you."

ro "I hope they did."

aga "So do I."

"The nun smiled warmly. The two acolytes were still with them, standing behind Rowan, somewhat uncomfortable with the odd reunion."

aga "But enough reminiscing about the painful past. Rowan Blackwell, Hero of Karst, I cannot express how happy am I to see you here. Solansia has finally answered our prayers."
aga "There is something you must assist us with-"

aco "Reverend Mother, you mustn’t!"

"One of the acolytes suddenly raised his voice in opposition."

aco "This man is not part of the Codifice! He cannot learn of-"

aga '"This man" is one of the six heroes who slew the last Demon Lord. He is more fitting for this task than any of us ever were in the first place!'

"The nun's voice cut the air, silencing the two acolytes with a tone of absolute authority."
"Rowan glanced behind him. While clearly chastised, the men did not seem all that convinced of the idea."

aga "I apologize. They mean well. There are dark forces abound, and trust is hard to come by."
aga "But I know your arrival must be a sign from the Goddess. I am certain of it."

"The nun turned to her two assistants."

aga "Leave us."

"The men hesitated for a moment, then reluctantly obeyed. Agatha smiled at Rowan once more."

aga "It will be easier to simply show you. Come with me."

"Rowan raised an eyebrow and followed the Abbess. Guess he stumbled upon whatever it was X'zaratl was speaking of."
"The two of them headed to the small door at the back of the temple, entering living quarters of the Solansia clergy. Occasionally, they would pass another nun or a priest."
"Judging from the size of it, Rowan estimated the abbey had around a dozen of faithful living in it, including the Abbess."
"Agatha led him to a spiraling staircase, guarded by a young nun."
"Though guarded was perhaps a bit of an overstatement, as the woman did not notice them approach. She stared into the distance with a dazed expression, and only snapped back to reality once the Reverend Mother touched her shoulder."

aga "Get some rest, Sister. I’ll keep watch for now."

"The nun blushed, stammered an apology, and quickly left the two. Agatha opened the door to what Rowan believed was the cellar. As they headed downstairs, the Abbess finally decided to shine some light on the whole mystery."

aga "A month ago, he came to us in our sleep. A demon most vile. He whispered words best left unspoken, and tried to lead us astray with promises of pleasure."
aga "We turned him away, obviously."
aga "But then, a vision came to me. The Goddess herself appeared before me, telling me of the demon that plagued us."
aga "She reminded me of the duty we all took upon ourselves and bestowed unto us a truly holy quest."
aga "You see, by turning the demon away, we only sentence others to be his prey. Rather than protect the people, we chose to protect ourselves."
aga "So instead…We laid a trap..."

"Her voice trailed off. The dramatic pause annoyed the hero, but he decided to wait for her to continue of her own accord and remained silent."
"A moment later, they reached the door. Rowan kept watching the Abbess from the corner of his eyes and noticed her breath growing slightly heavier, and her cheeks somewhat redder."
"The Abbess took out a heavy key and opened the cellar-"
"Instantly, Rowan's sense of smell was assaulted by an overwhelming stench of semen. He covered his nose with his sleeve and peered into the half-dark."
"He saw him, on the other side of the room. The demon. An incubus. He was illuminated by two nearby torches and chained to the wall."
"His head snapped upwards at the sound of the door opening, and he was now glaring at them both furiously, with glowing, pink eyes."

aga "His name is Dazzanath. For over three weeks now, he's been chained here, kept drained by us so he cannot escape his bonds."

"The two approached the incubus. Despite being allegedly trapped underground for nearly a month, he didn't seem all that weakened to Rowan."
"His pink eyes pierced through Rowan with intensity, and the chains rattled worryingly as his powerful arms threatened to break them with brute force alone."
"- but without success so far."
"Furthermore, the demon was surrounded by a circle of runes. While Rowan lacked the expertise to identify them, he believed they sapped his strength, at least partially."
"Finally, Rowan couldn't miss the fact the incubus lower half was exposed for the whole world to see. His dick swayed in front of their eyes, looking painfully erect."
"For some reason, Rowan felt his eyes drift to it of their own accord and he had to focus quite heavily to force them away."
"There was now no doubt this was what  X’zaratl spoke of. And while Rowan already had a pretty good picture of what was going on, there were still some questions he had to ask the Abbess."

$ event_tmp['ask_name'] = False
$ event_tmp['ask_rune_circle'] = False
$ event_tmp['ask_naked'] = False
$ event_tmp['ask_drained'] = False
$ event_tmp['Dazzanath cum dump'] = False
label AgathaMenu:

menu:
    "Ask how she knows his name.":
        $ released_fix_rollback()
        aga "Ah, one of the acolytes mentioned it to me last week. They check on him regularly, and some of them use the opportunity to learn more about him."
        ro "You don’t talk with him yourself?"
        "Agatha shook her head."
        aga "I've been too occupied scouring the ancient texts for ways to banish him. I fear it left me little time for other things, so I had to relegate keeping watch to other members of the Codifice."
        $ event_tmp['ask_name'] = True
        jump AgathaMenu

    "Ask about the rune circle.":
        $ released_fix_rollback()
        "Agatha smiled brightly in response and straightened her back proudly."
        aga "It’s a gift from Solansia herself! As we prepared our trap, she sent me another vision, showing what runes will keep him powerless. They've been exceptionally useful in keeping him pliant and obedient."
        'Rowan took another look at the incubus. The demon growled at him in response. How was that "pliant and obedient"?'
        ro "Have you experienced such visions in the past?"
        "The nun hesitated for a moment, then shook her head."
        ro "(Not suspicious at all.)"
        $ event_tmp['ask_rune_circle'] = True
        jump AgathaMenu

    "Ask why he’s naked.":
       $ released_fix_rollback()
       aga "Oh, that’s simple. We couldn’t risk him hiding any lockpicks in his clothes."
       ro "Did you find any?"
       aga "No."
       ro "So why is he still naked?"
       "The Abbess furrowed her eyebrows, uncertain how to respond."
       aga "Um... I believe some of the acolytes said they didn't want to come near him unless absolutely necessary?"
       "She blushed, ashamed of herself, and looked away."
       aga "I didn't really think about it until now, to be honest."
       ro "(Right...)"
       $ event_tmp['ask_naked'] = True
       jump AgathaMenu

    "Ask how exactly are they keeping him drained.":
        $ released_fix_rollback()
        aga "Oh, it’s simple! We drain his cum."
        ro "…"
        ro "You drain his cum."
        aga "Yes. It’s the incubus main source of power. As long as his testicles are empty, he is powerless to escape."
        ro "…"
        "He looked her straight in the eyes. She tilted her head, clearly not understanding his apparent disbelief."
        ro "(Oh Goddess.)"
        $ event_tmp['ask_drained'] = True
        jump AgathaMenu

    #only available after other four choices have been chosen
    "Ask why didn't they kill him." if event_tmp['ask_name'] and event_tmp['ask_rune_circle'] and event_tmp['ask_naked'] and event_tmp['ask_drained']:
        $ released_fix_rollback()
        aga "Oh, we couldn't! We cannot risk him reforming in the Outer Dark!"
        aga "A incubus this powerful cannot be slain with a simple sword, his essence would simply escape this realm, and in time, create a new body for itself!"
        aga "That's why we keep him here for now. And that's where you come in."
        aga "If you agree to help us, that is."
        "The Abbess looked up at him with a hopeful smile, while Rowan did his best to suppress a sigh. His eyes wandered to the runes surrounding the incubus."
        "He doubted they really did anything except look mysterious. Just as he doubted that keeping him “drained” actually weakened the incubus."
        "The whole damn story came apart at the seams the moment anyone stopped to think about it, and Rowan had no doubt the incubus had to work the clerics for some time to have them all discard basic logic so easily."
        'For crying out loud, the demons did not, and never did, "reform" after being slain. Just like people, they all die when they are killed. Even Karnas, for all his power, was never able to come back from the dead.'
        "It was time to decide what to do about the whole situation. Rowan looked at the incubus once more, his glowing eyes staring right at him-"
        "..."
        "Uh..."
        "…"
        "What was he on about…?"
        aga "Are you feeling alright, Rowan?"
        "Feeling a bit lightheaded, Rowan blinked rapidly a few times, trying to get his thoughts together. What was he..."
        ro "I... Yes, I'm feeling alright, just..."
        "This wasn’t like him, suddenly spacing out like that. Something was-"
        "He heard Agatha gasp loudly."
        aga "Oh no! Look, Rowan!"
        "She pointed to the demon's nether regions, and Rowan followed her finger."
        "Precum was leaking from Dazzanath painfully erect cock, filling the room with a heavy aroma of cum. The demon grunted in discomfort, and buckled his hips forward, making white droplets fall on the floor in front of them both."
        aga "But we already drained him today! Solansia protect us, we can’t let him regain his power!"
        "Eyes fixated on the organ before them, Rowan knew that one of them would have to kneel before Dazzanath, to prevent him from escaping. It was the only way, after all…"

menu:
    "Rowan kneels.":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        scene black with fade
        show rowan necklace happy behind black
        "Rowan felt his mouth water. His head was light from the intoxicating smell of Dazzanath’s cock, and he couldn't help but watch fascinated as its bulbous head swayed enticingly before him."
        "Without a word, Rowan knelt before the incubus. So did Reverend Agatha, by his side – either to advise him on the proper draining technique or just to watch."
        "Rowan was grateful for the consideration, but it wouldn’t be needed. He was a hero – and he always saw the job through."
        "Even a blowjob."
        "As he feasted his eyes on the sight before him, Agatha reached out, running her fingers under Dazzanath’s cock. She scooped up the leaked cum and brought it to her lips."
        "She licked it up greedily and sighed with satisfaction, a look of complete exaltation on her face."
        aga "Ah… So thick…"
        "Meanwhile, Rowan still couldn't take his eyes from the engorged head before him, its heavy aroma assaulting his senses. His mind felt heavy, and his body turned numb."
        "It was increasingly more difficult for him to focus on anything other than the growing need inside of him."
        scene cg201 with fade
        pause 3
        "Slowly, he leaned forward and opened his mouth. The incubus' hips buckled forward, and the tip passed through his lips."
        "Salty precum covered the inside of his mouth, and he started to explore the throbbing tool with reverence, running his tongue along it with passion. Whenever it hit the inside of his cheeks, it left a pleasant, numbing sensation, that went straight to his head."
        "Until now, he still heard a quiet voice in the back of his head that kept insisting something was wrong with the entire scene, but it was silenced the moment he tasted the demon's cock."
        "Rowan could now focus on properly draining the captured incubus, just he was supposed to."
        aga "Deeper. You have to take it deeper."
        "The Abbess urged him on from the sidelines, and Rowan didn’t need to be told twice. He leaned in, taking it halfway through, enjoying its shape and warmth. Little by little, he pushed forward, gurgling as the tip hit the back of his throat, and then further down, deep inside."
        aga "Now, move your head slowly… You need to bring him to the edge before we can drain him."
        "The Abbess clung to his arm, whispering excitedly in his ear, her hot breath on his neck. He could hear the hunger in his voice, and for some reason, he felt immense joy at the fact he was the one taking care of draining Dazzanath, and not her."
        "Elevated, he started to slowly slide his lips up and down the demon's cock, his jaw loosening up as he felt the incubus leak more and more precum into his mouth."
        "Quickly, he started to pick up the pace, not paying much attention to anything besides the taste of the corrupt cock and its semen."
        "A soft hand touched his own, left one, and the Abbess brought his fingers up, guiding them to the incubus sack."
        aga "Now, massage them gently… We have to drain him thoroughly."
        "His fingers touched the heavy balls, admiring their weight. The source of the incubus power. They had to empty them."
        "He had to empty them."
        aga "Almost there! Drink it up! You have to drink it! It's the only way to seal the dark power inside his semen!"
        "He heard the incubus grunt."
        "The quiet voice in the back of his head suddenly woke up again, screaming at him not to do it. Maybe drinking Dazzanath's corrupt, delicious cum wouldn't be such a great idea..."

        menu:
            "Drink it.":
                $ released_fix_rollback()
                scene black with fade
                show rowan necklace aroused behind black
                "Warm, thick cum hit the back of his throat. Greedily, Rowan started to drink it all down, a warm, pleasant feeling spreading through his body as he did."
                ro "Ah… Ah…"
                "Dazed, he fell back. Slowly, the fog that covered his mind seemed to dissipate, now replaced with a burning sensation deep inside his stomach."
                "He looked up-"
                "And saw the incubus cock was still hard and leaking cum."
                aga "Oh no, it’s still not drained!"
                "Panicked, the Abbess quickly positioned herself in front of the demon, read to do her duty as the incubus cum dump."
                aga "Cum... Cum... Been so long..."
                "Her excited whispers filled the room, and the gravity of the situation suddenly crushed into Rowan, washing away the numbness of his thoughts and body. Quickly, he grabbed the Abbess by the arm and painfully yanked her backward."
                "He saw her eyes flare up in anger, furious at being denied her treat."
                ro "Reverend Mother, we can’t both spend the day draining him. I’ll take care of things, while you consult the sacred texts. Maybe you’ll find something that will help us."
                "He couldn’t risk having her around when he confronted the incubus."
                "The abbess tried to protest, tried to struggle, but when she turned around to look at the incubus, her body suddenly lost all of its energy. She nodded in agreement, somewhat dazed, and left the room in a hurry, leaving the two of them alone."
                "Rowan stood up. He placed his hand on his sword and turned to address the incubus, careful not to look him in the eyes."
                #gain corruption
                $ change_base_stat('c', 2)
                #set flag: Dazzanath cum dump.
                $ event_tmp['Dazzanath cum dump'] = True
                jump confrontDaz

            "Don’t drink it.":
                $ released_fix_rollback()
                scene black with fade
                show rowan necklace concerned behind black
                ro "(Don’t!)"
                "Panicking, Rowan suddenly fell back, releasing the cock from his lips. It throbbed violently and unleashed a stream of thick cum into the air, some of which landed on Rowan's pants."
                "The Abbess gasped in horror and instantly took Rowan's place, obediently drinking all of the corrupt sperm. Rowan could only watch, dazed, as the once pure nun gulped loudly, choking from all the cum the cock kept pumping into her."
                "Half a minute later, she released his dick, an exalted look on her face as she still savored its taste."
                aga "Ah… Ah…. That… That should do it."
                "She sighed happily. Rowan took a quick glance at the demon's penis."
                "It was still erect and still leaking cum."
                aga "Oh no, no no no!"
                "Panicked, she turned around and looked at the hero."
                aga "Rowan, we must do something about this!"
                "Her terrified, cum stained face finally pushed the hero out of his stupor. He forced himself upwards, feeling a bit wobbly on his knees, but the numbing fog that covered his thoughts was quickly dissipating."
                "He placed one hand on his sword, while the other reached for the Abbess. He grabbed her by the arm and yanked back, away from the corruptive influence of Dazzanath's cock."
                ro "Reverend Mother, you should consult the sacred texts. Maybe you’ll find something that will help us."
                "He didn’t want her around when he confronted the incubus."
                "The abbess tried to protest, but when she turned around to look at the incubus, she suddenly lost her resolve and nodded in agreement. She left the room in a hurry, leaving the two of them alone."
                jump confrontDaz

    "Rowan watches as Agatha kneels.":
        $ released_fix_rollback()
        scene cg212 with fade
        show rowan necklace happy behind cg212
        pause 3
        "Rowan felt his mouth water. His head was light from the intoxicating smell of Dazzanath’s cock, and he couldn't help but watch fascinated as its bulbous head swayed enticingly before him."
        ro "(… Hold on… Something is…)"
        "Furrowing his eyebrows, Rowan couldn't help my think that something… Something wasn't exactly right with this scene."
        'A furious voice in the back of his head kept telling to "snap out of it", but he could not say why was he supposed to "snap out it", or what exactly was the "it" he supposed to snap out of.'
        "Standing motionlessly, he tried to make some sense of his thoughts, when the cock twitched again. By his side, the Abbess let out a startled gasp."
        aga "Oh no, it’s getting worse!"
        "Quickly, she knelt before the incubus. Rowan felt like he should probably stop her, but he couldn't determine why, and at the moment his heavy body wasn't exactly complying with his wishes."
        "He could only stare as the Abbess opened her mouth, and slowed enveloped the incubus tool with her lips. She eased it in slowly, carefully, with great reverence."
        "But as soon as she managed to force it all the way in, she rapidly picked her pace up, working the shaft with great tempo. It felt… Wrong, to see a woman of faith show such great practice in sucking a cock, but again, Rowan couldn't say why exactly."
        aga "Mmmph- Mmm! …. Mmmph!"
        "The incubus remained almost motionless, lightly bucking his hips to match the Abbess movement. Rowan could still feel his eyes on him, but he couldn't bring himself to look up."
        "Transfixed on the Abbess, he felt himself split between revulsion and jealousy, slowly growing aware that of these two conflicting feelings, only one was truly his..."
        "Suddenly, Agatha stopped. She slid off the cock, keeping her lips closed around the tip, and gently reached out to massage the demon’s balls."
        "Dazzanath grunted, and pushed his hips forward, coming straight into her mouth. Agatha's cheeks ballooned, and gulping loudly, the Reverend Mother started to drain the corrupt seed from the demon."
        aga "Mmm- ah, ah, ah…"
        "Finally, she released his cock, an exalted expression on her face. She sat down, panting, eyes still focused the throbbing tool in front of her."
        "… Which started leaking cum once more."
        aga "Oh no."
        "Panicked, she turned around and looked up at the hero."
        aga "Rowan, we must do something about this!"
        "Her terrified, cum stained face finally pushed Rowan out of his stupor. He placed one hand on his sword, while the other reached for the Abbess. He grabbed her by the arm and yanked back."
        aga "Reverend Mother, you should consult the sacred texts. Maybe you’ll find something that will help us."
        "He didn’t want her around when he confronted the incubus."
        "The abbess tried to protest, but when she turned around to look at the incubus, she suddenly lost her resolve and nodded in agreement. She left the room in a hurry, leaving the two of them alone."
        jump confrontDaz

    "(Fight this, damn it!)":
        $ released_fix_rollback()
        scene black with fade
        show rowan necklace neutral behind black
        "Rowan felt his mouth water. His head was light from the intoxicating smell of Dazzanath’s cock, and he couldn't help but -"
        ro "(NO!)"
        "Forcing himself into action, Rowan slapped himself across the face, the stinging pain that followed bringing him out of his stupor."
        "Dazzanath’s chains rattled dangerously. Rowan brought his hand to his sword and shook his head at the Incubus, careful not to look him in the eyes."
        "Not yet. Not with Reverend Agatha around."
        aga "Rowan? Is everything ok?"
        ro "Yes, Reverend Agatha. Would you mind leaving the two of us alone?"
        aga "I shouldn’t-"
        "The Incubus turned his eyes to the Abbess. In an instant, the resolve to be of assistance drained from her posture, and she nodded obediently."
        aga "… If you feel it best."
        "The Abbess left the room in a hurry, leaving the two of them alone."

label confrontDaz:

scene black with fade
show rowan necklace neutral behind black
show dazzanath neutral behind black

ro "…"
ro "I imagine you do speak, is that right?"

daz "Mhmmmm, I do."

"The incubus had a pleasant, almost velvety voice."

daz "But Agatha is always so… Fun to have around. How could I ever interrupt you two?"

"He chuckled softly. The chains that held his arms rattled again, and this time – popped off the wall, as the demon casually removed a fake link that must have been there from the start."

daz 'And I was... Curious. Agatha was supposed to keep her "holy quest" secret from everyone… And yet she brought you here. She must hold you in high esteem, “Rowan”.'

"It wasn’t often that Rowan met demons unfamiliar with his past. Dazzanath was a rare exception. "

daz "Which means the two of us are likely going to fight… Unless…"

"The incubus opened his arms up invitingly."

daz "Look… The fact you still haven't stabbed me with that pointy thing inclines me to think that maybe there is some… Common ground for us to find..."
daz "What is it that you desire, Rowan? Is it women? The abbey has no small number of them, you would just need to give me some time to finish my work. Men? Same as the above."
daz "Is it power? You’d be surprised what sort of concoctions can be prepared with incubus fluids..."
daz "Riches? Treasures? I have quite the collection... You could pick something for yourself..."

"The incubus went on, going through the usual “temptation” routine Rowan was slowly getting familiar with by this point."
"But there was indeed a common ground for them to find. There was something Rowan wanted from the incubus, though it was not what Dazzanath imagined."

#if corruption is higher than 49
if avatar.corruption > 49:
    "His work on the Abbey was impressive. If not for Rowan, he would likely succeed in converting it fully, without anybody ever noticing anything wrong. His method of infiltration was unorthodox, but the fact he was able to pull it off showed great skill."
    "Skill the twins could benefit from if Dazzanath agreed to spy for them."
else:
#else
    "The incubus sickened him, there was no denying it. It was downright demoralizing, witnessing the servants of Solansia being reduced to mere cock-slaves."
    "He also couldn't deny Dazzanath possessed both skill and a particular brand of bravado that would make him an excellent spy in the service of the twins."

#rejoin
"His method of control, in particular, would also be of great use. Rowan was accustomed to demons trying to break his will with brute force, but Dazzanath’s, while not as direct, and therefore much less effective, was also much less invasive."
"And in certain ways that was much more dangerous."

menu:
    "Recruit him as a spy.":
        $ released_fix_rollback()
        "Rowan signaled the Incubus to stop and finally took his hand off the sword."
        ro "Enough. None of these interest me."
        ro "But we might come to an agreement after all…"
        jump recruitDaz

    "Slay him.":
        $ released_fix_rollback()
        "… Far, far too dangerous."
        #if Dazzarath cumpdum is true
        if event_tmp['Dazzanath cum dump']:
            "… But did that really mean Rowan had to kill him?"
            "The hero hesitated, the memory of Dazzanath’s cock in his mouth, and his sperm in his stomach, still fresh in his mind."
            "His gaze wandered to the incubus' fully erect tool. The demon, still talking, quickly took notice."
            daz "Or is what you want… Me?"
            "… The Twins would find his skills useful... And with Dazzanath in castle Bloodmeen, Rowan could keep an eye on him to make sure he wouldn't be up to any mischief..."
            "Surely it was an option worth considering, right?"
            "Before Rowan could even consider the idea thoroughly, he found himself already agreeing."
            ro "We might come to an agreement after all…"
            jump recruitDaz
        else:
        #else
            "Without giving the incubus a moment to react, Rowan jumped forward, brandishing his sword. Instantly, his mind slowed down, as the demon attempted to stop him in his tracks with magic."
            "Too little, too late."
            "Powering through the mental domination, Rowan reached the demon and pushed his sword into his chest. With no armor, no blade of his own, and no room to dodge, the Incubus fate was sealed on the spot."
            daz "… No way… "
            "The demon coughed blood, desperately clinging to Rowan, but his strength was already failing him."
            daz "… Such a stupid death…"
            "Rowan pushed the incubus off him, pulling out his blade. The demon fell to the ground, lifeless."
            "..."
            #abbey
            scene black with fade
            "It took some time to explain the Abbess everything. At first, she was hysterical, and for a moment Rowan feared the whole situation would result in violence – further violence, that is – but in the end, he was able to talk the acolytes down."
            "Many still couldn’t believe the demon had deceived them, but in time, the corruptive influence would leave their body, and they would see reason."
            'For now, Rowan preferred not stick around, in case any of them choose to enact bloody vengeance for the death of their "prisoner".'
            "He sneaked away from the Abbey under the cover of night, knowing he already spent far longer in it that he should have had."
            "At least for now."
            "He could, at least, take comfort in knowing its residents would be safe."
            #gain solansia favour
            $ change_favor('solancia', 1)
            #Lose: corruption, guilt, X’zaratl influence (Only a small amount. Dazzanath is more of a passing acquaintance, so she's not to shaken by his loss, and has no proof it was Rowan who slew him. )
            $ change_base_stat('c', -2)
            $ change_base_stat('g', -2)
            $ change_relation('xzaratl', -1)
            return

label recruitDaz:

"In the following minutes, Rowan briefly explained who his masters were, and what was their goal. While Dazzanath proved to be horribly uninformed in the matters of demon politics, or any politics, he did hear of the twins and seemed intrigued by the idea of working with Jezera."
"Her style, at least, interested him, because as far as the overall goal went..."

daz "With all due respect, Rowan Blackwell, but I find world domination... Oh, so horribly cliché! It's a fun way to pass the time, don't get me wrong, but I cannot imagine ruling it to be anything but a massive headache."

"Rowan stopped himself from rolling his eyes and decided not to comment. Personal outlook aside, Dazzanath ultimately did agree to join them... He just had one little request…"
"That Rowan allowed him to remain in the Abbey, to finish his work. Shouldn't take him more than a month or so."
"In return, he’ll bring the “converted” clergy with him to castle Bloodmeen. Surely Rowan would find some use for a dozen of cum hungry slaves, no?"

menu:
    "Agree.":
        $ released_fix_rollback()
        "The Abbey was already lost. Might as well get something out of it."
        "Dazzanath would be free to do as he pleased."
        "He reattached the Incubus to the wall and headed out to find Reverend Agatha. He found her studying the texts, as he told her to."
        "Trying to avoid her trusting eyes, he told her he would look for a way to slay the Incubus, and that for now, they are too keep him drained and weakened, as they did before."
        aga "Thank you, Rowan! We will do just that. Our fate is in your hands now."
        "It was indeed. And it was already sealed."
        "Agatha insisted he stay over for dinner, but Rowan declined."
        "He already spent too much time at the abbey."
        "He left the same day."
        #Gain: Guilt. In 4 weeks: Launch event “Dazzanath arrives” (see below)
        $ activate_event('dazzanath_arrives')
        $ set_event_timer('dazzanath_arrives', 'after_abbey', 4)
        $ change_base_stat('g', 2)
        #Lose: -Solansia favour.
        $ change_favor('solancia', -1)
        return

    "Refuse. He’s leaving with you.":
        $ released_fix_rollback()
        "Whether it was because they needed his services now, or because Rowan found the idea of letting Dazzanath do as he pleased with the Abbey reprehensible, the incubus was informed they would be leaving the Abbey immediately."
        "Rowan found Reverent Agatha studying the sacred texts, as he told her too. He lied he knew somebody who would be able to help, but they couldn't risk waiting for them to arrive at the Abbey. Instead, he will take the incubus, and escort him personally to the destination."
        "At first, the Abbess opposed the idea, the corruptive influence forcing her to find more and more bizarre excuse to prevent the incubus from leaving the abbey."
        "But Rowan was relentless. After over two hours of persuading, Reverend Agatha finally gave up. The very same day, the Incubus was bound in chains and released in Rowan's care."
        "The two left the Abbey soon afterward. Agatha insisted the hero should stay over for dinner, but Rowan declined."
        "He spent in the Abbey way too much time anyway."
        #Gain: Dazzanath as a spy (see below). Solansia Favour.
        $ change_favor('solancia', 1)
        $ recruitDaz = True
        python:
            event_tmp['_spy'] = Spy('m')
            event_tmp['_spy'].name = 'Dazzanath'
            event_tmp['_spy'].traits = ['Master', 'Submissive Seducer', 'Methodical']
            event_tmp['_spy'].sprite = 'incubus3'
            castle.spies.append(event_tmp['_spy'].uid)
        return

#Dazzanath as a spy
#Image: Incubus 3
#Traits: Master, Submissive Seducer, Methodical.


label dazzanath_arrives:
#dazzanath arrives event
#//Quick message after 4 weeks when Dazzanath arrives at the castle. Occurs at end of week, in addition to any other events.
"Rowan was informed Dazzanath arrived at the castle while he was away, bringing with him the promised slaves."
"The brainwashed clergy was added to the prison, and the Incubus now awaited his orders."
#Gain: Dazzanath as a spy, +12 slaves.
$ change_prisoners(12)
$ recruitDaz = True
python:
    event_tmp['_spy'] = Spy('m')
    event_tmp['_spy'].name = 'Dazzanath'
    event_tmp['_spy'].traits = ['Master', 'Submissive Seducer', 'Methodical']
    event_tmp['_spy'].sprite = 'incubus3'
    castle.spies.append(event_tmp['_spy'].uid)
return
