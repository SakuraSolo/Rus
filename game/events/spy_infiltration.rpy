# Infiltration events
# The spy goes about either bringing the local leaders under their control or quietly replaces them.  The people never learn who they now serve.

# Infiltrating a village gives the same base income and guilt as capturing it, but less infamy.  Choosing to infiltrate has your chosen spy sent to that resource and they are unavailable for other missions until they finish.  The village is marked as explored.  A post exploration event is added at the end of a period of time, base is randomly 2-3 weeks, that is chosen immediately.  This event may modify how long it takes for the actual infiltrate event fires.

# Choose one of the following events at random to modify time and results.



############################################
label sm_infiltration_normal(tmp_spy):
# 1, As planned.
# No req.  No change to week time.

# Show village background.
scene village day

# name of the village
$ temp = get_map_resource(tmp_spy.mission.loc[0], tmp_spy.mission.loc[1]).name
"Over the last [tmp_spy.mission.duration] week(s), [tmp_spy.name] has slowly brought the high ranking members of the [temp] either under [tmp_spy.poss] control or replaced them with more impressionable individuals."
"Arrangements have been made to divert their taxes and goods towards drop points for Bloodmeen's agents to collect, which will then be transferred directly into the twin's treasury."
"The citizens of Rosaria are none the wiser that they now pay tribute to half demons with ambitions of conquest."
"However, soon they won't mind much either."
"As [tmp_spy.poss] parting gift, [tmp_spy.name] set into motion a campaign or propaganda that should eventually make the people far less open to the idea of sending levies to their lords should war come to Rosaria."
"[tmp_spy.name] has returned to Bloodmeen and is now available for further missions."

# End scene, no effect.
$ capture_resource(tmp_spy.mission.loc[0], tmp_spy.mission.loc[1])
$ add_spy_exp(tmp_spy.uid, 100)
return

############################################

label sm_infiltration_dominator_prisoners(tmp_spy):
#2, Dominator gets some prisoners.
#Req Master/Mistress trait and at least one open dungeon space.  No change to week time.

scene
$ temp = tmp_spy.pers.capitalize()
"[tmp_spy.name] has returned to the castle after [tmp_spy.mission.duration] week(s), reporting success in bringing village under Bloodmeen control. [temp] was very eager to explain [tmp_spy.poss] escapades, making Rowan rather uncomfortable."
"True to form, [tmp_spy.name] also made off with a few of the more attractive villagers afterwards. [temp] had been using them as toys during [tmp_spy.poss] off time, and now with access to the brothel's playthings again has turned them over to the Twins."
"Andras has given them accommodations in the dungeons, at least for the time being.  They have no real memory about what happened while under [tmp_spy.name]'s thrall, and are somewhat distressed about suddenly being behind bars."

#End scene, gain two or three prisoners.
$ change_prisoners(dice(2)+1)
$ capture_resource(tmp_spy.mission.loc[0], tmp_spy.mission.loc[1])
$ add_spy_exp(tmp_spy.uid, 100)
return

############################################

label sm_infiltration_delays(tmp_spy):
#3, Delays.  Impulsives are even worse.
#Req non-methodical trait.  Adds an extra two weeks to completion time, impulsives gain four weeks instead.

scene
"Long overdue from when [tmp_spy.pers] was suppose to finish [tmp_spy.poss] mission, [tmp_spy.name] has finally returned with a report of a successful capture.  It took [tmp_spy.poss] [tmp_spy.mission.duration] week(s) to finish the mission."
"Jezera has already reprimanded the spy for [tmp_spy.poss] incompetence, but will leave the decision as to whether or not [tmp_spy.name] will be removed from the staff list to Rowan."
"In the meantime, Shaya made an attempt to discern why such a delay happened.  Behind layers and layers of excuses and embellishments, she managed to gleam a little bit of information."

# (if spy is not impulsive)
if 'Impulsive' not in tmp_spy.traits:
    "It seemed that [tmp_spy.name] had failed to account for something that only the most methodical of planners would have noticed.  It didn't critically endanger the mission, but did force a significant delay to account for."
# (if spy is impulsive)
else:
    "An anomaly of sorts was present in the village that would have to be carefully planned for.  Most spies would have never realized this would be a problem until after their plans were significantly advanced."
    "[tmp_spy.name]'s usual brashness compounded the problem, essentially doubling the length of the mission."

#remerge
"The spymaster recommended that if Rowan wishes to avoid these sorts of delays in the future, he must be prepared to hire only the most methodical of spies.  Otherwise they are simply an eventuality that must always be prepared for."

#End scene, no further effects other than delay.
$ capture_resource(tmp_spy.mission.loc[0], tmp_spy.mission.loc[1])
$ add_spy_exp(tmp_spy.uid, 100)
return

############################################


label sm_infiltration_bribe(tmp_spy):
#Success + Bribe
##No req.  No change to week time.

#for now - randomly determine whether the infiltration succeeds or fails - success chance should be 75%
if dice(4) <= 3:
#success
    "Over the last few weeks, [tmp_spy.name] has slowly brought the high ranking members of the village either under [tmp_spy.poss] control or replaced them with more impressionable individuals."
    "[tmp_spy.persU] found the leadership of the village quite willing to hear out [tmp_spy.poss] proposals."
    "As a result, several of the villagers sent with them a trove of cash and jewels to Rowan as a personal gift. [tmp_spy.name] held out [tmp_spy.poss] arms to Rowan, and they flowed with golden gifts."
    "Arrangements have been made to divert their taxes and goods towards drop points for Bloodmeen's agents to collect, which will then be transferred directly into the twin's treasury. All in all, a good heist."
    "[tmp_spy.name] also brought with [tmp_spy.poss] a letter from the village elder bearing with it a pledge of fealty. The language the elder used was gaudy and filled with sycophantic praise. There will be no resistance from him or his people."
    "[tmp_spy.name] has returned to Bloodmeen and is now available for further missions."

    #gain personal gold.
    $ change_personal_gold(10)
    $ capture_resource(tmp_spy.mission.loc[0], tmp_spy.mission.loc[1])
    $ add_spy_exp(tmp_spy.uid, 100)
    return
else:
#failure
    #Frequency varies based on stats of agent sent.  No change to week time. (todo)
    "[tmp_spy.name] had been tasked by Rowan to bring high ranking members of the village under [tmp_spy.poss] control or replace them with loyal agents. However, not all has gone as planned."
    "[tmp_spy.name] arrived at the castle out of breath. The mission had gone well at first. Many of the local leaders had proven very receptive to the webs that [tmp_spy.name] had been weaving."
    "The other day, [tmp_spy.pers] had been attending a speech by a local village leader in the commons. It was supposed to be a normal village meeting."
    "But, in the middle of his speech he declared that [tmp_spy.name] was an agent of demons sent to bring the village to heel. He further revealed that some of his friends had already been killed by [tmp_spy.name]"
    "How he discovered that a plot was afoot is still a mystery. But, it meant that [tmp_spy.name] had been forced to flee from the village in a hurry."
    "Bruises on [tmp_spy.poss] arms and torso still bear the grips of villagers who had attempt to wrest [tmp_spy.him_her] from [tmp_spy.poss] horse."
    "Rowan listened to the whole story impassionatly, along with the apologies of [tmp_spy.name]. It seemed that infiltration is not a tactic that will work here."
    "The only options are destruction or occupation. A shame, they could have taken the easy way out."
    "[tmp_spy.name] has returned to Bloodmeen and is now available for further missions."

    #Village is uncaptured, if players return they only have occupy or destroy options.
    # TODO: 'unvisit' village, mark that no spy mission is available there
    return
