init python:
    
    event('ride_together', triggers='map_expl', conditions=('world.cur_tile_type == "forest"', 'week >= 30'), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('forest_break', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    
label ride_together:

scene bg3 with fade
show rowan hood neutral at midleft with dissolve

"Rowan’s horse made a clopping sound as it tread the dirt trail that ran through the trees. Rowan used the time to think. There was so much thinking to do and so little time to do it."

argo "Who goes there?"

"Rowan looked up to find himself staring at the face of another bearded man. Like Rowan he was well armed. But, unlike a town guard or soldier he wore a camouflage cloak and sensible leather armor. A ranger perhaps?"
"The man introduced himself as Argonui. He claimed was a hunter from a nearby village who had been living in the woods of late. At first he was reluctant to explain why, but when Rowan revealed his own identity, it put away any doubts the man still held."

$ argoName = "Argonui"

argo "You’re the greatest dirt general of all time. Surely you’d understand. When the famine hit, my neighbors were struggling. I could bring food from the woods, so my wife was okay." 
argo "But, all around me I saw suffering. The lord of the area, a landed knight named Sir Iris, had ordered that the grain taxes remained in place. He sells it to the Eastern Mines, and it makes up most of his income. I’ve seen his books."

ro "How have you seen his books?"

"The ranger dismissed the question with a wave of his hand."

argo "I interceded on behalf of my neighbor. But, the lord did not take kindly to that act. I was declared an outlaw and driven from my home. My eldest starved without me to bring food home."

"He scowled."

"Now, I wait in the woods. I intercept any of Iris’ men that I find and leave them strung up. Someday, I’m going to do it to Iris too."

"Rowan was shocked by the man’s admission, but insisted he had no interest in the private quarrel. Indeed, an insurgency out here in the woods might be a good thing. The two rode together the rest of the way."
"When they parted ways, he offered Rowan some tips on good trade goods to sell the nearby villages. He also left Rowan with new perspective on the state of the realm."

$ change_treasury(+10)
return

########################################################################
########################################################################
########################################################################

label forest_break:
    
scene bg3 with fade

"With a heavy sigh, Rowan pushed a particularly invasive branch away from his face. Rosaria forests, while not as dense as the Ealoen woodlands, could still grow pretty wild in certain areas."
"For most people it was hardly a problem, as the road network covered all the important locations, but unfortunately for Rowan, these rarely reached drider nests and orc camps."
"And so, he was forced to rely on hunter trails and small paths made by the many animals that lived nearby, ceaselessly trudging through the area. With any luck, he’ll reach something resembling a normal track soon enough."
"Few hours later, there was still no track in sight, but he did come across something that caught his attention."
"An open field, next to a small creek, with a lone tree in the middle. A strangely peaceful, almost romantic, sight, in the otherwise wild forest. Seemed like the perfect place to rest."
"… But an open position like that would leave him open to any predators that might live in the area…"

menu:
    "Rest a while.":
        $ released_fix_rollback()
        "Pushing forward without a moment of rest, while admirable in desperate times, as of now would only serve to needlessly exhaust him. Too much caution could be as detrimental as too little of it."
        "He approached the clearing, mindful of any beasts or archers that might’ve positioned themselves nearby."
        "He needn’t bother. There were none. He was free to appreciate the idyllic scenery in all it’s glory, without any interference."
        "And as he learned when he approached the tree, he wouldn’t be the first one. The tree had half a dozen of hearts carved into it, each with different initials. J+N, A+G, G+R…"
        "The last one was crossed out."
        if all_actors['alexia'].relation < 30:
            "Love rarely lasted, as he came to learn."
        else:
            "Rowan chuckled to himself seeing this. Ah, young love…"
        "In the end, he ended up camping under the tree, taking a much needed rest from his dreary journey."
        "He would resume his fight tomorrow. The twins, unfortunately, weren’t going anywhere."
        $ heal_wounds(1)
        $ avatar.mp -= 1
        return
        
    "Continue on.":
        $ released_fix_rollback()
        "He didn’t become the hero of Karst by being careless or taking breaks. He ignored the clearing, and marched on."
        "This stubbornness would help him shave off some time, if nothing else."
        $ avatar.mp += 1
        return

        

