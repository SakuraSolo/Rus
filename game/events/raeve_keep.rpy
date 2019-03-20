init python:

    #before week 5
    #While on the first mission, this event triggers every time that the player attempts to enter Raeve keep and forces them to go back the way they came.
    event('raeve_keep_visit_before_goal2', triggers='map_res_12', conditions=("week < 5",), group='map_res_fortress', depends=('not week4_introduction',),
        run_count=1, priority=pr_map_res)
    #Subsequent visits before goal 2
    event('raeve_keep_visit_before_goal2_ev2', triggers='map_res_12', conditions=("week < 5",), depends=('raeve_keep_visit_before_goal2', 'not week4_introduction'),
        group='map_res_fortress', priority=pr_map_res)
    ######## When goal 2 is active #########
    event('raeve_keep_visit_goal2', triggers='map_res_12', group='map_res_fortress', depends=('week4_introduction',), priority=pr_map_res)


######### pre goal 2 event ##########
#before week 5
#While on the first mission, this event triggers every time that the player attempts to enter Raeve keep and forces them to go back the way they came.

label raeve_keep_visit_before_goal2:
#First visit

scene bg16 with fade
show jezera neutral behind bg16
show rowan necklace neutral at midleft with dissolve

ro "I'm at Raeve keep, just past the river crossing. Do you want me to scout the place out or move past for now?"

je "Turn around and go back over the river. While that keep is there we can't move soldiers across the river, so ignore that area for now. We will deal with the duke later."
#end event and push Rowan back to previous map hex
$ prevent_tile_exploration()
$ push_to_previous_tile()
$ codex_add('raeve_keep_starting')
return

################################################################################


label raeve_keep_visit_before_goal2_ev2:
#Subsequent visits

scene bg16 with fade
show rowan necklace neutral at midleft with dissolve

ro "Jezera told me to avoid this place for the time being, and it'd be best not to antagonize her."
#end event and push Rowan back to previous map hex
$ prevent_tile_exploration()
$ push_to_previous_tile()
$ codex_add('raeve_keep_starting')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


# shows if "raeve_keep_visit_goal2" event is trigerred in first time
default raeve_keep_visit_goal2_first_visit = True
label raeve_keep_visit_goal2:
######## When goal 2 is active #########

$ codex_add('raeve_keep_starting')
# if this event triggered for second time or more, skip intro part and go to keep options
if raeve_keep_visit_goal2_first_visit:
    $ raeve_keep_visit_goal2_first_visit = False
else:
    jump .keep_options

scene bg16 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral behind bg16
show andras displeased behind bg16

ro "I'm at Raeve keep, the place that the pair of you wanted me to take control of."

je "Excellent, enter the castle as the hero and gather information."

an "Report back with the strength of their defenses and determine how strong of an army we will need to conquer it. This will be our strongest challenge as of yet."

ro "Understood."

scene black with fade

"Rowan openly approached the stone keep. It was one of the smaller castles in Rosaria and served as the seat of power for the duke of Yael's Fork, his home region."
"Duke Doran Raeve was not someone that Rowan had any particular fondness for, especially not after he'd been among those that had fled the siege at Karst. Though it was hard to blame the man fleeing with the others, given that he wasn't even the senior noble after Duke Werden died."
"Still, it was hard not thinking of the duke as anything but a pompous coward."

scene bg15 with fade
show helayna neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

hel "Halt, state your name and business in-"

show helayna shocked at midright with dissolve

hel "Rowan?!"

"His niece on the other hand, was something entirely different."

show helayna neutral at midright with dissolve

"Helayna had been too young to serve in the war with Karnas, but in the years that followed she proved to be a very capable soldier and commander. Her current post as captain of Raeve Keep's guard was deserved, even if she got the post due to her birth."
"Rowan's relationship with her was..."

menu:
    "... that of a teacher and student.":
        $ released_fix_rollback()
        "By her own personal request, Rowan had trained her in the art of the sword and of command. This had been against her uncle's wishes and had always been a divide between the hero and his lord."
        "She'd spent four months as his student, living in Arthdale, though not under the same roof. During that time she had been a good student, one of Rowan's best."
        "Of course, her path eventually lead to that of the horse and knight, so she was eventually forced to continue learning elsewhere."
        "The two remained good friends and Helayna occasionally sought out her old teacher for advice, especially when it came to management or when soldiers were giving her trouble."
        show rowan necklace happy at midleft with dissolve
        ro "I'm glad to see my student is still doing well for herself. Ever vigilant and elegant."
        show helayna happy at midright with dissolve
        hel "My apologies, teacher. I'd feared that... well, since the attack on Arthdale no one has seen you. The lords have been frantic to find out what happened to their best countryman."
        $ helaynaRelationship = 0
        $ helaynaTitle = "teacher"
        $ codex_add('helayna_starting')
        $ codex_add('helayna_rowan_teacher')

    "... old friends, she was one of the few nobles who liked him.":
        $ released_fix_rollback()
        "In the months following the war, she had been a strong proponent for raising Rowan's status in recognition for his service. She'd been opposed on all sides, but most especially by her uncle."
        "It wasn't until Rowan himself had told her he was perfectly happy with his lot in life that she finally gave it up. The two had become good, if distant, friends in the years since. Visiting with her was one of the few things the hero looked forward to when visiting the keep."
        show rowan necklace happy at midleft with dissolve
        ro "It's good to see you Helayna, it's be awhile."
        show helayna happy at midright with dissolve
        hel "I'll say! Where have you been? After the attack on Arthdale you up and vanished on us! The lords have been going crazy trying to find out what had happened to you."
        $ helaynaRelationship = 1
        $ helaynaTitle = "friend"
        $ codex_add('helayna_starting')
        $ codex_add('helayna_rowan_friend')

    "... respected acquaintances.  They'd never really spent time together.":
        $ released_fix_rollback()
        "The two worlds that both lived in prevented either from spending any real time together. Rowan had spoken with her while visiting the keep and had been impressed by her skill in combat. They'd sparred briefly, confirming it."
        "For her part, Helayna had informed him that she had a great deal of respect for him, thanks to his exemplary actions during the war."
        "She always found it unfair that he'd been forced to return to life as a peasant afterwards, but was somewhat relieved when he told her that was what he wanted."
        show rowan necklace happy at midleft with dissolve
        ro "Captain Raeve.  I'm glad to see you in good health."
        hel "You as well,  hero. There's been somewhat of an uproar among the nobility in your absence. Someone of your capabilities vanishing without a trace tends to stir things up."
        $ helaynaRelationship = 2
        $ helaynaTitle = "hero"
        $ codex_add('helayna_starting')

ro "I doubt that there was that much concern over one peasant villager going away for a year."

show helayna sad at midright with dissolve

hel "Alright, most of them haven't cared that much, but at least some of the nobles have been hounding us for answers on what happened to the great Rosarian hero."

show helayna neutral at midright with dissolve

hel "We thought that maybe the demons were targeting the heroes from the war, but none of the others were harmed. Then nothing happened for over a year and everyone's attention turned to dealing with other problems."

show rowan necklace neutral at midleft with dissolve

ro "It didn't have anything to do with me, I've just been trying to hunt down the monsters that attacked Arthdale... they took Alexia."

show helayna sad at midright with dissolve

hel "I'm so sorry Rowan. I assume then that you've returned because you heard the rumors?"

ro "Which rumors are those?"

show helayna neutral at midright with dissolve

hel "That the demons have returned. Word of new attacks has started to circle around, suggesting that they're now hitting the other villages in Yael's Fork."

show rowan necklace angry at midleft with dissolve

ro "Please tell me everything you know."

hel "Of course, [helaynaTitle] Rowan. Come into the keep, I'll explain everything there. The Duke will wish to speak to you as well, now that you've returned."

if helaynaRelationship == 0:
    hel "I could honestly use your help as well.  The state of things is... not good."

else:
    pass

scene bg17 with fade

"Helayna led Rowan to the main hall and dispatched one of the other guards to inform lord Raeve of their arrival. Then informed him exactly what they knew about the attacks. It wasn't much, mostly baseless rumors with a grain of truth sprinkled in."
"A red demon covered in tattoos was the one unifying detail, which Rowan confirmed was involved in the attack on Arthdale. He figured there was no reason to lie about that, given it was common knowledge at this point."
"Then it was Rowan's turn to share what had happened to him. He spoke of Alexia being abducted and the demand that he come to Bloodmeen Castle, but then spun it as if he'd discovered the castle still abandoned and assumed he'd been misled."

show rowan necklace neutral at midleft with dissolve
show helayna neutral at edgeleft with dissolve

ro "After that, I started the journey back home. I only just arrived back in Rosaria a few weeks back. It seems strange, I'd feared that the demons sought to distract me, but you said the attacks only started recently?"

hel "Indeed, their actions don't have an obvious reasoning behind them. There's something that we're missing here. Oh! My lord."

"The armored woman stood up and gave a bow. Rowan turned around and saw the duke approaching them from behind him. He stood up and gave a customary bow as well."

ro "Lord Doran Raeve, it is good to see you again."

show doran neutral at midright with moveinright

$ codex_add('doran_starting')

dor "I'm sure it is. Where have you been, boy? Rosaria is going to the pits of chaos. There's been a rise in banditry, a famine looms on the horizon, and it sounds as if the goblins in Blackholt are getting antsy."
dor "I've barely managed to secure enough food in my cellars to keep mine and my forces through the winter. I fear after we're through that I'll have to send knights out to plow the fields, there's no way the peasants will last."

ro "My lord, you've taken all the spare food in Yael's Fork?"

dor "Everything I could get my hands on. All the upper houses are following the baron's lead in securing everything we can. I've had to put down a couple rebellions trying to resist us buying it up too."

"The duke took a seat at the head of the table, at which point both Rowan and Helayna sat back down. The hero was grateful, it let him clench his fists under the table. Dealing with Doran was always trying, but to hear him so casually talk about starving his subjects..."

ro "I was explaining to Captain Helayna that I'd been to castle Bloodmean. The demons that attacked Arthdale claimed they'd take up residence there, but when I arrived I found it was still abandoned from the war."

dor "You fool! It was all a distraction, an attempt to get you away so their schemes could move unhindered. They're probably responsible for both the famine and the goblins! I see it now, I'll have to inform the baron."

show doran neutral at edgeright with move

"He stood up and started to leave the hall."

ro "Sir? Is that all?"

dor "Hmm?  Oh yes, just go and do hero things Rowan. Try to undo the damage your absence has caused. Maybe start with those brigands holed up in the forest West of Arthdale. The lords will clean up the real mess, we'll tell you if you need to stick your nose in it."

hide doran with moveoutright

"With a dismissive wave he departed, leaving the hero amazingly irritated. Was that man always so insufferable?"

hel "Apologies, [helaynaTitle] Rowan. My uncle is vain and doesn't always speak well to those below his status."

show helayna angry at edgeleft with dissolve

hel "Then he's all smiles and the perfect picture of courtesy when another lord visits."

if helaynaRelationship == 0:
    show rowan necklace happy at midleft with dissolve
    ro "Oh yes, I remember. He had quite a few choice words for me when you sought me out behind his back."
    show rowan necklace neutral at midleft with dissolve
    ro "Though he was never so dismissive to me before."
    show helayna sad at edgeleft with dissolve
    hel "He's stressed by the current situation. I think he fears that the baron blames him for your absence. In the last few months he's been trying to downplay your importance as a hero."
    show rowan necklace shock at midleft with dissolve
    ro "Why would he do that?"
    show helayna neutral at edgeleft with dissolve
    hel "To brush off his problems, make things seem better off? It isn't my place, I'm just the guard captain and you are my teacher."
    hel "I was hoping that maybe you could take a look at our garrison and offer your opinion? You can tell me the details of your journey at the same time."
    "The hero twitched slightly at this before giving his answer."
    show rowan necklace neutral at midleft with dissolve
    ro "Sounds good."
    show helayna happy at edgeleft with dissolve

elif helaynaRelationship == 1:
    "She shook her head in obvious frustration."
    hel "They're all the same, damn traditionalists."
    ro "Still wishing you'd convinced him to make me a noble or a knight?"
    hel "Oh don't bring that up!"
    ro "Hey, you were the revolutionary. I just wanted to live with my wife in peace. It seems that demons don't like that idea too much."
    show helayna sad at edgeleft with dissolve
    hel "On that note, I'm somewhat concerned about the state of our defenses in the event of a demonic attack. If you aren't in a rush anywhere, would it be possible for you offer your advice on how to handle one?"
    "The hero twitched slightly at this before giving his answer."
    ro "It would be my pleasure."
    show helayna happy at edgeleft with dissolve

else:
    ro "Let's not talk about the duke anymore. Perhaps you should give me a tour of your fortifications so I can have an idea of how well you'd hold out against a demon attack, should it come?"
    show helayna happy at edgeleft with dissolve
    "Brightening, the woman noded."
    hel "I think that's an excellent idea. You can tell me anything else about your journey at the same time."

"The woman stood up and held out a hand to the still seated man."

hel "Shall we, [helaynaTitle]?"

show rowan necklace happy at midleft with dissolve

"Rowan chuckled at her presented hand."

ro "Isn't it usually suppose to be the man who helps the woman rise?"

hel "Only if she's a lady. I am first and foremost, a knight."

menu:
    "Accept her hand and let her lead the way.":
        $ released_fix_rollback()
        $ helaynaHand = True
        "Rowan accepted her hand, letting her help him to his feet."
        ro "Lead the way."
        hel "It would be my pleasure."

    "Stand on your own.":
        $ released_fix_rollback()
        $ helaynaHand = False
        ro "Please don't make me choose between my pride and insulting you."
        show helayna sad at edgeleft with dissolve
        "She suddenly retracted her hand with a worried look on her face."
        hel "I'm sorry, I didn't mean to put you on the spot-"
        "The hero held up a hand to silence her as he stood up."
        ro "Relax, it's fine. Let's go."
        "He set off towards the barracks, letting the captain fall in behind him."

scene bg17 with fade

"The two of them inspected the barracks, the fortifications, and the food stores. For all of Helayna's worries, Rowan had to admit that things were far better than she thought. What few forces they had were well trained and there were plenty of supplies in the event of a siege."
"Still, it was a peacetime garrison, one that mostly existed as simply a formality rather than a legitimate military force. Most of the knights were veterans from the war, serving as honorary guards, though there were also some younger ones."
"In all, Rowan counted (forty) of their number, all with full suits of armor and well maintained weapons. Along with a dozen horses in the stables."
"The walls were in decent repair. No major weaknesses or obvious ways around them. That was, unless one could trick the defenders into opening the gates for their enemies."

if helaynaHand == False:
    "Helayna followed on Rowan's heels the whole time, hanging onto his every word, eager to answer every question to the best of her knowledge."

else:
    "Helayna showed everything off with a mix of both eagerness and trepidation. She desperately wanted to know what Rowan had to say, but also dreaded what it might be."

"This betrayal of her trust made Rowan feel sick, but he didn't let it show on his face.  The weight of Jezera's necklace was something he was keenly aware of."

scene bg16 with fade
show rowan necklace neutral behind bg16
show andras displeased behind bg16
show jezera neutral behind bg16

"A little over an hour later, Rowan stood on a hill nearby the keep. While still in sight of the small fortress, he was well outside of earshot of anyone who might be listening to him as he relayed details of the defenses to his masters."

ro "That's about it. I can probably trick the soldiers into letting our forces in if we attack, unlike most of the lord's family, they trust me."

an "Very well, when do we launch our assault?"

je "Patience brother, there might be other ways we can still take the keep than the bloodshed you seem to love so much. Besides, our forces may not be up to the task yet."
je "What is your opinion Rowan?"

################################################################################

# Keep option menu
label .keep_options:

ro "(Raeve keep has a military power of 150.)"

menu raeve_keep_assault_menu:
    "Launch an assault.":
        $ released_fix_rollback()
        #troop selection (to do)
        call screen raid_menu(150)
        if not raid_state.in_raid:
            jump raeve_keep_assault_menu
        else:
            $ raid_state.finish()
        jump raeveCapture

    #Speak with the occupants. (only if you have a reason to.)
    #Raeve keep events (To do)

    "Send in an infiltrator." if len(get_spies('idle')) > 0:  #(only if you have a free spy.)
        $ released_fix_rollback()
        # Spy selection page
        $ menu_res = renpy.display_menu([(spy.name, spy.uid) for spy in get_spies('idle')])
        $ tmp_spy = get_object(menu_res)
        call raeveInfiltrate(tmp_spy) from _call_raeveInfiltrate
        return

    "Leave for now.":
        $ released_fix_rollback()
        #return character to previous map square
        $ prevent_tile_exploration()
        $ push_to_previous_tile()
        return

################################################################################


label raeveCapture:

scene bg16 with fade
show rowan necklace neutral behind bg16

ro "It's time to launch our attack on Raeve keep. Andras, gather your forces and I'll explain my plan...."

scene bg15 with fade
show helayna neutral at midleft with dissolve
show rowan necklace neutral at midright with moveinright
show jezera disguised neutral at edgeright with moveinright

ro "Captain Raeve, this woman says that she knows where the demons are operating from."

show helayna shocked at midleft with dissolve

hel "Is that true?"

je "Yes, they captured me not long ago, but I managed to escape. The great hero here says that you'll be able to take them down? There aren't many of them."

show helayna happy at midleft with dissolve

hel "Yes, of course. You must have been through quite the ordeal. Please come inside."

ro "You two go on ahead. There was something about the walls that was bothering me that I need to check."

hel "Very well, but please don't take too long [helaynaTitle]. I believe we will need your advice soon."

hide helayna with moveoutleft
hide jezera with moveoutleft

scene bg17 with fade
show rosarian knight neutral at midleft with dissolve
show rowan necklace neutral at midright with moveinright
show andras angry behind bg17

"Rowan turned to the side and stepped into the small guardroom, where the mechanism for raising and lowering the portcullis was kept. Inside was a single knight sitting at a table."
"The armored man stood up when Rowan entered and gave a short bow."

rkn "Hero Rowan, what brings you in here?"

ro "I was worried about the door mechanism. Something was off when I was doing my inspection, but I just couldn't figure out what."

rkn "Sir, I assure you it is in perfect working order."

ro "Can we check it over, just to make sure it won't end up jammed if an attack comes?"

rkn "As you wish."

"The armored man turned to the side, looking down at the crank as Rowan shut the door behind him. Then he slipped out a dagger and buried it in the knight's neck, slipping between into the weak space between the main armor and the helmet."

show bg17 with flash
show rosarian knight injured at midleft with dissolve
play sound "music/SFX/BodyfallDirt.ogg"
pause 1
hide rosarian knight with dissolve

"He fell to the ground with a wet gurgle. It was over too fast for him to shout a warning or even realize who had stabbed him."
"For his part, even Rowan was somewhat shocked at how he'd killed the man. A Rosarian knight at that, one who'd obviously respected him as a hero. A shudder ran through his body. He fingered the sapphire amulet at his neck, which steadied his shaking hands."
"A handful of spears were laying in the corner of the small gatehouse. Rowan grabbed two of them, one he stuck into the portcullis crank, jamming it open. The other he used to brace the door to the room closed. Finally he sent a one word message to his master:"

ro "Now."

"A few moments later, a shout echoed high above. Then other shouts all confirming the same thing. Attackers were in sight."
"Someone started beating on the door to the gatehouse."

show rosarian knight neutral behind bg17

rkn "Sir Haris, close the portcullis! The crank on the walls seems to be jammed! Sir Haris?!"

"Rowan looked at the fallen knight on the floor and shuddered again."
"The banging and shouting at the door increased in intensity, then those on the other side began trying to break the door down. The spear held. A moment after that it was too late."

rkn "They're upon us! Forget the gate, man your stations!"
rkn "Where is Helayna? Why hasn't someone fetched her?"
rkn " Didn't the hero just get here? Find him instead!"

"What was once the distant roar of orcish screams of battle had become deafening. Battle was joined and Rowan could hear the sound of Andras's army pouring through the open gates. Then came his master's voice."

an "Hahaha! Kill them all in my name!"

"There was no need to hold the gatehouse anymore, so Rowan pulled out the spear he'd used to jam the door and prepared to join the battle."

hide rowan with moveoutright

scene black with fade
show rowan necklace neutral behind black

"He'd hardly needed to, there was nothing but chaos on the other side. The defenders had almost no direction and couldn't seem to mount a coordinated defense to deal with the savage attackers. The superior equipment of the knights was simply overwhelmed by the stronger orcs."

# TODO
# if cubi sorcerers participated in the battle: (to do when troop selection is added)
# "The cubis darted about at the same time, strengthening those who were losing their fights or flinging magically attacks at archers attempting to pick others off. One had even entwined themselves with one of the defenders and had turned him against his fellows."

"Most terrifying of all was the tattooed red demon, Andras himself. He moved about the battlefield, casually blasting foes with his magic to disable them with incredible pain, or to suddenly dart forwards and pierce through weak points in their armor with his bare hands."

scene cg107 with fade
show helayna angry behind cg107
pause 3

"Then an arrow struck him in the stomach, causing Andras to stumble backwards in shock."

hel "Knights to me! For Rosaria, for Raeve!"

"The red haired captain lowered a bow as she made her proclamation and started rallying the defenders. It looked as if perhaps she might turn the battle around. Rowan drew his sword, fearing he would need to join the battle but found his hands were shaking again."
"Then he looked up and realized that his fears were unfounded. Jezera had shed her disguise and was standing on the ramparts of the inner keep, magic smoking at her fingers."

#CG variation with blue ribbons added.

"Blue ribbons of energy shot down and whipped at the knights, tripping up some, striking others, and completely destroying any attempt at restoring morale. Still, Helayna made a valiant effort and stood her ground with those she'd rallied."
"The rest of the keep fared far worse."

scene black with fade
#CG of Helayna and knights surrounded by orcs and Rowan.

"Very soon, only Helayna and a handful of knights remained amongst the forty defenders in the keep's garrison. They'd made it to a secluded part of the keep, safe from Jezera's magic, but completely surrounded by enemies on all sides."
"Orcs jeered at the cornered knights, but none of them made any move to break the standoff."
"Hoping to prevent further bloodshed, Rowan pushed his way past the orcs.  Standing in front of Andras's forces, he addressed their remaining enemies."

show helayna neutral behind black

ro "Helayna, knights, please surrender. The battle is lost, end it before more lives are."

show helayna shocked behind black

hel "Rowan? What are you doing?"

if helaynaRelationship == 0:
    show helayna crying behind black
    "Tears welled up in her eyes, then streamed down her face."
    hel "No, no no no, teacher why? Why would you turn on your people, on those that trust you? How could you do this to me?"
    "She fell to her knees, still sobbing uncontrollably. The soldiers around her looked almost equally distraught, many of them visibly agitated or shaking. One dropped his sword, the impact of which sent a ripple through their ranks."
    "Then another blade hit the ground. Cracks had already started to form in their resolve from their captain's breakdown, with each weapon clattering to the ground being another leak in the dam."
    "Finally it broke, and the last of the Raeve knights surrendered."
    scene bg15 with fade
    show jezera happy behind bg15
    show helayna crying at edgeleft with dissolve
    show rowan necklace neutral at midleft with dissolve
    "Rowan rushed forward to help Helayna while the orc soldiers started stripping the defenders of their armor and chaining them as prisoners."
    hel "Why? You're the one person I trust above all others. The one who made me deserving of this post."
    "The former hero helped his student regain her feet with one hand, fingering his amulet with the other."
    ro "They took Alexia, then they imprisoned me. I still wear their chains and they'll kill both of us if I disobey."
    show andras angry at edgeright with moveinright
    "Both of them looked up as Andras approached them, an arrow still protruding from his belly and a look of fury in his eyes."
    an "Kill... that... bitch. That's an order, servant."
    "Before Rowan had a chance to respond, Jezera's voice drifted down from above them."
    je "That will hardly be necessary, brother. Our hero shouldn't have to kill a beloved student just to heal your fragile pride."

elif helaynaRelationship == 1:
    hel "No, it must be a trick. You can't be the real Rowan, the man I knew would never turn on his people. He loved his life!"
    ro "It is me. Even if it wasn't, look around. You're hopelessly outnumbered."
    "Several of the other knights around Helayna fidgeted nervously. They knew their situation was hopeless and evidently at least some of them did think that Rowan was their real hero. This was not lost on their captain."
    show helayna angry behind black
    hel "Stand strong men. Did our hero give up even against impossible odds at Karst?"
    ro "That was different."
    hel "What would you know, false hero?!"
    "Rowan gritted his teeth. Her words bit into him in a way she hadn't intended. The reaction actually caused Helayna's expression to change."
    show helayna shocked behind black
    hel "Huh? Wait, you said that they took your wife... you didn't!"
    "The hero grabbed the amulet on his neck, frustrated at the situation, angry with himself for agreeing to this, and also hopelessness at having no other options. He tried to tear the damn thing from his body."
    "It wouldn't come off."
    show black with flash
    #crackle sfx
    scene bg15 with fade
    show rowan necklace neutral at midleft
    show helayna shocked at edgeleft with dissolve
    hel "Ahhh!"
    "There was a sudden bright flash of light and a red circle of power formed over Helayna's body as she fell to her knees screaming in pain."
    show andras angry behind bg15
    an "Bitch."
    hide andras
    show andras angry at edgeright with moveinright
    "Andras had returned. An arrow still protruded from his side, but that wasn't stopping him from using the full force of his magic to punish the one who'd hurt him. There was a single-minded fury in his eyes."
    "With their captain bowed, the knights broke in an instant. Those that didn't throw down their weapons were overwhelmed by the orcs who charged them."
    an "Servant, kill her."
    "Rowan could respond, Jezera's voice drifted down from above them."
    show jezera happy behind bg15
    je "Now now, brother, do you plan on making our hero kill all of his friends? That's hardly an effective way to endear him to our cause."
    "Andras released the woman from his power and turned his attention upwards."

else:
    show helayna angry behind black
    hel "Is this a trick or a betrayal? Hmph, it makes no difference. Nothing you say will change anything, I will stand against these monsters until my dying breath."
    ro "Look around, you're hopelessly outnumbered.  Please, don't throw your lives away for nothing."
    hel "Be silent, servant of demons!"
    "Her resolve was absolute, however the rest of her forces were not so eager to continue the fight. If the captain fell, her forces would follow. All Rowan needed to do was...."
    show black with flash
    #crackle sfx
    scene bg15 with fade
    show rowan necklace neutral at midleft
    show helayna shocked at edgeleft with dissolve
    hel "Ahhh!"
    "There was a sudden bright flash of light and a red circle of power formed over Helayna's body as she fell to her knees screaming in pain."
    show andras angry behind bg15
    an "Bitch."
    hide andras
    show andras angry at edgeright with moveinright
    "Andras had returned. An arrow still protruded from his side, but that wasn't stopping him from using the full force of his magic to punish the one who'd hurt him. There was a single-minded fury in his eyes."
    "With their captain bowed, the knights broke in an instant. Those that didn't throw down their weapons were overwhelmed by the orcs who charged them."
    an "Servant, kill her."
    "Rowan could respond, Jezera's voice drifted down from above them."
    show jezera happy behind bg15
    je "I think that's enough senseless killing for the day. There will be no more deaths, take everyone who's left prisoner."
    "Andras released the woman from his power and turned his attention upwards."

hide jezera
show jezera neutral at midright with dissolve
"The voice's owner soon arrived on the scene, sliding down the wall on her ribbons of power."

an "You dare come between me and my vengeance, sister?"

je "Tearing her apart limb from limb would only be a temporary distraction. Why don't you take care of our prisoners and start looting our new keep? That's something you'll enjoy that has an actual long term benefit."

show andras displeased at edgeright with dissolve

an "Very well."

hide andras with moveoutright

show helayna angry at edgeleft with dissolve

hel "So now what, am I going to be a prisoner?"

ro "Andras is the jailer. She's as good as dead if we bring her back to Bloodmeen!"

show jezera happy at midright with dissolve

je "No, we're going to let her go."

hel "Just like that?"

je "Well, on one little condition. I can't have you going around telling everyone about how your great hero is now serving demons, after all."

"The blue skinned woman pulled a small obsidian band from a pouch."

je "Just put this on your finger and you're free to go. Otherwise, I'm afraid I'll have to leave you to my brother."

"After staring at the ring for a moment, the knight captain angrily threw off one of her gauntlets and held out her hand. With a flair and a pleasant smile, Jezera placed the band on Helayna's finger. Then stepped back and motioned for Rowan to release their captive."

show helayna aroused at edgeleft with dissolve

hel "What was, oh, hot, hot...."

"Apparently now heedless of her surroundings, the knight started stripping off her armor. Sweat poured off her while she worked at the clasps and hooks, constantly muttering about being too hot."

"Rowan looked away from her, not wanting to know what would happen next."

je "Oh, not interested in playing with her?  It looks like she's positively begging for it. Tell you what hero, since you were the one responsible for delivering a keep to us, I'll keep the orcs back so you can have first crack at lovely Helayna here."

show jezera neutral at midright with dissolve

je "With that band on her, she's desperate for cocks now. I wonder if all our green boys will even be able to satisfy her? It doesn't look like she's been broken in before and orcs don't exactly make for the gentlest lovers."

show jezera happy at midright with dissolve

je "You aren't going to leave her to those brutes are you? Some stretching first would do her good. Or... maybe you'd rather watch them go at it for a bit before we pay the duke a visit?"

$ codex_add('helayna_keep_taken_by_force')

menu raeve_keep_helayna_menu:
    "Try to protect Helayna" if not raeve_keep_rowan_tried_protect_helayna:
        $ released_fix_rollback()
        ro "No, this is wrong. I won't let anyone touch her."
        je "But look how much she needs it. You can't possibly deny her cocks now, unless you intend to claim her for yourself? My hero, how noble of you!"
        "Her voice dropped and she started whispering in Rowan's ear."
        je "Tell you what, if you fuck her right now I'll keep the others from her and let you keep her as your prize. Assuming she agrees to come along back to Bloodmeen, which I suspect she'll be all too happy to, I'll deliver her to your room to enjoy."
        je "Though, I wonder just how Alexia will react to find that her husband has brought another woman home to his bed? Will you assemble a harem of women from each new conquest? Just to protect them, of course."
        #Note player tried to protect Helayna.
        $ raeve_keep_rowan_tried_protect_helayna = True
        #Re-present choice, but with this option removed.
        jump raeve_keep_helayna_menu

    "Fuck Helayna.":
        $ released_fix_rollback()
        jump fuckHelayna

    "Watch the orcs fuck Helayna.":
        $ released_fix_rollback()
        "Rowan finally turned his gaze back to the woman on the ground, but made no move to approach her. After a moment, Jezera spoke up behind him."
        je "Looks like she's all yours boys. We'll watch round one."
        "With permission given, several orc soldiers started crowding around Helayna while shedding their armor and anything else that might be in the way."
        show cg54 with fade
        "After a little posturing and shoving, one of the largest males got down on the ground and lifted the woman on top of him so that he could penetrate her anally while another large orc took her in the pussy."
        jump orcsHelayna

    "Refuse.":
        $ released_fix_rollback()
        ro "No. I want no part of this."
        show jezera displeased at midright with dissolve
        je "A pity. Well then, we'd best be on our way."
        "The demoness lead Rowan deeper into the keep, leaving the sounds of Helayna and the orc soldiers behind them."
        jump confrontDuke

label fuckHelayna:

$ codex_add('helayna_keep_taken_by_force_fucked_by_rowan')

show helayna naked aroused at edgeleft with dissolve

"Rowan finally turned his gaze back to Helayna. She'd nearly removed all her armor and was using one of her hands to furiously masturbate herself. The franticness of her pace was only stopped for the moments when it took both hands to remove something."
"Once she'd managed to get everything off, her gaze started darting around the courtyard with a desperate gleam. She caught her [helaynaTitle]'s gaze and then dropped to the ground on her backside."

hel "Please... I need... I need...."

# CG of Helayna laying on the ground and presenting herself.
scene cg310 with fade
show jezera happy behind cg310
show rowan necklace neutral behind cg310
show helayna naked aroused behind cg310
pause 3

"Her furious self pleasure ceased and she spread her legs wide as well as her womanly lips with the fingers that had just been knuckling her as fast as possible."
"Hands from behind him started playing over Rowan's body, stroking his shoulders and gripping his cock through his pants."

je "Look how desperately she wants you. What kind of a man wouldn't give her what she needs?"

ro "You made her like this! This isn't who she is."

je "My band did change her priorities a little bit, but her desires turned to you first. That had nothing to do with my influence. She does want you. Deep down, she always has. Take her."

"The demoness pushed her servant forward, towards the woman who was writhing on the ground with a mix of need, pain, and arousal on her face. Somewhat hesitantly, Rowan moved his hands to loosen his garments, freeing his erection from his pants."
"A small part of him was surprised to find that he was actually aroused by this. The part that was now in control thought it the only appropriate answer."

scene cg59 with fade
show jezera happy behind cg59
show rowan necklace neutral behind cg59
show helayna naked aroused behind cg59
pause 2

"Unable to look at her in the eye, he pulled her up to her knees and positioned himself behind her, not bothering to strip off any of his other clothing."
"He pushed into her folds, finding them incredibly hot and slick with arousal. She gasped in shock at the penetration, then let out a sigh of incredible relief."

hel "Rowan, Rowan, my [helaynaTitle], my wonderful hero."

je "Listen to how much she wants you. All this time she's wanted you, but her duties and her honor required that she never act on it. My magic has liberated her from those chains."

hel "Fuck me. Please, please fuck me Rowan!"

"The man started moving his hips, slowly pumping his cock in and out of the knight's needy sex from behind. There were appreciative sounds in response to this, but also a slightly pained mewling. A hand was placed on Rowan's shoulders and he looked up to see Jezera smiling at him."

je "My hero, she asked you to fuck her. This slow, romantic stuff isn't fucking. Go hard, go fast!"

"He did so, roughly pushing into Helayna and roughly groping her body. This instantly caused screams of blissful pleasure and encouragement from the woman in front of him. This served to drive him to be even harder and more abusive, which seemed to make her even happier."
"Rowan really was fucking her with no regard for her well being or pleasure. This was probably her first time; he was claiming her virginity and doing it so crassly! The fact that she seemed to absolutely love it felt wrong, but he only pushed her even more."

scene cg59 with sshake
show cg59 with sshake
show cg60 with flash
show helayna naked aroused behind cg60
pause 2

"While it seemed to go on for an eternity, in truth such a frantic pace brought Rowan to a climax in under a minute of first penetrating the woman. Slightly dazed, he looked down at the woman before him."
"She looked back at him in confusion."

hel "Why did you stop?  I still need you!"

scene cg61 with dissolve
show jezera happy behind cg61
show rowan necklace neutral behind cg61
show helayna naked aroused behind cg61
pause 2

"As if finally realizing what he'd just done, the hero pulled back and staggered away. A trail of his cum followed him, some of it dripping out of his deflating member but also a great deal from the pussy he'd just fucked raw."
"Helayna let out a cry that was a mix of panic and disappointment."

hel "No!  Come back! Fuck me! Oh Goddess, fuck me!"

"Now that he was apparently done with the knight, several orc soldiers started to crowd around the woman now writhing on the ground, while shedding their armor and whatever else might be in the way."

#Rowan gains corruption
$ change_base_stat('c', 2)

menu:
    "Claim Helayna for yourself.":
        $ released_fix_rollback()
        ro "Stay away, all of you.  I claim this woman as my property, if she will accept me."
        hel "YES! I'm yours! Please take me again, oh Goddess, I've wanted you all my life Rowan!"
        "The eagerness that she said that actually stunned Rowan, making him feel very uncomfortable."
        je "Well, it sounds like she isn't interested in freedom anymore. Very well, this woman now belongs to Rowan, the rest of you can find other girls in the castle to satisfy yourselves."
        scene bg15 with fade
        show rowan necklace sad at midleft with dissolve
        show helayna naked aroused at midright with dissolve
        show jezera happy at edgeright with dissolve
        hel "Oh [helaynaTitle], why do you look so sad? Don't you like me? Please fuck me again, I need you, I want to make you happy!"
        "The demoness moved up to the woman on the ground, who'd started touching herself again as she continued presenting her womanhood to Rowan that his cum was drooling out of. She pressed her hand to the woman's head and a moment later Helaya was unconscious."
        hide helayna with dissolve
        je "She'll be waiting for you in your room when you return to Bloodmeen. For now, we have a meeting with the duke to take care of."
        #If player tried to protect Helayna, reduce corruption slightly.
        if raeve_keep_rowan_tried_protect_helayna:
            $ change_base_stat('c', -2)
        #Helaya is assigned to sharing Rowan's bedroom, forcing Alexia out if she was there. A confrontation event between Rowan and Alexia will trigger at the end of the week.
        $ raeve_keep_rowan_claimed_helayna = True
        $ codex_add('helayna_keep_taken_by_force_claimed')
        jump confrontDuke

    "Watch Helayna get fucked by the orcs.":
        $ released_fix_rollback()
        show cg54 with fade
        pause 2
        "After a little posturing and shoving, one of the largest males got down on the ground and lifted the woman on top of him so that he could penetrate her anally while another large orc took her in the pussy. It was still leaking Rowan's cum, but the orc didn't seem to care."
        jump orcsHelayna

    "Don't watch.":
        $ released_fix_rollback()
        #keep courtyard
        scene black with fade
        show jezera happy at midright with dissolve
        show rowan necklace sad at midleft with dissolve
        "Rowan tore his eyes away from the scene and quickly did up his garments. He found that Jezera had her hand on his shoulders again."
        je "You did me proud, my hero. However, now we've got a visit we need to pay to the duke."
        "The demoness lead Rowan deeper into the keep, leaving the sounds of Helayna and the orc soldiers behind them."
        jump confrontDuke

label orcsHelayna:

$ codex_add('helayna_keep_taken_by_force_gangrape')

"It wasn't just the males that were interested in Helayna. A female orc soldier laid claim to her face, pressing her green sex down onto the captain's mouth and silencing her cries of pleasure."
"Two final orcs joined their fellow soldiers, one male and one female, each getting a hand to start pleasuring them."
"Rowan felt a strange sense of morbid fascination as he watched events unfold."
"The two orcs who had been taking her lower holes had settled into a brutal rhythm of sorts, since they found it difficult to move while both of them were inside Helayna at the same time, they alternated between penetrating and pulling out for the other to enter."
"The two who were currently receiving a handjob and a fingerjob were casually talking to some of the observers about Helayna's skills. Those next in line were curious about the best place to be and were already figuring out a pecking order."
"Beastial cries of pleasure flew over all of it, not from the woman being used, but from the larger green woman who was using her face as a sex toy. She shamelessly screamed her lusts for all to hear, then climaxed and rose off of the red head."

show cg55 with dissolve
pause 2

"Between the many bodies, Rowan was able to catch sight of Helayna among them. Her eyes had rolled back and she'd stopped saying anything that might be a cohesive thought."
"All her face said was pure ecstasy and need, a tongue out searching for the lost pussy that she'd been licking a moment before."
"This time a male took her face, forcefully trying to jam his massive member down her throat. He failed, tried again, and finally returned to the onlookers to wait for a chance at the other end instead."
"He got his chance soon afterwards, at the same time as another woman took over the face."
"Rowan continued to stare until Jezera placed her hand on his shoulder and turned him away."

scene bg15 with fade
show jezera happy at midright with dissolve
show rowan necklace sad at midleft with dissolve

je "This will probably go on for hours, so we'd best finish up our business with the duke now. Don't worry, you can come back and watch more afterwards."

"The demoness lead Rowan deeper into the keep, leaving the sounds of Helayna and the orc soldiers behind them."

jump confrontDuke

label confrontDuke:

scene bg17 with fade
show jezera neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

"They passed through the hall and up the stairs. Eventually, the duke was located inside his bedroom, having barricaded the door. It took Rowan three tackles to knock the elaborate, but not terribly formidable, door open."

#CG of Raeve cowering before Jezera.
scene black with fade
show jezera neutral behind black
show doran shocked behind black

"Inside, a terrified duke Raeve waited cowering in one of the corners, whimpering slightly."

je "Pathetic wretch. Is this all the pride you can muster? Such a change from when the two of us first spoke."

"She glowered angrily over the terrified man. He tried to back up, found there was no where to go, then tried to straighten his back and put on a strong face."

dor "D-demon, s-stay back! I'm a duke of Rosaria, the baron will make you p-pay for this!"

"It was a very poor showing. Jezera slapped him across the face and he crumpled to the ground once again."

dor "Please don't hurt me!"

je "Hmph. You don't deserve to rule over anything. Let's see how well you can perform at other tasks."

#CG of Raeve holding Jezera's foot.
scene black with fade
show jezera neutral behind black
show doran shocked behind black

"She lifted up a foot, slipping it out of her shoe and pressing it against the side of the duke's face."

je "Kiss it."

"After a moment's hesitation, the duke took her blue foot in both hands and kissed the top of it."

je "Good."

"A swirl of energy started to surround Jezera."

je "Keep going. We'll have to see about fixing that attitude of yours, maybe something else too? It isn't like there's anything worth saving in that useless head."

menu:
    "Continue watching Jezera dominate the duke.":
        $ released_fix_rollback()
        jump dominateDoran

    "Leave Jezera to her business.":
        $ released_fix_rollback()
        "Sensing that his presence was no longer necessary, Rowan turned away from his mistress and the former duke of Yael Fork. He left them and headed back into the main keep."
        jump raeveEnd

label dominateDoran:

"Reave looked at her foot for a moment in confusion, then started kissing the tops of each of her toes. At the same time, the demon woman placed one of her hands on his head and the energies from her surrounded him."

je "What is your name?"

dor "Doran?"

je "No silly man, you don't have a name."

"He blinked several times, opened his mouth to speak, then stopped."

dor "Why don't I have a name? I thought I was a noble."

je "You are a slave. Slaves don't deserve names."

dor "But, I'm not a slave."

je "Really? What kind of a man does what you're doing right now?"

"The duke looked down at the foot still in his hands, hesitated, then kissed it again."

je "That's right. Now, time to move up my leg."

"He laid kiss after kiss up the blue skinned leg. His motions seemed somewhat jerky or robotic, this wasn't something he'd done before. However, this wasn't the reason that Jezera suddenly put her hand on his face."

je "No, stop. You're not touching my pussy with that awful beard. We're shaving that off right now. Where is your razor?"

"After pulling her leg free, she sent the man scurrying off to the side of the room where a desk and mirror rested. He extracted a set of scissors, shaving razor, and cream and showed them to Jezera."

je "Give me that."

#Show CG of Raeve's beard being cut off.

"She took the scissors from Raeve and roughly started cutting his mustache off. There was no protesting or complaining, just dull eyed observation as the man's facial hair fell away."
"After the top had been trimmed short, Jezera moved on to his beard and had that off in short order as well."

#CG of Raeve's beard trimmed short and patchy.

"Only now did the man react. He raised up a hand and patted the patchy short bristles while looking at himself in the mirror. The demon payed no mind, focused on slathering cream over what remained."
"There was some satisfaction that Rowan felt, seeing this man brought down like this, but it also seemed wrong at the same time. He couldn't decide if he was enjoying this or not."

je "Cut it off."

"She stuffed the razor into Raeve's hand. He raised it up slowly to his ear, then stopped. A long moment passed before the demon seemed to run out of patience and put her hand on his head to work her magic again."

je "I said, cut it off."

"Raeve did so.  He shaved off the last vestiges of his mustache and beard one stroke at a time.  At first he would hesitate before starting each cut, but by the end he seemed almost eager to become clean shaven."
"Now finished, he set his razor down on the desk and whipped off the rest of the cream with a towel. The shorn duke received a ruffle of his hair as a reward."

je "Now that's such an improvement! I always hated facial hair. Why don't we pick up where we left off?"

#CG of foot kissing, no beard variant

"She pulled him out of the chair and forced him back onto the ground. After putting both hands on his head, Jezera stopped and seemed to change her mind. After releasing her grip, she instead presented her foot once again."

je "Kiss your mistress' foot again."

"He did so."

je "Say your mistress' name, say Jezera."

dor "Jezera."

je "Good boy.  Who do you love?"

dor "Jezera."

je "That's right. Do you want to make her happy?"

"He nodded vigorously."

je "So eager! Then let's see how well you lick pussy."

scene cg265 with fade
show jezera happy behind cg265
show doran beardless neutral behind cg265
pause 3

"There was no kissing up her leg this time, instead Jezera pushed her foot past the duke and pulled his face forward into her womanhood."
"Rowan could no longer see what was going on, but he could hear the slurping sound of Raeve licking and sucking on his mistress. He could also hear the sounds of pleasure that resulted."
"Suddenly Jezera turned her head and locked eyes with Rowan. There was a moment of surprised and then she smiled at him."

if jezeraIntroSex == True:
    je "Worried that maybe he'll be better than you?"
    "She chuckled between soft moans of pleasure."
    je "Or maybe you're wondering if you'll have a chance at face fucking him after I've finished breaking him in?"

else:
    je "What are you staring at?"
    "She chuckled between soft moans of pleasure."
    je "Were you hoping to have a chance at face fucking him after I've finished breaking him in?"

"The demoness turned her attention back to her prize and laughed again."

je "That might be fun to watch. Actually maybe I should get you two to kiss one another for my enjoyment? Oh! What if I made this toy fall in love with you! Wouldn't that be fun?"

"She shuddered and cried out in orgasm, but also made sure that Raeve didn't stop working at her. Then turned to Rowan again and noted his obvious discomfort."

je "Oh my hero, if this bothers you so much, why are you still watching me? Obviously I don't need your help anymore and I haven't exactly been forcing you to stick around until I give you leave."

"She smiles widely."

je " The only reason you could possibly still be here is if you're enjoying watching me play with my pet."

"Realizing that he'd only be taunted further if he remained, Rowan decided to take his leave. He turned away from his mistress and the former duke of Yael Fork and headed back into the main keep."

label raeveEnd:

show bg17 with fade

"Rowan wandered around the halls for a time, seeing the aftermath of the battle."
"Orc soldiers were rounding up the remaining members of the staff and looting everything they could find. Many stopped to cheer to him as he passed. The celebratory cries twisted the former hero's stomach."
"Yes, he'd played a large part in bringing this fort down. It felt like this was the truest betrayal. This had been a direct attack on the baron's rule, not some gang or bandit attack taking temporary control over a village. This was an act of war."
"He climbed up to the top of the central keep and looked down over the courtyard from the place that Jezera had made her appearance and turned the tide of the battle in an instant."

#battle outcome CG
scene black with fade
show andras happy behind black
show rowan necklace neutral behind black

#if Helyana was not claimed, show the two lines below
if not raeve_keep_rowan_claimed_helayna:
    "Bodies of both attackers and defenders littered the ground everywhere. In one corner a small crowd of orcs were still gathered around the fallen captain."
    "The echoes of carnal screams confirmed that Helayna was still busy sating herself with anyone who was interested in using her."

an "Well, well, well, here you are, servant."

"The man turned to find his master, Andras, coming up the stairs with a broad smile on his face. Helayna's arrow had been removed and a bandage had been placed over the hole. The demon walked over and joined Rowan at the wall, looking down at the scene."

an "What a beautiful sight."

ro "Yes..."

an "I must say that you've really impressed me on this day. Your grasp of strategy and my might took this place far more easily than I thought we would. Lots of prisoners and loot to bring back home after this. The results speak for themselves."
an " I... apologize for arguing against your plan before, that was foolishness."

"That was very surprising coming from the ever arrogant Andras! Rowan looked at his master and found him smiling in-spite of his self admonishment."

#if Rowan did not claim Helayna
if not raeve_keep_rowan_claimed_helayna:
    an "Such a bloody conquest is well deserving of a reward!"

#else
else:
    an "I understand that you've already claimed the former captain as your own. That reward is very well deserved for such a bloody conquest!"

"The hero turned away at that, feelings of shame rushing through him."

an "Rowan, look at me."

show andras angry behind black

"The demon grabbed Rowan's chin and forced him to lock eyes again."

an "Do not dare insult me now. You have earned my favor, I hope that you will endeavor to maintain it."

"Andras kept his grip firm for an uncomfortable moment before finally releasing the man. He then looked back down over the courtyard, giving Rowan a blessed chance to breathe again."

show andras displeased behind black

an "My sister says that she's made the duke into her pet, while my men found the rest of his family hiding out in the cellars. I've appointed one of my officers to oversee this place in our name and we'll send some of the staff back after indoctrinating them."
an "Your task here is complete, and I would call it a job well done. Why not rest for the night here before resuming your scouting tomorrow? All you have to do now is meet the quota."

"The demon casually waved goodbye, then went back down the stairs. Rowan was once again alone with his thoughts, looking down over his success in the demon twin's names."

#End scene.  Show conquest summary.
# Rowan gains Andras's favor for using military strength to conquer Raeve keep.
$ change_favor('andras', 1)
# Rowan gains guilt + corruption + infamy. + several prisoners, + treasury.
$ change_base_stat('g', 10)
$ change_base_stat('c', 2)
$ change_base_stat('f', 2)
$ change_treasury(100)
$ change_prisoners(4)

$ codex_add('doran_keep_taken')
$ codex_add('raeve_keep_is_taken')
$ codex_add('dancer_s_whips')
# Raeve keep is conquered, reducing Rosaria's military strength.
# TODO change Rosaria's military strength
# set goal2_completed (temporary)
$ goal2_completed = True
# activate "dinner_is_served" if Rowan did not claimed Helayna
if not raeve_keep_rowan_claimed_helayna:
    $ activate_event('dinner_is_served')
    $ set_event_timer('dinner_is_served', 'after_raeve_keep_capture', 4)
return

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################


label raeveInfiltrate(tmp_spy):

#intial infiltration (week 18 or earlier)
if week <= 18:
    scene bg16 with fade
    show rowan necklace neutral at midleft with dissolve
    show jezera happy behind bg16

    ro "We're going to send in [tmp_spy.name], [tmp_spy.pers] will try to bring the duke under [tmp_spy.poss] control so that he turns over the keep to us willingly. This will save us men that we can't afford to lose."

    je "Music to my ears. I'll relay your instructions to Shaya and make arrangements for [tmp_spy.name] to travel there. Once the duke has been made compliant, we'll bring in our forces and take possession of the keep."

    "Rowan felt the hairs on his neck stand up straight and what sounded disturbingly like an animalistic growl over his shoulder."

    je "Oh hush, brother. There will be plenty of chances for you to test your armies later."

    #End scene.  Set up spy mission, they should finish in 2-3 weeks.  Raeve keep is marked as explored and can no longer be visited.
    # manually add spy mission to selected spy
    $ tmp_spy.mission = SMRaeveKeepInfiltrate().create_sm(tmp_spy, loc=(world.cur_map.uid, tuple(world.cur_map.pos)), started=week)
    $ msgs.show('{{color=#C6FE56}}New spy mission ({}):\n "{}" at {} (dur. {}){{/color}}'.format(tmp_spy.name, tmp_spy.mission.label,
        ' '.join((str(world.cur_map.uid), str(tuple(world.cur_map.pos)))), tmp_spy.mission.duration))

    return
else:
    #No time for infiltration (date is after week 18)
    scene bg16 with fade
    show rowan necklace neutral at midleft with dissolve
    show jezera neutral behind bg16

    ro "We're going to try infiltrating the keep and bring Raeve under our control with our spies."

    je "As much as I would love to do that, I'm afraid we simply don't have the time for our spy to actually infiltrate and dominate the duke. You'll have to find another way, Rowan."

    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return

####################################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################


# "spy mission report" for infiltrating Raeve Keep
label raeve_keep_infiltrated(tmp_spy):
#Keep has been infiltrated
#Triggers at end of week after spy finishes infiltrating.

scene bg10 with flash
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with dissolve
show andras displeased at edgeright with dissolve

je "It is time, [tmp_spy.name] has reported that our darling Duke Raeve has been brought under [tmp_spy.poss] control.  We will go now to take possession of the keep."

"Rowan looked about the portal chamber, noting the large number of soldiers arrayed for combat."

ro "Are we expecting any trouble with this?"

an "It seems that the captain of the guard is suspicious of our agent, so I am not taking any chances."

"The hero nodded and Andras gave the orders for his forces to march."

scene black with flash

scene bg16 with fade

"When the twins forces got close to the keep, the sounds of battle could be heard coming from inside. At the gate they were met by [tmp_spy.name] who quickly informed them that a split had occurred between the defenders who were loyal to the duke and those loyal to captain Helayna."
"With a huge grin on his face, Andras ordered his forces to take advantage of the situation and attack."

scene bg15 with fade
show andras angry behind bg15

"Helayna's forces had been winning the battle up until now, but they'd been tired out from doing battle with their fellows and had taken casualties. The scattered and weakened defenders were quickly overwhelmed by the savage orcs with the fearsome red demon at their head."
"[tmp_spy.name] was even able to bring some of the knights around to the twins side in the coming battle, if it could even be called a battle."

an "Ahahaha!  Kill them all in my name!  Gha!"

scene cg107 with fade
show helayna angry behind cg107
pause 3

"The only sign of hope for the defenders was in the moment where Helayna emerged from the keep's interior and fired a bow to strike Andras in his stomach before rallying the remaining defenders."

show helayna neutral behind black

hel "Knights to me! For Rosaria, for Raeve!"

#CG variation with blue ribbons added.

"However, this was short lived as Jezera lept up onto the top of the keep walls and used the height advantage to send dancing ribbons of blue energy through the captain's reinforcements, tripping or tossing any she could get her hands on."

#CG of Helayna and knights surrounded by orcs and Rowan.
scene black with fade

"Very soon, only Helayna and a handful of knights remained amongst the forty defenders in the keep's garrison. They'd made it to a secluded part of the keep, safe from Jezera's magic, but completely surrounded by enemies on all sides."
"Orcs jeered at the cornered knights, but none of them made any move to break the standoff."
"Hoping to prevent further bloodshed, Rowan pushed his way past the orcs.  Standing in front of Andras's forces, he addressed their remaining enemies."

show helayna neutral behind black

ro "Helayna, knights, please surrender. The battle is lost, end it before more lives are."

show helayna shocked behind black

hel "Rowan? What are you doing?"

$ codex_add('helayna_keep_taken_by_spies')

if helaynaRelationship == 0:
    show helayna crying behind black
    "Tears welled up in her eyes, then streamed down her face."
    hel "No, no no no, teacher why? Why would you turn on your people, on those that trust you? How could you do this to me?"
    "She fell to her knees, still sobbing uncontrollably. The soldiers around her looked almost equally distraught, many of them visibly agitated or shaking. One dropped his sword, the impact of which sent a ripple through their ranks."
    "Then another blade hit the ground. Cracks had already started to form in their resolve from their captain's breakdown, with each weapon clattering to the ground being another leak in the dam."
    "Finally it broke, and the last of the Raeve knights surrendered."
    scene bg15 with fade
    show jezera happy behind bg15
    show helayna crying at edgeleft with dissolve
    show rowan necklace neutral at midleft with dissolve
    "Rowan rushed forward to help Helayna while the orc soldiers started stripping the defenders of their armor and chaining them as prisoners."
    hel "Why? You're the one person I trust above all others. The one who made me deserving of this post."
    "The former hero helped his student regain her feet with one hand, fingering his amulet with the other."
    ro "They took Alexia, then they imprisoned me. I still wear their chains and they'll kill both of us if I disobey."
    show andras angry at edgeright with moveinright
    "Both of them looked up as Andras approached them, an arrow still protruding from his belly and a look of fury in his eyes."
    an "Kill... that... bitch. That's an order, servant."
    "Before Rowan had a chance to respond, Jezera's voice drifted down from above them."
    je "That will hardly be necessary, brother. Our hero shouldn't have to kill a beloved student just to heal your fragile pride."

elif helaynaRelationship == 1:
    hel "No, it must be a trick. You can't be the real Rowan, the man I knew would never turn on his people. He loved his life!"
    ro "It is me. Even if it wasn't, look around. You're hopelessly outnumbered."
    "Several of the other knights around Helayna fidgeted nervously. They knew their situation was hopeless and evidently at least some of them did think that Rowan was their real hero. This was not lost on their captain."
    show helayna angry behind black
    hel "Stand strong men. Did our hero give up even against impossible odds at Karst?"
    ro "That was different."
    hel "What would you know, false hero?!"
    "Rowan gritted his teeth. Her words bit into him in a way she hadn't intended. The reaction actually caused Helayna's expression to change."
    show helayna shocked behind black
    hel "Huh? Wait, you said that they took your wife... you didn't!"
    "The hero grabbed the amulet on his neck, frustrated at the situation, angry with himself for agreeing to this, and also hopelessness at having no other options. He tried to tear the damn thing from his body."
    "It wouldn't come off."
    show black with flash
    #crackle sfx
    scene bg15 with fade
    show rowan necklace neutral at midleft
    show helayna shocked at edgeleft with dissolve
    hel "Ahhh!"
    "There was a sudden bright flash of light and a red circle of power formed over Helayna's body as she fell to her knees screaming in pain."
    show andras angry behind bg15
    an "Bitch."
    hide andras
    show andras angry at edgeright with moveinright
    "Andras had returned. An arrow still protruded from his side, but that wasn't stopping him from using the full force of his magic to punish the one who'd hurt him. There was a single-minded fury in his eyes."
    "With their captain bowed, the knights broke in an instant. Those that didn't throw down their weapons were overwhelmed by the orcs who charged them."
    an "Servant, kill her."
    "Rowan could respond, Jezera's voice drifted down from above them."
    show jezera happy behind bg15
    je "Now now, brother, do you plan on making our hero kill all of his friends? That's hardly an effective way to endear him to our cause."
    "Andras released the woman from his power and turned his attention upwards."

else:
    show helayna angry behind black
    hel "Is this a trick or a betrayal? Hmph, it makes no difference. Nothing you say will change anything, I will stand against these monsters until my dying breath."
    ro "Look around, you're hopelessly outnumbered.  Please, don't throw your lives away for nothing."
    hel "Be silent, servant of demons!"
    "Her resolve was absolute, however the rest of her forces were not so eager to continue the fight. If the captain fell, her forces would follow. All Rowan needed to do was...."
    show black with flash
    #crackle sfx
    scene bg15 with fade
    show rowan necklace neutral at midleft
    show helayna shocked at edgeleft with dissolve
    hel "Ahhh!"
    "There was a sudden bright flash of light and a red circle of power formed over Helayna's body as she fell to her knees screaming in pain."
    show andras angry behind bg15
    an "Bitch."
    hide andras
    show andras angry at edgeright with moveinright
    "Andras had returned. An arrow still protruded from his side, but that wasn't stopping him from using the full force of his magic to punish the one who'd hurt him. There was a single-minded fury in his eyes."
    "With their captain bowed, the knights broke in an instant. Those that didn't throw down their weapons were overwhelmed by the orcs who charged them."
    an "Servant, kill her."
    "Rowan could respond, Jezera's voice drifted down from above them."
    show jezera happy behind bg15
    je "I think that's enough senseless killing for the day. There will be no more deaths, take everyone who's left prisoner."
    "Andras released the woman from his power and turned his attention upwards."

hide jezera
show jezera neutral at midright with dissolve
"The voice's owner soon arrived on the scene, sliding down the wall on her ribbons of power."

an "You dare come between me and my vengeance, sister?"

je "Tearing her apart limb from limb would only be a temporary distraction. Why don't you take care of our prisoners and start looting our new keep? That's something you'll enjoy that has an actual long term benefit."

show andras displeased at edgeright with dissolve

an "Very well."

hide andras with moveoutright

show helayna angry at edgeleft with dissolve

hel "So now what, am I going to be a prisoner?"

ro "Andras is the jailer. She's as good as dead if we bring her back to Bloodmeen!"

show jezera happy at midright with dissolve

je "No, we're going to let her go."

hel "Just like that?"

je "Well, on one little condition. I can't have you going around telling everyone about how your great hero is now serving demons, after all."

"The blue skinned woman pulled a small obsidian band from a pouch."

je "Just put this on your finger and you're free to go. Otherwise, I'm afraid I'll have to leave you to my brother."

"After staring at the ring for a moment, the knight captain angrily threw off one of her gauntlets and held out her hand. With a flair and a pleasant smile, Jezera placed the band on Helayna's finger. Then stepped back and motioned for Rowan to release their captive."

show helayna aroused at edgeleft with dissolve

hel "What was, oh, hot, hot...."

"Apparently now heedless of her surroundings, the knight started stripping off her armor. Sweat poured off her while she worked at the clasps and hooks, constantly muttering about being too hot."

"Rowan looked away from her, not wanting to know what would happen next."

je "Oh, not interested in playing with her?  It looks like she's positively begging for it. Tell you what hero, since you were the one responsible for delivering a keep to us, I'll keep the others back so you can have first crack at lovely Helayna here."

show jezera neutral at midright with dissolve

je "With that band on her, she's desperate for cocks now, and according to my spies a lot of the knights that turned were quite resentful of their commander, so it's unlikely they'll go easy on her."

show jezera happy at midright with dissolve

je "You aren't going to leave her to those men are you? Some stretching first would do her good. Or... maybe you'd rather watch them go at it for a bit before we pay the duke a visit?"

menu raeve_keep_infiltraded_helayna_menu:
    "Try to protect Helayna" if not raeve_keep_rowan_tried_protect_helayna:
        $ released_fix_rollback()
        ro "No, this is wrong. I won't let anyone touch her."
        je "But look how much she needs it. You can't possibly deny her cocks now, unless you intend to claim her for yourself? My hero, how noble of you!"
        "Her voice dropped and she started whispering in Rowan's ear."
        je "Tell you what, if you fuck her right now I'll keep the others from her and let you keep her as your prize. Assuming she agrees to come along back to Bloodmeen, which I suspect she'll be all too happy to, I'll deliver her to your room to enjoy."
        je "Though, I wonder just how Alexia will react to find that her husband has brought another woman home to his bed? Will you assemble a harem of women from each new conquest? Just to protect them, of course."
        #Note player tried to protect Helayna.
        $ raeve_keep_rowan_tried_protect_helayna = True
        #Re-present choice, but with this option removed.
        jump raeve_keep_infiltraded_helayna_menu

    "Fuck Helayna.":
        $ released_fix_rollback()
        jump fuckHelaynaInfiltrate

    "Watch the knights fuck Helayna.":
        $ released_fix_rollback()
        "Rowan finally turned his gaze back to the woman on the ground, but made no move to approach her. After a moment, Jezera spoke up behind him."
        je "Looks like she's all yours boys. We'll watch round one."
        "With permission given, several of the keep's knights started crowding around Helayna while shedding their armor and anything else that might be in the way."
        #helayna x knights CG 1
        jump knightsHelayna

    "Refuse.":
        $ released_fix_rollback()
        ro "No. I want no part of this."
        show jezera displeased at midright with dissolve
        je "A pity. Well then, we'd best be on our way."
        "The demoness lead Rowan deeper into the keep, leaving the sounds of Helayna and the orc soldiers behind them."
        jump confrontDukeInfiltrate

################################################
label fuckHelaynaInfiltrate:

show helayna naked aroused at edgeleft with dissolve

"Rowan finally turned his gaze back to Helayna. She'd nearly removed all her armor and was using one of her hands to furiously masturbate herself. The franticness of her pace was only stopped for the moments when it took both hands to remove something."
"Once she'd managed to get everything off, her gaze started darting around the courtyard with a desperate gleam. She caught her [helaynaTitle]'s gaze and then dropped to the ground on her backside."

hel "Please... I need... I need...."

# CG of Helayna laying on the ground and presenting herself.
scene cg310 with fade
show jezera happy behind cg310
show rowan necklace neutral behind cg310
show helayna naked aroused behind cg310
pause 3

"Her furious self pleasure ceased and she spread her legs wide as well as her womanly lips with the fingers that had just been knuckling her as fast as possible."
"Hands from behind him started playing over Rowan's body, stroking his shoulders and gripping his cock through his pants."

je "Look how desperately she wants you. What kind of a man wouldn't give her what she needs?"

ro "You made her like this! This isn't who she is."

je "My band did change her priorities a little bit, but her desires turned to you first. That had nothing to do with my influence. She does want you. Deep down, she always has. Take her."

"The demoness pushed her servant forward, towards the woman who was writhing on the ground with a mix of need, pain, and arousal on her face. Somewhat hesitantly, Rowan moved his hands to loosen his garments, freeing his erection from his pants."
"A small part of him was surprised to find that he was actually aroused by this. The part that was now in control thought it the only appropriate answer."

scene cg59 with fade
show jezera happy behind cg59
show rowan necklace neutral behind cg59
show helayna naked aroused behind cg59
pause 1

"Unable to look at her in the eye, he pulled her up to her knees and positioned himself behind her, not bothering to strip off any of his other clothing."
"He pushed into her folds, finding them incredibly hot and slick with arousal. She gasped in shock at the penetration, then let out a sigh of incredible relief."

hel "Rowan, Rowan, my [helaynaTitle], my wonderful hero."

je "Listen to how much she wants you. All this time she's wanted you, but her duties and her honor required that she never act on it. My magic has liberated her from those chains."

hel "Fuck me. Please, please fuck me Rowan!"

"The man started moving his hips, slowly pumping his cock in and out of the knight's needy sex from behind. There were appreciative sounds in response to this, but also a slightly pained mewling. A hand was placed on Rowan's shoulders and he looked up to see Jezera smiling at him."

je "My hero, she asked you to fuck her. This slow, romantic stuff isn't fucking. Go hard, go fast!"

"He did so, roughly pushing into Helayna and roughly groping her body. This instantly caused screams of blissful pleasure and encouragement from the woman in front of him. This served to drive him to be even harder and more abusive, which seemed to make her even happier."
"Rowan really was fucking her with no regard for her well being or pleasure. This was probably her first time; he was claiming her virginity and doing it so crassly! The fact that she seemed to absolutely love it felt wrong, but he only pushed her even more."

scene cg59 with sshake
show cg59 with sshake
show cg60 with flash
show helayna naked aroused behind cg60
pause 2

"While it seemed to go on for an eternity, in truth such a frantic pace brought Rowan to a climax in under a minute of first penetrating the woman. Slightly dazed, he looked down at the woman before him."
"She looked back at him in confusion."

hel "Why did you stop?  I still need you!"

scene cg61 with dissolve
show jezera happy behind cg61
show rowan necklace neutral behind cg61
show helayna naked aroused behind cg61
pause 2

"As if finally realizing what he'd just done, the hero pulled back and staggered away. A trail of his cum followed him, some of it dripping out of his deflating member but also a great deal from the pussy he'd just fucked raw."
"Helayna let out a cry that was a mix of panic and disappointment."

hel "No!  Come back! Fuck me! Oh Goddess, fuck me!"

"Now that he was apparently done with the woman, several of the knights who had betrayed the duke started to crowd around the woman now writhing on the ground, while shedding their armor and whatever else might be in the way."

#Rowan gains corruption
$ change_base_stat('c', 2)
$ codex_add('helayna_keep_taken_by_spies_fucked_by_rowan')

menu:

    "Claim Helayna for yourself.":
        $ released_fix_rollback()
        ro "Stay away, all of you.  I claim this woman as my property, if she will accept me."
        hel "YES! I'm yours! Please take me again, oh Goddess, I've wanted you all my life Rowan!"
        "The eagerness that she said that actually stunned Rowan, making him feel very uncomfortable."
        je "Well, it sounds like she isn't interested in freedom anymore. Very well, this woman now belongs to Rowan, the rest of you can find other girls in the castle to satisfy yourselves."
        scene bg15 with fade
        show rowan necklace sad at midleft with dissolve
        show helayna naked aroused at midright with dissolve
        show jezera happy at edgeright with dissolve
        hel "Oh [helaynaTitle], why do you look so sad? Don't you like me? Please fuck me again, I need you, I want to make you happy!"
        "The demoness moved up to the woman on the ground, who'd started touching herself again as she continued presenting her womanhood to Rowan that his cum was drooling out of. She pressed her hand to the woman's head and a moment later Helaya was unconscious."
        hide helayna with dissolve
        je "She'll be waiting for you in your room when you return to Bloodmeen. For now, we have a meeting with the duke to take care of."
        #If player tried to protect Helayna, reduce corruption slightly.
        if raeve_keep_rowan_tried_protect_helayna:
            $ change_base_stat('c', -2)
        #Helaya is assigned to sharing Rowan's bedroom, forcing Alexia out if she was there. A confrontation event between Rowan and Alexia will trigger at the end of the week.
        $ raeve_keep_rowan_claimed_helayna = True
        $ codex_add('helayna_keep_taken_by_spies_claimed')
        jump confrontDukeInfiltrate

    "Watch the knights fuck Helayna.":
        $ released_fix_rollback()
        jump knightsHelayna

    "Don't watch.":
        $ released_fix_rollback()
        "Not wanting to see what the knights had in store for their former commander, Rowan followed Jezera deeper into the keep."
        jump confrontDukeInfiltrate

################################################################################


label knightsHelayna:

#Hel on knees CG
scene cg119 with fade
show rosarian knight neutral behind cg119
show helayna naked aroused behind cg119

"Rowan looked on as the first of the duke’s former knights strode over to Helayna and placed his hand on her shoulder, pushing her down onto her knees."
"In her current state of mind, she offered very little resistance, and when he pulled his cock free from his undergarments, her eyes lit up with lust. When the man saw the glazed look on her face, he laughed."

rkn "Not so high and mighty now, are you bitch?"

"The female knight either did not hear his insult, or did not care. She was too busy staring at his now semi-erect member. The ring that Jezera had placed on her finger was clearly having a very strong effect on her mind."

rkn "Hungry for cock, commander?"

"The woman gave a meek nod, not taking her eyes from the dick in front of her."

rkn "You’ll have to do better than that."

hel "Please…"

rkn "Please what?"

hel "I need to taste it…"

"The traitorous knight laughed again, the effect the ring’s magic was having on her mind clearly amused him."

rkn "I guess since you asked so nicely, I can oblige you."

"That was all the approval she needed, and the redhead began to tongue his cock hungrily, starting by running it around the head, and then down the shaft in long strokes."
"The knight let out a sigh of contentment as he gazed down at the sight of his former commanding officer now reduced to worshipping his cock."

rkn "Don’t forget the balls, slut."

"Eager to please, Helayna licked his balls as instructed, before working her way back up to the tip of his dick. Taking the head into her mouth, she began to suck on it lightly, making a quiet slurping noise."
"As she did this, she slid a hand south to please herself, rubbing her clit."

rkn "Looks like someone is starting to enjoy herself, boys."

"The lady let out a moan of affirmation and with a grin, the knight placed his hand on her head and used it to guide it his cock deeper into his mouth."
"Despite her lack of experience, she did the best to accommodate him as he started to gently fuck her face, moving his hips back and forth with a groan."
"While he was doing this, other knights had removed their armour and were now standing around the kneeling knight commander with their dicks in their hands, waiting for their turn in her hungry mouth."
"From what Rowan could tell though, she looked so engrossed in her current task that she hadn’t even noticed them."

rkn "Let’s see how you handle all of it."

"With a grunt he forced his cock as far into his mouth and he could, and she surprisingly took most of it, albeit with a gag. As he withdrew it, it glistened in the sun from all the saliva that now covered it."

rkn "Not bad, eh lads?"
rkn "Don’t worry captain, we’ll train you and you’ll be deepthroating dick like a common street whore in no time."

"The Helayna Rowan knew would never have allowed anyone to speak to her in that way, but in her current state of mind, she moaned in arousal at the thought, and returned to sucking the man’s cock as best she could."
"The others had begun to jack off, complaining about having to wait their turn."

rkn "Quit ‘yer whining, if she keeps up like this it won’t be long until you get a turn. And you are going to swallow every drop, aren’t you whore?"

hel "Yesssssss…"

"Helayna fingered away at her pussy as she worked the man’s dick with her other hand and her mouth. Before long it became too much for the man, who came with a loud groan, and true to her word, she swallowed all of his load."
"The knight next to him practically shoved him out of the way to take his place, and as if it were a perfectly normal thing to do, the redhead began to suck his dick too."

scene cg119 with sshake
scene cg119 with sshake
scene cg120 with flash

"Before long she’d satisfied the desires of over a dozen of her former underlings. Rowan could only imagine how much cum she’d swallowed at this point, and just as many knights had chosen to cum on her instead, her face and tits plastered with jizz."

scene bg15 with fade
show jezera happy behind bg15

je "We should go, they’ve got two other holes to try so they are going to be at that for a while. Plus the orcs have to have their turn too, and we still have things to do."

"Rowan could only muster a sad nod, as he followed the blue demoness back into the keep’s interior."

$ codex_add('helayna_keep_taken_by_spies_gangrape')

################################################################################


label confrontDukeInfiltrate:

scene bg17 with fade
show jezera neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

"They passed into the hall, where the two were joined by [tmp_spy.name] and a nervous looking Rosarian knight that had fought against Helayna during the battle. Together they went up the stairs towards the royal bedchambers."

#Show CG of dazed looking Raeve.
scene black with fade
show jezera neutral behind black
show doran shocked behind black
show tempspy_image

"There [tmp_spy.name] took out a key and opened up the room to reveal a somewhat dazed looking duke sitting on his bed."

tempspy "May I present Duke Doran Raeve, slave to my charms and Bloodmeen castle."

je "Well done, [tmp_spy.name]! You may have first pick of the prisoners for your own personal use, I'll be taking him as my own trophy."

"[tmp_spy.name] bowed, then released Raeve from [spy.poss] control and left the room, taking the traitor knight with [spy.poss]."

hide tempspy_image
"The duke blinked and looked around the room in confusion. He jumped slightly and stumbled backwards in fear at the sight of Jezera's nature."

#//CG of Raeve cowering before Jezera.

dor "D-demon, s-stay back! I'm a duke of Rosaria, the baron will make you p-pay for this if you lay a finger on me!"

"It was a very poor showing. Jezera slapped him across the face and he crumpled to the ground once again."

#CG of Raeve holding Jezera's foot.
scene black with fade
show jezera neutral behind black
show doran shocked behind black

"She lifted up a foot, slipping it out of her shoe and pressing it against the side of the duke's face."

je "Kiss it."

"After a moment's hesitation, the duke took her blue foot in both hands and kissed the top of it."

je "Good."

"A swirl of energy started to surround Jezera."

je "Keep going. We'll have to see about fixing that attitude of yours, maybe something else too? It isn't like there's anything worth saving in that useless head."

menu:
    "Continue watching Jezera dominate the duke.":
        $ released_fix_rollback()
        jump dominateDoranInfiltrate

    "Leave Jezera to her business.":
        $ released_fix_rollback()
        "Sensing that his presence was no longer necessary, Rowan turned away from his mistress and the former duke of Yael Fork. He left them and headed back into the main keep."
        jump raeveInfiltrateEnd

################################################################################


label dominateDoranInfiltrate:

"Reave looked at her foot for a moment in confusion, then started kissing the tops of each of her toes. At the same time, the demon woman placed one of her hands on his head and the energies from her surrounded him."

je "What is your name?"

dor "Doran?"

je "No silly man, you don't have a name."

"He blinked several times, opened his mouth to speak, then stopped."

dor "Why don't I have a name? I thought I was a noble."

je "You are a slave. Slaves don't deserve names."

dor "But, I'm not a slave."

je "Really? What kind of a man does what you're doing right now?"

"The duke looked down at the foot still in his hands, hesitated, then kissed it again."

je "That's right. Now, time to move up my leg."

"He laid kiss after kiss up the blue skinned leg. His motions seemed somewhat jerky or robotic, this wasn't something he'd done before. However, this wasn't the reason that Jezera suddenly put her hand on his face."

je "No, stop. You're not touching my pussy with that awful beard. We're shaving that off right now. Where is your razor?"

"After pulling her leg free, she sent the man scurrying off to the side of the room where a desk and mirror rested. He extracted a set of scissors, shaving razor, and cream and showed them to Jezera."

je "Give me that."

#Show CG of Raeve's beard being cut off.

"She took the scissors from Raeve and roughly started cutting his mustache off. There was no protesting or complaining, just dull eyed observation as the man's facial hair fell away."
"After the top had been trimmed short, Jezera moved on to his beard and had that off in short order as well."

#CG of Raeve's beard trimmed short and patchy.

"Only now did the man react. He raised up a hand and patted the patchy short bristles while looking at himself in the mirror. The demon payed no mind, focused on slathering cream over what remained."
"There was some satisfaction that Rowan felt, seeing this man brought down like this, but it also seemed wrong at the same time. He couldn't decide if he was enjoying this or not."

je "Cut it off."

"She stuffed the razor into Raeve's hand. He raised it up slowly to his ear, then stopped. A long moment passed before the demon seemed to run out of patience and put her hand on his head to work her magic again."

je "I said, cut it off."

"Raeve did so.  He shaved off the last vestiges of his mustache and beard one stroke at a time.  At first he would hesitate before starting each cut, but by the end he seemed almost eager to become clean shaven."
"Now finished, he set his razor down on the desk and whipped off the rest of the cream with a towel. The shorn duke received a ruffle of his hair as a reward."

je "Now that's such an improvement! I always hated facial hair. Why don't we pick up where we left off?"

#CG of foot kissing, no beard variant

"She pulled him out of the chair and forced him back onto the ground. After putting both hands on his head, Jezera stopped and seemed to change her mind. After releasing her grip, she instead presented her foot once again."

je "Kiss your mistress' foot again."

"He did so."

je "Say your mistress' name, say Jezera."

dor "Jezera."

je "Good boy.  Who do you love?"

dor "Jezera."

je "That's right. Do you want to make her happy?"

"He nodded vigorously."

je "So eager! Then let's see how well you lick pussy."

scene cg265 with fade
show jezera happy behind cg265
show doran beardless neutral behind cg265
pause 3


"There was no kissing up her leg this time, instead Jezera pushed her foot past the duke and pulled his face forward into her womanhood."
"Rowan could no longer see what was going on, but he could hear the slurping sound of Raeve licking and sucking on his mistress. He could also hear the sounds of pleasure that resulted."
"Suddenly Jezera turned her head and locked eyes with Rowan. There was a moment of surprised and then she smiled at him."

if jezeraIntroSex == True:
    je "Worried that maybe he'll be better than you?"
    "She chuckled between soft moans of pleasure."
    je "Or maybe you're wondering if you'll have a chance at face fucking him after I've finished breaking him in?"

else:
    je "What are you staring at?"
    "She chuckled between soft moans of pleasure."
    je "Were you hoping to have a chance at face fucking him after I've finished breaking him in?"

"The demoness turned her attention back to her prize and laughed again."

je "That might be fun to watch. Actually maybe I should get you two to kiss one another for my enjoyment? Oh! What if I made this toy fall in love with you! Wouldn't that be fun?"

"She shuddered and cried out in orgasm, but also made sure that Raeve didn't stop working at her. Then turned to Rowan again and noted his obvious discomfort."

je "Oh my hero, if this bothers you so much, why are you still watching me? Obviously I don't need your help anymore and I haven't exactly been forcing you to stick around until I give you leave."

"She smiles widely."

je " The only reason you could possibly still be here is if you're enjoying watching me play with my pet."

"Realizing that he'd only be taunted further if he remained, Rowan decided to take his leave. He turned away from his mistress and the former duke of Yael Fork and headed back into the main keep."

################################################################################


label raeveInfiltrateEnd:

show bg17 with fade

"Rowan wandered around the halls for a time, seeing the aftermath of the battle."
"Orc soldiers were rounding up the remaining members of the staff and looting everything they could find. Many stopped to cheer to him as he passed. The celebratory cries twisted the former hero's stomach."
"His role had been fairly minimal in bringing this fort down, but this was different than taking control of a village.  This was a direct attack on the baron's rule.  This was an act of war, an act that had been his plan."
"He climbed up to the top of the central keep and looked down over the courtyard from the place that Jezera had broken the defender's last attack in an instant."

#battle outcome CG
scene black with fade
show jezera happy behind black
show rowan necklace neutral behind black

#if Helyana was not claimed, show the two lines below
if not raeve_keep_rowan_claimed_helayna:
    "Bodies of both attackers and defenders littered the ground everywhere. In one corner a small crowd of knights were still gathered around the fallen captain."
    "The echoes of carnal screams confirmed that Helayna was still busy sating herself with anyone who was interested in using her."

je "Ah, there you are my hero."

"The man turned to find his mistress, Jezera, emerge from the stairs with a mischievous smile on her face. She walked up next to him and surveyed the scene below for a moment before speaking again."

#If Rowan did not claim Helayna
if not raeve_keep_rowan_claimed_helayna:
    je "Hmm, they're still going at it. That girl really had a lot of pent up frustrations she needed to get out. I'm glad she was finally able to embrace her desires."

#else
else:
    je "As promised, no one else has laid a hand on your new woman. That girl really has a lot of pent up frustrations she needs to get out, I hope you'll be able to fully satisfy her desires now that she's embraced them."

ro "Yes...."

je "Today marked the start of something incredible, the first of our major successes from the shadows. I must say that you've impressed me Rowan, given your efforts at court allowing us to field spies in time to take this castle."
#If Rowan did not claim Helayna
if not raeve_keep_rowan_claimed_helayna:
    je "Few would have been able to accomplish that in such a short time, such talent deserves a reward."
    "At this, Rowan turned away from the scene, sick to his stomach at the sight of the death and continued raping below him. However, he was stopped by a hand on his shoulder when he started to walk away."

#else
else:
    je "Helayna is indeed a worthy reward for someone who was able to accomplish all that in such a short time. Few would have been able to do it."
    "At this, Rowan turned away from the scene, sick to his stomach at the sight of death below him. However, he was stopped by a hand on his shoulder when he started to walk away."

"Thin, but surprisingly strong, hands turned him back around and he was surprised to feel wet lips press against his own in a kiss, then felt a sharp pain when Jezera bit his lower lip. She continued to smile mischievously, but there was an edge to her eyes now."

je "Careful, my hero. Remember that fortune can shift fast, it would be best if you don't insult me now, when I'm singing your praises."

"She tapped a finger on Rowan's bleeding lips for emphasis, then stepped back from him and looked back down over the scene of the battle's aftermath."

je "My brother will soon finish up with looting this place and arranging for the prisoners to be brought back. The small entourage that [tmp_spy.name] built will remain behind to hold the castle and reduce suspicions. We should return to Bloodmeen now."

"The demoness started walking back towards the trapdoor. After a moment, Rowan followed her."

#Show spy mission summary.
#Rowan gains Jezera's favor for using spies to capture Raeve keep.
$ change_favor('jezera', 1)
#Rowan gains guilt + corruption + infamy.  + several prisoners, + treasury.
$ change_base_stat('c', 3)
$ change_base_stat('f', 3)
$ change_prisoners(7)
$ change_treasury(50)

$ codex_add('doran_keep_taken')
$ codex_add('raeve_keep_is_taken')
$ codex_add('dancer_s_whips')
#Raeve keep is conquered, reducing Rosaria's military strength.
$ capture_resource(tmp_spy.mission.loc[0], tmp_spy.mission.loc[1])
$ add_spy_exp(tmp_spy.uid, 100)
# TODO change Rosaria's military strength
# set goal2_completed (temporary)
$ goal2_completed = True
# activate "dinner_is_served" if Rowan did not claimed Helayna
if not raeve_keep_rowan_claimed_helayna:
    $ activate_event('dinner_is_served')
    $ set_event_timer('dinner_is_served', 'after_raeve_keep_capture', 4)
#End scene.
return
