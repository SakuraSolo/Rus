# Guest wing of the castle (training version)
label guest_wing_st:
    call screen room_screen('images/Backgrounds/guest room.jpg', None,
        (('Alexia', 'train_alexia'), ('Another char', 'pass'), ('Leave', 'return')))
    return


label train_alexia:
    call screen npc_controls('images/Backgrounds/guest room.jpg', alexia)
    jump guest_wing
