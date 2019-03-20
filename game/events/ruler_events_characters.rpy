# TODO: maybe
init python:

    # Dark Sanctum Event - Triggers at week end when building is purchased
    event('dark_sanctum_purchased', triggers="week_end", conditions=('week >=4', '"sanctum" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Forge Event - Triggers at week end when building is purchased
    event('forge_purchased', triggers="week_end", conditions=('week >=4', '"forge" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Intro to Indarah and tavern explanation
    #occurs week tavern is built (when purchased actually)
    event('tavern_purchased', triggers="week_end", conditions=('week >=4', '"tavern" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Andras opens the arena
    # Event triggered when the arena is built
    event('andras_opens_arena', triggers="week_end", conditions=('week >= 4', '"arena" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    ##### Breeding pit build scene #####
    #Event triggers when breeding pit is built.
    event('breeding_pit_build_scene', triggers="week_end", conditions=('week >= 4', '"pit" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)
    # Intro to Shaya and brothel tutorial
    # Triggers the week the brothel is built
    event('brothel_purchased', triggers="week_end", conditions=('week >= 4', '"brothel" in castle.scheduled_upgrades'), group='bld_intro', run_count=1, priority=pr_bld_intro)


label dark_sanctum_purchased:
#Dark Sanctum Event - Triggers at week end when building is purchased

#castle corridor BG
scene castle hallway with fade
show rowan necklace neutral at edgeleft with dissolve
show jezera neutral at midleft with moveinright

je "Ah, here you are Rowan. Punctual riser as usual. Since Skordred has now finished construction of the dark sanctum, we are now prepared to maintain a force of incubus and succubus sorcerers."

show xzaratl neutral at cliohnaright with moveinright

je "I've bought X'zaratl in to manage that force. She has agreed to take up residence here and serve me and my brother as head sorcerer."

je "Rowan, X'zaratl.  X'zaratl, Rowan. He is our figurehead, managing our finances as well as this castle's main link to the world."

xz "Oh my, what a handsome young man you are! Jezzy, why didn't you tell me you had such a fine specimen working for you?"

menu:
    "A pleasure to meet you.":
        $ renpy.block_rollback()
        show rowan necklace happy at edgeleft with dissolve
        ro "It is a pleasure to meet you, X'zaratl."
        xz "Likewise. I'm looking forward to working very closely with you, Rowan. I'd love to have a personal, one-on-one meeting with you after I get myself settled."
        xz "In fact, if you happen to have a special someone, I'd like to extend an invitation to both of you to come down to my chambers some time. I assure you, I'm well equipped to handle both men and women."
        # X'zaratl's advances event is high priority and can trigger after 2 weeks have passed.
        $ friendly_to_xzaratl = True
        $ activate_event('xzaratl_s_advances')
        $ set_event_timer('xzaratl_s_advances', 'dark_sanctum_purchased_delay', 2)

    "Watch it succubus, I'm a married man.":
        $ renpy.block_rollback()
        ro "Watch it succubus, I'm a married man."
        xz "Even better! Come down some time with your wife and I'm sure we'll have a wonderful time together. I assure you, I'm well equipped to handle both men and women."
        # X'zaratl's advances event can trigger after 3 weeks pass.
        $ activate_event('xzaratl_s_advances')
        $ set_event_timer('xzaratl_s_advances', 'dark_sanctum_purchased_delay', 3)

hide xzaratl with moveoutright

je "From now on she will be handling recruiting and managing our cubi sorcerers. They will be supporting our forces in battle as well as assisting Cliohna with research."

je "Hope you all get along..."

show jezera happy with dissolve

je "...really well."

$ codex_add('xzarartl_starting')
#end event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label forge_purchased:
#Forge Event - Triggers at week end when building is purchased

scene bg11 with fade
show andras displeased at trueedgeleft with dissolve
show rowan necklace neutral at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

an "This is him. This beast will be our forgemaster from here on."

"The great minotaur simply stood there, accepting the insult without any reaction."

an "Sort out your introductions, servants. Then show him the forge."

hide andras with moveoutleft

"Rowan studied the large bull in silence, while he in turn was also measured. He seemed, old? Maybe resigned or tired? Just before Rowan was about to open his mouth, he was surprised when the minotaur broke the silence first."

gh "Human, you know the pain of fighting even when you don't want to. I can see it in the way you hold yourself."
gh "It is a pain I bear as well."

"The hero nodded. There was an odd kinship that he'd felt between them, he just hadn't quite figured out why until then."

gh "The brat has said that I won't have to fight here as long as I make his weapons and armor. I don't like these bloodthirsty orcs, but maybe you can keep me company some time."
gh "Greyhide is my name, will you do the honor of telling me yours?"

show rowan necklace happy at midleft with dissolve

ro "Rowan is my name, I thank you for the honor of telling me yours."

"The minotaur blinked, seemingly shocked for a moment by the response."

gh "I... I thank you for the honor of telling me yours."

show greyhide neutral at cliohnaright with dissolve

"Something in the bull's stance changed. He seemed to stand up just a little bit straighter, maybe he seemed a little less resigned."

gh "From now on, I shall turn as much of the iron you supply me into equipment for the brat's soldiers as I'm able.  In time, I may forge with other metals as well."

ro "Perhaps we can get a drink together sometime soon and compare scars?"

gh "I’d like that very much."

ro "The twins are working me to the bone at the moment, but we can work something out when I have some free time."

gh "I shall look forward to it."

# follow up ‘Drinking Buddies’ event can trigger when player has tavern (or if player already has tavern, after 3 weeks)
$ activate_event("drinking_buddies")
$ set_event_timer('drinking_buddies', 'after_forge_purchased', 3)
$ set_event_timer('greyhide_s_first_gift', 'after_forge_purchased', dice(5))
$ greyhideMet = True
$ codex_add('greyhide_starting')
#end event
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label tavern_purchased:
# Intro to Indarah and tavern explanation
#occurs week tavern is built

#corridor bg
scene castle hallway with fade
show rowan necklace neutral at midleft with dissolve
show indarah neutral at midright with dissolve

"As Rowan was leaving his quarters and heading down towards the castle kitchens he ran into a dark skinned woman dressed in bright silks. She had a cheerful bounce to her movements, but also had a hard edge to her features."
"She gave a one handed curtsey to the hero before addressing him."

ind "A fine morning to you, hero Rowan. I am Indarah, the one called Jezera instructed me to seek you out and introduce myself."

ro "A fine morning to you as well, woman of the Dragon's Tail."

"As he spoke, he returned her greeting with the customary sweeping bow. As he did so, he noticed that there were some fighting scars on the woman's hands."
"When he returned his gaze to her face, he spotted the barest hint of another scar that she hadn't quite managed to cover up. This girl was a fighter."

ro "So what brings you to Castle Bloodmeen?"

ind "An opportunity I would never get back home, a chance to own a tavern of my own. Your mistress has offered me a property that was recently restored in the Wastes. My experience dealing with pirates, often violently, seemed to have impressed her."

ro "Well, I hope that your service does not prove to be a greater burden than you thought it would be when you agreed to serve Jezera."

"She measured Rowan's words for a moment before responding."

ind "I'm well aware that she is a demoness, as well as what she and her brother seek to do. I don't care what they are if they give me a chance to break free of the chains of my birth."
ro "Very well, Indarah. It was good meeting you, I'll see you around the tavern."

$ set_event_timer('indarah_s_first_gift', 'after_tavern_purchased', dice(5))

$ codex_add('indarah_starting')
#end event
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label andras_opens_arena:
# Andras opens the arena
# Event triggered when the arena is built

scene bg9 with fade
show rowan necklace neutral at edgeleft with dissolve
show alexia necklace neutral at midleft with dissolve
show andras smirk at midright with moveinright

an "In honor of the arena's completion, I would like to personally invite the two of you to see first blood spilled."

show alexia necklace look away at midleft with dissolve

"Alexia shifted uncomfortably and looked away from Andras."

menu:
    # Choice: Try to convince him that Alexia shouldn't have to come"
    "Try to convince him that Alexia shouldn't have to come":
        ro "Thank you for the invitation, but I think that Alexia isn't feeling up to this, so..."

    # Choice: Turn down his invitation"
    "Turn down his invitation":
        ro "I don't think we're all that interested, thank you."

show andras displeased at midright with dissolve
an "I'm sorry, but I must insist that both of you come as my honored guests.  I really won't take no for an answer."

scene bg14 with fade

"Under the demon's fierce gaze, Rowan and Alexia were escorted to the newly completed arena."

# arena bg
scene bg29 with fade
show rowan necklace neutral at edgeleft with dissolve
show alexia 2 necklace concerned at midleft with dissolve
show andras happy at midright with dissolve

"As they approached the entrance to the high seat, the sound of orcish cheering rose louder and louder."
"Rowan and Alexia were directed to sit in the seats surrounding the high seat, which Andras then took."

"He smiled and rubbed his hands in anticipation for a moment, then snapped his fingers causing a thundering crash. Shortly afterwards, several scared men shuffled into the arena followed by a troop of orcs from the other side."
"Alexia gasped in horrible realization at what's about to happen."
"Rowan's breathing stopped for several moments in even deeper horror, as he saw that the men were horribly under equipped compared to the orcs. This wasn't going to be a battle, it was going to be a slaughter."
"Andras only waved his hand, then smiled sadistically as the \"battle\" started."

an "Don't even think about looking away, this show is in the two of you's honor after all. Think of it as a thank you from me for finding the funds for this wonderful place."
an "I assure you that the troops will be much more content with a place like this to cut loose and have fun, especially if you can find me some prisoners for them to play with."

"The rest of his words were drowned out by the incredible noise from the soldiers in the stands as the first drops of blood hit the arena floor."
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label breeding_pit_build_scene:
##### Breeding pit build scene #####
#Event triggers when breeding pit is built.

scene bg14 with fade
show rowan necklace neutral at edgeleft with dissolve
show andras displeased at midleft with moveinright
show draith neutral at cliohnaright with moveinright
show jezera neutral behind bg14

"On his way to the throne room, Rowan found himself face to face with his master holding onto a short violet skinned man dressed in straps and leather pants who was nervously looking around the castle."

an "There you are, servant. I snagged a little dark elf to help us out with the new breeding pit. Found the poor sod wandering around outside their caves, shivering from the cold."

ro "What were you doing there?"

"Rowan addressed the elf, but there was no response. The dark skinned man wouldn't even meet his gaze."

je "Probably running from his mistresses.  Men don't get much in the way of rights in their society."

hide jezera
show jezera happy at edgeright with moveinright
show draith neutral at midright with move

je "What's the matter? I won't bite."

show draith neutral at midleft with move
show andras displeased at midright with move
show jezera neutral at edgeright with dissolve

je "Don't like ladies, hmm? I promise I'd treat you better than my brother will, but suit yourself. Rowan, would you be a dear and give this man a hug?"

ro "Excuse me?"

je "Brother, why have you dressed him like that?"

an "That was how I found him. He begged me to take him away from his home and said he knew how to handle monsters."

je "No wonder he was so cold.  This boytoy didn't have a chance to get any proper clothing for an escape, must have been an opportunity he couldn't pass up or a danger he had to flee. Why are you still standing there hero? Our new breeder needs to knock dicks with someone."

menu:
    "Give the dark elf a hug.":
        $ released_fix_rollback()
        "As instructed, Rowan stepped forward and wrapped his arms around the shorter man. The elf started slightly, but then almost immediately pressed himself into the embrace."
        "He wrapped his arms around the hero in turn, even pressing his waist forward. While Jezera had likely jested when saying their newest servant needed to knock dicks, it seemed that he really did want to do exactly that."

    "Give the dark elf a pat on the back.":
        $ released_fix_rollback()
        "Rowan didn't give the shorter man a full hug, but did clap him on the back and give a reassuring squeeze of the shoulders. That was how he'd always encouraged his male soldiers back during the war."
        "The elf evidently wanted to go a step further, but when the hero pulled back from him he didn't push the matter."

show draith happy at midleft with dissolve

"For the first time, a smile crossed over the dark elf's face and he meet Rowan's gaze for an instant."
"Behind the two of them, the twins continued their discussion. It was rapidly turning into an argument."

dra "Draith. I'm Draith."

ro "Good to meet you Draith, I'm Rowan. So, you're good with monsters?"

show jezera displeased at edgeright with dissolve

dra "Yes! I'm good with them, one of the only guys who managed to not lose a hand to them. If you can give me a place to stay, I'll take care of your monsters."

"He spoke with a mix of excitement and apprehension. The former was likely due to the possibilities of his new life. The later probably had to do with always being afraid of the next beating."

show andras angry at midright with dissolve

ro "Well then, why don't I show you the facilities and you can explain all about handling monsters."

"Talking about things that he liked, or at least was comfortable with, should help overcome that apprehension."

hide rowan with moveoutleft
hide draith with moveoutleft

je "Honestly brother, whatever will I do with you? Yeti hunting? Was that really the best use of your time?"

an "A yeti would have made a fantastic first addition to our pits! Our foes wouldn't know what hit them."

scene black with fade

"They left the two arguing twins behind, heading deeper and deeper into the castle underground."

scene bg25 with fade
show rowan necklace neutral at midleft with dissolve
show draith neutral at midright with dissolve

ro "Here we are."

"The dark elf looked around the cells and facilities for a few moments, then looked at Rowan with a confused expression on his face."

dra "It's empty."

ro "Yeah, well, we just finished building the place. There hasn't been time to actually get any monsters yet."
ro "Speaking of which, would you know what the best way would be to get monsters?"

dra "For small pens like these? Best to use newborns, growth enhanced if we can get the nutrients."

ro "So, stealing eggs or children from nests and bringing them here?"

dra "Exactly. We don't have large enough facilities for anything else, so find any monster nests you can and bring their young back here. I'll take care of the rest, at least I think I'll be able to."

ro "Sounds good. I'll just give you an overview on life here at Bloodmeen, where you can find me, and we'll see about getting you quarters to live in."

$ codex_add('draith_starting')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label brothel_purchased:
# Intro to Shaya and brothel tutorial
# Triggers the week the brothel is built

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with moveinright
show shaya neutral at edgeright with moveinright

"Rowan looked up and saw his mistress enter the throne room, accompanied by an olive skinned women wearing the attire of a dancer. Despite the fact that a veil covered her face, it was obvious that she was of a rare beauty."
"He stood up and bowed to them when they arrived at his desk."

ro "Good morning mistress."

je "A very fine morning to you too, my hero!"

ro "It's good to see you in such high spirits. How can I help you?"

je "Well, first of all I'd like to introduce you to a dear friend of mine, Shaya. We grew up together and I trust her above all others."

"The half demon turned to her companion."

je " I'm sure you've heard of the great hero of Rosaria, Rowan? He joined with Al-Serah and Deanara to defeat our father, but has been... {i}convinced{/i} to support my brother and I. Your budgets and assignments will be coming from him."

"The hero walked forward and extended a hand to the veiled woman."

ro "It is good to meet you Shaya."

"She hesitated, looking down at the man's outstretched hand and back up at his face. Then she abruptly stepped forward and took his hand with both of hers, pulling it up to her chest and pressing it between her breasts."

sha "It brings me great delight to meet a hero of your stature, Rowan. I dearly hope that the two of us shall work very well together."

"Her sudden show of affection felt somewhat off to Rowan and he tried to softly pull his hand away from her. The woman only held on tighter, so the hero decided to change tactics."

ro "So, how will you be helping us here in Bloodmeen?"

"She turned to look at Jezera for a moment."

sha "Jessy, uh, you haven't told me that yet either"

#jez shocked
je "I'm sure I said I was making you my assistant."

sha "Yes, but you didn't say what that meant."

#jez happy
je "Well then, I'll explain while I show you your new base. Rowan, you come along too. I'm eager to show off a bit."

"Finally Shaya let Rowan's hand slide away from her breast, but she kept a firm grip with one hand. This forced the two to follow after Jezera hand-in-hand."


scene bg24 with fade
show jezera happy at midleft with dissolve

je "Well, what do you think?"

"She spread her arms dramatically, still grinning and waited to hear what her followers had to say."

show rowan necklace neutral at midright with moveinright
show shaya neutral at edgeright with moveinright

ro "This is quite extravagant."

sha "Reminds me of home."

"Jezera had evidently spent a lot of effort in decorating the new spy facilities, as well as a lot of funds. Considering what Cliohna had said about cubi spies, it made sense."

je "Today marks a big day for me, as now I can finally say I am a true spymaster. From here, my masters of deception and seduction will infiltrate the Six Realms and wrap their rulers around my finger."

ro "She's really getting into this."

"Rowan and Shaya whispered to one another while Jezera continued her boasting."

sha "She's always been a fan of spies. When we were growing up she just couldn't get enough books about them."

"As she spoke, the woman drew closer to Rowan and wrapped herself around his arm. The hero wasn't sure how to respond to the strangeness of her advances, but he was distracted by Jezera directly addressing the two of them again."

je "That's where you two come in. Shaya, there's no one else I can trust to run this base. You'll be handling supplies and managing our staff. Rowan, it will be your job to find tasks for them to undertake. You'll also need to allocate funds to maximize our possible operations."
je "I'll handle locating spy candidates and transportation, of course. While they don't have other tasks to accomplish in the field, our spies can be used for more general things either in the castle or nearby my portals."

"While the demoness continued to explained the finer points of espionage, she lead her two followers over to one of the booths and they all sat down, Shaya still gripping Rowan's hand."

je "Now, keep in mind that my sublime shadow stalkers will take time to complete their tasks. While brother's armies can conquer villages and towns faster, it will cost you more than if my spies do the task."

"Rowan briefly looked down to see that Shaya had placed a hand on the inside of his thigh! His eyes shot over to the woman and saw that she was still paying close attention to her friend, who was in turn plowing along as if there was nothing out of the ordinary going on in front of her."

je "Also, there are some things that only my spies can do, such as infiltrating the capitals of the Six Realms to gather intelligence, and, although it pains me to admit, they cannot do everything. We'll still need to use force to take some territory or complete some tasks."

sha "It'll be nice to be together more and you keep very lovely company here, Jessy. I am happy to be your assistant from now on."

"The half-demon launched herself at her friend and wrapped her up in a big hug, finally releasing Rowan from Shaya's molestation. The hero took this opportunity to slip out of the booth and leave the two to whatever it was they wanted to do."

je "Oh, sweet Shaya, I knew I could count on you. Let's have some tea together and catch up."

"She casually waved to Rowan as he was walking out of the brothel."

je "My hero, would you be so kind as to arrange for Shaya's luggage to be brought down here? Thank you."

hide rowan with moveoutright

$ codex_add('shaya_starting')
#end scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

