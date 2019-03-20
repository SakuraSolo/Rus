init python:

    #Helayna escapes without Rowan's help
    #If Rowan choose not to help Helayna escape, triggers on week 35.
    event('helayna_escapes_without_rowans_help', triggers="week_end", conditions=('week >=35', 'helayna_escape_method == "without rowan"'),
        group='ruler_event', run_count=1, priority=pr_ruler_high)


label helayna_escapes_without_rowans_help:
#Helayna escapes without Rowan's help
#If Rowan choose not to help Helayna escape, triggers on week 35.

$ helayna_escaped = True
$ rowan_shares_room_with_helayna = False

#If Helayna is in Rowan's room.
if rowan_shares_room_with_helayna:
    scene bg9 with fade
    show rowan necklace neutral at midright with moveinright

    ro "Helayna? That's odd...."

    scene black with fade

    "Curious where that woman had gone, Rowan went around the castle looking for her. The staff soon joined in his search, then even the soldiers when one of the twins found out what had happened."
    "They couldn't find any sign of her and apparently no one had seen her either. When the twins learned of what had happened, they sent out an investigation of orcs and Skordred staff and kept Rowan working throughout the day on his normal duties."
    "When it became apparent that they weren't going to find anything, they called the man in for a meeting."

#else
else:
    scene bg10 with fade
    show bg10 with flash
    show rowan necklace neutral at midleft with dissolve
    show andras displeased at midright with dissolve

    #if total favour with andras is over 2
    if all_actors['andras'].total_favors > 2:
        an "Finally. Rowan, we have had a breach of security at the castle. A valued piece of property has gone missing."
    #else
    else:
        an "Finally. Servant, we have had a breach of security at the castle. A valued piece of property has gone missing."

    scene black with fade

    "It turned out that it was actually Helayna he was referring to. They realized she'd vanished the day before and had been searching for her since."

#rejoin
scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera displeased at midright with dissolve
show andras displeased at edgeright with dissolve

je " ...therefore we will be putting you in charge of investigating this matter. Should we have any traitors in the castle they must be dealt with severely."

ro "Understood."

an "As an added incentive, I'll inform you that someone will be made an example of by the time this is all over. It will be your job to make certain it is the one who deserves it."

show andras angry at edgeright with dissolve

$ event_tmp['time to search'] = 12
$ temp = event_tmp['time to search']

an "You have [temp] hours."

scene black with fade

#Rowan investigates how Helayna was able to escape.  Depending on choices and test checks, he may determine that Alexia helped Helayna (if she is not corrupted) and an unnamed member of the staff.  Rowan chooses how to act on this information.

"The hero knew that Helayna wanted to escape, though he'd kept that information to himself. There had been a few things he'd done after her confession a few weeks back to try and dissuade her and make it less likely. Evidently that had failed."

#if rowan did not claim Helayna
if not raeve_keep_rowan_claimed_helayna:
    "The first, and most obvious candidate to have rescued Helayna was the maid who'd brought her recovering mind to Rowan's attention. However, he'd already taken steps to make sure that she did no such thing. That path proved to be a dead end."

#rejoin
"The twins had given him their notes on what they'd managed to figure out. There wasn't much, but he did find a few leads out of there that they hadn't yet followed up on. Plus a hunch or two of his own."
"Rowan intended to get to the bottom of this himself. He hadn't decided yet if the twins would learn of his findings. First he needed to know what had happened."
"There was almost certainly at least one sympathizer for Helayna among the castle staff, the twins had already uncovered evidence of it.  However, perhaps unsurprisingly, they'd had no luck getting anyone to point fingers."
"The next option would be to search for routes out of the castle that Helayna could have taken through the tunnels. The main gates were under constant watch and had already been ruled out as possible routes that Helayna could have taken out of the castle."
"Jezera's portals were completely out of the question.  Unless she'd let Helayna leave, which Rowan highly doubted, there was no way those had been used by her to escape."
"Rowan's last idea would be to search the forests around the castle and see if he could find signs of Helayna there. He'd be the first to try, but he'd also be the best for the job as no one else in the castle was even close to as competent a tracker as him."


$ event_tmp['possible_accomplices'] = ['cook', 'butler', 'manager']
$ event_tmp['accomplice'] = random.choice(('cook', 'butler', 'manager'))
$ event_tmp['suspected as accomplice'] = None
$ event_tmp['can search for accomplice'] = True
$ event_tmp['can question stuff'] = False
$ event_tmp['visits to suspects'] = {'cook': 0, 'butler': 0, 'manager': 0}
$ event_tmp['found accomplice'] = False
$ event_tmp['accomplice search: intimidate bonus'] = 0
$ event_tmp['accomplice search: diplomacy bonus'] = 0

$ event_tmp['can search castle'] = False
$ event_tmp['asked Skordred'] = False
$ event_tmp['skordredSearchPass'] = False
$ event_tmp['castle search bonus'] = 0
$ event_tmp['castle search attempt'] = 0
$ event_tmp['found the armour in the caverns'] = False
$ event_tmp['castle search completed'] = False

$ event_tmp['forest search attempts'] = 0
$ event_tmp['found the potion'] = False
$ event_tmp['magic lore test bonus'] = 0
$ event_tmp['magic lore test attempts'] = 0
$ event_tmp['magic lore test completed'] = False

$ event_tmp['completed event chains'] = 0
$ event_tmp['timer'] = 0
$ event_tmp['time left'] = 0

################################################################################

label investigationMenu:
scene black with fade

if event_tmp['completed event chains'] >= 2:
    jump investigationTwoChains

$ event_tmp['time left'] = event_tmp['time to search'] - event_tmp['timer']

if event_tmp['time left'] <= 0:
    jump investigationFinal


menu:
    "Interview the castle staff for sympathizers." if event_tmp['can search for accomplice']:
        $ renpy.fix_rollback()
        jump investigationSympathizer

    #available after interviewing castle staff
    "Question Suspected Accomplice." if event_tmp['can question stuff']:
        $ renpy.fix_rollback()
        jump investigationQuestionAccomplice

    "Ask Skordred about possible escape routes." if not event_tmp['asked Skordred']:
        $ renpy.fix_rollback()
        jump investigationSkordred

    #available after questioning Skordred
    "Search the caverns." if event_tmp['can search castle']:
        $ renpy.fix_rollback()
        jump investigationSearchCaverns

    #available after fiding the armour in the caverns
    "Question orcs about Helayna's armour." if event_tmp['found the armour in the caverns'] and not event_tmp['castle search completed']:
        $ renpy.fix_rollback()
        jump investigationQuestionOrcs

    "Search the forest for signs of Helayna." if not event_tmp['found the potion']:
        $ renpy.fix_rollback()
        jump investigationSearchForest

    #available after finding the potion
    "Ask Cliohna about potion." if event_tmp['found the potion'] and not event_tmp['magic lore test completed']:
        $ renpy.fix_rollback()
        jump investigationQuestionCliohna

    #available after rowan has completed two event chains
    "Confront the rescuer."  if event_tmp['completed event chains'] >= 2:
        $ renpy.fix_rollback()
        jump investigationConfrontRescuer

################################################################################

label investigationSympathizer:
#randomly determine which of the following was the accomplice - the cook, the butler of the manager
# accomplice is choosen above menu
$ renpy.fix_rollback()

scene bg14 with fade

"The castle staff were the people who interacted with Helayna the most. If anyone knew anything about her or any plans to help her escape, it would be one of them."
"Rowan began interviewing the various members of the staff.  He used the same techniques he'd learned to find out who was stealing food or skirting their duties during the war, while simultaneously trying to avoid being too confrontational or suggestive."
"It was all too common for soldiers to band together against their commanders, especially when it was commoners and nobles. Jezera had certainly inspired a great deal of fear into her worker and many would likely try to defend one another in the hopes of staving off her wrath."

if check_skill(15 - event_tmp['accomplice search: diplomacy bonus'], 'diplomacy')[0]:
    "After some vague assurances and attempts to place blame on others, Rowan believed he now had a credible target."
    #if cook
    if event_tmp['accomplice'] == 'cook':
        "Apparently the cook who'd been serving Helayna her meals had taken pity on her. The man rather liked nobles with particular tastes and coming up with dishes to satisfy them. Naturally this attitude rubbed some people the wrong way."
    #if butler
    elif event_tmp['accomplice'] == 'butler':
        "A manservant who'd previously served as butler to a rich lesser noble was the one he was after. Jezera had recruited him from Rosaria and he was very familiar with Helayna, perhaps even a bit of a fan of her untraditional views."
    #if manager
    else:
        "The manager for the castle staff, and Jezera's second in command, was apparently responsible. Though an unpopular man among the staff, so many of them had pointed fingers at him that it was unlikely a coincidence."
    #Can no longer search for sympathizers, can now question cook / butler / or manager (correct character).
    $ event_tmp['suspected as accomplice'] = event_tmp['accomplice']
    $ event_tmp['can question stuff'] = True
    $ event_tmp['can search for accomplice'] = False
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

elif check_skill(7, 'diplomacy')[0]:
    "After some time, it was becoming apparent that Rowan wasn't making any headway with the staff. Several had tried to send him on the wrong track after people they disliked, and none of the others agreed on anyone being the culprit."
    "He wondered if maybe he should continue interviewing the staff, or follow a different lead?"
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

else:
    # choose wrong suspect
    if event_tmp['accomplice'] in event_tmp['possible_accomplices']:
        $ event_tmp['possible_accomplices'].remove(event_tmp['accomplice'])
    # if list of possible accomplices is exhausted, choose right accomplice finally
    if event_tmp['possible_accomplices'] == []:
        $ event_tmp['suspected as accomplice'] = event_tmp['accomplice']
    else:
        $ event_tmp['suspected as accomplice'] = random.choice(event_tmp['possible_accomplices'])
    $ renpy.fix_rollback()

    "After some vague assurances and attempts to place blame on others, Rowan believed he now had a credible target."
    #if cook
    if event_tmp['suspected as accomplice'] == 'cook':
        "Apparently the cook who'd been serving Helayna her meals had taken pity on her. The man rather liked nobles with particular tastes and coming up with dishes to satisfy them. Naturally this attitude rubbed some people the wrong way."
    #if butler
    elif event_tmp['suspected as accomplice'] == 'butler':
        "A manservant who'd previously served as butler to a rich lesser noble was the one he was after. Jezera had recruited him from Rosaria and he was very familiar with Helayna, perhaps even a bit of a fan of her untraditional views."
    #if manager
    else:
        "The manager for the castle staff, and Jezera's second in command, was apparently responsible. Though an unpopular man among the staff, so many of them had pointed fingers at him that it was unlikely a coincidence."
    #identical to the success one, but with one of the two innocent characters (Cook, butler, and manager) being presented instead at random as being responsible.
    #Can no longer search for sympathizers, can now question cook / butler / or manager (incorrect character).
    $ event_tmp['can question stuff'] = True
    $ event_tmp['can search for accomplice'] = False
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

################################################################################

label investigationQuestionAccomplice:
scene bg14 with fade

#If cook:
if event_tmp['suspected as accomplice'] == 'cook':
    #first visit
    if event_tmp['visits to suspects']['cook'] == 0:
        "Rowan had a talk with the cook who'd been serving meals for Helayna, asking about her tastes and what he'd thought of her."
    #following visits
    else:
        "Rowan had another talk with the cook who'd been serving meals for Helayna, asking about her tastes and what he'd thought of her."
    $ event_tmp['visits to suspects']['cook'] += 1

#If butler:
if event_tmp['suspected as accomplice'] == 'butler':
    #first visit
    if event_tmp['visits to suspects']['butler'] == 0:
        "Rowan had a chat with the butler who was apparently a fan of Helayna. Starting with some innocuous questions before moving onto his political views."
    #following visits
    else:
        "Rowan had another chat with the butler who was apparently a fan of Helayna. Starting with some innocuous questions before moving onto his political views."
    $ event_tmp['visits to suspects']['butler'] += 1

#If manager:
if event_tmp['suspected as accomplice'] == 'manager':
    #first visit
    if event_tmp['visits to suspects']['manager'] == 0:
        "Rowan sat down with Jezera's manager. It was time to find out how deep his loyalties lay with his mistress."
    #following visits
    else:
        "Rowan sat down again with Jezera's manager. It was time to find out how deep his loyalties lay with his mistress."
    $ event_tmp['visits to suspects']['manager'] += 1

"The rumors about her had some truth to them, that was easy enough to learn."

if check_skill(15 - event_tmp['accomplice search: intimidate bonus'], 'intimidate')[0]:
    #If suspect is sympathetic.
    if event_tmp['suspected as accomplice'] == event_tmp['accomplice']:
        "Rowan was somewhat forceful with the man, regrettably, but eventually he was able to get the information he'd wanted."
        #if helayna was not claimed
        if not raeve_keep_rowan_claimed_helayna:
            "Like the maid who'd found Helayna with the orcs, he was sympathetic to her desires to get out of Bloodmeen."
        #rejoin
        "The job he'd had in the escape attempt was to smuggle her down to the lower levels and meet up with someone else who was apparently the real mastermind behind the escape."
        "They'd been co-ordinating with notes and messages, never actually seeing one another in person, so he had no idea who the partner was."
        "The good news was that Rowan now had a time for the escape, so he could cross-check alibis and narrow down the list of suspects considerably."
        #Rowan has now questioned the correct accomplice, this part of the event chain is classed and completed, and is closed.
        $ event_tmp['found accomplice'] = True
        $ event_tmp['completed event chains'] += 1
        $ event_tmp['can question stuff'] = False
        $ event_tmp['can search for accomplice'] = False
        #advance timer
        $ event_tmp['timer'] += 1
        jump investigationMenu

    #if suspect is red herring
    else:
        "By the end of the interrogation, it was clear to Rowan that he'd been mislead. It was very unlikely that this member of the staff was involved in the escape attempt."
        "He'd have to either try again for a new suspect, or a different line of investigating."
        #Reset back to the first step of this event chain, do not repeat the same suspect if check is failed again.  Check is now somewhat easier.
        $ event_tmp['accomplice search: intimidate bonus'] = 0
        $ event_tmp['accomplice search: diplomacy bonus'] += 3
        $ event_tmp['can question stuff'] = False
        $ event_tmp['can search for accomplice'] = True
        $ event_tmp['possible_accomplices'].remove(event_tmp['suspected as accomplice'])
        #advance timer
        $ event_tmp['timer'] += 1
        jump investigationMenu

else:
    "Rowan slowly worked his way through the various tricks he'd learned for getting information out of people.  Unfortunately, this one was proving hard to crack and he called off the talk for a bit to rethink his strategy."
    "After all, he only had so much time and maybe a different investigation would be more successful?"
    $ event_tmp['accomplice search: intimidate bonus'] += 2
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

################################################################################

label investigationSkordred:
scene bg20 with fade
show skordred neutral at skorright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Skordred, the twins are having me follow up on the investigation into our escapee. Could I see your maps of the tunnel network?"

sk " Aye. What're ya lookin far?"

"As he spoke he pulled out several stacks of parchment with detailed maps on them and passed them to Rowan."

ro "I need to know what the possible escape routes were so I can search them."

sk "We already did that. Wha de ye hope to find tha me and my lads couldn't?"

"Rowan was hardly paying attention to the dwarf, focusing on the tunnels and comparing them to where excavation workers had been posted over the last week."

ro "I'm a professional tracker."

show skordred angry at skorright with dissolve

sk "Are ye insulting me?"

"He stopped looking at the maps for a moment and turned to face the dwarf, then considered his words."

#show hour many hours remain as the variable in the following lines (timeLeft)
$ temp = event_tmp['time left']
ro "Time is of the essence, the twins wish me to find Helayna in the next [temp] hours. I'm doing what I can and if you have any information you can give me to help, it would be appreciated."

if society_type == "might":
    show skordred neutral at skorright with dissolve
    "Already Skordred's expression was softening. He still looked a bit defensive, but Rowan felt like he was being given a chance to make up for lost ground. Probably because the dwarf still felt grateful for the man backing him up a few weeks ago."
    sk "Fine."
    ro "Good. How did you coordinate your search, who was on it?"
    if check_skill(7, 'diplomacy')[0]:
        jump skordredSearchPass
    else:
        jump skordredSearchFail

else:
    sk "An just why do ya think I should help the old master's killer? Do ya really think I owe ya anything?"
    "Oh, this was going to take awhile. Sometimes dealing with the dwarf was like pulling teeth out."
    if check_skill(15, 'diplomacy')[0]:
        jump skordredSearchPass
    else:
        jump skordredSearchFail

label skordredSearchPass:
"In spite of his initial outburst, Skordred was very forthcoming with what his teams had done and found during the investigation. Rowan already knew most of what he was saying, but he was able to get answers to the questions for what had been missing in the original reports."
"Rowan was in and out of the workshop in almost no time at all thanks to Skordred's help."
#This action is free.  Searching the castle will be easier.
$ event_tmp['castle search bonus'] += 5
$ event_tmp['skordredSearchPass'] = True
"Now he just needed to follow up on that information in the caverns."
$ event_tmp['can search castle'] = True
$ event_tmp['asked Skordred'] = True
jump investigationMenu

label skordredSearchFail:
"Skordred remained on the defensive for the remainder of the time that Rowan was in his workshop. The dwarf didn't make it easy, but Rowan eventually left with the information he needed that had been missing from the original report."
"It took nearly an hour to finally get everything out of him, not a good start on this line of investigation."
#Searching the castle will be slightly harder.
$ event_tmp['castle search bonus'] -= 3
$ event_tmp['skordredSearchPass'] = False
"Now he just needed to follow up on that information in the caverns."
#advance timer
$ event_tmp['timer'] += 1
$ event_tmp['can search castle'] = True
$ event_tmp['asked Skordred'] = True
jump investigationMenu

################################################################################

label investigationSearchCaverns:

#show cavern bg
scene black with fade

"Rowan began his sweep of the caverns, specifically searching in the tunnels that were far from where Skordred's teams were working and the inhabited tunnels."
"It was very unlikely that Helayna had escaped through routes that were well travelled, so it made the most sense to follow passages that had few people as possible going through them."
"The previous search had been much more exhaustive, but those hadn't been people with the same skill set as Rowan, nor had they been well coordinated. Orc soldiers and maids made poor searchers."
"While competent and dedicated, Skordred couldn't have personally searched everything.  Nor had he specifically followed the route that Rowan was now passing through."

if event_tmp['skordredSearchPass'] == True:
    "The dwarf had briefed Rowan on the areas he'd personally lead the search and the man was confident enough that he could leave those areas be for the moment."

else:
    pass

#if repeat visit
if event_tmp['castle search attempt'] > 0:
    "Rowan was becoming more and more familiar with these tunnels as his search continued. It didn't make him feel much better about the time that was being burned away as he went down yet another passage, looking for any signs of Helayna."

#rejoin
#Roll search check, DC18.  Add +5 if diplomacy check was successful and +2 for each previous search.
if check_skill(18 - event_tmp['castle search bonus'], 'search')[0]:
#success
    scene black with fade
    show rowan necklace neutral at midleft with moveinright
    "This was the end of the line. Yet another of the possible escape routes was cleared and no signs of anyone using it for part of an escape."
    show rowan necklace shock at center with moveinleft
    "However, as he turned around he saw something."
    show rowan necklace happy at center with dissolve
    ro "(Hello, what's this doing here?)"
    "There was a maid's dress laying on the floor next to an opened wooden crate. This certainly looked promising!"
    scene black with fade
    "Several minutes later, Rowan had made a full sweep of the room.  Unless there was someone else with that shade of light-red hair, Helayna had definitely been here. If he wasn't mistaken, a knight's armour had also been in the crate before the escape happened."
    "Suits of Rosarian Knight armour were custom fitted to their wearers. You'd be hard pressed to fit in one that wasn't yours, but all the signs in the area seemed to suggest that Helayna had put on the full suit.  That could only mean it had been her armour."
    "The most likely people to have had Helayna's armour would either be the twins or some trophy collecting orcs. It seemed unlikely that someone would have managed to smuggle a suit of armour out of one of the twin's chambers, so the orc barracks made the most sense to start with."
    #Can no longer search for escape routes, can now question orcs about armour.
    $ event_tmp['can search castle'] = False
    $ event_tmp['found the armour in the caverns'] = True
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

#fail
else:
    "Nearly an hour passed while he stalked through the tunnels, picking each path based on what Rowan thought was most likely to least. He was reasonably sure he hadn't missed anything on those routes, but he still hadn't found anything useful."
    "The clock was ticking, should he keep searching the tunnels or move onto another line of investigation?"
    #Increase counter for number of failed searches in the tunnels.
    $ event_tmp['castle search attempt'] += 1
    $ event_tmp['castle search bonus'] += 2
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

################################################################################

label investigationQuestionOrcs:
scene bg11 with fade

"It didn't take that long for Rowan to find out that the orcs had indeed kept several suits of armour from Reave Keep when the assault had happened."
"Some of the pieces had been salvaged to use for equipment, others had been used as improvised armour plating. A mish mash of pieces had also been put up on one of the walls as a trophy of the battle."
"This was Rowan's first clue as to what he was looking for, as the helmet and greaves were now missing from that display and the last any of the orcs had seen them was around when Helayna escaped."
"If the helm and greaves was from her suit, then obviously someone had taken them down to reassemble her suit. With that knowledge, he now had a lead that he followed through the soldiers until he had what he needed."

show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

"One of the orc soldiers, a male, was the one who'd gone through the trouble of getting several parts of Helayna's armour and delivering them to the crate he'd discovered in the tunnels."

ro "So, why exactly were you doing that?"

os "Humi woman paid me to."

ro "A human woman paid you?"

os "Ya."

ro "Can you tell me anything about her?"

"The orc just shrugged."

os "Was ona de humis dat come down here to clean and bring food. Sometimes dey ask for dings like dis. Was noting odd, dough bosses may be mad I took rose armor off wall. Don't tell dem I did dat, still need to find new ones."

ro "Did you see her any other time? Anywhere else?"

os "Hmmm. Wanted to get anoder girl to put on armor. Make sure it was de right one. Dat it."

"He shrugged again."

os "Never see girl any odder time."

"Rowan heaved a sigh.  He didn't doubt the orc's word, which unfortunately meant this was a dead end.  The orc had no idea why the woman he'd helped wanted the armor, nor did he care."
"Well, at least he knew that a woman was involved. Apparently someone from the regular cleaning staff too, though that wouldn't be too hard to get a disguise for if you had free reign of the castle."
#This choice can no longer be chosen, and Rowan has completed this part of the event chain.
$ event_tmp['castle search completed'] = True
$ event_tmp['completed event chains'] += 1
#advance timer
$ event_tmp['timer'] += 1
jump investigationMenu

################################################################################

label investigationSearchForest:

#first time
if event_tmp['forest search attempts'] == 0:
    #castle gate background
    scene black with fade

    "While the interior of the castle had been quite thoroughly searched, the exterior had not.  Quite frankly, no one in the castle had the right skills or expertise to track someone, except for Rowan."
    "So he doubted that they would have gotten far without his help anyway. Especially since they might not have even covered the right ground either. There really was only one route that Helayna could have taken after emerging from the tunnels; into the forest."

    show rowan necklace neutral at midleft with moveinright

    ro "Jezera, I'm leaving the castle as part of my investigation."

    show jezera neutral behind black
    je "Understood. Good luck out there, my hero."

    hide rowan with moveoutleft

#repeat attempts
#jump straight to below

#rejoin
scene bg3 with fade

#survival skill test is easier for each previous failed attempt.

#survival test DC 15
if check_skill(15 - event_tmp['forest search attempts'] * 2, 'survival')[0]:
#success
    show rowan necklace neutral at midleft with dissolve
    ro "(There.)"
    "He'd been following a likely trail for several minutes now and thus far hadn't been able to confirm if it was Helayna or not. Someone had struggled through a bush here and he was hoping to find out a little more information."
    ro "(Nothing... nothing... hmm?)"
    "He pulled up a long strand of hair and held it up to the light."
    ro "(That looks like the right colour.)"
    "He pawed through the bush a little more, finding another strand.  It was the same shade of light red, almost certainly Helayna's. So he was following the right trail, though he'd never catch up to her at this point."
    "Instead, he tried to follow the trail back to the castle and see how she'd come out, but the terrain quickly turned too rocky to find tracks. That was a dead end. However, just before he came out of the forest he found a discarded glass vial containing a deep red liquid."
    "It wasn't blood, but his nose tingled when he gave it a sniff. Magic maybe? If this was a potion, he'd better ask Cliohna about it."
    #Can no longer search the forest, can now ask Cliohna about potion.
    $ event_tmp['found the potion'] = True
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

#fail
else:
    "Rowan wasn't getting anywhere out here in the woods. That was becoming painfully apparent."
    "The man was a very experienced and skilled tracker, but that didn't help him if he just happened to not be in the right place or found the wrong tracks."
    "Hunters from the castle occasionally came here to try their hands at getting game, so there were many trails and false paths that he constantly found, followed, and eventually discarded."
    "Looking at the sun, he guessed that he'd been in the forest for about an hour now and wondered if maybe he should keep at it or try and follow a different lead."
    #Increase count of attempted forest searches.
    $ event_tmp['forest search attempts'] += 1
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

################################################################################

label investigationQuestionCliohna:

#first time
if event_tmp['magic lore test attempts'] == 0:
    scene bg12 with fade
    show rowan necklace neutral at midleft with dissolve
    show cliohna neutral at cliohnaright with dissolve

    ro "Ah Cliohna, I found a potion that I'd like to identify."

    "She waved her hand somewhat dismissively at him."

    cl "As long as you don't break anything, you may use my equipment to do so."

    show rowan necklace shock at midleft with dissolve

    ro "Actually, I was hoping you could help me with that."

    #If Rowan has high enough relationship with Cliohna
    if all_actors['cliohna'].relation > 5:
        cl "My apologies Rowan, but I am currently preoccupied with something that requires my personal attention. However, you may borrow one of my assistants for the moment. She will explain how to use them."
        scene bg12 with fade
        "Rowan found his way over to the equipment that Cliohna was talking about. Her assistant, a dark elf woman, explained to him how to operate the equipment and where he could find books on common potions and how to test for them."
        "He thanked her for her help and set to work as best he could."
        #Magic lore test is easier.
        $ event_tmp['magic lore test bonus'] += 3

    #else
    else:
        cl "No. I am currently preoccupied with something that requires my personal attention and my agreement with your masters is that I am not disturbed while so engrossed. Figure it out yourself, this is your problem to solve."
        scene bg12 with fade
        "Rowan found his way over to the equipment that Cliohna was talking about. After looking at the unfamiliar apparatuses for a moment, he remembered that he was in a library. Surely there was a book or two somewhere around here that could help him?"
        "He set to work, both looking through the library for anything that could help him and for what could possibly be in the potion."

#repeat visits
else:
    "Rowan set to work at the apparatuses again, hoping to find out what that potion was that he found in the forest."
    scene bg12 with fade
    #Each repeat attempt raises the chance of success.
    $ event_tmp['magic lore test bonus'] += 1

#rejoin
show rowan necklace neutral behind bg12
#intelligence test DC 10

if check_stat(10 - event_tmp['magic lore test bonus'], 'intelligence')[0]:
#success
    ro "(That's it, right?)"
    "He checked, then double checked."
    ro "Yes!"
    show rowan necklace happy behind bg12
    "So much was his relief at finally solving this problem that he actually shouted out loud. One of the library assistants gave him an annoyed look from down the aisle, but he hardly cared."
    ro "Sorry, sorry."
    "Still grinning, he quickly scribbled down the name and type of the potion, then turned off the apparatuses."
    "It had been a fairly common energy potion, the kind that some nobles used to focus when working late. He'd even used it himself a few times during the war, hunting at night and commanding during the day took its toll."
    scene bg19 with fade
    show rowan necklace neutral at midleft
    show clamin neutral at midright
    ro "So this is the full list?"
    cla "That's right, everyone who's bought any of that potion."
    ro "Thanks a lot."
    cla "Anytime boss."
    "Rowan scanned the list. It was short, not many people had used the drink in the castle. Mostly members of the domestic staff. He'd have to cross check this with what else he'd found to see if it pointed to anyone definitely."
    #Rowan has completed this part of the event chain.
    $ event_tmp['magic lore test completed'] = True
    $ event_tmp['completed event chains'] += 1
    #advance timer
    $ event_tmp['timer'] += 1
    jump investigationMenu

#fail
else:
    ro "(Damn.)"
    "Another negative result, at least he hoped that's what it meant."
    "He looked out the window. From how things looked, nearly an hour had gone by."
    "Testing for different potions was very time consuming, he wondered if maybe it was a better use of his time to follow a different lead?"
    #Increase count of failed attempts.
    $ event_tmp['magic lore test attempts'] += 1
    #advance timer
    $ event_tmp['timer'] = 0
    jump investigationMenu

################################################################################

label investigationTwoChains:
#once two investigation event chains have been completed, jump here when returning to the investigation menu.
scene bg9 with fade
show rowan necklace neutral at midleft with dissolve

#Learned escape time and that a women did it.
if event_tmp['found accomplice'] and event_tmp['castle search completed']:
    "Rowan looked at the schedules and list of duties, cross checking all the women on the staff that had access to the orc barracks. Then when he came up with no one, all the women that could have gone down there."
    show rowan necklace shock at midleft with dissolve
    ro "No, it can't be."
    "He checked everything again."
    show rowan necklace neutral at midleft with dissolve
    "There was only one woman in the castle who had access to the orc barracks who had also was unaccounted for at the time of escape."

#Learned escape time and that the escaper was getting an energy potion.
if event_tmp['found accomplice'] and event_tmp['magic lore test completed']:
    "Rowan checked over the departure time, comparing the people on the list who'd got the potion to their alibis. Hopefully that would tell him which had gotten a potion for Helayna."
    "He frowned, this couldn't be right. Her name being on the list had seemed innocuous enough, but she was the only one who wasn't accounted for at the time of escape."

#Learned accomplice was a woman and was getting an energy potion.
if event_tmp['castle search completed'] and event_tmp['magic lore test completed']:
    "First things first, Rowan started crossing off the names on the potion purchasing list of all the men."
    "He hesitated, already halfway down and looking at the full list over again.  All of the people on this list were men."
    "All except one."
    show rowan necklace shock at midleft with dissolve
    ro "No, it could't be."
    show rowan necklace neutral at midleft with dissolve
    "Well, if it was true, he had to go and confront her."

#rejoin
#~ jump investigationMenu
jump investigationConfrontRescuer

################################################################################

label investigationConfrontRescuer:
scene bg9 with fade
#no music
show rowan necklace neutral at midleft with dissolve

ro "I know what you did."

wom "Know what?"

ro "That you are the one who rescued Helayna."

wom "Oh. I... hoped you wouldn't figure that out."

show rowan necklace sad at midleft with dissolve

ro "You aren't even going to deny it? Just admitting it right away?"

"There was no response."

ro "At least tell me why you did this?"

"At long last he turned around."

show alexia 2 necklace look away at midright with dissolve

ro "Why Alexia?"

#Sad music starts playing.

"For a long moment she didn't say anything."

show alexia 2 necklace neutral at midright with dissolve

"Finally she met his gaze evenly, and spoke."
al "She wanted to leave, she hated what had been forced on her. But you didn't give that to her. So I did what I could in your place."

#if helayna was claimed
if raeve_keep_rowan_claimed_helayna:
    ro "It was too dangerous, how could she survive out in the wastes?"
    al "She's a knight! Trained by you! Are you so blind to your lusts for her that you couldn't even see that?"
    ro "Who better than me would know in what state she was, and whether or not she could make that journey?"
    al "And deny her wish to be free?"
    ro "Alexia, I can tell you're not telling me everything."
    show alexia 2 necklace look away at midright with dissolve
    show rowan necklace angry at midleft with dissolve
    ro "What's the other reason you did this?"
    show alexia 2 necklace angry at midright with dissolve
    al "Because of what you were becoming. Rowan, have you seen what's happening to you since you brought her back here? I know what you said. I know we're in a terrible situation. But the two of you were destroying one another"
    show rowan necklace neutral at midleft with dissolve
    "Her accusatory look caught Rowan off guard and he looked away from Alexia. The guilt at having abandoned Helayna came back and gnawed at him for several seconds. Then his thoughts turned to other acts he'd been forced to do in the twin's service."
    ro "I don't have a choice. Helayna wasn't the first person I've had to abandon since I became the twin's agent."
    show village elder wounded at edgeleft with dissolve
    hide village elder with dissolve
    show rowan necklace sad at midleft with dissolve
    "An image of one of the first to fall in his campaign for the twins flashed through his mind, reminding him once again of exactly what he was being forced to do."
    show alexia 2 necklace concerned at midright with dissolve
    "She put her hands over her heart and took a deep breath."
    al "The man I love was becoming something else in the arms of Jezera's curse. It was right in front of me, I had to do something."

#else
else:
    ro "I can't believe you took this risk. Not only were you almost certainly going to get caught, you sent a woman, who could barely keep herself focused for several minutes at a time, out into one of the most dangerous parts of the world."
    show alexia 2 necklace angry at midright with dissolve
    al "And what gives you the right to dictate what she should or shouldn't do? Honestly Rowan, this isn't like you. I couldn't believe it at first when she told me you'd refused to help her escape."
    "Her accusatory look caught Rowan off guard and he looked away from Alexia. The guilt at having abandoned Helayna came back and gnawed at him for several seconds. Then his thoughts turned to other acts he'd been forced to do in the twin's service."
    ro "I don't have a choice. Helayna wasn't the first person I've had to abandon since I became the twin's agent."
    show village elder wounded at edgeleft with dissolve
    hide village elder with dissolve
    show rowan necklace sad at midleft with dissolve
    "An image of one of the first to fall in his campaign for the twins flashed through his mind, reminding him once again of exactly what he was being forced to do."
    show alexia 2 necklace concerned at midright with dissolve
    al "I know I don't really understand what you're going through, but Helayna was suffering right in front of me. I had to do something."

#rejoin
"The woman let out a long shudder, then slumped.  Her anger burnt out and all of a sudden she looked half her usual size, looking like a little girl again. Rowan had an urge to reach out and comfort his wife."

menu:
    "Comfort Alexia.":
        $ renpy.fix_rollback()
        "Rowan stepped forward and wrapped his arms around his wife's shoulders, rocking back and forth as her tears streamed down her face."
        al "Darling..."

    "Don't touch her.":
        $ renpy.fix_rollback()
        "He resisted the urge to touch her, and stood back. After a moment, Alexia wiped away her tears and looked back up at him."
        #Rowan loses a little influence with Alexia.
        $ change_relation('alexia', -2)

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

al "What happens now?"

#show hour many hours remain as the variable in the following lines (timeLeft)
$ temp = event_tmp['time left']
ro "Now I have to give my report to the twins. They told me that I need to figure out who did it in [temp] hours so they can make an example of the traitor. Even if I didn't come up with the right person, Andras is going to punish someone anyway."
ro "You've put me in an awkward spot here, I could try blaming one of your accomplices or take the blame myself. I don't think I could tell them the truth..."
"he placed a hand on his arm and looked him in the eyes with a resigned expression."
al "Do what you have to do."
jump investigationFinal

################################################################################

label investigationFinal:

scene bg6 with fade
show jezera neutral at midright with dissolve
show andras displeased at edgeright with dissolve
show rowan necklace neutral at midleft with moveinleft

je "So, my hero, what have you learned?"

an "Yes, I am most eager to learn who was responsible for this... loss."

#Choices vary based on what Rowan has learned.

menu:
    #Requires that Rowan complete the staff line and learn the escape time.
    "Blame the accomplice." if event_tmp['found accomplice']:
        $ renpy.fix_rollback()
        jump investigationBlameAccomplice

    #Requires that Rowan complete the tunnel line and learn that a woman lead the escape.
    "Blame the orc soldier." if event_tmp['castle search completed']:
        $ renpy.fix_rollback()
        jump investigationBlameOrc

    #always available
    "Take the blame yourself.":
        $ renpy.fix_rollback()
        jump investigationBlameSelf

    #Only available if investigation was completely finished.
    "Tell them it was Alexia." if event_tmp['completed event chains'] >= 2:
        $ renpy.fix_rollback()
        jump investigationBlameAlexia

    #always available
    "Tell them you couldn't figure out who it was.":
        $ renpy.fix_rollback()
        jump investigationBlameNobody

################################################################################

label investigationBlameAccomplice:

#insert the correct staff member as variable
$ temp = event_tmp['accomplice']
ro "It was a [temp] on the staff. He took a shining to Helayna and got her out of the castle."

#if rowan knows Alexia was responsible, perform a decieve check DC15, if he fails jump to investigationCaughtLie, else continue below
if event_tmp['completed event chains'] >= 2:
    if check_skill(15, 'deceive')[0]:
        show andras angry at edgeright with dissolve

        an "Hmmhmmhmm, well sister, might I have some of your staff?"

        show jezera happy at midright with dissolve

        je "Absolutely brother, be my guest. Feel free to take that man's whole team. I'm sure I can find replacements."

        show rowan necklace shock at midleft with dissolve

        ro "Wait, it was only-"

        je "Hush my hero. Your job is done now. It is my brother's turn to act."

        an "Well said, sister."

        hide andras with moveoutright

        je "You'll get to take care of cleanup after he's done. Ta."

        hide jezera with moveoutright

        #Castle maintenance costs are increased for the next four weeks.
        # TODO: increase costs
        #Rowan gains a little guilt
        $ change_base_stat('g', 2)
        return
    else:
        jump investigationCaughtLie

################################################################################

label investigationBlameOrc:

ro "It was one of the orc soldiers, they got tricked into getting everything that she needed to escape into the Rakshan Wastes."

#if rowan knows Alexia was responsible, perform a decieve check DC15, if he fails jump to investigationCaughtLie, else continue below
if event_tmp['completed event chains'] >= 2:
    if check_skill(15, 'deceive')[0]:
        show andras angry at edgeright with dissolve

        an "Ohhh, this day you don't get to stop my punishment. Those orcs will know what happens when they turn against me, let them feel my wrath!"

        show rowan necklace shock at midleft with dissolve

        ro "Wait, it was only-"

        an "Silence! I said you will not be stopping me today. Today, there will be blood."

        hide andras with moveoutright

        ro "How many is he going to kill?"

        je "As many as it takes. Thank you for your help in this, ta."

        hide jezera with moveoutright

        #Lose five soldiers and 10% of morale.
        $ castle.buildings['barracks'].troops -= 5
        $ castle.morale = int(castle.morale * 0.9)
        #Rowan gains a little guilt.
        $ change_base_stat('g', 2)
        return
    else:
        jump investigationCaughtLie

################################################################################

label investigationBlameSelf:

ro "I did it."

show andras angry at edgeright with dissolve

an "Oh?  Then it was a mistake to-"

je "Stop."

je "I will not tolerate you covering for someone like this, Rowan. You're too valuable to make an example of. Now, tell me what you actually found out."

"Rowan spent several minutes explaining each of the clues he'd found during his search, but presenting himself as the mastermind behind each."

je " And you just went through all that just to confess at the end? Somehow I doubt you're being honest here."

an "Sister, dear sister, I don't think we will be getting much more out of this man. Let me teach him what it means to fail, then maybe he won't be so quick to defend others next time."

je "Fine brother, do what you will. Just make sure he's still useful afterwards."

hide jezera with moveoutright

an "Come along, I'll get your old accommodations ready again. What do you say to that being your sleeping quarters for a month? I think this time I'll be the one to administer the beatings."

#Rowan gains an irreversable injury for the next four weeks that reduces his movement points by 25% and applies a health penalty.
# TODO:

$ escapeBlameSelf = True
return

################################################################################

label investigationBlameAlexia:

$ rowanBlameAlexia = True
jump blameAlexiaOutcome

################################################################################

label investigationBlameNobody:

ro "I couldn't figure out who was behind it all."

#if rowan knows Alexia was responsible, perform a decieve check DC15, if he fails jump to investigationCaughtLie, else continue below
if event_tmp['completed event chains'] >= 2:
    if check_skill(15, 'deceive')[0]:

        an "Useless. Then I'll just have to decide on someone else to take the fall."

        show andras angry at edgeright with dissolve

        #Randomly choose either the staff, the orcs, or Rowan.
        $ temp = dice(3)

        if temp == 1:
        #staff
            an "Sister, your staff have been complacent for far too long. Some of them will be taking the blame for this."
            je "Very well, do with them as you will."
            hide andras with moveoutright
            je "The two of us will just have to pick up the pieces after he's done."
            hide jezera with moveoutright
            #Castle maintenance costs are increased for the next four weeks.
            # TODO: increase costs
            #Rowan gains a little guilt
            $ change_base_stat('g', 2)
            return
        elif temp == 2:
            #orcs
            an "I haven't been able to cull the weak in so long... now I at least can get some satisfaction."
            an "Some orc heads are going to roll."
            hide andras with moveoutright
            je "Hopefully you can piece an army back together when he's done."
            hide jezera with moveoutright
            #Lose five soldiers and 10% of morale.
            $ castle.buildings['barracks'].troops -= 5
            $ castle.morale = int(castle.morale * 0.9)
            #Rowan gains a little guilt.
            $ change_base_stat('g', 2)
            return

        #rowan
        else:
            an "Actually... this really was your failure Rowan."
            ro "Mine?"
            an "Yes, you're the {i}expert{/i} in these matters, yet here you stand a failure. You're the one who's going to suffer my punishment."
            je " Be my guest, but be sure he can still work afterwards. Rowan remains our best asset."
            an "Good. Now boy, let's get you settled back into my dungeon. I think I want a personal hand in your beatings this time."
            #Rowan gains an irreversable injury for the next four weeks that reduces his movement points by 25% and applies a health penalty.
            $ add_effect(MultiEffect('Sore muscles', 'neg', (('mp', -3),), 4))
            $ take_damage(-2)
            # TODO:
            return
    else:
        jump investigationCaughtLie

################################################################################

label investigationCaughtLie:

show andras angry at edgeright with dissolve

an "Hmph, then I've got someone I need to collect for our demonstration."

hide andras with moveoutright

show jezera happy at midright with dissolve

je "Clever, clever. Now, this is why I was right to choose you to be our agent. It's just a shame you aren't a better liar."

"Rowan clenched his jaw, not saying anything for the moment."

je "My brother will be so cross when I tell him about this and he'll probably throw you in the dungeon. Keep at it though, my hero. Someday maybe you'll be able to fool me. In the meantime, I'll make sure you survive well enough to carry on our work."

#Rowan gains an irreversable injury for the next four weeks that reduces his movement points by 25% and applies a health penalty.
# TODO: reduce % of MP, health penalty
$ add_effect(MultiEffect('Sore muscles', 'neg', (('mp', -3),), 4))
$ take_damage(-2)
#Gain a favor with Jezera, lose one with Andras.
$ change_favor('andras', -1)
$ change_favor('jezera', 1)
return

