label whitescar_dialogue:

if whitescarDialogueStage == 1:
    jump whitescarFirstDialogue
    
else:
    jump whitescarSecondDialogue

label whitescarFirstDialogue:

scene bg7 with fade

"Rowan walked to the doorway of the Red Sun Alliance representative’s guest room with a pit in his stomach. It was his duty to feel out the representative, but that didn’t mean he was happy about it. The last time the two had met alone in person, the Wolfman had nearly killed him."
"Rowan shoved those concerns aside, taking hold of the door and making a point to open it with force. He swept inside, his eyes alighting to the Wolf stalking around the luxurious, gilded room. His bestial presence looked all the more awkward in contrast to the frilly drapes and crimson curtains."
"The creature paced the room like a carnivore stalking the pack’s perimeter. He growled every so often to himself, his bulky form seeming confined by the small room. He let out a snarl as his yellow eyes held to Rowan’s."

#whitescar angry
show whitescar neutral at cliohnaright with dissolve

whit "Those thrice-damned Twins goad me with this useless finery. Do they take me for one of those feeble Midnight Court sychophants?"

show rowan necklace neutral at midleft with dissolve

ro "Chief Whitescar."

"The Wolf paused in his hectic pacing, his head snapping over to look straight at Rowan. The two stared each other down."

#whitescar neutral

whit "Rowan. So you have come."

ro "I have. On behalf of the Twins, I welcome you to Castle Bloodmee-"

whit "Skip the pleasantries, human. Empty words are a waste of air, forced platitudes even moreso."

ro "I only meant it as a sign of respect."

whit "Respect is earned through action, not seduced through frivolous boot-licking."

#whitescar happy

whit "You of all people should know that. It is why I am glad the Twins have chosen you to arbitrate these negotiations."

show rowan necklace angry at midleft with dissolve

ro "Well don’t get too comfortable with yourself. I haven’t decided on who I intend to pick yet."

#whitescar neutral

whit "The choice is obvious. The Red Sun Alliance is providing you exactly what a worthy ally should: strength and loyalty. The Midnight Court only offers deceit and betrayal."

ro "That remains to be seen."

whit "Well, if you have not come to render a decision, then what is your purpose here?"

ro "Honestly? To get to know you better."

"At this the white Wolf smiled, stretching his fangs wide across his bestial face as he gave Rowan a predatory grin."

#whitescar happy

whit "You already learned everything you need to know about me when we met in the canyon."

#whitescar neutral

whit "But at least I see what you are angling for, now. Ask your questions, human. I will do my best to answer them."

$ whitescarDialogueCount = 0
$ whitescarFirstQ = True

label whitescarDialogueMenu:
show rowan necklace neutral at midleft with dissolve

menu:
    "Why does the Red Sun Alliance even exist?":
        $ released_fix_rollback()
        if whitescarFirstQ == True:
            $ whitescarDialogueCount += 1
            whit "A fool’s question. Why does any alliance exist? To protect them from something by becoming stronger than the sum of their parts."
            ro "That’s hardly a good answer."
            whit "We are a confederation of Fae spirits, bound together in a compact of blood, magic and loyalty. Rosaria is a dangerous place, especially for nature spirits not born of this plane."
            ro "What do you mean, “not of this plane?”"
            #whitescar happy
            whit "It is a long an ancient story, one I shall recount to you in full, should you prove worthy of trust."
            #whitescar neutral
            whit "We are led by Sol. The Elder. The Ancient; a Dragon of incalculable age and wisdom. He has watched your masters’ recent campaigns with interest."
            show rowan necklace angry at midleft with dissolve
            ro "They are not my masters."
            #whitescar happy
            whit "When the Twins beckon, you grovel. That is submission. It is better to be honest with yourself than live in a delusion. The Red Sun Alliance knows this better than anyone."
            #whitescar neutral
            whit "Do you think we are any more pleased with this arrangement than you are? The spawn of Kharos are fickle and cruel. But the circumstances of the moment compel us to offer our friendship nonetheless."
            $ whitescarFirstQ = False
            menu:
                "Who is a part of the Red Sun Alliance?":
                    whit "We are the Fae. The {i}true{/i} Fae. We are spirits of wood and bole, of fur and claw. The form you now see me in is just the latest life cycle that I have inhabited."
                    whit "Ignorant mortals will call us “Beastmen,” but that is not what we are. The Red Sun Alliance are those spirits not bound by the false dichotomy of the Gods of Light and Darkness."
                    show rowan necklace shock at midleft with dissolve
                    ro "You… aren’t aligned with Solanse or Kharos?"
                    #whitescar happy
                    whit "Is choosing a middle path really so terrible? At what point does the cause no longer justify the bloodshed?"
                    #whitescar neutral
                    whit "There must be balance in all things, Rowan. An eternal twilight is just as awful as an endless noontime. Neither of the Gods are acting in anything other than their own self interest."
                    whit "...As are we all. My kind, at least, are pragmatic enough to acknowledge that fact of nature."
                    jump whitescarDialogueMenu
                    
                "Is the Alliance Stable?":
                    #whitescar sad
                    whit "..."
                    whit "It is. But we are no longer whole. The Midnight Court betrayed us long ago, taking many of our younger spirits with them in their exodus. They no longer follow Sol’s teachings."
                    whit "They have corrupted themselves with their own lust for power. They can no longer even be truly counted amongst the Fae. "
                    #whitescar neutral
                    whit "But those countless spirits that make up our Alliance remain true to our nature, and are unshakeable in our loyalty. We are of one mind: if you are a friend of the Fae, you are a friend to all of us."
                    jump whitescarDialogueMenu
                    
                "Why do your people hate the Midnight Court?":
                    #whitescar angry
                    whit "Why do {i}you{/i} hate slavers, bandits, brigands and rapists?"
                    whit "The putrid offal that makes up the Midnight Court are literal abominations. They are Fae who defied their own life cycle: choosing to inhabit the mortal forms of sentient beings!"
                    #whitescar neutral
                    whit "When a Fae reaches the end of its natural life, its body dies to allow the spirit to return to the plane of existence from whence we originate. "
                    whit "Over the course of centuries, our spirits are able to eventually return in a new form, possessing the body of either a plant or an animal. It is an eternal circle, a means for our spirits to remain pure and untainted in this alien place."
                    #whitescar angry
                    whit "The Midnight Court defied their very nature, occupying the bodies of beings that possessed souls of their own, for the sake of a false immortality."
                    whit "They are the corruption of life, the ultimate narcissists. Their very words are poison, their temptations of power a fickle mirage to draw you in to their spider’s web."
                    jump whitescarDialogueMenu
        else:
            menu:
                "Who is a part of the Red Sun Alliance?":
                    whit "We are the Fae. The {i}true{/i} Fae. We are spirits of wood and bole, of fur and claw. The form you now see me in is just the latest life cycle that I have inhabited."
                    whit "Ignorant mortals will call us “Beastmen,” but that is not what we are. The Red Sun Alliance are those spirits not bound by the false dichotomy of the Gods of Light and Darkness."
                    show rowan necklace shock at midleft with dissolve
                    ro "You… aren’t aligned with Solanse or Kharos?"
                    #whitescar happy
                    whit "Is choosing a middle path really so terrible? At what point does the cause no longer justify the bloodshed?"
                    #whitescar neutral
                    whit "There must be balance in all things, Rowan. An eternal twilight is just as awful as an endless noontime. Neither of the Gods are acting in anything other than their own self interest."
                    whit "...As are we all. My kind, at least, are pragmatic enough to acknowledge that fact of nature."
                    jump whitescarDialogueMenu
                        
                "Is the Alliance Stable?":
                    #whitescar sad
                    whit "..."
                    whit "It is. But we are no longer whole. The Midnight Court betrayed us long ago, taking many of our younger spirits with them in their exodus. They no longer follow Sol’s teachings."
                    whit "They have corrupted themselves with their own lust for power. They can no longer even be truly counted amongst the Fae. "
                    #whitescar neutral
                    whit "But those countless spirits that make up our Alliance remain true to our nature, and are unshakeable in our loyalty. We are of one mind: if you are a friend of the Fae, you are a friend to all of us."
                    jump whitescarDialogueMenu
                        
                "Why do your people hate the Midnight Court?":
                    #whitescar angry
                    whit "Why do {i}you{/i} hate slavers, bandits, brigands and rapists?"
                    whit "The putrid offal that makes up the Midnight Court are literal abominations. They are Fae who defied their own life cycle: choosing to inhabit the mortal forms of sentient beings!"
                    #whitescar neutral
                    whit "When a Fae reaches the end of its natural life, its body dies to allow the spirit to return to the plane of existence from whence we originate. "
                    whit "Over the course of centuries, our spirits are able to eventually return in a new form, possessing the body of either a plant or an animal. It is an eternal circle, a means for our spirits to remain pure and untainted in this alien place."
                    #whitescar angry
                    whit "The Midnight Court defied their very nature, occupying the bodies of beings that possessed souls of their own, for the sake of a false immortality."
                    whit "They are the corruption of life, the ultimate narcissists. Their very words are poison, their temptations of power a fickle mirage to draw you in to their spider’s web."
                    jump whitescarDialogueMenu
                
    "What is your role in the Alliance?":
        $ released_fix_rollback()
        $ whitescarDialogueCount += 1
        whit "I am the Mane, emissary of Sol and Speaker of the Council of Elders. I am the oldest living Fae, exempting those monsters of the Midnight Court."
        whit "I am here as a representative of my people, and am thus bound by their collective honor. It is the only reason why that Witch is still alive at all."
        #whitescar angry
        whit "Had I my choice, I’d have already stalked that misbegotten Arzyl through the Castle’s corridors, torn her to bloody ribbons, and sucked the vile marrow from her accursed bones."
        #whitescar neutral
        whit "...You’ll forgive my outburst. I find these man-built walls oppressive; being cooped up in here so close to a foe makes my pelt itch."
        jump whitescarDialogueMenu
        
    "Why did you attack me in the canyon?":
        $ released_fix_rollback()
        $ whitescarDialogueCount += 1
        #whitescar happy
        whit "Why does an instructor practice on the training field with new recruits? To take the measure of them."
        show rowan necklace angry at midleft with dissolve
        ro "So you decided to test me."
        #whitescar neutral
        whit "An ally is only as useful as the strength they provide. You are the face of the Twins’ War on this world, for better or worse."
        whit "I had to be sure we were not allying with weaklings."
        #whitescar happy
        whit "For what it’s worth? You passed the test."
        show rowan necklace neutral at midleft with dissolve
        ro "Gee, thanks a lot."
        jump whitescarDialogueMenu
        
    "Are you truly led by a dragon?":
        $ released_fix_rollback()
        $ whitescarDialogueCount += 1
        #whitescar happy
        whit "Yes. The Red Sun Alliance follows the teachings of the Dragon Sol."
        ro "I thought the Dragons had mostly died out."
        #whitescar neutral
        whit "For the most part, they did. Sol was one of the Elder race who chose a different path. He secluded himself in the Forest of Ardynne, millenia ago."
        whit "He allowed himself to be entangled within the heart of the forest. As vines slid between his scales and new trees dug their roots into his carapace, he became as one with nature."
        whit "He found my people, the Fae in desperate straits. We were the fading nature spirits of a dying plane of reality. Sol came into contact with us, and offered to bridge the gap between our world and his so that we might live."
        whit "Thus, we formed the Pact of Rebirth. In exchange for our lives and a new home, we became bound to the Lifebringer’s Draconic spirit, and accepted the life cycle he had created for us. It was a win-win situation."
        jump whitescarDialogueMenu
        
    "I have no further questions for you." if whitescarDialogueCount > 3:
        $ released_fix_rollback()
        #whitescar happy
        whit "I have no doubt that we will speak again, Rowan."
        ro "Hopefully next time it won’t involve a fight to the death."
        whit "I would not concern myself overmuch about such things, boy. Should we come into conflict in the future, I have a feeling it will be a bit more… intimate than that."
        ro "…"
        ro "If you say so."
        "Rowan turned to leave, but the sound of a muffled snort drew his eyes back to the White Wolf."
        #whitescar neutral
        whit "I have a question of my own, if you’ll indulge me."
        whit "Why do you serve the Twins? A man like you… you do not strike me as the type to serve at someone’s beck and call."
        ro "Most men don’t find themselves in my circumstances."
        if serveChoice ==1:
            ro "Truth be told, I am not doing this because I want to, but because I have to. The Twins have become far too powerful to be openly opposed."
            whit "Hmm… so like clever prey, you are playing dead."
            ro "For now."
            whit "..."
            #whitescar happy
            whit "You intrigue me, Human! You remind me of my own people’s philosophy: the strong survive, the weak are culled. As true in Empires as in the Wild."
            whit "Perhaps there is more potential to our prospective alliance than I first thought."
        elif serveChoice == 2:
            ro " I… it was made clear to me very early on what the alternative would be if I did not."
            #whitescar happy
            whit "Hah! So you have been blackmailed. "
            show rowan necklace angry at midleft with dissolve
            ro "No. This was worse. They were going to lock me up and throw away the key. I was afraid of becoming a prisoner in my own mind. "
            #whitescar neutral
            whit "..."
            whit "No living thing should suffer the cruelty of eternal captivity."
            whit "I think I am coming to understand you better, Rowan. You have been enslaved to a master who dangles punishments and rewards in equal measure over your nose, like a fresh kill."
            whit "Just have a care to remember which of the two is actually drawing your scent."
        elif serveChoice == 3:
            show rowan necklace angry at midleft with dissolve
            ro "And the only reason I go along with this charade in the first place is for the sake of my wife."
            whit "So that is why! They have taken your mate. I am surprised you have not murdered them all already."
            show rowan necklace neutral at midleft with dissolve
            ro "Don’t think for a second that I wouldn’t if I could. But for now, I have to pick my battles. For her sake."
            whit "Love is a potent but dangerous emotion, as prone to mistakes and missteps as anything else conjured by mortals. Have a care that you are not unwittingly serving those you claim to despise, boy."
        else:
            ro "And I’m not their ‘servant’ exactly. More like their partner."
            #whitescar happy
            whit "Perhaps you should discuss that with your ‘partners’ then! Ha ha!"
            show rowan necklace angry at midleft with dissolve
            ro "There is more truth in their words than you might think. It is not as if Solansia has made the world a better place for her rule."
            #whitescar neutral
            whit "...And you think that the Children of Kharos will be any better?"
            show rowan necklace neutral at midleft with dissolve
            ro "Perhaps. I would sooner try for {i}something{/i} than hope for nothing."
            ro "Besides: aren’t you here to make an alliance with them? If they are so terrible then what are you doing here?"
            #whitescar happy
            whit "The same as you are Human: Surviving."
        "Seeing that the bestial Fae had no more to say to him, Rowan turned and left the room."
        $ whitescarDialogueStage = 2
        return
        
label whitescarSecondDialogue:

#tunnels BG
scene black with fade

"The narrow, winding corridors closed in around Rowan as he descended into the deeper bowels of the Castle’s innards. Every footstep was punctuated by a cacophonous echo, as if his very presence was disturbing the ancient, dessicated ruins of the now-lost civilizations that had built upon them, one on top of the other."
"Dust hung heavy in the air, the collected offal of thousands of years of stagnation fluttering about like mouldering moths in the gloom. He had come to this abandoned section of the Castle’s basement for one purpose: to speak to the enigmatic Wolfman."
"The task became increasingly daunting the deeper Rowan went, moving through the cramped confines of the tomblike warrens with a nervous hand at his sword hilt. He turned a corner, coming to a small stone antechamber leading still deeper into the interior, and was caught off guard by what he saw."

show whitescar neutral at cliohnaright with dissolve

whit "I will tell you if anything changes; for now, we must assume that the Twins’ decision to make him the arbiter of this dispute is an honest one. "
whit "It does not seem to be a trick on their part. Or if it is, I can’t fathom the reason for it."

show heartsong neutral at midleft with dissolve

hear "You stand upon a knife’s edge, Father. Your willingness to trust the Servants of Kharos may prove to be our undoing."

whit "As if I had any illusions to the contrary. "
whit "Worry not, dearest Daughter: I know what is at stake."
whit "...You will inform Sol of my progress?"

#heartsong happy

hear "Of course, Father. You have my word."

whit "Good. Then you can come out now, Rowan. We have finished with our conversation."

"The hair on the back of Rowan’s neck rose. He stepped out from the shadows, his hand at his blade as he readied himself for an ambush. Both the Wolf man and his Lupine compatriot turned their heads to look at him."

hear "Hello again, Rowan."

show rowan necklace angry at edgeleft with moveinleft

ro "What are you two doing down here? What is this conspiracy?"

"Whitescar chuckled, his fangs pulling back from his face as he flashed Rowan a terrifying grin. Heartsong smiled, her hips twisting as she swayed seductively back and forth."

whit "What conspiracy? We are not the Midnight Court. If we intended you harm, it would come at the end of my claws, not from a poisoned chalice."

#heartsong angry

hear "Father!"

ro "How comforting."

#whitescar happy

whit "Heh. Worry not Rowan, these claws can be used in other ways as well. Perhaps, if you’re interested, I might even show you a few of the more erotic methods."

show rowan necklace neutral at edgeleft with dissolve

ro "I’ll… keep that in mind."
ro "-What is she doing here?"

#whitescar neutral

whit "This is my Daughter, Heartsong. You two have met before: she offered to help you escape from the clutches of some Goblins, as she tells it."

#heartsong happy

hear "It is nice to see you again, Rowan."

if trustHeartsong == True:
    hear "I am… glad you decided to let me in. Many mortals are intimidated by a Dreamwalker’s intrusion into their dreams."
    
else:
    #heartsong neutral
    hear "I am sorry you had to suffer through that Goblin’s awful poison. I tried to warn you, but… well, rejection is not an uncommon experience for Dreamwalkers like myself."
    
"Rowan nodded in the direction of the white-furred woman, her bushy tail swishing slowly behind her as she graced him with a nervous smile. Her yellow eyes were bright and intelligent, bestial like her fathers, but tempered by a certain warmth that was lacking in Whitescar’s eyes."

whit "The two of you would make a fine mating pair, I think."

if trustHeartsong == True:
    #heartsong neutral
    pass

hear "Father!"

#whitescar happy

whit "Hah! You were conceived three life cycles ago, yet still you stammer about when the topic turns to fornication."

#whitescar neutral

whit "Away with you now, girl. Rowan and I have things to discuss."

"Heartsong bowed her head, making for the exit. Rowan caught sight of the shy, sultry look she shot in his direction as she passed, the faint smell of cinnamon hanging in the air."

hear "Farewell for now, Rowan. Don’t rough him up too much, will you Father?"

whit "I make no assurances."

hide heartsong with moveoutleft

"... ... ..."
"... ..."
"..."

ro "I’ve been looking for you."

whit "A shame, I’d prefer to savor your scent in the clean night air."

ro "Uh… thanks."

"The Fae Wolf’s yellow eyes held to Rowan’s as a slow grin spread across his muzzle. "

whit "You desire answers. Come: pursue me, if you can. Perhaps you might just discover a few."

hide whitescar with dissolve

"Without another word the beast leapt on all fours, charging forth down a narrow corridor deeper into the catacombs. Rowan was caught off guard, watching as the white blur zipped past him into the gloom. After a long moment of silence, he drew his sword and moved to follow."
"He threaded his way along the narrow, winding path, glancing down sudden turns and in empty rooms as he moved. There was the sound of rustling in his ears in the distance, but he could not make out the source or location."
"He was being stalked. Rowan’s fingers tightened around his sword as he moved with slow calculation from footstep to footstep."

ro "...Where are you?"

show whitescar neutral behind black

whit "Ask your questions, and perhaps in time you’ll find out."

$ whitescarDialogue2Count = 0

label whitescarDialogue2Menu:
show rowan necklace neutral at edgeleft with dissolve

menu:
    "What were you and Heartsong doing down here?":
        $ released_fix_rollback()
        $ whitescarDialogue2Count += 1
        whit "Hah! Why? Don’t you trust us? What cause might we have to meet in a place like this?"
        ro "Conspiracy. Betrayal. Maybe something worse."
        whit "You misinterpret our methods, though I do not blame you."
        "Rowan could hear the low skitter of nails on stone as he moved deeper into the labyrinthine corridors that surrounded him. He couldn’t place just where the old Wolf was lurking."
        whit "When a lone wolf seeks out a new pack to integrate into, they learn everything they can about their prospective allies first. "
        whit "I am an emissary, a voice for the Red Sun Alliance. Heartsong is the other half of that equation: she is our eyes."
        whit "Have you not noticed the sudden abundance of foliage in the plains below the castle? How odd that so much game now flourishes there."
        show rowan necklace angry at edgeleft with dissolve
        ro "You’re spying on us."
        whit "As if your petty masters were not doing the same to us. Not all who walk the mortal realms hold to your scruples, Rowan. The Twins are many things, but honest dealers in diplomacy they are not."
        whit "The roots of this Castle run deep, its hidden networks are a legacy of civilizations that predate even the Fae’s arrival into this world. You shouldn’t be surprised that we know of some secret passages."
        whit "Think of Heartsong as my counterpart. We are both of the same Diplomatic Embassy, but she chooses to remain in the shadows."
        show rowan necklace neutral at edgeleft with dissolve
        ro "...While you draw both the Twins and the Midnight Court’s attention."
        "Rowan heard the guttural bark of a laugh down one corridor. He turned the corner and began to follow it to its source."
        whit "What better decoy is there, than a foul-mouthed braggart like myself?"
        jump whitescarDialogue2Menu
        
    "Who are you really, Whitescar? Why play these games with me?":
        $ released_fix_rollback()
        $ whitescarDialogue2Count += 1
        "Rowan heard no immediate answer. He came to a stop in the corridor, glancing around as a low, rumbling chuckle echoed down the hall."
        whit "Why? Because you are the first human I have ever met who managed to actually impress me."
        whit "Had you proven incapable of defending yourself back in the canyon, we would not be having this discussion. I’d have vivisected you from stem to sternum."
        show rowan necklace angry at edgeleft with dissolve
        ro "You’re avoiding the question."
        whit "And you are missing the point. I play these games because you are a worthy opponent. Hunting helpless prey is neither sporting nor eventful. {i}You{/i} on the other hand…"
        ro "So what, I’m your plaything?"
        "There was another rumbling chuckle. Rowan spun around, but he only managed to make out a momentary blur of movement in the shadows. Just as he turned to follow it, it was gone."
        whit "Only if you’re willing to play."
        ro "What do you get out of this? "
        whit "Who’s to say that “I” get anything? Were you not listening when last we spoke, pup? I am here at the behest of Sol, the Golden Dragon of the Fae. His will is mine."
        ro "Then why bother with this charade? Why bother answering my questions at all?"
        "There was a third chuckle. It was so close that Rowan spun around, slashing with his blade behind him at the voice in his ear. He cut nothing but air. The lingering, faintly piny scent of the Wolfman was now stuck in his nose."
        whit "Because you intrigue me, Rowan. In a way that few mortals have ever managed to do before."
        ro "Thanks for the attention. I’ll let you know when I decide I want to make a half-Fae mutant."
        whit "Ha! Children and pleasure are two different matters, mortal. They are not one and the same. My people seek sexual relations as much as any other; is that not nature personified?"
        whit "We Fae seek relationships with whomever, or whatever strikes our fancy. I have lived many lives, pup. I have had many conquests, but it is those with power who truly draw my eye."
        ro "..."
        whit "Ha ha! If you are not interested in the form I have chosen, perhaps my daughter would be of intrigue to you instead? Mortals seem strangely preoccupied with the specifics of their partner’s genitalia."
        show rowan necklace neutral at edgeleft with dissolve
        ro "I didn’t know offering up your own child on a silver platter to me was considered ethical to the Fae."
        whit "My daughter is... precious to me. Choosing a viable mate is an important part of her life cycle. If I cannot act in that stead for her, I can at least see someone of respectful character and capacity do it instead."
        whit "I would not worry for her sake: she is even more restless and wild than I am! You would be lucky to survive the first copulation."
        jump whitescarDialogue2Menu
        
    "What does the Red Sun Alliance even want?":
        $ released_fix_rollback()
        $ whitescarDialogue2Count += 1
        whit "Peace. Or at least: what you mortals conceive as peace:"
        whit "The struggle of life, without the imminent threat of annihilation."
        ro "And you think the Twins will provide you that?"
        whit "For a time, perhaps. There is no such thing as true ‘peace’ in this world, merely moments of lesser danger."
        whit "Sol is no fool. He knows the Twins’ plans for conquest. Maybe one day they shall become the alpha predator that we fear. But for now, they are useful to us."
        "Rowan cast his eyes around him, simmering with anger at his inability to determine the Wolf’s exact location."
        show rowan necklace angry at edgeleft with dissolve
        ro "-Then what do you even want from this?! Why not simply lurk in your forests like you’ve always done?"
        "The low, rumbling chuckle of the Wolf rebounded down the hallway to his right like a patronizing echo."
        whit "A fair question. Let me ask you in turn: why does the deer, or the sparrow, flee from a forest fire?"
        whit "Because staying where they were was a death sentence."
        whit "The Midnight Court is seeking the Twins as accomplices. What do you think my people’s fate will be, should they make such an unholy alliance?"
        jump whitescarDialogue2Menu
        
    "End this game. I have no more questions for you." if whitescarDialogue2Count > 2:
        $ released_fix_rollback()
        "The old Wolf laughed. A sudden blur of white fur flashed before Rowan’s eyes before he was tackled to the ground. He ended up on his back, his sword clattering from his hands as the Wolf slammed his wrists back against the ground and loomed over him."
        "The two shared a long moment of eye contact, Whitescar’s heavy breath tickling the nape of Rowan’s neck as he sniffed him."
        #whitescar happy
        whit "The game is finished."
        ro "Then let me go."
        whit "Why? Don’t you like the challenge?"
        ro "I prefer my freedom."
        whit "Then fight for it."
        show rowan necklace angry at edgeleft with dissolve
        ro "Let. {i}Go{/i}. Of me."
        #whitescar neutral
        whit "I already did, Rowan. You just have to wake up."
        show rowan necklace neutral at edgeleft with dissolve
        ro "...What? What are you-"
        "..."
        scene bg9 with flash
        show rowan necklace naked at midleft with dissolve
        ro "{i}GUH!{/i}"
        "Rowan came to sudden consciousness with the bursting clarity of one who had been hit with a bucket of water. He swept his gaze around the empty room, realizing as the seconds passed that he’d been asleep."
        ro "How did… was that a…?"
        "... ... ..."
        "... ..."
        "..."
        ro "Heartsong. I should have known."
        "The more he thought about the memory of stalking Whitescar through the underdark, the more Rowan realized the unreality he’d been surrounded by. It had all been a dream, brought up from the depths of his subconscious by Heartsong’s power."
        "But… to what purpose?"
        $ whitescarDialogueAvailable = False
        return
        

