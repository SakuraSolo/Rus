init python:

    #The cubi start an orgy
    #Requires at least 5 cubi sorcerers, at least 15 soldiers, and morale less than 80.
    event('cubi_start_orgy', triggers="week_end", conditions=('week >=4', 'castle.buildings["sanctum"].troops >= 5', 'castle.buildings["barracks"].troops >= 15',
        'castle.morale < 80'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Construction disruption
    event('construction_disruption', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Cliohna's Breakthrough
    event('cliohna_s_breakthrough', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Skordred damage report
    event('skordred_damage_report', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Jezera sticking her nose in books
    event('jezera_sticking_her_nose_in_books', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #The Icon
    event('the_icon', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Minor Hero Trouble
    #after Raeve keep has been captured
    event('minor_hero_trouble', triggers="week_end", conditions=('week >=4',), depends=('goal2_success',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Demon vs Demon
    #after Raeve keep has been captured
    event('demon_vs_demon', triggers="week_end", conditions=('week >=4',), depends=('goal2_success',), group='ruler_event', run_count=1, priority=pr_ruler)
    #The Slaver's Proposition
    #should occur after week 20
    event('slaver_s_proposition', triggers="week_end", conditions=('week > 20',),  group='ruler_event', run_count=1, priority=pr_ruler)


label cubi_start_orgy:
#The cubi start an orgy
#Requires at least 5 cubi sorcerers, at least 15 soldiers, and morale less than 80.

scene bg6 with fade
show rowan necklace shock at midright with moveinright

ro "Whoa, what the hell is going on?!"

"Rowan had arrived in the throne room to begin his duties with managing the castle, and had found the place filled with bodies writhing around on the ground together!"

show xzaratl neutral at edgeleft with moveinleft

xz "It's an orgy, silly. Haven't you ever seen one before?"

show rowan necklace neutral at midright with dissolve

"Participating in such an act had never been one of the hero's goals or desires in life and it wasn't something you just saw on street corners in Solansian guided societies."

ro "Where exactly would I have had the chance to experience... this?"

xz "Aww, poor thing. Don't worry, my lovelies and the soldiers would be happy to have you join them, it will be an excellent learning experience!"
xz "Oh! We should go get Alexia and add her to the pile too!"

"Rowan shook his head and tried to reorient his thoughts."

ro "Okay, before you go any further there, some other questions.  First, why is there an orgy here of all places?"

xz "It's the biggest room in the castle, need a lot of space to get all of the soldiers in here."

ro "(Guess I'm working somewhere else today.)"
ro "Second, why are you even having an orgy?"

xz "Just a way to have some fun. We succubi and incubi need sex to fuel our power, but that doesn't mean we don't really enjoy it too!"

"Looking back into the sea of bodies, the hero could now pick out several of the dark sanctum's sorcerers amongst them as well. They seemed to be the focal point of the entire act."

ro "Third, how did you okay this with the twins? I'm amazed that Andras was okay with you taking all his soldiers up here for a massive orgy."

xz "Oh they're both out right now. They didn't go for the idea, so I just did it anyway after they left."

"Rowan put his head in his hands and groaned in dismay. Great, just great."

ro "I guess, just one more question."

xz "Go right ahead, sweetie."

ro "Why aren't you participating too?"

xz "Just hopped out for a minute to grab a drink of water. Will you be joining us?"

hide xzaratl with moveoutleft

"She casually slipped out of her clothing and dived into the group, leaving Rowan both feeling oddly aroused and concerned with how he was going to deal with this mess."
"Well, at least the participants would probably be happy after this."

#gain 10 morale
$ change_morale(10)
return

############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label construction_disruption:
#Construction disruption
#No requirements.

scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show skordred angry at midleft with dissolve
show rowan necklace neutral at edgeleft with moveinleft

ro "Alright, what's this about?"

"The man had been called in to help with a dispute that was going on between Cliohna and Skordred. Odd, since the pair almost never interacted with one another."

cl "The construction teams have decided that beneath my library is the perfect location for highly disruptive noise and shaking I need them to leave, there's plenty of other places in the tunnels they could work instead."

sk "Ye canne dictate that yar work takes priority over tha castle's restoration!  We've discovered some very valuable materials here. I'm sure ya can live with a few weeks of noise while we excavate."

show skordred neutral at midleft with dissolve

ro "Alright, well, Cliohna what exactly are you working on that even requires calm and quiet?"

cl "It isn't only your research that I'm working on, but also my own alchemical and magical projects which very much depend on a still floor and clear focus."

#cliohna annoyed

cl "That's not to mention that my staff is rather preoccupied with making sure no books are damaged from falling off the shelves!"

#cliohna neutral

ro "Well then, Skordred is there any chance that your team could be a little quieter or spend less time under the library?"

sk "Impossible. Most a tha work is adding in supports and securing the foundations in tha places we're extracting materials from. Ye canne slow that down, it be just as disruptive but with less benefits."

sk "This is also tha best salvage we've discovered in a long time. Giving it up is unthinkable."

cl "Is that worth almost shutting down my work while you do it?"

sk "We'll only be a couple weeks."

menu:
    "Let Skordred finish his excavations.":
        $ released_fix_rollback()
        ro "Sorry Cliohna. Skordred, finish your excavations. Try to get it done as soon as possible so we can get the most benefit for the least damage."
        #cliohna angry
        show skordred happy at midleft with dissolve
        sk "A course, glad ya saw reason."
        hide skordred with moveoutleft
        "Rowan turned to look at the librarian, then saw sparks coming off of her threateningly."
        cl "I suggest you leave... now."
        #gain 100 treasury but the library provides no research points for two weeks.
        $ change_treasury(100)
        # TODO: stop researches for 2 weeks
        return

    "Make Skordred stop excavating under the library.":
        $ released_fix_rollback()
        ro "Sorry Skordred but I can't let you disrupt Cliohna's research, tell your team to clean up and move on to another part of the castle."
        show skordred angry at midleft with dissolve
        sk "Yar making a huge mistake here!"
        "Rowan started to reply, but was interrupted by Cliohna."
        show rowan necklace angry at edgeleft with dissolve
        cl "Be quiet dwarf, the decision has been made. Now get out of my library."
        "The dark skinned man wheeled around and looked like he was going to yell something more, but the sight of sparks coming off of Cliohna's hand threateningly made him instead stomp out of the room."
        hide skordred with moveoutleft
        ro "It wasn't your place to threaten him like that."
        show rowan necklace neutral at edgeleft with dissolve
        cl "I don't really care. You should just be happy that you're on my good side right now."
        #gain rep with Cliohna, lose rep with Skordred. Cannot build / improve for the following week
        $ change_relation('cliohna', 5)
        $ change_relation('skordred', -5)
        # TODO: disable build for next week
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label cliohna_s_breakthrough:
#Cliohna's Breakthrough
#no requirements.

scene bg6 with fade
show rowan necklace neutral at midright with dissolve
#cliohna excited
show cliohna neutral at edgeleft with moveinleft

ro "Oh, hello Cliohna! What's going on, it isn't like you to actually come here in person."

"The sorceress seemed to catch herself as she opened her mouth. Instead she took a deep breath, straightened her back, then spoke."

#cliohna neutral

cl "I am pleased to report that my research has struck an unexpected breakthrough. Based on my findings, I calculate that this will save weeks on the latest project!"

#cliohna happy

"As she continued, a smile crept onto her face again."

cl "You won't believe this, I found two separate authors who wrote books on the subject a century apart from one another. They'd stumbled onto solutions for each others problems by complete accident!"

show rowan necklace happy at midright with dissolve

ro "Uh, that's good news right?"

cl "This is incredible news, it's exactly what we needed to bring this to Bloodmeen! I might actually be the very first to combine their work. I'm coming up with new principles, perhaps an entirely new paradigm!"

"She was speaking so animatedly now that Rowan completely lost track of what she was saying.  He raised his hands and interrupted her passionate revelation."

ro "Whoa, slow down there. I understand this is a big moment for you, but I'm afraid you lost me from the start."

#cliohna neutral

cl "I suppose this would be beyond you. A shame."

ro "The important thing is that this means you'll be done your research sooner than expected, right?"

cl "Correct."

ro "Great news, thank you for telling me about your great accomplishment Cliohna."

"A hint of her smile came back for a moment, then the librarian crossed her arms with a pointed look."

cl "Your flattery feels hollow when you don't even understand what I've accomplished."

ro "Well, I can tell just how important it is for you and hope that you'll have a chance to discover many more things while you're here in the castle."

#cliohna happy

"This time she did smile."

cl "Oh, that is the very least of what I plan to do."

#double research points for the next two weeks
# TODO: double research points
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label skordred_damage_report:
#Skordred damage report
#No requirements

scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show skordred neutral at edgeleft with dissolve

"Rowan looked up from the maintenance report that Skordred had given him, detailing expenses that were rather larger than usual."

ro "Why exactly have our maintenance costs doubled this week?"

sk "Tha master had, an episode. He can be a bit... destructive during those."

"Slumping back in his chair a bit, Rowan put a hand to his face and let out a big sigh of frustration."

sk "Tis ta be expected. When one has such power, thar bouts do a lot more damage than mere mortals."

ro "I guess this is normal for you. My last employers could be incompetent asses, but at least they didn't break their assets from time to time just because they had a bad day."
ro "How was Karnas compared to Andras?"

sk "My old master's blood is strong. His son carries on his might and temper."

show skordred happy at edgeleft with dissolve

sk "Tis wonderful to see such might again bring itself to these walls."

ro "Not so wonderful for our treasury. I'm surprised that Karnas didn't do more damage to this place."

show skordred neutral at edgeleft with dissolve

sk "During tha war, I was not the only master builder here and much of Karnas's time was spent away fighting and conquering."

ro "Amazing that Bloodmeen is still standing after the punishment it took from nature, the six realms, and its masters."

sk "Don't underestimate me or the skill of tha dwarves. With time, workers, and funds, we can build something that will stand for a hundred years against anything. When tha time comes for it to fall, we shall do it again!"

show skordred happy at edgeleft with dissolve

sk "Tis our purpose to our masters, thar's no greater honor."

ro "(Easy enough for you to say, I'm the one who has to actually find the funds.)"

#doubled building maintenance costs next week
# TODO: double maintenance costs
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_sticking_her_nose_in_books:
#Jezera sticking her nose in books
#no pre reqs

scene bg12 with fade
#cliohna annoyed
show cliohna neutral at edgeright with dissolve
show jezera happy at center with dissolve

cl "Why is this so difficult for you to understand?"

je "Mayhaps you are being too uptight. You won't know until you try."

show rowan necklace neutral at edgeleft with moveinleft

"Rowan seemed to have stumbled in on an argument of some sort between Jezera and Cliohna."

cl "I made my intentions clear from the start, your constant pestering will not change anything."

"From the looks of things, his mistress was enjoying herself. Rowan wasn't sure exactly what her goal was, but it didn't seem like it was terribly conducive to the librarian's research."

je "Oh? I assure you that I can be very..."

show jezera happy at midright with moveinright

je "... persuasive."

"Blue hands rose up as she spoke, reaching towards Cliohna."

ro "*ahem*"

show cliohna neutral at center with moveinleft

"Using Rowan's arrival, Cliohna quickly brushed passed the demoness and approached the hero."

show jezera neutral at midright with dissolve

cl "Rowan, I have been expecting you. Please walk with me."

"She set a brisk pace down the aisle with Rowan falling into stride next to her after a quick glance back."

hide cliohna with moveoutleft
hide rowan with moveoutleft

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

ro "Now, uh, what did you want to see me about?"

"Cliohna didn't answer, only continuing to walk. After nearly a minute and a few turns, Rowan got the distinct impression that they weren't heading towards anything in particular, she just seemed to want to get away from Jezera."
"Abruptly they stopped at an apparently random shelf and the librarian finally broke the silence."

cl "These interruptions are becoming very tiresome. See to it that woman ceases this pointless chase so that I may focus on your projects again."
cl "If you cannot convince her to give this up, I may be forced to spend more time on my personal work instead."

ro "Is that a threat?"

cl "It is a warning or perhaps an incentive. Give her something else to focus on or call in a favor to get her off my back. I care not for the method you choose to employ, just ensure that harlot ceases this irritating chase."

show jezera happy at edgeright with moveinright

je "But it's just so fun!"

hide cliohna with moveoutleft

je "My hero, you're not going to try and ruin my fun, are you?"
je "I'll make it up to you later."

menu:
    "Convince Jezera to leave Cliohna alone.":
        $ released_fix_rollback()
        ro "Is hurting your research really worth this? You're trying to fight a war here, harassing your staff isn't exactly the best way to do things."
        show jezera happy at midright with moveinleft
        "The demoness stepped in close and sensuously caressed Rowan's face."
        je "Hmmhmm, and exactly what are you going to be able to do to stop me anyway?"
        ro "I might not be able to, but Cliohna could. You don't know how powerful she is."
        show jezera neutral at midright with dissolve
        je "You really do have quite the way with words. Such a charmer."
        #lose rep with jez, and if possible a favour, gain rep with cliohna
        $ change_relation('jezera', -5)
        $ change_favor('jezera', -1)
        $ change_relation('cliohna', 5)
        return

    "Allow Jezera to continue.":
        $ released_fix_rollback()
        ro "What exactly could I even do to stop you?"
        show jezera happy at midright with moveinleft
        "The demoness stepped in close and sensuously caressed Rowan's face."
        je "True. I don't need your permission for anything."
        je "Glad you aren't going to make a fuss about this. Ta."
        #20% research penalty for 3 weeks, lose Cliohna rep, gain Jezera rep and 1 favor.
        $ change_relation('jezera', 5)
        $ change_favor('jezera', 1)
        $ change_relation('cliohna', -5)
        # TODO: research penalty
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_icon:
#The Icon
#no pre reqs

scene bg6 with fade
show rowan necklace neutral at midright with dissolve

"It had been a long week, and Rowan was busy signing off the expenditures as the master builder entered room, carrying a large item wrapped within a sheet."

show skordred neutral at edgeleft with moveinleft

sk "Ah, there ya are champion, I’ve been looking everywhere for ya."

ro "I’ve been rather busy, it isn’t like the twins give me any free time with all their demands."

sk "And I’ve this entire castle ta rebuild, and ya don’t hear me complainin’."

"The hero sighed at the familiar path this exchange was beginning to take."

ro "Did you want something, builder, or did you just come in here to argue?"

sk "Aye, I want somethin’ laddie, and you’ll bloody well want ta hear what I have ta say once ya see what I have here."

"Skordred removed the cover from the item he had brought in. First, the human saw a long steel bar, and then a frame, and finally, atop the frame, a crude metal eight pointed star of chaos."

ro "Is that-"

sk "One a’ Karnas’ old banners, belonging to some orc champion by the looks of it."
sk "Not the work a’ any dwarf, that’s fer sure, but sturdy ennuf."

"Memories came flooding back to Rowan of the last time he had seen one of those, over seven years ago, fluttering in the bitter wind high above him on the castle ramparts."

ro "Haven’t seen one of those since the gate fell. Could have lived without ever seeing another, to be perfectly honest."

sk "Thought yer lot had melted ‘em all down me’self. Found this one when I was clearing some junk out one of tha storerooms that need fixing up."
sk "Ain’t nothing special about it magic wise on account a’ being made by tha greenskins, but if ya stick a banner on it an’ hang it, will probably rile ‘em up good and proper."

ro "Thanks, I’ll do that."

"Rowan motioned for one of the orc guards to take the standard from the Skordred."
"Once dispossessed of it, the dwarf gave him a typically curt retort about having more important things to do than standing around talking, before marching out of the throne room."

#gain 10 morale
$ change_morale(10)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label minor_hero_trouble:
#Minor Hero Trouble
#after Raeve keep has been captured

scene bg6 with fade
show andras angry at edgeright with dissolve
show orc soldier neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

an "There you are human, it’s about time. "

ro "What’s all this about?"

an "Report, soldier!"

"The demon grabbed the orc by the straps of his armour and thrust him in the direction of Rowan."

os "Been some trouble."

an "Trouble? Some bastard kills six of my orcs and you call it 'some trouble'?!"

ro "You’ll have to calm down Andras, or he’ll never be able to tell me what has happened."

an "Fine."

"The demon paced in the background skulking. Rowan turned back to the orc."

ro "Now, tell me more about this trouble."

os "Woz sent out on patrol with the ladz to make sure nuffin’ funny woz goin' on. "

ro "Who sent you? Andras?"

os "Yeah."

ro "Continue."

os "Went to 'uman lands like we woz told, 'ad a poke around a bit. Didn’t stray too far from portal."

os "Not a lot goin’ on, so we 'ad a rest-"

an "A rest!"

"The hero glared at Andras, who returned to his skulking."

os "Next thing you know, Grubnak’s got an arra' in 'is 'ead, and before anyone can do anyfin', Nuragg caught one in 'is throat too."
os "Some male pink with a sword comes rushin' in and kills two more. I only just managed to get back without losin' my own 'ead."

ro "So you were attacked by a man with a sword, and we lost four orcs?"

an "Five."

show bg6 with redflash
hide orc soldier with dissolve

ro "And what does that achieve, didn’t we lose enough soldiers for one day?"

an "As long as I am in charge, cowardice will not be tolerated. Any underling who runs from a fight would have been better staying there to die as far as I am concerned."
an "You have more important things to worry about anyway, like this stranger and what it is he wants."

ro "I think it is pretty obvious what happened."
ro "This isn’t the wastes, you know. If you start taking towns and sending out orc patrols, people are going to notice, and some of them will not stand for it."
ro "And the more you do, the worse it is going to get."

an "Just get rid of the problem."

hide andras with moveoutright

"The demon stormed off, leaving Rowan with yet another headache to deal with."

#lose 5 orcs
$ castle.buildings['barracks'].troops -= 5
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label demon_vs_demon:
#Demon vs Demon
#after Raeve keep has been captured

scene bg14 with fade
show andras angry at edgeright with dissolve
show jezera displeased at midright with dissolve

je "That is your solution to everything! Kill, kill, kill!"

an "And you think you can just fuck everything into oblivion!"

je "It is called tact. You’d know about it if you had even a shred of intelligence."

an "Thinking with your cunt counts as intelligence now?"

je "Might want to watch your words, {i}dear{/i} brother, considering that your cock seems to do all the thinking on your part."

an "Bitch!"

je "Oh, I’ll show you a bitch..."

show rowan necklace neutral at edgeleft with moveinleft

ro "(This doesn’t look good, I should get out of here before— )"

je "Ah, hero, perfect timing, perhaps you could settle this argument for us. Come here."

show rowan necklace neutral at midleft with moveinleft

an "And what help could the human possibly be?"

je "He fought our father, and defeated him, who better to decide which of us is right?"

an "I suppose. At the very least it will shut your damned mouth, woman."

show jezera happy at midright with dissolve

je "Rowan, Andras and I were just having a little- {i}discussion{/i} about our father and his eventual defeat at the hands of yourself and the rest of the armies of Solanse."
je "My brother believes that the failing lies in our father choosing to not to strike hard enough; that, if he had been more brutal when dealing with your people, he would have crushed you before you could regroup and defeat him."
je "I, on the other hand, believe that our father’s fault lay in refusing to ally himself with like minded people."
je "If he had been able to secure the support of all the minotaur clans and the three factions of the skandarii, he would have had the strength necessary to win the war."
je "As you spent years fighting our father’s armies all across the six realms, which of us do you think has the right of it?"

menu:

    "Agree with Andras.":
        $ released_fix_rollback()
        ro "Your brother is probably correct. There were times when the lines were spread so thin that had Karnas pressed on, he may have been able to rout them completely."
        ro "As for alliances, the dark elves care about nothing but their war with the elves, and the clans are far too splintered to ever come together, even to face a common enemy."
        show jezera displeased at midright with dissolve
        je "You men are all the same, small minded. All you ever think about is violence."
        hide jezera with moveoutright
        "The demoness stormed out after having the last word, without giving either the chance to reply. Andras grinned at Rowan."
        show andras happy at edgeright with dissolve
        an "Women, eh? Perhaps you aren’t as useless as you seem."
        #gain relationship with andras, lose some with jezera
        $ change_relation('andras', 5)
        $ change_relation('jezera', -5)
        return

    "Agree with Jezera.":
        $ released_fix_rollback()
        ro " You’re right. If Karnas has pushed harder, he probably would have overexposed himself, weakening his lines. And more brutality would have only galvanized his enemies upon witnessing his cruelty."
        ro "If he could have found some way to unite the tribes, and bring the dark elves around to his cause, he would have outnumbered us. It would have been more than enough to turn the tide of the war."
        an "Pah, you are just as soft headed as my sister! I should have known you’d come out with some crap like this."
        hide andras with moveoutright
        "Showing his usual level of restraint, the demon stormed off down the corridor, knocking down a suit of armour as he left. Jezera beamed at Rowan."
        je "Such a sore loser, that brother of mine. As for you, my hero, perhaps you aren’t as useless as the rest of your gender."
        #gain relationship with jezera, lose some with andras
        $ change_relation('andras', -5)
        $ change_relation('jezera', 5)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label slaver_s_proposition:
#The Slaver's Proposition
#should occur after week 20

scene bg6 with fade

"Rowan had spent the day dealing with the usual goings on within the castle; the ordering of supplies, the arrangement of battalions, small disagreements between soldiers that threatened to spill into bloodshed, and other minor issues known to induce boredom."
"When he signed the last of the parchments that had been placed before him, he asked the chamberlain if that was all, ready to retire to his chambers for the day."
"Apparently, it was not. He had one more visitor, a trader who had travelled all the way from Qerazel. He claimed to have something that would interest the hero, and had been waiting all day."
"With a sigh of exasperation, Rowan signaled for the traveller to be brought in. The doors opened to reveal an overweight Qerazellan, who strode into the room with a brisk pace."
"The way he puffed his chest out and his brightly coloured silks, contrasted against dusky sun-cracked skin, gave him the almost comical appearance of a tropical bird."

tamir "Hello, my friend. Tamir can tell you are a man with a good eye, and has travelled far to bring you his wares."

"Tamir clapped his hands, heavy with gold rings, and a number of female slaves filed into the throne room, chained together by a gold collar, and naked save for the silk veils covering their faces."
"They were all young and in good health, suggesting Tamir was a member of one of the more prestigious slaving organisations."

tamir "Tamir give you a little demonstration, yes?"

"He waved a swarthy hand and the women all kneeled before Rowan in unison without question, clearly they had all been well trained."

tamir "Women all been disciplined well, they do whatever you say without question."
tamir "So, my friend, what say you? Will you take these beautiful specimens off Tamir's hands?"

"The man had brought six women with him today, and as a gesture of friendship in consideration of future business, was willing to let Rowan have them for only 50 gold."

menu:

    "Purchase the women to use as slaves.":
        $ released_fix_rollback()
        "Rowan instructed one of the guard to pay the man, and he rubbed his hands together with glee as the money was placed before him."
        tamir "Tamir knew you were a man of good taste, he is sure we will become very good friends."
        "As he left, he mentioned that Rowan should come and see him if he is ever in Qerazel, as he has a few 'special jewels' that his new friend might be interested in."
        #lose 50 gold from treasury
        #gain small amount of corruption
        #gain 6 slaves
        #small morale increase
        #flag tamir as friendly
        $ change_treasury(-50)
        $ change_base_stat('c', 2)
        $ change_prisoners(6)
        $ change_morale(3)
        $ set_actor_flag('tamir', 'state', 'friendly')
        return

    "Purchase the women and free them.":
        $ released_fix_rollback()
        "Rowan instructed one of his soldiers to pay the man and then to remove the chains from the women, as Tamir looked on in disgust."
        tamir "I guess Tamir was wrong about you, what a waste of good slaves."
        "When he left with his gold, it was clear that he would not be returning. Rowan explained to the women as best he could that they are now free, and instructed the guards to show them to the guest rooms."
        "Once they were ready, he would show them to the portal, and their new life of freedom."
        #lose 50 gold from treasury
        #lose small amount of corruption
        #lose small amount of guilt
        #flag tamir as unfriendly
        $ change_treasury(-50)
        $ change_base_stat('c', -2)
        $ change_base_stat('g', -2)
        $ set_actor_flag('tamir', 'state', 'unfriendly')
        return

    "Kill Tamir and take the women to use as slaves.":
        $ released_fix_rollback()
        "Why would someone pay for the slaves when they could simply take them?"
        "The slaver had no idea when Rowan signalled for the orc behind him to slit his throat, and the look of surprise on his face was priceless."
        "After they cleared away the corpse, Rowan instructed the orcs to take the women to barracks for the soldiers to make use of."
        #gain corruption
        #gain guilt
        #gain 6 slaves
        #gain morale
        #flag tamir as dead
        $ change_base_stat('c', 3)
        $ change_base_stat('g', 3)
        $ change_prisoners(6)
        $ change_morale(4)
        $ set_actor_flag('tamir', 'state', 'dead')
        return

    "Kill Tamir and free the women.":
        $ released_fix_rollback()
        "Disgusted by the slaver and his trade, Rowan signalled for one of the orc guards to take the man away and execute him."
        "Tamir's pleas for leniency fall on deaf ears, not unlike the pleas of the poor women he had sold into slavery."
        "After he had been dragged out of the throne room, Rowan explained to the women the best he could that they were all now free, and instructed the guards to show them to the guest rooms."
        "Once they were ready, he would show them to the portal, and their new life of freedom."
        #lose a small amount of guilt
        #lose a small amount of corruption
        #flag tamir as dead
        $ change_base_stat('c', -2)
        $ change_base_stat('g', -2)
        $ set_actor_flag('tamir', 'state', 'dead')
        return

    "Send Tamir on his way with the women.":
        $ released_fix_rollback()
        "The slaver shook his head in disappointment."
        tamir "That is a shame, Tamir was hoping we could do some business today, but perhaps now is not the best time, eh?"
        "As he left, with the women in tow, he remarked that if Rowan should change his mind, he could find him in the slave markets of Qerazel."
        return
