init python:

    event('rastedel_battle_begin', triggers='week_end', conditions=('week==60',), run_count=1, priority=pr_story)
    event('rastedel_battle_2', triggers='week_end', conditions=('week==61',), run_count=1, priority=pr_story)
    event('rastedel_battle_3', triggers='week_end', conditions=('week==62',), run_count=1, priority=pr_story)

label rastedel_battle_begin:

scene bg9 with fade

show rowan necklace naked at midleft with dissolve

"Rowan was woken up by the light streaming through his bedroom windows. The Rakshan Wastes were not known for their bright mornings. It was a small fortune, because a moment later the door opened."

show alexia 2 necklace shocked at midright with moveinright

al "Rowan? You’re still in bed?"

"Rowan squirmed under the covers and groaned."

ro "It was a long week. A long year. Let me sleep in this one time."

show alexia 2 necklace happy at midright with dissolve

al "I can only imagine. That’s no excuse for waking past noon though."

"She walked towards the bed and pulled back the covers. He crossed his arms over his chest instinctively at the hiss of cold. Not even the days sleeping on the floors of Karst prepared him for the horror of losing a blanket."

if all_actors['alexia'].relation < 50:
    "For a moment, the tension of the past few months seemed to dissipate. Or at least not rear its ugly head."
    
    if alexiaWulump == True:
        "Still, her soft smile didn’t touch her eyes. It never seemed to touch her eyes much anymore."

ro "Noon? Really? I hadn’t thought myself capable...."

al "Yes, really. Now up with you."

show rowan necklace happy at midleft with dissolve

"Rowan grumbled to himself the entire time he worked on his clothing. Alexia sat on the bed watching him, as she had first done many years ago."

if all_actors['alexia'].relation < 50:
    "Something felt off about it…"

elif all_actors['alexia'].relation > 50 and all_actors['alexia'].corruption > 30 and avatar.corruption > 30:
    "For all about them that had changed, the way she looked at him hadn’t."

else:
    pass
    
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

al "Whatever adventure it was this week must have been quite rough if it left you incapable of even rising at a normal time."
al "Still Rosaria?"

"Rowan nodded."

ro "It’s been the focus of our operations."

al "How long has it been since I was back home? Bloodmeen has been my cage for so long now. I must have forgotten so much already. Is it still unchanged?"

show rowan necklace concerned at midleft with dissolve

"Rowan kept working his outfit’s buckle, but didn’t answer. Could he tell her about the famine or the problems he’d seen? In fact, had he even told her about the elder’s death?"

ro "It’s much the same as it always is. Green and lush. Not a gaudy statue of a demon lord in sight."

show alexia 2 necklace concerned at midright with dissolve

al "I miss the smell of it. The flowers, the trees. I never realized how beautiful it was until I actually left home…"

if all_actors['alexia'].flags['jezera_influence'] > 4:
    al "Perhaps Mistress Jezera will allow me a brief visit."

elif all_actors['alexia'].flags['andras_influence'] > 4:
    al "Perhaps Master Andras will allow me a brief visit."
    
else:
    al "Perhaps we will be free of this place someday soon."
    
"Rowan sighed. Even if she did return, the home that she knew wouldn’t be there anymore. The Arthdale she’d known had been destroyed."

#todo : if reconstruction quest is done:
    #"Even after it’s restoration, it will never be the same. No town is the same without the people who once lived there."
    
ro "I-"

show rowan necklace shock at midleft with dissolve
show alexia 2 necklace shocked at midright with dissolve

"Suddenly the door swung open, and a frantic looking maid burst in."

maid "Lord Rowan. You must come quickly."

show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

ro "What is happening?"

maid "The Master and Mistress are in a rage. The staff is terrified. You must come quickly. Please, follow me."

"Rowan and Alexia exchanged a concerned glance. Was he the cause of this?"
"Without a second word, he followed the maid out the door, leaving Alexia with her arms wrapped around her sides. This was their life."

if goal3_completed == False:
    hide rowan with moveoutright
    "After Rowan left, Alexia remained in bed, going over the possible reasons that Rowan might have been called down. She almost missed the knock on the door…"
    
scene bg6 with fade
show rowan necklace neutral at midleft with moveinleft

"Rowan walked hesitantly into the throne room, and found one of the tapestries lying on the ground in tatters. "

ro "Is something amiss, my masters?"

show jezera displeased at midright with dissolve
show andras angry at edgeright with dissolve

"Jezera stormed over to him in a huff, and threw a piece of parchment to the floor at his feet."

je "Read this. Now."

"He picked up the document and began to read aloud."

ro "Report from the Hydrangea. A large force of Rosarian soldiers has been reported moving down the South road from Rastedel."
ro "Estimated numbers are well over two thousand. Fully armored knights and men-at-arms included in the retinue. Based on their route, the objective is likely Raeve Keep. However, a force of this size can threaten any position in the duchy."

if palaceStage == 2:
    ro "Several surcoats spotted among the forces. Majority are wearing plain white or gold. Unit origins unknown."
    
else:
    ro "Several surcoats spotted among the forces. Majority are wearing plain white or gold. However, a force in purple was seen at their head. Unit origins unknown."

"Rowan put down the letter. It was far and away the largest force that had ever been put in the field against them. More too than any army they could call on short notice."

show rowan necklace concerned at midleft with dissolve

ro "...I see…"

"Andras was sitting stone faced on the throne. In contrast to his normal temperament, he was eerily silent. It seemed the tapestry had borne the brunt of his rage. Jezera, meanwhile, was not half as calm."

je "I heard nothing about this. Nothing from the capital at all. What good are spies who don’t tell you anything? How could that bitch have missed this?"

"She swatted at a half full wine glass, making it crash to the ground. The maid, still in the door frame, winced."

if palaceStage != 2:
    "Rowan softly wondered to himself who “that bitch” was?"
    
else:
    ro "Our friend in the capital didn’t say a word about this?"
    je "Not a word. We got this from an Incubus who happened to be near their path."
    
an "We are outnumbered. We are out armed. They are coming for us. You are our tactician. I don’t give a rat’s ass about her whisperers. Why didn’t you have a plan for this situation?"

"His glare pierced Rowan. At once he understood the kind of danger he was in. How he answered here might put his head on the line."

if goal3_completed == True:
    ro "I-"
    je "Oh be quiet, brother. We need our most able tactician with a pulse in this moment."
    "Andras growled, but slunk back into his throne."
    an "Able tactician."
    "He spat to the side."
    
else:
    an "So this is what it all comes to. All your sneaking and strategies. And we’re left sitting here with our dicks in our hands."

an "Clever tactics are nice. But, this will all end with me and my fiercest fighters charging through as many enemy knights as we can take. If we are outnumbered, it will only make it more glorious."

"Jezera rolled her eyes."

je "You’re not going out in the field to die fighting five hundred humans all at once. If need be, we will simply evacuate from the Rosarian plains. It will cost us greatly. "

if goal3_completed == True:
    je "Our new alliances were hard won. Losing our presence in Rosaria is not a thing to consider lightly."

je "And, of course, when they’ve taken back the area, we can little hide our direct involvement much longer. Our lovely friends in Prothea will not be pleased to learn of our existence. "

show rowan necklace neutral at midleft with dissolve

"Rowan went back to studying the letter. Just how did they get an army so fast?"

if palaceStage == 2:
    ro "Had High Arbitron Marianne accepted either Jacques or Duke Werden’s proposal for aid?"
    
"Maybe the answer had something to do with the colours of the troops that had been spotted..."

#TO DO - should check if goal 3 is completed, palaceStage !=2, or troop / funds requirement is not met
if goal3_completed == False or palaceStage != 2:
    jump battleFail


#TO DO: If goblins recruited

#TODO: If goblins and orcs recruited

if orciad_state == 2:
    jump orcBattlePath


label orcBattlePath:
    
if orciad_ally == "batri":
    ro "Have you already spoken to Batri? Do we know that our Orcish allies will join us in the field?"
    
elif orciad_ally == "ulcro":
    ro "Have you already spoken to Ulcro? Do we know that our Orcish allies will join us in the field?"
    
else:
    ro "Have you already spoken to Tarish? Do we know that our Orcish allies will join us in the field?"
        
"The unspoken problem was that the allied tribal confederation was not actually directly in the path of the Rosarian army. They might flake."
"Suddenly, he heard footsteps behind him. Someone had been waiting in silence nearby and had chosen now to emerge."
    
show tarish neutral at edgeleft with moveinleft
    
tar "Quit ya worrien, humie. Ya really think a buncha us tough orc-folk gonna run from a few pink men just caus dey hiding unda metal?"
tar "If da time ta fight is now, you best kno we gonna be der."
    
"Tarish crossed her arms over her chest."
"Jezera rolled her eyes and gestured to the new arrival in the throne room."
    
je "I believe you and Tarish have already met."
    
if orciad_ally == "ulcro" or orciad_ally == "batri":
        
    je "After the events that took place in the tribe, the new chief sent her here to Bloodmeen as a personal representative and ambassador. She’s been authorized to speak for them under certain parameters as well."
    je "This is recent of course, but don’t be surprised to see her around the castle from now on."
        
    "Tarish strode over to Rowan."
        
    tar "Ya Mistress speaks rite. Dis a real fancy place. Neva thought I’d get used ta livin in a stone castle like ya hummies do."
    tar "Ya lucky, hummie. I got me a nice job now. If I came outta da whole mess wit nuttin to show for it, ya’d have ta watch ya back."
        
elif orciad_ally == "tarish":
        
    tar "Aye aye. We be well known ta one anotha. Ain’t no alliance wit out him buttin in."
        
    if tarishSex == True:
        "The unspoken element was just how well they knew each other. Inside and out. Not that Rowan suspected for a second that Jezera didn’t have some idea."
            
    ro "Indeed. But, why is she here? Doesn’t she have an entire tribe to rule?"
        
    an "Are you that much of an idiot? She’s ‘in charge’ of the tribe. But, do you really think she could hold the place without us?"
        
    tar "What ya masta be tellin ya is dat is betta for me to keep around heres and pop in every otha day by portal. Keepin up ta date here is more important then bein down der."
    tar "So day means you gonna be seeing more ‘o lil ‘ol me in da future, hummie."
        
    "She gave him a small wink."
        
else:
    "The prospect of another meeting with Tarish, especially after all the damage caused by their previous encounter, made the prospect of a reunion less than ideal. So too did the disdainful expression on her face."
        
    ro "Indeed. But, why is she here? Doesn’t she have an entire tribe to rule?"
        
    an "Are you that much of an idiot? She’s ‘in charge’ of the tribe. But, do you really think she could hold the place without us? We’re the ones making sure that some idiot doesn’t put a sword in her gut."
        
    tar "Aye. For da moment gotta stay outa da way of dose who might nah be so friendly. Nah the worst place to be. I always wanted ta visit one ya big ass humie castles."
    tar "..."
    tar "I’m sha ya gonna enjoy havin me around."
        
    "Rowan kept his blank composure. Better to not address the unspoken threat there."
        
show jezera neutral at midright with dissolve

je "Let’s get us back to the matter at hand, shall we? No time for greetings and kisses."
je "So long as we have assurances that we actually have an army to use. Then the question becomes how to use that army to actually win."
je "Even with every grown soldier that the tribe has, along with our own forces, we still don’t have enough to go toe to toe with them."
je "At least, so my dear brother tells me."

"Andras scowled."

an "You’ve been mostly silent, Rowan. We didn’t bring your ass here for the weather. Do you have an idea how to get out of this situation or not."

ro "I’ve been going over it."

"Rowan’s eyes scanned over the letter again. He had never been a high level commander, but he did have experience in this situation. Facing down an enemy with larger numbers than yours."

ro "If I had to think about it, I would say that our strongest advantage is that we actually hold the territory. It’s not truly home ground, in that the nearby population won’t be friendly."
ro "But, we control the keep itself. We also have allies in the woods and on the mountains. They’re coming to us and that makes us stronger."

je "What does that matter? Numbers are numbers?"

"To Rowan’s surprise the person who chimed in was none other than Andras."

an "Quit your whining, woman. On the battlefield, the right terrain is worth double your troops. Sometimes more."

show jezera displeased at midright with dissolve

je "Fine. Sure. Continue, Rowan."

ro "We have another advantage too. Unless they have a traitor in our ranks, then they don’t know the numbers we hold. In fact, Doran Raeve gave a low estimate of the number of orcs who attacked."

tar "As far as da hummies know, my boys be up north. No way dey see us all coming."

ro "That means, we can secure at least one victory. When trying to pacify hostile enemy territory, and are not afraid of a pitched battle, you normally want to spread out."

show andras smirk at edgeright with dissolve

"Andras smirked wickedly. He already saw what Rowan was getting at. For all his flaws, Andras was a fighter."

an "An ambush. Wait for them to divide up their forces, and then make the smaller force our bitches."
    
ro "I wouldn’t have used that phrasing, but basically. When I fought in the last war, we’d use tactics like that all the time. Wait for stragglers to break off, looking to plunder or just take a breather. Then strike before they can rejoin the rest of the army."
ro "Only now we have hundreds of warriors. Not tens like I had before. We could fight an entire battle that way."

show jezera neutral at midright with dissolve

"Then tension in the room seemed to dissipate some. Now that someone had given the beginnings of a concrete plan, the air of panic seemed to have settled into something more productive." 
"Jezera paced back to the throne, while Tarish pulled up to Rowan’s side."

tar "A clever plan, humie. Real sneaky like. But, ya don know orc fighin’ like I do."
tar "Ya can do dat a few times. But, da hummies are smart like. They gon figga out what ya up about an stop ya. Always happens."

"Rowan sighed."

ro "She’s right. We can use harassment tactics and ambush smaller units a few times. But, once they realize that someone is out there hunting down their detachments, their strategy will change."

"Rowan didn’t mention the fact that was on his mind. How well this worked depended entirely on who the commander was. If it was someone dumb, they could lead him by the nose."
"But, if the man he worried was in command was leading the charge...his tricks would fall flat…"

show rowan necklace angry at midleft with dissolve

"Rowan silently cursed the note. For all of the value it had, it still didn’t tell him which troops exactly would be in the fighting line. The mystery of the army that shouldn’t exist underlined the entire situation."

show rowan necklace neutral at midleft with dissolve

ro "If that’s the case, we should prepare for a long campaign. Trying to hold the keep is a nice thought, but we should expect they’ll take it back relatively quick. "
ro "I see brutal back and forth fighting for awhile. Still, we might have a chance if we take out enough enemies in the first strike."

"Now it was Jezera who seemed deep in thought. Did she have an idea?"

show jezera happy at midright with dissolve

je "Ooh, intriguing. This I can work with."
je "If we can defeat more of the enemy army before they figure out what we’re up to, then we stand a better chance? What determines that?"

ro "How fast we move, and the number of enemy detachments. More detachments mean we’d have better numbers. But, it also means we’d need to move around a lot more and probably get to less of them."

je "Oh dear hero. You underestimate us still. It’s honestly kind of charming."
je "We can move as fast as we want."

show rowan necklace shock at midleft with dissolve

"Rowan’s mouth hung open in shock. Of course. Of course. It was so obvious. Why had he not thought of it before? He wasn’t commanding an army of humans or even an army of orcs."
"This was a demon army."

show rowan necklace neutral at midleft with dissolve

ro "..."

tar "Whacha mean by dat, Jezera?"

ro "I know what we need to do."
ro "Listen…"

"Rowan spent the next half hour explaining a strategy that had been churning in his mind over the conversation. Ten minutes in, he had the servants bring in a map of the duchy to help decide on the specific locations that they’d need to utilize."
"Andras and Tarish followed along, in Tarish’s case doling out suggestions and in Andras’ pausing to occasionally thump his chest. Jezera strained to pay attention, even beginning to zone out until Rowan explained what her role in the plan would have to be."
"By the time he was done, everyone around the map looked satisfied."
    
ro "...The number of troops we’d have in our custody would be high. I’m sure a number of them were forced levies or otherwise willing to switch sides in return for compensation and protection for their families."
ro "The rest we could keep around as a potential labour force."

"Andras had an instrutible expression and Rowan went over this part. But, otherwise didn’t go out of his way to comment."
"Finally, Rowan reached the end of the plan. When he finished explaining, he went down to one knee and waited for the twin’s judgement. Ultimately, this was the plan with the highest chance of success."

if serveChoice == 2:
    "It was the very best shot he had at keeping Alexia alive another day. And himself to boot."
    
elif serveChoice == 4:
    "Not only would it keep himself alive another day, but it would give those selfish monsters in Rastedel who’d been ignoring the famine a bit of well earned retribution."
    
else:
    pass
    
if avatar.corruption < 31:
    "The fact that it would involve more prisoners taken then casualties dolled out was also an additional bonus."

show andras happy at edgeright with dissolve

an "Hrmm. I like it. I like it."

show jezera displeased at midright with dissolve

je "Of course you like it. You just like any plan that happens to feature you killing people."

show jezera happy at midright with dissolve

"Rowan turned to Tarish."

ro "What do you think? Your soldiers are the backbone of our army."

tar "Aye. Ain’t no word of complaint outta me, humie. Is a good plan. Lotta Orc gonna survive from it. Maybe bring back some pretty gold along da way."

"Rowan let out a sigh of relief. It was a good plan. It would probably work."
"That was important. If he hadn’t been able to come up with any kind of plan on the fly, it would likely have been the end of him right here. The life he led in Bloodmeen was always on a razor’s edge."

an "It’s settled then. We will launch the plan that Rowan suggested in one week’s time. We will not retreat from Rosaria. We will stand and fight."

je "Inspiringly put. Now then, I best make preparations as soon as possible. I need to depart on the morrow."

"Jezera slunk towards Rowan, brushing her side against him as she passed."

je "Make good use of this week, hero. We need as much gold and men as we can muster for this operation."

ro "I understand."

"He felt a sudden jolt. A slap on the rear."

je "That’s what I like to hear. See you at the celebrations."

hide jezera with dissolve

tar "I best be movin too. Gotta let da boys hear dat ders a fight happenin. Gotta get ‘em all riled up. You best not be tryna pull summtin, hummie."

hide tarish with dissolve

"Now alone with Andras, Rowan turned to leave."

an "Hold."

"Rowan turned around."

show andras displeased at edgeright with dissolve

an "This will be the greatest test of your devotion to date. Your plan was good. But, that doesn’t mean I trust you. You understand that if you betray me in any way, I will feed Alexia your guts, don’t you."

"Rowan coughed."

ro "I do."

show andras happy at edgeright with dissolve

"Andras’ expression softened suddenly. He was smiling now."

an "But, that works the other way around too. I’m not going to put you on the field. Sister reminds me, constantly, that your anonymity is valuable. But, my victory here will be your victory too."
an "You’re a fighter. Haven’t you ever wondered about the thrills of conquest?"

"Those words would linger with Rowan long after the conversation was done. The thrills of conquest. He’d never truly fought a war of conquest to date. Even the events at Raeve Keep were mostly a skirmish in the scheme of things." 
"Would it feel any different from the righteous battles that he experienced in the past?"
"Perhaps, if everything went according to plan, he’d discover in a week."

return

label battleFail:

#TO DO - if goal3 is not complete or fund / troop goal is not met
if goal3_completed == False:
    
    show andras smirk at edgeright with dissolve

    "Andras suddenly rose from his seat, cracking his knuckles. The smile on his face was terrifying. His teeth glimmered."

    an "Enough of this. It’s time to get to the point, Rowan. What are we to do in this situation?"

    "Rowan put his hand to his chin. What was there to say? They didn’t have forces anywhere."

    ro "I..."

    "Andras stepped close to him."

    show rowan necklace concerned at midleft with dissolve

    an "Rowan. You can stop right there. There is no possible way that we can fight this army. The reason why not is because you failed us."
    an "Tsk tsk. Such a shame."

    "He spat. Everything from his posture to his expression went darker."

    an "Pathetic. Weak."

    show jezera happy at midright with dissolve

    je "Brother dearest, you forget the possibility that he might have simply been working for the enemy."

    if goal3_completed == False:
        je "After all, your failures in alliance building was quite the substantial blow to our cause. Perhaps you meant to trick us. To play us the fool."

    #elif didnt raise funds / troops TODO
        #je "Though, I suspect personally it wasn’t sabotage. What saboteur works diligently to secure alliances for us, but then simply fails to raise an army and funds to pay for it?"
        #an "Not that it matters. Without forces of our own, outside of any alliance, we stand no chance of holding our gains."

elif palaceStage != 2:
    
    show jezera happy at midright with dissolve
    
    "Jezera rose and approached him. Soon she was trailing a single finger tip along his shoulder blades. It was strangely menacing."
    
    je "Rowan Rowan Rowan."
    je "You did so much for us. So instrumental in gathering new allies for us. Yet, so useless when the time came to do something with them."
    je "I can tell you why I believe we’re in this situation."
    
    show rowan necklace concerned at midleft with dissolve
    
    "Rowan felt sweat starting to form on his brow. This was not the way that Jezera usually touched him."
    "She withdrew her hand, and drew closer to her brother’s side."
    
    je "It’s because you didn’t go to Rastedel. We could have had forewarning, I’m sure had you simply gone and met with our allies."
    
    je "Brother, do we have much use for a servant who doesn’t do what he’s told?"
    
    show andras smirk at edgeright with dissolve
    
    "Andras rose from his seat, face suddenly darkening sadistically."
    
    an "No. No, we do not."
    
    "He walked towards Rowan slowly, cracking his knuckles. This was not a bluff."
    
"Rowan looked back and forth between the two. Jezera was starting to draw closer now too. Andras was closing the distance fast. Rowan’s sword hand twitched."

je "I fear that our working relationship had come to naught, dear hero. Though I cannot say it wasn’t a fun experiment."

an "You’re useless to us now, cunt. Any last words?"

menu:
    "Fight.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        "Rowan’s gripped the handle of his blade. His mind was racing. This was a dangerous situation, but not a hopeless one. He’d even fought Andras before and made it out alright."
        an "Do you really mean to fight me? Gonna make it fun, bitch?"
        "Andras took a step closer."
        ro "I understand you’re angry. But, we don’t have to do this. You’ve gotten used to working with me and I’ve gotten used to working with you. It doesn’t have to end here."
        ro "But, if you refuse, I am prepared to defend myself."
        "Jezera interjected the brewing confrontation, smirking slightly."
        je "Are you now? Because, I know you well already hero. I knew that you wouldn’t go down easy. Which is why I took a few preparations before I had the maid bring you down here."
        "Before Rowan could figure out what she meant by that, he felt a sudden sharp sensation in his back. He collapsed to the floor, blood starting to pool around him."
        hide rowan with dissolve
        show rowan necklace shock behind bg6
        ro "Wha-"
        "As his vision started to fade, he looked up to see what had struck him. That was when he saw her."
        show alexia 2 necklace neutral at midleft with dissolve
        show succubus neutral at edgeleft with dissolve
        "Alexia was standing above him, with a bloody knife in her hands. She was looking at him with utterly blank eyes. To her side was a succubus grinning with malicious intent." 
        "...Why?"
        an "You dare take my prey from me, Sister?"
        "Jezera laughed coldly."
        je "Can you seriously tell me with an honest expression that this outcome isn’t way more delicious?"
        an "..."
        "Andras slowly laughed too."
        an "I admit it. You have a flair for the dramatic sister. That was almost worth missing the chance to kill him myself. Almost."
        an "Creature, best release her so she can see what she’s done."
        "The succubus snapped. At once the light returned to Alexia’s eyes."
        show alexia 2 necklace concerned at midleft with dissolve
        al "R-rowan?"
        show alexia 2 necklace shocked at midleft with dissolve
        al "Goddess no! Rowan!"
        "She stooped down to cradle him, but by that point he was already fading fast. The last thing that Rowan ever saw was the look of horror on his wife’s face as she realized what she’d done."
        scene black with fade
        "Game over."
        $ renpy.full_restart()
        
    
    "Die gracefully.":
        $ released_fix_rollback()
        "For a brief moment, Rowan considered drawing his sword. One last heroic stand in a castle full of demons. Maybe if he was lucky he could take one of them out with him. It could be his penance."
        "But, that idea was absurd. He was wearing Jezera’s magical pendant. He would die before he accomplished anything."
        "...And Alexia…"
        ro "I understand."
        "He bowed his head."
        ro "What will happen to Alexia? Will you treat her well?"
        "Andras grinned."
        an "Do you really want to know the answer to that question, worm?"
        "Rowan considered it for a moment. Then he shook his head."
        ro "I suppose I’d rather not. What’s the point? In all likelihood, I’ll get a chance to ask her first hand soon. Presuming the life after truly exists."
        ro "But, if the time I spent in this castle has left you with any fondness for me, I have one request. Treat her gently. I have no illusion that you’d ever actually release her. But, I do not want her to suffer."
        "That actually made Jezera giggle."
        je "Asking for kindness from demons. You truly never learn, hero. You know that?"
        ro "I suppose I do."
        "Jezera turned her back on the affair so she didn’t have to to watch."
        je "Get on with it, brother."
        "Andras chuckles to himself."
        an "What’s the fun if you don’t let them wriggle a bit first?"
        an "So long {i}hero{/i}."
        "Then Andras killed him."
        scene black with fade
        "Rowan Blackwell was soon forgotten by the people of Rosaria. His memory faded as the years after the war with Karnas departed."
        "As for what fate befell his wife?"
        "Without Rowan to protect her, was she tortured? Was she allowed to be happy? Was she allowed to finally just go home?"
        "One might say that no one left alive knew the answer. But, that would be incorrect. The truth is, no one left alive cared what the answer was."
        "Game over."
        $ renpy.full_restart()            
    
    "Beg.":
        $ released_fix_rollback()
        "Rowan sunk down on his knees. He was overcome with a desire to live. For the first time in his life, certain death was staring him in the face." 
        "He always thought that he was the kind of man who’d die with his head held high. Or with steel in hand."
        "But, he was not really that kind of man at all."
        ro "I- I- Please."
        ro "Oh masters please."
        ro "I need one more chance. One more chance. The next time, I will make sure that we don’t end up in such a disadvantageous situation. You don’t have to kill me now."
        ro "Please. Consider all the time we’ve spent together this past year. I’ve been helpful to you. You don’t have to kill me."
        ro "One more chance. I’m begging you."
        "Andras and Jezera went silent. The room seemed to obscure. It took Rowan a moment to realize that it was a tear rolling down his cheek." 
        "What would they do? How would they react?"
        show andras displeased at edgeright with dissolve
        show jezera displeased at midright with dissolve
        "Andras and Jezera shared a look with one another. Rowan’s heart sank. It was one of pure scorn."
        an "Boring."
        "Then Andras killed him."
        scene black with fade
        "No one would ever talk about Rowan Blackwell ever again. Nor would they talk about what happened to his wife. They both vanished from the annals of history."
        "Game over."
        $ renpy.full_restart()
        
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

label rastedel_battle_2:

#courtyard bg
scene black with fade
show orc soldier neutral at midleft with dissolve
show wild orc neutral at midright with dissolve

"Almost every fighting body in the castle was organized in the courtyard. Mercenaries and orcs alike swapped tips, tested their weapons’ readiness, and congregated together."
"At the center of the display, a square of orcs stood together, following the commands of a general. They struck out, fell backward, and acted all in unison."

os "Shields. Shields."

wo "Hup!"

"The troop raised their shields in unison."

os "Strike!"

"The front rank went down to one knee and slashed forward with their cleavers. The rank behind them jabbed forward with a motley collection of swords and axes. Standardized equipment was impossible to maintain."

os "Arrows. Arrows."

"The front row jumped back to their feet. Just in time for the entire unit to raise shields upwards. There was few gaps of any real size between them."

hide orc soldier with dissolve
hide wild orc with dissolve
show rowan necklace concerned at midleft with dissolve

"Rowan watched the scene with something approaching awe. He’d fought in the field with orcs many times. Only, always on the opposite side. These were hardly the most sophisticated infantry tactics, but they were still strides ahead of the unorganized fighting he’d seen before."

show andras displeased at midright with dissolve

an "Try not to soil yourself."
an "They’re disciplined now, but the moment the killing starts, every last one of them will break ranks. Still, they should be able to hold together for the initial charge. That’s all we really need from them."

"Rowan turned to face the demon. With a battle scheduled for the following day, he thought he’d see Andras feasting and fucking. But, he was surprisingly engaged in the preparation."

show rowan necklace neutral at midleft with dissolve

ro "Do you still plan on standing at their head?"
ro "I’m going to be on the neighbouring hill, observing. It would be safer if you were with me directing the battle from a safe distance."

"Andras spat to the side."

show andras angry at midright with dissolve

an "If you think for a moment that you can convince me not to be in thick of it, I’ve got some news for you."

ro "But, you know how battles can go. Even the victors lose people. And the moment you step on the battlefield, with your red skin and all, you will be the biggest target."
ro "You could well die out there."

"Andras didn’t respond for a moment. It was almost like the idea of death had never crossed his mind."

an "I could. So what?"

"Rowan blinked. How could he get this message across to Andras? The prospect of making him understand seemed impossible."

ro "Very well. It is not my place to make that kind of choice."

show andras displeased at midright with dissolve

an "Good. I didn’t have to remind you."

if all_actors['alexia'].flags['andras_influence'] > 10:
    show andras smirk at midright with dissolve
    an "Besides, if we were in each other’s places, I’d rather that you die. Quickly too. If you were really so smart, you’d be begging me to stay on the front lines."
    "Rowan pondered to himself what exactly Andras meant by that…"
    "...Probably just that if Andras died it would be easier for he and Alexia to escape."
    show andras displeased at midright with dissolve

ro "Can we move somewhere else?"

"Rowan glanced around the area, meeting the gaze for a flickering moment of a crusty Rosarian sellsword."

ro "I want to discuss the specifics of our battle strategy. Best not to talk about it out in the open with ears all around us."

"Andras rolled his eyes."

an "You’re starting to sound like my sister. Clearly, we’ve made a terrible mistake with you. Follow me, I know where to go."

scene bg18 with fade
show rowan necklace neutral at midleft with dissolve
show andras displeased at midright with dissolve

"Rowan looked around Jezera’s empty room. It felt rather stuffy. She hadn’t been here in days, so it felt oddly desolate. Still, why had Andras taken him here?"

ro "Why-"

an "Quiet. Jezera gave her assent for me to use the room while she is off on her fucking adventure."

ro "Of course."

"Rowan sighed."

ro "I wanted to review the information that we collected in the reports."
ro "The enemy army has encamped itself in the Astarte basin, about two days ride from Raeve Keep. We have estimates of their numbers here."

"He handed a roll of parchment to Andras."

ro "It has been confirmed that they’ve split up the army into four forces, each has fanned out to retake key garrisons and harass known orc encampments."
ro "That means that their army is divided up. Enough that if we fought a single force, we’d have the local advantage. But, with enough time and preparation, they’d be able to link up mid-battle."
ro "Or worse. Catch us from behind while fighting one force and pin us in the middle."
ro "If we truly want to win, the battle is going to come down to how effective Jezera has been on her mission. If she is successful, then we can ensure the battle is on our terms. "
ro "But, I haven’t had an opportunity to sit down with her since she last reported in. Do you have any idea if she’s been successful in her operation?"
ro "I’m genuinely worried by her lack of contact."

show andras smirk at midright with dissolve

"Andras flashed a grin and walked over to Jezera’s cupboard. But, otherwise, he didn’t even respond to the question."

ro "Master?"

an "Do you think I didn’t hear you? Shut up and wait."

"Andras pulled out a crystal ball from the cupboard. Rowan had seen Jezera with it before. From what he recalled, it was some kind of spying tool."
"The demon set it down on the table."

an "Say what you will about her, but sister is a clever little creature. She set her scrying crystal to her own signature before she left, and told me to keep track of her that way. Far easier than needing regular reports from her."

"He tapped the crystal once. After a few seconds, it came to life. At first it showed merely swirling light. But, that gave way in moments to a clear image. Two humans, one male and one female, in the midst of a sexual tryst."

menu:
    "Watch.":
        $ released_fix_rollback()
        jump jezBattleSex
        
    "Look away.":
        $ released_fix_rollback()
        show rowan necklace concerned at midleft with dissolve
        "Rowan ducked his head away immediately. He didn’t really want to look at it. Besides, it was not hard to guess what was happening."
        ro "Is that Jezera?"
        "Andras nodded."
        an  "It’s her and the enemy’s main commander right now. She’s worked her way in enough that she’s influencing him directly."
        an "You thought she failed, didn’t you, little hero?"
        show rowan necklace neutral at midleft with dissolve
        "Rowan shook his head."
        ro "Not at all. I knew she’d accomplish something. I’ve seen how good she is at manipulation first hand."
        ro " I just didn’t expect her to do so quite this well."
        "Andras shook his head and got a dark glint in his eye. It worried Rowan slightly. With Andras, one was always on the precipice of violence."
        an "You’re a strange one, hero."
        an "After all this time, you still underestimate her. You underestimate me too."
        "Andras turned off the crystal ball screen with another tap. The image in it swirled away into a mist, leaving nothing but a reflective surface in its wake."
        jump postBattleSex
        
label jezBattleSex:

#jez excursion cg1
scene black with fade

"The crystal ball showed an older gentleman was on his back, being ridden by a naked blonde. Her hands roamed over her body in jerky motions as she ground herself down on him."
"The image was so vivid. It was like he was really in the room able to see it. It took him a startled second to realize he could even hear it too. The ball emitted the faint sound of panting and groaning. Was the crystal ball really that effective a spying tool?"
"After a moment studying what the ball displayed, Rowan was able to figure out who one of the participants was. He’d seen that blonde before…"

scene cg5 with dissolve
pause 3

"The blonde woman, with vaguely Prothean features, who’d visited him the day of the attack on Arthdale."
"Jezera. She’d done it."


#jez excursion cg1
scene cg249 with fade
show rowan necklace neutral behind cg249
show andras displeased behind cg249
pause 3

"Her body bounced up and down, and moved with vigorous intensity. But, it was clear that the effect was one sided. The man was twisting his face and groaning. He was totally enraptured by the pleasure. Lost in it."
"But, Jezera? She was just smiling. In total control of her reactions. In total control of the man."

ro "She was this successful?"

"The plan had called for her to work her way into the camp and try to get close to one of the commanders. But, this was clearly the head commander’s tent. In under a week, she’d gotten herself in this much of a power position…"

an "You underestimate her, Rowan. You underestimate us. On the field of battle, no human can stand in my way. In her web of spiders, no human can best her."
an "Of course she was successful."

"Rowan turned back to the lewd display in the crystal ball. Jezera was still playing the man like an instrument. If she slowed down, he’d groan one way. If she sped up, he would groan another way. Almost like she was putting on a show for them."
"Did she know that they were watching her?"
"She was moving her body so skillfully now. Rowan could almost feel the friction of her movement." 
"The general could handle no more. He went rigid and jerked uncontrollably. Rowan even saw his eyes roll up. When he was done, he went stiff and sunk down further to the ground."

#jez excursion cg2
scene black with fade

"Jezera leaned down, cock still buried between her legs. Even as the general was limply gasping for air, Jezera led her body cover over him. Her lips pressed themselves to his ear."
"Rowan could not hear the whispers that streamed from her mouth. But, he could see the soft nibbling kisses that she left between sentences. He could also hear the responses that occasionally he let slip."
"Whatever it was she wanted, he sounded more than happy to give it to her."
"She gyrated slightly. Her breasts rubbed against his chest. A bit of his seed leaked from her cunt, and she even continued to softly roll her hips, as if still fucking his softening cock. The entire scene was strange in both its intimacy and its menace."
"The point had been gotten across. Andras chose this as the moment to bring down the feed from the crystal ball. Rowan’s eyes lingered on the empty reflection until he realized what had happened." 

scene bg18 with fade
show rowan necklace neutral at midleft with dissolve
show andras displeased at midright with dissolve

label postBattleSex:

an "I believe that’s the end of our business for today. Now, are you ready to leave me be so I can get ready for tomorrow?"
an "I’ve got a show to put on."

show rowan necklace concerned at midleft with dissolve

"Rowan sighed. There was still all sorts of uncertainties. But, they would know where the enemy was and fight them on their own terms. Still, tomorrow was the day it rested on. No plan survives first contact with the enemy."

ro "Good night, Andras. Good luck."

"As Rowan walked out of the room, a voice whispered in his head that he might be seeing Andras for the last time."

if (all_actors['alexia'].flags['andras_influence'] > 10 or avatar.corruption > 60) and rowanAndrasSex == 0:
    "It made him feel elated, if not somewhat concerned."
    
if rowanAndrasSex > 0:
    "He wasn’t sure how he felt about that, honestly."
    

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

scene bg31 with fade

"A portal opened on a tree covered hillside underneath Mount Scopus. Out stepped a cloaked man. Rowan."

show rowan hood neutral at midleft with dissolve

#TODO: If Helayna Knight Path
    #"Behind him, stepped another figure. This was covered in thick steel armor. Though the appearance of a Rosarian knight would leave little chance of drawing enemy attack. Helayna stood by his side, ready in case the battle came here as well."
    #show helayna neutral

"Rowan did not have a great mission here. Indeed, he didn’t have to do much of anything at all. He was here to watch." 
"Beneath him the Astarte Plains rolled in every direction. It was bounded by mountain ranges on both sides, and filled with small villages. From his vantage point, he could see the three different villages selected as bases by the Rosarian army." 
"They were separated by miles from one another. Just like the plan called for."
"Rowan caught the flash of movement that indicated the battle was about to begin. The glimmer of the sun reflecting on armoured troops as they marched in a line up to the summit. The fourth division. It was where they had been told the orc encampment was."

#TODO: If Helayna Knight Path
    #"Helayna clung tightly to her hilt. Her breath was heavy. Expectant."

"At the top waiting for them was a mass of orcish fighters, howling and putting on their war paint. Nothing in the numbers that would actually threaten the column of approaching troops."

#TODO: If recruited goblins
    # "But, what could not be seen was the whole host of goblins, hundreds and hundreds strong, waiting in hiding at the wings. And at their head...Andras."

if orciad_state == 2:
    "But, what could not be seen was the whole host of orcs, the vanguard of the northern confederation, waiting in hiding at the wings. And at their head... Andras."

"The eruption of violence happened in a flash. A wave of green went running down the hill towards the knights...only for other waves of green to emerge at the army’s sides."
"Rowan held his breath. It was starting."
"Through the emerging melee, Rowan strained his eyes to get a better view of what was happening. The waves broke. There was no lines or formation, just chaos and scattered individual fights. That was good. Probably. "
"In the crowd, for a brief moment, he spotted a flash of moving red. Perhaps a bloodied figure. But, perhaps Andras as well. And he was running around far ahead of their lines all by himself." 
"Did that fool want to die?"

#TODO: If Helayna Knight Path
    #ro "Can you see that figure over there?"
    #ro "Do you see if it’s Andras or not? If there is armor underneath the red or not?"
    #"Helayna shook her head sadly."
    #hel "I cannot, my love."

"This phase of the battle ended quickly. After all, they had both the advantage of terrain and surprise. The human forces crumbled and fled down the mountainside in a chaotic route. It hadn’t even been twenty minutes. With their backs to the enemy, they’d be vulnerable prey."
"Only, they was not what the plan called for next. Rather than pursue, the orcs formed their ranks again and waited. Rowan searched out for the red figure, but could only see a sea of green."
"He baited his breath. That had been the easy part. Now the others knew they were there. They would move to join up before a larger army could intervene."
"But, this was not a normal army."
"There was a purple flash. From down on the mountainside, Rowan could only just make it out. But, he knew what it meant. It was the flash of Jezera’s teleportation magic. "
"Then there was a second burst of light. When it cleared, they were gone. Every single fighter they had on the mountain side had been there one moment, and was gone the next."
"A minute later a clatter came up from the basin. Troops fighting and killing each other. Rowan turned his attention onto the new action. The second camp was under attack. A moment before they’d been suiting up and getting ready to support their allies. Now they were the center of the fighting."
"Now the real battle was on."
"Over the next few hours, the Astarte Plain was filled with the muffled sounds of screaming, fighting, and dying. The action seemed to move over many miles. Human forces moving to try to link up. The sudden appearances of Bloodmeen’s army in new places."
"Rowan’s mind was constantly racing. Were they winning as quickly as they needed too? Beating any of the individual forces would be inevitable. But, if routed troops rallied, or one of the other forces managed to link together, it would be the end."

#show plains night time

if orciad_state == 2:
    "The orcs met the final human force in battle, just four hours after the fighting had started. By now they were whittled down enough from casualties that it left Rowan genuinely worried. A little village along a river went up in fire as the clash grew more fearsome."

#if goblins recruited
    #"The goblins met the final human force in battle, just four hours after the fighting had started. By now they were whittled down enough from casualties that it left Rowan genuinely worried. A little village along a river went up in fire as the clash grew more fearsome."

"He waited."
"He waited."
"He waited."
"Then, finally, he saw the last of the humans break. The fading light glimmered on the armour of men and horses as they made a desperate, pathetic break for life."
"It was over. The humans had been defeated."
"There were still sounds emanating from the little village. No doubt the cleanup operations. Part of the army would need to break off to cut off the retreating enemy as well." 
"Stragglers would make it back to Rastedel, of course. But, there was no escaping en masse from a teleporting army."
"Rowan put a hand to his chin. The fighting was no doubt over by now. It was time to see the results first hand." 

"Besides, he had not caught a single glimpse of Andras since that moment on the hillside. He needed to know the most important result."

#TODO: If Helayna Knight Path
    #ro "I’m moving down to check out the battlefield for myself. It will be safer up here. I prefer if you wait."
    #"Helayna chuckled."
    #hel "You are not going down there without your bodyguard. I won’t allow it."
    #"Rowan rolled his eyes. Her armor might be a problem, but he was certain anyone on their side knew not to attack him."
    #ro "Very well. Stay close. And keep your weapon holstered. No misunderstandings."
    
scene black with fade

if orciad_state == 2:
    "The first thing he noticed was the smell. It stank of blood, piss, and shit. Horses, orcs, and men all had different smelling fluids and waste. Their unique scents melded together in close proximity."

#if goblins recruited
    #"The first thing he noticed was the smell. It stank of blood, piss, and shit. Horses, orcs, goblins, and men all had different smelling fluids and waste. Their unique scents melded together in close proximity."


#show Close up of Andras on the Field CG of the commander’s head on a pike.
scene cg244 with fade
pause 3

"Arriving at the village, Rowan stared at a head on a pike. He’d seen this man before. It was the commander who’d Jezera had been fucking the night before. It hadn’t worked out well for him."
"Did he have a wife? Did he have a family?"
"What would they have said about his final hours? What would they have said about his gruesome fate."
"Rowan didn’t show any signs of visible disgust. It was hardly the first mangled body part he’d ever seen. It was hardly the first mangled body he’d seen on his way over here." 
"The gore was generally localized to areas where specific fighting had occurred. So on the way over he’d only seen a few odd bodies."

if orciad_state == 2:
    "But, once he arrived at the village where the final clash had taken place, there was nothing besides bodies. The streets ran with blood. Human blood. Orcish Blood."

#if goblins recruited
    #"But, once he arrived at the village where the final clash had taken place, there was nothing besides bodies. The streets ran with blood. Human blood. Goblin Blood."

#TODO: If Helayna Knight Path
    #"Helayna, though had a hand to her mouth. She had been one of the best trained fighters in the entire land. But, she had been too young to take part in the worst battles of the last war. She’d have never seen the gore of a victorious chaos army."
    
"Even if Rowan had been able to keep walking at the sight of dead troops, there was another sight that stopped him in his tracks."
"This had been a village. They were provisioning a force from the capital, but the rapid onset of the fighting had left little time to flee. So, littered among the bodies, were women and children. Their blood too profaned this ground."
"Rowan had to close his eyes and turn away to not look at them."
"He leaned heavily against the wall of a nearby hut and looked around. It was a desperate effort to focus on something...anything...else."

#Show Andras on the Field CG
scene cg245 with Dissolve(0.75)
pause 2
scene cg246 with Dissolve(0.75)
pause 2
"What he focused on was Andras."
scene cg247 with Dissolve(0.75)
pause 2
scene cg248 with Dissolve(0.75)
pause 2
show andras displeased behind cg248
show rowan hood neutral behind cg248
#show hel if present


"Andras sat in the center of the village, under a banner of headless corpses and amidst the musk of the dead. A throne had been erected for him. Its savage splintered wood made it look like Andras sat atop a wreckage."
"In front of him, many captives crouched in terror. It was no wonder why. All around them, orcs were bringing cleavers down on their fellow men. They laughed as they butchered those who could not defend themselves."
"So to these dirty, weary men the mercy of Andras was their only salvation. There must have been a hundred men here."
"Rowan stayed in the shadows, not to be seen. These men were to be brought back as prisoners. But, there was no telling how word could get around if he was seen."
"Rowan focused his gaze on his master. His concerns really had been for nothing. Andras was covered in knicks, and dried blood. But, most of it was not his. How many men had Andras slain today? 10? 100? More?"
"It was wrong to doubt him. He may at times act like a dumb oaf, but on the battlefield he was a dragon."

an "Bring forward the highest ranking commander. Let him appeal to his new Master."

"One of the orcs grabbed a soldier with a long grey beard and dragged him, kicking and punching the entire way, to Andras."

an "Tell me, human commander. What is the most important thing to a leader of men?"

comm "...Victory."

"Andras roared with laughter."

an "Well, it’s too late for that, fool."
an "Let me simplify it a bit for you. I know you must have had a bad day."
an "What is more valuable to you? Your life? Or the lives of your men?"

"Rowan crossed his arms over his chest. He knew that Andras planned to keep these men alive. It was clearly a sadistic game meant to make the man quiver."

comm "..."
comm "...It is the lives of the men."
comm "Do as you will with me."

"Andras signaled an orc at his side. With a single swipe of his blade, the commander’s head was removed. It soon adorned one of the pikes that had been planted in the ground. His blood leaked out into the wet mud."

an "Bring forward the next in charge. I’m not done with dessert yet."

"Another man was hauled forward. This time there was no kicking or punching. He followed along with the resigned expression of a man on his way to the gallows."

an "What is more valuable to you? Your life or the lives of your men?"

"The man looked back at the huddled mass of prisoners. They stared back at him with hungry pathetic eyes. They pled to him silently."
"He lowered his eyes back to Andras’ feet."

comm "I have a family…"

an "A little wife in the country? A brat or two?"

"The man remained silent. So Andras kicked him."

an "Answer the fucking question, worm. Your family. Tell me about them."

comm "...N-no wife. She died. Or left. I don’t know. But, two daughters."

an "How old?"

comm "Nine and thirteen."

show andras smirk behind cg248

"Andras smirked darkly. There was blood in his mouth. It too could have been either his own or someone else's."

an "Your life? Or the others?"

"The commander looked back at the prisoners one last time."

comm "I need to see them again...I’m sorry…."
comm "My life. My lord. I’ll serve you. I swear. Just let me live."

"Rowan sighed. Knowing Andras, after that entire show he’d probably just kill the man. Perhaps claim it was a lesson in selling out your comrades. He readied himself for the man’s surprise execution."
"But, that was not what happened."

an "We have our answer, boys. Kill them."

"A troop of orcs went down the crowd, stabbing, beheading, and slaughtering everyone in the pile. The first few victims raised their hands and screamed, but otherwise offered no resistance."
"Some of the men in the back, especially the few who still had some kind of weapon, tried to mount a last ditch defense. Anything. But, there were too few of them, and they were boxed in. As the men around them went down one by one, methodically even, the walls grew closer."
"The commander sunk to his knees, mere inches from Andras’ throne. All color left his face."
"Rowan almost rushed to stop the massacre. No. No. No. These men were supposed to be taken as prisoners. The fighters had to die, but these men had surrendered. He only stopped himself with great effort. There was nothing he could do."
"Had...had Andras planned this all along?"

#TODO: If Helayna Knight Path
    #"Helayna sunk to her knees, dumbfounded by what she was seeing. She had sworn to serve Rowan, regardless of his ends. But, how could she compartmentalize this? It was not an easy thing to call just a casualty of serving Rowan."
    #hel "I didn’t...I didn’t…"
    #hel "No."
    
"When it was all done, when every last cowering man was now a leaking corpse, Andras rose to his feet clapping. It was as though he’d just seen a symphony." 
"With almost an after thought, he reached down and grabbed the commander’s head. Sensing something was wrong, he tried to protest. But, he couldn’t make it too far, because seconds later, Andras twisted his neck all the way around."
"It seemed he wasn’t going to see his daughters any time soon."
"Rowan wanted to vomit. His eyes blinked rapidly, as though the moment of darkness would actually take away the sight. He felt woozy. He needed to...He needed to…"

#TODO: If Helayna Knight Path
    #ro "I need a moment to myself. Just a moment."
    #hel "Wait! My love, you shouldn’t be all alone here. Please."
    #ro "No!"
    #ro "I just need...a second to myself. Please."
    #"Helayna gave him a worried expression. But, she could not deny him his request. She gave him a sad nod."
    #hel "Just be safe. Please."
    
#else:
"Rowan stumbled away, almost tripping over his feet. He couldn’t stay here any longer."

scene bg4 with fade
show rowan hood neutral at midleft with dissolve

"Half a mile outside of the village, there were still bodies strewn about. Bodies on the edge of the river. Bodies on the roadside. Bodies in the tall grass."
"He sunk to his knees, just by the riverbed. What had just happened? How could he have missed what he was doing until now?"
"He was so concerned with Alexia’s well being...with his own well being...that he hadn’t stopped to think about the effects he might have."
                                                                                                                                               
if avatar.corruption > 30:
    "He thought that he was ready for such a spectacle too. Wasn’t his days of fighting for the old order dead? This should have felt like nothing to him"

else:
    "But, now here he was. Kneeling in a stew of organs and suffering, wondering how he got here. What wrong turn he’d taken." 
    "How had he not processed what affect his actions would have? So many dead. So many dead."

"As he knelt, he heard something dragging along the river. It was a body. A soldier in broken chainmail settled down the river, leaving a red trail in his wake. Something to remember him by."
"But, even as he stared at this scene, Rowan felt something else bubble up inside of his belly. It wasn’t just disgust. It was a strange feeling to have in a moment like this. Perhaps, the reason that he felt such a strange dissonance watching the scene before."
"He felt…."

menu:
    "A heroic resolve":
        $ released_fix_rollback()
        "As much as he wanted to throw up, there was also something else in his stomach. A fire that had not been fully formed until he’d seen the true results of the twins’ brutality."
        "At that riverbed, Rowan silently swore there would be a reckoning for this. That someone would pay for all of the pain and bloodshed that this renewed war had caused."
        "That he had caused…."
        "...No. No. That Andras and Jezera had caused. He was a captive because of them. The fighting was because of them. If Rowan ceased to exist, their reign of terror would just continue."
        "One day they would pay for this. They would both pay."
        "He would stay alive until then. He had to." 
        "He had to."
        $ change_base_stat('c', -3)
        $ battleChoice = "resolve"
        return 
        
    "...The pride of a subordinate":
        $ released_fix_rollback()
        "He tried to put his finger on the emotion he was feeling. It wasn’t happiness. Who could be happy looking at this tragedy?"
        "It wasn’t adrenaline or victory. He’d never been in the fighting. All he’d done was observe from a hilltop."
        "No. It was something else."
        "...Perhaps, it was pride?" 
        "Rowan looked around him. There had been a mighty army here. Strong enough to face down any horde in the realm. But, he’d put together a strategy that had destroyed them. For all of the horror that came with, there was a certain buzz to it."
        "But, it wasn’t just that either."
        ro "It was expected of me…"
        "That was it. It wasn’t just that he’d done so well under pressure. It was that he’d been tasked with this. His masters had come to him and told him that he needed to fix this. He needed to come up with a plan. And he did."
        "His head buzzed."
        "He’d done a good job?"
        #show close up of pike cg
        "Hadn’t he?"
        $ change_base_stat('c', 3)
        $ servant_route += 1
        $ battleChoice = "pride"
        return
        
    "The thrill of conquest":
        $ released_fix_rollback()
        ro "Heh."
        ro "Heh heh."
        "This was his fault. He’d done this. All these people were dead because of his plan."
        ro "Heh heh heh."
        ro "Hah hah hah."
        "So many dead. Thousands dead. It was horrible. It was disgusting. It was the most soul crushing moment of his entire life."
        ro "Hahaha. Hahaha. Ahahaha."
        "And at times it almost felt good."
        "None of this would be possible without him. Andras may have led the charge, but this was his strategy. It was his victory. Every element of his plan had come off perfectly."
        ro "Ahahaha. Ahaha. Hahahahah."
        "It was almost a rush. Almost a shot to the arm. Was this what Andras had meant? Was this the thrill of conquest? His conquest?"
        "It was the greatest thing he’d ever accomplished in his life. No help from the other heroes. No one giving the orders but him. It was his masterpiece. Wasn’t that hysterical?"
        ro "Hahahaha. Ahahaha."
        ro "Hahaha. Ha."
        $ change_base_stat('c', 5)
        $ overlord_route += 1
        $ battleChoice = "thrill"
        return


########################################################################################################################
########################################################################################################################
########################################################################################################################

label rastedel_battle_3:

scene bg27 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve
show jezera happy at midright with dissolve

if battleChoice == "pride" or battleChoice == "thrill":
    "Jezera raised her goblet high into the air. The hundred or so commanders and important leaders crowded around the room followed in suit. Rowan followed along... If only to not seem out of place."

else:
  "Jezera raised her goblet high into the air. The hundred or so commanders and important leaders crowded around the room followed in suit. Rowan followed along."
   
je "And this one is to our heroic field commanders, who risked the swords of the despots for the sake of a better world."

cro "Go with Pride. Go with Power."

"The entire room took a drink from their cups."

je "And this one is to the guides and spies, who risked life and limb to ensure that our glorious armies were not left blind on the battlefield."

cro "Go with Pride. Go with Power."

"Rowan slumped slightly in his chair. This had been going on for the better part of twenty minutes now. If he enjoyed this kind of pageantry, he wouldn’t have been so accepting of being forced out of Rastedel in the first place."

if battleChoice == "pride":
    "After a few seconds of hesitation, Rowan finally lifted his goblet high like the rest. For better or for worse, though mostly for worse, it was only through the power of Jezera and Andras that victory had even been possible."
    "Rowan supposed this was just how they took pride in it."

elif battleChoice == "resolve":
    "Here the entire castle was, drinking and having a merry time. Did no one care about the bodies clogging the rivers of Rosaria? Did no one have anything to say about the slaughter of the prisoners?"

if battleChoice == "thrill":
    show rowan necklace angry at midleft with dissolve
    "Rowan had to stop himself from scoffing. Andras led the charge. Stupidly, he might have added. Jezera’s magic was useful. But, at the end of the day, the entire plan would have been a disaster without him."
    "He saw the weakness of the Rosarian formation. He understood the tactical value of divided armies. It was his victory. Yet, Andras and Jezera were on the podium being lauded, and he was relegated to the gallery."
                                                                                                                                                                                                                         
    if avatar.corruption < 30:
        show rowan necklace concerned at midleft with dissolve
        "Rowan shook his head. What was he even saying? The battle...its consequences...it had all been so horrible. How could credit for such horrors be a thing to desire?"
        "No wonder he was struggling not to glare at his Master and Mistress. What kind of creature desired credit for such a thing?"

    show rowan necklace neutral at midleft with dissolve
   
hide jezera with dissolve

"It was only this side of the ledger that was feasting." 
"Those captured Rosarian soldiers that had actually been brought in were being kept in the dungeons while assignments were made for them. Though, there were only grunts there. No one knew where the captured commanders had been sent."
"To escape his malaise, Rowan’s eyes searched the room."
"To his side, Alexia sat awkwardly. She’d dressed up for the occasion. No doubt she understood what had transpired to cause this feast. The news was all over the castle. But, she hadn’t told him what she thought of it."

if helayna_escaped == False:
    if helPath == "bedslave":
        show helayna collar neutral at midright with dissolve
    else:
        show helayna neutral at midright with dissolve
        
    "If anything, throughout dinner, her attention was focused on the person sitting on the other side of the table. Jezera had chosen to seat Helayna on the other side of the table. The two had spent much of dinner shooting each other dirty looks."
    "Had Jezera not bothered to consider the problems with seating them close to one another? Or had she done this on purpose?"
    hide helayna with dissolve
    
elif all_actors['alexia'].relation > 30:
    "Clearly, she sensed that Rowan was tense. Off and on over the past two hours, she’d been putting her hand on his shoulder for soft rubbing. He replied every time with a small smile. Even still, she was his anchor."
    
else:
    "If anything, her presence was just another source of stress from him. She’d spent much of the evening leaning across the table to talk to one of the men who’d been at that battle. That was when she wasn’t drinking deeply or staring off into space."
    "It was so hard to see her thoughts behind her eyes."
    
show andras happy at midright with dissolve

"Andras sat in the place of honor, right next to his sister. But, while she was composed and proper, he was downing as much alcohol into his body as Rowan had ever seen a man drink. She was a queen and he was a warlord."

an " ...Don’t actually need a weapon to kill a..."

"Just what did it take to leave a demon blasted? Rowan had spent the better part of the evening finding out. Andras had started out with rousing drinking contests and had reached the point where he was half slumped on the table murmuring."

hide andras with dissolve
show clamin happy at midright with dissolve

"Cla-Min had perched herself in the corner of the room. Rowan wasn’t exactly sure what she was doing, but people from the table kept on coming to her and putting coins in her hand. Better not to worry about it too much."

hide clamin with dissolve

#if goblin quest completed (TODO)

if orciad_state == 2:
    show skordred neutral at skorright with dissolve
    show tarish neutral at midright with dissolve
    
    "Skorded had risen to the dais, and had started talking to Tarish. As the highest ranking orc in the room, she was given prime placement right next to the twins. Skorded was discussing a familiar topic."
    
    sk "I see nah reason dat there needs ta be any heirachy among Kharos’ faithful after the victory. The Orcs will..."
    "Tarish didn’t seem like she could care less, but was tactfully nodding along to whatever he said. It was incredible how he could hold a conversation with so little input from the other person."
    
    if tarishBetrayed == True:
        "For a second, Rowan thought that she had shot a devious grin his way, but he couldn’t be sure. Tarish always seemed to be up to something."
        
if delane_status == "tarish":
    "For a second, Rowan thought he saw Tarish wink at him from the podium. But, in the chaos of the party he couldn’t be sure."
    
hide tarish with dissolve
hide skordred with dissolve
    
if delane_status == "ulcro":
    show ulcro happy at skorright
    show eleanor dress happy at midright
    "Between Tarish and Jezera were the smiling pair of Ulcro and Delane. Ulcro hadn’t taken part in the fighting, but was soaking in the praise and glory nonetheless. His warriors had been the backbone of the fighting after all."
    "He paid little mind to his woman, who was whispering back and forth with Jezera about something. Delane had stopped to speak with him briefly near the beginning of the feast, but had spent the rest of the time politicking about. It was a role she was a natural in."
    hide ulcro with dissolve
    hide eleanor with dissolve

if delane_status == "batri":
    "Batri had parked himself between Tarish and the Twins, in a position where he could oversee the rest of the feast. Despite his insistence, he’d been persuaded to stay back from the fighting. But, the critical role of his men meant he still got much of the glory."
    "He spoke in grunts with the progressively more and more sloppy Andras. A pale human woman was positioned underneath their segment of the table, and had spent the past few hours eagerly worshipping his cock."
    "It was a woman who Rowan knew quite well by this point."
    hide batri with dissolve
    
"But, eventually even just watching grew frustrating. It was like there just wasn’t enough air in the room. The more people there the more of it was sucked away. Rowan rose from his seat."

ro "Excuse me for a moment."

al "Is something wrong?"

if all_actors['alexia'].relation > 30:
    "She looked at him sympathetically."
    
ro "It’s nothing. Truly. Please, continue to enjoy the meal. It’s not often we get a chance to have a party around here. It must be a nice change of pace."

"Alexia mumbled off her reply in a voice quiet enough to avoid being overheard."

al "A shame it couldn’t be on better circumstances…"

"Rowan made for the door, keeping quiet so no one remarked on his departure. He wasn’t on the dais. Few would probably notice his disappearance."

if helayna_escaped == False:
    if helPath == "bedslave":
        show helayna collar neutral at midright with dissolve
    else:
        show helayna neutral at midright with dissolve
    "Of course, Helayna noticed. But, as she too started to rise from her seat, Rowan gestured for her not to follow. She was always so dutiful. She gave a soldier’s nod and kept in place."
    hide helayna with dissolve
    
scene bg14 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan looked out a window from a nearby spire. The sound of shouting and the light of fires wafted up from the courtyard. While the commanders feasted inside, the common troops were throwing a party on the courtyard." 
"When you’re a common frontline soldier, surviving is always worth celebrating. Rowan had been to parties like the one below before...if only with a slightly different mix of species. During the Eoleoan campaign, he and Lorelyn had celebrated the battle of..."

show orc soldier neutral at midright with dissolve

os "Hummie."
    
"Rowan looked to the side. He was standing next to one of the orc commanders who’d been at the commander’s feast."

os "Da battle. Came from yo head, yes?"

"Rowan shook his head."

ro "I was in the room. It was Andras’ idea mostly."

os "But, ya helped, ya?"

ro "I suppose I did. Yes."

show rowan necklace shock at midleft with dissolve

"The orc gave him a spartan nod of the head. By the standards of orc, it was high praise."

os "Nevah fought many hummies before an made it out wit as many of mah boys still talkin’. Some ‘o my boys lived ‘cause a ya. "
os "You sumtin special."

hide orc with moveoutright

"Without a further word, the Orc Commander kept on walking. He left Rowan in a state of silent shock. How could he even begin to process that?"

if battleChoice == "resolve":
    "…Was saving the lives of orcish raiders a good thing?"
    
if battleChoice == "pride":
    "How long had it been since he’d heard something as simple as the praise of fellow soldiers for a job well done?"

"He was still standing there when someone else arrived to speak with him."

show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

je "Alas, even my most faithful servant finds my own parties boring. What’s a woman to do about it?"
je "Mind joining me for a walk, my little hero?"

"Rowan raised an eyebrow. What was she doing out here? Wasn’t she entertaining dignitaries and basking in praise?"

ro "Do I have a choice in the matter?"

je "What a silly question."

"So, Rowan went walking with Jezera. It was clearly apparent she was leading him somewhere. This was no random walk."

ro "Is Andras going to join us?"

je "Alas no, he’s too busy trying to figure out the limits of our own expanded alcohol tolerance. Results so far suggest he may have found it."
je "But, he’s already heard the entire rant I’m about to give you and agreed with it. You can consider all of this as coming from as well."

ro "Entire rant?"

"Jezera giggled to herself."

je "My word, you didn’t think I’d excuse myself from my own victory celebration without a good reason, did you? You know how I do enjoy my little parties."

"Rowan sighed. Of course, she was up to something. Though, at the very least it meant that there wouldn’t be consequences for skipping out on her special self-congratulatory celebration."

show rowan necklace concerned at midleft with dissolve

ro "This is the path to the dungeons, isn’t it?"

je "I would have hoped you’d be astute enough to notice that by now, yes."

ro "Should I be concerned?"

je "Not a fan after your last visit? I can hardly blame you."
je "But, no. The news is positive today. Some plans have decided to at last bear some fruit."

"The two stopped at the door to the dungeon. But, rather than push open the door, Jezera walked to a segment of wall right next to the door and pushed on an innocuous looking stone. Before Rowan’s very eyes, a segment of wall re-arranged itself to form a doorway."

je "After you."

scene bg8 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at midright with dissolve

"The first thing Rowan noticed when he entered the dungeon was a sound. A disgusting, thrashing and squelching that was quite unlike what he’d ever heard before. That was new. That was very new. Moving flesh."
"Rowan walked through mysterious passways and over stone steps. And yet, Rowan could not focus on the questions of this place. How long had it been here? Had every moment he’d spent in the dungeons, prisoner or otherwise, been observable from here?"
"But, those questions were drowned out by the otherworldly sounds seeping through the walls. Just what were they keeping down here?"

je "This should be far enough."

"They arrived at a round opening in the hallway. A pair of metal double doors stood at the front of the opening. And from behind it, a low constant rumbling. The sounds not only found their source, but was joined with the stench of fluids."

ro "What is this place?"

je "A little spot where we like to engage in my projects from time to time. Don’t worry too much about it."

"Rowan found it hard to accept that direction."

je "The important thing is...we finally have some new intelligence. The accursed silence is over. Just in time too. Dreadfully suspenseful wait."

"Rowan didn’t much think that “silence” was the right word to describe the current situation. Not with the slithering sounds of movement coming from just the other side of the door."
"Jezera produced a letter from somewhere that Rowan didn’t see, and that frankly confused him. Rowan grasped it from her hands."
"“Well, the baker’s wife thought she could sneak a few loaves out in the middle of the night, but that didn’t do so well for her. The business is starting to look shaky.”"
"“I’d hate to ask a favor from such a dear friend, but with the situation as bad as it is, maybe you’d be willing to part with one of your laborers for a little while. Perhaps that strapping one I’ve talked to you about. Please, you must help. The business is at stake!”"
"Rowan returned the letter to Jezera."

#deception score is high enough (to do)
    #"Rowan put a hand to his chin. Jezera wouldn’t show him this if it wasn't important. This clearly had to be in code. But, what was it code for?"
    #"Something was in chaos. Baker’s wife. And a call for…"
    #ro "This is from Ameraine, isn’t it? She wants me to return to Rastedel. The first part is a bit trickier. But, something big is going on there."
    #"Jezera gave a shallow clap. The sound of it was drained out by the rattling of the doors. Rowan thought he heard a voice cry out."
    #je "Not bad, but you still have a long way to go, little hero."

#else

"Rowan put a hand to his chin. What on earth was this? Jezera wouldn’t show him something of the sort if it wasn’t important. It was probably code for something. But, Rowan couldn’t tell for what."
"Rowan shook his head."

show jezera displeased at midright with dissolve

je "Really now? Not even a guess. I’m going to have to give you more serious instruction at some point."

"Behind them, the door rattled slightly. Rowan thought he heard a voice cry out."

show jezera happy at midright with dissolve

je "It’s from Ameraine. It’s a call for you to return to the capital."

#rejoin

je "What it seems that our mutual friend is saying is that the time is ripe. The baker’s wife here is our dear devout friend Marianne. She tried to pull a fast one, and it’s turned the capital into open chaos."
je "So she is clearly insinuating that you must return swiftly to strike while the iron is still hot."

ro "We didn’t hear anything from her before the battle. Not a word about the army. Why should we trust her now?"

quest "Ahhhhhh!"

"That one was definitely a human voice. Female too from the sounds of it. Just what was happening back there?"

je "Well, strictly speaking, I don’t really trust anyone. But, I’m not especially suspicious of the letter."
je "There’s a key line in there. Marianne tried to pull the wool over people’s eyes it seems. She’s saying that as far as most of the capital is concerned, the fact that there was an army out in the field at all was news."
je "Granted, normally I wouldn’t be so quick to believe her. Only…"
je "..This time I have corroborating evidence."

ro "Corroborating evidence?"

"Jezera chuckled to herself."

je "Back up a bit, would you darling."

"Rowan retreated to back of the room."

je "Remember how I said that I just came down here because this was a safe place to talk?"
je "I lied."

"She snapped her fingers. At once the metal doors flew open."

#Show a very blurry version of The Other Feast CG 1
scene black with fade
show rowan necklace shock behind black
show jezera happy behind black

"Rowan only got a glance behind the doors for a second. There was a set of bars. Behind that, a swirling grey-green mass. The swirling, living thing behind the door wasn’t alone either. Vague skin toned bodies were intermingled, throbbing and writhing against it."
"He only caught the blurry outlines before pulling his head to the side, but it was clear what was happening. There were people in there and something was fucking them."

ro "Wha…"
ro "What is that thing?"

"Jezera giggled."

je "Turn your head immediately? How are you still such an innocent, Rowan. "
je " It’s called a Wulump. It isn’t surprising if you’ve never heard of it. It’s a rare and exotic creature that we were lucky to get possession of."
je "After testing it on some volunteers, we learned that it has many valuable properties when it comes to interrogation."

if alexiaWulump == True:
    je "I assure you that you’d enjoy our selection of test subjects."

"Rowan blinked softly. Did that mean that the human shaped things that he’d seen had been…"

menu:
    "Look at the wulump.":
        $ released_fix_rollback()
        $ wulumpLook = True
        #show other feast Cg1
        scene black with fade
        show rowan necklace shock behind black
        show jezera happy behind black
        "Rowan slowly turned back towards the doors. Now he could see the contours of the...the creature as it moved about. Long slithering tendrils sloped along the walls like coils of serpents. It must have been very large. If the thing had a body, he could not see it."
        "And in these disgusting limbs? People. Naked humans writhing and gasping. Rowan’s eyes were drawn to a woman, no doubt a knight if she was being interrogated, who had been forced to the ground by the weight of the creature’s body."
        "She was not being left alone. The Wulump was filling her with appendages. Penetrated in the mouth. Penetrated in both holes below. If he had not known it to bebiologically impossible, he might have assumed that it ran straight through her. Spitroasted. Turned into its sleeve."
        "The creature writhed, and the knight writhed with it. Every deliberate pump rolled her body along with, leaving her as little more than a rag doll. Her body moved when it wanted her to move. It danced when it wanted her to dance."
        "By now, the movement has turned dull. Slow, constant, pounding in an out. Pump. Pump. Pump. Yet, her half-limp body still shuddered without fail."
        "She was like a husk. Her eyes were open, but their contents were empty. She emitted a series of loud moans and groans, stifled by the huge mass in her mouth. Black sludge dripped out of every hole."
        "...There were nearly fifteen people in that room. All were in exactly the same state she was."

    "Keep averting gaze.":
        $ released_fix_rollback()
        $ wulumpLook = False
        scene bg8 with fade
        show rowan necklace shock at midleft with dissolve
        show jezera happy at midright with dissolve
        
"Jezera continued on, entire unphased by the sight in front of her."

je "The commanders who we caught from the little excursion. Well, the commanders who managed to make it through my brother’s lack of thirst for enemy intelligence."
je "We’ve been peeling them out, one by one, long enough to get some answers from them. The Wulump has some...amusing properties. Exposure makes it rather hard to lie, for example."

"An overpowering stench drifted out from the room. Cum and sweat, both smells he recognized. But, the Wulump reeked with a stench like rotting eggs and sulfur. Its scent drifted down the chamber like crashing waves."

if avatar.corruption < 60:
    ro "Will those people be okay?"
    "Jezera sighed."
    je "Yes yes. In a little while. There won’t be too much lasting effect. In all likelihood, once we’re done with them, they’ll wake up with little memory this even happened. Ready to start their new lives working for less incompetent masters."
    
    if alexiaWulump == True:
        je "Quite a handy effect, I may add. Especially if you don’t want little bugs going about talking about what they experienced."
        
ro "I...See…"

if wulumpLook == False:
    "Rowan wondered idly if he’d recognized any of the people in front of him emitting these disgusting inhuman sounds. He didn’t want to check and see."

else:
    "The woman he’d been looking at before shuddered violently. A guttural sound made it from her lips, despite the fleshy appendage filling her mouth."
    "Fluid dripped down her leg, onto the hard stone floor. It was frothing mixture of her own clear juices, and the black viscera that stained everywhere the Wulump subjected itself too."
    "A groaning pathetic orgasm. No doubt far from the first she’d experienced in the past week."

    je "So large, so fast. It must be because we fed it so many."
    
    "The slimy tendrils slid out of the woman’s body, though the binding arms kept her in place. For a moment, Rowan thought it was giving her a break. But, then they plunged back in with a sharp speed. They had just been repositioning."
    "Through it all, the woman’s expression barely changed. The orgasm. The penetration. They barely produced a twitch."
    "There were others throughout the room. Grinding and moaning. Being penetrated and used. Some male, some female. All had the same lifeless manner to them. It used them."

"Jezera suddenly snapped her fingers again. The metal doors slammed back shut, leaving the poor hapless commanders alone again with their jailor. The only sounds that emerged were the odd slithers and moans."

if wulumpLook == True:
    "Rowan turned his attention back to Jezera. The image of what he’d seen still lingered with him."
    scene bg8 with fade
    show rowan necklace shock at midleft with dissolve
    show jezera happy at midright with dissolve

ro "So, what did you find out?"

je "Oh, you’ll love it."
je "These fine folks here having so much fun? These are commanders of the Rastedel Royal Guard."

"Rowan blinked twice. That couldn’t be right..."

ro "We fought the Royal Guard?"

je "Thus the white cloaks. Yes."
je "What we’ve learned is that our dear High Arbitron didn’t have a large army that she could put into the field. The Rosarian army is too scattered. But, she has such fine friends, like Jacques and Duke Werden asking so many hard questions."
je "It seems that she sent out a contingent of the Royal Guard and the City Guard. Our newly talkative friends mentioned that they even moved out in the middle of the night while the city slept."

ro "That means…the reason that Ameraine never contacted us is because she didn’t know they’d even left."

"Jezera formed a dark smirk that stretched from ear to ear. It gave him a chill."

je "Silly boy. You’re missing the most important part."
je "This means that right now, at this very second, there is no army in Rastedel."

"Rowan’s jaw fell slightly. She was right. For the entirety of the last war, the Royal Guard had manned the capital itself to deter an attack."
"There would be no quick way to bring the scattered army back together. All those troops were tied down by the need to defend important outposts and keep the lines of communication and supply flowing."
"A new army could be put into the field, but it would take time and energy to bring up to fighting speed. Prothea could bring an army perhaps, but the holy capital was too far from Rastedel for quick travel."
"Perhaps the Dukes could raise their own banners to defend the city. But, clearly doing so would…"

je "You’re just standing there. What say you?"

ro "I think...I think you’re right. The next move would naturally be to strike now."

je "Exactly. So starting tomorrow you have new orders. No more time for gathering troops. No more time for attacking dinky forts in the middle of nowhere. You will return to Rastedel and link up with Lady Ameraine."
je "...And together, you will do everything in your power to make sure that when the army gets there, they find the city gates open and the palace in flames."
je "You have ten weeks. Am I clear?"

"Rowan bent down on one knee."

if avatar.corruption < 31 and serveChoice != 4:
    show rowan necklace concerned at midleft with dissolve
    "Rastedel had never fallen to a demon lord before. Even in the last war, the demons had been held at bay. Would the city fall because of….him? The prospect was frighteningly real for the first time. His heart beat fast."
    
elif avatar.corruption < 60 or serveChoice == 4:
    "Bringing down Rastedel. Once the very idea might have been unthinkable. But, so much had changed. New perspectives entering into his world. Perhaps, if he did this, the world could be a better place."
    
elif avatar.corruption > 59:
    show rowan necklace happy at midleft with dissolve
    "Rastedel. The den of vipers itself. For so long it had seemed a beacon of stability. No demon had ever taken the city before. Yet, now it stood defenseless." 
    "..And just as defenseless was everyone inside. The flower of Rosarian nobility. Of Rosarian tyranny. Ready to be plucked..."

ro "Your will shall be done. The city will fall. "

"Jezera ushered him back to his feet. He felt her soft hand pat him on the back. They were comrades in arms after all."

je "Such confident words. I look forward to seeing them realized."
je "Now then. Shall we return to the feast? There is much to celebrate today."

if avatar.corruption < 60:
    "Rowan followed along beside her, but didn’t have much to say on the matter. He had a city to bring to its knees. There was much more thinking to do then there was partying."
    
else:
    "Rowan followed beside her."
    ro "Yes. Much to celebrate indeed."

$ postBattleVisit = True

return

