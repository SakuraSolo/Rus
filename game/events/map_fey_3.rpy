init python:

    event('the_tavern_and_the_dragon_ogre', triggers='map_expl', conditions=('week > 16', 'world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)  

label the_tavern_and_the_dragon_ogre:

scene black with fade

"Rowan let out a sigh and lifted his hand up to his forehead, wiping the sweat that beaded across his brow as he shielded his eyes from the encroaching twilight. He had managed to reach a small inn at the base of the mountaintop, somewhere he could stay for the night."

scene bg21 with fade

"The inn was small and quaint, and as Rowan pushed open the door he had to lower his head to pass beneath the undersized door, wiping his feet on the snow-shod mat before entering."
"He was immediately blasted with a wave of warm air and raucous laughter. Pulling his cloak tighter about himself, Rowan funneled into the room."
"The small inn was packed: mostly Dwarves from the local mines, as well as a few more exotic visitors. Rowan seemed to be the only human in the joint."
"He strode up to the barkeep, who shot him an inquisitive eye."

show rowan necklace neutral at edgeleft with moveinleft

ro "Double-sizer Stonebreaker, and keep it frothy."

"The Dwarf behind the counter guffawed and nodded, lifting a hefty mug onto the bartop and filling it to the brim with effortless efficiency. He then slid the mug to Rowan’s hand, who tossed him a few silvers."
"Now properly armed for the evening’s adventures, Rowan took his seat at a nondescript table near the corner. Plopping down into the wooden chair, he sipped at his mug, wiping the suds from his lips as he observed the inn’s proceedings with a spectator’s eye."
"His gaze was drawn towards a particular being of draconic nature. Near the center of the room, a tall Dragon Ogress roared with laughter alongside a small table of Dwarven traders and a lone, ebon-armored human who seemed to be their bodyguard."

show ygriss neutral at cliohnaright with dissolve

ygris "And here I thought you said wouldn’t back down from a challenge! What, is the mere thought of my heavy teats mashed in your face enough to unman you?"

"The table erupted into laughter as the Dwarves clapped the unhappy-looking warrior on the back. The Ebon warrior, for his part, did his best to not look the Dragon Ogress in the eyes, calmly sipping from his drink as she pressed her muscular upper body against him."

ygris "Don’t think you can handle me, boy? Once you’ve had a Dragonness, you’ll never go back. When you’ve got a Spearwife guarding your flank, you’ll always be secure."

show rowan necklace happy at edgeleft with moveinleft

ro "Hah! With a woman like you on his side, I think more than just his flanks are secure."

show ygriss happy at cliohnaright with dissolve

"Rowan grimaced to himself as the Dragon Ogress’ head turned to look straight at him. A curling, draconic smile grew on her face. She let out a belly laugh, tilting her horned head skyward as she bellowed."

ygris "Ah {i}ha{/i}! See that, boy? You waited so long to say yes, you’ve now got some competition for my attention!" 

"She waddled up to Rowan, her four, reptilian legs moving smoothly across the ground as she approached. The large-breasted half-dragon leaned forward, displaying her bounteous cleavage as she quirked a haughty eyebrow." 
"Her smile was broad, it would have been almost friendly if she weren’t the size of a giant. She took Rowan by the wrist and half-dragged him back to the table. She pointed at the empty seat next to the Ebon Warrior. Rowan tried to beg off, but she gave him a hard stare."

menu:
    "Tell her you have no interest.":
        $ released_fix_rollback()
        show ygriss neutral at cliohnaright with dissolve
        "Rowan did his best to hold an awkward smile, raising his hands up as if to beg off an unsavory action. The crowd of Dwarves burst into drunken laughter at the Dragon Ogress’ embarrassment. Her face colored, but she recovered her composure quick enough."
        ygris "Ha! Are there no real men in this tavern? Away with you, boy! Like as not you’re even less endowed than this black-armored milksop sitting next to me!"
        ygris "Barkeep! Another round, and make sure this ebony git gets a splash of real liquor for once!"
        "The crowd shared a laugh, and even Rowan smirked at the woman’s effortless braggadocio. Taking this as his cue, Rowan backed off, returning to his table and finishing a few more mugs off before calling it a night."
        return
        
    "Take a seat":
        $ released_fix_rollback()
        "Rowan shrugged and took the offered seat, settling into the cushioned chair under the watchful gaze of the fiery Dragon Ogress. The ebon warrior seemed visibly relieved that he was willing to pick up the slack with the insatiable woman."
        ygris "That’s more like it. {i}Barkeep{/i}! A drink for the only man in this inn with balls!"         
        ro "The name’s Rowa-"
        $ ygrissName = "Ygriss"
        ygris "I am Ygriss! Spearwife seeker! You should feel honored, human: there aren’t many Spearwife seekers these days, even fewer looking for a {i}human{/i} mate!"
        "Deciding that discretion was the better part of valor in this instance, Rowan smiled and nodded. A new drink was thrust into his hands by the grinning Ogress and he accepted it, downing its contents as he heard the tall tales and laughter that arose from the rowdy group." 
        "After several more drinks, Rowan inquired in a not-so-subtle fashion about the Dragon Ogress. The woman, sitting back on her scaly haunches next to Rowan, cast a sly look in his direction. She winked at him in a way that Rowan assumed she intended to be seductive."
        ygris "My kind are simple and uncomplicated, Rowan. I am a Spearwife seeker, and I am in search of a proper husband."
        ro "You’re not very likely to find that kind of quality in this crowd, my lady."
        ygris "Hah! Maybe not. But I have long since lowered my standards; I am in search of a {i}human{/i} husband."
        "The Ebon Warrior squirmed in place at Ygriss’s statement. The man took this as his opportunity to bail, giving a half-hearted excuse before all but fleeing the scene. The Dragon Ogress’ eyes played across his retreating form before refocusing her attention on Rowan. "
        ygris "Shame. Seems now you’re the only human left."
        ro "Don’t worry, I was the only man in the room, anyway."
        "A chorus of jeering laughs erupted from the drunk Dwarves. Rowan saw Ygriss’s brow rise, and her eyelids lower. A sultry smile played across her lips."
        ygris "Prove it."
        ro "How?"
        ygris "Kiss me. Show me you’re real man. A man who can be with a {i}real{/i} woman."
        "Rowan considered the offer for a moment. Odd anatomy aside, Rowan was already married. and {i}one{/i} wife was altogether too much for him to handle as it was." 
        "That being said, Ygriss did not seem to be the type to take kindly to being denied. And Rowan was {i}far{/i} drunker than he had anticipated being when he first walked into the inn."
        
    "Buy the Dragon Ogress a stonebreaker and take a seat":
        $ released_fix_rollback()
        ro "-And a Double-sizer Stonebreaker for the lady!"
        ygris "What, are you trying to embarrass me, boy? Stonebreaker’s got all the impact of a light spring breeze upon my liver."
        ro "Barkeep! Make it two of them, for the sake of the lady’s liver."
        ygris "Hah!"
        ro "The name’s Rowa-"
        $ ygrissName = "Ygriss"
        ygris "I am Ygriss! Spearwife seeker! You should feel honored, human: there aren’t many Spearwife seekers these days, even fewer looking for a {i}human{/i} mate!"
        "Deciding that discretion was the better part of valor in this instance, Rowan smiled and nodded. A new drink was thrust into his hands by the grinning Ogress and he accepted it, downing its contents as he heard the tall tales and laughter that arose from the rowdy group." 
        "After several more drinks, Rowan inquired in a not-so-subtle fashion about the Dragon Ogress. The woman, sitting back on her scaly haunches next to Rowan, cast a sly look in his direction. She winked at him in a way that Rowan assumed she intended to be seductive."
        ygris "My kind are simple and uncomplicated, Rowan. I am a Spearwife seeker, and I am in search of a proper husband."
        ro "You’re not very likely to find that kind of quality in this crowd, my lady."
        ygris "Hah! Maybe not. But I have long since lowered my standards; I am in search of a {i}human{/i} husband."
        "The Ebon Warrior squirmed in place at Ygriss’s statement. The man took this as his opportunity to bail, giving a half-hearted excuse before all but fleeing the scene. The Dragon Ogress’ eyes played across his retreating form before refocusing her attention on Rowan. "
        ygris "Shame. Seems now you’re the only human left."
        ro "Don’t worry, I was the only man in the room, anyway."
        "A chorus of jeering laughs erupted from the drunk Dwarves. Rowan saw Ygriss’s brow rise, and her eyelids lower. A sultry smile played across her lips."
        ygris "Prove it."
        ro "How?"
        ygris "Kiss me. Show me you’re real man. A man who can be with a {i}real{/i} woman."
        "Rowan considered the offer for a moment. Odd anatomy aside, Rowan was already married. and {i}one{/i} wife was altogether too much for him to handle as it was." 
        "That being said, Ygriss did not seem to be the type to take kindly to being denied. And Rowan was {i}far{/i} drunker than he had anticipated being when he first walked into the inn."

label ygrissBarMenu:

menu:
    "Tell her you have a wife" if ygrissWife == False:
        $ released_fix_rollback()
        $ ygrissWife = True
        ro "Look, while I appreciate the offer-"
        ygris "It wasn’t an offer, sexy thing. It was a {i}command.{/i}"
        ro "I’m married. I wasn’t trying to lead you on, I just didn’t know how to tell you before this."
        ygris "You’re married?"
        ro "Yes."
        ygris "...And? Does the bloodflow to your cock dry up the moment you are free from your wife’s clutches?"
        show rowan necklace shock at edgeleft with dissolve
        ro "What? I-"
        "The husky Ogress tilted her head back and let out a hearty belly laugh."
        ygris "Hah! You’ve been unmanned by a wedding band! Your wife is away, dearest Rowan. Why not take the opportunity? It’s presenting its fertile rump to you!"
        show rowan necklace aroused at edgeleft with dissolve
        "Rowan’s cheeks colored at the assertion. Was he even sure what he wanted to do?"
        jump ygrissBarMenu
        
    "Accept the invitation":
        $ released_fix_rollback()
        jump ygrissBarSex

    "Gently turn her down":
        $ released_fix_rollback()
        show rowan necklace neutral at edgeleft with dissolve
        "Rowan shook his head back and forth. No, he could not do that to Alexia, despite everything that’s happened."
        ro "I… appreciate the offer. If it was under different circumstances I’d jump at the chance. But I’m going to have to decline."
        ygris "Heh, a man with principles… what a rare thing in this day and age."
        ygris "Fine, Rowan. But do not think that this ‘business’ between us is concluded. You and I still have much to… discuss."
        "Rowan watched as Ygriss stood up and made for the door, casting a long gaze behind her as she hovered at the entrance."
        ygris "Our paths shall cross again. I am certain of it."
        hide ygriss with moveoutright
        "And with that, she was gone. Rowan calmly finished off his drink and left. He slept better that night than he had in weeks."
        return

    "Explain that you just aren’t compatible":
        $ released_fix_rollback()
        show rowan necklace neutral at edgeleft with dissolve
        "Rowan grimaced at the prospect of confronting the opinionated Dragon Ogress with his denial, but she really had left little for him in the way of outs."
        ro "While I… appreciate the gesture, I’m going to have to decline."
        ygris "Oh? Got your pants so tight about your waist you cut off all circulation to your naughty bits, eh?"
        ro "No, I just… don’t think we’re that compatible."
        show ygriss angry at cliohnaright with dissolve
        "A scowl built upon the Dragon Ogress’ face. Her eyes flashed, and for a moment Rowan worried that she was going to snort and charge at him like a enraged bull cornered in a pen."
        show ygriss neutral at cliohnaright with dissolve
        ygris "Barkeep, a last drink for the road. I don’t think I’ll be staying much longer. There’s nothing for me here."
        "Rowan shifted uncomfortably in his seat as the Dragon Ogress spared him the barest glance out of the corner of her eye, before snatching her final mug and rumbling out of the inn. He could hear her muttering obscenities under her breath as she passed by him once more."
        "The inn door slammed shut with a disconcerting finality behind her as she disappeared into the night. ...Well that could have gone better."
        return


label ygrissBarSex:

scene black with fade
show ygriss aroused behind black
show rowan necklace naked aroused behind black

"What the hell. With everything else that has gone wrong in Rowan’s life, it’s not like this was exactly on par with a world-ending threat from Demons. Hell, this wasn’t even the oddest proposition Rowan had gotten in the last week." 
"Perhaps it was the alcohol simmering with a delectable, warm heat in his belly, or perhaps it was just the pent up frustration of a world that was slowly falling apart around him. Either way, Rowan’s blood was up."
"He smiled, leaning forward as Ygriss’s lips stretched wide into a triumphant grin. They came together, the larger Dragon Ogress leaning down at the same time Rowan lifted up." 
"Their lips met, their tongues circling around one another’s as the stolen kiss quickly turned into a drunken makeout session. The patrons of the bar cheered as the two threw their arms around one another, their eyes ablaze with lust as their hands began to wander. "
"Rowan reached out and took hold of one of her large tits, feeling the weight of them in his hands as his tongue moved in competitive circles around Ygriss’s own. Her lips were moist, her tongue long and draconic." 
"The Dragon Ogress laughed, reaching down with a hand to unsubtly grope at his nethers. Rowan grimaced as her solid fingers closed clumsily around the erection hardening in his pants."
"The randy Dragon Ogress let out a roar of approval. Before Rowan could so much as utter out a complaint, she’d taken him by the shoulders, lifting him bodily off the ground so that his feet dangled in the air." 
"Taking his outfit by the scruff of the neck, she pulled, tugged, then ripped. In one, smooth movement Rowan was left naked. The force of Ygriss’s pull all but split his outfit down the middle, with his shoulders serving as the split point on either side." 
"Rowan cursed, but had little time to recover, as the Dragon Ogress tossed him atop the drinking table, spilling drinks as the Dwarves let out hooting calls before clearing to safety out of the blast radius."
"Rowan scrambled to his feet atop the beer-slick table, his head woozy and the room spinning. He had downed far more alcohol than he remembered. Judging from Ygriss’s bright red face and wolfish grin, so had she."
"The Ogress slinked forward, her reptilian feet and toed claws clicking across the stone floor as she undid the straps around her bra, letting her breasts spill forth."
"She untied her loincloth, allowing it to drop to the floor like discarded rubbish as she ascended the step to the tabletop. Her eyes were ablaze with wanton need, and Rowan could feel a building weight in his tongue as he stared at her."
"As strange and otherworldly as she may have been, she was also beautiful. With a grace that belied her size, the Dragon Ogress pivoted on her back legs and did a half-circle, presenting her sizable hindquarters for Rowan’s viewing pleasure."
"Her ass was huge, her thighs thick like a broodmother’s. Rowan’s vision was obscured standing directly behind her, like a solar eclipse of Dragon cunt. Her bright, pink pussy lips were parted, dribbling feminine fluids down her leg as she perked her hips up for him."
"A waft of heated pheromones drifted up and blasted Rowan full in the face, and he nearly swooned from the scent of it. Something primal compelled him onwards, and before he had time to take stock of what he was doing Rowan had buried himself deep in Ygriss’s box."

ygris "{i}Mmmmh{/i}! Yeah, get in there, stud. Eat me out till you’re addicted to the taste of Dragon Ogress juices!"

"Rowan blushed, but obliged. Redoubling his efforts, he tongue-fucked her cavernous gorge till his tongue was straining to reach deeper. He tasted sopping-wet nectar as the beastwoman’s lust built up." 
"Rowan planted a hard {i}spank{/i} across her ass and the Ygriss let out a tortured squeal. By now, most of the patrons were giving catcalls and yelling suggestions, all of which Rowan ignored to focus on the Dragon Ogress’ ever-wettening puss."
"Rowan mashed at her muff with all the enthusiasm of a frenzied shark amidst a school of fish. He lapped at her insides, his tongue licking in long, languid strokes before diving deep and shortening his licks to breakneck speed." 
"Ygriss let out a booming cry of pleasure and stomped her foot, rattling the table they were on. Rowan pulled back, his cheeks splashed with the squirting wetness coming out of Ygriss’s cooter."
"He could no longer contain himself. Reaching out with his hand, Rowan slid the better part of his hand into her clenching pussy, eliciting a cry of joy from the Dragon Ogress who turned partially around to stare at him." 
"He felt the warm contractions of her cunt around his hand as he slathered it in her fluids, retreating only after lingering for a moment her large clit. He lubricated his cock in her accumulated juices, finishing with a flourish and a spank on the ass."

ygris "Take me… do {i}it!{/i}"

"Rowan heeded her breathless command, though he did not respond verbally. Taking himself in hand, Rowan positioned himself against the Dragon Ogress’ hind, his hands wrapping around her scaly hips as his cock teased her pink slit." 
"The Dragon Ogress wiggled her bum and tried to step backwards, nearly knocking Rowan off his perch on the table. He managed to recover, delivering a second, cautionary {i}spank{/i} to her ass to remind her who was taking the lead in this endeavor."
"Rowan pressed into her interior, his cock sliding in deep as her large pussy swallowed him into its velvety embrace. Rowan let out a deep moan as the clinging heat and snug wetness sucked him in." 
"Without thinking, he thrust as deep as he could, his balls clapping against her flank just as he pulled back to spear her again. The Dragon Ogress let out a snarling laugh, plumping her hips up to give Rowan a better position with which to fuck her thoroughly." 
"Taking this as his cue, Rowan began to move once more. He set a quick tempo, the wet schlicks coming from her sloppy cunt only further enunciating the illicit public dalliance as the cheering Dwarves egged him on."
"Rowan grunted, smashing his hips against the Dragon Ogress as she wiggled and squirmed in his grasp. Despite her imposing size, the Dragon Ogress seemed content to be in the breeding position now that Rowan had taken charge." 
"She let out a heady moan, tossing her hair across her shoulders as she thrust back at him. The hot, wet fuck got hotter and wetter. Rowan could feel the weight of the Dragon Ogress as he rammed his thick cock into her, the loud squelches growing ever more overt."
"Ygriss moaned, mauling at her tits with her hands, pinching at her nipples when Rowan slid to the hilt.  His hands found their way to the flare of the Draconic woman’s waist and began to pull her down with each piston forward he made, forcing her to meet him halfway." 
"The result was a wet, rhythmic metronome of thrust and retreat, the air growing heavy with the scent of sex and pheromones. Rowan grimaced at the sensitivity: her cunt was like a cock-vacuum. No matter how hard he pulled, it always seemed to try to suck him back inside." 
"Her strong vaginal muscles clenched with every thrust, and gripped him with every pull back. It was heaven, a burst of concentrated pleasure that he could no longer resist even if he wanted to."
"The Dragon Ogress’ dripping reply to Rowan’s thrusts became a sudden torrent as she squirted onto the table, basting Rowan’s legs in her sexual orgasm as she roared and reared back on her hind legs." 
"The table shifted beneath them with sudden force as all the weight shifted to one side. Rowan nearly toppled over but Ygriss slammed her feet down, reasserting the table’s stability. Another roar of approval arose from the assembled Dwarves." 
"The tabletop was soaked in a mixture of beer suds and Dragon cum. Rowan was reaching his peak. Every ounce of strength was devoted to stuffing as much of his dick into Ygriss’s pussy as possible, ramming so hard that he left ass-quakes on her cheeks from the thrust."
"Ygriss’s cunt stretched around his thickness, dripping its delectable honey across Rowan’s toes. Her front legs, already unsteady, collapsed under her, but she managed with his help to maintain her weight on her back legs as she submitted to his final, thrusting climax."
"The warrior’s pace picked up considerably, and he felt a building pressure in his groin. Just as he reached his climax, Ygriss turned around again, flashing him a wide smile as she quirked an eyebrow."

ygris "Inside, husband!"

"Responding as if on command, the warm ecstasy inside Rowan rushed out in a tremendous spurt, squirting globs of thick white cum into the Dragon Ogress’ clenching pussy. Ropes of creamy spunk fire inside the creature, and she roars in lustful approval." 
"Her hungry twat drinks down the seed with gusto, drawing it out of Rowan even as it milked him for more. By the time he was finished, Rowan was panting and spent, covered in sweat and empty of breath."
"The cum glazed lips reluctantly released Rowan’s withdrawing prick. {i}Schllurk{/i}, said the fucked cunt in belated goodbye to the cock that had made a creamy mess of her insides." 
"Remembering at least some of his former dignity, a butt-naked Rowan sheepishly descended the table to the ground. Several of the Dwarves proffered a ribald insult or two about ‘finishing what he started’, but Rowan brushed them off." 
"Ygriss, for her part, basked in the post-coital bliss of their sex. Far from descending the table, she allowed her body to collapse down upon it, rattling the table and nearly breaking it from her weight." 

scene bg21 with fade
show rowan necklace naked at edgeleft with dissolve
show ygriss happy at cliohnaright with dissolve

"Rowan saw the pooling puddle of cum leaking from her well-used pussy as she tilted her ass to one side and reclined against the table. She held his eyes with her own."

ygris "You have done well this day, husband of mine."

ro "I’m not your husband."

ygris "The seed leaking from my womanhood would seem to indicate otherwise."

ro "..."

ygris "{i}Ha!{/i} Look at your face. You haven’t even the common decency to be proud of your accomplishment: few mortals can make a Dragon Ogress cum as hard as you did."

ro "I’ll make sure to add it to my list of ‘accomplishments.’"

ygris "Mmmm, you should. "

show rowan necklace neutral at edgeleft with dissolve

"Rowan hurriedly re-dressed, feeling suddenly uncomfortable with the eyes in the room. Their nightly entertainment finished, most of the Dwarves turned back to one another, though a few inquired to Ygriss as to how long she’d need the table."

ygris "Our paths will cross again, Rowan. I know it: a husband like you does not come around often."

"Rowan did his best to ignore her sultry smile as he shouldered his pack and made for the door."

return
