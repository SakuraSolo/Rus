#Orciad Showdown

init python:
    event('orciadShowdown', triggers="week_end", conditions=('delane_status != "tent"',),
        group='ruler_event', run_count=1, priority=pr_ruler_high)


label orciadShowdown:

scene bg26 with fade

$ journal.complete_quest_note('orciad', 'note7')
$ journal.complete_quest_note('orciad', 'note8')
$ journal.complete_quest_note('orciad', 'note9')
$ journal.complete_quest_note('orciad', 'note10')
$ journal.complete_quest_note('orciad', 'note11')
$ journal.complete_quest_note('orciad', 'note14')
$ journal.complete_quest_note('orciad', 'note15')
$ journal.complete_quest_note('orciad', 'note16')
$ journal.complete_quest_note('orciad', 'note17')
$ journal.complete_quest_note('orciad', 'note18')
$ journal.complete_quest_note('orciad', 'note19')
$ journal.complete_quest_note('orciad', 'note20')
$ journal.complete_quest_note('orciad', 'note21')
$ journal.complete_quest_note('orciad', 'note22')
$ journal.complete_quest_note('orciad', 'note23')
$ journal.complete_quest_note('orciad', 'note24')
$ journal.complete_quest_note('orciad', 'note25')
$ journal.complete_quest_note('orciad', 'note27')
$ journal.complete_quest_note('orciad', 'note28')
$ journal.complete_quest_note('orciad', 'note30')
$ journal.complete_quest_note('orciad', 'note31')
$ orciad_state = 2

"Rowan had not been surprised when he had received word, from one of the twins agents, that something big was happening at the camp. After his own role in the events of the last few days, it was only time before the already tense relations between those vying for power came to a head."
"As he approached the camp, he knew that whatever it was, it must be important. He didn’t even see the sentries at their usual posts, and even orcs weren’t stupid enough to lower their defences for no good reason."
"When he got closer, he could see where the sentries had gone. A large group of orcs, perhaps nearly every one that made up Ulcro’s tribe, was crowded around the centre of the camp. Even from this distance he could hear the whoops and the jeers, as they jostled against each other."

if delane_status == "ulcro":
    $ journal.add_quest_note('orciad', 'note32')
    jump orciadShowdownUlcro

elif delane_status == "batri":
    $ journal.add_quest_note('orciad', 'note32')
    jump orcaidShowdownBatri

elif delane_status == "tarish":
    $ journal.add_quest_note('orciad', 'note32')
    jump orcaidShowdownTarish

else:
    $ journal.add_quest_note('orciad', 'note33')
    jump orcaidShowdownEscape


label orciadShowdownUlcro:

"He knew it could only mean one thing, newly emboldened by having lady Delane at his side, Ulcro had challenged Batri to do away with his snide comments and disobedience for good."
"As he entered the camp, he saw a pair of familiar faces coming towards him, Ulcro and his new mate, the lady Delane. Considering what was about to occur, they both seemed strangely chipper. More than that, they both seemed to be expecting him."

show rowan necklace neutral at edgeleft with dissolve
show ulcro neutral at center with dissolve
show eleanor dress happy at edgeright with dissolve

ele "Ah, Rowan, there you are. We were wondering when you would show up."

ro "You were expecting me?"

ele "Who do you think sent the little birdies that informed your masters of this little ruckus?"

ro "Next time, I suppose I will have to endeavor to get here sooner. However, you two look unusually in good spirits considering what is about to occur."

"The lady laughed, and Rowan could only think of the change in her since he had first met her, when she was a sad and angry woman, clothed in tatters and caged."

ele "That rowdy little upstart is no match for my man. He’ll see to him in no time at all, and when he is dead, his boys will have to fall in line, and this little rebellion will be over for good."

"Ulcro said nothing, he just stood at the side and beamed with pride at what Delane was saying. He was utterly besotted, and now she had made up her mind with Rowan’s help, it had not taken the noble long to wrap him around her finger."
"A loud horn sounded, long and low, and Delane smirked upon hearing it."

ele "That will be for us."

ulc "We talk after Batri taken care of, hum- Rowan. Once he dealt with, we have deal as promised."

ro "Good luck."

ele "Oh, don’t worry, he won’t need luck."

"Rowan watched as the two left, heading towards the crowd. The woman slipped her arm around the orc’s waist as they walked, and the hero could only hope that her support, and no doubt acts more carnal in nature, had rekindled enough of a flame in him to overcome Batri’s youth."

jump orciadFight


label orcaidShowdownBatri:

"He knew it could only mean one thing, the raid he helped Batri orchestrate had been the last straw, and now Ulcro, cornered by such a blatant act of defiance, had no option other than to play into the younger orc’s hand by accepting his challenge."
"As he entered the camp, he was greeted with a sight that would have shocked him only a few months ago, but was now becoming all too familiar. Batri approached him, a loud laugh emerging from him as the woman at his side, the once prideful lady Delane, tried to fondle his cock through his armour as they walked."

show rowan necklace neutral at edgeleft with dissolve
show batri neutral at cliohnaright with dissolve
show eleanor naked aroused at edgeright with dissolve

bat "Der yous are humi, was wonderin' when you’d get here."

ro "You were expecting me?"

bat "Who yous think let dem spies know dis was happenin’?"

"Rowan was surprised, Batri didn’t seem like the type for any sort of subterfuge. He had chosen to support him as chief because of his strength, not because of his intelligence. Maybe the lady Delane was rubbing off on him in more ways than one."

ro "Well I am here now."

bat "Just in time too."

"The noble was still fumbling at his armour and failing, when the orc placed one of his green, oversized hands on her breast, causing her to moan. If she felt any shame at Rowan being present, he could not discern it."

bat "First, I kill dat old bastard, easier than killin’ baby pink. When he saw his precious humi with her tongue down Batri throat, he looked like he was gonna cry."

"Batri laughed again, even louder than before. Rowan couldn’t help but feel a little bit sorry for the old orc, and the part he had played in the current outcome."

bat "Den, well, you tell 'im, humi."

ele "Once Ulcro is dead, Batri is going to… Umm.. Well..."

bat "TELL 'IM, SLUT!"

"Batri spanked her on the ass, hard, and again, she let out a moan. She clearly enjoyed being manhandled by the orc, perhaps the spy had done the job a little too well."

ele "Chief Batri is going to fuck me with his magnificent cock in front of the entire tribe for hours until I can’t take anymore. Mmmmm, I can’t wait…"

"Clearly turned on by the thought, she began to deeply french kiss the orc, who once again chuckled at her enthusiasm."

if avatar.corruption < 69:
    "Rowan did his best to not show it, but the sight made him a little bit sick. He couldn’t help but feel guilty, seeing what Delane had now become, and knowing he was responsible."
    $ change_base_stat('g', 2)

else:
    "Rowan couldn’t help but smile at the new Delane. Thanks to the efforts of Bloodmeen’s spies, the noble would finally learn her place. Perhaps Batri would even let the other orcs use her for relief once he had grown tired of her."

"As he was contemplating this, a low, loud horn rang out over the camp - a challenge had been issued. The time for battle had come."

bat "I kill Ulcro now, den we talk. But Batri very happy wit’ dis slut, humi. Once dis done, you and your masters have Batri’s support."

"Batri turned and headed off in the direction of the huddle, ready to face the tribe’s chief in a fight to the death. Delane flashed Rowan and embarrassed smile, and then headed off after him. The hero was left alone, wondering if he had backed the right horse. He would soon find out, at least."

jump orciadFight


label orcaidShowdownTarish:

"It could only mean one thing, Tarish’s plan had worked. Faced with a missing Delane, Ulcro would have accused Batri, and Batri would have denied it, since he was actually innocent for once. Ulcro, in a rage, must have challenged the younger orc, aiming to kill him over the woman."
"As he entered the camp, he was greeted with a sight that made him feel a little bit uneasy. Tarish was walking in his direction looking like the cat that got the cream, a huge grin on her face."

show rowan necklace neutral at midleft with dissolve
show tarish neutral at midright with dissolve

tar "Der you are humi, been waitin’ for yous."

ro "You knew I was coming?"

tar "Who do you think told dem spies about what was goin’ on. For a humi yous ain’t dat smart at times."

"She laughed at her own joke, she was clearly in a great mood."

ro "Well, I am here now, that is what matters."

tar "True, true. Everythin’ worked out exactly as we planned."
tar "When da humi went missin’ wit’ your help, old Ulcro went straight to Batri an’ accused him of takin’ his precious toy. Batri rightly denied it, an’ dat only made da old bastard even more mad."

"Rowan could tell from the zeal with which she told the story that she was very proud of how she had outwitted the two male orcs."

tar "So Ulcro challanges ‘im to a fight to the death, playin’ right into our hands. While those two were arguing I had my boys sneak into their tents and use dat poison you got me."
tar "Don’t matter which one a’ da idiots wins, they’ll both be dead by the end of it, an’ then I cans make my move."

ro "And lady Delane?"

tar "Aww, yous soft on da slut, hero? Don’t yous worry, she’s fine. Wet an’ ready for later. "
tar "Da tribe will give her one hell of a ride after dis."

if avatar.corruption < 69:
    "Rowan did his best to not show it, he felt a little bit sick. He couldn’t help but feel guilty, knowing he was responsible for what was about to happen to Delane."
    $ change_base_stat('g', 2)

else:
    "Rowan couldn’t help but smile. Thanks to the efforts of Jezera’s little helper, the noblewoman would finally learn her place. He imagined it would be quite the show."

"As he was contemplating this, a low, loud horn rang out over the camp - a challenge had been issued. The time for battle had come."

tar "I don’t wanna miss dis. Come find me afterwards, we talk about promise to serve yous masters."

"She left to go and watch the fight. Rowan was left to ponder if he had made the right decision - sure, the orc was clearly more intelligent than most and very cunning, but would the orcs really follow a female?"

jump orciadFight


label orcaidShowdownEscape:

"He knew it could only mean one thing, his role in helping Delane escape had escalated to violence consequences."
"Faced with a missing Delane, Ulcro would have accused Batri of taking her, and Batri would have denied it, since he had not. Ulcro, in a rage, must have challenged the younger orc, aiming to kill him over the woman."

jump orciadFight


label orciadFight:

#cg1
scene black with fade

"Getting to the front of the crowd was no easy task, he had to force his way through the orcs, who continued to push and shove, clearly agitated by what was about to occur, and their differing loyalties."
"When he finally managed to push his way to the front, he saw the two orcs, facing each other, ready to battle to the death."
"Ulcro had chosen a battleaxe so large that it was a two handed weapon, even in the hands of an orc like himself. Batri, on the other hand, had elected to wield two bastard swords as if they were normal swords."
"Even if he had no dog in this fight, the warrior in Rowan would still be interested in the outcome. Many soldiers often debated the merits of youth versus experience, he himself had on many occasions."
"Discussions of these sorts were all you really had when waiting for battle, in a vain attempt to pass the time, and turn your thoughts from the possibility of impending death. Now, he would get to see an almost ideal case study though."
"Ulcro had been a chief for many years, and even fought in campaigns, he had probably killed more men than Batri had even seen in his long life."
"That sort of experience was invaluable, it brought with it technique tested in battle, and more importantly, the ability to think reasonably and keep your head."
"Batri on the other hand, had all the advantages of youth. He was undeniably physically stronger, and should the battle go long, he had more stamina. He had also not suffered the many wounds Ulcro had over the years, which would also be a benefit to him."
"Could he keep his cool though? The young were often rash, and there was always the chance Ulcro could goad him into making a mistake."
"Regardless, Rowan was about to get his answer. The horn sounded for a second time, signalling the beginning of the battle."

#cg2
scene black with fade

"The younger orc wasted no time, coming at Ulcro like an animal released from a cage. He hacked and slashed at the chief with both swords, and all the hatred that had been brewing since he had decided Ulcro was too weak to lead the tribe."
"Ulcro did his best to block him with his axe, using both the large blade, and its long metal handle to shield himself, but he was already on the back foot, and with each blow he was forced to back peddle a little more."
"Soon he found himself at the edge of the crowded ring of onlookers that had gathered around them, with nowhere left to go. The first blow came down, a vertical slash he blocked with the heavy axe, but, as he soon learned, it had been a feign to force an opening."
"The second sword found his side, biting deep. Ulcro let out a roar in pain and brought the axe down to bear, cutting the arm that had wounded him. Batri let go of the sword as pain surged through him, and it clattered to the floor."
"Both now injured, they circled each other, each looking for an opening."

if delane_status == "ulcro":
    "Batri came at the orc, again and again, but each time Ulcro managed to dodge the blade or turn it away. No matter how he probed, Batri could not find an opening in the chief’s defences, and it began to frustrate him."
    "This time, it was experience that triumphed over youth. The moment the old orc had been waiting for finally came when Batri over extended himself, attempting to force through Ulcro’s defence, and the chief turn away from the blade, sending Batri sprawling with own large weapon."
    #cg3
    scene black with fade
    "Before he could recover, Batri found his enemy standing over him, axe in hand. Most of the orcs chanted the chief’s name as he brought the blade down to finish the would be usurper, and then it was over."
    "He leaned on the axe, exhausted as the chants grew louder, but to Rowan it seemed he couldn’t even hear them. Ulcro just gazed happily at the woman who had finally accepted his advances."
    "The hero realised that he might have forgotten the most important variable in his earlier analysis; having something to fight for."
    jump orciadAftermathUlcro


else:
    "Batri came at the orc, again and again, but each time Ulcro managed to dodge the blade or turn it away. But each successful parry seemed to take more and more from the older warrior, and Rowan wondered how much longer he could last."
    "It looked like youth would win out over experience this day. Despite his years as a seasoned warrior, Ulcro could do very little in the way of fending off the younger, stronger Batri, as his stamina was just too much for him."
    "The younger orc was finding ways through his defences now, just small wounds, but it was only a matter of time."
    "In desperation, Ulcro swung out with his axe, in one last attempt to mortally wound his assailant, but Batri ducked under it with ease and slashed low, hamstringing the old chief."
    #cg4
    scene black with fade
    "Ulcro fell to his knees, unable to stand now, as Batri brought his sword down, cutting deep into his neck. Two or three hacks later, and he had severed clean through the spine."
    "As the crowd began to chant his name, he picked up the head, and let out a loud roar of victory."

    if delane_status == "tarish":
        "As it happened, his celebration turned out to be a little premature. Suddenly, Batri began to cough violently, dropping the head as he brought his hands to his mouth. Black blood, a result of the deadly poison he had brought Tarish, now covered them."
        "He fell to his hands and knees, continuing to cough up more and more blood, as the crowd of orcs looked on, shocked at what was happening. Batri’ eyes darted around, looking for someone who would help, some shaman or priest."
        "None would arrive quickly enough. Shaking in violent spasms, he coughed one last time, and collapsed to the ground."
        jump orciadAftermathTarish

    else:
        jump orciadAftermathBatri


label orciadAftermathUlcro:

scene bg26 with fade

"After a few moments, the old orc saw Rowan at the front of the crowd, and started to walk towards him with a grin on his face."

show rowan necklace neutral at midleft with dissolve
show ulcro neutral at cliohnaright with dissolve

ulc "What yous think of dat, Rowan?"

ro "Very good, I guess youth is no match for experience after all."

"The orc let out a loud laugh from the bottom of his belly."

ulc "Dat’s true! Hopefully now dem boys will see who iz chief around here."

"The chief clapped one of his rather large arms around the much smaller man."

ulc "Ulcro cannot thank you enough for what yous done for ‘im, whatever tribe can do for yous and your masters, dey will. Ulcro promises."

ro "Thank you, Ulcro."

ulc "Many things to see to now, including woman."

"He grinned again, and the hero found it strange to see an orc so happy."

ulc "Yous come back in few days, we have big feast, thank friend Rowan."

ro "You don’t have to do that."

ulc "Ulcro insist!"

"The two continued to exchange pleasantries until Ulcro excused himself to go and look for his mate, presumably, Rowan thought, to get a reward for his victory. As the other orcs started to dissipate, Rowan made his way out of the camp to continue his duties."

$ orciad_ally = "ulcro"

scene black with fade

"A few days later..."

scene bg26 with fade
show rowan necklace neutral at edgeleft with dissolve
show wild orc neutral behind bg26

"Rowan had been through the camp many times in recent weeks. In many ways, it has become almost cozy to him. Even the usual festivals and celebrations had become familiar. But, tonight was different."
"Even as he was approaching the camp, he could hear an uproar like he’d never heard before. Not even the fight earlier had this level of intense excitement. The orcs were celebrating, and they did not celebrate in a polite way." 
"Inside the limits of the camp, the first thing Rowan noticed was how bright it was. At night, there were generally only campfires and the odd torch for light. But, tonight there were so many torches that one could mistake it for day."
"The orcs partied like only they could. It was pure chaos. Dancing and laughing. Drinking and fucking. Fighting and arguing."
"Rowan had to dodge out of the way of one orc who was staggering back and forth drunk. It would not be the last time tonight."

wo "Pah. Humi."

"He stopped to watch when one orc, a big grey fighter whose age and scars seemed to suggest that he’d been around for the last war, smashed open a younger foe’s skull in the fighting pits. A cheer went out. It was almost a re-enactment of the earlier fight."
"Yet, the brutality was never taken too far. For all of the chaos of the celebration, there appeared to be the odd heavily armed guard patrolling the camp making sure no one acted out. It was a celebration, but a controlled affair. No looting, no violence against those who had not agreed to fight."
"He turned around and found a large open pagoda filled with the sight of flesh ramming against flesh. Orcs, humans, even the odd goblin, were all naked and engaging in a great orgy. There were large orc cocks slammed into every orifice they could get their hands on." 
"Rowan had to step carefully around to avoid getting spunk on his boots."

show ulcro neutral at center with dissolve

"When he reached the center of the camp, he discovered that a poorly built dais had been raised, where Ulcro sat on his throne surveying it all. His chieftains, shamans, and loyalists sat on a lowered segment, where naked human slave girls came to serve them with wine and their bodies."
"Lesser loyalists sat in a great circle on the ground, feasting and making toasts. Rowan almost joined them before a commander on the dais gestured for Rowan to take a seat above."
"Ulcro’s raised platform was weighed down partially by the sheer amount of stuff on it. Swords, gems, and luxuries of all sorts." 
"Some of it was surely from the war chest, but many sub-chieftains and prominent orcs were coming up to offer their leader personal spoils from recent raids. At first, it seemed odd. That was until Rowan noticed that it was mostly Batri’s sub-commanders who were paying homage."
"After all, a rapier taken from a slain knight was better to lose then your head."
"One by one they presented their tokens of submission. He acknowledged each by slamming the butt of his axe against his chair. In a strange way, it reminded Rowan of the ceremonies where kings were crowned."
"Ulcro seemed to notice Rowan’s arrival and gave him a nod. Rowan lowered his head respectfully. What he was really wondering was where Eleanor was. It seemed strange that she wasn’t up there with him." 
"Rowan surveyed the crowd. He didn’t find Delane, but he did see someone with red skin on the far edge of the circle giving an orc female a rough tumble. It seemed Andras had come to enjoy the festivities too." 
"Then Rowan’s attention was drawn by a figure hidden by a number of cloths moving into the center of the circle. Ulcro raised a single hand. The boisterous crowd, seeing the gesture, went silent." 
"Then the clothes swirled open. They were being held by scantily clad young orc women, who retreated into the crowd...leaving Lady Eleanor standing naked alone in the center of the circle."

show eleanor naked aroused at edgeright with dissolve
show rowan necklace shock at edgeleft with dissolve

"Ulcro’s breath grew heavier. In the firelight, Lady Eleanor was radiant. Until now, he’d rarely seen her outside of her cage. Here she walked and moved with a practiced grace. Her body had been painted in subtle ways with orc tribal markings whose purpose Rowan could only guess at."
"She stepped, back erect, up to the dais. A grumbling whisper went through the crowd. Any open questioning of Ulcro was silenced by what he’d done to the last tribesman to question his choices. A human at Ulcro’s ear was more tolerable than his axe in your forehead."
"The orcs at the front of the dais moved aside. Lady Delane ascended the stairs, eyes fixed firmly on her new lover. She didn’t even acknowledge Rowan’s presence. The air tensed with anticipation..."

ele "My love. Once more you are unstoppable. Once more no one can challenge your will."

"She stepped on the upper most platform, stopping right in front of him. Then she gracefully sunk down to one knee, lowering her head submissively. All of this was a choreographed performance."
"It was almost a parody of the staged victory celebrations he’d been forced to attend after the war back in Rastedel."

menu:
    "Watch the scene unfold.":
        $ released_fix_rollback()
        pass
        
    "Turn away.":
        $ released_fix_rollback()
        jump ulcroSexSkip


#cg1 
scene black with fade
show eleanor naked aroused behind black
show ulcro neutral behind black

"It was in the same scripted manner that Ulcro reached down and scooped the naked woman from the ground, and settled her on his lap. The entire circle, thousands of orcs, had easy line of sight to her unblemished naked body. Her cheeks flushed."

ulc "No."

"The old orc growled loudly."

ulc "We iz unstoppable."

#cg1 variant
scene black with fade
show eleanor naked aroused behind black
show ulcro neutral behind black

"He wrenched her legs open with one hand. The strength of the motion made her gasp out loud. Her legs were spread wide enough to put her exposed pussy on display. Even Rowan could see the tell tale signs of arousal." 
"The idea of being fucked in front of the entire tribe must have been...exciting her. Rowan raised an eyebrow."

ulc "Dis tribe iz mine."

"His free hand pawed at her exposed breast. Her neck rolled back so she could let out a long guttural groan. Her hair draped over his scarred chest."

ulc "An' yous iz my woman. What’s mine iz yours."

"Eleanor was squirming eagerly in her lap, but even still she proved capable of reacting to his words. Pre-planned or not, a glimmer went into her eyes and she rolled her head to the side until she was looking him in the eyes. The watching orcs exchanged glances."

ele "Together."

#cg2 
scene black with fade
show eleanor naked aroused behind black

"In a sudden jerk, she turned around on his lap, so as to face her lover as opposed to the crowd. A hand lowered between the orc’s leg and worked his cock out of his loincloth. It was hard, thick, and veiny. It almost looked like it would impale her."

ele "Connected."

"She raised her hips and then slammed them downward, penetrating herself on Ulcro’s shaft. The moment it filled her, she let loose a powerful moan. All the inhibitions that she’d been storing up for so long were being opened up right there in public."

ele "Take me, my champion. Show them all who your woman is."

"Rowan watched on at the edge of his seat."

if avatar.corruption > 39:
    "The beginnings of a smile formed on his face. There was the slightest hint of pleasure for him in the idea that he’d unleashed this. Behind all of her good girl noble facades, Lady Eleanor was hiding this slut in her all along. But, the emergence was his work."
    
else:
    "When he decided to help Ulcro get lady Eleanor to agree to be his, he’d expected to convince her pragmatically. Perhaps even show her that being with an orc was not such a bad fate. But, he never could have expected to see her engage in such a wanton act with his own eyes."
    
"Ulcro was having no trouble accepting this turn of events. He let out a fearsome roar when his woman impaled herself on him and gripped her tight as he broke into a series of powerful upward thrusts. Despite being ostensibly on the bottom, he was the source of all the movement."

ele "Yes! Heavens yes!"

"The sound of their bodies in motion made a slamming noise. It was loud enough that it surely must have rung out at least to the back of the circle if not further. The pounding of flesh on flesh overpowered the scattered low whispers of the watching orcs."
"Lady Eleanor, meanwhile, had entirely lost all reason and sanity. She shook and pumped her body up and down in wild abandon. Her long hair flew in every direction. There was no rhyme or reason to it. Not even the careful pageantry of before. She was being fucked and she loved it."

ele "More. More. More. Yes. More. More."

"The same might that had once made Ulcro chief went into his movements. The muscles of years of warfare and fucking went into his thrusting. Certainly, it was clear he was into it, his normally stern expression had also taken on a look of shocked rapture."
"The crowd had at first been confused. Surely the way he treated Lady Eleanor as nearly an equal could not fit with their worldview. But, this they got. A few cheers broke out amidst the crowd, that soon spread. They raised their goblets and toasted to Ulcro and his human slut."
"Her vocalizations had lost all coherence. She rocked and shivered, shook and bounced, all while blubbering in incoherent bliss. It almost looked to Rowan like her eyes had rolled upwards. The pleasure consumed her."
"This really was no act. When the act was done, Lady Eleanor was really just a slut for orc cock."
"Ulcro’s body stiffened. He let out a loud groan and started to spasm. Lady Eleanor’s orgasm hit only a moment later. Bubbly white cum dripped out of her pussy down the exposed length of his cock. The watching orcs roared in approval."
"By the time it was done, she was clearly exhausted. She swayed back and forth, still groaning out half formed syllables. Ulcro picked her up, off his cock, and placed her on the arm of his throne. More cum leaked out."

scene bg26 with fade
show rowan necklace neutral at edgeleft with dissolve
show ulcro neutral at center with dissolve
show eleanor naked aroused at edgeright with dissolve

"He returned his focus to the tribe, who watched their leader with reference. When he spoke, his voice was a bellow."

label ulcroSexSkip:

ulc "Now yous sorry lot know who master iz again."

"He took one fist and slammed it against his chest."

ulc "I 'ave been yous chief for many years, and I will be yous chief for many years more. Let any other fool who wishes to join Batri come an' challenge me!"

"There would be no second challenge. Ulcro’s domination over the tribe was once more secure. They gazed up at him, nodding their heads in agreement. After a beat of silence, a roar of approval rang out to solidify it."
"Exhausted though she was, Lady Delane drifted an arm over to clutch Ulcro close to her. Rowan took a sip from his goblet. They would have their alliance. Ulcro would fight for them."

if avatar.corruption < 39:
    "...A thought that left a pit in his stomach. What had he just done?"
    $ change_base_stat('g', 2)
    
else:
    pass
    
return



label orciadAftermathBatri:

scene bg26 with fade

if delane_status != "batri":

    "After a few moments, Batri saw Rowan at the front of the crowd, and threw the head on the ground before approaching him, with an angry look on his face."
    show rowan necklace neutral at midleft with dissolve
    show batri neutral at cliohnaright with dissolve
    bat "What da fuck are yous doing 'ere humi?"
    "Rowan really didn’t know how to respond to the aggression, so he decided the best tactic would be to attempt some form of flattery."
    ro "Watching your magnificent victory. I see you defeated Ulcro."
    "Batri spat on the floor, clearly not fooled."
    bat "Yeh, without your ‘elp, and da humi slut iz gone."
    bat "Only thin’ Batri not sure of iz if yous a spy, or just fuckin’ useless."
    "This caused a loud laugh to rise from the crowd of orcs who were watching the scene unfold. Rowan began to worry that it might escalate."
    bat "Don’t worry, Batri not gonna kill yous. Not unless yous return to camp dat iz."
    bat "Yous slink outta here with tail between legs, an’ tell dem masters of yours dey won’t be getting any ‘elp from Batri or his boys."
    "More laughter. Rowan burned with anger, but there was nothing he could do, he couldn’t kill an entire orc tribe by himself, even if he wanted to. All he could do is accept he had lost this one, and hope saving lady Delane had been worth it."
    "He left to the sound of more whooping and laughing, before the orcs finally stopped watching him to celebrate Batri’s victory instead. And if that wasn’t already bad enough, now he had to worry how the twins would react to his failure."
    $ orciad_ally = "none"
    $ orciad_ban = True
    return

else:
    pass

"After a few moments, Batri saw Rowan at the front of the crowd, and threw the head on the ground before approaching him, with a grin on his face."

show rowan necklace neutral at midleft with dissolve
show batri neutral at cliohnaright with dissolve

bat "See, humi? Told yous dat old bastard would be no challenge for great warrior like Batri."

"He spat on the ground, to emphasize what he thought of his former chief."

bat "Now rest of tribe see what happen, dey fall in line, boys will help make sure of that."

ro "I’m sure they’ll be happy to have all of this put behind them, and get back to raiding."

bat "Dey will, dey will."
bat "An’ don’t yous worry humi, Batri ain’t forgotten about deal, he always keep word. Said he would kill Ulcro didn’t he, and now he iz dead."

"The orc laughed again, killing seemed to put him in a much better mood than when Rowan usually saw him."

bat "Batri need to take care of few things, whip rest of da orcs into shape, make sure dey know who boss now. Come back in few days, we ‘ave big feast."
bat "But Batri not forget what you do for ‘im, anythin’ tribe can do for yous and your masters, dey will, on this yous ‘as Batri’s word."

"The two continued to talk for a short while until Batri excused himself to go look for Delane, the reason for which Rowan had no trouble imagining. As the other orcs started to dissipate, Rowan made his way out of the camp to continue his duties."

$ orciad_ally = "batri"

#Batri's Feast

scene black with fade
"A few days later..."

scene bg26 with fade
show rowan necklace neutral at midleft with dissolve
show wild orc neutral behind bg26

"Rowan had been through the camp many times in recent weeks. In many ways, it has become almost cozy to him. Even the usual festivals and celebrations had become familiar. But, tonight was different."
"Even as he was approaching the camp, he could hear an uproar like he’d never heard before. Not even the fight earlier had this level of intense excitement. The orcs were celebrating, and they did not celebrate in a polite way." 
"Inside the limits of the camp, the first thing Rowan noticed was how bright it was. At night, there were generally only campfires and the odd torch for light. But, tonight there were so many torches that one could mistake it for day."
"The orcs partied like only they could. It was pure chaos. Dancing and laughing. Drinking and fucking. Fighting and arguing. As Rowan made his way through the camp he found the odd body lying on the ground."
"Rowan had to dodge out of the way of one orc who was staggering back and forth drunk. It would not be the last time tonight."

wo "Pah. Humi. I should kill yous where yous stand."

"He stopped to watch when one orc, a big grey fighter whose age and scars seemed to suggest that he’d been around for the last war, had his head chopped off in combat with a long haired brute. Almost a re-enactment of the previous fight."

show batri neutral at cliohnaright with dissolve
show eleanor naked aroused at edgeright with dissolve

"In the center were ten older looking orcs tied up and down on their knees. Rowan recognized their faces. They were Ulcro’s lieutenants and commanders. None of them moved or resisted. What was the point? They might as well already have been dead."
"Others came to Batri to kneel and offers tokens of submission. A few would grope the human slut at his feet. Batri seemed more amused than annoyed by it. He darkly smiled at lady Delane’s wanton moaning."
"Rowan kept by the edge of the circle. The fact that he had aided Batri only offered him so much protection. Orcs around the pit jeered at Ulcro’s tied up lieutenants. They wanted blood."
"In fact, he was so focused on the center of the pit, that he didn’t notice when someone more familiar snuck up on him."

show andras smirk at edgeleft with dissolve

an "Bah, I half expected not to see you here, Rowan."

"Rowan turned around to face his master."

ro "Andras?"

an "The one and only. This is my kind of party. Fucking and fighting, what more do you need?"

"Rowan looked around with apprehension."

ro "Do you know what’s going to happen to the prisoners? I’m surprised he hasn’t already killed them."

an "Oh he will. Probably later tonight as sport. This is just rubbing their noses in it first. You gotta really make them feel the sting of it, first."

ro "I see."

if avatar.corruption < 69:
    "Rowan felt a sting of guilt if only for a second. He had doomed these creatures. He had to remind himself that they were probably all the butchers of his countrymen themselves. Besides, this was just how Orc society was run. Still, his actions had put them in this place. They would not be the last."
    
else:
    "Rowan nodded softly. He felt nothing for the Orc Captains, in truth. They were not the first people he’d killed since he’d first shown up at Bloodmeen, nor would they be the last. If he’d seen his countrymen die and become numb to it, why care for these killers of men? They sealed their own fate by backing a weakling."

"Rowan grunted. Just then he noticed something interesting happening with Batri and lady Delane. He casually reached down and gripped his hand in her hair roughley. She groaned out, but was otherwise pliant and obedient. A perfect slut."
"It seemed he was about to use her for relief right here in the middle of camp. A degrading fall for the once proud noblewoman."

menu:
    "Watch the scene unfold.":
        $ released_fix_rollback()
        jump aftermathBatriSex
        
    "Turn away.":
        $ released_fix_rollback()
        "Rowan may have been responsible for making her this way, but he didn’t actually want to see it with his own eyes. He pulled his head in the other direction and refused to look back." 
        "Andras chuckled softly at this, but didn’t otherwise try to force Rowan to watch. Clearly he was enjoying the display though. He was treating the entire thing like nothing less then a show."
        an "They’re done. You can look again. Wimp."
        jump batriSexSkip

label aftermathBatriSex:

#cg 1
scene cg227 with fade
show batri neutral behind cg227
pause 3

"Batri wrenched her upwards towards his crotch, not showing an ounce of concern for her. Lady Delane’s cheeks were flushed red. All of the dark feelings that Rowan’s agents had drawn from her was to be displayed for the entire camp. Her chains rattled as she moved with the hand."
"For a moment, Rowan thought he saw glee."
"Batri pushed aside his loincloth, letting his cock out for the whole camp to see. It was nothing to be disappointed in. The orcs were endowed with massive cocks, the likes of which could leave a human woman limping."

#cg 1 - variant 1

"Lady Delane made a loud choking sound as he slammed it all the way down her throat."
"Her chains rattled and she shook slightly, but overall she tried to force the entire massive member into her small and inexperienced mouth."

bat "If yous stop, yous get da lash."

"Yet, despite the size of the thing and the threat of force, she didn’t give him the pathetic blowjob of a slave fearing the whip. Rowan saw her body start to wiggle, and her head bob as best as she could manage. Batri’s harsh words only made her more aroused."
"She even positioned her hips so that she was humping the bottom of the throne with her pussy even as she took his massive cock in her mouth. She was rubbing and grinding it for every ounce of stimulation that her eager pussy could want."
"Batri remained stoic. He surveyed the crowd, barely paying attention to the slobbering choking slut forcing herself down harder and harder on him. He barely seemed concerned."
"Her face went red, and at one point lady Delane pulled her mouth away so she could catch some air. Rowan almost shouted out to her to breathe with her nose. But, Batri ended this small break with a light glare."
"That was all it took. Her chains rattled softly as she got back to work panting and gasping each time her mouth was filled by his enormity."
"The bucking of her hips against his throne only got more frantic. Rowan was close enough that he could hear a wet squelching sound from her lewd masturbation. A little bit of her juices dripped down the length of the throne."
"Her head bobbed vigorously. Up and down, up and down. She looked so eager, so desperate. There was not a trace of lady Delane’s former grace and dignity. She looked as eager for his cum, if not as skilled at getting it, as the most broken of the camp free use pets."
"Suddenly, her entire body jerked and she pushed herself hard against the throne. The motion was unmistakable. She just came."
"Lady Eleanor fell to the ground gasping weakly. Her face was bright red and her thighs were soaked. But, before she had time to recover, Batri emotionlessly reached down and grasped her by the hair, dragging her back up."

bat "If yous too dumb to use your mouth, use ya hands."

"Lady Eleanor gave a weak nod and brought her hands up to his massive shaft. It was still lubricated by her spit."

#cg 2
scene black with fade
show batri neutral behind black
show eleanor naked aroused behind black

"Her hands got to work pumping his cock as best as the chains would allow. It was as inexperienced as her cock sucking, but the lady made up for it with enthusiasm. She panted loudly and threw both hands into the effort."
"Rowan forced his eyes away for just a moment to look at the crowd. Many of them weren’t even bothering to pay attention to this little scene. To Batri it was routine, and to them just as much. But, some actively cheered him on, throwing jeers and taunts at the human woman that their former chief had fancied."
"They called her a whore, a cunt, and a pig. All of it only made her stroke his cock harder."

bat "Yous gonna take all my cum, slut. Yous kno' where."

ele "Yes, Master! Anything, Master!"

#cg 2 - variant
scene black with fade

"He only lasted a second longer. In a fearsome tidal wave, his cum shot out, covering her face in a thick white layer. It dripped down her exposed breasts and covered her body." 
"That was when the most shameful moment of all came. She took one hand and brushed it over her face...only to slam it into her own pussy. She was filling herself with his cum."
"At once his prior declaration had started to make sense. He must have previously commanded her to not waste a drop. Yet, that realization didn’t make the sight any less shocking. She was shoveling as much of his cum as she could grasp into her pussy."
"Rowan stifled a gasp. The meaning of such an act was not hard to ascertain. Looking at the new chieftain of the orcs, along with his slave, he knew that within year’s end her belly would be swelling with child."

label batriSexSkip:

scene black with fade
scene bg26 with fade

"Rowan sat with Andras for the next hour or so. Andras was full of weird little stories and facts about the orcs that he’d picked up from so much time fighting and fucking them. Rowan nodded and followed as best as he could, but even after all this time at camp he was still a novice to the subject."
"By this point, it was so late into the night that even the orcs were starting to get tired. Many were wandering off to their tents to rest. Then the moment it seemed Andras was waiting for. The spent and cum covered Lady Delane was handed over to a subordinate and Batri wandered off towards Ulcro’s former tent."
"Andras rose to follow him."


show rowan necklace neutral at midleft with dissolve
show andras smirk at midright with dissolve

an "I’m going to go sit with the new chief. The alliance is set in stone. But, he’d take it as a slight if I didn’t meet him myself. You’re welcome to come along."
an "We could use the entertainment."

menu:
    'Join him as their "entertainment".':
        $ released_fix_rollback()
        $ rowanGaySex += 1
        jump batriGayScene
        
    "Call it a Night.":
        show rowan necklace happy at midleft with dissolve
        "Rowan gave Andras a polite smile. He had a sneaking suspicion what Andras had meant when he called him entertainment."
        ro "No, I think I’ve had enough orc diplomacy these past few weeks to last me a lifetime. Just tell me if anything important happens, please, so I can adjust the war plans accordingly."
        "Andras slapped his back and laughed."
        an "Your loss."
        "Rowan watched him leave. In the corner of his eye, he saw the bound prisoners being led away. No doubt so that Batri might have some entertainment for after his meeting with Andras. A new day was dawning for this camp. For better or for worse, its fates were tied to Rowan's."
        "Rowan took another swig of mead."
        return

label batriGayScene:

scene bg30 with fade
show batri neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve
show andras smirk at edgeleft with dissolve

"When they entered the tent, Andras wasted no time. Placing both hands on the human’s shoulders, he forced him down so that he was kneeling before him."

bat "What yous doin’ demon? Thought we wuz gonna talk about alliance."

an "We will, after we’ve had a little fun."

"The orc chuckled, realizing what the demon meant by that."

bat "Guess dis humi yous bitch in more ways than one."

"Rowan burned with shame at the insult. Even if he wanted to, he couldn’t have stopped Andras from forcing him down, his master was much stronger than him, physically. But more vitally, deep down he didn’t want to, part of him wanted this, to serve the demon with his body."
"The demon smirked as he freed his huge semi-erect cock from under his clothing, and saw the former hero staring at it."

an "You know what to do, slave."

#CG -1 BJ Andras with HJ Batri
scene cg287 with fade
show andras smirk behind cg287
pause 3

"Rowan then began to suck on the head, taking it inside his mouth. Andras wasn’t about to take it easy on his slave though, and grabbed him roughly by the back of the head, forcing his cock down the man’s throat."
"Rowan let out of gag of surprise, but did his best to take it deeper. The demon began to move his hips, fucking his face to a symphony of glug-glug-glugs." 

an "That’s it slut. Take it all."

"He half turned with his upper torso, so he was facing the orc at the other side of the tent."

an "Well, are you just going to stand there?"

"The orc let out of grunt of affirmation, and walked over to the pair, freeing his own thick cock, that had already grown had from the show Andras had been putting on. Knowing what was expected of him, Rowan reached out to grab it, and began to stroke it without instruction."
"The demon smirked, as an idea formed in his head. He leaned over to whisper something to the orc beside him."

an "Open wide, bitch."

#CG2 - Double BJ
scene black with fade
show andras smirk behind black
show batri neutral behind black

"Without warning, Batri moved forward to try and shove his cock inside Rowan’s mouth, alongside Andras’. All the human could do in his startled state was exactly what the demon had told him to."
"With a bit of jostling, and a little more force, the pair managed to fit both of their large dicks inside his very full mouth, as he sucked and tongued them as best he could. Andras laughed, and clapped the orc on the shoulder."

an "Told you they would both fit."

bat "Yous did. Ha, dis slut is even betta’ than well used camp whore."

"Rowan wanted to object, but his mouth was too full. Besides, as much as he hated it, being dominated so roughly by the pair was causing his cock to throb uncontrollably. He might not like it, but when it came to being the demon’s plaything, his body betrayed him."

an "That’s enough foreplay, I think."

#CG3  - Spitroast
scene cg228 with fade
show andras smirk behind cg228
show batri neutral behind cg228
pause 3

"With little effort, and zero resistance, Andras repositioned Rowan so he was on his hands and knees before him, with the orc in front of the former hero." 
"He spat on his hand, and then slid a finger inside the human’s asshole to make sure it was properly lubricated. Rowan let out a little moan as the digit entered him, causing the demon to chuckle."

an "Ready for my cock, slut?"

"Rowan nodded meekly, and Andras laughed again as he slid his fat cock deep into his willing slave’s ass, who shuddered in pleasure, and let out an even louder moan."

an "I think you should do something to shut this cockhungry whore up."

"Batri, who had until now been stood watching, and idly stroking his cock, grabbed Rowan’s head by the hair, and forced his thick cock all the way down his throat."

bat "Like dis?"

an "Much better."

"Rowan could do nothing, caught between the two as he was. Andras moved his hip in long, hard strokes, pumping balls deep against his ass. The pleasure was overwhelming, but all the hero could do was let out a muffled cry, as the orc fucked his throat."
"Once again the sound of glug-glug-glug rang out in the tent, joined this time with the slapping of flesh on flesh every time Andras bottomed out." 

show cg228 with sshake
show cg228 with sshake
scene cg229 with flash
pause 3

"Rowan didn’t know how much he could take of this, but thankfully it wasn’t long before their dual movements brought them to climax. Andras grabbed him by the hips and buried his cock in his ass, releasing a hot load of cum deep inside."
"The sensation made Rowan cum, hard, shooting ropey lengths of jizz from his throbbing cock. "
 
show cg229 with sshake
show cg229 with sshake
scene cg230 with flash
pause 3 
 
"Batri wasn’t far behind, holding him in place as he forced the human to swallow his salty load. Rowan collapsed on the dirt, cum oozing from both holes."

scene black with fade
show andras smirk behind black

an "Let the slut rest. We have much to discuss, he’ll be ready for round two later."

"It was going to be a long night."

$ rowanAndrasSex =+ 1

return


label orciadAftermathTarish:

scene bg26 with fade
show rowan necklace neutral at midleft with dissolve

"Silence fell on the camp."
"Then, all hell broke loose. Cries of traitors and scum rose from the crowd of orcs, outraged by what had just occurred."
"With their leaders dead, both sides turned against one another in an instant. There was no love among them, but they were all ready to accept the outcome of the duel. Tradition demanded they do."
"But now both Batri and Ulcro were no more. One slain in fair combat, the other, treacherously poisoned. Without a victor, the camp had no leader. And this could mean only one thing."
"Open war, winner takes it all. At least what remains."

cro "Ya boss knew he couldn'ta win! Dat why he cheated!"
cro "Horseshit! He would neva!"
cro "Yea? Then what'z dat black blood?!"

"Accusations flew freely, and Rowan began to sweat. Tarish overplayed her hand. There was no chain of command among orcs, the leadership did not just default to her now that her rivals were dead. She was crafty, and he knew the value of that."
"But he feared the orcs would not view things the same way."

cro "Vengeance! Vengeance for Warchief Batri!"
cro "Traitorz! Shoulda never joined dat bastard!"

"Blades were drawn, shields were raised. All it would take was a single arrow shot or an axe thrown, and the whole camp would descend into violence."

ro "Tarish..."

"He cast the woman an uncertain look. Did she really know what she was doing?"

show tarish neutral at midright with dissolve

"She only grinned in return, and took a step forward."
"Everything was proceeding exactly as she expected."
"Horns thundered through the air, putting an end to the commotion, and causing both sides to turn against the third group, who until now remained by the side. Tarish crossed the field, approaching the now dead warchiefs, her two most impressive warriors trailing behind her."
"One of them carried a human-sized sack on his shoulder. Delane."
"Head high, Tarish reached Batri’s body. She threw it a disinterested look, one of pure disgust. She raised her spear, and unceremoniously stabbed the dead orc through the skull."
"Batri supporters howled in fury. One even threw himself forward, sword in hand."

snag "Wait."

"He was stopped by a lean orc in the front. Rowan squinted his eyes. His armor was of much higher quality than most of the stolen equipment the camp orcs utilized. He must've been one of Batri's officers."

snag "Tarish. Dis 'hole shitshow stinkz of yous tricks."

tar "Snag, 'ow about ya kneel before ya new warchief?"

$ snagName = "Snag"

snag "Don’t make me laugh, ya witch. I shoulda slaughter yous on da spot for what ya did!"
snag "Ya dishonor da tribe!"

tar "I dishonor da tribe?!"

"She stabbed Batri’s body again – invoking another roar of disapproval."

tar "Batri and Ulcro 'ad us sitting for months! Raiding some shitty villagez that might've been growin' dirt, for all I know!  When wus da last time we raided somethin' good, eh?! When wuz the last time we got ourselvz some real loot?!"

"Rowan recalled Batri had some success in that area, but it paled in comparison to what the entire tribe could accomplish, if united."

tar "Deez two idiots 'ad us fightin’ over some dumb humi slut, but I dishonor da tribe?!"

tar "I’ll bring honor back to da tribe!"

"Rowan glanced at the crowd. Not the first time he heard a speech like that. Probably not the first time they heard it either."
"It didn't look like they were buying it. "

tar "No mo' sitting around! No mo' small raids! No mo' stupid fights ova nothin'!"
tar "An' most importantly!"

"The orc beside her set the sack down, and tore the material off-"
"Revealing Delane. Naked, scared, with her hands tied behind her back."
"And with thighs wet from the constant stream of juices that leaked from her pussy. Jezera's concoction was working."

tar "No mo' slave hoardin'!"

"The mob murmured in confusion. Many heard of the fabled Eleanor Delane, Ulcro's praised/stolen pet."
"This finally evoked a shout of approval, even among some of the Ulcro’s boys. Nothing made a forget his old boss like the prospect of fucking his bride-to-be."
"Batri's men lowered their weapons, discussing the prospect against one another. Their new 'leader', the orc named Snag, approached Tarish carefully, though Rowan saw his eyes were focused on Delane the entire time."
"He and Tarish exchanged a few sentences between themselves, voices low. Negotiations, no doubt. At one point, Tarish pointed to Rowan, and the hero saw the other orc smiling."
"Finally, despite just having his boss sneakily murdered, Snag let out a boisterous laugh and turned to his people."

snag "Tarish be right! No mo' slave hoardin'! From now on, fair spoils for everyone! Everyone gets to ride Ulcro’s bitch!"

"Tarish shoved Delane forward, and the opposing mobs started to dissolve slowly, united by the prospect of the upcoming gangbang. Ulcro's men weren't as quick to follow Batri's suit. There was some commotion in the back between them..."
"But it must have been enough for Tarish, for Rowan saw her retreat from the field, a triumphant smile on her face. As she neared him, he cocked an eyebrow at her."

ro "Everything under control?"

tar "Yeh. Snag wanted Delane from moment he saw 'er during raid. Kept ravin' about how Ulcro stole 'er from “dem”. As if Batri would ever share her."
tar "He'll make hiz boy fall in line. As for Ulcro's..."
tar "I’m havin' my spies deal with da few who would oppose me. Once dey laying in the dirt, camp will be mine."

"An overstatement, if Rowan ever heard one. Tarish was building her empire on backstabbing and bribery. It would not last. Sooner or later some other orc of Ulcro's or Batri's caliber would raise up and overthrow her. She simply did not command the same authority as they did."
"… That’s why she needed the twins. She needed Rowan to have her back, she needed Andras to be the big bad boss who made sure they wouldn't be acting up."

if avatar.corruption > 50:
    "Rowan smiled to himself. Something to hang over her head, in the near future."

else:
    "Something he might be able to use against her if there was a need to."

ro "Clean up the camp. I expect it to be ready battle by next week."

"Tarish nodded, still smiling, and Rowan left the area. Other duties called."

$ orciad_ally = "tarish"

scene black with fade

"Do you wish to witness Delane's fate?"

menu:
    "Yes.":
        $ released_fix_rollback()
        jump delaneBadEnd

    "No.":
        $ released_fix_rollback()
        jump orciadTarishSex


label delaneBadEnd:

$ seen_delane_bad_end = True

"Sometime later..."

scene bg26 with fade
show eleanor naked aroused

ele "Ah!"

"Delane gasped as Tarish shoved her into the center of the impromptu arena. Tripping over her feet, she fell into the dirt."
"For the hundredth time this day, she cursed quietly. Cursed Rowan for his betrayal. Cursed the Goddess for her cruel indifference. Cursed the orcs for just existing. Pathetic plague of rats, unworthy of sharing Solanse with those infinitely their better."
"Cursed herself, for foolishly trusting the first human that stumbled into her tent."

"Cursed her body, for turning against her."
"She didn’t know what was in the concoction Tarish fed her. She expected some sort of… Numbing drought. Something that would make her pliable for her captor."
"Instead, the potion set her loins ablaze, and she wished for one of those herbal teas the priestess always gave her mother. Her every sense was heightened – her mouth felt dry and empty, her naked skin shivered from every gust of wind-"
"Her eyes found every orc cock peeking from beneath the loincloths of these savages, her nostrils widened as she inhaled the intoxicating, disgusting odor of these beasts, and her ears caught every insult they threw her way."

cro "Tits small."
cro "Ass too."
cro "Looks puny, will break."
cro "Yus think she has all her teeth? Dey say humi warleader use magiks to keep em."
cro "No fair. Me want all teeth too."

ele "(It’s called personal hygiene, you brutes!)"

"Despite her frustration, she bit her tongue and kept the remark to herself. She was naked, tied up, and humiliated beyond all imagination. But she would not lower herself to… Basic banter."
"She was Lady Eleanor Delane, of the noble Delane family! They might strip her of her clothes, but she refused to be stripped of her dignity."
"Knees shaking, she rose up, standing tall and proud among the orcs. She held her head high-"
" -as high as she could without making it obvious to the orcs she was doing her best to avoid staring at the behemoths between their legs."

cro "Bwahaha! Look 'ow wet she is! It’s like a river!"

"She didn't need it pointed out to her. For the last couple of hours, her nether regions burned with... Need. Unnatural need. To leave such a trail of... Bodily fluids, could not be normal."
"But she refused to acknowledge the insult, no matter how true it was."
"Endure. She just had to endure. The situation seemed hopeless now, but as long as she kept her wits, then maybe… Maybe an opportunity for escape would present itself."
"The odds were small. Nonexistent event. But she would not give in to despair, or this… Artificial lust."
"The orcs kept jeering, but neither stepped forward to touch her yet. Not that she wanted them too."
"They were waiting for… Something..."
"Or someone."

snag "Kraug!"

krau "Snag."

"A huge, stocky orc pushed his way through the wall of orcs. He carried a bloodied axe in his right hand, and his torso decorated a shallow wound. His chiseled… Muscular torso…"
"Delane turned her head away, preferring to focus on the orc that spoke up. This one was leaner, more humanlike. She saw him earlier – he was talking with the orc called 'Tarish' about… Something. Too focused on her own situation, she wasn’t really paying attention to their words."
"Great, now she could also curse her own lack of attentiveness."

krau "Stupid Vorg. Thought 'e’d take my band."

snag "Shoulda cut 'iz skull open long time ago."

krau "Wus gud warrior. Shame to kill 'im."

"Based on the subtle differences in their armour, they must have belonged to opposing camps. Ulcro’s and Batri’s, most likely. Were they high ranking officer, then?"
"From the way they carried themselves, she would say so. They certainly seemed to command respect. So… Powerful and… Domineering..."

krau "Dis Tarish gift?"

snag "Aye! Ya boss’s whore."

krau "Hrm."

"Their lustful eyes fell on her naked body, and she met them with a defiant glare. She would not shrink under their gaze. No, never. Instead, she held her head high, and as they approached her, opened her mouth to deliver a cutting remark. "

ele "Iiiiiiiiiiii???!!!"

#cg1 - fingering
scene black with fade
show eleanor naked aroused behind black

"Without a word of warning, the massive orc shoved his fingers right into her snatch."
"Violent pleasure erupted from somewhere deep within her body, making her almost faint on the spot. The orc cared little for her weak moans. He kept exploring her insides, at first pushing two, then three fingers into her, making her spasms in ecstasy."

ele "Aaa-aah? Aaaah!"

"She couldn’t wrap her head around it. How- How could it feel so good? How could anything feel this good?! When she was young, she used to pester her maids about the matters of sex - asking how it felt to have a man touch your skin, kiss your lips. She had a vague idea, but this…"
"This ecstasy was beyond her wildest imaginations. She covered her mouth, trying to stop herself from crying out again. The pathetic moan from before was humiliating enough, she would not let out another one."
"She wouldn’t give these brutes the satisfaction."

krau "Hrm. Loose an' wet."

snag "Nice."

krau "Hate loose. Dibz on ass."

"His fingers left abruptly. Delane hoped her body would finally stop its rebellion against her. This… heightened sensitivity from before she could handle. As long as they weren’t touching her…"
"As long as they weren’t touching her…"

ele "Nnn… Aah?"

"Despite her earlier conviction, she couldn’t help but moan mournfully. What was this… Feeling of emptiness inside of her? This profound feeling of loss? It was as if there was this… Void inside of her..."
"A void she was now certain always existed. She just wasn’t aware of it. Until now."
"She imagined this is how a man who never ate his entire life would feel, after being given his first meal. Hunger, once muted, now ravished her body. She had- She had to-"

ele "(No!)"

"She wouldn’t give in to it. No matter how much she wanted to. She was Eleanor Delane, of the noble Delane family, not some... Floozy with no self-control!"
"Gathering herself, she threw the stocky orc her most cutting look. Batri and Ulcro killed themselves over her. If she could just turn his officers against that other woman…"

ele "Your chieftain is dead. Doesn’t that-"

krau "Shut up, slut."

"But she didn’t have much time to work them over. She should’ve tried to sway Ulcro to her side when she still had the opportunity to do so."
"She will pay dearly for choosing pride over survival."
"She swallowed heavily, trying to keep her composure. “Kraug”, meanwhile, walked past her. He placed his large hand on her shoulder, forcing her to stand still."
"Her bindings came undone, cut by a dagger."
"She turned her head around and addressed the orc again, trying a different strategy this time."

ele "The Baron will payyiiiiiiiiiiiiiiiiii?!"

#cg2 - nipple play
scene black with fade
show eleanor naked aroused behind black

"She didn’t get halfway past her ransom idea, when the orc in front of her roughly grabbed her by the bosom and twisted her nipples. He tugged at them without mercy, forcing another high-pitched shriek out of her."

ele "Aaaaaiii!"

snag "Eh, too small."

ele "Aaaah!"

krau "Yer not gonna fuck 'em."

snag "Wanted to, later."

"They exchanged a few more remarks, but Delane started having trouble with keeping with the conversation. The lean orc released her nipples and dug his fingers into her breasts. His cruel manhandling should’ve been painful, but instead…"

ele "Aah?!"

"A lustful moan escaped her lips. She used to.. Touch them, when she was younger, as all young, curious ladies did. But this violent arousal was completely unlike what she felt back then."

"It was as if her chest was on fire. It made her feel dizzy, like all her attention drained away from her head, and traveled downwards, to her breast and nether region."
"She had to stop this somehow-"

ele "Aaa-aaah?!"

#cg2 variant - pussy massage
scene black with fade
show eleanor naked aroused behind black

"Part of her – a part that now felt so very, very small – was embarrassed, ashamed at her own behavior."
"And another part reveled in how delightfully improper her reactions were."
"To be able to finally drop the pretense she was forced to maintain her entire life, and just… Indulge herself."
"How could she resist the temptation?"

ele "Aaah!"

snag "Ha! She’s salivatin'!"

"Was she? She didn’t know. She couldn’t really focus on anything except the burning pleasure in her tits and pussy."
"She didn’t really want to focus on anything except the burning pleasure in her tits and pussy. Not anymore."

ele "Aaah, aaah!"

"Finally, Kraug stopped rubbing her lower lips – and again shoved his finger inside of her. But this time, into her other hole."

ele "Iii?!"

"It was wrong, so delightfully wrong. She heard some men preferred to use the other entrance. Back then, she found the idea revolting."
"Now she couldn’t wait to try it."

ele "Aaaah, aaaah, put- put it…"

snag "Shh, slut, let Kraug get yous ready- or do you want to have 'er rough?"

krau "Hrm…"

"His finger left her suddenly – and Kraug grabbed her by the sides. He lifted her up, while Snag spread her legs open."

ele "(Yes!)"

#cg3 - standing dp
scene cg225 with fade
show eleanor naked aroused behind cg225
pause 3

ele "AAAH!"

"Pain and pleasure overtook her. The cock in the front slipped into her overflowing pussy with ease – while the one in the back ripped her asshole open with no consideration whatsoever.  She should be writhing in agony – but instead, the pain simply applied the ecstasy."
"The orcs gave her no time to rest, or to accustom herself to their massive cocks. Like a sack of flesh, they started to bounce her body up and down on, forcing a quick tempo onto her."

snag "Shit, what’ya know – she was a virgin!"

krau "Hrm."

snag "Tarish did keep 'er word, after all... "

"Another time, she would despair over losing her maidenhood before marriage. But now…"

ele "Aaa-aaah-aaah!"

"Now all she could think about was how wonderful having a dick inside of her felt."

ele "Aaaah! AAAH! AAAH!"

"She couldn’t stop herself from moaning – no, screaming in joy. Such violent delight – she couldn’t keep her voice down. She didn’t want to."

ele "Aaa-Aah! H-harder!"

"The orcs obliged, gripping her tighter and forcing her down on their dicks."

ele "Aah! Yes, yes!"

cro "Haha, split 'er apart!"
cro "Noble slut!"
cro "Bwahaha, Look at dem titties bouncin'!"

"She barely registered the other orcs cheering her on. So good, so good-"
"To think she could’ve had it months ago. She could’ve been bouncing on Ulcro’s cock every night for the past, what, half a year? It was difficult to keep track of time in the camp."
"Not that it mattered anymore. Nothing mattered anymore."

ele "Harder, harder!"

krau "Shut up."

"The orcs kept punishing her holes, locked in a dominance contest she wasn’t even aware of. She didn’t care. As long as they kept fucking her, nothing else really mattered."

#cg3 variant - standing dp cum
show cg225 with sshake
show cg225 with sshake
scene cg226 with flash
show eleanor naked aroused behind cg226
pause 3

ele "Aaah, aaah!!"

"Finally, the orc in front of her came, filling her with warm seed. Delane giggled in delight. So that’s how it felt… What a perfect ending to all that rough fucking…"
"The other one soon followed, filling her ass as well. She couldn’t stop giggling. There was nothing, nothing more inside of her, except for that burning desire in her loins. And the orc cum. Guess she should also count the orc cum..."

ele "(Orc cum... Orc cum...)"

"Her mouth felt empty. She was thirsty. She wondered how it tasted. She should ask them to fuck her mouth as well. She had three holes, no? They should all be filled. She wanted all of them to be filled."
"She looked to the side, at the mob of orcs that surrounded them. Surely some of will want to stick their orc dick into her mouth, right?"

ele "(Ahh... Orc dick...)"

"Something wet traveled down her cheek. She paid no attention to it."
"The orc behind her grunted and dropped her into the mud without a warning. She yelped, and threw them both a hurt look. Her ass and pussy were empty... She missed their warmth already..."

ele "Gah!"

"Someone yanked her head up from behind. An unfamiliar orc stared right at her, baring his teeth."

wo "Ready for round two, slut?"

"What a stupid question."
"Delane smiled from ear to ear, and reached out to grab his cock."
"She had a lot of orcs to service..."

label orciadTarishSex:

scene bg30 with fade

show tarish neutral at midright with moveinleft
show rowan necklace neutral at midleft with moveinleft

"Rowan and the newly minted orc chief stepped into the tent of her predecessor."
"Much of Ulcro's possessions had been removed and replaced with Tarish's, though the old throne remained. No one else was around, no doubt off either participating in the ongoing orgy or currently raiding."

ro "I see you've redecorated, it certainly looks like your home now."

tar "Haha, time to make dis place smell like mine too. Get on da ground, demon pink."

ro "Oh really? I think it's time you gave me a bit of respect, considering I was the one who got you this leadership position."

tar "Yous a weak little pink, I dos what I wants wit ya. Dat how dis work, unless you think ya can wrestle me."

"She loomed over him, glaring down with white eyes attempting to cow Rowan. Well this was certainly orcish behavior, they did tend to think they can just fuck whoever they want if they can overpower them."
"However, now was a good a time as any to make sure she wasn't going to cause trouble for Rowan or the twins."

ro "You don't get it, do you?  I'm not some messenger boy or demon's pet. I'm Andras' right hand, I'm the one who figures out who is useful and who's not. The one who decides who serves and who dies. I wasn't ordered to give you your position, I chose to."

tar "Eh?"

"Tarish hesitated for a moment, then put a hand forcefully on Rowan's shoulder trying for force him down again."

ro "Andras likes his orcs strong, and you're not cutting it. And without his support, there's now way you're keeping the camp together. I'm literally the only one keeping you where you are, if I change my mind or something happens to me, you're out of here in an instant."

"For all his bluster, that grip on his shoulder was really strong. If Tarish didn't take the bait, Rowan would have a hell of a time getting away from this woman. She was almost as strong as the men."

tar "Ha, yous just tryin' to make me afraid. Don't like orcs being rough?"

"Thankfully she'd started tapping her tusk and Rowan felt a little of his tension go out, she was nervous."

ro "I'm making sure you know where we stand. Today, we're equals, servants of a powerful demon who'll take over the world with our help. It's best if we keep it that way, so no more ordering me around."

"Now that all the threats had been put down Rowan was pleased to feel Tarish lift her hand from his shoulder. There was no question that she was confused and unsure how to respond to this situation, wise enough to recognize the danger, but the orc had no idea how to deal with it."
"That would be enough.  If he wanted to, the man could keep pushing but he didn't want to break the woman. That would defeat the point of having put her in charge in the first place."

"Take advantage of the situation?"

menu:
    "Yes.":
        $ released_fix_rollback()
        $ tarishSex = True
        jump orciadTarishSex2

    "No.":
        $ released_fix_rollback()
        tar "Alright humi, Tarish just tryin' to have a bit of fun iz all."
        ro "As long as you know where we stand. When the times comes, you'll be expected to do what you promised."
        tar "Tarish will keep 'er word, don't yous worry about dat."
        ro "Very well. I have other matters to attend to, but you will be called upon when needed."
        hide rowan with moveoutright
        "Rowan left to return to the castle. The orc could be a handful, but he was reasonably confident she would be a useful ally for the twins, when the time was right."
        return


label orciadTarishSex2:

ro "I'm glad we understand one another. How about we move onto what we came here to do in the first place?"

"Rowan took a seat on the former chief's throne and undid his pants, letting his member slip free. With a smile and a tug to go from half mast to full he invited her to sit down."

ro "This is what you wanted, didn't you? How about you sit on my lap."

tar "Sure. Dis lot more fun than talking politic."

scene cg232 with fade
pause 3

"Now also smiling, she promptly flipped off her belt and dropped her nether garments revealing her glistening sex. Then turned around and sat on Rowan's lap, letting his cock slip up between her legs."
"While Tarish busied herself with guiding peg into hole, Rowan was occupied with exploring her upper body, rubbing his hands over her well defined musculature and slipping his hands under her rags to grip and pinch at her nipples."
"Once she had him inside however, she abruptly started pounding her hips up and down on his lap, hard. It was to be expected, Tarish is an orc after all."

if avatar.corruption > 50:
    "Rowan still wanted a little playing around and romantic love, at least as much as one could while frantically fucking like this. So he kept up his explorations and tried to use his legs to slow the woman down at least a little bit. Sex was something to savour after all, right?"

else:
    "If she wasn't bothering with foreplay, Rowan wouldn't either. Instead of touching and exploring her, his hands went straight for the hips to help her impale herself as hard and fast as possible. Animalistic sounds of bodies slapping, pounding, and grunting followed."

"However Rowan's efforts were not yielding any fruit. The orc woman had more or less taken complete control of the situation anyway and he wasn't getting it back while planted on his ass with a ton of orc flesh jackhammering herself on him."
"As he could feel himself nearing his limit, Rowan decided that was enough sitting around. It was time to take a little more charge of the situation, so the man heaved his partner off of him. Briefly a frown formed on the woman's face."

#cg2 - throne standing
scene black with fade

"It didn't last long, a moment later Rowan was on his feet on the throne and lifting up Tarish's leg to penetrate her while she was standing. The awkwardness of the pose made it much easier for Rowan to control the pace of the sex."
"For all her bluster about men thinking with dicks, Tarish wasn't willing to let that dick out to regain some of her previous dominance. Fucking was just more important while she was being filled."


if avatar.corruption > 50:
    "Finally Rowan had a chance to slow things down and get the sex to a rate that was a little more familiar. Frantic fucking was enjoyable, sure, but it was nothing quite like taking your time and making love instead."

else:
    "Luckily for her, Rowan had every intention of giving her exactly what she wanted at the same pace as before. That meant that things would be ending pretty quickly, but that's just how sex was with an orc."

#cg2 variant - throne standing cumshot
scene black with fade
show rowan necklace happy behind black
show tarish neutral behind black

"As sex so always does, things now came to an end.  An explosion of fluids sprayed out of Tarish's cunt as Rowan felt his own orgasm build. The torrent was soon followed by quivering walls and a hard clamp down, which triggered Rowan's own climax to paint her insides white."
"They seperated, collapsed, and remained there for a couple minutes catching their breath. Tarish was the first to break the silence."

tar "Again?"

ro "Hah, you are insatiable."

scene black with fade
"..."

return


label delaneBadEnd2:

scene bg26 with fade

"With the leadership for struggle resolved, the orc camp was united once more. Tarish was the new warchief, having secured her position through bribery and trickery."
"A position she would not keep, if not the twin’s looming authority. Something he had reminded her of."
"As he walked through the camp, heading to Tarish's new tent, Rowan found himself passing next to the impromptu arena that served a battleground to Batri’s and Ulcro’s duel."
"Last time he was there, Tarish threw Delane into the crowd of orcs, to secure their backing."
"The noblewoman couldn't still be there..."
"Could she?"

menu:
    "Check the arena.":
        $ released_fix_rollback()
        if avatar.corruption > 50:
            "Curious on how the whole affair ended, he turned his steps to the arena. He had a pretty good idea…"
        else:
            "Heart heavy, he turned his steps to the arena, unable to ignore the gnawing suspicion he already knew what he would find there."
        $ seen_delane_bad_end = False
        jump delaneArena

    "Continue on":
        $ released_fix_rollback()
        if avatar.corruption > 50:
            "His business with Delane was over. There no longer was any point concerning himself with her."
        else:
            "Whatever became of Delane… He did not want to see."
            "It was easier this way."
            $ seen_delane_bad_end = False
        jump campMenu



label delaneArena:

"What once was an impenetrable circle of orc flesh, was now a group of four orcs, casually hanging around. Three of them talked about something, Rowan wasn’t certain what about."
"The fourth one was busy fucking Delane."

#cg1
scene cg253 with fade
show rowan necklace neutral behind cg253
pause 3

"Covered in filth and dry cum, the broken noblewoman laid on the ground, ass sticking up to give the orc good access to her pussy. She moaned softly, as he kept ramming his dick inside of her, without any consideration."
"A dazed, happy smile graced her lips, but her eyes were empty. Even when Rowan stood right in front of her, she did not register his presence, lost in her own little world - one that started and ended on the cock in her pussy."
"Perhaps Jezera’s concoction was a little bit too effective. "

ro "…"

if (avatar.corruption > 50) and (serveChoice == 4):
    "Rowan looked down on the broken noblewoman. Had he done nothing, another would take her place – some peasant girl, who knew nothing but hard work and poverty her entire life."
    "To see stuck up bitch like Delane reduced to such a state…"
    "Rowan smiled and knelt beside her. She still stared into nothingness, tongue hanging out as she moaned."
    "He patted her gently on the cheek. Lovingly, almost."
    ro "Welcome to the new world, Lady Delane."
    "She moaned pathetically in response. How adorable!"
    "His spirits lifted, he headed out."
    $ change_base_stat('g', -2)
    jump campMenu

elif (avatar.corruption < 50) and (serveChoice == 4):
    "Rowan looked down on the broken noblewoman. Had he done nothing, another would take her place – some peasant girl, who knew nothing but hard work and poverty her entire life."
    "Instead, the role of an Orc plaything fell to Delane."
    "Was this not justice?"
    "Without a word of commentary, he turned around and left the arena. There was much to be done."
    jump campMenu

elif serveChoice == 2:
    "Rowan looked down on the broken noblewoman."
    "Had he refused Jezera, his own fate might have been similar."
    if avatar.corruption > 50:
        "It was unfortunate that he had to sacrifice Delane to ensure his continued survival, but what other choice did he have?"
        $ change_base_stat('g', -2)
    else:
        "How many more would he have to sacrifice to save himself?"
        $ change_base_stat('g', 2)
    "No matter - there was no point sticking around. Rowan turned around, and headed out."
    jump campMenu

elif serveChoice == 1:
    "Rowan looked down on the broken noblewoman, swallowing heavily."
    "“I have to bide my time”. “Now is not the time to strike”. “The twins are too strong to resist now”."
    "How often did he tell himself these excuses…He knew he would have to agree to some sacrifices when he embarked on this path, but this…"
    "Wasn’t this a little bit too much?"
    "… No matter. Self-loathing won’t undo the damage now. He should go, there were things that needed doing."
    $ change_base_stat('g', 5)
    jump campMenu
    
else:
    "Rowan looked down on the broken noblewoman. Had he done nothing…"
    "Had he done nothing, this could’ve been Alexia. Not here, no. But back in Castle Bloodmeen. Perhaps it wouldn't be orcs, but some other creatures. Driders maybe. Or some bizarre beast summoned by Jezera." 
    "But none of it mattered, because Alexia was safe now."
    "But only as long as he kept being useful to the twins."
    if avatar.corruption > 50:
        "And as long as she was safe, no price was too high to pay."
        $ change_base_stat('g', -10)
    else:
        "Was it really right of him, sacrificing others just so his own wife could be safe? Perhaps not."
        "He didn’t want to think about it."
    "There was no point in sticking around. Rowan turned around, and headed out – he had things that he needed to do."
    jump campMenu
