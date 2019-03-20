init python:

    #Cla-Min bribing a proposition (benediction, sex)
    #Requires that Cla-Min's family dinner have happened at least 3 weeks prior and will require mission three to have started once the game timer has been extended.  Event can possibly be a trigger point for Cla-Min's stock to be updated.
    # activated in "goblin_family_dinner" with timer=3
    event('clamin_bribing_proposition', triggers="week_end", depends=('goblin_family_dinner', 'raeve_keep_visit_goal2'), conditions=('week >=4',), active=False,
        group='ruler_event', run_count=1, priority=pr_ruler)
    #Helayna has been claimed
    #Requirements - Rowan claimed Helayna during assault on Raeve Keep
    #High priority event, triggers the week that Helayna was claimed.
    event('helayna_has_been_claimed', triggers="week_end", conditions=('raeve_keep_rowan_claimed_helayna', 'week >=4'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Delf Dipping
    #Pre requisites - Breeding pit / met Draith
    #should probably occur within a few weeks of building
    event('delf_dipping', triggers="week_end", conditions=('week >=4', 'castle.buildings["pit"].lvl >= 1'), group='ruler_event', run_count=1, priority=pr_ruler)
    #Greyhide's table manners
    #Follow up from Drinking Buddies if player chose to introduce Greyhide to Alexia, and if Alexia and Greyhide have not met before.
    event('greyhide_s_table_manners', triggers="week_end", conditions=('week >=4',), depends=('drinking_buddies',), group='ruler_event', run_count=1, priority=pr_ruler)


label clamin_bribing_proposition:
#Cla-Min bribing a proposition (benediction, sex)
#Requires that Cla-Min's family dinner have happened at least 3 weeks prior and will require mission three to have started once the game timer has been extended.  Event can possibly be a trigger point for Cla-Min's stock to be updated.

$ cla_tit_job = True

scene bg19 with fade
show rowan necklace happy at midleft with dissolve
show clamin happy at midright with dissolve

ro "... and that's it for this weeks main orders."

cla "Excellent, then we can move onto more important matters!"

show rowan necklace neutral at midleft with dissolve

ro "Cla-Min, what is this about?"

"The goblin woman didn't answer, instead she busied herself with extracting a package from some nearby boxes, obviously intentionally taking the time to show off her backside to Rowan at the same time."
"As she came back around, her brother made his appearance and did an exaggerated stretch as he leaned against the nearby wagon. Rowan raised an eyebrow, realizing right away that this was a planned display."

#if Rowan was sucked off by Cla-Min's daughter
if goblin_family_dinner_mins_blowjob:
    "No doubt they were going to be making an attempt to earn his favor again, same as her family dinner.  Rowan felt himself become semi-hard at the thought of that night, to his discomfort."
#If Rowan refused the goblin blowjob
else:
    "Rowan rolled his eyes at this.  The Cla caravan was persistent, he'd give them that much.  Though he had to admit he was curious what they had planned for him this time, especially what that package was."

#rejoin
ro "Well, are you expecting me to ask what's in the package?"

cla "A little gift, of sorts."

ro "There's a catch then, isn't there?"

cla " Oh, I would hardly call this a catch. This item here is very powerful and rare, and I could never part with it for free to someone who wasn't a part of my family or I knew cared about them greatly."

"She unwrapped the package, revealing a glimmering sword of exquisite make and quality. It wasn't intended to be showy or beautiful, this was a weapon of function."
"Rowan could tell from a glance that it wasn't made of iron and might even have some magic in it."

ro "Couldn't I just buy that from you? I'm certainly interested, if that's not a brand made by the priest's of Balast, it is an extremely convincing forgery."

show clamin neutral at midright with dissolve

cla "You could, I would certainly part with it for a fair price."

show clamin happy at midright with dissolve

cla "However, wouldn't you rather an alternative? Why don't we have a nice personal discussion in my wagon, just let me take a seat on you until you fill me up with your cunning and sneaky spunk?"
cla "My brother could also discuss the details, if you'd rather have a man take you on for the time being. We'll worry about transferring the essence to a more compatible member of my family afterwards."

ro "It sounds like you're trying to pay for my body, am I a whore then?"

"The two goblins burst out laughing."

cla "No! No! Haven't you ever heard of a dowry, hero Rowan? It's traditional to give a gift when one departs their clan to join yours as a lover."
cla "Since you aren't really leaving a clan, I think it's appropriate that you receive the gift."
cla "We would be family then, after all?"

#If society chosen was feudal and Rowan has an unspent favor with Jezera or Andras.
if society_type == 'feudalism' and (all_actors['jezera'].favors >= 1 or all_actors['andras'].favors >= 1):
    cla "I suppose that since you've got the ears of our masters, if you could instead get them to grant a title to my brother here, that would convince me that you have my family's best interests at heart."

menu:
    "Have sex with Cla-Min":
        $ released_fix_rollback()
        jump claminSwordSex

    "Have sex with Cla-Min's brother, Cla-Bow.":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        jump brotherSwordSex

    #if feudal and you have the neccesary favour
    "Convince Jezera to grant a title to Cla-Bow." if society_type == 'feudalism' and all_actors['jezera'].favors >= 1:
        $ released_fix_rollback()
        #lose 1 favour with Jezera
        $ event_tmp['using favor'] = 'Jezera'
        $ change_favor('jezera', -1)
        jump clabowTitleGranting

    #if feudal and you have the neccesary favour
    "Convince Andras to grant a title to Cla-Bow." if society_type == 'feudalism' and all_actors['andras'].favors >= 1:
        $ released_fix_rollback()
        #lose 1 favour with Andras
        $ event_tmp['using favor'] = 'Andras'
        $ change_favor('andras', -1)
        jump clabowTitleGranting

    "Refuse":
        $ released_fix_rollback()
        ro "I think I'm good. Thank you for showing off your new stock, I'll definitely be considering a purchase soon."
        show clamin neutral at midright with dissolve
        cla "Such a shame.  Very well, this sword is now on sale. I hope you'll reconsider your other position soon. I assure you that under me is a very good place to be."
        #//End scene, Cla-Min's stock is updated to include the Balast's Brand at 300 gold, possibly other things as well.
        $ castle_shop_trader.inventory.add('balasts_brand_discounted')
        return

################################################################################

label claminSwordSex:

"Cla-Min was bouncing again and Rowan was having a hard time keeping his eyes off of her."

cla "Come on, you hot, wonderful, sneak, let's have a nice one-on-one."

scene black with fade

"A few minutes later inside Cla-Min's wagon..."

#CG1
scene black with fade
show rowan necklace happy behind black
show clamin happy behind black

ro "Well, someone is prepared."

cla "I'm always prepared for you."

"She was sitting on Rowan's lap, with both of them inside her caravan on a set of cushions arrayed in a corner. Her other family members weren't around and several incense sticks had been lit on a table nearby."

ro "Do you normally have discussions with people while you're sitting on them?"

cla "Normally? No. Preferably? Yes."

scene cg127 with fade
show rowan necklace happy behind cg127
#clamin naked
show clamin happy behind cg127
pause 3

"The goblin woman put a hand behind her and lifted the band of her top up and over her head, letting her breasts spill forth now that there was nothing to support them. Rowan's breath caught for a moment as he watched them bounce, then he took a deep breath."

cla "Now that's the reaction I was hoping for."

"There was a knowing smile on her face, the short-stack had taken note of the fact that she tended to distract the hero when she moved around."
"Now he was giving her his undivided attention and Min loved it. She grabbed one of his hands and brought it onto her breast."

scene cg128 with fade
show rowan necklace happy behind cg128
#clamin naked
show clamin happy behind cg128
pause 3

cla "Come on, get a nice feel for them. Make sure I've got the goods for your kids."

"With that encouragement, Rowan felt a little dirty as he got a firm grip of her flesh and ample endowments. He suspected that was part of the point."

ro "Can goblins and humans have kids with one another?"

"As he asked, the green woman on top of him busied herself with freeing his cock from his pants. Once his hardening member had been exposed, she looked up at him again, still smiling."

cla "Dunno, but I plan to find something else if the normal way doesn't work."

"One of her legs came up, a bare foot sliding across Rowan's chest, then she brought it back down on the other side so she could slip off her yellow silk pants."

ro "You sure you don't need me to help out, even a little bit?"

"Rowan could feel something hot and wet brushing over his leg as Cla-Min once again moved to be astride him."

cla "As the clan matriarch, I always make sure I'm the one on top at the end of all discussions."

scene cg69 with fade
show rowan necklace happy behind cg69
show clamin happy behind cg69
pause 2

"The goblin pushed her partner back as she rose up, then set herself down onto Rowan's stiff cock. This elicited a sharp gasp as her heat engulfed him."

ro "I see. Didn't take you for someone who'd be that fond of other races."

"She just smirked."

cla "As a secret just for you, I'm not. My pussy has felt non-goblin tongues, but yours is the first outsider's cock. Hmm...."

"She started rising and falling, while squeezing down tightly on her prize."

cla "...but I don't think of you as an outsider. You were born to the wrong family, you're a true goblin at heart."

ro "Gha, whoa. You're real tight."

"As it turned out, goblin women had some really strong muscles downstairs. Cla-Min might not be able to get her arms around Rowan for a bone crushing hug, but she was doing her best to do the same on his shaft."

cla "Don't want you trying to get away, hunny."

"Now the goblin started fucking in earnest, quickly pushing her small body up with her bare feet on the pillows, then letting herself fall back down at full speed."
"Rowan found his eyes drawn once again to her chest and watched those large breasts bounce and spin with her motion."

show cg70 with dissolve
pause 2

"Encouraged, he grabbed hold with both hands, using them to feel up those enthralling breasts once again. His lover approved."

show cg70 with sshake
show cg70 with sshake
scene cg71 with flash
show rowan necklace happy behind cg71
show clamin happy behind cg71
pause 2

"Finally, one more groan of pleasure escaped from Rowan's lips and he bucked against Min's hips, carrying her up into the air for a moment as he let out his seed into her womb. Just as she'd wanted him to."

ro "Hah, hah, you kinda make it hard to hold back."

cla "That was holding back? Goblin guys usually cum in half that time!"

ro "Hmm, normally I think guys would get annoyed for being compared to past lovers, but maybe I should take that as a compliment?"

cla "I think we'll be spending lots of time together, especially if this doesn't take. Who knows, maybe I'll want you to be my favored mate from now on? At the very least, I'm happy to welcome you to the Cla clan with a special gift."

"She slid off of him and happily trotted over to the wagon door."

cla "Come on hero.  I've got a gift for you."

#//End scene, gain Balst's Brand item, but flag that she'll be upset if you lose the item or refuse to have sex with her clan later.
$ set_actor_flag('cla_min', 'rowan_accepted_clamin_s_sword', True)
$ give_item('balasts_brand_gifted')
return

################################################################################

label brotherSwordSex:

"Rowan had been periodically stealing glances at Cla-Bow this whole time, there was some part of him found the goblin man attractive. His gaze had obviously been noted, as Bow stepped forward and ran a hand up and down Rowan's leg."

bow "Come on hero, we both know what you want. You big, beautiful hunk."

#CG1, Cla-Bow posing.
scene black with fade
show rowan necklace happy behind black

"A couple of minutes later, Cla-Min had excused herself and the two men had made themselves comfortable on a set of cushions that had been prepared for them inside the wagon."

bow "My sister had prepared some exotic items for this. I hope you don't mind if I dispense with most of them, not my style you see."

ro "Cla-Min does seem a bit overbearing."

bow "Yeah, let's forget about her for now. She isn't the one you just invited inside for some intimate negotiations about your future in our family. Speaking of which, I want to dispense with dancing around the subject too."

"He smirked and dropped his pants, revealing his semi-erect cock and tight sack."

bow "Let's fuck."

ro "Well you certainly get right to the..."

scene cg89 with fade
show rowan necklace happy behind cg89
pause 3

"As the hero spoke, the goblin popped open a bottle of some kind of ointment and got down on his hands and presented his ass up in the air towards Rowan."

ro "... point. Wow. Are you sure that's how you want to do this?"

"The short man twisted his head around to make eye contact while also starting to work the ointment into his anus, revealing his teeth in a wide grin at the same time."

bow "Hey, I figured that there aren't many guys in the castle who'd be willing to let you pack in their shit. So that's where I come in, or should I say, fill out?"

"He turned back away as Rowan undid his trousers and let his cock slip free, which had straining against its confines for the last minute or so. He'd finished lubbing up now but kept one of his hands back there to hold a cheek open."

bow "Besides, I like being with big studs like yourself. I don't get many chances, but when I do, ohhhh yessss...!"

scene cg90 with fade
show rowan necklace happy behind cg90
pause 3

"He'd slid in easy enough, that ointment worked well, but just how tightly his partner was squeezing down on him was tough to bear."

bow "Come on big guy, pound me."

"The egging on drove Rowan to do just that and he started thrusting in and out hard. Evidently Bow wanted this, so there was no reason to hold back and be soft. This was a romp, a chance to cut loose and just have fun."
"It was exhilarating to fuck a man's ass like this. He might be half Rowan's size, but Bow was a grown adult and his sounds made it clear he was loving every second of this. Evidently he was also adept at pleasing cocks, given how that ring was squeezing and teasing Rowan's shaft."
"In and out, push and pull. This tight muscular backside was a joy to have all to himself. The hero let himself go, giving into the rut and enjoying it as best he could."

bow "Dump everything inside me! Come on, you'll have plenty leftover, give me this load."

#CG2 variation 2, Rowan cumming.
scene cg90 with sshake
scene cg90 with sshake
scene cg91 with flash
show rowan necklace happy behind cg91
pause 3

"With one last growl, Rowan did so. He pushed himself up to the hilt on the goblin and unloaded several sprays of his seed deep inside Bow's asshole. Then he stepped back somewhat unsteadily."
"As the hero's head plopped out with a small strand of semen following it, Cla-Bow reached back and pressed a hand over his ass. He reorientated himself, while trying to hold everything in."

bow "Man, that felt really good. If it isn't too much trouble, I'd like to keep this souvenir for myself. I'll give you a blowjob in a few minutes, after you've had a chance to recover and I've had a chance to clean you off."

ro "Yeah, I think I can manage."

"Once again the goblin man grinned at him."

bow "Then I'll be sure to get sister to give you the promised gift. Maybe you'd like to go again after that? I'm not satisfied yet."

ro "You haven't gotten off yet?"

bow "No, I came three times while you were fucking me. Really, I just want to do it again!"

"Rowan shook his head in dismay."

ro "You're insatiable!"

#//End scene, gain Balst's Brand item, but flag that she'll be upset if you lose the item or refuse to have sex with her clan later.
$ set_actor_flag('cla_min', 'rowan_accepted_clamin_s_sword', True)
$ give_item('balasts_brand_gifted')
return

################################################################################

label clabowTitleGranting:

show rowan necklace happy at midleft with dissolve

ro "I think I could probably pull some strings on your behalf. What sort of a title where you thinking of? If I remember right, Cla-Bow doesn't have any children, does he?"

cla "Oh no, he just likes guys more than girls. That doesn't mean he doesn't have any kids that a nice title might not be passed on to. Anyway, I was thinking that..."

scene bg6 with fade

#if using Jezera favour
if event_tmp['using favor'] == 'Jezera':
    show rowan necklace neutral at midleft with dissolve
    show jezera neutral at midright with dissolve

    ro "... so I thought that would be an appropriate reward for his help."

    show jezera happy at midright

    je "Such a simple thing it is to give a title, just say it and it is. I rather like this system that Solensia has come up with, but she does seem far too stringent with who is honored."
    je "I'll perform the ceremony this evening at supper, please make certain that Cla-Bow is in attendance."

    "Rowan bowed to his mistress."

    ro "Of course."

    je "Will there be anything else?"

    ro "Let me see, domestic fees, new hirings, rewards, no we've covered everything."

    je "Excellent, I believe I will take a bath. Should you need me I will be in my chambers."

    hide jezera with dissolve

#if using favour with Andras
elif event_tmp['using favor'] == 'Andras':
    show rowan necklace neutral at midleft with dissolve
    show andras displeased at midright with dissolve

    ro "... so I thought that would be an appropriate reward for his help."

    an "These goblins are quite the strange sort to be so easily satisfied with words. It's by no means how I would have rewarded him, but if you say so I will agree to it. Inform me when it is time to grant the title and I will do so."

    "Rowan bowed to his master."

    ro "Of course."

    an "Is that everything, servant?"

    ro "Hmm, troop upkeep, recruitment, rewards, yes I believe we've covered all official business."

    an "Good, excuse me."

    hide andras with dissolve

#rejoin
show clamin happy at edgeleft with moveinleft

cla "I would say that went rather well. I'll tell my brother the good news, and you'll have a shiny new sword right after the ceremony finishes."
#End event, gain Cla-Min's item with no strings attached.
$ give_item('balasts_brand')
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label helayna_has_been_claimed:
#Helayna has been claimed
#Requirements - Rowan claimed Helayna during assault on Raeve Keep
#High priority event, triggers the week that Helayna was claimed.

scene bg14 with fade

show alexia 2 necklace angry at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

al "Rowan! What is going on? I just saw a naked woman get carried into your room!"

show rowan necklace sad at midleft with dissolve

ro "It was Helayna."

show alexia 2 necklace shocked at midright with dissolve

if (helaynaRelationship == 0):
    al "That noble girl that studied under you a few years back?"

else:
    al "Wait, I remember you telling me about that girl, Duke Raeve's niece was it? Why is she here?"

ro "Yes, that's her. She was corrupted, twisted by Jezera. I protected her from being gangraped, by claiming her as my own."

show alexia 2 necklace happy at midright with dissolve

al "So it isn't what it looks like? She isn't some sex slave for you."

"Rowan found himself freeze up, unable to find the words to answer his wife."

al "That's a relief, I was so worried that-"

ro "Alexia."

"Finally he was able to speak again. The way he said her name silenced Alexia immediately, and a creeping dread began to fill her heart again."

ro "To claim her, I had to do it physically, sexually. Not just because that's what Jezera wanted, but because Helayna had become so crazed that she needed someone, anyone, to fuck her."

"There was no question that this was going to drive a wedge between the two of them, only what form it would take. That all came down to why he'd claimed Helayna for himself."

if (helaynaRelationship == 0):
    menu:
        "A part of Rowan loved Helayna, his best student.":
            $ released_fix_rollback()
            ro "She looked like she was in such pain, someone I'd seen grow under my tutelage into a great young woman. In the moment I needed to make sure that it was me that she gave herself to, not some orc or brute."
            ro "I care about her. I had to protect her."
            show alexia 2 necklace concerned at midright with dissolve
            "For all his noble words, there was one part he left out. Alexia was not to be fooled."
            al "You care about her? Or love her?"
            "Rowan didn’t know how to answer that."
            "A loud cry suddenly came up from inside Rowan's room."            
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "And now you're going to do it again, aren't you? You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia wrapped her arms around her chest while tears streamed down her cheeks."
                al "When I think about all that has transpired since our ordeal began…" 
                "She cut herself off."
                al "I should understand. I should be able to forgive. You were with someone you cared about and you couldn’t control yourself. And yet.."
                al "You’re my anchor and you were sleeping with another woman. Loving another woman. Where’s my anchor now?"
            else:
                "Alexia reached out a placed a hand on his cheek. Tears had started to fall down hers."
                al "My Rowan. My sweet Rowan. What is this place doing to you?"
            #Alexia's relationship with Rowan falls.
            $ change_relation('alexia', -20)

        "Rowan had to protect someone who was in danger in whatever way he could.":
            $ released_fix_rollback()
            ro "I needed to do what I could to save someone, anyone, from what my actions had caused. I'd just helped the twins conquer Reave Keep, I couldn't bear to what what was going to happen!"
            show alexia 2 necklace concerned at midright with dissolve
            "Alexia chuckled softly and sadly."
            al "You’re such a hero. You always have been. More than that, you care about this girl, don’t you? You had to save her, right?"
            ro "Exactly."
            al "But, did you want to fuck with her?"
            ro "What?"
            al "When Jezera told you to sleep her, did you enjoy yourself? Did you want to do it?"
            ro "I had to save her…"
            al "You did. But, sometimes that means you grin and bear it. Something, you tell yourself that you had to, and you really liked it. Did you want fuck her?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    "Rowan straightened up his back and looked Alexia in the eyes. The moment she asked the question, he knew the answer. Still, saying it out loud was going to hurt."
                    ro "I think...I think I did...I had to, but you might be right. I might have liked it."
                "No.":
                    $ released_fix_rollback()
                    "Rowan felt caught in a vice. The moment she asked the question, in a moment he instantly understood there was a true answer and one he had to give."
                    ro "No of course. She was my student. I felt like I was violating her."
                    "Alexia studied his eyes closely."
                    al "I don’t believe you."
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "You're even going to do it again, aren't you?  You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia shivered softly and wrapped her arms around her chest."
                al "Look at me, getting worked up over this. I understand the temptations of this place…"
                al "But, you’re my hope. You’re my lodestar. Look what they’re twisting you into."
            else:
                al "Goddess. What are these fiends doing to you? Every day a little piece of you diminishes."
            #Alexia's relationship with Rowan severely falls, Rowan's guilt is reduced slightly.
            $ change_relation('alexia', -10)
            $ change_base_stat('g', -2)

        "Helayna's begging and Jezera's edging was too much to resist.":
            $ released_fix_rollback()
            ro "I didn't want to do it, I wouldn't have done it, but when Helayna started screaming it was me that she called for. She turned to me for help and, I'm ashamed to admit it, but I wanted to take her."
            show alexia 2 necklace concerned at midright with dissolve
            al "Oh Rowan, what have those monster doing to you?"
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "She turned her head to the side, refusing to meet him eye to eye. Then in a soft voice she added a whisper."
                al "What are they doing to us?"
            else:
                pass
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "My love, darling, please. Please don't give into the darkness. Keep your soul, keep your heart.  Please stay my Rowan."
            #Alexia's relationship with Rowan falls slightly, Rowan's corruption increases.
            $ change_relation('alexia', -3)
            $ change_base_stat('c', 2)

elif (helaynaRelationship == 1):
    menu:
        "Rowan had always wanted more than just friendship with Helayna.":
            $ released_fix_rollback()
            ro "She was one of the few nobles that ever cared about me, who ever put herself on the line for my sake. Who I ever cared about in turn. I hadn't forgotten that, and when I was in the moment and saw what had become of her..."
            ro "I had to protect her."
            show alexia 2 necklace concerned at midright with dissolve
            "For all his noble words, there was one part he left out. Alexia was not to be fooled."
            al "You care about her? Or love her?"
            "Rowan didn’t know how to answer that."
            "A loud cry suddenly came up from inside Rowan's room."            
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "And now you're going to do it again, aren't you? You have to, or it would have been for nothing."
            if alexiaJezeraSex == False and alexiaAndrasSex == False:
                "Alexia wrapped her arms around her chest while tears streamed down her cheeks."
                al "When I think about all that has transpired since our ordeal began…" 
                "She cut herself off."
                al "I should understand. I should be able to forgive. You were with someone you cared about and you couldn’t control yourself. And yet.."
                al "You’re my anchor and you were sleeping with another woman. Loving another woman. Where’s my anchor now?"
            else:
                "Alexia reached out a placed a hand on his cheek. Tears had started to fall down hers."
                al "My Rowan. My sweet Rowan. What is this place doing to you?"
            $ change_relation('alexia', -20)

        "Rowan had to protect someone who was in danger in whatever way he could.":
            $ released_fix_rollback()
            ro "I needed to do what I could to save someone, anyone, from what my actions had caused. I'd just helped the twins conquer Reave Keep, I couldn't bear to what what was going to happen!"
            show alexia 2 necklace concerned at midright with dissolve
            "Alexia chuckled softly and sadly."
            al "You’re such a hero. You always have been. More than that, you care about this girl, don’t you? You had to save her, right?"
            ro "Exactly."
            al "But, did you want to fuck with her?"
            ro "What?"
            al "When Jezera told you to sleep her, did you enjoy yourself? Did you want to do it?"
            ro "I had to save her…"
            al "You did. But, sometimes that means you grin and bear it. Something, you tell yourself that you had to, and you really liked it. Did you want fuck her?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    "Rowan straightened up his back and looked Alexia in the eyes. The moment she asked the question, he knew the answer. Still, saying it out loud was going to hurt."
                    ro "I think...I think I did...I had to, but you might be right. I might have liked it."
                "No.":
                    $ released_fix_rollback()
                    "Rowan felt caught in a vice. The moment she asked the question, in a moment he instantly understood there was a true answer and one he had to give."
                    ro "No of course. She's my friend. I felt like I was violating her."
                    "Alexia studied his eyes closely."
                    al "I don’t believe you."
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "You're even going to do it again, aren't you?  You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia shivered softly and wrapped her arms around her chest."
                al "Look at me, getting worked up over this. I understand the temptations of this place…"
                al "But, you’re my hope. You’re my lodestar. Look what they’re twisting you into."
            else:
                al "Goddess. What are these fiends doing to you? Every day a little piece of you diminishes."
            #Alexia's relationship with Rowan severely falls, Rowan's guilt is reduced slightly.
            $ change_relation('alexia', -10)
            $ change_base_stat('g', -2)

        "Helayna's begging and Jezera's edging was too much to resist.":
            $ released_fix_rollback()
            ro "I didn't want to do it, I wouldn't have done it, but when Helayna started screaming it was me that she called for. She turned to me for help and, I'm ashamed to admit it, but I wanted to take her."
            show alexia 2 necklace concerned at midright with dissolve
            al "Oh Rowan, what have those monster doing to you?"
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "She turned her head to the side, refusing to meet him eye to eye. Then in a soft voice she added a whisper."
                al "What are they doing to us?"
            else:
                pass
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "My love, darling, please. Please don't give into the darkness. Keep your soul, keep your heart.  Please stay my Rowan."
            #Alexia's relationship with Rowan falls slightly, Rowan's corruption increases.
            $ change_relation('alexia', -3)
            $ change_base_stat('c', 2)

else:
    menu:
        "Rowan had to protect someone who was in danger in whatever way he could.":
            $ released_fix_rollback()
            ro "I needed to do what I could to save someone, anyone, from what my actions had caused. I'd just helped the twins conquer Reave Keep, I couldn't bear to what what was going to happen!"
            show alexia 2 necklace concerned at midright with dissolve
            "Alexia chuckled softly and sadly."
            al "You’re such a hero. You always have been. More than that, you care about this girl, don’t you? You had to save her, right?"
            ro "Exactly."
            al "But, did you want to fuck with her?"
            ro "What?"
            al "When Jezera told you to sleep her, did you enjoy yourself? Did you want to do it?"
            ro "I had to save her…"
            al "You did. But, sometimes that means you grin and bear it. Something, you tell yourself that you had to, and you really liked it. Did you want fuck her?"
            menu:
                "Yes.":
                    $ released_fix_rollback()
                    "Rowan straightened up his back and looked Alexia in the eyes. The moment she asked the question, he knew the answer. Still, saying it out loud was going to hurt."
                    ro "I think...I think I did...I had to, but you might be right. I might have liked it."
                "No.":
                    $ released_fix_rollback()
                    "Rowan felt caught in a vice. The moment she asked the question, in a moment he instantly understood there was a true answer and one he had to give."
                    ro "No of course. She's my friend. I felt like I was violating her."
                    "Alexia studied his eyes closely."
                    al "I don’t believe you."
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "You're even going to do it again, aren't you?  You have to, or it would have been for nothing."
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "Alexia shivered softly and wrapped her arms around her chest."
                al "Look at me, getting worked up over this. I understand the temptations of this place…"
                al "But, you’re my hope. You’re my lodestar. Look what they’re twisting you into."
            else:
                al "Goddess. What are these fiends doing to you? Every day a little piece of you diminishes."
            #Alexia's relationship with Rowan severely falls, Rowan's guilt is reduced slightly.
            $ change_relation('alexia', -10)
            $ change_base_stat('g', -2)

        "Helayna's begging and Jezera's edging was too much to resist.":
            $ released_fix_rollback()
            ro "I didn't want to do it, I wouldn't have done it, but when Helayna started screaming it was me that she called for. She turned to me for help and, I'm ashamed to admit it, but I wanted to take her."
            show alexia 2 necklace concerned at midright with dissolve
            al "Oh Rowan, what have those monster doing to you?"
            if alexiaJezeraSex > 0 or alexiaAndrasSex > 0:
                "She turned her head to the side, refusing to meet him eye to eye. Then in a soft voice she added a whisper."
                al "What are they doing to us?"
            else:
                pass
            show helayna naked aroused behind bg14
            hel "Rowan! I need you, where are you?! Please, fuck me...."
            #alexia cry
            al "My love, darling, please. Please don't give into the darkness. Keep your soul, keep your heart.  Please stay my Rowan."
            #Alexia's relationship with Rowan falls slightly, Rowan's corruption increases.
            $ change_relation('alexia', -3)
            $ change_base_stat('c', 2)

"Another loud cry of frustration filled the air from Rowan's chamber."

ro "Alexia, I need to go to her.  If I don't, she'll probably go find someone or something else to try and deal with her uncontrollable lust."

#If Alexia was sleeping in Rowan's room, she tells him that she's moved out.
if not alexiaSeparateRoom:
    al "Then I'm going to move out. I don't want to see Helayna, I don't want to see you breaking our vows with her, even if it is to protect her. I'm sorry, darling."
    #Alexia is set to be sleeping separate.
    $ alexiaSeparateRoom = True

#rejoin
al "Go, deal with Helayna. I need some time to myself right now."
$ rowan_shares_room_with_helayna = True

#Helayna Sex
scene bg9 with fade
show helayna naked aroused at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

ro "Hello Helayna."

"Rowan entered into his room and found Helayna sprawled out on his bed, furiously fisting her womanhood in a desperate effort to get off. When he spoke to her, she froze up for a second and then started frantically looking around the room to find him."
"When she did, her unfocused eyes seemed to clear for a moment and she cried out."

hel "Rowan!  My [helaynaTitle]!  Please, please help me...."

"Then she once again became unfocused. She reorientated herself, presenting her puffed up womanhood to him as it drooled down onto his blankets incessantly."

hel "I... I need you inside me, I need you to fuck me, again and again...."

ro "It hurts to see you like this, you aren't yourself."

"In spite of his words, the hero was getting aroused at the display. Jezera wasn't here to egg him on this time, but there was no denying that some part of him wanted to claim Helayna again. He only hoped that he wouldn't be corrupted to his core by that part of him."

show rowan necklace naked at midleft with dissolve

"The hero shed his clothing and stepped towards Helayna as she mewled in excitement."

hel "Yes! Come to me! Fill meeee!"

ro "You might not understand me now, but know that I do this to protect you from yourself."

#CG1, Rowan fucking Helayna
scene cg112 with fade
pause 3
"As he said that, he climbed up onto the bed. A moment later, he was in position to start fucking her. He hesitated for a moment, letting his hand run over Helayna's smooth skin and over the shape of her soft cheeks and curve of her breasts."
"This wasn't for Helayna, it was for him. The fallen noblewoman only wanted him to fuck her, hard and fast. That's why, after that moment ended, he took her as she wanted, no needed, him to do."
"A loud cry of pleasure erupted as Rowan penetrated Helayna for the second time. Her passage was well and truly soaked, and it quivered and tensed around the man's shaft uncontrollably."
"He didn't wait for her to adjust to his violation of her, there was no need, instead Rowan just bucked against her body, making a loud wet slapping as their hips met again and again. Each of his thrusts was met by another sharp gasp or babble from Helayna."
"Soon the sensations were too much to her and her eyes rolled back in her head. Knowing that the worst thing he could do now was slow down, or worse - stop, the man took a firm grip of the woman's hips, grit his teeth, and kept fucking her."

#CG1 variation - cum
scene cg112 with sshake
scene cg112 with sshake
scene cg113 with flash
pause 3
"The frantic pace meant that orgasm would come swiftly, though Rowan grit his teeth through it and kept fucking Helayna right through it, in spite of his discomfort. One time wouldn't be enough for her, he needed to keep going and going until her fire was at least partially quenched."

#CG1 variation - super cum
scene cg113 with sshake
scene cg113 with sshake
scene cg114 with flash
show rowan necklace naked behind cg114
show helayna naked aroused behind cg114

"After cumming inside her three more times, and leaving quite a mess, Rowan was finally unable to go any more. Helayna seemed to want more afterwards, but didn't sound quite so desperate."
"Hopefully she'd be satisfied for now and wouldn't have to seek out help from someone else in the castle. The hero shuddered at the thought."

ro "I wish I could do more for you. Will you be able to last a week while I'm away though? Can I really just leave you in here?"

hel "Rowan... it's fine. As long as I know you'll come back to me, I can last."

"Something of her seemed to have surfaced, maybe Helayna was still in there, deep down?"

ro "I hope so. I'll watch over you whenever I can, whenever my duties don't take me away from you. It's the only way I can protect you."

hel "Thank you, thank you. I will do what I can to help, I'm still a knight."

ro "(Oh Helayna....)"

#Rowan gains corruption.  End scene.
$ change_base_stat('c', 2)

if NTR == True:
    jump AfterArgument
    
else:

    return

label AfterArgument:
    
scene bg7 with fade

show alexia 2 necklace concerned at midright with dissolve

al "(I can’t believe Rowan would do this to me. It is one thing to be unfaithful, but to bring this woman into our bed?)"

"The redhead had only recently managed to stop herself from crying, despite the argument with her husband happening hours ago. She now found herself back on the verge of tears."

al "(I know he was only trying to protect her, but could he really not see how that would hurt me?)"

play sound "music/SFX/door knock.ogg"
pause 1

"Her thoughts were interrupted by a knock at the door. Who could it be? Had Rowan come to apologize for the events earlier? Probably, but she wasn’t ready to see him, she was still too raw, and already felt as if she were about to start bawling again."

play sound "music/SFX/door knock.ogg"
pause 1

show andras happy behind bg7

an "Hello? Alexia? It is Andras, I just wanted to check that you are okay."

menu:
    "Don’t answer the door.":
        $ released_fix_rollback()
        "The demon must have taken the hint because he left without any further prodding. Alexia was glad, as she didn’t know if she could deal with him and whatever nonsense he was up to in her current state."
        "Still trying not to cry she lay on the bed, closed her eyes, and tried not to think about anything."
        return
        
    "Answer the door.":
        $ released_fix_rollback()
        show alexia 2 necklace concerned at edgeleft with moveoutleft
        "She opened the door just enough to converse, but not enough for it to seem inviting. The demon stood there, waiting, with a smile on his face."
        al "What do you want Andras? I’m not in the mood."
        an "So I hear, I just wanted to drop by and make sure you were okay, as I said."
        al "I’m {i}sure{/i} you did."
        an "And what is that supposed to mean?"
        al "If you cared about my well being, you wouldn’t have kidnapped me in the first place." 
        an "Did we lock you up in the dungeons? Have you been harmed in any way?"
        al "No, but-"
        an "Have you been forced to do anything against your will?"
        al "I suppose not…"
        an "I take time out of my busy schedule to come and check on you, because I’ve heard you were upset, and this is what I get?"
        al "I’m sorry, I’ve just had a rough day."
        an "It is perfectly fine, there’s no need to apologize. Anybody would be upset in your position, and if lashing out at me makes you feel better, I don’t mind."
        al "No, I shouldn’t be taking it out on you. You aren’t the one who has done anything, so it isn’t fair to you."
        an "Would you like to talk about it?"
        menu:
            "Yes.":
                $ released_fix_rollback()
                jump argumentSexScene
                
            "No.":
                $ released_fix_rollback()
                al "Thanks for the offer, but it is has been a long day, and I just need to rest."
                an "Okay, I won’t push you. If you ever want to talk about it, let me know. I’ll let you rest."
                al "Thank you Andras, and sorry again."
                an "Think nothing of it."
                "The demon left, and Alexia lay on the bed, closed her eyes, and tried not to think about anything."
                return
            
label argumentSexScene:

al "It is very kind of you to offer. I think it might help, please, come in."

scene black with fade
scene bg7 with fade
show andras happy at midleft with dissolve
show alexia 2 necklace happy at midright with dissolve

an "… and then the maid fell backward, and the chamberpot went flying, hitting Jezera. I thought she was going to skin the poor woman alive, but she just screamed and ran off."

"A loud giggle escaped from the mouth of the redhead."

al "I can’t really imagine Jezera as a girl, I suppose you don’t really think of demons being children."

an "Probably for the best, she was worse than she is now!"

"Alexia giggled again, before stopping herself."

al "Now, that is not a very nice thing to say about your sister."

"The demon pulled a purposely exaggerated face to feign exasperation, before a smile returned to his face."

an "I’m sure she’d be happy to know she has such a staunch defender."
an "Anyway, it has gotten quite late and this bottle is empty, I should let you get your beauty sleep."

"The demon stood, empty bottle in hand."

an "I hope I was able to cheer you up a little, or at the very least take your mind off your troubles for a little while"

scene cg20 with fade
show andras happy behind cg20
show alexia 2 necklace happy behind cg20
pause 3

"She stood now, to thank him."

al "Thank you Andras, it did help. Sometimes you just need a laugh, I think."

an "If you ask me though, I think your husband is a fool."

if all_actors['alexia'].flags['andras_influence'] > 0:
    jump argumentSex1

else:
    scene bg7 with fade
    show andras happy at midleft with dissolve
    show alexia 2 necklace happy at midright with dissolve
    al "You’d better go now, I need to lie down."
    an "Okay. Goodnight Alexia."
    al "Goodnight."
    hide andras with moveoutleft
    return
    
label argumentSex1:
    
scene cg21 with fade
show andras happy behind cg21
show alexia 2 necklace happy behind cg21
pause 3 

"She didn’t know if it was the alcohol, the fact he was being so nice to her, or even subconscious anger at Rowan for his actions earlier, but now face to face with the demon she leaned in."
"First their lips met, and then she opened her mouth to allow his tongue to make it’s forceful entry."

#Alexia on Andras lap, facing, french kissing
scene black with fade
show andras happy behind black

"Andras sat down on the bed, and pulled the much smaller woman down onto his lap with ease. The movement was strong and forceful, completely different from how her husband treated her; almost as if he were moving an object and not a person."
"Now, facing him, she resumed french kissing him. His mouth was hot and still tasted of wine, and their tongues pressed together, snaking side to side as saliva co-mingled."
"It was almost as if she were lost in a haze, until she felt that the demon’s substantial member had awoken and was pressing against her."

if all_actors['alexia'].flags['andras_influence'] > 1:
    jump argumentSex2

else:
    scene bg7 with fade
    show alexia 2 necklace concerned at midright with dissolve
    show andras happy at midleft with dissolve
    al "No, I can’t. Andras, please stop."
    an "Are you sure?"
    al "Yes, please… I’m just upset, and a little drunk."
    an "Okay then, I’ll leave you be."
    al "Thank you. I’m sorry, I’m just not feeling like myself."
    an "Say no more."
    hide andras with moveoutright
    "The demon left, and Alexia lay on the bed, closed her eyes, and tried not to think about anything."
    return

label argumentSex2:

an "Turn around."

#Alexia on Andras lap, reverse cowgirl (crotch to crotch), Andras gropes her breasts 
scene black with fade
show andras happy behind black
show alexia 2 necklace aroused behind black

"The redhead did what he said without reply, and now sat with her back against his chest. He reached down with one clawed hand and roughly groped her breast, causing her to let out a soft moan."
"Happy with the reaction, he ran his hand over her erect nipple, teasing her by lightly grazing it."
 
al "No fair…"

"As a response to the lack of stimulation, Alexia began to grind on the demon’s lap, her sodden cunt rubbing against his hard cock through her soaked panties."

#neck kiss variant
scene black with fade
show andras happy behind black

"Andras leaned in and began to softly kiss her neck, while continuing to grope her breasts."
"As he pinched her nipple, she let out a sharp cry, and increased her grinding to almost a bucking, trying to get off from the friction between their loins."

an "Take off your panties."

if all_actors['alexia'].flags['andras_influence'] > 3:
    jump argumentSex3

else:
    scene bg7 with fade
    show alexia 2 necklace concerned at midright with dissolve
    show andras happy at midleft with dissolve
    al "No, I can’t. Andras, please stop."
    an "Are you sure?"
    al "Yes, please… I’m just upset, and a little drunk."
    an "Okay then, I’ll leave you be."
    al "Thank you. I’m sorry, I’m just not feeling like myself."
    an "Say no more."
    hide andras with moveoutright
    "The demon left, and Alexia lay on the bed, closed her eyes, and tried not to think about anything."
    return

label argumentSex3:

scene cg115 with fade
show andras happy behind cg115
show alexia 2 necklace aroused behind cg115

"Again she complied with his order without a reply, she was desperate to get off now, and damn the consequences! She quickly whipped her underwear off, and the demon slid one of his hands down to her wet snatch."
"Without waiting on ceremony, he inserted two fat fingers into her and began to slowly frig her."
"Due to his abnormal size, it was like being fucked by an average size cock, and she let out a long moan as the slippery fingers slid in and out between her lips."

al "uhhhhh…"

"Andras grinned, and began to speed up, causing her moans to grow louder and longer."
"He slipped in a third finger, stretching her cunt, to which she gave a squeal of approval, and began to make come hither movements, stimulating her g-spot."
"Before long, she couldn’t take anymore."

al "Nnnnnn!! Oh gods, I’m going to cum!"

scene cg115 with sshake
scene cg115 with sshake
scene cg116 with flash
show alexia 2 necklace aroused behind cg116

"Deftly he quickly removed the fingers, and began to rub her clit. The stimulation was almost too much for Alexia, she felt as if she were going to go crazy."
"It didn’t take long for her to climax, and as she did she let out a scream, and squirted. A stream of clear liquid arced through the air, as she slumped back against the demon’s muscular chest, exhausted."

al "Wow, that’s never happened before…"

scene black with fade
"Suddenly tired, she closed her eyes. Sometime afterwards, she felt strong arms pick her up and lie her on the bed. She felt the wet brush of lips against hers, before she drifted off to sleep."

$ alexiaUnfaithful = True
$ alexiaAndrasSex =+ 1
$ all_actors['alexia'].corruption += 3
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label delf_dipping:
#Delf Dipping
#Pre requisites - Breeding pit / met Draith
#should probably occur within a few weeks of building

scene bg25 with fade

"Whilst doing his regular rounds about the castle, Rowan heard raised voices from the breeding pits. He didn't have to draw too close to recognise the female party: Jezera, in full, strident form."

show jezera displeased at midright with dissolve
show draith neutral at midleft with dissolve

je "...not good enough. We give you shelter and succour, more than a male dark elf deserves, and you repay us with laziness and insubordination! Where are my legions of wargs, worm?"
je "Where are the vast kennels of driders that you promised us?"

show rowan necklace neutral at edgeleft with moveinleft

"Rowan entered the main chamber to find Draith stood on the viewing dais, wringing his hands, staring at a floor he clearly wished would swallow him up. Jezera had one hand on her hip, the other waving disgustedly at the mostly empty pits."

dra "S-sorry, Mistress. I... I did say it was going to take time..."

je "If I had a piece of gold for every time I heard that, I could have bought the six realms by now! You will work your snivelling little ass off every hour of every day from now on, or by my own father I shall march you back to the Undersisters myself!"

ro "That's enough. What is to be gained from yelling at him like that?"

je "Huh? Oh, it's you. Well, of course {i}you{/i} would encourage such weakness. Go ahead Rowan, coddle the sissy. Ultimately it will be you who will be paying for his failures!"

hide jezera with moveoutright

"Jezera strode out of the room, leaving Rowan alone with the lithe, dusky male."

dra "Th- thank you. I hate it so much when she shouts at me. It makes me remember how - how it was in Cerandil. Th- the cold... the morning shriek and the bite of the whip..."

ro "Are you taken back to that whenever anybody gives you orders?"

dra "Oh no! When you do it, it feels good. Your voice is so kind and- and warm. And strong. Like the person it comes from."

"The dark elf had drawn closer to Rowan as he talked, as if the human was indeed a source of warmth in this dank underchamber. His hairless, delicate face shone with naked adoration."

menu:
    "Fuck him.":
        $ released_fix_rollback()
        $ rowanGaySex += 1
        "Had Rowan ever felt attracted to males before the demons installed him here? He couldn't recall any occasion when he'd looked at another man's body and felt heat draw inexorably into his crotch like it did now, certainly not when he had been in Rosaria's service."
        "But the dark elf was so lithe, so delicate in appearance, so sultrily exotic in dress and shade, that to compare him to a fighting human male such as himself seemed ridiculous."
        "And when Rowan looked into Draith's eyes and saw the naked hero worship and arousal that shone there, the temptation became far too much."
        "He stepped forward and drew the little guy into his arms commandingly. Draith gave a short gasp, giddy joy flickering in his tone as Rowan nakedly enjoyed the supple feel of the elf's flesh, plaining his hand down his slim back."
        ro "You belong to me, beastmaster. Not the Undersisters; not the demons. Me, and me alone. So pay no attention to them. Understand?"
        dra "I - yes, sir. Absolutely."
        "Draith exhaled, moulded his frame into Rowan's as the human's touch roamed down further, squeezing his delightfully pert ass."
        dra "I- I'm very good with all sorts of beasts, master. Perhaps there's one in particular you'd like to show me?"
        "Rowan laughed at this, making purple bloom over Draith's china-bone cheeks. Still, he stepped away from the dark elf and stepped out of his clothes, ripping away his breeches to allow his thick, hot erection to loll outwards, never taking his eyes off the subby, smaller male."
        #CG1 - Draith lubes Rowan's dick
        scene black with fade
        show draith happy behind black
        dra "Yes... I think I might have something for a big, powerful monster like that."
        "He turned, deliberately flaring his narrow hips in order to swing his cute apple-shaped backside over to a bottle-cluttered shelf above his desk. He withdrew a vial filled with clear fluid, removed the stopper and pooled the unguent onto his hands, rubbing it into his palms."
        "Heart beating, Rowan sat himself down on a bench and opened his thighs. Draith smiled at him shyly as he slowly descended onto his knees in front of the human."
        "Rowan sighed, and then groaned with pleasure as the dark elf wrapped his fingers around the human's cock, slithering his slender grip up and down his shaft, working the warm, coating oil into it until it was hard as oak and sang with pleasure."
        "Draith smiled and laughed, eyes darting up to Rowan's face and then batting submissively away again every time he drew a gratified sound out of the human; the act of giving pleasure seemed to give him genuine pleasure as well."
        "Lust throbbed through Rowan, enflaming his senses as the dark elf slid the long, nimble fingers of one hand in deeper, jerking his cock assiduously whilst cupping his balls, polishing every inch of Rowan's sex in warm, slick oil."
        #CG2 - Draith assfuck from behind
        scene black with fade
        #draith aroused
        show draith happy behind black
        "Feral lust gripping him now, Rowan rose up and grabbed the smaller male, turning him around and bending him over the bench, drawing a surprised squeal out of the submissive."
        "He pulled Draith's tight-fitting breeches down and admired his pert, naked ass for a long moment, slapping his urgently erect, oil-soaked cock between its crack as he did. Draith looked at him over his shoulder, color high in his cheeks."
        dra "Please go slow first, sir... then hard."
        "Rowan drew his hips back, allowing his erection to slither downwards meaningfully, lining himself up with Draith's cute little rose, enjoying the twitch and expectant inhalation it brought out of the dark elf."
        "Then he pushed forward, slowly penetrating it, gloving his cock-head in wonderful, clinging warmth, carefully working him loose with slow movements of his hips."
        "Draith gasped and clutched at the wood beneath him, a chorus of cute little grunts and huffs... but he never bade Rowan to stop."
        "Soon the human found himself easily sliding his length deep into the elf's tight tunnel."
        "Draith's own cock, as slender and cute as its owner, jerked in response to Rowan's efforts, wagging like a puppy's tail as the human pushed himself home into the boy-slut's tight, oiled warmth again and again."
        "Genuine excitement and slight giddiness energised Rowan; he was a complete novice to this, but his roughness seemed only to excite the dark elf, moaning at him to keep going, pulling Rowan’s hand to his flat chest and small, erect nipples."
        scene cg72 with dissolve
        pause 2
        "Animal lust overcame Rowan, and he suddenly grabbed Draith around the hips, hoisted him into the air and then firmly sat him down on his cock, thrusting into the dark elf’s opened asshole from below."
        scene cg73 with dissolve
        pause 2
        show cg73 with sshake
        show cg73 with sshake
        show cg74 with flash
        pause 2
        show cg74 with sshake
        show cg74 with sshake
        show cg75 with flash
        pause 2
        show draith happy behind cg75
        "Draith cried out with joy, slim arm thrown around Rowan's neck, his own dick gleefully erect, his tone of ecstasy climbing down to a coo of deepest satisfaction when the bigger human came with spectacular force, fluming a guttering fountain of cum deep into his gaping hole."
        "The dark elf's fingers curled up his shoulder, his silky hair tickling Rowan's jaw, nuzzling him happily."
        dra "I hope you will come by often, sir. A big, energetic beast like that needs a lot of care... and there's nobody better trained to give it than me."
        "With his impulsive ardour bitten, Rowan's thoughts now sank back to Alexia, somewhere in this very keep and blissfully unaware that her husband had just cheated with another man."
        "Still, he did not betray his feelings of guilt and uneasiness to Draith, who stroked his arm trustingly as the human dressed and departed."
        scene bg14 with fade
        show jezera happy at midright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        je "Oh, Rowan..."
        "That taunting, teasing voice froze Rowan in the corridor cold. He slowly turned to face the female demon, leaning against the wall outside the dungeon he'd just exited."
        ro "What are you doing? Were you listening in?"
        je "Of course! I didn't set that succulent little twink to all but fall into your arms just to miss you fucking him senseless. Mmm... I must say Rowan, beneath that dour exterior of yours, you are quite the surprise."
        je "So passionate and impetuous and energetic. You need to let that side of you come out more often."
        ro "...you were cruel to Draith just so I would be nice to him."
        je "Of course! I wouldn't be nasty to that slutty piece of violet sweet for no reason. Who do you take me for, my brother? But I couldn't have done it if you didn't already have the lust for it."
        je "Two handsome boys rutting each other for my entertainment... it was even better than I was anticipating."
        "She slid her claws along the insides of her thighs, sighing with contentment."
        je "I will remember this, Rowan. Those who entertain me are richly rewarded... in all sorts of ways."
        hide jezera with moveoutright
        "She left with a malicious titter. Waves of conflicting emotion washed through Rowan. The guilt he'd felt for cheating on Alexia was all the more gnawing for the knowledge that Jezera had deliberately set him up to it."
        "On the other hand... the sex had been undeniably good, and it had  certainly comforted that sensitive little beastmaster of his. And perhaps this favour he had inadvertently earned off Jezera could be turned to good purpose?"
        #gain small guilt amount of guilt, gain Draith relationship, +1 Jezera favour
        $ change_base_stat('g', 1)
        $ change_relation('draith', 3)
        $ change_favor('jezera', 1)
        $ rowan_draith_sex = True
        return

    "Give him a manly hug.":
        $ released_fix_rollback()
        show rowan necklace happy at edgeleft with dissolve
        "Rowan strode across and gripped the slight dark elf firmly in his arms, clapping him on the back a couple of times. He hoped with each strong slap he made crystal clear that brotherly, lordly affection was what was being expressed here."
        ro "You are my subject. Not the Undersisters; not the demons. Pay no attention to them - I know you have the potential to be a great beast-master, given enough space and time. I shall see to it that you have both."
        "Draith hugged him back tightly. Rowan presumed the message had gotten through - at least for now - because this time the supple little guy made no attempts to unsubtly hump him."
        show draith happy at midleft with dissolve
        dra "Thank you, sir. As long as you're - you're around... my hands won't shake. I'll do my best to fill these pits with creatures loyal to your name... and your name only."
        hide rowan with moveoutleft
        "Draith smiled at him shyly as Rowan released him and strode out of the Breeding Pits."
        scene bg14 with fade
        show jezera displeased at midright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        je "Hell and beyond Rowan, are you always this boring?"
        "That taunting, teasing voice froze Rowan in the corridor cold. He slowly turned to face the female demon, leaning against the wall outside the dungeon he'd just left."
        ro "What are you doing? Were you listening in?"
        je "Of course! I'd set that succulent little twink to all but fall into your arms... I was sat here waiting to lap up you two getting hot and heavy with each other... and what to do you do? Spurn the opportunity!"
        je "When are you ever going to loosen up some, you sexless grump?"
        ro "...you were cruel to Draith just so I would be nice to him."
        je "Yes! I wouldn't be nasty to that slutty piece of violet sweet for no reason. Who do you take me for, my brother? Pshh, but it was all for naught, thanks to you. I'll have to find some other form of entertainment."
        je "I wonder what your wife is up to?"
        ro "Stay away from her!"
        hide jezera with moveoutright
        "The female demon tittered, a sly, lingering look her only response as she slinked off."
        "Rowan was left feeling conflicted - he felt glad that he'd extended kindness to his dark elf servant and foiled Jezera's perversions, but inadvertently getting into the demon’s bad books did not bode well."
        #Guilt slightly down, small increase to Draith relationshop, -1 Jezera favour if possible
        $ change_base_stat('g', -1)
        $ change_relation('draith', 2)
        $ change_favor('jezera', -1)
        return

    "Tell him to stand up for himself.":
        $ released_fix_rollback()
        ro "Draith, I'm not always going to be around to stop others picking on you. You're not a slave to the Undersisters anymore, but nobody in this castle suffers the weak. Frankly, you're going to have to grow a harder skin if you're going to be one of my taskmasters."
        ro " Tell Jezera, and Andras for that matter, to get gone if they talk to you like that. If they have a problem, they can take it to me."
        "Draith looked thoroughly miserable, and Rowan didn't like the way he shrank away and wrung his hands in the exact same way he had when the demon had been bad-mouthing him."
        "Still, once Rowan had finished, the dark elf set his delicate jaw and made an effort to look his commander in the eye."
        dra "I understand, s-sir. I'll do my best to let them know they can't- can't talk to me that way."
        hide rowan with moveoutleft
        "Rowan gave him a firm nod, and strode out of the Breeding Pits."
        scene bg14 with fade
        show jezera displeased at midright with dissolve
        show rowan necklace neutral at midleft with moveinleft
        je "Hell and beyond Rowan, are you always this boring?"
        "That taunting, teasing voice froze Rowan in the corridor cold. He slowly turned to face the female demon, leaning against the wall outside the dungeon he'd just left."
        ro "What are you doing? Were you listening in?"
        je "Of course! I'd set that succulent little twink to all but fall into your arms... I was sat here waiting to lap up you two getting hot and heavy with each other... and what to do you do? Spurn the opportunity!"
        je "When are you ever going to loosen up some, you sexless grump?"
        ro "...you were cruel to Draith just so I would be nice to him."
        je "You weren't nice to him at all! Being nice to that slutty piece of violet sweet would have been to give him the good, hard ass-fucking he was practically begging for. And you've managed to disappoint us both, because now I'm going to have to find some other form of entertainment."
        je "I wonder what your wife is up to?"
        ro "Stay away from her!"
        hide jezera with moveoutright
        "The female demon tittered, a sly, lingering look her only response as she slinked off."
        "Rowan scowled. Somehow, an honest attempt to get one of his servants to stand on his own two feet and gone very badly indeed."
        #-1 Jezera favour if possible
        $ change_favor('jezera', -1)
        return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label greyhide_s_table_manners:
#Greyhide's table manners
#Follow up from Drinking Buddies if player chose to introduce Greyhide to Alexia, and if Alexia and Greyhide have not met before.

scene bg27 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

al "... it sounds like this Greyhide has had a difficult life."

ro "Yeah. Sorry I didn't tell you more about him before I roped you into this."

show alexia 2 necklace happy at edgeleft with dissolve

al "Oh relax. It's no trouble for me. I actually found it fun to prepare a huge vegetarian meal. I hope he likes it."

"She didn't mention that she was also curious about how big minotaurs actually were."
"There was a double meaning to that from stories that Alexia had heard from the other villagers which her mind had unfortunately permanently associated with minotaurs in her mind."

#greyhide happy
show greyhide neutral at skorright with moveinright

"The couple's conversation ended as the large minotaur that they were hosting for dinner today made his rather blunt entrance into the castle's dining room."

show alexia 2 necklace concerned at edgeleft with dissolve

gh "Hello friend Rowan."

show rowan necklace happy at midleft with dissolve

ro "Hello Greyhide. May I present to you my wife, Alexia. Alexia, this is Greyhide, the castle forgemaster."

"Alexia felt very nervous now that she actually confronted with Greyhide."
"She'd never seen a minotaur before, their great size and bestial appearance left quite an impression, far more than what childish rumors would have left her with."

al "A... pleasure to m-meet you."

show rowan necklace neutral at midleft with dissolve

gh "I thank you for the honor of meeting you."

"While Greyhide was apparently oblivious to the discomfort his presence was causing to Alexia, she was visibly shaking now. Her husband did take notice, and reached out to take one of her hands into his own, his warm sure grip quickly helping her get under control again."

show alexia 2 necklace neutral at edgeleft with dissolve

al "Thank you."

"She whispered her thanks to him under her breath, as he led her back to the table they'd laid with food and sat down together. Then Rowan indicated the place opposite."

show rowan necklace happy at midleft with dissolve

ro "Please, join us."

"With an appreciative nod, the minotaur did so."

scene cg105 with fade
show rowan necklace neutral behind cg105
show greyhide neutral behind cg105
show alexia 2 necklace neutral behind cg105
pause 3

"No sooner had Greyhide taken his seat, he set into the food in front of him with a vengeance. He grabbed large chunks of the salads around him and stuffed them into his mouth, without bothering with a plate or utensils."
"He wasn't eating very fast, but he was being efficient."
"Alexia was appalled by the complete lack of table manners or restraint that the minotaur showed in consuming the meal. She sat there in shock for several moments, until Rowan politely asked her to pass him the water, she didn't seem to notice."

ro "Alexia? Alexia?"

"At this point, Greyhide also noticed that the red haired woman was staring at him.  He swallowed what was in his mouth, then spoke."

gh "Yes? Is there something troubling you? Worry not about me, this food is very good, far better than perhaps I have ever eaten in my life."

al "Oh, thank you."

"The minotaur smiled, then resumed eating again."
"Rowan whispered in Alexia's ear."

ro "Please try not to let his manners bother you, he's never learned to be polite before."

"The woman knew that she was being unreasonable, but she couldn't help it. The way he let the juices of fruit dribble down the side of his face, the way he'd dig through the leaves in the bowl... she tried to focus on her own food and ignore Greyhide for now."
"Rowan made a few attempts at small talk, but Alexia was focusing so hard on not looking at Greyhide that she didn't pay much attention to what was said or what was happening."
"That was until she realized that an orc soldier had approached the table and was speaking hurriedly to Rowan."

scene bg27 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace concerned at edgeleft with dissolve
show greyhide neutral at skorright

al "Did something happen?"

ro "A small emergency, I'm afraid. I'm really sorry about leaving you now, but I assure you that Greyhide won't harm you. I'll try to be back as soon as I can."

al "Alright."

hide rowan with moveoutleft

"Rowan rose up from the table and joined the orc soldier, heading towards another part of the castle. This left Alexia with Greyhide, whom she noticed now had stopped eating and was looking at her."

gh "Do I frighten you?"

al "Well, a little. I'm sorry, I know it's silly but you're so much bigger than me and I've heard stories about minotaurs and their brutality...."

"The bull raised a hand to stop her."

show alexia 2 necklace neutral at edgeleft with dissolve

gh "Think nothing of it. I do not blame you, my brethren are brutal beasts. I came here to escape that life, it would be foolish for someone so much smaller than myself to not be wary."

"His voice was strong and deep, but with a slight rasp to it. Alexia studied him and noticed that the minotaur seemed very relaxed, which set her mind at ease somewhat as well. While she considered him, Greyhide picked up a tomato and studied it."

gh "At home, the food we have to live on are small tough bushes and the grasses that grow on cliffs. This is so, soft, so, fresh. It tastes like you look, lovely Alexia."

show alexia 2 necklace angry at edgeleft with dissolve

al "What?"

"Such a direct comment comment took her aback. Alexia immediately felt insulted by him speaking so crassly to a lady, but she recalled that it was no different than his previous table manners and Rowan had said he'd never been in polite company before."

show alexia 2 necklace neutral at edgeleft with dissolve

gh "This gentleness, tenderness. I have never known these sensations before. I don't deserve the love you and your husband have given me, but I would like to repay your kindness with what I can offer you."

show greyhide neutral at center with moveinleft

"The minotaur stood up, and walked around the long table. He took two flasks of something from his belt and held one out to Alexia."

gh "This is firegrout draft, one of the few things I enjoyed from my old home. Since you have done me the honor of sharing what you love from your home, can I share this with you from mine?"

al "Ah... okay, I mean, yes thank you!"

"Since she'd been so rude to the minotaur up until now, Alexia wanted to make up for lost ground and accepted the drink after only a moment's hesitation."
"When she realized that Greyhide meant to drink it at once, she hurriedly raised the flask to her mouth and downed the contents."

al "Wow, that's not bad!"

"It tasted like a spiced rum or another sweat alcohol and went down very smooth."

gh " I am glad you enjoy it. It is hard to get the ingredients this far away from my home, though this batch seems a bit stronger than usual. Would you like to hear about the Dragon's Tail?"

"Alexia had no objections to hearing about the realm of islands, she was surprised that there were minotaurs living there."

scene black with fade
pause 1
scene bg27 with fade
show alexia 2 necklace aroused at edgeleft with dissolve
show greyhide neutral at center with dissolve

gh "Your husband gave me Rosarian wine when we last spoke. So I wished to find and share the drink my people make. I thought it might also be a good gift such a beautiful woman as thanks for the fine meal you made."

"Alexia glanced at his belt and noted that he had at least two more of the vials."
"The heat of shame at having drank Rowan's gift was quickly erased as a different heat rose up at the sight of a pair of very large balls from the crack between his legs and crotch plate."

al "Whoa, those are some big balls. Are the stories about minotaur cocks true? Are you really over a foot long?"

gh "I know not what stories you have heard. I have not seen another race's balls before. Though I must admit that your soft frame is stirring something within me, something I thought I would never feel again."

"Her blush deepened. Hadn't she just been worrying about crass comments? What had gotten into her?"

al "*hic* (He doesn't care about politeness, and I've been curious all night!  Why am I hesitating now?)"

al "Well, I have sheen a human's balls! {i}I{/i} can tell you the difference."

if (NTR == False):
    jump skipGreyhide

else:
    pass

menu:
    "At that moment, Rowan returned from his task.":
        $ released_fix_rollback()
        label skipGreyhide:
        show rowan necklace neutral at edgeright with moveinright
        ro "I'm very sorry about that, I- Alexia?"
        "The sound of her husband's voice instantly broke Alexia's line of thought."
        al "Oh Rowan! Greyhide hash this amazing drink, what wash it? *hic*"
        ro "Are you drunk Alexia?"
        al "Hey! I only had a little bit."
        "She tried to hold out the small flask, but then she noticed that it seemed to have vanished."
        al "Huh? Where'd that flashk go?"
        gh "You dropped it on the ground... did you not notice?"
        al "Oh, but you shtill have two more there!"
        "She flailed slightly and managed to snag one of the other flasks."
        al "Rowan, darling, try this shtuff!"
        ro "I think it may be best if I get Alexia to bed now. I'm sorry to cut our dinner short, but it would seem that Alexia can't hold her minotaur liquor."
        gh "Very well, I hope she recovers soon. I am sorry if I hurt her."
        ro "I doubt there's going to be any permanent damage if she's still on her feet. Come on, give Greyhide back his flask. Good. Now, let's go Alexia."
        gh "Perhaps this is for the best, I am not feeling myself now either. Have a good night you two."
        hide rowan with moveoutright
        hide alexia with moveoutright
        if alexiaSeparateRoom == True:
            scene bg7 with fade
            show alexia 2 necklace aroused behind bg7
        else:
            scene bg9 with fade
            show alexia 2 necklace aroused behind bg9
        show rowan necklace neutral at midleft with moveinleft
        "As Rowan entered the room, he felt his wife let out a giggle and then start groping him through his pants."
        al "Hmm, got something in your pocket for me?"
        "She groaned out softly while being set down on the bed and helped out of her shoes. Her husband shook his head in confusion."
        ro "Okay... what's with you darling? It isn't like you to act like this, even when drunk."
        "There was no response, just soft steady breathing punctuated with an occasional hiccup."
        ro "Maybe I'll just let you sleep it off and see how you are in the morning."
        return

    "Come on, take off that flap and show me!":
        $ released_fix_rollback()
        jump alexiaGreyhideSex1

label alexiaGreyhideSex1:

scene cg76 with fade
show alexia 2 necklace aroused behind cg76
show greyhide neutral behind cg76
pause 2

"Without hesitation, Greyhide unhitched his breast plate and lifted the entire affair off of his body. Then he plopped down on a nearby table."
"A proper look at his very sizable fuzzy sack was already enough to make Alexia gape, but as she watch his cock emerged as well."

al "Holy moly, that thing's huge! What'sh gotten you so hot, eh big guy?"

gh "Oh, I think you have, soft lady of the fire hair. As surprising as I think it is to discover my desire for you, I would ask you to touch and feel my passion."

al "Touch it?"

"Without thinking, the woman stepped forward and did so. She ran a hand down the fleshy tube and then cupped the furred balls underneath. It felt really funny to her and she giggled."

al "Hehehe so big and ticklish. *hic* Oh, you smell niiiice!"

"Now not only was the firegrout having its way with her head, now minotaur pheromones were making her dizzy and horny as well."

gh "Your touch is very nice. Would you have sex with me? I would like to know what it would be like to be with a woman who is not concerned with dominance."

al "Oh don't be shilly! Theresh no way I could ever fit that thing inside me!"

scene cg77 with dissolve
show alexia 2 necklace aroused behind cg77
show greyhide neutral behind cg77
pause 2

"As he intoned his answer to her, Greyhide reached over and lifted the woman onto his lap. Alexia made no effort to stop him."

gh "That is fine, I am happy as long as you are touching me."

"As the woman started playing with his erection with a dazed smile on her face, the bull started pulling her dress away. The first thing he did was pull off her top, exposing her breasts."

gh "So small, so delicate."

"He pressed one of his thick digits into her breast, the long nail pressing into her nipple. Hard coarse skin met Alexia's much softer skin, sending a shiver up her spine."

gh "Oh, no milk either?"

al "Haha, no I haven't had any kidsh with Rowan yet, no milk for me! That doshen't mean I don't have plansh though! *hic*"

scene cg78 with dissolve
show alexia necklace naked aroused behind cg78
show greyhide neutral behind cg78
pause 2

"Now the minotaur started pulling the dress apart, soon managing to pull the buttons out. Before he got all the way through, he did manage to tear one of the buttons."

gh "Oh, I am afraid I just damaged your dress."

al "Don't worry about that! I can fix it later.  Right now, I want to play with thish fucking amazing dick!"

"With both arms wrapped around his shaft, Alexia started bobbing up and down while sliding her womanhood over the base. She loved the sensation of running over the ridge where fur gave way to flesh."
"At the same time, she found herself licking the head for some reason. The woman had no idea why she was doing it, but his pre-cum did taste really good!"

al "Wow, you taste and shmell good! *hic*  Oh, thish is sho much fun!"

gh "Oh sweet soft lady, you, you are so good to me. I think, I think..."

"He growled instead of continuing, then he came."

scene cg78 with sshake
scene cg78 with sshake
scene cg79 with flash
show alexia necklace naked aroused behind cg79
show greyhide neutral behind cg79
pause 2

"A huge geyser of hot misty fluid blasted Alexia in the face, then a second wave, finally a third."
"The storm caught her by complete surprise but, after a few moments of complete confusion, Alexia just started giggling incessantly."

gh "That was wonderful. You made me feel loved again, like I belong to someone. Oh Alexia, thank you for this. Thank you so much. I never thought I would be able to feel love again."

"Still giggling, Alexia tried to wipe her face clean with her hands, then accepted the tablecloth from Greyhide."

al "Oh, you really know how to make a lady feel like shomething, let me tell you."

"She tapped her hand on his chest in time with her last few words as he gathered up his armor and started fastening it back on."

scene bg27 with fade
show alexia necklace naked aroused at edgeleft with dissolve
show greyhide neutral at center with dissolve
show rowan necklace shock at edgeright with moveinright

ro "What in the hell happened here!?"

al "Oh Rowan! You should see thish guy's cock, it'sh like as big ash your leg!"

ro "Alexia, are you drunk?"

al "Don't be shilly! I only had one little bottle. *hic*  It'sh great shtuff! You should try some."

"Greyhide extracted one of the vials from his belt and held it out for Rowan to see."

gh "Firegrout draft, I thought I'd share some of my favorite drink from home with you after you gave me that nice wine."

show rowan necklace neutral at edgeright with dissolve
hide alexia with dissolve

"At that moment, Alexia started slumping forward and Rowan quickly ran forward to catch her before she collapsed completely, then carefully lowered her to the floor."

show greyhide sad at center with dissolve

gh "What happened? Is your wife alright?"

show rowan necklace angry at edgeright with dissolve

"The man wheeled on the minotaur, fury in his eyes."

ro "You mean you didn't mean to get my wife drunk so you could get her to break her vows to me?! Do you even know what marriage means?"
ro "It means that you pledge yourself to love only one another until death!"

"The minotaur was stunned. He'd never seen Rowan so angry before and slowly tried to process what had just been said to him."

gh "She was drunk? But she only had one! This batch is unusually strong but even normal grout takes four drafts to actually do that to anyone but children... oh. Oh!"

"Realization of what had just happened dawned on Greyhide and his head fell forward in shame."

gh "I am so, so sorry. I did not mean for, for..."

"Rowan's fury ran cold. He could see that his friend hadn't meant for this to happen and Rowan knew that minotaurs didn't practise marriage like humans did. This understanding only made things even more painful for him."

gh "Curse my ancestors, I feel so strange now! I do not know what has come over me!"

scene black with fade

"Instead of talking further, he turned around and picked up his unconscious wife from the floor. Then he left the room, carrying Alexia."

scene bg14 with fade
show jezera neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

"On his way out of the dinning hall, Rowan ran into Jezera in the hallway."

je "Oh, is dinner over already? Looks like lovely Alexia enjoyed herself at least."

ro "Shut up."

"The man kept walking past the demoness, in no mood to deal with her teasing."

show jezera happy at midright with dissolve

je "Temper temper, my hero."

"A finger slipped under his chin and forced Rowan to look into Jezera's eyes."

show jezera displeased at midright with dissolve

je "I can say and do whatever I want in {i}my{/i} castle."

show jezera happy at midright with dissolve

"Then her hand was gone and he was able to continue down the hall."

je "Oh, and thanks for your help earlier, I'm sorry I interrupted your dinner."

if alexiaSeparateRoom == True:
    scene bg7 with fade
    show alexia necklace naked aroused behind bg7
else:
    scene bg9 with fade
    show alexia necklace naked aroused behind bg9

show rowan necklace neutral at midleft with moveinleft

"As Rowan entered the room, he felt his wife let out a giggle and then start groping him through his pants."

al "Hmm, got something in your pocket for me?"

"She groaned out softly while being set down on the bed and helped out of her shoes."

al "Come on darling, don't you want to fuck me silly? {i}*hic*{/i}"

ro "What in the hells is with you tonight?"

"All he got in response was a giggle followed by heavy breathing."

ro "(She's asleep. Okay, that was not normal for Alexia, even while drunk. Solensia help me, I hate this place.)"

show rowan necklace sad at midleft with dissolve

#If (Alexia has had sex with another character than Rowan before now):
#"It was one thing to Rowan to know that Alexia had broken their vows before now. It was quite another to see her doing it right in front of him."

#rejoin

ro "(I shouldn't have yelled at Greyhide. I hope all three of us will be able to get past this....)"

#Alexia gains corruption, Rowan and Alexia lose a small amount of relationship.  Note that Alexia and Greyhide had sex.
$ alexiaUnfaithful = True
$ change_corruption_actor('alexia', 3)
$ change_relation('alexia', -1)
$ alexia_greyhide_sex = True
return
