init python:
    #Orientation
    #Triggers the first time that Alexia is assigned to work in the forge.
    event('forge_orientation', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), run_count=1, group='alexia_forge', priority=pr_story)
    #Injured on the job
    #No requirements.
    event('injured_on_the_job', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), run_count=1, group='alexia_forge', priority=pr_npc)
    #Missing iron found
    #No requirements.
    event('missing_iron_found', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), run_count=1, group='alexia_forge', priority=pr_npc)
    #Alexia doesn't like forge work
    #No requirements
    event('alexia_doesnt_like_forge_work', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), run_count=1, group='alexia_forge', priority=pr_npc)
    #Fun with Metalworking
    #No requirements (Alexia is not a mother?)
    event('fun_with_metalworking', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), run_count=1, group='alexia_forge', priority=pr_npc)
    #Staff come by to help
    #Requires that there be more iron than the forge can use (otherwise event would do nothing)
    event('staff_come_by_to_help', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'", "castle._iron > castle.buildings['forge'].capacity"),
        run_count=1, group='alexia_forge', priority=pr_npc)
    #How did Greyhide come to Andras's attention?
    #No requirements.
    event('how_did_greyhide_come_to_andras_attention', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), run_count=1, group='alexia_forge', priority=pr_npc)
    #Generic event 1
    #repeatable
    event('alexia_forge_generic1', triggers="npc_events", conditions=("get_actor_job('alexia')=='forge'",), group='alexia_forge', priority=pr_npc)


label forge_orientation:
#Orientation
#Triggers the first time that Alexia is assigned to work in the forge.

scene bg22 with fade
show greyhide neutral at skorright with dissolve
show alexia 2 necklace concerned at midleft with moveinleft

al "Good morning, mister Greyhide. Uh, Rowan told me to help you down in the forge."

"The great beast set down his tools and stretched his body out. Then he turned to face her for a long moment."

al "If this is a bad time, I can come back later."

gh "Have you ever worked a forge before?"

al "No."

gh "Does your small frame hide a great strength?"

al "No."

gh "Have you experience with weapons and armor?"

al "No."

gh "Then our need for equipment must be far greater than I realized for Rowan to send you here. I will endeavor to make as much use of your help as I can."

al "Uh, are you saying I won't be able to do much?"

"In response, the minotaur walked to the edge of the room, pulled a heavy apron off a rack and threw it at Alexia!"

show alexia 2 necklace shocked at midleft with dissolve

al "Ooph!"

"She almost fell over at the impact, but managed to keep her feet."

gh "Put that on. You can be my assistant."

show alexia 2 necklace concerned at midleft with dissolve

al "Are you sure about that?"

gh "You'll probably be better than most of the orcs here are."

scene alexia_forge_1 with fade
pause 3

"For the rest of the week, Alexia worked in the castle's forge as Greyhide's assistant. For the most part, it was all about figuring out exactly what Alexia could and couldn't help out with."
"Her small physique made her a poor candidate for a blacksmith, so most tasks were either beyond her strength or it took her so long to complete them that there was little point. After the first day it was clear that she wouldn't be hauling things around or using a hammer or tongs."
"Eventually she found a sort of niche with working the bellows, tempering iron that had already been worked, and running messages to the rest of the castle. By the end of the week, managing the movement and supply of iron around the castle had become her principle duty."

scene bg22 with fade
show greyhide neutral at skorright with dissolve
show alexia forge neutral at midleft with dissolve

gh "I would say that your time was not wasted here, in the end."

al "Well, I can thank you for that."

gh "I do not hold it against you that forge work is not your calling.  We must all sometimes do things that we find distasteful. Know that I will not mind your help again, should it be needed. Nor will I hold it against you should you decide never to help again."

al "Yeah, thank you Greyhide."

"She used a handkerchief to wipe a significant amount of sweat off her forehead."

al "Have a good evening."

gh "You as well."

$ alexiaForgeIntro = True
$ do_job_forge('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label injured_on_the_job:
#Injured on the job
#No requirements.

scene alexia_forge_1 with fade

"Occasionally while she was working in the forge, Alexia would try to do something more difficult or be assigned a task that she didn't have experience with. Unfortunately, the woman simply didn't have a knack for this line of work and accidents sometimes happened."
"One such case happened early on in the week."

scene bg22 with fade
show alexia forge neutral at midleft with dissolve

"One of blades being worked on had been dropped down into the coals and Alexia took it upon herself to try and fish it out rather than get help. Since she normally didn't handle the blades for more than a few seconds at a time, she had gotten into the habit of not always using her gloves."
"The lesson of why one does so was learned fairly quickly, as the tongues she was digging around in the coals with grew hotter and hotter in her hands until she was forced to drop them in surprise."

show alexia forge shocked at midleft with dissolve

al "Ah! What?"

"Her hands stung and she started blowing on them to try and cool them off."

show greyhide neutral at skorright with moveinright

gh "Did something happen?"

show alexia forge concerned at midleft with dissolve

al "The tongues got really hot..."

"Taking Alexia's hand, Greyhide examined them for a moment and pointed out a few blisters that were forming on her palm where she'd been gripping the metal."

gh "You were not wearing your gloves, so the metal burned you."

"Sheepishly, Alexia put a hand in her apron pocket and pulled out a thick leather glove, realizing her mistake. The stinging wasn't going away and touching the rough material made it hurt worse."

gh "Put them in water, then let them heal. I will take over for you."

al "Okay, um, I dropped a blade into the furnace... and the tongues I was trying to get it back with."

"He glanced into the coals and shifted them a bit with a poker."

gh "They have melted."

al "Oh."

scene black with fade

"There was no permanent damage from her burns, but Alexia wasn't able to do much work until after they'd healed. She effectively wasted most of the week."

#Alexia gets little to no work done, Alexia gains extra stress.
$ do_job_forge('alexia', 0.3)
$ change_actor_stress('alexia', 5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label missing_iron_found:
#Missing iron found
#No requirements.

scene alexia_forge_1 with fade

"One of the few things that Alexia was legitimately competent at in the forge was working as a courier and bookkeeper. That isn't to say that she excelled at it or found it engaging, but at least she wasn't stumbling through everything she did there."
"Before she'd even started working at the forge, they had had a problem with occasional light shipments. Sometimes the amount of iron that arrived in the forge was less than what was reported being sent."
"It wasn't enough to draw too much attention and could easily be explained as an error, but the overall trend of these seemed to suggest otherwise, as there was a lot more shipments that had less iron than more iron."
"This week Alexia happened to stumble on the cause. She noticed one of the orc shippers slip one of the iron nuggets into a satchel while on his way from the portal to the forge. She tailed him after he'd made his delivery, and he led her straight to his stash."
"After reporting the incident to Andras, and the greedy orc made an example of, the iron was brought down to the forge to be put to use. Alexia felt rather good afterwards, since her help had lead to some immediate and obvious help."

#Gain 5 extra pieces of equipment. Alexia loses the stress she'd normally get for working in the forge.
$ castle._equipment += 5
$ do_job_forge('alexia')
$ change_actor_stress('alexia', -5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_doesnt_like_forge_work:
#Alexia doesn't like forge work
#No requirements

scene alexia_forge_1 with fade

"Alexia found working in the forge felt like she was working in front of an open oven. Unfortunately, this wasn't anything so pleasant as cooking. Instead of the warm fresh smell of food, there was the smell of smoke, coal, and sweat. So much sweat."
"Constantly she felt like she was both wearing too much due to the heat, and too little due to the lack of protection against sparks and hot surfaces. There was no work to take pride in, each blade or plate was added to the pile, like the last one."
"Her arms and back felt stiff, her wrists and neck stung from where the heavy leather chafed at her skin. To add insult to injury, Alexia could tell she wasn't very good at what she was doing either."
"Greyhide constantly had to correct her mistakes, or else found the simplest of tasks for her to do."
"No matter how she concentrated or looked at things, nothing ever seemed to make sense or click.  It wasn't like cleaning or cooking at all, there was no easy way to tell when you messed up. Everything was done precisely one way, again, and again, and again."
"She hated this work. However, Rowan needed her to help in the forge. So she helped in the forge. As best as she could, as long as she could, until her darling needed her somewhere else."
"Alexia prayed that Rowan would need her somewhere else soon."

#Alexia gains extra stress.
$ do_job_forge('alexia')
$ change_actor_stress('alexia', 5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label fun_with_metalworking:
#Fun with Metalworking
#No requirements (Alexia is not a mother?)

scene bg22 with fade
show greyhide neutral at skorright with dissolve
show alexia forge concerned at midleft with dissolve

"With a grunt of displeasure, the minotaur put down the last large nugget of iron."

al "All of them?"

gh "Yes, the entire shipment cannot be used."

al "Last one was mostly bad, this one was entirely bad. I don't think we have a choice now, I'll let the twins know."

"She fingered her necklace and informed their masters of the subpar iron. Hopefully there wouldn't be any deaths and they'd just pass on word to the miners about the bad iron."

show alexia forge neutral at midleft with dissolve

"With the message now sent and received, she looked back at Greyhide."

al "Now what? We don't have any work to do, do we?"

gh "No, we cannot make any equipment until a proper delivery arrives."

al "Well, could we maybe use the bad iron for something other than equipment?"

"The minotaur didn't reply for a long moment. Alexia knew this was a sign that he was thinking and gave him some time."

gh "Would you like to make some toys, Alexia? That will be far easier than working blades or sheets."

al "Well, alright."

"She figured she might as well try. If she wasn't any good at that either there wouldn't be any harm done."

scene alexia_forge_1 with fade
show alexia forge neutral behind alexia_forge_1

"Greyhide got her a small hammer that made her think of those that the villagers used to construct buildings with. It felt almost comically small compared to the great tool he normally used."
"Then he walked her through extracting a small piece of iron and turning it into a long small wire which she then twisted into a loop."
"The metal soon snapped due to the low quality of the iron, but actually being able to work metal for once invigorated her, so Alexia kept at it with another."
"After half an hour, she'd managed to make a small figure out of wire holding a sword. Greyhide remarked that it looked like Rowan, which made Alexia blush in surprise. After that, he left her to work on her own."
"She made many more of the wires, then left the forge to weave them in her room. The better part of the day was then passed with her metalworking, twisting several more toys and figures together."
"The whole time she felt like a little boy building and coming up with stories about her creations."
"The thought brought a chuckle to her, then a tear followed it."

al "Someday."

#Alexia can only generate half her usual equipment, but loses stress.
$ do_job_forge('alexia', 0.5)
$ change_actor_stress('alexia', -5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label staff_come_by_to_help:
#Staff come by to help
#Requires that there be more iron than the forge can use (otherwise event would do nothing)

scene alexia_forge_1 with fade

"For once, Alexia's skills and background were actually helping out in the forge. Things were rather quiet in the castle since the twins weren't hosting any guests."
"So after finding this out, Alexia chatted up some of her friends from the staff and found a few that had experience with forge work."
"She invited them to help in the forge to work some of the iron that Greyhide and his normal help weren't able to keep up with. They in turn knew others who could help, who's friends then wanted to join in as well."
"Soon a small crowd of bored maids, butlers, and cooks were crowding into the forge offering to help out. There were far too many of them to all help at once, so Alexia helped coordinate an extra shift so everyone would have a turn."
"Together they managed to do quite well, getting through iron almost twice as fast as Greyhide could normally work. Though their enthusiasm quickly wore off and most of the staff was eager to get back to their normal work at the end of the week."
"For her part, Alexia envied them, wondering if maybe she'd get a chance to stop working in the forge soon too. Hopefully this week would be enough equipment to give her a break."

#Alexia's equipment boost this week is increased to as much equipment as the forge normally can produce.
$ do_job_forge('alexia')
if castle._iron > castle.buildings['forge'].capacity:
    $ event_tmp['bonus'] = castle._iron - castle.buildings['forge'].capacity
    $ castle._iron -= event_tmp['bonus']
    $ castle._equipment += event_tmp['bonus']

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label how_did_greyhide_come_to_andras_attention:
#How did Greyhide come to Andras's attention?
#No requirements.

scene bg22 with fade
show greyhide neutral at skorright with dissolve
show alexia forge neutral at midleft with dissolve

"Alexia watched as Greyhide beat the metal into shape with his greathammer, while she pumped the forge bellows. There was just the loud clanging of the hammer, no words were shared between one another."
"Almost all of the time that Alexia spent working with the minotaur was in silence. Greyhide never started any conversations that weren't directly related to their work and Alexia's tasks were quite simple so he didn't have much to say unless she screwed up."
"So sometimes Alexia would start a conversation herself, just as a way to break up the otherwise monotonous atmosphere."

al "Greyhide, how did you meet the twins?"

"The blows on the metal didn't stop, but Alexia could tell from the shift in his posture that he was thinking about something else now. Usually he didn't respond right away, so she waited a few moments for him to answer her question."

gh "It has been some time since I crossed pass with the foul mouthed whelp. Andras is his name."

"He spoke only while the blade was in the furnace, stopping while beating the metal as it would have been almost impossible to hear him over the many ringing impacts."

gh "At the time he was much smaller, though no less vicious. He had heard about a minotaur smith in the Tail and left his desert behind to find me."

"The blade was flipped over several times as the minotaur inspected his work, then he quenched the blade in water and placed a new one in the furnace. Alexia doubled her efforts to heat the blade up enough for Greyhide to start beating it into shape."

gh "At the time he wanted me to make a weapon for him, to see how his father's weapons were made. I had no idea what he meant, but his magic hurt painfully. So I had no choice but to make him one of my weapons."
gh "Throughout the next day he would watch me for several minutes, then disappear for sometime before returning to see how things were going and learn when I would finish. Impetuous, impatient, and incredibly demanding. The whelp was the same then as now."

"He pulled the blade out of the furnace and placed it on the anvil to start striking. However, he hesitated and spoke again."

gh "I thought him a fool too, but when I finished the weapon he demanded to I explain something he had missed in the construction."
gh "He was paying far better attention than I thought, for when I returned the next day to my forge I found that someone had used it in the night and made a near perfect weapon of his own that lay discarded next to the one I had made for him."

"Now he struck the blade at long last and Alexia thought that was the end of the conversion. She was almost surprised when Greyhide spoke again a few moments later."

gh "That was the only time I saw him before he wanted to bring me here. But I knew the whelp for who he was the moment I laid eyes on him again."

"Well, that was quite the story about Andras."

$ do_job_forge('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_forge_generic1:
#Generic event 1
#repeatable

scene alexia_forge_1 with fade

"This week Alexia spent time in the forge, doing odd jobs to help Greyhide and the other workers. The work was boring, the environment hot and stifling, and the people didn't have the best hygiene."
"Her primary work was moving metal around and documenting it. A trivial task that only took up a little of her time.  The rest of the work was freeing people up from other simple tasks like tempering iron and working the bellows."
"It was quite safe to say that Alexia couldn't name a task that was less pleasant than working in the forge and there was nothing she could take pride in. There was just the grind, the heat, and the smell of sweat and coal."

$ do_job_forge('alexia')
return
