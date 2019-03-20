# random map events that happen on plains
init python:

    # Local guide (Benediction)
    event('local_guide', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # A minor noble's gift (choice)
    event('minor_noble_s_gift', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Bandit attack (malediction)
    event('bandit_attack', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Snake bite
    event('snake_bite', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Monster hunter team
    event('monster_hunter_team', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Blighted farm
    # Req: First half year, already hear about famine looming.
    event('blighted_farm', triggers='map_expl', conditions=('world.cur_tile_type == "plains"', "week <= 24"), depends=('famine_looms',), run_count=1, group='map_expl', priority=pr_map_rnd)
    # Site of occult ritual
    event('site_of_occult_ritual', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Drakken highwaywoman (malediction)
    #No requirements
    event('drakken_highwaywoman', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #Roadside incident (judgement)
    #Req: Rowan has low corruption or is pure.
    event('roadside_incident', triggers='map_expl', conditions=('world.cur_tile_type == "plains"', 'avatar.corruption < 10'), run_count=1, group='map_expl', priority=pr_map_rnd)


label local_guide:
# Local guide (Benediction)

#countryside BG
scene bg31 with fade

"While he travelled the plains of Rosaria, Rowan came upon another traveller, a hunter by his style of dress. The man greeted him warmly and asked about his health."
"Upon learning Rowan's name and confirming that he was indeed the great hero from the war, the hunter offered to help Rowan in whatever way he could."
"Rowan took him up on the offer, asking for help in navigating the area and with mapping the region. The tips and information he gained from his guide helped Rowan travel through this area much faster than he otherwise would have."

# +3 movement points (this turn only)
#~ $ movementPoints += 3
$ change_mp(3)
# +10 xp
$ add_exp(10)
return

###################################################################################################
###################################################################################################
###################################################################################################


label minor_noble_s_gift:
# A minor noble's gift (choice)

#countryside BG
scene bg31 with fade

"On this day, Rowan had a fortuitous encounter with a minor noble's hunting party. The leader almost immediately recognized the hero for who he was and greeted him warmly."
"After thinking for a moment, Rowan was able to place the man's face as one of the officers in the Rosarian army during the war. The two of them had never been introduced."
"The noble didn't mind that Rowan didn't know his name, in fact he almost refused to even give it when Rowan asked."
"Even afterwards, he insisted in giving a gift of gold to the Rosarian hero from the war, something that Rowan deserved far more than he did."


menu:
    "Diplomatically reject the gift and praise his family." if ('history_of_rosaria' in castle.completed_researches): #(Req: History of Rosaria)
        $ released_fix_rollback()
        "With the knowledge of the etiquette and history of Rosaria that Cliohna had armed him with, Rowan was able to gracefully decline the gift while also praising the man for his family's contribution to the war."
        "The noble was incredibly impressed that Rowan knew what he'd done and promised to tell everyone of the hero's selflessness in service for his country."
        # - small amount of infamy
        $ change_base_stat('f', -2)
        # +10 xp
        $ add_exp(10)

    "Accept the gift and turn it over to the twins.":
        $ released_fix_rollback()
        "Having little other choice in the matter, Rowan accepted the gift to avoid upsetting the noble."
        "Later, he reported what had happened to Jezera, who was quite pleased with Rowan's deviousness in acquiring funding for their operations."
        # + small amount treasury and + small amount corruption
        $ change_treasury(10)
        $ change_base_stat('c', 2)
        # + small appoint Jezera opinion
        $ change_relation('jezera', 2)
        # +10 xp
        $ add_exp(10)

    "Accept the gift, but give it away before you return to the castle.":
        $ released_fix_rollback()
        "Having little other choice in the matter, Rowan accepted the gift to avoid upsetting the noble."
        "However, later he would leave the money nearby a farmer's door.  When their family found it later, they would no doubt put the gift from an unknown benefactor to good use."
        # - small amount corruption
        $ change_base_stat('c', 2)
        # +10 xp
        $ add_exp(10)
return

###################################################################################################
###################################################################################################
###################################################################################################


label bandit_attack:
#Bandit attack (malediction)

#countryside BG
scene bg31 with fade

"Bandits!  There is always a risk when travelling Rosaria these days of being accosted by ne'er-do-wells, and the hero turned demonic agent was now faced with just such a group."
"There was no other choice, he'd have to fight them."


# Combat check (d20 + str mod)
#~ $ res_roll = dice(20) + avatar.stat_mod('strength')
$ event_tmp['combat roll'] = check_combat(11)[1]
$ released_fix_rollback()

if event_tmp['combat roll'] >= 11:
    #11+ - Pass (defeat them):
    "Of course, such foes posed little challenge for an experienced warrior like Rowan. Though even one such as him was unable to escape completely unscathed."
    "After dispatching them, Rowan turned the bandits over to the baron's forces. As thanks for this service, he was granted their ill gotten gains and would later bring them back with him to Castle Bloodmeen."
    "On the other hand, word quickly got around that the hero of the siege of Karst was doing his part to keep the bandit problem down."
    #+15 xp
    $ add_exp(15)
    #Rowan is lightly wounded (lose 1 movement point until rest), + small amount treasury, - small amount infamy
    $ change_treasury(10)
    $ take_damage(1)
    $ change_base_stat('f', -2)

elif event_tmp['combat roll'] >= 6:
    #6-10 - Partial pass (fend them off):
    "There were so many of them that they nearly overwhelmed Rowan. Only his skill and experience as a warrior held them at bay long enough for them to decide he wasn't a target worth hunting and bid a hasty retreat."
    "Even with his injuries, Rowan was still able to bring down one of them and turn them over to the baron's forces. Word soon spread that the hero of Karst had sent some bandit home with their tails between their legs."
    #+10 xp
    $ add_exp(10)
    #Rowan is wounded (lose 3 movement points until rest), - smaller amount of infamy.
    $ take_damage(3)
    $ change_base_stat('f', -1)

else:
    #5 or less - Fail (captured and ransomed):
    "Even someone as experienced a warrior as Rowan still has to be wary of overconfidence and when they are outclassed. On this day, he was reminded of that very fact when he found himself overwhelmed and captured by the bandits."
    "They dragged his banged and bruised body back to their hideout, where Rowan was kept restrained until Jezera was able to ransom him from the bandits with funds from their treasury."
    #+5 xp
    $ add_exp(5)
    #Rowan is wounded (lose 3 movement points until rest), - small amount treasury, end turn regardless of remaining moves.
    $ take_damage(3)
    $ change_treasury(-10)
    # TODO: make castle.treasury a limited property
    # $ if castle.treasury < 0: castle.treasury = 0
    $ renpy.set_return_stack(renpy.get_return_stack()[:1])
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label snake_bite:
#Snake bite

# Show countryside background
scene bg31 with fade
show rowan necklace shock behind bg31

"While walking on the plains of Rosaria, one should endeavor to keep their eyes open for greensnap snakes."
"Their bites may not be lethal to most humans, but they hurt like hell and the effects of their poison causes irritability and making sleep difficult for some time."
"Unfortunately, spotting these creatures is next to impossible due to the camouflage of their scale pattern. A greensnap usually won't bite anyone unless they actually step on one."
"Sometimes you're just unlucky."

ro "Ahhh!  Damn, greensnap!"

# add 10 xp
# End scene, Rowan is injured, -reflex poison.
$ add_exp(10)
$ add_effect(Injury('Greensnap poison', 'reflexes', -2))
return
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label monster_hunter_team:
# Monster hunter team

# Show countryside background
scene bg31 with fade

"Rosaria is home to a well known monster hunting guild. From here almost all of the mightiest slayers are members or at least started their carriers."
"Teams are a fairly common sight in some areas of the realm where infestations are present or when other creatures are encroaching on human lands."
"Today Rowan ran into one such group. They instantly recognized the hero for who he was. As was often the case, his reputation had preceded him."

if avatar.infamy < 10:
    # Test low infamy: Pass
    "The story and history of the hero of Karnas won out today over the agent of the twins and he was greeted as a friend and idol."
    "Since the hunters were returning from a successful endeavor, they offered Rowan their leftover potions as a small gift."
    # End scene: add 10 xp, Rowan gains some minor stat bonuses for a couple weeks.
    $ add_exp(10)
    $ add_effect(MultiEffect('Potions bonuses', 'pos', (('strength', 1), ('reflexes', 1), ('vitality', 1)), 5))
    return
else:
    # Test low infamy: Fail
    "The stories of the atrocities that Rowan had been forced to commit were growing strong."
    "So strong in fact that this group actually decided to attack Rowan on sight, evidently hoping to either defeat evil or claim some bounty."
    if check_skill(10, 'escape')[0]:
        $ renpy.fix_rollback()
        # Escape challenge: Success
        "Since he was outnumbered against experienced foes, the agent of the twins opted to quickly make an escape rather than face the group head on."
        # End scene, add 10 xp, no effect.
        $ add_exp(10)
        return
    else:
        $ renpy.fix_rollback()
        # Escape challenge: Fail
        "When outnumbered against experienced foes, the best course of action is to escape.  The twin's agent knew this, as did his opponents. Only after a protracted defensive fight did Rowan finally find an opening and manage to slip away."
        "He'd gained some injuries during the experience and had been forced to cut down one of the hunters. This wasn't going to help his reputation at all."
        # End scene, add 5 xp, +infamy, Rowan is injured.
        $ add_exp(5)
        $ change_base_stat('f', 2)
        $ add_effect(Injury('Wounds', 'strength', -2))
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label blighted_farm:
# Blighted farm
# Req: First half year, already hear about famine looming.

# Show countryside background
scene bg31 with fade

"Another abandoned farm. Rowan had already found several in the area over the last few days. He decided to take a closer look and see if he could ascertain the reason for this."
"After checking two of them, he'd figured he had a good idea why."
"All of the granaries were empty, so no food left. On top of that, the crops in the fields had strange spots all over them, some kind of blight."
"He did a little further investigating and discovered that the same plant plague was responsible for the poor harvest last year."
"With famine already on the horizon, the year's crop already looking extremely poor did not bode well for the people here. Already farmers were abandoning their lands to become refugees, hoping to find food elsewhere."
# add 10 xp
# end scene.
$ add_exp(10)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label site_of_occult_ritual:
# Site of occult ritual
# No req.

# Show countryside background
scene bg31 with fade

"Signs of a fire, strange scratchings in the ground, two rotting animal corpses that had been drained of blood."
"At first Rowan had thought he'd found a campsite from the night before, but the more he looked the more certain he was that it was something else. This was no ritual of Solensia, this was either something born of occult superstition or the allure of chaos."
"Unless he got someone more attuned to magic than he was, there was no way to know for certain if anything beyond hopeful hokey pokey had occurred here. However, the very fact that people had been resorting to such things in his homeland disturbed the hero."
"He'd be keeping his eyes out for more signs of the occult and chaos worship as his scouting continued."
# add 10 xp
# End scene.
$ add_exp(10)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label drakken_highwaywoman:
#Drakken highwaywoman (malediction)
#No requirements

#Show countryside background.
scene bg31 with fade

"One of the less seen races in Rosaria are the drakken; the descendants of humans and dragons. Running across one by chance on the road is almost unheard of. One that has turned to banditry was even rarer."
"Rowan had just come face to face with one such highwayman. Or highwaywoman, as it were."
"She demanded his money, with the threat to take it by force if he did not comply. A very common demand from outlaws, but by no means a common demander."

#If treasury has less than 30 gold.
if castle.treasury < 30:
    $ released_block_rollback()
    "The hero laughed at her and casually informed her that she'd picked a poor target to rob, as he didn't have money on him. He didn't explain that the treasury was so low that he simply couldn't afford to carry any around."
    "He even let her pat him down, somewhat thoroughly, until she finally flew away in a frustrated huff. It was a bit of a lucky break for Rowan that she'd tried to rob him now of all times."
    #End scene. 5xp,  no effect.
    $ add_exp(5)
    return

#else
else:
    "This wouldn't be an easy battle, the hero needed to be in top form to hope to take on a drakken in a fair fight."
    menu:
        #Choice: Pay her 30 gold.
        'Pay her 30 gold':
            $ released_fix_rollback()
            "He decided that it wouldn't be worth the risk of a battle, and handed over the money he was carrying. Pleased with his 'gift', the dragonblood smiled and blew a kiss to Rowan before flying away."
            #End scene. 10xp, lose 30 treasury.
            $ add_exp(10)
            $ change_treasury(-30)
            return
        #Choice: Fight her.
        'Fight her':
            $ released_fix_rollback()
            $ temp1 = current_weapon()
            "Rowan drew his [temp1], preparing to square off with the dragonblood.  Before their battle began, he tried playing the hero card to get her to back off. The response was that being a great hero only meant that he was on the top of the pile of human filth, but was still human filth."

            #combat DC13
            #Fight challenge, success:
            if check_combat(13)[0]:
                $ released_fix_rollback()
                "The drakken proved to be overconfident to a fault. She sought to quickly overpower her opponent through sheer force, which Rowan was quickly able to turn against her. A hard impact on the ground and a large gash on the leg soon followed."
                "Realizing her folly, the winged woman made a hasty retreat, flying away from what she'd just thought was an easy target mere moments before."
                "Rowan watched her go, then cleaned and put away his sword."
                #End scene.  20xp.
                $ add_exp(20)
                return
            #Fight Challenge, failure:
            else:
                $ released_fix_rollback()
                "The drakken fell upon the man with a vengeance. She sought to quickly overpower her opponent through sheer force, which Rowan would normally have been able to turn against her. However, he wasn't in the best of shape on this day."
                "She simply bowled over his feeble attempt to flip her into the ground and dug large gashes into his body with her claws. It was all over in a single attack, with the winged woman triumphantly straddling her foe."
                "After tearing through his pack and swiping the thirty gold pieces her target had been carrying, she planted a kiss on his lips and then flew away."
                "Rowan watched her go, then struggled to get upright so he could bandage the wounds she'd left him. That hadn't gone well."
                #End scene. 10xp, rowan is injured.
                $ add_exp(10)
                $ add_effect(Injury('Wounds', 'strength', -1))
                return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label roadside_incident:
#Roadside incident (judgement)
#Req: Rowan has low corruption or is pure.

#Show countryside background.
scene bg31 with fade

"While on one of the side roads that criss-cross over the plains, Rowan encountered an incident of sorts. Two horse drawn carts had collided with one another, and the two owners were involved in a heated argument."
"The two were very agitated and after seeing Rowan, one asked him to mediate their dispute as both because he was an outsider and a hero. One believed that the other needed to pay for the damage caused, the other didn't think that was very fair."
"After inspecting the scene a little and hearing both stories, it became obvious to Rowan that the man trying to avoid paying for damages was the one at fault. There was no reason, save for carelessness or maliciousness that could have caused the collision."
"However, shortly before he made his decision, the man at fault quietly told him that he'd be willing to give the hero half of the money he'd need to pay if a judgement was made in his favor."
menu:
    #Choice: Accept the bribe and side with the man at fault.
    'Accept the bribe and side with the man at fault':
        $ released_block_rollback()
        "After making the judgement and watching the other trader storm off while ranting about being cheated, Rowan accepted the payment from the other trader."
        "He felt guilty about doing this, but he needed to get any money he could to protect himself and his wife."
        #End scene.  Gain 10xp, 30 gold, gain little guilt, gain little corruption, gain little infamy.  This is nowhere near as bad as attacking villages.
        $ add_exp(10)
        $ change_treasury(30)
        $ change_base_stat('g', 1)
        $ change_base_stat('f', 1)
        $ change_base_stat('c', 1)
        return
    #Choice: Side with the man in the right.
    'Side with the man in the right':
        $ released_block_rollback()
        "Rowan's sense of justice wasn't about to be swayed by a pouch of coins, he sided with the man who was owed. The other merchant called him a fool before paying the other and storming off."
        "The man who'd been wronged praised the hero for his high morals after learning that the other had tried to bribe him. He called him a good friend and that everyone he met would hear of this justice."
        #End scene. Gain 10xp.  Lose a little corruption, lose a little infamy.
        $ add_exp(10)
        $ change_base_stat('c', -1)
        $ change_base_stat('f', -1)
return
