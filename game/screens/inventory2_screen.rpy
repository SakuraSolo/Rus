screen inventory2_screen():
    # forbid rollback and mark changes made in this screen to be saved
    $ renpy.block_rollback()
    $ renpy.retain_after_load()
    # category (filter for showing items)
    default category = 'weapon'
    # current page used by backpack_widget
    default page = 0
    # when item is hovered, this is set to uid of that item
    default hovered_uid = None
    # add background and current character avatar
    frame:
        background 'gui/statsinventory_backdrop.png'
        textbutton 'Back' action Return() style 'back_button'
        # buttons to switch inventory/status
        use inventory_status_switch
        # inventory (equipped and backpack)
        # buttons for choosing category
        hbox:
            pos (540, 144)
            xsize 474
            spacing 15
            for cat in item_categories:
                textbutton cat.capitalize():
                    action [SetScreenVariable('category', cat), SetScreenVariable('page', 0), SelectedIf(cat == category)]
                    style 'top_tab'
        # show level up button if there is enough exp
        if avatar.new_exp >= avatar.req_exp:
            textbutton 'Level up' action Show('avatar_level_up'):
                style 'rcrect_button'
                text_color '#d5d3d4'
                pos (350, 31)
        # show backpack
        use backpack_widget(category, page)
        # show equipment slots
        use equipment_slots_screen
        # some info about stats and level
        use avatar_info




#~     frame:
#~         alt 'Inventory of [avatar.name]'
#~         xysize (800, 430)
#~         xalign 1.0
#~         ypos 40
#~         xoffset -5
#~         background Frame('gui/stats_border.png', 12, 12)
#~         vbox:
#~             xalign 1.0
#~             # buttons for choosing category
#~             hbox:
#~                 xsize 626
#~                 xpos -6
#~                 for cat in item_categories:
#~                     textbutton cat.capitalize():
#~                         action [SetScreenVariable('category', cat), SetScreenVariable('page', 0), SelectedIf(cat == category)]
#~                         style 'small_textbutton'
#~             # show backpack
#~             use backpack_widget(category, page)
#~         # show slots and equipped items
#~         grid 2 5:
#~             ypos 50
#~             spacing 5
#~             transpose True
#~             for slot in equip_slots:
#~                 # add icon for item slot
#~                 use equipped_item_widget(slot)
#~     # return from this screen
#~     textbutton 'Return' action Return():
#~         style 'small_textbutton'
#~         xpos 20
#~         ypos 40
#~     # show info for item
#~     use item_info(hovered_uid)
#~     # show short info for current avatar
#~     use avatar_info


# buttons to switch inventory/status
screen inventory_status_switch():
    frame:
        background im.FactorScale('gui/inventory/Inventory_Buttons_Base.png', 1.2)
        pos (750, 0)
        xysize (360, 140)
        hbox:
            ypos 20
            xalign 0.5
            spacing 30
            imagebutton action [Show('inventory2_screen'), Hide('status2_screen')]:
                idle 'gui/inventory/Button_Inventory_Neutral.png'
                hover 'gui/inventory/Button_Inventory_Pressed.png'
                selected 'gui/inventory/Button_Inventory_Pressed.png'
            imagebutton action [Show('status2_screen'), Hide('inventory2_screen')]:
                idle 'gui/inventory/Button_Stats_Neutral.png'
                hover 'gui/inventory/Button_Stats_Pressed.png'
                selected 'gui/inventory/Button_Stats_Pressed.png'


# show equipment slots
screen equipment_slots_screen():
    grid 2 5:
        pos (47, 180)
        xspacing 280
        yspacing 16
        transpose True
        for slot in equip_slots:
            # add icon for item slot
            use equipped_item_widget(slot)


screen equipped_item_widget(slot):
    # show small widget with equipped item
    fixed:
        xysize (64, 64)
        # if slot is blocked for equipping, do not show slot pic in it
        if slot in avatar.inventory.blocked_slots:
            frame:
                xfill True
                yfill True
                background None
        # if slot is free for equipping, show slot pic in it
        elif avatar.inventory.slots[slot] is None:
            frame:
                xfill True
                yfill True
                background None
                add 'gui/stats_{}.png'.format(slot) xalign 0.5 yalign 0.5
        # if slot has item equipped, show button with that item pic
        else:
            imagebutton action Function(avatar.inventory.clear_slot, slot):
                idle avatar.inventory.slots[slot].small_img
                xysize (64, 64)
                hovered SetScreenVariable('hovered_uid', avatar.inventory.slots[slot].uid)
                unhovered SetScreenVariable('hovered_uid', None)
                alternate Show('item_zoom', uid=avatar.inventory.slots[slot].uid)


screen backpack_widget(category, page):
    # show backpack (filtered by category)
    default cols = 10
    default rows = 7
    # square sell side size
    default cell_side = 66
    frame:
        xsize (cols * cell_side + 12)
        ysize (rows * cell_side + 12)
        pos (540, 176)
        xpadding 7
        ypadding 7
        background 'thick_rect'
#~         background Frame('gui/test_rect.png', 10, 10)
        frame:
            background 'cells_grid'
            xysize (cols * cell_side, rows * cell_side)
            pos (-1, -1)
            add 'gui/inventory/inventory damage bevell.png'
            add 'gui/inventory/inventory damage bevell.png' align (1.0, 1.0)
        $ i = 0
        $ j = 0
        # filter items by choosen category
        $ filtered_items = [item for item in avatar.inventory.bp if category in item.categories]
        # loop over items for current page
        for item in filtered_items[(page*cols*rows):((page+1)*cols*rows)]:
            # if item is meant to be equipped, use 'equip' action for item's imagebutton
            if category in ('weapon', 'armour', 'accessory'):
                imagebutton action Function(avatar.inventory.equip, item.uid):
                    idle item.small_img
                    hover im.Composite((64, 64), (0,0), item.small_img, (0,0), "gui/hover_border.png")
                    xpos i * cell_side
                    ypos j * cell_side
                    hovered SetScreenVariable('hovered_uid', item.uid)
                    unhovered SetScreenVariable('hovered_uid', None)
                    alternate Show('item_zoom', item=item)
                    # text for self-voice
                    alt item.name + ' ' + ' '.join(item.keywords) + ' ' + ' '.join(['{} {:+}'.format(letter_to_stat[eff], item.effects[eff]) for eff in item.effects]) + ' ' + item.descr
            # item and quest items are not usable now
            elif category in ('item', 'quest'):
                imagebutton action NullAction():
                    idle item.small_img
                    hover im.Composite((64, 64), (0,0), item.small_img, (0,0), "gui/hover_border.png")
                    xpos i * cell_side
                    ypos j * cell_side
                    hovered SetScreenVariable('hovered_uid', item.uid)
                    unhovered SetScreenVariable('hovered_uid', None)
                    alternate Show('item_zoom', item=item)
                    # text for self-voice
                    alt item.name + ' ' + ' '.join(item.keywords) + ' ' + ' '.join(['{} {:+}'.format(letter_to_stat[eff], item.effects[eff]) for eff in item.effects]) + ' ' + item.descr
            # if more than one item of this type, display their quantity
            if avatar.inventory.bp[item] > 1:
                text str(avatar.inventory.bp[item]) color '#0f0':
                    xpos i * cell_side
                    ypos j * cell_side
            # if this item is equipped, display this
            if item in avatar.inventory.slots.values():
                text 'E' color '#f00':
                    xpos i * cell_side + 47
                    ypos j * cell_side + 42
            # update i, j for next item
            python:
                i += 1
                if i == cols:
                    i = 0
                    j += 1
    frame:
        xpos ((cols * cell_side + 12) + 540 - 200)
        ypos ((rows * cell_side + 12) + 176)
        background 'gui/inventory/Arrow box.png'
        xysize (136, 53)
        # TODO: for some reason 'page' variable is changed in parent screen
        imagebutton action [SetScreenVariable('page', page - 1), SensitiveIf(page > 0)]:
            idle 'prev_arrow'
            insensitive 'prev_arrow_null'
            yalign 0.3
            xalign 0.1
        text str(page) xalign 0.5 yalign 0.3 line_spacing 0
        imagebutton action [SetScreenVariable('page', page + 1), SensitiveIf(len(filtered_items) > cols*rows*(page+1))]:
            idle 'next_arrow'
            insensitive 'next_arrow_null'
            yalign 0.3
            xalign 0.9


screen item_info(uid):
    # widget for showing quick item info when item is hovered
    frame:
        xalign 1.0
        yalign 1.0
        yoffset -40
        xoffset -5
        xysize (800, 200)
        background Frame('gui/stats_border.png', 12, 12)
        ypadding 12
        xpadding 12
        if uid:
            vbox:
                spacing 0
                $ item = Item(uid)
                # name of the item
                text '{{size=30}}{}{{/size}}     {{size=20}}Buy/sell values: {}/{}{{/size}}'.format(item.name, item.buy_value, item.sell_value)
                text '  '.join(item.keywords)
                if item.effects:
                    # if item has stats effects, show them
                    text ' '.join(['{{color={}}}{}: {:+}{{/color}}'.format('#f00' if item.effects[eff] < 0 else '#0f0', letter_to_stat[eff], item.effects[eff]) for eff in item.effects])
                else:
                    text 'None'
                # item description
                text item.descr


screen avatar_info():
    # small widget to show current avatar stats
    frame:
        pos (78, 685)
        background None
        hbox:
            spacing 4
            # show colored avatar's final stats
            for stat in ('strength', 'vitality', 'reflexes', 'intelligence', 'luck'):
                frame:
                    xsize 65
                    background None
                    text '{{color={}}}{}{{/color}}/{}'.format(ratio_color(getattr(avatar, stat), getattr(avatar, 'base_' + stat)), getattr(avatar, stat), getattr(avatar, 'base_' + stat)):
                        xalign 0.5
                        yalign 0.5
    frame:
        pos (200, 545)
        xysize (90, 90)
        background None
        text '[avatar.lvl]' size 50 xalign 0.5 yalign 0.5
    frame:
        pos (55, 595)
        xsize 150
        background None
        text '[avatar.gold] g' yalign 0.5 xalign 0.0
    frame:
        pos (300, 595)
        xsize 150
        background None
        text '[avatar.exp] exp' yalign 0.5 xalign 1.0


screen item_zoom(item):
    # shows bigger item image
    modal True
    add item.img xalign 0.5 yalign 0.2
    frame:
        style_group "navi"
        xalign 0.5
        yalign 0.95
        textbutton "Back" action Hide("item_zoom")
    # right click closes item zoom
    key 'mouseup_3' action Hide('item_zoom')
