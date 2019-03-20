init python:

    # special system event to update harassment counter and timer of maid job for some maid events
    event('alexia_maid_harassment_counter', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), init_flags={'harassment_counter': 0}, priority=pr_system_last)
    event('maid_orientation', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), group='alexia_maid', run_count=1, priority=pr_story)
    #Jezera sexcapading in front of Alexia
    event('jezeara_sexcapading_in_front_of_alexia', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='maid'", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"), group='alexia_maid', run_count=1, priority=pr_story)
    event('picky_cleanup', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='maid'", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"), group='alexia_maid', run_count=1, priority=pr_story)
    event('wandering_hands', triggers="npc_events",
        conditions=("get_actor_job('alexia')=='maid'", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0"), group='alexia_maid', run_count=1, priority=pr_story)
    #Jezera wants a new agent
    #Scene triggers on fourth harassment trigger (after three main scenes have triggered).
    event('jezera_wants_a_new_agent', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'", "get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') == 0", 'NTR == True'),
        depends=('jezeara_sexcapading_in_front_of_alexia', 'picky_cleanup', 'wandering_hands'), group='alexia_maid', priority=pr_story)


label alexia_maid_harassment_counter:
    # update harassment timer on Alexia (until harassment sequence will not be ended)
    python:
        if get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') > 0:
            set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', get_event_flag('alexia_maid_harassment_counter', 'harassment_timer') - 1)
    return


label maid_orientation:
#Orientation
#Event triggers the first time that Alexia works as a maid

scene bg14 with fade
show jezera neutral at midright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

je "Hello there Alexia, what brings you to see me?"

"Alexia curtsied slightly, like she'd seen the castle staff do to Jezera when they crossed paths."

al "It's good to see you Jezera. I've been talking with Rowan and the two of us have decided that it would be a good use of my time if I joined the castle staff with cooking, cleaning, and laundry. You're rather short staffed and I'm good at domestics."

show jezera happy at midright with dissolve

je "My dear, you're under no obligations to do anything to help us."

al "I know that, but I'd really like to do something useful. All that labor must be expensive, I can take some of that weight off."

show jezera neutral at midright with dissolve

je "Then be aware that I have high standards for my staff. If you're going to join their ranks, you best be prepared to meet those or be punished. Are you prepared to work for me?"

al "I am."

show jezera happy at midright with dissolve

je "In that case, let's you and I go get you fitted with a uniform, shall we?"

scene alexia_maid_1 with fade

"For most of the week, Alexia busied herself as a member of the castle's domestic staff. She cooked, cleaned, laundered, and even sewed clothing. There was no end to the work and Jezera was a harsh taskmaster."
"While she was completely exhausted by the end, Alexia felt surprisingly good about the whole ordeal. After getting sorted, she'd discovered that the homemaking skills she'd been working on much of her life translated rather well to working as a maid and cook."
"In fact, she may very well have been the best of the staff."

scene bg6 with fade
show jezera happy at midright with dissolve
show alexia maid neutral at midleft with dissolve

je "You've certainly left your mark on this castle and it's only been a single week since you started. I'm very impressed, though I think your skills may be going to waste here."

al "Whatever do you mean?"

show jezera neutral at midright with dissolve

je "A lady of your mind and beauty should be ambitious, you should seek intrigue and attach yourself to power. Make a name for yourself, more than just food, clothes, and kids for a husband's name."

#alexia annoyed
show jezera happy at midright with dissolve

je "Think on it, we'll talk about this soon. I'm sure there's still much I can teach you while you work under me."

#Roll harassment timer
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezeara_sexcapading_in_front_of_alexia:
#Jezera sexcapading in front of Alexia

scene bg7 with fade
#alexia maid happy
show alexia maid neutral at midleft with dissolve

"Alexia was humming a tune under her breath, while washing stains out of the furniture in one of the guest rooms. Just another day working in the castle's domestic staff, until her mistress arrived."

show jezera naked happy at midright with moveinright
#alexia maid shocked

al "Uh...."

"Behind the demoness were a couple of very handsome men, who were also quite naked."

al "Excuse me, I'll come back after-"

je "Oh no, I insist you continue with your work, we aren't bothered."

"Alexia ignored that and instead prepared to leave, only for Jezera to pull a key from somewhere and lock the door to the room!"

je "You may as well keep working, you aren't able to leave anyway."

hide jezera with moveoutright
#alexia maid blush

"To Alexia's horror, the three of them started fornicating right in front of her!  Apparently these guests either didn't care that she was watching them go at it, or they actually enjoyed it!"
"She pushed that thought as far away as she could and desperately tried to distract herself by setting to work once again on the furniture, while Jezera loudly worked on soiling other pieces with her company."

#Alexia gains a bit of corruption and stress.  Re-roll harassment timer, increase harassment event count by one.
$ change_corruption_actor('alexia', 2)
$ all_actors['alexia'].job_state.stress += 2
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label picky_cleanup:
#Picky cleanup

scene alexia_maid_1 with fade
show alexia maid neutral behind alexia_maid_1

al "(I wonder what Rowan's doing right now? No, perhaps it's best I try not to think about what he might be doing...)"

scene bg14 with fade
show alexia maid neutral at midleft with dissolve
show jezera neutral at midright with moveinright

je "Ah, there you are Alexia."

"Alexia stopped her sweeping, turned around to face Jezera and curtsied."

al "Yes mistress? How may I help you?"

show jezera happy at midright with dissolve

je "Today I'm giving you the job of making up my bedroom. I've already made arrangements for someone else to take over for you in the hallways."

"The half-demon stepped to the side and allowed another maid to pass. After a moment's annoyance, Alexia handed the newcomer her broom and followed Jezera."

hide jezera with moveoutright
hide alexia with moveoutright

scene bg18 with fade
show alexia maid neutral at midleft with dissolve
show jezera neutral at midright with dissolve

je "Here we are."

"The room was in quite the state of disarray, with cushions and blankets strewn all over the place as well as at least one pool of something unmentionable on the floor."

je "I expect my abode to be spotless and in perfect order when I return."

al "...  Very well, when will you return?"

je " In an hour? Perhaps two. Better get to work, chop chop."

"The demoness playfully swatted Alexia on the rear."

#alexia maid shocked

al "Hey!"

show jezera happy at midright with dissolve

je "Ta, lovely Alexia."

hide jezera with moveoutright

"She walked out of the room, leaving the red haired woman to her work."

scene black with fade

scene bg18 with fade
show alexia maid neutral at midleft with dissolve

"A little over an hour and a half later, Alexia had taken all of the sheets and soiled cushions down to the laundry and brought up replacements. She'd made up the bed and was working on cleaning up the unmentionable mess when Jezera returned."

show jezera displeased at midright with moveinright

je "What is this? No, no, no!"

#alexia maid shocked

"Taken aback by the harshness of her mistress's words, Alexia shied back from her and managed to soil her uniform in the mess she was cleaning."

al "What's wrong? What did I do?"

je "Do? What did you do?!"
je "YOU PUT GREEN BLANKETS ON MY BED!"

al "Wha-what's wrong with green?"

je "Does it look like green is my colour? Think! Use that small head of yours girl!"
je "Surely you're capable of at least grasping basic aesthetics, unbelievable."

#alexia maid concerned

al "I'm sorry, this really is beyond me. Court fashion and art just isn't something a common housewife like me should-"

je "SILENCE!"

#slap sfx

"At the same time as she said that, Jezera stepped forwards and slapped Alexia across the face!"

hide alexia with dissolve

"The blow sent Alexia to the floor, where she landed in the puddle with an audible splash."

je "You are absolutely capable of this, understand me? You, and only you, are going to take these back and bring some proper blankets for someone such as me."
je "We are going to keep at this until you learn how to do everything perfect."
je "That means that you will place and replace every cushion, every rug, and every curtain until it is exactly perfect. You will learn what it means to take care of a high class lady, no matter how long it takes and how much I have to beat it into you."

#alexia maid upset
show alexia maid neutral at midleft with dissolve
show jezera happy at midright with dissolve

je "Is that understood, darling?"

al "Yes mistress."

#Increase Jezera influence over Alexia.  Re-roll harassment timer, increase harassment event count by one.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label wandering_hands:
#Wandering Hands

scene alexia_maid_1 with fade

"For the most part, Alexia found working in the castle to be enjoyable. Her skills translated well and most of the staff was at least cordial most of the time."
"There were always bad apples, but the housewife felt like she was making friends and finding her place."

scene bg14 with fade
#alexia maid happy
show alexia maid neutral at midleft with dissolve

"The main unfortunate part of her work was her boss."

show jezera happy at center with moveinright
hide jezera with moveoutleft

#alexia maid shocked

al "Hey! Keep your hands off of me!"

scene bg6 with fade
show jezera happy at center with dissolve
show alexia maid neutral at midleft with dissolve

al "Mistress, I would really appreciate it if you'd stop pressing your boobs against me."

#ballroom cg
scene black with fade
#alexia concerned
show alexia maid neutral at midleft with dissolve
show jezera happy behind black

je "Oh lovely Alexia?"

hide jezera
#alexia maid shocked
show jezera happy at midright with moveinright

je "If didn't always assume the best in people, I'd say you're trying to avoid me..."

show jezera happy at center with moveinright
#alexia concerned
show alexia maid neutral at edgeleft with moveoutleft
show jezera displeased at center with dissolve

je "Aww, don't back away from me."

al "I'm worried you're going to touch me again."

show jezera happy at edgeleft with moveoutleft

je "Oh darling, I'm just showing how much I appreciate you. You're such a beautiful woman that I can't help myself."

#alexia maid shocked
show alexia maid neutral at edgeright with moveoutright

al "Ah! Hands off! Don't grope me!"

je "Let me reiterate how happy I am you're helping out around the castle. Keep up the good work."

scene alexia_maid_1 with fade

"Sometimes Alexia felt like Jezera was taking every opportunity to harass and grope her. If there was one thing she could do without, it was that."

#Jezera gains influence on Alexia, Alexia gains a little corruption.  Re-roll harassment timer, increase harassment event count by one.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ change_corruption_actor('alexia', 2)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_counter', get_event_flag('alexia_maid_harassment_counter', 'harassment_counter') + 1)
$ set_event_flag('alexia_maid_harassment_counter', 'harassment_timer', dice(3) + get_event_flag('alexia_maid_harassment_counter', 'harassment_counter'))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_wants_a_new_agent:
#Jezera wants a new agent
#Scene triggers on fourth harassment trigger (after three main scenes have triggered).

# deactivate harassment counter and timer
#~ $ deactivate_event('alexia_maid_harassment_counter')

scene bg14 with fade
#alexia maid happy
show alexia maid neutral at midleft with dissolve
show jezera happy at midright with moveinright

je "Oh Alexia? I've got a special job for you..."

#alexia maid angry

al "No! No more special jobs from you!"

je "Don't be that way, I'm sure you'll love this."

"The demoness stepped towards Alexia with a coy smile on her face and reached out a hand..."

show jezera happy at center with moveinright
show bg14 with sshake

"... only for Alexia to slap Jezera across the face!"

al "Stop touching me, you perverted bitch!"

show jezera displeased at center with dissolve

je "Huh."

#alexia maid concerned

al "Oh no, I, I didn't mean to do that, I..."

show jezera happy at center with dissolve

je "Tisk tisk, slapping your boss isn't good work etiquette."

#alexia maid crying

al "Neither is harassing your employees!"

je "Hah. The difference is I'm half greater-demon. You're just a human peasant girl. A girl who just so happened to fall in love with a man who'd become a hero."

"A lightning fast hand suddenly gripped Alexia's arm, she looked up to see who had seized her. While Jezera's expression remained cheerful, her body language suggested anything but."

#alexia maid concerned

je "Now my brother and I do need you around, insurance for your husband's continued obedience, but there's no reason you need to be able to walk the halls let alone assist my staff."

"Alexia felt completely trapped, unable to move or do anything while in the demoness's grip."

je "So, I get my fun and you accept it. Are we clear?"

"Now she released Alexia's arm, leading to the red haired woman collapsing to the floor a sobbing mess. Not since the very first time she'd seen her mistress's true face had the woman felt such absolute terror."

#alexia maid crying
show jezera neutral at midright with moveoutright

je "It's almost sad just how easy breaking you is. I wonder if you really have as much potential as I first thought."

al "Wh-what do you mean?"

je "Do you remember what I said when you finished your first week under me?  You're far too intelligent and beautiful to be a mere housewife or maid."
je "Those talents of yours could be used for so much more, if only you showed a bit of ambition. Truly I have been disappointed that you haven't sought my help even once yet.  Still, it's never too late to start."

show jezera happy at midright with dissolve

je "I even have the perfect job for you to start with, right now."

al "What are you going to subject me to now?"

je "Not subject, my dear, think of this as an opportunity. An opportunity to impress me."

show alexia maid neutral at midleft with dissolve

"Slowly Alexia stood up, wiping the tears from her eyes and carefully measuring her words and Jezera's responses as best she could."

al "What do you have in mind?"

show jezera neutral at midright with dissolve

je "There's a man of some magical power who is currently my guest at Bloodmeen. He has a history with demons and is rather cautious around me. Thus far he's been, difficult, to get information out of."
je "I would like you to spend some time with him, intimate time. Enough so that he lets his guard down and tells you things."

al "What exactly are you after?"

show jezera happy at midright with dissolve

je "Well, that's your test. The more you find out, the more impressed I'll be. So, are you ready to meet with Mr. Garforth?"

menu:
    "Accept Jezera's task.":
        $ released_fix_rollback()
        # deactivate this event
        $ deactivate_event('jezera_wants_a_new_agent')
        jump garforthMeet

    "Reject Jezera's task.":
        $ released_fix_rollback()
        al "No, I'd rather not do that sort of thing for you."
        je "That's such a shame. Guess I'll have to live with having a little fun with you from time to time."
        #alexia downcast
        al "(Hooray.)"
        #//Trigger generic harassment scene.  Before each subsequent harassment scene, Alexia will have the chance to do this task again.
        # TODO:
        # jump to generic tavern harassment scene for now
        jump generic_harassment_maid
        return

label garforthMeet:

scene bg14 with fade
show alexia maid neutral at midleft with dissolve

al "(This is the room.)"

"Alexia fidgeted in place, nervous about what was going to happen. Then she noticed that she was still holding the vial that Jezera had given her, to help her along, as the demoness had said."
"Resolving that she'd only take Jezera's potion if absolutely necessary, the red haired woman tucked the bottle away and knocked on the door."

play sound "music/SFX/door knock.ogg"
pause 1

#CG of Alexia speaking to Mr. Garforth.  CG is inside the generic guest room.
scene black with fade
show alexia maid neutral behind black

gar "Yes? Ah, I see that you've decided to prey on my weakness for redheads. Come in, come in. I'm curious what you're going to try on me."

"Still nervous, and now somewhat confused, Alexia entered the room. Her mistress hadn't really told her what to expect from the man, so there was no way to know what to expect."
"As it turned out, this man seemed to be a rather smaller thin man. He seemed to be about the same height as her, but a glance around the room suggested that he knew at least some magic."
"Tomes of power similar to the library were here, along with apparatuses that she'd seen Cliohna use."
"If anything, his appearance suggested a scholar that spent a great deal of time stooped over a book while neglecting his personal health."

al "Uh, Mr. Garforth, right?"

$ garforth_name = "Mr. Garforth"

gar "Yes. Trying to be a nervous girl?  Hmm, seems lazy. Honestly I thought that Jezera herself would come by to try and loosen my lips, but you don't have that level of power. I wonder, what class of demon are you girl?"

scene black with flash
#cg variant
scene black with dissolve
show alexia maid neutral behind black

"Alexia felt an indignant reply start to rise up, which died on her lips as a bright flash of light blinded her for a moment. When her vision cleared, she was surprised to see that there was a look of absolute terror on Mr. Garforth's face."

al "What was that for?!"

gar "Y-y-you're not a demon!"

al "Of course not! You just noticed that?"

gar "Oh, uh, I'm s-s-so sorry! I, uh, I'm not..."

"His voice trailed off too quiet for Alexia to hear him. The two simply looked at one another for a long awkward moment before the woman cleared her throat and spoke up again."

al "I didn't catch the end of that."

gar "I'm not good around girls."

al "Ah."
al "(Great. That only made the situation even more awkward. How do I want to go from here?)"

menu:
    "Introduce yourself.":
        $ released_fix_rollback()
        al "Maybe we got off on the wrong foot, I'm Alexia Blackwell, what's your name?"
        gar "B-b-blackwell?! You're Rowan of Rosaria's wife?!"
        al "Uh... Mr. Garforth?"
        "Far from helping the situation, telling the man her name had terrified him even more. Now Alexia was worried how much she could even get out of the man since he wasn't even responding to her words anymore."
        "Her hand brushed against the potion in her dress. Well, it was now or never."
        $ garInfo = "0"
        jump garPotion

    "Ask him some questions.":
        $ released_fix_rollback()
        al "Mr. Garforth, I was wondering if maybe you could tell me something about yourself."
        gar "Oh, I'm not anybody interesting. Just a sorcerer fresh off his apprenticeship who wanted to learn more about the castle."
        al "I guess you were expecting it to be empty, weren't you?"
        gar "Well, I was hoping to meet some cute demons here, but that violet bitch wasn't really what I was expecting."
        "While Alexia could perfectly understand someone calling Jezera a bitch, she wasn't quite so sure what to make about his other statement."
        al "Cute demons?"
        gar "Hmm...."
        "He broke eye contact, blushing furiously."
        al "How about we talk about something else, who was your master?  Mr. Garforth?"
        gar "Yes!  Uh, my master was the famed wizard, Ceradil!  He lives in Niernan’s Redoubt and specializes in earth magic, which is why he took me on as apprentice. During the war he fought in the elven armies until the day he was taken prisoner and..."
        "Once more, the man trailed off uncertainly, his blush coming back."
        al "Why do you keep falling silent like that?"
        gar "This isn't something a lady should hear about! Uh, thanks for visiting, but I'd really like it if you left now!"
        "Despite her attempts to convince him otherwise, it seemed that Garforth was quite done saying anything to Alexia. Just as she was about to give up, she remembered the potion in her pocket. Well, it was now or never."
        $ garInfo = "1"
        jump garPotion

    "Reassure him.":
        $ released_fix_rollback()
        al "Please relax Mr Garforth. I'm not going to do anything to you, talking a bit never hurt anyone."
        gar "Of course, right."
        al "Why were you much more confident when you thought I was a demon?"
        gar "Well, I studied a lot about demons when I was an apprentice. Especially safeguards against their influence and power. This was going to be how I tested myself, finding the demons of this place and showing that they could do nothing to me."
        al "That sounds very brave, what made you think that there'd be demons here?"
        gar "Well, I noticed a strange nexus in the world's flux field about a year and a half ago. I'd been tracking it since, and eventually figured out it originated here."
        al "Wow! That's impressive, were you the first to figure this out?"
        gar "Thanks, it's not something a normal sorcerer would notice, since most don't gaze around the outer dark looking for the specific kinds of demons I do."
        al "Specific kinds of demons?"
        gar "Yeah, they... uh... thank you for talking to me! It was really fun! Have a good day!"
        "Despite her attempts to convince him otherwise, it seemed that Garforth was quite done saying anything to Alexia. Just as she was about to give up, she remembered the potion in her pocket. Well, it was now or never."
        $ garInfo = "2"
        jump garPotion

label garPotion:

menu:
    "Drink the potion.":
        $ released_fix_rollback()
        $ garPotion = "1"
        jump garPotionDrink

    "Leave.":
        $ released_fix_rollback()
        $ garPotion = "0"
        jump garLeaveEarly

label garPotionDrink:

"Trying to be as discreet as possible, Alexia pulled the potion that Jezera had given her and downed the contents. A moment later, she felt a rising heat in her lower body."

#If (Alexia had tea with Jezera)
if jezNTR1:
    "She quickly realized that it was the same as the tea that she'd shared with Jezera several months back.  So, it was a lust draft or something like that."

#rejoin
"Next her gaze fell upon the nervous man once more. The red haired woman wasn't sure what exactly this was going to do to help her deal with the man. He was still in the same unconsolable state."


scene cg98 with fade
pause 3

"Abruptly, she grabbed and pulled him into a deep kiss. The instant their lips touched, the sorcerer froze in place, then seemed to relax for the time since he'd identified Alexia as a regular human woman."

menu:
    "Resist the potion, get out of the room.":
        $ released_fix_rollback()
        "Realizing what she'd just done, Alexia pushed away and ran out of the room as quickly as she could, before the potion made her do anything else."
        jump garLeaveEarly

    "Lean into the kiss.":
        $ released_fix_rollback()
        jump garSexScene1

label garSexScene1:

#Alexia gains a bit of corruption and Jezera influence.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ change_corruption_actor('alexia', 2)

"Their bodies grew closer and closer, becoming entwined as the kiss went on and on."

scene cg97 with fade
pause 3
show alexia maid aroused behind cg97

"Finally, Alexia broke it off, feeling both a mix of embarrassment and bewilderment at her actions. Still, the man seemed to have calmed down so she'd best use this opportunity."

if garInfo == "0":
    al "Relax Garforth. My husband will never find out about this. You can trust me, relax."

else:
    pass

if garInfo == "1":
    al "I'm not a normal lady, you can tell me all your dirty secrets."

else:
    pass

if garInfo == "2":
    al "We're having such a good conversation, I don't mind if there's something you aren't ready to talk about."

else:
    pass

scene cg96 with fade
show alexia maid aroused behind cg96
pause 3

"As she spoke, she lead him to sit down next to her on a bench."

al "Why don't we start over? What's your name?"

gar "Berrington."

al "What a nice name, I think I'll call you Berry. You don't mind, do you?"

gar "N-no."

"Alexia was surprised to notice that she was actually fondling him through his pants!"

menu:
    "Time to leave, before the potion makes you do anything else!":
        $ released_fix_rollback()
        "Alexia pushed the man away and ran out of the room as quickly as she could, before the potion made her do anything else."
        jump garLeaveEarly

    "It's fine, keep trying to get information.":
        $ released_fix_rollback()
        jump garSexScene2

label garSexScene2:

#Alexia gains a bit of corruption and Jezera influence.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 2)
$ change_corruption_actor('alexia', 2)

"However, her shock wasn't enough to make her stop or end the pseudo-interrogation she was engaged in."

al " Alright Berry, do you think you could tell me more about yourself, don't leave out any details."

"The man proved to be very pliable now that Alexia was stroking him, he was almost eager to talk about himself, why he was at the castle, and his interests. Apparently the guy had a rather submissive streak, Alexia realized it was a bit like how she acted around Rowan."
"However, he proved to be much more cagey about giving away information about his teacher and what happened during the last chaos war."

al "Oh Berry, why are you so hesitant about telling me about the war? You can trust me, I won't tell anyone what happened. I'd really like to know."

"She punctuated her last sentence with a much harder stroke, then slowed her fondling to a near stop to incentivize his answer."

gar "I... I... I really shouldn't say anymore about Ceradil. Sorry, but it's just not safe to talk about that."

"Clearly, something much more drastic than a kiss and a handy was needed now."

menu:
    "No! You're not the kind of woman who breaks her vows like this!":
        $ released_fix_rollback()
        "Alexia steeled her resolve and pushed the dirty thoughts from her mind. No, this was as far as she would go."
        al "Alright, thanks for chatting with me Berry. I'll see you some other time, okay?"
        "With a smile and a wave, she left the man behind."
        $ garInfo = "3"
        jump garLeaveLate

    "You're so close, only a little more and Garforth is yours!":
        $ released_fix_rollback()
        jump garSexScene3

label garSexScene3:

#Alexia gains a lot of corruption and Jezera influence.
$ set_actor_flag('alexia', 'jezera_influence', get_actor_flag('alexia', 'jezera_influence') + 3)
$ change_corruption_actor('alexia', 2)

scene black with fade

"Alexia flipped over, so she was straddling the sorcerer's lap. A grin filled her face as she pulled his stiff member free from its confines followed by lowering her lower garments so that her puffed up sex tasted the air."
"Ever since she'd drank the potion, she'd wanted to satisfy her need. Now she'd get exactly that chance."

gar "Uh, miss?"

show alexia maid aroused behind black

al "Shh, just let it happen."

scene cg92 with fade
show alexia maid aroused behind cg92
pause 3

"A low moan of satisfaction escaped from Alexia's lips as she sank down onto his length. There was no resistance, no attempt to stop her or hasten her. Garforth simply sat there and allowed the redhead to do as she willed with him."

al "Hmm, good boy. I'll take good care of you."

"A quick gasp came from him as Alexia started moving her hips, rising and falling in a steady rhythm. Then sudden gasps of excitement when she switched to a steady gyration of her hips."

al "Yeah, you like that?"

gar "Y-yes."

al "What about these?"

scene cg92 with sshake
scene cg92 with sshake
scene cg93 with flash
show alexia maid aroused behind cg93
pause 3

"As she said that, she pulled her breasts out of her dress and leaned forward to push one up into her plaything's face.  He giggled somewhat stupidly and used a hand to stroke her slightly. Then a low groan came from him and Alexia felt him let out his load inside her."
"Apparently he was a bit of a quick shot, that or the extended handjob had worn his endurance away already. She hid her disappointment at the sudden finish and instead whispered in his ear her question once more."

al "Now you owe me a full explanation. What happened to Ceradil during the war?"

scene black with fade

$ alexiaUnfaithful = True
$ garInfo = "4"
jump garLeaveLate

label garLeaveEarly:

scene bg14 with fade
show jezera displeased at midright with dissolve
show alexia maid neutral at midleft with moveinleft

"Shortly after leaving, she ran into her mistress."

je "Hmm, you weren't in there for very long. I hope you at least learned something useful."

if garInfo == "0":
    al "I'm sorry, but he seemed to panic after I introduced myself and-"
    if garPotion == "0":
        je "And you should have been able to wrap him around your finger. There's a reason I picked that man to be your first target, he's an easy mark. If you were feeling squeamish, my potion would have solved that problem in short order."
    else:
        je "And you should have been able to wrap him around your finger. There's a reason I picked that man to be your first target, he's an easy mark. If you hadn't panicked and run away, my potion would have solved that problem in short order."

    al "What exactly do you mean?"

    #jez angry
    #alexia scared
    je "Tease him, fuck him, make him beg for more and spill his life to you for it! Foolish girl, what do you think I'm doing most of the time? This body, this dress? They're not just for show, these are a lady's weapons."
    #jez annoyed
    je "A pretty face and a sharp tongue can be just as deadly as a sword."
    show alexia maid neutral at midleft with dissolve
    je "You could do so much, if only you didn't get hung up all the time."
    show jezera happy at midright with dissolve
    je " I have grown rather wary of this game. Perhaps you are only useful as a chain or a toy? Or perhaps you need more incentives to finally get your pretty little head in the game?"
    show jezera displeased at midright with dissolve
    je "Since you seem to like working in the staff so much and have wasted my time with this charade, you're off the castle staff for a month! Find someone else to bother in the meantime."
    hide jezera with moveoutright
    al "*sniff*"
    al "(Sorry Rowan, that wasn't my best work.)"
    #Alexia cannot be assigned as a maid for four weeks.
    # TODO:
    return

else:
    pass

if garInfo == "1":
    al "Well, I found out his master was someone named Ceradil from Niernan’s Redoubt.  I think there was something about Earth magic and something happened during the war to his master."
    if garPotion == "0":
        al "He got embarrassed after that and didn't want to talk anymore."
        je "Lost your nerve? Then all you needed to do was drink my potion. There's a reason I picked that man for you to practise on, he's such a sub that even you would have been able to wrap him around your finger."
    else:
        al "I drank your potion and started acting weird, so I got out as fast as I could."
        je "Lost your nerve? My potion should have fixed that, shame you are so apprehensive. There's a reason I picked that man for you to practise on, he's such a sub that even you would have been able to wrap him around your finger."

    show jezera happy at midright with dissolve
    je "You have such a pretty body and a clever mind, I just wish you'd recognize them as the weapons they are. We could do so much together then."
    show jezera neutral at midright with dissolve
    je "Next time, perhaps. Once I find a suitable target."
    show jezera happy at midright with dissolve
    je "Ta darling."
    hide jezera with moveoutright
    return

else:
    pass

if garInfo == "2":
    al "I didn't really understand what he was saying, something about a nexus in the world and it being tied to the kinds of demons he looks for in the outer dark. Somehow that lead him here."
    je "Good catch for such a small interview. From the sounds of things he found my portal network, I'll have to investigate this further. What else did you find out?"
    if garPotion == "0":
        al "Nothing else I'm afraid, he got really nervous and made me leave when I asked him what kinds of demons he was looking for."
    else:
        al "I tried drinking your potion after he got nervous about the kinds of demons he was looking for, but needed to get out of there when it made me do things."
    show jezera happy at midright with dissolve
    je "Heh, interesting boy you are Garforth."
    show jezera displeased at midright with dissolve
    je "As for you, that was your cue to wrap him around your finger. There's a reason I picked him to be your target, he's such a sub that even you should have had no trouble seducing him and getting him to pour his heart out."
    show jezera neutral at midright with dissolve
    if garPotion == "0":
        je "Guess I should take that potion back then, considering you obviously didn't take it."
    else:
        je "Jezera: I'll let you off the hook for wasting my potion, for the moment."

    je "Next time, you should use your beautiful body and clever mind for what they were made for. A lady with the will to do what's necessary is as dangerous as any man."
    show jezera happy at midright with dissolve
    je "I'll give you one more chance. Just give me a little while to find an appropriate target. Ta darling."
    hide jezera with moveoutright
    return

else:
    pass

label garLeaveLate:

scene bg14 with fade
show jezera happy at midright with dissolve
show alexia maid neutral at midleft with moveinleft

"Shortly after leaving the sorcerer's room, Alexia ran into her mistress."

je "Hmhmm, you look like you had fun."

#concerned
show alexia maid neutral at midleft with moveinleft

je "Don't look that way, I'm sure you did great. What did you think of Mr. Garforth?"

al "I don't know. He seemed, weak?  So different from Rowan."

je "Lots of girls hate those kinds of guys, they're very useful though, give them an inch and they'll give you a mile. That's why I made him your first target, I knew it wouldn't be very hard to wrap him around your finger."

show jezera neutral at midright with dissolve

je "Now, let's hear what you discovered from our guest."

if garInfo == "3":
    scene black with fade
    scene bg14 with fade
    show jezera happy at midright with dissolve
    show alexia maid neutral at midleft with dissolve
    je "So you weren't willing to take that last step? Even with my direction."
    #angry
    show alexia maid neutral at midleft with dissolve
    al "What, your direction? What do you mean!?"
    show jezera neutral at midright with dissolve
    je "Ah my dear, I do apologize for engaging in a little possession to help you along, but you instincts need a little work right now."
    show jezera happy at midright with dissolve
    je "Eventually I'm sure you'll just know what needs to be done without my influence. For the moment, I'm suitably impressed by your efforts. As a reward, I believe that I'll be able to restrain myself while you're working as a member of my staff."
    show alexia maid neutral at midleft with dissolve
    je "Darling Alexia, you will make an excellent informant soon enough. The next lesson will start as soon as I find an appropriate subject."
    hide jezera with moveoutright
    #happy
    show alexia maid neutral at midleft with dissolve
    al "(Maybe I can learn something from her.)"
    #Jezera will no longer harass Alexia while she's working as a maid.
    # TODO:
    return

else:
    scene black with fade
    scene bg14 with fade
    show jezera happy at midright with dissolve
    show alexia maid neutral at midleft with dissolve
    je "See? It isn't so bad once you get over your silly little hangups about marriage and vows. It can be a lot of fun having boys like that as playthings."
    #sad
    show alexia maid neutral at midleft with dissolve
    al "Men like that? Why would you want someone like that? He was done so quickly..."
    je "Sometimes they do need a little training, but there are other ways you can get pleasure out of a man than fucking them. You could have always had him eat you out afterwards. As you found out, he has a bit of a kink for dominant demonesses."
    #angry
    show alexia maid neutral at midleft with dissolve
    al "Wait, were you watching me the whole time?!"
    show jezera neutral at midright with dissolve
    je "Not directly, I couldn't see or hear what was going on, but I did know what you were feeling. I also touched your mind a little. I apologize my dear, but your instincts still need some work so you need a little help with doing the right thing for the situation."
    #sad
    show alexia maid neutral at midleft with dissolve
    je "Chin up, I'm very proud of what you did today. So proud that I can restrain myself while you work under me. Though, we can always keep at it if it turns out you want me to. In the meantime, we should continue your training in earnest. I just need a suitable subject."
    hide jezera with moveoutright
    al "(What's happening to me?)"
    #Jezera will no longer harass Alexia while she's working as a maid.
    # TODO:
    return
