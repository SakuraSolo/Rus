# screen for selling/buying items
screen shop_screen(trader):
    # forbid rollback and mark changes made in this screen to be saved
    $ renpy.block_rollback()
    $ renpy.retain_after_load()
    # category (filter for showing items)
    default category = 'weapon'
    # current page used by backpack_widget
    default page = 0
    # current page for shop
    default shop_page = 0
    # when item is hovered, this is set to uid of that item
    default hovered_uid = None
    frame:
        if trader.name == 'Cla-Min':
            background 'gui/shop/caravan_backdrop.png'
        # there is only Greyhide left currently
        else:
            background 'gui/shop/forge_backdrop.png'
        textbutton 'Back' action Return() style 'back_button'
        frame:
            xalign 0.5
            ypos 20
            background None
            add 'gui/shop/title area.png' xalign 0.5
            if trader.name == 'Cla-Min':
                text 'Caravan' ypos 25 xalign 0.5 size 30
            else:
                text 'Forge' ypos 25 xalign 0.5 size 30
        # buttons for choosing category
        frame:
            pos (500, 120)
            xysize (750, 580)
            background None
            hbox:
                xfill True
                for cat in item_categories:
                    textbutton cat.capitalize():
                        action [SetScreenVariable('category', cat), SetScreenVariable('page', 0), SelectedIf(cat == category)]
                        style 'angular_button'
            # show items in shop
            frame:
                align (0.0, 1.0)
                background None
                use shop_items(trader, category, shop_page)
            # show trader image
            if trader.name == 'Cla-Min':
                add 'gui/shop/Shop_Character_Portrait_ClaMin.png' xpos -70 yalign 1.05 zoom 0.8
            else:
                add 'gui/shop/Shop_Character_Portrait_Greyhide.png' xpos -70 yalign 1.05 zoom 0.8
            # show backpack
            frame:
                align (1.0, 1.0)
                background None
                use shop_backpack_widget(trader, category, page)
            # show Rowan
            add 'gui/shop/Shop_Character_Portrait_Rowan.png' xpos 340 yalign 1.05 zoom 0.8



#~     # inventory (equipped and backpack)
#~     # show shop trader name
#~     frame:
#~         ysize 430
#~         xfill True
#~         xalign 1.0
#~         ypos 40
#~         xmargin 5
#~         background Frame('gui/stats_border.png', 12, 12)
#~         vbox:
#~             xalign 1.0
#~             xfill True
#~             # buttons for choosing category
#~             hbox:
#~                 for cat in item_categories:
#~                     textbutton cat.capitalize():
#~                         action [SetScreenVariable('category', cat), SetScreenVariable('page', 0), SelectedIf(cat == category)]
#~                         style 'small_textbutton'
#~             hbox:
#~                 spacing 50
#~                 xalign 0.5
#~                 # show items in shop
#~                 use shop_items(trader, category, shop_page)
#~                 # show backpack
#~                 use shop_backpack_widget(trader, category, page)
#~     # return from this screen
#~     textbutton 'Return' action Return():
#~         style 'small_textbutton'
#~         xalign 1.0
#~         xoffset -10
#~         ypos 10
#~     # show info for item
#~     use item_info(hovered_uid)
#~     # show traders info
#~     use shop_trader(trader)


# show shop items
screen shop_items(trader, category, shop_page):
    default cols = 5
    default rows = 7
    # square sell side size
    default cell_side = 66
    frame:
        background None
        xsize (cols * cell_side + 12)
        ysize (rows * cell_side + 12 + 52)
        frame:
            xsize (cols * cell_side + 12)
            ysize (rows * cell_side + 12)
            xpadding 7
            ypadding 7
            background 'thick_rect'
            # item cells grid
            frame:
                background 'cells_grid'
                xysize (cols * cell_side, rows * cell_side)
                pos (-1, -1)
                add 'gui/inventory/inventory damage bevell.png'
                add 'gui/inventory/inventory damage bevell.png' align (1.0, 1.0)
            $ i = 0
            $ j = 0
            # create items from uids, filtered by category
            $ filtered_items = [item for item in trader.inventory.bp if category in item.categories]
            # loop over items for current page
            for item in filtered_items[(shop_page*cols*rows):((shop_page+1)*cols*rows)]:
                imagebutton action Buy(item, trader):
                    idle item.small_img
                    insensitive im.Composite((64, 64), (0,0), im.Grayscale(item.small_img), (0,0), "gui/forbidden_border.png")
                    hover im.Composite((64, 64), (0,0), item.small_img, (0,0), "gui/hover_border.png")
                    xpos i * cell_side
                    ypos j * cell_side
                    hovered SetScreenVariable('hovered_uid', item.uid)
                    unhovered SetScreenVariable('hovered_uid', None)
                    alternate Show('item_zoom', item=item)
                # if more than one item of this type, display their quantity
                if trader.inventory.bp[item] > 1:
                    text str(trader.inventory.bp[item]) color '#0f0':
                        xpos i * cell_side
                        ypos j * cell_side
                # update i, j for next item
                python:
                    i += 1
                    if i == cols:
                        i = 0
                        j += 1
        # change pages of inventory
        frame:
            background 'gui/inventory/Arrow box.png'
            xysize (136, 53)
            xalign 0.8
            yalign 1.0
            imagebutton action [SetScreenVariable('shop_page', shop_page - 1), SensitiveIf(shop_page > 0)]:
                idle 'prev_arrow'
                insensitive 'prev_arrow_null'
                yalign 0.3
                xalign 0.1
            text str(shop_page) xalign 0.5 yalign 0.3 line_spacing 0
            imagebutton action [SetScreenVariable('shop_page', shop_page + 1), SensitiveIf(len(filtered_items) > cols*rows*(shop_page+1))]:
                idle 'next_arrow'
                insensitive 'next_arrow_null'
                yalign 0.3
                xalign 0.9


# 'shop' version of avatar's backpack widget
screen shop_backpack_widget(trader, category, page):
    # show backpack (filtered by category)
    default cols = 5
    default rows = 7
    # square sell side size
    default cell_side = 66
    frame:
        background None
        xsize (cols * cell_side + 12)
        ysize (rows * cell_side + 12 + 52)
        frame:
            xsize (cols * cell_side + 12)
            ysize (rows * cell_side + 12)
            xpadding 7
            ypadding 7
            background 'thick_rect'
            # item cells grid
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
                imagebutton action Sell(item, trader):
                    idle item.small_img
                    insensitive im.Grayscale(item.small_img)
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
        # change pages of inventory
        frame:
            background 'gui/inventory/Arrow box.png'
            xysize (136, 53)
            xalign 0.8
            yalign 1.0
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


# show trader info and money of trader and avatar
screen shop_trader(trader):
    frame:
        xysize (450, 200)
        xpos 5
        yalign 1.0
        yoffset -40
        background  Frame('gui/stats_border.png', 12, 12)
        has hbox
        spacing 10
        frame:
            background  Frame('gui/stats_border.png', 12, 12)
            xysize (180, 180)
        vbox:
            text trader.name size 30 color '#ff0'
            text 'Gold: {}'.format(trader.gold) color '#ff0'
            text avatar.name size 30 color '#0f0'
            text 'Gold: {}'.format(avatar.gold) color '#0f0'


init python:

    class Buy(Action):
        '''Buy item (trader --> avatar)'''
        def __init__(self, item, trader):
            self.item = item
            self.trader = trader

        def __call__(self):
            self.trader.inventory.remove(self.item.uid)
            self.trader.gold += self.item.buy_value
            avatar.inventory.add(self.item.uid)
            avatar.gold -= self.item.buy_value
            renpy.restart_interaction()

        def get_sensitive(self):
            return avatar.gold >= self.item.buy_value


    class Sell(Action):
        '''Sell item (avatar --> trader)'''
        def __init__(self, item, trader):
            self.item = item
            self.trader = trader

        def __call__(self):
            self.trader.inventory.add(self.item.uid)
            self.trader.gold -= self.item.sell_value
            avatar.inventory.remove(self.item.uid)
            avatar.gold += self.item.sell_value
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.trader.gold >= self.item.sell_value
