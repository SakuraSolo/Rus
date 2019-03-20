#Tarish Quest Line - Initial Event
#occurs the first time Rowan visits Tarish after finding and meeting Delane

label tarishQuest:

scene bg30 with fade
show rowan necklace neutral at midleft with dissolve
show tarish neutral at midright with dissolve

tar "So, humie, did ya find da woman yet?"

ro "It took a while, but she’s being hidden away in one of the tents in the camp."

tar "Dat makes sense, Ulcro wouldn’t want ‘iz precious prize dat far away from ‘im, and he has da orcs to make sure Batri an’ iz boyz couldn’t just take her."

ro "The tent is guarded, yes. If I am to keep seeing her, I’m going to have to keep trying to sneak in, and hopefully avoid being seen. I can’t afford to get caught, even if I could fight my way out."

tar "Dat’s smart, don’t want to bring any attention to yerself or our plans at da moment."
tar "Can ya get ‘er out of da camp?"

ro "It’ll be tough. For one, those guards? I may be able to sneak past them if I need to, but with a noblewoman in tow? I doubt she has spent much time skulking around forests."

tar "Dat’s alright, I got a few tricks up my sleeve dat can take care of the guards when da time comes."

ro "It is not just the guards, unfortunately."
ro "Life in the courts, and as a prisoner here, has made her very wary of others. In order to convince her to try to escape, even if it was just a ruse, would require her to trust me, and I suspect that trust won’t be given easily."

tar "I can’t help you wit’ dat one humie, you gonna have to win ‘er over yaself. "

ro "Probably for the best. Even if you wanted to, I doubt you could offer much in the way of help. Adding an orc to the mix would only make her less likely to trust me, considering how she feels about your kind."

tar "It can be done though?"

ro "I think so. It will take some time to convince her to trust me I’m sure, but eventually the chance of escape, even if it is a risk, will grow to be a more desirable option than being the prisoner of orcs for the rest of her life."

tar "So what do ya say, humie, will ya help me dispose of da dumb male orcs for good of tribe?"

menu:
    "Yes.":
        $ released_fix_rollback()
        ro "Yes, I don’t have time to waste with bruised male egos, and petty squabbles over women. Someone who could actually get things done around here would be a much better choice."
        ro "I will help you become leader of the tribe Tarish, in return for your support at a future point, of course."
        "The orc woman grinned, clearly happy that Rowan had come around to her way of thinking."
        tar "Dat’s gud, I knew dat da demon’s pink was not as dumb as other stupid males."
        tar "In order to get rid of dem, I need three things."
        tar "Da first is what we talked about earlier, I need ya to win da trust of da woman and convince her to escape da camp. Once ya get outside da camp, you will deliver ‘er to me and my boyz, and we will take care of da rest."
        ro "And the other two things?"
        tar "I need sumthing to get rid of Batri and Ulcro. Missing humie slut will cause dem to fight, and we can take advantage of dis."
        tar "If ya can find me sum strong poison, I can have one of my spies put it on da weapons before da fight, dat way we kill two birds one stone."
        ro "I think I know a goblin merchant who will have something that we can use. And the last thing?"
        tar "Need sumthing to keep da humie nice and compliant after we get rid of da chief, which will help keep sum of da dumb males from leaving instead of serving a woman. Male orcs dumb, always get lost in humie pussy."
        ro "My mistress dabbles in that sort of thing, she might have something magical that will do the trick."
        tar "Get these things, convince pink slut to trust ya, and den return to me, and we get things rollin’."
        ro "Okay."
        scene bg26 with fade
        show rowan necklace neutral behind bg26
        ro "(I should continue to visit lady Delane until she trusts me enough to try and escape. When I get back to the castle, I can visit Cla-Min and Jezera about the other things that Tarish needs.)"
        $ get_cla_poison = True
        $ get_jez_potion = True
        $ tarish_path = True
        jump campMenu


    "No.":
        $ released_fix_rollback()
        ro "No, I don’t think so."
        ro "Delivering Delane to you would be a fate worse than what is already in store for her, and on top of that, I have no guarantees that the tribe would even follow a woman."
        "The orc woman scowled, angered by his lack of vision."
        tar "Pah! Stupid humie as dumb as other males after all. Gud luck dealing with Ulcro and Batri, ya deserve each other."
        scene black with fade
        "From the rather threatening look in her eyes, Rowan realized that this was his cue to leave, and, unless he wanted to risk the chance of violence, never come back."
        "This avenue of dealing with the camp's problems was now closed to him, that much was sure, and if he wanted the orcs to back him, he would now have to deal with Ulcro or Batri."
        $ tarish_angered = True
        jump campMenu


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Tarish Quest Line - Cla-Min Event
#Occurs when Rowan visits the caravan in Bloodmeen for the first time after the Tarish route is active

label tarishQuestCla:

scene bg19 with fade
show rowan necklace neutral at midleft with moveinleft

"Rowan arrived at the caravan in search of the goblin matron, the most likely person to have the poison that Tarish needed. Boxes and goods were strewn all around the place haphazardly, and Cla-Min was currently nowhere to be seen."

ro "Hello? Cla-Min? Are you here?"

show clamin neutral at midright with dissolve

"First, the sounds of rustling. And then, the goblin emerged from the back of her caravan carrying a box that Rowan assumed, from the way she was struggling, contained something rather heavy."
"Being the gentleman that he was, he rushed over to relieve her of the task."

cla "Oh Rowan, I didn’t know you were here."

"The next line she over exaggerated to the point that it would have been unsubtle to even the densest person. The wink was, perhaps, the cherry on the cake."

show clamin happy at midright with dissolve

cla "My hero."
cla "I’m sorry for my absence, I’m planning a new trade route through the wastes so I was preparing goods to be traded en route."
cla "Did you need something, or did you just come to visit because you missed me?"

"With this she flashed him a grin, with no doubt something dirty in mind. He wondered if all goblin women were this insatiable, or if she was exceptional among her race. "

ro "As nice as it is to see you, I did need something, and I was hoping that you might have it."

"Cla-Min let out a deliberately over the top sigh, before flashing him her usual cute smile."

cla "It is always work, work, work with you Rowan, you need to learn to take it easy a little more and have some fun. I could help you with that, you know."

show rowan necklace happy at midleft with dissolve

ro "I’m sure the twins would be very happy if someone were to tell them I was working less in order to spend more time having fun."

cla "Fair point, but there offer is always there if you want it, lover boy."
cla "Anyway, what can I do to help you?"

ro "Noted. I’m having some trouble dealing with a bunch of unruly orcs, and I was hoping you’d have a little something that would help me take care of them."
ro "Poison."

cla "There’s that famous Rowan trickery that we goblins love so much. Hold on, I have just the thing."

"The goblin returned to the caravan before emerging a few minutes later, carrying a small vial filled with a thick, yellow liquid."

cla "Picked this up from the assassins guild on my last trip to Qerazel, should do the trick nicely."

ro "What is it?"

cla "Venom from the barb of a manticore. The most powerful poison they have, apparently. Cost me a pretty penny but it will kill even the strongest person within a few seconds of being introduced to their body."

ro "That will work perfectly, what do I owe you for it?"

cla "It is for something that the twins want you to do, no?"

ro "Yes."

cla "Then it is on the house."

ro "That is very generous of you, Cla-Min."

"She chuckled and then flashed him another of her winning smiles."

cla "What can I say? I like the idea of you owing me one."

ro "I’d better go, but thanks for this, really."

cla "It’s fine, I need to get back to work anyway."
cla "Don’t be a stranger."

$ get_cla_poison = False
$ got_cla_poison = True
$ journal.complete_quest_note('orciad', 'note22')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Tarish Quest Line - Jezera Event
#Occurs when Rowan visits the throne room in Bloodmeen for the first time after the Tarish route is active

label tarishQuestJez:

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve
show jezera neutral at midright with moveinright

je "Ah Rowan, there you are. Did you need something?"

"Rowan was surprised that the demoness had sought him out. He hadn’t told anyone about his plans, but as usual, she seemed to already know what was going on."

ro "How did you know?"

je "I have my ways, but a woman never discloses her secrets."
je "Out with it hero."

ro "I’ve been having some trouble dealing with the orcs-"

je "Stupid brutes, I know, but my brother insists on dealing with them. I suppose we do need the manpower, after all."

ro "It isn’t so much manpower in this case."

"Jezera perked up, shifting from the usual nonchalant demeanor that seemed to be her natural state."

je "Oh?"

ro "The men are fighting over a human noblewoman they captured in a recent raid, and it has brought the entire camp to a standstill, as well as causing divisions between the factions that have formed as a result."

je "I had heard this. Typical men."

ro "There’s an orc, a female, who is trying to take advantage of this situation to take power, and has promised to aid us if I assist her in doing so."

show jezera happy at midright with dissolve

"Jezera grinned, and rubbed her hands together."

je "A female orc outsmarting the stupid men? Oh I do like this idea. What can I do to help?"


if goal2_completed == True: 
    
    ro "Well, she needs something to increase the noblewoman’s libido, and I was thinking, since you had the ring you used on Helayna-"

    je "That was a one of a kind I’m afraid. Unfortunately, I did not create the thing, it was something I picked up on my travels."

    ro "Couldn’t you just make another?"

    je "I could, but it is ancient magic, and to be honest, I don’t entirely understand it. Trying to recreate it would be dangerous, and I doubt killing the woman is the desired effect, no?"

    ro "Ah."
    
    je "Worry not, my hero, I have another way to help you with your problem. It won’t be as permanent as the ring, but it will do the trick all the same."

else:
    
    ro "I need something to make lady Delane a little more…Receptive to the orcs advances. This seemed like something that would be right up you alley."
    
    "The demoness laughed, and once again flashed him a big grin."
    
    je "Oh yes, my hero. I have something that will do the trick, don’t worry."


je "I need a few hours to put something together, but it will be in your room waiting for you tonight when you return."

ro "Thanks, I appreciate it."

je "Think nothing of it, it is all in our service anyway."

"Her mouth twisted into a strange smile. To Rowan, it struck him that it might be something similar to the way a predator looks at its prey."

je "Now, don’t you have other things that you should be doing?"

$ get_jez_potion = False
$ got_jez_potion = True
$ journal.complete_quest_note('orciad', 'note21')
return


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Tarish Quest Line - Return Event
#Occurs upon returning to Tarish after the initial event above

label tarishQuestReturn:

scene bg30 with fade
show rowan necklace neutral at midleft with dissolve
show tarish neutral at midright with dissolve

if (got_jez_potion == True) and (got_cla_poison == True) and (delane_trust > 2):
    jump tarishQuestComplete

else:
    pass


#If Rowan returns without the two items, and/or without Delane willing to try to escape

tar "So humi, is everything ready for da plan to commence?"

ro "Not yet, I still have a few things to take care of."

tar "Den why da fuck are yous wasting time 'ere den?"

jump campMenu


label tarishQuestComplete:

#if Rowan returns with both items and Delane is willing to try to escape

tar "So humi, is everything ready for da plan to commence?"

menu:
    "Yes.":
        $ released_fix_rollback()
        $ delane_abduction = True
        pass
        
    "No.":
        $ released_fix_rollback()
        ro "I need a bit more time to get things sorted."
        tar "Hurry da fuck up den, we don't 'ave foreva ya know."
        jump campMenu


ro "Yes, I have both of the things that you asked for, and Delane trusts me enough to try to escape."

tar "Dat’s gud, I knew I could trust yous to get it done. Hand ‘em over."

"Rowan handed over the items that he had acquired from Cla-Min and Jezera to the grinning orc, who tucked them into her clothing where they could be concealed safely on her person."

tar "Yous don’t worry about these now. I take care of poison before challenge when dumb orcs are yelling at each other. Everyone will be busy watching dat, easy to have spy slip in da tents."

ro "And the escape?"

tar "Yous go later tonight. I make sure guards are orcs dat are loyal to me, not Ulcro, they won’t try an’ stop yous. Once yous get ‘er outta da camp, I be waiting in da forest to take ‘er off yous hands."

"Rowan felt a tinge of guilt inside from betraying lady Delane. She thought she was escaping, but she was merely being moved from one jailer to another."

ro "And the woman?"

tar "Don’t yous worry about da humie slut. With what yous got us from da bloo lady, she’ll be enjoying ‘erself in no time, as will da rest of da boyz."

if avatar.corruption > 49:
    "She let out a belly shaking laugh, and to Rowan’s surprise, he found himself chuckling along with her."

else:
    "She let out a belly shaking laugh, which only increased the level to which Rowan felt uncomfortable with the whole thing."

tar "Youa go now, I see you in da forest later."

scene black with fade

if avatar.corruption > 49:
    "Rowan knew he should feel disgusted at his actions, but he couldn’t help smile at the thought of a horny noblewoman being forced to learn her new place as the orcs used her again and again."
    

else:
    "Rowan nodded and left, his mind much darker than it had been when he entered the tent earlier."
    $ change_base_stat('g', +5)
    
scene bg26 with fade

"Tarish and her girls would handle all the operational support – distract the guards, secure the way out of the camp, and make sure nobody randomly stumbles upon Rowan and his target as they make their 'escape'." 
"All Rowan had to do, was get Delane out of the quarters, across the camp, and near the guard towers next to Tarish tents. Simple in theory." 
"In practice, a single mistake and he'll have a few hundred orcs out to get his head."
"The similarities between now and the Siege of Karst were not lost to him. Amazing how often his duties had him sneak through orc camps."  
"But this was not the time to reminiscent about the past. Once more, Rowan found himself near Delane's prison tent." 
"As always, he waited patiently for the inevitable lapse in the guards' routine, and sneaked inside." 

jump orciadEscape