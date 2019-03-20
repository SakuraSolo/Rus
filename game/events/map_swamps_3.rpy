init python:
    event('slithering_premonitions', triggers='map_expl', conditions=('world.cur_tile_type == "swamp"',), run_count=1, group='map_expl', priority=pr_map_rnd)


label slithering_premonitions:

scene bg32 with fade

"Rowan stepped carefully through the bogs. This was a dangerous path with all kinds of horrors that could be found. He kept his eyes open for swamp beasts and unusually sized rodents."
"His diligence would prove tiring but well rewarded."
"Near the shambling path that might have been inaccurately called a road, he heard the sound of a disturbance. With a hand on his sword hilt, he went to investigate."
"Rowan found what looked like a pair of female legs being dragged into the swamp. Whatever torso they were connected to had long since been sucked under the bog. Rowan braced himself. Should he try to help her?"
"The thought was banished when he saw three small tendrils rise above the bog’s surface. To an uninformed traveler they might not have seemed so threatening, but Rowan understood their implications. The woman in the bog was well beyond saving by now."
"After that Rowan put even more diligence into every step. Alone in the moss would be a terrible fate."

$ avatar.mp -= 1
return