init python:

    #Talking to the assistants
    event('talking_to_the_assistants', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    #Getting caught up in a good book
    event('getting_caught_up_in_a_good_book', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    #Different alphabet orders
    event('different_alphabet_orders', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', run_count=1, priority=pr_npc)
    #Generic library event 1
    #no requirements - repeatable
    event('generic_library_event_1', triggers="npc_events", conditions=("get_actor_job('alexia')=='research_assistant'",), group='alexia_library', priority=pr_npc)


label talking_to_the_assistants:
#Talking to the assistants
#No requirements

scene alexia_library_1 with fade

"During the week, Alexia found herself without much to do in the library. She'd finished the work she'd been assigned and Cliohna had been away for most of the day already."
"With no idea when the librarian would return, and nothing else to do, Alexia and the other research assistants got together for a chance to get to know one another better."

#If library has not been upgraded
if castle.buildings['library'].lvl > 1:
    "There were only a handful of them, but the sheer size of the library and tight ship that Cliohna ran meant that they didn't get much chance to interact with one another at all."
#If library has been upgraded
else:
    "There were more people working here now than when Alexia had first arrived in the castle, thanks to Rowan funding upgrades to the library. However, they hardly saw each other due to the sheer size of the library. Leaving little chance to interact with one another."

#rejoin
"Right away it was quite obvious that there was little unifying them when it came to race. There were humans, goblins, elves of both types, and a spattering of mixed races on the staff, hailing from all over the Six Realms."
"Cliohna was rather particular about qualifications for who she let on her staff, but didn't much care about other details. Most, but not all, had some background as academics or sorcerers. Others were just lovers of books or had met the librarian at some event or another."
"The subject matter that some of these people had mutual interest with Cliohna disturbed Alexia, so she tried turning the discussion away from that to other matters."
"She was curious how things had been under Cliohna since the castle had been founded. When exactly had that ancient sorceress taken over and where did she come from?"
"The answers proved to be, underwhelming.  There really hadn't been any real difference between how Cliohna worked with one staff member to another, not even when her team had grown. Nor did any of them know who they were working for was. The librarian just... was."
"The one other interesting thing that Alexia discovered was that Cliohna's team hadn't lost any members since they were recruited. As far as everyone knew, she'd never gotten rid of anyone, nor had anyone died while in her service."
"Naturally there was some trouble with the twins and the soldiers underground, but they collectively felt they were among the best staff in the castle. That was assuming you didn't mind the work, but Cliohna had a knack for finding the competent and motivated."

#Alexia loses a little stress.
$ do_job_research_assistant('alexia')
$ change_actor_stress('alexia', -3)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label getting_caught_up_in_a_good_book:
#Getting caught up in a good book
#No requirements.

scene alexia_library_1 with fade

"For all her disdain towards the uses that some put books towards, Cliohna would always make sure the castle library's collection was complete as possible. That included fantasy stories and fable collections."
"This section of the library had been a big favorite for Alexia. At the librarian's urging she'd also read some history books and treatises, but she had always come back to the works of fiction to read another fanciful tale during the long months she'd been imprisoned."
"After making a stop in that section to catalogue some new material, one of the books caught her attention and she couldn't help but crack it open to read a little inside. It was an epic fable about fairies and the people who they visited."
"Alexia was almost instantly enthralled and slipped off to find a comfortable place to read. It wasn't until she noticed how hungry and tired she was that she realized just how many hours she'd spent reading that book."
"The next day, she got back to work, but soon the siren's call of that enthralling story of the fae of light and dark drew her in once more. She just couldn't help herself, it was such a good story."
"Over the course of the week, she devoured the massive volume. Cliohna realized what was happening after the second day, but wasn't terribly bothered. Instead, she had Alexia tell her a summary of the story and make a few notes while she read it."
"After all, it was the woman's love of books that had distracted her, and Cliohna seemed to like this spark that had taken her staff. So this time, she turned a blind eye."
"Of course, a summary of the story did little to help the librarian's work this week."

#Alexia performs at 1/4 effectiveness, but loses a lot of stress.
$ do_job_research_assistant('alexia', 0.25)
$ change_actor_stress('alexia', -5)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label different_alphabet_orders:
#Different alphabet orders
#No requirements

scene alexia_library_1 with fade

"This week, most of Alexia's time in the library was spent dealing with a minor organization crises. It started with a book that she couldn't find because it didn't seem to be in the right place."
"At first, Cliohna had assumed that someone had stolen the book, only to discover later that it was actually shelved in the wrong place. An investigation soon found that many other books had been improperly shelved."
"Eventually it turned out that the cause of the problem was the difference between the human and elvish alphabets.  Most of the characters were either the same or very similar, after all, humans had learned writing from copying elves in the first place."
"However, a critical difference was that the order of the traditional alphabet was different. Up until now, the elves had been organizing books according to the elvish alphabet, while the rest of the staff had been using the human ordering."
"Cliohna immediately decided to have everything reorganized according to the human standard and made certain that the elves understood what that was. The rest of the week was mostly taken up by doing just that."
"It was an incredibly tedious process, largely killing most of the enjoyment that Alexia usually found while she worked in the library. While she helped a great deal by working on this project, she just hated doing it."

#Alexia gains some stress.
$ do_job_research_assistant('alexia')
$ change_actor_stress('alexia', 7)
return

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


label generic_library_event_1:
#Generic library event 1
#no requirements - repeatable

scene alexia_library_1 with fade

"Alexia spent the week working for Cliohna as an assistant librarian. She fetched books when they were needed and returned them when they were not. When Cliohna didn't need her, she would catalogue the massive library shelf by shelf, book by book."
"This project had been something that Cliohna had been working on herself, and she'd memorized a large part of the library's organization. However, that took time away from research and it didn't cover the finer details of exactly what was stored here."
"There were also the new books that periodically arrived at the castle that needed to be stored in their proper place as well, which fell to Alexia."

$ do_job_research_assistant('alexia')
return
