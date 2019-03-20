init python:

    # Rowan goes hunting
    # Requires morale to be above 40 and Rowan to  have no stat affecting injuries
    event('rowan_goes_hunting', triggers="week_end", conditions=('week >=4', 'not av_has_injuries()', 'castle.morale > 40'), group='ruler_event', run_count=1, priority=pr_ruler)
    # Complete chaos
    event('complete_chaos', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    # Jezera has been spending money
    # Treasury has to be at least 50.
    event('jezera_has_been_spending_money', triggers="week_end", conditions=('week >=4', 'castle.treasury >= 50'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Learning about goblins
    #Requires that Rowan learn about goblin prince while exploring - Increasing high priority after 3 turns
    # TODO increase priority
    event('learning_about_goblins', triggers="week_end", conditions=('week >=4', 'new_goblin_prince_rumor'), group='ruler_event', run_count=1, priority=pr_ruler)


label rowan_goes_hunting:
# Rowan goes hunting
# Requires morale to be above 40 and Rowan to  have no stat affecting injuries

scene bg6 with fade
show rowan intro necklace neutral at midleft with dissolve

ro "Phew, is that it?"

"Rowan double checked the list of tasks and the messages he'd been given. He couldn't find anything else to do, today had gone remarkably smoothly and there hadn't been that much to do to begin with."

ro "It isn't even noon yet."

"He got up, stretched, and wondered what he should do with his unexpected free time."

scene black with fade
show rowan intro necklace neutral behind black

"After wandering the halls for a few minutes he found himself on the battlements and looking out into the forest nearby the mountain castle. His thoughts drifted back to when he would hunt game to keep Karst supplied."

ro "Yeah, why not?"

"He informed Alexia and his underlings of his plans. Then returned to his room to get his equipment before leaving the castle to go hunting. It felt a bit surreal to leave via the front gate rather than Jezera's portal."

scene bg3 with fade
show rowan necklace neutral at midleft with dissolve

ro "(Hmm, at least three of them and they were here for some time.)"

show bg3 with sshake
show jezera displeased behind bg3

je "Rowan, what are you doing out of the castle?!"

"After being out for over an hour, Rowan was startled by Jezera's voice coming out of his amulet. She'd contacted him while he'd been checking the tracks he had been following for a good fifteen minutes which sent him into a brief panic."

je "If you don't say anything, I'm going to teleport you back here!"

"Finally he was able to get his wits back and properly place his hands on the amulet to speak to Jezera."

ro "I'm out hunting. There wasn't anything left to do in the castle, so I thought I'd try and get some game."

je "Oh, really? Why didn't you say anything before you left?"

ro "Actually I did tell Alexia, Skordred, Cla-Min-"

je "One moment...."

"Rowan found himself at a loss for what to say or do."

je "Alexia and Skordred have collaborated your story. I will let this slide for the moment, but next time you are going to leave, {i}tell me first{/i}."

ro "Uh, will do."

"He waited for a little while to see if Jezera would say anything else, but when he heard nothing he returned to his hunt."

scene bg3 with fade
show rowan necklace neutral behind bg3

#roll 1d20 and add survival skill
$ (temp2, temp) = roll_skill('survival')
$ renpy.fix_rollback()

#if roll = 1 (critical fail)
if temp == 1:
    $ renpy.notify('Survival roll: {} + skill {} = {}: critical fail'.format(temp, avatar.skill('survival'), temp2))
    ro "Ah shit..."
    "This hunt had gone very poorly, as Rowan had run afoul of a large bear. While his skills allowed him to survive the experience with all his limbs still attached, he did get a broken arm for his trouble."
    "The injury forced him to return to the castle for the day, empty handed. While magical healing would mend the bone quickly enough, his arm would remain weak for at least a week."
    #1d6+1 strength injury til the end of next turn (the next week)
    $ add_effect(Injury('Broken arm', 'strength', -dice(6)-1, 2))
    #10 xp
    $ avatar.exp += 10
    #end event
    return
# 2-7 (partial fail)
elif temp2 <= 7:
    $ renpy.notify('Survival roll: {} + skill {} = {}: partial fail'.format(temp, avatar.skill('survival'), temp2))
    ro "(It's getting late.)"
    "Rowan was forced to call today's hunt a failure. He hadn't managed to catch anything and figured that it would not be wise to stay away from the castle now that evening was coming on."
    #10 xp
    $ avatar.exp += 10
    #end event
    return
# 8-14 (success)
elif temp2 <= 14:
    $ renpy.notify('Survival roll: {} + skill {} = {}: success'.format(temp, avatar.skill('survival'), temp2))
    ro "(It's getting late.)"
    "Rowan figured that since evening was coming on it was time to return to the castle."
    "He wasn't returning empty handed, as he'd killed a few rabbits that could be stewed later, but nothing that would make a real difference for the castle as it was. Still, it was nice to dedicate an afternoon to something like this again."
    #20 xp
    $ avatar.exp += 20
    #end event
    return
# 15+ (exceptional success)
else:
    $ renpy.notify('Survival roll: {} + skill {} = {}: exceptional success'.format(temp, avatar.skill('survival'), temp2))
    ro "(One.)"
    "Rowan loosed his bow and quickly drew back the second arrow in his hand."
    ro "(Two.)"
    "Release, pull."
    ro "(Three.)"
    "Whistle, thunk, and the third elk fell."
    "The hunter stood and admired his handiwork. Three heartshots in five seconds, taking down the whole gang without giving any a chance to bolt."
    "He'd matched his best hunt from the siege of Karst, though at least this time it would be easier to get his kills back to the castle than it had been that night so many years ago."
    "After dragging the carcases together and sitting on the set, he contacted his mistress."
    ro "Jezera, do you think you could bring me back to the castle? I've got quite the haul. It should cover most of our food bill for some time."
    #gain 30 gold
    $ castle.treasury += 30
    #gain 20 xp
    $ avatar.exp += 20
    #gain a small amount of morale
    $ castle.morale += 5
    #end event
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label complete_chaos:
# Complete chaos
#no requirements

#corridor BG
scene bg14 with fade
show jezera neutral at midright with dissolve
show andras displeased at edgeright with dissolve
show rowan necklace neutral at midleft with moveinleft

je "Ah, good morning, my hero."

an "Good, you're up servant."

"Rowan felt a sinking sensation in his stomach, he never met with both of the twins in the mornings like this."

ro "Alright, what's the bad news?"

"The twins looked at one another in surprise. This confirmation of his hunch didn't comfort their agent in the slightest."

je "Well, you see that while we don't normally want you to concern yourself with the day to day operations of the castle, today is a bit of an exception."
je "There will be a very important meeting today that demands the attention of both of us. In our absence, we are setting you the task of running everything in the meantime."

ro "Wha? Am I to continue with my usual duties as well?"

an "Of course. You will manage."
an "Oh, we'll also need you to coordinate the kitchens to prepare a banquet and I've got several hopeful soldiers arriving today that will need to be put through their paces."

show rowan necklace shock at midleft with dissolve

"With each new task being set before him, Rowan's eyes grew wider and wider."

ro "I... I..."

show jezera happy at midright with dissolve

je "Here is the day's schedule, I know you won't disappoint us. Good luck my hero."

hide andras with moveoutright
hide jezera with moveoutright

"Rowan was left dumbfounded, he couldn't believe what he was being ordered to do on such short notice."

scene black with fade

"What followed was complete chaos."
"Rowan desperately tried to coordinate everything and make emergency re-assignments and suspended projects in an attempt to keep the whole castle from collapsing under him."
"He managed to satisfy the twins for the time being, at the cost of enough stress to force him to take most of the next day of."
"It wasn't until the day after that he was finally able to complete his usual duties as steward and be prepared to go scouting again. This fiasco had cost him two full days."

#Lose 4 movement points on next scout
# TODO loosing MP on next week
#end event
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_has_been_spending_money:
# Jezera has been spending money
# Treasury has to be at least 50.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with moveinright

je "My hero, just dropping by to let you know that my work has necessitated spending some of the money in our treasury."

"The demoness handed Rowan a sheet of paper and then started to leave."

show jezera neutral at edgeright with moveoutright
show rowan necklace shock at midleft with dissolve

ro "10, 20, 5... what did you spend 50 gold on?!"

je "That doesn't concern you. You just need to adjust your plans with this expense in mind."

show jezera happy at edgeright with dissolve
show rowan necklace neutral at midleft with dissolve

je "I'm sure that won't be a problem."

hide jezera with moveoutright

"Rowan looked at where his mistress had been standing a moment before, then put his hand to his head and let out a long sigh."

#lose 50 gold from treasury
$ castle.treasury -= 50
#end event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label learning_about_goblins:
#Learning about goblins
#Requires that Rowan learn about goblin prince while exploring - Increasing high priority after 3 turns

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show clamin neutral at midright with dissolve

cla "Alright, what is it you wanted Rowan?"

ro "I've been hearing rumors about the goblins in Blackholt and was wondering if you could tell me anything about them?"

cla "'Fraid not. Those tribals still cling to the old ways."

ro "What do you mean?"

cla "How much do you know about goblin history?"

ro "Not much, I didn't have a reason to learn about goblins during the war. Never had to negotiate with them, you see."

"The merchant looked thoughtful for a moment, then plopped on the ground and extracted her pipe. She filled it while Rowan sat across from her, watching her patiently."

show clamin pipe at midright with dissolve

cla "There are two main groups of goblins."

"She lit the pipe and took a pull on it."

cla "The caravaners like me, who've abandoned the lands that our people once lived in and now move around the world as nomads, and the tribals like those in the Blackholt, who still want to live life in a way that doesn't exist anymore."
cla "Much of Rosaria once belonged to goblins and we called it our homeland. Humans have been slowly taking more and more of it away from the goblins. Today, some pockets and Blackholt are about all the goblins still have."

"Silence for a few moments as Cla-Min studied her audience through her red eyes, then puffed on her pipe again."

cla "The caravaners first left to try and find a new home for ourselves, but no one wanted goblins in their lands. Eventually we got so use to the roads that we just stayed on them."

show clamin happy at midright with dissolve

cla "The tribals curse us and call us 'civilized'. They're just shortsighted, no idea how much better you can scheme when people at least tolerate you and you can move on if you need to."

show clamin neutral at midright with dissolve

ro "I take it then that you don't have much contact between the two groups?"

cla "Sometimes, but our caravan hasn't been anywhere near the Blackholt for years."

ro "Well, rumor has it that they've been reorganizing themselves and have a new leader; Tue-Row. Ever heard of him?"

"Cla-Min rolled her eyes while she thought about the name. Seeing as how she'd finished off what was in her pipe she started to knock it out on the nearby pillar."

cla "Goblin names are made up of your family name followed by your given name. The tribals use the name of their tribe instead of a family name, so this leader's tribe would be 'Tue'. That is one of the tribes in Blackholt."
cla "I haven't heard of a goblin called 'Row' before. In fact, I've never heard anyone use that name. Goblins usually stick to the same set of names; you'll see a Min in pretty much every caravan, if you get my meaning."

"Finished cleaning out her pipe, the green woman put it away and stood back up."

cla "That's about all I can tell you about this 'Tue-Row'."

ro "Thank you for the help. Even if you couldn't tell me anything specific, most of that I'd never heard of before."

show clamin happy at midright with dissolve

cla " No problem, Rowan. If you wouldn't mind returning a favor sometime, I'd really appreciate it. I'll even make sure to keep ears on the ground if anyone from my caravan is nearby Blackholt, just for you."

#end event
return
