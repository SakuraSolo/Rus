init python:

    #Greyhide shares his people's liquor
    #Follow up to Drinking buddies if men was chosen.
    event('greyhide_shares_his_people_s_liquor', triggers="week_end", conditions=('week >=4', 'drinking_buddies_suggestion == "men"'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Jezera is stressed
    event('jezera_is_stressed', triggers="week_end", conditions=('week >=4', ), group='ruler_event', run_count=1, priority=pr_ruler)


label greyhide_shares_his_people_s_liquor:
#Greyhide shares his people's liquor
#Follow up to Drinking buddies if men was chosen.

scene bg22 with fade
show greyhide sad at cliohnaright with dissolve
show rowan necklace happy at midleft with moveinleft

ro "Good evening my friend, how have things been going for you down here these last few weeks."

show greyhide neutral at cliohnaright with dissolve

gh "Well enough, I hope that the whelp has not been driving you too hard on the surface."

ro "I'm managing. So what did you invite me down here for?"

gh "For this."

"The minotaur extracted two flasks from a drawer in the side of the room and handed one of them to Rowan. Then he sat down on a bench and motioned for the man to sit nearby."

ro "What is it?"

gh "Firegrout draft. You shared with me your people's drink, so I wanted to share mine. Here I can eat soft grain and fresh fruit, instead of dry bushes and the moss from stones. This wonderful drink is one of the few things from that place that I miss."

"Without further ceremony, Greyhide popped the stopper out with his teeth and downed the contents of the flask in a quick gulp. Making sure he wasn't going to pass out from drinking too much too quick, Rowan instead sipped his, then swallowed the whole flask."

ro "I can see why you miss having firegrout, it's quite good. Why is it hard to find around here?"

gh "One of the mosses from the Dragon's Tail is used to make it. A thing that grows nowhere else, so I had to ask for it and do favors to get some. I am very glad you like it."

ro "Tell me about your home...."

scene black with fade

scene bg22 with fade
show greyhide neutral at cliohnaright with dissolve
show rowan necklace happy at midleft with dissolve
gh "Would you like another?"

ro "Hah, no thanks. I'm starting to think one might have been too much."

gh "Perhaps that is because you are human? Your fragile body cannot take as much as mine."

#gh blush
gh "Wait, I apologize for calling you frail, I think your body is beautiful. Compact and toned, like a serpent you're ready to strike at any time. Uh, I fear that this is coming out wrong."

"Rowan was somewhat dumbfounded by the minotaur's apparent fluster. It didn't help that he was feeling a pretty hot under his shirt as well."

#rowan blush
ro "My friend, wh-where are you going with this? *hic* Wow, that stuff goes through you fast."

"Now Greyhide shifted uncomfortably in his seat, stealing glances at Rowan and rather obviously adjusting his garment about his waist."

gh " Last we spoke you said that passion could be shared between men. I have, hesitated to act on this. Now I find myself heated in a way that I have not felt in years. I desire you, friend Rowan."

ro "Oh, haha. *hic* With how big that bulge is, I doubt you're getting inside me."

gh "I do not mind, I want to see you, feel you, taste you."

menu:
    "Apologize, you're not interested in him like that.":
        $ released_fix_rollback()
        ro "Sorry Greyhide.  I'm very very *hic* flattered that you think of me like that. I just don't feel the shame way about you. I mean, you're the a really great guy but..."
        show alexia 2 necklace concerned at edgeleft with moveinleft
        "Abruptly Alexia arrived on the scene, nervously glancing around."
        al "Rowan? Are you in here? Dinner's getting cold and Jezera wanted to ask about... are you drunk?"
        ro "Ha, wow you certainly look really nice tonight Alexia.  I uh, guesh minotaur liquor doshen't agree with me."
        show alexia 2 necklace angry at edgeleft with dissolve
        "Somewhat dismayed to see her husband so smashed, Alexia helped him up and let him lean on her sholder while she threw a look at Greyhide and nervously asked him."
        al "How many did he have?"
        gh "Just one."
        show alexia 2 necklace shocked at edgeleft with dissolve
        al "ONE?!"
        gh "Yeah odd, it takes four to get a bull that drunk... oh.  Heh, sorry about that, uh..."
        show alexia 2 necklace neutral at edgeleft with dissolve
        al "I'm Alexia, and it's okay, I'll take care of my husband."
        gh "Okay. Before you go, I must say, I think the two of you make a great couple. There are no two more desirable humans I have ever seen before."
        show alexia 2 necklace angry at edgeleft with dissolve
        al "Yes, thank you. I think we'll leave now, come on Rowan."
        hide alexia with moveoutleft
        hide rowan with moveoutleft
        scene bg14 with fade
        show jezera happy at midleft with dissolve
        show alexia 2 necklace neutral at midright with moveinright
        show rowan necklace happy at edgeright with moveinright
        je "Well now, where was the party? Looks like maybe you left early."
        "A groan escaped from Rowan's lips, but he didn't say anything more."
        show alexia 2 necklace angry at midright with dissolve
        al "The party went too fast, just one drink laid Rowan out."
        je "I see, interesting. Well, better get him to bed then. Hopefully getting up tomorrow won't be too hard on him."
        hide rowan with moveoutright
        hide alexia with moveoutright
        return

    "Yes! You want him too!":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        jump rowanGreyhideSex

label rowanGreyhideSex:

ro "Well, I can't shay that sounds bad! Show me what you've got."

#CG of Greyhide pinup.  Image can be same as Alexia scene, but with a new forge background.
scene black with fade
show greyhide neutral at cliohnaright behind black
show rowan necklace happy at midleft behind black

"Hardly had those words left Rowan's mouth and Greyhide was already pulling his breastplate vest up and over his body. Instantly the man's eyes were drawn to the enormous throbbing member that was now able to stand at full height."

ro "Woah, that's even bigger than I thought it'd be."

gh "Heheh, let me see yours."

"Now just going with what happened rather than giving much thought to what he was doing, Rowan quickly peeled his clothing off and held his arms out theatrically. Only here did he realize just how hard he was, which seemed odd somehow but the hero paid it no mind."

show rowan necklace naked aroused at midleft behind black

ro "Well, what do you think?"

gh "Beautiful."

ro "Oh! Uh, thanks. Eh?"

#CG of 69, with Rowan laying on top.
scene cg108 with fade
show greyhide neutral at cliohnaright behind cg108
show rowan necklace naked aroused at midleft behind cg108
pause 3

"Abruptly the minotaur reached out and lifted Rowan up completely off the ground. He laid down on the table while also turning the man around and set him across his well muscled chest."
"That giant manhood filled his vision, as well as the sizable balls beneath. At the same time, he could feel hot breath blowing over his rear and much smaller nuts."
"With some idea of what was happening now, Rowan reached out to stroke his friend's member. In response, something warm and wet started playing over the skin around his groin and paying particular attention to his scrotum."
"A glance backwards confirmed that Greyhide was using his tongue on him, though Rowan was surprised to see just how long that pink appendage was! He'd have no trouble getting that thing well wrapped around Rowan's cock. The idea was appealing."

menu:
    "That was exactly what Greyhide had in mind.":
        $ released_fix_rollback()
        #CG variation for Greyhide wrapping his tongue around Rowan's cock.
        scene black with fade
        show greyhide neutral at cliohnaright behind black
        show rowan necklace happy at midleft behind black
        "A moment later, Greyhide did exactly that. This elicited an approving grunt of pleasure from the human, who just basked in the pleasure of being so entwined for a few blissful seconds."
        "However, Rowan wasn't the only one who was in need of some stimulation, so he began jerking and teasing the massive meat that was positioned in front of him. Then an idea struck him and he opening his mouth so he could lick and nibble on the tip."
        "Greyhide's impressive lengths were surprisingly convenient for enabling him to sixty-nine with someone so much shorter than him. While some doors were closed, others had been opened."
        "Suddenly Rowan was jerked backwards and his cock dropped straight down into Greyhide's maw! The shock of the sudden suction and engulfment pushed him over the edge and he loose his few spurts of seed down that throat."
        #CG Cum variation
        scene cg108 with sshake
        scene cg108 with sshake
        scene cg109 with flash
        show greyhide neutral at cliohnaright behind cg109
        show rowan necklace naked aroused at midleft behind cg109
        pause 3
        "Apparently this was enough to also push the minotaur over the edge, as he grunted and pumped an extremely impressive coating of semen all over his own chest. Then Greyhide's arms gave out, and Rowan fell forwards onto the warm stains of white."
        "The two simply lay there for several moments, panting in sudden exhaustion and feeling a strange wave of dizziness."
        gh "Friend, your father's milk was delicious."
        ro "Haha, you're such a flatterer this evening. *hic*"
        jump rowanGreyhideEnd

    "The minotaur had a different target, Rowan's ass.":
        $ released_fix_rollback()
        #CG variation for Greyhide giving Rowan a rimjob.
        scene black with fade
        show greyhide neutral at cliohnaright behind black
        show rowan necklace happy at midleft behind black
        "However, as it turned out the minotaur had a different target in mind. A moment later his tongue traced a path up and over Rowan's asshole. He inhaled sharply in response and reflexively clenched up."
        "Greyhide was not perturbed and started massaging the man's toned asscheeks with his thumbs. Little by little, Rowan relaxed until he finally allowed that long bovine tongue to invade his backdoor."
        "Instantly, it sought out his prostate and started flicking and prodding that ball hidden just past his sphincter. The sudden stimulation drove Rowan wild, making it impossible for him to focus on anything. Still, he did his best to continue tugging and pumping mino-cock."
        "Greyhide's impressive lengths were surprisingly convenient for enabling him to sixty-nine with someone so much shorter than him. While some doors were closed, others had been opened."
        "Then, almost as suddenly as it had started, it came to an end. Greyhide seemed to sense that Rowan was at his peak and lifted him up over his head as he brought the man to an anal induced climax."
        #Show cumming CG.
        scene cg108 with sshake
        scene cg108 with sshake
        scene cg109 with flash
        show greyhide neutral at cliohnaright behind cg109
        show rowan necklace naked aroused at midleft behind cg109
        pause 3
        "Apparently this was enough to also push the minotaur over the edge, as he grunted and pumped an extremely impressive coating of semen all over his own chest. Then Greyhide's arms gave out, and Rowan fell forwards onto the warm stains of white."
        "The two simply lay there for several moments, panting in sudden exhaustion and feeling a strange wave of dizziness."
        gh "Friend, I found your back hole delicious."
        ro "Haha, you're such a flatterer this evening. *hic*"
        jump rowanGreyhideEnd

label rowanGreyhideEnd:

"A shriek brought an end to the revelry and Rowan instinctively leapt up to see what the cause was."

scene bg22 with fade
show alexia 2 necklace shocked at edgeleft with dissolve
show rowan necklace naked aroused at midleft with dissolve

al "Wha-wha-what is happening here!"

ro "Hi Alexia. We were jusht having a drink between friendsh. *hic* Why did you scream?"

al "You're naked and covered in bull cum!"

ro "Oh, sho I am. How'd that happen?"

"Then his lethargy and sudden rise caught back up with him and Rowan's vision began to swim."

ro "My head, wha-?"

hide rowan with dissolve

"He swayed once, then fell to the ground unconscious."

show alexia 2 necklace angry at edgeleft with dissolve

"Alexia turned to the minotaur who was still laying down on the bench nearby..."

show alexia 2 necklace aroused at edgeleft with dissolve

"... then quickly turned back at the sight of the naked minotaur covered in his own spunk."

al "Damn it, put some clothes on! It's not proper to show yourself like that to a lady!"

"It didn't take long for the minotaur to pull his armor back on and readjust it."

show greyhide neutral at cliohnaright with moveinright
show alexia 2 necklace angry at edgeleft with dissolve

"She noted he hadn't bothered to clean the cum off, but Alexia tried to ignore that and spoke some rather choice words."

al "Exactly how much did my husband have to drink?"

gh "We just had one each."

al "Don't lie to me you bastard! That's not one drink!"

show greyhide sad at cliohnaright with dissolve

gh "It is strange, normally it takes four drinks to get to that point. Could his small body not take... oh."

al "So, not only did you give him something way to strong for a human, but you also seduced and fucked my husband right in front of my eyes!"

gh "This outburst is uncalled for! I am certain that our friend Rowan will be fine. Why did you call him 'husband'?"

show alexia 2 necklace look away at edgeleft with dissolve

"Her rage was running cold and Alexia could feel tears starting to form, but still she spoke with clenched fists and gritted teeth."

al "A husband is one who has vowed to love only one other, his wife, me."

gh "I... I did not know. I am sorry for doing this, I really am not feeling like myself today. Um, does that husband wife thing allow for a third to join them?"

#alexia crying

al "No! Shut up! I'm taking *my* husband home now."

#If this is the first time Rowan has had sex with anyone but Alexia
if rowan_non_alexia_sex > 0:
    "Now the tears were streaming down her face. They'd been together for so long, why was this massive monster the one Rowan had broken his vows with? Had he turned his back on her, no she mustn't think like that now."
    "Alexia had always feared that her darling would be taken by one of the denizens of this place, but for it to happen right in front of her? That was almost too much to bear."

#Else
else:
    "Now the tears were streaming down her face. Alexia had feared that her darling would be taken by many of the denizens of this place, but for it to happen right in front of her? That was almost too much to bear."

#rejoin

"Instead she blearily kneeled down and helped Rowan get to his feet. Thankfully she didn't need to carry him, he wasn't that out of it, just guide him and support him."

show rowan necklace naked at midleft with dissolve

gh "Curse my ancestors, I feel so strange now! I do not know what has come over me!"

#dungeon/underground tunnels.
scene bg14 with fade
show jezera neutral at midleft with dissolve
show alexia 2 necklace angry at midright with moveinright
show rowan necklace naked at edgeright with moveinright

je "I heard a scream. I thought that something had happened, but from the looks of things there was just a party?"

al "Don't talk to me now, demon."

show jezera happy at midleft with dissolve

je "Feisty tonight! Why are you so upset, you've got a handsome half naked man on your shoulder, shouldn't you be happy?"

al "Why the hells should I put up with... your..."

"She trailed off, suddenly realizing just who she was yelling at and feeling a deep chill in her heart."

je "Yes, this is {i}my{/i} castle and I can do what I want. Mouthing off to me like that isn't exactly the best of practises. Now, I can see that our man here isn't in the best of shape, so I'll leave my questions for later. Sorry about wasting your time finding him."

je "Ta."

hide jezera with moveoutleft

scene bg9 with fade
show rowan necklace naked at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

"Once they'd reached Rowan's room, Alexia laid her husband down on his bed and sat down next to him for several moments."

ro "Hmm, Alexia? Do you, feel like having some fun? I wanna fuck you till you drop."

"Alexia shot him an incredulous look, then saw he'd fallen asleep."

hide rowan with dissolve

show alexia 2 necklace concerned at midright with dissolve

al "(This isn't like you, what's going on?)"

#Rowan gains corruption.  Alexia and Rowan lose a little relationship.
$ change_base_stat('c', 2)
$ change_relation('alexia', -5)
#Note that Rowan and Greyhide had sex.
$ rowan_non_alexia_sex += 1
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label jezera_is_stressed:
#Jezera is stressed
#No requirements.

scene bg6 with fade

show rowan necklace neutral at midleft with dissolve
show jezera happy behind bg6

je "-Rowan, be a darling and come up to my room, I need some help unwinding."

ro "What exactly do you have in mind?"

je "Oh, just a massage from handsome company."

ro "... and?"

je "Well, maybe I'll tease you a bit too. You'd rather have a playful mistress than a grumpy one, wouldn't you?"

menu:
    "Tell her you're too busy.":
        $ released_fix_rollback()
        ro "Now really isn't a good time. You only give me a day to do all this work, you'll probably be a lot grumpier if I don't get it done."
        "There was no answer for a painfully long moment."
        show jezera neutral behind bg6
        je "Fiiiine. I'd have thought you'd have jumped at the chance to touch a lady's fine skin, but you just take care of those duties of yours then. I'll find someone else."
        "Rowan let out a breath he hadn't realized he was holding, then waited for several more moments before returning to his work."
        "Jezera wasn't as overtly frightening as her brother was, but that just meant she could be intimidating in other ways. Who could say when she felt offended?"
        #note rowan's refusal to give a massage
        $ jezera_is_stressed_massage_refusal = True
        return

    "Go up to Jezera's room.":
        $ released_fix_rollback()
        jump rowanJezMassage

label rowanJezMassage:

$ rowanJezSex =+ 1

ro "Alright, on my way."

je "Excellent."

scene bg14 with fade
show rowan necklace neutral at midleft with moveinleft

je "Enter."

"Rowan stopped, his hand raised about to knock on the door."
"Of course, since Jezera was expecting him, she'd been watching his position. It made sense that she knew he was there."

scene bg18 with fade
show jezera happy at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

"Entering into the finely decorated room, he found Jezera was laying down on her bed, propped up on one arm and running the other up and down her body enticingly."

je "I'm so glad you weren't too busy to come by and help me out."

"She let out long groan, then exaggeratedly stretched out."

je "Today was a damn frustrating one, so I just need a chance to unwind.  Come over here and give me a well deserved massage."

#massage CG
scene black with fade
show jezera happy behind black
show rowan necklace neutral behind black

"Knowing better than to keep his mistress waiting, Rowan immediately stepped next to the bed where she'd rolled onto her chest and placed his hands onto her back."
"Right away he noticed that her flesh was unusually soft and felt more pliable than normal human flesh. Yet there were no creases and no wrinkles, just perfect violet skin."

je "Hmm? Come, my hero, put some force into it. I am not so delicate that I'll snap in two if you don't restrain yourself."

"Deciding to test that limit, if just for a moment, Rowan put the whole of his upper body weight down on his hands. Then dragged them down between her shoulder blades. A long reassuring sigh was his response."

je "Oh, yes. That's much better."

"Demon, the man reminded himself, trying to put the same weight behind his touch as he continued the massage. This was difficult going and wore him down rather quickly. So he tried moving onto her arms instead."
"Abruptly Jezera rolled over onto her back, locking eyes with Rowan."

je "Nah, could you give my chest a massage instead? They're just so tender and perky right now."

"He hesitated, unsure what of make of this. Was it a proposition? Did she want to see how he'd interpret this?"

scene cg214 with flash
show jezera happy behind cg214
show rowan necklace neutral behind cg214
pause 3

je "Too slow, too slow."

"Or maybe she was just looking for an excuse to move onto something else. In an instant, Rowan had found himself completely tied up in magical bindings of blue light."

ro " I-"

"One of the tendrils wrapped around his face, cutting off his voice."

je "Shh. Now it's time for me to have some fun."

"Rowan was pulled forward up onto the bed and deftly freed of his garments as Jezera leaned back onto her arms and reached out with her toes to caress the man's cock."

#Show footjob CG
je "How does that feel? Hah, I love seeing you squirm around like that."

"Her teasing was ever so light, just barely touching him. Try as he might, there was no way that Rowan could either pull free, or get her to touch him more fully as he grew harder and harder.  The hero was fully in his captor's power."
"Now the demon's second foot came up and curled around the glans while the other continued to brush up and down Rowan's length. Still, she kept taking it slow. Such a pace was agonizing, Rowan couldn't help but let out a bit of a whimper."

je "Aww, is something wrong? You look like you're enjoying this."

"It did feel good to have those small, taloned toes touch him, tease him, toy with him. He wanted more. That was probably what Jezera wanted him to feel, but Rowan couldn't tell if it was his own desires or those which had been foisted on him."

je "I bet you'd like this too."

"Finally seeming to be done with the prelude, the demoness repositioned her feet so that one was on either side of Rowan's cock, toes up and pointed to his belly, and let him slide up through the gap between them."
"Rowan gave a satisfied grunt, now that the teasing seemed to be at an end.  Even still, Jezera took it slow.  Her violet souls went up and down a gentle steady pace."

je "Looks like you do, but what's with that face? Wanna cum? I bet you do."

"Her movements remained steady however, as she locked eyes with her servant."

je "In a moment, I'm going to take off your gag. I only want to hear three words from you, my hero, okay?"

"A grunt was the only answer Rowan could give."

je "Good, now say, 'Yes, mistress Jezera.' Do you want to cum?"

"The tendral came away."

menu:
    "Do as she wants.":
        $ released_fix_rollback()
        show rowan necklace naked behind black
        ro "Yes mistress Jezera."
        "Then his mouth was blocked again."
        je "Good boy.  Now, about your reward..."
        "At long last the pace increased, quickly driving Rowan towards his peak."
        #Show cumming CG
        scene black with fade
        show jezera happy behind black
        "Only a few moments later he felt his insides clench and let loose his seed over the soft flesh of Jezera's feet. She didn't let up her stroking until a moment after he'd finished, just before it started to hurt."
        je "I see you really like every part of your mistress, from top to bottom. There's still so much fun we will have together."
        "After wriggling her toes for a moment and working the white goo he'd covered them with in, she pressed the big one into his chest and drew a circle. A trail of cooling liquid was left in the wake."
        scene bg18 with fade
        show jezera happy at midright with dissolve
        show rowan necklace naked at midleft with dissolve
        "The tendrils of power retreated, releasing Rowan and allowing him to gather up his clothes."
        je "Well, I am thoroughly relaxed and satisfied now. Thank you, my hero, you are dismissed."
        #gain favour with Jezera
        $ change_favor('jezera', 1)
        return

    "Deny her.":
        $ released_fix_rollback()
        show rowan necklace naked behind black
        ro "I'm not saying it."
        "Then his mouth was blocked again."
        #denial cg
        scene black with fade
        show jezera happy behind black
        je "I guess then you don't want to cum. Well, I'm fine either way."
        "Her teasing didn't let up, if anything it adopted a pace that was intended to bring Rowan to the edge again and again, but then relax just before he hit his peak. It seemed that Jezera took great pleasure in this, constantly taunting him each time she did so."
        "Denying Rowan seemed like it was actually getting her off, as the demoness started to touch and run her fingers over her womanhood as the torture continued and brought herself to orgasm on at least two occasions."
        scene bg18 with fade
        show jezera happy at midright with dissolve
        show rowan necklace naked at midleft with dissolve
        "As she promised, the man never came. He simply was set down about an hour after he'd been summoned."
        je "Well, I am thoroughly relaxed and satisfied now. That is the important thing. Gather up your things Rowan, you are dismissed."
        "Rubbing a bit of feeling back into his limbs, Rowan scooped up his clothes and started towards the door."
        je "Oh, just so you know, today is going to be an inspection day. I hope you focus extra hard on your work and don't get caught up in any further pleasure seeking. You will have a very cross mistress if I catch you trying to get off today."
        #gain favour with Jezera
        $ change_favor('jezera', 1)
        return


