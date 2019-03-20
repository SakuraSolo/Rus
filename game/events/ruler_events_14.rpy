init python:

    #Liurial Wants a Protector (Worldbuilding + sex)
    #High priority event that probably triggers sometime around late mission 2 or early mission 3.
    event('liurial_wants_a_protector', triggers="week_end", conditions=('week >= 20', 'dice(3) == 1'), group='ruler_event', run_count=1, priority=pr_ruler_high)
    #Proposing Drider Occupation
    #Requires at least 2 driders in breeding pits, game is currently after mission 2, and player has occupied at least 2 villages in Rosaria of any size.
    event('proposing_drider_occupation', triggers="week_end", conditions=('week >= 4', 'goal2_completed', 'castle.villages >= 2', 'castle.buildings["pit"].driders >= 2'),
        group='ruler_event', run_count=1, priority=pr_ruler)
    #Drider guards resolution
    #Requires that flag for drider guard test be 1 and at least 5 weeks have passed since Proposing Drider Occupation.  High priority event?
    event('drider_guards_resolution', triggers="week_end", conditions=('week >= 4', 'drider_guard_test == 1'), active=False, group='ruler_event', run_count=1, priority=pr_ruler_high)


label liurial_wants_a_protector:
#Liurial Wants a Protector (Worldbuilding + sex)
#High priority event that probably triggers sometime around late mission 2 or early mission 3.

scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show liurial sad at midleft with moveinleft

"Out of the corner of his eye, Rowan saw a high elf woman approach him. She'd been watching him work for the better part of an hour now and seemed to have finally decided to talk to him."
"The man put down his work to study the woman directly now that she wasn't trying to hide anymore."
"This wasn't someone that Rowan had ever seen before, but based on how she was dressed he guessed she was a part of the castle domestic staff. A new recruit then? Jezera seemed to pick up new people every month or so, but this was the first high elf he'd seen in this roll."
"There was at least one or two high elves working in the library under Cliohna, so they weren't unheard of in Bloodmeen. Still, he wouldn't expect one to be all that comfortable here, especially under his mistress."

ro "Yes miss? How can I help you?"

$ Liurialname = "Woman"

liur "You're the hero Rowan Blackwell, are you not?"

ro "I am, which puts me at a disadvantage. Might I ask your name, maiden of the forest?"

$ Liurialname = "Liurial"

liur "My name is Liurial, but I am no maiden, not anymore."

"A shiver ran over the woman, but she pressed on regardless."

liur "A horrible man here is tormenting me, has forced himself on me. I, I thought that Jezera would put a stop to it, but she won't do anything!"

#liurial sad

"There was a note of betrayal in her voice."

liur "You are second to Jezera, yes? So you could stop him where she didn't. Please hero, I know not who else I could turn to for help."

show rowan necklace happy at midright with dissolve

ro "(At least it isn't Jezera or Andras themselves. I can actually do something!)"
ro "Alright, I'm going to pay this man a visit.  See what he has to say for himself and make sure he doesn't touch you again."

scene black with fade

"The man in question wasn't anyone important. Just some self-assured hotshot that Jezera had added to her staff recently as well. He hadn't even bothered trying to hide what he'd done and threw the first punch when Rowan told him to stop."
"The rapist hit the floor not ten seconds later, unconscious."
"It also turned out that Liurial wasn't the only woman he'd been harassing and other members of the staff were quite happy to see him brought down. The man made arrangements for a suitable punishment, then sent the man off with a couple other staff members."

scene bg13 with fade
show rowan necklace happy at midright with dissolve
show liurial sad at midleft with dissolve

"That left him with the elven woman who'd requested his aid."

ro "There, you shouldn't have to worry about him anymore."

"She didn't have a response at first, just looked at Rowan for several long moments. Then she rushed forwards and wrapped her arms around his waist with a hug."

liur "Thank you, thank you."

"The hero put his hand on her head and gave it a paternal rub. In response, she snuggled in closer to him. The tender moment took on a more sensual feel and the closeness of the comely woman stoked other passions."
"She rubbed against him, causing a full erection. Rowan wasn't sure if that was deliberate or not, but Liurial made no move to disentangle herself from him."

menu:
    "Kiss her on the mouth. See how far she's willing to go.":
        $ released_fix_rollback()
        jump liurialSex1

    "Push her away.":
        $ released_fix_rollback()
        "Deciding that was enough, Rowan pulled her arms off of him and pushed her away. This seemed to surprise the woman."
        liur "I... I thought you liked that. Do you not find me attractive?"
        ro "Liurial?  Is this proper for someone like you?"
        liur "I'm no proper elven maiden, I told you that. I came here because I hated the life I had to live. Having to live everyday the perfect picture of an elven maiden, walk this way, dress that way, stop slutting around."
        show liurial angry at midleft with dissolve
        liur "I wanted to be free. I wanted to love someone like Jezera, who promised me a place where I could just be myself. Then she betrayed my love."
        show liurial neutral at midleft with dissolve
        liur "You didn't. You protected me, and now I want to give myself to you. Please take me!"
        "She spread her arms wide, inviting Rowan to embrace her again."
        menu:
            "Kiss her on the mouth. See how far she's willing to go.":
                $ released_fix_rollback()
                jump liurialSex1

            "No means no.":
                $ released_fix_rollback()
                ro "I'm sorry Liurial, I'm a married man."
                show liurial sad at midleft with dissolve
                liur "Honorable on fidelity too, just my luck. Sorry about that.  I... didn't know."
                ro "What was that show all about, why were you trying to have sex with me?"
                liur "My kinsmen use to call me a slut. If that means I like sex then fine.  I'm a slut. You are strong, attractive, healthy, and kind. Anyone who didn't want you is either deluding themselves or they have very strange tastes."
                ro "All you wanted was some casual sex?"
                liur "It's not only sex. Bloodmeen is a terrible place, owned by terrible demons. You're the first decent person I've met her with any real power. I wanted to be your woman, so you'd want to protect me."
                ro "Well, I'm actually away from the castle most of the time, scouting the Six Realms for the twins. So I couldn't exactly help you anytime you were in danger. Besides, if the twins are after you there isn't much I could do about it."
                liur "So it was a fool's errand anyway. I am still grateful for your aid this day, hero. Farewell."
                "She bowed, then turned to leave."
                show liurial sad at edgeleft with moveoutleft
                jump liurialConclusion

################################################################################

label liurialSex1:

#Show first CG, Rowan kissing Liurial.
scene cg140 with fade
pause 3

"Rowan leaned forward, while simultaneously lifting up Liurial's chin to meet him. As their lips touched, she opened her mouth and welcomed him inside eagerly."
"The kiss was held for several seconds, then Rowan pulled back and saw the elven woman had a soft smile on her lips, that remained parted and eager for more. So he kissed her again, this time a little more vigorously."
"A pleased moan filled her mouth as his tongue invaded it, encouraging him to do more and more. In response, Rowan let his hands explore her body a bit, feeling the soft slim curves of her race."
"Something seemed off about her dress, and he broke off the kiss for a moment to see what had happened."

#CG of Liurial with her breasts exposed, blushing, and looking a bit sultry.
scene black with fade

"Sure enough, her dress had somehow come undone during their kiss, and her breasts were now exposed. A frown creased his forehead, which faded away when he looked back up at Liurial and saw she was glowering meaningfully at him."

$ event_tmp['teased'] = False

menu .liurial_first_encounter_kiss:
    "Tease her." if not event_tmp['teased']:
        $ released_fix_rollback()
        show rowan necklace happy behind black
        show liurial naked happy behind black
        ro "Well now, that's quite the display. One might think you were trying to seduce me."
        "Her blush deepened and she glanced back and forth somewhat furtively trying to figure out how to respond."
        ro "My dear, whatever is the matter with you?"
        "He put a hand on her cheek and force her to make eye contact with him again."
        liur "How much are you going to tease me? Do you like seeing a woman flustered and begging you?"
        #return to the previous menu, "Tease Her" has now unable to be chosen again
        $ event_tmp['teased'] = True
        jump .liurial_first_encounter_kiss

    "Take her.":
        $ released_fix_rollback()
        jump liurialTakeHer

    "End this.":
        $ released_fix_rollback()
        show rowan necklace neutral behind black
        show liurial naked sad behind black
        ro "I think that's quite enough, better cover back up now."
        "Liurial froze up, looking confused and worried."
        scene bg13 with fade
        show rowan necklace happy at midright with dissolve
        show liurial sad at midleft with dissolve
        liur "Did I do something wrong? I thought you liked me?"
        ro "I did kiss you didn't I? No, I'd like to know why you suddenly decided to throw yourself at me after another man was apparently forcing himself on you."
        liur "You are strong, attractive, healthy, and kind. Anyone who didn't want you is either deluding themselves or they have very strange tastes."
        ro "All you wanted was some casual sex? I'm surprised you turned to that so quickly after a man tried to force himself on you."
        liur "My kinsmen use to call me a slut. If that means I like sex then fine. I'm a slut. That's not all though."
        liur "Bloodmeen is a terrible place, owned by terrible demons. You're the first decent person I've met her with any real power. I wanted to be your woman, so you'd want to protect me."
        ro " Well, I'm actually away from the castle most of the time, scouting the Six Realms for the twins. So I couldn't exactly help you anytime you were in danger. Besides, if the twins are after you there isn't much I could do about it."
        liur "So it was a fool's errand anyway. I am still grateful for your aid this day, hero. Farewell."
        "She bowed, then turned to leave."
        show liurial sad at edgeleft with moveoutleft
        jump liurialConclusion

################################################################################

label liurialTakeHer:
$ liurialSex = True
scene black with fade


"Rowan cupped a breast with one hand and squeezed her ass with the other, then lead her backwards towards the bed. A joyful smile filled Liurial's visage, evidently she was very eager for what was going to come next."
"After a playful push, she tumbled backwards onto the bed and continued smiling as Rowan undid his straps and pulled off his pants, letting his hard cock spring free. Liurial groaned in excitement and rubbed her knees together a moment before spreading them wide."

#sex CG, Rowan leaning over Liurial with pants off and Liurial's dress has been compressed to her belly.
scene cg134 with fade
show liurial naked aroused behind cg134
pause 3

"He fell upon her and pulled her dress up, revealing the parted lips of her womanhood that pulsed and glistened in the low light, eager to be filled up. She'd slid her undergarments to the side, allowing him easy access."
"Then he filled her in one quick thrust, eliciting an excited squeal from his new lover. She filled out around him easily, conforming to his intrusion and squeezing down immediately afterwards. The passage was completely soaked, far more than Rowan thought was normal."
"He kissed her once, twice, then trusted against her in a steady rhythm. Each movement was met with encouraging sounds, but also somewhat plaintiff, as if she wanted more."

menu:
    "Be romantic.":
        $ released_fix_rollback()
        "Rather than fucking her hard as she seemed to be asking, the man instead redoubled his efforts to tease and toy with her. This felt more natural to him and certainly wasn't getting a thumbs down from his audience."
        "Liurial was surprised, but responded positively to his touches, to his tongue, to the ongoing gentle thrusts. In his hands, she was clay for him to sculpt. No resistance, no rejection, no initiative. This was Rowan's stage and she was the audience."
        "He didn't increase the pace at all until he sensed that his orgasm was incoming.  Then, and only then, did he start thrusting faster and faster. Just as he was about to crash over the edge, he began pulling his hips all the way out."
        "A cry of worry escaped Liurial's lips as his cock was completely removed from her."
        liur "Inside, please, inside me."
        scene cg134 with sshake
        scene cg134 with sshake
        scene cg135 with flash
        show liurial naked aroused behind cg135
        pause 3
        "Her cry soon turned into a cry of ecstasy instead, as he slammed home as per her request. That act put him over the edge and he filled her insides with his seed, a small worry at the back of his mind but that was overshadowed by her desire to be filled."
        liur "Yes, make me yours."
        "Rowan held her for several moments, savering the afterglow. Then he kissed her once and pulled out. Deciding to wait for her to recover from his treatment, he sat down on the chest next to the bed."

    "Fuck her.":
        $ released_fix_rollback()
        "Well, if she wanted him to fuck her, who was he to reject that request?"
        "She certainly wasn't complaining when he stopped teasing her and instead started pounding her. In an instant her body started writhing under him in ecstasy as he pistoned in and out of her at a rapid pace."
        liur "By Solansia, that's good!"
        "The man didn't try to respond to her, instead focusing on keeping his arousal in check with this level of stimulation. Her passage quivered around him, alternating between trying to hold him in and milking him of his seed."
        "Apparently he was more successful than he meant to be, as he was surprised by her suddenly crying out in a blissful orgasm. That didn't mean he was going to stop, if anything he was pretty sure that Liurial was enjoying being used for his pleasure."
        scene cg134 with sshake
        scene cg134 with sshake
        scene cg135 with flash
        show liurial naked aroused behind cg135
        pause 3
        "That hunch was all but confirmed when her gasps of pleasure kept ringing out and she rode her orgasm on and on around his pounding thrusts. Though this time he didn't hold back when he felt his seed spill out in response to her desires."
        liur "Yes, I'm yours! Fill me!"
        "One more thrust, two, then he was done. Heaving a deep sigh, Rowan pulled himself out of her well worn hole and sat down on the chest next to the bed to catch his breath."

scene black with fade

"Several minutes later."

scene bg13 with fade
show rowan necklace neutral at midright with dissolve
show liurial happy at midleft with dissolve

ro "You certainly pledged yourself to me in a hurry."

liur "Whatever do you mean?"

ro "Well, most of the women in this castle want something out of me when sex comes up. So forgive me if I suspect you want something more than just casual sex."

show liurial sad at midleft with dissolve

liur "Why are you so suspicious of me? Isn't it enough that I'm giving myself to you?"

ro "Whenever I want, however I want?"

show liurial happy at midleft with dissolve

liur "Yes!  How about a blowjob? Working for the twins must be so tiring, I bet you don't have any women who'll go down on you whenever you need."

ro "Wow. That's definitely not something you hear an elven woman say often."

show liurial angry at midleft with dissolve

liur "Hey, I like sex. If my kinsman call me a slut for it, then I'm a slut. Fuck them."

show liurial neutral at midleft with dissolve
show rowan necklace happy at midright with dissolve

ro "But a particular slut, since you won't just fuck anyone. What makes me different from that man I just protected you from?"

liur "You are strong, attractive, healthy, and kind. Anyone who didn't want you is either deluding themselves or they have very strange tastes"

show rowan necklace neutral at midright with dissolve

ro "That still doesn't explain why you threw yourself at me so suddenly, or why you so desperately seem to want to belong to me."

show liurial sad at midleft with dissolve

liur "Okay. Bloodmeen is a terrible place, owned by terrible demons. You're the first decent person I've met her with any real power. I wanted to be your woman, so you'd want to protect me."

ro "Well, I'm actually away from the castle most of the time, scouting the Six Realms for the twins. So I couldn't exactly help you anytime you were in danger. Besides, if the twins are after you there isn't much I could do about it."

liur "But they listen to you! The staff do what you say! Can't you tell them to leave me alone?"

ro "You just haven't seen it yet, but a lot of the time they do things I can't stop. The twins have hurt many people when I've tried to stop them, or sometimes because I don't want them to."

liur "Oh. Then I apologize for asking that of you."

"She bowed to Rowan once."

liur "Uh, if you still want to have sex or a blowjob sometime, I don't mind. That was really good."

"Then she turned away from Rowan and started walking towards the door."

show liurial neutral at edgeleft with moveoutleft

jump liurialConclusion

label liurialConclusion:

ro "Wait. I think I've got a better idea."

"Liurial stopped in her tracks and looked back at Rowan with a mix of a curious and hopeful expression on her face."

ro "The twins basically leave me to my own devices because I'm more useful to them that way. Can you read and write?"

liur "In spite of my efforts to seduce my teachers... yes."

ro "Then I might have a job for you...."

#Next week, trigger her follow up event.
# TODO: activate event
# this will allow to summon Liurial in throne room
$ can_summon_Liurial = True
return


###########################################################################################################################
###########################################################################################################################
###########################################################################################################################


label proposing_drider_occupation:
#Proposing Drider Occupation
#Requires at least 2 driders in breeding pits, game is currently after mission 2, and player has occupied at least 2 villages in Rosaria of any size.

scene bg6 with fade
show rowan necklace neutral at midright with dissolve
show draith neutral at midleft with moveinleft

ro "Good afternoon, master breeder. How can I help you?"

dra "Hey hot stuff. I wanted to run an idea I had by you about using our driders as guards."

ro "Alright then, why were you thinking of doing this?"

dra "Well, to get some more field training in for our handlers as well as freeing up some of our capacity. With your permission, I'd like to deploy a couple of our driders as guards for a village in Rosaria."

ro " You mean, as a part of our occupying force? What in the Six Realms makes you think that's a good idea?"

dra "Like I said, we don't get many chances to actually use the driders and they're really sex hungry so it will be nice to be able to sick'em on the troublemakers instead of our own all the time. Plus, like I said, our handlers could really use more practical experience."

ro "From what you've said about driders, it sounds like there's a good chance they'll go off and start raping random people. No matter how good your handlers are."

dra "Yeah, one or two might go on a rampage, but at the end of the day we're only really risking some random peasants. That's no worse than our soldiers, considering the danger of just holding monsters, even tame ones."
dra "If all goes well, we might even be able to incorporate driders into our garrisons at all our Rosarian holdings. That will really strike terror in the humans."

ro "(He sounds... proud of this idea.)"

menu:
    "Allow Draith to experiment with drider guards in an occupied Rosarian village.":
        $ released_fix_rollback()
        ro "Alright Draith, you have my permission to start your experiment."
        show draith happy at midleft with dissolve
        dra "Excellent! This is why I love having you as a boss. I'll start arrangements at once!"
        hide draith with moveoutleft
        "A moment after the dark elf departed, Rowan slumped in his chair a bit. Even if all went well, what exactly was he condemning his countrymen to?"
        #Set flag for drider guard test to 1
        $ drider_guard_test = 1
        $ activate_event('drider_guards_resolution')
        $ set_event_timer('drider_guards_resolution', 'after test', 5)
        #Lose 2 driders
        $ castle.buildings['pit']._driders -= 2
        #Rowan gains a little guilt and infamy
        $ change_base_stat('g', 2)
        $ change_base_stat('i', 2)
        #Gain some Draith relationship
        $ change_relation('draith', 2)
        return

    "Refuse Draith's proposal.":
        $ released_fix_rollback()
        ro "No Draith, my countrymen are not test subjects for this crazy experiment."
        dra "It isn't a crazy scheme! Do you have any idea how much we can benefit from this? I can guarantee that as soon as we've had some test research I can-"
        ro "This discussion is over. The answer is no."
        "Draith stared angrily at Rowan for several moments, then turned and walked away. His posture was stiff and indignant as he left the room."
        ro "(At least I spared them this horror.)"
        #Rowan loses a small amount of guilt.
        $ change_base_stat('g', -2)
        #Lose relationship with Draith.
        $ change_relation('draith', -2)
        return


###########################################################################################################################
###########################################################################################################################
###########################################################################################################################


label drider_guards_resolution:
#Drider guards resolution
#Requires that flag for drider guard test be 1 and at least 5 weeks have passed since Proposing Drider Occupation.  High priority event?

#luck check DC5

#success
if check_stat(5, 'luck')[0]:
    scene bg6 with fade
    show rowan necklace neutral at midright with dissolve
    show draith happy at midleft with moveinleft

    ro "It would seem that a congratulations is in order."

    dra "Indeed, our driders are proving very effective in keeping the twin's subjects in line. Already Andras is saying he'd like to see stepping up our operations and free up more of our soldiers for other tasks."

    ro "Yes... he told me as much already."

    dra "You don't seem all that pleased?"

    ro "Nothing you need to worry about."

    "The man's thoughts drifted to the multitude of people who'd been raped by the driders and how brutal the treatment of that town's populace had become."

    ro "(This is between my conscience and myself.)"

    "He could not deny that the task was more efficiently done this way and now that Andras was pushing for more drider involvement, there was no way he could stop it anymore."

    dra "I'm prepared to expand our drider guard operations, permitting availability of the hatchlings. The unneeded orc guards from our test site have already returned to Bloodmeen."
    dra "Assuming there is no pressing need for them, I can divert some of our new driders directly into service allowing us to free up the orc soldiers that would otherwise be needed as guards. How much should I expand the operation?"

    menu:
        #(Always available)
        "Minimal drider guards. Keep current recruitment rates.":
            $ released_fix_rollback()
            ro "I want to keep as many driders as possible right now, we don't need more orc soldiers."
            show draith neutral at midleft with dissolve
            dra "A shame. Very well, I'll maintain a minimal rotating guard. That way we can maintain our current level of drider production."
            jump driderChoice1

        "Small expansion of drider guards. -0.2 drider recruitment, +2 orc recruitment.":
            $ released_fix_rollback()
            ro "Well, we'd best satisfy Andras's demands. However, I want to keep the increased number of drider guards small."
            dra "If you're sure, alright. I'll start diverting a small amount of our hatchlings towards working as guards for Rosarian villages."
            #Reduce drider recruitment by 1, increase orc recruitment by 1.
            $ castle.buildings['pit'].drider_recruitment -= min(0.2, castle.buildings['pit'].drider_recruitment)
            $ castle.recruitment_bonuses['barracks'] = 2 + castle.recruitment_bonuses.get('barracks', 0)
            #Rowan gains a little guilt and corruption.
            $ change_base_stat('g', 2)
            $ change_base_stat('c', 2)
            jump driderChoice1

        #Requires drider recruitment be at least x2 and at least 3 Rosarian villages of any size occupied.
        "Significant expansion of drider guards. -0.4 drider recruitment, +4 orc recruitment." if castle.buildings['pit'].drider_recruitment >= 0.5 and castle.villages >= 3:
            $ released_fix_rollback()
            ro "You have my go ahead to expand the operation as per Andras's wishes."
            dra "Excellent! I'm very much looking forward to putting my wonderful hatchlings to work, thank you dearly for this opportunity, you big lug!"
            #Reduce drider recruitment by 2, increase orc recruitment by 2.
            $ castle.buildings['pit'].drider_recruitment -= min(0.4, castle.buildings['pit'].drider_recruitment)
            $ castle.recruitment_bonuses['barracks'] = 4 + castle.recruitment_bonuses.get('barracks', 0)
            #Rowan gains some guilt and corruption.
            $ change_base_stat('g', 3)
            $ change_base_stat('c', 3)
            #Draith gains positive opinion, gain one favor with Andras.
            $ change_relation('draith', 2)
            $ change_favor('andras', 1)
            jump driderChoice1

        #Requires drider recruitment be at least x3, at least 5 Rosarian villages of any size occupied, and Rowan must have partially abandoned his morals.
        "Maximum expansion of drider guards.  -3 drider recruitment, +3 orc recruitment." if castle.buildings['pit'].drider_recruitment >= 0.75 and castle.villages >= 5 and avatar.corruption > 20:
            $ released_fix_rollback()
            ro "Actually, I would like you to take it a step further and put as many drider guards in place as you possibly can."
            #draith surprise
            dra "Really sir? Andras had asked for..."
            "Rowan held up his hand."
            ro "The twins set the broad strokes, I'm the one who figures out the finer details. Put as many driders as you can working as guards."
            #draith happy
            dra "It would be my pleasure Rowan. Driders will be the terror of Rosaria in the coming weeks!"
            #Reduce drider recruitment by 3, increase orc recruitment by 3.
            $ castle.buildings['pit'].drider_recruitment -= min(0.6, castle.buildings['pit'].drider_recruitment)
            $ castle.recruitment_bonuses['barracks'] = 6 + castle.recruitment_bonuses.get('barracks', 0)
            #Rowan gains corruption and a little guilt.
            $ change_base_stat('g', 3)
            $ change_base_stat('c', 2)
            #Draith gains significant positive opinion, gain one favor with Andras.
            $ change_relation('draith', 4)
            $ change_favor('andras', 1)
            jump driderChoice1


    label driderChoice1:

    hide draith with moveoutleft
    ro "Good news for the castle...."
    #gain 5 orc soldiers
    $ castle.buildings['barracks'].troops += 5
    return

#fail
else:
    scene bg6 with fade
    show rowan necklace angry at midright with dissolve
    show draith neutral at edgeleft with moveinleft

    ro "Draith? Get in here."

    show draith neutral at midleft with moveinleft

    dra "Uh, yes sir?"

    ro "I have here on my desk a report detailing a major massacre that occurred two days ago in one of our occupied villages. Do you know what I'm talking about?"

    dra "No?"

    ro "The village where you were running your little experiment with drider guards. Do you want me to go in detail about how your handlers lost control of both those driders?"

    dra "What happened to my hatchlings?"

    "Rowan slammed his hand down on the table."

    ro "Damn it, that's your first concern? Not the dozen people they mutilated?"

    #draith upset
    show rowan necklace neutral at midright with dissolve

    ro "One escaped into the wild, the other was put down."

    dra "So there's a chance at least one of them can be saved and-"

    ro "No, no more people are going to be wasted on this."

    dra "But!"

    show rowan necklace angry at midright with dissolve

    ro "No!  Your handlers are to return to the castle at once. This experiment on my people is over! I don't want to hear anything more about drider guards, do you understand me Draith?"

    dra "Ye-yes sir."

    ro "Good."

    #Reduce castle income by 1, Rowan loses a bit of Rosaria reputation and Draith relationship.
    $ castle.villages_income -= 1
    $ change_base_stat('f', 3)
    #Net relationship change for the drider guard events should be positive, so you still get some relation for letting him try his experiment.
    $ change_relation('draith', -1)
    return

