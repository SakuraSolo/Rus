init python:
    
    event('draiths_visitor', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'",), run_count=1, group='alexia_breeding', priority=pr_npc)
    event('drider_exhibitionism', triggers="npc_events", conditions=("get_actor_job('alexia')=='breeding'", 'NTR == True', "castle.buildings['pit'].driders >= 1"), run_count=1, group='alexia_breeding', priority=pr_npc)
    
label draiths_visitor:

scene bg25 with fade

"Working in the breeding pits wasn’t exactly Alexia’s favourite job. The boy, Draith was nice, and she tried her best to be kind to him, for all that he has been subjected to before he arrived at Castle Bloodmeen, but the work was often hard going."
"Cleaning the cages was a long, and arduous task, and the creatures who lived in them were at best not particularly friendly, and at worst downright scary."

if friskyDrider:
    "She had seen what happened when one of the driders got free, and she wasn’t pleased at the prospect of the same thing happen to her."
    
else:
    "If she had met any of the monsters that Draith loved so much out in the world before coming to the castle, she would have run for her life screaming, and now she had to look after them."
    
"Today though, as it had turned out, had been her lucky day. Draith had a number of errands that needed doing around the castle, and had given her the task of doing them instead of her usual chores."
"When she saw the errand list, she understood why; a visit to Cliohna for books needed for research, Cla-Min for supplies, and delivering a report to Jezera. She knew how the young dark elf felt about women, and was no doubt happy for an excuse not to have to see them himself."
"In the end, the tasks had taken her longer than she had expected. The sorceress was busy, and Alexia ended up having to search for the books herself." 
"When she got to the caravan, later than intended, Cla-Min’s supplies were low, which meant waiting for one of her children to return with more stock." 
"Jezera had been the worst though, she had kept her waiting outside her chambers for almost an hour while she amused herself with the help, and when she was finally able to deliver the report, the demoness nonchalantly waved her off, uninterested in Draith’s research."
"By the time Alexia was finally able to head back to the pits, it was well past noon. She contemplated stopping for lunch, but still had the books and supplies, and felt she had best deliver them first, in case the dark elf needed them."
"As she approached, goods in hand, she heard two voices coming from the research area. At first, she could make out neither, but as she got closer, it became clear who were talking." 
"One voice, as she assumed, belonged to Draith. He would be there still working after all. But the other surprised her - it was Andras. Was what he doing down here?"
"She tiptoed closer, wanting to hear what was being said, but without wanting to intrude in case it was inopportune timing. With what she had seen of Andras’ temper, eavesdropping was the more prudent choice." 
"She stopped near the door and placed the items she had been carrying on the floor, carefully. First, the sounds of heavy breathing, and then the demon spoke."

show andras smirk behind bg25
show draith neutral behind bg25

an "You haven’t forgotten your place, have you?"

dra "No master."

"Place? Were they talking about work?"

dra "My place… my place is…"
dra "To do whatever you want me to, whenever you ask me to."
dra "You be… your fuck toy."

"Alexia went bright red as she realized what she had walked in on. She shouldn’t have been surprised really, Draith was so afraid of women it was obvious he’d prefer the company of men, and Andras was practically a walking erection." 
"She should leave now. This was obviously a private moment, and she didn’t really want to risk getting caught peeping, however…"

if all_actors['alexia'].corruption > 50:
    "She felt her loins grow hot at the thought of what was about to happen. The dark elf was a cutie, and the thought of the larger, muscular demon pounding his little butthole made her wet."
    if all_actors['alexia'].flags['andras_influence'] > 5:
        "And as wrong as it was to feel that way, she felt jealous of Draith."
    else:
        pass
else:
    pass
    
menu:
    "Peek.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +3)
        jump andrasDraithBPSex
        
    "Leave":
        $ released_fix_rollback()
        "No, this was a private moment, and she had no idea what would happen if the demon was to spy her watching, or the type of punishment he would inflict." 
        "Bending over, she picked up the books and supplies from where she had left them. She would return after eating to deliver them, when they had, hopefully, finished."
        return

label andrasDraithBPSex:

#CG1
scene black with fade
show andras smirk behind black
show draith neutral behind black

"While she had been contemplating what to do in the hallway, Andras had wasted no time putting the dark elf to work. When she peeked around the corner, she saw Draith was now on his knees behind the demon."
"She saw his grey-white hands on the demon’s ass, a strange contrast against his red skin. He spread the cheeks, and leaned forward to bury his face in it."

an "Uhhh.. That’s it, lick it slave."

"Alexia watched as the smaller elf began to tongue her captor’s asshole, licking up and down, and round in circles. It was obvious to her he had done this before, and was clearly enjoying himself. Andras didn’t seem to mind it either."

an "You’ve gotten good at this, haven’t you, my little ass slut?"

"At the use of the term, “ass slut”, the dark elf’s face reddened, not with shame, but with pride. He was getting off on the degradation, perhaps the result of the years he had spent as a slave to the females of his species. "

"He took a moment to move his face back, giving him room to respond."

dra "Yes master. I love the taste of your ass master."

"He really did. He went back to licking it as soon as the words left his mouth, the demon smirked."

an "Why don’t you prove it?"

"Draith didn’t need any more encouragement, he buried his tongue into his master’s hole as far  as it would go. Andras let out and groan, followed by a chuckle, as the elf swirled his tongue as best he could. Alexia wondered how he could breathe."
"As his slave jerked his head back and forth, stabbing his tongue into his butthole, Andras reached down and grabbed his engorged cock, moving his hand up and down in lazy strokes."

an "That’s a good start, slut. Now, assume the position."
     
#CG2
scene black with fade
show andras smirk behind black
show draith neutral behind black

"Draith got up from the floor, and walked over to the desk where he did his research. He pulled down his pants, and then leaned over to offer himself to his master. Andras walked up behind him, and placed a large hand on the elf’s posterior."

an "Now, do you think that performance deserves a reward? Hmmm?"
 
dra "No master."

an "No, what does it deserve then?"

dra "I think I…"

an "Yes?"

dra "I deserve to be punished!"

"The demon let out a chuckle."

an "I think so too, three should do it, don’t you think?"

dra "You are too kind, master."

"Andras smirked at his response."

an "You are right, of course, we’ll make it five."

"*THWACK*"

"His large hard came down in a flash, so fast that Alexia barely saw it. The elf let out a squeal as it met flesh, leaving a large red welt in its wake. It looked painful, but it was clear Draith was getting off on it."

an "That’s one."

"*THWACK*"

"Again the hand came down as the demon spanked him, this time leaving a welt on the other cheek this time."

dra "Unnnn……"

an "Two."

"*THWACK*"

"Once more, the hand met flesh with hard contact, making the cheek even redder. The dark elf shuddered and moaned in response."

an "Three."

dra "Please master…"
dra "No more…"

"This must have been part of the act, the woman surmised, he was clearly enjoying being manhandled by Andras."

an "Be quiet you wimp, and take it like a man."

"*THWACK*"

"The fourth spank fell, both cheeks were practically glowing now. Draith had bitten down on his lip to try and stop himself from crying out, but it hadn’t helped. He had a dazed look on his face, and his cock was twitching with arousal."

an "Four. Just one more."

dra "No no no…"

"*THWACK*"

"The final spank was so hard, the sound reverberated around the room. Draith collapsed on the table in extacy."

dra "Fuckfuckfuckfuck…"

"Andras gentled caressed his small ass with his hand. He then ruffled his hair in an uncharacteristic display of gentleness."

an "Good boy."

scene cg256 with fade
show andras smirk behind cg256 
show draith neutral behind cg256 

"Without a word, Andras flipped his smaller partner over so that his back was on the table, and spread his legs apart. The elf didn’t object, but then, even if he wanted to, he was hardly in a state to do so."
"Andras spit on his hand, and applied a copious amount of it to his dick, before fingering Draith’s asshole to lube it up for good measure. Reaching down he grabbed his cock, and pressed it against his slave’s ass, forcing it inside."

dra "Unnnf!"

"Without waiting on ceremony, the demon began to move his hips back and forth, deep fucking the elf. All the foreplay must have gotten him hot, and he was in no mood to play around any further."
"By this point, Draith was reduced  to a moaning mess. To add to it, Andras reached down and grabbed his cock, and stroked it with the same rhythm as the movement of his hips."
"The sound of thwack thwack thwack filled the room as flesh met flesh, each time the demon bottomed out, again and again. It was joined by the cries of the young elf, which grew louder and louder."

if all_actors['alexia'].corruption > 50 and NTR == True:
    "As if almost by instinct, Alexia slid a hand down into her panties, and began to massage her clit. As she watched the two handsome creatures before her, fucking like animals, she wished one of them was inside her too."
    if all_actors['alexia'].corruption > 75 and NTR == True:
        "Or both of them, she had more than one hole after all, and she knew she would feel so full..."
    else:
        pass
    if all_actors['alexia'].flags['andras_influence'] > 5:
        "She couldn’t stop herself from staring at the demon, so strong and so powerful. She knew it was wrong, and she tried to push the thought away, but all she could imagine was him holding her down, and having his way with her. A wave of orgasmic pleasure shot through her body."
    else:
        pass
else:
    pass

"It didn’t take long before they were both approaching climax. Draith came first, as Andras jerked him hard and fast, spraying cum into the air like a fountain." 

show cg256 with sshake
show cg256 with sshake
show cg257 with flash
pause 3

"With a smirk, the demon forced his cock into the dark elf’s asshole until he was balls deep, and then let out a satisfied grunt as he spunked inside him. Draith smiled as he felt his insides grow warm from his master’s creamy load."

show cg257 with sshake
show cg257 with sshake
show cg258 with flash
pause 3

if all_actors['alexia'].corruption > 50:
    "Alexia came last, greedily fingering her hole as she watched the two males cum. As she climaxed, she had to cover her mouth to avoid being discovered, before sliding to the floor in post orgasmic bliss."
else:
    pass
    
"With the show over, and both of them currently distracted, Alexia saw this as her best chance to slip away. She picked the goods, and the books, up from the floor, and carefully tiptoed away down the hall."
"She would return later to deliver them to the dark elf, and never mentioned what she had seen to anybody."

return

#############################################################################################################################################    
    
label drider_exhibitionism:

scene bg25 with fade

if castle.researches['monster_taming'].completed:
    show alexia breeding happy at midleft with dissolve
    show draith happy at midright with dissolve
    dra "Isn’t he simply adorable?"
    al "Not exactly the word I’d use."
    show draith neutral at midright with dissolve
    dra "Hmm… I guess that much is true."
    show draith happy at midright with dissolve
    dra "“Magnificent” is much more fitting!"
    "Alexia smiled to herself. Draith’s enthusiasm was infectious, even though the object of his adoration was slightly unorthodox."
    "Said object – a large drider they recently finished training – continued to pace restlessly in his cell. They’ve been doing great progress on them, and it was surprising to see these wild beasts act so… Servile."
    
else:
    show alexia breeding concerned at midleft with dissolve
    show draith happy at midright with dissolve
    dra "Isn’t he simply adorable?"
    al "Not exactly the word I’d use."
    show draith neutral at midright with dissolve
    dra "Hmm… I guess that much is true."
    show draith happy at midright with dissolve
    dra "“Magnificent” is much more fitting!"
    "With some concern, Alexia eyed Draith’s object of adoration – a large drider they recently finished training. The beast paced the cell restlessly, and Alexia suspected it wasn’t striking against the bars only because his master was here."
    "They had been making great progress with them, and Alexia had to admire Draith’s skill, but she just couldn’t share his enthusiasm. She couldn’t help but think they’ve been playing with fire here."

show alexia breeding neutral at midleft with dissolve

al "Do you think he’s fit for battle?"

show andras displeased behind bg25

an "He better be."

hide andras
show andras displeased at edgeright with moveinright
show draith neutral at edgeleft with moveoutleft
show alexia breeding shocked at midleft with dissolve

dra "M-Master?"

show alexia breeding concerned at midleft with dissolve
show draith happy at edgeleft with dissolve

dra "What a pleasant surprise! Have you come to inspect the pens?"

an "Yes. I was hoping to make use of our driders next month."

show andras displeased at midright with moveinright

an "So I believe you can imagine my disappointment when I saw the result of your “hard work”."

if castle.buildings['pit'].driders == 1:
    an "I was promised an army of driders, Draith! Is this one, measly bug all you have to show to me?!"
    
elif castle.buildings['pit'].driders == 2 or castle.buildings['pit'].driders == 3:
    an "I was promised an army of driders, Drath! Is a handful of bugs all you can show me?! What am I supposed to conquer with them, a cabbage farm?!"
    
else:
    an "I was promised an army of driders! And all you have here is a mob of half-feral bugs!"
    
dra "Technically they’re arach- gack!"

#draith terrified
show draith neutral at center with moveinleft
show alexia breeding shocked at edgeleft with moveoutleft

"Andras seized the elf by the throat, picking hip with ease, and he weighed nothing to him. And mattered nothing to him."

an "I found you wandering the tunnels like a lost dog, AND THIS IS HOW YOU REPAY ME?!"

show alexia breeding concerned at edgeleft with dissolve

al "Andras, please-"

show andras displeased at midleft with moveoutleft

an "Do not interrupt me woman."

"His low growl was enough to make her shut up, and she shriveled under his fury. His lone arm still choked the elf – Draith put his own hands on it, but made no attempts to break his hold."
"If there was anything both of them had learned already, it was that resisting Andras usually only made the situation worse."
"Even if his initial intent was to kill you."

an "Pathetic."

hide draith with dissolve

"He threw the pen master to the ground – violently. Alexia winced as she heard something crack and prayed it wasn’t anything important."

show draith neutral behind bg25

dra "*cough* M-mas…"

"Draith tried to apologize, but Andras paid no attention to him. He turned to Alexia and the housewife backed away immediately, instinctively. He wouldn’t hurt her, right?"

if alexiaAndrasSex > 2:
    "She’s been obedient, spreading her legs whenever he asked her to. He wouldn’t hurt her for a silly little thing like this, right?"
    "Right?"

else:
    "… Right?"
    
an "This is unacceptable. What are you two even doing here all week? Is this whole project just a massive money sink?"

dra "M-"

an "Shut up."

"Draith whimpered, and did just that."

"The demon turned away from both of them, and peered into the cell. The drider watched the situation unfold in silence, having retreated deep into the corner of his room."
"The beast recognized the presence of an apex predator, but with escape impossible, it could only try to put some distance between himself and red demon." 

an "…But I guess I can’t really blame you."

if castle.buildings['pit'].driders < 4:
    an "It’s not your fault you have no eggs to work with."
    
else:
    an "It’s not your fault you receive sup par eggs or that you don’t have enough staff to train everyone.    "

an "Rowan was supposed to handle this, but I guess I expected too much of him."

if all_actors['andras'].favors > 2:
    an "And to think he was starting to show promise…"
    an "..."

else:
    pass
    
an "Guess I’ll have to discipline him."

show andras displeased at edgeright with moveoutright

"Without another word, he headed for the exit. Alexia felt her heart sink. The threat hanged in the air, spoken so casually, yet carrying terrifying undertones."
"Rowan was not in the castle, but Andras was not one to calm down with time. His fury would only grow, and her husband would meet it head on the moment he steps from the portal."

show andras happy at edgeright with dissolve

al "Wait!"

show andras displeased at edgeright with dissolve

"Miraculously, the demon did just that. He turned his head around, eyes narrowed on her."

show alexia breeding neutral at edgeleft with dissolve

if all_actors['alexia'].relation > 30:
    "Even if things weren’t going so well between her and Rowan, she couldn’t just let Andras hurt him for no reason."
    "Despite everything, a part of her still loved him. She was still his wife – she had to find a way to protect him."

else:
    "She couldn’t just let Andras hurt her husband for no reasons. She was his wife – she had to find a way to protect him."

al "We might not have the army you wanted, but-"

show alexia breeding happy at edgeleft with dissolve

if castle.buildings['pit'].driders == 1:
    al "But we’ve been making great progress training them!"
    
else:
    al "But the ones we have are all well trained!"
    
al "Just look at this one!"

show andras displeased at center with moveinright

"She pointed to the cell. The drider still observed them all without as much as a peep, silent and alert."

if all_actors['alexia'].corruption < 30:
    hide andras with dissolve
    show alexia breeding concerned at edgeleft with dissolve
    "As Andras approached the cell, Alexia took a quick glance to where the demon dropped the pens master."
    hide draith
    show draith neutral at midright with dissolve
    "Draith didn’t look seriously injured, but did not dare to raise up. Alexia offered him a reassuring smile, mouthing “I’ll take care of it”. She then turned back to Andras before the demon noticed she was looking away."
    hide draith with dissolve
    show andras displeased at center with dissolve
    show alexia breeding happy at edgeleft with dissolve
    
else:
    pass
    
al "Strong and vicious in battle, but tame and obedient in the presence of his trainers!"

if castle.buildings['pit'].driders < 4:
    al "Rowan has been delivering some high-quality eggs, so the driders we have all show great potential!"
    
else:
    al "We might be a little bit understaffed, but the people Rowan assigned to us all are excellent trainers!  These driders will surely perform in battle, Master Andras!"
    
"It was straight up lies, but she had to say something. Her mouth was simply running faster than her mind could keep up. She only hoped Andras would buy it."

if castle.buildings['pit'].driders == 1:
    al "We just need some time to breed this one, and-"
    
else:
    al "We just need some time to breed the more promising ones, and-"

show alexia breeding shocked at edgeleft with dissolve

an "Hrm. Breed, you say?"

"She froze. This did not bode well."

show alexia breeding happy at edgeleft with dissolve

al "… Yes?"

show andras happy at midleft with moveoutleft

an "You had plenty of time to breed them before, didn’t you?"

"He placed his arm on her shoulder. She did her best not to shiver, and failed miserably."

an "I’d like to see some proof of your claims."
an "Strip."

show alexia breeding shocked at edgeleft with dissolve

al "What?"

show andras displeased at midleft with dissolve

an "I said strip."
an "You’re going to prove to me how well trained he is."

show andras smirk at midleft with dissolve

an "So, you’re going to strip. Then you’ll walk in there. Slowly."
an "You’re going to tell the drider to stay put."
an "Then, you’re going to spread your legs, and start playing with your pussy."
an "If, by the time you come, the drider does not jump you, then I’ll concede that maybe, just maybe, Rowan and Draith know what the fuck they’re doing here.  "

al "… You can’t be serious."

show andras displeased at midleft with dissolve

"He glared at her, and she stowed further complains. He was very much serious."

show alexia breeding neutral at edgeleft with dissolve

"Her eyes ventured to the drider. In the heat of the moment, she made some very bold statements, on some very shaky grounds. She couldn’t back down from them now, and she couldn’t expect the semi-sentient beast to play ball with her. "
"The drider still kept his distance, but even in the half dark of his cell, she could still see his large body looming menacingly behind the cell bars."

if alexia_ice_shard == True:
    "Was she really going to expose herself to this beast? With nothing to defend herself, except for a low-level magic bolt and faith in Draith’s unfinished training?"
    
else:
    "Was she really going to expose herself to this beast? With nothing to defend her, expect for Draith’s unfinished training?"
    
if all_actors['alexia'].corruption > 30:
    "It was reckless. It was foolish. It was downright insane."
    show alexia breeding aroused at edgeleft with dissolve
    "But Solansia save her, as much as she wanted to deny it, something deep inside of her was thrilled at the perspective of following through with this, thrilled at the prospect of exposing herself like that." 
    "It was wrong. But as much as she tried to suppress her feeling, they refused to leave her."
    
else:
    show alexia breeding concerned at edgeleft with dissolve
    "It was reckless, it was idiotic, and she shivered in fear at the thought of doing so."
    
show alexia breeding neutral at edgeleft with dissolve

"Besides her, Andras was waiting for her decision. He didn’t urge her on, but his mere presence was enough to make her sweat."

$ driderProtectAsk = False

label driderMenu:

menu:
    "Agree to his demands.":
        $ released_fix_rollback()
        "There was no use resisting. She’ll just make the situation worse if she tries to. It was best to just go along with his demands before he adds something even more unreasonable to them."
        if all_actors['alexia'].corruption > 30:
            show alexia breeding aroused at edgeleft with dissolve
        else:
            show alexia breeding concerned at edgeleft with dissolve
        jump driderHarrassSex
        
    "Ask Andras if he’ll protect her if something goes wrong." if driderProtectAsk == False:
        $ released_fix_rollback()
        show alexia breeding concerned at edgeleft with dissolve
        al "Um… Theoretically asking…"
        al "If the drider proves to be more rebellious than we previously anticipated… Will you make sure he doesn’t hurt me?"
        "Andras gave her a hard look, then burst into a loud, mocking laugh."
        show andras happy at midleft with dissolve
        an "Ahahaha, not so confident in your husband’s choices after all, are you?!"
        "He put his arm around her, and hugged her close to his chest. She blushed, feeling his rock hard muscles and heavy musk of his sweat, so characteristic to the demon."
        an "Very well. No harm will come to you. I am not like Rowan. I’d never allow anyone to touch you without my permission."        
        $ driderProtectAsk = True
        $ change_actor_num_flag('alexia', 'andras_influence', 1)
        jump driderMenu
        
        
    "Try to weasel yourself out of this.":
        $ released_fix_rollback()
        if driderProtectAsk == True:
            "Hearing her husband’s name, she felt a surge of guilt overtake her. She pushed herself away from the demon, and stammering, tried to think of an excuse to cut things short before they spiral out of control."
        else:
            pass
        show alexia breeding shocked at edgeleft with dissolve
        show andras displeased at midleft with dissolve
        al "This a little sudden don’t you think?"
        al "The drider is trained, but we haven’t fed him today, and that might make him a bit uppity-"
        an "Alexia."
        an "As much as it amuses me seeing you backtrack from your attempt of covering for Rowan’s mistakes, I am less pleased by the fact you think you can play me and get away with it."
        an "Need I remind you of your place here? Then allow me to rephrase my earlier demand."
        an "You will strip."
        an "You will walk into the cell."
        an "And you will fuck your slut pussy until you cum."
        an "This is an order."
        show alexia breeding neutral at edgeleft with dissolve
        al "…"
        if alexiaWulump == True:
            "Andras already proved he wouldn’t shy away from anything when Alexia got out of the line. And while refusing him here likely wouldn’t be enough to toss her into the dungeons again, she knew she couldn’t keep doing so."
        else:
            "She didn’t think he’d do anything to her from denying him here, but… He wouldn’t tolerate constant disobedience either."
        "Sooner or later, she will suffer the consequences from her continuous resistance."
        
        menu:
            "Submit to his will.":
                $ released_fix_rollback()            
                "Slanting her shoulders, she resigned herself to her fate. What else could she do? He was the Lord of the castle, while she was his prisoner."
                if all_actors['alexia'].corruption > 30:
                    show alexia breeding aroused at midleft with dissolve
                    "Besides… It’s not like she was wholly opposed to the idea…"
                else:
                    pass
                jump driderHarrassSex
                
            "Deny his request.":
                al "Andras, I-"
                show alexia breeding concerned at edgeleft with dissolve
                al "I’m sorry, I shouldn’t have made all these claims about the driders."
                if all_actors['alexia'].relation > 30:
                    al "Please have mercy on my husband-"
                else:
                    al "Please have mercy on me-"
                an "Enough. This is pathetic. I don’t have time for this."
                show andras displeased at edgeright with moveoutright
                an "I don’t have time for this."
                "Andras snapped angrily, stopping her midway, no longer paying attention to her excuses. He walked over to Draith, and Alexia fully expected him to kick the dark elf or punch him or something equally violent."
                an "Draith."
                "Instead, he knelt beside him and grabbed him by the chin, forcing him to look him in the eyes."
                show alexia breeding shocked at edgeleft with dissolve
                an "Do not make me hurt you again."
                an "Have I made myself clear?"
                show draith neutral behind bg25
                dra "Y-yes Master…"
                show alexia breeding neutral at edgeleft with dissolve
                an "Good."
                hide andras with moveoutright
                "He left the room as suddenly as he arrived, leaving behind an oppressive atmosphere."
                hide draith
                show draith neutral at midright with dissolve
                show alexia breeding concerned at edgeleft with dissolve
                al "Draith… "
                dra "… Let’s get back to work."
                al "Right."
                scene black with fade
                "Neither of them wanted to talk about what transpired. They returned to their duties, doing their best to avoid one another for the remainder of the week."
                $ andrasPunishmentCounter += 1
                return


label driderHarrassSex:

al "Alright… I’ll do it."

show andras smirk at midleft with dissolve

an "Good… Good."

show andras displeased at midleft with dissolve

an "Get on with it then, I don’t have all day."

hide draith
show draith neutral at edgeright with dissolve

"With trembling hands, she started to take off the heavy tunic she wore in the pens, and quickly moved on to everything else."

show alexia necklace naked concerned at edgeleft with dissolve

if all_actors['alexia'].corruption < 30:
    al "(Let’s just be done with this…)"
else:
    pass
    
show alexia necklace naked concerned at center with moveinleft
show andras displeased at edgeleft with moveoutleft
show draith neutral at midright with moveinright

"A moment later, she stood naked in front of the cell, Draith by her side with the keys in his hand. He kept rubbing his throat, the red imprinting of Andras hand clearly visible on his dark skin."

if all_actors['alexia'].corruption < 30:
    al "Are you okay Draith?"
    "He nodded solemnly, but didn’t speak up. She could only imagine how much it hurt."
else:
    "She couldn’t help but notice there was a soft blush to his cheeks. Did he like it when Andras treated him roughly?" 
    "Part of her wanted to feel his pants to check it, but this was not the right time."

"He opened the door for her. She took a deep breath, stepped inside."

#cg 1
scene cg263 with fade
show alexia necklace naked concerned behind cg263 
show andras smirk behind cg263 
pause 3

"She never was much of a fighter, but now, she felt more vulnerable than ever. The stone beneath her feet was hard and cold, and the cell had an unpleasant smell to it Alexia tried very hard not to think about."
"And in front of her, the drider watched her approach, slowly raising up to meet his prey."
"Protected by the orcs and separated by metal bars, Alexia sometimes forgot what a dangerous foe they were playing with here. The Drider towered over her easily, his eight black legs supporting a large body that could crush her with ease."
"Four pairs of eyes hid intelligence that rivaled human, while the chitin armor on his lower torso covered something that often surpassed its human equivalent."
"Alexia saw it break many slaves. And if their training was insufficient, she was next on that list."

if all_actors['alexia'].corruption > 30:
    "He would plunge his massive cock into her, ravishing her with abandon. She would scream, she would shout, but would Andras and Draith react? Would they save her, or would they let her be ravished in front of their eyes?"
    "… She only just entered the cell, and already she felt her pussy flare up."
    
else:
    pass
    
"The drider waited, uncertain of the situation. He glanced towards his dark elf master, expecting to see him follow Alexia into the cell, whip in hand."
"But Draith only watched the situation unfold, with a pained expression on his face. He would not intervene, that much was clear to the beast. And this only meant one thing to the drider."
"He smiled hungrily, and took a step forward." 

al "Stay!"

"The drider almost recoiled from the command. He was trained to obey the staff, no matter the circumstances. Draith made sure of it."

if all_actors['alexia'].corruption > 30:
    "And a small, twisted part of Alexia almost resented him for it. Such a glorious beast… Shackled and broken."
    "What a shame it was!"

else:
    "And again, Alexia prayed the training stuck. Overwhelmed with fear, she barely got the command out in time."
    
"She could almost see the invisible tethers of Draith's conditioning bind the drider, hold him in his place. How durable were they?"
"She was about to put them to the test."
    
if all_actors['alexia'].corruption > 30:
    "Giggly with anticipation, she spread her legs slightly. She watched the beast, as her hand slowly slid downwards."
    al "A-ah!"
    "She could not contain her voice. It was twisted, she knew that."
    "But with every passing moment, she cared less for it."

else:
    "Shivering in fear, she spread her legs slightly. She watched the beast while her hand ventured south, fully expecting the drider to pounce at her at any moment."
    
al "Stay."

if all_actors['alexia'].corruption > 30:
    scene cg264 with fade
    show alexia necklace naked aroused behind cg264
    show andras smirk behind cg264
    pause 3
    "It was amazing, watching this massive beast just… Stare, as she spread her pussy lips right in front of him. He could watch, but he could not touch. They lived to breed, and this wonderful soaking pussy was being denied to him."
    al "Stay and watch."
    al "..."
    al "Watch me fuck myself with my fingers."
    "She couldn’t contain her voice, the rush from taunting the drider banishing all reason."
    al "You can watch me, but you can’t fuck me."
    al "Watch my – Mmmh!- fingers!"
    al "Watch me put them inside of me!"
    "She felt a jolt of pleasure shoot up her spine, as she easily thrusted her hand inside of her. The drider’s erect cock swayed in front of her eyes, the sight of it tearing her apart-"
    "What was better? Taunting him, or laying on her back and letting him fuck her?"
    al "Ha… ha-ha!"
    "She had- she had to masturbate, but the more she did, the more remorse she felt Andras didn’t order her to just go and fuck the beast. She wanted- she wanted something bigger than this! Something bigger than her fingers!"
    an "Ahahahaha, panting like a slut already? You really are shameless!"
    "She heard Andras jeer, and could not find it in herself to refute his words. Here she was, naked, fucking herself with her hand in front of a massive drider dick, and all she could think about was how it was not enough for her."
    an "Tell him to watch you! Tell him to stare at your cunt!"
    al "W-watch meeeee fuck my cunt!"
    an "Tell him to stroke himself!"
    al "U-use your hand while yo-u watch!"
    an "Tell him he’s not worthy of breeding with you."
    al "You c-can’t fuu-uck me!"
    al "You caaa-n’t spray your cum inside of m-me!"
    an "Tell him your pussy is for me only."
    
    menu:
        "Obey.":
            $ released_fix_rollback()  
            $ change_actor_num_flag('alexia', 'andras_influence', 3)
            al "My pussy is for M-master Andras aloooone-!"
            
        "Don’t.":
            $ released_fix_rollback()
            "Despite the overwhelming lust, the words froze in her mouth, as the image of her husband flashed before her eyes."
            "She couldn’t do it. She couldn’t betray him like that."
            al "Ah-ah, ah!"
            "Instead, she redoubled her efforts. She had to cum."
            "She had to cum before Andras makes her say something she didn’t want to."
            
    
    if castle.researches['monster_taming'].completed:
        jump alexiaDriderCum
        
    else:
        jump andrasDriderIntervention
            
else:
    scene cg264 with fade
    show alexia necklace naked aroused behind cg264
    show andras smirk behind cg264
    show rowan necklace happy behind cg264
    pause 3
    "She slowly traced her fingers across her slit, but felt no arousal from doing so. What madwoman would? With a half-feral beast waiting to rape her, and with her captor watching her every move?"
    "But Andras wouldn’t let her go unless she orgasmed. Bastard…"
    "Too afraid to take her eyes off the drider, she imagined her husband behind her, and herself leaning her back against his muscular chest."
    "She imagined his arms embrace her, as he leaned in to whisper reassuringly in her ear:"
    ro "Everything will be fine. Just think about me."
    "And she did. Ignoring the drider in front of her, and the demon behind her, and the cold stone beneath her, and the horrid odor around her, she thought of her husband."
    "She thought of his kind smile, of his tender touch. She thought of the warmth of his body, and his gentle voice, firming guiding her movements."
    ro "Everything will be fine. Put your hand between your legs, and think about me."
    al "A-ah…"
    "She slid the first finger in, her eyes never leaving the drider."
    al "Ah-ah!"
    "She thought of the summer festival, three years into their marriage. She promised the Cavins she would help with the pies. Rowan pretended to go patrol around the village, only to sneak in into the bakery when no one was looking."
    "She recalled how he grabbed her from behind, shushing her. She tried to protest quietly, telling him it wasn’t proper, but he paid her no heed."
    "He reached under her skirt, and thrust his finger into her pussy, just as she did now."
    al "Aah! Mm-ah! S-stay!"
    "She saw the drider tense, and again she ordered him to stay. His erect tool swayed in front of her eyes, ready to plunge into her hole."
    "Insane. This was all insane. But she had to keep going."
    "She kept thrusting, with every moment with greater urgency. She tried to think of Rowan, but it was difficult to recall the fantasy again, with the cock reminding her of the danger she was in."
    al "(Why do I have to suffer through this…)"
    "She tried to think what Rowan would say, what comforting words he would offer-"
    an "Looking real nice, slut!"
    al "Nngh?!"
    an "Look how hard you got his dick! He looks like he’ll pounce you at any second!"
    al "S-stop it Andras!"
    "He laughed in response, as always not caring in the slightest for her concerns. No matter. She was getting close. She just had to ignore everyone and think about her-"
    an "It’s actually dripping with pre-cum! Driders must really love you Alexia!"
    al "(Ignore him, don’t-)"
    an "Spread your legs! Keep fucking your pussy!"
    al "Sto-o-op!"
    an "Keep fucking it!"
    al "D-damn it Aaa-Andras!"
    al "(Shut up, shut up, shut up!)"
    an "Keep fucking it right in front of his eyes until you cum, you slut!"
    al "I’m n-nngh-!"
    an "I said cum!"
    if castle.researches['monster_taming'].completed:
        jump alexiaDriderCum
        
    else:
        jump andrasDriderIntervention


label alexiaDriderCum:

al "A-ah, aaah, AAAH!"

"She closed her eyes, threw her head back, and allowed pleasure to overtake her."

scene black with fade

"..."

show alexia necklace naked aroused behind black

al "Nn… Uh?"

scene bg25 with fade
show alexia necklace naked concerned at center with dissolve

"With some fear, she opened her eyes, and looked up at the drider. He still glared at her furiously, cock painfully erect, but he dared not to step forward."
"She heard a slow clap from behind, and saw Andras enter the cell."

show andras smirk at midleft with moveinleft

an "Well done, well done."

"His gaze traveled across her body, but she was too tired to cover herself."

an "They really are well trained."
an "I’ll give you and Rowan a pass this time. Keep up the good work."

al "… Yes, Master Andras."

"She did it. She managed to protect her husband."
"But as she stood there, Andras eyeing her naked body with lust in his eyes, somehow, it did not feel like victory..."

$ change_actor_num_flag('alexia', 'andras_influence', 3)
$ change_corruption_actor('alexia', +3)
return

label andrasDriderIntervention:

scene black with fade

"Suddenly, all hell broke loose."

show black with sshake

"So engrossed she was in the situation, she didn’t notice the drider leap forward, screeching in frustration. She fell back, shouting-"

show black with redflash

"She felt a large arm embrace her, and a crimson energy flooded the cell. "

show black with sshake
show black with redflash

"She watched, as a large, red pentagram fell on the drider, crushing it into the ground, turning him into a red pulp right in front of her eyes. He kept screeching, until his head literally exploded from the pressure, spraying the cell red."

show andras displeased behind black

an "Nobody fucks Alexia without my permission."

scene bg25 with fade
show andras displeased at midleft with dissolve
show alexia necklace naked concerned at center with dissolve


"She looked up, eyes blurry, and saw it was Andras embracing her from behind. His left arm was raised up, glowing menacingly with terrifying power."

if alexia_ice_shard == True:
    "He was younger than her, and she almost never saw him train the library… Just how much innate power did he have at his disposal?"
else:
    pass
    
an "So much for it being well trained."

al "..."

"She couldn’t say anything. She just stayed in his arms, trying to stop her heart from jumping out of her chest."

an "But I guess I’ll let it pass. This one time."

"He broke the spell, and gently ran his fingers over her hair. Alexia did her best to ignore the stench of blood that now filled the room."

an "You did well Alexia. Take the rest of the week off."

"She nodded solemnly. She did it. She protected her husband."

scene black with fade

"Then why was she hugging another man?"

#lose 1 drider
$ change_actor_num_flag('alexia', 'andras_influence', 3)
$ change_corruption_actor('alexia', +3)
return