#Rebuilding Arthdale Quest Chain
init python:
    #First Event - First Time in Arthdale
    #Occurs when player visits Arthdale for the first time
    event('first_time_in_arthdale', triggers='map_res_102', run_count=1, group='arthdale', priority=pr_map_res)
    #Return to Arthdale ruins
    #Return visit to Arthdale while still needing either funding or refugees.
    event('return_to_arthdale_ruins', triggers='map_res_102', depends=('first_time_in_arthdale',), group='arthdale', priority=pr_map_res)
    #Return to Bloodmeen after visiting Arthdale
    #Ruler event, priority after visiting Arthdale for the first time.
    # TODO: probably it should be in same group as 'ruler_event', but with higher priority
    event('arthdale_return_to_bloodmeen', triggers="week_end", conditions=('week > 4',), run_count=1, depends=('first_time_in_arthdale',), priority=pr_story)


label first_time_in_arthdale:
#First Event - First Time in Arthdale
#Occurs when player visits Arthdale for the first time

scene bg5 with fade
show rowan necklace neutral behind bg5

"Rowan climbed up a familiar hillside, when he crested it, a somber sight greeted him. Arthdale's ruins lay before him for the first time since his departure. He wasn't far from where the Elder had dragged him to safety, but the place was very different now."
"Most of the charred buildings had either collapsed or become overgrown, for the most part people had left them as they were since the attack. It would seem there hadn't been any attempt at rebuilding in his absence."
"Now he could see a lone figure approaching him on the road through the ruined village.  Confident there would be no trouble and so as to appear a traveller himself, Rowan set off down the road towards the figure."
"As he got closer, it became apparent that the other traveller was a young woman, tall and thin, and pretty enough with mousy blonde hair. From her style of dress, he guessed a farmer or miller's girl, definitely one of the peasantry."
"Once the two were in earshot, he was surprised to be addressed by name right away."

#Tania's name should show as "Woman"
tan "Rowan?"

ro "Do I know you?  I'm terribly sorry, but I can't remember your face."

tan "We met once a few years ago, but you wouldn't remember it. It was at the harvest festival in Arthdale. My father is a forester and we live near the western woods, but sometimes he would take me to the village for the celebrations."

"She flashed an awkward smile which finally jostled the hero's memory."

ro "Oh yes. You're Tania, old Ruffock's daughter, aren't you?"

"Another smile, this one more genuine, then she gave a small nod."

#Change Tania's name to show as "Tania"
$ tania_name = 'Tania'

tan "Umm... if you don't mind me asking, where have you been? I overheard my father telling mother that ever since the fire at Arthdale, the Duke had been looking for you. There's been rumors that demons attacked, but father says that's nonsense."

"Rowan considered her words, deciding how much of the truth he should say."

menu:
    "Tell a full lie.":
        $ released_fix_rollback()
        ro "I... uh... had to visit a sick relative in Uvarth and couldn't return until the snow cleared."
        "He'd been thinking of what Jezera had said when she'd shown up at their doorstep back in the attack and the lie seemed reasonable enough."

    "Confirm the demon attack.":
        $ released_fix_rollback()
        ro "The rumors were true, demons burned Arthdale down. I've been tracking them since and was trying to avoid drawing attention to myself."
        "That's reasonable enough, hopefully it wouldn't scare her too much."

    "Confirm the demon attack and that Alexia was kidnaped.":
        $ released_fix_rollback()
        ro "The rumors were true, demons burned Arthdale down. They were after me, so they kidnapped Alexia to bring me to them. I needed to move fast, so I didn't speak to anyone afterwards."
        "She didn't ask any more of him, so he didn't elaborate on why he was back now or if he'd actually rescued Alexia."

ro "Speaking of the fire, has work begun on rebuilding yet?"

"She frowned."

tan "I'm afraid not. Father says that the Duke wanted to help, but has been unable to do so. There's been a few... problems while you have been away, Rowan."

ro "In that case, I'd better walk you home."

tan "It isn't that far, and I'll probably be fine by myself. I walk this part of the road to take pelts to the tanner for father often, and nothing bad has even happened."

ro "I insist."

"This would give him a chance to learn more information from her father about the problems she was talking about and compare that with what he'd already learned."

scene black with fade

"A few hours later, he said goodbye to the young lady at her father's cottage after exchanging some small talk with her parents."
"He'd learned that the harvest after his departure had been bad, and the signs pointed to this year being bad as well."
"To make matters worse, the bandits based in the western forest had grown bolder, raiding some farmhouses and even going so far as to ransack caravans on the White Road."
"There had been reports of people and animals vanishing around the realm that had been blamed on increased sightings of orcs moving in through the Rosarian Valley from the North and the goblins operating out of the Blackholt in the East."
"Lastly, and perhaps most disturbingly, there had been a large increase in reports concerning monsters, leading the Duke to stand bounties in the hopes of attracting more professional slayers."
"Rowan had mentioned that he'd like to help with rebuilding Arthdale, which Ruffock had been happy to say he'd help if Rowan could secure the funds needed and bring the refugees back."

#End scene.  Arthdale should be flagged for an event that triggers the appropriate Arthdale event.
# TODO: decide about event flag
$ prevent_tile_exploration()
$ codex_add('arthdale_after_visit')
$ journal.start_quest('arthdale_restoration')
$ journal.add_quest_note('arthdale_restoration', 'note1')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label return_to_arthdale_ruins:
#Return to Arthdale ruins
#Return visit to Arthdale while still needing either funding or refugees.

scene bg5 with fade

"Once again Rowan stood among the charred remains of his home. Nothing of note had changed since his last visit."
"He hoped that someday he would be able to rebuild and restore the village of Arthdale."

#End scene, do not clear Arthdale's event flag.
$ prevent_tile_exploration()
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label arthdale_return_to_bloodmeen:
#Return to Bloodmeen after visiting Arthdale
#Ruler event, priority after visiting Arthdale for the first time.

scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

"In the morning after having breakfast, Alexia stopped Rowan in the halls as he was heading down to the throne room to get started on the day's duties."

al "What's wrong Rowan? I can tell that something's bothering you."

show rowan necklace happy at midleft with dissolve

ro "You read me way too easy Alexia."

show rowan necklace neutral at midleft with dissolve

ro "The truth is that I was in Arthdale not too long ago and found that no work had been done on reconstructing it. Our home is still the ruin the twins left it in."

al "Oh, I see."

"He put his hand on her shoulder and smiled reassuringly."

ro "I want to see that change, even while I continue to serve the twins. I'm going to ask them if I can use funds from the treasury to help with the reconstruction."

show alexia 2 necklace happy at midright with dissolve

al "Then good luck! I hope that when your work is done that we'll be able to walk the streets together again."

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera displeased at midright with dissolve

je "No."

"However, as Rowan had feared, he was unlikely to get funds for this from Bloodmeen."

je "I don't care what excuses or morals you claim, you're not using our treasury for your pet project. Get some lord to pay for it, as long as it doesn't interfere with the rest of your duties."

hide jezera with moveoutright

"The hero's best bet would be to go to the Baron himself next, in Rastedel.  Even if he couldn't get funds from the top, the richest nobles all lived in the capital and it was the best place to find a patron."

"(This is the furthest you can get in the Arthdale restoration quest in the current version of the game.)"

#End event.  Getting funding in Arthdale is now possible.
$ journal.add_quest_note('arthdale_restoration', 'note2')
return
