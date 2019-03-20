# You can place the script of your game in this file.

init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)



init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
  Solid("#000")
image white:
  Solid("#FFF")


#

init:
    $ midright = Position(xalign=0.7)
    $ midleft = Position(xalign=0.35)
    $ edgeright = Position(xpos=0.88,xanchor=0.5)
    $ edgeleft= Position(xpos=0.1,xanchor=0.4)
    $ orcright = Position(xpos=0.83,xanchor=0.5)
    $ roleft = Position(xpos=0.32,xanchor=0.5)
    $ skorright = Position(xpos=0.86,xanchor=0.5)
    $ trueedgeleft = Position(xpos=0.1,xanchor=0.55)
    $ midedgeleft = Position(xalign=0.25)
    $ cliohnaright = Position(xalign=0.90)
    $ midmidright = Position(xalign=0.6)
init:
    define flash = Fade(.25, 0.0, .75, color="#fff")
    define redflash = Fade(.25, 0.0, .75, color="#8A0808")
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ smallshake = Shake((0, 0, 0, 0), 0.5, dist=7)


transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#fff", image="char", kerning=15, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed")
define narrator = Character(' ', color="#fff", kerning=15, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed")
image char = "gui/char.png"
image char happy = "gui/char.png"
image side char happy = LiveCrop((0, 0, 300, 300),"gui/char.png")
image char2= "gui/char.png"
image back = "gui/back.png"
image splash = "gui/splashscreen.png"
image white = "#fff"
image rowan_encyclopedia_image1 = im.Crop(im.FactorScale(im.Sepia("gui/back.png"), 0.7), 0, 100, 817, 200)
image lily_encyclopedia_image1 = im.Crop(im.FactorScale(im.Sepia("gui/back.png"), 0.7), 0, 100, 817, 200)
image peter_encyclopedia_image1 = im.Crop(im.FactorScale(im.Sepia("gui/back.png"), 0.7), 0, 100, 817, 200)


#Characters

define ro = Character ('[rowan_name]', image = "rowan", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ro"))
define el = Character ('Elder', image = "village", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("el"))
define al = Character ('[alexia_name]', image = "alexia", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("al"))
define je = Character ('[jezera_name]', image = "jezera", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("je"))
define wo = Character ('Wild Orc', image = "wild", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wo"))
define an = Character ('[andras_name]', image = "andras", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("an"))
define cm = Character ('???', kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed")
define os = Character ('Orc Soldier', image = "orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("os"))
define qm = Character ('???', image = "",kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("??"))
define sk = Character ('[skordred_name]', image = "skordred", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sk"))
define cl = Character ('[cliohna_name]', image = "cliohna", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cl"))
define xz = Character ("X'zaratl", image = "xzaratl", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("xz"))
define gh = Character ("Greyhide", image = "greyhide", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gh"))
define cla = Character ("[cla_min_name]", image = "clamin", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cla"))
define ind = Character ("Indarah", image = "indarah", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ind"))
define hel = Character ("Helayna", image = "helayna", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hel"))
define dra = Character ("Draith", image = "draith", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dra"))
define dor = Character ("Doran", image = "doran", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dor"))
define rkn = Character ("Rosarian Knight", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rkn"))
define rnb = Character ("Rosarian Noble", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rnb"))
define bri = Character ("Brinnid", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bri"))
define oll = Character ("Ollia", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("oll"))
define cook = Character ("Orc Cook", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cook"))
define orcs = Character ("Orcs", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcs"))
# temporary character for "andras challenge"
define cro = Character ("Crowd", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("crowd"))
# temporary character for "jezera_s_alliance_making_skills"
define wom = Character ("Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wom"))
# temporary character for "the_trapped_dryad"
define dry = Character ("[dryadName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dry"))
define sha = Character ('[shaya_name]', image = "shaya", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sha"))
# Tania for Arthdale quest
define tan = Character ('[tania_name]', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tan"))
define tempspy = Character ('[tmp_spy.name]', image = "tempspy_image", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tempspy"))
define brig = Character ("Brigand Leader", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("brig"))
define slave = Character ("Slave", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("slave"))
define archer = Character ("Elven Archer", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("archer"))
define bow = Character ("Cla-Bow", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bow"))
define mhunter = Character ("Monster Hunter", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mhunter"))
define tamir = Character ("Tamir", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tamir"))
define gar = Character ('[garforth_name]', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gar"))
define tar = Character ('[tarish_name]', image = "tarish", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tar"))
define bat = Character ('Batri', image = "batri", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bat"))
define ulc = Character ('Ulcro', image = "ulcro", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ulc"))
define cov = Character ('Coven Leader', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cov"))
define femorc = Character ("Female Orc", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("forc"))
define ele = Character ('[eleanor_name]', image = "eleanor", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ele"))
define eid = Character ('Eidood', image = "eleanor", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("eid"))
define wisp = Character ("[wispName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wisp"))
define kron = Character ("Kronn, God of Death", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("kron"))
define witch = Character ("[witchName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("witch"))
define liur = Character ('[Liurialname]', image = "liurial", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("liur"))
define nil = Character ('Nileth', image = "nileth", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nil"))
define dag = Character ("Daggertongue", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dag"))
define arz = Character ('Arzyl', image = "arzyl", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("arz"))
define shy = Character ("Shyrenthe", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("shy"))
define est = Character ("Estraea", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("est"))
define man = Character ("Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("man"))
define lorc = Character ("Limping Orc", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lorc"))
define orcp = Character ("Orc Priest", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcp"))
define orca = Character ("Orc Acolyte", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orca"))
define orcm = Character ("[matronName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcm"))
define emm = Character ("Emma", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("emm"))
define orc1 = Character ("[orcName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orc1"))
define orc2 = Character ("Orc 2", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orc2"))
define jak = Character ("Jak", image = "jak", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("jak"))
define aga = Character ("[agathaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aga"))
define aco = Character ("Acolyte", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aco"))
define daz = Character ("Dazzanath", image = "dazzanath", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("daz"))
define orcl = Character ("Orc Leader", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcl"))
define suc = Character ("Succubus", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("suc"))
define maid = Character ("Maid", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("maid"))
define ame = Character ("Amelia", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ame"))
define shee = Character ("[sheenaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("shee"))
define qais = Character ("[qaisName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("qais"))
define bern = Character ("[bernName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bern"))
define isaa = Character ("[isaaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("issa"))
define care = Character ("[caretakerName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("care"))
define snag = Character ("[snagName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("snag"))
define krau = Character ("Kraug", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("krau"))
define isdr = Character ("Isdruel", image = "isdruel", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("isdr"))
define peas = Character ("Peasant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("peas"))
define hear = Character ("Heartsong", image = "heartsong", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hear"))
define mary = Character ("Mary", image = "mary", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mary"))
define pris = Character ("Prisoner", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("pris"))
define joff = Character ("Sir Joffrey", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("joff"))
define nive = Character ("Lady Nive", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nive"))
define rosa = Character ("Lady Rosalie", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rosa"))
define lysa = Character ("Sir Lysander", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lysa"))
define harry = Character ("Horrid Harry", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("harry"))
define orcb = Character ("Orc Bandit", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcb"))
define whit = Character ("[whitescarName]", image = "whitescar", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("whit"))
define larry = Character ("[larryName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("larry"))
define omar = Character ("[omarName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("omar"))
define argo = Character ("[argoName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("argo"))
define ygris = Character ("[ygrissName]", image = "ygriss", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ygris"))
define pot = Character ("[potName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("pot"))
define werd = Character ("Duke Werden", image = "werden", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("werd"))
define mari = Character ("Marianne", image = "marianne", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mari"))
define casi = Character ("Baron Casimir", image = "casimir", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("casi"))
define patr = Character ("Patricia", image = "patricia", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("patr"))
define jacq = Character ("Jacques", image = "jacques", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("jacq"))
define amer = Character ("[amerName]", image = "ameraine", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("amer"))
define juli = Character ("Juliet", image = "juliet", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("juli"))
define crev = Character ("[crevName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("crev"))
define halfm = Character ("Half Minotaur Girl", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("halfm"))
define succ = Character ("Succubus", image = "succubus", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succ"))
define succ2 = Character ("Succubus", image = "succubus", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succ2"))
define comm = Character ("Commander", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("comm"))
define omaid = Character ("Other Maid", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("omaid"))
define serv = Character ("Servant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("serv"))
define jont = Character ("Jon", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("jont"))
define merc = Character ("Mercenary", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("merc"))
define quest = Character ("???", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("quest"))
define young = Character ("Young Aspirant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("young"))
define leatwom = Character ("Leather Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("leatwom"))
define opris = Character ("Other Prisoner", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("opris"))
define inq = Character ("Inquisitor", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("inq"))
define nas = Character ("Nasim", image = "nasim", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nas"))
define boot = Character ("[BootlegName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("boot"))
define cat = Character ("[cat_name]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cat"))
define man = Character ("Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("man"))
define aman = Character ("Another Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aman"))
define bwom = Character ("Bar Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bwom"))

################################################################################
# Character names for the start of the game
default rowan_name = 'Rowan'
default alexia_name = 'Alexia'
default cliohna_name = 'Cliohna'
default cla_min_name = 'Cla-Min'
default skordred_name = 'Skordred'
default shaya_name = 'Shaya'
default tania_name = 'Woman'
default garforth_name = 'Man'
default tarish_name = 'Female Orc'
define eleanor_name = 'Woman'
default matronName = '???'
default orcName = '???'
default agathaName = '???'
default sheenaName = "Voice 2"
default qaisName = "Voice 1"
default isaaName = "Voice 3"
default caretakerName = "Caretaker"
default snagName = '???'
default Liurialname = "Woman"
default whitescarName ="Beastman"
default larryName = "Man #1"
default omarName = "Man #2"
default argoName = "???"
default ygrissName = "Dragon Ogre"
default potName = "???"
default amerName = "Mystery Woman"
default crevName = "Man"
default BootlegName = "Bootleg Alexia"
default cat_name = "Cat"

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Rowan

image rowan intro neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro neutral side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro neutral naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro neutral naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro neutral naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro neutral naked side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro happy side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro smug = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro smug.png",
    (9, 14), "rowan eyes smug",
    )

image side rowan intro smug = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro neutral side.png",
    (0, 1), "rowan eyes smug",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed smirk.png"),
    )

image rowan intro aroused  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro aroused.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro aroused side.png",
    (0, 1), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro aroused naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro aroused naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro aroused naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro aroused naked side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro naked = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan intro naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro naked side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan happy side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan neutral side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan shock.png",
    )

image side rowan shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan shock side.png",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed shock.png"),
    )

image rowan attack = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan attack.png",
    )

image side rowan attack = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan neutral side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan jail neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan jail neutral.png",
    (11, 15), "rowan eyes normal",
    )

image side rowan jail neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan jail neutral side.png",
    (-9, 12), "rowan eyes normal",
    (-6, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan jail hurt = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan jail hurt.png"
    )

image side rowan jail hurt = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan jail hurt side.png",
    (-19, -4), WhileSpeaking("ro", "rowan mouth jail", "Sprites/Rowan/rowan jail mouth.png"),
    )

image rowan jail dirty = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan jail dirty.png",
    (11, 15), "rowan eyes normal",
    )

image side rowan jail dirty = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan jail dirty side.png",
    (-9, 12), "rowan eyes normal",
    (-6, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )


image rowan aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan aroused.png"
    )

image side rowan aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan aroused side.png",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan aroused mouth.png"),
    )

image rowan necklace happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace happy side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan necklace neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace neutral side.png",
    (-8, 11), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro necklace happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro necklace happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro necklace happy side.png",
    (-9, 12), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro necklace neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro necklace neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro necklace neutral side.png",
    (-9, 12), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro necklace angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro necklace angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro necklace angry side.png",
    (-9, 12), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan necklace shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace shock.png",
    )

image side rowan necklace shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace shock side.png",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed shock.png"),
    )

image rowan necklace sad = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan necklace sad.png",
    (18, 6), "rowan eyes sad",
    )

image side rowan necklace sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace sad side.png",
    (0, 1), "rowan eyes sad",
    (-9, 9), WhileSpeaking("ro", "rowan mouth normal",),
    )

image rowan necklace angry = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan necklace angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace angry side.png",
    (-9, 12), "rowan eyes normal",
    (-9, 9), WhileSpeaking("ro", "rowan mouth normal",),
    )


image rowan hood neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan hood neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan hood neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan hood neutral side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace aroused naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace aroused naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace aroused naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace aroused naked side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan necklace naked = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan necklace naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )


image rowan necklace naked sad = LiveComposite(
    (323, 600),
    (-9, 10), "Sprites/Rowan/rowan necklace naked sad.png",
    (9, 14), "rowan eyes sad",
    )

image side rowan necklace naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked sad side.png",
    (0, 1), "rowan eyes sad",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace naked concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace naked concerned.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked concerned side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace aroused  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace aroused.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace aroused side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan necklace concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace concerned.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace concerned side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )


image rowan necklace naked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace naked neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked neutral side.png",
    (-8, 11), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace naked angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace naked angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked angry side.png",
    (-8, 11), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )


image rowan eyes normal:
    "Sprites/Rowan/rowan eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Rowan/rowan eyes half closed.png"
    0.1
    "Sprites/Rowan/rowan eyes closed.png"
    .25
    repeat

image rowan eyes smug:
    "Sprites/Rowan/rowan eyes smug.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Rowan/rowan eyes half closed.png"
    0.1
    "Sprites/Rowan/rowan eyes closed.png"
    .25
    repeat

image rowan eyes sad:
    "Sprites/Rowan/rowan eyes sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Rowan/rowan eyes half closed 2.png"
    0.1
    "Sprites/Rowan/rowan eyes closed 2.png"
    .25
    repeat

image rowan mouth normal:
    "Sprites/Rowan/rowan mouth speak1.png"
    .2
    "Sprites/Rowan/rowan mouth speak2.png"
    .2
    repeat

image rowan mouth jail:
    "Sprites/Rowan/rowan jail mouth speak1.png"
    .2
    "Sprites/Rowan/rowan jail mouth speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Village Elder

image village elder neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Village Elder/village elder neutral.png",
    (0, 0), "village elder eyes normal",
    )

image village elder happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Village Elder/village elder happy.png",
    (0, 0), "village elder eyes normal",
    )

image side village elder happy = LiveComposite(
    (285, 300),
    (0, 0), "Sprites/Village Elder/Side/village elder happy side.png",
    (-20, -38), "village elder eyes normal",
    (0, 0), WhileSpeaking("el", "village elder mouth normal", "Sprites/Village Elder/village elder mouth closed happy.png"),
    )

image village elder wounded = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Village Elder/village elder wounded.png",
    (0, 0), "village elder eyes normal",
    )

image side village elder wounded = LiveComposite(
    (285, 300),
    (0, 0), "Sprites/Village Elder/Side/village elder wounded side.png",
    (-17, -36), "village elder eyes normal",
    (0, 0), WhileSpeaking("el", "village elder mouth wounded"),
    )


image village elder eyes normal:
    "Sprites/Village Elder/village elder eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Village Elder/village elder eyes half closed.png"
    0.1
    "Sprites/Village Elder/village elder eyes closed.png"
    .25
    repeat

image village elder mouth normal:
    "Sprites/Village Elder/village elder mouth speak1.png"
    .2
    "Sprites/Village Elder/village elder mouth speak2.png"
    .2
    repeat

image village elder mouth wounded:
    "Sprites/Village Elder/village elder wounded mouth speak1.png"
    .2
    "Sprites/Village Elder/village elder wounded mouth speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Alexia

image alexia intro neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia intro neutral.png",
    (19, 35), "alexia eyes normal",
    )

image side alexia intro neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro neutral side.png",
    (0, 0), "alexia eyes normal",
    (1, -2), WhileSpeaking("al", "alexia mouth normal", "Sprites/Alexia/alexia mouth closed neutral.png"),
    )

image alexia intro aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro aroused.png",
    (19, 35), "alexia eyes normal",
    )

image side alexia intro aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro aroused side.png",
    (0, 0), "alexia eyes aroused",
    (1, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth aroused.png"),
    )

image alexia intro aroused naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro aroused naked.png",
    (-6, -28), "alexia eyes normal",
    )

image side alexia intro aroused naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro aroused naked side.png",
    (0, 0), "alexia eyes aroused",
    (1, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth aroused.png"),
    )

image alexia intro naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro naked.png",
    (0, 0), "alexia eyes normal",
    )

image side alexia intro naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro naked side.png",
    (0, 0), "alexia eyes normal",
    (1, -2), WhileSpeaking("al", "alexia mouth normal", "Sprites/Alexia/alexia mouth closed neutral.png"),
    )

image alexia intro concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia intro concerned.png",
    (19, 35), "alexia eyes concerned",
    )

image side alexia intro concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro concerned side.png",
    (0, 0), "alexia eyes concerned",
    (0, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth concerned.png"),
    )

image alexia intro concerned naked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia intro concerned naked.png",
    (19, 35), "alexia eyes concerned",
    )

image side alexia intro concerned naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro concerned naked side.png",
    (0, 0), "alexia eyes concerned",
    (1, 0), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth concerned.png"),
    )

image alexia intro naked laugh = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro naked.png",
    (0, 0), "Sprites/Alexia/alexia eyes happy.png",
    )

image side alexia intro naked laugh = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro naked side.png",
    (0, 0), "Sprites/Alexia/alexia eyes happy.png",
    (1, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia open mouth speak2.png"),
    )


image alexia white neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia white neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia white neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia white neutral side.png",
    (0, -3), "alexia eyes normal",
    (0, 0), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia white happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia white happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia white happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia white happy side.png",
    (0, -3), "alexia eyes normal",
    (0, 0), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia white concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia white concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia white concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia white neutral side.png",
    (0, -3), "alexia eyes normal",
    (0, 0), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace neutral side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace concerned side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace shocked.png",
    )

image side alexia necklace shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace shocked side.png",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace happy side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace hopeful = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace hopeful.png",
    (0, 0), "alexia eyes hopeful",
    )

image side alexia necklace hopeful = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace hopeful side.png",
    (-19, -60), "alexia eyes hopeful",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace eyes closed = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace eyes closed.png",
    )

image side alexia necklace eyes closed = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace eyes closed side.png",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace angry side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace look away = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace look away.png",
    (0, 0), "alexia eyes look away",
    )

image side alexia necklace look away = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace look away side.png",
    (-19, -60), "alexia eyes look away",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace sad = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace sad.png",
    (0, 0), "alexia eyes sad",
    )

image side alexia necklace sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace look away side.png",
    (-19, -60), "alexia eyes sad",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace aroused side.png",
    (4, 5), "alexia eyes aroused",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked aroused side.png",
    (4, 5), "alexia eyes aroused",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked shocked.png",
    )

image side alexia necklace naked shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked shocked side.png",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )


### dress 2 ###

image alexia 2 necklace neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace neutral side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white"),
    )

image alexia 2 necklace concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace concerned side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia 2 necklace shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace shocked.png",
    )

image side alexia 2 necklace shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace shocked side.png",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia 2 necklace happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace happy side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia 2 necklace angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace angry side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia 2 necklace look away = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace look away.png",
    (0, 0), "alexia eyes look away",
    )

image side 2 alexia necklace look away = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace look away side.png",
    (-23, -57), "alexia eyes look away",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia 2 necklace aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace aroused.png",
    (23, 62), "alexia eyes aroused",
    )

image side alexia 2 necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace aroused side.png",
    (0, 5), "alexia eyes aroused",
    (0, 8), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth aroused.png"),
    )


image alexia necklace naked concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked concerned side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace naked angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked angry side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked sad = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked sad.png",
    (0, 0), "alexia eyes sad",
    )

image side alexia necklace naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked sad side.png",
    (-23, -55), "alexia eyes sad",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )



### jobs ###

image alexia librarian neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia librarian neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia librarian neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia librarian neutral side.png",
    (10, -9), "alexia eyes normal",
    (12, -3), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia maid neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia maid neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid neutral side.png",
    (10, -9), "alexia eyes normal",
    (12, -3), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia maid aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid aroused.png",
    (23, 62), "alexia eyes aroused",
    )

image side alexia maid aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid aroused side.png",
    (10, -9), "alexia eyes aroused",
    (0, 0), WhileSpeaking("al", "alexia maid aroused talk", "Sprites/Alexia/alexia maid aroused mouth.png"),
    )


image alexia maid happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia maid happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid neutral side.png",
    (10, -9), "alexia eyes normal",
    (12, -3), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia maid shock = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid shock.png",
    )

image side alexia maid shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid shock side.png",
    (13, -10), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia maid sad = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid sad.png",
    (0, 0), "alexia eyes sad",
    )

image side alexia maid sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid sad side.png",
    (-11, -71), "alexia eyes sad",
    (12, -10), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia barmaid neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid neutral side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid happy side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid concerned side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid shocked side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid angry side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid aroused side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge neutral side.png",
    (12, 5), "alexia eyes normal",
    (15, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge concerned side.png",
    (12, 5), "alexia eyes normal",
    (15, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge shocked side.png",
    (12, 5), "alexia eyes normal",
    (15, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding neutral side.png",
    (6, -5), "alexia eyes normal",
    (8, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding happy side.png",
    (6, -5), "alexia eyes normal",
    (8, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding concerned side.png",
    (6, -5), "alexia eyes normal",
    (8, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding shocked side.png",
    (6, -5), "alexia eyes normal",
    (8, -5), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding aroused side.png",
    (11, -5), "alexia eyes normal",
    (12, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia eyes normal:
    "Sprites/Alexia/alexia eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed.png"
    0.1
    "Sprites/Alexia/alexia eyes closed.png"
    .25
    repeat

image alexia eyes aroused:
    "Sprites/Alexia/alexia eyes half closed.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes closed.png"
    .25
    repeat

image alexia eyes concerned:
    "Sprites/Alexia/alexia eyes concerned.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed.png"
    0.1
    "Sprites/Alexia/alexia eyes closed.png"
    .25
    repeat

image alexia eyes hopeful:
    "Sprites/Alexia/alexia eyes hopeful.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed 2.png"
    0.1
    "Sprites/Alexia/alexia eyes closed 2.png"
    .25
    repeat

image alexia eyes look away:
    "Sprites/Alexia/alexia eyes look away.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed 2.png"
    0.1
    "Sprites/Alexia/alexia eyes closed 2.png"
    .25
    repeat

image alexia eyes sad:
    "Sprites/Alexia/alexia eyes sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed 2.png"
    0.1
    "Sprites/Alexia/alexia eyes closed 2.png"
    .25
    repeat

image alexia mouth normal:
    "Sprites/Alexia/alexia mouth speak1.png"
    .2
    "Sprites/Alexia/alexia mouth speak2.png"
    .2
    repeat

image alexia mouth open:
    "Sprites/Alexia/alexia open mouth speak1.png"
    .2
    "Sprites/Alexia/alexia open mouth speak2.png"
    .2
    repeat

image alexia mouth white:
    "Sprites/Alexia/alexia mouth speak1 white.png"
    .2
    "Sprites/Alexia/alexia mouth speak2 white.png"
    .2
    repeat

image alexia maid aroused talk:
    "Sprites/Alexia/alexia maid aroused talk 1.png"
    .2
    "Sprites/Alexia/alexia maid aroused talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Jezera

image jezera disguised hood worried = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro hood worried.png",
    (0, 0), "jezera disguised eyes worried",
    )

image side jezera disguised hood worried = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro hood worried side.png",
    (-21, -16), "jezera disguised eyes worried",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )

image jezera disguised hood crying = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro hood crying.png",
    (0, 0), "jezera disguised eyes crying",
    )

image side jezera disguised hood crying = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro hood crying side.png",
    (-21, -16), "jezera disguised eyes crying",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )

image jezera disguised worried = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro worried.png",
    (0, 0), "jezera disguised eyes worried",
    )

image side jezera disguised worried = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro worried side.png",
    (-21, -16), "jezera disguised eyes worried",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )


image jezera disguised crying = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro crying.png",
    (0, 0), "jezera disguised eyes crying",
    )

image side jezera disguised crying = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro crying side.png",
    (-21, -16), "jezera disguised eyes crying",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )

image jezera disguised neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro neutral.png",
    (0, 0), "jezera disguised eyes worried",
    )

image side jezera disguised neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro neutral side.png",
    (-21, -16), "jezera disguised eyes worried",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )


image jezera disguised happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro happy.png",
    )

image side jezera disguised happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro happy side.png",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal", "Sprites/Jezera/jezera mouth closed happy.png"),
    )

image jezera disguised smirk = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro smirk.png",
    (0, 0), "jezera disguised eyes smirk",
    (-0, -0), "Sprites/Jezera/jezera mouth closed smirk.png",
    )

image side jezera disguised smirk = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro smirk side.png",
    (-21, -16), "jezera disguised eyes smirk",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal", "Sprites/Jezera/jezera mouth closed smirk.png"),
    )

image jezera naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera naked happy.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera naked happy side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )

image jezera neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera neutral.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera neutral side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )


image jezera happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera happy.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera happy side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )

image jezera hands happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera hands happy.png",
    (0, 0), "jezera eyes hands",
    )

image side jezera hands happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera happy side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )

image jezera displeased = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera displeased.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera displeased = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera displeased side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )


image jezera disguised eyes worried:
    "Sprites/Jezera/jezera eyes worried.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera eyes closed.png"
    .25
    repeat

image jezera disguised eyes crying:
    "Sprites/Jezera/jezera eyes crying.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera eyes closed.png"
    .25
    repeat

image jezera disguised eyes smirk:
    "Sprites/Jezera/jezera eyes smirk.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera eyes closed.png"
    .25
    repeat

image jezera eyes normal:
    "Sprites/Jezera/jezera demon eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera demon eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera demon eyes closed.png"
    .25
    repeat

image jezera eyes hands:
    "Sprites/Jezera/jezera demon eyes hands open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera demon eyes hands half closed.png"
    0.1
    "Sprites/Jezera/jezera demon eyes hands closed.png"
    .25
    repeat


image jezera disguised mouth normal:
    "Sprites/Jezera/jezera mouth speak1.png"
    .2
    "Sprites/Jezera/jezera mouth speak2.png"
    .2
    repeat

image jezera mouth normal:
    "Sprites/Jezera/jezera demon mouth speak1.png"
    .2
    "Sprites/Jezera/jezera demon mouth speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Wild Orc

image wild orc neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Wild Orc/wild orc neutral.png",
    )

image side wild orc neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Wild Orc/Side/wild orc neutral side.png",
    (0, 0), WhileSpeaking("wo", "wild orc mouth normal"),
    )

image wild orc wounded = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Wild Orc/wild orc wounded.png",
    )

image side wild orc wounded = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Wild Orc/Side/wild orc wounded side.png",
    (0, 0), WhileSpeaking("wo", "wild orc mouth wounded"),
    )

image wild orc mouth wounded:
    "Sprites/Wild Orc/wild orc wounded speak1.png"
    .2
    "Sprites/Wild Orc/wild orc wounded speak2.png"
    .2
    repeat

image wild orc mouth normal:
    "Sprites/Wild Orc/wild orc speak1.png"
    .2
    "Sprites/Wild Orc/wild orc speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#andras

image andras displeased = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras displeased.png",
    (0, 0), "andras eyes normal",
    )

image side andras displeased = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras mouth closed.png"),
    )

image andras displeased hands = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras displeased hands.png",
    (0, 0), "andras eyes normal",
    )

image side andras displeased hands = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras mouth closed.png"),
    )

image andras angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras angry.png",
    )

image side andras angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras mouth closed.png"),
    )

image andras smirk = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras smirk.png",
    (0, 0), "andras eyes normal",
    )

image side andras smirk = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras smirk mouth closed.png"),
    )

image andras happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras happy.png",
    (0, 0), "andras eyes normal",
    )

image side andras happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras happy side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal","Sprites/Andras/andras mouth smile.png"),
    )

image andras eyes normal:
    "Sprites/Andras/andras eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Andras/andras eyes half closed.png"
    0.1
    "Sprites/Andras/andras eyes closed.png"
    .25
    repeat


image andras mouth normal:
    "Sprites/Andras/andras speak1.png"
    .2
    "Sprites/Andras/andras speak2.png"
    .2
    repeat


#disguised

image andras disguised neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised neutral.png",
    )

image side andras disguised neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised neutral side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised talk 1.png"),
    )

image andras disguised happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised happy.png",
    )

image side andras disguised happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised neutral side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised talk 1.png"),
    )

image andras disguised smirk = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised smirk.png",
    )

image side andras disguised smirk = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised neutral side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised mouth smirk.png"),
    )


image andras disguised angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised angry.png",
    )

image side andras disguised angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised angry side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised mouth angry.png"),
    )


image andras mouth disguised:
    "Sprites/Andras/andras disguised talk 1.png"
    .2
    "Sprites/Andras/andras disguised talk 2.png"
    .2
    repeat




#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#orc soldier

image orc soldier neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Orc Soldier/orc soldier neutral.png"
    )

image side orc soldier neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Orc Soldier/Side/orc soldier neutral side.png",
    (0, 0), WhileSpeaking("os", "orc soldier mouth normal"),
     xoffset=-30)


image orc soldier mouth normal:
    "Sprites/Orc Soldier/orc soldier talk 1.png"
    .2
    "Sprites/Orc Soldier/orc soldier talk 2.png"
    .2
    repeat


init -2:
    image ctc_icon:
        "gui/stats_strength.png"
        xpos 0.95
        ypos 0.9
        alpha 0.7
        linear 1.0 rotate 360
        0.75
        repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#skordred

image skordred neutral = LiveComposite(
    (457, 521),
    (0, 0), "Sprites/Skordred/skordred neutral.png",
    (0, 0), "skordred eyes normal",
    )

image side skordred neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Skordred/Side/skordred neutral side.png",
    (0, 0), WhileSpeaking("sk", "skordred mouth normal"),
     xoffset=-10)

image skordred happy = LiveComposite(
    (457, 521),
    (0, 0), "Sprites/Skordred/skordred happy.png",
    )

image side skordred happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Skordred/Side/skordred neutral side.png",
    (0, 0), WhileSpeaking("sk", "skordred mouth normal"),
     xoffset=-10)

image skordred angry = LiveComposite(
    (457, 521),
    (0, 0), "Sprites/Skordred/skordred angry.png",
    )

image side skordred angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Skordred/Side/skordred neutral side.png",
    (0, 0), WhileSpeaking("sk", "skordred mouth normal"),
     xoffset=-10)

image skordred eyes normal:
    "Sprites/Skordred/skordred eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Skordred/skordred eyes half closed.png"
    0.1
    "Sprites/Skordred/skordred eyes closed.png"
    .25
    repeat

image skordred mouth normal:
    "Sprites/Skordred/skordred talk 1.png"
    .2
    "Sprites/Skordred/skordred talk 2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Cliohna


image cliohna neutral = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna neutral.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna neutral side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )

image cliohna angry = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna angry.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna angry side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )

image cliohna happy = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna happy.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna happy side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )



image cliohna eyes normal:
    "Sprites/Cliohna/cliohna eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Cliohna/cliohna eyes half closed.png"
    0.1
    "Sprites/Cliohna/cliohna eyes closed.png"
    .25
    repeat

image cliohna mouth normal:
    "Sprites/Cliohna/cliohna speak1.png"
    .2
    "Sprites/Cliohna/cliohna speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# X'Zaratl


image xzaratl neutral = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl neutral.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl neutral side.png",
    (-123, -2), "xzaratl eyes normal",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)

image xzaratl naked = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl neutral.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl naked side.png",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)




image xzaratl eyes normal:
    "Sprites/Xzaratl/xzaratl eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Xzaratl/xzaratl eyes half closed.png"
    0.1
    "Sprites/Xzaratl/xzaratl eyes closed.png"
    .25
    repeat

image xzaratl mouth normal:
    "Sprites/Xzaratl/xzaratl speak1.png"
    .2
    "Sprites/Xzaratl/xzaratl speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Greyhide

image greyhide neutral = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Greyhide/greyhide neutral.png",
    (0, 0), "greyhide eyes normal",
    )

image side greyhide neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Greyhide/Side/greyhide neutral side.png",
    (0, 0), WhileSpeaking("gh", "greyhide mouth normal"),
     xoffset=-20)

image greyhide sad = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Greyhide/greyhide sad.png",
    (0, 0), "greyhide eyes normal",
    )

image side greyhide sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Greyhide/Side/greyhide neutral side.png",
    (0, 0), WhileSpeaking("gh", "greyhide mouth normal"),
     xoffset=-20)

image greyhide eyes normal:
    "Sprites/Greyhide/greyhide eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Greyhide/greyhide eyes half closed.png"
    0.1
    "Sprites/Greyhide/greyhide eyes closed.png"
    .25
    repeat

image greyhide mouth normal:
    "Sprites/Greyhide/greyhide speak1.png"
    .2
    "Sprites/Greyhide/greyhide speak2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Cla-Min

image clamin neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin neutral.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin neutral pipe = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin neutral pipe.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin neutral pipe = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin happy.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin annoyed = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin annoyed.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin annoyed = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin angry.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin sad.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin eyes normal:
    "Sprites/Clamin/clamin eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Clamin/clamin eyes half closed.png"
    0.1
    "Sprites/Clamin/clamin eyes closed.png"
    .25
    repeat

image clamin mouth normal:
    "Sprites/Clamin/clamin talk1.png"
    .2
    "Sprites/Clamin/clamin talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Indarah

image indarah neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Indarah/indarah neutral.png",
    (0, 0), "indarah eyes normal",
    )

image side indarah neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Indarah/Side/indarah neutral side.png",
    (-21, -24), "indarah eyes normal",
    (0, 0), WhileSpeaking("ind", "indarah mouth normal"),
    )

image indarah shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Indarah/indarah shock.png",
    )

image side indarah shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Indarah/Side/indarah neutral side.png",
    (-21, -24), "indarah eyes normal",
    (0, 0), WhileSpeaking("ind", "indarah mouth normal"),
    )

image indarah naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Indarah/indarah naked.png",
    (0, 0), "indarah eyes normal",
    )

image side indarah naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Indarah/Side/indarah naked side.png",
    (-21, -24), "indarah eyes normal",
    (0, 0), WhileSpeaking("ind", "indarah mouth normal"),
    )


image indarah eyes normal:
    "Sprites/Indarah/indarah eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Indarah/indarah eyes half closed.png"
    0.1
    "Sprites/Indarah/indarah eyes closed.png"
    .25
    repeat

image indarah mouth normal:
    "Sprites/Indarah/indarah talk 1.png"
    .2
    "Sprites/Indarah/indarah talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Helayna

image helayna neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna neutral.png",
    (0, 0), "helayna eyes neutral",
    )

image side helayna neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna neutral side.png",
    (-19, 0), "helayna eyes neutral",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna shocked.png",
    )

image side helayna shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna shocked side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna happy.png",
    (0, 0), "helayna eyes happy",
    )

image side helayna happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna happy side.png",
    (-18, 0), "helayna eyes happy",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal", "Sprites/Helayna/helayna mouth happy.png"),
    )

image helayna sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna sad.png",
    (0, 0), "helayna eyes sad",
    )

image side helayna sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna sad side.png",
    (-18, 0), "helayna eyes sad",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna angry.png",
    (0, 0), "helayna eyes angry",
    )

image side helayna angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna angry side.png",
    (-18, 0), "helayna eyes angry",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna crying = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna crying.png",
    )

image side helayna crying = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna crying side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna aroused.png",
    )

image side helayna aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna aroused side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna naked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked neutral.png",
    )

image side helayna naked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked neutral side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked happy.png",
    )

image side helayna naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked happy side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna naked sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked sad.png",
    )

image side helayna naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked sad side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna naked aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked aroused.png",
    )

image side helayna naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked aroused side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna 2 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 neutral.png",
    (0, 0), "helayna eyes neutral",
    )

image side helayna 2 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 neutral side.png",
    (-23, 0), "helayna eyes neutral",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna 2 happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 happy.png",
    (0, 0), "helayna eyes happy",
    )

image side helayna 2 happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 happy side.png",
    (-32, 0), "helayna eyes happy",
    (-16, 0), WhileSpeaking("hel", "helayna mouth normal", "Sprites/Helayna/helayna mouth happy.png"),
    )

image helayna 2 aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 aroused.png",
    )

image side helayna 2 aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 aroused side.png",
    (-16, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna 2 concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 concerned.png",
    (0, 0), "helayna eyes sad",
    )

image side helayna 2 concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 concerned side.png",
    (-23, 0), "helayna eyes sad",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna collar neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar neutral.png",
    (0, 0), "helayna eyes neutral",
    )

image side helayna collar neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar neutral side.png",
    (-23, 0), "helayna eyes neutral",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna collar aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar aroused.png",
    )

image side helayna collar aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar aroused side.png",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna collar naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar naked happy.png",
    (0, 0), "helayna eyes happy",
    )

image side helayna collar naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar naked happy side.png",
    (-23, 0), "helayna eyes happy",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal", "Sprites/Helayna/helayna mouth happy.png"),
    )

image helayna collar naked aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar naked aroused.png",
    )

image side helayna collar naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar naked aroused side.png",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna eyes neutral:
    "Sprites/Helayna/helayna eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat

image helayna eyes happy:
    "Sprites/Helayna/helayna eyes open happy.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat

image helayna eyes sad:
    "Sprites/Helayna/helayna eyes open sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat

image helayna eyes angry:
    "Sprites/Helayna/helayna eyes open angry.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat



image helayna mouth normal:
    "Sprites/Helayna/helayna talk 1.png"
    .2
    "Sprites/Helayna/helayna talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Draith

image draith neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Draith/draith neutral.png",
    (0, 0), "draith eyes normal",
    )

image side draith neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Draith/Side/draith neutral side.png",
    (-13, 0), "draith eyes normal",
    (0, 0), WhileSpeaking("dra", "draith mouth normal"),
    )

image draith happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Draith/draith happy.png",
    (0, 0), "draith eyes normal",
    )

image side draith happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Draith/Side/draith happy side.png",
    (-13, 0), "draith eyes normal",
    (0, 0), WhileSpeaking("dra", "draith mouth normal"),
    )



image draith eyes normal:
    "Sprites/Draith/draith eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Draith/draith eyes half closed.png"
    0.1
    "Sprites/Draith/draith eyes closed.png"
    .25
    repeat

image draith mouth normal:
    "Sprites/Draith/draith talk1.png"
    .2
    "Sprites/Draith/draith talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Doran

image doran neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Doran/doran neutral.png",
    (0, 0), "doran eyes normal",
    )

image side doran neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Doran/Side/doran neutral side.png",
    (-13, 0), "doran eyes normal",
    (0, 0), WhileSpeaking("dor", "doran mouth normal"),
    )

image doran shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Doran/doran shocked.png",
    )

image side doran shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Doran/Side/doran shocked side.png",
    (0, 0), WhileSpeaking("dor", "doran mouth normal"),
    )

image doran beardless neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Doran/doran beardless neutral.png",
    (0, 0), "doran eyes normal",
    )

image side doran beardless neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Doran/Side/doran beardless neutral side.png",
    (-13, 0), "doran eyes normal",
    (0, 0), WhileSpeaking("dor", "doran mouth normal"),
    )



image doran eyes normal:
    "Sprites/Doran/doran eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Doran/doran eyes half closed.png"
    0.1
    "Sprites/Doran/doran eyes closed.png"
    .25
    repeat

image doran mouth normal:
    "Sprites/Doran/doran talk 1.png"
    .2
    "Sprites/Doran/doran talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Rosarian Knight

image rosarian knight neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rosarian Knight/rosarian knight neutral.png",
    )

image side rosarian knight neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rosarian Knight/Side/rosarian knight neutral side.png",
    )

image rosarian knight injured = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rosarian Knight/rosarian knight injured.png",
    )

image side rosarian knight injured = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rosarian Knight/Side/rosarian knight injured side.png",
    )


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#shaya

image shaya neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Shaya/shaya neutral.png",
    (0, 0), "shaya eyes normal",
    )

image side shaya neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Shaya/Side/shaya neutral side.png",
    (-66, 0), "shaya eyes normal",
    (0, 0), WhileSpeaking("sha", "shaya mouth normal"),
    )

image shaya happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Shaya/shaya happy.png",
    (0, 0), "shaya eyes normal",
    )

image side shaya happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Shaya/Side/shaya happy side.png",
    (-66, 0), "shaya eyes normal",
    (0, 0), WhileSpeaking("sha", "shaya mouth normal"),
    )

image shaya eyes normal:
    "Sprites/Shaya/shaya eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Shaya/shaya eyes half closed.png"
    0.1
    "Sprites/Shaya/shaya eyes closed.png"
    .25
    repeat

image shaya mouth normal:
    "Sprites/Shaya/shaya talk 1.png"
    .2
    "Sprites/Shaya/shaya talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#tarish

image tarish neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Tarish/tarish neutral.png",
    (0, 0), "tarish eyes normal",
    )

image side tarish neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Tarish/Side/tarish neutral side.png",
    (-12, 0), "tarish eyes normal",
    (0, 0), WhileSpeaking("tar", "tarish mouth normal"),
    )

image tarish eyes normal:
    "Sprites/Tarish/tarish eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Tarish/tarish eyes half closed.png"
    0.1
    "Sprites/Tarish/tarish eyes closed.png"
    .25
    repeat

image tarish mouth normal:
    "Sprites/Tarish/tarish talk 1.png"
    .2
    "Sprites/Tarish/tarish talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#batri

image batri neutral = LiveComposite(
    (478, 650),
    (0, 0), "Sprites/Batri/batri neutral.png",
    )

image side batri neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Batri/Side/batri neutral side.png",
    (0, 0), WhileSpeaking("bat", "batri mouth normal"),
    xoffset=-30)


image batri mouth normal:
    "Sprites/Batri/batri talk 1.png"
    .2
    "Sprites/Batri/batri talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#ulcro

image ulcro neutral = LiveComposite(
    (478, 650),
    (0, 0), "Sprites/Ulcro/ulcro neutral.png",
    )

image side ulcro neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ulcro/Side/ulcro neutral side.png",
    (0, 0), WhileSpeaking("ulc", "ulcro mouth normal"),
     xoffset=-30)


image ulcro mouth normal:
    "Sprites/Ulcro/ulcro talk 1.png"
    .2
    "Sprites/Ulcro/ulcro talk 2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Eleanor

image eleanor rags neutral = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags neutral.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags neutral side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor rags happy = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags happy.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags happy side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor rags concerned = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags concerned.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags concerned side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor rags angry = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags angry.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags angry side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )





#dress

image eleanor dress neutral = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress neutral.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress neutral side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress happy = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress happy.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress happy side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress concerned = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress concerned.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress concerned side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress angry = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress angry.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress angry side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress aroused = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress aroused.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress aroused side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor naked aroused = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor naked aroused.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor naked aroused side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )




image eleanor eyes normal:
    "Sprites/Eleanor/eleanor eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Eleanor/eleanor eyes half closed.png"
    0.1
    "Sprites/Eleanor/eleanor eyes closed.png"
    .25
    repeat

image eleanor mouth normal:
    "Sprites/Eleanor/eleanor talk 1.png"
    .2
    "Sprites/Eleanor/eleanor talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Liurial

image liurial neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial neutral.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial neutral side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial happy.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial happy side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial sad.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial sad side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial angry.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial angry side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial aroused.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial aroused side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )



image liurial naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial naked happy.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial naked happy side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial naked sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial naked sad.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial naked sad side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial naked aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial naked aroused.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial naked aroused side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )


image liurial eyes normal:
    "Sprites/Liurial/liurial eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Liurial/liurial eyes half closed.png"
    0.1
    "Sprites/Liurial/liurial eyes closed.png"
    .25
    repeat

image liurial mouth normal:
    "Sprites/Liurial/liurial talk 1.png"
    .2
    "Sprites/Liurial/liurial talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#nileth

image nileth neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nileth/nileth neutral.png",
    (0, 0), "nileth eyes normal",
    )

image side nileth neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nileth/Side/nileth neutral side.png",
    (0, 0), WhileSpeaking("nil", "nileth mouth normal"),
    )



image nileth eyes normal:
    "Sprites/Nileth/nileth eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Nileth/nileth eyes half closed.png"
    0.1
    "Sprites/Nileth/nileth eyes closed.png"
    .25
    repeat

image nileth mouth normal:
    "Sprites/Nileth/nileth talk 1.png"
    .2
    "Sprites/Nileth/nileth talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#arzyl

image arzyl neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Arzyl/arzyl neutral.png",
    (0, 0), "arzyl eyes normal",
    )

image side arzyl neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Arzyl/Side/arzyl neutral side.png",
    (0, 0), WhileSpeaking("arz", "arzyl mouth normal"),
    )




image arzyl eyes normal:
    "Sprites/Arzyl/arzyl eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Arzyl/arzyl eyes half closed.png"
    0.1
    "Sprites/Arzyl/arzyl eyes closed.png"
    .25
    repeat

image arzyl mouth normal:
    "Sprites/Arzyl/arzyl talk 1.png"
    .2
    "Sprites/Arzyl/arzyl talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#succubus

image succubus neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/succubus 1.png",
    )

image side succubus neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/succubus 1 side.png",
    xoffset=-27)


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#succubus 2

image succubus 2 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/succubus 2.png",
    )

image side succubus 2 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/succubus 2 side.png",
    xoffset=-27)


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


# spies

image incubus1 = 'images/Sprites/Spies/Incubus 1.png'
image side incubus1 = 'images/Sprites/Spies/Side/Incubus 1 side.png'
image incubus2 = 'images/Sprites/Spies/Incubus 2.png'
image side incubus2 = 'images/Sprites/Spies/Side/Incubus 2 side.png'
image incubus3 = 'images/Sprites/Spies/Incubus 3.png'
image side incubus3 = 'images/Sprites/Spies/Side/Incubus 3 side.png'
image incubus4 = 'images/Sprites/Spies/Incubus 4.png'
image side incubus4 = 'images/Sprites/Spies/Side/Incubus 4 side.png'
image incubus5 = 'images/Sprites/Spies/Incubus 5.png'
image side incubus5 = 'images/Sprites/Spies/Side/Incubus 5 side.png'
image incubus6 = 'images/Sprites/Spies/Incubus 6.png'
image side incubus6 = 'images/Sprites/Spies/Side/Incubus 6 side.png'

image succubus1 = 'images/Sprites/Spies/succubus 1.png'
image side succubus1 = 'images/Sprites/Spies/Side/succubus 1 side.png'
image succubus2 = 'images/Sprites/Spies/succubus 2.png'
image side succubus2 = 'images/Sprites/Spies/Side/succubus 2 side.png'
image succubus3 = 'images/Sprites/Spies/succubus 3.png'
image side succubus3 = 'images/Sprites/Spies/Side/succubus 3 side.png'
image succubus4 = 'images/Sprites/Spies/succubus 4.png'
image side succubus4 = 'images/Sprites/Spies/Side/succubus 4 side.png'
image succubus5 = 'images/Sprites/Spies/succubus 5.png'
image side succubus5 = 'images/Sprites/Spies/Side/succubus 5 side.png'
image succubus6 = 'images/Sprites/Spies/succubus 6.png'
image side succubus6 = 'images/Sprites/Spies/Side/succubus 6 side.png'

image tempspy_image = DynamicImage('[tmp_spy.sprite]')
# dynamic side image that depends on current tmp_spy.sprite
image side tempspy_image = DynamicImage('side [tmp_spy.sprite]')

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Room Sprites

#Alexia

image alexia room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Alexia/Castle_Alexia_Body.png",
    (0, 0), "alexia room eyes normal",
    )


image alexia room eyes normal:
    "Sprites/Room Sprites/Alexia/Castle_Alexia_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Alexia/Castle_Alexia_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Alexia/Castle_Alexia_EyesClosed.png"
    .25
    repeat


#skordred

image skordred room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_Body.png",
    (0, 0), "skordred room eyes normal",
    )


image skordred room eyes normal:
    "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_EyesClosed.png"
    .25
    repeat


#cla-min

image clamin room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_Body.png",
    (0, 0), "clamin room eyes normal",
    )


image clamin room eyes normal:
    "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_EyesClosed.png"
    .25
    repeat


#cliohna

image cliohna room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_Body.png",
    (0, 0), "cliohna room eyes normal",
    )


image cliohna room eyes normal:
    "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_EyesClosed.png"
    .25
    repeat


#jezera

image jezera room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_Body.png",
    (0, 0), "jezera room eyes normal",
    )


image jezera room eyes normal:
    "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_EyesClosed.png"
    .25
    repeat

#andras

image andras room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Andras/Castle_Andras_Body.png",
    )


#orc soldier

image orc soldier room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Orc/Castle_Orc_Body.png",
    )


#shaya

image shaya room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_Body.png",
    (0, 0), "shaya room eyes normal",
    )


image shaya room eyes normal:
    "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_EyesClosed.png"
    .25
    repeat


#xzaratl

image xzaratl room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_Body.png",
    (0, 0), "xzaratl room eyes normal",
    )


image xzaratl room eyes normal:
    "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_EyesClosed.png"
    .25
    repeat


#greyhide

image greyhide room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Greyhide/Castle_Greyhide_Body.png",
    (0, 0), "greyhide room eyes normal",
    )


image greyhide room eyes normal:
    "Sprites/Room Sprites/Castle_Greyhide/Castle_Greyhide_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Greyhide/Castle_Greyhide_EyesClosed.png"
    .25
    repeat


#draith

image draith room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Draith/Castle_Draith_Body.png",
    (0, 0), "draith room eyes normal",
    )


image draith room eyes normal:
    "Sprites/Room Sprites/Castle_Draith/Castle_Draith_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Draith/Castle_Draith_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Draith/Castle_Draith_EyesClosed.png"
    .25
    repeat


#indarah

image indarah room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_Body.png",
    (0, 0), "indarah room eyes normal",
    )


image indarah room eyes normal:
    "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_EyesClosed.png"
    .25
    repeat



#helayna

image helayna room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_Body.png",
    (0, 0), "helayna room eyes normal",
    )


image helayna room eyes normal:
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesClosed.png"
    .25
    repeat


#naked helayna

image naked helayna room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Helayna/Castle_NakedHelayna_Body.png",
    (0, 0), "naked helayna room eyes normal",
    )


image naked helayna room eyes normal:
    "Sprites/Room Sprites/Castle_Helayna/Castle_NakedHelayna_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesClosed.png"
    .25
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Dazzanath

image dazzanath neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/Incubus 3.png",
    )

image side dazzanath neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/Incubus 3 side.png",
    )



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#jak

image jak neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jak/jak neutral.png",
    (13, 10), "jak eyes normal",
    )

image side jak neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jak/Side/jak neutral side.png",
    (0, 0), WhileSpeaking("jak", "jak mouth normal"),
    )




image jak eyes normal:
    "Sprites/Jak/jak eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jak/jak eyes half closed.png"
    0.1
    "Sprites/Jak/jak eyes closed.png"
    .25
    repeat

image jak mouth normal:
    "Sprites/Jak/jak talk1.png"
    .2
    "Sprites/Jak/jak talk2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

image isdruel neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Isdruel/isdruel neutral.png",
    (0, 0), "isdruel eyes normal",
    )

image side isdruel neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Isdruel/Side/isdruel neutral side.png",
    (0, 0), WhileSpeaking("isdr", "isdruel mouth normal"),
    )

image isdruel angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Isdruel/isdruel angry.png",
    (0, 0), "isdruel eyes normal",
    )

image side isdruel angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Isdruel/Side/isdruel angry side.png",
    (0, 0), WhileSpeaking("isdr", "isdruel mouth normal"),
    )

image isdruel happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Isdruel/isdruel happy.png",
    (0, 0), "isdruel eyes normal",
    )

image side isdruel happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Isdruel/Side/isdruel happy side.png",
    (0, 0), WhileSpeaking("isdr", "isdruel mouth normal"),
    )




image isdruel eyes normal:
    "Sprites/Isdruel/isdruel eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Isdruel/isdruel eyes half closed.png"
    0.1
    "Sprites/Isdruel/isdruel eyes closed.png"
    .25
    repeat

image isdruel mouth normal:
    "Sprites/Isdruel/isdruel talk1.png"
    .2
    "Sprites/Isdruel/isdruel talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Heartsong

image heartsong neutral = LiveComposite(
    (400, 600),
    (0, 0), "Sprites/Heartsong/heartsong neutral.png",
    (0, 0), "heartsong eyes normal",
    )

image side heartsong neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Heartsong/Side/heartsong neutral side.png",
    (0, 0), WhileSpeaking("hear", "heartsong mouth normal"),
    )


image heartsong eyes normal:
    "Sprites/Heartsong/heartsong eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Heartsong/heartsong eyes half closed.png"
    0.1
    "Sprites/Heartsong/heartsong eyes closed.png"
    .25
    repeat

image heartsong mouth normal:
    "Sprites/Heartsong/heartsong talk1.png"
    .2
    "Sprites/Heartsong/heartsong talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


image whitescar neutral = LiveComposite(
    (600, 600),
    (0, 0), "Sprites/Whitescar/whitescar neutral.png",
    )

image side whitescar neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Whitescar/Side/whitescar neutral side.png",
    (0, 0), WhileSpeaking("whit", "whitescar mouth normal"),
    )



image whitescar mouth normal:
    "Sprites/Whitescar/whitescar talk 1.png"
    .2
    "Sprites/Whitescar/whitescar talk 2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

image ygriss neutral = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss neutral.png",
    (0, 0), "ygriss eyes normal",
    )

image side ygriss neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss neutral side.png",
    (-150, 0), "ygriss eyes normal",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )

image ygriss happy = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss happy.png",
    (0, 0), "ygriss eyes normal",
    )

image side ygriss happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss happy side.png",
    (-150, 0), "ygriss eyes normal",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )

image ygriss angry = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss angry.png",
    )

image side ygriss angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss angry side.png",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )

image ygriss aroused = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss aroused.png",
    (0, 0), "ygriss eyes normal",
    )

image side ygriss aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss aroused side.png",
    (-150, 0), "ygriss eyes normal",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )




image ygriss eyes normal:
    "Sprites/Ygriss/ygriss eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Ygriss/ygriss eyes half closed.png"
    0.1
    "Sprites/Ygriss/ygriss eyes closed.png"
    .25
    repeat

image ygriss mouth normal:
    "Sprites/Ygriss/ygriss talk1.png"
    .2
    "Sprites/Ygriss/ygriss talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Werden

image werden neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Werden/werden neutral.png",
    (0, 0), "werden eyes normal",
    )

image side werden neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Werden/Side/werden neutral side.png",
    (-14, 0), "werden eyes normal",
    (0, 0), WhileSpeaking("werd", "werden mouth normal"),
    )


image werden eyes normal:
    "Sprites/Werden/werden eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Werden/werden eyes half closed.png"
    0.1
    "Sprites/Werden/werden eyes closed.png"
    .25
    repeat

image werden mouth normal:
    "Sprites/Werden/werden talk1.png"
    .2
    "Sprites/Werden/werden talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Casimir

image casimir neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Casimir/casimir neutral.png",
    (0, 0), "casimir eyes normal",
    )

image side casimir neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Casimir/Side/casimir neutral side.png",
    (-22, 0), "casimir eyes normal",
    (0, 0), WhileSpeaking("casi", "casimir mouth normal"),
    )


image casimir eyes normal:
    "Sprites/Casimir/casimir eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Casimir/casimir eyes half closed.png"
    0.1
    "Sprites/Casimir/casimir eyes closed.png"
    .25
    repeat

image casimir mouth normal:
    "Sprites/Casimir/casimir talk1.png"
    .2
    "Sprites/Casimir/casimir talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Marianne

image marianne neutral = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne neutral.png",
    (0, 0), "marianne eyes normal",
    )

image side marianne neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne neutral side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )

image marianne happy = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne happy.png",
    (0, 0), "marianne eyes normal",
    )

image side marianne happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne happy side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )


image marianne eyes normal:
    "Sprites/Marianne/marianne eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Marianne/marianne eyes half closed.png"
    0.1
    "Sprites/Marianne/marianne eyes closed.png"
    .25
    repeat

image marianne mouth normal:
    "Sprites/Marianne/marianne talk1.png"
    .2
    "Sprites/Marianne/marianne talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Patricia

image patricia neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia neutral.png",
    (0, 0), "patricia eyes normal",
    )

image side patricia neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia neutral side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia happy.png",
    (0, 0), "patricia eyes normal",
    )

image side patricia happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia happy side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia annoyed = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia annoyed.png",
    (0, 0), "patricia eyes normal",
    )

image side patricia annoyed = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia annoyed side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia sad.png",
    (0, 0), "patricia eyes sad",
    )

image side patricia sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia sad side.png",
    (-22, 0), "patricia eyes sad",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia eyes normal:
    "Sprites/Patricia/patricia eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Patricia/patricia eyes half closed.png"
    0.1
    "Sprites/Patricia/patricia eyes closed.png"
    .25
    repeat

image patricia eyes sad:
    "Sprites/Patricia/patricia eyes open sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Patricia/patricia eyes half closed.png"
    0.1
    "Sprites/Patricia/patricia eyes closed.png"
    .25
    repeat

image patricia mouth normal:
    "Sprites/Patricia/patricia talk1.png"
    .2
    "Sprites/Patricia/patricia talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Ameraine

image ameraine masked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine masked neutral.png",
    (0, 0), "ameraine eyes normal",
    )

image side ameraine masked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine masked neutral side.png",
    (-11, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine masked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine masked happy.png",
    (0, 0), "ameraine eyes normal",
    )

image side ameraine masked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine masked happy side.png",
    (-11, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine naked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine naked neutral.png",
    (0, 0), "ameraine eyes normal",
    )

image side ameraine naked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine naked neutral side.png",
    (-11, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine naked happy.png",
    (0, 0), "ameraine eyes normal",
    )

image side ameraine naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine naked happy side.png",
    (-11, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine neutral.png",
    (0, 0), "ameraine eyes normal",
    )

image side ameraine neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine neutral side.png",
    (-11, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine happy.png",
    (0, 0), "ameraine eyes normal",
    )

image side ameraine happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine happy side.png",
    (-11, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )



image ameraine eyes normal:
    "Sprites/Ameraine/ameraine eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Ameraine/ameraine eyes half closed.png"
    0.1
    "Sprites/Ameraine/ameraine eyes closed.png"
    .25
    repeat

image ameraine mouth normal:
    "Sprites/Ameraine/ameraine talk1.png"
    .2
    "Sprites/Ameraine/ameraine talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Juliet

image juliet neutral = LiveComposite(
    (395, 600),
    (0, 0), "Sprites/Juliet/juliet neutral.png",
    (0, 0), "juliet eyes normal",
    )

image side juliet neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Juliet/Side/juliet neutral side.png",
    (-48, 0), "juliet eyes normal",
    (0, 0), WhileSpeaking("juli", "juliet mouth normal"),
    )

image juliet happy = LiveComposite(
    (395, 600),
    (0, 0), "Sprites/Juliet/juliet happy.png",
    (0, 0), "juliet eyes normal",
    )

image side juliet happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Juliet/Side/juliet happy side.png",
    (-48, 0), "juliet eyes normal",
    (0, 0), WhileSpeaking("juli", "juliet mouth normal"),
    )

image juliet shocked = LiveComposite(
    (395, 600),
    (0, 0), "Sprites/Juliet/juliet shocked.png",
    )

image juliet eyes normal:
    "Sprites/Juliet/juliet eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Juliet/juliet eyes half closed.png"
    0.1
    "Sprites/Juliet/juliet eyes closed.png"
    .25
    repeat

image juliet mouth normal:
    "Sprites/Juliet/Juliet talk 1.png"
    .2
    "Sprites/Juliet/Juliet talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Jacques

image jacques neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jacques/jacques neutral.png",
    (0, 0), "jacques eyes normal",
    )

image side jacques neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jacques/Side/jacques neutral side.png",
    (-11, 0), "jacques eyes normal",
    (0, 0), WhileSpeaking("jacq", "jacques mouth normal"),
    )

image jacques happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jacques/jacques happy.png",
    (0, 0), "jacques eyes normal",
    )

image side jacques happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jacques/Side/jacques happy side.png",
    (-11, 0), "jacques eyes normal",
    (0, 0), WhileSpeaking("jacq", "jacques mouth normal"),
    )



image jacques eyes normal:
    "Sprites/Jacques/jacques eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jacques/jacques eyes closed.png"
    .25
    repeat

image jacques mouth normal:
    "Sprites/Jacques/jacques talk1.png"
    .2
    "Sprites/Jacques/jacques talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Mary

image mary neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Mary/mary neutral.png",
    (10, 32), "mary eyes normal",
    )

image side mary neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mary/Side/mary neutral side.png",
    (0, 0), "mary eyes normal",
    (0, 0), WhileSpeaking("mary", "mary mouth normal"),
    )


image mary happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Mary/mary happy.png",
    (10, 32), "mary eyes normal",
    )

image side mary happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mary/Side/mary happy side.png",
    (0, 0), "mary eyes normal",
    (0, 0), WhileSpeaking("mary", "mary mouth normal"),
    )

image mary concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Mary/mary concerned.png",
    (10, 32), "mary eyes normal",
    )

image side mary concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mary/Side/mary concerned side.png",
    (0, 0), "mary eyes normal",
    (0, 0), WhileSpeaking("mary", "mary mouth normal"),
    )

image mary eyes normal:
    "Sprites/Mary/mary eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Mary/mary eyes half closed.png"
    0.1
    "Sprites/Mary/mary eyes closed.png"
    .25
    repeat


image mary mouth normal:
    "Sprites/Mary/mary talk 1.png"
    .2
    "Sprites/Mary/mary talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Nasim

image nasim neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nasim/nasim neutral.png",
    (0, 0), "nasim eyes normal",
    )

image side nasim neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nasim/Side/nasim neutral side.png",
    (-11, -15), "nasim eyes normal",
    (0, 0), WhileSpeaking("nas", "nasim mouth normal"),
    )

image nasim happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nasim/nasim happy.png",
    (0, 0), "nasim eyes normal",
    )

image side nasim happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nasim/Side/nasim happy side.png",
    (-11, -15), "nasim eyes normal",
    (0, 0), WhileSpeaking("nas", "nasim mouth normal"),
    )

image nasim angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nasim/nasim angry.png",
    (0, 0), "nasim eyes normal",
    )

image side nasim angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nasim/Side/nasim angry side.png",
    (-11, -15), "nasim eyes normal",
    (0, 0), WhileSpeaking("nas", "nasim mouth normal"),
    )



image nasim eyes normal:
    "Sprites/Nasim/nasim eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Nasim/nasim eyes half closed.png"
    0.1
    "Sprites/Nasim/nasim eyes closed.png"
    .25
    repeat


image nasim mouth normal:
    "Sprites/Nasim/nasim talk1.png"
    .2
    "Sprites/Nasim/nasim talk2.png"
    .2
    repeat






#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

    #BGs
init:
    image bg1 = "images/Backgrounds/village day.png"
    image bg2 = "images/Backgrounds/home.png"
    image bg3 = "images/Backgrounds/forest1.png"
    image bg4 = "images/Backgrounds/townfire.png"
    image bg5 = "images/Backgrounds/town aftermath.png"
    image bg6 = "images/Backgrounds/throne room.jpg"
    image bg7 = "images/Backgrounds/guest room.jpg"
    image bg8 = "images/Backgrounds/castle dungeon.png"
    image bg9 = "images/Backgrounds/Rowans room.jpg"
    image bg10 = "images/Backgrounds/portal-room.jpg"
    image bg11 = "images/Backgrounds/barracks.jpg"
    image bg12 = "images/Backgrounds/library.jpg"
    image bg13 = "images/Backgrounds/guest room dark.png"
    image bg14 = "images/Backgrounds/castle hallway.jpg"
    image bg15 = "images/Backgrounds/keep courtyard.png"
    image bg16 = "images/Backgrounds/keep exterior.png"
    image bg17 = "images/Backgrounds/keep interior.png"
    image bg18 = "images/Backgrounds/jezera chambers.png"
    image bg19 = "images/Backgrounds/wagon.png"
    image bg20 = "images/Backgrounds/workshop.png"
    image bg21 = "images/Backgrounds/tavern.png"
    image bg22 = "images/Backgrounds/forge.png"
    image bg23 = "images/Backgrounds/sanctum.png"
    image bg24 = "images/Backgrounds/brothel.png"
    image bg25 = "images/Backgrounds/breeding pit.png"
    image bg26 = "images/Backgrounds/orc camp.png"
    image bg27 = "images/Backgrounds/ballroom.png"
    image bg28 = "images/Backgrounds/arena.png"
    image bg29 = "images/Backgrounds/arena balcony.png"
    image bg30 = "images/Backgrounds/orc tent interior.png"
    image bg31 = "images/Backgrounds/plain.png"
    image bg32 = "images/Backgrounds/swamp.png"
    image bg33 = "images/Backgrounds/rastedel.png"
    image bg34 = "images/Backgrounds/mirrored palace day.png"
    image bg35 = "images/Backgrounds/mirrored palace night.png"
    image bg36 = "images/Backgrounds/grandlodge.png"
    

#CGs

init:
    image cg1 = "images/CG/RowanxAlexia 1.png"
    image cg2 = "images/CG/RowanxAlexia 2.png"
    image cg3 = "images/CG/RowanxAlexia 3.png"
    image cg4 = "images/CG/RowanxAlexia 4.png"
    image cg5 = "images/CG/Jezera Appears.png"
    image cg6 = "images/CG/Orc Ambush.png"
    image cg7 = "images/CG/Jezera Revealed.png"
    image cg8 = "images/CG/Burning Village.png"
    image cg9 = "images/CG/Rowan Bowed.png"
    image cg10 = "images/CG/Before the Gates.png"
    image cg11 = "images/CG/JezeraxRowan 1.png"
    image cg12 = "images/CG/JezeraxRowan 2.png"
    image cg13 = "images/CG/JezeraxRowan 3.png"
    image cg14 = "images/CG/JezeraxRowan 4.png"
    image cg15 = "images/CG/AndrasxRowan 1.png"
    image cg16 = "images/CG/AndrasxRowan 2.png"
    image cg17 = "images/CG/AndrasxRowan 3.png"
    image cg18 = "images/CG/AndrasxRowan 4.png"
    image cg19 = "images/CG/Reunion.png"
    image cg20 = "images/CG/AlxAn Kiss 1.png"
    image cg21 = "images/CG/AlxAn Kiss 2.png"
    image cg22 = "images/CG/AlxAn Kiss 3.png"
    image cg23 = "images/CG/AlxAn Anal 1.png"
    image cg24 = "images/CG/AlxAn Anal 2.png"
    image cg25 = "images/CG/AlxAn Anal 3.png"
    image cg26 = "images/CG/AlxAn Anal 4.png"
    image cg27 = "images/CG/AlxAn Sex 2.png"
    image cg28 = "images/CG/AlxAn Sex 1.png"
    image cg29 = "images/CG/AlxAn Sex 3.png"
    image cg30 = "images/CG/RowanxAlexia 2 1.png"
    image cg31 = "images/CG/RowanxAlexia 2 2.png"
    image cg32 = "images/CG/RowanxAlexia 2 3.png"
    image cg33 = "images/CG/RowanxAlexia 2 4.png"
    image cg34 = "images/CG/RowanxAlexia 2 5.png"
    image cg35 = "images/CG/XxRxA 1.png"
    image cg36 = "images/CG/XxRxA 2.png"
    image cg37 = "images/CG/XxRxA 3.png"
    image cg38 = "images/CG/XxRxA 4.png"
    image cg39 = "images/CG/XxRxA 5.png"
    image cg40 = "images/CG/XxRxA 6.png"
    image cg41 = "images/CG/XxRxA 7.png"
    image cg42 = "images/CG/AlxAn Strip 1.png"
    image cg43 = "images/CG/AlxAn Strip 2.png"
    image cg44 = "images/CG/AlxAn Strip 3.png"
    image cg45 = "images/CG/AlxAn Strip 4.png"
    image cg46 = "images/CG/AlxAn Strip 5.png"
    image cg47 = "images/CG/AlxAn Strip 6.png"
    image cg48 = "images/CG/AlxAn Strip 7.png"
    image cg49 = "images/CG/AlxAn Strip 8.png"
    image cg50 = "images/CG/JezxAl 69.png"
    image cg51 = "images/CG/AnxRo Frot 1.png"
    image cg52 = "images/CG/AnxRo Frot 2.png"
    image cg53 = "images/CG/AnxRo Frot 3.png"
    image cg54 = "images/CG/OrcsxHel 1.png"
    image cg55 = "images/CG/OrcsxHel 2.png"
    image cg56 = "images/CG/AnxAl Bed 1.png"
    image cg57 = "images/CG/AnxAl Bed 2.png"
    image cg58 = "images/CG/AnxAl Bed 3.png"
    image cg59 = "images/CG/RoxHel Keep 1.png"
    image cg60 = "images/CG/RoxHel Keep 2.png"
    image cg61 = "images/CG/RoxHel Keep 3.png"
    image cg62 = "images/CG/AnxRo BJ 1.png"
    image cg63 = "images/CG/AnxRo BJ 2.png"
    image cg64 = "images/CG/XxRxA 8.png"
    image cg65 = "images/CG/XxRxA 9.png"
    image cg66 = "images/CG/XxRxA 10.png"
    image cg67 = "images/CG/RxJxDE 1.png"
    image cg68 = "images/CG/JezxSha 1.png"
    image cg69 = "images/CG/RoxCla 1.png"
    image cg70 = "images/CG/RoxCla 2.png"
    image cg71 = "images/CG/RoxCla 3.png"
    image cg72 = "images/CG/RoxDraith 1.png"
    image cg73 = "images/CG/RoxDraith 2.png"
    image cg74 = "images/CG/RoxDraith 3.png"
    image cg75 = "images/CG/RoxDraith 4.png"
    image cg76 = "images/CG/GreyhidexAlexia 1.png"
    image cg77 = "images/CG/GreyhidexAlexia 2.png"
    image cg78 = "images/CG/GreyhidexAlexia 3.png"
    image cg79 = "images/CG/GreyhidexAlexia 4.png"
    image cg80 = "images/CG/ClixRo 1.png"
    image cg81 = "images/CG/RoxGirls 1.png"
    image cg82 = "images/CG/RoxGirls 2.png"
    image cg83 = "images/CG/RowanxAlexia 3 1.png"
    image cg84 = "images/CG/RowanxAlexia 3 2.png"
    image cg85 = "images/CG/AlxAn Jerk 1.png"
    image cg86 = "images/CG/AlxAn Titjob 1.png"
    image cg87 = "images/CG/AlxAn Titjob 2.png"
    image cg88 = "images/CG/AlxAn Titjob 3.png"
    image cg89 = "images/CG/RowanxClaBow 1.png"
    image cg90 = "images/CG/RowanxClaBow 2.png"
    image cg91 = "images/CG/RowanxClaBow 3.png"
    image cg92 = "images/CG/AlxGar 1.png"
    image cg93 = "images/CG/AlxGar 2.png"
    image cg94 = "images/CG/RoxClaDaughter 1.png"
    image cg95 = "images/CG/RoxClaDaughter 2.png"
    image cg96 = "images/CG/AlxGar 3.png"
    image cg97 = "images/CG/AlxGar 4.png"
    image cg98 = "images/CG/AlxGar 5.png"
    image cg99 = "images/CG/AlxRo 1.png"
    image cg100 = "images/CG/AlxRo 2.png"
    image cg101 = "images/CG/AlxRo 3.png"
    image cg102 = "images/CG/AnxHel Dinner 1.png"
    image cg103 = "images/CG/AnxHel Dinner 2.png"
    image cg104 = "images/CG/AnxHel Dinner 3.png"
    image cg105 = "images/CG/GreyhidexAlexia 5.png"
    image cg106 = "images/CG/JezxAl 1.png"
    image cg107 = "images/CG/andras injured.png"
    image cg108 = "images/CG/RoxGreyhide 1.png"
    image cg109 = "images/CG/RoxGreyhide 2.png"
    image cg110 = "images/CG/RoxOrcWoman 1.png"
    image cg111 = "images/CG/RoxOrcWoman 2.png"
    image cg112 = "images/CG/RoxHel 1.png"
    image cg113 = "images/CG/RoxHel 2.png"
    image cg114 = "images/CG/RoxHel 3.png"
    image cg115 = "images/CG/AndrasxAlexia Finger 1.png"
    image cg116 = "images/CG/AndrasxAlexia Finger 2.png"
    image cg117 = "images/CG/AlxRo&Xz 1.png"
    image cg118 = "images/CG/AlxRo&Xz 2.png"
    image cg119 = "images/CG/KnightsxHel 1.png"
    image cg120 = "images/CG/KnightsxHel 2.png"
    image cg121 = "images/CG/DriderxRo 2.png"
    image cg122 = "images/CG/DriderxRo 1.png"
    image cg123 = "images/CG/AnxRo&Sk 1.png"
    image cg124 = "images/CG/JezxSha 2.png"
    image cg125 = "images/CG/RoxHel BJ 1.png"
    image cg126 = "images/CG/RoxHel BJ 2.png"
    image cg127 = "images/CG/RoxCla 4.png"
    image cg128 = "images/CG/RoxCla 5.png"
    image cg129 = "images/CG/AnxRo Arena 1.png"
    image cg130 = "images/CG/AnxRo Arena 2.png"
    image cg131 = "images/CG/DriderxOrc 1.png"
    image cg132 = "images/CG/DriderxOrc 2.png"
    image cg133 = "images/CG/DriderxOrc 3.png"
    image cg134 = "images/CG/RoxLi 1.png"
    image cg135 = "images/CG/RoxLi 2.png"
    image cg136 = "images/CG/RoxHel Window.png"
    image cg137 = "images/CG/ArzxRo 1.png"
    image cg138 = "images/CG/ArzxRo 2.png"
    image cg139 = "images/CG/ArzxRo 3.png"
    image cg140 = "images/CG/RoxLi Kiss.png"
    image cg141 = "images/CG/RoxDry 1.png"
    image cg142 = "images/CG/RoxDry 2.png"
    image cg143 = "images/CG/RoxAla 1.png"
    image cg144 = "images/CG/RoxAla 2.png"
    image cg145 = "images/CG/RoxAla 3.png"
    image cg146 = "images/CG/RoxAla 4.png"
    image cg147 = "images/CG/X&AxR 1.png"
    image cg148 = "images/CG/X&AxR 2.png"
    image cg149 = "images/CG/X&AxR 3.png"
    image cg150 = "images/CG/RoxLi BJ 1.png"
    image cg151 = "images/CG/RoxLi BJ 2.png"
    image cg152 = "images/CG/RoxLi BJ 3.png"
    image cg153 = "images/CG/RoxLi Dun 1.png"
    image cg154 = "images/CG/GHxRo 1.png"
    image cg155 = "images/CG/GHxRo 2.png"
    image cg156 = "images/CG/GHxAl 1.png"
    image cg157 = "images/CG/GHxAl 2.png"
    image cg158 = "images/CG/WulxAl 1.png"
    image cg159 = "images/CG/WulxAl 2.png"
    image cg160 = "images/CG/WulxAl 3.png"
    image cg161 = "images/CG/WulxAl 4.png"
    image cg162 = "images/CG/WulxAl 5.png"
    image cg163 = "images/CG/RoxLi Dun 2.png"
    image cg164 = "images/CG/GHxAlxRo.png"
    image cg165 = "images/CG/WulxAl 6.png"
    image cg166 = "images/CG/WulxAl 7.png"
    image cg167 = "images/CG/WulxAl 8.png"
    image cg168 = "images/CG/WulxAl 9.png"
    image cg169 = "images/CG/WulxAl 10.png"
    image cg170 = "images/CG/WulxAl 11.png"
    image cg171 = "images/CG/Hel's Daydream 1.png"
    image cg172 = "images/CG/Hel's Daydream 2.png"
    image cg173 = "images/CG/Hel's Daydream 3.png"
    image cg174 = "images/CG/JakxInd 1.png"
    image cg175 = "images/CG/WulxAl 12.png"
    image cg176 = "images/CG/WulxAl 13.png"
    image cg177 = "images/CG/WulxAl 14.png"
    image cg178 = "images/CG/WulxAl 15.png"
    image cg179 = "images/CG/WulxAl 16.png"
    image cg180 = "images/CG/WulxAl 17.png"
    image cg181 = "images/CG/Hel's Daydream 4.png"
    image cg182 = "images/CG/Hel's Daydream 5.png"
    image cg183 = "images/CG/Hel's Daydream 6.png"
    image cg184 = "images/CG/RoxGirls 3.png"
    image cg185 = "images/CG/RoxGirls 4.png"
    image cg186 = "images/CG/ClixRo 2.png"
    image cg187 = "images/CG/ClixRo 3.png"
    image cg188 = "images/CG/JezxSha 3.png"
    image cg189 = "images/CG/RoxOrcWoman 3.png"
    image cg190 = "images/CG/AnxAl Dun 1.png"
    image cg191 = "images/CG/AnxAl Dun 2.png"
    image cg192 = "images/CG/AnxAl Dun 3.png"
    image cg193 = "images/CG/AnxAl Dun 4.png"
    image cg194 = "images/CG/AnxAl Dun 5.png"
    image cg195 = "images/CG/RoxCla TF 1.png"
    image cg196 = "images/CG/RoxCla TF 2.png"
    image cg197 = "images/CG/RoxCla TF 3.png"
    image cg198 = "images/CG/RoxCla TF 4.png"
    image cg199 = "images/CG/RoxCla TF 5.png"
    image cg200 = "images/CG/RoxSh 1.png"
    image cg201 = "images/CG/DazzxRo 1.png"
    image cg202 = "images/CG/RowanxAlexia 3 3.png"
    image cg203 = "images/CG/JezxAl Fj 1.png"
    image cg204 = "images/CG/JezxAl Fj 2.png"
    image cg205 = "images/CG/JezxAl Fj 3.png"
    image cg206 = "images/CG/AnxAl Dun BJ 1.png"
    image cg207 = "images/CG/AnxAl Dun BJ 2.png"
    image cg208 = "images/CG/AnxAl Dun BJ 3.png"
    image cg209 = "images/CG/AnxAl Dun BJ 4.png"
    image cg210 = "images/CG/AnxAl Dun BJ 5.png"
    image cg211 = "images/CG/AnxAl Dun BJ 6.png"
    image cg212 = "images/CG/DazzxAg 1.png"
    image cg213 = "images/CG/RoxLi 3.png"
    image cg214 = "images/CG/JezxRo 1.png"
    image cg215 = "images/CG/AnxRo BJ 3.png"
    image cg216 = "images/CG/AnxRo BJ 4.png"
    image cg217 = "images/CG/JakxInd 2.png"
    image cg218 = "images/CG/JakxInd 3.png"
    image cg219 = "images/CG/Shaya Dance 1.png"
    image cg220 = "images/CG/Shaya Dance 2.png"
    image cg221 = "images/CG/Shaya Dance 3.png"
    image cg222 = "images/CG/Shaya Dance 4.png"
    image cg223 = "images/CG/Shaya Dance 5.png"
    image cg224 = "images/CG/Shaya Dance 6.png"
    image cg225 = "images/CG/OrcsxDel 1.png"
    image cg226 = "images/CG/OrcsxDel 2.png"
    image cg227 = "images/CG/BatrixDel 1.png"
    image cg228 = "images/CG/An&BatxRo 1.png"
    image cg229 = "images/CG/An&BatxRo 2.png"
    image cg230 = "images/CG/An&BatxRo 3.png"
    image cg231 = "images/CG/RxJxDE 2.png"
    image cg232 = "images/CG/RoxTarish 1.png"
    image cg233 = "images/CG/RoxDraith BJ 1.png"
    image cg234 = "images/CG/RoxEmma Slut 1.png"
    image cg235 = "images/CG/RoxEmma Slut 2.png"
    image cg236 = "images/CG/RoxEmma Slut 3.png"
    image cg237 = "images/CG/RoxEmma Slut 4.png"
    image cg238 = "images/CG/RoxEmma Pure 1.png"
    image cg239 = "images/CG/RoxEmma Pure 2.png"
    image cg240 = "images/CG/RoxEmma Pure 3.png"
    image cg241 = "images/CG/RoxEmma Pure 4.png"
    image cg242 = "images/CG/RoxLixAl 1.png"
    image cg243 = "images/CG/RoxLixAl 2.png"
    image cg244 = "images/CG/rastedel battle 1.png"
    image cg245 = "images/CG/rastedel battle 2.png"
    image cg246 = "images/CG/rastedel battle 3.png"
    image cg247 = "images/CG/rastedel battle 4.png"
    image cg248 = "images/CG/rastedel battle 5.png"
    image cg249 = "images/CG/JezxCom 1.png"
    image cg250 = "images/CG/PoT 1.png"
    image cg251 = "images/CG/PoT 2.png"
    image cg252 = "images/CG/PoT 3.png"
    image cg253 = "images/CG/delbadend.png"
    image cg254 = "images/CG/RoxHel Bed 1.png"
    image cg255 = "images/CG/RoxHel Bed 2.png"
    image cg256 = "images/CG/AnxDraith 1.png"
    image cg257 = "images/CG/AnxDraith 2.png"
    image cg258 = "images/CG/AnxDraith 3.png"
    image cg259 = "images/CG/JezxAl Dun 1.png"
    image cg260 = "images/CG/JezxAl Dun 2.png"
    image cg261 = "images/CG/JezxAl Dun 3.png"
    image cg262 = "images/CG/bloodmeen.png"
    image cg263 = "images/CG/pits harassment 1.png"
    image cg264 = "images/CG/pits harassment 2.png"
    image cg265 = "images/CG/JezxDor 1.png"
    image cg266 = "images/CG/roxmaidxhel 1.png"
    image cg267 = "images/CG/RoxSkor 1.png"
    image cg268 = "images/CG/RoxSkor 2.png"
    image cg269 = "images/CG/RoxSkor 3.png"
    image cg270 = "images/CG/RoxSkor 4.png"
    image cg271 = "images/CG/picnic 1.png"
    image cg272 = "images/CG/picnic 2.png"
    image cg273 = "images/CG/picnic 3.png"
    image cg274 = "images/CG/picnic 4.png"
    image cg275 = "images/CG/picnic 5.png"
    image cg276 = "images/CG/picnic 6.png"
    image cg277 = "images/CG/picnic 7.png"
    image cg278 = "images/CG/tavern harassment 1.png"
    image cg279 = "images/CG/tavern harassment 2.png"
    image cg280 = "images/CG/tavern harassment 3.png"
    image cg281 = "images/CG/tavern harassment 4.png"
    image cg282 = "images/CG/GHxAl sex 1.png"
    image cg283 = "images/CG/GhxAl sex 2.png"
    image cg284 = "images/CG/alexia futa 1.png"
    image cg285 = "images/CG/alexia futa 2.png"#
    image cg286 = "images/CG/RoxAl BJ 1.png"
    image cg287 = "images/CG/An&BatxRo 4.png"
    image cg288 = "images/CG/JezxMino 1.png"
    image cg289 = "images/CG/JezxMino 2.png"
    image cg290 = "images/CG/JezxMino 3.png"
    image cg291 = "images/CG/JezxMino 4.png"
    image cg292 = "images/CG/JezxMino 5.png"
    image cg293 = "images/CG/JezxMino 6.png"
    image cg294 = "images/CG/JezxMino 7.png"
    image cg295 = "images/CG/RoxAmer 1.png"
    image cg296 = "images/CG/RoxAmer 2.png"
    image cg297 = "images/CG/RoxAmer 3.png"
    image cg298 = "images/CG/RoxAmer 4.png"
    image cg299 = "images/CG/RoxAmer 5.png"
    image cg300 = "images/CG/RoxAmer 6.png"
    image cg301 = "images/CG/alexia tree solo 1.png"
    image cg302 = "images/CG/alexia tree solo 2.png"
    image cg303 = "images/CG/alexia tree solo 3.png"
    image cg304 = "images/CG/alexia tree solo 4.png"
    image cg305 = "images/CG/arzxcourt.png"
    image cg306 = "images/CG/Hel solo 1.png"
    image cg307 = "images/CG/anxal baths 1.png"
    image cg308 = "images/CG/anxal baths 2.png"
    image cg309 = "images/CG/roxhel 4.png"
    image cg310 = "images/CG/Hel solo 2.png"
    image cg311 = "images/CG/gob dinner.png"
    image cg312 = "images/CG/skor sketch.png"
    image cg313 = "images/CG/AxXxR hug.png"
    
        
    image alexia_maid_1 = 'images/Jobs/Alexia Maid1.png'
    image alexia_library_1 = 'images/Jobs/Alexia Library1.png'
    image alexia_tavern_1 = "images/Jobs/Alexia Barmaid1.png"
    image alexia_pits_1 = "images/Jobs/Alexia Pits1.png"
    image alexia_forge_1 = "images/Jobs/Alexia Forge1.png"



define left1 = Position(xpos=0.1)
define right1 = Position(xpos=0.9)
define dissolve2 = Dissolve(2.0)

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



init python:
    _game_menu_screen = "pause_menu"
    # controls if saving allowed at navigation menu
    saving_allowed = True

label splashscreen:
    $ renpy.block_rollback()
    scene black
    $ mouse_visible = False
    scene white
    with fade
    scene splash
    with MultipleTransition([
        False, dissolve2,
        True, Pause(3),
        True])
    scene white
    with dissolve2
    scene black
    with fade
    $ mouse_visible = True

    sv 'A Venus Noire production'

    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .50
            _preferences.volumes['sfx'] *= .70
    return


# The game starts here.
label start:
    jump rowan_intro
