init python:

    #Wall Inspection
    event('wall_inspection', triggers="week_end", conditions=('week > 8',), group='ruler_event', run_count=1, priority=pr_ruler)
    #Five Years Alone
    event('five_years_alone', triggers="week_end", conditions=('week >= 30',), depends=('champion_statue_sculpting',), group='ruler_event', run_count=1, priority=pr_ruler)
    #what is precious to me?
    event('what_is_precious_to_me', triggers="week_end", conditions=('week >= 40',), depends=('five_years_alone',), group='ruler_event', run_count=1, priority=pr_ruler)


label wall_inspection:

#outer wall bg
scene black with fade

"At the end of lunch, Rowan had asked Skordred to show him the castle's defenses and familiarize himself with what would likely be his home for the foreseeable future. The dwarf had grumbled, but refused to let his boss go alone when he'd offered to do so."

show rowan necklace neutral at midleft with dissolve
show skordred neutral at midright with dissolve

"So, here they were walking the perimeter of the walls that had fallen to the six heroes seven years before Rowan took charge of it himself."

sk "As ye can plainly see, thar's only one entrance ta tha outer walls. Which is tha main gate at the end of a four hundred foot bridge. Tha rest is a sheer forty foot drop down walls and the cliffs of the dry lakebed."

"The dwarf pointed at several metal fittings spaced at even points around the walls."

sk "Though they're empty now, ballista are intended to be mounted at these points to drive back fools who seek to scale those walls with siege towers or ladders.  The main bridge is equipped with catapult emplacements."

ro "Yes, I oversaw them being disassembled. As I recall, they were better built than the ones the Six Realms had, even without steel, so I made sure they were brought back with us to be studied."

sk "Hmph."

"The dwarf was silent for a moment and Rowan surveyed his surroundings, taking note of the statues lining the walls and realizing why they'd been bothering him since he'd arrived at Bloodmeen."

ro "Skordred, I don't think these statues were here back then. Do you know anything about them?"

sk "Aye, tha're the champions of chaos. Our heroes and the heralds of Kharos."

"Rowan took a closer look at one, a man with a surprisingly lifelike appearance and finely detailed physique. There was some weathering but, if he wasn't mistaken, the statue had been repaired or touched up recently. The next, an elven woman, was the same."

ro "Incredible, these are in far better condition than I would have thought. Where did they come from?"

sk "In tha days just before Karnas's death, I carefully took down each of them and hid them in a cave in the mountains thar."

ro "On your own?"

sk "Aye. I knew the end had come, I needed to save what I could so they could be returned when Bloodmeen was reborn. Some of the other builders left to return to our homelands, the rest stood and fought."

ro "Why didn't you fight?"

show skordred angry at midright with dissolve

"The dwarf was silent for a very long moment. When Rowan glanced at the Skordred he saw him mumbling something to himself over and over again while staring at the ground at his feet. One of his gold chains was now in his hand in a white knuckled grip."

show rowan necklace concerned at midleft with dissolve

ro "Skordred?"

"Suddenly his muttering turned into loud screams!"

sk "I'm a builder, not a fighter! I'm a builder, not a fighter! I'm a builder, not a fighter!"

show rowan necklace neutral at midleft with dissolve

"Rowan rushed forwards and put his hands on Skordred's own, forcing him to relinquish his trembling hands from the chain as a trickle of blood ran down them."

ro "Whoa there, calm down Skordred! It's over, what's done is done."

"The dwarf stared blankly at Rowan for a moment, then seemed to recognize the man and turned his head to the side before spitting on the ground."

sk "Let me go, ya monster."

"Doing as he was asked, the man took a step back. After a moment Skordred glanced down at his hands and seemed to see the blood for the first time. He grimaced, but otherwise didn't make a move."

ro "We should go inside so you can get that dressed."

show skordred neutral at midright with dissolve

sk "No, this is nothing. We will finish the inspection first, the one who leads Bloodmeen must know its defenses."

"Without another word on the sudden outburst or the statues that had inspired it, the two of them once again set off on their walk around the walls and the topic of the lecture moved onto the walls composition."

return

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

label five_years_alone:

#outer wall bg
scene black with fade
show skordred neutral at midright with dissolve
show rowan necklace neutral behind black

sk "... should help with that crick ya've had. But don't warry, I'll be with ya again-"

ro "Hello Skordred."

hide rowan
show rowan necklace neutral at midleft with moveinleft
show skordred angry at midright with dissolve

"The dwarf dropped his chisel in surprise and stepped back from one of the statues watching over the castle in shock."

sk "What're you doin here?!"

"He demanded, then stooped over to reclaim his tool, and pointed it angrily at Rowan as if it was his fault that it had been dropped."

ro "I'm going for a walk. Morning patrols of my home whenever I have the energy has been something of a ritual for me for many years now."

show skordred neutral at midright with dissolve

sk "Yer home? Pfah."

"He turned to the landscape surrounding the castle. Rowan did the same, waiting to see if Skordred would say anything else."

sk "Yar time here is nothing next to mine. Ya never saw this castle when it was at its greatest, or at its lowest."

ro "The twins told me they found you here when they first arrived at Bloodmeen. Where you here the whole time since it fell?"

sk "Aye. I alone watched over these walls as time took her toll. For five years I kept my vigil, never leaving these mountains."

ro "What did you do all that time?"

sk "Why do ya ask?"

ro "I wanted to get to know you, considering how important your work here is it's best to know your subordinates."

sk "Not only are ya a monster, yar also a nosey monster."

"Rowan glanced over at the man to see if he was still scowling. To Rowan's surprise he was not, instead his expression was calm and complaintive. However the hero also noted that his subordinate was also gently stroking the leg of the statue next to him."

sk "I was waiting, hoping, that I'd live to see the next lord come to claim Bloodmeen. The castle had to be ready, my works couldn't have all been for nothing."

"Abruptly Skordred turned away from the morning view and stomped away, back towards the interior."

ro "Where are you going?"

sk "To work! I have important duties to attend to."

hide skordred with moveoutright

ro "(Well, he's opening up to me a bit now. That's a start. I wonder if all that time by himself has unhinged him at all?)"

return

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

label what_is_precious_to_me:

scene bg20 with fade
show rowan necklace neutral at midleft with moveinleft

ro "Skordred?"

show rowan necklace shock at midleft with dissolve

ro "(Wait, what happened here?)"

show rowan necklace neutral at midleft with dissolve

"The workshop was in quite the state of disorder, with its owner nowhere to be seen. It looked as if the dwarf had been working on a sculpture, but it had fallen to the floor and fallen apart. No, this had been deliberately destroyed."

ro "(Oh.)"

"Looking closer, Rowan realized that this wasn't any statue, it was probably of him. That was his sword, another piece partially carved from the rock and probably his hair. There was nothing left of the face, that had been completely destroyed."

ro "(Okay, now I'm worried.  Where is that dwarf?)"

scene black with fade

"After looking around and asking some of his staff, Rowan determined that Skordred had been missing for most of the day. The build and salvage teams were working alone, making this absence very uncharacteristic for their superior."

scene bg3 with fade

"He left Bloodmeen and headed into the forests, towards the mountains that Skordred had spent five years as a hermit. He didn't know exactly where the cave would be, but he was confident enough in his tracking skills that he'd find it eventually."

scene black with fade

"Luckily enough the dwarf hadn't exactly been hiding it, as there were clear wheel tracks running through the forest right up to the entrance."

#Show Skordred meditation CG
scene black with fade
show skordred neutral behind black
show rowan necklace neutral behind black

"After giving a moment for his eyes to adjust to the dark interior, Rowan could see the dark dwarf sitting in the middle of a room surrounded by stones of various colours and sizes. The man was naked, facing away from him, his robes folded neatly to the side."

sk "Who be ye, who disturbs my sanctuary?"

ro "Rowan."

sk "Why are ya here?!"

ro "I was worried about you, since it's mid afternoon and no one's seen you since breakfast."

"The dwarf moved for the first time, turning his head to look back at Rowan and out the cave entrance."

sk "Has it been tha long?  I... apologize. I shall be more mindful of my duties."

"He began to rise from the floor, but stopped when Rowan waved him off."

ro "Wait, I saw the smashed statue in your workshop. Does that have something to do with why you're here?"

"Skordred settled back down and resumed his hunched, contemplative stance."

sk "Aye.  Karnas hated you. He hated all the heroes, he would never have wanted ya as a proper champion. In a dream, my lord told me to destroy you, so I did. He said he'd take me back, that he'd love me again."

"Rowan stepped inside, getting closer to the dwarf and saw for the first time that Skordred was crying."

ro "Love you again?"

sk " As the war went on, my master grew angry and paranoid. He lashed out at everyone, refused the touch and comfort of all us. All he said was that he wanted his enemies destroyed, he cared for nothing else. He was no longer the master had known, the master I loved. Ya killed him."

ro "Denara and Solansia killed him, I was just there."

sk "No, Karnas was already dead then. Ya, the general who brought down his armies and pushed them back to Bloodmeen, ya are the one who killed him. From yar own lips I heard ya say the war was already over when you came to Bloodmeen."

"Now his hostility made sense. Rowan wasn't sure how to respond to this man who blamed him for so much, yet his duties forced to follow."

sk "Now I have new masters, however I canny deny tha yar the one who is the true power here. I've seen what you've done for Andras and Jezera in tha short time you've been here. Ya, who took the world from chaos, will be the one to give it back."
sk "Tha is why I must complete yer statue. However, I canny decide what stone represents ya."

"He spread his arms wide as he spoke."

sk "Which would you say is your stone?"

"Rowan looked about the room, noticing that the rocks around him were of all kinds, probably from all corners of the Six Realms!"

ro "Where did you get all these?"

sk "Cla-Min, I have paid her a great deal over tha last year for a proper collection."

ro "I'm not that familiar with stone, is there some other way I can help you?"

"A long moment of silence passed between them, leaving Rowan feeling that perhaps he'd given the wrong answer."

if skordred_bj == True:
    
    sk "I've already tasted ye, what is a little more?"
    
    ro "I'm sorry?"
    
    "Suddenly the dwarf adjusted his pose, unfolding his legs and leaning forwards so that he was on all fours and presenting his backside to Rowan."
    
    sk "To complete your statue, I need to understand yar passion better, show me! Take me! Use me like a proper champion of Kharos!"
    
    menu:
        "Fuck Skordred":
            $ released_fix_rollback()
            $ rowanGaySex += 1
            jump skorCaveSex
            
        "Don't fuck Skordred":
            $ released_fix_rollback()
            ro "No, I don't think so."
            "The dwarf resumed his original seated pose."
            
else:
    pass
    
sk "Then I shall have to hear yar story so I can understand what kind a man ye are."

ro "Alright, I'll tell you a story or two every week at breakfast, how does that sound?"

"The dwarf picked up his garments off of the floor and stood."

sk "Tha will work. I am finished here, for now. I shall return to my duties."

"Satisfied as well, Rowan left the dwarf to get dressed and return to the castle on his own. After all, there were still duties of stewardship of his own to deal with."

return


label skorCaveSex:

"Rowan's mind went back to the time that he was being measured for the statue and the dwarf's mouth on his member. It wasn't the most enjoyable of experiences, but the heat and feel of the dark skinned man. There was definitely something enticing there."

ro "Alright."

#cg1
scene black with fade
show skordred neutral behind black
show rowan necklace naked behind black

"Rowan removed his clothes and stepped behind the dwarf.  As he placed his hands on either side of the dwarf's firm well-muscled backside, he noticed Skordred fumbling in his clothes for a moment before holding up a bottle of some kind"

sk "If ya don't mind, I'd appreciate if ya used this first. Rather not go bareback, yar not a demon after all."

"It turned out to be a rather oily lubricant, which Rowan spread over his member before positioning himself at Skordred's back entrance. Already the dwarf felt hot to the touch, what would his insides feel like?"
"He pushed forward, easily passing inside and being enveloped by the dwarf."

sk "Oh ho, it's been ta long since I had a man in me."

"There was virtually no resistance, Skordred obviously wasn't lying about previous experience. Nor did he have any trouble providing ample stimulation on Rowan's member as he fucked the dwarf."

sk "Naw, show me yer passion!  Fuck me!"

if avatar.corruption < 29:
    
    "There was only one way this felt natural to Rowan, which was to take it slow and relish the sensations. He wanted to make his partner feel just as good as he did, so at the same time as he pumped his shaft in and out he reached around and gripped Skordred's fat, semi-hard member."
    
    sk "Now wha's this? Yer fucking me like I was a girl!"
    
    "Smirking, Rowan pinched and jerked the dwarf's cock for a few moments to get it completely hard and chuckled in response."
    
    ro "What's wrong with that? You asked me to know how I love, what my passion is. Based on your dick, I'd say you're enjoying it."
    
    "The dwarf merely grumbled, but his cock was rock hard under Rowan's fingers. So evidently he was enjoying the treatment regardless."
    
elif (avatar.corruption > 28) and (avatar.corruption < 59):
    
    "What were his passions? What were his desires? What were his emotions?"
    
    "Rowan pushed in hard, trying to show the heights he could go to the dwarf. This was what he wanted, right? To be used as a receptacle for those lusts. So Rowan took him with vigour."
    
    sk "Haha! Yes! This is what I wanted!"
    
    "Continuing the rapid pace of his ponding, Rowan reached around and grabbed at Skordred's cock, discovering it already rock hard. Well, if he was already fine then he probably could just focus on his own pleasure."
    "So he did, fucking the dwarf's hot, slick insides at full speed. Skordred had no trouble taking him again and again, driving Rowan closer and closer to his peak."

else:
    
    "Rowan didn't much care what Skordred wanted at this point, he was going to do things the way he wanted to."
    "Things went into overdrive, with loud wet sounds of him bottoming out over and over again, slapping his balls on Skordred's own with almost each pump."
    
    sk "Aye, this is not wha-"
    
    ro "Shut up."
    
    "Skordred did so, taking everything that Rowan had to throw at him as he took his pleasure out of the dwarf. Whether or not his partner was enjoying it was irrelevant, what mattered was what Rowan wanted now."


#cumshot cg
scene black with fade
show skordred neutral behind black
show rowan necklace naked behind black

"A low growl escaped Skordred's lips and he clamped down hard on Rowan's shaft. Wet squirting and the smell of cum filled the air as the dwarf came from his rectal penetration. The hero wasn't too far behind him, dumping his load inside, then drawing a small trail when he pulled out."
"Several pants escaped both of their lips before either spoke a word."

sk "Thank ye. I am finished here, for now. I shall return to my duties."

"He reached over to take his clothes, then felt at his backside for the trail of Rowan's cum flowing down his rear."

sk "Perhaps I will need a little time to contemplate this passion?"

ro "Pff, don't be ridiculous. Look, if we're going to be fucking on the regular, I kinda want you to know me outside the bedroom too. I've heard some of your stories, why don't I tell you some of mine?"

sk "If thas what ye want, very well."

"Satisfied, Rowan left the dwarf to get dressed and return to the castle on his own. After all, there were still duties of stewardship of his own to deal with."

$ skordred_fuck = True
return
