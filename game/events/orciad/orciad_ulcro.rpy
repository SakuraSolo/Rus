init python:

    #first visit to Ulcro in orciad camp
    event('first_visit_ulcro', triggers='orciad_ulcro', conditions=("week >= 4",), run_count=1, group='orciad_camp', priority=pr_map_res)
    #repeat visit (if Rowan failed diplomacy check and he has not yet met Ulcro)
    event('visitUlcro_repeat', triggers='orciad_ulcro', conditions=("week >= 4", 'rowan_met_ulcro=="repeat visit"'), depends=('first_visit_ulcro',), group='orciad_camp', priority=pr_map_res)
    #Repeat meetings with Ulcro
    #The following event occurs if Rowan returns to see Ulcro after meeting him the first time, and has not completed ulcro's path
    # TODO: check for completion
    event('repeat_meetings_with_ulcro', triggers='orciad_ulcro', conditions=("week >= 4", 'rowan_met_ulcro=="met"'), depends=('first_visit_ulcro',),
        group='orciad_camp', priority=pr_map_res)


#visit ulcro
label first_visit_ulcro:

#first visit
scene bg26 with fade
$ rowan_met_ulcro = 'repeat visit'

"Rowan set off towards the center of the main camp, at which there was a small hill that Ulcro had set up his tent, surrounded by those belonging to his lieutenants. As the hero got closer, he noticed that the orcs around him were getting older and more scarred."
"These soldiers were clearly veterans of the previous war, many of them still wore Bloodmeen issued armor with Karnas's sigil upon it."
"They also cared greatly for their equipment, actively cleaning and maintaining it.  He even saw one who was sharpening axes and swords on a grindstone."
"At the base of the commander's hill sat a carved wooden altar dedicated to Kharos. None were currently praying at the altar, but Rowan spotted an offering had been placed there recently. A rather grisly trophy he decided not to examine too closely."

show orc soldier neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

os "Human, we hear from Tarish you be demon's errand boy. Say why you here at warchief's tents?"

if check_skill(15, 'diplomacy')[0]:
    ro "The one whom I serve is the son of Kharnas and has taken possession of Bloodmeen castle. I'm gathering the armies that continue the fight in the name of the many faced God to join together, Ulcro is needed once again."
    "The orc eyed Rowan suspiciously for several moments, then spoke again."
    os "Then follow me."
    jump ulcroFirstMeeting

else:
    ro "I represent the new lords of Bloodmeen, who've come seeking soldiers and warriors to join them once again. As he was one of the great generals of the last war, I have great interest in meeting with Ulcro."
    "The orc eyed Rowan suspiciously for several moments, then spoke again."
    os "If you truly respect Ulcro, prove it with a gift. Give him a weapon worthy of a general of Bloodmeen, then he will meet with you."
    ro "(Almost any weapon will do for that. I probably shouldn't give him anything unique, I might not get it back.  A common iron axe from Cla-Min will do the job.)"

    $ event_tmp['gifts_to_ulcro'] = [item for item in avatar.inventory.bp if 'weapon' in item.keywords]
    if len(event_tmp['gifts_to_ulcro']) > 0:
        $ event_tmp['choosen_gift'] = menu([('Walk away', 'walk_away')] + [(item.name, item.uid) for item in event_tmp['gifts_to_ulcro']])
        if event_tmp['choosen_gift'] != 'walk_away':
            $ avatar.inventory.remove(event_tmp['choosen_gift'])
            #If player has a weapon in their inventory, they can gift it.  Any melee weapon is suitable.  If the player gifts one:
            os "Ulcro will be grateful for this, follow me."
            jump ulcroFirstMeeting

    #Add Orciad note3 to journal
    $ journal.add_quest_note('orciad', 'note3')
    jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label visitUlcro_repeat:
#repeat visit (if Rowan failed diplomacy check and he has not yet met Ulcro)

os "If you truly respect Ulcro, prove it with a gift. Give him a weapon worthy of a general of Bloodmeen, then he will meet with you."
ro "(Almost any weapon will do for that. I probably shouldn't give him anything unique, I might not get it back.  A common iron axe from Cla-Min will do the job.)"

$ event_tmp['gifts_to_ulcro'] = [item for item in avatar.inventory.bp if 'weapon' in item.keywords]
if len(event_tmp['gifts_to_ulcro']) > 0:
    $ event_tmp['choosen_gift'] = menu([('Walk away', 'walk_away')] + [(item.name, item.uid) for item in event_tmp['gifts_to_ulcro']])
    if event_tmp['choosen_gift'] != 'walk_away':
        $ avatar.inventory.remove(event_tmp['choosen_gift'])
        #If player has a weapon in their inventory, they can gift it.  Any melee weapon is suitable.  If the player gifts one:
        os "Ulcro will be grateful for this, follow me."
        jump ulcroFirstMeeting

jump campMenu

################################

label ulcroFirstMeeting:

scene bg30 with fade
show ulcro neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

#Mark Orciad note3 as complete, if it was added to the journal
$ journal.complete_quest_note('orciad', 'note3')

"After giving a moment for his eyes to adjust to the darkness of the tent, the leader of this horde of orcs came into vision."
"Sitting on a throne of sorts was an older orc, covered in scars and missing an eye. He was slouched down, but watched the new arrival with great intensity. Rowan could tell at once that this was a veteran of many battles, like himself."
"Even though Ulcro was maintaining every appearance of being calm and uninterested, the human could see how tense his muscles were, how he was holding his axe in such a way that it could be brought to bare in an instance, if necessary."

ro "I bring you greetings from Bloodmeen, great warlord Ulcro."

ulc "Rowan. Tell me, what's a great hero of humans doing as a demon's messenger?"

"So, the warchief knew who Rowan was. Given his age and rank, it should have been more surprising if he hadn't. The hero admonished himself silently, then changed plans."

ro "Someone important to me was taken away. We humans can be a bit, sentimental."

"To Rowan's surprise, the orc actually chuckled and seemed to relax!"

ulc "A year ago I wouldn't have understood, now I do. My heart has been stolen by a woman I cannot please. Rowan, help me reach my beloved's heart like she has taken mine and I will gladly serve your master."

show rowan necklace shock at midleft with dissolve

"This was the third time that the orc's words had surprised Rowan and this time he wasn't able to keep it from showing on his face."

ulc "Do not be so surprised. Orcs can love too. My lovely lady lost her home and now I want to give her a new one."

show rowan necklace neutral at midleft with dissolve

ro "The human woman that Batri's raiders found?"

"The chief spat on the ground."

ulc "That bastard almost did unspeakable things to my love. She is no mere woman, she is of noble blood. Though this is also a part of my troubles with her, it is a trouble I intend to overcome for her sake."

ro "Can talk to her? Is she in your tent?"

ulc "No. She isn't here or in any of my commander's tents. She is hidden away somewhere safe, it isn't your place to see her."

ro "Well then, can you at least tell me what exactly is the problem?"

"Ulcro waved his arms around the room."

ulc "This!  An orc camp isn't a place for a noblewoman! She doesn't have proper beds, proper clothes, or proper food! I want to convince her I can give her just as good a life as she had back in her family's home."
ulc "I don't care if you steal, buy, or even make those treasures for her, just bring them to me! If you need a raiding party I will provide you one, but I refuse to let this army go anywhere until my love accepts me!"
ulc "Then, and only then, will your master get his soldiers."

ro "I understand.  It was an honor to meet you, warchief."

"Ulcro merely gave a dismissive wave, done with the hero for the time being."

#Add Orciad note5 to journal
$ journal.add_quest_note('orciad', 'note5')
$ rowan_met_ulcro = 'met'
$ giftHuntAvailable = True
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label repeat_meetings_with_ulcro:
#Repeat meetings with Ulcro
#The following event occurs if Rowan returns to see Ulcro after meeting him the first time, and has not completed ulcro's path

if ulcro_path < 2:
    scene bg30 with fade
    show rowan necklace neutral at midleft with dissolve
    show ulcro neutral at cliohnaright with dissolve
    ulc "The lady iz as angry as always. You take her more gifts, den we talk."

elif ulcro_path == 2:
    scene bg30 with fade
    show rowan necklace neutral at midleft with dissolve
    show ulcro neutral at cliohnaright with dissolve
    ulc "I think she iz starting to come around, but she needs more. Convince her, den we talk."
      
else:
    jump eleanorUlcroPath4


ro "Very well."

jump campMenu

label eleanorUlcroPath4:
    
scene bg30 with fade
show rowan necklace neutral at edgeleft with dissolve
show ulcro neutral at center with dissolve
show eleanor dress happy at edgeright with dissolve

"Rowan walked into Ulcro’s tent, only to find an unusual occupant. Delane was sitting at the side of Ulcro’s seat, with hair disheveled in a telling way. Ulcro had his arm around her, and despite the strangeness of the scene Delane was looking back at him with tender eyes."

ulc "Thanks to yous help, I haz what I sought. A beautiful concubine dat loves an' accepts me. I am ready to follow yous Master."
ulc "But, one problem remains. Dat boy. Batri."
ulc "He want a fight, a fight. So Ulcro will give him one."

show eleanor dress concerned at edgeright with dissolve

"Lady Eleanor tilted her head at the conversation."

ele "Rowan!?"
ele "So you were working for Ulcro?"

"Rowan went to a single knee and lowered his head."

ro "No, my lady. I serve other forces. Ones who understood that the best result for everyone would be Ulcro continuing to lead this tribe, with you by his side."

show eleanor dress happy at edgeright with dissolve

ele "I underestimated your slyness, hero."

show rowan necklace happy at edgeleft with dissolve

ro "And yet, you don’t say that as though it were a bad thing."

ele "I suppose not."

ulc "Yous come back in few days, den you see what happen to those who challenge Ulcro."

$ ulcro_path = 5
$ delane_status = "ulcro"
jump campMenu

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

