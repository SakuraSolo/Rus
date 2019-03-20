# Global vars that form the story. They should exist from the very start to the end

default alexiaOffer = False
# Sex between Andras and Alexia in the beginning of the game (in first week event)
default andras_alexia_sex = False
# reason why Rowan agreed to serve the twins (in the intro)
default introserve = False
# with whom Rowan had sex in the intro
default jezeraIntroSex = False
default andrasIntroSex = False
# if NTR content should be shown
default NTR = False
# if Alexia had NTR scene with Jezera (in jezera_s_tea_party)
default jezNTR1 = False
# if Alexia lives with Rowan in his room, or it lives separately, in living quarters
default alexiaSeparateRoom = False
# if Rowan knew rumors about new goblin prince
default new_goblin_prince_rumor = False
# temporary variable: if goal 2 is completed
default goal2_completed = False
# Was Rowan friendly to X'zaratl in her intro?  Makes her events happen more quickly.
# TODO: temp fix for "default" bug
define friendly_to_xzaratl = False
# if Rowan had sex with X'zaratl in 'X'zaratl's advances'
default xzaratl_s_advances_rowan_sex = False
# if Rowan used a favor to protect self from X'zaratl in 'X'zaratl's advances'
default xzaratl_s_advances_used_favor = False
# society type (None, 'feudalism', 'might')
default society_type = None
#if Rowan was sucked off by Cla-Min's daughter
default goblin_family_dinner_mins_blowjob = False
# "clamin_bribing_proposition" - flag that she'll be upset if you lose the item or refuse to have sex with her clan later.
default clamin_bribing_proposition_balasts_brand_gifted = False
# Rowan claimed Helayna during assault on Raeve Keep
default raeve_keep_rowan_claimed_helayna = False
# Rowan want to intorduce Alexia to Greyhide
default drinking_buddies_introduce_alexia = False
# What suggestion did Rowan make to Greyhide after a round of friendly drinks?
define drinking_buddies_suggestion = False
# if Alexia and Greyhide had sex
default alexia_greyhide_sex = False
#Raeve keep assault: player tried to protect Helayna.
default raeve_keep_rowan_tried_protect_helayna = False
# if Rowan shares room with Helayna
default rowan_shares_room_with_helayna = False
# What previous relationship did Rowan and Helayna have? 0 = teacher, 1 = friend, 2 = respected awkwaintence
default helaynaRelationship = 0
default helaynaTitle = 'teacher'
# alexia job maid var
default meetMary = False
default xzaratl_scene_count = 0
#  Who did Alexia go to for help with her book?  1 = No one or she avoided sex scene, 2 = Andras, 3 = Jezera
default alexia_and_her_demon_book = 0
default alexia_has_sex_with_jezera_during_demon_book = False
# Mine
default fucked_sheera = False
default fucked_isaac_mage = False
default isaac_cleric = False
default isaac_mage = False

default old_hero_event = False
default halaynas_day_off = False
default halaynas_day_off_c1 = False
default halaynas_day_off_c2 = False
default halaynas_display = False

default cla_tit_job = False
default helayna_escaped = False
default skordred_bj = False
default skordred_fuck = False

#abbey
default garin_in_rastedel = False

default alexiaForgeIntro = False
default ghBatriLater = False
default ghBatriHelp = "na"
default jezDelaneHelp = "na"
default cliohnaDelaneHelp = "na"
default trustHeartsong = False
default shayaShow = False
default shayaShowFirst = True
default rowanLiurialLie = False
default liurialSex = False
default cliohnaHJ = False
default greyhideMet = False
default helPathChoice = False
default helBedslavePath1 = False
default helAlexiaWhip = False
default alexiaWulump = False
default rowanJezSex = 0
default rowanAndrasSex = 0
default alexiaWhippedRowan = False
default rowanBlameAlexia = False
default alexiaThreesomeStormout = False
default admitIntroSex = False
default rastedelFirstVisit = False
default recruitDaz = False
default helPath = "none"
default ygrissWife = False
default whipJezPotion = False
default friskyDrider = False
default helCuck = False
default helMaidFirst = True
default arzylMet = False
default whitescarMet = False
default andrasPunishmentCounter = 0
default rowanFutaAnal = False
default rowanFutaSuck = False
default futaIntrigued = False
default maryKissLiked = False
default alexiaWatchedJak = False
default escapeBlameSelf = False
default jezeraDress = False
default PostRaidingJezeraHandjob = False
default strangerFirst = True
default jezDenialSex = False
default rowanGaySex = 0
default ghThreesome = False

default nasimAvailable = False
default nasimFirstVisit = True
default nasimAttitude = 0
default aboutTransSeen = False
default aboutFertSeen = False
default bootlegAlexiaSeen = False
default bootlegAlexiaFucked = False
default nasimCatSeen = False

default goal3_completed = False

define servant_route = 0
define overlord_route = 0
define sabotage_route = 0

################################################################################
# Orciad
# state of orciad quest (0 = undiscovered/inactive, 1 = active, 2 = completed, 3 = failed)
define orciad_state = 0
#Rowan can now encounter Batri's raiders while exploring the camp, in case the player wants to join a raid anyway.
default rowan_can_encounter_batri_s_raiders = False
#If Rowan has joined Batri's raiders
default rowan_joined_batri_s_raiders = False
# state of Rowan's visits with Batri ('first visit', 'met', 'repeat visit')
default rowan_met_batri = 'first visit'
# How much has the player increased Batri's power in the camp.  Needed to side with him in the quest.
define batri_power = 0
# Tarish power (spy_on_the_orcs)
define tarish_power = 0
# state of Rowan's visits with Ulcro ('first visit', 'met', 'repeat visit')
default rowan_met_ulcro = 'first visit'
# Has the player found the captured noblewoman's loction?
define found_delane_tent = False
# Which week was the player's previous visit with the noblewoman, used to prevent visiting twice on the same week.
define last_delane_visit_attempt = 0
# Has the player met with Delane already?
define met_with_delane = False
# orciad "explore" count - how many times camp is visited (with "explore")
define orciad_explore = 0
# if Rowan betrayed slaves in "camp_slaves"
define orciad_betray_the_slaves = False
# count of visiting orc priest of Kharos
define orciad_priest_visit_count = 0
# if player had chance to visit priest this turn
define orciad_priest_visited = False
define orciad_priest_training_unlocked = False
# which training Rowan took in orciad priest of Kharos (any 3 of 'climb', 'sneak', 'listen', 'dodge')
#~ define orciad_priest_trainings_completed = []
define orciad_priest_complete_climb = False
define orciad_priest_complete_sneak = False
define orciad_priest_complete_listen = False
define orciad_priest_complete_dodge = False
define orciad_priest_complete_count = 0
# if Rowan took any training before (reset to False on any training)
define orciad_priest_first_training = True
# if Rowan has met Ulgan
define rowan_has_met_ulgan = False
define delane_corruption = False
define delane_corrupt = False
define tarish_angered = False
define tarish_path = False
define get_cla_poison = False
define get_jez_potion = False
define got_cla_poison = False
define got_jez_potion = False
define delane_status = "tent"    #tent / ulcro / batri / etc
define delane_visit = 0 #used to determine how many times the player has visited Delane
define delane_trust = 0
define delane_captivity = False
define delane_affairs = False
define delane_court = False
#How long has it been since the player visited Delane?
define last_delane_visit = 0
define ulcro_path = 0
define delane_gifts = 0
define orciad_ally = "none"
define orciad_ban = False
define seen_delane_bad_end = False
define delane_corruption_occurred = False
define delane_abduction = False
define emmaNotMet = True
define emmaMet = False
define emmaIgnored = False
define woodCarverSaw = False
define emmaRowanSex = False
define emmaPure = True
define batri_raid_count = 0
define delane_plan = False
define batriBoysFirst = True
define batriSweetFail = False
define batriTauntFail = False
define delaneDistraction = False
define ulganBloodmeen = False
define ulganHelpFirst = True
define observePerimeterFirst = True
define perimeterSearchCount = 0
define delaneEscapePerimeter = 0
define orcMatronState = 0
define tarishBetrayed = False
define delaneEscapeWound = False
define desperateEscape = False
define giftHuntFirst = True
define giftHuntAvailable = False
define giftRaidTravel = 1
define knowKraug = False
define giftHuntTraining = False
define kraugCommander = False
define meetingBanditsSeen = False
define findingMonksSeen = False
define findingCaravanSeen = False
define noblesHuntingSeen = False
define summerResidenceSeen = False
define eleanorCaveSex = False
define tarishSex = False



################################################################################
default rowan_draith_sex = False
# using define to work around Ren'py bug and for saves compatibility
# if Alexia knows any magic (set in alexia_s_power)
define alexia_knows_magic = False
# level of Alexia's ice shard spell
define alexia_ice_shard = 0
# times Rowan has had sex with anyone but Alexia (set/used in greyhide_shares_his_people_s_liquor)
define rowan_non_alexia_sex = 0
# Method of Helayna's escape attempt ("rowan", "without rowan", "no escape")
define helayna_escape_method = False
# Can Helayna be moved around the castle? (False until she escapes or not)
define helayna_moveable = False
# If Rowan allowed Draith to perfom test in proposing_drider_occupation
define drider_guard_test = 0
# if Rowan can summon Liurial in throne room
define can_summon_Liurial = False
# number of times Rowan had sex with Greyhide
define rowan_greyhide_sex = 0
# Further sex scenes with Greyhide (after "What happened after drinking Greyhide's alcohol?")
define further_sex_scenes_with_greyhide = False
################################################################################
# if player seen intro of Liurial orgasms control in throne room
define liurial_orgasms_control_intro_seen = False
define liurial_orgasm_control_receded_ever = False
# if currently orgasm control is on
define liurial_orgasm_control_on = False
# orgasm control total time (weeks)
define liurial_orgasm_control_total_time = 0
# if "perform" intro triggerd before
define liurial_perform_intro_seen = False
# if Liurial asked player for permission this week
define liurial_orgasm_control_plea = False
# -1 = no blowjob, 0 = blowjob was requested, >0 - number of weeks
define liurial_weeks_after_blowjob_request = -1
define liurial_domination_count = 0
################################################################################
#Goblin Recruit Variables
define goblinRecruit = False

###################################################################################
#fey variables

define arzylDialogueAvailable = False
define whitescarDialogueAvailable = False
define whitescarDialogueStage = 0


###################################################################################

# temp variables, todo convert into status effects
# Alexia is removed for a while
define alexia_away_weeks = 0
# Alexia can't be assigned to jobs for a while
define alexia_cant_work_weeks = 0


################################################
# Alexia Sex Variables

default alexiaUnfaithful = False
default alexiaAndrasSex = 0
default alexiaJezeraSex = 0


################################################################################
#Rastedel

default rastFirstVisit = True
default rastLodgeAccess = False
default rastAlleysAccess = False
default rastCodificeAccess = False
default rastGuildAccess = False
default palaceStage = 1
default palace2Repeat = False
default lodgeFirstVisit = True
default delaneReject = False
default amerFirstSex = True
default postBattleVisit = False
default rastCurrentEnd = False



default roomName = ""
default menuActive = False
default statusActive = False
define notification = False

define gui.room_name_font = "Kinesis_Std_Italic.otf"

init python:
    # story vars can be registered here to be shown in the debug
    story_vars_list = ['alexiaOffer', 'andras_alexia_sex', 'introserve', 'jezeraIntroSex', 'andrasIntroSex', 'NTR', 'alexiaSeparateRoom',
        'new_goblin_prince_rumor', 'goal2_completed', 'friendly_to_xzaratl', 'xzaratl_s_advances_rowan_sex', 'xzaratl_s_advances_used_favor',
        'society_type', 'goblin_family_dinner_mins_blowjob', 'clamin_bribing_proposition_balasts_brand_gifted', 'raeve_keep_rowan_claimed_helayna',
        'drinking_buddies_introduce_alexia', 'drinking_buddies_suggestion', 'alexia_greyhide_sex', 'raeve_keep_rowan_tried_protect_helayna',
        'rowan_shares_room_with_helayna', 'helaynaRelationship', 'helaynaTitle', 'meetMary', 'xzaratl_scene_count', 'orciad_state',
        'rowan_can_encounter_batri_s_raiders', 'rowan_joined_batri_s_raiders', 'rowan_met_batri', 'batri_power', 'rowan_met_ulcro',
        'found_delane_tent', 'last_delane_visit_attempt', 'met_with_delane', 'rowan_draith_sex', 'alexia_knows_magic', 'alexia_ice_shard',
        'rowan_non_alexia_sex', 'helayna_escape_method', 'helayna_moveable', 'drider_guard_test', 'can_summon_Liurial', 'alexia_away_weeks',
        'alexia_cant_work_weeks', 'further_sex_scenes_with_greyhide', 'liurial_orgasms_control_intro_seen', 'liurial_orgasm_control_receded_ever',
        'liurial_orgasm_control_on', 'liurial_orgasm_control_plea', 'liurial_weeks_after_blowjob_request', 'liurial_domination_count', 'orciad_explore',
        'tarish_power', 'orciad_priest_visit_count', 'orciad_priest_visited', 'orciad_priest_trainings_completed', 'orciad_priest_first_training',
        'rowan_has_met_ulgan', 'liurial_perform_intro_seen', 'liurial_orgasm_control_total_time', 'back_for_seconds', 'resistance_futile', 'alexia_dungeon_week_4',
        'mine_level_3_party', 'orc_wants_to_lead', 'old_hero_destroy', 'old_hero_occupy', 'old_hero_trade', 'test']
