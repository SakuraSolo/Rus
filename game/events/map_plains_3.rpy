# random map events that happen on plains
init python:

    ##### Plains event: Lost Flock ####
    event('lost_flock', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #### Plains Event: The Hanged Man ####
    event('the_hanged_man', triggers='map_expl', conditions=('world.cur_tile_type == "plains"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label lost_flock:
##### Plains event: Lost Flock ####
$ released_block_rollback()
scene bg31 with fade
show rowan necklace neutral behind black

"Upon the grassy hillocks ahead Rowan saw dotted a large flock of sheep, unusual since there were no settlements close at hand. Lost, the possession of slain farmers, or the result of extravagant carelessness? Impossible to tell."

menu:
    "Round them up.":
        $ released_fix_rollback()
        ro "I've found something that may prove useful. Send me a few orcs."
        "A short time later, a small detachment of orcs arrived. They were disgusted at first with the task assigned to them, but once Rowan described what he had in mind, they set about it eagerly enough."
        "After an hour or so, most of the sheep were rounded up and funnelled back through the portal."
        "Back at Bloodmeen, the garrison licked their lips as they watched the witless, woolly train arrive and be shepherded towards the abattoir."
        cook "Tonight, you lucky scumbuckets, we feast!"
        orcs "OORAH!"
        "Rowan felt a pang of guilt about this literal act of sheep-rustling. But he knew an army marches on its belly, they would be able to sell some of the excess meat, and bandits would probably have helped themselves if he hadn't."
        #gain 5 xp
        #lose 1 move point, small guilt gain, small morale gain, small treasury gain
        $ add_exp(5)
        $ avatar.mp -= 1
        $ change_base_stat('g', 2)
        $ change_morale(3)
        $ change_treasury(15)
        return

    "Try to return them.":
        $ released_fix_rollback()
        "It took him a while, but eventually Rowan was able to find a tiny hamlet and ask about who the sheep might belong to. The inhabitants said they were likely the property of another village, destroyed by orcs."
        "Were they telling the truth? Either way, Rowan made the lives of these peasants immeasurably better by helping to herd the lost sheep to their own paddocks. He left with their praises and gratitude ringing in his ears."
        #lose 1 move point, small infany loss
        $ avatar.mp -= 1
        $ change_base_stat('f', -2)
        return

    "Ignore them":
        $ released_fix_rollback()
        "The sheep were somebody else's problem - or boon. Either way, Rowan did not trouble himself any further about the fate of these stupid creatures."
        #no effect
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_hanged_man:
#### Plains Event: The Hanged Man ####
scene bg31 with fade

"Rowan had been walking through the fields for the better part of the day when he spied a lonely tree in the distance, a solitary figure in green against the horizon."
"His heart sank a little as he grew closer; something large was hanging from one of the tree’s sturdier branches, flapping back and forth in the breeze."
"The hero could only hope that his assumptions about the shape were wrong."
"An hour later, his worst fear was confirmed. He could see the man hanging from the tree, the rope tied around a neck that had broken from the weight of the body, leaving a face transfixed with a perverse grin by rigour mortis to loll about at the wind’s fancy."
"How long the corpse had been up there, he could not tell, but it hadn’t entered the later stages of decay, so he could only assume it had not been too long. He was equally unsure about the events that had lead this man to this particularly cruel end. "
"While there was always the possibility that the man was a criminal, perhaps even an especially vile one, in dark times like these suspicious villagers were often just as likely to hang a stranger."
"The only question he could really answer at this moment was what he was going to do about the poor man’s body."

menu:
    "Plunder it.":
        $ released_fix_rollback()
        # gain guilt
        $ change_base_stat('g', 3)
        "During the war, Rowan had learned the importance of survival, and in his current predicament, that skill was more necessary than it had ever been. He felt bad about what he was doing, but whatever the man had now was of no use to him anyway."
        #climb check dc12
        if not check_skill(12, 'climb')[0]:
        #fail
            "Rowan spryly made his way up the trunk of the tree, and carefully edged his way along the relatively sturdy branch from which the body hung."
            "The extra weight made the branch unsteady, and as the hero edged along towards where the corpse hung, he slipped and fell."
            "A sharp stab of pain was accompanied by a sickening crunch as he landed left foot first on the ground, and he was sure his ankle had snapped."
            "There was no way of getting up the tree in his current state, and all he could do was limp off, leaving the tree and its strange fruit behind."
            #gain a wound and 5 xp
            $ avatar.take_damage(1)
            $ add_exp(5)
            return
        else:
        #pass
            "Rowan spryly made his way up the trunk of the tree, and carefully edged his way along the relatively sturdy branch from which the body hung."
            "The extra weight made the branch unsteady, and it threatened to break with each new step, but in the end it held long enough for the hero to make his way across."
            "Pulling his sword from its scabbard, he severed the rope, cutting the man free."

            #choose one of the following three outcomes at random
            $ temp = dice(3)
            #1
            if temp == 1:
                "Back on the ground, Rowan began the unsavoury task of searching the body. As he ran his hand along the lining of the man’s tunic, he discovered that whoever had done this before him had not done their job well enough."
                "Once again drawing his sword, he cut away at the shirt’s stitching to reveal a secret pocket, within which had been hidden a small coin purse."
                #gain 1d20 + 10 gold
                $ change_treasury(dice(2)+10)
                menu:
                    "Bury him.":
                        $ released_fix_rollback()
                        "Rowan began the task of preparing a grave for the man to lie in. Without a shovel, all he had to dig with was his hands, and it was a long and arduous task."
                        "Eventually though, Rowan had dug out a pit deep enough for the man, and he carefully placed the body in it. After saying a silent prayer to Solansia for the man’s soul, he began the task and refilling the hole."
                        "By the time he was done, night had fallen, but he felt a lot better for what he had done, despite the time lost. After all, we all need somebody else to do this for us."
                        #lose some guilt (less than gained for plundering) and 2 move points, gain 10 xp
                        $ change_base_stat('g', -2)
                        $ avatar.mp -= 2
                        $ add_exp(10)
                        return
                    "Leave the Corpse.":
                        $ released_fix_rollback()
                        "It was getting late, and Rowan decided that he didn’t have time to do anything more with the body. Nature, and the local wildlife, would have to take care of the rest."
                        #gain 10 xp
                        $ add_exp(10)
                        return
            #2
            elif temp == 2:
                "Back on the ground, Rowan began the unsavoury task of searching the body. However, what he had assumed to be the usual post-death bloat turned out to be something much worse - corpse worms!"
                "As he pressed against the dead man’s tunic, the body exploded, foul gas leaking from the new cavity in its chest. Rowan staggered back, bile rising in his throat, to avoid infection from the disgusting parasites."
                "When he felt he had reached a safe distance, he twisted his body to retch, being violently sick on the soft grass."
                "He had been very lucky to survive an encounter with corpse worms without becoming infected, but he was still going to feel quite ill for quite some time."
                #gain a wound and 10 xp
                $ avatar.take_damage(1)
                $ add_exp(10)
                return
            #3
            else:
                "Back on the ground, Rowan began the unsavoury task of searching the body. He carefully ran his hands over the body, seeking anything that may have been missed, but it was to no avail."
                "Whoever had hung him had already picked him clean of anything that might have been useful, if the man had had anything to begin with, that is."
                #gain additional guilt
                $ change_base_stat('g', 1)
                menu:
                    "Bury him.":
                        $ released_fix_rollback()
                        "Rowan began the task of preparing a grave for the man to lie in. Without a shovel, all he had to dig with was his hands, and it was a long and arduous task."
                        "Eventually though, Rowan had dug out a pit deep enough for the man, and he carefully placed the body in it. After saying a silent prayer to Solansia for the man’s soul, he began the task and refilling the hole."
                        "By the time he was done, night had fallen, but he felt a lot better for what he had done, despite the time lost. After all, we all need somebody else to do this for us."
                        #lose some guilt (less than gained for plundering) and 2 move points, gain 10 xp
                        $ change_base_stat('g', -2)
                        $ avatar.mp -= 2
                        $ add_exp(10)
                        return
                    "Leave the Corpse.":
                        $ released_fix_rollback()
                        "It was getting late, and Rowan decided that he didn’t have time to do anything more with the body. Nature, and the local wildlife, would have to take care of the rest."
                        #gain 10 xp
                        $ add_exp(10)
                        return
    "Bury it.":
        $ released_fix_rollback()
        "Rowan couldn’t just leave the man there, he deserved a proper burial like everyone else, regardless of the reasons that he may have been hanged. No one should be left to rot, and it wouldn’t be long before the body began to attract carrion."
        #climb check dc12
        if check_skill(12, 'climb')[0]:
        #pass
            "Rowan spryly made his way up the trunk of the tree, and carefully edged his way along the relatively sturdy branch from which the body hung."
            "The extra weight made the branch unsteady, and it threatened to break with each new step, but in the end it held long enough for the hero to make his way across."
            "Pulling his sword from its scabbard, he severed the rope, cutting the man free."
            "Back on the ground, Rowan began the task of preparing a grave for the man to lie in. Without a shovel, all he had to dig with was his hands, and it was a long and arduous task."
            "Eventually though, Rowan had dug out a pit deep enough for the man, and he carefully placed the body in it. After saying a silent prayer to Solansia for the man’s soul, he began the task and refilling the hole."
            "By the time he was done, night had fallen, but he felt a lot better for what he had done, despite the time lost. After all, we all need somebody else to do this for us."
            #lose guilt and 2 move points, and gain 10 xp
            $ change_base_stat('g', -3)
            $ avatar.mp -= 2
            $ add_exp(10)
            return
        else:
        #fail
            "Rowan spryly made his way up the trunk of the tree, and carefully edged his way along the relatively sturdy branch from which the body hung."
            "The extra weight made the branch unsteady, and as the hero edged along towards where the corpse hung, he slipped and fell."
            "A sharp stab of pain was accompanied by a sickening crunch as he landed left foot first on the ground, and he was sure his ankle had snapped."
            "There was no way of getting up the tree in his current state, and all he could do was limp off, leaving the tree and its strange fruit behind."
            #gain a wound and 5 xp
            $ avatar.take_damage(1)
            $ add_exp(5)
            return
    "Leave it.":
        $ released_fix_rollback()
        "Rowan felt bad, but after all he could not be sure what type of a man the person hanging from the tree had been. For all he knew, this punishment could have been well deserved."
        "With the twins being such harsh task masters, and the price of failure being so high for both Rowan and his wife, he decided to leave the body as press on."
        "Hopefully, someone else would come along and bury the poor fellow."
        #gain a small amount of guilt
        $ change_base_stat('g', 2)
        return
