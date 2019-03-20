init:
    # dummy placeholder image for the gallery
    image dummy = 'gui/char.png'

image compass surface="gui/compass.png"

image gattsublade_small = im.FactorScale("gui/main_gattsublade.png", 0.1)
image gattsublade_small2 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.5)), 0.1)
image gattsublade_small3 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0)), 0.1)
image gattsublade_large = "gui/main_gattsublade.png"
image gattsublade_large2 = im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.5))
image gattsublade_large3 = im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0))

image inventory_main_swap1 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap2 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.5)), 0.05)
image inventory_main_swap3 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0)), 0.05)
image inventory_main_swap4 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap5 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap6 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap7 = im.FactorScale("gui/main_gattsublade.png", 0.05)

###
#Credits
###
########################################################
##### C R E D I T S #######################################
########################################################

image next = "gui/next.png"
image prev:
    "gui/next.png"
    xzoom -1

image credits:
    contains:
        "black"
    contains:
        "cg1"
        alpha 0
        1.0
        linear 5.0 alpha 1.0
        5.0
        linear 5.0 alpha 0
    contains:
        "cg2"
        alpha 0
        8.0
        linear 5.0 alpha 1.0
        5.0
        linear 5.0 alpha 0
    contains:
        "cg3"
        alpha 0
        13.0
        linear 5.0 alpha 1.0
        5.0
        linear 5.0 alpha 0
    contains:
        Text([
    "{b}{size=26}My Company \n \n \n"
    "\nCreated by{/b} \nPerson \n \n \n"
    "\nWritten by{/b} \nPerson \n \n \n"
    "\nArt \nPerson \n \n \n"
    "\nProgramming \nPerson \n \n \n"
    #"\n{size=-5}{image=gui/company_logo.png}{/size}"
    ], outlines=[(1, "#000000", 0, 0)], text_align=0.5, color="#ffffff")
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        2.0
        linear 30.0 ypos 0.0 yanchor 1.0

