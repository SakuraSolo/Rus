init python:
    
    event('andras_humiliated_rowan', triggers="week_end", conditions=('week >=30', 'castle.villages > 2',), group='ruler_event', run_count=1, priority=pr_ruler)
    #rastedel not complete TODO
    event('jezera_slave_reward', triggers="week_end", conditions=('week >=30', 'castle.villages > 2',), group='ruler_event', run_count=1, priority=pr_ruler)
    





label andras_humiliated_rowan:

#Andras humiliates Rowan

scene bg14 with fade
show rowan necklace neutral at edgeleft with dissolve
show andras happy at midright with dissolve

ro "Andras, you wanted to see me?"

an "Rowan! Finally. Yes, I did send for you."

"As per the twin's request, Rowan met the red demon near the front door of the dungeons – a place the hero wasn’t particularly fond of. But as always, his personal sentiment hardly mattered when the twins were concerned."

show andras smirk at midleft with moveinleft
show rowan necklace shock at edgeleft with dissolve

an "Come, let me show you something."

hide andras with moveoutright
hide rowan with moveoutright

"He grabbed him under his arm, and almost dragged him into the dungeon."

scene bg8 with fade
show rowan necklace concerned at midleft with dissolve
show andras happy at center with dissolve

"Upon seeing the small cells around them, Rowan was forced to fight down a feeling of unease. Not long ago, he was certain his story would come to an end in one of them. And now…"

an "Behold, the fruits of your labour!"

"Now the cells were full of people just like him. Full of common folk of Rosaria, who Rowan captured at the behest of the demons he now served."

show rowan necklace neutral at midleft with dissolve

an "Isn’t this a beautiful sight?"

if serveChoice != 4:
    show rowan necklace angry at midleft with dissolve
    ro "(Fucking bastard… He just has to gloat, doesn’t he…)"
    show rowan necklace neutral at midleft with dissolve
    "Rowan put on his best poker face, and with an air of absolute indifference, told Andras what he wanted to hear."
    
ro "I am glad you find my work acceptable, Lord Andras."
ro "Do you require my assistance with something, or did you merely desire my company as you inspect the stocks?"

an "Always so serious, Rowan. Lighten up a little! Come, let’s talk to these poor sods."

"Andras flashed him a wide grin. Always the sadist… Rowan suppressed a sigh, and followed along as the demon approached the cells."

show andras happy at edgeright with moveoutright
show rowan necklace neutral at center with moveoutright

"Inside, the poor people of Rosaria scurried away from the metal bars, instinctively realizing Andras was not someone to be messed with. Or did the demon already made himself known to some of the people here? Not unlikely."
"A few of them watched them approach – the few who were either too stupid or too proud to hide and avoid attracting attention. Most focused on Andras, but one… One laid his eyes on the man behind the demon, his eyes widening in recognition."

show rowan necklace shock at center with dissolve

pris "… Rowan?"

show rowan necklace neutral at center with dissolve
show andras smirk at edgeright with dissolve

pris "Rowan Blackwell is that you?"

"Rowan did not answer. From the corner of his eyes, he saw Andras adopt his usual shit-eating grin."

pris "Oh bless the heavens our prayers have been answered! Please, Rowan, you must help us! You have to do something!"

show rowan necklace concerned at center with dissolve

pris "They’re beating us! And-and I d-don’t know what that one blonde elf wants to do, but she’s been coming down here, talking about “running experiments”!"

show rowan necklace neutral at center with dissolve

pris "Please! You have to do something!"
pris "… Rowan?"

"Rowan turned his head away. The people here – they found themselves in this position because he ordered their villages raided and ransacked. There really wasn’t anything he could do for them now."

if avatar.corruption < 50:
    "He felt his chest tighten. How far has he fallen… Enslaving people on behalf of the children of Karnas. So much for the proud hero of Rosaria…"
else:
    "He thought he would feel worse about being responsible for ruining their lives, but somehow, all he did was feel… Emptiness."
    "People lost their lives and end up in shackles all the time. What was the guarantee the people here wouldn’t fall pretty to a bunch of marauding orcs later on? Why should he feel guilty about his action…?"

opris "… He’s not going to do anything."

"Another voice followed, bringing Rowan out of his thoughts. This time, it came from a curled up, beaten man, hiding away in the depths of a nearby cell. He was young. Strong. No doubt, he fought the orcs when they fell upon the village. It was a miracle he was not killed."

opris "He’s with them. We were played from the start."

pris "What? No! That’s-"

show rowan necklace concerned at center with dissolve

pris "That can’t be true!"
pris "Tell us it’s not true! Rowan!"

show rowan necklace neutral at center with dissolve

"The silence stretched, and the man’s face slowly twisted into absolute despair as realization set in. Nobody dared to speak another word."
"Except for Andras, who broke into a healthy, loud laugh."

show andras smirk at midright with moveinright

an "AHAHAHAHA! That’s right, you were betrayed! Betrayed by the man you thought your savior!"

show andras smirk at center with moveinright
show rowan necklace angry at midright with moveoutright

"The demon shoved Rowan from behind, right at the cell doors. Rowan threw him a hostile look, but Andras paid no attention to it."

an "Look at him! The hero of Rosaria. Now my bitch!"
an "Enslaving and murdering people as I order him!"
an "Isn’t this wonderful?!"


menu:
    "Say nothing.":
        $ released_fix_rollback()
        jump allowAndrasHumiliation
        
    "Don't let him push you around like this." if serveChoice != 4:
        $ released_fix_rollback()
        jump resistAndrasHumiliation
        
    "Unacceptable! You’re their ally, not some lowly servant." if serveChoice == 4:
        $ released_fix_rollback()
        jump resistAndrasHumiliation
        
        
label resistAndrasHumiliation:

"Still gloating, Andras walked up to him, and it looked like he was about to put his arm around him."

show andras displeased at center with dissolve

"Rowan seized him by the wrist, stopping him in his tracks."

show andras angry at center with dissolve

ro 'I think that’s quite enough, "Lord" Andras. I am not some lowly servant you can push around.'
ro "I offered you my help, and I think these people are proof enough of my commitment. It’s high time you start showing me some damn respect."

#ToDo - also add "or rastedel completion"
if goal2_completed == True and escapeBlameSelf == False:
    show andras displeased at center with dissolve
    "Andras stared him down for a short moment, before, surprisingly, taking his hand back and laughing heartily."
    show andras happy at center with dissolve
    show rowan necklace shock at midright with dissolve
    an "Haha, lighten up Rowan! It’s just some harmless fun. Thought I’ll scare the prisoners a bit, so they don’t try anything stupid like running away or plotting a revolt!"
    show rowan necklace neutral at midright with dissolve
    ro "I dread to ask for the details of your master plan here."
    show andras displeased at center with dissolve
    "Andras waved his hand dismissively."
    an "Well, the mood is spoiled anyway, so I won’t be going with it anyway."
    ro "… Then can I go? I have a castle to manage."
    an "Bah! Yes, yes, you can go. I’ll think of something else…"
    an "Maybe..."
    show andras smirk at center with dissolve
    show rowan necklace concerned at midright with dissolve
    "His voice started to regain it’s usual sadistic glee, and instantly raised all the red flags in Rowan’s mind."
    menu:
        "Intervene before he finishes his thought.":
            $ released_fix_rollback()
            show rowan necklace happy at midright with dissolve
            ro "I’ll look over the patrol routes and make sure there are no weak spots the prisoners can exploit."
            show andras displeased at center with dissolve
            an "Haven’t they been perfected already?"
            show rowan necklace concerned at midright with dissolve
            "The words carried a hostile note to it, and Rowan saw his animosity already turning away from the prisoners and back at him. He thought fast, and miraculously managed to come up with something on the spot."
            show rowan necklace happy at midright with dissolve
            ro "They are, but we can have some fun with them if we want to."
            ro "Randomize them so no pattern emerges. Created false weak points to trap people in."
            ro "It will be a good exercise for the orcs as well. It will teach them some discipline."
            ro "No doubt they’ll bitch about it, but I invite them to do it to my face."
            show andras happy at center with dissolve
            an "Ha! That would be a sight!"
            "His mood again improved by the sudden development, Andras took him by the shoulder and both of them left the dungeon to discuss Rowan’s ideas."
            "The prisoners would be spared the worst of the twins wrath… For now."
            $ change_base_stat('c', -3)
            $ change_morale(-5)
            return
            
        "Don't try and stop him.":
            $ released_fix_rollback()
            hide rowan with moveoutleft
            "He shook his head a little, and headed for the exit while Andras was still lost in thought."
            scene black with fade
            "The man was irredeemable… There was no point wasting time with him any further."
            $ change_base_stat('c', 3)
            $ change_prisoners(-3)
            return
            
else:
    show bg8 with sshake
    show bg8 with redflash
    hide rowan with dissolve
    show andras angry at center with dissolve
    "Rowan's whole world exploded in pain, as Andras delivered a furious blow."
    "It was like taking a hammer to the face and it came with similar result. Rowan kept all his teeth, but his whole world went dark for a moment, and the next thing he registered was the cold stone floor he was laying on."
    "The thing he registered after that, was Andras looming over him, glaring angrily."
    an "Respect, Rowan? You want respect?"
    if escapeBlameSelf == True:
        an "After they shit you pulled with that noble slut? Oh I don’t think so."
        an "You have a lot of work ahead of you if you want to make up for that. Capturing potato farmers will not be enough. Not nearly enough."
    else:
        an "Do you think capturing potato farmers is enough to earn you respect?"
    an "The world is ours to take, and I will not hesitate to drown it in blood if that’s what it will take to have it kneel. Until you show yourself willing to do the same you will not be our equal."
    an "Have I made myself clear?"
    "It took Rowan every ounce of self-control not to reach for his sword. Not yet. The gap between them was still too big."
    show rowan necklace neutral behind bg8
    ro "… Yes."
    an "“Yes” what?"
    ro "Yes, Lord Andras."
    an "… Good."
    "The demon glared for a moment, then took one last look at the prisoners around him."
    show andras displeased at center with dissolve
    an "Hrm, now the mood is gone. Can’t believe I have to keep wasting my time disciplining you."
    hide andras with moveoutleft
    show rowan necklace neutral at center with dissolve
    "He left in a huff, leaving Rowan alone with the prisoner. Wearily, the hero got up, the slaves watching in silence."
    if serveChoice != 4:
        "Perhaps this small display of resistance will help them endure…"
    else:
        "The things he was forced to endure so that one day their kids could have a brighter future…"
    return
    

label allowAndrasHumiliation:

show rowan necklace concerned at midright with dissolve

if serveChoice == 4:
    "Rowan lowered his head in defeat. He and the twins might be allies but the pecking order was clear. One side had shock collars around their necks, the other – the magical commands that activate them."
else:
    "Rowan lowered his head in defeat. Stay low, keep quiet – that was all he could do for the time being."
    
show rowan necklace shock at edgeright with moveoutright
show andras smirk at midright with moveoutright

ro "?!"

"Without as much as a word of warning, the demon pushed him right at the cell doors, making him hit the steel bars – hard. Andras’ hand grabbed him by the neck, holding him in place."

an "My bitch to use and abuse."
an "So do not blame him for your predicament. He has no other choice!"

"He tried to struggle, but Andras only gripped him tighter. Goddess, that man strong!"

an "I can use him however I want! Hahaha! He will do everything I demand!"
an "Come on Rowan, say it!"
an "Tell them you’re my little bitch!"
an "Apologize for being a stupid weakling who couldn’t protect his own wife from abduction, and now raids and enslaves the very people who worship him as a hero!"

menu:
    "Do it. It’s easier this way.":
        $ released_fix_rollback()
        jump andrasHumilateSex
    
    "Elbow him in the stomach.":
        $ released_fix_rollback()
        if check_combat(20)[0]:
            "Elbowing Andras felt like punching a stone wall, but despite the sudden pain in his arm, he heard a soft grunt, and the grip around his neck lessened."        
        else:
            "Elbowing Andras felt like punching a stone wall, and had similar results. Rowan felt his arm explode in pain, and he was certain he injured it in the process. But despite that, he heard a soft grunt, and the grip around his neck lessened."
            $ take_damage(3)
        show rowan necklace neutral at midleft with moveoutleft
        show andras angry at midright with moveinright
        "Seizing the opportunity, he pushed Andras off him and quickly put some distance between them. He put his hand on the sword and waited for Andras to make a move."
        "… The moment dragged on. Andras cracked his neck, his eyes burning a hole in Rowan’s skull. Finally, he spoke up, in a low, deadly tone."
        an "Really, Rowan?"
        an "Growing a spine suddenly? Do you think that a stupid display like this will somehow inspire these men? Bring them hope?"
        an "A quick reminder then."
        show andras angry at center with moveinright
        show rowan necklace shock at midleft with dissolve
        "Andras turned his head to the prisoners. Rowan saw his gaze fall on a small girl. She scuttled back."
        show rowan necklace neutral at midleft with dissolve
        ro "Andras, don’t-"
        "He didn’t even manage to get the warning out. Without any theatrics, Andras simply raised his fist, and brought it down."
        show bg8 with sshake
        show bg8 with redflash
        "A red pentagram came crashing down on the girl. Blood splattered everywhere, and screams filled the dungeon. Not the girl’s – Rowan saw her skull crushed almost instantly. A swift, brutal death."
        show bg8 with redflash
        show andras displeased at center with dissolve
        an "So fragile. I continue to be amazed you were able to withstand it Rowan."
        show andras displeased at midright with moveoutright
        an "Now, as much as I’d love to break most of the bones in your body, I know Jezera wouldn’t stop bitching if I harmed her prized toy without good reason."
        show rowan necklace shock at midleft with dissolve
        show andras happy at midright with dissolve
        an "So instead, I’ll let you pick three people here for me to make an example of."
        show rowan necklace angry at midleft with dissolve
        show andras displeased at midright with dissolve
        an "Do take your time, if you want, but have them prepared by your departure at the end of the week."
        hide andras with moveoutleft
        "Rowan could almost hear himself grind his teeth, but he didn’t say anything as Andras passed him by. This was not the time. This was not the place."
        show rowan necklace neutral at center with moveoutright
        "With heavy heart – and burning anger- he picked the three most sickly looking people, and quickly departed the dungeons, leaving the screams and lamentations of the prisoners behind."
        $ change_prisoners(-4)
        return

label andrasHumilateSex:

$ rowanGaySex += 1

if serveChoice == 4:
    "He already sold his soul out to them. There was no turning back. He couldn’t turn back or doubt, or else the mounting guilt will catch up to him and crush him into powder."
    "Perhaps putting all the blame on Andras will bring him some peace of mind, even if only a little…"

if serveChoice == 2:
    "One bad word, one wrong move, and he’ll find himself in that cell again, left to either rot or go insane from the isolation. His insides twisted at the mere thought. He couldn’t let that happen. No matter what."
    
if serveChoice == 1:
    "His position was still precarious. He had to play it safe… Even it meant publicly humiliating himself in front of everybody."
    
else:
    "His wife’s life was o the line. As long as he kept doing whatever the twins demand of him, they’ll leave her alone."
    "Humiliation was a small price to pay for her safety."

ro "I’m sorry everyone. It’s true."
ro "I’m a weak, pathetic bitch who can’t protect anyone. Not myself... Not my wife… Not the people that depended on me…"
ro "I… I let myself be captured, and now I have to do whatever they tell me."
ro "I’m sorry. I really am."

an "Good. Good!"

"Andras hand traveled south and groped his ass. The humiliation would not stop there. And the former people of Rosaria would all bear witness to it. He could almost see the light of hope die in their eyes."

an "Don’t stop there! Tell them everything Rowan! All your sins! Show them what a sissy bitch you are!"

"Andras tore the pants off his body, and pushed Rowan against the cell with force. Held firm by his iron embrace, the “hero” moaned weakly."

ro "I- I…"

an "Out with it!"

ro "I had the orcs raid your villages. Capture you- your families- Aah!"

"Something was forced into his ass. A wet finger, soon followed by another – and another. He cried out from the sudden pain, but his voice was drowned out by Andras’ bellowing laughter."

an "That’s right, show them what you are! A toy to the demons!"
an "Keep talking, Rowan!"

"His fingers started to piston in and out of his ass, making him whimper. He could barely get the words out."

ro "I- pillaged abbeys, enslaving priests. I l-let Cliohna turn them into mindless puppets-"

if goal2_completed == True:
    ro "I delivered Raeve Keep right into their – ah! - hands. I handed them Helayna, who thought the world of me..."
    an "And what a fine slut she proved to be!"
    
ro "Ah!"

"Andras pulled his fingers out suddenly. Rowan felt the demon change his position, his hands now placed on Rowan’s hips. A feeling of dread raised within him, as realization dawned."

ro "Andras, dont-!"

#cg1
scene black with fade
show rowan necklace aroused behind black
show andras smirk behind black

"His cries of protests were cut short as he felt something long and hard pushed straight up his ass!"

ro "Aaaah!"

"He felt Andras’ cock pushed in deep, all while he was still pressed against the cell bars. All while the people of Rosaria still watched, frozen with horror. Fear. Despair. Disgust. All mixed together into a disgusting cocktail he never thought he’d taste."
"He looked away. He couldn’t bear it. This was too much-"

an "Don’t close your eyes! Look at them! Look at the people you swore to protect!"
an "Look at them!!!"

ro "Aaah!"

"Andras grabbed his hair and violently yanked it back. He held him in that position, pointing his face at the people of the other side of the bars."
"… Tentatively, Rowan opened his eyes."
"He would not forget this image anytime soon."

an "Ha ha ha ha! Amazing! Your ass is great Rowan!"
an "I should be fucking it more often, don’t you think?"

"He grumbled something in response. He cried again as Andras slapped his back."

an "Answer me when I talk to you!"

ro "Y-yes! You should fuck it more often!"

"He tried to ignore the paralyzing pain, tried to ignore this massive dick inside of him. But what he couldn’t ignore, was how despite the brutality of his fucking, Andras was hitting this one spot up his ass-"

ro "Aaah!"

"He just couldn’t help it. Violent pleasure mixed in with pain and humiliation. His dick strained against his pants, painfully erect."
"They noticed. Goddess, he saw them notice. The sympathy disappeared from eyes one by one, as they realized what was going on. As they realized that Rowan Blackwell, the Hero of Rosaria, was enjoying getting fucked in the ass by a demon."

an "Ha ha! Aren’t their faces amazing? Look at the girl in front! She looks like she’s about to cry!"

ro "I’m so-orry, I have no cho-oo-ice, aah!"

"She didn’t believe him. They didn’t believe him. And he didn’t believe himself either. He could’ve done a hundred things differently to avoid this situation. He choose to do none of them."
"Because some part of him wanted Andras to demean him like this. Some sick part of him he didn’t quite understand, wanted all of this to happen."

ro "A-andras, ple-ease!"

an "What’s that? Begging for mercy?"
an "As if that ever worked, haha!"

"… Not that his desires mattered to the red demon. Andras took what he wanted. He always did. And right now, he wanted Rowan squirming beneath his dick, and Rowan’s only choice here was whether he would let his voice out, or if he tried to preserve the last shreds of his dignity."

menu:
    "Start moaning. No point pretending anymore.": 
        $released_fix_rollback()  
        $ change_base_stat('c', 3)
        ro "Aaaa-ah! Aaaah! A-aH!"
        "There was no point pretending anymore. None at all. He let his voice raise high, above the sounds of fucking, above even Andras’ laughter."
        an "Hahaha! That’s a nice voice you have there!"
        if alexiaAndrasSex > 0:
            an "You bring your wife to shame with it!"
        an "Come on, bitch! Higher!"
        ro "AAAAH!"
        "He screamed as loud as he could, as Andras suddenly rammed his dick all the way in, as deep as possible."
        
    "Just take it in silence.":
        $ released_fix_rollback()
        "He didn’t have it in him to resist anymore, but the least he could do, was not give in completely."
        "He whimpered pathetically as Andras kept pounding his asshole, but despite his continuous gloating, he refused to raise his voice."
        an "Why so silent now Rowan? Where’s your usual fire? Hahaha!"
        "He wasn’t certain why – it didn’t in any way diminish his humiliation. But somehow, knowing he still could usher at least this tiny bit of resistance… It made the whole experience more bearable."
        "And yet, despite his earlier conviction, he couldn’t help but cry out as Andras suddenly rammed his dick all the way in, as deep as he could."

an "Nn-aaaah! Take it!"
an "Take my cum Rowan!"

"He braced himself, trying to relax his backside as Andras kept pushing in, pumping him full of semen. He couldn’t say what was warmer – the seed up his asshole, or his ears when he heard the prisoners start whispering between themselves..."

an "Hahaha! How do you like it Rowan? Enjoying yourself?"

"A sudden feeling of emptiness brought him back to reality. Andras pulled out, his cum slowly seeping out of Rowan’s stretched anus. Absentmindedly, he gave a small nod, if only out of fear of what would happen if he tried to be defiant now."

scene bg8 with fade
show rowan necklace shock at midleft with dissolve
show andras happy at midright with dissolve

"That must have pleased the demon, because a moment later, Andras gave him a few almost affectionate pats on the head. Somehow this was the most humiliating part thus far."

show rowan necklace concerned at midleft with dissolve

an "Well done Rowan! Well done! I think they’re all sufficiently cowed right now!"

ro "You… You did this just to… Intimidate them?"

an "What? Ahaha, no, of course not!"
an "I did it because I thought fucking you in the ass in front of them would be fucking great! And Karnas' balls were you tight!"
an "But if I can kill two birds with one stone, then why shouldn’t I?"

"If not the context of the situation, Rowan might have burst out laughing at the mind numbing-simplicity of the male twin. But now… All he managed was one last tired look at the whispering prisoners."
"None of them would dream of escaping now… Of that he was certain."

$ rowanAndrasSex += 1
return


############################################################################################################
############################################################################################################
############################################################################################################

label jezera_slave_reward:

#Jezera slave reward

scene bg6 with fade
show rowan necklace neutral at center with dissolve

"As a peasant turned general, Rowan always wondered – how did the nobles do that? "
"How were they able to just… Toss the life of their soldiers away, without any apparent forethought, or visible guilt after the fact, once their stupidity inadvertently kills thousands of people?"
"But as he was now staring at the small stack of files he ordered compiled after his last sacking of the Rosarian villages, he was starting to understand. He reached out for the one on the top, and read:"
"“Prisoner number R034. Name: Annette. Age: 17. Occupation: Daughter of a carpenter. Measurements: 78/65/88. Noticeable traits: Pretty face. Child bearing hips.”"
"And so on, and so on..."

show rowan necklace concerned at center with dissolve

"Numbers. Dry descriptions, without a face attached to them. And their final fate would be now be decided by him, with a few strokes of a pencil. The cruel banality of evil."

show rowan necklace neutral at center with dissolve

"With a resigned sigh, he moved to the bottom of the page."
"“Recommended assignment: ______________ “"

menu:
    "Kitchen help.":
        $ released_fix_rollback()
        #To Do - Lower castle maintenance cost a little 
        $ change_base_stat('c', -3)
        $ change_base_stat('g', -3)
        "An easy job, or as least as easy as anybody could receive in Castle Bloodmeen."
        
    "Manual labour.":
        $ released_fix_rollback()
        #To do - Lower castle maintenance cost moderately.
        "She had to learn something from her father. Skordred would have use of her."
        
    "Orc relief toy.":
       $ released_fix_rollback() 
       $ change_morale(10)
       $ change_base_stat('c', 5)
       "A pretty face was hard to come by, after all…"
        
    "Monster breeding." if castle.buildings["pit"].lvl >= 1:
        $ released_fix_rollback() 
        #TO DO - some bonus to pens
        $ change_base_stat('c', 5)
        "With hips like that, it shouldn’t be too painful for her to serve in the pens… Probably."
        
"He signed the file, then put it away and reached for the next one."

je "Working hard, I see."

show jezera happy at midleft with moveinleft
show rowan necklace neutral at midright with moveoutright

ro "Funny how the bards always omit the paperwork that comes with both saving and conquering the world."

show jezera happy at center with moveinleft

je "Never trust a man whose craft primarily revolves around telling pretty, made-up stories-"

ro "Indeed."

je "-which is why I am happy to know you proved not to be one of such men."

show rowan necklace neutral at center with moveinright
show jezera happy at midright with moveoutright

"Trailing her finger up his arm, Jezera walked past him. A moment later, he felt her arms close around him. Her breath gently tickled his cheek, making his stiffen. "

je "As I expected, you are proving to be an invaluable asset Rowan. I have not been blind to the work you’re doing in Rosaria."

ro "I’m only doing what is expected of me."

je "Oh, don’t be so modest. And insincere."

"Her hands traveled further south, grasping at his chest possessively."

show rowan necklace concerned at center with dissolve

je "I know it hasn’t been easy for you, going after your countrymen like that. They used to look up to you. Tell high tales of your exploits. And now you’ve…"

"A heavy pause followed. “enslaved” was such a dirty word… "

je "Now you’ve granted them a new purpose in life! A better purpose, a better role!"
je "No longer will they be worked to death by for nobles who care little for their well being!"

show rowan necklace neutral at center with dissolve

ro "Seriously, Jezera?"

je "Oh, I know their current situation is not that much better, but trust me, it is only a temporary arrangement. Once our position is secured, my sweet hero, we’ll discuss how we’ll keep treating them."

if serveChoice == 4:
    "He sighed again, and threw the paper on his desk. They endeavored to bring down a cruel society that cared not for the people it was supposed to protect, and they started with widespread raiding and kidnapping."

else:
    "He sighed again, and threw the paper on his desk. Did she honestly believe they were creating a better society this way? Impossible. She had to be at least somewhat self-aware."
    "But it’s not like he could point that out. Besides, as long as he breathed, their little project was doomed to fail anyway."

ro "A temporary arrangement… For the greater good."

je "Exactly! I’m glad you understand."

show jezera happy at midright with dissolve

je "Or at least, that you try to understand. I know how it is Rowan… The mind knows one thing, while the heart…"

"Her slender palm traveled to the left side of his chest, and she put him in what almost could be a reassuring embrace, if the person giving it was not a ruthless tyrant."

show jezera displeased at midright with dissolve

je "… The heart has its own set of truths and refuses to bend to our desires."

show jezera happy at midright with dissolve

je "So let’s deal with that treacherous heart of yours shall we? Right here… Right now."
je "Drop the act, and stop trying to play strong. Allow yourself a moment of respite."
je "Relax, and trust your Mistress. If there’s anything she can do to alleviate that heavy feeling in your heart… You need only to ask."

menu:
    "Ask for better treatment for Rosarian slaves.":
        $ released_fix_rollback()
        ro "Lady Jezera, I am not the one who requires a moment of respite. These people are."
        "He pointed out to the pile of papers on his desk. Prisoner number R034… Annette. He couldn’t give back her freedom. But at least he could make her life somewhat bearable."
        ro "I understand the primary appeal of slave labour is precisely that we do not have to concern ourselves with silly little things like “wages” or “decent living conditions”, and that our position is still precarious, but…"
        show jezera displeased at midright with dissolve
        show rowan necklace concerned at center with dissolve
        ro "But I feel like they’ll always be some excuse to put that matter off."
        show rowan necklace neutral at center with dissolve
        ro "I joined you precisely to improve the situation of Rosarian peasantry. If we have to force them slave for us, then so be it, but at the very least we can treat them decently while we’re at it!"
        "He didn’t see her face, but he could bet his wedding ring Jezera’s eyes were rolling so hard they threatened to pop out. The tired sighed that followed as she took her hands away only confirmed his suspicions."
        show jezera displeased at center with moveinright
        show rowan necklace neutral at midright with moveoutright
        je "I suppose. What in particular would you see us do?"
        show rowan necklace angry at midright with dissolve
        ro "For starters, can Andras PLEASE stop murdering people for no reason?"
        show jezera happy at center with dissolve
        je "Very well. What next? Should I ask the sun to rise in the west? Turn the moon green?"
        if castle.buildings['sanctum'].lvl >= 1:
            je "Have X’zaratl take on vows of chastity?"
        ro "A simple “no” would suffice."
        je "You really should know better by now, my hero."
        show rowan necklace neutral at midright with dissolve
        show jezera displeased at center with dissolve
        ro "Then we’ll start with warm three times a day, meals and 7 hours of sleep. That’s more than we were getting in the army."
        je "Sounds like a waste of resources to me, but you did capture them. It’s only fair for you to take responsibility."
        je "I trust you will take care of the paperwork?"
        ro "Of course."
        je "Then I will take my leave."
        ro "You have my thanks, Lady Jezera."
        show jezera displeased at edgeleft with moveoutleft
        je "I know, I’m amazing. But Rowan..."
        show jezera happy at edgeleft with dissolve
        je "Do think about yourself every once in a while, will you? This self-sacrificial nature of yours is awfully uninteresting."
        show rowan necklace angry at midright with dissolve
        ro "… I’ll keep that in mind."
        $ change_base_stat('c', -3)
        $ change_base_stat('g', -3)
        #to do - raise castle maintainance
        return
        
    "Return the sweet talk, to get into her good graces.":
        $ released_fix_rollback()
        show rowan necklace happy at center with dissolve
        ro "There is no need for you to go out of your way to reward me, Lady Jezera. Despite the difficulties, to see our dream slowly come to fruition is a reward in itself."
        ro "Though I will concede your company is much appreciated. It makes the paperwork almost bearable."
        "Her delighted laugh ringed in his ears, while her hands continued to travel across his chest, checking his every muscle. Like a princess who just got back her favorite doll, and wished to inspect every nook and cranny."
        je "“Almost bearable”? Oh Rowan, you have the best compliments."
        show rowan necklace neutral at center with dissolve
        je "But you shouldn’t just shower me with gifts and praises like that, my hero. They might make me grow indulgent."
        je "They might make me start hungering for more of your attention."
        je "Awaken something in me… "
        show rowan necklace shock at midright with moveoutright
        show jezera happy at center with moveinright
        "In a single swoop, she was in front of him – sitting on his lap, her face close to his. Her purple eyes shone brightly, just as her smile did. Her fangs have a predatory edge to what Rowan believed was supposed to be a playful expression."
        je "Oh Rowan..."
        show rowan necklace neutral at midright with dissolve
        if escapeBlameSelf == True or delane_status == "free":
            je "You do err at times, but I am happy to see you put in the effort."
            je "Really happy…"
        else:
            je "Always putting out when it matters… You really are my most precious possession."
        "She kissed him suddenly, forcefully, biting him on the lip. Driven by instinct, his hands reached for her hips-"
        show rowan necklace shock at midright with dissolve
        "Jezera slapped them away with lightning speed, her joyful laugh once more filling the room."
        show rowan necklace happy at midright with dissolve
        je "No touching! You had your chance to ask your mistress for a reward, but instead, you chose to pour more honey into her ears."
        je "And now... I think I will be using your mouth some more today."
        show jezera happy at center with dissolve
        "Her dressed disappeared from view as Jezera casually took it off and tossed it to the side. Two perfect orbs greeted Rowan’s eyes, with small, pointed nipples that begged for attention."
        if NTR == True:
            show rowan necklace concerned at midright with dissolve
            "A soft voice in the back of his head asked him: “What would Alexia think if she saw you now?” He tried to quiet it. And failed."
        show rowan necklace neutral at midright with dissolve
        je "Lick em."
        "-a quick, harsh command-"
        je "You know you want to."
        "-followed by a sweet whisper, right into Rowan’s ear."
        menu:
            "Do it.":
                $ released_fix_rollback()
                jump jezLick
        
            "Hesitate. You shouldn’t be doing this to Alexia.":
                $ released_fix_rollback()
                show rowan necklace concerned at midright with dissolve
                show jezera displeased at center with dissolve
                je "Well?"
                "He turned his head away, ashamed. He shouldn’t have let her get this close…"
                ro "… It’s not right."
                je "What do you mean it’s not right! Is it-"
                je "Is it because of Alexia? Suddenly remembering you’re a married man?"
                show jezera happy at center with dissolve
                je "Oh, Rowan, Rowan, Rowan…"
                "She ran her fingers through his hair, in what was almost an affectionate gesture."
                je "You’re such a sweet lover…"
                show jezera happy at midleft with moveoutleft
                show rowan necklace shock at midright with dissolve
                je "I suppose I can’t blame you for trying to be faithful. I wouldn’t want my most valuable servant to develop a habit of betraying the women he loves."
                show rowan necklace neutral at midright with dissolve
                je "And now that I think of it..."
                show rowan necklace concerned at midright with dissolve
                "She folded her arms beneath her breast, and pushed her orbs upwards."
                je "I do have two of these. I guess it’s only prudent you and Alexia share them."
                je "Maybe not today, but at some point. Look forward to it, my sweet hero."
                hide jezera with moveoutleft
                show rowan necklace shock at midright with dissolve
                "And just like that, she was out of the room."        
                "Her dress still on his desk."
                show rowan necklace neutral at midright with dissolve
                ro "(I just hope the staff won’t start talking about her leaving my study like this…)"
                $ jezeraDress = True
                return
                
            "Politely, but firmly, ask her to stop distracting you and let you work.":
                $ released_fix_rollback()
                show rowan necklace angry at center with moveinright
                show jezera displeased at midright with moveoutright
                ro "Jezera…"
                "He seized her hands, finally putting an end to her groping. Did that woman have no concept of personal space?"
                ro "I appreciate the attention, but need I remind you I’m a married man?"
                show jezera happy at midright with dissolve
                je "I do seem to vaguely recall that fact."
                ro "You should, since as it happens the woman I am married to - love of my life, remember? - is being kept prisoner by you and your brother."
                show jezera displeased at midright with dissolve
                ro "So unless I proved myself enough for you to finally remove these bloody amulets, and maybe allow my wife some freedom of movement outside the castle, I’d rather just focus on my work."
                "He heard a pouting “hmph!”, behind him, and the demoness took her hands away."
                show jezera happy at center with moveinright
                show rowan necklace angry at midright with moveoutright
                "When she appeared before him again, it was as if the pleasant smile never left her face."
                show rowan necklace neutral at midright with dissolve
                je "You tell it as they were only a bother to you. What about the communication they provide!"
                ro "Useful for me, not so for my wife."
                if NTR == True:
                    show rowan necklace angry at midright with dissolve
                    show jezera displeased at center with dissolve
                    ro "I do not know if you can send images through them, but if yes, I can only imagine Andras primarily usage for it is to send my wife the outline of his junk."
                    je "It does sound like something he would do."
                    show rowan necklace neutral at midright with dissolve
                else:
                    show jezera displeased at center with dissolve
                ro "So how about it?"
                je "..."
                je "I shall keep that in mind, but we still have a long road ahead of us. You have to be patient my sweet hero."
                ro "Of course."
                "She continued to observe his reactions, and he held his gaze firm. For a short moment, it seemed like Jezera was starting to feel uncomfortable under it."
                "Perhaps she was starting to realize that a man who had no trouble enslaving the very people he swore to protect, and who cared not for her feminine charms, would not be so easy to control."
                show jezera happy at center with dissolve
                "But the moment passed, and soon enough her posture once more projected confidence and power. The Lady of the castle… An act, nothing more."
                je "Do not worry Rowan. Serve us well, and you will be rewarded. With you by our side, we can reshape the world as we desire."
                show jezera happy at edgeleft with moveoutleft
                je "Don’t overwork yourself, and remember – my doors are always open for you."
                hide jezera with moveoutleft
                ro "… Of course."
                $ castle.treasury += 20
                return
                
            "Enough teasing! Throw her against the desk and fuck her.":
                $ released_fix_rollback()
                show rowan necklace happy at midright with dissolve
                "He placed his hands over hers, and looked up to give her his most benevolent smile."
                ro "You’re right, there is something my Mistress can do for me."
                show rowan necklace neutral at midright with dissolve
                show jezera displeased at center with dissolve
                "He rose up suddenly, pulling her to him. The surprised demoness offered almost no resistance, and Rowan threw her at the table, his earlier paperwork sent flying."
                ro "My “mistress” can stop being such a tease, and start putting out."
                "For a moment – just a short moment – he saw the cold fury enter her eyes. But it was gone just as quickly as it appeared, hidden behind her usual, cocky smile."
                show jezera happy at center with dissolve
                je "Oooh, someone’s feeling domineering today. "
                je "Whatever will I do! How can I stop this violent man?"
                "She spread her legs invitingly, her voice taking a dramatic undertone as she pressed the back of her hand against her forehead, like a damsel in distress."
                show rowan necklace angry at midright with dissolve
                je "Oh woe is me! I guess I have no choice but to allow him ravage me! Allow him to plow me like a common street whore!"
                if get_actor_flag('alexia', 'andras_influence') >= 5:
                    je "I can only lay down, and take it like his slut of a wife takes my brother’s cock!"
                "He grit his teeth in fury. That damn slut-!"
                show jezera happy at center with dissolve
                "But she wasn’t resisting at all, and it made him hesitate. It was almost as if she was inviting him to make some stupid move... "
                menu:
                    "Fuck her right here, right now.":
                        $ released_fix_rollback()
                        $ jezDenialSex = True
                        jump jezDenialSexScene
                        
                    "Don’t play into her hand.":
                        $ released_fix_rollback()
                        show jezera displeased at center with dissolve
                        ro "No… You will “allow” me nothing."
                        if get_actor_flag('alexia', 'andras_influence') >= 5:
                            ro "And you will refrain from further comments about my wife."
                        show rowan necklace neutral at midright with dissolve
                        ro "I think I’ve proven myself enough, and it’s high time you start treating me like an equal."
                        show jezera happy at center with dissolve
                        je "Like an equal, you say? Oh, my sweet hero, you know I like you…"
                        if escapeBlameSelf == True or delane_status == "free":
                            je "But your record is far from spotless."
                        else:
                            je "But our work has only begun."
                        show rowan necklace shock at edgeright with moveoutright
                        show jezera neutral at center with dissolve
                        "With a snap of her fingers, magical tethers shot out from all around them, binding Rowan and forcing him away from the demoness. Jezera closed her legs, got up, and ostentatiously removed an invisible speck of dust from her shoulder."
                        show rowan necklace angry at edgeright with dissolve
                        show jezera happy at center with dissolve
                        je "But I do hear you my hero. And truth be told… You know I wouldn’t mind getting a bit more… Intimate with you."
                        je "But first, let’s focus on solidifying our hold on Rosaria, shall we? Once it falls... Then we can talk."
                        show jezera displeased at center with dissolve
                        ro "You mean once I take it for you."
                        show jezera happy at center with dissolve
                        je "Once you help us take it. With our soldiers. Our spies. And our magic."
                        je "My sweet hero, I’ll pretend this little outburst of yours never happened, but be a dear and don’t forget your place, would you? I’d hate to have to discipline you."
                        if NTR == True:
                            je "Especially since, as always, Andras would insist I let him punish Alexia in your stead, which I find awfully… Primitive."
                        "She circled her finger, and Rowan growled as he felt himself being forced down into his chair. The magical strings went under his arm and wrapped both his chest and the back of the chair."
                        show jezera happy at midleft with moveoutleft
                        show rowan necklace angry at midright with moveinright
                        "Then they circled around his desk, and with a screeching sound, pulled him to it."
                        je "Now as much as I’d enjoy toying with you further, I do believe you have work to do."
                        je "Don’t let me occupy you any further. Ta ta!"
                        hide jezera with moveoutleft
                        "She left him alone with his papers, his wounded pride, and cold, boiling anger in his heart." 
                        "He would get her… In due time."
                        return           
    
    
label jezLick:

$ PostRaidingJezeraHandjob = True

#cg 1 blurred
scene black with fade
show jezera naked happy behind black

"Hungrily, he started sucking on her breasts, starting from the left, and agonizing Jezera forbade him from reaching for the other."
"His efforts were rewarded with a soft, joyous chuckle, so common whenever Jezera was pleased with him."

je "That’s right… Worship your mistress nipples. Suck ‘em. Lick ‘em. You can even use your teeth, if you want to."

"He did just that, evoking a moan of delight from the demoness. Her voice ringed in his ears – a beautiful melody she magnanimously bestowed upon him."

je "Yesss… That’s right Rowan… You’re doing a wonderful job. Now the other."

"He followed her lead, feeling her warmth, basking in her perfume. Damn it, why did she not allow him to touch her!"

je "Such a good servant you are… And so selfless too…"

"Her body curved erotically as she clung to him, her sweet whispers never ceasing."

je "A bit too selfless even…"

"Rowan gasped in surprise as her hand suddenly grabbed his crotch. His dick was already painfully erect, there was no way Jezera did not feel it earlier."

je "A heart can be a difficult guide, Rowan. I think you would be much happier if you listened to this little guy more often."

#cg 1
scene black with fade
show jezera naked happy behind black
show rowan necklace aroused behind black

"She continued to fondle him through his pants, making him moan in desire. Her fingers started to undo his buckle deftly, and soon enough, his cock sprung forth, growing from beneath her touch."

je "See how hard you are? "

"Jezera poked it with a smile on her face, making Rowan inhale sharply."

je "See how much you desire me? How much you want me? "
je "And yet you did not ask me to take care of it."
je "Was it because you hoped I would service you of my own accord, hmmm? Or do you still lie to yourself, that it is not something you desire?"
je "Be honest with yourself for once Rowan. Tell me this is what you wanted. Tell me this is what you hoped would happen the moment I walked through that door."

menu:
    "Admit that you did.":
        $ released_fix_rollback()
        ro "I did. Goddess, I did. You drive me crazy Jezera."
        je "I know. And I plan to keep doing it."
        
    "Avert your gaze, say nothing.":
       $ released_fix_rollback()
       je "Too ashamed to say it? Oh, Rowan… If I didn’t have you kissing my tits, I might’ve gotten mad here"
       je "But this one time… I’ll give you a pass."
       
"Her mouth found his, locking their lips in a passionate kiss while her fingers gripped his cock. She started to gyrate her hips, moving her body up and down, with her fingers still locked around his phallus."
"The tip of his cock kept brushing against her lower lips, against the skin of her stomach, teasing him, but never allowing him to come even close to experience the warmth of her pussy lips."

ro "Jezera-"

je "Shh… Not today, my sweet hero…"

if jezeraIntroSex == True:
    je "You’re doing well… But if you want me to let you in again, you’ll have to do better than a few villages."
    
else:
    "You’re doing well… But if you want me to let you in, you’ll have to do better than a few villages."


"There would be no negotiating with her in this regard, not that Rowan had it in him to try and push the issue. He focused his attention on her breasts, on her lips, kissing and licking to please the woman that – at the moment – was literally holding him by the balls."
"And as long as he was playing nice… It really didn’t sound that bad…"
"Locked in her embrace, the two of them continued their caresses. And even though Jezera kept teasing him about wanting to “use him” for her own pleasure, she did not shy from showering him with affection."
"More than once, she had him stop his ministrations, just so she could focus on playing with his cock. Tease his tip gently, or fondle the base enthusiastically."
"But her eyes never left his own, and she would not allow him to look away either. She wanted to see him come. Wanted to see him climax beneath her fingers."
"And it didn’t take long for that to happen." 

ro "Nn-aaah!"

"She laughed happily as she saw his face twist in ecstasy. She jerked his cock away from her body, so the seed would not land on her - and obviously ended on him. But he couldn’t even be mad at this."

je "Enjoyed yourself?"

ro "Y-yes, Mistress."

scene bg6 with fade
show rowan necklace happy at center with dissolve
show jezera naked happy at midleft with dissolve

"Satisfied with his answer, she gave him one last kiss and climbed off him. As she grabbed her dress, she stopped for a moment to appreciate her handiwork."

#jez naked sad

je "Ah… I almost feel bad about wasting it like that."

#jez naked smirk

je "Perhaps next time I’ll bring a slave for you to finish in."

ro "I feel like there’s like a simpler solution here…"

show jezera naked at edgeleft with moveoutleft

"She flashed him a cheeky smile headed for the exit, not bothering put the dress on. Her ass swayed before his eyes, and he almost missed her parting words."

je "Maybe there is… Keep up the good work my sweet hero, and maybe I’ll consider it..."

$ change_base_stat('c', 3)
$ change_base_stat('g', -3)
return

label jezDenialSexScene:

show rowan necklace neutral at midright with dissolve

"If this was a trap, it was a damn enticing one. A sweet smile, parted legs, and an overall aura of submission that could not be natural. Mocking remarks aside, everything about Jezera screamed “Take me”."

"“Take me. Ravish me. Claim me. Fuck me. Fuck me. Fuck me!”"

show jezera happy at center with dissolve
show rowan necklace angry at midright with dissolve

"It was too much to bear."

"Without another thought, he unbuckled his pants, making his erect cock spring forth. Jezera made a loud “Ooooooooooh!”, and ran her finger along the side of it."

je "So big! It will split me apart!"

ro "Enough with the chatter, Jezera. Open wide."

#cg2
scene black with fade
show jezera happy behind black
show rowan necklace angry behind black

"She prepared another mocking remark, only to have it cut off midway as Rowan mercilessly thrust into her!"

je "Ah, so rough! Rowan, I never suspected you had it in you!"

"“That’s what you get for teasing me all the time”, he thought, but he did not grace her with a response. Instead, he started to move hips with vigor, pushing into her without any consideration for her demoness."
"Finally, he got to enjoy that tight pussy of hers. All he had to do was cut through all that teasing bullshit of hers and get straight to the point, straight to the fucking."

je "Yes! Fuck me! Fuck me harder! Harder!"

"Her jeering moans chafed his ears, even though he did his best to ignore them. He redoubled his efforts to silence the demoness, but all that got him was further laughter."
"Perhaps later, he would regret his hasty decision. But he couldn’t care less about “later” now. In this moment, all that mattered was painting Jezera’s whorish hole white with his seed."

je "That’s right, fuck me, my stud! Please your mistress!"

ro "This is not your circus Jezera, it’s- ngh?"

show black with redflash

"Something was wrong. He felt the pressure rising in his crotch, but only for it to- to hit a wall of sorts."
"He looked down. A blue ribbon was tied around the base of his penis."

ro "You-!"

#cg2 - variant 1
scene black with fade
show jezera happy behind black
show rowan necklace aroused behind black

"Her legs tightened around his hips and pushed him further into her tight hole, making him lose his train of thought as another moan escaped his lips. His cock pulsated with pleasure, but Jezera's spell denied him his much needed release."

je "What’s wrong Rowan? Cat got your tongue?"

ro "Stop-"

"He tried to pull out, only for further tethers to jump out of Jezera’s fingers, tightening around his body, around his neck."

je "Oh, I’ll stop when I want to stop. You, on the other hand, should do anything but that."
je "Keep thrusting Rowan. Make your mistress cum."

"His anger rose, only to be met, and defeated by, the combined efforts of the numbing pressure in his balls and the dangerous tightening of the thread around his neck. She wouldn’t hurt him… Probably not."
"But he needed release, and Jezera’s wet pussy still squeezed around his cock. His body told him to keep fucking, even if his mind knew it would be of no use."
"In the end, his mind failed to provide a way out, so instinct took over. He started to once again push into the demoness, thrusting enthusiastically, without the earlier roughness, but with twice the need."

je "Ooooh~, that’s better!"
je "It’s so nice to have a reminder of why I keep you around."

ro "-it’s – AAH!"

"The tether around his dick tightened, causing him to shout out in pain. Jezera’s cold stare dispelled all doubts that it might have been unintentional."

je "I think you’ve said enough today, my sweet hero. So how about you keep quiet for a moment here, and listen to what your Mistress has to say."

"Her foot kicked from behind, ordering him to resume thrusting. He complied, partially of fear, but mostly out of vain hope she’ll finally let him find relief."

je "I do not mind that rebellious streak of yours, I really don’t. I did not spend months orchestrating your capture just to gain a spineless puppet incapable of acting on her own."

"Thrust. Thrust. Thrust. Damn it, how much longer!"

je "But do not – oooh, yes, that’s the spot, keep that tempo! - But do not forget your place. Do not – ah! - forget who you serve."
je "If you want my pussy this badly-"

"Jezera pulled the tether around his neck, causing him to almost fall forward. Knowing better than to oppose her now, he quickly recovered and resumed his movements. "

je "Then I wouldn’t mind letting you have it every once in a while… But on MY terms."
je "Do you – ah! - understand?"

ro "Y-yes, mistress Jezera!"

"Her pussy tightened, and Jezera’s smile grew wider."

je "Again!"

ro "Y-yes, Mistress Jezera, whatever you say!"

je "Again!"

ro "On your terms only-!"

je "Again!"

ro "I’ll do whatever you say, just please-"

"Her body arched and her mouth closed around his, locking them both in a tight embrace as the demoness finally climaxed beneath him."
"He was hoping she would undo the spell, but no- he could still feel the tether around his cock, he could still feel the agonizing pressure that came with it."

je "Mmmmm… Well done, my sweet hero. Well done."

scene bg6 with fade
show jezera happy at center with dissolve
show rowan necklace concerned at midright with dissolve

"She pushed him off her, just as suddenly as he threw her earlier, in what now felt like an eternity before. He allowed himself to fall to his knees, too exhausted to cling to his pride."
"His erect cock swayed in front of his eyes."

show rowan necklace happy at midright with dissolve

je "Now… You know I am not a cruel woman. I see my string was perhaps… A bit too intense for you. I will remove it, and let you cum."
je "And all you have to do is say “I’m sorry for everything Mistress Jezera. Please let me cum”."

menu:
    "Say it.":
        $ released_fix_rollback()
        show rowan necklace aroused at midright with dissolve
        "Halfway through the last words, the string came undone, and slid up his cock. He felt himself explode, waves of ecstasy taking over, as he started cumming all over the place. Some of it got into the carpet. Some at the desk."
        show jezera happy at midleft with moveoutleft
        "Jezera took a step to the side to avoid getting hit by it, and chose to merely watch the spectacle."
        if rowan_shares_room_with_helayna == True:
            je "Ahhh, what a mess. Want me to send Helayna to clean it up? I think she wouldn’t mind getting a mouthful of your seed."
        else:
            je "Ahhh, what a mess. Want me to send Alexia down to clean it up?"
        ro "I… No, please do not."
        je "She straightened her dress, then bent over to pick up all the stray papers the two of them threw off. She arranged them neatly on his table."
        je "Now, we had our fun, but don’t forget to do your job! Work hard!"
        je "Ta ta, my sweet hero!"
        
    "Don’t. Keep a shred of your dignity, if nothing else.":
        $ released_fix_rollback()
        "He didn’t dare to look up at the demoness. He knew she would not take kindly to his resistance."
        je "Oh? Nothing?"
        je "Have you grown fond of my strings, by any chance?"
        show rowan necklace concerned at midright with dissolve
        "He saw the blue ribbon break. Half of it returned to her fingers, the rest – further tightened itself around his dick, causing him to gasp in pain."
        je "Then you can keep it! For the remainder of the evening, at the very least."
        "A sheet of paper was put in front of his face. It read “Prisoner number R017. Name: Jack. Occupation: ...”"
        je "But do get these sorted out will you? Or else we’ll start talking… Consequences."
        "He took the sheet of her hands, trying not to look her in the face. He couldn’t stand the gloating."
        je "Ah, this was fun. But enough of that. Enjoy your evening Rowan! Ta ta, my sweet hero!"
        
ro "..."
ro "Fuck..."

$ rowanJezSex += 1

return

    