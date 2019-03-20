# random map events that happen on hills
init python:

    # Minor iron vein
    #can only occur in year one
    event('minor_iron_vein', triggers='map_expl', conditions=('world.cur_tile_type == "hills"', 'week <= 48'), run_count=1, group='map_expl', priority=pr_map_rnd)
    # The Shrine on the Hill
    event('shrine_on_hill', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Slipped (malediction)
    #no requirements
    event('slipped', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Friends in high places (worldbuilding)
    #No requirements.
    event('friends_in_high_places', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #### Hills Event: Harsh Valley ####
    event('harsh_valley', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #### Hills Event: The Bridge ####
    event('the_bridge', triggers='map_expl', conditions=('world.cur_tile_type == "hills"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label minor_iron_vein:
# Minor iron vein
#can only occur in year one

#hillside (countryside) bg

"During Rowan's survey of this hilly region, he was fortunate enough to stumble on an exposed vein of iron. While nothing terribly large, it was definitely worth exploiting."
"He charted a route to reach it and reported the details to Jezera so she could set up a small mining expedition. The operation would be so small that no special arrangements would be needed to get a little extra iron into the castle's supply."
"Small boons like this could make all the difference during the early days of Bloodmeen's restoration."
"Later on, it would be unlikely that Rowan would bother with the effort and paperwork as the minor benefits simply wouldn't be worth it."

#Increase iron income by 1.
$ castle.iron_per_week += 1
$ renpy.notify('Iron per week: +1')
#gain 10 xp
$ avatar.exp += 10
#end event
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label shrine_on_hill:
    # The Shrine on the Hill
    scene
    $ released_block_rollback()
    # choose which gods the shrine is for
    $ shrine_on_hill_god = renpy.random.choice(('Solansia', 'Balast', 'Nerios', 'Nessa', 'Cessair', 'The Sisters'))
    'The sun had been shining, and the sky a brilliant azure blue threatened only by a few fluffy, white cumulus clouds when Rowan had begun his ascent of the hill, a little over two hours ago, but as he neared the crest, it looked like it was going to rain.'
    'What had begun as a leisurely stroll had become more and more strenuous the higher he got up the hill, where the gradient had become steeper, and the path had given way to a mixture of soft earth, and loose stone.'
    'He had struggled to keep his footing, as the scree made each step a little more treacherous than the last, and one wrong step would have no doubt sent him rolling down the hill.'
    'As he reached the top, he almost slipped and had to kneel and use both of his arms to steady himself, but when he rose, he found himself on the surprisingly flat hilltop.'
    'It had begun to rain, and the cool drops of light drizzle were welcome after such a long, hard climb. Up there, the air was crisp, and it took more than a few steady breaths to get his wind back.'
    'Ahead he could see a small shrine, currently lacking any devotees, which was surprising, as he had passed a few more travelers coming down from the top on his own journey toward it.'
    # TODO: update when researching will be available
    # show the god the shrine for
    if shrine_on_hill_god == 'Solansia':
        $ released_fix_rollback()
#~         $ unlock_codex('solansia')
        'Rowan smiled as he saw the shrine ahead, the six wings of the large stone statue that sits atop it visible even from a distance.'
        'He knew it is a shrine to Solansia, the Goddess of Light, who created Solanse as a haven from the Outer Dark, and protected it even now from the evil forces that would harm its denizens.'
        'Compared to the extravagance of the grand cathedral in Prothea, this shrine was very modest indeed, but Rowan was still struck with a feeling of awe, standing before the goddess. He was not alone, all around the statue people had left offerings.'
        'There were a good number of gold pieces, and the fact the shrine had many very poor visitors yet the coins remained showed just how revered Solansia was among the folk of the Six Realms.'
        'Those who had no coins to give had left small mementos of their own, bits of string, cotton, locks of hair, whatever they had to give.'
    elif shrine_on_hill_god == 'Balast':
        $ released_fix_rollback()
#~         $ unlock_codex('balast')
        'As Rowan approached the shrine, he saw littering the ground of the hilltop blades of different sizes, daggers, swords, broken spear tips, and more. All of no longer use, either rusted, chipped, or bent to the point of being in dire need of repair.'
        'They had been left in tribute, along with bits of warped plate, leather, and broken chainmail links before the statue that Rowan recognized.'
        'Standing on top of the shrine, made from heavy bronze, it depicted a man in full plate, his face hidden, with a sword in either hand. The shrine is for Balast, the Lord of Blades.'
        'Men offered up prayers on his name on the eve of battle, both for protection, and that their own blades should hold true. Around the statue were coins left behind as offerings by those hoping to earn the god’s favour.'
    elif shrine_on_hill_god == 'Nerios':
        $ released_fix_rollback()
#~         $ unlock_codex('nerios')
        'As Rowan approached the shrine, he found it to be a very simple affair.'
        'The altar, so to speak, was an old wooden crate that had started to rot from exposure to the elements, and atop it was a simple black bowl, filled to the brim with rainwater. On the sides of the bowl, crude images had been painted in white.'
        'A wavy line represented the sea, undoubtedly choppy judging from the curvature of the line, above with were a number of boats of varying sizes. Beneath the line there was the sea life, including one rather fearsome looking beast that could only be a kraken.'
        'This was a shrine to Nerios, the Lord Under the Waves, usually worshipped by pirates and more law abiding sailors, but judging from the number of single gold piece coins that littered the top of the crate, he had also found some popularity here.'
    elif shrine_on_hill_god == 'Nessa':
        $ released_fix_rollback()
#~         $ unlock_codex('nessa')
        'Rowan\'s first thought upon seeing the statue resting upon the makeshift altar was that a hill in the middle of nowhere was an odd place to find a shrine for the Lady of the Shadows.'
        'He had seen a shrine to Nessa before, but it had been on the corner of a lane in the poorest part of Arthdale, where a few urchins had been congregating, no doubt asking for a blessing to aid in their latest mischief.'
        'As the statue attested to, with the way that the figure drew he cloak close around her and hid her face behind a hooded mask, Nessa was a goddess worshiped by thieves, assassins, and all others who worked under the cover of night.'
        'Around the pile were a few piles of gold coins left as offerings.'
        'Probably, Rowan thought, by those hoping that it would lead to the offer receiving a much larger pile of coin in exchange.'
    elif shrine_on_hill_god == 'Cessair':
        $ released_fix_rollback()
#~         $ unlock_codex('cessair')
        'A look of surprise crossed Rowan\'s face as he approached the shrine. He had not expected to find, here of all places, a shrine to the Mother of Sorrows. Elven gods were rare in Rosaria, and indeed most of the other realms these days.'
        'The elves, those of them that still remained, were loath to leave the sanctity of the great forest of Ealoean, to the point that meeting one of your travels had become something of a novelty.'
        'He recognized Cessair because of the veil that her statue wore, that one that in the elven legends she had worn to cover her weeping eyes since the day of the sundering.'
        'Before the statue were a number of loose coins, but also a collection of other tragic looking small objects.'
        'A sword that had snapped off at the hilt, a broken child\'s toy, a lock of hair wrapped around a plain iron band; Rowan imagined each one has its own sad little story to tell.'
    # The Sisters
    else:
        $ released_fix_rollback()
#~         $ unlock_codex('the_sisters')
        'Any man or woman in the Six Realms would recognize the figures on the altar before Rowan. Two woman, one light and one dark, who held the fate on our people in their hands.'
        'Both possessed of a striking beauty, The Sisters governed the twin poles of fortune that affected the lives of man and beast alike, good and bad.'
        'Layren, the lighter of the two, was the one from which people sought a blessing, while Uula, well, it was best to hope that you never caught her eye at all. It never ended particularly well for the poor people that she took an interest in.'
        'All around the altar were scattered the gold pieces that bore the sisters on opposite sides, left by people who were hoping that their luck would change.'
    menu:
        'Offer a prayer to the shrine':
            $ released_fix_rollback()
            'With the task at hand, Rowan needed all the help he can get, so he decided to offer up a silent prayer to [shrine_on_hill_god] in the hope that he might receive a blessing.'
            'Once he was done making his offering in the rain, he turned away from the shrine and headed back down the hill in the direction from which he came.'
            if check_dc(7, 'luck'):
                if shrine_on_hill_god == 'Solansia':
                    $ avatar.base_luck += 1
                    $ avatar.base_corruption -= 2
                elif shrine_on_hill_god == 'Balast':
                    $ avatar.base_strength += 2
                elif shrine_on_hill_god == 'Nerios':
                    $ avatar.base_vitality += 2
                elif shrine_on_hill_god == 'Nessa':
                    $ avatar.base_reflexes += 2
                elif shrine_on_hill_god == 'Cessair':
                    $ avatar.base_intelligence += 2
                # The Sisters
                else:
                    $ avatar.base_luck += 2
        'Take the offerings and destroy the shrine':
            $ released_fix_rollback()
            'After checking that nobody else was around, Rowan gathered as many coins as he could from the shrine, before taking out his weapon and smashing it to pieces.'
            'Once he had finished the job, he turned away from the shrine and headed back down the hill in the direction from which he came.'
            $ avatar.base_corruption += 3
            $ change_personal_gold(dice(20, 2) + 10)
    # in any case, give exp reward
    $ add_exp(10)
    return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label slipped:
#Slipped (malediction)
#no requirements

#Show hill or countryside background.

"A sudden gust of wind catches Rowan off guard, forcing him to find a quick foothold to avoid falling. It isn't safe, so his foot slips, along with the rest of him."
"The short cliff had seemed like it would be child's play to climb, after all those times he'd scaled castle walls many times its height. He'd been arrogant, forgetting to be more careful with a smaller challenge."
"Now he was paying the price."

#reflex test: DC12
$ temp1, temp2 = check_stat(12, 'reflexes')
$ released_fix_rollback()

if temp1:
    #Test reflexes: Success.
    "The man flung his arms out, seeking something, anything to grab onto.  He managed to snag a tree root with an arm, causing his body to swing into the cliff face, hard. A grunt escaped his lips on impact. It hurt like hell, but it was much better than it could have been."
    # 10 xp, small vitality injury for the rest of the week.
    $ add_exp(10)
    $ add_effect(Injury('Wounds', 'vitality', -1))
    return
elif temp2 >= 4:
    #Test reflexes: Partial failure (4-11).
    "A tree root flew past the man, he tried to throw his arms out to grab it, but he wasn't fast enough. Instinctively he tried to prepare for the impact, letting his body relax and putting his arms over his head."
    "Shortly afterwards, he lifted himself off of the ground.  He was battered, bruised, but alive. A curse escaped his lips as he looked up at the short cliff that had defeated him. He wasn't going to be doing any climbing for awhile now."
    #5 xp, Vitality injury for three weeks.
    $ add_exp(5)
    $ add_effect(Injury('Fall damage', 'vitality', -2, 3))
    return
else:
    #Test reflexes: Total failure.
    "A tree root flew past the man, he tried to throw his arms out to grab it, but he was too slow. He tried to prepare for the ground that would soon come, but his body was still sluggish."
    "A loud scream of pain accompanied the dull thud and wet crack of his body's impact on the ground. He'd fallen at an odd angle and broken one of his legs, but the pain that shot through him made it impossible to act."
    "It wasn't until nearly an hour later that he managed to pull himself up and get his broken limb out from under his body. Realizing he would get no further like this, Rowan was forced to contact his masters and request a return to the castle."
    "It seemed his explorations for the week were done."
    #End week's exploration. Vitality injury for three weeks.
    $ add_effect(Injury('Fall damage', 'vitality', -3, 3))
    jump end_map_exploration
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label friends_in_high_places:
#Friends in high places (worldbuilding)
#No requirements.

"Rowan was surprised to find a small cottage with a herd of goats surrounding it, high in the hills and far away from any other humans. There, he was even more surprised to be greeted by an old friend from the war."
"The hero hadn't been the only commander that circumstance had made out of a peasant. Until he'd joined up with Deanara, the other two 'dirt generals' had been his only comrades amongst the officers."
"While Rowan had the honor of being one of the six heroes who'd defeated Karnas to protect him, the other two did not. The nobility didn't like the natural order to be upset, they hated the threat that the dirt generals presented to them."
"One had found his way to the hills and hidden away from the rest of civilization to live his life out as a hermit, desiring no part of the politics that his existence brought. The two reminisced for a time together, thinking back to some of the things they did during the war."
"Neither knew what had become of their third comrade."
# 5xp, end scene
$ add_exp(5)
$ codex_add('dirt_general_starting')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label harsh_valley:
#### Hills Event: Harsh Valley ####
$ released_block_rollback()

"Trekking through the mountainous region, Rowan found himself at the foot of a long valley, shouldered on either side by steep, craggy peaks."
"A shepherd he had passed the day before had warned him about the fierce weather that could sweep down valleys like these, trapping and perhaps killing the unprepared."
"Beyond the peaks Rowan could see banks of cloud building and looming forbiddingly."
"And yet - the very nature of its hostility and remoteness surely made the sheltered territory worth exploring. Who knew what lay further back, untouched by most scavengers. Dwarven ruins? Rich iron ores? Abandoned treasures?"
"Rowan had to decide whether it was worth risking those heavy clouds rallying behind the mountains to put time into exploring the valley."

menu:
    "Explore.":
        $ released_fix_rollback()
        "Rowan gripped his pack, set his face to the wind and marched into the vast cleft of land, attention split between scouring the cliff sides for anything interesting and the clouds above."
        #dice roll - weather
        $ event_tmp['weather'] = 'weather holds' if dice(5) == 1 else 'weather breaks'
        #weather holds (20% chance)
        if event_tmp['weather'] == 'weather holds':
            "Weather in the mountains is indeed fickle, and not always for the worst. As the day progressed the clouds that promised a blizzard blew over, dissipated by a beaming sun."
            "The air is like wine in the mountains on days such as these, and Rowan went about searching the valley with a happy heart."
            #go to loot rolls
            jump .loot_rolls
        #weather breaks (80% chance)
        else:
            "The peaks disappeared behind the grey blanket as the day progressed, and fat flakes of snow began to kiss Rowan's face. Wind channelled down the back of the valley and soon Rowan had his arm raised against a heavy blizzard."
            "Progress was going to be tough."
            # survival check dc12
            #pass
            if check_skill(12, 'survival')[0]:
                "However, Rowan was experienced enough in the outdoors to tough out a simple snowstorm."
                "He stuck to the side of the valley with the most shelter from the gale, and huddled between rocks, constructing small fires, whenever he felt his temperature drop."
                "Hindered but undeterred, he advanced into the remote valley."
                #go to loot rolls
                jump .loot_rolls
            #fail
            else:
                "The terrain became impossible to navigate through the billowing curtains of snow, and Rowan got lost in the howling gale."
                "Panic set in as he felt his fingers and toes begin to go numb, and he had to turn in the only direction he could go - the way the wind was pushing him."
                "After several deeply miserable hours he arrived back at the head of the valley, alive but very much worse for wear."
                #gain 1 wound, lose 3 move points
                $ take_damage(1)
                $ change_mp(-3)
                return
    "Leave it.":
        $ released_fix_rollback()
        "Rowan was no mountaineer, much less an expert of these particular peaks. He did not waste valuable time on a dangerous, unknown valley, and after resting for a short time moved on."
        #no effect
        return

label .loot_rolls:
#loot rolls - choose one of the following at random
$ event_tmp['loot'] = dice(4)
if event_tmp['loot'] == 1:
    #1 - Nothing
    "Unfortunately, despite diligent hours spent searching every nook and cranny within that bleak corridor of rock, Rowan found nothing of interest."
    "Sometimes, he ruefully considered as he picked his way back the way he came, place that seem uninhabited since time began look that way for a reason."
    #gain 10xp, lose 2 move points
    $ add_exp(10)
    $ change_mp(-2)
    return
elif event_tmp['loot'] == 2:
    #2 - Chest
    "Near the back of the valley Rowan found a pile of wreckage; what appeared to be all that remained of a heavily loaded wagon. How did its owners get so lost, and what grim end did they meet?"
    "A sealed chest, half-buried amongst the rotting wood, caught his attention. It was a moment's work to get inside, and retrieve the fine piece of craftsmanship inside."
    "More than satisfied with his prize, Rowan retraced his steps back out of the valley."
    # gain 10 xp, random piece of armor gained, lose 2 move points
    $ add_exp(10)
    $ change_mp(-2)
    $ get_rnd_item(0, 500, 'armour')
    return
elif event_tmp['loot'] == 3:
    #3 - Orc Standard
    "It didn't take much searching for Rowan to find evidence of a battle fought here; spears stuck in the rocky ground, rusted armor clothing the broken remains of orcs and humans, picked apart by the crows."
    "Pacing around the sorry, rotting detritus, Rowan saw in his own mind how the chess pieces must have fallen; how the human commander must have forced the orc battalion back into the valley, so there could be no escape from the massacre that followed."
    "One item caught his eye. A tall standard stuck into the ground, its banner long since gone, the crude but powerful symbols at its tip still intact and recognisable. Rowan plucked it out and considered it thoughtfully."
    "Useless to him perhaps, but the orcs under his command would be glad to have this symbol of their old master to march under. Satisfied with his prize, Rowan retraced his steps back out of the valley."
    #gain 10 xp, gain morale, lose 2 move points
    $ add_exp(10)
    $ change_mp(-2)
    $ change_morale(5)
    return
else:
    #4 - Dwarven Ruin
    "At the back of the valley, Rowan found what he suspected he would find. The square, black gateway into the mountainside was guarded on either side by a dwarven statue, proud and stern for all that they were crumbling into scree."
    "Rowan would want a party of experienced mercenaries at his back to properly explore a dwarven ruin - there would be a reason why it was abandoned, the race were known to delve far and improvidently - so he settled on carefully scouting the entrance hallways."
    "This was still enough to discover a stash of polished topaz and an expertly crafted weapon, left in the remains of a guardroom."
    "More than satisfied with his prizes, Rowan retraced his steps back out of the valley."
    #gain 10 xp, gain treasury, gain random weapon, lose 3 move points
    $ add_exp(10)
    $ change_mp(-3)
    $ change_treasury(20)
    $ get_rnd_item(0, 500, 'weapon')
    return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_bridge:
#### Hills Event: The Bridge ####
$ released_block_rollback()

#50% the bridge is safe, 50% it will not hold
$ temp = dice(2)

"As Rowan crested the top of the hill, he was not prepared for what was awaiting him. In the middle of the hilltop a long fissure split the hill in twain, like a long scar along the landscape."
"He wondered what could have possible done this, as it seemed very unlikely it had been done by anything natural."
"Gazing down into the abyss, the bottom could not be seen, and he could only assume it was too deep to climb. At the edges, he could see the rock had been shorn, had grand mage’s duel, or a battle between gods done this?"
"His thoughts now turned to how he could possibly cross it, lest he have to turn back and lose even more time. The gap was far too long to jump, of that he was certain."
"As he traversed the cliff edge, he eventually came across an old rope bridge. Judging from the state of dilapidation, it must have been years, perhaps decades, since anybody had carried out any repairs on it."
"The question before him now was simple, but not particularly appetizing - risk the bridge, or turn back?"

menu:
    "Cross the bridge.":
        $ released_fix_rollback()
        "Rowan placed his hand on the rope that suspended the wooden slats over the chasm, and it seemed firm enough, despite its ragged appearance."
        "Carefully, he began to make his way across the old bridge, testing each wooden slat as he went to make sure it would take his weight."
        #if the bridge is safe
        if temp == 1:
            "Remarkably, each one did as he cautiously made his way to the other side of the chasm. A few times he was sure the rotted board would give way beneath him, but before he knew it he was once again on solid ground."
            "Thanking the gods for his luck, he set off down the other side of the hill."
            #gain 10xp
            $ add_exp(10)
            return
        #if the bridge is unsafe
        else:
            "Everything was going well until Rowan reached the middle of the bridge. He placed his foot upon one of the rotted boards and it split in two beneath him."
            "All he could do was lurch back to avoid tumbling to his death. As he did, he heard the unmistakeable snap of rope as the rest of the bridge began to give way."
            #reflect check dc12
            if check_stat(12, 'reflexes')[0]:
            #pass
                "Thinking fast, Rowan launched himself forward to grab hold of the rope as it fell away from him toward the opposite side of the chasm. Bracing for impact, he bent his knees to absorb the blow as he swung across the gap, colliding with the far wall."
                "Now he had made it to the other side, he began the task of slowly making his way up the rope, until he pulled himself clear at the top of the cliff."
                "The expedition had been far riskier than he had hoped, but at least he had made it to the other side, and would not lose any more time."
                #gain 10xp
                $ add_exp(10)
                return
            #fail
            else:
                "Rowan hardly had time to think as he grabbed the rope nearest to him, swinging backwards towards the side he had begun at."
                "Pain lanced through him as his back slammed into the side of the cliff, and it took everything he had to hold on to the rope and not fall to his death."
                "Gritting his teeth, he slowly pulled himself up the rope until he was once again where he started."
                "With no other way to cross the divide, all he could do was start back down the hill the way he came, and hope that the damage to his body from this failed endeavor did not turn out to be that severe."
                #gain 5xp, lose 3 move points
                $ add_exp(5)
                $ avatar.mp -= 3
                return
    "Return the way he came.":
        $ released_fix_rollback()
        "Deciding that the bridge looked far too dilapidated to risk a crossing, Rowan decided to go back the way he came. Yes, he would lose a lot of time, but it was still better than losing his life."
        #lose 3 move points
        $ avatar.mp -= 3
        return

