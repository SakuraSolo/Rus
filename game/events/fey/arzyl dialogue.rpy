
label arzyl_dialogue:

if arzylDialogueStage == 1:
    jump arzyl_first_dialogue

if arzylDialogueStage == 2:
    jump arzyl_nileth

else:
    jump arzyl_isdruel



label arzyl_first_dialogue:

scene bg7 with fade

"Rowan stopped at the entrance to Arzyl’s chambers, the sound of low chanting drifting through the doorway. The lyrical tune of her voice carried a strange resonance, and his head buzzed as he pressed onwards through the entryway."
"The pale Elf sat cross-legged in the center of the room, her blank white eyes glowing as her full lips mumbled a haunting chorus low under her breath. She seemed to be almost in a trance, her head bowing low as she huddled forward. "
"At the sound of Rowan’s arrival her head snapped up, her lidless gaze swiveling to focus upon the human intruder. A wide smile spread across her face; Rowan could have sworn her body posture was intended to entice him with her hanging, milky cleavage."

show arzyl neutral at midright with dissolve

arz "Rowan! I was just thinking of you."
                                                                                                                                                                                                                                                               
show rowan necklace neutral at midleft with dissolve

ro "No doubt while chanting a paralyzing spell."

#arz happy

arz "Oh, I don’t think so. I took the lead {i}last time{/i}. Now it’s your turn to prove yourself worthy of me!"

ro "Don’t hold your breath on that."

arz "Why would I? I’d prefer to have you take it away from me."

ro "..."

arz "Oh, don’t give me that look Rowan! Can you honestly say that I was the first being in Solance to try such a maneuver on you?"

show rowan necklace angry at midleft with dissolve

ro "No. But that doesn’t make it right."

#arz neutral

arz "Maybe not, but neither was Whitescar’s attempt to corner you like a wounded animal in that canyon, don’t you think?"

show rowan necklace neutral at midleft with dissolve

ro "How do you know about that?"

arz "I know much more than you might think, Rowan. "
arz "About you. About the Twins. About… "

#arz happy

arz "Your wife."

show rowan necklace angry at midleft with dissolve

ro "Tread lightly with your next words, Arzyl. I don’t respond well to threats."

arz "Oh, sweet Rowan: I would never dream of such a thing!"


"The statuesque Elf stood up from the ground, smiling at the long look Rowan gave to her jiggling mammaries as she rose. She strode with a seductress’ walk over to him, her lips pursed as she slid comfortably to his side."

#arz neutral

arz "Now: what can I do for you?"

$ arzylDialogueCount = 0
$ arzylFirstQ = True

label aryzlDialogueMenu:
show rowan necklace neutral at midleft with dissolve

menu:
    "What is the Midnight Court?":
        $ released_fix_rollback()
        if arzylFirstQ == True:
            $ arzylDialogueCount += 1
            arz "We are the Eternal Heirs of the Outer Spheres, the Imperators of a New Era, Witches and Warlocks of the Third Path."
            arz "We are the Drach’Hyl, the twice-born, and we are the rightful rulers of this world."
            ro "Yeah? And I’m the Baron of Rosaria."
            #arz happy
            arz "Now now, Rowan! There’s no need to be rude."
            #arz neutral
            arz "We are a Cabal of the most powerful of the Fae, those unbound by the rule of that Golden Dragon that the Red Sun Alliance obsequiously worships.  We broke free from his tyranny centuries ago, and now govern ourselves as we see fit."
            arz "We are led by her grace, Queen Kassandra. Firstborn and most beloved of the true Fae. For she alone of the first Fae understands that there is only one thing in this world that truly matters:"
            arz "Power, and the means to acquire more."
            ro "Alliances made purely for the sake of power are rarely worth the paper they’re printed on."
            #arz happy
            arz "A marriage of convenience is preferable to lonely impotence, wouldn’t you agree Rowan? Especially when that marriage comes with so many… ‘convenient’ perks."
            "Rowan’s mouth twisted in distaste as he felt the ageless Fae’s long fingertips slide down his arm, drifting inexorably towards his genitals. He took a purposeful step back, which caused Arzyl to let out a lilting laugh."
            $ arzylFirstQ = False
            menu:
                "What Races are in the Midnight Court?":
                    #arz neutral
                    arz "Only one. The Fae."
                    ro "That’s blatantly untrue. I have seen your servants around the castle: Elves, humans, even a Goblin or two."
                    #arz happy
                    arz "Oh ho! For all your heroic sensibilities, you really can be short sighted in your judgement. Those beings you saw {i}looked{/i} like Humans and Elves, I’ll grant you that."
                    #arz neutral
                    arz "But I can assure you: they are Fae, just as I am."
                    arz "Have you never wondered about the old folk legends? Of entire villages’ slumbering children being abducted from their beds in the middle of the night by spirits of the woods?"
                    ro "They’re children’s tales. Fiction and fantasy."
                    #arz happy
                    arz "Exaggerated, yes. Fantasy, no. The ones we abduct are the {i}Nekarae{/i}, “host vessels.” Unlike the Red Sun Alliance, the Midnight Court chooses to possess sapient beings."
                    #arz neutral
                    arz "The spiritual merge that occurs anchors the Fae to this adopted realm, granting the host unending life, and the Fae spirit a permanent body to reside in. We do not suffer the same ills that the false Fae do."
                    ro "...And the hosts themselves?"
                    #arz happy
                    arz "Is immortality really such a terrible thing? What is the cost spiritual freedom in comparison to eternal life?"
                    ro "So are there no other races in the Midnight Court at all?"
                    #arz neutral
                    arz "We are a single people, and have little use for the lesser races of the world. The Glades of the Midnight Court are our playground, far removed from the mortals of Solanse. "
                    arz "We are visited on occasion by the odd adventurer or ambitious Warlock, seeking knowledge, or power, or simply a test of their skills."
                    #arz happy
                    arz "It does not matter their reasons: to step into the forbidden Glades is to make one’s life forfeit."
                    jump aryzlDialogueMenu
                    
                "Is it true that the Midnight Court mates with demons?":
                    "A deep, menacing smile spreads across the Fae’s face. Her eyes seem to gleam with a malicious light as she fluttered her eyelashes at him."
                    #arz happy
                    arz "My, aren’t {i}you{/i} a curious sort. Is this question a subtle attempt to ask if the Fae will copulate with anyone?"
                    ro "Just answer the question."
                    #arz neutral
                    arz "Very well. The short answer? Yes. We will mate with Demons. We’ll also mate with Elves, Orcs, Minotaurs and even {i}Dragons{/i} - if it suits our needs."
                    ro "Why?"
                    arz "Silly boy, the answer is as obvious as it is self evident. Why does a beautiful Noblewoman have an affair with an Elderly King? Why do the street-walking whores of your squalid cities choose to bed strangers?"
                    arz "To get something out of it. Pleasure can be a purpose unto itself. The Demons have sired many of our progeny in the past, and will doubtless do so again, should this Alliance conclude to our satisfaction."
                    arz "Sex is a tool. A delightful one, to be sure: but a tool nonetheless."
                    jump aryzlDialogueMenu
                    
                "Why is the Midnight Court at odds with the Red Sun Alliance?":
                    #arz angry
                    arz "They are the false Fae, alien spirits of an alternate dimension who abandoned their own customs to follow the clarion call of that Glimmering Lizard and his drooling sycophants."
                    arz "My Queen, her Grace Kassandra herself, was the first of the Realm-born: a Fae spirit born from the loins of another Fae in this reality. She was the first to recognize the Dragon’s tyranny for what it was."
                    #arz neutral
                    arz "She led a revolt, and freed her most loyal followers from the clutches of that beast’s enslavement spell."
                    ro "..the Dragon enslaved you?"
                    arz "Imagine if you will, Rowan: a desperate people, spirits of a dying reality, cast adrift in the currents and eddies of the great void between dimensions."
                    arz "When out of the ether there comes a voice: “I can save you.” it says, “I can give you life, love, happiness and peace. All you need to do is swear fealty to me, and tie your very essence with my own."
                    #arz angry
                    arz "-And now picture the rage we felt when that promise turned out to be a lie."
                    jump aryzlDialogueMenu
                    
        else:
            menu:
                "What Races are in the Midnight Court?":
                    #arz neutral
                    arz "Only one. The Fae."
                    ro "That’s blatantly untrue. I have seen your servants around the castle: Elves, humans, even a Goblin or two."
                    #arz happy
                    arz "Oh ho! For all your heroic sensibilities, you really can be short sighted in your judgement. Those beings you saw {i}looked{/i} like Humans and Elves, I’ll grant you that."
                    #arz neutral
                    arz "But I can assure you: they are Fae, just as I am."
                    arz "Have you never wondered about the old folk legends? Of entire villages’ slumbering children being abducted from their beds in the middle of the night by spirits of the woods?"
                    ro "They’re children’s tales. Fiction and fantasy."
                    #arz happy
                    arz "Exaggerated, yes. Fantasy, no. The ones we abduct are the {i}Nekarae{/i}, “host vessels.” Unlike the Red Sun Alliance, the Midnight Court chooses to possess sapient beings."
                    #arz neutral
                    arz "The spiritual merge that occurs anchors the Fae to this adopted realm, granting the host unending life, and the Fae spirit a permanent body to reside in. We do not suffer the same ills that the false Fae do."
                    ro "...And the hosts themselves?"
                    #arz happy
                    arz "Is immortality really such a terrible thing? What is the cost spiritual freedom in comparison to eternal life?"
                    ro "So are there no other races in the Midnight Court at all?"
                    #arz neutral
                    arz "We are a single people, and have little use for the lesser races of the world. The Glades of the Midnight Court are our playground, far removed from the mortals of Solanse. "
                    arz "We are visited on occasion by the odd adventurer or ambitious Warlock, seeking knowledge, or power, or simply a test of their skills."
                    #arz happy
                    arz "It does not matter their reasons: to step into the forbidden Glades is to make one’s life forfeit."
                    jump aryzlDialogueMenu
                    
                "Is it true that the Midnight Court mates with demons?":
                    "A deep, menacing smile spreads across the Fae’s face. Her eyes seem to gleam with a malicious light as she fluttered her eyelashes at him."
                    #arz happy
                    arz "My, aren’t {i}you{/i} a curious sort. Is this question a subtle attempt to ask if the Fae will copulate with anyone?"
                    ro "Just answer the question."
                    #arz neutral
                    arz "Very well. The short answer? Yes. We will mate with Demons. We’ll also mate with Elves, Orcs, Minotaurs and even {i}Dragons{/i} - if it suits our needs."
                    ro "Why?"
                    arz "Silly boy, the answer is as obvious as it is self evident. Why does a beautiful Noblewoman have an affair with an Elderly King? Why do the street-walking whores of your squalid cities choose to bed strangers?"
                    arz "To get something out of it. Pleasure can be a purpose unto itself. The Demons have sired many of our progeny in the past, and will doubtless do so again, should this Alliance conclude to our satisfaction."
                    arz "Sex is a tool. A delightful one, to be sure: but a tool nonetheless."
                    jump aryzlDialogueMenu
                    
                "Why is the Midnight Court at odds with the Red Sun Alliance?":
                    #arz angry
                    arz "They are the false Fae, alien spirits of an alternate dimension who abandoned their own customs to follow the clarion call of that Glimmering Lizard and his drooling sycophants."
                    arz "My Queen, her Grace Kassandra herself, was the first of the Realm-born: a Fae spirit born from the loins of another Fae in this reality. She was the first to recognize the Dragon’s tyranny for what it was."
                    #arz neutral
                    arz "She led a revolt, and freed her most loyal followers from the clutches of that beast’s enslavement spell."
                    ro "..the Dragon enslaved you?"
                    arz "Imagine if you will, Rowan: a desperate people, spirits of a dying reality, cast adrift in the currents and eddies of the great void between dimensions."
                    arz "When out of the ether there comes a voice: “I can save you.” it says, “I can give you life, love, happiness and peace. All you need to do is swear fealty to me, and tie your very essence with my own."
                    #arz angry
                    arz "-And now picture the rage we felt when that promise turned out to be a lie."
                    jump aryzlDialogueMenu
                
    "What is your role in the Midnight Court?":
        $ released_fix_rollback()
        $ arzylDialogueCount += 1
        "Arzyl laughs, putting a hand over her mouth as if to chastely conceal her humor. Her sultry look puts lie to the act, though. The Fae leaned forward just slightly, her heaving bosom front and center. Rowan felt a stirring in his groin."
        #arz happy
        arz "It is whatever I choose it to be. We are not the hierarchical taskmasters that the Red Sun Alliance is. Each member of the Court is an individual: a singular, unique soul."
        #arz neutral
        arz "I am one of the greatest of the true Fae, the Queen’s most trusted servant. Thus, she asked that I come here as a favor, and represent her interests in this delicate time."
        arz "I have no title, nor any true authority save that which I am willing to stake my life upon. If Queen Kassandra does not like the terms I return with…"
        #arz happy
        arz "Well, let’s just say that everyone has to answer for their actions in the end."
        "Despite the disturbing implication of her words, Arzyl seems jovial about the situation. Rowan quirked an eyebrow as she breezily ran her fingers through her hair, tossing it behind her shoulders."
        arz "We are living beings, Rowan. Not cogs in an infernal machine. The life we make is our own, for better or for worse. I bear no titles, save the ones I give myself."
        ro "Yet you represent the Midnight Court."
        arz "I look after the interests of the Midnight Court - and thus, my own interests as well. Anything beyond that is pedantic and unnecessary. My brothers and sisters can speak for themselves."
        jump aryzlDialogueMenu
            
    "Why did you ambush me with your servants?":
        $ released_fix_rollback()
        $ arzylDialogueCount += 1
        "Arzyl’s eyes brightened considerably. A slow, creeping smile spread across her cheeks."
        #arz happy
        arz "Why? Didn’t you enjoy our time together? If you are so eager to repeat the experience, my servants would be happy to oblige."
        show rowan necklace angry at midleft with dissolve
        ro "That’s not my point and you know it. You attacked me without provocation. Why?"
        #arz neutral
        arz "Mortals are such strange creatures: always seeking answers to questions far beyond the purview of their own ability to comprehend."
        arz "It is as if you are asking me: “Why do the rains come? Why does the storm collapse my hovel, but leave my neighbor’s safe and sound?”"
        arz "Content yourself with the fact that I chose you for a reason, and that the outcome was even better than I expected!"
        #arz happy
        arz "After all: I could have just as easily cut your throat, had I wished to. The fact that you even have the opportunity to demand answers from me should be an answer unto itself."
        jump aryzlDialogueMenu
            
    "Who leads the Midnight Court?":
        $ released_fix_rollback()
        $ arzylDialogueCount += 1
        #arz happy
        arz "Queen Kassandra, her most illustrious Grace. Lady of the Fae, Royarch of Beauty, and Goddess of the Freeborn."
        ro "That’s a lot of titles for a woman I’ve never heard of."
        #arz neutral
        arz "And that’s precisely why she still bears them, after thousands of years of turmoil and strife."
        arz "If the lesser races knew of her beauty, it would cause a war of such titanic proportions that the very firmament of the sky would collapse."
        ro "Bold words for a myth. If she’s anything like her servants, I doubt that ‘beauty’ sinks deeper than the skin."
        #arz happy
        arz "Ha ha! Oh Rowan, if you were in her clutches right now, you would not even have the breath to scream."
        jump aryzlDialogueMenu
            
    "I have no further questions for you." if arzylDialogueCount > 3:
        $ released_fix_rollback()
        arz "You do, you simply lack the knowledge to ask them, yet. All in due time though."
        ro "Just make sure you avoid using that sorcery on me while you’re here, Arzyl."
        #arz happy
        arz "Of course! I have no doubt that your masters would be resentful if I interfered with their favorite toy."
        show rowan necklace angry at midleft with dissolve
        ro "...!"
        ro "At least I am not begging them on bended knee, prostrating myself like a common whore, praying that their ‘toy’ chooses them to be the latest of their easily-discarded allies."
        arz "Oh, Rowan. Now you’re just making me blush."
        arz "I think we’re going to get along just fine."
        $ arzylDialogueStage = 2
        return


#############################################################################################################################################################

label arzyl_nileth:

$ arzylDialogueStage = 3

scene bg9 with fade

"Rowan awoke in the middle of the night to the sight of pale, glowing eyes staring at him in the dark."

show rowan necklace naked concerned behind bg9

ro "{i}Guh!{i}"

hide rowan
show rowan necklace naked concerned at midleft with dissolve

"He leapt out of bed, his heart pumping as the figure in the darkness snapped her fingers. A purple, flaming light erupted in the palm of her hand, casting her face in the cover of flickering shadows."

show arzyl neutral at midright with dissolve

arz "Rowan. Come. The Midnight Court has need of you."

show rowan necklace naked angry at midleft with dissolve

ro "What the {i}hell{/i} are you doing in my room at this time of night?!"

arz "There is no time. I heard a psychic call upon the wind. My acolyte, Nileth is in trouble."

show rowan necklace naked neutral at midleft with dissolve

ro "What are you talking about?"

arz "I dispatched Nileth to the castle to give him a report on the state of things with the Twins. But it seems he has run into a band of their Orc servants, near the base of the mountain."
arz "He thinks that they intend him harm. If we do not intervene now, there may be severe consequences… for everyone involved."

ro "Then go handle it! Why are you waking me up at Gods-know what time to tell me this?"

#show arzyl happy at midright with dissolve

arz "Oh, Rowan. I thought you’d know me better by now."
arz "If {i}I{/i} go down there, the only thing left in my wake will be bodies. As detestable as the Orcs are as a species, killing the Twins’ servants would not endear them to me much at all."
arz "Don’t you think a ‘softer’ touch is needed here?"

menu:
    "Yes.":
        $ released_fix_rollback()
        jump orcsNileth
        
        
    "No.":
        $ released_fix_rollback()
        ro "Deal with it your damned self, woman. It is the middle of the night."
        "If his anger had any effect on the pale elf, she showed no sign of it. Her lips curled into a smirk that sent a chill down his spine."
        arz "Very well Rowan, but do not come running to me if you do not like the outcome."
        hide arzyl with dissolve
        "With that, the witch disappeared, leaving him stood alone in his chambers. He didn't learn what happened that night, but in the morning he discovered two orcs were missing, neither were ever seen again."
        $ castle.buildings['barracks'].troops -= 2
        return

label orcsNileth:

show rowan necklace naked angry at midleft with dissolve

ro "All right! Damn it! At least let me get some clothes on!"

arz "Oh don’t mind me, Rowan! I’m just admiring the view."

ro "Ugh."

show rowan necklace neutral at midleft with dissolve

"Rowan threw on his travel cloak and shoved his sword into his belt. He kept his eyes upon the shifty Fae and her imperious smile, wondering to himself if this was just another in the long line of the endless mind games she loved to play on him."

#outside bloodmeen BG
scene black with fade

"Rowan followed the nebulous Fae’s instructions, picking his way down high embankments and rock-strewn crevices to reach the base of the mountain upon which the Bloodmeen Castle perched. As he reached at last a bend in the road he overheard the sound of voices."

show orc soldier neutral at midright with dissolve

os "Wots dat sound?"

show wild orc neutral at edgeright with dissolve

wo "Wot sound? You get nogged ur someden? Is just dis coward wimperin! Heh heh."

#nileth scared
show nileth neutral at edgeleft with dissolve

nil "You uncultured swine! S-stay back! I am the acolyte of Arzyl herself!"

os "Acka-who?"

wo "Wots an “Arr-zeal?”"

dag "She’s your worst nightmare, you green skinned gits!"

"Rowan’s eyes were drawn to the small, impish creature caught in the grasp of one of the Orcs. He was tiny, fitting into the palm of the creatures’ hand as he struggled in futility to free himself."

dag "Do as you please with that jizz-swilling toadie - Sol’s Bones, he may even like it! But leave me out of it, or Queen Kassandra will hear of this!"

os "Imp talks too much. {i}*Squeeze*{/i}"

dag "{i}Gak!{/i}"

nil "Please good sirs: I am a diplomatic representative, here to meet with the Midnight Court’s ambassador to the Twins, your mighty rulers."
nil "I only ask that you allow us safe passage, as becoming of a diplomatic mission of such importance."

wo "Hah! It talks more dan ‘da Imp duz!"

nil "...“it?”"

os "Da way ‘e uses his mouth, ‘e’s more girl than boy."

wo "Wot? It not girl? It {i}shaped{/i} like girl!"

dag "He’s got a {i}dick{/i}, you assholes!"

os "Yap, e’s a girl, no mistakin it."

wo "I dunt believe ya."

os "Well, dere’s only wun way ta find out!"

nil "Oh, goodness! I didn’t even lube myself!"

"The two Orcs chuckled, menacing upon the poor, Fae twink. Rowan saw his chance: the Orcs were distracted, too busy pulling aside their loincloths to bother looking in his direction. Rowan watched as Nileth halfheartedly shrinked back from the two of them."
"Rowan could take this opportunity to confront the Orcs and prevent any ‘harm’ from befalling Nileth (though truth be told: it seemed less ‘harmful’ and more sexual. And even Nileth didn’t seem {i}that{/i} frightened.)"
"As the first Orc produced his member, shoving directly in Nileth’s face."

menu:
    "Intervene.":
        $ released_fix_rollback()
        "Rowan gritted his teeth. He couldn’t just sit by and watch this helpless being be menaced by the Twins' lackeys. He stood to his feet, stalking over to the two Orcs as they loomed over the Fae creature."
        show rowan necklace neutral behind black
        ro "Stop!"
        hide rowan
        show rowan necklace neutral at center with moveinleft
        wo "Wot?"
        ro "What is the meaning of this? What are you two guards doing with that man?"
        os "E’s more of a girl than a git, boss."
        show rowan necklace angry at center with dissolve
        ro "I don’t care if he’s a bloody busty succubus! Unhand him immediately!"
        "The two Orcs shared an uncertain look, staring stupidly into one another’s eyes in hopes that the other might take charge and defy Rowan’s order. Seeing that neither was taking the bait, both stepped back from Nileth."
        dag "Finally! Someone with a lick of sense! Thanks, effeminate stranger!"
        "Rowan had to bite his tongue to not strike the impudent imp. Brushing aside the two Orc Guards, he knelt in front of Nileth, offering his hand to pull him to his feet."
        show rowan necklace happy at center with dissolve
        ro "I apologize for my master’s servants. They can be a bit energetic in their efforts to defend our borders."
        nil "Th-that’s quite all right, Sir."
        "Nileth’s face flushed and he glanced away, unable to properly meet Rowan’s eyes. It was vaguely charming. Rowan reached out and took the demon twink by the wrist, pulling him to his feet."
        show rowan necklace neutral at center with dissolve
        ro "I guarantee that you will not be accosted. Do you think you can reach your lady’s chambers from here?"
        nil "Y-yes, I can feel her presence. I uh… I don’t need an escort or anything."
        "Judging from the way he blushed, Rowan wondered if he was more terrified of Rowan’s presence than he was the Orcs'."
        ro "I am sure we will be seeing more of each other in the coming days."
        ro "Guards, I want the two of you to escort Nileth to Arzyl’s chamber and ensure he reaches there with no more… issues."
        "Rowan planted his hand upon the pommel of his sword."
        ro "If I find out that it was anything to the contrary, I will personally make a point of finding and punishing the ones who did it. Am I clear?"
        os "Yes, boss."
        wo "Count on us."
        show rowan necklace angry at center with dissolve
        ro "I don’t. But you {i}can{/i} count on the consequences. Now begone."
        nil "Thank you, Sir."
        show rowan necklace happy at center with dissolve
        ro "It’s Rowan. And it was my pleasure, Nileth."
        dag "Yeah yeah, let's get goin’ you glorified sex toy. Lady Arzyl’s lookin’ for us."
        "Rowan made a point to watch as the Orcs led their former victim back towards the Castle. He caught glimpse of Nileth stealing long glances over his shoulder before disappearing inside. He let out a sigh and resolved to keep a closer eye on the guards from now on."
        return
    
    "Stay hidden and see where this goes.":
        $ released_fix_rollback()
        "Rowan decided to observe the unfolding action, keeping hidden till he felt certain he should intervene. He watched as the two Orcs continued with their plans unmolested. The Orc not holding Daggertongue reached down and roughly fondled the androgynous Fae’s crotch."
        #cg1
        scene black with fade
        show wild orc neutral behind black
        show orc soldier neutral behind black
        #nileth aroused
        show nileth neutral behind black
        nil "{i}Ah!{/i}"
        wo "Hah! Its fer sure a ‘he!’ I felt his lil’ cock!"
        nil "Nnngh!"
        "The Orc continued to fondle the Fae, his leering grin growing as Nileth blushed and looked away. The other Orc let out a boisterous guffaw, holding up Daggertongue face to face with Nileth so that he could see his humiliation."
        os "Imp bitch get to see Fae bitch squeal!"
        dag "I’m gonna make you squeal out your {i}intestines{/i} once I’m done with y- {i}gak!{/i}"
        "As the Imp struggled in his new owner’s grasp, Nileth gasped, his girlish face twisting with repressed lust as the Orc’s hand began to move faster. He squirmed back and forth, but was unable to escape the creature’s thick hand."
        "He pumped him back and forth, his brutish fingers closing about the Fae’s crotch in a vice-like grip as the other Orc loomed over him."
        "Nileth’s pale eyes stared up, his lower lip trembling as the Orc pulled aside his loincloth, revealing the green, pulsating cock beneath. He was already rock hard, his erection jabbing forth to poke Nileth in the cheek. The pale-skinned trap let out a simpering wimper."
        #cg2
        scene black with fade
        show wild orc neutral behind black
        show orc soldier neutral behind black
        #nileth aroused
        show nileth neutral behind black
        os "Time fer sum fun."
        "The Orc took himself in hand, laughing as he began to jerk in front of Nileth’s face. Emboldened by his companion, the second Orc soon followed suit: releasing Nileth’s pitifully small cock as he ripped his own loincloth clean off. Nileth shivered, the air heavy with the musk of superior masculinity." 
        "Nileth’s face was red, his eyes flicking back and forth from dick to dick as he licked his luscious, cocksucking lips. There was a low heat in the air, a sort of erotic tension that made the scene seem less like an inflicted punishment and more a debauched fantasy of domination."
        "Even Nileth was rock hard, his cock pointing straight up from his outfit."
        wo "You like dis, girl?"
        nil "N-no! And I’m a man!"
        os "Mmm, yeah ya do. Lick it, girl."
        "The Orc responded to Nileth’s protestations by rubbing his dribbling cockhead across his face. Nileth grimaced but did not push him away, groaning as the Orc spread precum under his nose."
        "Against his better judgement Nileth took a deep whiff, shuddering as he planted a short, hesitant kiss upon the cock."
        os "Dats right. You like bein held down, dontcha?"
        nil "No… n-no I don’t…"
        wo "She’s a shy one. Wot say we give her wot she wants?"
        #cg2 - cumshot
        scene black with fade
        show wild orc neutral behind black
        show orc soldier neutral behind black
        #nileth aroused
        show nileth neutral behind black
        nil "Eeek!"
        "Nileth closed an eye as a long string of pearlescent spunk squirted up along his face. The second shot threaded across his nose, his downcast eyes squeezing tight to keep the sloppy load from getting in them."
        "The Orcs grunted, their heavy breathing heralding new jets of cum to come roaring forth. Soon Nileth’s face was caked in the stuff, the shameful residue of stronger males coating him like a lurid christening. He groaned, unintentionally licking his lips and getting some of the creamy cum on his tongue."
        os "She looks good dis way."
        wo "You ever want to come ‘round here again, you just ask."
        nil "I-I… I wont…"
        os "Heh. We heard dat one before."
        "Laughing, the two Orcs unceremoniously dropped the struggling Imp to the ground and left, whistling an off-key tune as they moved on with their patrol."
        "They did not spare so much as a half-glance in the direction of the thoroughly-humiliated Fae, who picked himself up off the ground only after waiting to be sure that they were gone."
        nil "Ugh… mmph. S-stupid Orcs."
        nil "...What’s Arzyl going to say? I couldn’t even take on a pair of brutes!"
        dag "I dunno dick-lips, but you can be damn sure {i}I’m{/i} not getting in trouble with this!"
        "Realizing that his opportunity to intervene had come and gone, Rowan wisely decided to simply fade back into the brush. At this point, it was probably better to tell Arzyl that he simply wasn’t able to find the Fae twink at all, otherwise he doubted she’d take kindly to him in the future for letting it happen."
        return


###############################################################################################################################################################

label arzyl_isdruel:
    
scene bg13 with fade

"Rowan entered Arzyl’s dank chambers, the dying candles casting the room into a murky darkness like the inside of a witches cauldron. He found the Fae pacing the room, a tense expression across her ageless features."

show rowan necklace neutral at midleft with dissolve

ro "Hello again, Witch."

show arzyl neutral at midright with dissolve

arz "Give me a moment, Rowan. I am just about to receive word."

ro "...Word of what? From who?"

"Before Rowan could inquire further, there was a flash of light. Suddenly, a note was in Arzyl’s hands. It was sealed with blood-red wax, an unintelligible symbol gracing its back that looked vaguely like three moons interlocking with one another."
"With a single, long {i}rip{/i} of her nails, Arzyl broke the seal. A small fount of magical power erupted out from beneath the seal, melting the wax away in a single instant. Arzyl folded open the letter, her glowing eyes skimming across its length as she read."

arz "..."
arz "I have been summoned by her Flawlessness, Queen Kassandra herself. It would appear that it's urgent."

ro "It must be, if she’d dare to send a sealed letter into the Twins’ own fortress."

"Arzyl spared a half smirk in Rowan’s direction before she began to pace the room once more."

arz "I never pass up a chance to meet with my beloved Queen. However, this does complicate matters a bit."
arz "Another member of the Court is headed here to the castle as we speak. I was supposed to meet her at the gate to ensure safe passage… unlike my sweet Nileth."
arz "She is being ‘delivered’ here soon."

ro "...Delivered?"

arz "The Midnight Court boasts many different kinds of Fae within its ranks, Rowan. She just happens to be more - {i}eccentric{/i} than most."

ro "Given what few Fae I’ve met who are a part of the Midnight Court, that’s saying something."

#arzyl happy
arz "Oh Rowan, you should know by now that I’m the most eccentric Fae you’ll ever meet! Isdruel just happens to be far less dignified about it than I."
arz "As a result, the Queen and I decided we needed to use some discretion in getting her here."
arz "But now the Queen wishes to speak to me! And I am quite loathe to deny her wishes. Would you be a dear and meet my sister Fae at the gate when she gets here? "
arz "I shudder at the thought of what she might do if she’s left… unattended."

ro "Well, I-"

arz "Oh! There is my Queen calling now!"

"Before Rowan could respond, a sudden blast of light blinded him. A swirling maelstrom of energy erupted from the ground at Rowan’s feet, a gleaming portal into Gods-know what. With a wink and a wave Arzyl stepped onto its surface, sinking like quicksand as the eldritch energy engulfed her."

arz "I promise I won’t be long, Rowan…"

hide arzyl with dissolve

"Her otherworldly smile stays in Rowan’s mind long after the ground swallowed her into nonexistence. He stood there for a moment in her room, contemplating his options."

menu:
    "Help Arzyl.":
        $ released_fix_rollback()
        jump helpArzyl
        
    "Don’t involve yourself.":
        $ released_fix_rollback()
        "Considering his options, Rowan decided that this was a classic example of ‘none of his business.’"
        "Given the Midnight Court’s disturbing propensity for sadism and cruelty, the thought of helping Arzyl ‘retrieve’ a servant deemed dangerous enough to have to send them in a sealed box set off warning bells in his head."
        "Rowan shrugged to himself, resolving to let the situation work itself out."
        return

label helpArzyl:

"Considering his options, Rowan decided that learning more about the Midnight Court and their baffling ways was worth the potential blowback of whatever Arzyl had just saddled him with. Besides: what’s the worst that could happen?"
"Rowan did his best to ignore the pit in his gut as he considered the actual implications of the question."

scene black with fade

"Hurrying to catch this newcomer before she waltzed in the front door unattended, Rowan reached the front gate of Castle Bloodmeen in record time. What he found waiting for him shocked him."

show rowan necklace shock at midleft with dissolve

ro "W-what the hell is going on?!"

"True to Arzyl’s words, her companion had been ‘delivered’ to the front gate in what appeared to have once been a sealed, runic crate of alien design. Rowan could see the shattered splinters of the thing lying in shards across the ground, its occupant now stood at the entrance, a picture of rage and spite."
"The pair of Orcs guarding the gateway had inadvertently opened the crate without asking permission, freeing the being within from her interminable confinement. Now free from her shackles, the bark-skinned creature had enacted her vengeance upon them."
"She was a creature of wood and vine, leaf and root. Her eyes were the color of sap, her hair like knotted brambles tangled together, her lips a curling, contemptuous oak. Though her body was feminine and curvaceous, she looked more akin to a living growth than a human."
"Her eyes swept across Rowan, a dark grin growing upon her lips. One Orc guard was laid out on the ground, his body splayed back with his eyes rolled into his head. Rowan bent down and checked the brute’s pulse. It was still going, if very faintly."
"The other Orc let out a roar of fear, dangling by the leg from a series of curling vines that emerged from the Dryad-woman’s body. Her cruel smile widened as she dragged a set of brambles across the struggling Orc’s body."

show orc soldier neutral behind black
os "Aaaaugh!"

show isdruel neutral at midright with dissolve

isdr "Yes, {i}yes{/i}! Feel it, you worm! Taste the delectable agony of my vines! "

"The Dryad rose up, floating upon a canopy of vines that bear her up to the high place she’s dangled the helpless Orc. The stupid creature flailed about, helpless in her grasp as she inflicted herself upon him. Her bark-encrusted hands roamed about the Orc’s green skin, pinching and groping at whatever struck her fancy."

isdr "You thought you’d use me, you little tick, didn’t you? First words out of your mouth when you saw me: ‘I’m gon’ fuck dat plant lady’ huh? Well {i}now{/i} who’s fucking who?"

"Her claws raked his back, the Orc twitching in place as he cried out in pain. Rowan winced. He approached the plant woman, whose amber eyes darted over to him as he approached."

isdr "Ah… Rowan. It has been a while."

show rowan necklace neutral at midleft with dissolve

ro "Have we… met?"

isdr "Oh, sweetling, you don’t remember your beloved Isdruel?"
isdr "That gang of villagers… that {i}brute{/i} with the crossbow and his army of lackeys who had stolen my sister’s mushrooms? Surely you’d at least recall the fight. "

if dryad_side == "isdruel":
    isdr "After all, you saved me like a blushing damsel in the fairy tales. You sexy thing."
    isdr "Arzyl really did give me a treat, sending {i}you{/i} of all people to greet me at the door!"

else:
    isdr "After all, you left me to fight those heathens on my own, despite their thieving manner."
    isdr "I did not expect a weakling like you to be the one Arzyl sent to fetch me."

ro "Well, she sent me. What are you doing to these guards?"

isdr "You mean these {i}brutes{/i}?!"

"Isdruel reached out, grasping the Orc’s upturned face by the chin as she leered down at his helpless expression. A dark smile graced her chlorophyllic lips."

isdr "I am teaching them some manners. Care to join in on the fun?"

show rowan necklace angry at midleft with dissolve

ro "I’ll pass."

isdr "A shame. Perhaps another time then. Something tells me that you could indulge in a bit of {i}domination{/i} better than most."

"As if to exemplify this fact, Isdruel let go of the Orc’s chin, her other hand curving around and slapping him hard in the face. The Orc wimpered, and Isdruel went eye to eye with him."

isdr "You. Do {i}not{/i}. Touch me without permission, worm!"

"She slapped him hard across the face again, her brambly vines dragging themselves across his back as the Orc’s face contorted in pain. There was a manic, almost sadistic look in the Dryad’s eyes." 
"Rowan felt a vague stirring in his gut: these were just Orcs, after all. Brutes who themselves had undoubtedly committed whatever atrocities they could in the early days of the Twins’ campaigns. Who was he to judge a bit of comeuppance? Then again, something about the Dryad’s pure malice made him feel…"

$ isdrWatchFailed = False

label isdrMenu:

menu:
    "Disgusted. Put a stop to this now, however you can!":
        $ released_fix_rollback()
        ro "Let the Orcs go Isdruel. {i}Now{/i}."
        isdr "Hehe, why?"
        "Rowan’s knuckles went white from his grip on his blade hilt. His scowl deepened as he saw Isdruel, her eyes matching with his, dragged her sharp fingernails down the Orc’s back in spiteful malevolence. Her smile widened as Rowan drew his sword."
        ro "Because if you don’t, I’ll hack you to pieces and use your bark for kindling."
        isdr "You flirt."
        "There was a long moment of tenseness, the two staring each other down as the Orc dangled in the air, whimpering in a desperate tone. At last Isdruel shrugged, her vines unravelling around the Orcs legs as he collapsed to the ground in a heap. Rowan did not let go of his sword."
        isdr "Funny, Arzyl said you {i}liked{/i} a girl who was into the rough stuff."
        ro "Then Arzyl is sorely mistaken."
        isdr "Or you’re just playing coy."
        isdr "...Fine, lead the way. But I don’t grovel to mortals. Arzyl’s going to get an earful about this."
        ro "I don’t doubt that for a second. Tell her I said she should fix her own messes, next time."
        isdr "If this is how you solve problems for Arzyl, I’m sure she’ll take you up on that offer."
        jump aryzlDialogueEnd
        
        
    "Impatient. Negotiate with the Dryad to let the Orc go.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        ro "Look, Isdruel-"
        isdr "Hold on a moment, Rowan. We’re just getting to the best part."
        os "Gaaaah!"
        ro "I get that these guards acted outside their station, but they are loyal soldiers of the Twins."
        show rowan necklace angry at midleft with dissolve
        ro "And if you think that torturing the servants of your would-be allies is going to secure their friendship, then you’re sorely mistaken."
        "Isdruel’s sap-colored eyes trailed across Rowan’s impassive expression, her smile widening as she winked at him, as if it were all just some perverse game she was playing. She gave her best pout and released the Orc, who collapsed onto the ground in a heap."
        isdr "Fine. I see your point. Arzyl would be quite cross with me if I messed up her little diplomatic excursion."
        "The viney creature sidled up to Rowan, her arms wrapping around his as if he were her escort."
        isdr "Shall we, Rowan? I hope next time we meet you won’t be so adverse to sharing little ‘fun’ between us."
        ro "Something tells me that your definition of ‘fun’ involves inflicting pain."
        isdr "Hehe, only on my inferiors. Who knows? Perhaps we can find someone mutually beneath us."
        jump aryzlDialogueEnd
        
        
    "Intrigued. Watch to see what she does." if isdrWatchFailed == False:
        $ released_fix_rollback()
        if avatar.corruption < 30:
            "Rowan heard the first sound of the Orc’s agony and felt a stirring in his chest. He couldn’t just sit by and watch this happen! He had not yet sunk so low beneath his own morality, that he could sit by and ogle another being’s pain."
            $ isdrWatchFailed = True
            jump isdrMenu
        else:
            "Rowan felt a strange sort of thrill watching Isdruel effortlessly torment the Orc. Despite his own misgivings, he found himself electrified by the sounds of the creature’s distress."              
            "Perhaps it was because of their ghoulish nature, or perhaps Rowan understood Orcs well enough to know that most of them were contemptible swine; either way, he could not bring himself to look away when Isdruel continued her sadistic vexations."
            "The Dryad lowered the Orc, his face level with her waist as she came face to face with his hanging junk. She reached out, her hands grasping the sexual organ with the curiosity of a child playing with a picked dandelion."
            isdr "Hm, so much fuss over so meagre an endowment."
            "Her hands began to roughly jerk him, her free hand reaching up to cup his testicles in a solid, tugging grip."
            isdr "Do you feel this, whelp? This is power. {i}This{/i} is control, not that banal bluster you and your friend were trying with me. That might make a mere mortal cower with fear, but I see it for the ruse that it is."
            "Her fingers clenched, and Rowan saw the Orc’s face contort with pain. She held him for a long moment in her crushing grip, his body trembling at the precariousness of his position. The Orc let out a cry of pain."
            isdr "I could eviscerate you in an instant, you filthy cur. Had I less important business to attend to for my Queen, I’d have likely done so."
            "The Dryad let the terrifying threat hang in the air for another long moment, then released her grip on the Orc, the vines holding up his legs and keeping him suspended in the air unravelling." 
            "The Greenskin let out a yelp of surprise as he toppled to the ground, landing in a heap on top of his fellow Guard. The two collapsed into a pile of pitiful moaning."
            "She turned to face Rowan, a brilliant, emerald smile spreading across her face. Without a word she took him by the arm and ambled forward into the Castle courtyard, humming a low, hypnotic tune as she moved."
            isdr "My apologies for being late, Rowan. I was held up by the Twins’ unruly servants. You know how mongrels can get. The weak and powerless covet that which they cannot have."
            show rowan necklace neutral at midleft with dissolve
            ro "Sure."
            isdr "I see you did not try to stop the theatrics! Could it be I’ve found a kindred spirit amongst the Twins’ misbegotten slaves?"
            show rowan necklace angry at midleft with dissolve
            ro "I am no slave, Dryad."
            isdr "Mmm, no. You’re not. I can tell. You’re something {i}infinitely{/i} more intriguing than that."
            isdr "I would like to discuss this more with you in the days to come. Perhaps next time you can be a more… {i}active participant{/i} in the fun?"
            ro "That depends entirely on where I am in that situation."
            "Rowan felt the Dryad’s grip tighten around him as her eyes held steady to him. Her smile widened."
            isdr "Oh don’t worry sweetling… you won't be the one dangling from my vines."
            jump aryzlDialogueEnd
            


label aryzlDialogueEnd:

$ arzylDialogueAvailable = False
return