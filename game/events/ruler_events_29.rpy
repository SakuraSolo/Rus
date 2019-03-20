init python:

    event('nasim_intro', triggers='week_end', conditions=('week==14',), run_count=1, priority=pr_story)


label nasim_intro:
    
scene bg14 with fade
show rowan necklace neutral at midleft with dissolve
show skordred neutral at midright with dissolve

ro "You wanted to see me? Is there an issue with the renovations?"

sk "Na exactly. There is a problem, but na with the castle itself."
sk "A very naggin’ problem."


show nasim neutral at edgeright with moveinright

nas "Do not speak of me this way, dwarf."
nas "The name is Nasim, and you will address me as “Researcher Nasim.”"

sk "A high name for Cliohna’s pantler."

nas "And a low insult from a member of a lowly race."

show skordred neutral at skorright with moveoutright 
show nasim happy at center with moveinright

nas "But where are my manners. You must be Master Blackwell! An honour to meet you."
nas "Researcher Nasim. I am one of the wizards who work with Cliohna on making sense of the Castle’s extensive - and poorly maintained - archives."

ro "An apprentice of hers, then?"

show nasim neutral at center with dissolve

nas "… Master Blackwell, please."
nas "My area of expertise includes, though is not limited to: Earth Elemental Magic, Energy Field Manipulation, Hexes, Rune Analysis, Rune Crafting, Mental Barriers, Charm Countermeasures-"
nas "- Divination and Antidivination Protections, elf Stasis Magic, goblin Shaman Rituals, restorative alchemy with focus on anti-toxins, Abjurations,  and recently-"

show nasim happy at center with dissolve

nas "Chaos Magic and Transformations!"

show nasim neutral at center with dissolve

nas "While it is true I work under Mistress Cliohna - and consider doing so quite the privilege - “apprentice” is hardly the proper term here."

"Rowan sneaked a quick look at Skordred. The head builder had a face of pure marble. "
"Having served who knows how many generations of Demon Lords, Nasim could hardly be the most stuck up person he ever got to work with."

ro "Quite the portfolio."

show nasim happy at center with dissolve

nas "Usually I wouldn’t boast, but-"

show nasim neutral at center with dissolve

ro "So mind telling me why exactly you two are wasting my time?"

nas "… I assure you Master Blackwell, I am no less agog as to why Skordred has ordered you here. All I ask of him is to make a small adjustment to his digging schedule, and he’s being obstinate!"

ro "What adjustment? And why?"

nas "I suppose some context is necessary."

nas "As I already mentioned, recently my primary subject of research has been the practical application of chaos magic in the form of transformations, both in inanimate objects and living human beings."
nas "And just yesterday, as I was cataloguing the castle’s old records with some of the other students, we stumbled upon a truly marvellous discovery! "

show nasim happy at center with dissolve

nas "A diary of one of the castle’s earlier librarians, and in it, schematics for a special chamber built deep beneath castle Bloodmeen, by the orders of the demon lord Talmath!"
nas "If the schematics are accurate, and I have every reason to believe them so, Talmath wanted to create special nexus for gathering chaos energies, one of the few present in Solanse! I believe the nexus was indeed finished, and later used to-"

show nasim neutral at center with dissolve

nas "Well, If the records are accurate I suppose it would be primarily used for the creation of somewhat grotesque female sex slaves, as Lord Talmath is well known to be quite fond of improbable proportions, especially around the chest and the backside-"

show nasim happy at center with dissolve

nas "But according to the schematics, that would be only a fraction of the chamber’s true power! If we were to find it and restore it to its former glory, we could progress our understanding of Alteration by millennia!"
nas "Magic almost exclusive to the Gods themselves might be within our grasp, Lord Blackwell! Permanent body modifications! Grafting functional limbs! Chimerism! Gender Reassignment! Therianthropy!"

show nasim neutral at center with dissolve

nas "… Which is why I politely asked for the dwarf to dig it out. And he’s being difficult about it!"

sk "And I keep telling ye, I’m not going to dig straight for yer fairytale chamber! It’s not practical!"

show rowan necklace shock at midleft with dissolve

ro "“Fairytale chamber”? Might it not exist?"

show rowan necklace neutral at midleft with dissolve

sk "Who knows? Wasn’t around when ah came here. The castle has been destroyed and rebuilt countless times, a large portion of it still remains in ruins."
sk "Which is why I have a precise plan on what is gettin’ restored first. If ye want us to dig straight to where the pantler boy is pointin’ at, I would have to pull people from other jobs, and that’s gonna to cost us."

nas "How does a dwarf fail at digging deep- You know what, never mind, just make it happen you vertically challenged simpleton! I can’t progress my research without it!"
nas "Master Blackwell, I assure you the chamber exists, and that the research boost from it will far outweigh adjusting the renovation schedule."

ro "I will be the one to judge that, Nasim." 

nas "… Of course."
nas "Then if you’ll excuse me, Master Blackwell, I’d like to return to my research now. You can find me in the library if you have further questions. I bid you a good day."

hide nasim with moveoutright

ro "Charming fellow."
ro "Has he been causing other trouble?"

sk "Eh, na that I know of. The Masters seem to like him for some reason? He mostly keeps to the library, I think."

ro "A small blessing then, I have enough on my plate as it is. Keep me informed, will you?"

sk "Aye. If it’s any consolation, ya can just ignore him. That chamber doesn’t seem to be that deep in… We’ll probably get to it in a year anyway."

ro "I am sure he won’t mind waiting."

if serveChoice != 4:
    hide skordred with moveoutright
    ro "(And I don’t plan to stick around for that long.)"

$ nasimAvailable = True

return
