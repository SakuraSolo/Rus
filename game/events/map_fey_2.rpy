init python:
    
    event('isdruel_introduction', triggers='map_expl', conditions=('week > 16', 'world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)    
    event('heartsong_introduction', triggers='map_expl', conditions=('week > 16', 'world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)  
    event('whitescar_introduction', triggers='map_expl', conditions=('week > 16', 'world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)  

label isdruel_introduction:
#isdruel introduction event
scene bg3 with fade

"Rowan took a long, frustrated inhale and tilted his head skyward, staring up into the canopy of forest green, wondering how on earth he had gotten himself into this mess."
"He stood near the center of a circle of steel, a short distance away from a tall, plant-like Dryad. Her snarling, alien face contorted with anger as she adopted an aggressive pose to the villagers clustered around her." 
"Rowan stood between them and her in the inner ring of the circle, his hands outstretched towards both hostile parties as he desperately tried to ease the lethal tension hanging in the air. He had only just arrived in time to prevent an outright war breaking out."

show rowan necklace neutral at midleft with dissolve

ro "If you’ll all just calm down, we can-"

cro "{i}Burn{/i} the bitch!"

show rowan necklace angry at midleft with dissolve

ro "You take one step past me before we try to sort this out, and I’ll cut you down myself."

"Several of the villagers backed away at Rowan’s deadly serious proclamation. Taking advantage of the momentary lull in violence, he considered the situation."
"Opposing this assorted rabble, in the center of the encirclement stood an emerald-skinned female. Her gaze darted back and forth in an almost bird-like manner from person to person as her scowl only deepened."
"The rage in her eyes was punctuated by the writhing fury of her tentacle-like vines. She looked ready to snap at any moment. Rowan realized that he had to tread lightly here."
"Looking around the crowd, he recognized something peculiar about these townsfolk: they were surprisingly well-armed, bearing weapons of quality steel and even {i}crossbows{/i}." 
"Despite their numbers and thuggish aggression, this was no mere peasant mob. Contradictorily, he also saw something in their eyes that gave him pause: real, genuine fear."
"To have even the slightest chance of mediation Rowan needed to know the facts about this impromptu war with nature. He scanned the crowd with a tactician’s eye, spotting something strange upon his second look: a young man, absent a weapon of any kind." 
"Instead he clung a host of linen bags to his chest as if his life depended on it. The fabric of the bags was thin enough that Rowan could see an unnatural, green light emanating from between the seams." 
"One of the sacks hung open. Looking closer, Rowan saw the source of the bags’ glow: within the sack were packed dozens of green mushrooms, each as big as his hand." 
"They throbbed with a strange, pulsing power; they looked like they were from another world… a {i}decidedly green and forested{/i} world. The pieces were starting to click into place."
"Rowan decided to approach the situation from a different angle. He needed to know if the plant-like woman could be reasoned with."
"He met her eyes, approaching with his hands in front of him, in an attempt to display his peaceful intentions. He spoke in short syllables, trying to gauge how much she could comprehend of his speech."

show rowan necklace neutral at midleft with dissolve

ro "Um… Excuse me?"

show isdruel neutral at midright with dissolve

isdr "…"

show rowan necklace happy at midleft with dissolve

ro "Hell-o, there! My. Name. Is. Ro-wan!"

isdr "…"

ro "What. Is. {i}Yours{/i}?"

isdr "You speak as if I am without sentience, child. I am Isdruel, the Avatar of the Black Birches, the {i}seething thorn{/i} of the Bloodrose!"
isdr "Step aside, my quarrel is with these villagers, not you."

show rowan necklace neutral at midleft with dissolve

ro "Why are you threatening these people? They pose no threat to you."

show isdruel angry at midright with dissolve

isdr "No {i}threat{/i}?! These thieves pilfered my sisters’ stock and attempted to make off with it like bandits!"

ro "Look, I just want to end this without any bloodshed."

show isdruel happy at midright with dissolve

"The Dryad smiled wickedly at the statement."

isdr "That is fine. I can strangle the lot of them without shedding a single, worthless drop."

"At this murderous proclamation a man stepped forward from the crowd. He was clad in boiled leather, wielding an arming sword. The armor, along with the ease with which he commanded their attention made it clear that he was this rabble’s ‘leader.’"
"They had come prepared for a fight. Whatever it is they intended to use the stolen mushrooms for, they seemed willing to go to extreme lengths for it. The leader assumed an assertive stance, drawing his sword and pointing it directly at the Dryad’s heart."

peas "Ready arrows, lads! Let's make sure the tree-bitch feels the cold touch of your steel!"

"Well this was an unexpected change. Rowan turned back to face the crowd of villagers and affixed them with a glare. He could see in the uncertain look they passed around between them that the Dryad’s words were, indeed true." 
"The villagers had attempted to raid the nature sprite’s mushrooms, and had been caught red handed. Rowan’s face tightened."

show isdruel angry at midright with dissolve

isdr "Get out of my way, ‘Ro-wan.’ My quarrel is only with the interlopers."

"He paused to consider the situation. One one hand, the Dryads were fae creatures of the woods, less ‘living beings’ than forces of nature. He had no real love for them, nor did he know the true purpose of these mushrooms." 
"The forest-kin had always been a danger to local villages growing up, and Rowan had been raised on bedtime stories of Dryads luring little children out into the woods to boil for their supper."
"That being said, the villagers were thieves. And far from trying to diffuse the situation, they were actively threatening the Dryad. She hadn’t attacked yet, so Rowan assumed that it was at least trying to hold back her anger. He could not say the same thing for the villagers."
"This was bad. Violence seemed inevitable, and Rowan saw only three real options available to him." 
"He could side with humanity and aid the treacherous townsfolk, he could side with nature and aid the inhuman Isdruel, or he could simply step back and let the volatile situation resolve itself… likely in a very bloody manner."
"The first option seemed immoral, the second one unnatural, and the final one a shirking of his own self-imposed responsibility. No option was ideal, but Rowan knew he needed to make a choice."

menu:
    "Side with the villagers.":
        $ released_fix_rollback()
        "Despite the fact that they are both the intruders and aggressors in this confrontation, Rowan felt that he had to side with his own kind. They may have been thieves, but the Dryad was a monster."
        "His hand clenched around his sword hilt as he turned his back on the villagers to face the Dryad, a stormcloud brewing on his features."
        show rowan necklace angry at midleft with dissolve
        ro " Leave. Now. Or I’ll slay you myself."
        "To punctuate his point Rowan drew his blade. Its metallic ring echoed in the branches around as he pulled it free from its scabbard. The Dryad took a step back at Rowan’s sudden heel turn. She looked deep into Rowan’s eyes, a green fury burning in her gaze."
        "She seemed to consider the merits of continuing her attack, then lowered her head towards the ground in resignation. Her head snapped back up a little too quick for human reaction. She affixed him with a spiteful sneer."
        isdr "The Queen will hear of this, treacherous fiend! You and all your kind will pay for your transgressions!"
        "Even as she spoke the Dryad was melting away into the brush, her body seeming to almost disintegrate into the trees around till there was no sign that she had ever been anything more than a cluster of leaves in a deep thicket." 
        "As she took her leave, a cheer arose from the villagers around the hero. The townsfolk’s leader patted Rowan on the back, taking him by the shoulder as he dropped a bag of coin into his hand." 
        "After a dozen thanks and praises the men were on their way, jovial and singing bawdy tunes due to their bounty. The trees rustled with an unseen wind as they passed."
        $ change_personal_gold(+10)
        $ dryad_side = "villagers"
        return
        
    "Support Isdruel":
        $ released_fix_rollback()
        "Human or not, you see these townsfolk for what they really are: thieves. The Dryad may be a monstrous creature of a different realm than mankind, but she at least was in the right in this situation." 
        "Turning his back on the Dryad to face the villagers, Rowan put his hand upon the pommel of his blade, speaking to them through clenched teeth."
        show rowan necklace angry at midleft with dissolve
        ro "Give the mushrooms back to Isdruel. Now. You stole something from her that wasn’t yours."
        peas "He’s a bloody sap-sucker! Loose arrows! Kill them both!"
        "Before Rowan could so much as draw his weapon Isdruel lashed out. Like lightning a multitude of viney tendrils erupted from her hands and body, reaching out to snatch bows, arrows and weapons from the hands of the very people wielding them." 
        "In seconds more than half the villagers - including {i}all of the archers{/i} - were defenseless. Gasps and cries of terror erupted from the crowd of villagers and momentary chaos ensued." 
        "It took the shouting voice of their leader to calm them down and bring them back to normalcy. He stared at both Rowan and Isdruel with a look bordering on disgust."
        peas "You… you win. Take the mushrooms, traitor. They aren’t worth dying for."
        "The leader gestured, and the young man carrying the bags tossed them on the ground at Rowan’s feet. He gathered his men, disappearing back the way they came as quiet returned to the woods. Rowan could hear the chirp of a bluebird far above, and let out a sigh of relief."
        show isdruel happy at midright with dissolve
        "Isdruel approached him, a victorious smile on her face as she pulled him suddenly into a hug. She pulled him closer, turning it into a strangely intimate hug as she put her lips to his ear."
        isdr "The Queen will hear of this, Rowan. I will tell her of the aid you have given to the Midnight Court."
        "Isdruel pulled back, a longing look in her expression as she affixed Roland with her chlorophyll-colored eyes. She smiled at him."
        "Her vines curled around the bags, hefting the mushrooms onto her shoulder as she strode with seductive grace into the trees, melting away as if she had never been there in the first place."
        "...Well that was something."
        $ dryad_side = "isdruel"
        return
        
    "Step aside and let them fight":
        $ released_fix_rollback()
        "This is a fool’s errand. Rowan knew that neither side was truly ‘innocent’ in this. The villagers were thieves and brigands, and the Dryad was an inhuman monster of questionable intent." 
        "Neither deserved his consideration in this, and in fact it likely served his ultimate purposes to simply not intervene. Rowan let go of his sword, stepping back from the line of fire as he threw up his hands. If they wanted their bloodbath, by the Gods they’d get one."
        hide rowan with dissolve
        "Sensing Rowan’s dickering, the village leader called on his men to open fire. Rowan dodged to one side as a crossbow bolt {i}twanged{/i}, shooting forth with sudden fury." 
        "The Dryad lets out an inhuman cry of anger and swarmed forward, lashing out with her vines as she slashed at villagers left and right. What followed was a short but brutal fight, one that left several villagers limbless and headless upon the ground." 
        "The townsfolk, faced with an ethereal being of far greater power than they, scattered in moments. The only one who maintained his composure throughout was the village leader, who bravely (or perhaps foolishly) rushed the Dryad as his friends were dying around him." 
        "They exchanged a few blows before the Dryad grabbed him by the neck, lifting him off the ground as the villager’s feet dangled. The leader cast a long, last look in Rowan’s direction, the fear and anger in his eyes palpable as the Dryad shoved her fist through his chest." 
        "Rowan looked away as the leader’s eyes rolled into the back of his head and the Dryad let him go, crumpling bonelessly to the ground."
        "The Dryad was wounded, a porcupine of crossbow bolts peppering her chest and body, though she seemed to take no notice of it. When it was all said and done, only Rowan and the injured Dryad stood in the empty clearing amidst the bodies."
        isdr "The Queen will hear of this, treacherous fiend! You and all your kind will pay for what you have done!"
        "Her threat hanging in the air, the Dryad’s tendrils wrapped around the bag of mushrooms, pulling them to her. She hefted them over her shoulder and turned away without a second glance, disappearing into the copse of trees as if she had never been there in the first place." 
        "Rowan picked his way across the body-strewn earth towards the forest exit, a pit in his stomach as he went."
        $ dryad_side = "no one"
        return

#########################################################################################################
#########################################################################################################
#########################################################################################################

label heartsong_introduction:

scene bg3 with fade

"Nightfall. The forest’s trees closed in with a haunting stillness. Rowan felt cold, clammy nervousness sit in the pit of his gut like a dead, nerveless fish. A stiff breeze blew the swirling leaves into a torrent of falling green."
"His hand hovered close to his blade, his eyes flicking back and forth, searching for something hidden in the undergrowth. He held his breath, listening for the unseen assailant."
"Then: the battle cries. The screeching wail of small, green creatures as the Goblin raiding party burst forth from all around. Some were riding wolves, others running forward on foot with an assortment of rickety short bows and plundered, rusty military equipment. "
"He ducked the first charging spearman, breaking the haft of the spear between his hands as he yanked the thing from the creature’s grasping fingers."
"He slashed at the next one that came riding by on its wolf, dodging the snapping jaws as he cut down the rider in a swift, smooth horizontal strike." 
"In the confusion, one the Goblins managed to leap forward, leaving a shallow cut in Rowan’s arm before the hero repaid in kind, impaling the creature on the spot with his longer blade."
"The fight was a chaotic blur; within seconds several of the Goblins lay dead, and the rest had fled screaming into the undergrowth." 
"Rowan let out a deep sigh, wiping his dirtied blade upon his pant leg before sheathing his blade. His arm smarted from the light cut, but he was all right otherwise. Fucking Goblins."
"That night, Rowan tossed and turned in his bedroll. His head was hot, his cheeks flushed as he panted, despite the cool air. He was sweating, as he blinked in the darkness, he could see flashes of shapes and whorls of colors bleed across his eyes like a hallucination."
"He groaned, sitting up out of his bedroll and leaning against a tree, staring up at the stars as his heart beat out of his chest. His hallucinations soon worsened: he saw burbling buboes, infected wounds, the slow, torturous decay of time upon a corpse left out in the open."
"All the images were different, but all kept this unifying truth in his sight: disease.  The better part of the night passed this way, with Rowan drifting in and out of consciousness in an awful, waking limbo."
"Amongst the horrid images of creeping, wet death, Rowan suddenly saw a bright light: a beautiful woman engulfed in white glimmers, an elegant voice emerging from her lips."

show heartsong neutral at center with dissolve

hear "Let me in, Rowan. Let me {i}help{/i} you. It is for the best. I am here for you."

hide heartsong

menu:
    "Trust the woman.":
        $ released_fix_rollback()
        "Rowan could not stand this interminable misery. He let go, allowing this strange woman into… well, he wasn’t quite sure. It seemed that the intent to open himself up to her was enough, as a sudden warmth suffused him." 
        "The woman’s smile became a brilliant, pale light; the radiance blinded him, removing all pain and discomfort. It was as if a fog had rolled away and he could finally see the daylight. She stood before him, glimmering like a strange, luminescent mirage."
        show rowan necklace shock at midleft with dissolve
        ro "Are you… am I dreaming? Or are you really here in front of me?"
        show heartsong neutral at midright with dissolve
        hear "Both."
        "Her smile sent wings of laughter into Rowan’s heart. His breath was taken away by the ease with which she could instill joy."
        hear "You are lucky the Goblin’s attacked you while my dreaming body was nearby, Rowan."
        show rowan necklace neutral at midleft with dissolve
        ro "..What?"
        hear "Ha ha! It is all right: you don’t need to fully understand now. Just know that my name is Heartsong, and that I am here to help you. I am a Dreamwalker."
        ro "..."
        hear "I will aid you as best as I can through your recovery. Those creatures will be in for a surprise, when they come for you on the ‘morrow."
        hear "Rest now. Come dawn, you will be hale and hearty, I will prepare you for their arrival."
        scene black with fade
        scene bg3 with fade
        "The next morning, a troop of Goblins flitted through the boughs of the forest surrounding Rowan’s sleeping place. They crept forward, silent save for the low growling of their wolves on the periphery." 
        "The Goblins had coated their blades in a deadly hallucinatory toxin, and had paid a high price to incapacitate the warrior. They would not be denied their spoils, now that he was helpless to resist."
        "As they came upon the warrior’s full bedroll, a trio of them approached, their weapons at the ready. At a signal from the leader, they flipped open the blanket, beneath which they fully expected to see a feverish and incoherent Rowan."
        "What they discovered instead, was a pile of rocks. Turning to one another in confusion, they chattered back and forth in their language. It was only the sound of Rowan’s battle cry far above them that caused them to stop their loud bickering."
        "Rowan, having waited for his opportune moment to strike, leapt from the branches high above, his sword drawn. The nearest Goblin half-heartedly lifted her sword to fight him, but Rowan simply yanked the hilt from her hands and tossed it away."
        "Surprised, caught off guard and not expecting the warrior to be so healthy, the Goblins panicked and fled, dispersing in all directions. Rowing let out a grunt of satisfaction and brushed himself off. He knew the goblins wouldn’t be back after that stunt." 
        "Seeing that it was now well into the morning, he resolved to continue onwards with his quest, sparing only a glance backwards after packing up to the tree he had lain against. He wondered to himself if he’d ever get to see the beautiful Heartsong again."
        $ trustHeartsong = True
        return
        
    "Resist the illusions with all your strength.":
        $ released_fix_rollback()
        "Panting, shivering and feverish, Rowan nonetheless mustered his strength and did everything he could to resist the illusions, especially the beautiful siren calling to him." 
        "His resistance seemed to succeed, as her beautiful visage slowly faded away to nothingness, leaving him alone with his visions of death, decay and drudgery."
        "The next morning, a cold and shivering Rowan was rudely awoken by the pack of Goblins from the day before, come to finish the job. He stumbled out of his bedroll, shakily drawing his sword as he struggled to defend himself." 
        "The Goblins spare just enough time to kick his legs out from under him and shove him to the ground before moving to his possessions. One particularly spiteful creature even kicks him in the gut as she passes."
        "Helpless, Rowan watched as the Goblins pilfered his purse. The creatures laugh and call him all manner of names in Goblin as they leave, heaping insults upon him as their wolves snarl and snap from a distance. Darkness claimed Rowan as he once again fell into a stupor."
        "Later that afternoon, Rowan awoke once more, light on coin and feeling profoundly nauseous. His vision had at least returned to normal - thank the gods. And with some effort, he found that he could walk." 
        "With his camp in shambles and his coin purse noticeably lighter, he soldiered on, promising to himself that he’d kick the first Goblin he saw next square in the stomach."
        $ change_treasury(-30)
        $ trustHeartsong = False
        return

#########################################################################################################
#########################################################################################################
#########################################################################################################

label whitescar_introduction:

$ whitescarMet = True

scene bg31 with fade

"Rowan felt the prickling sensation at the back of his neck with the weary awareness of a man too-used to being followed. Craning his neck around for what felt like the hundredth time, he looked over his shoulder, across the wide plains of Rosaria and saw nothing." 
"He let out a sigh and shouldered his pack, moving onwards towards a small canyon in the distance where he intended to set his trap."
"Whoever - or {i}whatever{/i} - it was, the thing had been pursuing Rowan for days now, hovering just out of sight, always a vague mirage on the horizon, a flicker across the waving fields of grain."
"Today was the day he would finally catch them in the act… whoever it was. Glancing around at the high ridges of the hills that formed the narrow canyon, Rowan knew that he had found the right place." 
"The only real way to follow was to take the narrow path through the canyon. Now all that was left was to decide how to engage this would-be stalker."

menu:
    "Set up a classic but effective trap.":
        $ released_fix_rollback()
        "Rowan decided that the sneakier approach was likely the best. Given his lack of real knowledge of what kind of foe he was facing, the element of surprise would be crucial in ensuring his ultimate victory over whatever ended up crashing through the brush."
        "Moving with a speed that belied his own weariness, Rowan took his boots off and removed his shirt, sticking just on the inside of a deep crevice in the wall of the canyon. He wanted it to look like he had found some momentary respite inside the crevice."
        "Taking care to avoid leaving any tracks behind, Rowan scaled the nearby cliffside, scrabbling on hands and knees near the top to reach an ideal vantage point." 
        "Then, he waited."
        "It took several minutes, but Rowan finally managed to spot a strange, furry object moving across the trammeled earth as it entered the mouth of the canyon. He saw the shaggy pelt and dark fur of a Beastman wolf, moving with swift surety towards his hiding spot."
        "It paused for a long moment, lifting its long snout into the air to sniff at the wind." 
        if check_skill(10, 'survival')[0]:
            "Fortunately, Rowan had foreseen this eventuality, and had positioned himself downwind of the creature so as to be out of his scent. Noting the discarded boots near the crevice below Rowan’s hiding spot, the Beastman slipped into the crevice." 
            "Rowan took this as his chance. He scurried down the hillside, sword in hand, ready to face his now-cornered opponent."
            "The creature didn’t notice him till it was almost too late. Lunging out of the way of Rowan’s deadly strike, it spun around in place, snarling as it drew its blade."
            jump whitescarConfrontation
            
        else:
            "Something off caught in the Beastman’s nose. The creature’s head snapped up to stare directly at Rowan atop the cliff. The warrior’s folly became immediately apparent: he had placed himself upwind and inadvertently given the creature a full whiff of his presence." 
            "Its golden eyes blazed into Rowan’s own, locking gazes with him as a voracious smile spread across its bestial features. It was a monster’s toothy grin, one only the Beastmen were capable of producing."
            "In a flash the creature has drawn its sword, lunging up the short cliff face at Rowan, who had little choice but to defend himself."
            jump whitescarConfrontation

    "Face whomever is stalking him head on.":
        $ released_fix_rollback()
        "Rowan let out a frustrated grunt; he was tired of playing games. If the thing that was following him was so intent on continuing the pursuit, then Rowan would face it head on like a man."
        "He turned to face the entrance to the canyon, drawing his sword in one long, languid movement. Sching! Screeched the blade as it slid from its scabbard."
        "There was the sudden crumbling of rocks overhead, and Rowand glanced up in time to see a grey blur leap at him from the cliffside above." 
        "The height was such that Rowan hadn’t expected an attack from that direction, naively assuming anyone stupid enough to do so would die from the fall. He lifted his blade just in time to block a brutal strike that might have decapitated him had he been less aware."
        "The beast landed to his right and rolled to its feet, snarling at Rowan as it lifted its serrated blade once more. This was no mere mortal: it was a Beastman!" 
        "The Wolfish creature grinned, wiggling its blade, which dripped red from the tip. Rowan lifted his hand unthinkingly to his cheek. His hand came away red. Rowan let out a warrior’s yell and charged the creature."
        jump whitescarConfrontation
        
label whitescarConfrontation:
    
"Rowan smoothly sidestepped the Beastman’s clumsy strike, smacking into the rock formation next to him and chipping off chunks of rock." 
"He ducked when the creature slashed in a sweeping half-circle at his head, backpedaling as the monstrous beast continued to advance upon him, giving no space to recover."
"The creature was faster, stronger, and more ferocious by far than Rowan. It became immediately apparent that he could only hold off the creature for so long by going toe to toe with it." 
"Rowan batted aside another strike for his head as he searched in desperation for some advantage in the fight. He got in a good swing or two, but the creature’s peternatural agility always saw his precise strikes come only within grazing distance."
"At last, Rowan slipped, his foot catching upon the uneven ground and giving way. He stumbled backwards, his guard breaking as the monster leapt to take advantage of the opening." 
"However, instead of disemboweling the warrior, the creature kicked him in the chest, sending him sprawling to the ground. Rowan’s sword clattered out of his hands. Rowan tried to scramble to his feet, but the creature unmanned him by throwing his head back and laughing." 

show whitescar neutral at cliohnaright with dissolve

whit "A good tussle."

"{i}Tussle{/i}? As far as Rowan was concerned this was a fight to the death! He struggled to his feet, leaping to retrieve his blade. But the Beastman unnerved him by sheathing his own."

whit "You’ve got good form, for a pinkskin. You should be honored you held off as long as you did."
whit "I see now what the Golden One first saw in you… you may yet prove to be the way forward for us."

show rowan necklace angry at midleft with dissolve

ro "What in the hell are you talking about?"

"The Beastman did not respond to Rowan, he merely smiled. The fangs pulled back from his narrow lips, and the creature’s full row of teeth were displayed. It was unnatural and unnerving, like seeing a four-legged animal walking upright on its hind legs."

whit "This was a test. You have earned the right to speak with us, for you have earned our respect."

"The Beastman lifted its head, sniffing at something in the distance. Its grin grew wider, predatory."

whit "...But now is not the moment. Now is the time for the {i}hunt{/i}!"

"With a roar the beast took off, sparing not a second glance for Rowan’s exasperated expression. Within moments the beast was clear of the canyon, leaping forward on all fours as it crossed the distance at near-superhuman speed."
"Rowan retrieved his sword with a certain baffled befuddlement. He had more questions now than when the beast had first appeared!"
"As Rowan departed the canyon, he checked to make sure that he wasn’t still being followed. The tingle on the back of his neck had gone away, so that was something. But the Beastman’s words continued to linger in his mind long after the encounter." 
"...The Golden One?"

return
