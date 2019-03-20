# events for various monster lairs (drider nests etc.)
init python:
    # Drider nest: No breeding pit
    event('drider_nest_no_breeding_pit', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl < 1",), group='lair', priority=pr_map_res)
    # Drider nest: Have breeding pit
    event('drider_nest_with_breeding_pit', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl >= 1",), group='lair', run_count=1, priority=pr_map_res)
    # Hunting Party
    event('hunting_party', triggers='map_res_9', group='lair', run_count=1, priority=pr_map_res)
    #The Spider’s Prey
    #requires breeding pits
    event('spider_s_prey', triggers='map_res_9', conditions=("castle.buildings['pit'].lvl >= 1",), group='lair', run_count=1, priority=pr_map_res)


label drider_nest_no_breeding_pit:
# No breeding pit
# If the player has no breeding pit, they cannot capture the resource site.

scene bg3 with fade

"Rowan had discovered a breeding nest for the fearsome drider, one of the most common monsters in Rosaria. However, he had no reason to approach any closer. All he'd be able to get here was drider eggs."
"Once a proper place to hold monsters was constructed at the castle, then he would be able to return here and use the nest to get stock for breeding driders to use in the twin's armies."
#End scene, do not mark the drider nest as explored, move back to previous space.
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#############################################


label drider_nest_with_breeding_pit:
# Have breeding pit
# Capturing this resource increases drider recruitment by 0.5 each week.  Currently the breeding pits will be only able to have driders, so the pits should slowly fill up with driders once you capture a nest..
$ world.cur_map.resources[world.cur_map.pos].capture()

#Choose one of the following options at random, it may change the outcome slightly.
$ event_tmp['variant'] = dice(3)

#1 - no effect
if event_tmp['variant'] == 1:
    scene bg3 with fade

    "In a secluded part of the forest, Rowan discovered several massive cocoons of spider silk. He checked them more closely and discovered that they were filled with large eggs. Each was at least twice the size of his head!"
    "That could only mean one thing, this was a drider nest! Something had obviously drawn the creatures to lay their eggs here, and it was likely that they'd keep doing so if the nests were left undisturbed."
    "He sent a message to his masters and relayed the location of the site. This was then passed on to Draith who confirmed that this would be an excellent site to collect eggs from to use for drider stock. He'd start as soon as possible."

    # No effect, end event
    return

#2 - lose orcs.
elif event_tmp['variant'] == 2:
    scene bg3 with fade

    "After avoiding the adults who were hunting nearby, Rowan found a nest of drider eggs and reported both its location and how to avoid the potentially vengeful parents nearby."
    "Unfortunately, the orcs who were dispatched later to collect the eggs were much less proficient at avoiding the driders than the hero had been. Eventually a few of them proved capable of completing the task so that the rate of collection was not reduced."
    "There were, however, several casualties before this point."

    # Lose 3 orc soldiers, end event
    $ castle.buildings['barracks'].troops -= 3
    return

#3 - gain money.
else:
    scene bg3 with fade

    "After spending several hours following the signs of driders, Rowan was fortunate enough to locate their nest, nearby the desiccated remains of what had certainly been a meal for the parent."
    "He sent a message to his masters, detailing the location and confirming that this would be a suitable source of drider eggs to use in the breeding pits."
    "Then he rifled through the bones and scraps of clothing nearby to see if there was anything of value there. He found a pouch of coins, which he pocketed as a small bonus to himself for this find."

    # Gain 20 coins for Rowan's personal money, end event
    $ change_personal_gold(20)
    return


label hunting_party:
#Hunting Party
#can occur if Rowan does or does not have breeding pits

"As Rowan approached the nest, he was met by three heavily armoured men, carrying a burlap sack."

mhunter "Hail, sir Rowan. Came here to take care of the nest, did ye?"

"The man flashed him a grin and dropped the sack to the ground in front of him."

mhunter "‘Fraid you’re a bit late, me and the lads will be getting the reward for this job."

"Dead eyes looked out from the sack up at Rowan from the severed head of a female drider, and judging from the size of the bag, it wasn’t the only one in there."

mhunter "Hope you weren’t looking forward to getting a few yerself, we took care of ‘em all, even the little ones."

"Rowan looked around the nest and could see fragments of eggs scattered across the forest’s floor, he wouldn’t be taking anything back to the castle from this excursion."
"He exchanged pleasantries with the hunters for a while before they left with their bounty, already laughing about the ways in which they would spend the money coming their way."
"Rowan on the other hand, would be leaving this nest empty handed."

#Nest is explored, but no resource is gained
# TODO: probably mark nest as captured, but avoiding "on_capture" (or maybe it is better to remove nest from map)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label spider_s_prey:
#The Spider’s Prey
#requires breeding pits

"A man’s scream cut through the peaceful quiet of the forest. Running toward the sound of distress, Rowan saw the poor soul who had cried out for help."
"The man was trapped beneath a female drider, who had bound his upper body and lower legs with its webbing, ensuring that it was impossible for him to escape."
"Something sharp had torn away the lower half of the man’s clothing, and it now had pinned him down with its pedipalps as it positioned itself above him to milk him of his seed."
"If Rowan was going to help him, he’d have to act fast."

menu:
    "Get the drider’s attention.":
        $ released_fix_rollback()
        "Rowan yelled out at the creature, and it turned to look at him quizzically."
        "Drawing his sword from its sheath, he advanced toward the drider as it, sensing the harm the hero intended toward it, readied itself to strike."
        #combat check DC12
        if check_combat(12)[0]:
        #pass
            "The monster struck out at Rowan with its front legs, but the human brought his sword to bear, cutting deep into the drider’s flesh."
            "It roared in pain, and lunged forward to bite at Rowan with its mandibles, but the hero deftly stepped backwards to avoid it, and slashed downward at the creature’s exposed neck."
            "It wasn’t enough to sever the head, but it was certainly a mortal blow, and the drider collapsed, writhing in pain. While it was in its death throes, Rowan went to the man and cut him free of the webbing."
            "He was rather shocked but unharmed by the assault, and after thanking Rowan profusely for saving him, headed off in search of pants"
            "Now free of any prying eyes, he signalled the orcs to come and collect any eggs that may have been left behind."
            #gain 20xp, lose a little guilt
            $ add_exp(20)
            $ change_base_stat('g', -1)
        else:
        #fail
            "The creature lunged forward with its front legs as Rowan brought his sword up to block, barely pushing them wide enough to avoid piercing his chest."
            "Down came the drider’s jaw as it buried its mandibles into the hero’s shoulder. Gritting his teeth against the pain, he brought his sword up, driving it through the monster’s chest."
            "It slumped backwards under the weight of the mortal blow, writhing in pain. While it was in its death throes, Rowan went to the man and cut him free of the webbing."
            "He was rather shocked but unharmed by the assault, and after thanking Rowan profusely for saving him, headed off in search of pants."
            "Now free of any prying eyes, he signalled the orcs to come and collect any eggs that may have been left behind."
            #gain 10xp, lose a little guilt, gain one wound
            $ add_exp(10)
            $ change_base_stat('g', -1)
            $ take_damage(1)
    "Watch what happens.":
        $ released_fix_rollback()
        "Deciding it would be too risky to get involved, Rowan watched as the monster lowered itself onto the man’s cock."
        "It was clearly enjoying the act, toying with its prey and it rose and fell on top of him. The man, for his part, had stopped yelling for help and was grunting and groaning as the drider rode him."
        "It wasn’t too long before he was completely spent, and the creature got off him. Weaving more strands of webbing around him to further enforce his captivity, it dragged him off in the opposite direction, away from the hero, by its spinneret."
        "With the coast now clear, the human contacted the orcs to come and collect  any eggs that may have been left behind."
        #gain a little guilt
        $ change_base_stat('g', 1)

$ world.cur_map.resources[world.cur_map.pos].capture()
return
