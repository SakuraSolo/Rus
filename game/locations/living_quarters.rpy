# living quarters
label quarters:
    call screen room_screen("bg14", "jezera room",
            (('Talk', '_operator_talk'),
            ('Visit', 'visit_menu'),
            ),
            'jezera_living_quarters')
    return


label visit_menu:

menu:
    "Visit Arzyl." if arzylDialogueAvailable:
        jump arzyl_dialogue
        
    "Visit Whitescar." if whitescarDialogueAvailable:
        jump whitescar_dialogue
        
    "Back.":
        jump quarters