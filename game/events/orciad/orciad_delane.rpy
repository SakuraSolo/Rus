label eleanorFirstVisit:

if delane_visit == 1:
    jump eleanorSecondVisit    

elif delane_visit > 1:
    jump eleanorRepeatVisit

else:

    pass

$ met_with_delane = True

scene bg26 with fade

"Rowan expertly approached the fake tent from the blind spot created when one of the guard posts changed shifts. At just the right moment, he slipped underneath the canvas while the orcs were distracted."

scene bg30 with fade

"Immediately he took stock of his surroundings, in case there were other guards inside, fortunately there were none."

show rowan necklace neutral at edgeleft with dissolve

"The large tent only had a small space someone could stand in, since most of it was taken up by a wooden building. The structure was larger than a simple shack, but much smaller than a peasant's house."
"A step up from a prison cell, but a far cry from quarters fit for the nobility."
"After doing a quick run around the perimeter, Rowan determined that there was one reinforced door, locked, and one barred window. Additionally, there were no guards inside the tent. The hero wasn't sure if that was for protection or secrecy."

show rowan necklace neutral at midleft with moveinleft

"Cautiously, he crept to the window and lightly tapped on its frame. A moment later a tentative feminine voice emerged from inside."

ele "Y-yes?  Who's there?"

ro "Rowan Blackwell, hero of Rosaria."

show eleanor rags concerned at midright with moveinright

"A moment after he spoke, a scared looking human woman in tattered clothes emerged from the shadows of the crude building."
"Without fancy clothing, jewelry, or styled hair, she looked no different from a comely peasant woman. However, Rowan could see the telltale way she bore herself that this was someone who held herself above others, even in her current state."

$ eleanor_name = "Delane"

ele "Rowan? I am Lady Eleanor Delane, heir to the Delane manor... or what's left of it. Have you come to rescue me?"

ro "Lady Delane."

"Rowan bowed his head respectively as he answered her."

ro "I am afraid that I am not here to rescue you, at least not yet. I came to confirm where you were held prison and ask out how you came to be in this place?"

show eleanor rags happy at midright with dissolve

"For a second a frown flashed on her face. But, she must have thought better of it, because she soon nodded and smiled softly."

ele "Missions of this variety take time, I understand. Nevertheless, it is good to see a friendly face. Or at least one not in a shade of green. Praise Solania, Praise Solania, for your arrival."

show eleanor rags neutral at midright with dissolve

"She took a deep breath to steady herself, then began recounting her story in as composed a manner as she could manage."

ele "My family, House Delane, are vassals of Duke Werden. Our holding is along the South-Eastern edge of the Rosarian Valley.  In the spring of this year, a group of orcs led by a monstrous beast set fire to our home and slaughtered many of our servants."
ele "At the time, I was out on a morning stroll in our gardens. I was only alerted to the attack when I saw the smoke, but when I tried to flee to safety I was unfortunately cornered by the raiders."

show eleanor rags angry at midright with dissolve

"She spat to the side."

ele "They came fast, carrying sacks of plunder from the manor and armor they'd torn from the bodies of our family's knights. The vile monsters. The vile monsters."
ele "Their leader, he dared to take the clothes from my body."
ele "Dared!"
ele "Had I not told them of my nobility and had they not decided to bring me back to their war leader, I can only shudder to imagine what would have happened to me."

"She glanced to the side blushing softly."

ele "That was when my one stroke of luck hit. The chief decided he wanted me for himself. Before the war leader could have me, I was taken here. Only by the grace of the goddess have I avoided being..."

show eleanor rags concerned at midright with dissolve

ele "...Well it would be unladylike to talk about such things."

"Her expression faltered and a quiver entered her voice."

ele "I know not what has happened to my family. I had seen what I thought was our carriage escaping, but I cannot know for certain."
ele "If you could tell me what happened...anything at all...I would be in your debt. A woman of house Delane always pays her debts."

ro " Has the older orc done anything to you since he brought you here? Ulcro."

show eleanor rags neutral at midright with dissolve

ele "Blessed be, no. He comes to see me on occasion. Bringing whatever passes around here for gifts. As though he could seduce a noblewoman with raggedy dresses and mutton."

"She raised a broken looking goblet and made a confused face."

ele "It a strange thing being courted by an orc. He has been my shield from those who would see worse done to me. Thus far he has been shockingly polite."

show eleanor rags angry at midright with dissolve

"An indignant edge filed her next words."

ele "But, I am a Delane. I am noble of the realm. Our arms have graced our banner for near a millennia."
ele "Does he expect me to cavort with a creature like him just because he gives me a nice cage? To fall to my feet swooning because he won’t take me by force?"
ele "Bah, even thinking about it makes me angry."

show eleanor rags neutral at midright with dissolve

ele "But hero Rowan, what of you?  Did you come to this orc warband seeking me?"

ro "I can’t say that I did."
ro "I came here for other business, but when I learned that the orcs were keeping a noblewoman prisoner I sought you out."

show eleanor rags happy at midright with dissolve

ele "It matters not. Whether you came here to rescue me or not, it is your mission now."

"Rowan opened his mouth to speak, but closed it before he answered."

ele "However, forgive me if I find it strange that you were able to safely sneak your way here. For now, I am unsure if I can trust you to bring me to safety or not."

ro "Have you ever heard the stories about what I did in the war? It shouldn't be too surprising that I was able to slip past orcs."

show eleanor rags neutral at midright with dissolve

ele "I am afraid that life in court forces us to be wary of deception and betrayal from every direction, even our closest friends. I know you certainly look like the hero of Rosaria, but how do I know you aren't some demon in disguise?"

ro "My lady, I-"

ele "Please don't take my suspicion personally.  I do genuinely appreciate having an actual person to speak to. This prison is... maddening and for all my other conversation partner’s eagerness, his wit leaves much to be desired."

show eleanor rags happy at midright with dissolve

ele "If you ever find yourself able, you must come and speak with me again."

show eleanor rags concerned at midright with dissolve

ele " But you should leave now.  It is almost time for the old orc to come see me, best if you're far from here when that time comes. I believe he plans to try reading to me today. Won’t that be...lovely..."

ro "Then I shall take my leave. Until I can return, goodbye Lady Delane."

ele "Farewell hero Rowan Blackwell. I await your return with bated breath. After all, what else do I have to do with my time?"

scene bg26 with fade

"The hero made a quiet exit and left the area as fast as he dared. Even still, there were suspicious eyes watching him so he would have to wait until next week to make another attempt to visit Delane."

#Visiting noblewoman option is now listed as visiting Delane (disable for now).  Add note 7 to journal, mark note 6 as complete.
$ journal.add_quest_note('orciad', 'note7')
$ journal.complete_quest_note('orciad', 'note6')
$ journal.complete_quest_note('orciad', 'note4')
$ journal.complete_quest_note('orciad', 'note5')
$ delane_visit = 1

jump campMenu


label eleanorSecondVisit:

scene bg26 with fade

"Rowan approached the tent, where he had discovered that Ulcro had been keeping Lady Delane, for the second time. Last time, he had seen the guard patterns, so avoiding them and sneaking in had become a relatively easy task."
"On the hour, the orc guards lurched off in search of booze, and probably a women or two if they could find one." 
"The other guards were late, something Ulcro would no doubt not be too happy about  should he find out, and Rowan used their lack of discipline to sneak into the tent unnoticed."

scene bg30 with fade
show eleanor rags concerned at midright with dissolve
show rowan necklace neutral behind bg30

ele "Who’s there?"

ro "It is only me, Lady Delane."

show eleanor rags neutral at midright with dissolve
hide rowan
show rowan necklace neutral at midleft with dissolve


"The woman breathed a sigh of relief, Rowan could only assume she was worried about some other visitor."

ele "Ah, Rowan. Thank the gods. Another day without proper contact and I fear I might have started speaking in fractured sentences."

ro "You weren’t expecting anyone else, were you?"

ele "What’s there to expect besides more dreary misery?"
ele "I’m glad to see you though. Truly. I must admit, I was worried you wouldn’t visit again."

"Rowan did his best to smile at her. For all the signs of discomfort, even mistrust, in her shrunken posture, it was still easy to see the way her face lit up from even casual conversation. It brought back less than pleasant memories of his own time in the dungeons at Bloodmeen."

ro "I promised I would, did I not?"

ele "Perhaps. But, suspicion is conducive to endearing oneself to others. I had worried I might be left to my lonesome for my suspicions of your motives."

ro "Think nothing of it. In your position suspicion is not only natural, but it is to be advised. You had no proof if I was friend or foe, or even if I was who I said I was."

ele "{i}Still{/i} have no proof, I suppose."

ro "Exactly, so think nothing of it. Were our positions reversed, I’d be giving you a skeptical eye the entire time."

"Rowan noted to himself the wry irony of the statement. In his own prison, each and every visitor could easily have been some kind of seductive shape shifter. He’d barely trusted the mice on the ground."
"Still, his assurances seemed to cool the jittery noblewoman. She gave him a soft smile, that spoke of warming trust."

ele "Come, let us talk. If I don’t have something to keep my mind going, I might try talking to the chicken next. Please, you must tell me all about what is going on."

$ delane_visit = 2
jump eleanorMenu

label eleanorRepeatVisit:

if ulcro_path == 3:
    scene bg26 with fade
    show rowan necklace neutral behind black
    ro "There's no point visiting the tent when she's not there anymore."
    jump campMenu
        

else:

    pass

if ulcro_path == 2:
    if delane_gifts < 40:
        scene bg26 with fade
        show rowan necklace neutral behind black
        ro "I should acquire more gifts from around the camp before I visit Delane again."
        jump campMenu
    
    else:
        jump eleanorUlcroPath3

else:

    pass


if ulcro_path == 1:
    if delane_gifts < 20:
        scene bg26 with fade
        show rowan necklace neutral behind black
        ro "I should acquire more gifts from around the camp before I visit Delane again."
        jump campMenu
    
    else:
        jump eleanorUlcroPath2

else:

    pass

scene bg26 with fade

"Rowan sneaked past the guards stationed outside the tent with ease. It had become almost second nature to him now to slip past them in the dark, and gain access to where they were keeping the lady Delane prisoner."

scene bg30 with fade
show eleanor rags happy at midright with dissolve
show rowan necklace neutral at midleft with dissolve

"She saw him as he pulled apart the lining of the tent to enter, which brought a smile to her face."

ele "Rowan!"

ro "My lady."

ele "Thank the gods. I was starting to go mad. What brings you to my...humble abode?"

jump eleanorMenu


label eleanorMenu:

menu:
    "Gain her trust.":
        $ released_fix_rollback()
        jump eleanorTrustMenu
        
    "Convince her to Accept Ulcro.":
        $ released_fix_rollback()
        jump eleanorUlcroPath
    
label eleanorTrustMenu:
    
menu:
    "Talk to her about her captivity." if delane_captivity == False:
        $ released_fix_rollback()
        ro "I trust the orcs are still treating you well?"
        ele "Yes yes, as if the brutes would lay their hands on me with their lord salivating over me like a dog."
        show eleanor rags concerned at midright with dissolve
        "A look of concern crossed the young woman’s face."
        ele "I admit that I have worries of what will happen when he realizes what he desires is an impossibility."
        ro "You mustn't lose hope, M’lady. You are not without friends on the outside."
        ele "Hrm."
        show eleanor rags neutral at midright with dissolve
        "She slouched back against the back of her enclosure and crossed her arms. She didn’t respond, but she still was clearly chewing on his words."
        ele "Other than that, it has been dull. Excluding yourself, most of the louts are not even allowed to visit me. The one who delivers food is the closest thing to a person I regularly see."
        ele "The most I get in the way of conversation is an angry grunt though, I’m afraid."
        ro "Orcs aren’t the mostly friendly people even at the best of times."
        ele "True, although it is the boredom more than anything that gets to me. People are tolerable, but I’d kill for a book. My father told me that books are how you sharpen the mind, and all this lying about has me dull."
        ro "I’ll see what I can do, but you’ll have to find somewhere to hide it. Wouldn’t want them to know that someone has been in here, after all."
        ele "Of course, I have just as much interest in seeming the good little captive to Ulcro’s eyes as you. More probably."
        ro "Of course, My current home castle has a rather large library, I doubt it would miss a book or two. And I’ve been involved in much more challenging smuggling operations, I assure you."
        ele "Current home castle? Somewhere nearby?"
        ro "It’s a longer story then I can tell, my Lady. My current benefactors might not be so keen on me sharing such details with someone the orcs can torture information out of."
        "Delane huffed and gave him a skeptical look."
        ele "I suppose I understand the need for discretion. The lady above knows I’d do the same in your shoes. Besides, if you bring me a book, it could be from Karnas’ personal vault and I wouldn’t complain."
        "There was a long pause. Lady Eleanor was collecting herself, or perhaps deciding what to say next."
        ele "Tell me, Hero Rowan, did you spend much time reading?"
        ro "Reading? Hrmm. Well I’m capable of it. And I’ve read books before. Though, in my line of work, troop details, scouting reports, and the like are more common."
        ro "But, a lifetime hunting, then soldiering didn’t leave me much time to get lost in books."
        ele "I see. I suppose that makes sense."
        ele "I used to think I’d go mad without reading material. I was only half right. But, in all my days, growing up to the court of Rastadel I never went too long without taking a pause to read."
        ele "It sharpens the mind, a lady’s only weapon. And it allowed me to escape the dreariness of my surroundings. It let me escape the everyday world for a little while."
        ele "It’s funny is it not? The time I need to escape most is the time when I don’t have any books."
        ro "But, by that logic, isn’t it funny that the people who need to escape most, the small folk, are the ones who have the least access to them?"
        ele "Hrmm. I’ve never considered that."
        "They talked about other things for some time after that, but like on all other occasions there was only so long he could stay."
        ro "I’d better go, the sun will be up soon and the guards will be coming in to check up on you."
        ele "I wish that wasn’t the case."
        ro "I know, but don’t worry, I’ll be back to visit you soon."
        ele "Goodbye, Rowan."
        ro "Until next time, my lady."
        "He flashed her a smile, and lifted the tent side, before ducking out and disappearing into the cool, morning air."
        $ delane_captivity = True
        $ delane_trust +=1
        $ last_delane_visit = 1
        jump campMenu
        
    "Talk to her about her current affairs." if delane_affairs == False:
        $ released_fix_rollback()
        ele "Tell me, hero Rowan, is there any news from court? Back a my family estate, I always did so enjoy the latest gossip. Entertain me."
        ro "I’m afraid that I can’t say that I have. I’ve never been quite involved in those sorts of affairs. I am just a commoner after all."
        ele "Is that so? But surely you know some nobles? You’re the hero of the realm. If a single commoner was to know something, it would be you."
        ro "I know many nobles, but I never picked up their taste for petty squabbles. After the war, I didn’t much keep in touch with them."
        ele "I will have you know there is no joy in this world quite as sweet as petty squabbles."
        ele "Still, you haven’t spoken to any nobles since the war?"
        
        if goal2_completed == True:
            ro "Well, I have seen Lord Raeve..."
            ele "Lord Raeve. What a… pleasant man."
            "Delane coughs into her hand brazenly. As though to get the lie out of her mouth."
            ele "But, some news is better than none I suppose. What is the word from Raeve Keep?"
            ro "Bad. The only gossip worth spreading is that Raeve Keep has fallen. Duke Raeve is a prisoner of the demons who took it."
            ele "Uch. Terrible. Just terrible."
            ele "What of his niece? I knew Helayna Raeve, if only on an acquaintance level. More interested in playing with the boys then me or my sisters, but she seemed the good sort."
            ro "Helayna is safe, I’ve seen her with my own two eyes not too long afterwards."
            "Eleanor let out a sigh of relief. A natural response. Good news was scarce around these parts."
            ele "I remember that Doran was always trying to marry her off to advantage himself. The gossip of last year was she would try to pair her with Lord Larkspur’s son. Dumb match. Weak man. She’d have eaten him for dinner and asked for seconds. "
            show rowan necklace happy at midleft with dissolve
            "Rowan smiled, remembering how she would chase the boys off with a wooden sword when she was younger."
            ro "She is quite a fearsome woman."
            ro "Or at least she used to be…"
            show rowan necklace neutral at midleft with dissolve
            "He thought of the effects on Helayna since she first put on the ring. Certainly the Helayna of these days couldn’t hope to match her former self in the field."
            ele "Did something happen to her?"
            ro "..."
            ro "As I said. She’s alive."
            ele "I see. My apologies. You know her well I assume?"
            "Rowan nodded."
            ele "Well, so long as she is still alive, that’s all that counts. After all, your own visits help remind me that life continues apace, even if the only ones I have to gossip with are you and the rats."
            
        else:
            ro "I'm afraid not, since I returned from the war, I have spent all my time in the village with my wife."
            ele "That is a shame, good gossip is hard to come by."
        
        ele "Any other news? It doesn’t have to be court related."
        ro "Nothing good out in the fields. It has been another poor year for the harvest."
        ro "It’s looking like famine in unavoidable at this point."
        ele "I see..."
        ro "You know the nobles, what do you think they’ll do about it?"
        ele "It depends on the noble. All will make sure they have enough for their manor. Some will put the rest out to the peasantry, others will use this as an opportunity to increase local profits. Especially those who grow valuable crops."
        ro "Increase their profits?"
        ele "Profits are important. Profits are what kept the staff fed, and supply the arms and armor to fight off the demons. Perhaps if my family had profited a bit more, I wouldn’t be in this cage."
        ro "Perhaps, but such a mindset might see many people die who might otherwise have survived."
        "Rowan didn’t want to talk his own culpability in these matters. Even still, as he said this the matter weighed on him."
        "For her part, Delane didn’t have a response to this, but seemed deep in thought. She was a smart girl, and she was well used to having her world kicked out from under her by now."
        ro "I had better go, the sun is almost up and the guards will be here soon."
        ele "Please come back soon, Rowan. Even bad news is better than no news."
        ro "I will."
        "He left her alone to ponder what she had learned, as he slipped out into the blackness of pre-dawn."
        $ delane_affairs = True
        $ delane_trust +=1
        $ last_delane_visit = 1
        jump campMenu
        
    "Ask about her life at court." if delane_court == False:
        $ released_fix_rollback()        
        ro "Tell me, I’m assuming that you spent some time at court in Rastadel, right?"
        "Delane raised an eyebrow. Though, it seemed to Rowan that something about her lit up in response to the question."
        ele "Oh, have you finally developed an interest in politics?"
        ro "Not particularly, but I thought talking about it might take your mind of things. For a little while, at least."
        "She turned away, he wasn’t sure if it was to hide her disappointment, or her response to his kindness."
        ele "I suppose the life of a noble isn’t very interesting to a soldier like you. Still, I admit it’s somewhat...thoughtful of you."
        ro "On the battlefield, there isn’t much time to worry about politics."
        ro "The generals play their little games, but we’re always too busy dying to notice much. There’s no time for it."
        ele "Perhaps you might find court life more familiar than you think. The movement of large armies may or may not affect you. But, you have to look in front of you. Get to caught up in a cause and you might wind up with a knife in your back."
        ele "Court politics is its own life and death struggle."
        ro "That doesn’t sound like a good thing."
        ele "Perhaps. But, you fight your war and we fight ours."
        ro "What do you mean?"
        ele "From a young age I was taught to see everyone else at the court as an enemy. In the place of swordsmanship and warcraft, we are taught diplomacy and seduction."
        ro "That sounds like a very lonely way to live."
        ele "It is…"
        show eleanor rags happy at midright with dissolve
        "A smirk crossed her face."
        ele "But, I was the best at it. I knew the right courtesies, had read all the books, and all the moderns styles. I was always three steps ahead of the competition."
        "She giggled."
        ele "I suppose it would have been some smelly orcs responsible for my downfall. No friend in the right place will save you from a raiding party unless that friend is Solania herself."
        ele "Still, it wasn’t all daisies and knitting. Love is completely out of the question, marriage is for strengthening political ties. The best you can hope for is a strategic partnership with somebody you can tolerate."
        ro "I’m sure you had a lot of suitors."
        ele "My parent’s wealth and power had lots of suitors. I was the pretty bow they came wrapped in."
        show eleanor rags concerned at midright with dissolve
        "All of a sudden her face turned white. She looked away weakly."
        ele "My parents...did you ever find out what happened to them?"
        show rowan necklace happy at midleft with dissolve
        "Rowan smiled."
        ro "I admit, I’m still unsure. However, i’ve heard talk that they may have appeared at court. If so then they most likely managed to escape intact."
        show eleanor rags happy at midright with dissolve
        "She turned back and forced a smile."
        ele "I’m sure that must be the case. Father would not let something as unseemly as a band of orcs bring him to ruin. Knowing him, he’s already making plans to rise again."
        ele "And if he’s bearing this, then so must I."
        ele "I am Lady Eleanor of House Delane. I will escape this."
        show eleanor rags neutral at midright with dissolve
        ele "...."
        ele "Thinking back on the life I lived before...it all feels so strange now."
        ro "Why is that?"
        ele "Everything about it. The fancy clothes, the large manor, my time at the court. All my petty victories at court had seemed so vivid back then and yet here I am. In a box."
        show rowan necklace neutral at midleft with dissolve
        ro "I can understand how frustrating this all might seem to you. The world is a cruel place. It takes away our choices from us."
        ro "I know that better than anyone. Better than anyone."
        ro "But, you must consider the other side of the matter as well."
        ro "If you’d been born as the daughter of some peasant girl, rather than a noblewoman, you probably wouldn’t be alive now."
        ele "Hrmm. I suppose that is true."
        ro "I’m not chastising you, I’m trying to tell you there are circumstances in this life that are already set in stone for us that we cannot choose."
        ro "But, these circumstances don’t last forever. You will get out of here, my lady. You will return to your family, or at least whoever is left of them. You will get to decide what you do with your life after that."
        ele "…"
        ele "I will consider that."
        show rowan necklace happy at midleft with dissolve
        "Rowan smiled warmly at her."
        ro "Good. Can’t have you giving up here. That would be unbecoming for Lady Eleanor of House Delane."
        show eleanor rags happy at midright with dissolve
        ele "Exactly. Now you get it."
        "The two spoke for a little while longer, though nothing quite as heavy as the topics already covered."
        ro "It is almost dawn, I’d better go before the guards arrive. I’ll be back soon."
        "With that he disappeared from her sight, slipping through a gap in the rear of the tent, leaving her alone to await a visit from her orcish jailers."
        $ delane_court = True
        $ delane_trust +=1
        $ last_delane_visit = 1
        jump campMenu
        
label eleanorUlcroPath:

ele "Did you desire to speak about something specific, hero Rowan?"

ro "Is the desire to give you a bit of company not enough? Surely besides Ulcro, there are not many friendly faces to speak to."

show rowan necklace happy at midleft with dissolve

"Rowan tried to put on his best charming smile, if only to hide his little nudge towards Ulcro. Not that Delane was fooled."

ele "Including Ulcro. I don't know what the old orc’s game is, but I prefer to keep a close eye on him."

"She clutched her arms to chest and looked to the side."

show eleanor rags concerned at midright with dissolve

ele "Tell me, is there any news of my family? Not knowing what happened to them is maddening."

show rowan necklace neutral at midleft with dissolve

ro "A little. I cannot promise much. I never knew them after all. But, I heard one “Sir Delane” had appeared at court of late."

"That much he’d been able to hear from, a supremely disinterested, Jezera. Apparently, he had become one of the leading voices for a more aggressive counter attack against the orcish bands."

ro "There also is no sign, either in camp or out, that the orcs managed to capture any of your other family members. None of the clothes you said they wore. No reports from other orcs of abducting other nobles."
ro "With the extent that you've become a prize, I'm sure you can imagine the ruckus another captured noble woman would have caused. I doubt that they could have cornered your family without anyone knowing about it."

show eleanor rags happy at midright with dissolve

ele "Thank the lady. At least, brother got out. At least. The line endures."

show eleanor rags neutral at midright with dissolve

ele "I will take that lack of knowledge as a cold comfort. My parents had a hidden second estate not far from the Blackholt."
ele "Perhaps they retreated there. It is only their power they have lost. Their pride."

show eleanor rags concerned at midright with dissolve

"Delane walked back to the edge of her dark cage and sunk down to the ground. Her hair covered her face, obscuring her eyes."

if avatar.corruption < 69:
    "Rowan’s heart sank. Everything this woman had ever known had been taken from her. Noble or not, he could see the same sorrow in her that he’d seen in people on their farmsteads when their villages had been destroyed."
    
else:
    pass
    
"Rowan reached through the bars and handed the noble woman a clean white handkerchief with frilly edges. He’d intended it as a small gift for her anyway."

ele "Thank you kindly."

ro "You're concerned with your family’s prestige? Even in this cage?"

"There was something almost obscene about the notion. There was no reason, after all, to assume that she’d ever even again be in a position where such things would matter."

show eleanor rags neutral at midright with dissolve

ele "Prestige. Power. All of it. All my life we've been a house in decline. Manor Delane was large, but it was ill placed. Where once we were a first rate house, now we are second rate at best."

"The most pathetic hint of a smile brushed over her lips. Or at least, as much of her lips as Rowan could see behind her hair."

ele "It was a good life nonetheless. Enough to allow me a spot a court in Rastedel, during the summers."

"She brushed her hair backwards, uncovering her face. With one last sniffle, she banished the last of her tears."

ele " I loved court, you know. The dresses and the pageantry, of course. But, most of all the dance of hidden daggers. The whisper wars for power. I don't think a peasant such as yourself could understand truly, but it was thrilling."

"Rowan had to hide a rye smile. “The dance of hidden daggers” as she had called it was his life at Bloodmeen."

ro "Of late, I find myself understanding more and more."

"Lady Eleanor breezed by his statement, seemingly totally unaware of its implications. She was lost in her own little world."

ele "Regardless even should I be freed, all of that is over now. A lady without an estate is no lady at all. At least not one who matters."

show rowan necklace happy at midleft with dissolve

"Rowan offered her a look of encouragement through the bars. To her, he was almost certainly a figure of hope. It would be better to use that. Perhaps to direct it in a way that would work towards his ends."

if avatar.corruption < 39:
    "At the moment, Lady Eleanor couldn’t know it, but she shared the same goal as him. Her freedom from this cage. But, there really was only one way to achieve that. Or at least, only one way to achieve that which Rowan could indulge in. She needed to learn to accept Ulcro. She needed to."
    
else:
    "The goal for Rowan here had to be transfering all of those longings for escape, as well as her hope that some famous hero would rescue her into Ulcro. She needed to see Ulcro as the key to her salvation. By whatever means necessary."

"Rowan paused to collect himself. Manipulating people. Corrupting people. All of this was a game he was new to with a very brutal learning curve."

ro "Take heart, lady Eleanor. There is still a place for you in this world yet. You will not have to rot away in this cell for long."

"He gave his best heroic wink."

ele "I should hope so. Madness will take me before anything else at this rate."

ro "Indeed. But, doesn’t Ulcro provide you with luxuries and treasures? I’m sure he’s no nobleman, but you are getting special treatment, after all."

ele "Hrmph. The orc attempts to."

"She held up the tattered edges of her dress. Once it might have even been pretty. But, with all the tears and patches, to call it a luxury was comedy."

ele "But, the operative word there is “attempt”."
ele "No green skinned brute could ever understand even one tenth of the needs and wants of a lady. "

"Lady Eleanor sneered. That almost sounded like a challenge. At the very least, her opinion of Ulcro would rise if she had more of her wants fulfilled."

ro "Perhaps, I could be of some help here."
ro " I’ve been sneaking around the camp of late, and have made a few contacts. Ulcro is mad for you. I imagine that the only reason he doesn’t pamper you is simply because he doesn’t understand what kind of gifts you’d want."

ele "Even if he knew, I doubt he’d be able to match my standards. The entire idea is absurd."

ro "You underestimate the power and reach of an orc chieftain. You’ve got this one head over heels for you. It would be a waste not to use it to try to make yourself more comfortable."
ro "Just tell me what sorts of things you might want, and we’ll see if the chieftain can get them."

"Lady Eleanor struck a mischievous look."

ele "Trying to milk the beast for all he’s worth, eh?"

if andrasIntroSex:
    "Rowan blushed ever so softly. The turn of phrase reminded him of some of his own recent exploits with Andras..."
    
else:
    pass
    
ro "In a manner of speaking."

"Delane sighted and approached the bars."

ele "It’s not the worst idea in the world. I doubt it will succeed. As if he could even afford what it would take to make me comfortable. But, it’s an honest attempt. Let me list a few items…"

"For the next half an hour, Lady Delane talked about all the things she might want. An outfit more befitting her person. Some of her jewelry, if the orcs had managed to take it. A proper bed and sheets for when she slept. Dishes and silverware that didn’t disgust her."
"Most pressingly, she declared, was her need for a way to pass the time. Books in particular were a favourite pastime for her, and the lack of reading materials was a source of constant consternation."

ro "I fear the sun will be up before too long. But, I will return to check in on you soon, my lady."

ele "And I will await your return with baited breath. One must have something to look forward to, after all."

$ ulcro_path = 1
$ jezDelaneHelp = "get"
$ cliohnaDelaneHelp = "get"


scene bg26 with fade
show rowan necklace neutral behind bg26

ro "If I'm going to convince her, I need luxuries. I should probably search the camp."

return

label eleanorUlcroPath2:

scene bg30 with fade
show eleanor dress happy at midright with dissolve
show rowan necklace happy at midleft with dissolve

ro "You’re looking in much better spirits, my lady."

ele "Looking much better is an accurate statement, though I think not just my spirits."

"Lady Eleanor gave a short twirl to show off her dress. The long skirt twirled in every direction. In truth, it lacked the crispness it might have had in a noble’s home where it could be better maintained. But, her brow was raised simply by its presence."
"Rowan chuckled and gave a small clap."

ele "It’s not enough, but it’s a start. A solid start. Even simply having something new and pretty to wear is enough to make me feel like my old self again."

"She walked back to the bars, soft smile framing her lips."

ele "I suppose it’s rather funny. I’m happy to receive beautiful clothes and splendid jewels, but I have no one to wear them for besides the orc."

"He raised an eyebrow."

ro "Perhaps you enjoy the way Ulcro looks at you in them."

show eleanor dress concerned at midright with dissolve

"Lady Eleanor turned her head to the side and straightened her posture defensively. It was like the very concept was an attack."

ele "Pishaw. You speak in absurdities."
ele "Though, you can hardly imagine the old hog’s face when he saw me in my new dress. I had been worried that my protector might have a heart attack then and there."

"A small grin flashed through her armor. Perhaps, even, a hint of pride."

show eleanor dress neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

ele "Alas, I don’t have everything I could want just yet. Books and games are in short supply. As are proper furnishings."
ele "It matters little if I look like a noblewoman again if I still have to eat with my hands and spend my waking hours staring at cage bars."

"Rowan nodded. Good work had already be done, but so long as she felt so much like a captive of savages, there was only so much progress he could make."

ro "I will put the word to my man on the inside. Regardless, I am happy to see the improvement in your condition."

ele "Indeed, indeed. And I have you to thank, at least partially. You may not be speedy enough in your escape efforts, but I owe my new comfort here to you, at least."

show rowan necklace happy at midleft with dissolve

"Rowan bowed slightly."

ro "I just nudged along the process. You underestimate your potential influence here. You’ve got this orc leader wrapped around your finger. And he has an army thousands strong."

show eleanor dress happy at midright with dissolve

"Delane huffed, but she was easy prey to a compliment. Rowan had been complimenting these noble types his entire life when he was forced to. It was not so different from the demeanor he was forced to take with his own commanders in the war."

ele "Hrmm. That is no lie."

ro "Besides, have you seen the way the other human women around camp are treated? I assure you, ladylike is no proper word for it."

"How did the lady feel about the prospect with sex with an orc?"

if avatar.corruption > 39:
    "A flash of Jezera went through his mind. It was as though she was advising him to just throw her in a pile of orc cocks and see if she took a liking to them. There was an appeal to the...simplicity of the idea, to be sure."
    
else:
    pass

show eleanor dress aroused at midright with dissolve
show rowan necklace neutral at midleft with dissolve

ele "I see nothing in my gilded cage. But, I hear it. The sound at night are often quite loud. More then one night, I have been prevented from sleeping because of the...moaning."

"She clutched her body tightly, and looked away. A short jerk traveled down the length of her body. A shiver perhaps?"

ele "I’m sure if I spread my legs wide enough, my “generous” benefactor would attempt to wrench the same sounds from me."

"Her voice was half a sneer, but he couldn’t help but notice the fact that sex was where her mind went first. But, he also couldn’t help but notice the strange fact that he picked up at all."
"Jezera really was rubbing off on him."

ro "Perhaps. But, there’s a difference between treasured concubine and a common whore."

ele "Hrmpph. From the way you speak of the man, I half suspect you of working for him."

"There was a second where Rowan panicked. Had he really been found out? No. She was probing. He just needed to remain confident."

show rowan necklace happy at midleft with dissolve

ro "Ulcro is rich, but he cannot afford the rates of the hero of the realm."

"He chuckled playfully. That seemed to put her at east, if only as much as the topic would allow."

show rowan necklace neutral at midleft with dissolve
show eleanor dress concerned at midright with dissolve

ele "Clearly. Still, I may understand the distinction. At least consciously. But, I was there at the fall of the manor. My...honour may be intact, but the same can’t be said of my former ladies in waiting."

"If she looked uncomfortable before, now she looked positively panicked. This topic was very far out of her element."

ele "I admit, there was something uncomfortable about their screams. They were not entirely in anguish."

show eleanor dress aroused at midright with dissolve

"She turned back to him. Her cheeks were burning."

ele "Tell me, hero Rowan. You’ve been around camp here. Seen the state of affairs. The human women they keep...do they enjoy their captivity here? And the activities they participate in?"

"Her lip quivered."

ele "I worry, you know. For my former ladies-in-waiting. I can only imagine how Adelana Indigo is adjusting to her own captivity."

"Rowan’s mind raced. This was exactly the opportunity he needed to seize. That was certain. But, his voice started to shake at first."

ro "In truth, I have heard that most of the women who find themselves having relations with the orcs eventually grow to like it. If you’ll permit a bit of impoliteness from a peasant such as myself…"

ele "Permission granted."

"He breathed in softly. So far she seemed less to notice his nervousness, and was more focused on his words. That was a reprieve of sorts in of itself. It meant he had a chance."

ro "From my understanding, human women are not initially accustomed to the...girth of orc lovers. But, size is associated with pleasure. So, once they learn to accommodate such things, there is even talk that they surpass human lovers in pleasure."

"Delane stared at him with wide eyes. When he finished, she could barely form words."

ele "Oh."

"She paused."

ele "Then I suppose I will count Adelana and the rest lucky for that small reprieve."

"The topic of conversation from there was mostly little things. The dailies of camp life. Rowan talking in small detail about the world outside the bars. Nothing of great import. All of the important steps had already been taken."
"Rowan left the tent that day with an enhanced confidence. A few more gifts. A little bit more persuasion. That would be all it would take to bring her to acceptance. He was strangely sure of it."

$ ulcro_path = 2

scene bg26 with fade
show rowan necklace neutral behind bg26

ro "She's getting closer, but it'll probably take a bit more to convince her. I should keep looking for more gifts to sway her."

jump campMenu


label eleanorUlcroPath3:

scene bg30 with fade
show eleanor dress happy at midright with dissolve
show rowan necklace happy at midleft with dissolve

ro "You look happier still. It’s rare to see a prisoner grow brighter as her captivity continues."

"Rowan looked on as Lady Eleanor sat on the floor of her cell, flipping idly through a book."

ele "I will admit that the introduction of some reading materials to my repertoire of activities has done a wonder for my mood."
ele "Perhaps, the history of farming is not the most riveting of topics. But, I have already asked Ulcro to bring me any other books he finds."

"She placed the book to her side and rose to her feet."

ro "And you have no further doubts about Ulcro’s abilities to furnish you, I see."

ele "It’s not manor Delane. But, of late I’ve been quite happy here. I’m sure that mother and father would laugh at that mere notion. A lady of house Delane humming along happily in an orc’s cage."

ro "Perhaps, perhaps not. After all, with but a grasp of your hands, you could be more powerful than your father ever was."

show eleanor dress aroused at midright with dissolve

"A puzzled look crossed her face. Then she understood his implications. Once more a blush crept on to her cheek."

ele "You mean if I...consort with the orc."

ro "I’m not suggesting that you do. He’s quite ugly, I understand. But, if your concern is power and prestige, then you strike me as being in a paradox of sorts."
ro "You’re here in a cage longing for power and influence. But, with a word you could be the queen of an army far larger than anything your father could ever muster. The undisputed mistress of an entire clan."

show eleanor dress angry at midright with dissolve

"She turned her back, twirling her skirt in the process. Then made a high pitched noise to signal her disapproval. Everyday more of her noble demeanor had seeped back in."

ele "And resign to spend the rest of my life in said cage? Bah."

ro "The creature adores you. If you insisted on your freedom, I doubt he’d hold you any longer."

"That was when an idea struck him. Delane still acted as though sitting around waiting until someone, probably him, freed her. Perhaps with a starker understanding of her situation, she might be more inclined to cling to Ulcro."

ro "Besides, surely this cage is better than the one Batri would put you in."

show eleanor dress concerned at midright with dissolve

ele "Batri?"

"Her eyebrows narrowed."

ele "I’ve heard of him. Ulcro speaks of him from time to time. But, so did my initial captors. What about him?"

ro "You know he aims to usurp Ulcro. Of late I’ve been suspecting that without your intervention he might just succeed."

ele "My intervention?"

ro "The chief is strong, but he’s not all there anymore. He needs a fire inside of him to fight for his position. And you’re what he has come to care about most."

show rowan necklace neutral at midleft with dissolve

"He sighed and shrugged his shoulders, trying to adopt a more defeated expression."

ro "In truth, perhaps I am trying to sway you to Ulcro’s side, at this point."
ro "But, my aim has always been your safety. I had hoped to secure your rescue at first. But, that seems increasingly unlikely. And with Batri’s challenge growing ever more present, I fear Ulcro’s downfall."
ro "And if he wins. He will take you."

show eleanor dress concerned at midright with dissolve

ele "And if he does that, what will he do to me?"

ro "My mind does not work like that of an orc. But I can only imagine it will involve nothing less then copulation in the middle of the camp square."

show eleanor dress aroused at midright with dissolve

"She gasped loudly and put a hand to her mouth. Yet, there was that same shortness of breath and blush that he’d noticed in the prior conversation. The idea of sex with an orc was clearly having some effect on her."

ro "My lady, you don’t look at appalled by the idea as I would have expected."

ele "I-"

"She straightened herself up, realizing how she must have looked. There were a few half-hearted attempts to explain her demeanor, but none of them got off the ground. At last she resigned herself to admitting the truth."

ele "I suppose the thought has been on my mind of late."
ele "I am about to reveal something to you that cannot be spread about. I have a reputation to consider. You must swear to me my words will remain here."

ro "On my life."

"He bowed his head softly. A traditional gesture of submission."

ele "Okay."

"She took in a deep breath."

ele "Ending up the prisoner of orcs is...well, you could call it an ironic fate if you were to use the term incorrectly. When I had been a younger lady, I had been beset by fantasies of being…"
ele "...ravished, by creatures of the sort. Now they were just silly girlhood nocturnes, you understand. Well pressed away by the time I reached maturity. It was improper for a lady to even think of such thing."

ro "But, being in their captivity, the thoughts have returned. Is that what you’re saying?"

ele "From time to time. I’ve imagined what would happen if I agree to the proposal. Or if the ravagers from before had gotten their way."

show eleanor dress neutral at midright with dissolve

"Rowan paused to consider this latest gift to him. Sexually interested in orcs. Afraid of Batri. Eager for power and influence. Appreciative of Ulcro for material comforts. All she needed was a final push."

ro "My lady. There is a simple answer to your situation. I do not believe I can free you. But, you can still have the power and prestige you crave. Accepting your lusts does not have to mean the break of your pride."
ro "Become Ulcro’s lady. Rule at his side. Be his queen. It is the best recommendation I can give you in this thing. It is the only viable path."

"Delane went silent. She didn’t seem to outwardly accept his statement. But, at the same time, the refusal or ridicule of the idea that she would have once given was gone."

ele "Thank you for your advice, hero Rowan. And for your discretion. I will consider my situation carefully. "

"She was so close to acceptance, he could almost taste it in the air. Maybe one final push..."

ro "You are a Lady of the House Delane. You are not the prisoner to circumstances. You still have choices. What you choose could decide the future of your entire house."
ro "Pleasure. Power. Luxury. All of it can be yours, and in so doing your ancestors would be proud."

"She didn’t reply to this idea, either. At least not overtly. But, her head bowed darkly."

ele "I understand."

"Just like that the conversation ended. There was no more point in pleasantries. Rowan said a quick goodbye, explaining the sun was rising. She quietly nodded along as he left. Her mind had other places to be."
"Rowan would need to check in with Ulcro the next opportunity he had. By then, his plan may have already been successful."

$ ulcro_path = 3
$ journal.complete_quest_note('orciad', 'note14')
$ journal.complete_quest_note('orciad', 'note16')
$ journal.add_quest_note('orciad', 'note28')
jump campMenu
