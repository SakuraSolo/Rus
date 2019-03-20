init python:

    #Introduction
    #Triggered when Rowan enters the orc warband camp in Northern Rosaria for the first time.
    event('orciad_introduction', triggers='map_res_105', run_count=1, group='orciad_camp', priority=pr_map_res)
    #Camp Menu
    #should show after the intro, and every time on entering the camp after
    event('campMenu', triggers='map_res_105', conditions=("week >= 4",), depends=('orciad_introduction',), group='orciad_camp', priority=pr_map_res)





label orciad_introduction:
#Introduction
#Triggered when Rowan enters the orc warband camp in Northern Rosaria for the first time.

#orc warband CG
scene black with fade
show rowan necklace shock behind black
show andras displeased behind black

ro "Whoa!"

"Hidden amongst the trees and rocks overlooking one of the many smaller valleys that branched off of the main Rosarian Valley, Rowan had discovered what appeared to be massive orcish warband!"
"He watched as a few thousand orc soldiers milled about crude tents and campfires. This obviously wasn't a village or settlement, but they didn't seem to be doing much right now either. A report to Bloodmeen needed to be sent immediately."

#fade to black and back

"While he waited, he realized that there seemed to be a divide among the orcs. What had first seemed to be one camp was actually two, with an obvious gap between them."
"Fights occasionally broke out along the boundary line, and the man could see at least two corpses remaining from previous skirmishes."

an "Well now, that's not a common sight."

show rowan necklace neutral behind black

ro "Glad you could join me, master."

"The man whom Rowan had been waiting for, joined him in his hiding place and observed the large camp below."
"This army that they had discovered would be of great value to Bloodmeen, but the sheer size of it meant that it would be much more difficult than smaller tribes to bring into the fold."

if goblinRecruit == False:
    "However, a great army was exactly what the twins wanted Rowan to find, and he had found it. Andras certainly had a glint in his eyes that indicated he was quite pleased by this discovery as well."
    an "It would seem that you have found an alternative to the goblins, excellent. Orcs are far stronger and more brutal than those small weaklings."
else:
    an "Another army?  Well having two would certainly be nice, assuming you can get them to follow us. Do be efficient with your time, I wouldn't want something vital missed while you were trying to dick kiss me with a proper orc army."

"He looked down on the camp for a moment before continuing."

an "I can see why you didn't want me to make a grand entrance. What is your plan, servant?"

ro "I figure that the first step should be to meet with their leaders, find out why they're here and go from there."

"Rowan hesitated a moment, considering his words."

ro "I would have done that myself ahead of time, but being a human means that it wouldn't be safe for me to go in on my own."

"The half-demon looked over the valley with a thoughtful look on his face before answering."

an "I'll forgive you using me as a diplomatic shield, if you can get me a new orcish army."

"The man fingered his amulet as he answered."

ro "Yes, master."

scene bg26 with fade
show rowan necklace neutral at midleft with moveinleft
show andras displeased at edgeleft with moveinleft

"It was evident even as they made their approach to the camp that discipline was long gone, if it had ever been there at all. The pair didn't see any scouting patrols or even guards at the edge of the camp."
"While there were several raised heads as the two of them were moving through the tents, no one made any move to stop or even speak to the intruders that had waltzed right in."

show tarish neutral at midright with moveinright

"The first sign of any order at all came when a small group of female orcs caught up with Rowan and Andras from behind them, and their leader addressed the demon."

tar "Boss demon, what brings you to orc camp?"

"Andras looked questioningly towards Rowan, curious if he should speak or not."

menu:
    "Let Andras decide how to continue.":
        $ released_fix_rollback()
        "Rowan bowed his head slightly and waited for his master to speak."
        #if player chose might society
        if society_type == 'might':
            an "I am Andras, lord of Bloodmeen and I have come to lay claim to this army, as is my right. Why have you stopped me, woman?"
        #else
        else:
            an "I am Andras, Emperor of Bloodmeen and I have come to lay claim to this army, as is my right. Why have you stopped me, woman?"
        #rejoin
        "The orc's eyes went wide in shock at this revelation, then she quickly glanced around the tents to see if anyone else was paying attention to what had just been said."
        tar "Shh! Don't say that so loud."
        "She waved to her companions, who scattered and started searching the nearby area more thoroughly. Andras looked on with a bemused expression."
        "Rowan decided he'd best take over for the time being, things had taken a turn he hadn't expected."
        ro "Why? Is there disloyalty or hatred towards the demon lords here?"
        tar "No, is different problem. Come, we talk in private."

    "Speak on Andras's behalf, claim to be seeking out soldiers for a new army.":
        $ released_fix_rollback()
        ro "My master has come in search of soldiers for his army. Your numbers have intrigued him, though I see that your discipline is rather lacking."
        tar "Yous want orcs to fight for you? I might help with dat."
        "She waved to her companions to form up around the two. Andras looked at them with a mix of bemusement and annoyance on his face."
        ro "How exactly are you going to do that?"

    "Speak on Andras's behalf, claim to be looking for the leader of this band.":
        $ released_fix_rollback()
        ro "My master has come to speak with the leader of this band. Unless you command this force, it would be in your best interests to tell us where we might find them."
        tar "Is two chiefs. Fight over pretty girl. Very bad business. Should talk to me before you meet wit dem."
        ro "Oh? Would this be something that you can't tell us here?"
        "She waved to her companions to form up around the two. Andras looked at them with a mix of bemusement and annoyance on his face."
        tar "Can promise good talk boss demon."

    "Speak on Andras's behalf, say you intend to discover where the band came from.":
        $ released_fix_rollback()
        ro "My master has come to discover the origin of this band and why you seem to be just sitting here. Why do you fight amongst yourself instead of raiding the humans?"
        tar "Was raiding pinks, then big orc find pretty lady and won't giv'er up."
        ro "Give her up?"
        tar "Yes, come, can tell more away from dis place."
        "She waved to her companions to form up around the two. Andras looked at them with a mix of bemusement and annoyance on his face."
        ro "Surely this isn't a big secret?"

"The orcish woman waved the two to follow her, and set off towards another part of the camp."

hide tarish with moveoutright

"The half-demon turned to his companion with a quizzical look on his face. Rowan only shrugged, the orc woman hadn't given him anything to go off of and he doubted that she could cause them much trouble, so there wasn't anything wrong with following her."
"Andras came to a decision and started following the orc woman, Rowan trotted after him obediently."

hide rowan with moveoutright
hide andras with moveoutright

scene black with fade
scene bg26 with fade
show tarish neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve
show andras displeased at edgeleft with dissolve

"Evidently this woman held a fairly high standing in the orcish hierarchy, she had her own, though much smaller than the other two, camp that Rowan had missed before now."
"She'd led them back here and was now sitting with them in private, with a well cooked pig roast between them."
"While Rowan was hesitant to partake in orcish cuisine, Andras had no such problem and was devouring much of the roast whole. He had more decorum than the orc woman did, but she only ate the meat."

ro "Well, I think you'd best be telling us why you wanted to meet with us here."

an "Yes, that was rather presumptuous of you to insist we follow you. What does an orcish woman of some standing, but not true leadership, want with the ruler of Bloodmeen?"

"She picked at her tusk for a moment before answering.  Right away Rowan noticed the tick, if he wasn't mistaken, it looked like she was nervous."

tar "Am Tarish, warrior of Ulcro's hoard. Dis be what left of Ulcro's hoard after war."

"She spread her arms wide, referring to the camp that was outside."

tar "We run from pinks North who ride beasts and cover themselves with heavy armor."

ro "Prothea's Legions."

"Andras nodded."

tar "A moon ago, warrior Batri comes back from raid with really pretty pink girl in nice dress. Ulcro took her, made Batri mad. He challenged for rule but Ulcro won't fight him. Camp split in two. Now we sit here waiting for North pinks to come and kill us."

an "All over a woman?"

tar "Boys dumb, thinking with cocks. If both gone, I'd become chief of da hoard by making pretty girl hoard slut like pink girls ought be. Get me girls close to Batri and Ulcro, get me da pink girl, and we make em kill each odder."
tar "Den we raid again and we do boss demon's jobs."

scene black with fade
scene bg26 with fade
show rowan necklace neutral at midleft with dissolve
show andras displeased at edgeleft with dissolve

"An hour later..."

an "Even the orcish women are schemers... What do you make of this?"

ro "Well, Ulcro was a very accomplished general during the war, it would be in our best interests to recruit him if we can. However, from what I heard from the other women here, Batri is also quite skilled and has the advantage of youth."

an "Not a fan of Tarish's plan of offing both of them?"

ro "It doesn't seem very... orcish? It sounds more like what your sister would come up with."
ro "Tarish is a coward, she wouldn't fight Ulcro and Batri for the spot of chief, that's why she wants us to do her dirty work for her. That's not exactly orcish general material."

an "Heh, is there any reason we should even consider her offer?"

ro "She'd owe us and we'd be able to hang this over her for the rest of her life. Plus, getting an underhanded orc chief is pretty rare. I'm just not convinced she's worth giving the other two up."
ro " I should speak with the other chiefs and that woman that they're so taken with. Find out more before we make our decision. If you can convince Tarish to give me free passage through the camp, I can figure out what our move should be and then take care of this."

an "Are you sure you aren't just hoping to rescue the pretty lady yourself?"

ro "Getting the orcs for your army is my first concern."

an "For your sake, I hope so."

#Add Orc-iad quest to journal.  Add Orc-iad note1 to journal.
$ journal.start_quest('orciad')
$ journal.add_quest_note('orciad', 'note1')
$ orciad_state = 1
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label campMenu:

if orciad_ban == True:
    scene bg26 with fade
    show rowan necklace neutral behind bg26
    ro "I should avoid the camp after the last conversation with Batri."
    return
    
else:
    pass


if seen_delane_bad_end == True:
    jump delaneBadEnd2
    
else:
    pass


#Camp Menu
#should show after the intro, and every time on entering the camp after
$ prevent_tile_exploration()

if orciad_state != 2:

    if rowan_met_batri == 'met' and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.complete_quest_note('orciad', 'note1')

    if castle.buildings["brothel"].lvl == 0 and rowan_met_batri == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note10')

    if castle.buildings["brothel"].lvl >= 1:
        $ journal.complete_quest_note('orciad', 'note10')

    if castle.buildings["brothel"].lvl >= 1 and rowan_met_batri == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note11')

    if castle.buildings["brothel"].lvl >= 1 and rowan_met_batri == 'met' and met_with_delane == True and delane_corruption == True:
        $ journal.complete_quest_note('orciad', 'note11')
        
    if rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note14')

    if rowan_met_ulcro == 'met' and met_with_delane == True and ulcro_path == 3:
        $ journal.complete_quest_note('orciad', 'note14')

    if delane_gifts < 40 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note15')
        
    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.complete_quest_note('orciad', 'note15')
        $ journal.complete_quest_note('orciad', 'note18')
        
    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note16')

    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True and ulcro_path == 3:
        $ journal.complete_quest_note('orciad', 'note16')

    if rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note17')

    if rowan_met_ulcro == 'met' and met_with_delane == True and cliohnaDelaneHelp == "got":
        $ journal.complete_quest_note('orciad', 'note17')

    if delane_gifts > 39 and rowan_met_ulcro == 'met' and met_with_delane == True:
        $ journal.complete_quest_note('orciad', 'note17')


    if met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note19')

    if delane_trust == 3:
        $ journal.complete_quest_note('orciad', 'note19')
        $ journal.add_quest_note('orciad', 'note20')
        
    if met_with_delane == True and delane_corruption == True:
        $ journal.complete_quest_note('orciad', 'note20')
        
    if tarish_path == True and met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note21')
        $ journal.add_quest_note('orciad', 'note22')
        
    if got_jez_potion == True:
        $ journal.complete_quest_note('orciad', 'note21')
        
    if got_cla_poison == True:
        $ journal.complete_quest_note('orciad', 'note22')
        
    if met_with_delane == True:
        $ journal.add_quest_note('orciad', 'note23')
        
    if delane_plan == True:
        $ journal.complete_quest_note('orciad', 'note23')
        
    if delane_corrupt == True and batri_power > 10:
        $ journal.add_quest_note('orciad', 'note26')
        
    if delane_status == "batri":
        $ journal.complete_quest_note('orciad', 'note26')
        
    if delane_trust == 3 and got_jez_potion == True and got_cla_poison == True:
        $ journal.add_quest_note('orciad', 'note29')
        
    if delane_status == "tent" and delane_plan == True and delaneDistraction == True and delane_trust > 2 and delaneEscapePerimeter > 0:
        $ journal.add_quest_note('orciad', 'note31')

scene bg26

menu:
    "Explore the camp." if avatar.mp > 0:
        # (costs x movement point(s))
        # movement cost is applied in each event separately
        $ choose_and_insert_next_event('orciad_explore')
        $ orciad_explore += 1
        return
        
    "Go on a raid." if (rowan_joined_batri_s_raiders == True) and (avatar.mp > 0):
        $ released_fix_rollback()
        $ change_mp(-5)
        $ batri_raid_count += 1
        jump orcRaid

    "Visit Tarish, powerful orc woman." if (tarish_angered == False) and (delane_status == "tent") and delane_corrupt == False:
        $ released_fix_rollback()
        jump visitTarish

    "Visit Batri, rival for warchief." if delane_status == "tent":
        $ released_fix_rollback()
        $ choose_and_insert_next_event('orciad_batri')
        return

    "Visit the warchief Ulcro." if delane_status == "tent" and delane_corrupt == False:
        $ released_fix_rollback()
        $ choose_and_insert_next_event('orciad_ulcro')
        return

    "Hunt for gifts for Delane." if delane_status == "tent" and giftHuntAvailable == True:
        $ change_mp(-10)
        $ released_fix_rollback()
        jump hunt_for_gits
        
    
    #Sneak in to meet with [noblewoman/Lady Delane] (costs y movement point(s), can only attempt once each week)
    "Sneak in to meet with noblewoman" if (last_delane_visit_attempt < 1) and found_delane_tent and delane_status == "tent" and delane_corruption == False:
        $ released_fix_rollback()
        $ last_delane_visit_attempt += 1
        #Sneak in to meet with Lady Delane, the captured noblewoman
        #Selecting this option triggers a sneaking check (DC15), which Rowan can only attempt once per week.  There is no time cost to attempting this.  There should be some indication in game that tells the player they need to wait a week before trying to meet with Delane again.
        if check_skill(7, 'move_silently')[0]:
            #Success
            # TODO: not an event for now
            jump eleanorFirstVisit
        else:
            "Try as he might to slip into the noblewoman's prison, Rowan simply couldn't find a way past the guards. His attempt drew unfortunate attention from the guards, so he'd have to wait until next week to try again."
            jump campMenu

    "Corrupt Delane (Requires available spy)" if (rowan_met_batri) and (met_with_delane) and (delane_status == "tent") and delane_corruption == False:
        $ released_fix_rollback()
        if get_spies('idle'):
            jump corrupt_delane
        else:
            "Rowan needs an available spy in order to do this."
            jump campMenu

    "Plan Delane's rescue." if delane_status == "tent" and delane_trust == 3:
        $ released_fix_rollback()
        $ journal.complete_quest_note('orciad', 'note23')
        $ journal.add_quest_note('orciad', 'note24')
        $ journal.add_quest_note('orciad', 'note25')
        jump delaneRescuePlan
    
    "Leave orc horde camp.":
        #exit to map
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


#visit Tarish
label visitTarish:

if (met_with_delane == True) and (tarish_path == False):
    jump tarishQuest

elif (met_with_delane == True) and (tarish_path == True) and (get_cla_poison == False):
    jump tarishQuestReturn

elif (met_with_delane == True) and (tarish_path == True) and (get_jez_potion == False):
    jump tarishQuestReturn

elif (met_with_delane == True) and (got_jez_potion == True) and (got_jez_potion == True):
    jump tarishQuestComplete

else:
    pass


scene bg30 with fade
show rowan necklace neutral at midleft with dissolve
show tarish neutral at midright with dissolve

tar "Demon's pink."

ro "Tarish."

tar "We need dat pretty pink lady before I can become da chief. Find 'er, make 'er think you friend, den bring here."
tar "Do all dis, den I serve your master."

jump campMenu
