# codex entries for a journal
init python:
    # codex consists of categories (like 'Characters') that divided into topics (like 'Rowan Blackwell'); topics consist of list of entries, that are shown as single composed text in codex screen
    codex_entries = {
        'rowan_starting': ('Characters', 'Rowan Blackwell',
"""Rowan Blackwell was the only son of a hunter couple who lived in the Western Forest, nearby Arthdale in Rosaria.  When he was nine, his parents were killed by the monsters in the forest and the village elder of Arthdale took him in.  There he met Alexia and the two became sweethearts.

When the chaos war broke out in 868 A.F., Rowan was levied into the Rosarian army at the age of seventeen.  Shortly afterwards he was sent to join the garrison at the Northern Rosarian keep of Karst.  When the keep feel under attack and the commander (duke Werden) was killed, Rowan took command after the rest of the nobility fled and held out for four months before reinforcements arrived, earning him the moniker, "The hero of Karst".

He would later be recruited by Deanara into her party of heroes from the Six Realms.  Together they would lead the war and undermine Karnas's efforts.  Eventually they confronted him in Bloodmeen and ended his life.

After the war ended, Rowan returned to Arthdale and married his childhood sweetheart, Alexia.  Since then, they have lived in peace together.  He is sometimes called to events or ceremonies hosted by the nobility due to his status as a hero, but both prefer to leave each other be when possible.
"""),
        'alexia_starting': ('Characters', 'Alexia Blackwell',
"""Alexia was born to a family of bakers, in the town of Arthdale in the realm of Rosaria.  Her upbringing was typical for a Rosarian peasant women.  She formed a close relationship with a boy named Rowan who'd been taken in by the village elder, who lived in the general store next door.

After Rowan was called away by the war, she remained behind in Arthdale.  During this time she continued to train her skills as a housewife, hoping that her darling would return to her when the war ended.  As tales of his heroics trickled back to the village, she found herself filled with hope, trepidation, and fear.  A hero might die at any time, and there'd be countless women fawning over him while he was away.

She was overjoyed when her beloved returned to her after the war ended.  She could hardly believe that such a great hero had done so, but thanked Solensia every day for being so blessed.

Many who meet Alexia are surprised that the wife of a hero is in almost all respects an ordinary, though beautiful, woman.  She has little to no ambition beyond marrying Rowan and raising a family with him.  Oftentimes she ends up being ignored by nobility and other upper members of society, usually not being invited to official events when her husband is.
"""),
        'village_elder_starting': ('Characters', 'Village Elder',
"""The village elder of Arthdale is a very respected member of the community who previously ran the general store next to the bakery with his wife Meris.  The two were married for fifty years before Meris's death, but never had any children of their own.  After Rowan's parents died, he took the boy in and raised him as his own until the war of chaos broke out.

After the war ended he finally retired from his work at the store in his seventies, spending the rest of his time relaxing and offering advice to those he met on his regular walks around the village.  Rowan still sees him as a father figure and close friend.

The elder's actual name is Travis Potts, but no one can ever remember what it is and he prefers if they just call him "friend" instead.
"""),
        'village_elder_killed_by_rowan': ('Characters', 'Village Elder',
"""After the twin's attack on Arthdale, he fled to Rastedel with the rest of the villagers but soon traveled to Arthdale's Southern neighbor, the village of Briarbridge, to wait for Rowan's return.  Rowan was forced by Andras to kill him when the twins occupied Briarbridge.
"""),
        'village_elder_killed_by_andras': ('Characters', 'Village Elder',
"""After the twin's attack on Arthdale, he fled to Rastedel with the rest of the villagers but soon traveled to Arthdale's Southern neighbor, the village of Briarbridge, to wait for Rowan's return.  Andras killed him when the twins occupied Briarbridge.
"""),
        'karnas_starting': ('Characters', 'Karnas',
"""The most recent demon lord who attempted to take control of the Six Realms in Kharos's name during the last war.  His forces first started spreading from Bloodmeen twelve years before the events of this story begins.  He was killed by the six heroes, one of whom was Rowan, at the conclusion of the war, five years after it had started.
"""),
        'deanara_starting': ('Characters', 'Deanara',
"""A living saint of Solansia, said to be the direct descendant of the humans chosen by Solansia to lead all the races of the world around nine hundred years ago.  As a direct conduit to the goddess, she is the most magically powerful living human.  By command of her patron she assembled the party of heroes that defended the Six Realms and ultimately defeated the demon lord Karnas.  Deanara personally struck down Kharos's son with her companions at her side.
"""),
        'jezera_starting': ('Characters', 'Jezera',
"""Jezera is a half demon, sibling to Andras and one of the many bastards Karnas left in his wake.  She was raised by her mother in the town of Qerazel, located in the Empire of Sand.  Her innate demonic powers fostered a strong sense of entitlement and ambition as she grew up, eventually leading her to attempt her own bid for power while working in partnership with her twin brother.

Jezera has a natural affinity for manipulation and intrigue.  Whenever possible, she prefers to use subtler means to achieve her goals and is in the habit of maintaining a large number of schemes and plots all over the Six Realms.  This is facilitated by a large network of portals that she has built up and maintained since taking over Castle Bloodmeen's surface operations.
"""),
        'andras_starting': ('Characters', 'Andras',
"""Andras is a half demon, sibling to Jezera and one of the many bastards Karnas left in his wake.  He was raised by his mother in the town of Qerazel, located in the Empire of Sand.  Andras was a wild boy who spent most of his time in the desert outside his home, where he would hunt, kill, and even torture the animals he found with his innate demonic powers.

As he grew older, he'd start to pick up hangers on or even force people to follow his orders with threats and his growing reputation.  When his sister suggested that they work together to grab even more power for themselves, he was eager to join her.  Although he appears brutish and impulsive, there is a powerful intellect behind his eyes that now leads the Bloodmeen underground.
"""),
        'cla_min_starting': ('Characters', 'Cla-Min',
# (Unlocked after second mission briefing finishes)
"""The head of a goblin caravan clan, the Cla clan.  Cla-Min and her caravan have agreed to serve the role of acquiring and transporting any equipment or resources that are needed for the restoration of Castle Bloodmeen in exchange for exclusive rights to trade using Jezera's portal network.

She and her family have a great respect for Rowan and his underhanded heroics.
"""),
        'skordred_starting': ('Characters', 'Skordred',
# (Unlocked after second mission briefing finishes)
"""A dark dwarf master builder and the head of the team that lead the construction of the most recent Castle Bloodmeen in preparation for Karnas's arrival.  He survived the war and became a hermit living nearby the castle after it was mostly destroyed.  Andras and Jezera found him when they came to take the castle for themselves and convinced him to resume his previous position.

He harbors a grudge with Rowan for having been one of the heroes who killed Karnas.
"""),
        'cliohna_starting': ('Characters', 'Cliohna',
# (Unlocked after second mission briefing finishes)
"""A mysterious and ancient sorceress who appears much younger than she actually is.  She arrived at Castle Bloodmeen one day asking for access to the library there.  The twins agreed to let her in, in exchange for doing research for them.  No one really knows who she is or where she came from and she isn't telling any stories about her past.
"""),
        'greyhide_starting': ('Characters', 'Greyhide',
# (Unlocked after Forge is built event finishes)
"""An elderly minotaur who has become disillusioned with the brutal life he use to lead among his fellows.  He has taken up the position of forgemaster at the behest of Andras, having been promised that he would not have to fight anyone ever again.

Rowan and he feel a kinship with one another, both being veterans of many battles who've tired of blood.
"""),
        'xzarartl_starting': ('Characters', "X’zaratl",
# (Unlocked after Dark Sanctum event finishes)
"""A magically inclined succubus that Jezera found to manage the cubi sorcerer team in Castle Bloodmeen.  She possesses both male and female genitals and has shown an interest in putting them to use on both Rowan and Alexia.  She has a thing for joining married couples under the sheets and corrupting them.
"""),
        'indarah_starting': ('Characters', 'Indarah',
# (Unlocked after Tavern event finishes)
"""Hailing from the Dragon's Tail, Indarah is a barmaid who's spent most of her life dealing with poorly behaved patrons and knows how to brawl.  By chance, she met Jezera while the demoness was scheming in the area.  Instantly she took a shining to the barmaid and offered to let her take over the Tavern in the Rakshan Wastes they were in the process of restoring.

Indarah has a strong dislike of hereditary authority figures, resenting the fact that her low birth would normally prevent her from amounting to much of anything.
"""),
        'draith_starting': ('Characters', 'Draith',
# (Unlocked after Breeding Pits event finishes)
"""Draith is an escaped dark elf male who fled his home after his mistress's monster menagerie was slaughtered by a rival and feared for his life.  By chance, he was found by Andras, who happened to be in the area searching for rare monsters, and ended being swept up by the powerful man to be the master breeder for Bloodmeen castle.

Draith dislikes women, thanks to his hard life in dark elf society.  He prefers the company of men and monsters.
"""),
        'shaya_starting': ('Characters', 'Shaya',
# (Unlocked after Brothel event finishes)
"""A childhood friend of Jezera from Qerazel who has found herself swept up in the twin's bid for power.  While Shaya previously served as an informant and agent in her hometown, Jezera has brought her to Bloodmeen to assist in the management of her new cadre of incubus and succubus spies.
"""),
        'helayna_starting': ('Characters', 'Helayna Raeve',
# (Paragraph one [character information] should appear after meeting Helayna, and a second paragraph detailing what happened to her should appear after Raeve Keep is captured)
"""Helayna Raeve is Duke Raeve's niece and captain of his knight garrison.  She was too young to participate in the last demon war and now mostly serves in a ceremonial role due to it being a time of relative peace.  Unlike most nobles, she dislikes the strict hereditary hierarchy enforced by Solansia's will.
"""),
        'helayna_rowan_teacher': ('Characters', 'Helayna Raeve',
# (If helaynaRelationship is 0 - teacher)
"""During her knight training, she sought out Rowan to be her teacher against the wishes of her uncle.  The hero agreed to train her in the art of sword and command for several months before she returned to the keep to learn horseback riding and how to fight in heavy armor.  Occasionally she will seek out her old teacher for advice.
"""),
        'helayna_rowan_friend': ('Characters', 'Helayna Raeve',
# (If helaynaRelationship is 1 - friend)
"""After the war ended, Helayna had made it her personal mission to see Rowan raised up to the rank of noble, much to the anger of her uncle.  That endeavor only ended when the hero himself had dissuaded her from it, but the two had become good friends with one another afterwards.
"""),
# (If helaynaRelationship is 2 - acquaintance) - no additional information
        'helayna_keep_taken_by_force': ('Characters', 'Helayna Raeve',
# (After Raeve keep has been taken by force)
"""After being defeated in the defense of Raeve Keep, Jezera placed an obsidian band on her finger that drove her into a mindless lust.
"""),
# (If Rowan fucked her)
        'helayna_keep_taken_by_force_fucked_by_rowan': ('Characters', 'Helayna Raeve',
"""She called out to Rowan and Jezera goaded him into taking her there.
"""),
        'helayna_keep_taken_by_force_claimed': ('Characters', 'Helayna Raeve',
# (If Rowan claimed her)
"""In order to pretect her from being gangraped by orcs, Rowan claimed Helayna as a personal prize for his part in taking the castle.  She now lives with him in Bloodmeen.
"""),
        'helayna_keep_taken_by_force_gangrape': ('Characters', 'Helayna Raeve',
# (else)
"""An orc gangrape followed that lasted at least most of the day.  The girl was released in exchange for donning the ring, but Rowan didn't know what happened to her after that.
"""),
        'helayna_keep_taken_by_spies': ('Characters', 'Helayna Raeve',
# (After Raeve keep has been taken by spies)
"""After being defeated by her own men at Raeve Keep, Jezera placed an obsidian band on her finger that drove her into a mindless lust.
"""),
        'helayna_keep_taken_by_spies_fucked_by_rowan': ('Characters', 'Helayna Raeve',
# (If Rowan fucked her)
"""She called out to Rowan and Jezera goaded him into taking her there.
"""),
        'helayna_keep_taken_by_spies_claimed': ('Characters', 'Helayna Raeve',
# (If Rowan claimed her)
"""In order to pretect her from being gangraped by her former underlings, Rowan claimed Helayna as a personal prize for his part in taking the castle.  She now lives with him in Bloodmeen.
"""),
        'helayna_keep_taken_by_spies_gangrape': ('Characters', 'Helayna Raeve',
# (else)
"""She was gangraped by her former underlings and several orcs afterwards that lasted most of the day.  The girl was released in exchange for donning the ring, but Rowan didn't know what happened to her after that.
"""),
        'doran_starting': ('Characters', 'Doran Raeve',
# (Paragraph one [character information] should appear after meeting Doran, and a second paragraph detailing what happened to him should appear after Raeve Keep is captured)
"""Duke Doran Raeve is a high ranking noble in the realm of Rosaria and the head of the Raeve dynasty.  His duchy is Yael Fork, the region that Rowan's home village of Arthdale is located.  While he had a reputation as an ambitious man in his youth, he seems to have become cowed by the baron and tends to be a bit of a yes man to his betters.  Those below him are not worthy of his respect.

While Raeve had been fairly cordial towards Rowan after the war was finished and occasionally invited him to events, he has become much more bitter towards the hero since Arthdale was burned to the ground.  Rowan is unsure why.
"""),
        'doran_keep_taken': ('Characters', 'Doran Raeve',
# (After Raeve Keep is taken)
"""Upon his keep being taken over by the twins, Doran Raeve has been reduced to a nearly mindless sex slave by Jezera.  She keeps him as a trophy of their conquest and occasionally has him service her guests.
"""),
################################################################################
        'arthdale_starting': ('Places', 'Arthdale',
"""Arthdale is a small Rosarian village in the duchy of Yael's fork, nestled between the Western Forest and the river Yael's Southern tributary.  It is famous for being the home village of the hero Rowan, but not much else.  Rowan and Alexia have made their home here after the demon war ended, closeby where they grew up together.

The village was burned down by the demon twins when they sought out Rowan.  None of the villagers died during the attack, fleeing to Rastedel as refugees at the same time as the hero set off to Castle Bloodmeen.
"""),
        'arthdale_after_visit': ('Places', 'Arthdale',
#(after visiting Arthdale)
"""No effort has been made towards reconstructing the village after Rowan's departure, it is still a sad set of burned out buildings.  The only people still living in the area are those whose homes were outside the village proper.
"""),
        'bloodmeen_starting': ('Places', 'Castle Bloodmeen',
"""Castle Bloodmeen is the seat of the demon lord in the Six Realms, the champion of Kharos.  Much of the interior was destroyed after Karnas's defeat, including the extensive underground tunnel network, then abandoned.  However, the main structure remained intact and the demon twins have turned it into their base of operations after restoring many parts of it.

The Castle is located at the Northwestern edge of the Rakshan Wastes and unofficially rules over them.
"""),
        'raeve_keep_starting': ('Places', 'Raeve Keep',
# (Unlocked appear after visiting the keep)
"""This keep is the seat of the noble Reave dynasty, who currently holds the title of Duke of Yael's Fork.  It is one of the smaller castles in Rosaria, but is built nearby the main bridge crossing the Yael's Southern tributary so it is a place of both strategic and economic importance.
"""),
        'raeve_keep_is_taken': ('Places', 'Raeve Keep',
# (after Raeve Keep is taken)
"""The keep was captured by the twins early on in their conquest.  Rowan's efforts were instrumental in its taking
"""),
################################################################################
        "dancer_s_whips": ('Magic', "Dancer's whips",
# (Unlocked after Raeve keep is taken or Jezera kills the dark elf queen)
"""This spell creates a number of ribbons of magical energy that move at the caster's command.  They can be used to grasp things, push things, or even lift the caster off the ground.  It takes practise to control these whips and most magic-users start out with only two at a time.  Very skilled or talented ones may maintain upwards of eight.  Four is usually enough to completely immobilize a humanoid.

The half-demon twin Jezera uses this as her signature spell.
"""),
        "punishment": ('Magic', "Punishment",
"""A circle of magic forms over the target of the spell to bind them in place, afterwhich they start to feel incredible pain until the caster releases the spell.  Punishment is generally used by greater demons as a means to keep their minions in line.  Most mortals will lose consciousness from the intensity of the pain if the spell is maintained on them for more than a few seconds, it takes someone of especially great fortitude and will to stay awake.  Even for those, they will likely find themselves unable to even try and free themselves.

The half-demon twin Andras uses this as his signature spell.
"""),
################################################################################
        'solansia_starting': ('Greater Deities', 'Solansia',
"""The greater deity of order who created the world and whose worship forms the basis of religion in the Six Realms.  Her focus of power in the world is in the holy city of Prothea, where the upper echelons of her priests reside as well as the family of saints from which the living saints, such as Deanara, emerge whenever a new demon lord appears.
"""),
        'kharos_starting': ('Greater Deities', 'Kharos',
"""Kharos, also known as the God of Many Faces, is the greater deity of chaos.  Since the tragedy that became known as Neryon’s Folly allowed a fragment of himself to enter Solance, he has sought to corrupt and conquer the world.  His initial entrance into the world twisted many races and created others, giving rise to the chaos races.

Since then, he has concentrated his efforts into building up a significant amount of power in order to create a pathway for one of his children to enter the world and conquer it on his behalf: the demon lords.
"""),
################################################################################
        'solance_starting': ('World terms', 'Solance',
"""The world this story takes place in.
"""),
        'six_realms_starting': ('World terms', 'Six Realms',
"""The Six Realms can refer to the Westernmost continent in the world of Solance or to the collection of six nations on it: Prothea, Rosaria, the Frozen Wastes, Ealoean, the Empire of Sand, and the Dragon's Tail.
"""),
        'dirt_general_starting': ('World terms', 'Dirt General',
# (After second mission finishes or Rowan meets the dirt general event in Rosarian hills)
"""A derogatory term for commanders of low birth.  Generally used by nobles to refer to anyone who they feel has risen above their station.  Notably the hero Rowan is viewed as a Dirt General by the majority of the Rosarian high born and they fear the potential threat he represents against the established order.
"""),
    }
