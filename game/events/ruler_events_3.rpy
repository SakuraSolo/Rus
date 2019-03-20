init python:

    # X'zaratl's advances
    # Can trigger three weeks after Dark Sanctum is built, can happen 1 week earlier and is high priority if Rowan was friendly with X'zaratl.
    event('xzaratl_s_advances', triggers="week_end", conditions=("castle.buildings['sanctum'].lvl >= 1", 'week >=4'), group='ruler_event', active=False, run_count=1,
        priority='pr_ruler_high if friendly_to_xzaratl else pr_ruler')
    # A Trip to the Library
    # Requires post week 8, priority after week 11.
    event('trip_to_library', triggers="week_end", conditions=('week >= 8',), group='ruler_event', run_count=1, priority='pr_ruler_high if week > 11 else pr_ruler')
    # Goblin family dinner
    #Requires that Rowan have talked to Cla-Min about goblins.
    event('goblin_family_dinner', triggers="week_end", conditions=('week >= 4',), group='ruler_event', depends=('learning_about_goblins',), run_count=1, priority=pr_ruler)
    # Problem squad
    # Req at least 10 orc soldiers and morale less than 70%.
    event('problem_squad', triggers="week_end", conditions=('week >= 4', "castle.morale < 70", "castle.buildings['barracks'].troops >= 10"), group='ruler_event', run_count=1, priority=pr_ruler)
    # Poisoned
    event('poisoned', triggers="week_end", conditions=('week >= 4',), group='ruler_event', run_count=1, priority=pr_ruler)
    # Salvaged supplies
    # Requires pre-end of first year.
    event('salvaged_supplies', triggers="week_end", conditions=('44 <= week <= 48',), group='ruler_event', run_count=1, priority=pr_ruler)


label xzaratl_s_advances:
# X'zaratl's advances
# Can trigger three weeks after Dark Sanctum is built, can happen 1 week earlier and is high priority if Rowan was friendly with X'zaratl.

scene bg14 with fade
show rowan necklace neutral at midleft with moveinleft

ro "(Hmm?)"

show xzaratl neutral at edgeleft with moveinleft
hide xzaratl neutral with moveoutleft

ro "(There she is again....)"

show alexia 2 necklace concerned at midright with moveinright

al "Ah Rowan, I need to talk to you. I think someone is stalking me around the castle."

"Rowan ushered his wife down the hallway away from where he'd seen X'zaratl before he answered her."

ro "Was it a strange looking four armed woman?"

show alexia 2 necklace shocked at midright with dissolve

al "Yes!  How did you know?"

ro "She's been following me too. In fact, she's behind us right now."

show alexia 2 necklace concerned at midright with dissolve

al "What does she want with us?"

ro "Given that she's a succubus, I think that's fairly obvious. When I met her, she made her interests in me and any special partner I might have very clear."

al "Oh no!  What should we do?"

ro "(Hmm, she's a powerful sorcerer so a confrontation will be dangerous, but can we really waste the time needed to avoid her?  At least with her weak aptitude for sneaking I know I won't have to worry about either of us getting caught.)"

menu:
    "Confront her now.":
        $ renpy.fix_rollback()
        ro "Since she's probably looking for the right time to ambush us, we best confront her about this now."
        al "Alexia: Alright, if you think that's the best course of action."
        scene black with fade
        label confrontxzaratl:
        scene bg14 with fade
        show alexia 2 necklace concerned at edgeleft with dissolve
        show rowan necklace neutral at midleft with dissolve
        show xzaratl neutral at skorright with dissolve
        xz "How nice to see you again Rowan, is this your wife? You simply must introduce us!"
        ro "Don't act like that X'zaratl. You've been stalking us for most of the day."
        xz "Oh dear, was I that obvious? I've just been hoping to catch the two of you together to make my appearance."
        al "You could have just asked, there was no need to sneak around us like that."
        xz "That's no way to start off a new relationship!  Especially one you want to be as hot, steamy, and deep as I'm hoping to have with you two lovely pets."
        ro "Pets?!"
        "Rowan felt himself becoming very annoyed with the succubus."
        xz "I guess there's no use hiding it. You're such a wonderful couple that I must make you into my sexy little toys. I have a thing for married partners, you see."
        xz "I just get so hard at the thought of joining them under the covers...."
        al "Wait, what?"
        ro "I've had enough of you acting like you already own us!"
        show bg14 with flash
        "The succubus suddenly waved her staff. Magical power shot from it, striking Rowan and Alexia. Neither of them felt any pain, but they were suddenly unable to move or speak."
        xz "Sorry hunny, but I was never going to give you a choice in the matter. Come along pets, let's go somewhere private."
        scene bg9 with fade
        #option to skip?  The player may want to corrupt Rowan and Alexia without seeing the sex scene.
        show xzaratl neutral at skorright with moveinleft
        xz "This your room?  Looks like a lovely place to get well acquainted with one another."
        show rowan necklace neutral at midleft with moveinleft
        show alexia 2 necklace concerned at edgeleft with moveinleft
        "The immobilized couple floated in behind the demoness, even their faces were still frozen in indignation."
        xz "Let us begin by removing these stifling clothes."
        show bg9 with flash
        show rowan necklace naked at midleft with dissolve
        show alexia necklace naked at edgeleft with dissolve
        "She waved her staff again, causing all their garments to teleport a short distance away from their bodies and crumple into a heap. Only the magical amulets remained on Rowan and Alexia."
        "She removed the lower half of her outfit, revealing her mixed sex. Both a male member and female slit. She flourished her hands over them as her shaft became quite erect."
        scene cg35 with fade
        pause 2
        "Then the succubus set her staff and crystal down in the corner of the room and busied herself with removing her corset. As the top fell forward, her perky breasts bounced for a moment now free from restraint."
        show cg36 with dissolve
        pause 2
        "After that, she removed the bottom half of her corset, leaving her long black stockings on."
        show cg37 with dissolve
        pause 2
        "X'zaratl retrieved her staff and spun around on the balls of her feet, causing her endowments to bounce either worryingly or enticingly, depending on your perspective."
        "She smiled at her prisoners, then placed barriers over the door and windows before letting their bodies move again."
        "Rowan knew now that he'd made a mistake in trying to confront the sorcerer. There really was no way for them to escape and if they tried to resist they'd probably be paralysed again, allowing their captor to get off regardless of whether they were willing or not."
        show xzaratl naked behind cg37
        show alexia necklace naked behind cg37
        show rowan necklace naked behind cg37
        xz "Now, I don't want to get between you two lovelies, so which of you will be kind enough to donate their ass while you're enjoying one another?"
        al "What do you mean?"
        "The succubus only smiled and pointed to her very stiff cock and bounced it up and down once more."
        menu:
            "Rowan will be in the middle.":
                $ renpy.fix_rollback()
                "Before Alexia could respond, Rowan stepped forward. This surprised his wife, she wasn't expecting him to protect her like this."
                ro "Me."
                "X'zaratl looked both pleased and intrigued. She took a few steps forward herself to meet the man, running a pair of her hands down his sides."
                xz "Hmmhmm, a man after my own heart. There aren't many who'd give lovely old me their ass so willingly."
                # CG of Rowan being penetrated by X'zaratl
                scene cg64 with fade
                show xzaratl naked behind cg64
                pause 2
                "She turned him around, grabbing his hips with her lower arms firmly before forcing him backwards and impaling Rowan on her cock in one smooth motion. It went in easily, coated in some form of demonic or magical lubrication that the hero hadn't noticed before."
                "Being violated like this sent both a shudder of horror and a wave of pleasure through Rowan's body. In an instant he was under the succubus's more carnal power, letting out a rather unmanly gasp of pleasure as she bottomed out and pressed her breasts into his back."
                "X'zaratl shook her hips side to side with a playful giggle, dragging her shaft in and out along with the movement. Then she turned the man's head to the side for a kiss with one of her upper hands.while crooking a finger to the woman with the other."
                "The aura of sexual energy coming off the succubus was so strong that Alexia felt the cold feeling in her stomach of seeing Rowan kiss another woman fade away. Instead the desire to join them took over."
                scene cg65 with dissolve
                show xzaratl naked behind cg65
                pause 2
                "With the arrival of his wife in front of him, Rowan seemed to instinctively know to lift her body up and guide her down onto his cock. He took her without even breaking the kiss with the sorcerer who had taken him."
                "Although the man had taken his wife many times before, this time felt strangely dirty. Perhaps profane was the word he was looking for?"
                "X'zaratl broke the kiss with a loud smack of her lips."
                xz "Not all that skilled, but there is lust in there. Why don't you show me how you kiss your wife, my lovely? Do it with all your heart, while my taste is still in your mouth!"
                "Still keeping her lower hands firmly holding Rowan's hips, she used the top ones to push Rowan and Alexia's faces together. They did kiss, but it felt hollow. The woman felt like one of the dolls she'd played with as a child."
                "While attempting to please the succubus in his performance, the man also had to contend with the shaft that was now idly pumping in and out of his backend. He felt like a cocksleave, or perhaps just a hand unconciously masterbating it's owner's penis."
                xz "Aww, that's so cute! You two really are the loveliest couple one could ever find."
                "She let them break the kiss, then used her upper arms to embrace Alexia and pull all three of them close together. At the same time she started moving Rowan's hips forward and backwards, forcing him to both fuck his wife but also assfuck himself on her."
                "Sex came naturally to cubi, almost as easy as breathing."
                "With both of the humans under her near complete control, X'zaratl was able to direct the threesome with a practised grace and efficiency."
                "What little wits Rowan had managed to maintain at the start was now gone, overwhelmed by the dual pleasures coming from his lower body. Now he was moaning almost as loudly as Alexia was. There was nothing left but to give himself to X'zaratl completely."
                show cg65 with sshake
                show cg65 with sshake
                scene cg66 with flash
                show xzaratl naked behind cg66
                pause 2
                "The hero let out a loud cry of pleasure as he felt his orgasm crash over him. Rope after rope of his cum sprayed into his wife's passage, which in turn caused her to clamp down on him with her cunt."
                xz "Good boy."
                "X'zaratl rested her head against the back of Rowan's, rubbing him with one hand as fluids flowed into his rectum. The succubus didn't change her pace or seem to grow weaker like he and Alexia did with their orgasms. If anything, filling his ass was making the sorcerer stronger."
                "Only after the last drop was out did the sex finally end. The two humans almost immediately collapsed against one another, but were gently carried over to the bed and laid down in one another's arms."
                scene black with fade
                show xzaratl neutral behind black
                xz "Rest now, we'll do this again sometime soon."
                "The last thing that either of them remembered was being kissed on the lips."
                "They woke up maybe an hour later, still laying naked in each other's arms. X'zaratl and her things were gone, along with the barriers, but Rowan could still feel her jizz leaking out of him."
                #end scene, Rowan and Alexia gain corruption
                $ avatar.base_corruption += 1
                $ all_actors['alexia'].corruption += 1
                $ xzaratl_s_advances_rowan_sex = True
                return
            "Alexia will be in the middle.":
                "After a moment's hesitation, Alexia stepped forward. She didn't check for her husband's approval, nor waited for it."
                al "I guess as the only full woman present, I'm going to be the one in the middle."
                xz "Well, not necessarily. Taking it up the bum can be quite a pleasurable experience for men."
                "The succubus eyed Rowan for a moment before stepping up to Alexia and spinning her around."
                xz "Of course, a lot of them seem to find that act unmanly. It's a real shame, I do so love to play with boys like this."
                show cg38 with fade
                show xzaratl naked behind cg38
                show alexia necklace naked behind cg38
                pause 2
                "She put both of her lower arms on Alexia's hips and lifted the smaller woman up, then down onto her cock in one smooth motion. It went in easily, coated in some form of demonic or magical lubrication that had previously gone unnoticed."
                al "Ah!"
                "There was a sharp gasp from being invaded, though Rowan's wife felt only a mild discomfort. Strangely, she actually felt somewhat empty, like something was missing."
                "The hero himself was finding it somewhat horrifying to see his love being taken like this before him, but that sensation was quickly pushed aside by raw lust as X'zaratl curled a finger to him in invitation while the other upper arm held Alexia's lower folds open."
                "A part of him realized that the demoness was influencing his emotions, but it wasn't strong enough to force her control back. He accepted the invitation, quickly moving forward and pushing his own cock into Alexia's womanly passage."
                show cg39 with fade
                show alexia necklace naked aroused behind cg39
                al "Ahamama..."
                "This time the human woman only whimpered, her eyes rolling back in shock from the sensory overload."
                "Rowan could feel the hardness of X'zaratl's shaft against his, separated only by a few soft walls. He looked past his wife, into her uncovered eye. A grin was what he found."
                xz "Oh dear, looks like we broke her. Aw well, let's see just how many pieces we can shatter her into?"
                "With the guidance of one of her hands, Rowan soon settled into a rhythm of pumping in and own, opposite the succubus. That way, while one was going in, the other was on their way out. The stimulation was certainly having an effect, the noises Alexia was making was proof of that."
                "After that, he was guided to start licking and sucking on one of his wife's nipples while the other upper arm started tweaking and cupping the other breast. In response, the red head's moans soon almost grew into screams."
                "These were quickly muffled by fingers pressed into her mouth by X'zaratl, which Alexia sucked and licked almost instinctively. It was about the only thing she was doing at this point, the rest of her having gone limp from the incredible pleasure of the threesome."
                "Of the two humans, the man was doing quite a bit better as far as keeping his head went. Even still, there was a distinct sensation that he wasn't really in control of himself here. The sorcerer was the one in charge, controlling the two of them like puppets."
                show cg39 with sshake
                show cg39 with sshake
                show cg39 with flash
                show cg40 with dissolve
                pause 2
                "Finally Rowan could take it no more, and found himself unleashing his seed into his wife's passage."
                "This didn't seem to have much of an effect on Alexia, she only continued to give out muffled moans around X'zaratl's fingers as her pussy continued to quiver and clench around her husband's cock."
                xz "Done hunny? I think you did a great job there, I counted no less than four orgasms from your wife! Now, just give me a second..."
                show cg40 with sshake
                show cg40 with sshake
                show cg40 with flash
                show cg41 with dissolve
                pause 2
                "In spite of the increased sensitivity of having just came, Rowan was surprised to find that his hips wouldn't stop moving. Obviously the succubus wasn't going to let him stop until she decided. Thankfully, that wasn't too long."
                xz "...theeeere we go."
                "Only after the last drop was out did the sex finally end. The two humans almost immediately collapsed against one another, but were gently carried over to the bed and laid down in one another's arms."
                scene black with fade
                show xzaratl neutral behind black
                xz "Rest now, we'll do this again sometime soon."
                "The last thing that either of them remembered was being kissed on the lips."
                "They woke up maybe an hour later, still laying naked in each other's arms. X'zaratl and her things were gone, along with the barriers, but Rowan could see the proof of the encounter: both of their jizz leaking out of his wife's holes."
                #end scene.  Rowan and Alexia gain corruption.
                $ avatar.base_corruption += 1
                $ all_actors['alexia'].corruption += 1
                $ xzaratl_s_advances_rowan_sex = True
                return

    "Do whatever it takes to avoid her.":
        $ renpy.fix_rollback()
        ro "We avoid her. It might make it hard to get other work done, but this is where we have the advantage."
        al "Are you sure about that, my love?"
        ro "It shouldn't be that hard for you, for all her magical skill that succubus has no talent for stealth. You certainly needn't worry about me avoid her when needed."
        al "Alright, I trust you."
        #End scene.  Rowan is injured: "distracted at court", gaining -movement points for the next 3 weeks.  Alexia cannot be used as a place-able NPC during that time as well.
        # TODO NPC job restriction
        $ add_effect(MultiEffect('Distracted at court', 'neg', (('mp', -2),), 3))
        return

    "Get help from the twins.":
        $ renpy.fix_rollback()
        ro "We should get help from Jezera. She should be able to get that succubus off our backs."
        al "If you think that's the best thing for us to do."
        scene bg6 with fade
        show rowan necklace neutral at midleft with dissolve
        show alexia 2 necklace neutral at edgeleft with dissolve
        show andras displeased at midright with dissolve
        an "Now what are the two of you looking for?"
        ro "We're seeking your sister. The castle's head sorcerer has decided to try and make us her pets."
        an "I'm sorry, but Jezera is currently out on some business. If you need help with your problems, you'll have to ask me."
        #if Rowan has no favours with Andras
        if all_actors['andras'].favors == 0:
            an "Though I'm afraid that I don't really care about your predicament. As long as X'zaratl doesn't interfere with your work, she can do whatever she wants with you two."
            "He waved a hand dismissively to them, as he walked off."
            an "Deal with her yourselves."
            hide andras with moveoutright
            al "Now what?"
            menu:
                "Confront her.":
                    $ renpy.fix_rollback()
                    jump confrontxzaratl
                "Avoid her.":
                    $ renpy.fix_rollback()
                    ro "We avoid her. It might make it hard to get other work done, but this is where we have the advantage."
                    al "Are you sure about that, my love?"
                    ro "It shouldn't be that hard for you, for all her magical skill that succubus has no talent for stealth. You certainly needn't worry about me avoid her when needed."
                    al "Alright, I trust you."
                    #End scene.  Rowan is injured: "distracted at court", gaining -movement points for the next 3 weeks.  Alexia cannot be used as a place-able NPC during that time as well.
                    # TODO NPC job restriction
                    $ add_effect(MultiEffect('Distracted at court', 'neg', (('mp', -2),), 3))
                    return
        #if Rowan has at least one favour with Andras
        else:
            an "Now normally I wouldn't really care what happened to you, as long as you got your duties finished. However, I'm feeling generous today and might be willing help my playthings deal with their problems for them."
            "He leaned forward, looming over Rowan and placing a hand against the wall behind the man"
            menu:
                "Use a favour with Andras to deal with X'Zaratl":
                    $ renpy.fix_rollback()
                    ro "Please help us, master."
                    an "Very well, I'll have a little talk so you needn't worry about that naughty woman bothering you anymore. After all, I can't have her messing with my playthings, can I?"
                    hide andras with moveoutright
                    al "I suppose it's better to be that man's toy rather than the entire castle's."
                    #-1 favour with Andras, end scene.
                    $ change_favor('andras', -1)
                    return
                "Confront her yourself.":
                    $ renpy.fix_rollback()
                    ro "Fine, we'll deal with this ourselves."
                    an "Maybe you do have some spine? Good luck!"
                    hide andras with moveoutright
                    al "Rowan?"
                    jump confrontxzaratl
                "Forget Andras's help and avoid the succubus instead.":
                    $ renpy.fix_rollback()
                    ro "Fine, we'll deal with this ourselves."
                    an "Maybe you do have some spine? Good luck!"
                    hide andras with moveoutright
                    al "Rowan?"
                    ro "We avoid her. It might make it hard to get other work done, but this is where we have the advantage."
                    al "Are you sure about that, my love?"
                    ro "It shouldn't be that hard for you, for all her magical skill that succubus has no talent for stealth. You certainly needn't worry about me avoid her when needed."
                    al "Alright, I trust you."
                    #End scene.  Rowan is injured: "distracted at court", gaining -movement points for the next 3 weeks.  Alexia cannot be used as a place-able NPC during that time as well.
                    # TODO NPC job restriction
                    $ add_effect(MultiEffect('Distracted at court', 'neg', (('mp', -2),), 3))
                    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label trip_to_library:
# A Trip to the Library
# Requires post week 8, priority after week 11.

scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show alexia 2 necklace neutral at midleft with moveinleft

cl "Ah Alexia, hello. Haven’t seen you in here for a while."

"Despite the arrival of the other woman, the sorceress did not look up from the tome on the desk before her, continuing to study intently whatever was contained between its covers."

al "Yes, I meant to visit sooner, but things have been a bit hectic since Rowan appeared and I haven’t had as much as free time as I did before."

cl "I was beginning to think that you had lost interest in our little collection."

al "Oh no! I love reading."

cl "Glad to hear it. It is nice to know there’s a least one other person in this castle who isn’t an ignorant savage."
cl "There’s hundreds of years of knowledge in this library, some of it lost to the rest of the world, and most of these books look like they have never been touched. "

"The librarian let out a loud sigh and closed the book in front of her."

cl "Anyway, how can I help you today?"

show alexia 2 necklace look away at midleft with dissolve

"The directness of her question seemed to set Alexia back a little, who looked down at the floor as she replied."

al "Well, I’ve been in this castle for months now, and to be honest I don’t know anything about it...."

cl "Hmmm?"

al "...or the people who inhabited it, and I was just wondering, if, maybe, somewhere…"

cl "Yes?"

al " ...there might be some books in the library about that sort of thing?"

cl "If it is information about the castle itself that you are interested in, you’d do better talking to Skordred instead, as he was originally involved with its construction. He’ll probably know more about it than any book that I have here."
cl "As for its inhabitants, there are no books on the twins themselves, but if it is knowledge of their line you are after, you might try demonology, aisle 67 on the left."

show alexia 2 necklace happy at midleft with dissolve

al "Oh, thank you."

cl "I’d take you myself, but I have a lot of work that needs to be done."

al "No, I’m sorry for taking up so much of your time."

cl "It is quite alright. If you will excuse me…"

"The blonde reopened the book on her desk and returned to whatever it was that she had been studying before the other woman had arrived. Armed with the knowledge of where she might find the book that she sought, Alexia headed off deeper into the library."

scene black with fade
scene bg12 with fade

"While she had spent quite a bit of time exploring the place when she had been a prisoner of the twins before being reunited with her husband, Alexia had never been this far into the library before."
"It took her longer than she thought it would to reach her destination as all the aisles began to look similar, and some of them seemed to be endless. Eventually, almost an hour after she had left the librarian at the desk, she stood before the demonology section."

show alexia 2 necklace neutral at midleft with dissolve

"Cliohna had elected not to mention how large it was. Nor that, as far as Alexia could see, any of the books had been written in any sort of language that she was able to recognize."
"One book stuck out from the others. It was large and bound in some sort of thick brown material that had begun to crack with age. She ran her finger over the strange gold symbols that adorned its spine, and it was thick with dust as the librarian had earlier lamented. "

show andras smirk behind bg12

an "I wouldn’t touch that one, if I were you."

show alexia 2 necklace shocked at midleft with dissolve
pause 1
show alexia 2 necklace neutral at midleft with dissolve

al "Oh, Andras! You scared me."

hide andras
show andras happy at midright with dissolve

an "Azar’s {i}Theologica Demonica{/i}, written after the mage was driven mad by his attempts to see beyond the veil into the Outer Dark, and bound in the flesh of his disciples."

"The woman withdrew her hand in disgust."

al "That’s… That’s…"

show alexia 2 necklace shocked at midleft with dissolve

al "How vile!"

show alexia 2 necklace neutral at midleft with dissolve

an "True. All humans who foolishly think that they can harness the power of chaos end up changed by the experience, more often than not in horrifying ways. That is, if they even survive."
an "It is seductive none the less though, as you can attest to."

"Terrifying as it was, the demon was right. There was no denying that she had felt drawn to the one book alone among all the others, and even now, having learned what she had, she still seemed unable to take her eyes off it."

an "Don’t worry, that book isn’t for you. I think you’ll find this one a lot more helpful."

if andras_alexia_sex == True:
    "The demon came and stood behind her in front of stack she was currently perusing. This is the closest she had been to him since the event that occurred a few weeks ago."
    "The return of her husband, as well as Andras’ actions, had made it easy for her to avoid him, but now there was nowhere for her to go."
    "He leaned forward to take something from the very top shelf, bring his front into contact with the woman’s back. She could feel the demon’s cock, still huge despite its currently dormant state, press against the small of her back."
    "The sensation caused her to grow flush, as flashes of memory came back to her; the waves of pleasure she had felt when he had used her so roughly. But was her redness shame at the way in which her body had betrayed her, or arousal?"
    "Using what was left of her willpower, she broke contact from Andras, pushing herself flat against the shelves before her. As she did, the demon, who had clearly been lingering, brought down another dusty old tome from the shelf."
    "While this one was different, bound in red leather and gilded with gold, the runes on the cover were just as indecipherable as all the rest."

else:
    "The demon came and stood behind her in front of stack she was currently perusing. He leaned forward to try and take something from the very top shelf, but Alexia was too smart to allow him to trap her this way."
    "Leaning flat against the shelves in front of her, she was able to avoid his obvious attempt at forcing contact."
    "More amused than angry at the human’s evasive tactic, he brought down what he had been reaching for, another dusty old tome from the shelf."
    "While this one was different, bound in red leather and gilded with gold, the runes on the cover were just as indecipherable as all the rest."

an "I think you will find that this is more along of the lines of what you were looking for."

"He took a step back and handed the book to her. It was surprisingly heavy for its size, and she almost dropped it when she took it from him. She cracked open to discover the book was filled with more of the strange language that she had seen on the cover."
"As she flipped through the pages, she discovered it also contained illustrations."

al "Andras, these images…."

"The book was filled with depictions of violence and lewd acts that shocked the human woman to her very core. She slammed it closed, and held it out to return it to the demon who had given it to her."

show alexia 2 necklace angry at midleft with dissolve

al "This is not something suitable to give to a woman!"

an "You wanted to learn about demons, and those are the things that demons do."

show alexia 2 necklace neutral at midleft with dissolve

al "Even so, I can’t understand a single word in it."

an "Take it to my sister, she’ll be more than happy to help with reading it."

"Alexia was torn as she looked at the book in her hands. What lay between its covers disturbed her, but there was a chance it could contain information that would be useful. That would be worth the potential risk, surely?"

al "I’ll… think on it. Thank you, Andras."

an "Think nothing of it, and if you need any more suggestions about books, you only have to ask."

hide alexia with moveoutleft
show andras smirk with dissolve
pause 2
# activate "the_demonic_tome" with a timer
$ activate_event('the_demonic_tome')
$ set_event_timer('the_demonic_tome', 'after_trip_to_library', dice(3)+3)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label goblin_family_dinner:
# Goblin family dinner
#Requires that Rowan have talked to Cla-Min about goblins.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

ro "There, done."

"The hero let out a long sigh of relief. He was finished his duties for the day and would have the evening off before he had to go out again on his weekly scouting mission."
"He might still do some last minute decisions for construction or purchases, but the stuff that actually took up his time was done."

show clamin happy at midright with moveinright

cla "Rowan! How nice to see you're finished in time for a little dinner I've been putting together for you."

ro "No, you've been hiding behind that pillar for almost an hour waiting for me to finish."

cla "Oh don't be silly, why would I ever do that?"

ro "You also tried to catch me for breakfast and then lunch. You've been trying all day to get me to come to this family dinner."

# Cla-Min looks shocked.

cla "How? I thought..."

#Cla-Min smiles.

cla "Well, if you hadn't seen though a trick like that, I suppose you wouldn't be much of a hero for my people, would you?"
cla "Still, I do hope that you'll grace us with your sly presence. I really did put a lot of work into this, just for you."

show rowan necklace happy at midleft with dissolve

"Rowan rose from his work table, looking somewhat exasperated but also smiling."

ro "Alright, let's go meet your family."

"The goblin matriarch bounded up to him excitedly and grabbed his hand. She tried to drag him back to her caravan, but the difference in size and weight meant that in the end she was forced to just lead."

# Transition, show first CG.  Table inside a large wagon with Cla-Min's immediate family in the image.
scene black with fade
show clamin happy behind black
show rowan necklace happy behind black

"As Rowan was ushered inside the wagon, he found he had to stoop slightly to avoid banging his head on the ceiling. Made sense, goblins didn't need as much headspace as humans. What was more surprising was the number of them crowded around the table."
"There were a dozen of them, of various ages. Excited whispering broke out among them while the hero was led to a cushion on the floor, the rest of them were sitting on small chairs, but the table was too low for a human to sit on one of those comfortably."
"He was seated next to Cla-Min herself, with a vibrant male goblin about the same age as her on the other side."
"Like nearly all of the female goblins at the table, that one was also eyeing him in a rather suggestive way. Rowan's attention was drawn away as his host started introducing everyone at the table."

cla "That's my paw, Cla-Sty. On your left is my twin brother Cla-sty, followed by my younger brother Cla-Sel. Those two lovely things are my sisters Cla-Tre and Cla-Owi. Ver-Tod here is my favored mate and his sister Ver-Min is visiting with us tonight."
cla "Then you have my wonderful children, my youngest twin boys: Cla-Kes and Cla-Lij. Plus my older triplets: Cla-Sty, Cla-Tod, and Cla-Min."

"The last was a young woman, notably as the only goblin at the table that hadn't met Rowan's eyes. She was a very cute little thing, and obviously quite shy towards the hero for some reason."

cla "Everyone, this is the great hero Rowan!"

"The room exploded into excited chatter, making it impossible for Rowan to pick out what was being said by pretty much everyone there.  Instead, he turned to Cla-Min to ask her a question."

ro "So your daughter has the same name as you?"

cla "Yeah, I think I told you that Min was a very common goblin name, there's three of us here at this table! Just call her Min if you have trouble with the names, she'll know you're talking to her."

"Evidently deciding that was enough gossiping for the moment, the matriarch clapped her hands together to get everyone's attention and the chorus of voices quickly died off."

cla "Boys, please bring out the food. Let's show our guest a good time!"

"Her four sons quickly jumped up and rushed out of the room. They returned shortly afterwards with steaming pots and placed them on the table."

# CG, Rowan sitting at the table with Cla-Min on one side and a male goblin on the other, both "putting the moves" on Rowan.  Their plates have meat and nuts on them.
scene cg311 with fade
show clamin happy behind cg311
show rowan necklace happy behind cg311
pause 3

"The meal served was roasted meat and nuts. For the most part game and forage, but some of it obviously would have been traded for. Goblins could eat most things, but they really liked meat with bite sized bones and anything that had a good crunch to it."
"They were also fond of fresh blood, which was also served (probably from the same animals that supplied the meat), though Rowan passed on that."
"At first Rowan was the only one that anyone wanted to hear about. The family here wanted to hear all about their hero's goblin-like traits, famous tricks and feats of dexterity for the most part. It was interesting to learn which parts of his tales were the most famous from their perspective."
"He just wished that they didn't get annoyed at him everytime he mentioned anything that sounded heroic or honorable. This audience didn't like to hear that their ideal trickster had a goody two-shoes human scum side to him."
"Eventually the group shifted to small talk and several smaller conversations sprang up around the table."
"For the most part they discussed either the food or their latest trading operations. Before being pulled into one such talk himself, Rowan noted that these caravaners had been putting their access Jezera's portals to good use."
"Min was the only one at the table that didn't seem to have anything to say, always looking down shyly and only raising her head to steal glances at Rowan when she thought he wasn't looking at her."
"That girl almost certainly had a crush on him, the hero was fairly certain, but then he got distracted by her mother."

cla "So what do you think of my little family?"

ro "They're a lively bunch. I haven't seen too many goblin families before, but this does feel like a home. For all your talk of schemes and tricks, you all trust and love one another."

"The matriarch puffed up with an air of pride about her."

cla "Yes, family is a wonderful thing. It's one thing that we caravaners have learned about from the other races. I wouldn't trade any of my children or relatives here for anyone."

"She took Rowan's right hand, making him glance down in surprise. When he looked back up, he saw that she was giving him a very meaningful look."

cla "There's a place for you here too, if you'll join us. We goblins don't practise monogamy you see and are quite willing to invite anyone worthy into our ranks."

# to be added when we have cla-bow sprite
#"Rowan looked around, trying to find something to turn the conversation away from that direction. He found Cla-Bow on his other side who was watching them with interest."
#ro "What about you, Cla-Bow, have you got any children or another goblin family that you're away from tonight?"
#Cla-Bow: Nah, never been one for girls myself, last I checked you need those to make kids.  Handsome men like yourself have always been my thing.
# Now he took the man's left hand while flashing a big toothy grin!  Trapped between the two, with both hands held, one final shock was given as someone started to undo Rowan's pants!

"Cla-Bow, the goblin on his left, also made his interest in Rowan quite obvious, taking his hand. Trapped between the two, with both hands held, one final shock was given as someone started to undo Rowan's pants!"
"His gaze shot downwards and discovered the shy goblin girl, Min, was currently working at his pants with a look of reverence and her tongue hanging out. Was she about to... wait, had this entire dinner been a setup for this?"

menu:
# Choice:
    # "Receive a blowjob from Min."
    "Receive a blowjob from Min.":
        # Jump to Min's blowjob.
        jump .mins_blowjob

    # "Stop the girl."
    "Stop the girl.":
        "He shook his hands free from the two goblins on either side of him and pushed the young woman between his legs away from him."
        "This actually shocked the girl, and she intentionally made eye contact with Rowan for the first time this evening with a pleading look. Before he had a chance to say or do anything more, her mother placed her hands on his arm again and spoke softly into his ear."
        cla "Please accept our hospitality. My family is very eager to make you feel welcome in every way we can, especially my darling Min."
        "Rowan looked to meet the shy goblin's gaze once more, however she was looking at his pants again, lips slightly parted and pushing against his grip. Evidently she really did want him."
        menu:
            # Choice: "Give in and let Min blow you."
            "Give in and let Min blow you.":
                # Jump to Min's blowjob.
                jump .mins_blowjob
            # Choice: "No means no."
            "No means no.":
                "There was a final shake of his head, at which point Cla-Min relented and shooed her daughter away. The younger Min was obviously disappointed, but did as she was told."
                "The so-called goblin hero turned to apologize for rejecting this advance, but hesitated when he saw that Cla-Min was smiling conspiratorially at him."
                cla "Don't worry, next time I'll get you into my family for sure!"
                "With that, she returned to her meal and acted like nothing had happened."
                # Jump to meal ending.
                jump .meal_ending

label .mins_blowjob:
#Min's blowjob
# CG, under the table, Rowan being blown by a female goblin, Cla-Min's foot is giving direction.  Also cum variation.
$ goblin_family_dinner_mins_blowjob = True

scene cg94 with fade
show clamin happy behind cg94
show rowan necklace happy behind cg94
pause 3

"No resistance was given as the goblin girl undid his trousers and pulled them apart, allowing the man's cock to flop free. Rowan glanced around hurriedly to see if anyone was looking at him, though no one was paying any attention anymore except for Cla-Min and Cla-Bow."

"Evidently these two were in on it, what with all the holding his arms back so he didn't interfere with Min, who was now eagerly licking his semi-erect member."
"He started when she poked a finger underneath him and invaded his rear, though he couldn't do anything about it between not wanting to alert the table and being somewhat tied up."

cla "I must say Rowan, that there would be no human more worthy to join my family than you."

ro "Sorry, what was that?"

"He sharply inhaled as the younger Min opened wide and stuffed her face with his manhood, taking it up to the hilt with a single motion."

cla "Everyone here would be eager to have you join us anytime, in any way! Well, at least there'd always be someone who's willing to take you in whatever way you want."

"It was difficult to concentrate on what the matriarch was saying, being distracted two ways from trying to focus on both what was going on between Rowan's legs and what the girl's mother was saying."

ro "Well, that's a very nice offer of yours."

"Min began to bob her head up and down while also curling her finger that was embedded in him, trying to find something...."

cla "Of course! If you need someone on top of you, I'm your girl. If you're after some male company, Cla-Bow here has you covered. Min, when she decides to show her face again..."

"Cla-Min winked to Rowan."

cla "...I'm sure she'll eat up anything you need to get out of you."

"Rowan tried to shift in his seat, and was rewarded with a whining sound from under the table as the girl blowing him tried to keep him planted exactly where he was."
"He looked down, and was surprised to find that Cla-Min actually had a foot on her daughter's head, directing her movements!"

cla "We're a talented bunch, with a great matriarch and teacher. So just think of how much more we'll be with you in our numbers? Maybe our children can be even greater with such an amazing hero in their ancestry."

scene cg94 with sshake
scene cg94 with sshake
scene cg95 with flash
show clamin happy behind cg95
show rowan necklace happy behind cg95
pause 3

"A sudden jolt of pleasure flooded through Rowan's body as Min found what she was evidently looking for in his ass, which then sent him into the throws of orgasm. As he did so, Min's head dropped down to the hilt again and he came directly into her throat."
"She seemed to hum contentedly as he sputtered in her, the vibration adding something that the man had never felt before. This girl was quite good at giving blowjobs."
"Her skill was such that she never coughed or gasped when she finally pulled back off of him and retreated back to her side of the table."

# Rowan at the dinner table CG again.
scene black with fade
show clamin happy behind black
show rowan necklace happy behind black

cla "What do you think Rowan, will you join the Cla family? I'll make certain that you never regret it."

ro "I- wait, no I have a family. Alexia is-"

cla "She can join too! It's not a problem at all, just so long as she doesn't hog you all to herself."

"Rowan only frowned and pulled back, trying to collect himself again. However the goblin didn't seem to be taken aback at all, instead smiling conspiratorially."

cla "It's fine if you need a little time before you make the jump. It is a big life choice after all. Just remember that your goblin family is here, waiting for you."

"The conversation seemed to just end there, leaving Rowan feeling somewhat overwhelmed. This was, without a doubt, the strangest way of securing a mate he'd ever encountered."

# Jump to meal ending

label .meal_ending:
# Meal ending
"The rest of the evening was blessedly uneventful. While this was by no means a standard meal by human standards, Rowan had dined at the tables of many different races and was reasonably comfortable with unusual hosts or guests."
"Eventually he excused himself, and left the wagon to a chorus of happy goodbyes and questions of when he'd be joining them again."
"He took with him a bowl of deep fried potato wedges, intending to share some of the crispy things with Alexia. The thing he was most happy to leave behind was the annoying grinding sound from goblins gnawing on bones."
"Just thinking about it made him shudder. That was one thing that would be haunting his nightmares from now on."

$ activate_event("clamin_bribing_proposition")
$ set_event_timer('clamin_bribing_proposition', 'after_family_dinner', 3)
# End scene
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label problem_squad:
# Problem squad
# Req at least 10 orc soldiers and morale less than 70%.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

ro "So this is all of them?"

os "Yes lord."

"Rowan surveyed the group. There were five of the orcs, four men, one slightly bigger than the others who'd become their leader, plus a woman."
"This group had become dissatisfied with serving in Andras's armies and were causing trouble now. They wanted better beds, better food, better everything. Even giving them the smallest of concessions had only made things far worse."
"Now the steward had to decide what to do with them.  Their troublemaking could no longer be ignored."

menu:
    # Choice: "Challenge the leader to a duel." - Req lv 1 Arena.
    "Challenge the leader to a duel." if castle.buildings['arena'].lvl >= 1:
        "It was time to deal with this problem in the traditional orc fashion, that would definitely get through to them. He stood and pointed at the leader."
        ro "It's time to see if you're worthy of everything you think you deserve. A duel to the death! Prepare yourself, we will soon face one another in the arena!"
        "All the orcs in the chamber erupted into guttural cheers, with one exception. The leader, who stared daggers to the man."
        # arena background.
        scene black with fade
        show rowan necklace neutral at midleft with moveinleft
        show orc soldier neutral at midright with moveinright
        play sound "music/SFX/sword_draw.ogg"
        pause 1
        play sound "music/SFX/orc_attack.ogg"
        pause 1.5
        play sound "music/SFX/sword_hit_1.ogg"
        show black with sshake
        pause 0.3
        play sound "music/SFX/sword_hit_2.ogg"
        show black with sshake
        pause 0.3
        play sound "music/SFX/sword_hit_3.ogg"
        show black with sshake
        pause 0.3
        "An hour later, the two fought one another in the arena. The battle was fierce, though the ending was not in doubt for Rowan. This orc was sloppy, poorly trained. He'd actively avoided learning how to fight, resenting the entire military system."
        os "Rawrg!"
        "Suddenly he dived forward, throwing himself entirely into a massive frontal attack."
        ro "(Idiot.)"
        "That move had left the orc complete exposed, allowing Rowan to easily duck forward and cut into the orc's chest, piercing its heart."
        show black with redflash
        "However much to Rowan's shock, this didn't disable the orc, instead it continued is attack and brought down all its strength into one final attack on the man. Apparently it never expected to actually win the duel, just wanted to hurt him!"
        #rowan hurt
        ro "Argh!"
        "He screamed in pain, desperately wrenching himself to the side before his entire body was torn in half. He nearly lost an arm in the process, but managed to get free of the mighty attack as the orc's blow hit the ground, then his broken heart finally caught up with him and he dropped to the ground unmoving."
        "Grunting with supreme effort, the hero stood up and raised his sword triumphantly above his head as the crowd of soldiers around him roared."
        # //End scene, Rowan is injured, -1 orc soldier, + morale.
        $ add_effect(Injury('Wound', 'strength', -2))
        $ castle.buildings['barracks'].troops -= 1
        $ castle.morale += 1
        return

    # Choice: "Fire them."
    "Fire them.":
        "It was time to cut this troublesome lot free."
        ro "You're fired.  The whole lot of you. If you can't follow orders or manage with the accommodations we give you, then you have no place in this army."
        "This seemed to startle the troublemakers and they glanced around between one another in confusion."
        ro "Get out of my sight."
        scene bg14 with fade
        show orc soldier neutral at midleft
        show andras displeased behind bg14
        "The group was lead away from the throne room and towards the castle entrance. Instantly the leader started loudly complaining that this couldn't be done, he was too important to Andras's armies and that the demon would not be happy about this."
        an "What was it that I wouldn't be happy about?"
        hide andras
        show andras displeased at midright with moveinright
        os "Uh, that yous wouldn't be happy about us being fired?"
        an "No, of course not."
        show andras smirk at midright with dissolve
        #stab SFX
        show bg14 with redflash
        hide orc soldier with dissolve
        play sound "music/SFX/BodyfallDirt.ogg"
        "With several quick motions, he blasted the group of five with bolts of demonic energy, killing all of them almost instantly."
        an "You should have been executed instead."
        # End scene.  -5 orc soldiers.
        $ castle.buildings['barracks'].troops -= 5
        return

    # Choice: "Force them into hard labor."
    "Force them into hard labor.":
        "Well, if they couldn't be soldiers at least there'd be another use for them."
        ro "The punishment for your transgressions will be hard labor. You five will become slaves and work in mines or as builders."
        "A collective sound of quiet outrage sounded not only from the troublemakers, but also from several of the other orcs in the room. Apparently this wasn't a popular sentence."
        ro "That's enough, the decision has been made.  Take them away."
        scene black with fade
        "It was done in spite of the complaints, though Rowan feared that the benefits might be outweighed by the decent his decision had caused."
        # End scene.  -5 orc soldiers, - morale, + treasury.
        $ castle.buildings['barracks'].troops -= 5
        $ change_treasury(50)
        $ castle.morale -= 1
        return

    # Choice: "Turn them over to the cubi sorcerers." - Req lv 1 Dark Sanctum.
    "Turn them over to the cubi sorcerers." if castle.buildings['sanctum'].lvl >= 1:
        "Well, if they couldn't be soldiers at least there'd be another use for them."
        ro "Those who will not fight in the armies will be used for other things. You five will be turned over to the cubies, to assist them in their research."
        "A collective sound of quiet outrage sounded not only from the troublemakers, but also from several of the other orcs in the room. Apparently this wasn't a popular sentence."
        "The one person who seemed to be happy was the succubus who'd been in attendance. Already she was dancing around what she called her new 'toys' with no small amount of glee."
        ro "That's enough, the decision has been made. Take them away."
        scene black with fade
        "It was done in spite of the complaints, though Rowan feared that the benefits might be outweighed by the decent his decision had caused."
        # End scene.  -5 orc soldiers, - morale, + one time research points.
        $ castle.buildings['barracks'].troops -= 5
        $ castle.morale -= 1
        $ castle.rp += 5
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label poisoned:
# Poisoned

show bg14 with fade

#ill rowan

show rowan necklace neutral at midleft with dissolve

ro "Ugh, what?"

show bg14 with sshake

ro "(My head is spinning...)"

show bg14 with sshake
hide rowan with dissolve
play sound "music/SFX/BodyfallDirt.ogg"

# If Alexia is pure
if all_actors['alexia'].corruption < 10:
    show alexia 2 necklace concerned at midright with moveinright
    al "Rowan?  What's wrong!?"

scene bg9 with fade
show rowan necklace naked behind bg9
show jezera neutral at midright with dissolve

ro "Hmm?"

show jezera happy at midright with dissolve

je "Ah good, you've awakened. I'm glad to see the initial shock has worn off."

ro "What happened?"

je "One of the castle staff tried to poison you with your lunch. I've taken care of them and will be more careful about hiring such potential problems in the future."

ro "What do you mean?"

show jezera neutral at midright with dissolve

je "That isn't your concern, just focus on your duties once you've recovered enough to continue. Your senses will probably be dulled from the after effects of the poison, but there hasn't been any permanent damage."

hide jezera with moveoutright

ro "Right."

# If Alexia is pure
if all_actors['alexia'].corruption < 10:
    show alexia 2 necklace happy at midright with moveinright

    al "Oh thank goodness, you're alright."

# End scene. Rowan is injured, -int for 3 weeks.
$ add_effect(Injury('Poison after effects', 'intelligence', -2, 3))
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label salvaged_supplies:
# Salvaged supplies
# Requires pre-end of first year.

# Show workshop background (throne room for now)

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show skordred neutral at skorright with dissolve

sk "...musta been a hidden storeroom or a section that caved in during the attack. We found a few others like it before you became steward."

"The hero nodded, watching the builders bring in the supplies that they'd found under the castle while doing salvage work for materials."

sk "It isn't much, but given the state of things, every bit we can find counts."

ro "No, your men did well here. With all the unexpected expenses and setbacks, this will do much to bring us back on schedule. Is this enough to accelerate your projects or start a new one?"

sk "Aye. Give the word and I'll begin within the hour."

menu:
    # Choice: Sell the materials for 25 gold.
    "Sell the materials for 25 gold.":
        $ change_treasury(25)
        #gain 25 gold

    # Choice: Use the materials to accelerate current construction (Building/upgrade finishes instantly and trigger the event for that right after this one, if we change them to have time requirements.  Otherwise ignore this choice, also ignore it if nothing is currently being built or upgraded.)

    # Choice: Use the materials for a new project (Discount of 75 gold on next upgrade or building started)
    "Use the materials for a new project":
        # TODO discount for next project
        pass

sk "Understood... boss.  Thar was one other thing."

"After a moment's hesitation, the dwarf reluctantly handed Rowan a package."

sk "We also found this. As much as it pains me to offer it directly to you, I figured that it would be best for the masters if you had it."

# Rowan gets a free random piece of equipment.
$ get_rnd_item(0, 200)
# End scene.
return
