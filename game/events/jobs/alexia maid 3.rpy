init python:
    
    event('more_with_mary', triggers="npc_events", conditions=("get_actor_job('alexia')=='maid'",), depends=('alexia_and_mary',), group='alexia_maid', run_count=1, priority=pr_npc)
    

label more_with_mary:

scene bg14 with fade
show alexia maid neutral at midleft with dissolve

"Alexia had been working in the kitchens when it hit her. She didn’t know what it was. She didn’t know how to describe it. All she knew was that one moment she was doing her duties as a maid, entirely fine. The next moment she was on the ground crying."

show alexia maid sad at midleft with dissolve

"She didn’t even understand what had happened. Why did she feel like this? If someone had just asked her, she would have only been able to say that she felt...she felt…"
"...empty."
"She felt like there was something missing that should be there." 
"So, she stumbled off, tears strolling down her face into the hallway. Mary looked to the side to see what the disturbance was. But, Alexia just kept on stumbling. She clutched the walls. She put a hand to her heart. But, nothing eased it."
"Eventually she found herself crouching alone in her room…"

if alexiaSeparateRoom == True:
    scene bg7 with fade
    
else:
    scene bg9 with fade
    
show alexia maid sad at midleft with dissolve

"That was then when the door opened."

al "(Huh?)"

show mary concerned at midright with moveinright

mary "Hey..."

"Alexia turned around her. Her eyes were strained and red with tears. In the doorway stood Mary, with a concerned look on her face."

mary "You ran out, halfway through the job. If you were willing to risk punishment from Mistress J, I figured it must be pretty serious."

"She took a step closer and waited. Alexia didn’t stop her. So she took another step. Alexia didn’t know that she wanted to talk to Mary, she didn’t know that she wanted to talk to anyone, but she didn’t stop her friend."
"Mary took a spot next to Alexia and crouched down."

mary "What’s wrong?"

al "I...I don’t know. I can’t really describe it."

"Mary nodded."

mary "Do you want to talk about it?"

"Alexia considered the question. Did she want to talk about it?"

al "Not at the moment. I guess. Not really?"

mary "Alright. I’ll just sit with you."

"So they sat. At least for two hours. Mary didn’t say much, and neither did Alexia. It didn’t cure the...the...whatever it was that left her feeling so damn empty. But, it was good to have someone else there, even for a little bit."

al "Do you ever feel that...feel that this place takes your soul away? Just a little bit?"

mary "I don’t know if I’d say that."

al "Ugh. I don’t know. I don’t know how to explain it. It’s just...there is something that should be there and isn’t. And I want it to be right, but I don’t know how…"

"Alexia went on. She continued to try to explain how she was feeling, but she simply could not find the words for her state. Mary, though, listened intently. She nodded along to what Alexia was saying, and didn’t interrupt her or challenge her."
"By the time she was done, the feeling was gone too. It almost was like a passing phantom. It swooped in without warning, and just as quickly had vanished. Alexia even managed to smile."

show alexia maid happy at midleft with dissolve
show mary happy at midright with dissolve

al "Thank you. Really. Thank you. You don’t know how much you’ve helped me, Mary."

mary "You don’t have to thank me. I saw something was wrong, and I knew I had to help out. Who else do I have to laugh about Skorded’s beard with?"

"Alexia giggled."

al "No really, I do. I probably would have been miserable for hours without you. I really owe you one."

"Suddenly a mischievous look settled on Mary’s face."

mary "Welllllll. If you insist…"

#i kissed a girl CG
scene black with fade
show alexia maid shock behind black

"Alexia’s eyes shot open. Mary had suddenly closed the distance between them and pressed their lips together." 
"Alexia didn’t even have time to fight or come up with a coherent response to what happened. It had all happened so suddenly she didn’t know how to react."
"She had trouble even making sense of the sensation. Perhaps it was her confusion, but it felt odd. Mary’s lips were different from any man she’d kissed. They were softer. There was also something unusual. She wouldn’t realize until later that it had been Mary’s tongue piercing."

al "Mary...?"

"She withdrew slowly. Mary didn’t seem to mind. She had a smirk clear on her face. She looked like a child who’d eaten fruit from the tree they were supposed to stay away from."

if alexiaSeparateRoom == True:
    scene bg7 with fade
    
else:
    scene bg9 with fade

show alexia maid shock at midleft with dissolve
show mary happy at midright with dissolve


mary "That was my way of saying you're welcome."

"She rose to her feet."

mary "I’m just happy I could help however I could. Don’t worry about the chores. I’ll cover for you."

hide mary with moveoutright

"She gave Alexia a little wave and walked out the door. Alexia remained in place, incapable of speech or even rational processing."

"Alexia put a hand to her lips. What was that? The conversation had been so simple and wholesome, but then that kiss had come out of nowhere. It was so strange."
"But, more than that, she had to process if she even liked it." 

if all_actors['alexia'].corruption < 60:
    "Kissing girls was something she distinctly was not used to."
else:
    pass
    
menu:
    "It was oddly enjoyable.":
        $ maryKissLiked = True
        $ released_fix_rollback()
        show alexia maid happy at midleft with dissolve
        "She tasted her lips. It was hard to describe how she felt about it. It wasn’t disgust. Different from kissing a man, but not worse. It was softer. More on even footing."
        "Alexia giggled softly. Her earlier concerns had eased entirely."
        al "Maybe…"
        $ change_corruption_actor('alexia', 3)
        return
        
    "It wasn’t for her.":
        $ maryKissLiked = False
        $ released_fix_rollback()
        show alexia maid neutral at midleft with dissolve
        "Alexia tasted her lips. It took a few seconds to process, but she didn’t really like it. She wasn’t mad. Mary had been too playful, and before she had been so helpful. She didn’t even feel violated, even though if a man had done that, she certainly would have. It was too...innocent."
        "Alexia sighed. Her earlier concerns were mostly eased. Still, she was pretty sure that kissing girls just wasn’t for her."
        return


