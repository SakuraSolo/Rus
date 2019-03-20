# random map events that happen on plains
init python:

    # Famine Looms
    event('famine_looms', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # The New Goblin Prince
    # should happen only if rumor about new goblin prince is not known yet
    event('new_goblin_prince', triggers='map_expl', conditions=('not new_goblin_prince_rumor', 'world.cur_tile_type == "plains"'), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Goblin Scouts
    event('goblin_scouts', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Is Rowan A Thief?
    event('is_rowan_a_thief', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Travelling Monk
    event('travelling_monk', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Please Fetch Medicine
    event('please_fetch_medicine', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Orcs in the North
    event('orcs_in_the_north', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Ancient Chest
    event('ancient_chest', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Thief in the Night
    event('thief_in_the_night', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label famine_looms:
# Famine Looms

scene bg31 with fade

"During his travels, Rowan stopped by one of the small farm communities to chat with the locals and hear the latest news. He learned that there was a recent fire in one of the largest Arthdale granaries."
"Goblin arson was blamed for the attack, but the farmers were mostly concerned with the baron's actions afterwards."
"It seems that he was so desperate to refill the city's food stores that he forced farmers to sell him even their own meager supplies."
"Combined with the poor harvest last year, there's a very real risk of famine among the peasantry now."
"The scramble to maintain enough food in the capital and castles has left many of the smaller communities with dangerously low stores."
$ add_exp(5)
#end event
return

##############################################################################
##############################################################################


label new_goblin_prince:
# The New Goblin Prince

scene bg31 with fade

"Word has spread to this corner of Rosaria that the goblins of Blackholt forest have been reorganizing themselves. They've been growing bolder in their raids over the last few months and have started a guerrilla war with the baron."
"As with all rumors, the stories are muddled and contradictory.  Some suggest that an army has come out of the Eastern mountains. Others suggest that the disparaging clans have been unified."
"Someone even claimed that they'd seen goblins creating doubles of themselves with foul magic. One thing that they agree on is that these raiders have been heard chanting a name after their victories again and again, 'Tue-Row'."
"Exactly who, or what, Tue-Row is remains another topic of wild speculation."
$ add_exp(5)
$ new_goblin_prince_rumor = True
#end event
return

##############################################################################
##############################################################################


label goblin_scouts:
# Goblin Scouts

scene bg31 with fade

"A small team of goblins crossed Rowan's path on this day.  Both of them seemed very surprised to encounter the other, but the hero quickly recovered and prepared for battle."
"He could tell immediately that this was either a scouting or raiding party from the Blackholt."
"Instead of preparing to fight the man, the band of small green folk called out to him and offered to look the other way if he gave them a little bit of money."
"If not, it was quite possible his life would be difficult for the next few days."

# Choice
menu:
    # TODO
    # Req: Must have completed goblin quest (not done yet)
    #menu response - "Tell them you're allied with Tue-Row."
    "Tell them you're allied with Tue-Row." if False:
        $ released_fix_rollback()
        "Upon learning who Rowan was and the alliance that had been made with Tue-Row, the goblins quickly apologized for the trouble they'd caused and assured him that no bribe was necessary."
        "Just before leaving, one of the goblins even asked their hero for an autograph."
        $ add_exp(10)
        #end event
        return

    #menu response - "Pay their bribe."
    "Pay their bribe.":
        $ released_fix_rollback()
        "Figuring it was best to avoid trouble for now, Rowan gave the goblins their money. Hopefully he wouldn't be needing that money from the castle treasury anytime soon."
        # lose money from treasury
        $ change_treasury(-10)
        $ add_exp(10)
        return


    #men response - "Let them do their worst."
    "Let them do their worst.":
        $ released_fix_rollback()
        "The goblins simply left after this point. At first Rowan believed that they'd been making empty threats, but over the next few days he found himself always being harried and harassed by distant figures."
        "This forced him to take detours, sometimes retrace his steps, and spend a significant amount of time finding safe places to rest at night."
        #lose movement points
        $ avatar.mp -= 2
        $ add_exp(10)
        return

##############################################################################
##############################################################################


label is_rowan_a_thief:
# Is Rowan A Thief?

scene bg31 with fade

"Traders are common passers by on the plains of Rosaria.  There are almost always humans living in an area, so there's always a demand for their goods."
"The one that Rowan ran into today was one that specialized in various flavorings, spices, and herbs."
"Nothing that would be of use to trade for, but Rowan did notice that she kept her money in a somewhat insecure place, at least for someone of Rowan's skills."
"Though stealing from her went against Rowan's ideals, the possibility of getting a little extra to help him meet the twin's quotas did occur to him."
"Especially since the merchant seemed to be fairly well off and ran a successful business."


# Choice
menu:
    #(Req: Rowan must be somewhat pure)
    #menu response - "Don't try to steal any money."
    "Don't try to steal any money." if avatar.corruption < 3:
        $ released_fix_rollback()
        "Staying true to his nature, Rowan made no attempt to steal any of the merchant's money."
        $ add_exp(5)
        #end event
        return

    #menu response - "Try to steal a little money."
    "Try to steal a little money.":
        # Roll a low difficulty sleight of hand check.
        $ released_fix_rollback()
        if check_skill(5, 'sleight_hand')[0]:
            #Success:
            "Without alerting the merchant, Rowan quickly slipped some coins out of the money case. Then went on his way."
            "He probably had taken a small enough amount that the merchant would never realize that someone had robbed them."
            # Gain a small amount of treasury, modified by a luck roll.  Gain a little bit of guilt and corruption.
            $ change_treasury(10 + dice(avatar.luck))
            $ change_base_stat('c', 1)
            $ change_base_stat('g', 1)
            $ add_exp(10)
            return
        else:
            #Failure
            "Rowan soon discovered that he'd made a mistake while trying to open the money case, which unfortunately attracted the confused gaze of the merchant. Rather than push his luck any further, Rowan went on his way."
            # Gain a small amount of guilt and infamy.
            $ change_base_stat('g', 1)
            $ change_base_stat('f', 1)
            $ add_exp(5)
            return

    #menu response - "Try to steal a lot of money."
    "Try to steal a lot of money.":
        # Roll a moderately difficult sleight of hand check.
        $ released_fix_rollback()
        if check_skill(10, 'sleight_hand')[0]:
            #Success:
            "Once he spotted an opportunity, Rowan worked quickly to open the money case and take a significant portion of the coins stored inside. He felt a mix of shame an exhilaration as he left the merchant behind."
            "He'd taken enough that it was likely the merchant would soon realize that something had happened. There might be rumors, but who had done it would be difficult to say."
            # Gain a larger amount of treasury, modified by a luck roll.  Gain a little bit of guilt and corruption.  Gain a small amount of infamy.
            $ change_treasury(20 + dice(avatar.luck))
            $ change_base_stat('c', 2)
            $ change_base_stat('g', 2)
            $ change_base_stat('f', 1)
            $ add_exp(10)
            return
        else:
            # Failure
            "Rowan set to work after spotting an opportunity. Unfortunately, his opportunity ended prematurely, and he was caught by the merchant red handed, forcing him to flee."
            "He still got away with a little money, but being caught as a petty thief was going to be a big problem for his reputation. Hopefully not too many people believed the merchant's stories."
            # Gain a small amount of treasury, modified by a luck roll.  Gain a little bit of guilt and corruption.  Gain a small amount of infamy.
            $ change_treasury(10 + dice(avatar.luck))
            $ change_base_stat('c', 2)
            $ change_base_stat('g', 2)
            $ change_base_stat('f', 1)
            $ add_exp(5)
            return

    #(Req: Rowan must be somewhat corrupt)
    #menu response - "Try to steal all of the merchant's money."
    "Try to steal all of the merchant's money." if avatar.corruption > 5:
        # Roll a difficult sleight of hand check.
        $ released_fix_rollback()
        if check_skill(15, 'sleight_hand')[0]:
            #Success:
            "Throwing any attempt to cover up his actions over the long term, Rowan took the first chance he had to take the entire money case and make a break for it. He'd have plenty of time to open it later."
            "There'd be no doubt that the merchant would know who'd done it when they saw the case was gone, but Rowan knew that would happen beforehand. The question was how many people would believe a destitute spice merchant."
            # Gain the largest (though still small) amount of treasury, modified by a luck roll.  Gain a little bit of guilt and some corruption.  Gain a small amount of infamy.
            $ change_treasury(30 + dice(avatar.luck*3))
            $ change_base_stat('c', 2)
            $ change_base_stat('g', 2)
            $ change_base_stat('f', 1)
            $ add_exp(10)
            return
        else:
            #Failure
            "Things go poorly and the merchant soon catches Rowan attempting to pry the money case off of their cart. The merchant pulled a crossbow on the hero, forcing Rowan to retaliate and stab them with a knife."
            "He then made off with the money case to deal with later, leaving the prone bleeding figure behind him."
            # Gain largest (though still small) amount of treasury, modified by a luck roll.  Gain a lot of guilt and corruption.  No witnesses, no infamy.
            $ change_treasury(30 + dice(avatar.luck*3))
            $ change_base_stat('c', 3)
            $ change_base_stat('g', 3)
            $ add_exp(5)
            return

##############################################################################
##############################################################################


label travelling_monk:
# Travelling Monk

scene bg31 with fade

"A monk of Solensia crossed paths with Rowan on this day. The elder man seemed to sense a shadow over Rowan's soul and offered to pray with the hero to help set his mind and heart at ease."
"He claimed it was always good to meditate on one's place in the world and how they fit into the Goddess's plan."
"Spending some time doing so certainly would do a great deal for Rowan's conscience, but time spent like that is time not spent working on the twin's quotas."

#Choice
menu:
    #menu response -  "Spend only a short time praying."
    "Spend only a short time praying.":
        $ released_fix_rollback()
        "In the end, Rowan choose to simply offer a token set of prayers before bidding the monk goodbye."
        $ add_exp(5)
        #end event
        return

    #menu response - "Spend a long time in deep prayer, meditation, and be purified."
    "Spend a long time in deep prayer, meditation, and be purified.":
        $ released_fix_rollback()
        "Rowan allowed the monk to guide him through the seven prayers followed by the three stages of self reflection. Then he asked to be purified and washed of sin. The hours went on and on, even into the next day."
        "That said, by the end Rowan felt cleaner and more himself than he had in a long time."
        # Lose movement points, lose corruption.
        $ change_mp(-2)
        $ change_base_stat('c', -2)
        $ add_exp(10)
        return

##############################################################################
##############################################################################


label please_fetch_medicine:
# Please Fetch Medicine

scene bg31 with fade

"In one of the small farm hamlets, Rowan stumbled upon a giant spider attack! He quickly sprung to assist the farmers and was able to help them fend the creature off."
"Afterwards he learned that the beast had poisoned the head of the community and he was quickly turning for the worst. The monster slayers guild made antidotes for this, but the nearest one was a long ways away."
"On top of that, it wasn't cheap. Everyone quickly concluded that Rowan was the only one who could make the trip in time to save the chief and offered to give him the money he'd need to buy the antidote."
"It would be a long trip to collect and wouldn't allow for detours along the way."

# Choice
menu:
    #(Req: Rowan must be somewhat pure.)
    #menu response - "Go get the antidote."
    "Go get the antidote." if avatar.corruption < 4:
        $ released_fix_rollback()
        "Rowan couldn't bear to abandon these people in their time of need, so he took the money and made the long trip to the monster slayer's guild and back."
        "He managed to return just in time, saving the chief's life. The farmers were ecstatic and threw a small party for the hero and promised to sing his praises for years to come."
        # Lose movement points, lose infamy.
        $ change_mp(-2)
        $ change_base_stat('f', -2)
        $ add_exp(10)
        return

    #menu response - "Refuse to get the antidote."
    "Refuse to get the antidote.":
        $ released_fix_rollback()
        "While it was difficult to say, Rowan simply couldn't take the time to help the farmers. At first they were unable to believe that this hero was forsaking them, but eventually they became resigned to losing their chief."
        # Gain guilt.
        $ change_base_stat('g', 2)
        $ add_exp(10)
        return

    #(Req: Rowan must be slightly corrupt)
    #menu response - "Take the money for yourself."
    "Take the money for yourself." if avatar.corruption >= 4:
        $ released_fix_rollback()
        "Rowan agreed to get the antidote for the farmers, but shortly after leaving the hamlet he returned to his work for the twins. The money they'd given him was in the twin's treasury by the end of the week."
        # Gain treasury, infamy, guilt, and corruption.
        $ change_treasury(10)
        $ change_base_stat('f', 2)
        $ change_base_stat('g', 3)
        $ change_base_stat('c', 1)
        $ add_exp(10)
        return

##############################################################################
##############################################################################


label orcs_in_the_north:
# Orcs in the North

scene bg31 with fade

"Word is spreading from the North about an orc warband has crossed the Rosarian Valley while being hunted by Prothean forces. This vicious group has begun raiding the scattered settlements North of Rastedel."
"It is likely they're from Karnas's scattered armies."
"Many people are worried that they'll move to other parts of the realm and cause trouble closer to home, though they've been staying put for the moment."
"Some are annoyed at the baron for his inaction against this threat. According to a local noble this is due to the more pressing issues of the bandits and goblins."
"If the orcs do head further South, then they will feel the fury of the Rosarian armies. If they stay where they are, the Prothean forces will eventually catch up and deal with them."
"Of course, since they're hunting many stragglers in the area that might take several months."
$ add_exp(5)
return

##############################################################################
##############################################################################


label ancient_chest:
# Ancient Chest

scene bg31 with fade

"Fortune smiled on Rowan this day, as he stumbled on an ancient chest half buried in the ground."
"He'd often wondered why he'd sometimes had the good luck to find these old goodies, normal people didn't seem to ever tell stories of old chests or treasures lying around."
"Come to think of it, the other heroes were the only ones who'd ever mentioned this kind of thing happening to them. Perhaps they were a way that Solansia blessed her champions."
"Maybe they were some other power's way of helping him."
"Rowan could only speculate. The only answer he would get this day was what was inside the chest."

#Roll luck and get a random simple piece of equipment based on result.
if check_stat(15, 'luck')[0]:
    $ get_rnd_item(200, 300)
    $ add_exp(10)
else:
    $ get_rnd_item(100, 250)
    $ add_exp(10)
return

##############################################################################
##############################################################################


label thief_in_the_night:
# Thief in the Night

scene bg31 with fade

#Make a spot check
if check_skill(10, 'spot')[0]:
    #Success
    "While Rowan was resting for the night, his dreams were disturbed by the sound of someone nearby going through his pack!"
    "Instincts learned many years ago kicked in and he sprang towards the intruder as silently as he could. The thief let out a cry of shock as Rowan fell upon him."
    "The small man, whom Rowan could now tell was a goblin, put up a desperate struggle to escape but was soon subdued and bound."
    "After relighting his fire, Rowan patted down the goblin and relieved him of what was probably stolen gear."
    "The hero interrogated the goblin for a few minutes to see if there was anything useful he could get out of them, but realized that the green man was likely a lone wolf."
    "In the morning Rowan released the failed thief."
    # Gain a random piece of low value equipment.
    $ get_rnd_item(0, 100)
    $ add_exp(10)
else:
    #Failure
    "While Rowan was resting for the night, his dreams were disturbed by the sound of running footsteps. He listened carefully to see if there was any further movement, but couldn't detect anything."
    "After making a sweep of his camp, Rowan checked his things and realized that he'd been robbed! He cursed himself for letting this happen and hoped he wouldn't be needing what he lost anything soon."
    "Thankfully they didn't take anything irreplaceable."
    #Lose a piece of non-unique equipment, or if the player cannot lose a piece of equipment, a small amount of gold.
    if not lose_rnd_item(0, 100):
        $ change_treasury(-10)
    $ add_exp(5)
return
