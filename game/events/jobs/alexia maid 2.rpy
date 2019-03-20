init python:

    event('a_new_friend', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', run_count=1, priority=pr_npc)
    event('changing_staff', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', run_count=1, priority=pr_npc)
    event('rough_firing', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', run_count=1, priority=pr_npc)
    event('alexia_and_mary', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", "meetMary == True",), group='alexia_maid', run_count=1, priority=pr_npc)
    #Generic Maid Event 1
    #No requirements - Repeatable
    event('generic_maid_event_1', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', priority=pr_npc)
    #Generic harassment scene
    #Plays when harassment is needed but no scenes available. Repeatable.
    # currently this event simply directly called from "Jezera wants a new agent"
#~     event('generic_harassment_maid', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"),
#~         group='alexia_tavern', priority=pr_npc_high)



label a_new_friend:
#A new friend
#No requirements

scene alexia_maid_1 with fade

"While she was working among the domestic staff, Alexia was approached by one of the maids who engaged her in an animated discussion. Since she was hoping to make few friends among the staff, Alexia was happy to have someone to talk to."
"The two of them spent much of the day with one another, talking about the other castle staff and the lives they use to have back in the Six Realms."
"Alexia learned that the other maid's name was Mary and she was from the South-Eastern region of Rosaria, nearby the Tundra pass."
"Several years younger than her, Mary had never had a man as a lover and actually ended up working here after an unforgettable encounter with a woman who eventually turned out to be Jezera."
"For all the hardship she'd since had at her mistress's whims, Mary was ultimately happy to be in the castle since she felt like she could be herself."
"Exactly what that meant she proved to be evasive about, but Alexia was promised that she'd get the chance to learn soon enough."
"The two would chat amicably throughout the rest of the week, on the occasions when their work brought them together."

$ meetMary = True
#Alexia loses a little stress.  Further Mary events can now happen.
$ all_actors['alexia'].job_state.stress -= 1
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label changing_staff:
#Changing staff
#No requirements

scene alexia_maid_1 with fade

"Jezera was a very demanding boss. That much was obvious from working just a day or two for her. What was less obvious what just how quickly she seemed to go through her staff."
"Try as she might to remember everyone, every few days Alexia always seemed to discover a castle servant she'd never seen before."
"They weren't as understaffed as the castle had been when she'd first been brought here, but Alexia doubted there was more than two dozen maids and butlers working in Bloodmeen at any one time."

if meetMary == True:

    "There were a handful that she saw all the time, including Mary, but the rest just blurred together."

else:

    "There were a handful that she saw all the time, but the rest just blurred together."

"This week Alexia was even given the job of orienting three new members of the staff. She handled the job well enough, though it wasn't something she particularly enjoyed."
"What was strange was the wide variety of backgrounds each of these new servants had. Three different Realms and three different statuses in society. The only unifying aspect was that they'd run into Jezera at some point before being recruited to work in Bloodmeen."
"Her mistress evidently spent a lot of time finding people to work for her in the castle. Apparently she also hand picked her staff based on looks and personality, not skill. Everyone of them was very attractive and been given a fond word before being given for training."
"There was a definitive gap of skill between the three newcomers as well. Perhaps that was the reason that so many of them didn't stick around for long as servants? If it was, Alexia at least would not need to worry about being dismissed over incompetence."

#Alexia gains a little stress.
$ all_actors['alexia'].job_state.stress += 1
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label rough_firing:
#Rough Firing
#No requirements.

scene alexia_maid_1 with fade

"While working this week as a maid, Alexia was unfortunately partnered with a rather lazy butler. The man proved to be easy on the eyes but incredibly grating on the nerves. He wouldn't do any work and took every opportunity he could to flirt with and grope Alexia."
"Jezera soon took note of his poor performance and started avoiding the two of them. Thankfully for Alexia, her mistress wasn't interested in bothering her this week. It was her partner who was the focus of attention."
"Towards the middle of the week, he was finally confronted by Jezera over his laziness. Alexia suggested that he was also harassing her, which unfortunately turned out to be completely fine. As long as it didn't interfere with their work, Jezera was completely fine with some sexual harassment."
"For one more miserable day, she had to deal with the man's hands and catcalls. Thankfully, by the end of that her mistress had now had enough. The butler had been given one more chance to get himself in gear, he hadn't."
"The man was indignant at first, then reduced to muffled cries of panic when he'd been wrapped up in Jezera's bindings of blue energy."
"Although she was very glad to see that bastard be carried away, Alexia wasn't entirely sure she was comfortable watching him be taken by a demon like that."
"She never saw that man again."

#Alexia gains a little stress.
$ all_actors['alexia'].job_state.stress += 1
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label generic_maid_event_1:
#Generic Maid Event 1
#No requirements - Repeatable

scene alexia_maid_1 with fade

"This week Alexia would work as a member of the castle staff again, directly serving Jezera. Fortunately for her, the demon twin was largely preoccupied with other things or out of the castle for most of the week. So Alexia escaped her influence."
"While some of the staff resented Alexia for her outdoing them, none of them did much to her beyond minor inconveniences. Having a clear common enemy in their demonic mistress did a lot to help keep the staff civil to one another."
"Domestics always has more work for it, it's a field of maintenance, not of creation or destruction.  Alexia did her part in keeping the castle as it should be and in livable order."

return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label generic_harassment_maid:
#Generic harassment scene
#Plays when harassment is needed but no scenes available. Repeatable.

scene alexia_maid_1 with fade

"During her period of service towards the castle's upkeep this week, Alexia was unfortunate enough to have nearly the full attention of her mistress."
"The demoness spent much of the week either directly harassing Alexia, or orchestrating events specifically to bother her."
"Jezera groped, pestered, or otherwise made things as sexually uncomfortable as possible. For Alexia's part, she did a very admiral job of completing her work in-spite of the interruptions and awkward situations."
"In some ways, the harassment was a good motivator to be as quick and efficient as possible. In others, it was a serious obstacle."
"By the end of the week, most things had been balanced out, but Alexia felt very dirty."
#Jezera gains influence on Alexia, Alexia gains a little corruption
#Re-roll harassment timer, increase harassment event count by one.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ change_corruption_actor('alexia', 2)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

label alexia_and_mary:

scene alexia_maid_1 with fade

"Once more, Alexia found herself working side by side with Mary, the maid from near the Tundra passes. Today they were running food up to the rooms of the different major figures of the castle." 
"When she stopped at Andras’ room he wryly noted he was disappointed in how plain an outfit Jezera picked for her."
"Through it all, she chatted with Mary idly."

scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show mary neutral at midright with dissolve

mary "The first time my parents caught me with another girl they already knew what to do with me-"

al "Caught you with another girl?"

mary "Abigail from just down the way. She was the town mare. Everyone took their turn riding her, guys and girls alike."
mary "After I was caught though, they wanted none of that. So they sent me up to the convent on the hill overlooking the passes. It was a horrible thing for them to do. Send their only child away over such a minor thing. To such a cold and inhospitable place too."

al "Parents in Rosaria are conservative."

"Mary sighed and straightened out her uniform."

mary "Well, the joke is on them. May I ask you a philosophical question?"

al "Yes, of course."

mary "If you wanted to put all the repressed little gay girls in the region somewhere that would fix them into proper young ladies, where would you place them?"

al "Where?"

show mary happy at midright with dissolve

"Mary giggled."

mary "Not in a secluded building with all the other little gay girls."

show jezera displeased at edgeright with moveinright

"The door they were standing outside opened. Jezera grabbed the tray of food that both of her skimpily dressed maids brought her. But, then she noticed that mary was giggling to herself."

je "Having fun, huh? Are you behaving yourself girls?"

show mary neutral at midright with dissolve

"Alexia and Mary straightened up at once."

al "Yes, mistress."
mary "Yes, mistress."

"This time it was Jezera’s turn to giggle."

je "If you say so."

hide jezera with dissolve

"She closed the door to her room, leaving Alexia to exhale a sigh of relief. Mary though only seemed heartened by the encounter."

al "One of these days she’s going to catch you chit-chatting when you’re on duty, you know?"

show mary happy at midright with dissolve

mary "One of these days? It’s happened twice this month already. I’ve got the welts on my backside to prove it."

"They both shared a laugh at that. Though Alexia couldn’t help but notice that Mary sure didn’t seem to be angry about the treatment she’d received."
"Of course, Alexia noticed the way that Mary looked at her when they were on duty. The odd glance in her direction. The way she’d always talk to Alexia first even when there were other maids around."
"Alexia knew what it all meant, but for the time being she was happy just to have a friend to share in the day to day struggles of keeping the castle clean while dressed as eye candy."
