init python:

    #Lost and gifted
    #Requires tavern, and early enough in the game for the item to be useful.
    event('lost_and_gifted', triggers="week_end", conditions=('week >=4', 'castle.buildings["tavern"].lvl > 0'), group='ruler_event', run_count=1,
        priority='pr_ruler_high if week > 10 else pr_ruler')
    #Caravan delayed
    event('caravan_delayed', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Extra Equipment
    #Requires forge, forge must be less than level 3, and have at least 5 iron income.
    event('extra_equipment', triggers="week_end", conditions=('week >=4', '0 < castle.buildings["forge"].lvl < 3', 'castle.iron_per_week >= 5'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Forge breakdown
    #Requires forge
    event('forge_breakdown', triggers="week_end", conditions=('week >=4', 'castle.buildings["forge"].lvl > 0'), group='ruler_event', run_count=1, priority=pr_ruler)
    # Warning about famine
    # Triggers around week 28 (high priority starting then?), explaining how the famine is going to affect you and what you can do about it.
    event('warning_about_famine', triggers="week_end", conditions=('week >= 27',), group='ruler_event', run_count=1, priority='pr_ruler_high if week > 28 else pr_ruler')


label lost_and_gifted:
#Lost and gifted
#Requires tavern, and early enough in the game for the item to be useful.

scene bg6 with fade
show indarah neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Yes, how can I help you?"

show rowan necklace happy at midleft with dissolve

ro "Oh Indarah. Good to see you again."

ind "You as well.  I, had a rather strange guest last night at the tavern. They never spoke and I never saw their face. They just dropped the coins for a room on the counter and then left for the night."

"After breaking eye contact contact with him, Rowan noticed that Indarah was nervously fidgeting with the frills on her skirts."

show rowan necklace neutral at midleft with dissolve

ro "I take it something strange happened or you felt unsettled by them?"

"A frown creased her forehead for a moment, then was gone."

ind "I hate dealing with secretive people. I'd much rather know exactly how threatening you are upfront. Show me what you got so I know what to expect and all that."
ind "I didn't even notice them leave, but when I went to check in the morning they'd gone. The bed had been slept in, so I know they used the room, but not much else."

ro "So, maybe they were just a quiet traveller then?"

ind "Maybe. They did forget something in the room, nothing fancy but I thought you might be able to use it or have Cla-Min trade it since the traveller didn't come back for it."
ind "Better than just leaving it sitting around or maybe pawning it off to a random merchant comes by."

"She indicated a package sitting on Rowan's desk."

show rowan necklace happy at midleft with dissolve

ro "Alright, thank you."

"With a sweeping bow, Indarah took her leave."

hide indarah with moveoutright

#Inform player of item they got. This is a random item from the early game, probably equipment.
$ get_rnd_item(0, 300)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label caravan_delayed:
#Caravan delayed
#No requirements

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show clamin neutral at midright with moveinright

ro "There you are! What's kept you so long? I was worried something had happened."

"The entire goblin caravan had been gone missing last week and there'd been no word throughout the morning and into the early afternoon. Rowan was relieved to finally see her matriarch arrive so he could learn what had kept them."

show clamin annoyed at midright with dissolve

cla "Something did happen. A bastard merchant guild woman decided to have my caravan detained, for 'health and safety concerns'. Horseshit."

ro "So that's why you were delayed with your supply shipments this week? When will you be able to bring things in?"

cla "The supplies, my stocks, and half a dozen business opportunities all gone because some city trader doesn't like competition in the silver trade of all things."

"Her irritation was palpable and she'd started grinding her teeth in frustration, much to Rowan's discomfort."

ro "Wow, that's pretty harsh. Were you looking to get some cash to cover a bribe or something to get out of there?"

show clamin angry at midright with dissolve

cla "At least some gold would be something I could stand as a business expense. Can you believe that the only bribe she's willing to accept is one of my sons!? Either that bitch has a thing for green boys or she's got her eyes on starting a slave trade."

"After taking a deep breath, the goblin woman managed to calm herself down. A crease of worry now crossed her face instead of rage."

show clamin neutral at midright with dissolve

cla "Look Rowan, I've got to get back there as soon as I can. My family's still stuck with the guild thugs, I came here to let you know what was up in the meantime. A mother can't just abandon her kids to someone like that."

ro "Alright, I understand. We should be able to manage with our existing stores for another week or two while you get that sorted out."

cla "Thanks hun. It goes without saying that as much as I'd like to take your money, I can't exactly sell you anything today. Hopefully things will be back to normal next week."

hide clamin with moveoutright

"Well, that meant paperwork and using up some of the deep stores intended for sieges or emergencies, but at least Rowan had the peace of knowing what was going on now."

#Cla-MIn's shop is disabled this week and the caravan cannot be visited.
# TODO:
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label extra_equipment:
#Extra Equipment
#Requires forge, forge must be less than level 3, and have at least 5 iron income.

scene bg22 with fade

#rowan tired
show rowan necklace neutral at midleft with dissolve

"A very fortuitous event had occurred this week, as an extra large shipment of iron had come in from the mines. While this on its own wouldn't have meant much more than a trickle of extra income, Andras had decided to make it mean something more."

show andras displeased at midright with moveinright

an "No slacking! Drink, then keep working!"

"A mug of fluid was forced into Rowan's hands and he eagerly drank the substance."

hide andras with moveoutright

show rowan necklace happy at midleft with dissolve

"Feeling new energy and strength flow into his body, Rowan allowed a smile to form on his lips. He watched Andras for a moment moving throughout the forge, delivering both demands and more drafts to his conscripted workforce for the day."
"The second seemed to be the far more effective method of keeping production going. Rowan decided to log this trick for rushing production in the back of his mind that the demon seemed to have stumbled on. Then turned back to his own station."
"It had been some time since he worked in a forge. The man was well versed in regular equipment maintenance out in the field, but rarely ever worked in places like these. Such a stuffy and sweaty environment was something he prefered to avoid."

show greyhide neutral at cliohnaright with moveinright

gh "Have you finished that plate?"

"Using some tongues to lift and turn over the hot metal he'd been hitting for the past thirty or so minutes, Rowan inspected his work."

ro "Looks like it."

"Then he quenched the metal in a bucket and used a rag to wipe some of the sweat from his forehead. It was looking more and more like they might actually get through all the iron by the end of the day after all."

ro "Odd to see this place bustling with so much activity."

gh "Yes, I wonder if perhaps I fear this will be my future down in the depths."

show greyhide sad at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve

ro "What do you mean?"

gh "We are building and equipping an army, something I cannot hope to do alone. Therefore, a larger forge with more people will be built, eventually."
gh "I think I am afraid of when that day comes. I wonder if I will even notice."

"Before the hero really had a chance to think of a response, Greyhide had provided a new plate to work on to Rowan and taken away the old one."
"As he raised his hammer to pound the new slab of metal into shape, similar philosophical introspection started to plague Rowan's thoughts."

#Get 10 extra pieces of equipment this week.
$ castle._equipment += 10
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label forge_breakdown:
#Forge breakdown
#Requires forge

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

gh "I am so sorry about this."

ro "Please calm down, it will be fine. I'll take care of things."

gh "No! I cannot let you just take the blame for my failings."

"Rowan sighed inwardly. He was touched that Greyhide was willing to take a punishment like this so that he didn't have to, but no one really needed that. It was unlikely that what had happened would get past Rowan's desk anyway."
"In the ongoing efforts to improve equipment production for the armies, Rowan had put together a reclamation program for old equipment and had Greyhide train some apprentices to repair the gear."
"The experiment had been a disaster, at least for the moment. While the principles were sound, Greyhide had proven to be less than capable as a master for his apprentices."
"They had managed to severely damage the forge in the scant time they'd been working in it and all equipment production had to be halted while replacements were acquired."

ro "Greyhide!  Stop, what is done is done. This situation is no one fault, specifically. As much as Andras would love to torture or kill someone for the damage done, it will get us nowhere."
ro "For now, we must simply fix things and then make sure it doesn't happen again."
ro "Promise me right now that you will not go to our master and beg him to punish you in my stead, that would hurt me far more than you realize. I depend on you here in the castle, so don't throw your life away."

gh "Such kind words, yet I cannot help but feel I never can deserve it. How can I possibly accept someone who is under such burdens take even more onto himself?"

ro "It's just who I am. Please, trust me on this."

gh "Very well, the whelp will hear nothing of this from myself. I promise."

show rowan necklace happy at midleft with dissolve

ro "Thank you."

gh "I wish I could do something else to honor you for what you did."

ro "Well, since you won't have much more work today, why don't you stay up here and we can chat a bit? I'd love to hear a little more about yourself. Going through the castle finances isn't the most demanding thing to do."

show greyhide neutral at cliohnaright with dissolve

gh "Then, what about me do you wish to know?"

ro "How about you tell me how did you come to be a blacksmith?"

show greyhide sad at cliohnaright with dissolve

gh "There is little to tell on that subject. Smithing and metalworking is simply a task I took up as a way to avoid fighting. My people are a little less likely to want to prove themselves against you if you make their weapons and armor."
gh "I learned by watching and testing.  It took time, but my skills have grown much since the first time I struck an anvil."
gh "Once I had iron, anvil, and knowledge, my tribe suddenly had the power to leave the safety of the mountains and go to the towns on the coasts."

show rowan necklace neutral at midleft with dissolve

gh "They like being able to raid and steal from the humans, something they can rarely do while unarmed. Sadly, this drew attention to us. So we end up fighting different battles. I was glad when the welp gave me a way out of it."

ro "Strange how different things can turn out than we expect."

#Lose next two weeks of equipment production, iron is sold instead.
# TODO:
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label warning_about_famine:
# Warning about famine
# Triggers around week 28 (high priority starting then?), explaining how the famine is going to affect you and what you can do about it.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

os "'umies green thingies not do well in tribe. So now we hunt'n."

ro "Thank you. You're dismissed."

hide orc soldier with moveoutright

"It was as Rowan had feared. Harvest had come, and come with a ruined crop."
"The story was the same across the whole realm. That same strange blight that had appeared last year and destroyed what had been a promising harvest had been even worse this year."
"With fall settling in, most of the livestock had already been slaughtered and the peasantry had been forced to turn to heavy hunting to stay fed."
"That wasn't going to last through winter, especially with what stores that were left had been essentially confiscated by the nobility."

show clamin happy at midright with moveinright

cla "Hey Rowan, you wanted to see little old me?"

show clamin neutral at midright with dissolve

"The bounce in her step faltered as she got close and sensed the mood in the room."

ro "Yes, this is about the food situation in Rosaria."

cla "Uh, pardon sir, but what does that have to do with me?"

ro "I want to know if your caravan can do supply runs for the villages. Essentially buying supplies from the other Six Realms and bring relief to those starving people."

show clamin annoyed at midright with dissolve

#If no trading villages in Rosaria
cla "Begging your pardon, but goblins aren't exactly too popular in Rosaria. I'd absolutely love to take advantage of the situation for a little profiteering off the sods, but-"

#Else
# TODO:
#cla "I'm already doing that with the villages you made trading deals with. Don't doubt I wouldn't make take advantage of the situation where I can. The rest of those poor sods can shove it where the sun don't shine."

#rejoin
show rowan necklace angry at midleft with dissolve

ro "DAMN IT!  Cla-Min, those are {i}my{/i} people!"

cla "And I'm talking about the safety of {i}my{/i} people. My family is not welcome in Rosaria, not anymore. The caravan was attacked on the roads just last week!"
cla "Cla-Kes, my grandson, came out of that with a broken arm, he's just a boy!"

"The two glared at one another for a long moment. Then Rowan closed his eyes and took a deep breath. Echos of activity rung through the halls, amplified by the acoustics of this great stone cavern."

show rowan necklace neutral at midleft with dissolve

ro "Fine. However, your caravan can go to the occupied villages and bring them food."

show clamin neutral at midright with dissolve

"Now it was the trader matriarch's turn to rock on her heels and take a long moment to compose herself. Once again the noises of the castle were all that filled the air. Rowan thought that maybe he could hear Andras shouting something from far below."

cla "That we can do, assuming you either provide the food or cover the expenses."

ro "We've got the stores captured from Raeve Keep, since we've left only a skeleton garrison there, it isn't like they need all of them. If we need more, we can pay out of the treasury for it. Keeping our subjects alive is an expense I can justify to the twins."

"Cla-Min nodded."

cla "Do you need us to start right away?"

ro "No, not yet. They can still manage for some time yet. When things get bad, I'll call on you to do a relief run. It probably won't be the only time we need to feed my, no, our masters' people."

show clamin happy at midright with dissolve

cla "Alrighty then. Since I'm doing a little favor for you here, how about you do one for me? Like I said earlier, we can't trade in Rosaria anymore. Unfortunately this means that I'm unable to do some rather lucrative trades in the capital city."
cla "Perhaps you might be able to go on my behalf? My items are fairly small and perfectly legal. Funny, isn't it? The goblin isn't allowed in when she actually wants to do a fair trade."
cla "If you can make it there in the next four weeks, there'll be a nice little finder's fee for you."

ro "I'll keep my eyes out if I get the chance."

cla "Great! See you around."

hide clamin with moveoutright

"With his excitable subordinate gone, the hero returned his thoughts to the threat of death by starvation to the people of Rosaria. He still had a chance to do something before the situation got worse. Raeve Keep wasn't the only noble stronghold that would have food stores in it."
"That was cold comfort considering what he'd have to do to actually get those food stores. Still, capturing fortresses was still helping towards the twins conquest and came with the extra benefit of helping feed the people in any villages he helped capture."
"Unfortunately, that didn't help those who were still free. If he wanted to do something to help all of Rosaria... well perhaps visiting the capital sooner rather than later wasn't such a bad idea. The baron must have plans for the famine and it would give a better idea of what's happening."
"(Visiting Rastedel, the capital of Rosaria, is not yet implemented)"

#Side quest for Cla-Min's legal goods is activated (does nothing until Rastedel is implemented).
# TODO:
return
