# random map events that happen on forests
init python:

    # Elven Patrol
    event('elven_patrol', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)



label elven_patrol:
#Elven Patrol
#No requirements

scene bg forest1
"The problem with elves was, they always saw you before you saw them. It lent to their air of insufferable smugness."
"Rowan slowly came to a halt as he realised there were five arrows on tautened bowstrings in the trees around him, all pointed at him."

#if infamy is high
if avatar.infamy > 10:
    archer "We know of you, servant of Kharos. Never enter these woods again, lest you want an arrow in the eye."
    archer "And when you next get on your knees and touch the robes of your vile masters, you can tell them the same."
    "They weren't true elves, Rowan realised, looking at the hostile, dirty faces above him; their simple, rough clothes and fuller features marked them out for the half-born outcasts they really were."
    "Still, they probably could carry out their threat.  He slowly backed away, retracing his steps out of the glade under their watchful glare. It would take an arduous amount of time to find a way around them."
    #lose 4 move points
    $ change_mp(-4)
    return
#else
else:
    archer "The hero of Rosaria, said to be a truly inhuman paragon of righteousness. Now said to be corrupted, and bending the land to the will of Kharos."
    archer "And yet... I have heard much that backs up the former, precious little the latter."
    "They weren't true elves, Rowan realised, looking at the suspicious, dirty faces above him; their simple, rough clothes and fuller features marked them out for the half-born outcasts they really were."
    "Still, that subtracted nothing from the threat of their bows."
    ro "No matter how bitter the circumstance I have found myself in, I have always tried to do the right thing. Always."
    archer "...I have no reason to believe you, human. Yet I do. Rest here for a while if you wish - there are medicines under the stump behind you should you need them."
    archer "But tell the ones that you serve never to come here, if they value their lives."
    "The half-elves slid their bows away and clambered further back into the trees, disappearing from view. It was as if it were a trick of the light on the bobbing leaves that they were ever there at all."
    #if wounded
    if avatar.wounds > 0:
        "Breathing a sigh of relief, Rowan dozed for a short time in the peaceful glade and helped himself to the wraps of herbal medicines stowed within the hollow stump, soothing balms upon his old wounds."
    #else
    else:
        "Breathing a sigh of relief, Rowan dozed for a short time in the peaceful glade."
    "Once he felt fully rested, he picked himself up and carried on."
    #gain 2 move points, and heal 1 wound (if wounded)
    $ change_mp(2)
    $ heal_wounds(1)
    return

