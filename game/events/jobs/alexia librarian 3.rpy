init python:
    
    event('magic_bookshelf', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    

label magic_bookshelf:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"Alexia pushed her cart through the dark part of the library. The low ceiling and distance from the windows made it into almost an alcove. The only visibility came from torchlight."

pot "Girl. Over here. Girl."

"Alexia blinked twice. Was someone speaking to her? She looked around, but the room was empty."

pot "No. Don’t turn around again. I’m right over here."

al "Where are you? I can’t see you."

pot "The bookshelf, girl. The bookshelf."

"Suddenly, a bookshelf on the far right went crazy. Books started popping out and then jumping back in with no indication that anyone had touched them. Alexia approached slowly."

al "You’re...the bookshelf?"

pot "Correct in spirit if not in nomenclature. Once upon a time, I was called the Prince of Tomes."

$ potName = "Prince of Tomes"

"Alexia cocked an eyebrow. Hardly the weirdest thing she’d found in the castle so far."

al "That’s a pretty fancy name for a bookshelf. "

"She brushed her hand over the spine of the books. They were all old and dusty. Indeed, it didn’t look like anyone had taken any of the books off the shelf for many years. Just how old was this creature?"

pot "I’ve resided here for many hundreds of years. The first demon lord to make use of my mighty talents was Azerion the Dread. The works I carry are timeless."

#alexia shocked
al "How did you-"

pot "Know what you are thinking? Reading is a talent of mine. The human mind is as obvious as words on the page."

"Alexia drew her hand back. How had it done that? Could it see her? Was it able to read thoughts? She almost waited to answer to her own internal monologue, but if the bookshelf really did know what she was thinking, it didn’t reveal it."

al "So, “Prince of Tomes”, what is it you want with me exactly?"

pot "Entertainment mostly. It’s so rare to see a human girl working this segment of the Bloodmeen library."

if all_actors['alexia'].corruption < 60:
    pot "Rarer still one so innocent. This castle has such a way of disposing with that virtue."

else:
    pass
    
#alexia neutral
pot "I think we could establish a mutually beneficial relationship. You’re new to this world, yes? The works on my shelves are full of knowledge. Knowledge that one trapped in your position might find valuable."
pot "And I need a way to pass the time. What good is a collection of books that is never read? I want to fulfill my purpose."

"Alexia took a step back, crossing her arms over her chest. Part of the benefits of working in the library was all the reading material. Furthermore, Cliohna didn’t seem much interested in recommending her reading material of value in her situation."

if all_actors['alexia'].corruption > 50:
    "he squinted slightly. What mysteries did the books contain? Perhaps there would be something of value in their pages…"

elif all_actors['alexia'].corruption > 70:
    "Alexia briefly flashed a grin. What dark mysteries must be contained on the pages of the books. Powerful and valuable insights...perhaps something a bit more erotic..."
    
else:
    pass
    
"But, it wasn’t like she needed to be told that the bookshelf could just be lying. It was clearly magic. Who knew what curses could be on it."

if alexia_and_her_demon_book > 0:
    "Alexia knew full well what kind of malice evil books were capable of from first hand experience."
    
else:
    pass
    
pot "What do you say? I know just the book for you. I always know what books people are looking for, even if they do not know it."

"One of the books on the shelf suddenly pushed outward, standing out amidst the rest."

menu:
    "Take the book.":
        $ released_fix_rollback()
        jump potTakeBook
        
    "Keep on walking.":
        $ released_fix_rollback()
        "Alexia stared at the book in silence for a moment before she shook her head. This was a trap. It almost had a glowing sign declaring as much. Alexia had not been in this castle for more than a year without coming to understand how dangerous trusting anything here was."
        "She went back to her cart and started to push it back into the light segment of the library."
        pot "Wait. Come back."
        al "Not today, bookshelf. Maybe another time."
        "She kept about her rounds for the day, making sure the library was in the proper condition. Every so often she’d glance back at the darkened corner where she knew the creature was no doubt observing her."
        return        
        
label potTakeBook:

"Alexia put her hand on the book extending from the shelf. It felt normal enough."

al "And there are no charms on this book? No curses or anything?"

pot "It is but a normal book. You have my word. No doubt you can understand how important my word is to one such as myself."

"Alexia sighed. There was no harm in a bit of reading. Besides, this creature seemed to suggest this book to her specifically. Perhaps there was a reason for it."
"She grabbed the book and put it on her cart. If the Prince of Tomes had a reaction, it did not show it."
"Shortly afterwards, was her normal break time. Alexia found a quiet corner of the room, far away both from the mistress of the library and the strange bookshelf. There she opened the book to a random page."

if all_actors['alexia'].flags['jezera_influence'] > 5 and all_actors['alexia'].relation < 30:
    scene cg250 with fade
    pause 3
    "The book was about the culture and secret practices of the dark elves. Even a cursory glance proved that it had the sorts of information that no conventional human book would ever have. This might be useful. Alexia dug into the pages."
    "{i}The third high elf reconciliation mission was led by a male named Fargut. Fargut’s plan was to offer Queen Varyn and Queen Maieria plots of forest near the banks of the river Anurillindill. {/i}"
    "{i}The twin offer was designed to exclude Queen Arrania. This was part of Fargut’s plan of division, however it would later prove to be the doom of the proposal, when…{/i}"
    "Alexia skimmed around more, reading through various segments. Much of it was dry details of history that might have been recorded elsewhere. She kept on searching for the secret details of Dark Elven society."
    "Then she opened the book to a fascinating segment... "
    "{i}A portion of the captured human women, the most beautiful portion, are taken by Queens, High Nobles, and those instrumental in their capture. They are to become Tongue Girls, eternal servants of their dark mistresses.{/i}"
    "{i}Before the litany of spells can be applied, the first step is to wear down the resistance of the captives. Consent empowers the spells, for the strongest chains are those self forged.{/i}"
    "{i}Future Tongue Girls are kept in seclusion in the dark. They must be taught not to expect the light. The only food they are given are from the Fruits of the Underground Skenia tree. It’s addictive flavor has been long attested too. {/i}"
    "{i}The Skenia fruit take on the flavor of the first liquid they contact. When put to the taste of the Tongue Girl’s future Mistress, they replicate their taste exactly. Tongue Girls are conditioned to their Owner from afar.{/i}"
    "{i}The key test to decide if a Tongue Girl is ready the trial of binding. A conventional blindfold is used and they are taken from their cell for the first time. There they are presented with the naked body of their Mistress and four of her servants.{/i}"
    "{i}A future Tongue Girl is expected to use her mouth to bring pleasure to each of the five. Failure to do so is met with severe consequences. At the conclusion, she is to be given the test of selection. She must identify her Mistress by the flavor.{/i}"
    "{i}If the Tongue Girl fails, she is to be taken back to her cell and her diet of Skenia fruit is resumed. If she succeeds, it means she has accepted her Mistress’ unique flavor, and the next stage of her training can begin. {/i}"
    "{i}That involves-{/i}"
    #alexia aroused
    "Alexia slammed the book shut in a hurry. She’d been so lost in the passage she hadn’t even been paying attention."
    if all_actors['alexia'].corruption > 50:
        "There was no other word for what she had been reading besides depraved. She had not finished the passage, but the meaning of the name “Tongue Girl” was hard to miss."
    elif all_actors['alexia'].corruption > 70:
        "Alexia bit her lip. The talk of Tongue Girls didn’t go into nearly enough detail, but what had been described was so depraved...sexy…"
    else:
        pass
    $ change_actor_num_flag('alexia', 'jezera_influence', 3)
    jump potResolution

elif all_actors['alexia'].flags['andras_influence'] > 5 and all_actors['alexia'].relation < 30:
    scene cg251 with fade
    pause 3
    "The book was about a human knight named Eleanor, the woman who’d popularized the name. She’d been Solansia’s campion in a war vs the Demon King Nekolio more than 400 years before. The first time a human champion of Solansia had emerged since ancient days."
    "Alexia knew her story. It was very common in Rosaria. But, there was nothing wrong with looking at it again. After all, this was the work of an author in Bloodmeen. In the known story, she vanished in the last battle on Rosarian soil. Her fate was considered something of a mystery."
    "She opened the book to the segment after the battle."
    "{i}Nekolio, King of Kings, King of Lands, brought his new trophy with him to all functions and events. He was seldom seen without the slave groaning and seething at his feet. The rattle of her chains was heard often.{/i}"
    "{i}The King would take great pleasure in using his slave in public. She was taught the arts of pleasure, in contrast to her former training. She was taught to replace the sword with the shaft.{/i}"
    "{i}The King said loud and strong that she would learn to enjoy herself. All human sluts did. The slave insisted that she was not a slut. Yet, the first signs of resistance breaking were observed. The wetness of the thighs, the eyes focused on his cock.{/i}"
    "{i}It was only when the first stage of her resistance was broken that the King announced that his slave would be made to bear his next child. She would be fucked mercilessly day in and day out until his seed had taken hold.{/i}"
    "{i}The slave did not speak at this announcement. Perhaps even this early she was learning to accept the pleasure that a human man could not provide-{/i}"
    #alexia aroused
    "Alexia slammed the book shut there, cheeks flushed. That phrase she’d just read, about pleasure a human man couldn’t provide, had hit a bit close to home."
    if all_actors['alexia'].corruption < 30:
        "She couldn't put her finger on why. It seemed wrong to her. Like something that shouldn’t even be said. Yet...it did have an effect on her…"
    else:
        "Her finger traced the cover of the book. Even if she didn’t want to admit it, she had thought that exact same thing during her past...encounters...with her captor."
    $ change_actor_num_flag('alexia', 'andras_influence', 3)
    jump potResolution

else:
    scene cg252 with fade
    pause 3
    "Alexia skimmed the book with a furrowed brow. The topic of it was strange. Not something she ever expected to read about. The first human to reign as a queen of Bloodmeen."
    "The story of how it happened was a curious one. After the fall of a demon lord, the daughter of a high lord was placed as caretaker of the castle. Perhaps it could even become a functioning part of the realm."
    "She flipped ahead in the story. Already she could see the way it went wrong."
    "{i}The Queen brought the Knights of Bloodmeen to the throne room, and they were shocked by what they had seen. She sat naked upon her throne, impaled upon a phallic object. The chaste men shielded their eyes.{/i}"
    "{i}The slutty queen declared her new allegiance to chaos. The pleasure that came from sex and power. She revealed the sexual encounters she’d had throughout the castle with the remaining prisoners.{/i}"
    "{i}She spoke of the joys of sex. The hatefulness of purity. What was the point of limiting ones pleasures in the name of a lady who loves them not?{/i}"
    "{i}She revealed the interests that had grown in the interim. How lovingly she spoke of large cocks and rough sex.{/i}"
    "{i}The Knights of Bloodmeen debated continuing their mission and removing their queen from her throne. But, without consulting the others, Sir Vasylio approached the throne and stripped off his armor.{/i}"
    "{i}The Knights were yet more astonished as the Queen mounted her loyal knight right there and fucked him in front of the entire-{/i}"
    "Alexia slammed the book shut. A shiver went up her spine."
    if all_actors['alexia'].corruption < 30:
        "Just what was she reading? How could a woman choose to do such a thing? Yet, everything she read merely reminded her of her day to day life."
        "She felt the constant caress of this place at all times. Behind every nook and cranny, something was here urging her to go further, do something that she might have viewed wrong for her entire life."
        "It could be quite seductive..."
    else:
        "Alexia licked her lips. She understood the chain of events that had led the queen to that mental state. In truth, it wasn’t like she’d never thought about having sex in public, or any of the debaucheries she’d ever read."
        "People did what felt good, right?"
        if all_actors['alexia'].corruption < 60:
            "Part of her, a part from back before, loudly reminded her that this was wrong. But, reading the story just now had made that part of her easier to ignore. Whiny. Annoying."
        else:
            pass
    
label potResolution:

scene bg12 with fade
show alexia librarian neutral at midleft with dissolve

"For the briefest moment, she glanced towards the front of the library. Would Cliohna be too angry with her if she stopped to touch hers-"

"Alexia shook her head. That was a bad idea. She should just finish her work."

"Alexia picked up the book and walked towards the darkened section of the library."

pot "I knew you’d like the book. I always know the books that humans long to read most."

"Alexia answered quietly."

al "It was illuminating."

"She placed the book on the empty spot of the shelf and then returned to her duties. Part of her suspected that this might not be the last time she paid the Prince of Tomes a visit."

$ change_corruption_actor('alexia', +3)

show cliohna neutral at cliohnaright with dissolve

"On her way out for the night, she was stopped briefly by Cliohan. The woman did not even raise her glance from her reading material."

cl "Be careful with the creature in the back of the library. It is mostly harmless, but it is not trustworthy. There is a reason why I have not made use of it’s talents in my studies."

"Alexia walked on, unsure of what to make of Cliohna’s warning. Just what was that thing?"

al "...Right."

return
