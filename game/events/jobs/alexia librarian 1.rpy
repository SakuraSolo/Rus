init python:

    # special system event to update counters of library job for some library events
    event('alexia_library_counter', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), priority=pr_system_last)
    #Orientation
    #Event triggers the first time that Alexia works in the library.
    event('library_orientation', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_story)
    #A book of magic
    #Triggers only after Alexia has worked in the library for at least three weeks.  Repeat version will trigger periodically every 2-4 weeks after that until Alexia either chooses to take the book, or her class changes.
    # TODO: check for job_class?
    event('a_book_of_magic', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'", "get_event_flag('a_book_of_magic', '_library_job_delay')==0"),
        group='alexia_library', run_count=1, init_flags={'_library_job_delay': 3}, priority=pr_npc)
    #A book of magic (repeat)
    #Repeat version will trigger periodically every 2-4 weeks after that until Alexia either chooses to take the book, or her class changes.
    event('a_book_of_magic_repeat', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'", "get_event_flag('a_book_of_magic_repeat', '_library_job_delay')==0"),
        group='alexia_library', active=False, priority=pr_npc)
    #Alexia's self-taught magic
    #Triggers two weeks after Alexia takes the book, regardless of her current assignment.
    event('alexia_s_self_taught_magic', triggers="npc_events", run_count=1, active=False, priority=pr_story)
    #Cliohna warms to Alexia's magic
    #High priority.  Triggers when Alexia works in the library after she learns magic.
    event('cliohna_warms_to_alexia_s_magic', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), run_count=1,
        depends=('alexia_s_self_taught_magic',), group='alexia_library', priority=pr_story)
    #Alexia's Power
    #Alexia must have been working in library for three weeks after Cliohna warms to Alexia's magic triggers.
    event('alexia_s_power', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'", "get_event_flag('alexia_s_power', '_library_job_delay')==0"),
        group='alexia_library', active=False, priority=pr_npc)


label alexia_library_counter:
    # update delay for all library job events that are active currently and has that delay set
    python:
        for ev_name in all_events_data:
            if get_event_flag(ev_name, '_library_job_delay') > 0:
                if get_event_flag(ev_name, '_active'):
                    set_event_flag(ev_name, '_library_job_delay', get_event_flag(ev_name, '_library_job_delay') - 1)
    return


label library_orientation:
#Orientation
#Event triggers the first time that Alexia works in the library.

scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

"Alexia waited for a moment to be addressed after arriving in the library. When it seemed that none was forthcoming, she cleared her throat awkwardly."

al "Ahem, excuse me?"

"The librarian let out a weary sigh and stopped ignoring the woman."

cl "Yes Alexia? Why is it you're bothering me?"

show alexia 2 necklace concerned at midleft with dissolve

al " I was wondering if there was anything I could do to help you out here in the library?"

cl "Well then, what scale are we speaking of here? Something to keep you occupied for an hour, until lunch, the whole day?"

al "The week, actually. I want to make myself useful and Rowan suggested that the library would be the place to go."

cl "You certainly have shown a bit more interest in the realm of knowledge and literature that my employers have sadly lacked. There are some tasks that I can set you that will save me time and help things run more efficiently here."

show alexia 2 necklace neutral at midleft with dissolve

cl "Very well, I will accept your assistance for the time being and we shall see how you perform."

scene alexia_library_1 with fade

"After getting settled, Alexia spent most of the week in the library as Cliohna's assistant. She catalogued books, retrieved them, returned them, and aided with basic experiments when Cliohna trusted she was up to the task."

scene black with fade

scene bg12 with fade
#cliohna happy
show cliohna neutral at cliohnaright with dissolve
show alexia librarian neutral at midleft with dissolve

cl "That will be all for the day. I must say that you have proven to be quite capable at the tasks I have assigned you. I will welcome your aid again when you are available."

al "Thank you sorceress. Working in the library was quite pleasant and I would be happy to help you again."
$ do_job_research_assistant('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label a_book_of_magic:
#A book of magic
#Triggers only after Alexia has worked in the library for at least three weeks.  Repeat version will trigger periodically every 2-4 weeks after that until Alexia either chooses to take the book, or her class changes.

scene alexia_library_1 with fade
show alexia librarian neutral behind alexia_library_1

"While cataloguing the books in the library, Alexia stumbled upon a book whose title rather intrigued her."

al "'The Apprentice's Guidebook to Basic Spells'. Oh."

"She hesitated, considering the book.  Her mind returned to the time when Cliohna had tested her and determined that she had the potential for magic. The sorcerer hadn't said anything further on the subject, and Alexia hadn't inquired either to avoid upsetting her."
"However, it was possible for Alexia to use magic, she knew that now, and here was possibly a book that she could potentially learn from. Cliohna didn't mind if she checked out books from the library for personal use, maybe she should do so with this one and try to learn?"

$ do_job_research_assistant('alexia')

menu:
    "Alexia took the book to study.":
        $ released_fix_rollback()
        al "Magic...."
        "With some trepidation, she pulled the small handbook from the shelf and tucked it into her apron.  This wasn't entirely out of the ordinary and she noted the time and place that the book had been taken on her list."
        "Tonight, she'd begin her studies of the arcane."
        #Note Alexia is now studying magic.  In two weeks time the follow up event will trigger, regardless of what job she is doing then.
        $ set_actor_flag('alexia', 'studying_magic', True)
        $ activate_event('alexia_s_self_taught_magic')
        $ set_event_timer('alexia_s_self_taught_magic', 'library', 2)
        return

    "Alexia left the book where it was.":
        $ released_fix_rollback()
        al "No, I shouldn't."
        "Shaking her head and forcing the alluring thoughts of power from her mind, Alexia returned to her work."
        #Roll a new event for the library, so that this scene isn't constantly overriding normal library scenes.
        $ activate_event('a_book_of_magic_repeat')
        $ set_event_flag('a_book_of_magic_repeat', '_library_job_delay', 1+dice(3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label a_book_of_magic_repeat:
#A book of magic (repeat)

scene alexia_library_1 with fade
show alexia librarian neutral behind alexia_library_1

"Alexia looked up and started. She hadn't been paying much attention to where she was going and had found herself in an aisle of magical tomes that seemed to call to her. Seemingly of its own accord, one of her hands was reaching towards one of the ancient books."
"A warning to be wary of books flashed through her mind and she reflexively pulled away. At the same time, she recalled a much smaller less threatening book that had stuck out in her mind previously."

al "This is where I found that Spell Guildbook, isn't it?"

"Once again, she considered taking the book and trying to learn magic from it."

$ do_job_research_assistant('alexia')

menu:
    "Alexia sought out the book to study magic.":
        $ released_fix_rollback()
        "Alexia rolled one of the ladders across the floor and scanned the shelves for the small handbook. When she spotted it, she almost thought her heart would beat out of her chest in anticipation."
        al "Magic...."
        "With some trepidation, she pulled the small handbook from the shelf and tucked it into her apron.  This wasn't entirely out of the ordinary and she noted the time and place that the book had been taken on her list."
        "Tonight, she'd begin her studies of the arcane."
        #Note Alexia is now studying magic.  In two weeks time the follow up event will trigger, regardless of what job she is doing then.
        $ activate_event('alexia_s_self_taught_magic')
        $ set_event_timer('alexia_s_self_taught_magic', 'library', 2)
        return

    "Alexia pushed back the urge and continued her work.":
        $ released_fix_rollback()
        "And again, she pushed the urge away.  Magic was not her place and she wasn't going to mess with it if at all possible."
        #Roll a new event for the library, so that this scene isn't constantly overriding normal library scenes.
        $ set_event_flag('a_book_of_magic_repeat', '_library_job_delay', 1+dice(3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_s_self_taught_magic:
#Alexia's self-taught magic
#Triggers two weeks after Alexia takes the book, regardless of her current assignment.

scene bg12 with fade
show alexia librarian neutral behind bg12

"Since Alexia had taken the magic guidebook from the library, she'd been studying it whenever she'd had the chance. Sometimes it referenced other works that she was able to find in the library, but most of what she needed was in the apprentice's guide."

al "('The main types of magic are: elemental, divine, chaotic, and fae. Their types depending on the source of power that is drawn upon. Elemental magic is drawn out from within those with magical potential. Its power is a reflection of the person calling upon it.')"
al "('The other three groups are all gained from the power of something else, drawing on their will and making it manifest in the world. Divine magic calls upon the power of Solansia and the lesser righteous gods. Worthy worshipers can be granted these powers by their patrons.')"
al "('Chaotic and fae magics are brought forth from the denizens of the Outer Dark and will inherently twist and corrupt the users. Many a foolish apprentice has sought these as a quick means of gaining power, but this has always ended in tragedy for the poor fool.')"
al "('Therefor the magics you will be most concerned with directly is elemental magic and its uses.')"

scene bg7 with fade
show alexia 2 necklace neutral at midleft with dissolve

al "(Come on Alexia, you can do this.  Focus!)"

"This week, she was trying to seriously call on her magic. There had been a few failed attempts already, but that didn't stop her from trying again."
"Alexia held her hand in front of her, trying to concentrate like she'd read how to.  She called upon the flame within, tried to coax it out."
"Opening her eyes, she saw with a start that her hand was actually glowing!"

show alexia 2 necklace shocked at midleft with dissolve

al "Did I do it?  Did I actually do it?!"

"With her concentration broken, the light from her hand went out."

show alexia 2 necklace neutral at midleft with dissolve

al "(Okay girl, calm down.  Maybe this was a fluke, just try it again.)"

"Once more she called upon the power within, trying to draw it out of her. This time she thought she could actually feel the power within as it came out and opened her eyes to see her hand was glowing once more!"

al "Wow, I can actually do this. It's almost unbelievable."

scene bg7 with fade
show alexia 2 necklace neutral at midleft with dissolve

"The next day, she'd prepared for the next step suggested by the guide."
"On the table in front of her, Alexia had placed a candle, a glass of water, two iron spoons, some dirt, and a sealed waterskin filled with air."
"The book had instructed that this was a good way to determine your aptitude with the different elements and learn what kind of magic you were most attuned with."
"Once more she closed her eyes and focused on the power within her and held her hand forwards, trying to figure out which of the items on the table she resonated most with. She couldn't really feel any different, had she done something wrong?"

al "(Maybe I'm just too far away from them?)"

"After stepping forwards, she tried again. This time, was that something? Maybe a flicker, a flow, a wave."
"Alexia's hand was hovering very close by the glass of water, almost touching it. She picked the glass  up and looked into the clear liquid closely."

al "(Yes, the water doesn't look any different, but I can feel something about it I never noticed before. So I guess this means I'm attuned to water?)"

"This was somewhat of a disappointment for the red haired woman. Water wasn't terribly exciting next to fire or lightning. Then again, compared to air and earth, water did seem like it fit her the best."

al "A water sorcerer. I wonder what Rowan would have been if he'd learned magic?"

show alexia 2 necklace happy at midleft with dissolve

al "Heh, probably earth, he's a foundation, someone who grounds you and keeps everyone together."

show alexia 2 necklace neutral at midleft with dissolve

al "Is Cliohna maybe water too? No, when she found out about my potential, it was lightning that sprang from her hands. That's what she must be."

"After setting the glass down and blowing out the candle, Alexia took out the apprentice's guide to spellcasting again."

show alexia 2 necklace happy at midleft with dissolve

al "(What kind of basic spells does this have for water sorcerers?)"

#The next time she works in the library, Cliohna warms to Alexia's magic event triggers.
$ do_job_research_assistant('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label cliohna_warms_to_alexia_s_magic:
#Cliohna warms to Alexia's magic
#High priority.  Triggers when Alexia works in the library after she learns magic.

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve
show cliohna neutral at cliohnaright with moveinright

al "Yes sorceress?"

cl "I have taken note that you've shown an interest in the arcane arts."

#alexia concerned

al "What do you mean?"

cl "Much of your free time has been spent in the library studying whatever you can get your hands on with regards to novice magic."

#cliohna happy

cl "I must admit that your enthusiasm is impressive. Have you managed to learn anything in this time?"

al "A little bit, I've figured out that I'm attuned with water and uh, can do this at least."

"She took a deep breath, closed her eyes, and held out her hand palm down."

show bg12 with flash

"An icicle emerged from her palm, about a quarter of a meter in length, then dropped to the floor with a thud."

#alexia / cliohna neutral

cl "Well, I would say that is a start on the elementals. Have you learned anything besides basic magic with water?"

al "No! Why would I want to meddle with corrupt forces? It's already hard enough to be a devout follower of the goddess here in Bloodmeen."

#cliohna happy

cl "Hmm, now what book exactly have you been reading to react like that?"

#alexia concerned

al "Uh, that would be this one."

"Sheepishly she pulled the guide from her apron and held it out to the librarian."

#cliohna neutral

cl "'The Apprentice's Guidebook to Basic Spells', one of Gordash's works? Ha! No wonder you're confused. Let me tell you girl, there's no difference between what he calls the divine and chaotic magics."
cl "Both of them are drawing on the power of higher beings and both of them will affect the users. Also, you won't get very far with just the elementals. Those are only the start of learning magic, communing and channeling is where true power lies."

#alexia neutral

"Dismissively she tossed the book back to Alexia who fumbled a bit before catching the book."

cl "I will admit he is right that someone like you shouldn't mess with higher beings without help. Weak and inexperienced sorcerers are the perfect tools for demons to find their way into this world. They want someone they can easily control after all."
cl "Keep reading Gordash if you want, but should you desire to learn proper magic you'll need a teacher. Perhaps Rowan will be able to help you with that? Assuming you can get the twins to let you out long enough to hone that fledgling power."

al "Couldn't you teach me something?"

#cliohna happy

cl "I admit I'm curious what you will learn and how you will grow. It softens the frustration I felt when I discovered your inborn gift to know how seriously you're taking that power. Perhaps I can spare a little time while you're working for me to hone your skills."
cl "Good luck, Alexia."

hide cliohna with moveoutright

#Alexia's power event can now trigger after working in library for 3 more weeks.
$ activate_event('alexia_s_power')
$ set_event_flag('alexia_s_power', '_library_job_delay', 3)
$ do_job_research_assistant('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label alexia_s_power:
#Alexia's Power
#Alexia must have been working in library for three weeks after Cliohna warms to Alexia's magic triggers.

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

cl "Again."

"Once more Alexia drew on her power, brought her hand up, a glow of power surrounded her outward facing palm..."

show bg12 with flash
#thunk sfx

"... and a meter long lance of ice flew forth and embedded itself into the target on the other side of the library."

cl "Very close to the center. You're definitely getting better with your aim."

"While her training had started outside, Cliohna was confident enough that Alexia wouldn't be causing much collateral damage at this point and had permitted training to happen in the library now."
"Admittedly, the reason for that had been mainly due to how long Alexia had to rest between using her magic. The strain from spellcasting tended to leave her winded after throwing only a handful of those shards and it took many hours for her to be able to cast again."

cl "Again."

al "No, I have to stop now... I feel so... tired."

#Alexia's eyes close, Cliohna looks disappointed.

cl "For all these weeks of training you still can only employ a pittance of power before running dry? It would seem that your potential is rather- limited."

"Alexia's fears had been confirmed. While she did have magical potential, her magic was weak."

#Cliohna half smiles.

cl "One can hardly fault you for a lack of dedication and perseverance. Far too many would-be sorcerers rely purely on talent and raw potential, never truly honing what they have or seeking to discover the true depths of what they can accomplish through hard work."

#alexia neutral

cl "Bearing this insight in mind, I would recommend that we shift the focus of your training away from power and endurance training towards learning what you can do with what little power you do have. Perhaps it is time to bring another element under your power?"

scene black with fade

"Three days later..."

#Show Alexia magic CG
scene black with fade
show cliohna neutral behind black

"Cliohna had set Alexia a challenge, to call on three different elements. Yesterday, she'd learned how to call on electricity under direct tutalage, then had been instructed to learn another on her own. Today, Alexia was going to demonstrate what she'd learned."

cl "It is time to demonstrate what you have learned. I am curious what power you managed to call on, if any."

"The red haired woman didn't answer. Instead she simply focused her power, drawing on that force, and focusing it between her hands."

#CG shows a floating stone between Alexia's hands.
show black with flash

"A stone, or perhaps a clump of sand, seemed to materialize between her hands."

cl "Ah, earth.  It would seem that you have a talent for learning new tricks rather fast. Most students aren't able to call on their second element without help until they've been using magic for many months."

#CG shows a drop of water floating to the left of stone.
show black with flash

"Now drawing on the more familiar and more natural power, Alexia called a drop of water into existence as well. This show wasn't over yet, she wasn't about to be patronized and had every intention of completing the entire challenge that had been set to her."

cl "Huh? Two elements at once?"

"Finally, the most difficult part. While still making sure not to let the powers mix between her hands, Alexia called forth on the power that Cliohna had awakened in her the day before."

#CG shows a ball of electricity floating on the opposite side of the water.
show bg12 with flash

"Then there was a ball of energy floating on the other side of the rock."
"The strain of maintaining these powers caused Alexia's hands to shake, but while practising she'd found that she could maintain this for almost a minute as long as the earth was between water and electricity."
"To the woman's surprise, her teacher said nothing more to her.  So she maintained the configuration for as long as she could, then released it."

#first cg
show bg12 with flash

"The tiny nodes of power quickly dissipated.  Alexia took a deep breath to steady her heart, then opened her eyes."

show bg12 with fade
show alexia librarian neutral at midleft with dissolve
#cliohna shocked
show cliohna neutral at cliohnaright with dissolve

"Cliohna appeared to have been struck dumb.  For a moment, Alexia feared that perhaps she'd somehow harmed her teacher."

#alexia concerned

al "Oh no, Cliohna are you alright? Did I do something wrong?"

cl "I... Alexia, I cannot maintain three elements at once. Such a talent usually takes years, even a decade to learn. You just did it in a matter of weeks. One that I have never been able to accomplish."

#alexia happy

"Such unexpected praise caught her off guard and Alexia felt her face grow hot in embarrassment. Then she started giggling uncontrollably."

al "No, hahah, I'm just a housewife, ha, you're joking, haha, right?"

#cliohna neutral

cl "It would seem that I have underestimated you. A lack of power may have just given you a talent for manipulation of magic."

al "Haha, you know, it kinda does feel like I'm knitting when I use magic or like when you're doing delicate cooking. Always watching several things at once, making sure nothing is burning or keeping track of a lot of pieces at the same time."

cl "Just a housewife... yet simply understanding magic the way you seem to makes you invaluable as an assistant."

#cliohna happy

cl "I do hope that I can continue to count on your services in the future, Alexia. It would seem that we both have things to learn from one another."

#Rowan can now talk to Cliohna about Alexia becoming her apprentice.  Alexia now has relative mastery of the ice shard spell, she can use it in other scenes.
$ alexia_knows_magic = True
$ alexia_ice_shard = 1
$ do_job_research_assistant('alexia')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
