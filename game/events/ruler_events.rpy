init python:

    # Captured Merchant Cargo
    event('captured_merchant_cargo', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    # Andras is stressed
    # should be forced to occur by week 12 at the latest
    event('andras_is_stressed', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority="pr_ruler if week < 11 else pr_ruler_high")
    # Fire in the Stores, Type - Malediction, Tier - I
    event('fire_in_the_stores', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)
    # Orc Platoon Returns
    event('orc_platoon_returns', triggers="week_end", conditions=('week >=4',), group='ruler_event', run_count=1, priority=pr_ruler)


label captured_merchant_cargo:
# Captured Merchant Cargo

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

"'Solansia's breath,' Rowan thought as the soldiers carried the gold and other valuables into the throne room, 'good news for a change.'"
"Where the haul had come from, Rowan did not know, but as he watched, they continued to bring the sacks in, and he thought perhaps his luck was starting to change."
"Once all of the goods had been brought in, the leader of the group, a particularly fearsome orc by the name of Ozzag, came to stand before the throne."

show orc soldier neutral at orcright with moveinright

"After being commanded to give his report, he begans to tell Rowan of the good fortune that befell their unit when they were out on a routine patrol. They had been assigned to the mountain passes north of the frozen tundra."

os "...cold as Neiron's tits, but'sa good place for ambush. Path's narra, see, and snow provides plenty'a cover."
os "No ways round it either, so anyone who wants'ta go through tha' mountains, has'ta go through there."

"Rowan nodded, remembering the tales of snow blockades and ogres that Jezera had told him when she had visited them disguised as a damsel in distress."
"The passes of the Broken Mountains were treacherous, now even more so with his men patrolling them."

os "Anyway, been pretty quiet out there, see one of those ugly bastard ogres every now an' then, nothin' really to report on. 'Bout as exciting as'a Prothean virgin."

"The greenskin laughed at his own joke, letting out a throaty chuckle."

os "Mostly, the lads and I pass tha' time fuckin' and fightin', one way'a keepin' warm."
os "Anyways, other day sentry spots something different like, coming up the pass, and wouldn't ya knows it? Three trade caravans, all lined up, nice an' easy pickins."

"A grin revealed sharpened fangs as the orc gleefully recounted what had happened next to his superior. They set up in position and waited for the caravans to roll into the perfect spot for an ambush."
"Once they had the merchants surrounded on all sides, he signalled for the ambush to begin, and an arrow knocked one of the caravan guards clean off his horse."
"Whatever they were being paid, it must not have been worth dying for, as seeing the leading guard take a crossbow bolt in the chest was enough to make most of the other guards flee, leaving the traders to the mercy of Rowan's men."
"After that, it was mere child's play; the orcs struck down the remaining guards and traders where they stood, and a few minutes later they had dispatched them all without a single casualty."

os "Shame, was hoping for a good fight, but what can you expect from fuckin' humans?"

"Remembering who he was talking to, the orc flashed Rowan a grin."

os "No offence, of course."
os "Afta that I had tha men gather everything up, and bring it 'ere. An' don't worry, it's all there. Told the bastards I'd 'ave their 'eads if there was so much as a gold piece missin'."

"Rowan didn't doubt for a second that the orc meant what he had said, but now he had to decide what he should do with the spoils."

menu:
    "Keep the gold.":
        $ renpy.fix_rollback()
        "After careful consideration Rowan decided that the most prudent thing would be to place the money in the castle coffers for a rainy day."
        "He had to deal with many expenses after all, between outfitting and feeding the castle's denizens, and the general upkeep needed to keep the place running."
        "He ordered Ozzag to have his men take everything down to the castle treasury, but not before he picked up a small pouch of gold and slipped it into his pocket."
        "After all, you never know when a little extra gold may come in handy."
        #gain 100 gold
        $ castle.treasury += 100
        #end event
        return
    "Use the gold to hire more soldiers.":
        $ renpy.fix_rollback()
        "After spending some time weighing all the available options, Rowan decided that the best course of action would be to spend this money on recruiting more soldiers."
        "It was soldiers that had brought him this windfall in the first place after all, and he still needed many more if he was going to form an army."
        "Rowan instructed Ozzag to have his men take to money to Jezera so that she can bribe, hire, and influence people using her persuasive talents."
        #gain soldiers (To do)
        # TODO
        #end event
        return
    "Distribute the gold amongst the people of the castle.":
        $ renpy.fix_rollback()
        "After meditating on the issue, Rowan decided that the fairest thing that he could do with the spoils is to share them with the rest of the castle."
        "He had not been responsible for their acquisition after all, so it is only fair that he divided the good fortune among everybody."
        "Rowan asked Ozzag to instruct his men to distribute the spoils evenly between the inhabitants of the castle, making sure that everybody received a fair share by lot."
        "Even the orc seemed pleasantly surprised by his decision, which probably spoke volumes for how the rest of the castle's populace would feel."
        #boost to morale
        $ castle.morale += 5
        #end event
        return


##########################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label andras_is_stressed:
# Andras is stressed
# No requirements, high priority after 10 weeks (or 5 if you already had sex with Andras).  Should be before major NPCs are unlocked and can be placed in the dungeon.

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show andras displeased at midright with moveinright

an "Servant, drop what you're doing and service me. I need something to get my mind off of the useless rabble downstairs."

ro "What's wrong with your men?"

show andras angry at midright with dissolve

an "What's wrong?! They can't hit shit, they refuse to accept discipline, and I can't make examples of them!"

"Andras turned to face Rowan with a sharp glare in his eyes."

an "This is your fault! Why did I ever let you convince me not to cull the weak?!"

ro "We wouldn't have any troops then. You'll never have an army if you kill anyone who loses a single fight."

an "AHH!"

show bg6 with sshake
show bg6 with flash

"The red demon screamed in frustration, then punched his fist into the wall. The force of the impact left a sizable crater behind. Rowan winced, hoping his master wasn't about to cause more damage that would have to be repaired."

an "Grrr, why are you still talking? Didn't I tell you to service me?"

if andrasIntroSex == True:
    an "You know how to suck dick, get over here."
elif jezeraIntroSex == True:
    an "Forget about my sister, this time you're taking care of my needs."
else:
    ro "What makes you think I'll say yes this time?"
    an "I don't expect you to say anything! I expect you to just swallow my cock, you fucking slut!"

menu:
    "Tell him you're too busy.":
        $ renpy.fix_rollback()
        if not NTR:
            ro "I can't help you with that right now. You and your sister are already only letting me work here one day a week, that's barely enough time as it is to take care of your finances and planning."
            ro "I'd never get anything done if I have to take care of you every time something stresses you out a little bit."
            "Andras breathed heavily for several seconds, continuing his furious stare. Rowan worried that maybe the demon would finally ignore the logic of his arguments and snap."
            "After what felt like an eternity, his master finally seemed to back off. Instead of forcing a cock down Rowan's throat, Andras turned around and headed back down towards the barracks."
            an "Fine, I'll take out my frustration on some useless orcs then."
            menu:
                "Try and stop him.":
                    $ released_fix_rollback()
                    "Rowan shuddered as he thought about what was going to happen next. With the quotas and the goals that the twins had placed on him, he needed every soldier he could get."
                    "If Andras were to go down to the barracks, he’d no doubt kill half a dozen orcs, and that was half a dozen orcs he could not afford to lose."
                    ro "I’m afraid I can let you do that."
                    "Rowan drew his sword as the demon turned back to face him, and was surprised to see not the flash of anger that he expected, but a grin."
                    an "It is about time you showed some backbone human. Looks like I’ll get to take my frustrations out on you after all."
                    #combat check DC30
                    # TODO: this will never pass
                    if not dice(20) > 30:
                    #fail
                        "Without warning, the demon came at Rowan like a creature from the very depths of the hells."
                        "It was all he could do to bring his sword up just in time to stop the demon plunging one of his razor sharp claws into the hero’s chest."
                        "Time and again, Andras came at Rowan with lightning speed."
                        "He did his best to parry the blows, but after a few minutes, blood was leaking through from under the fabric of his tunic."
                        "Seeing the puddle of blood that had started to pool on the floor, the demon let out a chuckle."
                        an "I suppose I had better stop before I kill you. You were right though, this did help relieve me of some of my frustration."
                        an "Now go get yourself patched up before you bleed to death, I’d never hear the end of it from my sister otherwise."
                        #gain 10 xp and 2 wounds
                        $ add_exp(10)
                        $ take_damage(2)
                        #end scene
                        return
                    else:
                    #pass
                        "Without warning, the demon came at Rowan like a creature from the very depths of the hells."
                        "He was fast, inhumanly so, but a skilled warrior like Rowan had learned to anticipate his opponent’s attack, and was able to parry his razor sharp claws at every pass."
                        "After a few minutes, he had begun to turn the tide; the demon found himself having to block the human’s blows as he drove him back across the room."
                        an "ENOUGH!"
                        "Grabbing the hero’s sword with his claw, Andras struck him square in the chest with his other hand’s open palm, sending the hero sprawling backwards onto his behind."
                        an "Not bad human, perhaps my sister was right and you will make for a strong champion after all."
                        #gain Andras favour and 100 xp
                        $ add_exp(100)
                        $ change_favor('andras', 1)
                        #end scene
                        return
                "Let him go.":
                    $ released_fix_rollback()
                    "As he was leaving to no doubt massacre some poor, unsuspecting orcs, the demon turned back one last time to berate Rowan."
                    an "Just get your fucking work done then, I'll never hear the end of it from Jezera otherwise."
                    "Rowan felt like his heart would beat out of his chest, when Andras got like that he never knew what would happen."
                    #lose 5 orcs
                    $ castle.buildings['barracks'].troops -= 5
                    #end scene
                    return
        #if NTR = true
        else:
            ro "I can't help you with that right now. You and your sister are already only letting me work here one day a week, that's barely enough time as it is to take care of your finances and planning."
            ro "I'd never get anything done if I have to take care of you every time something stresses you out a little bit."
            "Andras breathed heavily for several seconds, continuing his furious stare. Rowan worried that maybe the demon would finally ignore the logic of his arguments and snap."
            "After what felt like an eternity, his master finally seemed to back off. Instead of forcing a cock down Rowan's throat, Andras turned around and headed back down towards the barracks."
            an "Fine, I'll just have to pay a visit to your lovely wife then. I’m sure she’s less busy than you, and will be a lot more accommodating."
            menu:
                "Try and stop him.":
                    $ released_fix_rollback()
                    "Rowan shuddered as he thought about what was going to happen next. With the quotas and the goals that the twins had placed on him, he needed every soldier he could get."
                    "If Andras were to go down to the barracks, he’d no doubt kill half a dozen orcs, and that was half a dozen orcs he could not afford to lose."
                    ro "I’m afraid I can let you do that."
                    "Rowan drew his sword as the demon turned back to face him, and was surprised to see not the flash of anger that he expected, but a grin."
                    an "It is about time you showed some backbone human. Looks like I’ll get to take my frustrations out on you after all."
                    #combat check DC30
                    if not check_combat(30)[0]:
                        #fail
                        "Without warning, the demon came at Rowan like a creature from the very depths of the hells."
                        "It was all he could do to bring his sword up just in time to stop the demon plunging one of his razor sharp claws into the hero’s chest."
                        "Time and again, Andras came at Rowan with lightning speed."
                        "He did his best to parry the blows, but after a few minutes, blood was leaking through from under the fabric of his tunic."
                        "Seeing the puddle of blood that had started to pool on the floor, the demon let out a chuckle."
                        an "I suppose I had better stop before I kill you. You were right though, this did help relieve me of some of my frustration."
                        an "Now go get yourself patched up before you bleed to death, I’d never hear the end of it from my sister otherwise."
                        #gain 10 xp and 2 wounds
                        $ add_exp(10)
                        $ take_damage(2)
                        #end scene
                        return
                    else:
                    #pass
                        "Without warning, the demon came at Rowan like a creature from the very depths of the hells."
                        "He was fast, inhumanly so, but a skilled warrior like Rowan had learned to anticipate his opponent’s attack, and was able to parry his razor sharp claws at every pass."
                        "After a few minutes, he had begun to turn the tide; the demon found himself having to block the human’s blows as he drove him back across the room."
                        an "ENOUGH!"
                        "Grabbing the hero’s sword with his claw, Andras struck him square in the chest with his other hand’s open palm, sending the hero sprawling backwards onto his behind."
                        an "Not bad human, perhaps my sister was right and you will make for a strong champion after all."
                        #gain Andras favour and 100 xp
                        $ add_exp(100)
                        $ change_favor('andras', 1)
                        #end scene
                        return
                "Let him go.":
                    $ released_fix_rollback()
                    "Rowan’s heart sank in his chest as he heard the demon’s threat, but there was nothing he could do to stop him."
                    "The pair of them were at the mercy of the twins, and they took every opportunity to remind them of that."
                    an "Just get your fucking work done then, I'll never hear the end of it from Jezera otherwise."
                    "Rowan felt powerless as his unwanted master left, and could only hope that his threat was an empty one, otherwise Alexia..."
                    #go to NTR events
                    # TODO: maybe turn call into running subevents
                    call ntr_event2 from _call_ntr_event2
                    return
    "Suck him off.":
        $ renpy.fix_rollback()
        $ rowanAndrasSex =+ 1
        $ rowanGaySex += 1
        "Rowan never knew what would happen when Andras got like this. As of yet the demon hadn't actually harmed him, but it always felt like he could snap at any time."
        "The hero feared not being able to complete his duties on time, but he also feared the wrath of not satisfying needs here and now. Hopefully he would not be detained by his master for long."
        #CG of clothed Rowan kneeling in front of Andras, the demon is flaccid
        scene cg215 with fade
        pause 3
        "Without saying anything more, Rowan obediently kneeled in front of Andras's groin and pulled the loincloth which hid the cock he was to suck."
        "He found that the member was flaccid, evidently the stress was such that he'd need to do some work before he could suck."
        scene cg216 with fade
        show rowan necklace neutral behind cg216
        show andras displeased behind cg216
        show skordred neutral behind cg216
        pause 3
        "Without wasting time thinking about how to get the demon's red cock hard, Rowan simply did whatever seemed natural. In this case, it was kissing the tip and then running his tongue up and down its length."
        "Andras continued to fume above him, seeming to ignore the efforts on his shaft for the time being. Worried that he wasn't going to be able to please his master, Rowan redoubled his efforts and tried taking the whole manhood into his mouth to swirl around."
        "Finally his master gave an approving grunt and the servant felt the cock in his mouth start to stiffen. He was quickly forced to let it slip out of his lips, unable to take the whole of its full size. Instead he returned to kissing and licking."
        "Struck by a sudden inspiration, Rowan tried sucking on the demon's balls while using a hand to keep up the stimulation on the shaft. This seemed to finally work some of the tension out and he felt Andras relaxing above him."
        "The sound of someone clearing their throat startled the steward for a moment and he tried to turn to see who it was. However, he was stopped by a hand from Andras which pushed him back to his work."
        "Even without looking, the sound of several voices whispering behind him told the hero that he now had a fairly sizable audience."
        scene cg123 with fade
        show rowan necklace neutral behind cg123
        show andras displeased behind cg123
        show skordred neutral behind cg123
        sk "Is now a bad time, master?"
        an "No, no, please give your report or whatever it is that you came to say. I've got plenty of time."
        "Rowan resumed kissing and licking, this time while also fondling the thick sack as well, while Skordred delivered his report about repairing damage to the castle. It was mostly about the things that Andras had caused, but the demon didn't seem to mind."
        "After a minute or two, the dark dwarf took his leave and the demon turned his attention to the man who was currently tonguing his cock."
        an "Stand and disrobe slut, that's enough foreplay."
        scene cg51 with fade
        show rowan necklace neutral behind cg51
        show andras smirk behind cg51
        pause 2
        "As Rowan's garments hit the floor, he was surprised when Andras pushed his massive red manhood against the human's much smaller dick. A tight fist wrapped around their mismatched members and the demon jerked his hips a few times to frott with his servant."
        an "How does it feel to have a real man show you just how inferior you are? Or maybe you just like having a real cock touch your tiny thing for just a few seconds?"
        "Laughter rang through the halls as the arrogant demon continued to taunt and buck. Rowan wasn't sure what to make of the sensation of rubbing against another man like this. However, he could not deny that it was very stimulating."
        show cg51 with sshake
        show cg51 with sshake
        show cg52 with flash
        show andras smirk behind cg52
        pause 2
        "So stimulating, that he started moving against his master.  Soon he felt himself hit his peak, and sprayed his load over their mixed shafts. Andras made no move to stop frotting, obviously intending to go until he finished. That didn't mean he wasn't going to taunt Rowan, however."

        #if Andras has had sex with Alexia
        if andras_alexia_sex:
            an "You and your wife are nothing but my playthings. This proves that."
        #else if Andras has had sex with Rowan, but not also Alexia
        elif andrasIntroSex:
            an "Hahaha! I see you really love my cock, no matter what part of your body it's on or in!"
        #else
        else:
            an "What a good slut you are, giving your master some lube to work with!"

        "Of course, having now cum the human found the pleasure of rubbing against his master start to give away to pain from the overstimulation. Thankfully, their session together ended soon afterwards when a second geyser of cum spewed forth."
        show cg52 with sshake
        show cg52 with sshake
        show cg53 with flash
        show andras smirk behind cg53
        pause 2
        "This one was of far greater quantity and went a greater distance, covering most of Rowan's belly instead of only the rubbing manhoods."
        "Now satisfied, Andras released his plaything and let out a big contented sigh."
        an "Very good, servant. You may now resume your other duties."
        show rowan necklace naked aroused behind cg53
        ro "Ha... right."
        #gain Andras favour
        $ change_favor('andras', 1)
        #end event
        return


##########################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label fire_in_the_stores:
# Fire in the Stores

# No requirements

# Rowan chambers night BG

show bg9 with fade

"The candles had all long since burned out in Rowan's bedchamber when he woke, groggily, for the first time. His usual, deep slumber had been interrupted by what seemed to him, in his semi-awake state, a buzzing or a murmur."
"A pseudo, almost haunting noise, somewhere on the periphery of his hearing."
"As his senses began to return, he could make out individual sounds within the cacophony; the shouting from somewhere down below, the clunking of armour, and more than one pair of iron boots clattering against stone."
"Rising from his bed, he threw on a pair of trousers and was in the process of pulling his shirt over his head when the heavy banging began on the room's wooden door."

play sound "music/SFX/door knock.ogg"
pause 1

show rowan intro necklace neutral at midleft with dissolve

ro "One minute, I'm coming."

"When he opened the door, he found two rather worried soldiers standing before him, both looking sheepish and neither quick to talk."

ro "Well, I assume there is a really good reason I've been woken up in the middle of the night?"

scene black with fade

#storehouse blaze cg

"When one of the soldiers finally blurted out the reason for their late night intrusion, Rowan discovered that a small disaster has struck; a fire had broken out in one of the stores, used to house grain and other supplies."
"He followed them down the stairs and to the courtyard, into the cold night air."
"As they approached the part of the castle where the storehouses are located, he could feel the waves of heat pulse against his skin; a welcome sensation from an unwanted situation."
"He sighed at the knowledge that it would probably be a long night before he found himself back in the warmth of his own bed."

"Arriving at the scene, Rowan found a small fire blazing away in the storehouse, just like the soldiers had told him. A number of people, his men, were stood around watching it burn and doing little to impede the spread of the fire."
"When he grabbed the nearest by his lapels and gave him a good shake, the answer that Rowan received was that there were two options on how to tackle the blaze."
"They had been waiting for him to arrive and instruct them on which of the two solutions they should enact."

"The first solution was to blockade the storehouse and allow the fire to burn itself out."
"While this would mean the loss of the supplies already in that building, there would be no chance of anyone getting hurt, or of the fire spreading to any of the nearby buildings."
"Alternatively, Rowan could order the men to attempt to put the fire out, which might save more, perhaps even all the supplies if they were lucky enough."
"It would, however, put lives at risk and increase the chances that the flames might spread."

"What should he order them to do?"

#choice
menu:
    "Isolate the fire and allow it to burn itself out":
        "Rowan watched as his men spent the next few hours gathering as much non-flammable material that they could in order to build a blockade."
        "Ultimately, their efforts were successful and the fire died out, but not before it has consumed everything that was being stored in the building."
        "A quick tally before he returned to his chambers confirmed that a quarter of the total supplies had been lost in the fire and would have to be replaced with funds from the treasury."
        "Not exactly ideal, but far from the worst that could have happened."
        # lose 30 gold
        $ castle.treasury -= 30
        #end event
        return
    "Order your men to attempt to put out the fire":
        # Roll d20 and add luck modifier
        $ temp_res = dice(20)
        $ temp_res2 = temp_res + avatar.stat_mod('luck')

        #If player rolls a natural 1
        if temp_res == 1:
            "The attempt to put out the fire was such a disaster that Rowan thought that the gods themselves must have sided against him. As he looked on, it seemed that everything that could go wrong was doing so in a spectacular fashion."
            "As the flames grew higher, spreading to the other outbuilding storing supplies, men banged into each other, or tripped, sending their pails full of water clattering against the courtyard stone."
            "Others ran around like headless chicken, despite Rowan barking orders in his best attempts to direct them."
            "By the time all was said and done, all the supplies had been lost to the fire; a costly enough outcome already, without the additional loss of a few lives."
            # lose 75 gold
            $ castle.treasury -= 75
            # lose 1d6 + 3 orcs
            $ castle.buildings['barracks'].troops -= min(castle.buildings['barracks'].troops, dice(6)+3)
            #small loss to morale
            $ castle.morale -= 5
            #end event
            return
        #If result = 2 – 6
        elif temp_res2 <= 6:
            "Rowan looked on as his men fought the fire as best they could, but despite his best efforts to coordinate them, their attempt was clumsy and inefficient."
            "They constantly got in one another's way, knocking each other over and spilling precious water."
            "When the fire spread to a small storeroom nearby, it seemed like they might be fighting a losing battle."
            "However, under Rowan's expert command, he was able to rally the troops, and after a few hours the blaze was once again under control."
            "By dawn the fire had been extinguished, but not without significant loss; a third of the castle's supplies."
            "The truth was though, as Rowan knew, if luck had gone in the other direction, it could have been much, much worse."
            #lose 50 gold
            $ castle.treasury -= 50
            #end event
            return
        #If result = 7 – 14
        elif temp_res2 <= 14:
            "After a few hours of fighting the fire, it was clear that Rowan's men were getting nowhere."
            "Their efforts had managed to contain that fire to the original building, but despite all attempts they were unable to put the flames out for good."
            "In the end, the entire affair turned out to be somewhat of a pyrrhic victory, as by time the fire has burned itself out in the morning, it had taken with it all the supplies that were in the storehouse."
            "With a quarter of the castle's supplies lost, Rowan could have saved both himself and his men a lot of time and effort had he just chosen to isolate the fire in the first place."
            #lose 30 gold
            $ castle.treasury -= 30
            #end event
            return
        #If result = 15 – 19
        elif temp_res2 <= 19:
            "Rowan stood in the courtyard, barking orders to the men around him."
            "First, he had them form a long chain from the castle's well to the scene of the fire, and before long the men were passing buckets of water down the line with speed and efficiency."
            "Thanks to his quick thinking, the flames were soon under control, and within a half an hour after the effort began, all that remained of the fire were a few smouldering embers, and coils of smoke rising into the night sky."
            "When a full inventory was taken the next morning, the findings were that the damage was so minimal that the loss to the castle's supplies is inconsequential."
            #end event
            return
        #If result = 20 or higher
        else:
            "Rowan stood in the courtyard, barking orders to the men around him."
            "First, he had them form a long chain from the castle's well to the scene of the fire, and before long the men were passing buckets of water down the line with speed and efficiency."
            "Thanks to his quick thinking, the flames were soon under control, and within a half an hour after the effort began, all that remained of the fire were a few smouldering embers, and coils of smoke rising into the night sky."
            "When a full inventory was taken the next morning, the findings were that the damage was so minimal that the loss to the castle's supplies is inconsequential."
            "In addition, stories of how well Rowan was able to handle the crisis under pressure had begun to spread throughout the castle, raising the spirits of those who hear them."
            #small increase to morale
            $ castle.morale += 5
            #end event
            return



##########################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label orc_platoon_returns:
# Orc Platoon Returns

# No requirements

show bg6 with fade
show rowan necklace neutral at midleft with dissolve

play sound "music/war-horn.ogg"
pause 1

#rowan confused

# if orc count is lower than 40
if castle.buildings['barracks'].troops < 40:
    "Suddenly a loud horn sounded, echoing through the mostly empty halls of castle Bloodmeen. It sounded like one of the warhorns used by Karnas's armies."
    "Rowan felt an instinctive sinking of dread in the pit of his stomach."
# if orc count is at least 40
else:
    "Suddenly a loud horn sounded, followed by several answering calls. A deep guttural cheer rose up around the Castle Bloodmeen, echoing around the halls and growing louder and louder."
    "Rowan felt unsettled. This was eerily similar to the frenzies that Karnas's armies would whip themselves into just before launching attacks."

ro "What's happening?"

show clamin happy at midright with moveinright

"The goblin merchant master came running into the throne room, waving her hands excitedly."

cla "Come on Rowan, you've got to come and see this!"

scene black with fade

"Cla-Min lead him out to the castle walls, from which he was able to watch in astonishment as a full platoon of orc soldiers carrying Karnas's colours marched through the gates."

# battlements bg
show rowan necklace neutral at midleft with dissolve
show clamin happy at midright with dissolve

ro "Where did these soldiers come from?"

cla "Dunno, they just showed up. Their gear looks like it's forded its fair set of rivers though."

"Rowan looked at her, then tore his eyes away from her bouncing up and down while trying to look over the battlements. She was right, their equipment was on its last legs."
"In fact, they looked like they'd been on their last legs for years."
"Only expert maintenance would have kept that armor in service as long as it seemed to have been. The soldiers to the back didn't have any metal left on them, only hides and bones."
"This precession had been designed to look good."

scene black with fade

"Realizing that he should meet the troop and find out what was going on, Rowan hurried back to the throne room."

show bg6 with fade
show rowan necklace neutral at midedgeleft with dissolve
show orc soldier neutral at midmidright with dissolve

os " We’s returned, where’s our lord?"

show andras displeased at orcright with moveinright

"Before Rowan could say anything, Andras entered and sat on the throne while shouting to the platoon of orc soldiers who'd just arrived."

an "I am one of the lords of this castle! You will submit to me and join my armies!"

os "You’s not master, too small."
os "Where is Karnas? We know war is not over, puny humans could never hurt big boss!"

show bg6 with sshake
show bg6 with flash

"In a flash, the red demon shot forward and jabbed his hand into the orc's chest. He pierced through the carefully maintained armor emblazoned with Karnas's symbol like it were butter."
"The leader of this band barely let out a grunt before falling to the ground."

show bg6 with redflash
play sound "music/SFX/BodyfallDirt.ogg"
hide orc soldier neutral with dissolve

"Andras raised his blooded hand above his head and turned to look at the rest of the assembled orcs."

show andras angry at orcright with dissolve

an "Karnas is dead, but there are now new lords of Bloodmeen. Under our banner, the six realms will kneel!"

"As he spoke, several of Andras's own orc soldiers entered into the throne room and took up positions next to him."

an "Serve and you will have a chance at a place in our world. Defiance will result in death."

"He turned around and returned to the throne. The new arrivals looked between one another in both confusion and anger."
"Rowan felt angry himself. By killing the platoon's leader, Andras had thrown away his best chance at securing the soldiers to his banner as well as eliminated the best of them."
"Already he could see that many of the orcs were preparing to desert the castle."
"The twin's champion stepped forward and offered to give a tour of the castle's facilities in an effort to calm the situation somewhat. Hopefully he'd be able to convince at least some of them to stay."

scene black with fade

"There were those that left almost immediately, a few stayed out of fear, the rest was up to Rowan's abilities and the state of the castle."

#There are 40 potential recruits.
#5 are guaranteed to stay.
$ temp_res = 5
#5 more will stay if the orc barracks has been upgraded to lv 2.
if castle.buildings['barracks'].lvl >= 2:
    $ temp_res += 5
#5 will stay if the arena has been built.
if castle.buildings['arena'].lvl >= 1:
    $ temp_res += 5
#5 will stay if the castle hall has been upgraded to lv 2.
if castle.buildings['hall'].lvl >= 2:
    $ temp_res += 5
#The remaining 20 will depend on Rowan's diplomacy skill roll.
$ temp_res += min(dice(20) + avatar.skill('diplomacy'), 20)
#After determining how many will stay, reduce that number down to how much capacity the orc barracks has left if greater.
$ castle.buildings['barracks'].troops += min(temp_res, castle.buildings['barracks'].capacity-castle.buildings['barracks'].troops)

"After Rowan had said his peace and done what he could, there were [temp_res] more orc soldiers in the barracks under Bloodmeen."
"Some of those that left were cut down not long after by the vengeful Andras, though he certainly didn't get all of them."

#end event
return

##########################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
