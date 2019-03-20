# events for village interactions (occypy, destroy etc.)
init python:

    #Village Event: Swamp Coven
    #triggers on entry
    event('swamp_coven', triggers=('map_res_3', 'map_res_4', 'map_res_5',), run_count=1, group='village', priority=pr_map_res)


label swamp_coven:
#Village Event: Swamp Coven
#triggers on entry

scene black with fade
show rowan necklace neutral behind black

"From his vantage point on a nearby hill, Rowan looked down upon the village, nestled in a hummock of land near the grim, misty expanse of the swamps."
"It was a small huddle of turf-thatched dwellings, some on wooden stilts, a community of peat miners that was clearly a miserable and downtrodden place at the best of times (which these weren't)."
"Light flickering in the haze of the swamps nearby caught Rowan's eye - there seemed to be a congregation down there, gathered near a large fire. He slowly descended into the wet to take a closer look."
"Half a dozen women, middle-aged and dressed in ragged robes, stood in a circle on a small heath. The bonfire leapt into the sky from a hollow nearby. One, face obscured by hood and a horned animal skull, thrust her skinny arms at the sky."

cov "As the light of Solance fails, as the laws of men and elf fail, we turn back to the old ways for succour, those which lie like a bedrock beneath all else. As our folk did before us, in times of need. As their folk did before them."

"The rest of the congregation uttered some harsh, guttural response as one."

cov "They knew, as we know, that the wetlands are a gateway to the lands of black eternity. We mutilated and disparaged this place when the lights of other Gods shone... now we crawl to it and beg when those lights are all extinguished, and our children starve."
cov "The old ways are eternal. But they are also unforgiving."

"As Rowan watched, a young man stepped forward from beyond the bonfire. Dressed only in filthy trousers, his limbs trembled and his face was creased with fear... but he walked into the circle of women of his own accord."
"One of the women stepped to his side, stone knife in hand."

cov "How may we prove our need? Our will to renew our bonds with the Underneath, and have It forgive us our trespasses?"
cov "The price is eternal. The blood of innocence."

menu:
    "Stop this.":
        $ released_fix_rollback()
        ro "Stop!"
        "The interruption startled the coven into silence, and Rowan leaped out onto the heath and snatched the stone knife out of the would-be sacrificer's hand."
        ro "Barbaric rituals aren't going to save your village. And nobody has to starve! My army will march through here soon, and if you surrender, you shall come under my protection."
        cov "You? Who subvert the will of the very land you seek to tyrannise? We may as well submit to a rampaging boar! The Underneath has turned from us in disgust - you've ruined us all!"
        cov "Get thee from our sight, cursed one, and 'ware sending your soldiers against our homes. We shall drown them in the air!"
        "The young man scrambled to his feet and ran into the mists, flashing a fearful look behind him as he went - whether at his rescuer or the women, it was impossible to tell."
        "Rowan felt dire, crawling energy worming its way towards the raised hands of the skull-headed witch, and he hastily retreated back to his former vantage point."
        "Diplomacy was no longer an option - the only question was whether to capture this bleak village, or destroy it."
        #lose guilt, lose corruption

        menu:
            "Capture it.":
                $ released_fix_rollback()
                "If he couldn't take it peacefully, Rowan could at least free these people from their own evil superstitions. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them grim-faced, beginning to chant as the invaders closed the distance."
                "The leader gesticulated at the orc vanguard bearing down on them; the orcs yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                "Rowan inspected the village afterwards, noting the resentful but cowed expressions of the surviving crofters."
                "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much with the acquisition of this poor hamlet."
                "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make his army's own sacrifice worth it."
                #lose a few orcs
                #resolve as a normal conquered village
                $ castle.buildings['barracks'].troops -= 5
                $ castle.villages += 1
                $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                $ change_base_stat('f', 2)
                $ change_base_stat('g', 2)
                return

            "Destroy it.":
                $ released_fix_rollback()
                "Burn these pagans down, salt the earth, leave not a trace of their evil worship, that was Rowan's attitude. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them stony-faced, beginning to chant as they closed the distance."
                "The leader gesticulated at the orc vanguard bearing down on them, and they yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                "Quite a few of the common folk attempted to surrender then, but the orcs had their bloody orders, and were more than happy to comply with them."
                "After a few hours of brutal work, there was nothing left of the village but a pile of corpses and some ruined hovels. Even those would be swallowed by the marshes in the full course of time."
                "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much through the looting of this poor hamlet."
                "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make Rowan's army’s own sacrifice worth it."
                #lose a few orcs
                $ castle.buildings['barracks'].troops -= 5
                #resolve as a normal destroyed village
                $ change_prisoners(3)
                $ change_treasury(20*human_villages_defs[eventHex[6]][3])
                $ change_base_stat('c', 5)
                $ change_base_stat('i', 5)
                $ change_base_stat('g', 2)
                $ change_relation('andras', 2)
                $ change_relation('alexia', -2)
                return


    "Let it play out.":
        $ released_fix_rollback()
        "The flint knife flashed. A high, wheezing cry of agony was torn out of the young man."
        "The skull-headed witch raised his severed right hand up by the ring finger, allowing the blood to drop in a steady drizzle onto the loamy ground."
        cov "If the Underneath forgives us our transgressions, if It would give us aid in our time of need, It shall send us a sigul. If not... we shall offer, and offer again, until the scales are balanced."
        "Rowan felt unreal, as if the clammy fog that burdened the air here was the haze of a dream. Did he just allow that to happen? He shook his head and tried to concentrate."
        "Was there any way of turning this situation to his advantage? Did he intend to negotiate with these women for the village?"
        #gain guilt
        $ change_base_stat('g', 2)

        menu:
            "Negotiate with the coven.":
                $ released_fix_rollback()
                "Rowan gathered himself, and then clambered up onto the heath."
                ro "Greetings, Ladies of the - uh, this land. I felt drawn here, and wish to speak with you."
                "The seven grim-faced, ragged women - as well as the horribly injured young man - stared at him for a long moment."
                cov "Yes? And who might you be?"
                ro "I am Lord Rowan, commander of Castle Bloodmeen. My aim is to free this land of the tyranny of the Baron, he who has failed your people so badly. Submit to my rule, and you shall be protected, and will know prosperity again."
                cov "Substitute one set of man's laws for another, then? With no guarantee you will do as you say? What a tempting offer."
                "A bitter rattle of laughter ran around the circle of women."
                cov "...but the old magic works in mysterious ways. Perhaps you are the sigul we have been waiting for, aye, and perhaps anything is better than the misery our families know now."
                cov "Very well, Lord Rowan. We will make pax with you - on the condition that you allow the practice of the old ways to continue. With us at its head."

                menu:
                    "Agree.":
                        $ released_fix_rollback()
                        ro "Continue your rituals, then. Just so long as you obey my soldiers, all shall be well."
                        cov "Smart boy! Truly you are an emissary of the Underneath. We shall explain the new arrangement to the ordinary folk, and spill blood in your name... for as long as your words hold true. Go, with this blessing."
                        "She moved her long, thin fingers in the air, as if tracing a letter. A surge of energy entered Rowan, seething and hot. He staggered slightly, drawing a chuckle from the women."
                        "Heart hammering in his chest, Rowan watched the coven slowly head back to their village with their young charge, and after a while a large detachment of his soldiers pick their way down the hill towards it as well."
                        "He felt tainted by black magic, and impatient to get back onto the road in order to use up the restless energy that had been implanted into him. Perhaps if he did that, he wouldn't have to think too much about allowing the practice of witchcraft to flourish."
                        #gain corruption, gain guilt, lose 4 move points
                        $ change_base_stat('c', 2)
                        $ change_base_stat('g', 2)
                        $ change_mp(-4)
                        #resolve as a normal conquered village
                        $ castle.villages += 1
                        $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                        $ change_base_stat('f', 2)
                        $ change_base_stat('g', 2)
                        return


                    "Try and persuade them to abandon black magic":
                        $ released_fix_rollback()
                        ro "These pagan rituals of yours lead to pain and disappointment at best, horror and death at worst. Trust someone who's seen real black magic - you must abandon it, for your own sake. Trust in the protection and trade my forces will offer you."
                        if check_skill(21, 'diplomacy')[0]:
                            cov "It is true our folk used to tell us to only turn to the old ways when all else has failed... Very well - no more rituals. If your words turn out to be true."
                            "She took off the animal skull cloaking her face, and was suddenly a simple old peasant woman, like all the rest. Rowan breathed an inward sigh of relief."
                            ro "Thank you. Your trust is not misplaced. My soldiers will present themselves to you shortly. Do as they say, and all shall be well."
                            "Rowan watched the coven slowly head back to their village with their young charge, and after a while a large detachment of his soldiers pick their way down the hill towards it as well."
                            "He felt gladdened that he had taken the hamlet, and dismantled its practice of witchcraft, without a single life being lost."
                            $ add_exp(25)
                            #lose corruption, lose guilt
                            $ change_base_stat('c', -2)
                            $ change_base_stat('g', -2)
                            #resolve as a normal conquered village
                            $ castle.villages += 1
                            $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                            $ change_base_stat('f', 2)
                            $ change_base_stat('g', 2)
                            return
                        else:
                            cov "You claim our magic drew you here, then scorn it? Fah! We shall continue to follow the old ways, fool, whether you choose to march your army through here or not. Agree to our terms, or remove yourself at once."
                            menu:
                                "Agree.":
                                    $ released_fix_rollback()
                                    ro "Continue your rituals, then. Just so long as you obey my soldiers, all shall be well."
                                    cov "Smart boy! Truly you are an emissary of the Underneath. We shall explain the new arrangement to the ordinary folk, and spill blood in your name... for as long as your words hold true. Go, with this blessing."
                                    "She moved her long, thin fingers in the air, as if tracing a letter. A surge of energy entered Rowan, seething and hot. He staggered slightly, drawing a chuckle from the women."
                                    "Heart hammering in his chest, Rowan watched the coven slowly head back to their village with their young charge, and after a while a large detachment of his soldiers pick their way down the hill towards it as well."
                                    "He felt tainted by black magic, and impatient to get back onto the road in order to use up the restless energy that had been implanted into him. Perhaps if he did that, he wouldn't have to think too much about allowing the practice of witchcraft to flourish."
                                    #gain corruption, gain guilt, lose 4 move points
                                    $ change_base_stat('c', 2)
                                    $ change_base_stat('g', 2)
                                    $ change_mp(-4)
                                    #resolve as a normal conquered village
                                    $ castle.villages += 1
                                    $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                                    $ change_base_stat('f', 2)
                                    $ change_base_stat('g', 2)
                                    return
                                "Refuse.":
                                    $ released_fix_rollback()
                                    ro "No. I will not countenance black magic of this kind amongst common folk under my rule."
                                    cov "Then there is nothing left to say. Withdraw, or know our wrath."
                                    "Rowan felt dire, crawling energy worming its way towards the raised hands of the skull-headed witch, and he hastily retreated back to his former vantage point."
                                    "Diplomacy was no longer an option - the only question was whether to take this bleak village, or destroy it."

                                    menu:
                                        "Capture it.":
                                            $ released_fix_rollback()
                                            "If he couldn't take it peacefully, Rowan could at least free these people from their own evil superstitions. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                                            "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them grim-faced, beginning to chant as the invaders closed the distance."
                                            "The leader gesticulated at the orc vanguard bearing down on them; the orcs yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                                            "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                                            "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                                            "Rowan inspected the village afterwards, noting the resentful but cowed expressions of the surviving crofters."
                                            "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much with the acquisition of this poor hamlet."
                                            "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make his army's own sacrifice worth it."
                                            #lose a few orcs
                                            #resolve as a normal conquered village
                                            $ castle.buildings['barracks'].troops -= 5
                                            $ castle.villages += 1
                                            $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                                            $ change_base_stat('f', 2)
                                            $ change_base_stat('g', 2)
                                            return

                                        "Destroy it.":
                                            $ released_fix_rollback()
                                            "Burn these pagans down, salt the earth, leave not a trace of their evil worship, that was Rowan's attitude. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                                            "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them stony-faced, beginning to chant as they closed the distance."
                                            "The leader gesticulated at the orc vanguard bearing down on them, and they yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                                            "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                                            "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                                            "Quite a few of the common folk attempted to surrender then, but the orcs had their bloody orders, and were more than happy to comply with them."
                                            "After a few hours of brutal work, there was nothing left of the village but a pile of corpses and some ruined hovels. Even those would be swallowed by the marshes in the full course of time."
                                            "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much through the looting of this poor hamlet."
                                            "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make Rowan's army’s own sacrifice worth it."
                                            #lose a few orcs
                                            $ castle.buildings['barracks'].troops -= 5
                                            #resolve as a normal destroyed village
                                            $ change_prisoners(3)
                                            $ change_treasury(20*human_villages_defs[eventHex[6]][3])
                                            $ change_base_stat('c', 5)
                                            $ change_base_stat('i', 5)
                                            $ change_base_stat('g', 2)
                                            $ change_relation('andras', 2)
                                            $ change_relation('alexia', -2)
                                            return


                    "Refuse.":
                        $ released_fix_rollback()
                        ro "No. I will not countenance black magic of this kind amongst common folk under my rule."
                        cov "Then there is nothing left to say. Withdraw, or know our wrath."
                        "Rowan felt dire, crawling energy worming its way towards the raised hands of the skull-headed witch, and he hastily retreated back to his former vantage point."
                        "Diplomacy was no longer an option - the only question was whether to take this bleak village, or destroy it."

                        menu:
                            "Capture it.":
                                $ released_fix_rollback()
                                "If he couldn't take it peacefully, Rowan could at least free these people from their own evil superstitions. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                                "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them grim-faced, beginning to chant as the invaders closed the distance."
                                "The leader gesticulated at the orc vanguard bearing down on them; the orcs yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                                "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                                "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                                "Rowan inspected the village afterwards, noting the resentful but cowed expressions of the surviving crofters."
                                "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much with the acquisition of this poor hamlet."
                                "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make his army's own sacrifice worth it."
                                #lose a few orcs
                                #resolve as a normal conquered village
                                $ castle.buildings['barracks'].troops -= 5
                                $ castle.villages += 1
                                $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                                $ change_base_stat('f', 2)
                                $ change_base_stat('g', 2)
                                return

                            "Destroy it.":
                                $ released_fix_rollback()
                                "Burn these pagans down, salt the earth, leave not a trace of their evil worship, that was Rowan's attitude. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                                "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them stony-faced, beginning to chant as they closed the distance."
                                "The leader gesticulated at the orc vanguard bearing down on them, and they yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                                "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                                "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                                "Quite a few of the common folk attempted to surrender then, but the orcs had their bloody orders, and were more than happy to comply with them."
                                "After a few hours of brutal work, there was nothing left of the village but a pile of corpses and some ruined hovels. Even those would be swallowed by the marshes in the full course of time."
                                "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much through the looting of this poor hamlet."
                                "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make Rowan's army’s own sacrifice worth it."
                                #lose a few orcs
                                $ castle.buildings['barracks'].troops -= 5
                                #resolve as a normal destroyed village
                                $ change_prisoners(3)
                                $ change_treasury(20*human_villages_defs[eventHex[6]][3])
                                $ change_base_stat('c', 5)
                                $ change_base_stat('i', 5)
                                $ change_base_stat('g', 2)
                                $ change_relation('andras', 2)
                                $ change_relation('alexia', -2)
                                return

            #if the player has favour with Jezera
            "Have Jezera appear as if summoned by the ritual." if all_actors['jezera'].favors > 0:
                $ released_fix_rollback()
                "It was a brazen tactic, but Rowan had made his name by not doing the obvious. He fell back into the mists, and touched his communication crystal."
                ro "Jezera. I need your help with something."
                "He explained the situation, and what he wanted the female demon to do."
                show jezera happy behind black
                je " Ooh, how delightfully deceitful! See, this is exactly the sort of thing I wanted from you. That innate guile of yours, being let loose and channelled towards a greater purpose. I'll enact this plan of yours with great pleasure!"
                "Rowan crept back to the heath and watched. The circle of witches started, then froze in shock as purple smoke began to fume from their bonfire."
                "The thick, acrid blossoms took sultry shape, and then Jezera stepped out from the blaze, clothes flapping around her, eyes flashing."
                je "I heard the call, and the blood bonds have been woven. What is thy bidding, miserable mortals? I may grant it, if I find it sufficiently amusing."
                cov " I... we were never told that - w-we wish for aid, o emissary of the Underneath. Our village starves - the men of our land tax us and send us nothing in return. Bandits take what little we have left. We will die without your help."
                je "Hmm. And what shall I get in return? Paltry peasant body parts? Pah, no matter. In a day a black army will be at your doorstep. Submit to them, do as they say, and you shall be protected and fed. Suffer not my wrath by attempting anything different."
                cov "To... to hear is to obey, emissary."
                "Jezera smirked, and disappeared in another flume of purple smoke. She reappeared next to Rowan."
                je "That was fun! You should call on me more often, you know. Humans are so easy to mislead."
                ro "I doubt that will work on anyone that hasn't been trying to summon evil forces."
                je "Well, whatever. Thanks to me, that village is ours - and not a soldier wasted. Keep playing smart, commander of mine!"
                "She sent herself back to the Castle. Rowan watched the coven slowly head back to their village, and after a while a large detachment of his soldiers pick their way down the hill towards it as well."
                "He felt queasy about falsely promoting black magic in the way that he had - on the other hand, it was hard to argue with a free, peaceful victory."
                #gain corruption
                $ change_base_stat('c', 2)
                #resolve as a normal conquered village
                $ castle.villages += 1
                $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                $ change_base_stat('f', 2)
                $ change_base_stat('g', 2)
                return

            "Capture it.":
                $ released_fix_rollback()
                "If he couldn't take it peacefully, Rowan could at least free these people from their own evil superstitions. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them grim-faced, beginning to chant as the invaders closed the distance."
                "The leader gesticulated at the orc vanguard bearing down on them; the orcs yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                "Rowan inspected the village afterwards, noting the resentful but cowed expressions of the surviving crofters."
                "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much with the acquisition of this poor hamlet."
                "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make his army's own sacrifice worth it."
                #lose a few orcs
                #resolve as a normal conquered village
                $ castle.buildings['barracks'].troops -= 5
                $ castle.villages += 1
                $ castle.villages_income += human_villages_defs[world.cur_hex[6]][3]
                $ change_base_stat('f', 2)
                $ change_base_stat('g', 2)
                return

            "Destroy it.":
                $ released_fix_rollback()
                "Burn these pagans down, salt the earth, leave not a trace of their evil worship, that was Rowan's attitude. He summoned his army, and instructed them to overrun the village from the higher, less swampy ground."
                "Screened by a paltry line of armed peasants, the coven of seven witches watched Rowan's army descend upon them stony-faced, beginning to chant as they closed the distance."
                "The leader gesticulated at the orc vanguard bearing down on them, and they yelled, then screamed in fear as the air around them twisted and pulsed with awful, dank light."
                "From where Rowan was stood, the colors of their flesh and armor seemed to run together with the land like a ruined painting."
                "The skull-headed witch howled in triumph - and then was flung to the ground as an arrow punched into her midriff. Rowan's soldiers easily broke through the peasant line and slaughtered the rest of the coven in a fearful fury."
                "Quite a few of the common folk attempted to surrender then, but the orcs had their bloody orders, and were more than happy to comply with them."
                "After a few hours of brutal work, there was nothing left of the village but a pile of corpses and some ruined hovels. Even those would be swallowed by the marshes in the full course of time."
                "The soldiers hit by the coven's hex had died horribly, soldered together into a poisonous mess, and they'd hardly gained much through the looting of this poor hamlet."
                "Still, the destruction of those pagan crones was worth celebrating, and perhaps in time the deadly arithmetic of war would make Rowan's army’s own sacrifice worth it."
                #lose a few orcs
                $ castle.buildings['barracks'].troops -= 5
                #resolve as a normal destroyed village
                $ change_prisoners(3)
                $ change_treasury(20*human_villages_defs[eventHex[6]][3])
                $ change_base_stat('c', 5)
                $ change_base_stat('i', 5)
                $ change_base_stat('g', 2)
                $ change_relation('andras', 2)
                $ change_relation('alexia', -2)
                return
