init python:
    #generic event 1
    #repeatable
    event('alexia_barmaid_generic_1', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), group='alexia_barmaid', priority=pr_npc)
    #Unexpected hero
    event('unexpected_hero', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    #Quiet week, let's bond
    event('quiet_week', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    #Legionnaires of Prothea drop by
    event('legionnaires_of_prothea_drop_by', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    #Tavern living standards
    event('tavern_living_standards', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    #Sand's Noble troupe
    event('sand_s_noble_troupe', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    #Night Terrors
    event('night_terrors', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    #Orientation
    #First event when Alexia is assigned to the tavern
    event('barmaid_orientation', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_story)


label alexia_barmaid_generic_1:
#generic event 1
#repeatable

scene alexia_tavern_1 with fade

"This week Alexia helped out Indarah in the tavern. In the mornings she cleaned rooms and prepared meals. In the evenings she worked as a barmaid serving drinks."
"The travellers that visited this tavern were a rough bunch, you had to be to brave the Rakshan Wastes. Many were just happy to have a taste of civilization, hot food, and a warm bed. Others were after the pleasures of drink and flesh."
"Indarah was quite proficient at dealing with unruly patrons, but that didn't stop Alexia from getting several slaps on the bum and crude catcalls. On the flip side, the fact that she was getting tips from her patrons helped make up for it."
"Having extra help around made travellers more likely to stay an extra day, earning the tavern more money for Bloodmeen. The tips Alexia kept, then gave to Rowan when he returned from the week's explorations."
$ do_job_barmaid('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label unexpected_hero:
#Unexpected hero
#No requirements.

scene alexia_tavern_1 with fade

"It was still early, at least for a tavern, when the cry came from outside. Something was happening, Alexia looked up trying to figure out why people were shouting so much."

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve

al "What's going on out there?"

#bell ringing sfx

"Abruptly someone started ringing the bell on the porch ferociously. That meant one of two things, either someone had a very poor sense of humor, or the tavern was under attack!"

show alexia barmaid concerned at midleft with dissolve

al " (I... hope that's just our soldiers coming by, for some reason.)"

scene bg21 with fade
#indarah worried
show indarah neutral at midright with dissolve
show alexia barmaid neutral at midleft with moveinleft

"Quickly she rushed over to Indarah."

al "We aren't expecting any of the twin's boys to come by, are we?"

"She waved her hand in response, then spoke in a hoarse whisper."

ind "No, keep your voice down!"

"A loud crash sounded behind them, a glance back at the entrance revealed that wild orcs had forced the door open and were grinning around at the clientel. They ducked under the countertop, hoping they hadn't been noticed."
"Now truly fearful, Alexia fumbled with her amulet a moment."

al "Jezera, Rakshan orcs are attacking the tavern!"

show jezera neutral behind bg21

je "Ah, I just got the panic signal from Indarah. Don't you worry a thing, help has been dispatched. Just make sure they don't kill anyone for a few minutes."

ind "What are you doing, girl?"

al "Talking to Jezera, she says she's sent help and we should try and stop the orcs from killing anyone?"

"Screams of pain rang out, accompanied by a sloppy crunching sound."

ind "That's easy for her to say, those orcs have weapons, and I'm used to fighting unarmed drunks!"

#if alexia knows any spells
if alexia_ice_shard > 0:
    al "I might be able to get one, maybe two with my ice lances, but there's no way I can take down all of them."

#else
else:
    al "Don't look at me!"

#rejoin
"Now there was a clanging of weapons hitting one another, followed by the impact of wood as someone decided to put the bar stools to use."

ind "Well, at least a couple of our guests know how to fight. Stay down, unless you think you can make a difference."

hide indarah with moveoutright

"Cautiously, Indarah slipped around the counter and out of Alexia's sight. A moment passed, then the sounds of battle seemed to shift and Alexia cautiously peeked up."

"Unfortunately, things had not gone well for Indarah and her guests. One orc was bruised, one bleeding a bit, but all were standing and ready to fight. Their opponents were almost all either down for the count or on the verge of falling."
"Thankfully, it only looked like one of them was actually dead. He was sprawled over a table with a huge dent in his head, bashed in by a club."
"Realizing she could do nothing, Alexia ducked back down as one of the orc men caught Indarah in his hands and quickly subdued the dark skinned woman."

show wild orc neutral behind bg21
wo "Hehehe, you's gots fight in yus. Kinda like orc woman."

femorc "Not like dis bitch."

al "Eh? Ah!"

hide alexia with moveoutleft

scene black with fade

"Alexia was abruptly yanked out from behind the counter and thrown onto the floor in the common room. One of the attackers, a female orc, was the one who'd found her and pulled her from her hiding place."

show wild orc neutral behind black

wo "Looks like we gots two pretty humi girls dis time! One cherry, one olive."

"He poked each of them with his club and chuckled loudly, which his comrades joined in shortly."

scene bg21 with fade

show andras disguised angry at midleft with moveinleft

#If Andras has not been seen disguised before.
# TODO:

$ andras_name = "Stranger"

an "Foul creatures! You dare attack this place? You will die by my blade!"

"Alexia couldn't believe her eyes, a strange man had just leapt in through the broken door brandishing a sword and crying a challenge at the orcs."
"It was almost how she'd imagined Rowan would arrive in the knick of time to rescue her, but that only happened in stories, didn't it?"
"The orcs were quick to answer his challenge, quickly fanning out around him to attack all at once.  At first Alexia thought he would let them make the first strike, then watched in amazement as he suddenly dove forward and skewed the apparent leader through the heart!"

an "Ah ha!"

"Then he spun around quickly cleaved another's head off!"

an "Take that!"

"A surprise attack had already cost two of their six number, but now orcish counter attacks came forth. Alexia felt her heart skip a beat as one nearly struck their savior, but then gasped anyway as the orc seemed to almost literally explode!"
"Gore splashed around, then a moment later it was over."

an "Hmmhmmhmm, you weaklings were no match for my power."

show andras disguised happy at midleft with dissolve

an "Barmaid, get a round of drinks for everyone!  I think I've earned it."

show indarah neutral behind bg21

ind "Yes, right away!"

"As the dark skinned woman hurried to the back of the room, the strange man stepped forward and held out a hand to Alexia, who was still kneeling on the ground."

an "Well my lovely lady, it would seem that I arrived just in the knick of time. Guess that makes me your hero, doesn't it?"

show alexia barmaid neutral at midright with dissolve

"This man was almost annoyingly arrogant, but Alexia accepted his hand anyway and rose with as much grace as she could muster."

al "Yes, thank you very much for your help. Uh, I think I'll go and help with the drinks."

"As she turned away from the man, he put an arm around her shoulder and lead her away from the tavern main floor."

an "There's no rush, I'm sure she can manage on her own."

"Then he noticed that she was fingering her amulet nervously and trying to pull away from him."

an "Oh, you won't need to use that. I have everything under control."

"Alexia was confused for several seconds, worried that something impossible had happened. Then she realized it as the man almost forcefully pulled her into an unused guestroom."

show alexia barmaid shocked at midright with dissolve

al "Andras?"

$ andras_name = "Andras"

an "In the flesh. Well, fake flesh."

show andras happy at midleft with flash

"Then in an instant, he had shifted back to his own form."

#else
#to do

#rejoin
an "What did you think of my performance?"

show alexia barmaid neutral at midright with dissolve

al "A little overdramatic, but you did make a good hero. I think it's the voice that really sold it."

an "Thank you, my beautiful lady. I do rather pride myself on my range, but I don't get that many chances to use different voices. My natural, deep commanding and powerful oration is rather choice my day to day."

show andras smirk at midleft with dissolve

an "And I wouldn't have it any other way."

show andras disguised smirk at midleft with flash

if NTR == True:
    an "Now, let's get back to the floor for something to drink before I get accused of being a rapist myself. We can carry on when you return to the castle."
    an "For now, I think the hero should get his kiss."
    scene black with fade
    "Before she could stop him, the disguised human leaned forward and planted a deep kiss on her lips. It was thankfully brief, and the shocked Alexia didn't get a chance to respond before being swept back into the tavern."
    #alexia gains 3 andras influence
    $ change_actor_num_flag('alexia', 'andras_influence', 3)
    $ do_job_barmaid('alexia')
    return

else:
    an "Now, let's get back to the floor for something to drink before I get accused of being a rapist myself. I could use a drink after all that killing."
    $ do_job_barmaid('alexia')
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label quiet_week:
#Quiet week, let's bond
#No requirements

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve

al "(sigh)"

show indarah neutral at midright with moveinright

ind "Hmm, good morning."

al "It's afternoon, but good morning."

ind "Still nothing?"

al "Nope, really quiet this week."

ind "It isn't out of the ordinary to just have no one coming by. We are out in the Wastes after all."

al "Yeah, seems like a really odd place for a woman from the Dragon's Tail to want to make her home. Why did you agree to come here?"

ind " In short, it was a once in a lifetime opportunity. In the Dragon's Tail, you can't own property unless you're born to the upper class. You call them nobles, we call them captains or chiefs. It depends on which group you're from."

al "Oh, and owning a tavern has been what you've wanted to do all your life?"

ind "A tavern, a ship, a castle, I've wanted lots of different things. When I was a girl, I travelled all along the islands trying to find a place I could become a chief, then a captain, and finally just a place to call my own."

ind "What about you, Alexia? Any childhood dreams you're chasing?"

al "Well, not really."

ind " Nothing? Never even wanted something childish like flying as a bird or getting your hands on some really fancy jewelry?"

al "My dreams were really silly. I wanted to be like my mother, I wanted to be loved by the people around me, I wanted to make my kids feel like I did growing up. Yours are a lot more interesting."

ind "I don't know, you can tell a lot about someone from their dreams. We were from different worlds, with different experiences under Solansia's laws. I can't fault you for being happy trapped in that bondage just because I was not."
ind "Especially considering our present situation."

#if Alexia has not had a child
# TODO:
ind "Do you mind if I ask why you haven't had any children yet?"

#alexia barmaid angry
show alexia barmaid angry at midleft with dissolve

al "I do mind."

ind "Then consider the matter dropped."

#else
#to do

#rejoin
ind "Why don't you tell me a bit about your home?"

show alexia barmaid neutral at midleft with dissolve

#Alexia earns a little less money for Rowan.
$ do_job_barmaid('alexia', 0.8)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label legionnaires_of_prothea_drop_by:
#Legionnaires of Prothea drop by
#No requirements

scene bg21 with fade

"A somewhat shocking arrival at the tavern this week was a company of Prothea Legionnaires."
"Abruptly in the middle of the afternoon a squad of the white clad soldiers bearing the mark of Solansia marched into the tavern floor, catching Alexia and Indarah rather off-guard. Being the first to recover, the red haired woman welcomed them and asked if they'd be staying here."
"With an affirmative from the commander, she set to work allocating rooms. When she returned, she was surprised to see that Indarah was still shocked into silence and the commander was becoming suspicious of her."

scene bg21 with fade
show alexia barmaid shocked at midleft with dissolve
show indarah shock at midright with dissolve

al "What's wrong?"

"She'd apologized for needing to take her boss away for help and then pulled Indarah into a side room."

ind "I... this can't be real. How... how did they find out about us? They'll kill all of us!"

show alexia barmaid angry at midleft with dissolve

al "No! Calm down. Look, they're not attacking us, just some more travellers looking for a place to sleep and escape from the Wastes for a time."

ind "It's over... it's all over..."

show alexia barmaid concerned at midleft with dissolve

al "Come on, get it together.  Look, uh, I'll take over the bar, you deal with their rooms, okay?"

"All she got was the barest hint of a nod. For the moment, that was good enough for Alexia and she returned to the common room."

hide alexia with moveoutleft

scene alexia_tavern_1 with fade

"Upon returning to the floor, Alexia immediately started preparing food and serving drinks as quickly as she was able. There were a total of thirty legionnaires in the group, all human, along with a priest to heal injuries and offer spiritual guidance."
"Rather than directly interacting with the commander right away, she instead asked for some information from the others as to why they were in the Wastes. After a few drinks she was able to learn that they were hunting orcs."
"There wasn't a specific group they'd been sent after, this was simply one of the teams that were about the Six Realms cleansing the remnants of Karos's forces. This was an important duty that these people were honored to take part in."
"While the commander was still suspicious of the two women running this place, he'd come to the conclusion that some deal had been struck with orcs to leave her tavern alone. This was evidently not a crime significant enough to pursue and he let them be."
"This wasn't enough to help Indarah completely overcome her terror, and she spent much of their stay still unsteady and nervous. As such, Alexia essentially found herself running things for the week, giving her the lion's share of the tips."
"Even so, it was quite a relief for both of them when the company finally left."

#Alexia earns extra money.  Alexia gains some stress.
$ change_actor_stress('alexia', 5)
$ do_job_barmaid('alexia', 1.3)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tavern_living_standards:
#Tavern living standards
#no requirements

scene alexia_tavern_1 with fade

"Alexia never really felt like she belonged in the castle. Bloodmeen was not only a place of demons, but it was a place of high class and wealth. Being, and still thinking of herself as, a peasant woman meant that she always felt an alien or invader while walking the halls."
"Sleeping there was even worse. Large stone rooms filled with fancy furniture had very different acoustics to the small wood and mortar rooms filled with simple furniture that Alexia had lived her entire life in."
"Simultaneously things were both louder and quieter. The creaking of wood in the wind was completely absent. Rarely do you think of things that are strange by not being there, but when they're gone they can be the most jarring of all."
"Here, however, things were familiar. Wind and creaking were back. The patter of rain on the thatch occasionally played. Alexia could imagine that she was just out on a trip or resting at the inn while her home was being repaired."
"She actually belonged, rather than constantly being a fish out of water being toyed and taunted by her betters."
"Indarah was a hard woman, but a fair one. Here there was no need to always look over one's shoulder or worry that your boss would be about to jump you. Plus the slightly lower quality bed actually felt better to sleep in than what had once felt like heaven, but now was just a cage."
"Well, until the next time she noticed her amulet again."

#Alexia loses a little stress.
$ change_actor_stress('alexia', -5)
$ do_job_barmaid('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label sand_s_noble_troupe:
#Sand's Noble troupe
#No requirements.

scene alexia_tavern_1 with fade

"Among the more unusual guests that sometimes visited the tavern were nobles. Rarely would one ever leave their fiefs for anything but events with others of their class, let alone their realm. That is to say nothing of those who would brave the wastes rather than the sea."
"Still, sometimes an entourage would make their appearance. Alexia had the distinguished honor of welcoming a high ranking nobleman of Sand to the tavern during this week."
"It seemed that he was acting as a diplomat or ambassador of some kind, but essentially just kept to himself during his stay in the best room of the house. Instead, the ones who flavored this period were the knights and servants accompanying him."
"Well, at least they sort of where what Alexia had an image of in her mind of what a knight was. Sands's gentlemen were somewhat different from Rosaria's. Their code was still Solansia's, but their traditions and mannerisms were completely alien."
"Speaking to them reminded the woman of the stories she'd heard from Rowan about his travels around the Six Realms. Of all the different cultures that he'd encountered and learned about. Alexia wished that he was here, not for the first time, but for once it would have been for advice."
"One of those lesser nobles took a shining to Alexia, and not in a good way. He was one of those people who enjoyed having power over others. There was no place for duty, honor, or order in his heart."
"When she rejected his advancements and attempts to entice her, he began to harass and stalk Alexia. Eventually she retreated back to the castle for a day or two at Indarah's suggestion, until the nobles left."

#Alexia's boosted income and money is halved this week.
$ do_job_barmaid('alexia', 0.5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label night_terrors:
#Night Terrors
#No requirements.  Not corrupt Alexia?

#tavern backroom
scene bg21 with fade

#creak sfx

show alexia necklace neutral behind bg21

al "Hmm."

#cracking sfx

al "Hah!"

hide alexia
show alexia necklace concerned at midleft with dissolve

"Alexia woke with a start and glanced around the room hurriedly, trying to find the source of her discomfort."
"Then she saw it, something was forcing its way into the window to her room!"

al "Solansia help me..."

"The strange shadowy beast managed to wrench the window open and started forcing itself inside. Its form was indistinct, seeming to change with every shift in the tiny bit of light that was inside the room."
"Alexia inched along the wall, hardly taking her eyes off the beast and feeling around for anything that might help her. A loud clang sounded as she knocked over a chair, sending the beast into a frenzy. Now Alexia let out a shriek of terror, it knew she was here!"


#If Alexia knows ice lance spell
if alexia_ice_shard:

    #alexia eyes closed

    "Desperately she brought her hand forward and tried to summon the discipline needed to focus her magic. She jammed her eyes closed for a moment, then felt the power come forth!"

    show alexia necklace angry at midleft with dissolve

    "Ice dripped from her hand, her eyes shot open and locked with the creature just as it managed to clear the window. It growled unnaturally in her direction, then let out a shuddering gasp as the lance of magical power struck its center."
    "Leaving nothing to chance, Alexia immediately followed up with another one as fast as she could."

    show alexia necklace concerned at midleft with dissolve

    "The beast seemed to explode into thousands of small fragments of black as the second shot hit home, leaving the room silent save for gasping breaths and a pounding heart."
    "A moment later, the sound of pounding footsteps came from the hallway."

    show indarah shock at midright with moveinright

    "The door to the room flew open, allowing Indarah to rush into the room holding a lantern."

    ind "What is it Alexia?!"

    show alexia necklace neutral at midleft with dissolve

    al "Some kind of creature broke through the window, I think I killed it with magic?"

    "Bringing the light forward, the damage to the window came into focus, along with the impact sites of Alexia's two attacks. All that remained of the creature was small flecks of shadow on the ground that rapidly disappeared in the lantern light."

    show indarah neutral at midright with dissolve
    ind "A night terror. They seem to come from the ruins north of here, thankfully they don't come to the tavern that often. Those shadows won't kill you, but they will terrorize your dreams and feed on you lifeforce if they can get to you."

    ind "Nice job taking it out. Since that window is in pretty rough shape, let's move you to another room for the night. We'll worry about repairs in the morning."

    #Alexia loses a little stress.
    $ change_actor_stress('alexia', -5)
    $ do_job_barmaid('alexia')
    return

#else
else:

    "She grabbed something off the table and threw it towards the thing. The object passed right through it, then clattered to the floor. Another object soon followed and proved to be equally ineffective."
    "Now just trying to flee, Alexia stumbled around the table trying to get to the door to her room. Her eyes locked with the creature once more, just as it cleared the window and started towards her!"
    "Her body felt like it suddenly went numb with cold and her limbs were molasses. They just wouldn't follow her mind's commands fast enough! The shadows got closer, closer..."

    scene black with fade
    show alexia necklace concerned behind black

    al "No..."

    "Suddenly, light! Warmth!"

    scene bg21 with fade
    show alexia necklace concerned at midleft with dissolve
    #indarah serious
    show indarah neutral at midright with dissolve

    al "Wha? Indarah?"

    ind "Glad to see you're okay. I heard you scream and dragged you out of there, we're safe in the common room now."

    al "What was that thing?"

    ind "A night terror. They seem to come from the ruins north of here, thankfully they don't come to the tavern that often. Those shadows won't kill you, but they will terrorize your dreams and feed on you lifeforce if they can get to you."

    ind "They can't stand light, so we should be fine in here tonight with the fires high."

    #alexia eyes closed
    al "Thanks for saving me."

    ind "Don'ch you worry about it."

    #Alexia gains some stress.
    $ change_actor_stress('alexia', 5)
    $ do_job_barmaid('alexia')
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label barmaid_orientation:
#Orientation
#First event when Alexia is assigned to the tavern

scene bg21 with fade
show indarah neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

ind "There you are, a fine afternoon to you. Welcome to my little island in the wastes. I am Indarah."

show alexia 2 necklace happy at midleft with dissolve

al "Alexia, it's good to meet you."

ind "How does it feel to be out of the castle?"

show alexia 2 necklace concerned at midleft with dissolve

"Alexia fiddled with her necklace for a moment before she replied."

al "Different. It's been a long time since I was in a place that was actually plain and homely. Though I'm afraid the scenery is actually even drearier here than back at Bloodmeen."

show alexia 2 necklace shocked at midleft with dissolve

al "Uh, sorry. I shouldn't have said that."

show alexia 2 necklace neutral at midleft with dissolve

ind "Think nothing of it Alexia. The setting of my abode is very much an advantage in the trade."
ind "Normally our isolation would make it hard to keep the bar stocked and the larder supplied, but our little friends have solved that problem thanks to the network."

show indarah neutral at midright with dissolve

ind "I do advise you to keep your door locked and windows bolted at night."

ind "Now, why don't we take a look at some outfits for you while I go over what you'll be helping me with here?"

show alexia 2 necklace happy at midleft with dissolve

al "Alright, please lead the way."

hide indarah with moveoutright
hide alexia with moveoutright

scene alexia_tavern_1 with fade

"Being a baker's daughter, Alexia had some experience when it came to dealing with customers. Her extensive practise at domestics during the war also lent itself well to the various tasks that needed to be done around the tavern."
"Between shifts on the floor, she'd be cooking big pots of food, cleaning dishes, washing floors, and laundering bedding. It would not be inaccurate to say she excelled at these tasks. Dealing with the merchant caravans and occasional travellers serving drinks was a different matter."
"While most were decent enough, there was almost always someone who had wandering hands or who tried to put the moves on her. At least twice that week Alexia had to rely on Indarah to come and rescue her from a rowdy drunk."
"At least the tips she was getting and encouragement from Indarah helped make her feel better about the catcalls and harassment. At least there were occasional free nights since no one was in the tavern."
"An advantage of being out in the middle of a barren, monster infested, wasteland."
$ do_job_barmaid('alexia')
return
