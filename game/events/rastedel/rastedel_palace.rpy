label rastPalace:

if palaceStage == 1:
    jump palaceFirstVisit
    
else:
    jump palaceRepeatVisit


label palaceFirstVisit:
#First visit


#palace BG
scene bg34 with fade
show rowan necklace neutral at midleft with dissolve
show doran beardless neutral at edgeleft with dissolve
show werden neutral at midright with dissolve
show rosarian knight neutral behind bg34

"Duke Werden escorted them briskly over the river to the palace. Inside, Rowan was treated to a familiar experience, the whisper of nobles in darkened corners when he passed by. No one greeted him as he approached, but everyone had something to say to someone else."
"It was so quiet that one could have heard a dish clatter if a servant dropped one."
"Duke Werden stopped them right outside of a large doorway that led into the throne room. There was chatter from behind the door. Court was probably in session."

werd "You will wait right here until the Baron calls you in. Good luck."

hide werden with moveoutright

"Then he strode through the doorway, leaving Rowan and Raeve together, and with no one else insight."

dor "Please tell me you remember your story...Mistress will be horribly displeased indeed if we fail..."

ro "I know what I must do. You needn’t have to worry."

"Rowan looked around. Here in the halls of power was the nerve center of the kingdom. Clearly this is the place where Jezera wanted him gathering contacts." 
"But, how he was going to do that was a mystery. Raeve was a spineless dullard and he had no native ability to schmooze with nobles." 
"Then the door suddenly opened."

rkn "Now presenting, Duke Doran Raeve of Raeve Keep and Rowan Blackwell, Hero of Karst."

"Rowan and the Duke exchanged a brief glance. Then they walked into the throne room."
"The sides of the hall were lined with men and women in outfits made from silk and fine cotton. No doubt each was a noble. Strangely, Duke Werden was not here. He must have already left. Rowan and Doran walked into the center of the hall and fell to one knee." 
"There were facing a large dais with a luxurious throne on it. And on that throne was the most important man in the entire realm."

show casimir neutral at midright with dissolve

"Baron Casimir IX De’Rosa was the nominal sovereign of the realm. At a word, he could have the head of anyone in the realm. He could martial troops, order special taxes, or even decide the innocence or guilt of an accused man." 
"Which is why it was so strange that few looked to him to put out the first command."
"In truth, the Baron had not been all there in a long time. Even Rowan, disconnected from court politics as he was, knew that. The man’s dull gaze was remarked upon even in taverns and shops." 
"Some argued that in his prime he had been competent enough. But, there was little time between his coronation and the death of his son on the North Illia Fields during the early years of the war. It was said the Baron had wept for two fortnights straight."
"He’d never fully come back after that. In all of Rowan’s prior visits to court, the only thing striking about the man was the dull grey of his eyes."

show marianne neutral at edgeright with dissolve

"That is why, it was not the Baron who spoke first when they entered the hall. It was instead the woman at his side."

mari "Duke Doran Raeve! Solansia’s blessings be upon you. The whole realm prayed eagerly for your safe return. It is good to see you returned to us."

"She took a step down from the dais that the throne was raised on. This was also a person Rowan recognized easily. It was High Arbitron Marianne of Prothea. A leading servant of Solansia who had been sent to lead the Rosarian branch."
"She was, in effect, the highest religious authority in all of the realm. All of the priests and nuns, even those of native Rosarian blood, were commanded by her. Her divine bloodline was her claim to authority."

dor "It is good of you to say that, Your Beatitude. It has been a hard journey from my keep, filled with many sleepless nights."

mari "Indeed."

"She stepped down from the dais. She walked with her palms up and to her side. They had a perfect symmetry to them. Indeed, from her pose to her outfit, there was nothing disorderly at all about her appearance. Even her silver hair, a mark of divine descent, was even exactly."
"She walked all the way to where the two were kneeling, and herself bent down. Rowan was shocked to feel her hands touch his cheeks. They were so very warm and soft."

mari "And you are the cause of this joyous occasion, are you not?"

if avatar.corruption < 30 and serveChoice != 4:
    "Rowan sighed. His heart sank at the mere prospect of lying to this woman. All his life he had learned that this woman was a gift to the people directly from Solansia herself, and now he had to lie to her? But, it had to be done. For his sake and Alexias."

elif avatar.corruption > 60:
    "Rowan held back a scowl. She hadn’t said anything yet, but he already knew she was going to spill out into some sanctimonious nonsense. Is that all it took for her to keep power? Dress nice and talk in that exaggerated manner?"

else:
    "Rowan sighed. Being in the presence of this woman was strange and confusing. He’d learned his whole life that she was a gift to the people directly from Solansia. Yet, she was overlooking a world where nobles and demons alike wreaked havoc on the common people."
    "Would lying to her really be so bad?"

ro "I was, Your Beatitude. I live near Raeve Keep, and when the fighting started, I personally spirited him from the castle."

"The nobles at the sides whispered to one another. Rescuing a duke from a falling keep fit their perceptions of Rowan perfectly. That was the genius of the lie."

ro "Afterwards, I had to lead him through hostile country. We had to spend many days in hiding to escape from patrols."

mari "How revolting!"

"She looked back at Baron Casimir."

casi "Indeed. A great tragedy."

dor "You cannot imagine the challenge. Half my beard was singed in a fire as well. Without Rowan, I never would have been able to survive unaided. So many fell to orcish blades in front of my own eyes."
dor "I have thought every day since then of the lady. Her guidance was as valuable as my saviour."

"Marianne rose to her feet, brushing off the dirt from her long skirt. Her piercing, golden eyes studied Rowan inscrutably."

mari "Indeed. Though, in this case perhaps they were one and the same. Rowan is one of the six heroes Solansia blessed us with, in our time of need. No doubt his appearance in time to save you was one of Solansia’s blessings."

"The Baron scratched his beard and continued looking on without having much to say. It was strange how a man raised above all else could somehow fade into the background so easily."

mari "Surely, you are both very tired after your journey. Please take my blessing and-"

show patricia neutral behind black

patr "Wait!"

hide patricia 
hide casimir with dissolve
show patricia neutral at midright with dissolve

"A middle-aged noblewoman wearing her hair in a bun and with long tired eyes emerged from the pack and went up to the dais to whisper something to the Baron. Marianne turned, eyes briefly narrowing."

mari "Chancellor Crevette. Is there some business you wish to discuss?"

"Rowan had heard the name before, he believed. Patricia Crevette. She’d been a functionary in the royal administration at the time. They’d met once when she’d been sent to the front to discuss provisions. Was she the chancellor now?"

patr "These are the first two individuals who have arrived who saw the events in Raeve Keep first hand, it would be a mistake to dismiss them without first learning what they saw."

mari "Surely this can wait? They are no doubt quite tired."

"She smiled softly."

patr "No, it cannot. Tonight is the ball. And the docket is filled for the coming days. Do you plan to detain them indefinitely?"

mari "Very well, ask what you wish."

"Marianne made a broad sweeping gesture and made a move to the side. Rowan looked back and forth between the two. The conversation had been polite enough, but he understood noble politics well enough to realize that these two were not friends."

patr "Duke Raeve, please explain further the events that led to the fall of your home. Who was it that attacked? You’d sent off a report involving demons before the events in question."

"Doran started to sweat. The earlier segment about his rescue had been the subject of most of his coaching. This might actually require improvisation."

dor "I-indeed, My Lady. It is prudent of you to ask. Your interest in my plight warms my heart."
dor "It was a large band of orcs. I cannot say how long they had been organizing for, but they came upon Raeve Keep quite suddenly."

"Chancellor Crevette gave a skeptical eye."

patr "You mean to tell me that your keep was felled by some simple band of orcs?"

"Duke Raeve shook his head nervously. The absurdity of the idea was not lost on him. Raeve Keep could have held off an entire army of orcs with some ease."

dor "If only it was just orcs. If only."
dor "There remain many foul creatures from the time of the last war. There were some demons at the head of the force. No doubt minor demons who, lacking a mistress...or master, brought some wretched brutes under their banner."

"This was the explanation that been worked out in advance. It was implausible to say there were no demons involved. Prior demonic sightings, the possibility of a witness, and common sense suggested something unusual was afoot."
"But, Rowan could only imagine the punishment that would befall him or his wife if he actually warned them that demons of the powers of his Masters were gathering strength."
"Marianne visibly seemed to tense when the word demons was brought up. Was it fear of the demons, or something else?"

mari "Demonic remnants. Solansia be praised. Were these the same demons that you had reported sightings of earlier?"

ro "I was there for both the attack on Arthdale and Raeve Keep. T’was the same creatures at both. Large brutish creatures. They resembled the Skull-Splitters that served as blood guards in Karnas’ army."

"Marianne’s composure returned. Skull-Splitters were dangerous melee combatants, but they were not pressing foes in the way that demon lords were."

mari "Truly a horrible thing to hear. And with such creatures roaming around the outlying provinces, surely great suffering will come to pass. It is a shame that so little can be done about it with our forces in their present state. Otherwise, we would-"

"Patricia interjected, trying to cut the High Arbitron off."

#Show Patricia and Marianne (both look upset. They are on opposite ends of the screen.)

patr "Actually-"

mari "Otherwise, we would do more to return your seat to you. Solansia’s guidance will surely lead us too-"

patr "Stop. Listen."

"Marianne turned backward towards the Chancellor. Even the Baron lazily looked towards her."

patr "I believe it should be viable for us to put together a royal force and march them out to the west in order to-"

mari "A good thought. Oh, I pray we could. But, Solansia has put a trial to us, and we find ourselves fighting so many foes. Goblin raiders in the south. Orcish confederations in the north. Strikes in the mines and bandits in every direction. Truly it is a shame that-"

patr "No. Stop. Listen."

"Marianne’s face darkened. It seemed that even a messenger from Solansia herself didn’t like being interrupted. Chancellor Crevette was openly glaring at her now. Rowan and Doran exchanged a brief glance."

patr "You’re right that the deployment of the regular army in force in this situation is impossible. We’d, at the very least, need to call in the levies, and even then we’d have limited numbers."
patr "But, Solansia’s Thorns are based here in Rastedel. The most noble of knightly orders in all of the realm. Duke Antoine of Werden is their commander. He can summon them at a word’s notice. "
patr "That’s at least one hundred of the best trained and armed knights in the realm to use as a core for our forces."
patr "And he has levies of his own as well. So does Duke Mortimer. Surely with their levies supplementing the Thorns and a contingent of the Royal Guard, a force large enough to retake Raeve Keep can be mustered."
patr "We can give this man his keep back. All we need to do is call for the Duke of Werden’s support.  "

"The prospect raised alarm bells to Rowan. The Duke was the most dangerous soldier in the realm. At the head of a force bearing down on Raeve Keep, he could be a real problem." 
"The man had an iron sense of justice. He was famous for the row of gallows that he placed those who tried to bribe him or his lieutenants. There would be no tempting him, no corrupting him, and no deal to be struck."
"It seemed that Rowan was not the only one taken aback by that idea. A wave of whispers went out in the back of the room, the place where the lesser nobles congregated. It seemed the idea was not popular among them either."

mari "Ah yes. Your friend Duke Antoine. I have no doubts of his piety, nor his devotion to Solansia’s justice. Still, it is a strange thing to hear. Are the reports I have heard of raids within his own lands untrue? Brutal savages slaughtering his peasants as well."

patr "The fall of an entire duchy is more pressing. Minor raids can wait."

"Marianne took a step towards the dais. She was regaining her momentum."

mari "It is indeed a horrible tragedy. Solansia weeps for the fallen. But, if he were to call his arms, then surely the northern orcish tribes would take the opportunity to strike. Solansia’s love can only be returned to the west through balance. He must put his house in order."
mari "And so when the time comes to bring the light back, the royal army must be reformed and ready for such an operation."

"She stepped on to the dais. Now the High Arbitron and the Chancellor were standing face to face."

hide rowan with dissolve 
hide doran with dissolve
show patricia neutral at midleft with dissolve
show marianne neutral at midright with dissolve

patr "We must be prudent and deal with problems based on priority. The loss of a duchy is a threat to the entire order of this world."

mari "Your fears are becoming of you, Chancellor. But, you should have more faith in Solansia’s wisdom. We will overcome this issue once other, more pressing, business has been completed. Don’t you agree, Your Regality?"

show patricia neutral at edgeleft with moveoutleft
show marianne neutral at edgeright with moveoutright
show casimir neutral at center with dissolve

"The Baron blinked twice, as if waking from a stupor. He looked back and forth between the two of them for a moment, and then coughed."

casi "Yes. Yes. You are quite right. First the bandits and the famine, then Raeve Keep. You will simply have to wait, Lord Raeve."

show casimir neutral at midright with moveoutright
show marianne happy at edgeright with dissolve

"Marianne didn’t show any overt signs of gloating, but her back straightened, and her eyes kept matching the other woman’s. Rowan didn’t quite understand all of what had just transpired, but it was simple enough to understand that this was not the first time they have disagreed."

show patricia neutral at midleft with moveinleft
show doran beardless neutral at edgeleft with dissolve

dor "I am saddened to hear this. B-but perhaps it is for the best. I need rest and recuperation before I am able to serve as your man again to my usual standards."

"Lady Crevette gave a terse curtsy and made for the door. It seemed that she didn’t even want to stay for the rest of the proceedings. She walked with a standard dignified strut, but Rowan could see raw anger in her eyes as she passed him."

hide patricia with dissolve
show rowan necklace neutral at midleft with dissolve

casi "Guards, please make suitable arrangements for the Duke in the palace. Make sure, too, that Rowan Blackwell has a place to stay."
casi "Is there any further business? No? Then, I declare this session adjourned."

"The guards all around their room banged the bottoms of their polearms on the ground, signaling the end of the session. Nobles of all stations began streaming towards the exits. However, Marianne made no motion to leave. She was even whispering something into the Baron’s ear."

hide casimir with dissolve
hide marianne with dissolve
show rowan necklace concerned at midleft with dissolve

"Doran rose to his feet, and walked out besides Rowan. A few faces, mostly those Rowan had never seen before, stopped to try to speak. Rowan exchanged a few words, but mostly waved them away. He had something to ask his companion."

ro "Can you explain what happened in there?"

"Doran shook his head."

dor "Some, but not all. I fear I’ve been quite disconnected from capital politics. I never much liked it…"
dor "The Baron rules the realm, but it is said that Marianne rules the Baron. When she speaks of someone else, he listens."
dor "My sense of it is that she tried to take control of the session. But, despite his absence, this was the Duke’s show."

ro "Duke Antoine of Werden? But, he was not even in the room."

"Doran shook his head. The man was normally quite spineless, but at least he was able to decipher all of this noble nonsense."

dor "He could not be seen in the room, lest he be accused of acting for personal gain, but it was his session nonetheless. The chancellor was no doubt a member of his circle, and was acting to advance his interests."

"Rowan nodded along. That explained why the woman had been so insistent about Duke Antoine, and perhaps why the priestess had dismissed the idea. It was some type of power play. But, something about it didn’t add up."

ro "But, why though? I know the Duke passably well. The man has...many faults, but he was never the type to seek personal power."

"Doran just chuckled to himself."

dor "Nobles are nobles. They all just want personal power. But, Mistress is coming, yes? Soon they’ll all see the light!"

"Rowan didn’t answer the man. Just how badly had Jezera broken him? Still, not everything added up."

dor "Tonight, there will be the weekly ball. As a Duke, I’m entitled to attend. I do not know what Mistress wishes for you to do in that time, but…"

ro "No. You’re allowed to bring a bodyguard, right? If so, I’ll go with you. "

"Doran nodded softly. It was not in his nature to disagree." 
"As they walked towards the entryway, Rowan’s mind was free to wander. He thought about the last time he’d been to the palace."

scene black with fade
show rowan neutral behind black
show werden neutral behind black

"…"

werd "It must be done like this. There are rules to this world. Order. That is what we fought for. We bled for it. What is our victory if we would so readily abandon it?"

ro "But...but, after everything that I’ve done?"
ro "Don't..."

werd "You have done much. But, it must be this way. There is no future for you in Rastedel, Rowan Blackwell. Your service was exemplary. But, it is time for you to return home."
werd "Surely you have a homestead. A wife. You cannot stay here. There will be no knighthood waiting for you. I have made sure of it."
werd "Solansia makes a place for all of us. Solansia is good. It will all work out for the best."

ro "..."
ro "I was there when your brother himself died. I saved his men. I saved your son. How could-"

werd "So you did, Rowan."

ro "..."
ro "Solansia is good."

#throne room
scene bg34 with fade
show rowan necklace concerned at midright with dissolve
show doran beardless neutral at midleft with dissolve

ro "Go on ahead. I need a minute to myself."

hide doran with moveoutleft

"Doran went on by himself, leading Rowan standing in the doorway of the palace. He pressed his head against the side."

if avatar.corruption < 30 and serveChoice != 4:
    "A tear rolled down his cheek silently, and then another. He tried his best to keep it hidden, but Rowan had started to weep."
    
else:
    "Rowan balled his hands into a fist. Being here...seeing that man face to face...It all made his blood boil."


################################################################################################################################################
#Ball scene

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve
show doran beardless neutral at edgeleft with dissolve

"Later in the evening, Rowan and Doran returned to the palace for the ball. Outside the gates, the sound of music must have drawn beggars from the other side of the river. Knights in gleaming armor pushed them back from the gates with the flat sides of their pikes."

show rosarian knight neutral at midright with dissolve

rkn "Disperse. Disperse now."

"The threat seemed to do the trick. Famine was a far less certain killer than a pike."

hide rosarian knight with dissolve

"Doran didn’t seem to notice the disturbance, save for a shake of the head. Rowan watched the display wearily. He kept his distance though, less the starving beggars try to rally behind him."

#throne room BG
scene bg34 with fade
show rowan necklace neutral at edgeleft with dissolve
show doran beardless neutral at midleft with dissolve
show rosarian knight neutral at midright with dissolve

rkn "Do you have an invitation?"

hide rosarian knight with dissolve

"Rowan and Doran walked through the door of the palace into the long well lit entrance hall. Night had just fallen outside. Doran showed him a mark of office. Rowan meanwhile, slinked along behind him."
"Of course, Rowan’s normal leather garb was not much fit for an event like this, but since he was only coming as a guard, it was acceptable. Indeed, the sides of the hallway were lined with a surprising number of men at arms and mercenaries. The protectors of various high nobles."

dor "I must speak with some of my former acquaintances. Mistress has commanded me to make contacts for her." 

"Rowan nodded. He had his own explorations to make."

hide doran with dissolve

"The ball itself was being held in the throne room proper, which had been converted for the occasion. The rest of the palace was open, but essentially everyone of note was there. So Rowan made his way there, staying generally close to the wall not to draw too many eyes."
"None the less, he was stopped three times by nobles who simply wanted to ask him about his adventures. Rowan faked a smile and muddled his way past."
"Inside of the throne room itself, he found himself caught in a cloud of perfume and colour. The floor was packed. Tables at the side were lined with the powerful and their guards. The center of the floor was filled with men and women stiffly dancing in circular patterns."
"There was more splendor and luxury here then he’d ever seen. Even the post-war celebrations had been done in the aftermath of decades of hard times. But here there were jewels of all sorts everywhere."
"The tables were lined with foods. Expensive pastries made from specialty shops, expertly cooked fish, even dishes Rowan had never seen before that must have come from overseas. The fattest of the nobles parked themselves at the table and filled their faces."

if avatar.corruption > 30 or serveChoice == 4:
    "Rowan had to stop himself from glaring. Didn’t these pigs know there was a famine going on? Rowan was half tempted to grab food from the table to hand out to the beggars outside."
    "But, no. He was here on a mission."

else:
    "Rowan shook his head at all of this nonsense. The frivalities of the rich was not why he was here."
    
hide rowan with dissolve
show casimir neutral at midright with dissolve
show marianne neutral at edgeright with dissolve

"Of course, Rowan recognized some familiar faces here. Sitting in his usual spot on the throne was the Baron. He watched the proceedings with a glazed over expression. Occasionally he turned to Marianne, who was by his side."

hide casimir with dissolve
hide marianne with dissolve
show patricia sad at midright with dissolve

"The chancellor from before, Lady Crevette, was sitting at a table with a man who looked to be about her age. She was pouring wine into her mouth at a quantity that Rowan suspected was less than healthy."

hide patricia with dissolve
show werden neutral at midright with dissolve

"The Duke of Werden was also here, of course. Though, in his typical fashion, he kept near the wall speaking to some well clothed men. He was as far from the festivities in proximity as he was in expression. Best to avoid him."

hide werden with dissolve

"There were a few guests that he didn’t recognize that also stood out to him."
"For example, a great many people seemed to be gathered around tables on the right side of the hall. They were directly opposed to where Duke Werden was standing."

show jacques happy at midleft with dissolve

"At their center, laughing and schmoozing with relative ease, was a well dressed man whose most noted feature was that the top of his head was entirely bald. Despite that, he was still quite handsome."

show ameraine masked neutral at edgeright with dissolve

"As he observed the man, he also noticed the occasional glance in his direction from a woman wearing a ball mask sitting not far from the bald man. She was definitely, watching him. What little he could see of her skin was porcelain and her figure was slight, almost fragile looking."
"The mask was odd, but not too unusual at an event like this. Perhaps one in three guests had some sort of mask. But, it still made her gaze unnervingly inscrutable."

hide jacques with dissolve
hide ameraine with dissolve
show juliet neutral at midright with dissolve

"There was someone else looking at him, a pretty young girl with golden hair, who couldn’t hide the fact that every so often she was staring at him. She couldn’t have been older than eighteen and definitely could never have experienced a day of poverty in her life."
"If the reason behind the masked woman’s staring was a mystery, this girl’s stare couldn’t be easier to read. Two or three friends would seemingly tease her about it too. How often did young noble girls meet a hero in the flesh?"

if delane_status == "free":
    "And standing only a few feet from his mystery admirer was…"
    "Rowan blinked twice."
    "Long black hair that reached all the way down to her waist. A dress that showed off her keen fashion senses. A style of movement like the entire world belonged to her."
    show eleanor dress happy at edgeright with dissolve
    "It was Lady Eleanor Delane. A familiar face indeed."
    "The fact that she was here and looking so lively meant that she’d probably returned with no further troubles. Good."

else:
    pass
    
hide juliet with dissolve
hide eleanor with dissolve

$ casiConvo = False
$ patrConvo = False
$ jacqConvo = False
$ juliConvo = False
$ eleaConvo = False

label ballMenu:

#throne room cg
scene bg34 with fade

"In short, there were a number of possible figures that Rowan could possibly approach. Who might be valuable to make contact with?"

menu:
    "Baron Casimir and High Arbitron Marianne" if casiConvo == False:
        $ released_fix_rollback()
        show casimir neutral at midright with dissolve
        show marianne neutral at edgeright with dissolve
        show rowan necklace neutral at midleft with dissolve
        "Rowan made his way to the dais where the ruler of the realm watched the proceedings. Of course, there was always a crowd of sycophants waiting to speak with the Baron. Rowan waited his turn before approaching and sinking to one knee."
        ro "M’lord."
        casi "...Rowan."
        casi "Great deeds you’ve done. Great deeds. You are a model subject."
        "Rowan didn’t meet his eyes."
        ro "You are too kind."
        mari "Perhaps, perhaps not."
        "The priestess put a hand on his shoulder. They were perfectly soft. Perfectly warm."
        mari "The Goddess gives powerful gifts to those who believe in her. She chose you, Rowan. I have faith that she did so for reasons beyond any of our mortal comprehensions. I speak to her at times, and she illuminates my sight."
        ro "You are able to commune with Solansia herself? That must require powerful magic."
        "Marianne flashed a brief grin."
        mari "Indeed."
        casi "‘tis the source of her incredible wisdom. The knowledge of a mortal is nothing compared to heaven herself."
        "Marianne laughed, taking her perfect hand off of Rowan’s shoulder and placing it on the Baron. This was a different kind of touch. More familiar."
        mari "Now you really are being too kind, Casimir."
        "She turned back to Rowan."
        if avatar.corruption < 30:
            "A voice in Rowan’s head screamed at him that this was his opportunity. He could simply tell her about the pendant around his neck, right now. Perhaps she could free him with her own magics. He could be free of the hell that he’d been trapped in for so long."
            "But his voice was stayed. Even if he was here, Alexia was not."
        else:
            pass
        mari "I apologize for the ruckus of court earlier. I beg you forgive sweet lady Crevette despite her outbursts, I’m sure she only means the best for the realm."
        mari "We truly desire to do everything we can for your home. It will not be so long before the Royal Army is ready to march again. No doubt months at longest. Will you be alright out there in the meantime?"
        "Rowan blinked twice."
        ro "Alright out there?"
        mari "Of course. Surely you mean to return to the fight out west. I can scarce imagine what will happen without you there to sabotage the demons’ designs."
        mari "Truly it would be the easiest solution. For everyone. "
        show rowan necklace concerned at midleft with dissolve
        "There was something troubling about the way she said that. It almost seemed like it wasn’t a request."
        ro "Of course. I’ll be on my way back soon. I simply had to escort the Duke here. I will make personally sure to keep the citizenry safe while the royal army completes its other duties."
        show marianne happy at edgeright with dissolve
        mari "Excellent. I can rest much easier knowing that Solansia’s faithful have a shepherd in Rowan Blackwell."
        mari "But, feel free to visit me in the Grand Codifice. I am sure that we can come to some sort of arrangement that might be of aid."
        show rowan necklace neutral at midleft with dissolve
        "The Baron, meanwhile, appeared to have lost track of the conversation at some point. He was now staring out into the crowd of dancing nobles."
        ro "It was a pleasure to speak with you, M’lord. You bless me with your wisdom."
        casi "Oh yes. Oh yes. Of course. Carry on the good fight, carry on."
        if avatar.corruption < 30:
            "Rowan left the dais, feeling slightly deflated. Should he be happy or sad that the man tasked with keeping the Rosarian people safe was a puppet?"
        else:
            "Rowan left the dais feeling more confused than anything. What justice was there in a system where a dullard could be left in charge? Its destruction was only natural at this point."
        $ casiConvo = True
        jump ballMenu
        
    "Chancellor Patricia Crevette." if patrConvo == False:
        $ released_fix_rollback()
        show patricia sad at midright with dissolve
        show rowan necklace neutral at midleft with dissolve
        "Rowan approached the table where the Chancellor was sitting, along with the other man. His suspicions that he was her husband’s was only improved when he saw them both wearing the same pin. It featured the emblem of a crab."
        patr "Oh fuck...it’s you."
        "She was half slumped over in her chair now. The booze seemed to be getting to her. Rowan pulled up a chair."
        ro "Standing up to Marianne was a brave thing. Not many would have the strength of character to stand up to her."
        ro "And to bring support to my homeland as a cause no less. Thank you."
        "The drunk noblewoman rolled her eyes. "
        patr "I didn’t do it for you. Someone has to stick a thumb in that bitch's eye. Prancing around like she owns the whole damn region, just because she’s fucking the-"
        crev "Patricia!"
        "The man shot her a glance and then looked back at Rowan."
        crev "I’m so sorry about all this. It’s the wine talking."
        ro "Indeed. I’m sure your wife didn’t mean any of it."
        show patricia happy at midright with dissolve
        patr "Wife?"
        "She spat out a dark laugh."
        patr "I bet to you peasants we might all seem inbred. But, uh...don’t you think it would be a bit far to fuck my own brother?"
        $ crevName = "Lord Crevette"
        crev "I am Earl De Crevette of the Marble Shore. It is good to meet you, Hero Rowan. Everyone in my entire domain knows the tales of your bravery. This is my sister Patricia."
        "Rowan raised an eyebrow."
        ro "She still uses her maiden name? Unmarried?"
        patr "Thankfully too. A spouse will only get you into trouble."
        "Rowan thought darkly about that statement."
        ro "I take it then that you’re not a fan of the administration of the region then?" 
        show patricia sad at midright with dissolve
        "Lady Crevette swished the wine around in her goblet. Her brother put a concerned hand on her shoulder."
        patr "Who is?"
        "Rowan sensed an opportunity here. This woman was clearly dissatisfied with the situation here in the capital. That instantly made her a potential ally."
        if avatar.corruption > 30:
            "And though no longer in her prime, she still wasn’t bad looking either. If only her brother was not looking after her…"
        else:
            pass
        ro "If you were in charge, what would you do differently?"
        "She tilted her head."
        patr "If I were in charge…"
        patr "Heh. That’s a silly thought. I don’t know if something like that is even possible. We’ve got that pact with Prothea after all. They may call us an independent realm, but the holy city snaps and we bark. Like fucking bitches."
        ro "I see."
        patr "Look to Duke Werden though. I mean. I mean. I don’t know about in charge. But, none of this shit would have happened if we’d listened to him. We coulda made shit right after the war. Shoulda listened."
        "Her brother nodded along to the sentiment. It seemed a loyalty to the man was something they shared."
        "Still, drunk or not, the very prospect she was on Werden’s side meant trouble. Perhaps she was less of a natural ally then he’d hoped."
        ro "I see. This has been very illuminating. I look forward to speaking to you again, should I have the chance."
        "Her eyes drooped slightly."
        patr "Yeah, don’t count on it. So long as Marianne has this place by the balls, I doubt we’ll be seeing much of each other again."
        crev "You really shouldn’t have said so much…"
        patr "Please. Who cares if this gets back to her? He ain’t the first person I’ve said this shit too. Let him gossip."
        ro "Your secrets are safe with me, my lady."
        patr "See?"
        "Rowan stood up and departed from the table. That had been...productive..."
        $ patrConvo = True
        jump ballMenu
        
    "The Bald Man." if jacqConvo == False:
        $ released_fix_rollback()
        show jacques happy at midright with dissolve
        show rowan necklace neutral at midleft with dissolve
        "Rowan approached the table where the unusually large group had gathered. He had to dodge his way through quite a few dancing couples in order to do so."
        "By the time he arrived, he noticed that the masked woman who had been watching him was no longer there. He scanned the room, but couldn’t find a trace of her. The point was moot. She was not the person he wanted to speak to most."
        "When he saw Rowan approach, the bald man rose to his feet and extended a hand."
        jacq "Jacques Mineur."
        "Rowan shook it."
        ro "Rowan Blackwell."
        jacq "I assumed as much. Your presence is the talk of the town. If not your wardrobe."
        "Rowan paused to consider this. He’d never heard of the Mineur family. Yet, clearly this guy seemed to have quite the entourage. Though, Rowan’s deliberations proved quite predictable to the other man."
        jacq "Wonder who me and my friends are, huh?"
        ro "I will admit, I’ve never heard of house Mineur before."
        jacq "Few have. But, it would be a mistake to judge a man’s ability on his ancestors. If anyone proves that fact, it’s Rowan Blackwell."
        "Rowan nodded. Very few of the people sitting around seemed to have any kind of recognizable sign of heraldry. Though their clothing did sure look expensive. Most wore gold or jewelry."
        "Though strangely, the most common color he saw among them was actually copper. It seemed everyone of them had clothes in that color."
        jacq "I was in the crowd during your audience today. It sure was something, huh?"
        ro "Indeed. Are you friends with Duke Werden?"
        "Jacques chuckles, and glanced across the room towards the Duke."
        jacq "I wouldn’t say that. I wouldn’t say that at all. We have quite the history of disagreeing with each other. I’m not the only one with something like that, huh?"
        jacq "But, I do agree with him on occasion. For one thing, you wouldn’t believe my disappointment about how this morning went. You weren’t the only one hoping to retake your friend’s keep."
        jacq "In truth, after everyone left, I went back to Marianne. I have some friends among the bankers. It wouldn’t be too difficult to supplement what’s standing of the regular army with sellswords. And that approach wouldn’t empower your friend Werden."
        "Jacques shook his head."
        jacq "Didn’t matter. She still refused."
        "Rowan considered the man’s words. The fact that he never stopped smiling unnerved Rowan. He had a salesman’s demeanor. A good salesman too. Still, it seemed like this man ran a powerful clique. Perhaps one of the key factions of Rastedel."
        "Perhaps even a possible ally."
        ro "I see. That was most kind of you."
        "Jacques gave him a pat on the back. Rowan recoiled slightly from the proximity."
        #todo: track gay sex
            #"Though, even as he did, he felt a slight jolt. This man was attractive and knew it. For some reason, Rowan got the sense that he was not the sort inclined to chaste virtue."
        jacq "Think nothing of it, Rowan. I just want you to remember that even among the nobility, we aren’t all like Werden. You’ve got real friends here. People whose lives you’ve saved and their sons."
        jacq "Friends who understand the value of merit."
        ro "That is...something to keep in mind. I thank you, my lord, for your offers of friendship."
        jacq "No “my lord” bullcrap. I’m sure you have to do it enough when in a city like this."
        "Rowan nodded. The two talked for a small time afterwards, though before Rowan had a chance to ask him more about the political situation, a group of people arrived to speak with him."
        "The hero politely ended the conversation there, having gained an increased understanding of the political situation."
        $ jacqConvo = True
        jump ballMenu
        
    "The Blonde Girl." if juliConvo == False:
        $ released_fix_rollback()
        show juliet neutral at midright with dissolve
        show rowan necklace neutral at midleft with dissolve
        "Rowan imagined that the younger maiden shooting him looks was probably no political mover and shaker. But, she seemed eager to speak with him, and there was no point ignoring her. Rowan walked over to her and her friends."
        "When her friends saw him approach, they exchanged quick whispers and then scurried out of the way, leaving her alone with him."
        ro "Good evening, My Lady."
        juli "You must be Rowan! The Rowan! My name is Juliet. It’s a pleasure to meet you!"
        "Her voice was unsteady but excitable. Juliet could not yet be past her twentieth year. Her clothing struck of properness, though it was well ornamented. He immediately surmised that she was from the family of no lesser noble."
        juli "I suppose you caught me staring, didn’t you…?"
        show rowan necklace happy at midleft with dissolve
        "Rowan chuckled and gave her a reassuring smile."
        ro "I assure you, I did not think it too impolite."
        juli "Good. Good."
        "She brushed a strand of golden hair from in front of her eyes."
        juli "I had heard tales of your exploits. First hand accounts even. I did not believe that such a famous hero would be so…"
        "She suddenly blushed."
        juli "Oh goddess, you’re going to think this silly. But, I had assumed that a great hero would be more muscularly built."
        ro "I am sorry to have disappointed, My Lady."
        "Juliet looked mortified. Clearly, that had not come out the way she had meant it too. Perhaps even speaking to men was a new activity for her."
        juli "No! I didn’t mean it as an insult. I merely meant to say it was surprising."
        ro "That is quite alright. I knew what-"
        "Before, Rowan could finish, the two were joined by the sudden approach of another figure. One who towered over the smaller girl."
        show werden neutral at edgeright with dissolve
        show rowan necklace shock at midleft with dissolve
        werd "Rowan."
        "Juliet almost jumped in surprise at the approach."
        juli "Father? I was just speaking with him."
        werd "Indeed."
        "He put his hand on her shoulder and looked back towards Rowan."
        werd "This is my youngest, Juliet. I apologize if she displayed any rudeness."
        show rowan necklace neutral at midleft with dissolve
        "Rowan nodded. Of course. That explained it all. Her obvious wealth was because she was a Duke’s daughter. Furthermore, her mention of having heard tales of him made sense. Her brother Arthur had been at Karst."
        ro "Not at all, My Lord. She was asking curiously about my exploits. In truth, I came to her to speak."
        "Juliet shrunk a little bit. It was no doubt embarrassing to have your father interject in the middle of a conversation with a man you’d been staring at."
        juli "Father, I saw Adelaide grabbing a plate of food. May I join her?"
        werd "Of course."
        hide juliet with dissolve
        "She skipped along, shooting Rowan one last eager glance. Now he was left with only Duke Werden. Rowan inhaled sharply. He expected the Duke to question him now for once more leaving his allotted place. He steeled himself for it."
        werd "So you are back."
        ro "So I am. I kept my word. I returned to my village."
        werd "So you did…"
        werd "...Had only I kept mine."
        "The Duke turned, no longer facing him. Instead he looked at the hall."
        werd "Many mistakes have been made these past few years. You see it too, no doubt. That is why you are here."
        ro "I am not sure I follow."
        "The Duke looked at him impassionately. Rowan did not believe the man to be of no emotion. But, Rowan had certainly never seen him get worked up before."
        werd "I don’t believe you mean that."
        ro "What?"
        werd "Solansia’s order is complicated. This is a place you do not belong. But, you are here again. Something bad is about to happen. When it does, we will fight side by side once again."
        "Rowan was taken aback. Did Werden know that there was another Demon Lord war brewing? Perhaps he was just smart enough to know that something was wrong." 
        "Still, that did explain some of his insistence on immediate action."
        ro "I do not think it will come to that, My Lord. The event at Raeve Keep were a tragedy, but one that can be easily rectified. I am sure with your efforts, the orcs will be pushed back."
        ro "You do want me back in my village, sooner rather than later, I’m sure."
        werd "Hrmph."
        "He placed one hand on his sword hilt. It had a gleaming silver falcon in the pommel. The rumor, of course, was that the sword was magic. But, Rowan had never been close enough to see him wield it with his own eyes."
        werd "Disappointing."
        show rowan necklace angry at midleft with dissolve
        hide werden with moveoutright
        "Without a further word, the Duke walked off. This left Rowan to stew in his corner. He’d admitted that ensuring Rowan’s return home was a mistake. Yet, he blew right past it, as though the admission were meaningless."
        "But, before Rowan could get too lost in old resentments, his attention turned to what Werden had actually been saying."
        "He believed that the post-war political situation was unsustainable. He was making his moves with an eye towards protecting Rosaria. In short, he was acting directly against the Twins."
        if avatar.corruption < 30 or serveChoice !=4:
            "Fate was a strange thing. Rowan was the prisoner of demons. Yet, the person who might be most willing and capable of saving him...was the man most responsible for him being susceptible to this situation in the first place."
            "Rowan almost laughed. Almost."
        else:
            "That meant that the one person Rowan would need to defeat if the day came for him to take Rastedel, it would be, of all people, Duke Antoine."
            "Why was that idea so satisfying?"
        $ juliConvo = True
        jump ballMenu
        
    "Lady Delane." if eleaConvo == False and delane_status == "free":
        $ released_fix_rollback()
        show eleanor dress happy at midright with dissolve
        show rowan necklace happy at midleft with dissolve
        "Rowan slowly made his way over to where Lady Delane was standing. The moment she caught his approach, she smiled wide."
        if juliConvo == True:
            ele "I was waiting for you to come and speak to me. I’m sure the daughters of dukes come first for in-demand dirt generals. Though, I’m sure Juliet dear’s eagerness to speak to you put mine to shame."
            "Rowan laughed. The first words out of her mouth, and already she was spouting witticisms. This certainly was no imposter."
        else:
            pass
        ro "It is good to you in good health, My Lady. I had been concerned about you after you reached the keep. Though, I am sure you would not let a little matter of having just survived an ordeal slow you down."
        ele "Concerned about me?"
        ele "You are the one, who vanished into a puff of smoke. I asked around Rastedel for you, but no one had a word for your whereabouts. The Goddess above alone knows where you’re zig zagging now."
        "Rowan sighed. He had to be careful with her. Her cleverness, while at times refreshing, made her potentially quite dangerous to him. Her very presence in the capital was a threat to him with Jezera’s spies about."
        ro "Times are dire everywhere. I am sure you know that better than anyone. I can’t rest while the realm is on fire."
        show eleanor dress concerned at midright with dissolve
        ele "Indeed."
        "She hid her face behind her bangs."
        ele "Returning here has been quite strange. It’s so detached from...from everything out there. A gilded cradle."
        ele "Still, everyone needs to rest sometimes. Even Heroes of the realm."
        show eleanor dress aroused at midright with dissolve
        "She leaned up to his ear to whisper into it."
        ele "For the moment, I am staying at the Grand Camellia Lodge. If you wish for a bit of...rest. Pay me a visit."
        show rowan necklace aroused at midleft with dissolve
        "She backed away, leaving Rowan tracing the lingering ghost of her breath at his ear."
        ro "I will keep that in mind, My Lady."
        if eleanorCaveSex == True:
            #cave sex CG
            scene black with fade
            "As she walked away, Rowan had a flickering memory of that day in the cave. The sight of her naked body illuminated by the firelight. The way they had kept from being too loud, from fear of discovery. It had been a good night."
        else:
            pass
        $ eleaConvo = True
        jump ballMenu
        
    "Finished speaking.":
        $ released_fix_rollback()
        jump postBallConvo

        
label postBallConvo:

show rowan necklace neutral at midleft with dissolve
        
"Rowan sat alone near the back of the hall. In truth, he’d tired of this quite early on. The word games these nobles played grated on him. This noble was feuding with that noble for that reason. This noble wanted to marry his daughter to that noble, but she was really sleeping with someone else."
"It was endless."
"As he massaged his aching calves, someone approached him. He looked up in just in time, thanks to his reflexes."

show ameraine masked neutral at midright with dissolve

amer "Do you dance?"
        
ro "I cannot say, I do."

"He considered his reply further. What did this woman want with him?"

ro "Further, I am not quite dressed for the part. There aren’t many here dancing in leather armor. I understand my fame, but I’m only here about as a guard."

"The woman rolled her eyes under her mask."

amer "No, you’re not. You’re here to learn about Rastedel politics. Refusing me isn’t a good way to do that."
amer "Dance with me. No one will care how you’re dressed. You’re Rowan."

"Rowan tried to formulate a reply, but there really was nothing to say to that. She made a salient point."
"He rose to his feet, taking the woman by the hand and leading her to the dance floor. In truth, he’d never danced like this in his life. But, the moment they began, the woman took the lead. He might not be trained, but he could follow along with her movements."

#ballroom dance CG

ro "May I ask My Lady’s name."

"The woman twirled a lock of her straight onyx hair."

amer "There is nothing stopping you besides futility. Do you think the mask is just decoration?"
amer "Let’s talk of other things instead. You’ve spent the past day in court. You’ve seen the fracture points. You’ve even spoken to some of the players involved. I’m sure your friend Doran helped fill in the blanks."
amer "Find out anything interesting?"

"Just how long had this woman been keeping tabs on him? He might not be able to see her face, but he certainly didn’t remember anyone this pale from the audience earlier."
"The answer was obvious though. She likely had a friend who was there, or knew someone who knew someone. Gossip was a plague here."

ro "I was rather hoping that I’d be the one learning from you. You seem so wise, and I’m only a peasant."

amer "I can’t help you if I don’t know where you’re starting from."

ro "I see."

if jacqConvo == True:
    "It would be wise to be careful with his wording here. From what he saw this woman appeared aligned with Jacques. More to the point, he could already tell that she was quite a bit sharper than most of the others he’d spoken to."
    
else:
    "It would be wise to be careful with his wording here. From what he saw this woman appeared aligned with the bald man he'd seen earlier. More to the point, he could already tell that she was quite a bit sharper than most of the others he’d spoken too."

if casiConvo == True:
    ro "High Arbitron Marianne is a powerful force and has the Duke’s ear. She is far and away the person with the most influence on policy. She doesn’t much want me here, it seems."

else:
    pass
    
if patrConvo == True:
    ro "There exists an opposition party of real force. They tend to be centered around the nobility and are likely to have some of the bureaucratic and council jobs not taken up by the priesthood. I’m not sure what they want exactly."
    
else:
    pass
    
if juliConvo == True:
    ro "Duke Werden. He’s right in the thick of things. He was the one who organized the royal session today on the fly. He’s on some kind of mission, but I’m not sure what exactly."
    
else:
    pass
    
if jacqConvo == True:
    ro "There’s a coalition led by that man, Lord Mineur. He made several references to meritocracy and to friendship with the merchants. But, who he is and what he wants is a mystery to me."
    
else:
    pass
    
"The woman nodded along, swaying to the music and doing most of the hard work of helping Rowan keep up with the other dancers. The tempo changed and Rowan had almost tripped over his own feet."

ro "This is all quite a challenge."

amer "You don’t know the half of it, sweet."
amer "It seemed you picked up quite a bit. With enough time here, I’m sure you’ll pick it all up. Let me speed it up for you."
amer "You just gotta remember three colors. Blue, Purple, and Copper. The Blues are the easy one. Marianne wears blue. The other Prothean priests come in blue. There ain’t many of them, but the entire state is effectively at her command."
amer "But, her legitimacy is thin. She gets it all from the Baron and from the Goddess. Rumble on the street is that even the lay priests, the locals instead of the Protheans, don’t much like her. But, while she’s got the Baron’s ear and Solansia's, she can do no wrong."

ro "Do you like her?"

"The woman giggled. It seemed she would not be probed so easily."

amer "Perhaps. For all you know I could be a blue myself."
amer "You’ve also got the Purples. I’m sure you know the color of the Thorns of Solansia by now."

ro "Duke Antoine’s faction."

amer "He’s off on some idealist tangent of his. Perhaps he thinks demons seek to overrun the capital. Perhaps he thinks that they might already be in the capital."
amer "He has all of the high nobles not cowed by Marianne in his camp. Though, for those who aren’t our pious duke, I doubt that their motives are particularly altruistic. If you box up the High Arbitron’s power, someone has to fill in the void."
amer "But, Marianne has a handle on them for now. The Duke wouldn’t dare a destabilizing action unless he felt he had no choice."

if jacqConvo == True:
    ro "What about Jacques though?"
    
else:
    ro "What about the other man though?"
    
amer "The Coppers. My lovely friends. I’m sure you saw me sitting among them."

ro "I had noticed."

"There was a twinkle in the woman’s eye. She had been watching him of course. He was starting to suspect that this woman might actually be quite dangerous."

amer "In a society where the only ones making choices look like…"

"She glanced around."

amer "...this. There are always others who think they can do the job better."
amer "For now, the coppers are quite limited in their powers at court. But, then it is not titles that bring such delicious caviar to a venue like this. And there is much influence to be had when you can offer the merchants greater freedom and social advancement."

ro "So he doesn’t believe in Solansia’s hierarchy?"

"Rowan scrunched his brow. Such a thing would be quite chaotic. They might overturn the entire social order if they were not careful. The Twins would do well too…"

amer "And why shouldn’t he? You’re a testament to the failures of that hierarchy. All these great deeds being done by a commoner." 
amer "Saving Karst…"
amer "Defeating a Demon Lord…"

#ballroom CG #2
show rowan necklace angry at midleft with dissolve

amer "...And allowing a demon army into Raeve Keep…"

"Rowan half jumped, stepping on someone’s boot. A mustached noble gave him a dirty look."

ro "Excuse me."

amer "Keep dancing."
amer "I know all about what you’ve been up to of late, Rowan Blackwell."

if avatar.corruption > 30:
    amer "I wonder what the goddess must think of it all. Certainly she’d disapprove."

else:
    pass
    
amer "Your solo adventure up north. Your subsequent disappearance. Even some of what you’ve been up to since then."

if orciad_state == 2:
    amer "Your adventures at the Orc encampment were quite the sight to behold, one can only imagine. First you show up, and now they secretly pledge themselves to new masters."
    
else:
    pass
    
#todo: if goblin complete:
    #amer "And that quest of yours down to Blackholt. You must have been quite surprised to see how they’d react to a real hero in their midst."

#else:
    #pass


amer "Though, I must say I’m surprised that you agreed to serve the twins at all. I had thought you of all people would be resistant to their charms."

if rowanJezSex > 0 or rowanAndrasSex > 0:
    amer "I suppose they must be quite...Persuasive."
    
else:
    pass

"Rowan’s eyes narrowed. This woman was talking about things she shouldn’t be able to know about. Things that if she mentioned to other people might mean his death."

if all_actors['alexia'].flags['andras_influence'] > 0:
    amer "Alexia’s as well…"
    
else:
    pass

ro "Where did you hear about all that?"

"The woman chuckled softly to herself. To her this was all a game. Rowan was close enough that he could probably strangle her dead if he tried. But, surrounded by fellow nobles she was safe."

amer "You can’t even get a name out of me, and you think I’m going to just up and tell you how I know all of your little secrets? Let no one say you haven’t lost your optimism."

"Rowan lowered his voice and growled."

ro "You haven’t told anyone. If you had, I’d be dead."

amer "Perhaps one or two confidants. In case something were to happen to me, of course. But, no. I happen to think myself a good keeper of secrets."

ro "Then what do you want with me?"

amer "Can’t I just want to actually meet the man who’ve I’ve heard so much about these years?"

"Rowan gave her a harsh look."

amer "Not in the mood for games then. Very well. Let’s meet in private. I have other curiosities about you as well. We have general free roam of the palace tonight save for the guards. But, they should let you into the west hall if I ask them very nicely."
amer "Meet me there in half an hour."

"Then, just as suddenly and strangely as she approached him, she broke off from him. She actually left him standing in the middle of the dance hall, surrounded by twirling couples."

#show throneroom bg
#show rowan necklace angry at midleft
#show ameraine masked at midright

amer "An adieu for now, Rowan Blackwell."

hide ameraine with dissolve

"And then, with a surprising grace, she slid away. Rowan attempted to follow after her, but the woman was quite adept at hiding herself in this kind of environment."

ro "Fuck."

#######################################################################################################################

label amerainescene1:

scene bg35 with fade
show rowan necklace neutral at midleft with dissolve
show ameraine naked happy behind bg35

"Rowan walked into the west hall. True to the masked woman’s word, the guard had stood assign and let him past. But, all that he found inside was total darkness."
"He could make out the basic shape of the room. A series of interwoven rooms with their own frames all connected by a single main room. But inside it seemed to be empty. Devoid of light."

ro "Hello?"

"He walked further in. There was not a sound. Not even a trace of movement. Was she even here? Did she mean for him to wait for her?"

ro "Are you there?"

"He took another step in."
"Then a flash on his periphery. Something moved. A long graceful leg was all he saw the outline of and then darkness."
"Someone was definitely in here."
"Rowan kept a hand on the hilt of his sword, just in case it was anyone besides the woman. Or perhaps if it was the woman and she’d set a trap for him."
"He focused on his hearing. There would be little to see in here, but his ears were still sharp."
"Which is why it was so odd when he felt a hand brush against the back of his neck, without hearing so much as a foot step."
"Rowan spun around, but again there was no one there."

ro "I can leave, you know. I can grab a lamp from outside. Bring yourself close so I can see you."

"He spun around again. Another sound behind him. This one was further away. It was light, almost like a single drop of water landing on the ground. Eerie. Unnatural."

amer "Why don’t you come over to me."

"The noblewoman’s voice. It almost sounded like a purr. Rowan relaxed slightly. It wasn’t an ambush. But, how was she doing that?"
"Her voice seemed like it was coming from the section the opposite way from how he came in. Rowan began to cautiously step in that direction. His sword still never left its sword hilt."
"He walked through the doorway of the room. And what he saw amazed him."
"The room itself was mostly pure darkness. There was only one source of light, and that was a small glass skylight on the ceiling. It left a small circle of moonlight that was the sole illuminated part of the room."

#cg1
scene black with fade
show rowan necklace neutral behind black
show ameraine naked happy behind black
pause 3

"And sitting in the middle of it was the masked woman. Naked."

amer "Rowan…"

"Rowan recoiled in shock. What was her intention here?"

amer "I said I’ve heard a great deal about you. Do you think I would not have heard of your exploits? Your conquests?"

"Rowan allowed himself to peak at the woman. Her skin, so porcelain as to almost be white. As to almost be the moon itself. It was impossible. It was stunning."
"His eyes swept over her lithe form. How did she develop such a slight build. There was a sensual grace to her thin frame."

amer "I want my own taste, Rowan."
amer "Come to me, and I will tell you what you want to know."

menu:
    "Go to her.":
        $ released_fix_rollback()
        $ amerFirstSex = True
        "Rowan took a step forward. This was a situation that had grown increasingly common to Rowan’s life. Everyone was fucking someone, or seducing someone. That the woman asking him to fuck her was willing alone was a positive. Willing and radiant."
        ro "You are no succubus? I can trust you?"
        "She smiled wide under her own mask."
        amer "Not a succubus. This is not a trap. If I wanted to hurt you, I’d do it another way."
        "Rowan took another step closer to her, throwing off his shirt and lowering his pants."
        if avatar.corruption < 30:
            "This was all strictly a matter of necessity. This woman was far and away the most informed in all of Rastedel. This was all politics. The strange ephemeral beauty didn’t hurt either."
        else:
            "Rowan could have said that he was doing this just for the sake of the mission. He could have said it was to get in close with a valuable contact. But, that was a lie and he knew it."
            "He wanted to fuck this strange shimmering beauty. He wanted his cock inside of her."
        "Rowan sunk down to his knees, now naked and cock erect. The two sat on the ground, mere inches from one another. His breath was heavy. Now he too was illuminated by the moonlight. Though his skin didn’t shine in it like her."
        amer "Wonderful. Simply wonderful."
        #cg2
        scene cg295 with fade
        pause 3
        "The pale lady lifted herself up and lowered herself on top of him. She wasn’t heavy. But all the same, she was easily capable of pressing her pussy down on to him. She rolled her head back and let out a pleased gasp as she was filled."
        scene cg296 with fade
        pause 3
        "Rowan wrapped his arms around her waist to hold her steady. She seemed to have the same idea, because she dug her long nails into his shoulder. He winced from the pain, but the sensation was lost amidst the pleasure."
        scene cg297 with fade
        show ameraine naked happy behind cg297
        pause 3        
        "Rowan rolled his hips upwards into her. She leaned her face down to his ear."
        amer "We’re all alone here. Fuck me like I’m the only one else in the world."
        scene cg298 with fade
        pause 3       
        "So he did." 
        "The silence of the room was pierced by the slap of body on body and the moans that came with it. Breathless eager noises."
        scene cg299 with fade
        show rowan necklace naked behind cg299
        show ameraine naked happy behind cg299
        pause 3
        "His hands clenched her body, gripping it like a vice. Her nails dug into him. A little bit of blood dripped down his shoulder, but he didn’t even notice. There were other sensations overcoming it."
        "The softness of her body, the tightness of her insides, and the friction of it as it moved."
        amer "Yes. Dark one, yes. Fuck yes."
        "Her words were lost on him. She could have said whatever and it wouldn’t have elicited more than a gasp. He spoke one language and it was the language of the flesh."
        "The moonlight now sparkled on the sweat that dripped down his back. It was beautiful and ephemeral. Almost like the moonlit motion of their forms against the darkness."
        ro "I can’t hold it...I can’t…"
        show cg299 with sshake
        show cg299 with sshake
        show cg300 with flash
        pause 3
        "Rowan burst. A shot of pleasure went through him like a spike of energy, and he leaned back. Hot cum went inside of her. As his dick plopped out, it was leaking from her pussy."
        scene bg35 with fade
        show rowan necklace naked at midleft with dissolve
        show ameraine naked happy at midright with dissolve
        "The woman rolled backwards, giving Rowan some space to recover. For example, now was the first time he’d noticed what her severe nails had done to his shoulder."
        ro "That might need bandaging..."
        "She gave a breathless laugh."
        amer "Surely the worst wound you’ve received in the field."
        "Rowan looked down to the side. As the high faded he was starting to remember why he’d come here in the first place."
        "Rowan placed a hand on his forehead."
        ro "Who are you? How do you know what I’ve been doing? How do you know about the twins?"
        "She stretched out and twisted her back. It was a strange motion. Almost like a cat uncurling itself after waking from a nap."
        amer "Well, you have fulfilled your end of our little arrangement..."
        jump amerPostSex
        
    "Refuse, but demand answers.":
        $ released_fix_rollback()
        $ amerFirstSex = False
        "Rowan shook his head. There was something mistifying about her form, even in the moonlight. But, he was not here to fuck this woman. He was here to get answers. She was clearly playing a game with him."
        scene black with fade
        show rowan necklace neutral at midleft with dissolve
        show ameraine naked neutral at midright with dissolve
        ro "I’m not going to fuck you. I don’t trust you."
        amer "That would be awfully disappointing."
        "Her face strained underneath the mask. She even parted her legs slightly. It wouldn’t matter though. Rowan had already made up his mind."
        amer "Perhaps, I should speak to my friend Marianne about my disappointments. They might fascinate her. One sexually active woman to another."
        "Rowan sat down. He was already tired of this."
        ro "I don’t believe you. If you told the High Arbitron everything you knew about the hero of Rosaria, the entire realm would be turned upside down. You might do that. But, I don’t believe for a second, that you’d base that choice on whether or not I fuck you."
        #ameraine bemused
        amer "I suppose I wouldn’t do that now, would I?"
        "She turned her back to him. Now all he could see was the outline of her straight jet black hair and the gentle curve of her back. Even that was somewhat...stirring."
        amer "I must admit, I do not know if that answer makes me less interested in you…"
        amer "...Or more."
        "Rowan waited. He didn’t have much to say in response to that."
        amer "Very well. You followed me for answers. I don’t recall telling you that you’d need to fuck me for them."
        
label amerPostSex:

$ amerName = "Ameraine"

amer "My name is Ameraine. It would be Lady Ameraine to a commoner, though."

if society_type == "feudal":
    amer "Though, I suppose you’re not truly a commoner anymore."
    
else:
    pass
    
"Rowan sighed. It was a name he’d never heard of. But, that was too be expected. Rowan didn’t know most of the nobility off the top of his head. Especially not those from outside his own home duchy."

ro "It is good to meet you then, Lady Ameraine. "

amer "As for how I know who you are…"

"The woman paused to chew over her words."

amer "I suppose you were ordered by Jezera to come and find a potential “ally”, is that correct?"

"Rowan nodded softly, even if he didn’t expect her to see him when he was outside of the small cone of light created by the moon."

ro "She did."

amer "Well, I am the ally. Me and Jezera have had something of a correspondence for some time now. Before you came, I asked to meet you. I also mentioned it was important to me for you to be seen coming into the city. Thus your mission."

"She chuckled. Apparently to her this revelation was great fun."

amer "I asked her not to tell you, of course. If you’d known you were coming at my behest, then I wouldn’t have got to see your investigation in progress. Besides, you were far more useful to me blundering around blind then had you actually known."

"Rowan chewed over her words. Much of it made sense. Furthermore, if she was lying, he’d only have to ask his Mistress. Still, he couldn’t say he had a full view of the situation. After all, his arrival had seemingly benefitted Werden most. But, she said she was aligned with the Coppers."

ro "Why though? What did you hope to gain with my arrival?"

amer "Why does anyone on our side of this little conflict do anything? It was for the chaos. Because you came, there is more pressure for everyone to act. I like pressure."

"Rowan nodded. That too made some sense. Though, the  danger of such a play was apparent to him. Making the enemy more proactive was rarely sound strategy."

amer "I believe, that should satisfy the terms of our arrangement. And the terms of your mission."
amer "Please give my regards to Jezera. Take that to mean whatever you wish."

"Ameraine rose to her feet. Her hair swayed softly. Rowan rose, attempting to stop her departure. He still had questions. About the capital. About her. About whatever plan the two women were hatching. But, then Ameraine walked out of the area illuminated by the skylight."

hide ameraine with dissolve

"When Rowan went to chase after her, he found it strangely difficult. She didn’t make much noise as she walked. He ran to the spot where he thought she’d be, and felt nothing."
"Ameraine was gone." 
"Outside of the hall, he heard the shuffling of feet and the chatter of a crowd moving. It seemed that the ball had come to an end. There was no point staying in this room. Rowan straightened out his outfit and headed out to join the moving crowd."

$ palaceStage = 2
$ palace2Repeat = False
$ rastLodgeAccess = True

jump rastMenu

#################################################################################################################################################################

label palaceRepeatVisit:

if palace2Repeat == False:
    scene bg34 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan went up to the palace to see what information he could collect about the current political situation. After all, he may have completed his mission, but it wasn’t like there wasn’t more to discover. Perhaps he might even bump into Lady Ameraine."
    "He ran into someone else instead."
    show werden neutral at midright with dissolve
    werd "Rowan."
    "Rowan went down to one knee at once."
    ro "My lord."
    werd "Hrmm."
    werd "I expected you in the field."
    "He rose back to his feet. The kneel had lasted exactly as long as was polite and not a second longer."
    ro "I returned to speak with some friends of mine. I also wished to see how my liege lord, Duke Raeve, was fairing."
    werd "To be sure."
    "He brushed past Rowan, to continue the way he was going. It was not rude. Merely disinterested."
    hide werden with moveoutleft
    "Rowan continued his exploration of the palace, but otherwise found few familiar faces. The Baron was around, of course, but he was in his private chambers doing...whatever it was that he does. With a sigh, Rowan left the palace. Not much had been gained in the effort."
    $ palace2Repeat = True
    jump rastMenu
    

else:
    scene bg34 with fade
    show rowan necklace neutral at midleft with dissolve
    "Rowan spent some time roaming the palace. It seemed there was not much activity going on through. The palace guard didn’t even seem particularly out in force. Rowan scratched his head at how easy it was to sneak around the building."
    "However, he found nothing of particular value. It seemed to be a waste of time."
    jump rastMenu







