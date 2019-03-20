# some styles
# other styles in options.rpy, screens.rpy, special_effects.rpy etc.

# TODO: remove this, use small_button instead
style small_textbutton:
    xpadding 25
    top_padding 15
    bottom_padding 10
    idle_background Frame('gui/button_idle.png', 30, 12)
    hover_background Frame('gui/button_hover.png', 30, 12)
    insensitive_background Frame(im.Grayscale("gui/button_idle.png"), 30, 12)
    selected_idle_background Frame("gui/button_hover.png", 30, 12)


style small_button:
    xpadding 25
    top_padding 15
    bottom_padding 10
    idle_background Frame('gui/button_idle.png', 30, 12)
    hover_background Frame('gui/button_hover.png', 30, 12)
    insensitive_background Frame(im.Grayscale("gui/button_idle.png"), 30, 12)
    selected_idle_background Frame("gui/button_hover.png", 30, 12)


style menu_list_button is small_button:
    xfill True
    xalign 0.5
    ypadding 15


style menu_list_button_text is text:
    xalign 0.5
    line_spacing 0


style menu_list_text is text:
        xalign 0.5
        text_align 0.5
        yalign 0.5
        size 25
        kerning 2
        outlines [(1, "#000", 0, 0)]
        idle_color "#fff"
        hover_color "#fff"

#style room_title_text is text:
#    outlines [(1, "#000", 0, 0)]
#    font FontGroup().add("Kinesis_Std_Italic.otf"

# style for debug screens
style small_debug_button is button:
    idle_background Frame('gui/stats_border.png', 12, 12)
    insensitive_background Frame(im.Grayscale('gui/stats_border.png'), 12, 12)


style small_debug_button_text is text:
    line_spacing 0
    insensitive_color '#555'
    selected_color '#0f0'
    hover_color '#ff0'


# reset default paddings and margins
style frame is default:
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0


style button is default:
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0


init -2:
    # this styles are from coding.rpy
    # TODO: check if these styles are used anywhere
    style statsname_box_text:
        xalign 0.5
        size 13
        color "#fff"
        kerning 5
        drop_shadow None
        outlines [ (0, "#fff", 0, 0) ]
    style statsname_box_vbox:
        ymaximum 100
        xmaximum 50
        xalign 0.5
    style statsname_box_grid:
        ymaximum 100
        ypadding 160
        xmaximum 150
        xalign 0
        ysize 320
        xsize 760
        yfill True
        xfill True


image thumb_idle = "gui/universal/ScrollBar.png"
image thumb_hover = im.MatrixColor("gui/universal/ScrollBar.png", im.matrix.opacity(1.0) * im.matrix.brightness(0.2))
image scrollbar_back = Solid('#343434')
# frames
image rect_highlight = Frame('gui/rect.png', 5, 5)
image listbox_border = Frame(im.MatrixColor('gui/rect.png', im.matrix.brightness(-0.5)), 5, 5)
image button_border = Frame(im.MatrixColor('gui/rect.png', im.matrix.brightness(-0.8)), 5, 5)
# cells grid for inventory/shop
image cells_grid = LiveTile(im.Scale('gui/inventory/item_cell.png', 66, 66))

#buttons
# back button
image norm_button = Frame('gui/universal/Button box.png', 30, 0)
image norm_button_grey = Frame(im.MatrixColor('gui/universal/Button box.png', im.matrix.brightness(-0.5)), 30, 0)
image norm_button_hover = Frame(im.MatrixColor('gui/universal/Button box.png', im.matrix.brightness(0.5)), 30, 0)
# inventory tab
image top_tab = Frame('gui/inventory/inventory_top_tab.png', 30, 0)
# rect with round corners
image rcrect = Frame('gui/rcrect.png', 5, 5)
image rcrect_grey = Frame(im.MatrixColor('gui/rcrect.png', im.matrix.brightness(-0.8)), 5, 5)
# rect with rounded left and right sides
image round_rect = Frame('gui/round_rect.png', 96, 0)
image round_rect_grey = Frame(im.MatrixColor('gui/round_rect.png', im.matrix.brightness(-0.5)), 96, 0)
image round_rect_hover = Frame(im.MatrixColor('gui/round_rect.png', im.matrix.brightness(0.5)), 96, 0)
# rect with thick border
image thick_rect = Frame('gui/thick_rect.png', 6, 6)
# "next" arrow
image next_arrow = 'gui/inventory/Button_Arrow_Neutral.png'
image next_arrow_null = 'gui/inventory/Button_Arrow_Null.png'
# "previous" arrow
image prev_arrow = im.Flip('gui/inventory/Button_Arrow_Neutral.png', horizontal=True)
image prev_arrow_null = im.Flip('gui/inventory/Button_Arrow_Null.png', horizontal=True)
# shop buttons
image angular_button_img = Frame(im.FactorScale('gui/shop/Item_button_Neutral_L.png', 0.5), 50, 0)
image angular_button_img_hover = Frame(im.FactorScale('gui/shop/Item_button_Pressed_L.png', 0.5), 50, 0)
# room buttons (angular buttons for room screen)
image room_button = Frame('gui/universal/Button_Room_neutral.png', 75, 0)
image room_button_hover = Frame('gui/universal/Button_Room_Hover.png', 75, 0)
image room_button_grey = Frame(im.MatrixColor('gui/universal/Button_Room_neutral.png', im.matrix.brightness(-0.05)), 75, 0)


init 1:
    style vscrollbar:
        base_bar Frame('scrollbar_back', 1, 1)
        xmaximum 12
        xminimum 12
        thumb "thumb_idle"
        hover_thumb "thumb_hover"
        thumb_offset 26
        thumb_shadow None
        top_gutter 26
        bottom_gutter 26


    # main caption for room screens
    style room_caption is text:
        size 25
        xalign 0.5
        ypos 45


    # secondary caption for room screens
    style sec_room_caption is text:
        size 20
        color '#686868'
        xalign 0.5
        ypos 75


    # room button
    style room_button is button:
        idle_background 'room_button'
        hover_background 'room_button_hover'
        selected_background 'room_button_hover'
        insensitive_background 'room_button_grey'
        top_padding 10
        bottom_padding 15
        xpadding 55

    style room_button_text is text:
        line_spacing 0
        align (0.5, 0.5)
        idle_color '#9c979b'
        hover_color '#eaeaea'
        insensitive_color '#373539'


    # listbox caption (room screens)
    style room_listbox_caption is text:
        pos (55, 100)
        size 20


    # "back" button for room screens
    style back_button is button:
        pos (31, 31)
        background 'norm_button'
        insensitive_background 'norm_button_grey'
        hover_background 'norm_button_hover'
        xpadding 12
        ypadding 5

    style back_button_text is text:
        line_spacing 0
        insensitive_color '#444'


    # quick menu button for dialogue screen
    style quick_button is button:
        background 'norm_button'
        insensitive_background 'norm_button_grey'
        hover_background 'norm_button_hover'
        xpadding 30
        ypadding 5

    style quick_button_text is text:
        line_spacing 0
        color '#3f3e3c'
        hover_color '#999'


    # rect button with round corners (prisoners management)
    style rcrect_button is textbutton:
#~         background 'rcrect'
#~         insensitive_background 'rcrect_grey'
#~         ysize 35
#~         xpadding 10
        background 'norm_button'
        insensitive_background 'norm_button_grey'
        hover_background 'norm_button_hover'
        xpadding 10
        ypadding 5

    style rcrect_button_text is text:
        line_spacing 0
        align (0.5, 0.5)
        color '#3f3e3c'
        hover_color '#999'


    # inventory top tab
    style top_tab is textbutton:
        background 'top_tab'
        ysize 64
        xpadding 30
        ypadding 5

    style top_tab_text is text:
        line_spacing 0
        align (0.5, 0.1)
        color '#464449'
        hover_color '#AFAFB1'
        selected_color '#AFAFB1'


    # button with round left and right sides
    style round_sides_button is button:
        background 'round_rect'
        insensitive_background 'round_rect_grey'
        hover_background 'round_rect_hover'
        ypadding 12
        text_align (0.5, 0.5)

    style round_sides_button_text is text:
        size 25
        line_spacing 0
        align (0.5, 0.5)
        color '#292929'


    # button for shop screen (with angular left and right)
    style angular_button is button:
        idle_background 'angular_button_img'
        hover_background 'angular_button_img_hover'
        xpadding 40
        ypadding 7
        text_align (0.5, 0.5)

    style angular_button_text is text:
        size 22
        line_spacing 0
        align (0.5, 0.5)
        color '#AFAFB1'
