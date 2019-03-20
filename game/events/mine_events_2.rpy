# events for mines (hire workers, deploy soldiers etc.)
init python:

    #Orc Mine
    event('orc_mine', triggers=('map_res_6', 'map_res_7', 'map_res_8',), group='mine', run_count=1, priority=pr_map_res)


label orc_mine:
#Orc Mine

#mine BG
scene black with fade
show rowan necklace neutral behind black

"Usually, Rowan encountered mines that were either abandoned or occupied by humans."
"This time, things were different."
"As he scouted the approach to the mine, he saw a familiar sight near the entrance of it."
"Orc tribal signs, painted in red. Fresh ones, to boot."
"Rowan scratched his chin in deep thought. Based on his information, the mine was still functional recently. It looked like some time ago a group of orcs kicked out the old owners out, and made the location their new base of operations."
"If they could be convinced to join the twins, then they would gain both an operating mine and a new tribe of orcs. This was a unique opportunity… But simply walking in and demanding the orcs submit could prove risky."
"A show of strength would ensure nothing goes wrong."

#Army screen pops up.  Rowan is required to send at least 60+ military strength. It checks for driders and succubi as well.
call screen raid_menu(60)

#On cancel, once only.
if not raid_state.in_raid:
    "But Rowan couldn't commit the necessary forces now. He should return later, once he has enough soldiers available."
    #return to map, mine is unclaimed, can return for same event
    $ prevent_tile_exploration()
    # TODO: return here to same event
    return

#if forces are assigned
"Soon, he stood in front of the mine entrance, a small army behind his back."
'It was time to "discuss" the terms of the "alliance".'

ro "Send the message."

#if some of the assigned troops were orcs
if raid_state.troops.get('orc', 0) > 0:
    "A muscular orc, carrying a horn in his hand, stepped forward. He took a deep breath and sounded it three times."

#IF = somehow Has ONLY driders in the battle group. (easter egg)
elif raid_state.troops.get('orc', 0) == 0 and raid_state.troops.get('cubi', 0) == 0 and raid_state.troops.get('drider', 0) > 0:
    "The surrounding driders looked at him dumbly, not understanding."
    ro "…"
    ro "(Maybe I should’ve brought some orcs with me for this)"

    "Left with no choices, Rowan brought his hands to his face, and shouted out loud."

    ro "IN THE NAME OF CASTLE BLOODMEEN, I DEMAND AN AUDIENCE WITH YOUR LEADER!"

#rejoin
"At first, nothing happened."
"Fifteen minutes later, they could hear a group approaching. A large, young orc, leading about a dozen orc warriors, emerged from the mine."
"The leader took a long look at Rowan's forces. His expression darkened, as he realized what was about to transpire."

orcl "What do you want, humie?"

"While Rowan disliked intimidating people into compliance… He couldn’t deny the effectiveness of it."
"What followed was a short exchange to establish who had the upper hand in the negotiations. Rowan demanded that the orc tribe submitted to the twins authority."
"The orc answered he knelt to nobody. Rowan casually pointed out his meager force had no chance of surviving in a direct battle. The orc said they would see about that."
"He was bluffing, and Rowan was sure of that. The orc was smart enough to realize he had no chance of winning this one, but his pride wouldn't allow him to simply bend the knee. He needed a way to submit that wouldn't jeopardize his position among his fellow warriors."
"A promise of future conquests, and a gift, of either slaves or gold, would certainly do the trick."

#Calculations:
    #Base Gold: 90.
        # -20 if you have more than 100 military power invested in the event
        # -20 if you have driders with you.
    #base slave amount: 7
        # -2 if you have more than 100 military power invested in the event
        # -2 if you have driders with you.
$ event_tmp['gold_cost'] = 90
$ event_tmp['slave_cost'] = 7
$ event_tmp['bribe_with'] = None
if raid_state.mp > 100:
    $ event_tmp['gold_cost'] -= 20
if raid_state.troops.get('drider', 0) > 0:
    $ event_tmp['gold_cost'] -= 20

if raid_state.mp > 100:
    $ event_tmp['slave_cost'] -= 2
if raid_state.troops.get('drider', 0) > 0:
    $ event_tmp['slave_cost'] -= 2


$ temp1 = event_tmp['gold_cost']
$ temp2 = event_tmp['slave_cost']
"Rowan estimated it would take about [temp1] gold or [temp2] slaves to make the orcs submit."
"That is… If he really wanted them at his side. With the forces currently at his disposal, taking the mine by force would be easy. He would lose a tribe, but perhaps they weren’t worth the cost?"

menu:
    "Bribe them with gold.":
        $ released_fix_rollback()
        $ event_tmp['bribe_with'] = 'gold'
        jump .mineBribe

    "Bribe them with slaves.":
        $ released_fix_rollback()
        $ event_tmp['bribe_with'] = 'slaves'
        jump .mineBribe

    "Eradicate them.":
        $ released_fix_rollback()
        "There was no small amount of orcs waited to be recruited. Rowan could afford to lose this group."
        "Without another word, he signaled for his men to ready their arms."
        scene black with fade
        "…"
        "The following battle was long and bloody."
        "The enemy orcs quickly retread into the mines, trying to take advantage of the narrow corridors inside them. A good strategy, which might have worked against someone less experienced than Rowan."
        "Maintaining discipline, Rowan prevented his forces from swarming inside and instead formed a small strike force with him at the vanguard, which, albeit with some difficulty, ultimately broke through the enemy defenses."
        "After that, it was merely a matter of cleaning up the strays."
        "Soon, Rowan could inspect the mine in all it had to offer. As he expected, it was still operational, and he sent orders to the castle to send the workers in."
        "He also found the half-built orc village. They were still just settling in."
        "… But they already managed to do some raiding in the area."
        "In one of the huts, he found three human slaves. With his forces nearby, he couldn't set them free without raising suspicions, so he had them delivered to Castle Bloodmeen."
        "Soon, the area was secured, and Rowan could move to his next target."
        #GAIN: Operating Mine and +3 slaves.
        #Lose: Small amount of military power.
        $ change_prisoners(3)
        # TODO: lose small amount of military power
        $ castle.mines += 1
        $ castle.iron_per_week += mines_defs[world.cur_hex[6]][2]
        $ raid_state.finish()
        return

################################################################################

label .mineBribe:

"Praising the orcs stubbornness, Rowan remarked that this was precisely what the twins expected from their orcs. He hinted that those loyal to Castle Bloodmeen could expect to be compensated for their services and that they will receive a sample of their generosity soon."
"This placated the orc leader, and Rowan could see the obvious relief in his eyes at the sudden chance of saving face."
"Graciously, the orc responded they will consider the proposal if the gifts are up to their liking."
"Rowan did not have to add his little entourage would be back in full force if they dared to find them lacking."
"It was implied."
"..."
scene black with fade
"As expected, he got a message from castle Bloodmeen a few days later, telling him the orc leader found the gift acceptable, and that both the mine and the orc tribe were now at their disposal."
#GAIN: One fully operation mine AND one orc settlement.
#LOSE: Bribe (either gold or slaves, depending on choice).
$ castle.mines += 1
$ castle.iron_per_week += mines_defs[world.cur_hex[6]][2]
$ raid_state.reset()
$ change_recruitment_bonus('barracks', 1)
if event_tmp['bribe_with'] == 'gold':
    $ change_treasury(-event_tmp['gold_cost'])
else:
    $ change_prisoners(-event_tmp['slave_cost'])
return
