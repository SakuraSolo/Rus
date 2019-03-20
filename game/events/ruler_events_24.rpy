init python:
    
    event('arrival_of_the_emmisiaries', triggers="week_end", conditions=('week >=30', 'arzylMet', 'whitescarMet',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('paperwork_sabotage', triggers="week_end", conditions=('week >=30', 'castle.buildings["barracks"].troops >= 6',), group='ruler_event', run_count=1, priority=pr_ruler)
    
label arrival_of_the_emmisiaries:

scene bg6 with fade
show rowan necklace neutral at edgeleft with dissolve

"Rowan stepped into Bloodmeen’s cavernous throne room to the sound of shouting. He had been summoned by the Twins, for some unholy purpose or renewed humiliation, no doubt. Rowan fingered his blade as he marched through the vaulted entryway."
"The source of the shouting was  - for once - not the Twins themselves, but rather their guests. Instead of another round of their endless bickering sessions, the two sat quietly while the two figures beneath their matching thrones argued back and forth."
"Rowan recognized both of the offending parties. The first was a hulking brute of a beastman… the same one who had ambushed him in fact in the canyon! Opposing him was a busty Elf of pale complexion and even paler eyes: Arzyl."

hide rowan with dissolve

show whitescar neutral at midleft with dissolve

whit "Truly that fetid court of corrupted monsters has no scruples! They send their scentless spies into the very heart of the Alliance!"
whit "How else could this filth have known to arrive at the {i}exact{/i} moment I did, bearing an inferior offer to the one I currently present to your illustrious persons?"

"The Wolf man snarled at the ephemeral Elven Matron, his fangs gleaming a bestial off-white as her bared his teeth. Arzyl’s snow-white eyes glittered with amusement as her full lips curled into a derisive smirk."

show arzyl neutral at edgeright with moveinright

arz "My, what labyrinthine conspiracies you pin upon me, creature. Do all your fellow ‘Beastfolk’ live up to your brutish name?"
arz "The Old Ones are one with magic, and ofttimes things work out in their favor if they simply surrender to that flow."

"Rowan caught eyes with Arzyl, whose brow lifted with surprise for a moment. The confusion quickly dissipated, and she gave him a playful wink. She licked her lips, her knowing look reminding Rowan of his last encounter with her… he shuddered."
"Whitescar’s reaction was more perfunctory, but perhaps more friendly as well. After noticing where his rival’s eyes were moving, the Wolfman deigned to glance in Rowan’s direction. His sharp gaze held to Rowan for a long moment. He let out a curt nod of respect."

hide arzyl with dissolve
hide whitescar with dissolve

show jezera happy at midright with dissolve
show andras displeased at edgeright with dissolve

je "Ah, Rowan! Just the man we were hoping to see! Come in, you’re just in time for the bloodsport."

an "It would seem that the Red Sun Alliance have come to offer us a treaty of ‘friendship and cooperation.’"

je "Such a tempting offer, don’t you think?"

"Jezera’s condescending tone did little to hide the revealing nature of her self-satisfied smile. She gestured carelessly with her hand in direction of the pale Elf standing before her."

je "And what coincidence! As if by magic, the Midnight Court has come to beg for the same opportunity!"
je "A pack of Beastmen led by one of the last Dragons, and a Cabal of ancient and timeless races, both claiming to be Fae. War makes such strange bedfellows, no?"

"At this last statement the beastman snarled."

show whitescar neutral at edgeleft with dissolve

whit "Do not compare my kind to these simpering weaklings! They are as powerless as they are treacherous!"

hide whitescar with dissolve
show arzyl neutral at midleft with dissolve

arz  "Hmm, such bold words Whitescar. I could turn your pelt inside out of your own skin if I so chose, with just a snap of my fingers."

hide arzyl with dissolve
show whitescar neutral at edgeleft with dissolve

whit "I’d rip your throat out before you could utter a single word, Witch!"

hide whitescar with dissolve

an "ENOUGH!"

"Andras’ booming voice echoed in the chamber like rolling thunder. Both emissaries fell silent, bowing their heads in the direction of the demonic sovereigns."

an "Chief Whitescar, you bring us an offer of warriors, of battle hardened hunters and keen eyed scouts. The Beastfolk’s ferocity is legendary, as is their brutality."

je "They also smell."

an "Even so, it’s hard to argue with {i}those{/i} kind of results, sister. You may place stock in all of your machinations, but I believe in strength over some abstract ‘magic’ that the Midnight Court offers."

show arzyl neutral at midleft with dissolve

arz "You underestimate us then, my Lord. The Midnight Court has {i}many{/i} secrets left to share. Some of them could even be yours, should you allow us to teach you."

hide arzyl with dissolve
show whitescar neutral at edgeleft with dissolve

whit "An offer from the false Fae is a poisoned well. You can only draw death from it. It does not matter what they offer you my Lord and Lady, they can’t be trusted."

"Arzyl laughed, turning to face Jezera directly. She acted as if Andras was not even present in the room."

hide whitescar with dissolve
show arzyl neutral at midleft with dissolve

arz "Ha ha! Would you rather put your trust into a talking wolf? Their kind would gladly hunt the lot of you for sport, were you not the biggest predator in the Six Realms."

hide arzyl with dissolve

je "Their magic is indeed potent, brother. And it is of a type that I myself have no access to! We could learn much from their lore."
je "Perhaps Arzyl has a point. I do so cherish my dalliances with the Fae! And the Red Sun seem… volatile."

an "I would hardly call their kind’s savagery a ‘negative,’ sister."

je "Then it appears we have once more reached an impasse, my beloved sibling."
je "Rowan! Come here, my hero. Your caring masters have need of your counsel."

show rowan necklace neutral at midleft with dissolve

"Rowan set his jaw and stepped forward, aware of the looks he was getting from both Arzyl and Whitescar on either side of him. He put a hand to the pommel of his sword and affected a careless posture."

ro "What is it?"

je "Oh, now don’t take that pouty tone with me! I was just about to gift you with the responsibility of making the decision."
je "Since we have in our infinite wisdom tasked you with handling the specifics of our campaign, I figured it was only fair you got to decide upon our prospective allies as well!"

an "Are you certain of this, sister? Rowan has made many questionable decisions already."

je "Certain? Why my dearest brother: I can argue with you for however long it takes to get my way, you only have to say so!"

"The two demons shared a long, intense look."

an "...I yield to your judgement in this situation, sister. Rowan may decide."

je "I thought as much. Arzyl, Chief Whitescar: you are both welcome to stay in the Castle for the time being as guests of Bloodmeen."
je "I offer you lodging, as well as whatever base comforts and luxuries you desire. Your close confidants may also stay, at least till Rowan has made a decision."

hide rowan with dissolve
show arzyl neutral at midleft with dissolve

arz "My eternal thanks, my Lady."

hide arzyl with dissolve
show whitescar neutral at edgeleft with dissolve

whit "I look forward to proving my worth to the young whelp."

hide whitescar with dissolve
show arzyl neutral at midleft with dissolve

arz "Hmm, me as well."

an "Leave us. You are all dismissed. My sister and I have… something to discuss."

je "Goodness, Andras! I hope its not another one of your tongue-lashings!"

scene black with fade 

"Rowan turned hard on his heel and stalked from the throne room, consciously ignoring the long looks both of the prospective factions offered him as he left the room. He kept his face flat and controlled till he was free of their eyes."
"He knew better than to think that the twins had truly given him the choice for some tactical reason. Odds were it was just another move in their endless power struggles. He had no doubt that they would try to sway him in one direction or the other."
"He was not looking forward to the result of his decision."

$ arzylDialogueAvailable = True
$ whitescarDialogueAvailable = True
$ whitescarDialogueStage = 1
$ arzylDialogueStage = 1

return

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

label paperwork_sabotage:

scene bg6 with fade
show rowan necklace neutral at center with dissolve

"With a sight, Rowan eyed the seemingly never-ending pile of paperwork before him."

if week < 80:
    "It was deceptively small now, but with time, Rowan had no doubts it would grow large enough to tower over him."
    
else:
    "As the twins realm expanded, so did the paperwork, and he knew it would only get worse with time."

"And yet there was no escaping it. Every half-competent commander knew wars were won and lost by the small details hidden inside of them."
"Just like the ones he just noticed in a seemingly simple request from Cla-Min, that now laid on his desk."
"She wanted to send a caravan south from the Rosaria portal, but since the area it would pass banned goblin traders, she wanted half a dozen orcs to act as caravan guards as she sneaked through it."
"It was a reasonable request, if not for the fact Rowan was fairly certain the caravan would be slaughtered. He knew the region Cla-Min wanted to send it through, and he was familiar with the lord who oversaw it. During the war, the two of them worked together briefly, not so long after Rowan was named general."
"If he thought hard, he’d probably remember his exact title and full name, but neither his titles nor his face was important at the moment. What mattered was the intellect and ruthlessness, and his devotion to Solansia's most hardline doctrines." 
"He ruled over a small fief, but did so efficiently, and without mercy. During the military campaigns, he always advised for the most radical course of action – and often made a very compelling point."
"Rowan never liked him, but he knew for a fact there were no bandits or orcs in his lands. The noble did not tolerate opposition, and all who entered his lands met a swift end."  
"A goblin caravan accompanied by a detachment of orcs would not pass his fiefdom unnoticed. Once they enter his lands, they would not emerge from it."  

if serveChoice == 4:
    jump rerouteCaravan
    
else:
    "It would be such a simple thing to grant Cla-Min’s request, and claim ignorance once the Caravan would no doubt end up assaulted and destroyed. Neither Cla-Min nor Jezera would have any right to blame him for the unexpected loss."
    "After all, how could he have known any better?"
    "It wasn’t often he got a chance to sabotage the twin’s efforts just by doing his job only adequately. The question was - could he afford to do so right now?"

    menu:
        "Grant Cla-Min’s request, send the caravan to its doom.":
            $ released_fix_rollback()            
            "One signature, and the orc and goblin lives were now forfeit."
            if avatar.corruption > 60:
                "Rowan chuckled to himself. He spent half his adolescent life learning the sword so he could slay beasts like that in the name of Solansia, and just now he killed half a dozen of them with his pen only."
                "Who could have known the most efficient way of killing his enemies was by being intentionally inept?"
                "It was so much cleaner too!"
                "He chuckled again, then put the request on the finished pile and reached for the next one. With luck, maybe there would be another request like that."
            else:
                "He furrowed his brows as he stared at his signature. He spent half his adolescent life learning the sword so he could slay beasts like that in the name of Solansia, and just now he killed half a dozen of them with his pen only."
                "… The bards did sing the pen was mightier than the sword. Guess there was something to it after all."
                "He sighed to himself, then put the request on the finished pile and reached for the next one."
            $ change_base_stat('c', -5)
            $ change_treasury(-50)
            $ castle.buildings["barracks"].troops -= 6
            return

            
        "Order Cla-Min to reroute the caravan.":
            $ released_fix_rollback()
            label rerouteCaravan:
            if serveChoice != 4:
                "He stared at the parchment for a long time. Going out of his way to save orc lives…"
                "But he had no choice. If the twins’ army did not perform adequately, he would be blamed for it, no matter what external circumstances led to such results."
                "He needed more time, as much as he loathed to admit it."
            else:
                pass
            "He wrote “Request Denied” on Cla-min’s letter, then added “Route dangerous. See me for alternatives.” underneath."
            if serveChoice == 4:
                "Cla-Min would no doubt be grateful for his diligence. The twins were lucky they had him on their side."
            else:
                "At least Cla-Min would be grateful for his intervention. If nothing else, keeping her happy might come in useful later on."
            $ all_actors['cla_min'].relation += 5
            return









