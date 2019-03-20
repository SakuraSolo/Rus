# Rowan's chambers in the castle
label rowans_chambers_st:
    scene bg9
    # debug check (for all calls closed by returns)
    python hide:
        if renpy.call_stack_depth() != 1:
            raise Exception('call_stack_depth in Rowan\'s chambers == {}'.format(renpy.call_stack_depth()))
    call screen rowans_chambers_screen_st
    jump rowans_chambers_st


label rest_st:
    "Rowan spends the week resting, and recuperating from the toll of his adventures thus far. By week's end, he feels back to his old self."
#~     $ avatar.heal()
    return


label castle_map_st:
    scene
    call screen castle_map_st
    jump castle_map_st
