init python:
    
    event('mary_event_4', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('more_with_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('hanging_with_the_maids', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', priority=pr_npc)
    event('I_got_your_back', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('alexia_and_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    event('girl_of_ill_repute', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('more_with_mary',), group='alexia_maid', run_count=1, priority=pr_npc)


#Mary Event 4
label mary_event_4:
scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

"Alexia plodded down the hallway towards the servant’s quarter wiping the sleep from her eyes. Today’s shift was set for quite early in the morning. She was replacing a maid too sick to work. The fact that there were sick days for the servants seemed quite odd."
"Would Jezera really allow that?"
"She was considering that fact all the way until she opened the door to the changing room." 
"When she opened the door she discovered she was not alone."

#Mary’s “Interesting” Body
scene black with fade

"Mary was standing near the clothing pile, rifling for a uniform. Her lithe form was entirely naked. Alexia blinked twice in confusion."
"It was not that she had not seen a naked woman before. Or that there was something unusual about seeing a naked female body in the changing room. It was the specific naked female body she was staring at."
"Her body had clearly been heavily modified. Gleaming golden ring piercings hung from each nipple. But, that was just the start of it. There were a string of piercings at her navel as well. But, more shocking still was what was between her legs."
"A single small gold ring was clearly attached to her clit. But, other rings seemed to line each side of Mary’s lower walls. It was like her pussy had been built to be laced up."
"But, there were also all that tattoos. The word “Slave” written right above her privates. The pair of purple handprints etched around her breasts. And the image of two women engaging in...relations...tattooed in intimate detail on her side."
"Alexia just stood in place, shocked. Who would let their body be marked with such filthy...degrading...things. It made her look like such a slut…"
"Alexia brushed a hand over her own right side."

scene bg14 with fade
show alexia 2 necklace shocked at midleft with dissolve
#show mary naked

"Mary didn’t appear to have noticed Alexia’s presence. She was too busy focusing on one of the skimpy maid outfits she liked to wear. When she’d found the one she wanted, she turned her back towards Alexia."
"Alexia still just stood in place as Mary bent over to work the dress up her hips. Of course, there was a pattern on the small of her back. Though, Alexia proved unable to focus on making it out, when her eyes were glued to Mary’s pert backside. Alexia shifted her posture."
"The entire thing was uncomfortable. It was like she’d seen something private. Trying not to make a sound, she hurried out the door. She could change when Mary was done."

scene bg18 with fade
show alexia maid shock at midleft with dissolve
show mary neutral at midright with dissolve

mary "You’re looking at me funny. Is something wrong?"

"Alexia shook her head, perhaps a little too fast."

show alexia maid neutral at midleft with dissolve

al "No, I’m not. You’ve got such an imagination, Mary."

show mary happy at midright with dissolve

"Mary rolled her eyes and giggled. Then she went back to cleaning, though the persistent smirk on her face made Alexia think that Mary didn’t believe her. Alexia ran a hand down her side."
"Had Jezera been the one to do that to her? Had Mary wanted her body marked up that way? If it had been against her will, it sure didn’t seem like she was too unhappy about it." 
"Were the other maids marked up like that too?"

if all_actors['alexia'].corruption < 31:
    "Alexia decided she didn’t want to know. She didn’t want to think about it. There was work to do anyway. Alexia went back to cleaning, and tried her best not to stare at Mary. She was able to stop herself. Mostly."
    
else:
    "Alexia squirmed slightly. As degrading as the thought was, perhaps there was something to the idea of being marked...the permanence of it…"
    "If she kept working as a maid, did that mean that…?"
    "Alexia decided it would be best not to think about it too much. She had work to do. Though, her productivity throughout the day was somewhat limited. Working with Mary was...distracting."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

#Hanging with the Maids Event (Repeatable)
label hanging_with_the_maids:
scene bg14 with fade
show alexia maid neutral at midleft with dissolve

"Today, Alexia was working from the kitchens, bringing meals over to some of the higher ups who could not be bothered going down to main hall and getting food for themselves. Naturally, Skorded, Jezera, Cliohna, and Andras were all on her delivery list."

if all_actors['alexia'].flags['andras_influence'] > 5 and all_actors['alexia'].flags['andras_influence'] > all_actors['alexia'].flags['jezera_influence']:
    show alexia maid aroused at midleft with dissolve
    "Naturally, Andras took the opportunity to make her feed him. It was hard to explain to the kitchen staff why it took her so long."
    show alexia maid neutral at midleft with dissolve

elif all_actors['alexia'].flags['jezera_influence'] > 5:
    show alexia maid aroused at midleft with dissolve
    "Jezera had, of course, chosen today to lounge about in strategic nudity. She took the opportunity of Alexia’s presence to have her do a few menial chores. By the time that Alexia returned to the kitchen, her cheeks were tomato red."
    show alexia maid neutral at midleft with dissolve

else:
    pass
    
scene alexia_maid_1 with fade

"However, for the most part the day was mostly monotonous. One did not expect to change the world when assigned to housework, but this was especially mindless work. Eventually settled in with a few other maids to engage in some gossip."
"She was pretty disconnected from the social circles of the servant’s quarter. Unlike them she stayed in the suites and could interact with anyone at any time. But, there was something sweet about their conversations about who was friends with who, and who was sleeping with who."
"It almost reminded her of gossip with the girls back at Arthdale. That reminder made her sad for a second when she remembered them. Almost like Arthdale. But, not Arthdale."
"Alexia came away from it with a greater sense of camaraderie with the serving staff. Bloodmeen was a living thing, and these people and their everyday lives and struggles were the blood flowing in its veins."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

#I Got Your Back
label I_got_your_back:
scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show mary neutral at midright with dissolve

"Alexia moved her duster back and forth over the antique vase. It certainly needed it. This segment of the castle hadn’t been occupied since the last war, and it was very much not fit for human habitation."

al "Oh no!"

"While not paying attention, she’d accidentally used a bit too much force. The vase fell over off its pedestal and crashed on the ground."
"Alexia jumped to her hands and knees, trying to grab up all the pieces. Fuck. What was she going to do if anyone found out? Just how valuable was this thing?"

mary "As much fun as you are in that position, you should move out of the way for a second."

"Alexia turned to the side to find Mary, standing there with a broom. With her help, the mess was entirely swept up in seconds."

show mary happy at midright with dissolve

mary "Don’t worry about it. If anyone asks, I’ll just say that it was badly situated on the pedestal. Since no one can flog you, as the general’s wife, everyone will probably just let it go."

"Mary gave Alexia a reassuring wink." 
"It was good to have friends."

return

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

#The Girl of Ill Repute

label girl_of_ill_repute:
scene bg14 with fade
show alexia maid neutral at midleft with dissolve

maid "Did you hear about Mary and Agnes?"

"Alexia’s ears perked up. She was one table over from the two maids who were chatting, setting silverware."

omaid "Agnes this time?"

"The first maid chuckled softly."
"Why was she always the voyeur?"

maid "Yup. The little runt must have fucked her way through half of the serving staff by now."

omaid "So what happened?"

maid "Falisiona went to the storeroom, and found Agnes with a strap-on buried in Mary. They didn’t even stop either."

omaid "I bet they were hoping Falisiona would join in. Wouldn’t be Falis’ first go around."

"Was Mary really that sexually active with the other maids? She knew that Mary liked girls, and that she had a flirtatious manner to her. But, Alexia hadn’t expected it to be such a routine occurrence…"
"She briefly even considered going over to the neighboring table and asking for more details."

omaid "So wait, is that why the two of them weren’t in rotation today?"

maid "I can only imagine."
maid "If I’ve heard of it, that means the Mistress has heard about it. And you know that she enjoys little miss cunt-munchers antics."
maid "She probably brought them in for a private viewing."

"The other maid rolled her eyes, but didn’t show much surprise. This probably wasn’t the first time Jezera had called up some of the maids this week."

omaid "So wait? Have you ever…?"

maid "Slept with Mary?"

omaid "Yeah, that."

maid "No way. They told me I didn’t have to fuck anyone when I took this job. I’m cleaning houses, not here to whore around."

"The other maid giggled."

omaid "That must be why the taskmistress assigned you the bad cot."

"The topic turned further away from Mary, and with it so did Alexia. She was mostly thinking about her friend." 
"Of course, it all made sense. It wasn’t like Alexia didn’t know that Mary was a bit of a bitch-in-heat. But, she didn’t know that Mary had that kind of reputation. And there was also the bit about Jezera keeping up with her antics…"

if maryKissLiked == False:
    show alexia maid concerned at midleft with dissolve
    "The thought brought a pit to Alexia’s stomach. Even if her friend might enjoy it, being the subject of Jazera’s attentions couldn’t be good for Mary. Perhaps Jazera might even be responsible for her current...reputation..."
    return
    
else:
    show alexia maid aroused at midleft with dissolve
    "Did that mean though, that before...when Mary kissed her...that it was because…"
    "Alexia shook her head quietly."
    "Still, the idea of what was no doubt happening to Mary at that exact moment lingered. Being forced to fuck another person as a show for another person..."
    "Having your body, your sexuality, everything private used as a way of entertaining someone else... "
    "Captured by her eyes…"
    "Alexia shook her head again. She had work to do."
    $ change_corruption_actor('alexia', 3)
    return