# events for specific resources on map

init python:

    # tutorial village
    event('first_village_captured', triggers='map_res_100', run_count=1, priority=pr_map_res)
    # Tutorial Mine event
    event('tutorial_mine', triggers=('map_res_6', 'map_res_7', 'map_res_8',), run_count=1, only=True, priority=pr_story)


label first_village_captured:
#when Rowan discovers the first village
$ renpy.block_rollback()

#village outskirk CG

scene black with fade
show rowan necklace neutral at midleft with moveinleft

"As Rowan approached the village of Briarbridge, he let out a long sigh. Being the closest neighbor to Arthdale, this was a place that he'd been to many times. He knew the people, he knew the families, and now...."
"He touched the tracking medallion in the way he'd been instructed to make contact with Andras."

ro "I'm at the village, what do you want me to do?"

an "Scout out their defenses, determine how much of a resistance they can muster against an attack, and locate the weakest point."
an "Today is a mission of conquest, but in the future there will also be missions of... destruction."

"The demon savored that last word, relishing the intonation of each syllable. Rowan felt sick."

an "Occupying villages will give us regular income to support larger and larger armies. Destroying them will give a large amount of loot immediately as well as valuable prisoners, assuming we have space in our dungeons for them."
an "Of course, we can't do either if we can't spare the forces to defeat the defenders.  In that case we'll have to leave and come back later."
an "Oh, and there's one more thing. As I'm sure you're well aware, villages have a nasty habit of supplying soldiers and \"heroes\" to their homelands. Each of them we take will weaken the ability of the realm they're in to defend against our eventual conquest."
an "Not by much, but it will add up."
an "Now go and gather intelligence.  I will ready the orcs, they're eager to get started."

scene bg1 with fade

"It was an almost surreal moment for Rowan, walking through the village and getting all the friendly waves and inquires to his health and wellbeing from the villagers."
"Many times he contemplated fleeing and forgetting the whole thing, but in the end he did make his report to Andras."

#Show soldier selection interface.  Only option is orcs, and the village's military strength is ~30 (6 orc losses).

an "As our armies expand, we will need to decide which of our forces we risk on these expeditions. Losses are simply a fact of conquest."
an "The orcs are ready, wait there for my arrival."

"Rowan made his way to the edge of town, trying desperately not to think about what was going to happen that evening. He waited away the hours, guilt constantly gnawing away at him."
"That was until shortly before evening...."

show rowan necklace neutral at midleft with moveinleft

qm "Rowan?  You *are* back!"

ro "Yes, I, I...."

show village elder happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

ro "I...."
ro "(Oh no.)"

show rowan necklace neutral at midleft with dissolve

el "What's wrong, my child? I haven't gone to meet the Goddess yet if that's what you're thinking."
el "Please tell me, what of Alexia? What happened in Castle Bloodmeen?"

ro "Old friend, why are you here? Were you not going to Rastedel?"

el "These old bones aren't meant for the big city. I never felt comfortable and needed to go back to Arthdale in case you returned. Briarbridge was the natural place to live in the meantime."
el "But that shouldn't be your worry. Please, where is Alexia? I thought that-"

play sound "music/SFX/VillageBells.ogg"

"The loud ringing of alarm bells interrupted their conversation, and Rowan felt like the world had fallen out from under him for the second time. Heedless any further words from the village elder, he ran away from Briarbridge."

hide rowan with moveoutleft

scene black with fade

"The hero of the siege of Karst fled, fled until he could hear the sounds of battle no more, and cowered in a grotto far from the roads."
"..."
"A little over an hour later."

show bg4 with fade
play music "music/burning village loop.ogg" fadein 1.0
show orc soldier neutral at edgeright
show andras displeased at midright


show rowan hood neutral at midleft with moveinleft

an "Ah, servant, so wonderful for you to join us. Your report was quite helpful, I was able to eliminate the defenders with minimal losses. The remaining villagers have been made to understand their new situation."

show andras happy at midright with dissolve

an "Very well done."
an "I even found an old friend for you."

ro "What?"

show village elder wounded at edgeleft with moveinleft

el "*Coughing* Wait, Rowan?  What's going on?"

#elder eyes closed

"Andras roughly pushed the old man onto his knees before addressing the crowd of scared onlookers."

an "Not much, there's just going to be a bit of an execution. I want to make things clear what will happen for disobedience."

"The red demon turned to Rowan and spoke quietly enough that the crowd couldn't hear them."

show andras angry at midright with dissolve

an "Draw your sword, boy, and sever this wretched thing's head from its neck. If you don't, I'll order the deaths of a dozen villagers at random."

menu:
    "Kill the elder.":
        $ renpy.fix_rollback()
        stop music
        "Without saying a word, Rowan stepped forward and drew his blade from its scabbard."
        "He looked down at the man he'd known his whole life, that had helped him through so much. The hero squeezed his eyes shut for a moment as tears started to stream down his face."
        "Then he raised his blade and brought it down."
        # sword sfx
        show bg4 with sshake
        show bg4 with redflash
        play sound "music/SFX/BodyfallDirt.ogg"
        hide village elder with dissolve
        show andras happy at midright with dissolve
        an "Ah. That was beautiful."
        ro "..."
        scene black with fade
        #Rowan gains guilt, castle income increase from village is 1 higher.
        $ avatar.base_guilt += 3
        $ castle.villages += 1
        $ castle.villages_income += 6
        #End of event. Give player summary of event: Village was occupied, how many orcs were lost, and how much income increased by.
        #return to castle for week end
        $ codex_add('village_elder_killed_by_rowan')

    "Refuse.":
        $ renpy.fix_rollback()
        "Rowan simply stood there for a moment, then he slowly shook his head."
        show andras happy at midright with dissolve
        an "Fine then. Captain, have your men gather some subjects."
        "As the screams and cries for help are renewed around them, the village elder tries to stand back up and speak again."
        el "Why is this happening? What are you trying to do?"
        stop music
        show andras angry at midright with dissolve
        an "Shut up old man."
        show bg4 with sshake
        show bg4 with redflash
        play sound "music/SFX/BodyfallDirt.ogg"
        hide village elder with dissolve
        an "The weak and frail are no use to me."
        ro "Why?"
        an "I told you, to demonstrate what happens when there is disobedience."
        ro "..."
        #Rowan gains less guilt.
        $ avatar.base_guilt += 2
        $ castle.villages += 1
        $ castle.villages_income += 5
        #End of event. Give player summary of event: Village was occupied, how many orcs were lost, and how much income increased by.
        #return to castle for week end
        $ codex_add('village_elder_killed_by_andras')
#~ $ renpy.set_return_stack(renpy.get_return_stack()[:1])
# return to map currently
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tutorial_mine:
# Tutorial Mine event

#countryside BG

scene black with fade

show rowan necklace neutral at midleft with dissolve

ro "I've found what looks like an abandoned mine. There's no signs of anyone working here recently, but it seems to have been an iron mine."

je "A useful find, we can sell the iron to help raise funds."

an "Or build a forge and build our own stockpile of weapons and armor."

je "Where exactly is it?"

ro "Close by the portal, just a little to the South-West."

je "Excellent. I'll make arrangements to bring in some workers. That is, unless you have orcs available to do the work instead, brother."

an "Ha, those warriors would hate to be sent off to do menial labour after the tales I fed them. Later, I won't mind sending them off like that, but I don't have the numbers to spare right now."

je "Humans it is then. I've already got some people in the area we can use, but next time I'll have to use funds from our treasury to start mining operations using locals."
je "Wait for me there, Rowan, and keep an eye on things."

scene black with fade

#xp +10
$ add_exp(10)
# mines + 1
$ castle.mines += 1
#iron production +3 per week (to be balanced later)
$ castle.iron_per_week += 3
#end turn
#return to castle for week end
#~ $ renpy.set_return_stack(renpy.get_return_stack()[:1])
# return to map currently
return

###################################################################################################
###################################################################################################
###################################################################################################

