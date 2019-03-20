######## Winery events ########

#Private winery
#When claimed, gives a one time boost to morale.
init python:

    #Event 1: Choose a twin to gain a favor with.
    event('private_winery_raid_ev1', triggers='private_winery_raid', group='map_res_private_winery', priority=pr_map_res)
    #Event 2: Lose some cash and random soldiers totaling 20 base military strength (4 orcs for now).
    event('private_winery_raid_ev2', triggers='private_winery_raid', group='map_res_private_winery', priority=pr_map_res)
    #Abandoned Winery
    #Requires famine to still be active
    # TODO: check if famine still active
    event('abandoned_winery', triggers='private_winery_raid', run_count=1, depends=('famine_looms',), group='map_res_private_winery', priority=pr_map_res)
    #R & R
    event('r_r', triggers='private_winery_raid', run_count=1, group='map_res_private_winery', priority=pr_map_res)
    #Siege
    event('winery_siege', triggers='private_winery_raid', run_count=1, group='map_res_private_winery', priority=pr_map_res)


label private_winery_raid_ev1:
#Event 1: Choose a twin to gain a favor with.
$ change_morale(5)
"Once the guards at the winery realized how large a force was coming at them, they made tracks. With the winery now undefended, Rowan and the soldiers accompanying him looked through the stock and made off with it before burning the buildings down."
"A little was sampled on the spot, but the hero forbade any significant consumption until they'd returned to the castle. One particular bottle he picked out from the set for a special purpose, as it was definitely the most valuable of the bunch."
#Fade to black.
"This particular bottle was something special. Rowan had himself only enjoyed a single cup of it, during the celebratory banquet following the end of the war. However, that one cup was quite a cup and he knew that there was someone who would likely be very happy to have this bottle."
menu:
    #Choice: Give the bottle to Jezera.
    'Give the bottle to Jezera':
        "His mistress, the blue skinned Jezera, was extremely pleased with his gift. Not only was she quite fond of the drink for herself, but it would make a fantastic treat for her guests when in high society."
        "He'd definitely earned her favor for that, something he wouldn't regret."
        #Gain 1 favor point with Jezera.
        $ change_favor('jezera', 1)
        return

    #Choice: Give the bottle to Andras.
    'Give the bottle to Andras':
        "His master, the half demon Andras would take the bottle soon afterwards. At first he regarded the gift with disdain, but upon taking a drink his mood quickly changed."
        "Rowan had definitely earned his favor for that, something he wouldn't regret."
        #Gain 1 favor point with Andras.
        $ change_favor('andras', 1)
        return


label private_winery_raid_ev2:
#Event 2: Lose some cash and random soldiers totaling 20 base military strength (4 orcs for now).
$ change_morale(5)
"While the store itself was easy enough to capture, keeping the soldiers from partaking in the loot proved impossible. Rowan found that he would have had to cut down several of them to stop them from drinking themselves into a stupor."
"By the end of the day he wished that he had chosen to do so, as several of them had gotten lost on the way back to the castle. They never turned up."
"To make matters worse, the breakdown of discipline in the resulting party at the castle resulted in significant damages to the infrastructure that had to be repaired later. Orcs were very rowdy drunks."
#Lose some gold, lose 4 orc soldiers.
$ change_treasury(-20)
$ castle.buildings['barracks'].troops -= 4
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label abandoned_winery:
#Abandoned Winery
#Requires famine to still be active

"As Rowan approached the winery, he could tell that something was off even before he reached the main building."
"Being an easy target, he had only brought a small group of orcs with him to help him secure the location, but he now told them to hold back as he did a little scouting on his own."
"Entering the winery, he found it to be completely deserted, and judging from the dust that covered every surface, it had been so for a while."
"A cursory glance at his surroundings also revealed that anything of value had been taken, so whoever had left had probably not done so in a hurry."
"Whatever had caused the evacuation of the winery’s former owners, it seemed to Rowan that in all likelihood it had been planned."
"As the hero feared, they’d also emptied the stores before they had left. If the room had once been filled with bottles of the harvest’s bounty, it was no longer."
"Someone had either drunk the wine or taken it with them, and either way, it meant that he had been left with no way to raise the spirits of his nearby orc subordinates, nor those back at Bloodmeen."
"All that remained was to check the vineyard, and it was there that Rowan learned why the place had been abandoned."
"The blight had struck here, leaving the ground hard and cracked, and what remained of this year’s grape crop to wither on the vine. Capturing this place would be pointless, as even if the famine relented, it would be years before anything could grow in this soil."
"He returned to the orcs to move on, with nothing but wasted time to show for his efforts."

#Winery is explored, but not added to resources.
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label r_r:
#R & R

"For a change, everything had gone well for the hero."
"He had arrived at the winery before his troops and convinced the people who had been occupying it to leave before they showed up, avoiding any bloodshed."
"At first they had been loathe to leave their lives behind, but when he had pointed out that the alternate was the loss of their actual lives, they had seen reason."
"With the orcs out securing the grounds, he finally had a moment to himself. Such occurrences were rare these days, between his increasing duties and the watchful eyes of the twins."
"Finding himself in the store room, he perused the shelf until he found a good vintage, one that he had bottled before he was born."
"Knowing that he probably shouldn’t, he took his knife and popped the cork from the neck of the bottle. He’d worked hard, and he deserved a little reward, didn’t he?"
"Taking a deep sniff, he found the red to be rich and oaky, and knew that he had made a good choice."
"When the orcs came to find him a few hours later, he’d polished the entire bottle off by himself, and decided it wiser to spend the night there before heading off in the morning."
"The result of his little tipple had been a small loss of time, but he felt a lot better for the chance to spend a little time unwinding."

#lose 1 move point, lose guilt, lose one wound if able
$ change_morale(5)
$ change_mp(-1)
$ change_base_stat('g', -1)
$ heal_wounds(1)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label winery_siege:
#Siege

"Rowan cursed as he saw the bows sticking out from a second floor window of the winery, aimed in the direction of himself and his troops."
"One of the workers must have seen them approaching, and by now there was no doubt they would have secured the building as best they could to defend from the attackers."
"The ground floor windows had been blocked off using whatever furniture had been available, and he was sure there would be something heavy blocking the door as well."
"Assaulting the place now would be risky; even if the bowmen lacked skill there was no cover, and anyone trying to breach the door was almost certain to be struck by arrows from above."
"The situation would inflame the orcs already violent temperament, and capturing the occupants would be very difficult, even if they were willing to let themselves be taken alive."
"Rowan had three options; he could order to orcs to attack and hope for the best, knowing that anything can happen in the heat of battle."
"Or, he could try and talk the defenders down, but doing so would be a daunting challenge as they clearly had no intention of leaving their home."
"Lastly, he could simply leave, which, while not ideal, would at least ensure they there were no casualties on either side."

$ event_tmp['tried to negotiate'] = False

label .ws_menu:
menu:
    "Order the Assault.":
        $ released_fix_rollback()
        "Rowan had no choice, he had to capture the winery, so he ordered the orcs to take the building, and capture the inhabitants if possible."
        #roll 1d6 - result equals number of orcs casualties
        $ event_tmp['orcs casualties'] = dice(6)
        $ released_fix_rollback()
        if event_tmp['orcs casualties'] <= 3:
        #If 1, 2, or 3
            "Arrows rained down on the attackers, but they were able to clear the door quickly with few casualties."
            "When the building was taken and Rowan made his way to the second floor, he found the winery’s occupants, all five of them, apprehended alive as he had ordered."
            "As he instructed the orcs to secure the rest of the grounds and see the prisoners back to the nearest portal, he thanked the gods that things had not gone a lot worse."
            #Lose orcs equal to the die roll, gain 5 prisoners
            $ castle.buildings['barracks'].troops -= event_tmp['orcs casualties']
            $ change_prisoners(5)
        else:
        #If 4, 5, or 6
            "Arrows rained down on the attackers as they struggled to force the door open. By the time they were able to force entry, a number of orcs lay dead on the ground, peppered with arrows."
            "The orcs surged upstairs in a frenzy, and all the winery’s defenders were put to the sword before Rowan could arrive to stop them."
            "He ordered the orcs to secure the rest of the grounds, whilst the corpses spread around the room begged the question of if it had been worth the heavy price."
            #Lose orcs equal to the die roll, gain medium guilt
            $ castle.buildings['barracks'].troops -= event_tmp['orcs casualties']
            $ change_base_stat('g', 3)
        $ change_morale(5)
        return

    "Try to negotiate with them." if event_tmp['tried to negotiate'] == False:
        $ released_fix_rollback()
        #Diplomacy check DC15
        if check_skill(15, 'diplomacy')[0]:
        #Pass
            $ released_fix_rollback()
            "It took a good deal of time, but with much discussion and the promise that everybody would be allowed to leave unharmed, with anything they could carry, Rowan was able to talk the occupants of the winery down."
            "He looked on as they left unmolested, happy that he was able to bring about a peaceful resolution to the situation."
            #gain 25xp, lose small amount of guilt
            $ add_exp(25)
            $ change_base_stat('g', -1)
            $ change_morale(5)
            return
        else:
        #Fail
            $ released_fix_rollback()
            "Rowan did his best to try and persuade the inhabitants to leave the building of their own accord, but they were not having it."
            #dodge check DC12
            if check_skill(12, 'dodge')[0]:
            #Pass
                $ released_fix_rollback()
                "An arrow flew through the air in his direction, but Rowan was able to duck out of the way just in time as it sailed dangerously close over his head."
                "More arrows followed as he ran back toward cover. If he wanted to take the winery, he’d have to try a more aggressive tactic."
                #gain 15xp, lose one move point, return to previous menu with negotiate option removed
                $ add_exp(15)
                $ change_mp(-1)
                $ event_tmp['tried to negotiate'] = True
                jump winery_siege.ws_menu
            else:
            #Fail
                $ released_fix_rollback()
                "An arrow flew through the air in his direction, leaving a nasty gash in the hero’s arm. More arrows followed as he ran back toward cover."
                "If he wanted to take the winery, he’d have to try a more aggressive tactic."
                #gain 5xp, lose one move point, gain one wound, return to previous menu with negotiate option removed
                $ add_exp(5)
                $ change_mp(-1)
                $ take_damage(1)
                $ event_tmp['tried to negotiate'] = True
                jump winery_siege.ws_menu

    "Leave them be.":
        $ released_fix_rollback()
        "Rowan decided it was best not to risk it, as situations like this could get out of hand very fast."
        "He informed the orcs that they would be leaving, which raised grumbles and objections from the crowd, who were clearly spoiling for a fight."
        "Having been ordered for the second time by the hero though, they began to pack up their equipment to move on, clearly unhappy with the human’s handling of the situation."
        #lose morale, winery is explored but not added to resources
        $ change_morale(-5)
        return

