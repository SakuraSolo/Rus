init python:
    #Indarah gets that D
    #requirements: Orientation
    event('indarah_get_that_d', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)
    event('andras_tavern_visit', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'", 'NTR == True'),  depends=('unexpected_hero',), run_count=1, group='alexia_barmaid', priority=pr_npc)
    event('indarah_get_that_d2', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), depends =('indarah_get_that_d',), run_count=1, group='alexia_barmaid', priority=pr_npc)
    event('pony_stop', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'",), run_count=1, group='alexia_barmaid', priority=pr_npc)


label indarah_get_that_d:
#Indarah gets that D
#requirements: Orientation

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve


"Alexia was working the usual afternoon shift. A long caravan was passing through on the way to the castle, and that turned what would have otherwise been a slow day into a maelstrom of work."
"The monotony of the day was broken up by a sight that changed a few perceptions for Alexia."

show indarah neutral at midright with moveinright

"Indarah was walking through the usual crowd of travellers holding beers in each hand. There was something majestic about the way she could duck and dive her way through a hazard field of roaming hands, tightly packed bodies, and whatever the drunks had spilled on the floor."
"Suddenly, a hand shot out of the crowd. A deliberate motion. It squeezed down hard on the Tavern Keeper’s rear, and drew her closer. Alexia held her breath from across the room. Was that man about to lose a hand?"

#indarah aroused
show alexia barmaid shocked at midleft with dissolve

"But, no. Surprisingly, she let out a playful gasp and let herself be dragged on to the man’s lap. Alexia almost gasped. She’d never seen Indarah liked to flirt with the customers, but she didn’t seem the type to be manhandled."
"The man was huge. Nearly half a head taller than the other men around. He had fire red hair and a red dragon tooth tattooed on his cheek. Certainly he was an intimidating figure, but Indarah certainly didn’t look scared."
"When he finally let her boss go, Alexia went to discuss what she’d seen with her."

#indarah happy
show alexia barmaid neutral at midleft with dissolve

al "I thought you were going to eat him alive. You’re normally really good at avoiding getting groped by the drunks."

ind "It wasn’t a matter of good at it or bad at it. If he was a normal customer he never would have got a hand on me."
ind "But, I’ve known Jak for years. He used to stop in port back when I lived on the isles. I was the one who set up his trade compact with Jezera. When he gets too handsy, just means I need to put him back in his place later on."

"Alexia nodded. If she knew him well that made far more sense. Still..."

al "Put him back in his place?"

ind "Or perhaps he’ll be putting me in mine. The man makes for a good time. You never know who will end up on top by the end of the night."

"Alexia looked over him. He was laughing and taking swaggering gulps of his tankard. How did he even get so huge?"

#if alexia corruption is less than 50
if all_actors['alexia'].corruption < 50:
    al "That’s really. Uh. Well it sounds like you really enjoy it."
else:
#else
    al "Sounds like you’re in for a wild night."
    "She giggled softly to herself."

#rejoin
ind "You know, if you’re curious, you can always drop in and see for yourself. A pair of eyes doesn’t do much for me either way, but Jak’s always eager for an audience."
ind "Besides, the fucker claims he has dragon’s blood. Now, I suspect he’s full of shit, and it’s just orc blood. But, either way it sure makes for a real impressive sight."
ind "Interested in a show?"

menu:
    "Stay and watch.":
        $ released_fix_rollback()
        $ alexiaWatchedJak = True
        jump jakIndarah


    "Politely decline.":
        $ released_fix_rollback()
        "Alexia shook her head."
        al "I don’t think so. Not today at least. I appreciate the offer though."
        ind "Think nothing of it. I’m a more practical boss then those you’ll find in your castle. I know for a fact that Jezera at least doesn’t much like hearing no."
        show alexia barmaid happy at midleft with dissolve
        al "The two laughed together and then Indarah was off. While Alexia was making the rounds an hour later, she noticed the woman was gone. She smiled softly to herself, confident that the other woman was having a good time."
        return


################################################################################
label jakIndarah:

if all_actors['alexia'].corruption > 49:
#if alexia corruption is greater than 49
    al "That sounds like it could be a great time, actually. I accept your offer."
else:
#else
    "Alexia didn’t say much in reply. How could she even vocalise her feelings about that kind of offer? She just nodded silently and blushed."

#rejoin
ind "I thought you might like that. Just wait to go until you see me and Jak head upstairs. Then follow along yourself. Alright?"

"Alexia agreed and returned to work. Every so often, Indarah would shoot her a knowing look. Hours passed before she saw the sign. While most of the men were distracted by a conversation about dangerous places to travel, Indarah sashayed up the stairs after Jak."

if all_actors['alexia'].corruption < 50:
#if alexia corruption is less than 50
    show alexia barmaid concerned at midleft with dissolve
    "She bit her lip softly. It was hardly a betrayal of Rowan if she was just watching, right? Still, was she really going to do this?"
    "Clearly though, the answer was yes. After all, after a few moments she started the slow walk towards the staircase."

#rejoin
scene black with fade
"Alexia followed the path that Jak and Indarah had followed, through by now they were both out of sight. Naughty thoughts of what the two must be doing together filled her head."
"Of course, in the darkness, it was hard to tell which room the two has sojourned off too. The answer came in the sound of a soft moan muffled by a door halfway down the hallway."
"Alexia pressed her ear to the door. Panting. Slapping. Moaning. Gasping. She heard Indarah’s swarthy voice amidst the soundscape. This was it."
"She slowly opened the door, trying to make as little noise as possible. She was here to watch, not disturb the proceedings."

#Indarah dicking CG 1
scene cg174 with fade
show indarah naked behind cg174
show jak neutral behind cg174
pause 3

"The door opened and Alexia almost gasped. Indarah was naked, sweat covered skin gleaming in the moonlight. And she was not alone. Her hips were pistoning downwards, impaling herself on a massive cock. One that belonged to the man from before. Jak."
"She expected at least some kind of acknowledgement of her presence, but the two just kept on thrusting and thrusting like she wasn’t even there. Alexia silently closed the door behind her and took a seat."
"What she was watching was not lovemaking. No, this was fucking."
"Alexia marveled at Jak’s body. The size of his build. Maybe he really was part dragon? The muscles and scars that ran the entire way over his chest. Not to mention the size of other parts of his anatomy."

#if NTR is on and Andras' Influence on Alexia is at least 5
if NTR and all_actors['alexia'].flags['andras_influence'] >= 5:
    "A stray thought ran through her head. A red cock inside of her…"

#rejoin
"Her eyes also trailed over Indarah. The domineering powerful way that she slammed herself down on his cock again and again. Alexia’s eyes followed her form. How had she not realized what a beautiful body Indarah had until now."

#if NTR is on and Jezera's Influence on Alexia is at least 5
if NTR and all_actors['alexia'].flags['jezera_influence'] >= 5:
    "Of course, Alexia had been having many strange...stirring...thoughts about women of late. Her mouth watering attraction to Indarah was hardly unusual."

#rejoin
"Jak was red faced and grunting loudly now. Alexia leaned forward in her chair. Was he approaching his limit?"
"That was when Indarah brought her hand up and brought it crashing down in a loud smack across Jak’s face."

ind "Is that the best you can do? Really? You’ll never satisfy me unless you put some back bone in it. Did your cock shrivel up from too much time on dry land?"

"He grunted once more. The slap was etched into his face by a glowing pink hand print. She rode him harder, using his body as if it were nothing but a sex toy."

ind "I said is that the best you can do?"

jak "Maybe..."

"Without warning, the room exploded into activity. Jak shot up, seizing Indarah by the hips and sending her smacking down against the bed. She hissed and wriggled in his grasp, but to no avail. He now had her pressed against the bed by overwhelming weight."

#Indarah dicking CG2
scene cg217 with fade
show indarah naked behind cg217
show jak neutral behind cg217
pause 3

ind "Fuck. No."

"Alexia muffled a gasp. One of her hands drifted between her legs."

jak "Maybe, maybe not."
jak "After all, little bird, maybe you’re the one who's gotten soft. Fucking merchants when you used to fuck pirate lords? That ain’t a real challenge."
jak "Not like me, bitch."

"His cock had gotten free of her body in the process of retaking control. It shone in the moonlight, massive and still gleaming with her fluids. Of course, within moments he penetrated her, ramming his cock into her again. Indarah couldn’t stifle a defeated moan."
"Now the one on the bottom, Indarah is subjected to his vengeance. He mercilessly pounded her again and again, earning a groan each time. Her hands struggled, trying to gain leverage, but were caught and forced to the bed."
"Alexia’s hand sneaked underneath her dress. She panted softly as her fingers toyed with her wet sex. Her eyes were trained solely on them."

ind "Ooooohhhh..."

"He thrusted forward again and again, grunting and working his muscles. How her normal form even kept up is seemed like a minor miracle. She seemed to steady somewhat, and started twisting her hips as she thrusted back, caressing his cock with her body movements."

ind "You’re still going to have to do better than that, asshole. Fuck me like you mean it. Do I look like your hand? Is this masturbation? Fuck me like you mean it!"

"Her provocations would prove more than effective. She only fell silent after an animalistic thrust left her gasping too hard to even speak. Her eyes glazed over and her words melted from her lips. The heat of their bodies colliding was just too much."
"This brutal fucking was coming to an end. Even Indarah had stopped struggling beneath him. Their bodies moved in pitch perfect rhythm. The air was consumed by their musk. Alexia felt her own heat rising."
"Watching this scene had left her breathless. She could feel her orgasm approaching as inescapably as she could feel theirs."
"Unsurprisingly, it was Indarah who came first. She let out a sound halfway between a squeal and screech."

ind "Yes. Yessssss."
show cg217 with sshake
show cg217 with sshake
scene cg218 with flash
show indarah naked behind cg218
show jak neutral behind cg218
pause 3

"The spasming of her body set of Jak. He groaned out loud, and his whole body went stiff. Alexia could almost feel the sticky white cum filling Indarah’s hole."
"That sight, that mental image, was the final straw for her too. Alexia rolled her head back and let herself cum. The third limp body and the only one not overwhelmed with raw physical force."
"Some time passed. Alexia regained her senses. Indarah and Jak were lying on the bed, which was now stained with their juices. Somehow, Alexia knew that she’d be the one to clean it up."
"Indarah and Jak didn’t cuddle. They didn’t hold one another. They laid with little concern for one another."
"Jak recovered first. He stumbled shakily to his feet and pulled on his clothes."


#if NTR is on and Alexia's corruption is greater than 49
if NTR and all_actors['alexia'].corruption > 49:
    "The man turned towards Alexia and loosely groped his crotch in a lewd show of masculinity."
    jak "Liked what you saw, did you bitch? If you're lucky maybe next time I'll split you in half as well."
    show alexia barmaid aroused behind black
    al "Is that a promise big boy?"
    "She slid her hand down to her cunt, and pulled her lips apart in an inviting gesture."
    al "I can't wait..."
    "Jak laughed and headed back to the tavern proper, muttering something about sluts."

#if NTR is on and Alexia's corruption is less than 50
if NTR and all_actors['alexia'].corruption < 50:
    "The man turned towards Alexia and loosely groped his crotch in a lewd show of masculinity."
    jak "Liked what you saw, did you bitch? If you're lucky maybe next time I'll split you in half as well."
    "Alexia blushed intently, she couldn't deny she was aroused by what she had just seen, but would she really let him have her?"
    "Jak laughed and headed back to the tavern proper, muttering something about sluts."
else:
#else
    "For a brief moment as he left, he gave Alexia a tiny nod. The only time he’d acknowledged her in the entire time she was here."

#rejoin

"Indarah purred softly from the bed, and at last turned her attention back to Alexia. She beamed with pleasure. She was like a satiated cat."

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve
show indarah neutral at midright with dissolve

ind "Ignore his manly gruff nonsense. He was happy you were there. And based on what you were up to, I’m guessing you didn’t mind either."
ind "Perhaps we might have to do this again at some point."

#if Alexia's corruption is greater than 49
if all_actors['alexia'].corruption > 49:
    "Alexia simply smirked and nodded along. She was already considering what fun could be had next time."
else:
#else
    "Alexia blushed softly and gave a small nod. It seemed kinky, but at the end of the day, all that really watched was she had fun watching other people have sex. What was wrong with trying it again?"

#rejoin
#alexia gains a small amount of corruption
$ change_corruption_actor('alexia', 3)
#alexia loses a little stress
$ change_actor_stress('alexia', -4)
return


#############################################################################################################
#############################################################################################################
#############################################################################################################

label andras_tavern_visit:

scene alexia_tavern_1 with fade

"Another week went and passed, spent on tirelessly serving the customers."
"As always, the visiting travelers were evenly split between polite and rowdy, though both groups enjoyed ogling the waitresses to a similar degree, the only difference being whether or not they tried to be sneaky about it."
"… And being sneaky mostly meant staring at their asses rather than their tits."    

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve

"The evening was slowly turning into night, and with it, Alexia’s shift was about to end. She was cleaning up the last of the dirty tables when she heard a deep voice behind her, and a large hand landed on her shoulder."

show alexia barmaid shocked at midleft with dissolve

$ andras_name = "???"

an "Excuse me?"
an "Fair maiden, if you would please point me to your best spot?"

show alexia barmaid neutral at midleft with dissolve

al "Of course, it’s-"

show alexia barmaid shocked at midleft with dissolve
show andras disguised happy at midright with dissolve

$ andras_name = "Andras"

al " You-!"

an "“You”? Is this how you treat your hero, my beautiful lady? Ha ha ha!"

show alexia barmaid neutral at midleft with dissolve

"He let out a boisterous laugh that thundered across the tavern. He even struck a heroic pose, flexing his arm, no doubt expecting some sort of applause in recognition of his heroic deeds from a while ago."
"And he might have gotten some cheers, if not for the fact none of the currently visiting patrons were present during the last orc attack. None of them were there to witness his gallant display of heroism, martial skills and “selflessness”." 
"So the only thing he got in response was a long silence. If the tavern was in Rosaria, Alexia would no doubt hear a cricket."
"Not that it stopped him from letting out another loud “Ha!” and flexing his other arm." 

al "Ha… Ha…"

"Alexia did her best not to roll her eyes. He really did enjoy this act of his a little bit too much…"
"It was probably better than having everyone in the tavern whipped for insulting him, but still."
"She couldn’t imagine Rowan behaving the same way if, for whatever contrived reason, he had to play a villain or a bandit."

an "Now then, fair maiden, certainly you know why is it that I come here."

show alexia barmaid shocked at midleft with dissolve

"His grip tightened, and a predatory smile briefly entered his lips. The tavern was all but empty by now, with only a few lost travelers remaining."

menu:
    "Did he come for her to “service” him?":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +3)
        $ change_actor_num_flag('alexia', 'andras_influence', 2)
        show alexia barmaid aroused at midleft with dissolve
        show andras disguised smirk at midright with dissolve
        al "Is it for me to… “Service” you?"
        an "Yes… Service me…"
        show alexia barmaid shocked at midleft with dissolve
        show andras disguised happy at midright with dissolve
        an "With your best meat and wine, ha ha!"
        show andras disguised happy at edgeright with moveoutright
        show alexia barmaid neutral at midright with moveoutright
        "He let another boisterous laugh, then wrapped his arm around the dumbstruck Alexia and led her to one of the cleaner tables."
        
    
    "He came for meat and wine, obviously.":
        $ released_fix_rollback()
        show alexia barmaid neutral at midleft with dissolve
        al "For the best meat and wine in this part of the Rakshan Wasteland."
        an "And for the best service, ha ha!"
        show andras disguised happy at edgeright with moveoutright
        show alexia barmaid neutral at midright with moveoutright
        "This time she did roll her eyes, and firmly nudged him in the direction of the nearest clean table."
        
"Alexia had no doubt the red-skinned demon was plotting something nefarious, but she couldn’t confront him about it. Not while he was disguised, with people around them." 
"Andras took his seat, and lazily asked how the tavern had been doing since his last “visit” - as if he didn’t have access to weekly reports from Rowan. She indulged him, mentioning some of the highlights, but without going into too much detail."
"He also made some not exactly subtle remarks regarding the beauty of the tavern staff, and how lucky they were to have such a “devoted protector” looking after them."
"Ten minutes into his monologues, she almost wished he’d go back to threatening bodily harm."
"Another ten minutes in, he finally placed his order. He demanded whatever was roasting in the kitchen, as well as “The best wine the house could deliver”."

al "(Best wine you say…)"

menu:
    "Bring him the best wine you have.":
        $ released_fix_rollback()
        $ change_actor_num_flag('alexia', 'andras_influence', 1)
        hide andras with moveoutright
        show alexia barmaid neutral at center with moveinleft
        "It was best not to anger the demon. Whatever game he was playing, she’ll do as he asks, and soon enough he’ll be on his way."
        show alexia barmaid neutral at edgeleft with moveoutleft
        "She headed for the kitchen, and carefully went through their wine stock. It didn’t take her long to find what she was looking for. She grabbed one of the bottles, and swiftly returned to Andras."
        show andras disguised happy at midright with dissolve
        show alexia barmaid neutral at center with moveinright
        al "Here you go sir, our finest wine."
        "With a polite smile she started pouring the red liquid. When the glass was half full, Andras stopped her, and picked it up. He swirled it gently, and brought it to his nose to sniff it."
        an "Mmmm… Acceptable aroma…"
        show alexia barmaid shocked at center with dissolve
        "He took a careful sip, and smiled approvingly."
        an "Mmm… Unbelievably rich and weighty… And I like the spicy oak in it."
        an "Well picked."
        show andras disguised angry at midright with dissolve
        an "But your service is abyssal!"
        show alexia barmaid shocked at midleft with moveoutleft
        show bg21 with sshake
        "He threw the glass to the ground, sending shards everywhere. Alexia yelped in terror and jumped away from him."
        an "Do you wish to offend me woman?! After everything I did for this place?!"
        show indarah shock at edgeleft with moveinleft
        show bg21 with sshake
        "With a swing of his arm, the wine bottle flew through the air and shattered on the nearby wall. Alexia winced again as the cracking sound pierced the air."
        an "Bring me another, and this time, offer it to me properly!"
        al "Y-yes sir!"
        
    "Bring him something cheap. He won’t be able to tell the difference anyway.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +2)
        hide andras with moveoutright
        show alexia barmaid happy at center with moveinleft
        "Andras liked to pretend he was sophisticated, but he she knew it was a rouse. Perhaps it was petty of her, but she couldn’t resist the opportunity to mess with him a little."
        show alexia barmaid neutral at edgeleft with moveoutleft
        "She headed for the kitchen, and carefully went through their wine stock. It didn’t take her long to find what she was looking for – several bottles stashed at the bottom, for a particular type of clients."
        "Clients who liked expensive wine, but drunk so much of it, that an hour into the party they couldn’t tell what was being served to them. It might have been dishonest, but Indarah looked for profit wherever she could."
        "She grabbed one of the bottles, and swiftly returned to Andras."
        show andras disguised happy at midright with dissolve
        show alexia barmaid neutral at center with moveinright
        al "Here you go sir, our finest wine."
        "With a polite smile she started pouring the red liquid. When the glass was half full, Andras stopped her, and picked it up. He swirled it gently, and brought it to his nose to sniff it."
        an "Hmm..."
        show andras disguised angry at midright with dissolve
        show alexia barmaid shocked at center with dissolve
        an "Disgusting!!!"
        show alexia barmaid shocked at midleft with moveoutleft
        show bg21 with sshake
        "Without as much as taking a sip, he threw the glass to the ground, sending shards everywhere. Alexia yelped in terror and jumped away from him."
        an "Do you wish to offend me woman?! After everything I did for this place?!"
        show indarah shock at edgeleft with moveinleft
        show bg21 with sshake
        "With a swing of his arm, the wine bottle flew through the air and shattered on the nearby wall. Alexia winced again as the cracking sound pierced the air."
        an "Unacceptable! Is this what counts for service here?!"
        an "Bring me something actually good! And this time, offer it to me properly!"
        al "Y-yes sir!"
        
hide andras with moveoutright
show alexia barmaid neutral at edgeleft with moveoutleft
show indarah neutral at center with moveinright

"She hurried back to the kitchen, passing Indarah who kept the door open for her. "

al "I’m sorry, I-"

ind "Don’t worry, it’s not your fault."

"The woman offered Alexia a reassuring smile, closing the kitchen and ordering the rest of the girls away for a moment. They needn’t have people listening in on them. "

ind "I know people like that. People like Andras."
ind "Over-buffed men who get off from treating women like dirt."
ind "Do not think he cared for the wine or the service for even a minute. He just needed an excuse to blow his fuse."

"Alexia could not suppress a grimace, even though Indarah words hardly surprised her. Of course. Andras would not be satisfied with merely tormenting her in the castle. He would follow her wherever she went, like a curse."

show alexia barmaid concerned at edgeleft with dissolve

al "I’m sorry Indarah, this is all because of-"

ind "Do not apologize Alexia. You are not at fault here. None of this is your fault."
ind "Take the rest of the night off. I’ll handle Master Andras."

"Again, Indarah tried to smile reassuringly, but this time Alexia was not fooled. The tavern keeper had plenty of experience dealing with pushy drunks, but Andras was on a whole other level. Her smile was strained, and Alexia saw her swallow nervously."

ind "This is an order."

"… Yet she would not allow Alexia to face the red demon herself."

menu:
    "It’s Alexia that Andras is after. She can’t let Indarah fight this battle for her.":
        $ released_fix_rollback()
        jump andrasBarAlexia
        
    "Let Indarah take care of Andras. She knows how to handle people like him.":
        $ released_fix_rollback()
        "Maybe it was cowardly. Maybe it was selfish. But could anyone blame her for not wanting to be on the receiving end of Andras wrath?"
        jump andrasBarIndarah
        
label andrasBarAlexia:

al "Indarah, I…"
al "Thank you, for looking after me. But I can’t leave you with this on your head."

show alexia barmaid happy at edgeleft with dissolve

al "I’ll handle Andras myself, alright?"

#indarah angry
show alexia barmaid shocked at edgeleft with dissolve

ind "Foolish girl, you-!"

show alexia barmaid concerned at edgeleft with dissolve

ind "..."

#indarah neutral

ind "Alexia, you’re a kind woman, and I’m glad Rowan chose to put you in my care."
ind "But I worry this kindness will spell doom for you. You cannot bend to Andras’ every whim just because you fear what he might do to people around you."

show alexia barmaid neutral at edgeleft with dissolve

al " I know. But this is not your burden to shoulder."

show alexia barmaid concerned at edgeleft with dissolve

al "Now, will you help me survive the night with at least some dignity intact, or will I have to do it all alone?"

ind "..."

#ind happy

"The tavern keeper burst into a low, humorless chuckle."

show alexia barmaid happy at edgeleft with dissolve

ind "Oh Alexia, Rowan must have quite the headache with you. Very well, I’ll advise you on what to do."

show alexia barmaid neutral at edgeleft with dissolve

"Shaking her head in disbelief, Indarah headed for the glass shelf. She walked along it slowly, looking for a particular glass in her collection."

#ind neutral

ind "What people like him desire is not sex, though that may be a part of it. What they really want is for us to degrade ourselves, to grovel at their feet, and admit we are less than them."
ind "… And I’m afraid that’s exactly what you will have to do.  "

"She stopped, finally finding what she was looking for. She took the object and showed it to Alexia. It was a tall glass with a long stem and a wide rim. A cocktail glass."

ind "Luckily for us, as we still have guests and he maintains his disguise, so we should be able to get away with using this. We’ll give him the “proper service” he grumbles on about.   "

al "Meaning?"

ind "You’ll let him drink from your cleavage. You’ll put this glass into your shirt, pour the wine in, and let him drink from it.    "

if alexiaAndrasSex == 0:
    show alexia barmaid aroused at edgeleft with dissolve
    "Alexia blushed a little. This wasn’t that bad, but still…"
    
else:
    show alexia barmaid shocked at edgeleft with dissolve
    al "Huh. That’s it?"
    show alexia barmaid concerned at edgeleft with dissolve
    "The words left her mouth before she could stop herself. Indarah said nothing, but for a brief moment, she saw the pity in her eyes." 
    "Alexia tried her best to be discreet in her liaisons with Andras, but some rumors must have circulated the castle. Her words merely confirmed what Indarah already suspected."

ind "Last chance to back down."

menu:
    "Serve Andras":
        $ released_fix_rollback()
        pass
        
    "Let Indarah handle this after all.":
        $ released_fix_rollback()
        "It wasn’t just Andras they were taking into account here. The entire tavern would see her attend to Andras. It would not only be humiliating – it could also impact her reputation."
        jump andrasBarIndarah
        
hide alexia with moveoutleft

"Her mind was already set. With a determined expression, she took the glass from Indarah’s hands, and headed for the wine rack to pick the most expensive bottle they had."

ind "You might feel tempted to try and get him drunk, but I’d advise against it. He might get… Handsy."

show alexia barmaid neutral at edgeleft with moveinleft

al "I’ll keep it in mind. Thank you."

#indarah happy
ind "You’re welcome dear."

#ind sad
ind "Take care."

"There was no use stalling. Alexia steeled her nerves, and with the wine in hand, went to face her tormentor."

hide indarah with moveoutleft
show andras disguised happy at midright with dissolve

"All eyes turned to her the moment she left the kitchen. Andras’ earlier display sobered up every drunk in the tavern, and they all wanted to see how Indarah would handle the issue."
"None of them knew throwing him out was not an option. Except for the man in question."
"With a triumphant smile on his lips, Andras devoured her form with his eyes, before he reminded himself he was supposed to play the role of a disgruntled customer."

show andras disguised neutral at midright with dissolve

"But even after that, she swore his eyes had a mocking spark in them."

show alexia barmaid neutral at center with moveinleft

"She forced herself not to grit her teeth, and with her most charming smile approached his table."

show alexia barmaid happy at center with dissolve

al "My deepest apologies my Lord, for the sub-par vintage we offered earlier."
al "Will this one be more to your liking?"

"She held the bottle up to her chest and leaned forward, the label on it strategically placed right in front of her bosom."

an "Hmmm…"

show alexia barmaid neutral at center with dissolve

"He stroked his chin in thought, shamelessly ogling her tits. She suppressed the urge to smack the bottle over his head. She was used to having her boobs looked at, but unsurprisingly, willingly posing like this made it much more humiliating."

show alexia barmaid happy at center with dissolve

an "I suppose. If the service is right."
an "A hero deserves the very best, don’t you agree? "

menu:
    "“A *true* Hero does indeed.”":
        $ released_fix_rollback()
        show andras disguised angry at midright with dissolve
        an "..."
        $ andrasPunishmentCounter += 1
        
    "“Of course, my Lord.”":
        $ released_fix_rollback()
        show andras disguised happy at midright with dissolve
        an "Glad you agree."
        
an "Then get to it."

al "(Here goes nothing.)"

show andras disguised neutral at midright with dissolve

"Dying on the inside, she opened the bottle and put it aside on the table.  She saw Andras’ eyes widen as she grabbed the edge of her cleavage, and pulled at it."

show andras disguised happy at midright with dissolve
show alexia barmaid neutral at center with dissolve

"Keeping her most unreadable expression, she put the glass between her breasts. It wobbled a little, so she had to put her arm around her bosom, to squeeze her tits together."

al "I apologize, one moment."

"Magnanimously, Andras allowed her to continue. She grabbed the bottle, filled the glass, and leaned in to push her chest right into Andras face."

#cg1 - var 1
scene cg278 with fade
show andras disguised happy behind cg278 
show alexia barmaid neutral behind cg278 
pause 3

al "Please, take a sip."

"Andras held his hand up, and shook his head."

an "Now, now… You have to let it breathe first."
an "But keep the pose."

#cg1 - var 2
scene cg279 with fade
show alexia barmaid neutral behind cg279
pause 3

al "(Bastard!)"

"She wanted to smash the bottle right on his smirking, annoying face. But she couldn’t. For her and Indarah’s sake, she had to keep him happy, no matter how much it sickened her."

#cg1 - var 1
scene cg278 with fade
show alexia barmaid neutral behind cg278
pause 3

al "But of course, Sir."

"All around them, people started to switch seats, so they could get a better view of the unfolding show."
"So they could see the red-haired spunky wench, who usually never allowed anyone to grab a feel, demeaned herself with a smile on her face. To witness her providing a service one could only find in brothels or other similar establishments."

al "(Solansia protect me… Get on with it Andras!)"

"She squirmed, trying to avoid their judging gaze. But it was no use."

#cg1 - var 3
scene cg281 with fade
pause 3

"It was no use."

#cg1 - var 1
scene cg278 with fade
show andras disguised smirk behind cg278
show alexia barmaid neutral behind cg278
pause 3

"She swallowed heavily, and resigned herself to the situation."
"…"

scene cg280 with fade
show andras disguised smirk behind cg280
show alexia barmaid neutral behind cg280
pause 3

"Finally, Andras leaned in and took a long, overly theatrical whiff."

an "Mmm… What a wonderful bouquet."
an "Very promising…"

al "I’m glad you approve, sir."
al "Care to taste it?"

an " So eager to have my face between your tits?"

show alexia barmaid shocked behind black

al "! ! !"

"The tavern roared in laughter, like the simpletons they were, while Andras finally leaned in to taste the wine. His eyes never left her, and Alexia again had to suppress a scowl."

an "Mmm…"
an "You know… I don’t usually approve of Rosarian wine… I think most of them are simply austere…   And the last one that was offered to me… Not here, mind you… Was borderline disappointing… "
an "So tired in taste it was… You could barely call it wine. It was a cheap, vinous insult to the palate."
an "But this one…"
an "I can see it becoming one of my favorites…"
an "Complex… Robust… Earthy, but in a good way."
an "A rich finish that leaves you yearning for more."
an "Mmm… Yes. I approve of this."
an "Another."

scene black with fade

"… …. …."
"… …"
"…"

#cg1 - var 3
scene cg281 with fade
show andras disguised smirk behind cg281
show alexia barmaid neutral behind cg281
pause 3

"In the end, she followed Indarah’s advice and allowed Andras to pace himself. Just as tavern owner predicted, he kept his hands to himself."

an "-now, their women, with their constant fights for dominance in bed, are quite fun to subdue. But the lack of tits is a bit of a let down."

al "I see, my lord."

"But it did not stop him from having her serve his every whim, and stand by his side as he recalled his many “adventures”, many of them serving as pretexts to comment on her looks."

an "Everybody likes a big bosom. Yours is nice, but it could be a bit bigger…"

al "I apologize for disappointing you my lord."

"… And of course, she had to keep nodding and agreeing with him. For the last two hours."

an "But you do show your tits off, like a nice little slut, so that’s a plus."

al "Please do not call me a slut, my Lord."

an "My apologies. My fair maiden, it’s nice to see you show off your tits so shamelessly, just like a slut would."

#cg1 - var 2
scene cg279 with fade
show andras disguised smirk behind cg279 
show alexia barmaid neutral behind cg279 
pause 3

al "..."

an "And I do love the way you updo your hair. Is it for convenience’s sake?"

al "Yes, my-"

an "For when you suck the clients off?"

#cg1 - var 3
scene cg281 with fade
show andras disguised smirk behind cg281
show alexia barmaid neutral behind cg281
pause 3

al "… We do not provide this service here, my lord."

an "Such a waste. Your body was made for serving men."

al "Thank you, my lord."

"It was humiliating at first, but as the night went on, she gave up on being angry, and just went along with it."
"Let him say whatever he wanted about her, as long he doesn’t cause any more trouble…"

scene black with fade

"… …. …."
"… …"
"…"

scene bg21 with fade
show alexia barmaid concerned at midleft with dissolve
show indarah neutral at midright with dissolve

ind "Is he gone? "

al "… Yeah."

ind "How are you feeling."

al "Tired."

if all_actors['alexia'].flags['andras_influence'] > 5:
    al " But I’m used to it by now."

else:
    al "I hope this doesn’t become a regular thing."

ind "Oh Alexia…"
ind "Take tomorrow off. That’s an order."

"She nodded numbly. With any luck, this was just a one-time thing, and Andras won’t make harassing her like this his new favorite past time."

scene black with fade

"A girl could hope."

$ change_corruption_actor('alexia', +5)
$ change_actor_num_flag('alexia', 'andras_influence', 3)
return

label andrasBarIndarah:

al "Will you promise you’ll be safe?"

#ind happy

ind "Of course. No need to worry about me."

al "… Then I’ll let you handle it. "

"Indarah nodded with a smile, and sent her off to her room."

scene black with fade

"Tomorrow, she would not say what Andras ended up demanding of her, but judging by the bruises on her wrists, he was not happy with Alexia’s disappearance."

$ andrasPunishmentCounter += 1
return

#############################################################################################################
#############################################################################################################
#############################################################################################################

label indarah_get_that_d2:

#Indarah Gets the D 2

scene bg21 with fade
show alexia barmaid happy at midleft with dissolve
show indarah neutral at midright with dissolve
show jak neutral at edgeright with dissolve

"Indarah returned to the table with another round of warm Uvarthian Mead. Alexia and Jak had sat waiting for her, kept company by a flickering candle light. Their cheeks were flushed from the past hour of drinking."
"Alexia politely thanked the other woman for her drink, and took in the strange aroma wafting up from her goblet. Her head was already delightfully fuzzy, but she didn’t mind a bit more.."
"Jak, meanwhile, grabbed his goblet with one of his big meaty hands and took a long gulp. Indarah rolled her eyes. If his men hadn't already gone up for the night, they would have no doubt approved."

jak "The Tundra folk have one virtue, and it's that they ain't wilting flowers when it comes to their booze."
jak "It's a wonder they make it so strong and flavorful. Especially once you've tried some of their food. Stale bread, hard rations, meat with seasoning no more complex than salt."
jak "But, when it's time to drink? Then they perk up."

show alexia barmaid neutral at midleft with dissolve

"Alexia nodded along, taking a sip from her drink. As intoxicating as the drink was, there was also something spellbinding about Jak's stories. He'd seen so many places, done so many things."

if NTR and all_actors['alexia'].flags['andras_influence'] >= 5:
    "Jak had a confidence to him that was kind of magnetic. He was confident and knew what he wanted. Alexia was fascinated by that."

#ind happy

"Indarah meanwhile, yawned and stretched her arms."

ind "You talk like you've been out discoverin' ancient wisdom."
ind "You'd want a drink too if you had to live in snow up to your knees and monsters passing by weekly."

"He smirked back at her."

jak "I'd probably never be sober."

"Jak turned to Alexia. He liked a rapt audience."

jak "Really though, you had it good in Rosaria. If you had a bite of the food down south, you'd long for a punch in the gut. Disgusting stuff."

al "It can't have been the worst you had to eat traveling around. I've heard from some of the men that pass by that the food they take for travel is barely edible."

show alexia barmaid happy at midleft with dissolve

"Alexia took another swig, finishing off her drink. When she put the cup down, she noticed that she felt warm. It was like the fire of the candles had grown stronger."

jak "Bunch of liars. Most of them probably keep a bag 'o spices around for flavoring. Road food is bland, but it ain't that bad."

"Indarah leaned forward with a smirk on her face. In the process, she tilted her cleavage towards him. Jak's eyes took the bait."

if NTR and all_actors['alexia'].flags['jezera_influence'] >= 5:
    show alexia barmaid aroused at midleft with dissolve
    "Though, he wasn't the only one. Alexia had been finding it harder and harder to resist a look at exposed breasts of late..."
    show alexia barmaid happy at midleft with dissolve

ind "You say that, but a moment before you were running your gums about how bad the food down in Uvarth was. You've got a spice belt too. I've seen it around your waist."

jak "I'm sure you have."

"He reached down and produced a small bag."

jak "Though, I mostly use it for keeping dried randado root. Potent aphrodisiac for women. One bite and they get randy enough to spread their legs on the spot. When I mention it, the ladies always want a taste."

show alexia barmaid neutral at midleft with dissolve

"Alexia raised an eyebrow. Was that true? Why had she never..."

ind "That stinks worse than minotaur dung."
ind "You really think I've never had randado root before? It's fake."
ind "That talk is the prattle you tell doe eyed maidens who haven't traveled out of their home town, when you're trying to get them out of their dresses."

show alexia barmaid happy at midleft with dissolve

"Alexia broke out into a huge giggle. Larger than the situation demanded. Jak rolled his eyes and laughed."

jak "No, no. It's the real thing. Whatever you had must have been garlic that some goblin used for a swindle. This is the real thing."
jak "Besides..."

"His eye sparkled with devious intent."

jak "I don't need no randado root to get a girl on the table."

#ind aroused

ind "Please. You couldn't get me over the table if you tried."

jak "Oh? Wanna bet?"

ind "So what if I do?"

show alexia barmaid aroused at midleft with dissolve

"Alexia looked back and forth between the two. She'd seen the signs of flirting. Aggressive posture, targeted smiles. But, it struck her all at once how far along it had gotten. They really were right about to fuck here and now."
"Probably without much concern if she was still here to see."

if all_actors['alexia'].corruption > 69:
    "Alexia got a glint in her eye. Debauchery was such a joy."
    
menu:
    "Stay and watch.":
        $ released_fix_rollback()
        jump jakIndarah2
                
    "Leave.":
        $ released_fix_rollback()
        show alexia barmaid concerned at midleft with dissolve
        al "I have...uh...some chores I need to deal with. Sweep up and all. I gotta run."
        "Neither of them seemed to acknowledge what she said. Indarah gave her a short nod, and Alexia rushed out of the room."
        if all_actors['alexia'].corruption < 69:
            "In the process she nearly stumbled over her own feet."
        if alexiaWatchedJak == True:
            "She had watched last time, of course. But, that had been an invitation. A choice. This felt more like an ambush."
        if alexiaWatchedJak == False and all_actors['alexia'].corruption > 69:
            "Alexia sighed to herself. As much as she did love a good sexual encounter, watching just didn’t seem like something she’d enjoy this time."
        "Alexia wasn't sure. If someone had asked her to explain it in this moment, she probably would have failed. Uvarthian mead was known to have that effect."
        "The moment she closed the door behind her, she heard the sound of rustling and movement behind her. The rustling turning to bangs and groans as she walked away from the door."
        "Jak and Indarah were good company, but spending time with them carried the risk of awkward moments."
        return
                                                                                                             
label jakIndarah2:

"Jak responded to this by calmly rising from his seat, walking around the table, and then lunging at Indarah."
"In a movement so fast that Alexia barely registered it initially, he had his hand in Indarah's hair and was forcing her face down into the table. Her chair fell over to the side."

al "W...woah."

#cg1
scene black with fade
show alexia barmaid aroused behind black
show indarah neutral behind black
show jak neutral behind black

"Indarah let out a gasp against the hardwood counter top. Her half full mead pitched over, staining her dress. She pushed off with her hands to no avail. Jak had her pinned with a mercenary's skill."

ind "Fuck you."

jak "If you insist."

"Jak grinned darkly, as he worked down his trousers. Even while still struggling with her upper body, her hindquarters rubbed backwards against him. She was daring him to take her."
"Alexia watched quietly. Her temples were pounding, her breath was quickened, and her body ached. It was a desperately arousing spectacle."
"Two of her fingers slipped underneath her skirt. Soon she was mewling out lustfully. Her sounds added to the crashing and slapping of the struggling happening in front of her."
"Jak worked Indarah's dress up. It was no easy task. Every time he left her hands free for more than a second, she was forcing herself upwards. He had to bring his hands back swiftly to prevent her from wriggling out."

ind "Do it. Do it, you piece of shit."

"Her growling tone didn't match the soft smirk on her face. But, in moments that smirk was about to be erased."
"Jak brandished his long black cock, and positioned it right behind her."

#//If Alexia has done the stretching scene.
#Alexia knew all too well that taking such a well endowed man was no simple task.

"Then, with a fearsome grunt, he impaled her with it."
"Indarah didn't stop struggling, even as her grunts of effort turned into groaning. If anything, the pushing and shoving became even more frantic. Her hips bucked, albeit mostly backwards. Her wiggling took on an animalistic quality."

jak "Still think...I can't...fuck a girl...on a table...if I want?"

"His hips moved with a steady pounding rhythm. Each time his body made contact with hers, it produced a loud slapping sound."
"Indarah made one last play to fight her way off the table, even as the response of her body to his cock inside of her grew more and more apparent."
"She pushed up with all her might, even working her way free for a second, before his hands forced her back down on the table. He had to reposition himself to resume pounding away at her."
"After that, Indarah played along fully. Her movements mainly focused on the pumping of her hips."

ind "You call this...ah...you call this fucking?"
ind "Fuck me like you mean. Like you mean it."

"Alexia's eyes fluttered. Her own pleasure was steadily mounting, aided by the erotic struggle in front of her."

if all_actors['alexia'].corruption < 31:
    "Still, her cheeks flushed dark. Doing something like this was so lewd…was this something that a slut would do?"

"What followed was a dance of fucking and moving. Hands banging on the table. Teeth snarling and lips moaning. A sexual hurricane throwing empty goblets to the floor and making tables bang and creak."
"Alexia came first. Her fingers worked fast, and soon the stimulation to her clit was more then enough to send her, moaning and shaking, over the edge."

jak "Having a good time, eh?"

"He called over to her, through strained breath. Alexia was too busy shuddering to answer with any degree of intelligence. Too busy being blissed out of her mind."
"At that point, Jak had been pounding his huge cock into Indarah for what felt like forever. Her initial struggling and taunting had collapsed into spasms and incoherent moaning, as her insides were stirred again and again."
"She climaxed with a brutal force, flailing her arms, and knocking one of the few still upright mugs right off the table. The sound of it clattering on the floor was overcome only by Indarah's orgasmic screech."
"Jak kept pounding her, over and over, even as Indarah's movements collapsed into an exhausted heap. The force of his slamming rocking her still body."
"It was her second orgasm that sent him over the edge. As her shaking and moaning picked up for a second powerful crescendo, he too started to feel the sap rise. Alexia could only imagine that her body had tightened down against him."
"Jak responded by quickly whipping his cock out of her, just fast enough that his seed launched all over her back, with some even landing in her hair. It was hard to be accurate when forced to move at that speed."
"Some of his cum even landed on the table."
"As he bent over, panting and gasping. The room around them was a mess. Tables bumped into, goblets overturned. It was like a hurricane had come through."
"Though, it wasn't like anyone particularly seemed to mind. They were all gasping and panting in the afterglow."

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve

"After their little tryst, Indarah and Jak retreated to her room. Whether or not they planned to sleep was a question that eluded her."
"Alexia, meanwhile, was cleaning up the dining room. There was not merely the result of their “conversation” to deal with, but also some of the bottles and plates from Jak's men when they had eaten earlier."

if all_actors['alexia'].corruption > 30 and NTR == True:
    show alexia barmaid aroused at midleft with dissolve
    "Alexia's eyes wandered back to the table, while carrying some bottles. She froze in place. There was a long trail of white sitting on the hard wood right where Indarah had been positioned."
    "She walked over. It wasn't a lot, but it still had the overpowering musk of cum to it. A soft smile worked it's way on to her lips."
    "Alexia placed the bottles down on the floor, and worked her hair back. Then, without the slightest hint of shame, she leaned forward and ran her tongue along the table."
    "It still had that familiar creamy and salty taste to it. Alexia licked and licked until she'd tasted every last drop."
    "After that she returned to work with a new spring in her step. There were so very many messes to clean."
    $ change_corruption_actor('alexia', 3)
    
else:
    show alexia barmaid concerned at midleft with dissolve
    "Alexia's eyes wandered back to the table, while carrying some bottles. She froze in place. There was a long white trail of white sitting on the hard wood right where Indarah had been positioned."
    "There was a bright red blush on her face as she toweled off the table. She hoped that wasn't going to leave a stain on their too. A few days later she'd learn that hope was in vain."
    
return

#############################################################################################################
#############################################################################################################
#############################################################################################################

label pony_stop:

#Pony Stop

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve
#ind concerned
show indarah neutral at midright with dissolve

"Alexia descended down the staircase. The sound of voices down below warned her that it was time for work. She found a crowd of rough looking men and women, mostly in leather, making themselves at home in the main room. Their swarthy complexion was unmistakably eastern."

ind "Keep yourself nice and respectful. These here are imperials."

"From the odd talk around the inn up until now, Alexia knew that to mean they were regular members of the Empire of the Sand’s army."

show alexia barmaid concerned at midleft with dissolve

al "Do you know why they’re here?"

"Indarah sighed."

ind "‘Course. Imperials make a nice bit of mint moving people around. They’re tryin’ sell some folks to the Dark Elves under the woods."
ind "As far as they’re aware of, we must not be anything at all ‘cept a convenient point to rest."

al "Slavers?"

"She didn’t know much about the eastern slave trade, except that it existed. Slavery was not as large an institution down in Rosaria. Especially not in the countryside."

al "Should we be worried about what they might do?"

ind "Nah. They tend to behave themselves. These are army men and women. They know not to go around starting things under the imperial banner."
ind "But, them Imperials ain’t known for their humbleness. So like I said before. Keep it nice and respectful, and nice and respectful is what you’ll get back."

"Indarah shoved a pair of beers into Alexia’s hands, and directed her towards some of the slavers. Obediently, Alexia put on her smile."

"As she bent down to serve them, one more person walked in. This one was different than the rest. They were all wearing sensible boiled leather. She strut in all black leather, showing ample cleavage, and pants and boots for riding. Completing the look was a whip coiled at her hips."
"It was a special kind of leather too. It was sleek. Thin and texture-exposing, but also sturdy and imposing. Sexy in a come-and-get-it-if-you-dare kind of way."
"Alexia blinked twice. Who in the world was {i}that{/i}?"

ind "Everything I said for the others is still true for her. You treat her with respect now. Don’t get into anything trouble. And she’s nothing to worry about."

"Yet, Alexia could tell from the furrow of Indarah’s brow that she was worried about her for whatever reason. She definitely knew why this woman was dressed so differently."
"Alexia kept one eye on the woman throughout the evening. She interacted with the other slavers normally enough. She drank, she joked around, she behaved like one of the guys."
"Though, when she looked closely, she did notice a few little tidbits. None of the jokes or ribbing was ever directed her way. Neither was the odd bit of flirting directed at the other women slavers. Not even the leader of the caravan seemed to get too comfortable with her."
"She was with them. But, she was not truly one of them either." 
"When she asked Indarah about her, Indarah just waved her off. There were promises to explain later, but that wasn’t exactly satisfying to Alexia’s curiosity this very moment."

ind "By now the horse trough is probably as parched as the horses. Be a dear and bring them something to sip on, please."

"Alexia went out, not a complaint on her lips, with full buckets in either hand. She was not surprised to find large carriages with iron bars in a large circle. A few of the slavers patrolled the circle’s perimeter. Alexia didn’t much want to think about what their cargo."
"She turned her head the other direction, towards the watering trough. But, she found no respite."

al "Huh?"

#cg1
scene black with fade

"There was a woman tethered with the horses. A dark skinned beauty with equally dark hair cascading in a ponytail down her back. She stood at stiff attention."
"No doubt aiding this stance was her unusual wardrobe. She was standing here, in the cold night, almost entirely naked. What little clothing she had was an oppressive leather."
"Leather straps criss crossing her body, holding it firm but leaving much of her skin, including her pierced breasts exposed. A stiff collar that held her neck at attention. A contraption that held her arms behind her back in extreme bondage. "
"Even a strange pair of boots that ended in a large metal horse print. Along with the bit and bridle in her mouth, it looked like she was pretending at being a horse."
"There was something unmistakably lewd about it. It was like a mix between a discipline lover’s wet dream and something that a woman might wear to bed. The animalistic nature of it was only highlighted by her placement at camp. She was with the horses."
"Alexia took a step closer. This was definitely not something she would ever find back home."
"It had taken her some time to recognize the metal contraption that the woman wore. It was connected to the leather harness, and ran between her legs. The big bulky plate that covered her crotch had small holes in it."
"It was a chastity belt. It was meant to keep someone from sleeping with her. Or from stimulation from touching her nether regions. The belt had a lock on it. Alexia doubted strongly that this woman held the key."
"Naturally, Alexia’s mind drifted to the woman in sleek black leather before. Were the two somehow related to one another?"
"Alexia walked over and filled the trough with new water. Now she definitely needed to ask Indarah about who that woman was."
"As Alexia walked back inside, someone crossed her path. Dark leather boots strutted confidently on the ground. Alexia turned around. That sleek woman from before was coming outside."

leatwom "Awe, did you miss me, Johara? I didn’t keep you waiting too long, now did I?"

"At the sound of the woman speaking behind her, Alexia scrambled for the door. Better to watch from the door's frame, and not be seen catching an eyeful of what was happening."

#cg2
scene black with fade

"The horse woman’s eyes went wide at the approach of the woman in black. Alexia could only assume it was her Mistress."
"Once the Mistress reached her, her hands enveloped the bound woman. She wrapped herself behind her, with her lips pressed to her victim’s neck, one hand toying with the horse woman’s nipple chain, and the other stroking her inner thighs."
"The horse woman rolled her head back as far as the posture collar would allow and let out a strange whining sound. Her discipline of her posture buckled. In mere moments, she had become an instrument in her dominant’s hands."

if alexiaJezeraSex > 0:
    "The image it brought to mind was her own relationship to a certain powerful demoness…"
    
"The woman brought a hand up to the straps binding her captive’s head. When the bit fell away, Alexia thought that she might finally hear the exotic pet speak. But, all she did was let out a soft whine and open her jaw wide."
"She was asking for something with her mouth."

if alexiaJezeraSex > 0:
    "Yet again Alexia’s mind supplied an answer. This time in the form of a moist purple sex drawing inevitably closer to her face. So close she could smell its overpowering musk."
    "Alexia’s pussy tingled."

leatwom "So eager for your treat. A wild filly indeed. You are a fortunate creature in that I am not a more cruel owner."

"What was meant by that soon became apparent. The Mistress reached into a small pack on her belt and pulled out a strange brown square. Alexia had to strain to even see it."

#cg2 - variant 2
scene black with fade

"Her lips pressed themselves to the “filly’s” ear and whispered unheard words for her alone. Then, she placed the strange cube in her open mouth. It dissolved into nothing." 
"In response, the horse woman let a long low groan out into the night. Her eyes rolled backwards. The sound was only silenced by the bit gag being fit back into her mouth."
"Whatever had been placed into the bound woman’s mouth was having an overwhelming effect on her."
"Whatever self-restraint she had was simply gone. She squirmed, bucked, and ground her body into the dominant woman’s with mindless abandon. Especially her crotch, which Alexia could only imagine was starved of all feeling."
"Her Mistress responded back with a sadistic zeal. Sharp pinches, brutal tugs on her nipple chain, hands roaming her plaything’s body. The horse woman responded to each with a pathetic stifled whine. She was being handled and she loved it."
"Alexia couldn’t help but flash her attention back every so often to the steel belt. There was moisture on it now. The shine of liquid in the moonlight was unmistakable. This girl was soaking wet, teased but helpless."
"Watching it reminded Alexia of her own presence. It also reminded her of the dampness between her own legs."
"With a blush, she ducked back into the inn. If she stayed out too long, she might get caught. Best not to risk such a thing with an imperial."

scene bg21 with fade
show alexia barmaid aroused at midleft with dissolve
show indarah neutral at midright with dissolve
    
"It wasn’t until late at night that Alexia got a chance to sit down with Indarah. By then, all of the guests were tucked into the beds, or standing guard with the carriages."

al "I’d really like to ask about that woman now. I saw what she had parked outside."

#ind concerned

ind "Ya mean that noble steed of her, eh? Yeah, there was no hiding it from ya."

"Indarah shifted in her stool."

ind "That’s just how the empire is. They don’t have much respect for people out that way. None of the Eastern Lords do. In their culture, there are all sorts of ranks and rules. You gotta be half mad to keep it all straight."
ind "That woman is in a special class. Ain’t many of them, but they can be pretty scary. The Faras’i. Fierce fighters and trackers. Raised from birth to it too. Real scary stuff when they get into battle."

al "And the horse woman outside?"

ind "I was getting to that, I was getting to that."
ind "I don’t know how it works or why they started doing it. I’m sure those imperial types have a reason for it. Though, they didn’t think to tell me ‘bout it. But, they have a special type of training for their captives. They make ‘em into beasts of burden."
ind "Mares are what they’re called."
ind "They’ve got these mean old chariots they ride around in when they want to fight, and they got one or two of those lovely things out there to pull it along."
ind "Still, when I said you have got to be careful, I meant it. I had a friend once who ran into trouble with a Faras’i. That’s a tale you’d need to put a lot of alcohol in me before you’d ever hear."

"Horse women. Alexia opened her mouth and closed it again. If she hadn’t seen one for herself, she never would have believed it. What do you believe when your own eyes tell you stranger stories then fantastical books?"
"Had she really been living in a world with such things this entire time?"

scene black with fade

"The following morning, the caravan went on its way, none the wiser as to the allegiance of the inn that they had crossed paths with. Before they left, Alexia watered the horses. She used the opportunity to take a final eyeful of the Mare."
"It was strange to look into her eyes. She had the face of the human, but the vacant expression of an animal. Just how much thought ran through her head? It would not be the last time she pondered that question."

return

    