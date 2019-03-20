init python:
    
    event('rastedel_introduction', triggers=('map_res_106', 'map_res_107'), group='rastedel', priority=pr_map_res)
    
label rastedel_introduction:

if not goal2_completed:
    "Rowan stopped in his tracks and looked out into the distance. There, sitting on the river, was Rastedel in all of its glory. Stinking, noisy, Rastedel. He knew that heading that way would be dangerous. The arrival of the hero of the previous war in the capital could not be hidden."
    "What would Jezera think if she discovered him there without her knowledge?"
    "Better not to risk it. Rowan turned away."
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

else:
    pass
    
if postBattleVisit == True:
    jump rasPostBattleVisit

elif rastCurrentEnd == True:
    scene bg33 with fade
    "More content to come in the future. Stay tuned for the next build."
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

elif rastFirstVisit == False:
    jump rastMenu

else:
    pass

#######################################################################################################################

#First Visit

#rowan's arrival CG
scene black with fade
show doran beardless neutral behind black
show rowan necklace neutral behind black

"There it was. A gust of wind blew over the tall grass on the side of the road. Rowan parked his horse. Seeing this, Duke Reave pulled his to a stop as well. Rowan just wanted to look at it. He had not been back here in so many years."
"Down below them was Rastedel. The capital of Rosaria and home of the nobility. Rowan sighed. A place that held so many memories."
"The first thing he noticed as they approached was the sight of the Grand Codifice in the distance. Its eight towers are the tallest buildings in the city. There, the High Arbitron runs her bi-weekly sermons in the name of Solansia." 
"Now, from the hilltop, he could look at it in all of its glory. He could even see the movement of tiny figures up and down the boulevards. Rastedel was always alive. Always moving and squirming."
"The city itself was on the fork of a river. The north side was entirely taken up by the lower class districts. Endless pathways of bakeries, bars, and brothels. The river separated them from their more well to do brethren."
"The South East side was somewhat more upscale and was the center of industry. The merchant guilds, the granaries, the smiths, and the mining companies that dominated the east were all settled there. It was also where one went when looking for a doctor or other professional."
"And to the South West was the home of the nobles. The smallest part of the city, it was a collection of estates, servants homes, fine stores, and military facilities." 
"But, its most striking feature was the shining shimmering palace where the Baron lived. Its gardens were an unparalleled marvel in all of Rosaria, and its size and splendor was bested only by the Codifice on the other side of the river."
"In the last days of the war, especially after Bloodmeen had fallen, this place had been his home. There was still a fondness for it in his heart. Among other things."

dor "We must get on with it. It is expected of us."

"Rowan turned to the man. Duke Raeve was a hollow shell of his former self. Not only had Jezera taken his beard, but his pride. He now searched around any space he was in with a nervous expression. It was a good thing that so little was expected of him."

ro "Onward then."


scene bg33 with fade
show rowan necklace neutral at midleft with dissolve
show doran beardless neutral at edgeleft with dissolve

"At the gates, the soldiers didn’t even try to stop him. One of the guards moved to approach."

show rosarian knight neutral at midright with dissolve

rkn "Halt travelers. Where are you coming from?"

"The guard blinked twice, surprised at what he saw."

rkn "Rowan Blackwell? Goddess above. Let him through, let him through!"

hide rosarian knight with dissolve

"And just like that, the two riders were allowed entrance into the city."
"Rowan looked around and breathed in the scent. Where else was there like Rastedel?"
"The stink from the garbage and manure from the streets mixed with that of the fish from the river. The lines of buildings, entwined like lovers, stretching for miles. There was always someone on the street, always someone talking, always movement." 
"And the people. Louder and bolder than those of the villages by ten. Some dirt poor and reduced to rags. Other wearing whatever fashion had become common. It was a place built atop itself in so many layers that it had fused into a cohesive and distinct whole. "
"Smelly, massive, hopeful, flawed Rastedel."

cro "Rowan?"

"The guards were not the only ones who swiftly realized who the two newcomers were. A few people who had seen him in the parades of years before started to notice."

cro "Rowan’s here?"

"A murmur went down the street. Rowan rode with his back held high. He may have been accompanying a duke, but no one paid much attention at all to Doran. People pointed and chatted."
"Rowan rode down the long central boulevard. Every stretch saw the streets more and more filled. People opened second and third story windows to look down at him. Before long, the streets were mobbed by a crowd of people. They called out to him from all sides."
"It was like an impromptu celebration."

show rowan necklace happy at midleft with dissolve

"Rowan waved to the people. Being beloved had never been his goal, nor his addiction, but who wouldn’t feel a bit of energy when so many people showed so much affection for him."
"The people looked disturbingly similar to how he’d seen them last. That had been in the immediate aftermath of the war, when easy access to food was just being restored." 
"The hollowness of some of the cheeks he saw was a testament to the famine. Here too, it wreaked havoc in the form of higher bread prices. But, the people still looked in good spirits, and cheered earnestly at his approach."
"Doran bristled softly at all this attention, but didn’t protest as Rowan stopped to be greeted by several veterans. Rowan didn’t know them, of course, but they claimed to have fought by his side. A large matronly woman thrusted a small pastry into his hands."
"But, the ruckus was soon broken up by the arrival of five knights. In gleaming armor and strong horses, they immediately drew attention. But, Rowan’s eyes most lit up at the sight of the neat purple cloaks swept over their armour."
"They were of the Thorns of Solansia, the oldest and most exclusive knightly order in the entirety of Rosaria. The second sons and cousins of Dukes, Earls, and Counts had all pined for a spot in their ranks for generations."

show werden neutral at midright with dissolve

"And at the front of their ranks was a man a much older than the others, with armour a bit more ceremonial as well."

werd "Duke Reave. Rowan Blackwell."

show rowan necklace neutral at midleft with dissolve

"Rowan narrowed his eyes. He knew the man very well. He had commanded the Thorns during much of the last war. Duke Antoine Villele of Werden." 
"Rowan had fought at the side of this man’s brother at Karst. He’d actually fought with him too at Bloodmeen, but that didn’t mean there was much camaraderie between them. Duke Antoine didn’t share camaraderie with commoners."

ro "My lord..."

"The Duke and his entourage rode up to Rowan and Doran. Rowan controlled his emotions and kept a neutral expression. He remembered how frustrating the Duke could be to talk with. He didn’t suffer conversation."

werd "I had not expected you to appear, Lord Raeve. When your keep fell and no word came of your arrival, I assumed you lost."

"Doran clenched his teeth. Duke Antoine turned to Rowan. Rowan made sure to meet his gaze at equal level."

werd "I had not considered all the variables. Rosaria seemingly finds itself in the debt of Rowan Blackwell yet again."

"He put a hand to his chin."

werd "Hmmm."

"Suddenly the older man’s eyes brightened. He turned his steed around and gestured to be followed. The Thorns under his command spaced themselves out to push through the crowd."

werd "Follow. The Baron will need to speak with you immediately. Both of you."

"He was quite insistent on the matter. There was no room for debates. Rowan and Doran moved to follow. Still, Rowan was skeptical. Why was a Duke doing the dirty work of escorting them to the Palace?"

$ rastFirstVisit = False

jump rastMenu

#########################################################################################################################

label rasPostBattleVisit:

$ postBattleVisit = False

#Rowan comes to Rastedel Variant 2
scene black with fade

"There it was. A gust of wind blew over the tall grass on the side of the road. Rowan parked his horse. He just wanted to look at it. Despite having been back recently, Rowan was looking at a different Rastedel."
"It still stank. It still stretched out over the riverbed. The bearer of memories, and the home of disappointments."
"But, the city was quiet today. There was no subtle hints of movement down below in the city. There was not the usual clattering of activity. Even from a distance, the bustle of figures would still be visible from here. But, today nothing. Dead quiet."
"Well, at least it still stank. So there was that."
"Rowan spurred his horse onward. The city was waiting for him."

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

"At the gates, Rowan wasn’t even checked. There were no troops in front of the gate stopping anyone from entering the city. A few guards patrolled the top of the walls though. They had dark circles under their eyes. Probably had been pulling multiple shifts back to back."
"They just let him through. He seemed human enough. Besides, the only people going through the gate was the odd person, here and there, who was leaving the city."
"The path he tread through the city was equally desolate. It wasn’t that there was no one on the street. It was just that there was no life. Everyone out had their head down and was just trying to get somewhere. No crowded boulevards and loud conversations."
"The windows and doors were all closed. A cloud of fear hung over the city."
"The last time he had come, people had thronged the streets to see him. The Hero of Karst in flesh and blood. This time no one came out to greet him." 
"It wasn’t that he was unnoticed. As he went, doors and windows creaked open. Eyes peeked out to see if it was really true. If he was really back. But, no one rushed out to greet him."
"He finally ran into someone with an interested in a longer conversation when he reached the main square. The silent spirals of the Grand Codifice hung like a phantom over the city below."

show rowan necklace happy at midleft with dissolve

ro "Well met, Inquisitors."

"A pair of blue clad guardsmen approached him on foot. Their bright blond hair gleaned in the sunlight. Inquisitorial Guards were Protheans. The direct defenders of the High Arbitron of whichever region they were assigned to. Naturally, they’d been left back from the fighting."

if avatar.corruption > 59:
    ro "Cunts."

inq "Good day, Rowan Blackwell. When Her Beatitude the High Arbitron heard of your arrival, she dispatched us at once. She would most kindly like to bestow a blessing of protection on you."

"Rowan scratched the top of his head. That seemed like a pretext to him."

#if deception high (TODO)
    #"Probably an excuse to get him alone in a room with her."

"He’d intended to visit Ameraine and the ever valiant Duke Raeve first upon arrival. Surely they were waiting for him. But, if Marianne was calling for him, it was probably best not to offend her by blowing her off."

ro "Of course. I will speak to her at the earliest convenience."

"The guards gestured for Rowan to follow them."


menu:
    
    "The Grand Codifice":
        $ released_fix_rollback()
        jump rastCodifice
    


##########################################################################################################################
#Town Menu

label rastMenu:

scene bg33 with fade

menu:
    
    "The Palace.":
        $ released_fix_rollback()
        jump rastPalace
        
    "The Noble Lodge" if rastLodgeAccess == True:
        $ released_fix_rollback()
        jump rastLodge
    
    "The Northside Alleys" if rastAlleysAccess == True:
        $ released_fix_rollback()
        jump rastAlleys
    
    "The Grand Codifice" if rastCodificeAccess == True:
        $ released_fix_rollback()
        jump rastCodifice
    
    "The Trade Guild." if rastGuildAccess == True:
        $ released_fix_rollback()
        jump rastGuild
    
    "Back to map." if palaceStage !=1:
        $ released_fix_rollback()
        $ prevent_tile_exploration()
        $ push_to_previous_tile()
        return
