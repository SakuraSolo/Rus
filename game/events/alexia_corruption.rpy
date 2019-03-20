init python:
    
    event('alexia_med_corruption', triggers='week_end', conditions=('all_actors["alexia"].corruption > 30',), run_count=1, priority=pr_story)

label alexia_med_corruption:
scene bg31 with fade
show alexia intro neutral at midleft with dissolve

"Alexia hummed to herself as she carried a pair of wooden buckets up the rolling hillside. A light breeze ruffled the tall grass to either side of the dirt trail. The faint sound of activity rose from the village below."
"This was not the first time she’d made the trek this week. Not even the first time today. She was heading to the secret little garden of flowers that she’d been working on at the summit. Her plants were so hard to please. They always sang for more water."
"It had everything. Petunias, Roses, Irises. In a sea of green hillside, it was a colorful landmark. A monument to the fact that Alexia lived here."
"The first sign that something was off, was the absence of a frequent companion. The cat that had a home in a nearby tree wasn’t there at this afternoon. Despite herself, she was almost disappointed. He was a constant, almost always in his little perch."

show alexia intro concerned at midleft with dissolve

"But, when she reached the hilltop, where her garden was waiting, her jaw fell. She even dropped the buckets to the ground."
"In the mere hours since she’d last been there, something horrible had happened. Something impossible. A large sapling was bursting out of the ground in the middle of the plot for the daisies. "
"The wood of the invader was a repulsive black."
"But, the effect it had extended to the entire garden. Long obsidian tendrils poked out of the dirt in all of the other plots. The sapling’s roots. Wherever it went, it brought death and chaos. Flowers that had hours before been fine were wilting."

"She sunk to her knees."

al "How could this have possibly happened?"
al "I was here just hours ago. This is monstrous. This is impossible. I worked so hard to make this place perfect. "
al "This was my private place."

"Her eyes narrowed in on the sapling. Her heart swelled with emotion. It was disgusting. It was vile. It had destroyed the garden that she’d cared so much about. She should bring an axe and chop it down. She should destroy it."
"She rose, and approached the sapling cautiously. It was almost as tall as she was, yet it was still thin and weak. Perhaps she could simply snap it in half with her bare hands. Let the broken black husk of the invader serve as the tombstone to this place that she loved."
"It looked so smooth. Unnatural yet oddly appealing. In a strange way it was almost…"
"Almost...beautiful…."
"The tree shook slightly. It rattled the same way old bones do."
"Then, in the center of the trunk, an eye opened. It’s wide iris looked directly at Alexia. It surveyed its new home. Alexia put her hands over her mouth. The eye looked at her with judgement. She felt undressed."
"The eye swiveled around taking in the sights of the garden. Then it refocused on her."
"Alexia felt her feet glued to the ground. Did she want to scream at it? Did she want to run from it? Did she want to understand how it had come to be."

quest "You’re confused."

"Alexia felt her mouth open, without understanding why."

al "I’m afraid."

quest "You’re confused. Why are you confused?"

"Alexia’s mouth spoke again."

al "Because you’re strange. You’re wrong. This is wrong. You don’t belong here?"

quest "I don’t belong here? Are you sure?"

al "…"
al "No."

quest "Come here. Will you still feel I don’t belong here if you come to know me?"

"Alexia couldn’t argue with that logic. Yet, there were still voices in her head screaming. What had happened to her garden? How can such a black vile thing be trusted."

show alexia intro aroused at midleft with dissolve

"She approached the tree and put a hand on its perfect trunk. At once she felt a fire, spread through her body from the point of contact. It settled between her legs."

al "Ah."

quest "Now do you know me? Now are you confused?"

al "I-"

scene black with fade

"Alexia blinked."
"Alexia saw a blue storm rage overhead above a land where the trees grew from up to down. The broken incoherent landscape was as overwhelming and consuming as the storm over head. Yet, it too was almost beautiful."
"Alexia blinked."
"She was standing in front of a doorway. Inside all she could see was a winding traverse of paths. The structure was old. Writing carved into it had long since been erased. "
"But, the area around the doorway was all wrong. The sand was pure crimson, and the sky was illuminated by dancing colors. Alexia had not been too many places, but she knew that this was not anywhere she’d ever even heard of."
"Alexia blinked."
"She was naked and kneeling on some strange platform. She gazed forward, and a familiar face gazed back at her. Rowan. The man she loved. The man she’d centered her entire life around. "
"She wanted to open her mouth and tell him about the flower garden. About that beautiful horrible sapling. But, she couldn’t speak."

if all_actors['alexia'].relation > 50 and avatar.corruption > 30:
    "Instead, she was forced to watch on in silent horror as the face in front of her distorted and twisted in on itself. Bones and cartilage twisted and contorted unnaturally. When it finally finished, she was staring at an entirely new, entirely different face."
    "The question was just if it was still Rowan’s face at all?"
    
elif all_actors['alexia'].relation > 50 and avatar.corruption < 31:
    "Instead, she was forced to stare straight ahead as something happened to her. At first it was a little bit painful. It was only through him she knew something was happening. His mouth gaped in shock...in disgust at the changes that were happening. He was disgusted by her."
    "There was a creaking sound. Her entire face was shifting. Changing. Would she even recognize herself when she was done? Would he?"

else:
    "She stared at Rowan’s face for a long time. The longer she looked the more angry she got. How could he just look at her like that? How could he expect her to keep on staring at him forever? Didn’t he know that she was her own person? That she didn’t owe him anything?"
    "Fuck him. Fuck him. Fuck him. Fuck him. Fuck him. She spat in Rowan’s face."

"That was when the silence was broken. A single statement that pierced the veil."

show rowan necklace neutral behind black 

ro "Why?"

"Alexia didn’t know. She blinked."

if alexiaSeparateRoom == False:
    scene bg9 with fade
    show alexia white concerned at midleft with dissolve
    "Alexia felt cold. She blinked twice more, but the world around her didn’t fade away anymore. She was in bed with Rowan. The cold was the breeze through the slightly opened window."
    "Alexia rose from bed and shut the window. There was sand in her eyes."
    "Just what had that dream been?"
    "She looked back at Rowan. Her arm stretched and unstretched." 
    "The garden, the tree, that strange cacophony of images? She’d never had a dream like that before. Hell, she’d ever even kept a garden when she lived in Arthdale."
    "She had wanted too, though."
    "Rowan was on his side snoring loudly. It had been years since the peaceful post-war days. But, he still looked the same. Or at least mostly the same."
    if avatar.corruption > 30:
        "But, looks could be deceiving..."
    else:
        "After all, when it came down to it, she was the one who’d changed most..."
    al "...Rowan, I…"
    "She shook her head. What was there to even say to him?"
    show alexia white neutral at midleft with dissolve
    "Maybe she shouldn’t have shut the window. Alexia decided that perhaps she needed some air. Some real air." 
    "Alexia walked over to the closet. She needed to get dressed."

else:
    scene bg7 with fade
    show alexia white concerned at midleft with dissolve
    "Alexia felt uncomfortable. She was sweating. She blinked twice and looked around. She was back in her guest room. All the blankets on her must have trapped the heat."
    "Just what had that dream been?" 
    "She stretched her arms and let out a big yawn. Her eyes scanned the room. It felt like there should be something else here."
    "The garden, the tree, that strange cacophony of images? She’d never had a dream like that before. Hell, she’d ever even kept a garden when she lived in Arthdale."
    "She had wanted too, though."
    "Alexia wrapped herself in her arms. Even that element of touch felt good. "
    al "I shouldn’t have wine before bed."
    "She rose from bed and walked automatically to her closet. The room had a malaise hanging over it. It was too stuffy and too quiet. It made Alexia want to get a bit of air. Use a walk to get that dream out of her system."
    
scene cg262 with fade
show alexia 2 necklace neutral behind cg262

"The wind swept softly over the black Bloodmeen sky this morning. Alexia could feel it clearly from atop one of the unused castle spires that pierce the clouds. From this vantage point she could see the peaks of mountains miles away. The snow on their peaks was so beautiful."
"Alexia brushed her hand along the stone railings. This was no the first time that she’d come up here. She liked to take private walks to clear her head. It was all in the castle, so her captors didn’t mind."
"She looked over the railings and found a seemingly endless drop. From her readings, she’d learned that being thrown from the spires had once been a common execution method here. So it was strange that she found this a place of peace."
"Alexia breathed in the air. It was rather thin here. It was easy to get light headed. Perhaps that was the point?"

al "Sometimes, I feel like you don’t live out here, Solansia. That this is a place you can’t reach."

"She spoke out towards the rising sun."

al "Mother taught me that you were always watching over us. That you cared for your children above all else. "
al "But, if you do, why did this all happen?"
al "So, I have to believe it’s something about the place. That you want to help, but you can’t. Otherwise, mother was wrong."
al "..."
al "The more I think about it, the more it feels that mother was wrong about a lot of things…"

"The back of her hand brushed against her bosom. Even that felt good."
"She turned the corner of the spire, and found herself staring at something she hadn’t expected to see. Something that shook her bones."
"Many of the spires had little gardens at the top. Because this was Bloodmeen, and thus designed by demons, they often had demonic roses or thickets of spiky plants designed less to lighten the place up and more to terrify. They clung to life on the moisture of passing clouds."
"But, this garden had something she’d never seen before."
"There was a tall strong hardwood tree bursting out of the ground, with its uppermost branches entwining with gargoyles on the spire. It was a tree that had grown together with the building. It was an astonishing sight, unlike anything she’d seen before…"
"...and the wood of the tree was absolutely pitch black. All color drained from Alexia’s face."
"It wasn’t the same tree exactly. It looked more real, more natural, then the gangly creature of last night. It was also old and strong, unlike the strange ephemeral sapling. The lack of a giant eye was also a fairly notable distinction."
"However, the wood was the same unsettling black. More to the point, it certainly had a dark aura to it. As Alexia stood in its presence, she felt it like a gravity pool urging that she come closer."

menu:
    "Flee from the tree.":
        $ released_fix_rollback()
        "Alexia took a step backwards. Then another. In moments, she broke into an open run away from the nightmare come to life. How had that got there? Had it always been there?"
        "She ducked back inside the building. Suddenly she didn’t seem to mind the stuffiness quite as much. Her mind was racing. Her heart was racing."
        "What had she just seen? And why had she...why has she wanted to approach it, just like she had in the dream?"
        if alexiaSeparateRoom == False:
            scene bg9 with fade
        else:
            scene bg7 with fade
        show alexia 2 necklace concerned at midleft with dissolve
        "She curled up in the corner, with her arms wrapped around her legs. Tears had started rolling down her face."
        "There was something strange going on. Something horrifying. That couldn’t have been an ordinary tree. It must have been somehow magic. After all, surely someone like Jezera or Clionha had the power to warp the dreams of their subject."
        "Alexia balled her hands into a fist."
        "But, did they have the power to make someone like those dreams?"
        if alexiaSeparateRoom == False:
            show rowan necklace naked at midright with dissolve
            ro "Alexia, are you okay? What’s wrong?"
            show alexia 2 necklace happy at midleft with dissolve
            al "It’s nothing really. You don’t have to worry about it at all. I’m just still getting used to this place. Even after all this time, it’s still so strange, you know?"
            al "...That’s all."
            al "That’s all."
        scene black with fade
        "Alexia has now reached medium corruption. Her reaction to different events and scenes will change as a result. At this rate, Alexia’s corruption will only grow and grow…"
        return
        
    "Approach the tree.":
        $ released_fix_rollback()
        "Alexia’s eyes glazed over slightly. What would be so wrong with taking a closer look? It wasn’t every day one saw the figment of a dream come to life. Maybe, it would just be a strange coincidence"
        "Her hips swayed ever so slightly as she stepped towards it. The dream had already started to blur, but that fire she’d felt hadn’t."
        "Her hand touched the exterior of the tree. Hard. Strong. Smooth. The smoothness was the most unnatural element. It should have felt more coarse and bumpy. But, what she didn’t feel was that same fire shoot up her body."
        "She stroked the tree softly. Perhaps it had all been her mind playing tricks on her. Perhaps she’d seen this tree before, and the reason there was a black tree in her dream was because her brain was playing tricks on her. Certainly this tree didn’t have a large eye in the middle of it."
        "Alexia sighed and slumped down against the tree. It was a good spot to lay against. Despite the tree’s hardness, it almost felt like laying down in freshly cleaned sheets."
        "She wasn’t even cold anymore. Her conscious mind didn’t even process it, but the closer she was to the tree the less she felt the high altitude wind and the chill it sent through her body."
        "She closed her eyes…and at once images went through her head."
        scene black with fade
        if all_actors['alexia'].flags['andras_influence'] > 6:
            "The strong embrace of a hand on the back of her neck. The knowledge she was about to...taken…and that there was nothing she could do about it. The feeling of a massive cock filling her body…"
            "...slamming into her with a strength not held back by sentiment or concern. The man wanted to user her body, and didn’t care what she thought on the matter…"
            "...Not that she disliked it..."
        elif all_actors['alexia'].flags['jezera_influence'] > 6:
            "The scent of female anatomy mere inches from her face. The feeling of her arms and legs tied down. No escape to be found anywhere. That intoxicating scent coming closer and closer..."
            "...Then smothering her. Making it impossible to breathe. Only one thing to do…"
            "...Open her mouth and put her tongue to work."
        else:
            "Hands were running up and down her body. It could have been two. It could have been a hundred. But, everywhere they touched, like rippled in a pond, electricity moved out in every direction. A thrilling, erotic lighting…"
            "...It was everywhere now. In her legs, in her arms, in her bosom. Her body squirmed outside of her control…"
            "...Everything was lost to the pleasure. Everything was the pleasure…"
        "When she opened her eyes, she found her own hands moving. They were rubbing her breasts, and her legs. Alexia gasped out. How had her body gotten so sensitive, so eager, in such a short amount of time?"
        "In a rush, she threw off her dress. She didn’t need it. The tree would be her warmth."
        #cg1
        scene cg301 with fade
        show alexia necklace naked aroused behind cg301
        pause 3
        "Now, without anything to get in her way, her hands went back to work. A long feminine groan slipped past her lips at the exact moment that two of her fingers sank into her cunt. Her other hand was busy pawing at her nipples, tweaking and rubbing them."
        "It had taken some time, but she could feel it now. Her body was alight. There was fire running through her veins. Fire between her legs. She felt like she bursting with constrained heat. She liked how that felt."
        al "Ah..."
        "Normally she liked to put more effort into rubbing her clit, but her fingers sank deep into her sex. It felt good to have something inside of her. She liked how it felt too."
        "That one thought prevailed over the others. She liked this. She liked the frantic movement of her fingers into her body. She liked the lewd display she was putting on. She liked the thought of someone coming up here and seeing what a slut she was."
        "That’s right. What a total slut."
        al "Fuck. Fuck. Fuck. I’m a slut. I’m a total slut. Ah."
        "The sound it made would be unmistakable. The watery sound of a pussy in use. So too would the smell. There was something deeply erotic about the knowledge that this place would smell like her lewdness if anyone passed."
        "Alexia worked her finger faster and faster. Building up to it. There was no restraint or consideration. Just a powerful desire to bring herself to orgasm. To bathe in the way that it felt."
        al "A slut. A slut. Ah. Such a slut. Such a fucking slut. Ah."
        "She was so close now. The heat was rising up. It was consuming her. It was mere moments from pouring out her body. Her fingers put everything they could into…"
        "Plop. There was an odd sound next to her. Alexia slowed down, though did not stop touching entirely, to see what it had been."
        #cg2
        scene cg302 with fade
        pause 3
        "One of the strange fruit growing high up in the tree had fallen right next to her. She used the hand that had been at her breast to pick it up and examine it."
        "Had it been...a gift for her? There would only be one way to find out…"
        "A voice in the back of her head pleaded for her to stop. Didn’t she understand what would happen to her if she indulged herself too much? Didn’t she see what was happening to her?"
        "Alexia didn’t listen to that voice. Instead she bit into the bizarre fruit."
        #cg3
        scene cg304 with fade
        show alexia necklace naked aroused behind cg304
        pause 3
        "The moment she tasted it’s sweet nectar, her head went fuzzy. It tasted like it had been dipped in honey. She took another bite. Orange juices dribbled down her chin, down her breasts, over her stomach…"
        "Her body was stained by its juices. The taste of it made her head buzz. It was so hard to think. She just wanted more."
        "The fingers between her legs slowly pumped away. They kept her riding the edge of a coming orgasm. So close she could feel it, but still building and building the longer she kept this high."
        al "I….Oh…"
        "She couldn’t help herself. She couldn’t stop biting into the sweet tasting fruit. She couldn’t stop fucking herself at just the right pace to keep her moaning and squirming."
        "With all the liquids running over her body, she was making herself dirty. The sticky filth of the fruit’s juices stained her skin, and pooled together underneath her with her own wetness. The strange mixture watered the dark tree."
        "Alexia’s mind had long since faded off. It was lost in the overpowering high that both the fruit and the eroticism of the moment offered her. Instead it was like her body was acting on its own. Like a marionette. "
        "Her empty moaning called out into the distance. It was like a cry to the heavens. How could she even care if she was being too loud? If everyone in the entire castle could hear what a fucking slut she was, that would make it all the sweeter."
        "Her nether region spasmed. Her cunt ache for pleasure. The fire in her body ached for release. The high in her mind ached for complete whiteness. The entirety of Alexia’s being cried out to go over the edge."
        "And it was obliged."
        quest "Cum."
        #cg4
        scene cg303 with fade
        show alexia necklace naked aroused behind cg303
        pause 3
        al "Ah! Ah! Ah!"
        "Alexia gasped and squirmed and spasmed. Her body was in the midst of pure release. The fire that had swept her insides exploded out with all of her energy. It was an eye rolling, mind melting orgasm."
        "In the process, her spasming cunt let loose a torrent of her own juices. It watered the base of the dark tree."
        "When the ghost of the orgasm had passed, it left the limp form of Rowan’s wife, curled up against the trunk. Her eyes fluttered weakly, and her mouth hung awkwardly. Her form was devoid of all strength, all energy."
        "As the fog over her head cleared, a single thought pierced through. If that what was the pleasure of living in a place like Bloodmeen, then why would anyone ever leave?"
        "But, that thought was followed by a second, less accepting one. A curiosity. Why had she done that? Didn’t she know that she shouldn’t have approached the tree? After all, it was surely magic. It had to be trying to do something to her."
        "...Something…"
        quest "Is this where you heard that noise from?"
        "Alexia blinked awake. There were voices in the distance, figures talking. With that realization, came the second realization that she was naked and covered in filth."
        quest "Do you think it’s some kind of infiltration?"
        quest "Idiot. Since when can humans fly?"
        "Alexia scrambled to her discarded dress, and threw it on as quickly as she could. That had been a fun...diversion, but it would be better if no one found her. Especially not like that."        
        scene bg14 with fade
        show alexia 2 necklace happy at midleft with dissolve
        show jezera happy at midright with dissolve
        "Later on, that same day, another odd occurrence happened. Alexia was walking down the hallway when she ran into Jezera. Her Mistress looked her up and down, as the woman always seemed to do, and kept going."
        "But, as she passed, she let loose a sly little comment."
        je "Someone is looking sunny today. Did something fun happen that I had the misfortune to miss?"
        "Alexia didn’t respond to the demoness. But, when she reflected on the encounter, she realized that Jezera had been right."
        "She really had been smiling."
        $ change_corruption_actor('alexia', +5)
        scene black with fade
        "Alexia has now reached medium corruption. Her reaction to different events and scenes will change as a result. At this rate, Alexia’s corruption will only grow and grow…"
        return




        






