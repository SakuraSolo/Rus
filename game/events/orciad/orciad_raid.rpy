

label hunt_for_gits:

if delane_gifts > 39:
    scene bg26 with fade
    "As always, Rowan headed to where Kraug and his orcs gathered. But this time, only a single orc awaited him."
    show rowan necklace neutral at midleft with dissolve
    show wild orc neutral at edgeright with dissolve
    wo "Chief sayz Delane happy with ‘er gifts. No more raidz."
    ro "Hm."
    "He should've foreseen this. Unlike Batri, Ulcro didn't raid for fun. He had a clear objective in mind, and now that it was accomplished, he wouldn't risk his best men on further risky ventures." 
    "Once the leadership struggle was resolved, Rowan would probably be able to go regular raids with the other orcs, if it was something he was interested in."  
    $ giftHuntAvailable = False
    jump campMenu

else:

    if giftHuntFirst == True:
        
        scene bg26 with fade
        "Ulcro promised him a raiding party, and Rowan would be a fool not to use it. Expensive gifts weren’t that easy to acquire."
        if jezDelaneHelp == "get":
            "Now that he thought of it, Jezera might have some old jewelry she might be willing to part with... If she was feeling generous, and if the stars aligned. Her help usually came at a price, but it would be the quickest way to get something good for Delane."
        else:
            pass
        if cliohnaDelaneHelp == "get":
            "The library had a section dedicated to Rosaria nobility which Delane might find interesting.  He should ask Cliohna if some of the tomes weren't essential to her research."
        else:
            pass
        "For now, it was best if he made use of Ulcro's men."
        show rowan necklace neutral at edgeleft with dissolve
        show wild orc neutral at center with dissolve
        show orc soldier neutral at center with dissolve
        "The raiding party waited for him at the edge of the camp. Twenty veteran orcs, long time soldiers, some of which old enough to have fought under Karnas. They were led by a massive orc named Kraug, and would be Rowan's company for the upcoming days."
        ro "The central and eastern regions of Rosaria are too unstable for us to find any high-value targets. The western lands will yield better loot."
        "Kraug nodded in silence. While he was technically their leader, Rowan was to act as the tracker of the party." 
        "It was up to him to him to locate targets suitable for their objective." 
        ro "Let’s go. We have a long road ahead of us."
        scene black with fade
        "..."
        $ giftHuntFirst = False
        jump giftRaidProper
        
    else:
        scene bg26 with fade
        "Once again, Rowan met with Kraug’s raiding party. As always, his men were ready to depart at a moment's notice."  
        scene black with fade
        "It was time to go get Delane her gifts."
        "..."
        jump gift_Raid_Travel
        
label gift_Raid_Travel:

if giftRaidTravel == 1:
    scene bg3 with fade
    "It was day three of their little escapade west."
    "With this being their second raid, Rowan found, much to his own surprise, that Kraug and his men were growing on him. They were disciplined. Quiet. Organized." 
    "Everything his own orcs were not." 
    "Most likely, this would not be their last raid, and there was no reason to continue keeping his guard up. He should use this time more constructively." 
    "He could try to break ice between him and the silent leader of the party, Kraug. Once Ulcro pledges his tribe to castle Bloodmeen, his officers will become important figures in the twin's army. Knowing their strengths and weaknesses could be of great benefit to him in the future." 
    "Alternatively, he could spend the time training. Months of captivity took their toll on him - he knew he was not as strong as he was in the past. The orcs would make for good sparring partners." 
    menu:
        "Get to know Kraug.":
            $ released_fix_rollback()
            $ knowKraug = True
            "His decision made, he approached the veteran soldier during their next stop."
            "An orc of few words, Kraug wasn't too keen on engaging him, but after a couple of prodding questions, Rowan got him to open up a little." 
            "He had his own warband, once. Raided in the valley north of Rosaria, with a small group of companions, never larger than three dozens of men."  
            "This did not surprise Rowan, as many orcs had their own small tribes, before a strong chief located them and decided they would become part of their group." 
            "But Kraug, apparently, sought Ulcro of his own accord. The old warchief had something he wanted."
            show rowan necklace neutral behind bg3
            ro "And what was that?"
            krau "Strength."
            "... Guess he shouldn't expect much more from an orc."
            "He wanted to drill Kraug on the subject more, but to the large orc the topic must have been particularly sensitive, since he wouldn't engage him any further." 
            "They would have to continue this another time." 
            $ giftRaidTravel = 2
            jump giftRaidProper
            
        "Practice combat.":
            $ released_fix_rollback()
            $ giftHuntTraining = True
            "On their next stop, once the camp was set, Rowan approached some of the orcs that struck him as the reasonable kind." 
            "He explained his malady to them - that his form has atrophied over the months and that he needed some reliable training partners to regain it."  
            "The orcs shrugged. For them, it was as good of a way to pass the time as any." 
            "From now on, Rowan adopted a strict regimen of practice every evening, focusing on his footwork and blade mastery, against both a single and multiple opponents." 
            "The orcs proved to be competent partners. Like many of their kind, they favoured offense and overwhelming the enemy with powerful attacks, but Ulcro's men learned not to rely on their physical superiority alone." 
            "Unable to fall back to this usual tricks, Rowan found the sparring sessions worthwhile, though it would take some time to see tangible results." 
            $ add_exp(5)
            $ giftRaidTravel = 2
            jump giftRaidProper
            
elif giftRaidTravel == 2:
    scene bg31 with fade
    
    if knowKraug == True:
        "Again, they ventured west. And again, Rowan took the time to try and befriend the massive orc." 
        "Sharing some ale over the campfire, Rowan tried to pry more information from Kraug. One topic in particular weighted on his mind, as it surely did on everyone's else."  
        "Did Ulcro stand a chance against Batri?"
        "To that the answer was a collective, if somewhat unenthusiastic, 'yes', coming from both Kraug and the rest of Ulcro's men. The warchief was an old, experienced fighter. Batri might was a rising star, but in the eyes of many, it was too early for him to take over the tribe." 
        "But apparently, if Batri were to win the upcoming bout, they would have no issue following him."
        show rowan necklace neutral behind bg31
        krau "Ancient right. Tha strongest leads. Tha rest follows."
        ro "Wouldn't you seek revenge over Ulcro's death? Or try to become warchief yourself?"
        "While there was no doubt the two chiefs were the strongest of the camp orcs, they were many of comparable prowess, serving as lieutenants and aides. Kraug would be one of them." 
        "But the large orc growled angrily and shook his head."  
        krau "No. No point. Everyone tired of dis."
        krau "Entire fight a mess. Want nothin' to do wit' it."
        krau "Enough headache wit' Tarish around, stirrin' trouble."
        krau "... As yous know. "
        "The orc narrowed his small eyes at him. Perhaps it was a mistake to accept Tarish invitation when he first entered the camp with Andras. It cast a shade on everything he did now."
        show rowan necklace angry behind bg31
        ro "My loyalty is with Ulcro. Do you doubt this?"
        krau "..."
        "The atmosphere turned sour quickly. Rowan would get nothing more from the orc this trip."
        $ giftRaidTravel = 3
        jump giftRaidProper
        
    else:
        "Once more on the trail with the orcs, Rowan resumed his training regimen." 
        "This time, his main sparring partner was a sly-looking orc named Vorg. Shorter and thinner than most of his comrades, he fought with two short blades and wore light, leather armor."
        "There was something stereotypically dishonest about him, from the dirty fighting style to the devious smirk he always had when he thought nobody was looking."  
        "Rowan labeled him 'Most likely to stab someone in the back', and quite honestly felt the other orcs shared his opinion here." 
        "Regardless, practice was practice. Though he made a mental note to never turn his back to the orc."   
        $ add_exp(5)
        $ giftRaidTravel = 3
        jump giftRaidProper
        
elif giftRaidTravel == 3:
    scene bg31 with fade
    if knowKraug == True:
        "Their fourth raiding escapade. How many more, Rowan wondered, as they set camp for the evening." 
        "He saw Kraug nearby, preparing the campfire. Their last talk ended on a low note, but after all their adventures, the hero felt like they shared at least some camaraderie." 
        "Enough of it, to ask perhaps the most divisive question one could ask in the camp."  
        "What did Kraug think of Ulcro's infatuation with Delane?" 
        "To most orcs, it must have appeared bizarre. Many thought Ulcro was just being possessive of her. If they knew the real reason for action, he would no doubt be mocked for it."
        "Never to his face, obviously, but quietly, discreetly, over a pint of ale and among trusted allies."
        "Rowan expected Kraug to either dodge the question or provide some noncommital answer. But instead, the orc looked him deep in the eyes, and spoke up in a low, growling tone." 
        show rowan necklace neutral behind bg31
        krau "I 'ad a mate, once, Rowan. Long time ago."
        "In the half-dark of the evening, Rowan saw the orc gritting his teeth."
        krau "Long white hair. Like a winter spirit."
        krau "Made good stew."
        krau "…"
        krau "'ad a kid on tha way. "
        "His expression softened, for just a moment-"
        krau "Wasn't supposed to be 'er mate. Lost tha duel over 'er. "
        krau "But she liked me. Liked my spirit."
        krau "Chose me over the other."
        "-only to turn into a hateful scowl."
        krau "And humi killed her."
        "The orc stared into the campfire, its flames dancing lazily in the dark."
        "Anger and hate, carefully tended to for years. A desire for revenge so strong, it would not be quenched by the passing of time."
        show rowan necklace angry behind bg31
        ro "... You don't really care for Ulcro, do you?"
        "He bared his teeth, in a mockery of a smile."
        krau "No. "
        krau "But he will deliver us to ya master. To tha Red Demon."
        krau "And dat is enough for me."
        
        if serveChoice == 4:
            "Ulcro might have been one of the few orcs who could move past his rage, and desire something more from life than war and violence." 
            "But his soldiers weren't like that. All they wanted was vengeance. Blood. Murder and rape." 
            "Not that it mattered. They were tools, nothing more."  
            show rowan necklace happy behind bg31
            ro "Do not worry. Andras will make sure you see action." 
            krau "Good."
            "Beasts like him also had their uses."
            
        else:
            "Rowan said nothing. Orcs like Ulcro proved that even creatures of chaos were capable of growing beyond their instinct." 
            "But many more were still driven by hate and desire for violence." 
            "He could only hope he would be able to do something to prevent them from setting the world ablaze." 
        
        show rowan necklace concerned behind bg31
        krau "Enough talk."
        krau "These hunts take too long. From now on, focus on lookin' for a target."
        ro "Agreed."
        "He doubted he would get much more from him. It was best to wrap up this hunting business, and move on to the next target."
        $ kraugCommander = True
        $ giftRaidTravel = 5
        jump giftRaidProper
        
    else:
        "Their fourth raiding escapade. Despite himself, Rowan couldn't help but start to genuinely like some of the orcs that made their small group. They found him amicable as well, and some of them were starting to treat him less like unwanted weight, and more like a worthy companion."  
        "One of them even offered him tips on his usual castle workout routine. Given the discrepancy between his and the orcs stamina, Rowan was reasonably certain that following his full regime would literally kill him, but there was some sound advice here and there." 
        "And thanks to their regular sparrings, Rowan already felt himself growing stronger. He was looking forward to their future training sessions." 
        "But they would not be." 
        krau "Rowan, dis is taking too long"
        krau "Stop wasting time. Focus on findin' a good target."
        "It has been a month, and Kraug was getting impatient. As much as Rowan wanted to use this time to hone his skills, he shouldn't be pushing his luck here." 
        "The training he had so far will have to suffice. It was time to wrap this up." 
        $ add_exp(100)
        $ giftRaidTravel = 5
        jump giftRaidProper


else:
    jump giftRaidProper


label giftRaidProper:

if check_skill(12, 'survival')[0]:
    jump giftEventSelection
    
else:
    jump giftHuntFailed
    

label giftEventSelection:

$ res_roll = dice(20)

if res_roll < 15:
    
    $ res_roll = dice(3)
    
    if res_roll == 1:
    
        if meetingBanditsSeen == False:
            jump meetingBandits
        else:
            jump giftEventSelection
    
    if res_roll == 2:
        if findingMonksSeen == False:
            jump findingMonks
        else:
            jump giftEventSelection
    
    if res_roll == 3:
        if findingCaravanSeen == False:
            jump findingCaravan
        else:
            jump giftEventSelection
            
else:
    $ res_roll = dice(2)

    if res_roll == 1:
    
        if noblesHuntingSeen == False:
            jump noblesHunting
        else:
            jump giftEventSelection
    
    if res_roll == 2:
        if summerResidenceSeen == False:
            jump summerResidence
        else:
            jump giftEventSelection

                                             
label giftHuntFailed:
scene bg31 with fade

"Despite Rowan’s best attempts, the group failed to locate a suitable raid target."  
"The hero expected Kraug to blame him for wasting their time, but when he told the orc they had to cut this hunt short, he took the news in stride." 

krau "Understandable. Try next week."
            
"He would have to do just that."

return

label meetingBandits:

scene bg31 with fade

"Rowan didn’t find what he was looking for, but he would take whatever he could."
"In the north-west, they stumbled upon a group of bandits. After customary insults and threats were exchanged, the group proved to be willing to parley."
"Having connections in nearby cities, they proposed a trade – females slaves for gifts."
"Kraug approved it swiftly, never asking Rowan for his opinion. Getting Delane to accept Ulcro was, at the moment, top priority, and no price was too high to pay." 

$ delane_gifts += 5
$ meetingBanditsSeen = True
return


label findingMonks:

scene bg31 with fade

"With the twins orcs largely plaguing central and east Rosaria, the western regions saw far more trade, and more travelers."  
"A pair of monks, en route to one of the nearby abbeys, ended up as their target. Accompanied by a holy knight and his squire, they wouldn’t be bothered by most bandits. They had nothing of value on them."
"Except for books."
"The orcs made short work of them, adding “Crop fertilization”, “Hymns to Solansia”, “Faith Everlasting”, and “The Annals of Western Dynasties” to Delane’s library."
"Maybe not the most fascinating collection, but at least it was something."

$ delane_gifts += 5
$ findingMonksSeen = True
return

label findingCaravan:

scene bg31 with fade

"When traveling on his, Rowan would sometimes pass caravans and merchant. But he rarely got the opportunity to send orcs to intercept them."
"Simple matter of logistics – if they weren’t heading in the direction of one of the portals, his orcs wouldn't be able to catch them on time."
"But now that he was moving with a proper raiding band behind his back…"
"The merchant caravan he managed to track down consisted of three carts, and over a dozen mercenaries. A difficult target, for most bandit groups."
"Kraug told him he was to sit tight and readied his men. Rowan tried to protest, but the orc would have none of it. His group has trained together for a while now. The knew how to work together - Rowan would just get in the way." 
"He would deal with the caravan."

show rowan necklace neutral at center with dissolve

"Rowan watched from a safe distance, as the orcs set up the ambush, and executed it as soon as the merchants were in the right position." 
"The unfolding fight was a bit disconcerting to watch." 
"Rowan was used to orcs displaying moderate competence at best, and complete lack of it at worst. But these… These were Ulcro’s elite men. Orcs he trusted with securing gifts for his beloved Delane."
"They were disciplined. They were quiet. And they were ruthless."
"The slaughtered the mercenaries with little difficulty." 
"Rowan doubted either Batri or Tarish really understood what “excellence” meant in a soldier."

if serveChoice == 4:
    show rowan necklace happy at center with dissolve
    "He backed the right horse."
    
else:
    show rowan necklace concerned at center with dissolve
    "He was giving the twins a dangerous ally. "

show rowan necklace neutral at center with dissolve

"Once the battle was over, Rowan moved in to inspect the caravan’s cargo."

krau "Hrm. Raw materials."

ro "It would seem so."

"Iron bars. Grain. Seeds. Stuff that would be useful for Castle Bloodmeen, but nothing Delane would appreciate."
"Except for..." 

ro "Fabrics."

"Three bales of expensive fabrics, perfect for decorating Delane’s tent."
"After short negotiations, Kraug agreed to leave most of the construction materials to Rowan, while they took the fabrics and some of the gold hidden inside the cart compartments." 
"This ought to help with the restoration project."

$ change_treasury(+80)
$ delane_gifts += 10
$ findingCaravanSeen = True
return

label noblesHunting:

scene bg3 with fade

"Having ventured far to the west, Rowan lead the orcs to what he knew was noble hunting grounds." 
"Luck smiled on them. Incredible luck, to boot."
"On their third day scouring the area, Rowan finally found what he was looking for. A hunting party, consisting of a pair of young noble lords, four knights, and two ladies, likely being courted."
"One of whom had a figure similar to Delane’s."

show rowan necklace neutral at midleft with moveinleft

krau "What’s tha plan?"

ro "Hmm..."

"They couldn’t exactly take their clothes from their dead bodies. Moral ramifications aside, blood was awfully difficult to wash out."
"But they did outnumber them quite considerably…"

ro "If possible, I don't want to anger another noble family. "
ro "So we should try to resolve this without a bloodbath. "

krau "Most knights rather die with honour than surrender to orcs. "

"In Rowan's long military career, it was usually the lack of noble honor that kept being a problem for him. He couldn't believe a day arrived where it was the abundance of it that stood in his way."

ro "Then we'll make sure death 'with honour' is not an option to them."

show rowan necklace happy at midleft with dissolve

ro "This might be a bit unorthodox, but just follow my lead."

scene black with fade 

scene bg3 with fade

joff "And then I said: “Hold right there criminal scum!”, and with a single swing of my sword, knocked the axe straight out of his hand!"
joff "Swoosh!"

nive "Oh my!"

rosa "(Oh Goddess, please end me.)"

"Lady Nive gasped audibly, covering her mouth in astonishment. The rest of the retinue, depending on their distance from Sir Joffrey, either nodded politely, rolled their eyes, or, in case of a single knight at the very end of the party, mimicked stabbing himself in the heart to a friend of his."  
"Said friend, while sharing his feeling on the matter, was too well-behaved to offer anything except an understanding smile."

rosa "You must be quite the fighter Sir Joffrey."

joff "Well, I don’t like to brag-"

lysa "Nobody's accusing you of that, Joffrey."

joff "-But my uncle, Lord Polignac, says he has not seen a warrior of my skill in twenty years!"

nive "Oooh!"

rosa "Very Impressive."

lysa "Very impressive indeed."

rosa "Oh yes, you simply must tell us more."

"How did Lady Nive buy any of that crap, was beyond Lady Rosalie comprehension. With any luck, her friend would soon get over her crush, and she will be freed of that buffoon's presence."
"At least Sir Lysander was an amicable company."

joff "Well, if you insist-"

rkn "Wait."

"The knight in the front raised his hand, his voice strained."

rkn "… Something’s not right."

harry "An accurate assessment, my adventurous attendant!"

"A masked man entered their vision, stepping from behind a tree in front of them. Leather clad, he had a single, broadsword in his hand, and a piece of cloth that covered his face."

harry "Horrid Harry at your service."
harry "And this is a robbery."

"Sir Joffrey burst out laughing."

joff "Ha, you and what-"

lysa "-This band."

"All around them, orcs stepped out of their hiding spots."

rosa " (How did we not see them?!)"

lysa "… Your orcs are quite skilled, Sir Harry."

harry "Please, it’s “Horrid Harry and his hideous rascals.”"

"..."

harry "I couldn’t find anything that started with “H”."

nive "... Hooligans?"

harry "..."

orcb "Fuck, iz better."
orcb "Eh."

"Rosalie looked around in panic. Why were these people casually chatting like that? They were about to get murdered!"
"She leaned to one the knight by her side, and whispered angrily:"

rosa "Do something!"

"Exemplary leadership."

"The knight hesitated for a moment, then carefully reached for his sword-"

harry "A-a-a! "

"- but Horrid Harry immediately noticed his movement, and wiggled his finger menacingly at the group."

harry "I'd advise against that. We are all well armed, we have you surrounded and we outnumber you two to one."

harry "Well, three to one, since the lovely ladies are technically noncombatants."
harry "… But I will see them upgraded to “Collateral” if you refuse to cooperate."

joff "Bastard!"

harry "Thank you. Now, how about you all drop your gold and jewelry, and we end this… Unfortunate for you, very fortunate for me, debacle, without a single drop of blood shed?"

joff "If you think-"

lysa "Joffrey, the ladies."

"His friend’s warning tone must have gotten through to the hotheaded noble. Joffrey shut his mouth, and after some hesitation, tossed the bag of coins by his belt to the bandit." 
"The knights followed suit. Getting robbed by bandits was humiliating, but acting rashly and getting their wards killed was far worse."  
"Soon, a small pile of riches laid in front of the masked man. Horrid Harry nodded with appreciation."  

harry "Good, good, we’re all en route to a very happy ending here, at least compared to some of the other options. Just one more thing."
harry "Young lady, can I know your name?"

"The bandit turned to Rosalie. She gaped at him in surprise."

harry "Your name?"

rosa "… Rosalie. Lady Rosalie Dolloway."

harry "Ah, pleasure to make your acquaintance. Dolloway, great line, great line..."
harry "Now, Lady Rosalie…"
harry "I like your dress. Strip down."

"Rosalie flushed red."

rosa "Wha- How dare you!"

harry "With great impunity.  Now, enough chit-chat. Strip down. Hop hop!"

"Rosalie stared agape, not comprehending what was happening. She looked around, hoping for some rescue from this insanity." 
"None of the knights met her eyes. They grasped their swords nervously but had yet to take them out. "
"Except for one."

joff "… No."

"Sir Joffrey jumped off his horse, sword drawn and faced the bandit."

joff "I said no. You can take our jewelry, our gold- "
joff "But you will not take our honour! I will not allow you to humiliate Lady Rosalie for your sick enjoyment! "

"The air became tense. For some reason, it felt like the masked bandit was no longer smiling underneath his mask."

harry "Boy, I don’t think you understand the position you are in here…"

joff "Don’t you dare to call me boy!"
joff "I am Sir Joffrey Rowley, squire to Sebastian Coombs! And I will not allow some common bandit to treat a noble born lady this way!"
joff "I don’t care if you have us surrounded! Honour dictates that I stand in her defense!"
joff "Though I doubt you understand what it means, to keep your ideals at the face of adversity."

if avatar.corruption > 80:
    "A subtle change came over the bandit. Rosalie didn’t like the look in his eyes."
    rosa "Joffrey-"
    harry "Very well. I accept your challenge."
    "Harry's cold voice cut her off. The bandit raised his hand and signaled for Sir Joffrey to approach him." 
    "A moment later both combatants faced one another. Joffrey with his arming sword, the bandit with his own, bastard blade. He had the advantage of reach, but Joffrey was trained since childhood."
    "Maybe he had a chance?"
    harry "Lady Rosalie, if you would give us the signal."
    rosa " I don't-"
    harry "Do not make me repeat myself, Lady Rosalie."
    "She swallowed heavily. She didn’t want to. But she had to."
    rosa "Fight!"
    "It all happened in an instant."
    "Joffrey jumped at the bandit-" 
    show bg3 with sshake
    "Horrid Harry knocked his sword away with a single swing, and went in for a counterattack."
    show bg3 with sshake
    show bg3 with redflash
    joff "Aaaaah!"
    "The young squire howled in pain, as the bandit’s sword struck his face. He fell to the ground, clutching the right side of his face."
    joff "My eye! You took my-"
    "The bandit struck his face by the hilt, knocking him out cold."
    harry "But I spared your life. Consider yourself lucky."
    "His eyes turned to the noblewoman. A shiver ran down her spine."
    harry "Now, Lady Rosalie…"
    harry "The dress, if you would."
    scene black with fade
    scene bg31 with fade
    show rowan necklace neutral at edgeright with dissolve
    show wild orc neutral at center with dissolve
    show orc soldier neutral at center with dissolve
    "A dress for Delane. Jewelry. Some gold."
    "Fine loot, as far as Rowan concerned."
    wo "Heh, this wus pretty fun."
    ro "Shut up."
    "But it didn’t feel like a victory to him."
    $ delane_gifts += 15
    $ change_base_stat('g', +3)   
    $ noblesHuntingSeen = True
    return
    
else:
    "A subtle change came over the bandit. Rosalie couldn’t quite put her finger on it. Was it… Sorrow?"
    
    harry "Very well. I accept your challenge. Ready yourself."
    "The bandit raised his hand and signaled for Sir Joffrey to approach him."
    "A moment later both combatants faced one another. Joffrey with his arming sword, the bandit with his own, bastard blade. He had the advantage of reach, but Joffrey was trained since childhood."
    "Maybe he had a chance?"
    harry "Lady Rosalie, if you would give us the signal."
    "She sighed softly. Somewhat, she felt this would not end well."
    rosa "Fight!"
    "It all happened in an instant."
    "Joffrey jumped at the bandit. Horrid Harry knocked his sword away with a single swing."
    scene bg3 with sshake
    "And knocked him out with the hilt of his sword."
    nive "Sir Joffrey!"
    "The young squire fell to the ground, unconscious." 
    "So much for all his bragging."
    harry "I admire his gallantry, I really do. But it will get him killed."
    harry "One should never throw their life away needlessly."
    "His eyes turned to the noblewoman."
    harry "Now, Lady Rosalie…"
    harry "The dress, if you would."
    scene black with fade
    scene bg31 with fade
    show rowan necklace happy at edgeright with dissolve
    show wild orc neutral at center with dissolve
    show orc soldier neutral at edgeleft with dissolve
    "A dress for Delane. Fine jewelry. Some gold."
    "Fine loot, overall."
    wo "Heh, this wus pretty fun."
    os "Name sucked."
    wo "Yeah. Me not hideous."
    show rowan necklace neutral at edgeright with dissolve
    "Rowan rolled his eyes."
    ro "You all had an opportunity to come up with something yourself. Everyone's a critic..."
    "They were lucky things didn’t turn ugly. And with how everything went down, Rowan doubted anybody would connect “Horrid Harry and his Hideous Rascals” with the orc camp in northern Rosaria."
    show rowan necklace happy at edgeright with dissolve
    "All in all, great job."
    $ delane_gifts += 15
    $ change_base_stat('c', -3)   
    $ noblesHuntingSeen = True
    return


label summerResidence:

#wineryCG
scene black with fade
show rowan necklace neutral behind black

ro "Jackpot."

"He and Kraug were standing on a hill overlooking a small, stylish residence. A noble’s summer retreat, at the moment with only a token garrison protecting it."
"Everything they needed to make Delane comfortable, right under their noses."  

krau "We strike at midnight. Be ready."

"Most of the time, orcs lacked the discipline to keep their mouth shut long enough not to compromise their position. But Ulcro ran a tight ship. Rowan gave them some tips, but they knew how to stay hidden."
"Night came, and the resident guards were none the wiser about their presence."

if check_skill(6, 'move_silently')[0]:
    "They struck quickly and without mercy, killing the guards, and capturing the staff."
    if avatar.corruption > 50:
        "Rowan ordered them bound and chained. Castle Bloodmeen could use more slaves, and he knew Kraug and his men were watching him. Even if he wanted to, he couldn't show any mercy. His behavior would impact how Ulcro thought of the twins."
        $ change_prisoners(5)
    else:
        "Rowan ordered them set free. Slave hunting was not their objective here. He saw Kraug narrow his eyes on him, but he didn't care."
        $ change_base_stat('g', -3)   
        "As they expected, the residence was rich in high-quality items. Not expensive items – there was no jewelry, rare books, or paintings. But the residence possessed well-made cutlery, fabrics one could use for embroidery, and a fine collection of wines." 
        "Small things that made life comfortable, that the nobles never really paid attention to, until they were taken away from them."
        "Delane would certainly enjoy seeing her standard of life at least partially restored."
        $ delane_gifts += 15
        $ summerResidenceSeen = True
        return
        
else:
    "Or so they thought."
    "They struck without mercy, but the guards were ready for them. Two of Ulcro’s warriors fell from the opening salvo of arrows, another fell from the second one. Not enough to stop them. Not nearly enough."
    "And the defenders knew that all too well."
    krau "No!"
    "Rowan didn’t know if what followed was what the residence owner told them to do in cases like this, or did the defenders did it out of spite. Unwilling to let the residence be plundered, they set the building on fire."
    krau "Don’t let any escape! I want 'em all DED!"
    "Rowan could only curse out loud, as he watched the fire grow stronger. There was no way of saving the wooden building now." 
    "The orcs quickly captured the fleeing garrison and put them all to the sword, but he found no solace in that. Their raid failed." 
    "In the morning, they would sift through the rubble and loot what was still of some worth. Cutlery, mostly. It wasn’t what Rowan expected, but at least it was something."
    $ delane_gifts += 5
    $ summerResidenceSeen = True
    return






    