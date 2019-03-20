init python:
    
    event('orciad_debrief', triggers='week_end', conditions=('orciad_state == 2',), run_count=1, priority=pr_story)



label orciad_debrief:

$ goal3_completed = True

$ journal.complete_quest_note('orciad', 'note32')
$ journal.complete_quest_note('orciad', 'note33')


scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

if delane_status == "free" or delane_status == "dead":
    show andras displeased at edgeright with dissolve
    show jezera displeased at midright with dissolve
    
else:
    show andras happy at edgeright with dissolve
    show jezera happy at midright with dissolve
    
je "Rowan, come forth and kneel."

"Rowan took a knee in front of the throne. Andras sat on the throne with legs spread confidently. He didn’t so much sit on the throne as occupy it. Jezera hovered like a shadow over his shoulder."

je "We commanded you to make an ally for us among the races that were once part of our forefather’s coalitions. The orcs of Rosaria were an intelligent choice for this mission. Dumb. Strong. Malleable."

if delane_status == "free" or delane_status == "dead":
    je "It’s too bad then that you failed in your effort to recruit them."
    "Jezera walked down the length of the stairs. Moments later, she was standing over Rowan, regarding him with a dark look. He didn’t change his posture. For a brief moment, he had the flickering worry that they might know about what he had done."
    je "Rowan. Rowan. Rowan. What am I to do with you?"
    an "I know what we should do with him."
    "Jezera rolled her eyes, but turned back to Rowan with an expression that did not at all match her playful tone."
    je "You tried, I’ll give you that. But, this entire enterprise has been a lengthy debacle. The noblewoman escaped, and that means no leverage on the tribe."
    "Rowan kept his head bowed. Better to not appear contrite. He was already deep in a pit of vipers."
    ro "I am deeply sorry for my failings, Mistress. I could not account for all the variables, even though it was my responsibility."
    ro "I am assuming we cannot bring Batri into the fold?"
    je "Batri? I suppose you’ve been here and haven’t heard the news." 
    je "Batri is dead."
    show rowan necklace shock at midleft with dissolve
    "Rowan half gasped. He’d seen Batri only a few days before. He’d been alive and well then."
    show rowan necklace neutral at midleft with dissolve
    ro "Batri is dead? Who rules the tribe now?"
    show tarish neutral behind bg6
    tar "I do."
    hide tarish
    show tarish neutral at edgeleft with moveinleft
    "Rowan looked behind him, and saw a feminine figure slither out of the shadows. It seemed she’d been there the entire time. It was a female orc who he’d come to be well acquainted with."
    ro "Tarish?"
    $ tarish_name = 'Tarish'
    tar "If Batri ‘n Ulcro are dead, who da ya think the tribe belongs to now? Batri went out huntin’ dat noble gal who went missin'."
    if delane_status == "dead":
        tar "Didn’t know nuttin, but he thought dat one ‘o your people’s castles had 'er. Heard a rumor. Went chargin' up to it without no fear. Caught an arrow right in eye."
    else:
        tar "His boys caught her tracks near one ‘o your people’s castles had 'er. Heard a rumor. Went chargin' up to it without no fear. Caught an arrow right in eye."
        "She made a whooshing sound to emphasize the point."
        an "With the dumb oaf dead, the tribe started to split apart. But, Tarish here jumped in the middle and kept about two thirds of them together. Unlike Batri or Ulcro, she’s proven far more willing to make a deal."
        "Tarish interjected, shooting Rowan a dark glance."
        tar "I see what way da wind blowin. Is a good deal for us…"
        "She leaned forward, and whispered in his ear. She coated her words with cold anger."
        if tarish_path == False:
            tar "...but, I not be forgettin' bout da deal I offered you. You didn bring me da girl. I coulda had da whole tribe. Not just part."
        else:
            tar "We had a deal, humie. Ya broke the faith. Ya cost me nearly half da tribe. I not be forgetting dat at all."
        "Rowan kept totally still in place. Tarish’s return would be trouble. More to the point, such a valuable ally could not be antagonized in front of the twins."
        je "In short, you failed, but by pure happenstance events transpired in a way that worked out for you. If I didn’t have oh so much evidence to the contrary, I’d say you were a lucky man, Rowan." 
        je "So we can forestall punishment this time. We would have prefered the whole tribe, but this will do for the moment. Next time, more will be expected of you. That girl’s escape almost ruined everything."
        an "Though, I think you’ll want to know the terms our deal, boy. Tarish may be joining us, but we had to agree to throw her a bone too."
        tar "Da tribe wants slaves. Many were taken by dose who left. We need more."
        "Rowan gulped."
        an "The next few villages you take, you’re bringing back to Tarish here. No chickening out and making trade deals. You hear me?"
        ro "Of course, master."
        "He swore inwardly. Tarish’s propensity for brutality was no secret. With her not only at the helm of the orcs, but with no love, it meant a possibly more brutal then normal orcish army."
        if delane_status == "free":
            "His heart sank softly, taking with it any self esteem he’d regained from the escape."
            "Even his small acts of heroism still meant the suffering of innocents. He had to force himself not to scowl."
        else:
            "His heart sank hard. Not only had he failed to rescue Lady Delane, but in the process had ensured greater suffering as a result of his actions." 
            "Today was a dark day."
        #TODO
        #Next 3 villages, forced enslavement. No reward. 
        #Max Morale reduced by 20 (from 100 to 80)


else:
    "Andras laughed loudly and joined in."
    an "You continue to surprise me. I expected you to sneak off with a bunch of goblins. That is if you didn’t go yellow like a coward. But, you went to take the bull by the horns."
    je "We’ve been in contact with the leadership of the tribe and they have agreed to not only support us, but send out war chieftans to the other clans to raise a larger force. With their presence we will be able to put the beginnings of a real army in the field."
    
    if orciad_ally == "tarish":
        show andras displeased at edgeright with dissolve
        an "Though, I don’t know how much use these fighters will be with a spider at their head. Poisoners and schemers are no fit for leading an army of raiders and killers."
        "Jezera waved him off."
        je "We’ve been discussing her of late. As you can see, brother is less than pleased with the choice of ally. But, I recognize your wisdom in this situation. Unlike the men, she has a head on her shoulders as opposed to between her legs."
        je "But, she is far shrewder than the men of the tribe. All of them dueling over dick size. With Tarish at their head, we will have no fear that they will bungle off into a trap of some sort."
        "Andras rolled his eyes, but didn’t press the point. Rowan silently updated his mental calculus. So long as Jezera vouched for her, he doubted Andras would pin his annoyance at the choice of leader on Rowan."
        
        if avatar.corruption > 39:
            "And, perhaps, in the process had placed someone at the head of the tribe whose loyalty could be transferred to him personally..."
            
        else:
            pass
    
    if orciad_ally == "ulcro":
        an "Ulcro is an old hand. He fought in the last war. And with that new concubine of his, he’s got some fire in his belly again. I could have used someone with some more of a savage in him, but I can take solace that they’re led by a real soldier."
        je "He’s a strange beast. He’s almost too human. But, I see the wisdom in your choice, hero. Any other conender would have more will of his own. But, whispering birds tell me that his new human woman rules him."
        je "Do you believe that this Lady Delane will be a friend?"
        "Rowan nodded softly."
        ro "I found her quite amenable to persuasion. She likes sex and power, but fancies herself an intellectual. Court her and make her feel important, and she will ensure that Ulcro does as you bid."
        "Jezera’s smile grew larger."
        je "You have more cloak and dagger in you then I first anticipated. You’re a most interesting toy indeed, Rowan."
        "Rowan didn’t have an answer to that. He kept his head bowed and his mouth shut."
        
    if orciad_ally == "batri":
        an "You made the right choice in who to support. This Batri is a fighter. With him at the head of our orcish contingent, we will send the Rosarians running back behind their walls."
        je "Don’t be too excited, brother. Batri is tough, but he is a blunt weapon. His will may also make him a frustrating ally."
        je "More to the point, I doubt we can expect much guile from him."
        je "Whether that means he will be an incompetent tactician or if it means he will be easy to control...well we’ll see. Probably both."
        "Jezera turned to Rowan with an eyebrow raised."
        show jezera neutral at midright with dissolve
        je "The part that surprised me was that you chose him at all. The most brutal of all the possible contenders. Perhaps our little hero has a bit more Andras in him then we realized."
        "Rowan didn’t have an answer to that. He kept his head bowed and his mouth shut."
    
show andras displeased at edgeright with dissolve
show jezera neutral at midright with dissolve

if rastedelFirstVisit == False:
    je "Do not forget to visit your dear old capital. I’m eager to see how your long awaited return turns out."
    "She let out a playful giggle."
    
else:
    pass
    
"Rowan nodded and rose to leave. As he left his hall his mind turned to larger matters. The forces at the twins command had grown substantially. Until now, it had all been skirmishes, but a true war was in the making."

if avatar.corruption > 39:
    "Yet, why did that prospect sound almost...exciting?"
    
else:
    pass
    
return


