init python:

    #Witnessing the old ways 1
    event('witnessing_the_old_ways_1', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #The Riddle of the Dead
    event('the_riddle_of_the_dead', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #The Nyverian Wisp
    event('the_nyverian_wisp', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label witnessing_the_old_ways_1:
#Witnessing the old ways 1

scene bg32 with fade
show rowan necklace neutral behind bg32

"The bogs and marshes of Rosaria always made Rowan feel uneasy. He imagined their dreary nature triggered a subconscious response that lingered until he set foot into greener pastures. Today the reason for his unease was far more tangible; he heard ominous chanting."
"Rowan could not mark the language of the incantations, but they seemed of dark intent to him. Honing in closer it felt as if the air came alive with a mischievous character, and though he had no esoteric knowledge he was certain something was being invoked. "
"Rowan saw the source of chanting: two female forms lit by eerie purple lamplight, covered in smoke rising from censers they held, and dancing around a stone altar. Rowan could not make out further details from his vantage point. He would need to venture closer."

menu:
    "Try to sneak closer.":
        $ renpy.fix_rollback()
        #move silently check DC15
        if check_skill(15, 'move_silently')[0]:
            #succeed
            jump witchSneak
        else:
            #fail
            jump witchSneakFail

    "Don’t risk it and escape.":
        $ renpy.fix_rollback()
        "Rowan was a fighter and a strategist. He was aware of his strengths, but also his glaring weaknesses. He had no real defense against magic, and even less so against a potential enemy he could not even perceive. He cautiously crept away from the scene."
        return

################################################################################

label witchSneakFail:

"His approach went well until a rather large twig snapped. Rowan attempted to dart behind a tree before he was spotted, but hit a dozen branches getting there. There was no way in all of the hells that his position wasn’t compromised."

$ witchName = "Unknown Female"

witch "Conjure a black dart, sister! I will offer my sacred red substance - may the slumbering demons of the forest itself come to our aid!"
witch "Agh Draghul Elas! Rise up from the womb of eternity with poisonous intent!"

"Rowan drew his sword but greatly disliked his odds. One of the naked forms was cradling a black bolt of writhing energy she drew from the ground into her hands. The other had cut her hand and was offering her blood as a means to conjure demonic spirits."

menu:

    # TODO
    #"Fight!":
     #   $ renpy.fix_rollback()

    "Run for it!":
        $ renpy.fix_rollback()
        "Rowan’s one thought was the thing the female had called a black dart. That would be flung his way soon, and if it hit him his odds of survival were slim. “Fly with vengeance!” he heard a voice scream behind him. This was it, he only needed to dodge once!"
        #dodge check DC15
        if check_skill(15, 'dodge')[0]:
            #succeed
            "At this pace only instinct existed. Rowan zig-zagged right, then left, and then pushed left again. Something shot past him at an unnaturally fast speed and buried itself in a tree in front of him. The tree became black almost instantly. Rowan had successfully dodged."
            "Inhuman screams of rage started to screech in the distance. Rowan wasn’t too worried - the summoning of spirits was known to be a slow practice. When he saw the sun shine through the trees he knew he had made it. He sighed in relief."
            return
        else:
            #fail
            "Rowan intended to zig-zag as a diversive ploy but was flung forward instead. Something had hit him in the shoulder and had at least partially breached his pauldron. He screamed out in agony as poison seeped into his skin."
            "Poison or not, he knew his only chance of escape lay in running for his life. When inhuman screams of rage started to screech in the distance Rowan wasn’t too worried - the summoning of spirits was known to be a slow practice. "
            "When Rowan saw the sun shine through the trees he knew he had made it. His poor judgement would cost him, however. The poison wasn’t fatal or too severe, but it would hamper his progress this week greatly."
            #gain 2 wounds for the week
            $ add_effect(MultiEffect('Wound', 'neg', (('strength', -2),), 1))
            return

################################################################################

label witchSneak:

"Rowan skillfully closed the distance. From his new perspective he realized how dire the situation was. The women were elf maiden of the dreaded sisterhood of Nyx, of whom Rowan had heard tales so horrible he regarded most of them as fancy. Not anymore."
"The stone altar was home to a naked man bound by leather straps. He was gagged, and his entire skin was ornamented with fiendish-looking symbols. The man looked around himself in sheer terror, yet ironically had a rock hard erection. "
"As the chanting continued Rowan saw - for the merest moment only - that which the sisters were calling into our world. Sylvan creatures that were part tree, part woman, and part demon danced to their hymns. Tentacles and arm-sized erections swung every which way."
"Rowan pieced the information together. The sisters would copulate with the Sylvan spirits, that much was clear. The man he could not place, however. Would he be sacrificed, or was he merely to be used as a sexual tool? The latter Rowan could live with, the first..."
"Rowan realistically weighed his options. The sisters were armed with daggers and likely possessed at least some magical ability. The spirits they were conjuring into our world had not fully manifested, but that was no guarantee that they could not retaliate."
"The odds were stacked against Rowan. And even if he took them, what was he supposed to do? Cold-bloodedly cut the two maidens down? What if they were just planning to have some fun with the poor soul? None of this sat right with Rowan."

menu:
    "Silently make your escape.":
        $ renpy.fix_rollback()
        "Rowan saw too many variables; this would not end well for him. Whatever fate held in store for the man on the altar, it wasn’t worth risking his death (and in doing so condemning Alexia to a lifetime under Andras’ care). He slowly crept away from the ominous scene."
        return

    "Try to save the poor soul":
        $ renpy.fix_rollback()
        jump witchNegotiate

################################################################################

label witchNegotiate:

"Rowan took a deep breath. The play he intended to make was a risky one, but it was better than storming in sword in hand. He exhaled. Then he walked towards the sisters of Nyx."

ro "..."

$ witchName = "Crimson-haired sister of Nyx"

witch "Have you come to pay your respects?"

$ witchName = "Raven-haired sister of Nyx"

witch "To fuck us in the honor of the Spirits of the Old Ways?"

$ witchName = "Crimson-haired sister of Nyx"

witch "Look at those serious eyes, sister. He is not here to deliver his seed..."

$ witchName = "Raven-haired sister of Nyx"

witch "I fear you are correct. He comes to bargain for this pitiful creature."

ro "May I know what you intend to do with him?"

$ witchName = "Crimson-haired sister of Nyx"

witch "We will use his energy to empower the ritual."

$ witchName = "Raven-haired sister of Nyx"

witch "Orgasm after sweet orgasm… he’ll love it."

ro "But will he survive?"

witch "This ritual? Most likely. "

$ witchName = "Crimson-haired sister of Nyx"

witch "But sooner or later the expanse of energy will claim its toll."

$ witchName = "Raven-haired sister of Nyx"

witch "Lament not for his fate. He’ll go out in a blaze of orgasmic glory, that I can guarantee."

$ witchName = "Crimson-haired sister of Nyx"

witch "And now we lay a question at your feet, handsome stranger. Are you a friend of the Old Ways? "

$ witchName = "Raven-haired sister of Nyx"

witch "By which my sister means to ask: do we get to fuck and suck as we had intended, or shall events take a turn for the darker?"

"Rowan felt for the poor soul. Whatever his cock said on the matter, his eyes contradicted; he did not wish to be where he was. He could bargain with the sisters and perhaps secure his release, but it could backfire and antagonize them. Them and their demonic forest spirits."

menu:
    "Bargain for the release of the victim.":
        $ renpy.fix_rollback()
        #diplomancy test DC18
        if check_skill(18, 'diplomacy')[0]:
            #succeed
            "Rowan’s tongue had never sounded so convincing. He brimmed with confidence; this ought to work. The red-haired sister shrugged at the futility of Rowan’s request. Did he not see the man was doomed by his own stupidity, regardless of their use of him?"
            "Eventually they conceded. This would be the last time they used the man, but Rowan would have to take them on their word. He had disrupted their work enough. Rowan nodded, wished the dark-minded sisters the best and departed. They promptly resumed chanting."
            #lose a little guilt
            $ change_base_stat('g', -2)
            return
        else:
            #fail
            "Rowan attempted for all he was worth, but the responses ranged from rejection to straight-out ridicule. The sisters especially laughed when he threatened with his employers and played the ‘legendary hero’ card. At one point his hand was on his sword hilt, yet he dared not draw."
            "Eventually he accepted defeat. The man’s fate was sealed, and he wasn’t about to risk death (and in doing so condemning Alexia to a lifetime under Andras’ care). Rowan nodded, wished the dark-minded sisters the best and departed. They promptly resumed chanting."
            #gain a small amount of guilt
            $ change_base_stat('g', 2)
            return

    "Allow them to continue and leave":
        $ renpy.fix_rollback()
        "Rowan wanted to aid the man, but he was outnumbered three to one, and had no way knowing just what sort of powers these witches possessed. He wasn’t about to risk death (and in doing so condemning Alexia to a lifetime under Andras’ care)."
        "With his tail between his legs, he slinked back through the swamp that way that he came, leaving the poor man to his fate."
        #gain a small amount of guilt
        $ change_base_stat('g', 2)
        return

    #requires x corruption
    "Allow them to continue and stay to watch" if avatar.corruption > 10:
        $ renpy.fix_rollback()
        jump witchWatch

################################################################################

label witchWatch:

"What possessed Rowan to ask to watch? Was it the sensual elven frames and the hope one would tend to his obvious needs? The taint of the dark spirits they were conjuring? Or was it Chaos itself that was creeping up on Rowan?"
"The sisters agreed, but only on one condition. As the chanting and dancing rekindled Rowan stood watching, his cock in his hand as agreed on. He was commanded to slowly stroke, and with a heart heavy with guilt he did."
"The censers were hung on tree branches; the elves wanted their hands free. The redheaded sister crawled atop the man on the altar and started to grind her sex against his groin. The moistness of her mound glistened teasingly against the purple lamplight. "
"The Raven-haired sister focused on Rowan. She slid behind him, grabbed a chunk of his hair, and with it directed him to watch her sister. She started stroking Rowan’s cock just as her sister pushed the captive’s cock inside her cunt."
"The sister atop the man set a slow but relentless rhythm; she was balls deep and never released an inch of the man’s cock. Instead she ground her hips back and forth in sensual motions, massaging his member inside her swollen mound."
"Rowan’s eyes were almost hypnotically locked on the display before him, but his mind was at his nethers. Two hands were active there now: one was stroking his cock in a firm manner, the other teasingly massaged and tugged at his balls."

$ witchName = "Crimson-haired sister of Nyx"

witch "Mine is ready to offer his first release, sister! Is yours?"

$ witchName = "Raven-haired sister of Nyx"

witch "As is mine... But has he earned the right to claim such a prestigious station? He has neither knowledge of - or love for - our blessed Ways of Old."

ro "I… Ugn…"

$ witchName = "Crimson-haired sister of Nyx"

witch "I fear you are right, good sister. Not only should he not get his desired release, he should also see none of the coming spectacle!"

"A word was whispered into Rowan’s ear and something pricked his neck. Almost instantly his legs went weak and his view became a spinning mess. He heard fiendish laughter blend into feverish moans while he spiraled towards the floor."
"The last thing he remembered before he passed out was an invitation. Should he desire more of what transpired here, he could find the sisters of Nyx via the magnificent Queen of the Fae, Kassandra thornheart. She was the gate to the Old Ways, the ways of pleasure."

return


##########################################################################################################
##########################################################################################################
##########################################################################################################


label the_riddle_of_the_dead:
#The Riddle of the Dead

scene bg32 with fade
show rowan necklace neutral behind bg32

"{i}They’ve been dead for at least two weeks{/i}, Rowan thought as he surveyed the corpses. Scavenger birds fled the scene as he walked around: he saw a score of soldiers clad in crude armor, dead as can be, each with one or more fatal wounds and signs of rot."
"He walked carefully; it was ill luck to step on the dead. He also walked fast, as the smell the corpses left was intolerable. Since no sensible soldier brought valuables into combat he was relieved of the burden of scavenging the dead… there was no reason to linger."
"Rowan passed the last of the unlucky souls when the hairs on his neck rose in collective unease. He had heard something he thought was a faint voice. At first he imagined one of the soldiers had survived, yet he quickly dismissed the idea as folly (without water and food they had no chance)."
"He turned and saw the corpse he had just passed, still inanimate and quite dead. One thing had changed, however. Where earlier its eyes were closed in acceptance of the inevitable finale of life, he then found them open. Brilliant red eyes gazed at Rowan; then dead lips curled into a smile."
"Rowan had seen a great many things in his time, including the animated dead, yet this was different. He was unnerved to his very core; this was beyond mere necromancy. Before the voice spoke again Rowan knew in whose presence he was - the Lord of Death Eternal, Kronn."

kron "To see my true nature in this broken vessel requires a keen mind. A pity it is wasted on ever-decaying flesh. In time I may offer to remedy that."

ro "I greet you with the utmost respect, Lord Kronn. To what do I owe the honor of your exalted presence?"

kron "Curiosity. When Chaos stirs I am ever intrigued. Where you walk it flares up in ways I have not seen for ages. Therefore I wondered in earnest - what is so special about this Rowan Blackwell?"

ro "Less than you would think, Lord Kronn. As all others I am a mere mortal subject to your will and rules."

kron "Are you? Can you not see Chaos flock around you?"

ro "I cannot, lord Kronn. All I know is that I do the work of two of Chaos’ demonic offspring, perhaps this is what you perceive?"

kron "Nay, the matter is not so simple. But with the absence of your knowing, the interest for me to discuss it with you wanes. I will be watching you with interest, however."

"Rowan nodded and intended to thank Kronn for the audience, yet then he remembered something. Legend held that if one solves one of Lord Kronn’s many riddles of Death, favor and fortune are the reward. The price of failure is never mentioned, however."

menu:
    "Thank the Lord of Death for the audience.":
        $ renpy.fix_rollback()
        "Rowan bowed low and thanked the Lord of Death for the honor of his time. A final unnerving smile crept onto the dead man’s visage, then its eyes became cold and lifeless again. Kronn was gone, yet he left Rowan with plenty to ponder..."
        return

    "Ask the Lord of Death for a riddle.":
        $ renpy.fix_rollback()
        jump kronRiddle

################################################################################

label kronRiddle:

ro "If I may be so bold as to claim a moment of your time, Lord Kronn. I wonder if you would honor me with one of your riddles, as that I may incur your favor?"

kron "Bold indeed. Also brave, and perhaps even foolish. You are familiar with the consequence of failure?"

ro "I am not, Lord Kronn."

kron "Perhaps for the best. Let us play then."
kron "A murderer is condemned to death. He has to choose between three rooms. The first contains a torrent of raging fire, the second a hundred armed assassins, and the third a score of lions that haven't eaten in years. Which room will allow him to escape my embrace?"

menu:
    "The room of fire.":
        $ renpy.fix_rollback()
        jump kronWrong

    "The room of assassins.":
        $ renpy.fix_rollback()
        jump kronWrong

    "The room of Lions.":
        $ renpy.fix_rollback()
        kron "The lions are of most certainly dead after a year. You do not disappoint. I will keep my eye on you, Scion of Chaos! Here is your reward..."
        jump kronRight

    "Trust your luck and pick one.":
        $ renpy.fix_rollback()
        #lick check DC20
        if check_stat(20, 'luck')[0]:
            #succeed
            kron "You dare gamble in my presence? Brazen beyond words! And yet a game is a game only if the rules are honored. You will have your reward."
            jump kronRight
        else:
            #fail
            jump kronWrong

################################################################################

label kronWrong:

kron "Where earlier you showed keen mind, now you disappoint. Under normal circumstances I would severe Spirit from flesh and claim you here and now! As you have a destiny that includes Chaos, I am however loathe to do so."

"The God of Death parts with words of advice - do not meddle with the Gods unless you are prepared! To ensure Rowan takes the lesson to heart a ‘reminder’ is instilled… as Lord Kronn leaves the dead body Rowan’s nose begins to bleed and his stomach churns. He feels deathly sick."

#lose 3 vitality for 2 weeks
$ add_effect(MultiEffect('Sickness', 'neg', (('vitality', -3),), 2))
return

################################################################################

label kronRight:

"The corpse started to hum open-mouthed. The sound became louder and deeper over a short period of time, causing Rowan to step back. When he felt like the dead husk was going to explode it suddenly stopped. Gold coins spurted forth from the mouth of the corpse."
"Rowan bowed low and thanked the Lord of Death for the honor of his time. A final unnerving smile crept onto the dead man’s visage, then its eyes became cold and lifeless again. Kronn was gone, yet he left Rowan with plenty to ponder..."

#gain 30 personal gold
$ change_personal_gold(30)
#gain 3 vitality for 2 weeks
$ add_effect(MultiEffect('Blessing', 'pos', (('vitality', 3),), 2))
return


##########################################################################################################
##########################################################################################################
##########################################################################################################


label the_nyverian_wisp:
#The Nyverian Wisp

$ wispName = wisp

scene bg32 with fade
show rowan necklace neutral behind bg32

"The bog Rowan found himself in was depressing in more than one way: it was moist to the point of claiming half of his boots with each step, the air was putrid, and its dense foliage allowed for very little light. Rowan was barely able to see where he was going."
"A glimmer in the distance that moved from behind tree trunks caught his attention. He could not make out what it was, but the glimmering spectrum of blues and pinks told him it was of magical origin. Its elegant movement allowed for a second conclusion - it was alive. "

menu:
    "Inspect the entity.":
        $ renpy.fix_rollback()
        jump inspectWisp

    "Leave it alone.":
        $ renpy.fix_rollback()
        "Ethereal lights in dark forest were considered an ill omen for a reason, and in muddy swamp like this a quick exit would not be an option. Rowan ducked behind a tree and waited for the creature to pass. Better safe than sorry."
        return

################################################################################

label inspectWisp:

"Ethereal lights in dark and damp forests weren’t the wisest thing to pursue, but Rowan’s curiosity won the day. He attempted to make his way to the creature when its movement suddenly stopped."
"The light the entity emitted flared up in magnificent fashion, coloring the forest around it sensual hues of pink and purple. Then, in a flash almost too quick for Rowan’s eyes to follow, the thing was before him."
"The visage of a gorgeous female hovered before Rowan. Her face was that of lascivious temptress, with hunger and desire shining in brilliant eyes, but a benign quality seemed also present. For hair it had strands of vibrant energy that writhed as if alive."

$ wispName = 'Alanarithe'

wisp "Well met, child of man. I am Alanarithe of the Nyverian lights. May I inquire as to your name?"

ro "Well met. I am Rowan Blackwell."

wisp "And what brings you to my domain, Rowan Blackwell?"

ro "I was merely passing through when I saw your radiance illuminate the darkness. If I intrude and am unwelcome I apologize, and can be on my way."

"As Rowan spoke with Alanarithe he noticed the entity’s presence had a soothing, almost healing quality. Whatever thoughts of danger he initially had were gone. In their place was a warm and fuzzy feeling that slowly but certainly grew as he lingered."

"During their conversation time passed in a strange yet pleasant manner. Rowan asked Alanarithe if she was a sort of wisp, upon which the feminine creature grinned seductively and said she was of the Nyverian lights. Rowan did not recognize the heritage."
"After what felt like hours of pleasant and at times sensual dialogue Rowan noticed a soreness in his legs. Initially he wished to disregard it, as he had never held such pleasant company as he did then. What the Nyverian said next worried him, however."

wisp "You seem encumbered, Rowan Blackwell? Are you afraid that my demeanor will turn predatory soon?"

ro "I am not. But there is a strange passing of time in your presence. As much as I enjoyed your company, I fear I must be on my way."

wisp "If you want to leave you can, but I would insist you pay a trivial tithe."

ro "Payment in the form of? I doubt you’re interested in gold, and I have nothing else to offer."

wisp "The currency you mortals hold dear is not the one nature covets, true. Nevertheless you certainly have something I desire, Rowan."

"Rowan felt himself stir below: first to a general level of arousal, but seconds later to the point of unbearable hardness. Alanarithe licked her upper lip provocatively. It couldn’t be any clearer what the fey creature desired."

menu:
    #requires x corruption (TODO)
    "Agree to Alanarithe’s tithe." if avatar.corruption > 10:
        $ renpy.fix_rollback()
        jump agreeWispTithe

    "Disagree to Alanarithe’s tithe":
        $ renpy.fix_rollback()
        jump disagreeWispTithe

################################################################################

label disagreeWispTithe:

"The mouth of the Nyverian seemed, at that time, as the most desireable orifice one could ever be inside. Rowan wanted to indulge with all his being, yet shook his head stoically. He wouldn’t stoop to this low. He worked for the twins, yes, but Chaos had not claimed him yet."

ro "I’m honored, Alanarithe, but I cannot pay such a tribute. If you would so kind as to allow me to pass freely?"

wisp " I freely give hours of my prestigious attention and you cannot even indulge a simple request? I have killed men for worse, Rowan Blackwell! But… I do confess to liking you. You’ll get off with a minor curse."

menu:
    "Accept a minor curse as the price of your curiosity":
        $ renpy.fix_rollback()
        "Rowan considered drawing his blade. He disliked his odds against the otherworldly creature, but he had an equal dislike for curses. Eventually he decided against physical conflict; he wasn’t certain his blade could damage an entity so otherworldly as Alanarithe."
        "Alanarithe smiled wickedly. Rowan felt a spike of agony rush into his legs from the floor, surging through his legs up into the rest of his body. They were like energetic barb wire, and wherever they passed they left insufferable agony."
        "Eventually the energy found his heart and concentrated there. Alanarithe mumbled something about the Heavens and Hells, puckering her delightful lips as a final tease, and then Rowan fell to the floor and everything turned dark."
        "When Rowan awoke he found Alanarithe was gone. She had taken her warmth with her, and had left him with the feeling of broken bones. He slowly rose and found he was in better shape than he felt, but not by much. Eerie lights in swamps? Never again, he vowed."
        #lose 1 move points
        $ change_mp(-1)
        return

    "Try and bluff your way out of the curse":
        $ renpy.fix_rollback()
        #bluff check DC15
        if check_skill(15, 'bluff')[0]:
            #succeed
            ro "That would be quite unwise. My employers are pair of unforgiving demons, and have tasked me to be the extension of their will in these lands. They would not look kindly on anyone that thwarts my progress."
            wisp "You are working yourself into a bind here, Rowan Blackwell. If your demonic masters would take offense for me cursing you, am I then not better off ending your existence instead?"
            ro "They’d know and repay you in kind."
            wisp "Would they now? I don’t see anyone, Rowan. Nor do I feel any incorporeal presence observing us."
            "Rowan failed to suppress a sly smile. He tapped the ornate amulet around his neck and explained its function to Alanarithe. The Nyverian intently looked at the blue stone Rowan wore for the better half of a minute, then shook her head in spiteful resignation."
            wisp "Should I find you here again, and with that stone not gracing your neck, know that you will suffer greatly. Death would be gentle compared to what I have in store for you, Rowan Blackwell!"
            return
        else:
            #fail
            ro "Cursing me may blow up in your face. I have powerful employers that-"
            "Before Rowan could finish his bluff he felt a spike of agony rush into his legs. Coming from the ground it surged from his lower limbs into his torso. The sensation felt like energetic barb wire, and wherever they passed they left insufferable agony. "
            "Eventually the energy found his heart and concentrated there. Alanarithe mumbled something about the Heavens and Hells, puckering her delightful lips as a final tease, and then Rowan fell to the floor and everything turned dark. "
            "When Rowan awoke he found Alanarithe was gone. She had taken her warmth with her, and had left him with the feeling of broken bones. He slowly rose and found he was in better shape than he felt, but not by much. Eerie lights in forests? Never again, he vowed."
            #lose 3 move points
            $ change_mp(-3)
            return

################################################################################

label agreeWispTithe:

wisp "To receive is to give, and to give is to receive. It fills me with joy to see there are mortals that still honor the old way. Now then, enough talk - show me your cock!"

scene cg143 with fade
pause 3

"Rowan nodded. He unceremoniously unzipped his trousers and produced his fully erect manhood. He could not deny being excited at the prospect of the Nyverian’s ‘tithe’; a drop of pre-cum dangled from his cockhead."
"As Alanarithe slowly hovered closer the alien nature of the fey entity became more apparent. Her eyes were like glistening gateways into a dark infinity and her energetic hair danced as if it had a life of its own. For a moment Rowan considered backing out. "
"All Rowan’s resistance failed when Alanarithe pressed her mouth to the head of his cock. Her lips parted just enough to let his slit enter the warmth of her oral cavity. It was greeted by Alanarithe’s moist tongue."
"Alanarithe’s tongue teased the opening of his head while her eyes were fixed on his own. For a second he entertained an uncharacteristic thought: to grab the creature by her ethereal hair and press himself balls-deep into her. Then Alanarithe swallowed his head fully."

menu:
    #requires x corruption
    "Act on the uncharacteristic thought" if avatar.corruption > 10:
        $ renpy.fix_rollback()
        jump wispFinaleDominant

    "Let Alanarithe pleasure you as she sees fit":
        $ renpy.fix_rollback()
        jump wispFinale

################################################################################

label wispFinaleDominant:

scene cg144 with fade
pause 3

"Rowan clasped the back of Alanarithe’s and buried himself balls deep in a single gesture. The Nyverian glanced at him in an insidious manner, in which Rowan read a hint of approval. This was all he needed."
"He started to fuck her mouth forcefully, slowly pulling back to the head, before plunging into her again in one violent motion. Whenever he pulled out Alanarithe’s cheekbones became extremely pronounced; she sucked at his cock fiercely."
"Burying himself into the depths of Alanrithe’s deep oral cavity was a guilty pleasure Rowan enjoyed far more than he should have. Back out was pleasurable in an entirely different manner. On the return trip he felt like he was orgasming the entire journey back."
"The climaxes Rowan felt whenever Alaranthe’s sucked weren’t true orgasms. There was no ejaculate, nor was there a feeling of being ‘done’. What he did feel were tendrils coming from his cockhead, filaments of energy disappearing in whatever void the mouth of Alanrithe truly was."
"Rowan came again and again in that strangely energetic fashion, and over time three things happened: he began to feel weaker, especially in the knees, he became extremely light headed, and he felt a huge explosion of semen was about occur."
"It was clear the tithe was more than Rowan bargained for. The question was by how much? What would happen if Rowan unloaded hot semen into this entity’s mouth? Gods know he wanted to… Besides, did he even have the fortitude to stop at this point?"

jump wispFinaleChoice

################################################################################
label wispFinale:

"A slow but powerful blowjob followed. Alanarithe’s suction was divinely pleasant as she pressed forward, yet when she pulled back her cheekbones became extremely pronounced and she sucked hard. At first the sensation was too extreme, but Rowan soon edged into it."
"The duality of Alanarithe’s in and out movement slowly but surely became a rhythm that held Rowan spellbound. Going into the depths of her mouth he was relaxed as pleasure tingled through his glans, back out he felt like he was orgasming the entire movement."
"The climaxes Rowan felt whenever Alaranthe’s sucked weren’t true orgasms. There was no ejaculate, nor was there a feeling of being ‘done’. What he did feel were tendrils coming from his cockhead, filaments of energy disappearing in whatever void the mouth of Alanrithe truly was. "
"Rowan came again and again in that strangely energetic fashion, and over time three things happened: he began to feel weaker, especially in the knees, he became extremely light headed, and he felt a huge explosion of semen was about occur."
"It was clear the tithe was more than Rowan bargained for. The question was by how much? What would happen if Rowan unloaded hot semen into this entity’s mouth? Gods know he wanted to… Besides, did he even have the fortitude to stop at this point?"

jump wispFinaleChoice

################################################################################

label wispFinaleChoice:
menu:
    #requires some sort of resistance / endurance stat (TO DO)
    "Attempt to pull out just in time.":
        $ renpy.fix_rollback()
        "A true physical orgasm was seconds away, and Rowan would not have been able to stop it even if Alexia popped up from behind a tree. He knew Alanarithe would not let him go freely, and with his cock in her mouth he could afford no risk - he would pull out at the last moment."
        "The Nyverian knew Rowan was on the brink and swallowed his full manhood in gleeful anticipation. She was ready to devour his seed. With all the signs that semen was about to erupt from his cock Rowan started his ploy."
        "“Yes!” Rowan shouted, feigning cooperation. Alanarithe’s unnatural eyes looked up at his and shone with delight; she was going to get swallow hot cum. Rowan intertwined his fingers in her hair and pinned her balls-deep on his cock. His orgasm started."
        scene cg146 with flash
        pause 3
        "Alanarithe moaned of pleasure when the first burst of sperm shot from Rowan. It hit her in the left eye; Rowan had pulled out just in time. Timely or not, there was no stopping the maddening amount of semen the seductive entity had caused him to produce."
        "Another burst hit Alanarithe’s face at blistering speed. Rowan had not shot like this since he was sixteen, and even then the semen had not been so thick and plentiful. He groaned as he struggled to keep Alanarithe’s head in place while cumming so violently."
        "Burst after burst erupted until Alanarithe was smeared with strands of white goo. Alanarithe was beyond words and screeched in fury as she bit at the air, hoping to maim Rowan cock. While it was becoming harder to hold her in place Rowan had no fear of reprisal."
        "The eyes of the entity were - as well as much of the rest of her face - covered in semen. Rowan smiled and thanked the twins. When Alanarithe pulled at him with all her might he indulged her, and with all his might swung the entity in the direction it tugged."
        "Rowan the hero, the thought amused as he ran through the bog with his cock in his hand. He heard Alanarithe screeched and screamed behind him, yet without hands to clean her face she was unable to pursue Rowan."
        "As the screams and death threats became distant Rowan slowed his pace. The Gods were surely cruel at heart. Lacking hands Alanrithe was now dependant on heavy rainfall to regain her eyesight. {i}That or a deer with a taste for cum{/i}, he mused grinning."
        return

    "Explode in Alanarithe’s mouth":
        $ renpy.fix_rollback()
        "Rowan groaned in unison with Alanarithe. He did not have the vitality to to pull himself away from her heavenly cock-sucking mouth. He didn’t even have the will to want freedom. His cock was right where it ought to be. Whatever the price encompassed, he would pay."
        "The Nyverian knew Rowan was on the brink and swallowed his full manhood in gleeful anticipation. She was balls deep and her eyes glimmered with emotion. {i}Is that love{/i}? Rowan wondered momentarily. Then he correctly saw it for what it truly was - pure lust."
        "Rowan grabbed the back of Alanarithe’s head by instinct and pulled her into his groin with all his might. No one had sucked his cock like this, and he knew it was likely no one ever would again, he wanted to enjoy it. He wanted to gift Alanarithe his cum."
        scene cg145 with flash
        pause 3
        "He came like never before. Semen and the energetic strands from before spurted from his cock into the warm haven that was Alanarithe’s otherworldly insides. The entity moaned and groaned in feverish pleasure, yet never stopped sucking."
        "Burst after burst disappeared inside Alanarithe and there was no sign Rowan was about to stop. He realized he had fallen to the floor at some point (yet lacked the memory), and was thrusting his hips into Alanrithe’s mouth as if to impregnate her. Eventually he passed out."
        "When Rowan awoke he found Alanarithe was gone. She had taken her warmth with her, and a good deal of his constitution as well. He rose slowly and found all his muscles were sore. He would not be able to explore much this week…"
        #lose 3 vitality for 2 weeks
        $ add_effect(MultiEffect('Sore muscles', 'neg', (('vitality', -3),), 2))
        return

