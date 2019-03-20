# glossary entries for journal
init python:
    # glossary consists of categories, categories consist of list of entries, that are shown as single tesxt in glossary screen
    glossary_entries = {
        'checks_start': ('Checks',
"""Similarly to Dungeons and Dragons and other pen and paper role playing games, whenever Rowan needs to perform actions like jumping over a gap, scaling a jagged cliff face, or bluffing his way out of a tense situation, he must pass a test to see if he succeeds in doing so. When the player wants to perform an action that requires a check, the game rolls a virtual twenty sided die and adds any relevant modifiers from {b}Skills{/b} or {b}Primary Statistics{/b} to determine whether they succeed or not. The harder the action the player wants to perform, the higher the number that must be matched or bettered for them to succeed.
"""),
        'checks_partial': ('Checks',
"""{b}Partial success and partial failure{/b}: Not all events have two outcomes for {b}Checks{/b}.  Sometimes you can get a lesser success or failure by meeting a lower threshold.  These might be Rowan falling down, but not being hurt as much by the fall or convincing someone he isn't an enemy, but failing to convince them that he isn't suspicious.
"""),
        'corruption_start': ('Corruption',
"""Corruption is a statistic that represents how corrupted by chaos the player and other characters have become. As it increases, their empathy and tendency towards goodness decreases, while their impulsiveness and attraction towards darkness increases. Corruption can change the options that the player can choose during events, and may also be a requirement for certain events to occur.
"""),
        'corruption_increasing': ('Corruption',
"""Corruption can be increased by the following:
    * Crossing, entering, or spending time in an area that has become corrupted by chaos.
    * Committing dishonourable or despicable deeds for personal gain / lacking moral justification.
    * Taking possession of a cursed or tainted item.
    * Engaging in sexual congress with with an agent of / creature tainted by chaos.
"""),
        'gold_start': ('Gold',
"""Gold is the term for the funds that Rowan carries on his person, and is separate from {b}Treasury{/b}. These are used, generally speaking, for things like purchasing items or information, paying tolls or bribes, etc.
"""),
        'guilt_start': ('Guilt',
"""Guilt is a negative statistic that represents the extent to which Rowan is being mentally affected by the evil acts he is being forced to commit. It has very little bearing on events or choices within them, but instead applies penalties to Rowan’s statistics if it rises too high to represent the emotional turmoil he is experiencing. If Rowan’s {b}Corruption{/b} increases, the threshold for these penalties also increases to represent the shift in his values.

Guilt is increased when Rowan is forced to act against his character, committing evil deeds, regardless of doing so for good ends. Whenever Rowan commits an act that is inconsistent with his character he will accrue guilt, leading to negative consequences. Guilt can be lowered by performing any action that is beneficial to others, especially those that are selfless, as knowing he can still do some good lightens Rowan’s burden. Guilt decays slowly over time."""),
        'infamy_start': ('Infamy',
"""Infamy is a negative statistic the represents what the world at large thinks about Rowan. As it increases, the fewer options the player has in exploration events, and the more like he will become treated harshly by people he meets. At very high levels, negative events about Rowan being being hunted by local authorities or other heroes will begin to trigger.

Infamy is increased by acting in any negative way that is likely to be seen by an average person as morally wrong or evil, when it is also likely that news of the act might spread. In most cases, this would be due to a witness to the aforementioned action(s), but this is not solely necessary if it is believable that word would get around.
"""),
        'intelligence_start': ('Intelligence',
"""One of the five {b}Primary Statistics{/b} that can be increased when the player levels up. It governs how intelligent Rowan is and is used to modify {b}Checks{/b} during events when smarts are required, i.e. thinking on his feet, and solving problems. It is also used an an additional modifier for all {b}Skills{/b} that are related to brain power.
"""),
        'luck_start': ('Luck',
"""One of the five {b}Primary Statistics{/b} that can be increased when the player levels up. It governs how lucky Rowan is, and is used to modify {b}Checks{/b} during events when luck is a factor, i.e. discovering treasure or other secrets. Luck works differently from the other {b}Primary Statistics{/b} in that it doesn’t modify any {b}Skills{/b}, instead it works in a more general sense. A player who invests in the statistic may find himself being grazed by heavy blows, or accidently avoiding traps by sheer luck alone.
"""),
        'military_capacity_start': ('Military Capacity',
"""Military Capacity is the statistic that represents the combined strength of all the player’s current military assets, and is used to determine whether or not Rowan has meet his quotas. It includes but is not limited to: troops in the barracks, military equipment, monsters, and magical relics, or special characters acquired.
"""),
        'military_capacity_conquest': ('Military Capacity',
"""{b}Conquest Capacity{/b}: Not all of the castle's military capacity is necessarily available to use when conquering or capturing points of interest on the exploration map.  When different to total military capacity, the player's conquest capacity will be displayed next to military capacity in brackets.  This represents what portion of the castle military is available to be used freely on the map or during events involving the military.
"""),
        'morale_start': ('Morale',
"""Morale is the statistic that represents the happiness of inhabitants of Castle Bloodmeen, which must be carefully managed to avoid potential problems. All troops have a morale cost that must be met every week, so the player must find ways to increase Morale generation as their army grows. Morale can be gained or lost by events; the excitement of conquest will award Morale, while an unpopular decision like limiting the spoils of battle will lead to a loss. If Morale falls too low it will lead to unruly behaviour, desertion, and in the direst of circumstances, outright rebellion.
"""),
        'primary_statistics': ('Primary Statistics',
"""The main statistics that are used to determine Rowan’s various abilities. There are five Primary Statistics - {b}Strength{/b}, {b}Vitality{/b}, {b}Reflexes{/b}, {b}Intelligence{/b}, and {b}Luck{/b}. These are used to determine the outcome of {b}Checks{/b} in which they are used, and to modify relevant {b}Skills{/b} when necessary. The player can choose how they would like to increase these statistics when levelling up, and they are modified by most equipment.
"""),
        'reflexes': ('Reflexes',
"""One of the five {b}Primary Statistics{/b} that can be increased when the player levels up. It governs how dextrous Rowan is, and is used to modify {b}Checks{/b} during events when his agility is put to the test, i.e. running, avoiding, and when quick reflexes are needed. It is also used an an additional modifier for all {b}Skills{/b} that are related to agility.
"""),
        'skills': ('Skills',
"""Skills represent specialized abilities that Rowan possesses, that can be increased when the player levels up. They are used primarily for {b}Checks{/b}, along with any other modifiers, to determine whether or not the related action succeeds.

Rowan has the following skills:

    * Bluff
    * Climb
    * Deceive
    * Decipher Script
    * Diplomacy
    * Disarm Device
    * Dodge
    * Escape Artist
    * Hide
    * Intimidate
    * Jump
    * Listen
    * Move Silently
    * Open Lock
    * Search
    * Sleight of Hand
    * Spot
    * Survival
    * Swim
"""),
        'strength': ('Strength',
"""One of the five {b}Primary Statistics{/b} that can be increased when the player levels up. It governs how physically strong Rowan is, and is used to modify {b}Checks{/b} during events when that strength is to put the test, i.e. lifting / gripping / pulling things. It is also used an an additional modifier for all {b}Skills{/b} that are related to physical strength.
"""),
        'treasury': ('Treasury',
"""Treasury is the statistic that represents how much money is currently in the castle coffers to be spent on all matters involving Castle Bloodmeen, such as any building and maintenance work, supplies, etc. Unlike {b}Gold{/b}, it is not available to Rowan in a personal capacity.
"""),
        'vitality': ('Vitality',
"""One of the five {b}Primary Statistics{/b} that can be increased when the player levels up. It governs how healthy Rowan is, and is used to modify {b}Checks{/b} during events when his health is a factor, i.e. enduring pain, resisting disease and/or infection, or holding his breath. It is also used an an additional modifier for all Skills that are related to health and physical endurance.
"""),
    }
