init python:

    #requires 3 abbeys to have been visited - TODO
    event('the_faithful_caretaker', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)
    event('abbey_cliohna', triggers='map_res_19', group='map_res_abbey', run_count=1, priority=pr_map_res)
    event('abbey_first', triggers='map_res_19', conditions=('week > 3',), group='map_res_abbey', run_count=1, priority=pr_story)

label the_faithful_caretaker:

#abbey BG
scene black with fade

$ garin_in_rastedel = True

"Another day, and another abbey lingered on the horizon."
"But this time Rowan did not contact Cliohna immediately. Something didn’t feel right about it…"
"Trusting his intuition, the hero approached it slowly."
"The area was quiet. Devoid of signs of human activity. They abbey garden, usually the pride of many temples, now laid unattended. The heavy doors to the temple interior, during the day always open to welcome incoming faithful, were now closed shut."
"Was the place abandoned? If so, it couldn’t have happened recently, it was still in good condition... Which also made an enemy raid unlikely."
"The mystery would not solve itself on its own, and it would be sloppy work on his part to send his orcs in blindly. Making his decision, Rowan pushed the front gate open, and entered the building."
"As expected, the large, octagonal hall laid empty, not a single soul around. Many of the religious paraphernalia – paintings, cups, holy symbols – were also missing."
"But again, no signs of battle."
"The abbey was evacuated-"
"-but not entirely."
"Rowan brushed the surface of a nearby sculpture. It was clean – without a speck of dust on it."
"Someone still looked after the abbey, even if only after the interior."

if all_actors["kharos"].favors > all_actors["solancia"].favors:
    "Determined to get to the bottom of things, Rowan crossed the hall, passing by the altar and heading to one of the side exists."
    
else:
    "Determined to get to the bottom of things, Rowan crossed the hall. When he reached the altar, he knelt for a moment, and spoke a couple of words to Solansia in a quick prayer. Then, he headed to one of the side exits."
    
"He passed one room after another. All were deserted, stripped of anything of value, but still clean. Whoever the caretaker was, did not slack off."
"In fact, as Rowan learned upon entering the abbotts office, he was working at the very moment."

show rowan necklace neutral at midleft with dissolve

"The caretaker proved to be a lively old man, almost entirely bald, with but a few gray strands of hair on his head. Humming an old song, he was dusting a now half empty bookshelf."
"The office was also stripped of anything of worth."
"Though maybe it had some sentimental value to some."

ro "Excuse me?"

care "Oh!"

"The man gasped in surprise, and turned around to face the unexpected visitor."

care "Ah, hello, young man! Come, have a sit."
care "You have my sincerest apologies, but I’m afraid there will be no sermon today. Or in the near future."

"The man smiled sadly."

show rowan necklace happy at midleft with dissolve

care "But I can make you some tea, if you’d like to?"

ro "No, thank you. But can you tell me what happened here? Where is everyone?"

show rowan necklace neutral at midleft with dissolve

care "They left."

"Rowan watched as the caretaker returned to his duties, voice serious as he explained the situation."

care "Things haven’t been too well recently. Pilgrims kept talking about orcs raiding the countryside, driders coming out of their lairs, and the kind."
care "People stopped feeling safe. Some tried to find protection here, but…"
care "… Reverend Garin said the abbeys weren’t safe either. One was burned down. Another stopped responding to letters, and when he sent some acolytes to check it, they said there was something wrong with it, but they were too afraid to enter it to confirm."
care "So he packed his stuff and left."

"The man’s hand stopped, as if he was struggling whether to continue or not."

care "And that’s the gist of it."

if avatar.corruption > 74:
    show rowan necklace angry at midleft with dissolve
    ro "Rowan scowled. Great. The abbey was all out of slaves, valuable tomes, and riches. All it had was one decrepit old man."
    "Not that he would be of much use. Rowan doubted that for all her decadence Jezera could possibly have a fetish for old men."
    "… Probably."
    show rowan necklace neutral at midleft with dissolve
    ro "I see. I’ll leave you to it, then."
    care "You sure you don’t want to-"
    show rowan necklace angry at midleft with dissolve
    ro "No."
    "Rowan cut the conversation short and exited the office without another word. He quickly contacted Cliohna, informing her he had another abbey up for the taking, but this one without anything of worth in it."
    "The abbey was still useful for it’s magic focusing properties, but the plundered library would be a blow to Cliohna's research."
    "Yet another unfortunate complication."
    $ change_research_bonus(1)
    return
    
else:
    pass
    
show rowan necklace angry at midleft with dissolve

"Rowan scowled. It was unlike an abbot to straight up abandon their abbey. It was their duty to look after it, no matter the danger."
"Guess he couldn’t blame him for doing so, given how he was literally there to occupy it with a contingent of orcs. But the fact that he ran away, while a simple peasant remained to look after the place, was… Jarring."

show rowan necklace happy at midleft with dissolve

ro "What’s your name, good man?"

$ caretakerName = "Lois"

care "Lois. Lois of Fernsworth. Mother named me after the great Lord Lois Delane. Wonderful man, he was. Many years ago, he was passing by my family farm on his way home..."

show rowan necklace neutral at midleft with dissolve

ro "Lois."
ro "I think you should leave as well."
ro "Your abbot was right. It isn’t safe here."

care "..."

"The caretaker, Lois, did not respond. He stopped his work for a moment so he could turn and take get a good look at Rowan. His expression was grim, and Rowan thought there was an angry flicker in his eyes – but the sight of it was gone so quickly, it might have been just his imagination."
"The man sighed heavily, and put down his cleaning cloth. Walking around the abbots desk, he sat down at the chair usually intended for the guests, and leaned back with a tired groan."
"After a moment, he smiled slightly and finally spoke up."

care "Would you mind telling me your name young man?"

show rowan necklace happy at midleft with dissolve

ro "Rowan."

care "Ha, like the hero of Karst! A good name, young man!"

show rowan necklace neutral at midleft with dissolve

ro "… Yeah."

care "Well, Rowan… I have spent 40 years looking over this abbey. Cleaning the floors, washing the curtains, doing the dishes."
care "I was its caretaker before Karnas appeared, and I was its caretaker when he waged his war. And now that he is gone, I remain its caretaker."

"The man smiled benevolently."

care "It is the Holy Goddess' will that put me here when I was young, it is by her will that I remain here. And by her will, I will do so till I draw my final breath."
care "And I will do so with a smile, knowing I have served her faithfully."
care "So please, do not mind me, Rowan. I am content with my fate. To die taking care of one of Solansia’s temples..."
care "I can think of no greater honour."

menu:
    "He’s throwing his life away needlessly. Convince him to leave.":
        $ released_fix_rollback()
        ro "Lois, I understand this place is important to you, but without the abbot, and without the pilgrims… It’s no longer a temple to Solansia."
        "Rowan pointed to the walls around them."
        ro "It’s just… A building like any other."
        ro "It’s not worth dying for."
        ro "I don’t believe Solansia would want you to throw your life away like that."
        ro "So please, rethink your decision."
        care "..."
        "Lois didn’t answer again. Not at first."
        "But then, Rowan saw his expression harden, and the angry flicker in his eyes returned."
        care "… I think you’d like Reverend Garin, young man. He also said something along these lines."
        care "Said he was…  “Burdened with glorious purpose”. And that he wouldn’t die protecting some…"
        show rowan necklace shock at midleft with dissolve
        care "“Shabby old abbey in the middle of fucking nowhere.”"
        show rowan necklace neutral at midleft with dissolve
        "His face twisted into an expression of pure hate, and he continued with voice so full of bile, Rowan couldn’t believe it was the same good-natured old man he met just a few minutes ago."
        care "Well Rowan, I’ll tell you what I couldn’t tell him, because it looks like you forgot what is expected of you."
        care "It’s not our place to decide when and where to die. The Goddess decides our lot in life, and it is our duty to fulfill it to the end, no matter how hard or difficult our fate might seem."
        care "It’s only when conceited little brats like you and Garin start thinking they’re too damn important to die, and wander off to play hero, does the world go to shit."
        care "So stop pretending to know what the Holy Goddess might want, and stop trying to “save” me, like it’s your damn job or something."
        care "Because it’s not."
        care "Now get out of my damn sight."
        ro "..."
        ro "If that’s your choice."
        hide rowan with dissolve
        "The two men stared at each other for a while, until Rowan turned his gaze away and  headed to the exit. He didn’t have time to argue theology with an old man. Wouldn’t be able to convince him anyway."
        "He contacted Cliohna and informed her he found a new abbey, but without the personnel and with most of its books taken away. Luckily it would still be of use, due to its location."
        "He said nothing of the caretaker. If the man wished to put his fate in Solansia’s hands..."
        "Then so be it."
        $ change_research_bonus(1)
        $ change_base_stat('g', -2)
        return
        
    "Respect his choice.":
        $ released_fix_rollback()
        ro "… If that’s what you believe is best."
        "The elderly man chuckled lightheartedly."
        care "You’re a good lad, Rowan."
        "His gaze wandered off to the side, and his voice grew distant."
        care "Far better than Garin ever was..."
        "His eyes snapped back to Rowan, and he straightened up."
        care "Now, young man, I don’t think you ever mentioned why you’re here…?"
                
        menu:
            "Wanted some place to contemplate." if avatar.guilt > 30:
                $ released_fix_rollback()
                ro "I hoped a sermon would do me good."
                care "Rough week?"
                "Rowan couldn’t help but snort. A bit of an understatement, right there."
                ro "To put it lightly."
                "The elderly man scratch his chin in thought."
                care "I’m afraid I can’t help you here… I wouldn’t be right for me to recite the words, even if I did hear them a thousand times, but..."
                care "My daughter always said gardening helps her regain a peace of mind."
                care "Maybe you should stay a while, help me around a bit?"
                care "Might do you some good."
                "The amulet at Rowan’s neck weighted heavily. He really did not have the time to be playing gardener. Especially not with someone who would soon end up a mind controlled servant to Cliohna’s apprentices."
                "… But maybe that was exactly what he needed?"
                
                menu:
                    "Agree.":
                        $ released_fix_rollback()
                        ro "..."
                        show rowan necklace happy at midleft with dissolve
                        ro "Maybe for a little while."
                        care "Ha! Atta boy!"
                        care "Alright, help these old bones up. We have a lot to do..."
                        hide rowan with dissolve
                        "The following days were that of frustratingly calming laziness."
                        "He shouldn’t be doing that. Rowan knew that. He should be running around Rosaria burning villages and corrupting nobles, or whatever it was that the twins demanded of him at the time."
                        "But there was more to life than setting the world on fire, and he knew it was in the twins interest for him to forget that."
                        "..."
                        "A few days later, with the garden now fixed up, Rowan bid the elder farewell. He told him he hoped everything would turn out alright for the man."
                        "He already told Cliohna the abbey was empty, but it still was a location of power, so her apprentices were scheduled to arrive at the place a few days from now."
                        "They were instructed to allow the man to remain a caretaker, once he was sufficiently pacified."
                        "Probably not the fate Solansia had planned for him…"
                        "But then again, who could know?"
                        $ change_research_bonus(1)
                        $ change_base_stat('g', -5)
                        $ change_base_stat('c', -5)
                        $ change_mp(-4)
                        #add abbey flowers (TODO)
                        return
                        
                    "Pass.":
                        $ released_fix_rollback()
                        ro "…"
                        ro "I apologize, Lois. But I will have to decline."
                        ro "There are things I need to take care of."
                        "Lois sighed, defeated."
                        care "Ah, you young people…"
                        care "Take care of yourself lad. It was nice seeing a friendly face again."
                        
            "Just passing through.":
                $ released_fix_rollback()
                ro "I was in the vicinity. That’s all."
                care "Ah."
                care "Well… I won’t keep you then?"
                    
hide rowan with dissolve

"With his objective achieved, Rowan bid the elder man farewell. He told him he hoped everything would turn out alright, and that maybe one day, a new abbot will arrive, and the abbey would flourish once more."
"Of course, as soon as he was out of the temple gates, he contacted Cliohna to inform her of the abbey’s location. The abbey might have been plundered of anything that had any value, but as all others, it was placed on a magical nexus, so it was still a valuable find."
"Her apprentices would arrive in a few days. By Rowan’s instructions, they were to leave the caretaker alone, once his compliance was assured with magic."
"Probably not the fate Solansia had planned for him…"
"But then again, who could know?"
$ change_research_bonus(1)
return

##########################################################################################################################################################################

label abbey_cliohna:

#abbey BG
scene black with fade


show rowan necklace neutral at midleft with dissolve
show orc soldier neutral at midright with dissolve

ro "Careful with that, it’s a relic."

os "Yes, masta."

hide orc soldier with moveoutright
show rowan necklace concerned at midleft with dissolve

"The orcs hurried off with the ancient painting, with far less care than the object in their hands demanded. Rowan shook his head in disapproval. As if crimes against humanity weren’t enough, he’d now have to add cultural losses to his increasingly depressing hero resume."

show rowan necklace concerned at center with moveinleft

"Cultural losses of no small caliber, as this was no ordinary abbey. With wooden, low walls, and a thin forest around it, it had none of the splendor of what one would usually find in Solansia’s place of worship – but it had ten times the history."
"He looked around again, taking in the sights. One of Rosarian oldest abbeys, created soon after The Folly. Inconspicuously hidden away…"

show rowan necklace shock at center with dissolve

quest "Are the orcs finished Rowan?"

show rowan necklace neutral at center with dissolve

"A harsh voice brought him back to reality. He turned around to face the person who specifically requested he target this location."

show rowan necklace neutral at midleft with moveoutleft
show cliohna neutral at cliohnaright with dissolve

ro "You’re in a foul mood, Cliohna."

cl "I wish to be done with this place, so I can resume my research. Do you find that surprising?"

ro "No, of course not. But you needn’t join us."

cl "I could not risk leaving the matter to anybody else, Rowan. This place is ancient, and I expected it to have protections and artifacts befitting of its history."

ro "And…?"

"A frustrated sigh was his answer. Nothing then."

ro "We’re almost done. Once the orcs carry away the statue, I’ll leave you to establish another research-"

cl "We will do no such thing."
cl "I will not be taking this abbey over. It was not built on a leyline, therefore it is of no use to me."

ro "Then I suppose we can go….?"

show rowan necklace neutral at edgeleft with moveoutleft

"He took a few steps towards the exit. Cliohna did not move, still looking at the abbey, at the place where the altar to Solansia stood."

show black with redflash

"She raised her hand, and snapped her fingers. A small flame burst from her hand, burning brightly between her fingers."

show cliohna happy at cliohnaright with dissolve

cl "Of course. I will be right behind you, Rowan."

menu:
    "Stop her, now!":
        $ released_fix_rollback()
        $ change_base_stat('c', -2)
        show rowan necklace neutral at center with moveinleft
        show cliohna neutral at cliohnaright with dissolve
        "In a split of a second he was by her side, holding her wrists. Cliohna didn’t even flinch. She turned her eyes to Rowan slowly, an expression of mild annoyance reflected in them."
        cl "Is there something you wish to say, Rowan?"
        ro "What are you doing Cliohna? We got what we wanted. Why burn this place down?"
        cl "And why should we not? Correct me if I’m mistaken, but isn’t the twins’ ambition to subvert Rosaria and claim it for themselves?"
        cl "We have no use for this place, and by destroying it we put a clear signal that the Church of Solansia no longer has control over the region."
        ro "We’ve done that already by pillaging it. At this point, burning it is just being… Vindictive."
        show rowan necklace concerned at center with dissolve
        ro "What’s going on Cliohna?"
        "The sorceress shook off his hold, an angry scowl passing through her face for just a moment."
        show rowan necklace neutral at center with dissolve
        cl "This place is nothing but a superfluous monument to an empty culture of ignorance and repression. I am doing future generations a favor by removing all traces of it from this world."
        cl "And it is my assumption that Solansia is no ally to the twins, them trying to bring down her morally hollow order. So why defend her temple, Rowan?"
        "Her cold stare drilled through his skull. It wasn’t often Cliohna got heated over anything. Would he stand in her way here?"
        menu:
            "Solansia still has a place in this world. The abbey is to be left standing.":
                $ released_fix_rollback()
                $ change_base_stat('c', -2)
                $ all_actors["solancia"].favors += 1
                $ all_actors['cliohna'].relation -= 3
                show rowan necklace angry at center with dissolve
                ro "I don’t know what feud you have with Solansia, but I’m not letting you burn her abbeys for no reason."
                "Her thin eyebrows narrowed ever so slightly, like that of a mother who was about to scold a rebellious child."
                show cliohna neutral at edgeleft with moveoutleft
                "Only for her to turn around and head for the exit."
                cl "Very well, but know this: In time, you will realize the world will be better off if Solansia ends just like this abbey."
                scene black with fade
                show cliohna neutral behind black
                cl "Forgotten by time, and prey to those who seek greater things."
                return
                
            "There is no point opposing Cliohna here. Let her burn it down.":
                $ released_fix_rollback()
                $ change_base_stat('c', 2)
                $ all_actors["kharos"].favors += 1
                $ all_actors['cliohna'].relation += 3
                "The two remained locked in an impasse, neither really willing to back down."
                show rowan necklace neutral at midleft with moveoutleft
                show cliohna happy at cliohnaright with dissolve
                "In the end, it was Rowan who stepped back, throwing his hands up in defeat."
                ro "Do as you wish."
                cl "Thank you Rowan. Trust me: Nothing of value will be lost."
                hide rowan with moveoutleft
                show cliohna happy at center with moveinright
                "A wave of heat reached his back as he left the temple, red light illuminating the surroundings. 800 years of history…"
                scene black with fade
                "Gone in a instant."
                return
                
    "Let her burn it down.":
        $ released_fix_rollback()
        $ change_base_stat('c', 2)
        $ all_actors["kharos"].favors += 1
        $ all_actors['cliohna'].relation += 3
        ro "Don’t take too long."
        hide rowan with moveoutleft
        show cliohna happy at center with moveinright
        "A wave of heat reached his back as he left the temple, red light illuminating the surroundings. 800 years of history…"
        scene black with fade
        "Gone in a instant."
        return
                
#############################################################################################################################################################

label abbey_first:

#abbey bg
scene black with fade
show rowan necklace neutral at center with dissolve

"In front of him, the abbey’s gates loomed."
"As per instructions given to him, he contacted castle Bloodmeen upon seeing the building on the horizon. He scouted the region while waiting for the subjugation force to arrive, so no unpleasant surprises would welcome them."

hide rowan
show orc soldier neutral at midleft with dissolve
show wild orc neutral at edgeleft with dissolve
show rowan necklace neutral at center with dissolve

"To his mild annoyance, the orcs made no effort to hide their approach, and the local priest barricaded themselves inside the abbey, ready to fight off the invaders."
"Not that it would make any difference, as Rowan would soon learn."

show cliohna neutral at cliohnaright with dissolve

ro "Shall we begin, Cliohna?"

cl "Hm? Ah, yes, in a moment Rowan. I wanted to take a good look at it first."

"He didn’t expect the castle librarian to join them personally, yet the sorceress did so, accompanied by two of her students. And now she kept staring at the temple, as if this was the first time she’s ever seen one."

cl "Hmph… I expected more..."

"Her voice was quiet, and by her tone it sounded like she was… Mad at herself? For expecting more? Rowan couldn’t quite figure out what was going through Cliohna’s head at the moment, and the sorceress was unlikely to enlighten him."

cl "I suppose we can begin now."

hide wild orc with moveoutleft
show orc soldier neutral at edgeleft with moveoutleft
show rowan necklace neutral at midleft with moveoutleft
show cliohna neutral at center with moveinleft

"He raised his hand to give the orcs their orders, only to be cut off by Cliohna stepping forward. The sorceress spread her arms and fingers."

show black with flash

"An arc of lighting jumped across them. Rowan saw the two students cover their ears."

if check_stat(8, 'reflexes')[0]:
    show black with sshake
    "At the last second he managed to cover his own, as a thundering *CRACK* pierced the air and the massive gates of the abbey shattered in an instant. Splinters rained around them, testimony of Cliohna’s power."
    hide cliohna with moveoutright
    show rowan necklace shock at midleft with dissolve
    "Without missing a beat the sorceress strolled forward, crossing into the abbey. Rowan saw the dazed abbot raise to his feet, heard him mutter “Cursed Witch!” before being cut off by another of Cliohna’s spell."
    show rowan necklace concerned at midleft with dissolve
    show cliohna neutral behind black
    cl "Kneel, and be quiet."
    hide cliohna
    show rowan necklace concerned at center with moveinleft
    "She flicked her hand, and the man fell to his knees, clawing at his throat. The other acolytes soon followed suit."
    "Rowan couldn’t believe his eyes. The whole scene lasted a total of ten seconds. Just how powerful was the sorceress?"
    show rowan necklace neutral at center with dissolve
    "He’d ponder on this later. Shaking his head, he turned around to make order of the dazed orcs. Utilizing the centuries old military language of head-smacking and finger-pointing he had them secure the perimeter, then approached Cliohna again."
    
else:
    #Add Wound: Light penalties to listening/perception, for a couple of weeks (perforated eardrums) (TODO)
    show black with sshake
    "A thundering *CRACK* pierced the air, and the massive gate of the abbey shattered in an instant. Splinters rained around them as Rowan cursed out loud – or at least was fairly certain he did, his ears ringing."
    hide cliohna with moveoutright
    show rowan necklace shock at midleft with dissolve
    "Meanwhile, Cliohna strolled into the abbey, unconcerned with the chaos. Rowan saw the dazed abbot raise to his feet, but Cliohna simply flicked her hand and the man was once again fell to the ground clawing at his throat. The other acolytes soon followed suit."
    show rowan necklace concerned at center with moveinleft
    "In ten seconds, the abbey was theirs. Just how powerful was the sorceress?"
    show rowan necklace neutral at center with dissolve
    "He would ponder on this later. He got his orcs to get up, and using the old military language of head-smacking and finger-pointing had them secure the perimeter. Once the ringing in his ears subsided, he approached Cliohna again."
    
show rowan necklace neutral at midleft with moveoutleft
show cliohna neutral at cliohnaright with dissolve

"She was interrogating a young acolyte. The poor man knelt before her, his neck craned backwards as he looked into her eyes, unblinking."

cl "Why do you serve Solansia?"
    
aco "She… Protects… Us…"

cl "If you could pick between learning magic or serving this oppressive goddess of yours, which would you pick…"

aco "We… Serve… Solansia… She… Protects… Us…"

"The sorceress furrowed her eyebrows in annoyance. She cast the boy aside, then approached the next one."

ro "What are you doing?"

cl "Looking for students. People who value the pursuit of knowledge over misbegotten notions of “stability”."
cl "As I understand the church of Solansia often recruits their clergy from among the magically gifted. It is my hope that at least some of them still retain an interest in the craft itself, rather than study it just to better channel Solansia’s divine energies."

"Rowan saw one of her students direct his orcs to the unconscious man, and the green soldiers dragged him to one of the side chambers. The other knelt by the temple abbot, holding a glowing crystal in front of his eyes."

ro "What about him?"

cl "It is far too late for people like him. He will be brainwashed along with the other failures, and shall continue overseeing the abbey, with my apprentice here as his new right hand."
cl "According to my research, Rosarian abbeys were often built on magical leylines, which makes them good research outposts."

show rowan necklace shock at midleft with dissolve

cl "And should the situation in the region deteriorate due to your future actions, I hope they will attract refugees seeking protection, and provide us with a steady supply of test subjects."

show rowan necklace concerned at midleft with dissolve

ro "(I hope it won’t come to this.)"

show rowan necklace neutral at midleft with dissolve

os "Ey, boss, there ain’t no gold here!"

"The sorceress arched an eyebrow at him. Rowan shrugged his arms."

ro "I wasn’t expecting there to be. Gifts from the faithful are usually sent back to the capital."

hide orc soldier with moveoutleft
show cliohna happy at cliohnaright with dissolve

cl "Of course. It would be unreasonable to expect a Goddess support herself through faith alone. "

show cliohna neutral at cliohnaright with dissolve

cl "Now, unless you have further questions, your presence here is no longer required. You can leave the orcs with me, I’ll send them back to Castle Bloodmeen once I’m done with the place."

ro "They weren’t even needed."

cl "They will be next time, I do not intend to accompany you often. It’s important to take to the field every once in a while, but I have no intention of making a habit of visiting Solansia’s temples. They have little to offer."

"The abbot finally got up, his dazed expression replaced with a stern scowl, likely a one he wore ofen. Rowan saw him nod slowly as Cliohna’s student asked him about the abbey’s library, and point to the back of the building."

ro "You are certainly making full use of what little they have."

hide cliohna with moveoutright

"But Cliohna was no longer listening, already halfway to the library."

show rowan necklace concerned at midleft with dissolve

"With a sad sigh, Rowan threw the abbey one last look, then headed for the exit. He didn’t like what Cliohna was doing with the priests… But he wasn’t certain if he could afford alienating the castle librarian."

hide rowan with moveoutleft
scene black with fade

if serveChoice != 4:
    "Judging by the display earlier, she was not lacking in power. If he was to rebel against the twins one day… He might need her support, no matter the price."
    
else:
    "Judging by the display earlier, she was not lacking in power, and her research was crucial to their efforts. I he was to succeed in toppling Solansia’s order, he would need her support, no matter the price."

return


