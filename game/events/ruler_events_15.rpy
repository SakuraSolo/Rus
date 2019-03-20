init python:

    #Solansia's First Dream
    #If Rowan suggested feudalism society, this event triggers on week 40. (# high priority to force triggering around week 40)
    event('solansia_s_first_dream', triggers="week_end", conditions=('week >= 40', 'society_type == "feudalism"'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Kharos's First Dream
    #If Rowan suggested might society, this event triggers on week 40.
    event('kharos_s_first_dream', triggers="week_end", conditions=('week >= 40', 'society_type == "might"'), group='ruler_event', run_count=1, priority=pr_ruler_high)


label solansia_s_first_dream:
#Solansia's First Dream
#If Rowan suggested feudalism society, this event triggers on week 40.

scene black with fade

"Someone was ahead of him, moving through stone passageways that were strangely familiar. Rowan followed, desperate to catch up with the figure, but always he was just barely keeping up."
"Sometimes he lost sight of them, but minutes later he'd see them just turn a corner ahead of him leading him deeper and deeper into the labyrinth."
"There was a feeling at the back of his mind that whoever it was that he was following that they wanted him to follow. He glanced back, then wished he hadn't."
"A creature was also following him. It had the look of a demon about it, but like the stranger leading Rowan forward, the form was indistinct and impossible to define."
"Rowan redoubled his efforts, both to reach whoever was his guide and to escape whatever it was that sought him."
"A great cavern opened up before him, so sudden was its appearance that Rowan wasn't sure if he'd actually stepped into the room or it had just come into existence around him. There was a great crevice below, upon which he could see the stranger stood waiting for him."
"The man descended down, but with each step a strange headache at the back of his mind grew in intensity. Something about this place was alien and dangerous. Yet he couldn't stop, only press on deeper and deeper."
"The crevice loomed before him, radiating heat and the source of that strangeness. No, not strangeness, instincts, emotions, his deepest desires and drives. Rowan reeled back, rejecting the raw chaos before it engulfed him."
"Someone was at his side, looking towards the crevice."

show rowan necklace shock at midleft with dissolve
show village elder neutral at midright with dissolve

ro "Elder?"

el "That is our darkness, something within humans that we will never fully escape from. Yet we are protected. The goddess saw fit to save and preserve us, so that we might live in peace and prosper."

show rowan necklace neutral at midleft with dissolve

"The pain in Rowan's head shifted and he felt nauseous and dizzy. What was happening? Why was the elder here of all places?"

el "All of those born of chaos can rise above it, no matter who or what their origins were. Everyone can be saved. This is the gift that Solansia has given us."

"The creature that was following him was close now, very close. No, it wasn't one, there were two! They were breathing down his neck and their claws were reaching for him! Rowan stumbled backwards, desperate to get away."

ro "Ghuh..."

hide rowan with dissolve
play sound "music/SFX/BodyfallDirt.ogg"

"He was falling, falling, falling...."

scene black with fade

"Rowan opened his eyes and glanced around. A moment later he realized he was resting in his bedroom in Bloodmeen, having returned from the week's expedition. There was still no sign of dawn, but the candles had all burned out."
"He put a hand to his face and felt cold sweat on his brow. Then turned his thoughts back to the nightmare he'd awoken from moments before. The labyrinthine passages of ancient stone and the massive crevice they'd contained, everything was still so vivid."

show rowan necklace naked concerned behind black
ro "(Everyone can be saved.)"

"Why exactly had that stood out in his mind? For that matter, why was his mind turning to this now of all times? These thoughts plagued him for the rest of the night."

#rowan loses a little corruption
$ change_base_stat('c', -2)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label kharos_s_first_dream:
#Kharos's First Dream
#If Rowan suggested might society, this event triggers on week 40.

scene bg1 with fade
show rowan intro happy at edgeleft with dissolve

ro "Good job, that's the first time you've hit all three targets in a row."

show rowan intro happy at center with moveinleft

"He moved past his first student, to check on the second."

ro "Well that's no where near the target. What did I say about how to nock the arrows? Yeah, that's right. Try again. There you go, that was much closer. Keep at it, and remember the feather always points away from the bow."

#if Helayna was Rowan's student
if helaynaTitle == "teacher":
    show rowan intro happy at edgeright with moveinleft
    show helayna neutral at center with dissolve
    ro "Helayna? Let's see you take a... where is your bow?"
    show rowan intro neutral at edgeright with dissolve
    ro "Why are you wearing..."

    #If Helayna has agreed to stay with Rowan (instead of escaping)
    if helayna_escape_method == 'rowan':
        show helayna 2 happy at center with dissolve
        hel "Isn't this your favorite outfit though?"

    #if Helayna is visible
    hide helayna with dissolve

#rejoin
scene bg1 with sshake
show rowan intro neutral at edgeright with dissolve

ro "Ugh. (My head....)"

show village elder happy at center with dissolve

ro "Oh, old friend. I'm feeling a little under the weather, would it be alright if I asked you to watch my students while I-"

el "It won't be enough."

ro "I'm sorry?"

el "The greatest general of the realm can't even train a force to protect his home."

ro "What are you talking about? We're at peace! The war is over!"

el "War is never over. Bandits or monsters could attack at any time, you could have taught them how to defend themselves."

ro "Solansia's laws clearly forbid that and the nobility would never-"

el "Exactly, they'd rather let anyone die than allow a dirt general to threaten their rule with even the smallest of militia."

ro "Old friend? Why are you saying all this?"

scene bg4 with redflash
show rowan intro neutral at edgeright with dissolve
show village elder wounded at center with dissolve

el "You could have stopped this."

ro "What?"

"All around him the village had changed, the buildings were ablaze and the people were gone. Panic and thoughts of his wife flooded his mind."

el "If the people could fight, if they had proper weapons and the skills to use them, your skills, then this village wouldn't have burned."

ro "Gha!"

"Now his body seared with pain, pain he had always felt but somehow didn't notice before now."

hide rowan with redflash
play sound "music/SFX/BodyfallDirt.ogg"

"It was too much, he felt his legs give out from under him and he fell down, down into blackness."

scene black with fade

"Rowan opened his eyes and glanced around. A moment later he realized he was resting in his bedroom in Bloodmeen, having returned from the week's expedition. There was still no sign of dawn, but the candles had all burned out."
"He put a hand to his face and felt cold sweat on his brow. Then turned his thoughts back to the nightmare he'd awoken from moments before. The village blazing as his friend accused the nobility and Solansia for being responsible for it, everything was still so vivid."
"Thoughts of what might have been and how things could have played out differently plagued him for the rest of the night."

#rowan gains a small amount of corruption
$ change_base_stat('c', 2)
return
