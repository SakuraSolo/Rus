init python:
    
    event('rastedel_debrief', triggers='week_end', conditions=('palaceStage == 2',), run_count=1, priority=pr_story)



label rastedel_debrief:

scene bg14 with fade
show jezera happy behind bg14

"Rowan approached Jezera’s door. She would expect a report on how his trip to Rastedel had gone, and Rowan had learned by now that such things were best handled sooner than later."
"He knocked on the door."

je "Come in~!"

"Rowan opened the door, and had to pause because of what he found. Jezera had company with another woman, it seemed."

menu:
    "Watch.":
        $ released_fix_rollback()
        $ bovineBondageWatch = True
        #cg1 - var 1
        scene cg288 with fade
        show jezera naked happy behind cg288
        show rowan necklace neutral behind cg288
        pause 3
        "Jezera was naked on her bed, and with her was a young woman. Rowan could have mistaken her for human, if not for her larger the normal mammaries, horns, and animalistic legs. It was a half-minotaur girl."
        "The demoness had the girl tied up, with her wrists behind her back, a harness made from rope pressing into her body, and even a taunt segment running between her legs. Other ropes emerged from the harness, linking to the bed, and leaving her hovering inches off it."
        "This was all having quite the effect on her. The half-minotaur's face was flushed red with arousal. Her eyes were sealed shut and her mouth was twisted by a series of moans that seemed to follow along so close after the previous one as to blend together into one long twisted sound."
        "Jezera, for her part, was entertaining herself by brushing two finger over the top of the crotch rope, pressing it even harder against her bound subject’s clit. Her free hand glided over the knots that held the entire piece together."
        jump bovineBondage
        
    "Avert his gaze.":
        $ released_fix_rollback()
        $ bovineBondageWatch = False
        scene bg18 with fade
        show rowan necklace shock at midleft with dissolve
        show jezera naked happy at midright with dissolve
        "Rowan saw just enough to notice that the girl whom Jezera was toying with was not human. She looked mostly humanoid, but her large breasts, the horns jutting out from her hair, and her strange cow-like legs told him that she must be a half-minotaur."
        "Jezera had her in some sort of elaborate bondage. Clearly she was having a bit of fun."
        show rowan necklace neutral at midleft with dissolve

label bovineBondage:

je "Yes, my hero?"

"Rowan leaned against the door frame with his arms crossed."

ro "My apologies. I didn’t mean to interrupt your fun."

if avatar.corruption < 30:
    "He blushed slightly at the comment. Such open sexuality was still new to him."
    
else:
    "Rowan smirked to himself."

"Jezera didn’t seemed perturbed at all. If anything, the movement of her hands along her captive’s body seemed to increase."

if bovineBondageWatch == True:
    "The girl moaned out and tried to squirm in her bonds. The stimulation effect was clearly getting to her. But, the rope held steady."
    #cg1 - var 2
    scene cg289 with fade
    "Her captor seemed to have no time or energy for that though. She brought her hand back, and gave the girl a quick slap to her crotch. "
    "The girl let out a high pitched yelp, and shrunk back into her restraints. Still, she was now wiggling even more than she had been a moment before."
    "Jezera brushed her hand against the bed sheets, wiping the juices off. She didn’t much change her expression during the act. Rowan knew she wasn’t the sadist her brother was."
    #cg1 - var 1
    scene cg288 with fade
    show jezera naked happy behind cg288
    show rowan necklace neutral behind cg288
    pause 2
    
else:
    pass
    
je "Not at all. You’re not interrupting much."
je "I visited the slave markets on a recent trip back home. The half breeds they sell there are not particularly pricey, but I took a liking to this one. She claimed she didn’t like girls when I asked her. Is that still true, dear?"

halfm "No Mistress! I like girls! I like girls!"

"Jezera smirked wickedly."

je "So, as you can see, I’ve been showing her the ropes. It is my duty to make sure she understands what is expected of her here. "

"Rowan shook his head. The longer he stayed here, the more predictable Jezera’s antics had become."

ro "I returned from my mission to Rastedel, Mistress. As you commanded, Doran Raeve has been slotted back into noble politics, and I observed the court and its workings."
    
"Jezera nodded softly, and reverted her attention back to the girl."

if bovineBondageWatch == True:
    #cg1 - var 3
    scene cg290 with fade
    show jezera naked happy behind cg290
    show rowan necklace neutral behind cg290
    pause 3
    "Jezera took two fingers, digging them around the rope. There was a wet sound as they entered the girl’s body."
    halfm "Ah!"
    "Her breath grew more and more intense. Her chest, with its massive heavy bosom, heaved up and down as much as the restraints would allow. Her inexperienced body, already overstimulated, was no match for Jezera’s very skilled fingers."
    halfm "Ah! Ah! Ah!"
    "Jezera snickered softly."
    je "Shush dear. Your betters are speaking."
    "The girl slammed her lips shut as best as she could, but pathetic aroused noises kept on slipping from them."
    
else:
    pass
    
je "I do not believe that was all I asked you to do, Rowan. What about allies?"

"Rowan looked at the squirming halfbreed and then back at Jezera."

ro "Is there a way you could prevent her from hearing? She is new after all."

"Jezera sighed."

je "So mistrustful. Do you really believe my servants are so easily compromised?"
je "But, if it will make you feel better, then I suppose something can be done about it."
    
"All she did though was snap her fingers. There was not even any kind of physical change. Yet, he did smell something. It faintly smelled of sulfur."

je "One of the benefits of this being my room is all of the spells weaved in. For now, all that my new acquisition will hear will be white noise."
je "Isn’t that right dear?"

"The Half-Minotaur didn’t respond. It could have just been from the mind numbing pleasure she was being subjected to, but it really did seem like she hadn’t even heard."

je "Now, you were saying?"

ro "My contact was Ameraine, correct? That is who you intended me to meet up with?"

if bovineBondageWatch == True:
    "Jezera’s fingers still worked the poor girl's pussy. The change from whimpering to full on gasping for air showed just how close the girl was to cumming. The constant massage of the rope against so much of her skin combined with Jezera’s ministrations were relentless."
    
else:
    pass
    
je "So you did manage to meet with her. Good. I can only hope you have not somehow wrecked our alliance."

ro "No. We spoke briefly. It seemed she was pleased with the effects of my presence."

if amerFirstSex == False:
    "Rowan decided not to mention the part where he had placed the alliance at risk by refusing a sexual encounter with her. Best if she didn’t know about that."
    
else:
    pass
    
je "Excellent. Then with that-"

halfm "Mistress! I can’t hold it back any longer! Mistress, I’m going to-"

if bovineBondageWatch == True:
    "The girl shook violently. The ropes around the bed rattled and shook with her. At one point, he was even worried that one of the knots, a rather loose looking one whose weakness was no doubt caused by Jezera’s laziness, might slip."
    #cg1 - var 4
    scene cg291 with dissolve
    pause 2
    show cg292 with dissolve
    pause 2
    show cg293 with dissolve
    pause 2
    show cg294 with dissolve
    pause 2
    show jezera naked happy behind cg294
    show rowan necklace neutral behind cg294
    "When it finally ended, the girl laid back limp in her bonds. The rise and fall of her chest showed she was still alive. But, all energy had been drained from her body. She was entirely exhausted."
    "Jezera withdrew her hand and ran her tongue over it to collect the taste of the girl’s juices."
    scene bg18 with fade
    show rowan necklace neutral at midleft with dissolve
    show jezera naked happy at midright with dissolve

else:
    "It seemed that the Half-Minotaur girl had reached her limit. In that moment, she came on Jeera’s hand. Afterwards, Jezera had to stop talking for almost a minute to clean up. Meanwhile, the girl had gone limp with exhaustion."
    
je "Now then, with that distraction out of the way. I was going to say that you have completed your mission admirably."
je "I’m not finished with Rastedel. It must fall if we are to succeed."
je "How do you feel about that, Hero?"

menu:
    "Remain silent.":
        $ released_fix_rollback()
        ro "..."
        je "What? Don’t have much to say?"
        "She giggled softly to herself."
        je "I suppose that matters little. It’s not like you have much of a choice in the matter."
        
    "Detached acceptance.":
        $ released_fix_rollback()
        ro " If that is your command."
        "Jezera rolled her eyes."
        je "How obedient of you."
        
    "Agree heartily.":
        $ released_fix_rollback()
        ro "..."
        ro "Being back there had an effect on me."
        ro "It reminded me of all of things I expected to get after the war."
        "Jezera sighed."
        je "And all of the ways they disappointed you?"
        ro "If I must be the one to do it. To bring an end to that entire little world. I think I could do that."
        "Jezera smirked softly."
        je "That’s the spirit."
        
je "One last thing."

ro "Yes?"

je "What is Ameraine like?"

ro "What?"

je "I’ve never actually met her in person before. I know her only from correspondence and reputation. She was acquainted with my father, and I reforged that old contact. But, we have yet to actually meet."

"Rowan stroked his chin. It was strange that Jezera would seemingly trust a figure like Ameraine in a position of great influence, especially if the two had never even met."

ro "She’s clever and playful. She likes to put on games and show off her wit…"

"Rowan had to consider the question. Certainly Ameraine had many similarities with Jezera. But, there was something different about them too. A sense he got from Ameraine, even when he didn’t know her intentions in a particular moment."

ro "She’s very deliberate though. I can’t explain it exactly. But, I get a sense from her like she plans each of her moves ten steps ahead."

"Jezera yawned to herself. Rowan knew her well enough to know that she was trying to hide her annoyance."

je "Sounds like my kind of woman then."
je "You may go."


if goal3_completed == False:
    je "Just remember that I expect you to complete your assigned task of bringing in another race as an ally. We need an army. Every day we don’t have one, you are gambling with your life, my hero."
    
else:
    pass
    
#TODO: when we have requirement
#if recruitment/money requirements are not met.
    #je "Don’t forget to grow our war chest and barracks the normal way too. You were given a mission and we expect it completed."

"Rowan nodded softly, and left the room. Better to leave Jezera with her exhausted plaything. Better, as well, to leave Rowan with his thoughts."

return
