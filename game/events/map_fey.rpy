init python:

    #The maddening side of nature
    #Can occur on a forest tile after week 16
    event('maddening_side_of_nature', triggers='map_expl', conditions=('week > 16', 'world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    #The gentle side of nature
    #Can occur on a forest or swamp tile after week 16
    event('the_gentle_side_of_nature', triggers='map_expl', conditions=('week > 16', 'world.cur_tile_type in ("swamp", "forest")',), run_count=1, group='map_expl', priority=pr_map_rnd)


label maddening_side_of_nature:
#The maddening side of nature
#Can occur on a forest tile after week 16

$ arzylMet = True

scene cg305 with fade
pause 3

"It happened fast. Unnaturally fast. One moment Rowan was blissfully ignorant of their presence, the next he was surrounded by them. One moment he has his sword drawn, and was ready to defend himself, the next he was reeling from a kick to the guts."
"He had lunged at one of the assailants as a warning, and had been effortlessly disarmed in the process. Rowan was flustered, the weapon he had been disarmed with was a dagger. Whatever these women were he faced, they were not human."
"With his back against a thick birch tree Rowan did what he always did. He assessed how bad the situation was, and laughed internally. Technically it wasn’t all that bad. Three women with maliciously curved ritual daggers. How bad could that be?"
"The women approached him, each from a different angle. There was no escape except through one of them. As they closed in on him the already dim afternoon sunlight graced their features, and Rowan gasped."
"Three pairs of snow white eyes gazed feverishly into his own. Lips painted black as midnight smiled at him like ferocious predators, betraying sharp fangs made for drawing blood.  When he spied pointy elven ears large bestial horns his heart skipped a beat."
"These creatures were the legendary Drach’Hyl. In the common tongue they were unceremoniously called Nocturnal Elves, yet there was nothing trivial about them. The Nocturnal Elves fornicated with the Demon Lords of old, and had received dark gifts as a reward."
"Rowan opened his mouth to speak, hoping the Nocturnal Elves could be bargained with. He shuddered when he felt a prick in his neck. He turned his head to the left and found glassy eyes looking at him, and the tip of a dagger in his neck."
"In a fraction of a second he felt another sting, and to his right another of the elves had pierced his skin. They were fast beyond mortal capacity, and their venom worked just as fast. He expected to fall to the floor for an agonizing death, but instead he stood rooted like a tree."
"Rowan could not move a muscle save those of his eyes. He looked to the left and the right but found his eyes could not clearly make out the elves that had flanked him. The figure in front of him was the only thing his situation allowed him to focus upon."
"She was their leader, Rowan understood as he took her in. She had pale eyes that gazed at him with a cold intensity, plump lips curved into a wicked grin, and pronounced cheekbones that gave her face a devilish sort of regality."
"Rowan imagined the elf was in her early forties as far as appearance went, yet immediately conceded that while that may be so, she was the most well-preserved mature woman he had ever laid eyes on."
"When Rowan gazed lower he found a pair of overly-ripe breasts, the largest he had ever seen. He wondered whether such an absurd size of breasts was even aesthetically pleasant. When his manhood stirred Rowan had his answer."

scene bg3 with fade

show rowan necklace neutral at midleft with dissolve
show arzyl neutral at midright with dissolve

arz "Greetings to you, Rowan Blackwell. I am Arzyl, and these are my acolytes Estraea and Shyrenthe."

ro "..."

arz "I imagine you have many questions. What will we do with you? How do we know your name? Will we drink your blood? Perhaps something far darker?"
arz "I am not one to give information freely, however. None of your questions will be answered today. Instead, you will be sent away with more."
arz "We know you, Rowan. And we know for whom you work. Soon you will know us, and you will make a choice. To empower that choice with wisdom, I command you to observe."
arz "Be a good boy, and obey. If not… you will miss a spectacle few men ever get to witness."

menu:
    "Observe as instructed.":
        $ released_fix_rollback()
        jump arzylObserve

    "Try and break free of the venom.":
        $ released_fix_rollback()
        #vit test 18
        if check_stat(18, 'vitality')[0]:
            #pass
            "Rowan gathered all his mental fortitude and fought for control over his own body. He strained his mind in ways he had never done before, and felt a finger twitching. A finger eventually become a hand, which led to an entire arm."
            arz "What a disappointment. Do you have any idea what you are missing out on?"
            ro "All good and well, but I prefer to be in control."
            arz "Control is illusion, especially for you mortals."
            arz "If my orders did not specifically prohibit it I would slay you where you stand."
            ro "Who’s orders?"
            arz "You insult me, and then ask for information? You truly are a simple soldier, aren’t you?"
            arz "Estraea. Shyrenthe. Come. This one is not worthy of our exquisite company."
            scene black with fade
            "As inhumanly swift as they came, the Nocturnal Elves elves departed. One moment they were there, and then they were gone. Rowan picked up his sword and started walking, and for an hour or more a question had him spellbound. Who’s orders?"
            return
        else:
            #fail
            jump arzylObserve

label arzylObserve:

"He had no options. Rowan did as he was told. In his mind he heard his subconscious mock him. {i}Such an obedient boy. Andras would be proud of you.{/i} Rowan realized the red demon had gotten under his skin. He vowed he would deal with him in time."
"Rowan’s thoughts on Andras quickly dispersed when Arzyl spread her arms. She raised her chin dominantly, and gazed at Rowan with the longing of a predator. Rowan’s eyes scooped down and settled on Arzyl’s now showcased chest."
"Arzyl smiled when she noticed Rowan’s attention on her plump bosom. She bit her lower lip and winked at him. Rowan found it maddeningly erotic, yet again saw clearly the predator that Arzyl truly was."

#cg naked Aryzl
scene black with fade
show arzyl neutral behind black
show rowan necklace neutral behind black

"One of the ancient Nocturnal Elf’s acolytes came from behind her and respectfully disrobed her. She dropped the robe on the floor behind her and started to undo her brassiere. The other acolyte went to one knee and started to undo Arzyl’s lower garment."
"Arzyl’s breast popped free, and in doing so gifted Rowan with a new definition of ripeness. They were full and heavy, with an undeniable weight to them, but possessed of a youthful firmness as well. They were, Rowan mused, as unnatural as most else of the Nocturnal Elves."
"Rowan did not have much time to enjoy the bountiful orbs. Arzyl’s side-cut dress dropped to the floor and exposed a perfectly trimmed tuft of dark moss hair, from which a bloodshot clit stood out proudly. Arzyl’s clitoris was pierced by a silver ring adorned with a precious stone."
"Arzyl was the epitome of maternal sexuality, and Rowan’s body had responded against his will. That fact was bad enough as it was, but what troubled Rowan more was how his erect manhood had become uncomfortably stuck in his pants. Paralysis sucked; he was disgusted."

arz "Look at that, my acolytes. It seems our prey is a little… stuck!"

shy "Perhaps we should release the poor worm from it’s bondage?"

est "Surely he would have to earn such a privilege first?"

scene bg3 with fade
show rowan necklace neutral at midleft with dissolve
show arzyl neutral at midright with dissolve

arz "My sweet acolytes have a fair point. Your cock seems painfully stuck, but if you want us to release it, you must earn it."

ro "..."

arz "Blink with your eyes once and we will allow your poor cock to be free. Any poison can be conquered, Rowan. You need but the will."

"The mature Nocturnal Elf looked at Rowan with fiery intrigue. He could tell power and focus excited Arzyl, and that she was testing his capacity. Part of him wished to tell her to go to hell, that he was no toy. Another part wished to give this creature anything she wanted."

menu:
    "Try to blink your eyes.":
        $ released_fix_rollback()
        #vit check 8
        if check_stat(18, 'vitality')[0]:
            #pass
            "Rowan strained to focus his desire into a singular intent, and then, for as long as he could muster, applied all his will. His vision flickered not once but twice, which filled Rowan with a strange sense of accomplishment."
            "Arzyl smiled, bearing pointy fangs. She pointed at Rowan’s crotch, upon which one of the acolytes moved forward to undo his breeches. Rowan’s cock popped free as his pants hit the floor, a dangle of precum hanging from his cockhead."
            "The acolyte teasingly stroked his shaft a few times, ran her hand over the bottom of his length and gathered the pre-cum. This she brought to her mouth, and seductively licked off her finger. She then returned to Arzyl’s side."
            jump arzylSex
        else:
            #fail
            "Rowan strained to focus his desire into a singular intent, and then, for as long as he could muster, applied all his will. For a second he thought something was about to happen, but then his focused lapsed and he was back at square one."
            "Arzyl shook her head and shrugged mockingly. The acolytes laughed at Rowan’s failure, and their leader soon joined in."
            return

    "Don’t play along with her game.":
        $ released_fix_rollback()
        arz "What, don't want to play? Nevermind, I will show you anyway, so you may witness."
        jump arzylSex

################################################################################

label arzylSex:

arz "What I offer is a glimpse of the forgotten, a vision of the darker side of nature. A truth that courses through your veins, even if your entire being has forgotten it in favor of illusionary civilisation."
arz "Feast of me, my beautiful acolytes. Drink of my lifeblood, and in doing so take my essence into you. Indulge in the sacred alchemy. Devour!"

#cg acolytes drink
scene black with fade

"The acolytes did not need to be told twice. The first plunged her face into the area above Arzyl’s left breast, and buried her fangs into her skin. Arzyl groaned loudly as her skin was pierced, yet lovingly cupped the head of the acolyte in approval."
"The second acolyte was bolder. She fell to her knees and brought her sharp fangs before the sex of her mistress, and looked up longingly. Arzyl smiled ferociously and nodded. Arzyl then released a low and guttural moan; the sensitive skin above her cunt was punctured."
"What followed was a showcase of vampiric lust and lesbianism. Blood was drank from various parts of Arzyl’s skin, leaving puncture marks and tiny strings of red ichor. Hands found every intimate spot, cupping breasts and buttocks, and later disappeared into orifices."
"The alchemy Arzyl spoke of became apparent to Rowan. The acolytes drank of Arzyl, and Rowan had no doubt as to the boons - it formed the acolytes into the image of their mistress. It gave them eternal life and power."
"Arzyl in turn had become an idol of worship. The servants that she blessed with eternity would - for that same eternity - love and cherish her totally. The exchange was one of perfect balance, and as dark and uncivilised as the ancient Elf had proclaimed."
"Arzyl’s grunting intensified, indicating her climax was at hand. She stood spread legged, with fangs buried into either side of her inner thighs. Her glistening sex was clearly visible to Rowan, and was filled with fingers from both acolytes."
"Arzyl groaned loud, her voice low and hoarse. Juices bursted from her swolled sex with with furious intensity, coating the faces of her wanton acolytes. She gazed at Rowan in between her spasms, with a knowing glistening in her eyes."

#cg acolytes drink variant - squirt
scene black with fade
"Arzyl spasmed orgasmically for a good few minutes. The barrage of juices she spurted from her sex slowly subsided, and only then did the enigmatic mature return to her composed ways. The acolytes below her had resorted to slurping the juices of each other’s faces."

scene cg137 with fade
pause 3

"Arzyl moved towards Rowan whist never losing eye contact. Upon reaching him she pressed her sweaty body against his. Rowan felt her massive mammaries against his chest, and his stiff cock against her moist sex."

scene cg138 with fade
pause 3

"Arzyl took Rowan’s cock and brought it to her slit, and pushed it in for a mere quarter of an inch. It was hot as a furnace, and dripping juices still. She then brought her mouth to his ear, licked it, and spoke a single word. “Cum”."

show cg138 with sshake
show cg138 with sshake
scene cg139 with flash
pause 3

"Rowan exploded into her sex. He was barely inside her, and for some inexplicable reason lamented this greatly. All of his sticky seed bursted not into her warm cavity, but dripped from the sides of her sex over her legs to the floor."
"Arzyl laughed wickedly into Rowan’s ear. She asked him if he knew what she had ignited in him. When he did no answer she assumed he had not, and explained."
"Arzyl told Rowan she had invigorated his primal essence, the beast in him. She had him leashed like a dog - referring to the poison that debilitated him - or else he would have ravaged her. She asked Rowan what his inner-most desire had been at that moment."
"Here too Arzyl waited not for the response Rowan was incapable of giving. She explained that Rowan, at that point a beast in heat, had wanted to shoot his seed deep into her fertile womb. He had wanted to impregnate Arzyl. To breed her. For that is what beasts do."
"She laughed, and said that if Rowan aligned to Arzyl he would learn of bestial lust and desire like never before. Arzyl would teach him to channel such characteristics to reach his innermost essence - the maddening side of nature."

scene black with fade
"Before parting Arzyl told Rowan that they would meet again. Rowan would have time to consider his loyalties, and also what she offered. If he respected the Old Ways and the darker side of nature properly, there would be no poison next time."
"As inhumanly swift as they came, the Nocturnal Elves elves departed. One moment they were there, and then they were gone. Rowan picked up his sword and started walking, and for an hour or more a question had him spellbound. What piqued their interest in him?"
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label the_gentle_side_of_nature:
#The gentle side of nature
#Can occur on a forest or swamp tile after week 16

scene bg3 with fade

"The swamp was clearing into regular forest. Vivid rays of light could be seen through the trees, and the ground was no longer a boot-devouring monstrosity. Rowan’s mood had lifted accordingly, and as he trekked on under those circumstances he heard a queer voice."
"The voice was high-pitched and comical. Rowan could not make out what it said, but by the sound of it the creature was frantically spurting out word after word. When he heard penetrating laughter in the conclusion of the verbal interaction, his interest was piqued."
"Rowan followed the speech and discovered a second, far more gentle and softer voice, was returning conversation. Whether it was male or female he could not tell. He did recognize there was no need to fear for danger, and casually walked up."

show nileth neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

"Rowan found a queer looking creature he could neither identify as male or female, seated in the shadow of a large oak. The creature was slender and frail, and smiled meekly at him. On its shoulder sat a hand-sized being, which was the source of the high-pitched barrage of words."
"Both creatures had wings, identifying them as Fae. Rowan had heard rumors that there were different classifications of these beings, some almost as tall as mortals, and some tiny and alien. Before him sat the proof."

nil "A traveller? How exciting. Please, Daggertongue, behave? Just this once?"

dag "The manner of your request confers the unlikelihood of it, does it not? Halfwit!"

nil "..."
nil "I’m Nileth. This is my companion and royal guard, Daggertongue."

dag "I’m the reason you’re alive, ‘cause you’re a halfwit!"

nil "..."

ro "Well met, Fae-folk. I am Rowan Blackwell."

dag "Blackwell? More like Borewell! You look dull!"

nil "Please excuse Daggertongue, sir Blackwell. He has poor manners… "

ro "Don’t worry about it, I’m used to snarky remarks. It is a pleasure to meet you."

nil "The pleasure is ours. Would you care to sit down and join us for some idle conversation, or do your duties require you to move onward?"

menu:
    "Sit down with Nileth and Daggertongue.":
        $ released_fix_rollback()
        jump nilethTalk


    "Explain you need to keep moving.":
        $ released_fix_rollback()
        ro "I’m afraid I need to keep moving, otherwise I would be happy to talk. Perhaps our paths will meet again some day."
        dag "I pray to the Goddesses of the Old Ways they do not. You’re boring! Boring!"
        nil "…"
        nil "If the Goddess is willing, we will. I for one would enjoy that prospect…"
        dag "Ha! That and other ‘prospects’, you sissy!"
        "With that Rowan left the fey creatures to their discussion. As he walked away he heard Nileth plead to Daggertongue to behave from now on, to which the only response was maniacal laughter."

label nilethTalk:

ro "Rowan nodded and took of his boots, then sat down cross-legged. It felt good to be free of their constraints. He looked at Nileth and smiled, who lowered his eyes shyly in response."

dag "Wish you’d kept those on…"

nil "If you would sate my curiosity, Sir, perhaps you could tell me what brings you to these lands?"

ro "My employer requires me to gauge the land around their keep. They wish to… Hmm, how shall I put it? They wish to better the land with their influence."

nil "A noble pursuit, although one would think the land is just fine. At least, it was, until mortals started messing with it."

dag "You tell ‘em! All was well until you broad shouldered oafs came around and started spreading that nonsensical civilisation of yours."

nil "Daggertongue’s words are overly harsh, but in essence I am afraid I agree with him."

ro "I can hardly fathom how civilisation is a thing to be frowned upon. I do however understand that you, as creatures of the forest, feel you are better off without mortals meddling in your affairs."

dag "Your kind cuts our sacred forest away! You’re an ignorant lot, and you stink to boot!"

nil "What Daggertongue means is that humankind is generally focused on achieving its own desires, and is blind to the destruction they leave in their wake…"

dag "If that’s what I meant I would have said it, dimwit! Humans are ignorant and they stink, no need to sweet-mouth it. They disrespect the Old Ways greatly, which I pray will become their downfall!"

nil "…"
nil "So what are your thoughts on the matter, Sir Blackwell? Do the new races, of which humanity is the most promising and numerous, disrespect the Old Ways or not?"

dag "Stop calling him Sir... I remember what you did with the last human that you kept calling Sir, you sissy!"

nil "I’m just being respectful…"
nil "Anyway, your thoughts, Sir?"

menu:
    "The old ways are called old for a reason - man is the future.":
        $ released_fix_rollback()
        ro "When the balance between races changes over the course of time, I feel it is a natural process. The world changes, and if the old races refuse to re-align, is it not only natural their position falters?"
        nil "Survival of the fittest? Is that it?"
        dag "Don’t indulge that nonsense! We’re not done with the world yet, not even a little!"
        ro "Survival of the fittest? I would sooner say survival favors that race which is most natural for the current time. It would seem that humanity currently holds that position."
        dag "You’re only fit to carry large things around, oaf! You’re not better than us!"
        ro "I never said I was. I speak merely of what I observe - humanity thrives, while the elder races are in decline. For however long the Gods will it so, it shall be."
        nil " I agree with Daggertongue. I don’t think we’re past our expiry date. And I don’t think we ever will be!"
        dag "Tell ‘em, Nileth! For once you’re not a sissy!"
        nil "…"
        ro "You asked for my opinion on the matter, and I respectfully gave it. There is no need to be offended."
        nil "Perhaps you should continue on your journey…"
        dag "Yeah! Put those big boots back on and stink your way to somewhere else!"
        nil "…"
        ro "Very well. I will be on my way."
        scene black with fade
        "With that Rowan returned to his travels. He felt a stab of guilt; Nileth has been truly shocked at his view of the Fae’s place in the modern world. Daggertongue he prayed he would never see again… not even Andras had been able to insult Rowan so often in so little time."
        #-1 fae relationship
        $ change_relation('fey', -1)
        return

    "The old and the new can live in harmony. We just need to tolerate each other.":
        $ released_fix_rollback()
        ro "With the rise of the younger races everything changed. It’s up to both the new and the old races to learn to live together."
        nil "A wise viewpoint, Sir Blackwell, and one I can rally behind."
        dag "Of course you can! It would require a spine to defend your noble heritage, after all. Sissy!"
        nil "Stop saying that! I’m not a sissy!"
        dag "You’re not? Are you certain? Shall I tell ‘Sir’ Blackwell what your desires are regarding those you title as such?"
        #+1 fae relationship
        $ change_relation('fey', 1)
        jump nilethInterest

    "The old ways deserve more respect. I wish mankind knew better.":
        $ released_fix_rollback()
        ro "You and yours deserve more respect than us younger races are offering. The old races and their knowledge are a heritage we should not squander."
        nil "Your wisdom is refreshing, sir Blackwell. You’re someone I see myself spending time with, should the situation ever allow for it. I’d much enjoy that..."
        dag "Of course you would! You’re a sissy, after all."
        nil "Stop saying that! I’m not a sissy!"
        dag "You’re not? Are you certain? Shall I tell ‘Sir’ Blackwell what your ambitions are regarding those you title as such?"
        #+3 fae relationship
        $ change_relation('fey', 3)
        jump nilethInterest

label nilethInterest:

"Upon Daggertongue’s remark Nileth’s gaze fell to the floor. As it did Rowan inspected the frail Fae with abandon, and saw clearly what Daggertongue meant: Nileth was not just deeply submissive at heart, the creature likely preferred his sexual interactions interspecies."
"Rowan weighed his options. He could side with Daggertongue and play into being the masculine dominant, side with Nileth and be a gentle superior, or make clear he had no interest in any of these queer happenings."

menu:
    "I’m not at all interested in Nileth’s ambitions in that area.":
        $ released_fix_rollback()
        dag "Ha! You’re not getting any from him!"
        nil "…"
        ro "Take no offense. I just don’t swing that way…"
        nil "None taken, Sir Bla- "
        dag "You can stop with that! Ha!"
        nil "…"
        scene black with fade
        "Rowan enjoyed the company of the eclectic Fae duo a bit longer, and then said his goodbyes. While the Fae were an enigma to him still, Rowan felt that he had been a pleasant conversation partner, and was in good standing with them and their allies."
        return

    "You don’t need to share anything you’re not ready for, Nileth.":
        $ released_fix_rollback()
        dag "How sweet… if only he knew how you like it. Or should I say need it? Sissy!"
        ro "How he likes it is none of your business. And even then, I’m certain Nileth can tell me himself."
        nil "You are most kind, Sir Blackwell. How I like it…"
        dag "Get ready to be shocked, Sir Borewell!"
        nil " I.. well… I’d like it if you were a bit rough with me. And would use me as a… "
        ro "As a?"
        nil "…"
        nil "A possession. Someone, or something you… own. "
        dag "Where I’m from we call that a sissy! Ha!"
        nil "…"
        dag "Gonna deny it?"
        nil "…"
        scene black with fade
        "They talked for a good while. Rowan expressed that Nileth’s desires were perfectly normal, and that he need not be ashamed. Nileth was ecstatic with Rowan’s support, and more than once stated he expected they would meet again. He hoped to spend time with Rowan."
        "Rowan enjoyed the company of the eclectic Fae duo a bit longer, and then said his goodbyes. While the Fae were an enigma to him still, Rowan felt that he had been a pleasant conversation partner, and was in good standing with them and their allies."
        return

    "Go ahead, Daggertongue. Tell me how the sissy likes it.":
        $ released_fix_rollback()
        dag "See that, Nileth? It’s me and him! We’re going to have fun with you!"
        ro "Let’s not get ahead of ourselves here. You were about to explain something?"
        dag "Yes! Yes!"
        nil "…"
        dag "Nileth here likes to think he’s complicated and layered. Not so much! Turn him into a cocksleeve and a sexual servant, show ‘em who’s boss, and his little pee-wee will drip like the Absydine waterfalls!"
        ro "He likes to be manhandled? You’re certain his frail body won’t break?"
        nil "It’s very rude to talk about me like I’m not here."
        dag "He won’t break. Much."
        ro "Interesting…"
        nil "Guys?"
        scene black with fade
        "They talked for a good while. Rowan and Daggertongue developed a weird bond: they could not be more different from one and other, yet Nileth as a sexual object for their dominance united them in an unexpected way."
        "Rowan expressed that the meeting with Daggertongue and Nileth had been most pleasurable. Daggertongue agreed, and stated he expected them to meet again in the short future. The creature winked one of his small eyes at Rowan. It had devious plans."
        "Rowan enjoyed the company of the eclectic Fae duo a bit longer, and then said his goodbyes. While the Fae were an enigma to him still, Rowan felt that he had been a pleasant conversation partner, and was in good standing with them and their allies."
        return
