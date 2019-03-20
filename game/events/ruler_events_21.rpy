init python:
    event('liurials_hard_work', triggers="week_end", conditions=('week >=25',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('foraging_request', triggers="week_end", conditions=('week >=10',), group='ruler_event', run_count=1, priority=pr_ruler)
    event('thoughts_on_governance', triggers="week_end", conditions=('week >=21',), depends=('foraging_request',), group='ruler_event', run_count=1, priority=pr_ruler)


label liurials_hard_work:
#Liurial's hard work

scene bg6 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan wiped the sleep from his eyes on the way towards his desk. The past week had left little time for him to tackle the mounting pile of paperwork that seemed to pile up around him. Reports on hauls from raids. Weekly supply consumptions. Complaints and scouting reports."
"It was enough to make him unsure if he should rush over to eek out a bit more time for himself, or slow down to savor that last little bit of freedom he’d have before he started."
"Which is just about when he arrived and saw the large stack of papers in the “reviewed” pile."

show liurial happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

liur "Good morning, Lord Rowan."

"Liurial gave a small curtsey. Rowan looked between the pile of completed work and his assistant."

ro "What...what happened to all the documents? I had them all in the “To Review” pile…"

liur "I wanted to get a bright start on the day. So I took the morning and reviewed most of the outstanding documentation. Anything that requires your signature has been placed in a special pile."
liur "There was a report of a skirmish on the outskirts of our active territory involving a group of orcs."
liur "I also noticed a slight irregularity in the shipments of new rags for orcs, and figured out which trader is trying to raise the prices on us. Details will be in my short report."
liur "I also took the liberty of cleaning up a bit…"
liur "...and making you some tea…"

"Rowan ran a hand through his hair. True to Liurial’s word, there was a cup of tea simmering next to the pile."

ro "You did all that? When did you sleep?"

"Liurial giggled softly."

liur "Elves don’t need to sleep. Well, not exactly. So long as I rest in the next few hours, I’ll be alright."
liur "Are you..pleased with me?"

show rowan necklace happy at midleft with dissolve

"Rowan nodded slowly, an encouraging smile coming to his face. He put a hand on the top of her head right above her strange elven cap, and gave it a little pat. Liurial glowed."

ro "I am. I am. This is wonderful. Good work, Liurial."

"Rowan went to his desk, and took a sip from his tea. It had a strange flavor to it. Something sour."

ro "What’s in the tea?"

liur "I put a hint of a fruit called lemon from traders out in the Dragon’s Tail."

"Rowan grunted softly. He liked the taste of it. This was going to be a good day."

$ change_treasury(25)
return


label foraging_request:

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

cl "Ah Rowan, excellent timing."

ro "Hello Cliohna, you wanted my help with something?"

cl "Yes, I was reading through your history and learned that you are an accomplished herbalist and forager?"

ro "Well, a little rusty since I haven't done much foraging since the war ended, but I was taught a thing or two by my parents. What did you need?"

cl "Identify these plants."

"She placed two sketches on the nearby table, then stepped back so Rowan could have a look."

ro "That's hemlock and that's cottongrass."

#cliohna happy

cl "Very good, I would like you to collect some of each for me."

ro "That's easy enough, you can find both in this area, but why do you need hemlock? It's very poisonous."

#cliohna neutral

cl "Exactly, the point of my upcoming experiment is to find an anti-poison. I need the poison in order to test it. Now will you collect those plants for me or not? There are precious few in the castle who could."

ro "Alright, I have a little free time. I should be back in a couple hours."

hide rowan with moveoutleft

scene black with fade
scene bg12 with fade
#cliohna happy
show cliohna neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with moveinleft

cl "Punctual, I like that. Let's have them then."

"Rowan placed two bags on the table containing several of the two plants Cliohna had requested."

ro "You're not planning on using that cottongrass to cure hemlock poisoning, are you?"

cl "Hmm? Why do you ask?"

ro "The only medical use I know of for cottongrass is to help with... err... bathroom problems."

cl "Really? I didn't know that... when did you learn of this use?"

ro "When we were marching on Bloodmeen, it was my business to learn every possible use we could find for what little we could find in the wastes and mountains around here. Both for food and other uses."

"The woman stepped over to a lectern and pulled an inkwell and quill from underneath."

cl "Tell me more."

scene black with fade
scene bg12 with fade
show cliohna neutral at cliohnaright with dissolve
show rowan necklace neutral at midleft with dissolve

ro "... and that's just all I can think of off the top of my head. There were probably a few others that I either forgot about or got mixed up."

"Closing her notebook with a definitive thunk, Cliohna stepped back from her writing. Rowan had only been speaking for about fifteen minutes, but she'd been furiously taking down what he said the whole time."

cl "My, what an unexpected fount of knowledge on this subject you've proven to be. Admittedly much of this will not be useful in my studies, but it is information I have not read anywhere else."
cl "To answer your earlier question, no the cottongrass is not for curing the hemlock. I wish to test it for use as a filter and its use with hemlock is incidental. Regardless, I am quite grateful for the help you've given to me today.  That will be all Rowan."

"She didn't even turn to look at him as she dismissed him, only immediately replacing her notebook with a nearby tome and setting to read it."

ro "(Well, it was a thank you at least.)"

#gain relationship points with cliohna
return


label thoughts_on_governance:

scene bg12 with fade
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with moveinright

cl "Hmm, it would seem like you are out of your element Rowan."

show rowan necklace shock at midleft with dissolve

ro "That obvious, huh?"

cl "Those who are literate but not experienced with books are certainly not unfamiliar to me. You are not unlike much of the nobility in this regard. Tell me, what exactly are you looking for? You've spent quite enough time fruitless browsing at random."

show rowan necklace neutral at midleft with dissolve

ro "I remembered about a philosopher that had come up with a detailed and well thought out government system. It didn't fit with Solansia's order, so nowhere practises it today, but I can remember some nobles talking about them at a party a few years back."
ro "Since I'm more or less running the castle, I figured I could maybe make use of the basics."

cl "Surely you are not speaking of Baleron Astare?"

ro "Yes, that sounds right."

show cliohna angry at cliohnaright with dissolve

cl "Oh that Baleron Astare was a buffoon! Always on about high ideals and miracle solutions, yet the man lived on charity! All theories, no practical tests, just feel good ideas about natural order and legal responsibilities."
cl "No wonder these fools are so backwards if they're using Astare thought to guide them! Whatever the hell happened to people knowing what they were doing being the ones who should make the decisions? Honestly, it's so damn obvious."

ro "If I'm not mistaken, I think that's sort of what we are doing in Bloodmeen?"

cl "Really? Seems quite ad-hock if you ask me. When was the last time you had a lawmen council examination? I bet you Andras would fail his."

show cliohna neutral at cliohnaright with dissolve

"The woman let out a long sigh and her mask of calm settled back into place after her momentary loss of composure."

cl " No, this isn't relevant. Nor would it be terribly effective when ruling over orcs. I'm sorry Rowan, but I fear that this exercise will be in vein. Studies on humans and our brethren of this world likely will not extend to those of chaos."
cl "The people that you lead and must govern over have not been subject to much philosophical thought with regards to how to rule them in the past eight hundred years. Much of it is simply the law of might makes right, after all."
cl "This may be different for the dark elves and lizardfolk, but I very much doubt you'll find much use for Astare's ideas to help in that regard. Best you focus on your own intuition for the time being, you do have a knack for it from what I've seen."

ro "Alright then, I'll take your advice on the matter. Thanks."

cl "You are quite welcome, and please, seek out this place again should you be in need of knowledge. There is much to be gained from these shelves."

#gain relationship points with cliohna
return
