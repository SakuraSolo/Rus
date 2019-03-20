init python:
    
    event('shoulda_locked_the_bathroom', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), group='alexia_barmaid', priority=pr_npc)
    event('no_caravan_comes_through', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), group='alexia_barmaid', priority=pr_npc)
    event('stranger_in_a_strange_land', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), group='alexia_barmaid', priority=pr_npc)
    event('a_reminder_of_home', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'", 'all_actors["alexia"].corruption < 60',), group='alexia_barmaid', priority=pr_npc)
    event('just_a_bit_of_fun', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'", 'all_actors["alexia"].corruption > 29',), group='alexia_barmaid', priority=pr_npc)
    event('lifes_a_marketplace', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    event('a_wifes_suspicions', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'", 'rowanGaySex > 2',), group='alexia_barmaid', priority=pr_npc)
    
    
label shoulda_locked_the_bathroom:

scene bg21 with fade
show alexia barmaid concerned at midleft with dissolve
show indarah neutral at midright with dissolve

"Indarah and Alexia looked into the store room. Sounds had been rumbling from it for a few minutes, and it had them concerned." 
"What they found...wasn’t great."
"A naked orc, lay gurgling next to a pile of wine jugs. Some were broken. Some were empty. His woozy movements and vacant demeanor told them where the missing wine had gone."

ind "Drunken sod. Help me move him."

"So, Alexia and Indarah spent the next half hour getting the orc back to his company. They offered to pay for the damages, but figuring out how much had been lost as a result of his little adventure was hard to judge."
"Sometimes running a place where people got drunk could be a pain."

$ castle.treasury -= 5
return

####################################################################################################
####################################################################################################
####################################################################################################

label no_caravan_comes_through:

scene alexia_tavern_1 with fade

"There aren’t always travelers passing through this area. The land path through the Rakshan Wastes can be quite treacherous, after all."
"This week, the inn proved quiet. Boring even."
"Alexia and Indarah spent much of the time playing cards. Indarah knew many strange games from her island homeland, and she passed the time by showing Alexia some."
"Alexia lost at first, of course. But, she quickly wrapped her head around the often inane rules of the different games, and by week’s end she could boast that she was actually quite proficient at a number of new games." 
"As time allowed, they did long term chores, like noting what beds needed repairs and replacement. Maintenance prevented the entire week from being a loss. Still, they would have to report back to the castle that income would be slow."

$ castle.treasury -= 5
return

####################################################################################################
####################################################################################################
####################################################################################################

label stranger_in_a_strange_land:

scene bg21 with fade
show alexia barmaid shocked at midleft with dissolve

"The front door was opened, followed immediately by a loud crashing sound. It roused Alexia, who’d retired to the back room for her lunch. When she rushed to see what had happened, she saw a man dressed in rags. He’d stumbled in and collapsed on the ground."
"It was a few hours before he was in the condition to speak again."

scene black with fade

"He was a caravan guard who’d been protecting a shipment of wheat that was being transported overland into the Empire of Sand. It was good paying work, but always dangerous. The Rakshan Wastes did not always abide."
"Strange monsters had struck in the night. The man couldn't describe them well. Even talking about them made his voice shake."
"The last that he’d seen of his comrades, they were being torn apart, limb from limb. He only survived himself by making a cowardly run for it. He lived. His friends didn’t. "
"After that he’d been staggering through the wastes without provisions. Had he not reached this place, he no doubt would have been dead within the day. He thanked them for saving his life over and over again in a hoarse tone."

scene bg21 with fade
show alexia barmaid concerned at midleft with dissolve
show indarah neutral at midright with dissolve

if strangerFirst == True:
    "Alexia listened with steadily mounting horror. Just what nightmares lived out in the waste?"

"They let the man stay at the inn for a few days. He helped out with a few chores to pay his board, but clearly something needed to be done with him."
"Eventually, they settled on sending him back to Castle Bloodmeen. He had combat training. He could be useful as a mercenary still. After that, Alexia was a little bit more reluctant to wander outside while working."
"Perhaps there were good reasons few ventured into the wastes…"

$ change_recruitment_bonus('barracks', 1)
$ strangerFirst = False
return

####################################################################################################
####################################################################################################
####################################################################################################

label a_reminder_of_home:

scene alexia_tavern_1 with fade

"The highlight of the week was when a band of flour merchants from the south stopped at the rest point. Their red hair and fair skin singled them out as Rosarians."
"The Rosarian traders were kind and friendly. They questioned Alexia about the part of the country she came from, and marveled at the fake story she’d come up with for how she ended up in this desolate part of the world."
"Some of the men had even been to Arthdale before, and they fondly recounted a summer fair that they’d attended some years back. Hearing about it brought a smile to Alexia’s face."
"They’d even brought some games from the south with them. Pastimes with balls and sticks that the teenage boys would sometimes play. Alexia watched lazily as some of the men passed the time by playing."
"It almost felt wrong. Like she was a voyeur to a world that didn’t exist."
"When the caravan left, her mood soured a little. Had it not been for Jezera's pendant around her neck, she would have no doubt asked to go with them. They were a tantalizing taste of home."

return

####################################################################################################
####################################################################################################
####################################################################################################

label just_a_bit_of_fun:

scene alexia_tavern_1 with fade

"This week, Alexia woke up one day with a strange tingle in her spine. Working could be so boring sometimes. She wanted some fun. Just a bit of fun."
"So, when a caravan stopped in later that day, Alexia pounced on the opportunity. She convinced Indarah to let her work the bar, and she made the most of it."
"She was all smiles and flirts. When she made a drink, she’d bend low to give the patrons a view of her chest. Men pinched her ass or told lewd jokes, and she told lewd jokes back."

if get_actor_flag('alexia', 'andras_influence') >= 5:
    "At one point, she ended up on one of the men’s lap. She used the opportunity to squirm a lot, purposefully grinding her rear all over his most sensitive spot. Knowing she was doing something so lewd was...thrilling."
    "Suffice to say, he left a big tip."
    
if get_actor_flag('alexia', 'jezera_influence') >= 5:
    "At one point, she ended up sitting next to the caravan’s one female member, drunkenly locking lips together. All around the room, the men cheered. She didn’t know what she liked more. Their reaction, or the other woman’s lips."
    "By the time they were done the men were practically throwing tips at her."

"As the evening wore on, the room broke out into songs and toasts. Alexia was right there with them, singing and toasting. She even showed off her dancing skills. The audience whistled at every smooth shake of her hips."
"Eventually, most of the newcomers were fast asleep, in the rooms or in their carts. A slightly dazed Alexia went back to the bar to review her earnings. She’d make a lot today."
"Sometimes, being a slut paid off."

$ castle.treasury += 5
return

####################################################################################################
####################################################################################################
####################################################################################################

label lifes_a_marketplace:

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve
show indarah neutral at midright with dissolve
show clamin neutral at edgeright with dissolve

"Alexia walked into the bar room. It was sparsely populated, with only Indarah and a few goblins. The goblins sat at the bar, drinking deep from various odd coloured ales. At their centre was a familiar face."

cla "Oh, don’t play that game with me. I’ve got thirty crates of Rosarian Sweet Wine, collected from a very accommodating quota manager, and I need to sell it somewhere. "
cla "What kind of friend would we be if I didn’t let you know about a special opportunity?"

"Indarah seemed unperturbed by Cla-Min’s excited squawking."

ind "Maybe. But, you must think me a wee girl if you think I’m going to take that swill off your hands for ya. There’s a reason no one’s taken it. You’ve probably already been sitting on it for months."
ind "Years maybe."

"Cla-Min rolled her eyes, but quickly found a new angle."

show clamin happy at edgeright with dissolve

cla "See. It’s aged! Means you can sell it for more."

ind "You ain’t going to make a customer outa me today. Do you ever put a plug in that whole routine of yours?"

"Alexia rolled her eyes and brought her mop to the floor. Cla-Min was the same wherever she went. On more than one occasion, she’d found the goblin matriarch whispering in dark corners with guardsmen and servants in the castle."

show clamin neutral at edgeright with dissolve

cla "Life’s a marketplace. You stop selling for a minute, and you’ll miss a customer. No wonder you ended up out here in the middle of nowhere."

"That was right around when Cla-Min actually noticed that Alexia was there. Cla-Min’s eyes lit up with recognition when she noticed her."

cla "The Competition! What a surprise."

"Alexia opened her mouth to say something, but then thought better of it. For the first time, Indarah’s confident expression cracked. It showed real concern."

cla "Found work I see. All the way out here too. Not a fan of castle life?"

show alexia barmaid angry at midleft with dissolve

al "Oh I love being a prisoner. Can’t you tell?"

cla "It’s alright, darling. You wouldn’t see me cooped up so far away from the rest of the world. Bloodmeen is a fascinating place to visit. But, it’s so far from the arteries of the world."

"Alexia raised an eyebrow."

al "Why even stop in here then? You have portals you could use. If you find Bloodmeen to be dull, then surely our little neck of the woods would be positively lifeless."

"Cla-Min chuckled to herself, and took a swig from her pink drink."

cla "You don’t believe I’d come just to check in on my friend, Indarah?"

ind "No one believes that."

cla "Such rudeness. I put up with a lot, Indarah. You’re lucky you have such forgiving friends."

ind "We don’t strictly need help supplying this place, because of the portals. But, Cla-Min is responsible for the castle’s supply stock. So when I need something, that normally means running it through her."

"Cla-Min giggled and raised her glass in a toast."

cla "Nothing like a captive market!"

show alexia barmaid happy at midleft with dissolve

"Alexia leaned against the bar. One of the goblins was ogling her, but she didn’t pay it much mind. Working as a barmaid meant getting used to being eyed up."

al "You’re really milking this trading deal with the twins for all it's worth."

show clamin happy at edgeright with dissolve

"Suddenly, the smile on Cla-Min’s face grew a shade darker."

cla "Oh, this is nothing. You haven’t even seen milking yet. I assure you…"
cla "I’m the best at it."

show alexia barmaid concerned at midleft with dissolve

"Alexia backed up a step. The implication of her words were hard to miss."

if helayna_escaped == False:
    "Alexia had more than enough competition for husband, absent an assertive goblin hungry for his seed."
    
else:
    "Alexia wasn’t exactly the greatest fan of this woman making lewd innovations about her husband, every time they were in the same room together."

al "I’m sure I haven’t."

"Cla-Min whispered something into the ear of the goblin sitting to her left. He promptly scrambled over to another open seat."

cla "Sit down, sit down. You and I should have had a proper conversation about him a long time ago. No one knows about his...preferences more than you do."
cla "You’re a reasonable young lady. I’m sure some kind of arrangement can be worked out."

"Before Alexia could even process what Cla-Min was suggesting, Indarah interjected into the conversation."

ind "As riveting a thing to listen to as I’m sure it would be, Alexia is not free at the moment. She has work to do."
ind "Get some food started, will you?"

"Alexia didn’t need to be told twice. She rushed off to the kitchen, thankful for an excuse to duck out of the conversation. She half suspected that Cla-Min would have tried to slide a husband sharing contract into her hand before the next round of drinks could even be served."

return

####################################################################################################
####################################################################################################
####################################################################################################

label a_wifes_suspicions:

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve

"Alexia looked out of the room she was cleaning, and saw two men walk by. They were stumbling slightly. It seemed like they were going back to their room after having a bit too much of the bar’s ‘hospitality’."
"She met eyes with one of the men. He was slim and muscular with dark brown hair."
"There was the sound of the door slamming right after. Alexia thought little of it at the time."
"But, fifteen minutes later, when she was crossing the hallway to another room, there were a series of strange rhythmic bumps emerging from the room."

show alexia barmaid aroused at midleft with dissolve

"Alexia pressed her ear to the door, but what she heard quickly brought a blush to her cheek. She scrambled away, lest she be discovered peeping. The sounds from the room were ones she knew well. Sex."

show alexia barmaid concerned at midleft with dissolve

"That moment lingered in her head for the remainder of the evening, as she went about the busy work of making sure everything was ready for the night."
"The strange part was that try as she might, she couldn’t even tell why it occupied her mind this way. After all, it wasn’t like Alexia didn’t know that men did things with other men. How could anyone live in Bloodmeen for months and not realize that?"
"Eventually it dawned on her. One of the men had looked so much like Rowan. Had she almost imagined that Rowan was the one going into the room with the other man?"
"In the morning, Alexia was working near the rooms again. The entire time, she had one eye on the door of the room that the men were sleeping in."
"When it opened, the two men walked out yawning. She had been right. The brown haired man really did look so much like Rowan. It was no wonder she’d thought about him. He winked at her as he passed by."

show alexia barmaid shocked at midleft with dissolve

"But, then right after them, a woman walked out too. Her long blond hair was disheveled and sloppy. Alexia exhaled loudly."

show alexia barmaid neutral at midleft with dissolve

"Clearly she’d just been silly up until now. Why had she just assumed that there wasn’t a woman involved?"
"She kept on sweeping the floor, standing still in one spot. Someone walking past might wonder why she was spending so much time on that one spot."
"Maybe...maybe it was the fact that he looked so much like Rowan…"
"But, why would she associate Rowan with…"

menu:
    "Pretend nothing is off.":
        $ released_fix_rollback()
        show alexia barmaid happy at midleft with dissolve
        "Alexia shook her head. That was just silliness, of course. She was a wife who barely got to see her husband because of all the time he spent working. Of course she sometimes missed him. It was natural to focus on people’s similarities to him."
        "And thinking that the two men has been sleeping together?"
        "Well, she hadn’t seen the woman walk in. Based on what she knew, it was the most logical assumption."
        "Alexia moved to another patch of floor."
        "She was just worrying herself over nothing. Rowan was the same man he always had been deep down. She was sure of that."
        $ change_corruption_actor('alexia', -1)
        return
        
    "Question Rowan’s sexuality.":
        $ released_fix_rollback()
        show alexia barmaid concerned at midleft with dissolve
        "Just now, she’d associated Rowan and men...who were interested in other men... together…"
        "Why would she do that?"
        show indarah neutral at midright with dissolve
        ind "Is everything alright?"
        "Her boss was standing behind her with a concerned look on her face. Alexia fixed a smile on her lips. Best not to show what was wrong."
        show alexia barmaid happy at midleft with dissolve
        al "It’s nothing. Just got lost in my own head for a second."
        ind "Alright...just...keep on working. You polish that corner much longer and it’s going to start to glow like rubies."
        "Alexia laughed and moved to work on another spot."
        hide indarah with dissolve
        show alexia barmaid concerned at midleft with dissolve
        "But, once she was gone, Alexia’s frown returned. There was just no escaping it."
        "She never used to think about it, bur Rowan really did seem to act almost...flirtatiously with other men sometimes. She must have noticed it in the past, but it had become more noticeable since he’d arrived at Bloodmeen."
        if rowanFutaAnal or rowanFutaSuck == True:
            "She knew for a fact that he enjoyed playing with another penis. Her own dalliance with a succubus seemed to show that."
        if ghThreesome == True:
            "When they had been together with Greyhide, Rowan certainly didn’t seem to have minded the presence of another man…"
        "Did Rowan like other men? It was hard for her to say."
        "What’s more...what did that mean about his feelings for her?"
        show alexia barmaid neutral at midleft with dissolve
        "She shook her head. The longer she thought about this, the deeper in the trap she would get. It would be best...best not to think about it much further."
        "Yet, she knew that it would be hard to stop thinking about entirely. Once a box was opened, it was hard to close."
        $ change_relation('alexia', -3)
        return
