
label nasim_dialogue:

scene bg12 with fade

if nasimFirstVisit == True:
    jump nasim_First
    
elif nasimCatSeen == False:
    $ res_roll = dice(7)
    if res_roll == 1:
        jump nasim_cat
    else:
        if nasimAttitude > 0:
            show nasim happy at midright with dissolve
            nas "Master Rowan. How can I help you today?"
            jump nasim_talk

        
        else:
            show nasim neutral at midright with dissolve
            nas "Master Blackwell. How can I be of assistance?"
            jump nasim_talk   
    
    
else:
    if nasimAttitude > 0:
        show nasim happy at midright with dissolve
        nas "Master Rowan. How can I help you today?"
        jump nasim_talk

        
    else:
        show nasim neutral at midright with dissolve
        nas "Master Blackwell. How can I be of assistance?"
        jump nasim_talk


label nasim_First:

$ nasimFirstVisit = False

"Nasim wasn’t hard to find. When asking about the man at the library, one of Cliohna’s apprentices made a face like he just stepped into something unpleasant, then pointed him to a small room near Cliohna’s own."

show rowan necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

ro "You make friends everywhere you go, don’t you Nasim?"

"Rowan took stock of his room. It was suspiciously impersonal. Books, potions, scrolls, simple furniture. For a man with such a high opinion of himself, Nasim either preferred to live humbly, or did not plan to stay in Castle Bloodmeen for long."

nas "If you’re referring to some of the library workers here, I’m afraid I don’t see why I should bother."

ro "Out of simple camaraderie, perhaps? Aren’t you all fellow wizards?"

nas "“Wizards”? Please. Most of them are at best “magically inclined menial help”, though calling them that might be considered an insult to actual, professional house staff."
nas "They all think themselves future dark lords, even though they have as much talent among them as a flock of seagulls."
nas "And I have seen seagulls capable of casting spells."

ro "Aren’t you full of creative insults."

nas "These are not insults, these are factual observations."
nas "… Though now that I am giving the matter due consideration, I suppose that my remarks might seem no different to indignant complains of a capricious child, unaccustomed to not getting his way."
nas "I assure you Master Blackwell, this is not me being difficult. This is me expecting some basic level of competency and cooperation from the people I work with. A level they continuously fail to raise up to."
nas "But I will concede I should’ve handled my temper better."

show nasim happy at midright with dissolve

nas "So I’d like to express my regret over my unpleasant tone during our first encounter, and from the bottom of my heart, to apologize. I hope this will not reflect poorly on our future relationship."

$ futRelChoice = True

label nasimFirstMenu:

menu:
    "All is forgiven.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "Apology accepted."
        nas "Thank you."
        $ nasimAttitude += 1
        show nasim neutral at midright with dissolve
        show rowan necklace neutral at midleft with dissolve
        
    "Reprimand him lightly.":
        $ released_fix_rollback()
        ro "I suppose I can see how Skordred's remark might make one lose their temper."
        ro "Just be more respectful from now on. I don’t tolerate such outbursts among subordinates."
        nas "Of course. I will keep this in mind."
        show nasim neutral at midright with dissolve
        
    "Reprimand him harshly.":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        show nasim neutral at midright with dissolve
        ro "If you want to unload on someone, I’d suggest visiting a whorehouse or using the “menial help”. I do not tolerate such blatant disrespect among subordinates."
        ro "Have I made myself clear?"
        nas "..."
        show rowan necklace happy at midleft with dissolve
        nas "Crystal clear, Master Blackwell."
        show rowan necklace neutral at midleft with dissolve
        
    "“Future Relationship”?" if futRelChoice == True:
        $ released_fix_rollback()
        ro "And by “future relationship” you mean…?"
        "The wizard coughed uncomfortably and offered Rowan an apologetic smile."
        nas "A strictly working relationship, I’m afraid."
        nas "So about our first meeting…"
        $ futRelChoice = False
        show nasim neutral at midright with dissolve
        jump nasimFirstMenu

nas "Now, how can I be of assistance?"

jump nasim_talk

#########################################################################################################################

label nasim_cat:

$ nasimCatSeen = True

show rowan necklace neutral at midleft with dissolve

ro "Nasim, I wanted to talk with you-"

show rowan necklace shock at midleft with dissolve

ro "Hm?"

show rowan necklace neutral at midleft with dissolve

"The arrogant wizard was nowhere to be found. He must have been out on some task from Cliohna, as Rowan couldn’t imagine him dropping his research for any other reason."
"What he found in his room instead, was a grey, spotted cat, laying on a small pillow next to his desk. It was unusual for the people in Castle Bloodmeen to keep pets, and Nasim especially didn’t strike him as someone who would enjoy the company of one."

#if wilderness Survival ranks 2+ (TODO
#"Though a pure breed like that certainly suited him. Where did the wizard get this one? Had to cost a fortune… And certainly wasn’t native to the area."
# $ nasimCat = 1

menu:
    "Pet the cat.":
        $ released_fix_rollback()
        show rowan necklace happy at midright with moveoutright
        ro "Aren’t you a little out of place?"
        cat "Meow."
        
    "Look around Nasim’s study.":
        $ released_fix_rollback()
        show rowan necklace neutral at midright with moveoutright
        "A rare opportunity to snoop around. He ignored the cat, and approached Nasim’s table."
        cat "Meow?"

show rowan necklace shock at center with moveinleft

ro "What the-?!"

show nasim happy at edgeright with dissolve

nas "Ah, Master Blackwell, I see you’ve had the pleasure of meeting my family cat. A charming fuzzy ball, isn’t he?"

show rowan necklace neutral at center with dissolve

ro "Nasim, why did your cat just say “meow” to me?"

nas "Master Blackwell, whatever do you mean? Don’t all cats meow?"

ro "Don’t play dumb with me, he didn’t meow, he literally said the word “meow”!"

cat "Meow?"

ro "See?"

show rowan necklace neutral at midleft with moveoutleft
show nasim happy at midright with moveinright

"The wizard chuckled to himself, finally dropping the pretense. He picked up his cat and showed it off to Rowan, like some prized possession."

nas "Fine, fine. Master Blackwell, please meet Percy. He is – was – my mother’s cat, and he’s one my of early works on transformation magic."

nas "Percy, say “Hello” to Master Blackwell."

$ cat_name = "Percy"

cat "Meow."

show nasim neutral at midright with dissolve

nas "… As you imagine, this wasn’t exactly what I was aiming for."

ro "I have a feeling I’ll regret saying this, but care to share the full story?"

nas "There isn’t much to it. Cats exhibit high animal cognition – a feral intelligence, to put in simpler terms. It was my theory that perhaps, if given human vocal cords, a cat might, over time, develop the capacity to speak human language."
nas "But I have overestimated the sophistication and precision of the transformation spells I had access to at the time. While I succeeded in transforming his vocal cords, the spell also affected his brain, without me ordering it to."
nas "It wired it to try and replicate the sounds the cat was already used to making."
nas "And so, I have wasted three weeks on creating what Solansia’s church would call an “unholy abomination”, whose horrifying abilities consist of being capable of saying “Meow”."
nas "“Miaow”, and “Hissss”."

cat "Purrrr…"

nas "And “purr”, of course. How could I ever forget about “purr”."

ro "Good grief…"
ro "So what’s the next step? A human/animal hybrid?"

nas "Heavens no! That would unethical, barbaric, heavy-handed-"
nas "And a complete waste of time, as the experiment has already been conducted and properly documented in “Usho’s guide to true alchemy”. Quite the gruesome read, if you ask me. "
nas "Fascinating, of course, even if Usho’s approach to the subject was downright dreadful." 
nas "You can’t just slap chaos magic on something and expect it to do the work for you! Some wizards…"

ro "I am glad you hold yourself up to a higher standard."

show nasim happy at midright with dissolve

nas "Of course. I strive for excellence."

"The cat jumped off his arms and ventured away, likely in search of the castle rats."

nas "So how can I be of assistance, Master Blackwell?"

jump nasim_talk

#########################################################################################################################

label nasim_talk:

menu:
    "Ask about transformation magic.":
        $ released_fix_rollback()
        jump aboutTransMagic
        
    "His early work?" if aboutTransSeen == True:
        $ released_fix_rollback()
        jump earlyWork
    
    "Ask about Alexia fertility treatment." if aboutTransSeen == True:
        $ released_fix_rollback()
        jump aboutFertTreat

    "Alexia’s first fertility treatment. (Coming soon!)" if aboutFertSeen == True:
        $ released_fix_rollback()
        "Not yet, pervs."
        jump nasim_talk
        
    "Leave":
        $ released_fix_rollback()
        return



#########################################################################################################################

label aboutTransMagic:

$ aboutTransSeen = True

show rowan necklace neutral at midleft with dissolve

ro "So how exactly does transformation magic work? Why do you need the chamber for it?"

if nasimAttitude > 0:
    show nasim neutral at midright with dissolve

"The wizard furrowed his eyebrows, giving Rowan a long, judgmental look."

nas "How can I explain it so you would understand…"

ro "I have been known to comprehend words."

nas "They all say that, but then you get to Sadi’s Second Law, or start talking about the symbiotic relationship between Chaos and natural entropy, and suddenly everybody has a blank look on their face."

show nasim happy at midright with dissolve

nas "Let’s start with personal experiences, these usually work best. Have you ever witnessed a physical transformation? Experienced one? Not just an illusion, but actual restructuring of a body."

ro "I’ve seen it a few times. A particularly nasty event from the war comes to mind. One of Karnas’ generals used a spell that crushed over a dozen of my soldiers, then amalgamated their bodies into some sort of horrid abomination.  "

show rowan necklace shock at midleft with dissolve

nas "Large, black-red beasts with several mouths?"

ro "How did you know?"

show rowan necklace neutral at midleft with dissolve

nas "It was “Aspect of Gluttony”, I suspect. It was mentioned in one of the castle’s books… The description of its effects was quite gruesome."

show rowan necklace concerned at midleft with dissolve

ro "I assure you, it did not do it justice."

nas "They rarely do, as I’ve come to learn. Anything else?"

if ev_happened("alexia_become_like_xzaratl"):
    show rowan necklace neutral at midleft with dissolve
    show nasim neutral at midright with dissolve
    ro "There was this one time with X’zaratl…"
    nas "And that’s all I need to know. I’m just going to assume it involved multiple futanari phalli, and little else."
    show rowan necklace happy at midleft with dissolve
    ro "This is the angriest I have ever seen somebody get at the mention of futa dicks."
    nas "Rowan, you have a species with intrinsic shapeshifting abilities, and they use it almost exclusively to create genitalia. It’s like seeing the man who painted the frescoes of Prothea cathedrals draw stick figures."
    nas "... But back to the topic at hand, before I launch myself into a rant. Transformations! - and why they’re so complicated."
    show rowan necklace neutral at midleft with dissolve
    
    
else:
    show rowan necklace neutral at midleft with dissolve
    ro "Nothing worth mentioning."
    nas "I see. Then allow me to explain the problem with transformation magic."
    show nasim neutral at midright with dissolve
    
nas "As you might know, on Solanse all things have a form. Not just a physical one, but also an inner form. A transcendantal idea of themselves, tied to the soul, engraved in the mind. A holy mandate of being, from Solansia herself."
    
"Rowan watched as the wizard scanned his room for something. Finally, he snagged a fresh apple from the top of his desk."

nas "Even inanimate objects possess it, though at a lesser capacity."

"He spoke a short incantation. The apple glowed pink, then with a loud “pop!” turned into a cube. He tossed it to Rowan, so he could take a closer look."

ro "How can something with no mind of its own know what form it should hold?"

show rowan necklace shock at midleft with dissolve

nas "It does not, and it cannot. But Solansia knows it, and her holy energies are all around us."

ro "Are you telling me Solansia dictates the shape of our fruits?"

nas "Vegetables too! Bit of a smotherer, our dear Goddess."

if avatar.corruption > 50:
    show rowan necklace angry at midleft with dissolve
    ro "Don’t you find that terrifying?"
    show nasim happy at midright with dissolve
    nas "It is disconcerting, but do not worry Master Rowan. I don’t expect us to be bound by her laws for much longer."
    show nasim neutral at midright with dissolve

show rowan necklace neutral at midleft with dissolve

nas "Now, If you pay attention to the apple…"

"He watched as, before his very eyes, the cubic apple started to lose its sharp edges, slowly resuming the form it held just moments ago."

nas "Had I used more power, it would keep this form for weeks or months. Had I used a lot of it, or used the chamber, I could implant a seed of chaotic energies inside it. A seed that would continuously refill the apple with energies that fuel the spell, countering Solansia’s influence."

ro "So the chamber is necessary to achieve permanency."

nas "It does a lot more than that, but for starters, yes. True, lasting alterations are simply out of our reach without it, as it would take considerable power to bruteforce the creation of a seed."
nas "Granted, some transformation rituals I’ve researched have been designed to conjure such a seed as the body is altered, but to my considerable disappointment the whole process is always woven into the spell. I can’t reverse engineer it."

show rowan necklace shock at midleft with dissolve
show nasim happy at midright with dissolve

nas "To be honest, I do feel a bit cheated. When I was a neophyte the local priests always warned us against dabbling in the dark arts. It was supposed to be an easy road to power. "

show rowan necklace happy at midleft with dissolve
show nasim neutral at midright with dissolve

nas "And here I am, a hurdle at every step."

ro "It might not be too late to rethink your career as a mad wizard."

nas "And quit halfway? Master Blackwell, how can you even suggest that!"

show rowan necklace neutral at midleft with dissolve

nas "But amusing banter aside, this is a much greater problem than you would expect. Demons aren’t exactly known to plan for the long term. "
nas "Castle Bloodmeen might appear to have quite the extensive library, but few tomes contain worthwhile information in them."

show nasim happy at midright with dissolve

nas "Luckily for us, what little they have was enough to give me some ideas. Ideas I have put to good use."

show rowan necklace shock at midleft with dissolve

nas "Would you suspect that it is possible to use Solansia’s own laws against her? Have her divine energies not fight the chaotic transformation, but reinforce it instead? "

show rowan necklace neutral at midleft with dissolve

ro "I’m not sure I follow."

nas "Don’t worry, I’ll dumb it down for you."

show nasim neutral at midright with dissolve

nas "It all ties to the “image of self” I talked about earlier. The one that is supposed to be in accord with our bodies."
nas "Consider this Rowan. You wake up every day, look into the mirror, and see a face that is not your own. This happens once, you suspect foul play. This happens again, you still think it trickery."
nas "But as it continues to repeat, day by day, every day, sooner or later a seed of doubt will sprout within you. A rogue thought telling you “Maybe this is who I am now? Maybe this is who I have always been?”"

ro "Hmph. That would never happen to me."

if avatar.corruption > 50:
    "For some reason, his words ringed hollow, but engrossed in his little speech Nasim did not notice it. "
    
nas "Likely not. But most people lack your iron will, Master Rowan."
nas "Prolonged transformation. Repeated daily. On a subject with low mental defences. And a few months later, you start to see results."
nas "You start to see their image of self perverted, transformed into the one you crafted for them. "

ro "It sounds like you tried it already."

show nasim happy at midright with dissolve

nas "Oh yes. Yes I did."

show nasim neutral at midright with dissolve

nas "But while the whole experiment was both exhilarating and quite illuminating, it took several months, and required quite the magical investment on my part. It provided me with the knowledge on how to proceed, but not the means."

#if tfchamber == true: (TODO)
    #show nasim happy at midright with dissolve
    #nas "And with the chamber uncovered, I now possess the means as well. I just need more time to get it going." 
    

#else

nas "Which is why-"

ro "Yes, yes, which is why you need the chamber."

show nasim happy at midright with dissolve

nas "You know the saying: If you have an important point to make, don’t try to be subtle about it."

show nasim neutral at midright with dissolve

nas "Regardless, I believe this covers the important bits. I could keep explaining the many, many particularities of transforming each body part, but that information would of little use to you."
nas "Anything else I might do for you, Master Rowan? Further questions, perhaps? "

jump nasim_talk

#########################################################################################################################

label aboutFertTreat:

$ aboutFertSeen = True

show rowan necklace neutral at midleft with dissolve
if nasimAttitude > 0:
    show nasim neutral at midright with dissolve
    
ro "Tell me Nasim, how extensive is your knowledge of the female anatomy?"

show rowan necklace shock at midleft with dissolve

nas "…. Are setting up some sort of joke here, Master Blackwell?"

menu:
    "Yes.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "Do your powers not spike after your thirtieth birthday?"
        show nasim angry at midright with dissolve
        nas "..."
        show nasim happy at midright with dissolve
        show rowan necklace shock at midleft with dissolve
        nas "Astounding work, Master Blackwell! I expect this will evoke a hearty laugh from all the orcs in the barracks! Well done, well done indeed!"
        show rowan necklace concerned at midleft with dissolve
        ro "A low blow, but I suppose I deserved that."
        show rowan necklace neutral at midleft with dissolve
        ro "Jokes aside, I do have a question."
        show nasim neutral at midright with dissolve
        
    "No.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "I phrased myself poorly."
        show rowan necklace neutral at midleft with dissolve

ro "When you make somebody female, is their equipment… Fully functional, so the speak? Would they be able to carry a child?"

nas "I believe so. But until I get the chamber going, there’s no way to test it. Any impregnation that happens during a temporary transformation might result in… Unpleasantness once the spell ends."
nas "The science is sound Rowan. I am merely limited by the resources at my disposal."

ro "Then hypothetically speaking, could your magic make a woman more or less fertile?"

nas "I suppose so? What are you building up to, Master Blackwell?"

show rowan necklace concerned at midleft with dissolve

ro "We have been… Trying for a child with Alexia for several years now. To no success. I was wondering if there were ways to increase the odds of conceiving."

show rowan necklace neutral at midleft with dissolve

nas "Assuming the fault lies with her… Hmmm…"

show rowan necklace happy at midleft with dissolve
show nasim happy at midright with dissolve

nas "There is something we could try."

show rowan necklace shock at midleft with dissolve

nas "I did mention repeated transformations can affect the “idea” of a person. If Alexia’s “form” is that of an infertile woman, we could try to break it by changing her body into that of a pregnant one."

show rowan necklace neutral at midleft with dissolve

nas "Or at least partially so. I cannot create life, as much as I’d wish otherwise."

show rowan necklace concerned at midleft with dissolve

nas "But a high enough concentration of chaos magic directed at her womb… And stimulating the breast tissue to prepare the body for maternity… Should be sufficient to show results."

show nasim neutral at midright with dissolve

ro "“High concentration of chaos magic?”"

nas "A womb is considerably more complex than an apple, Master Blackwell. We won’t get anywhere with half measures here."

"Nasim never dropped his casual tone. After all, he wouldn’t be the one whose wife was being made a test subject."

show rowan necklace neutral at midleft with dissolve

ro "… I’ll think about."

nas "Of course."

jump nasim_talk

####################################################################################################################################

#bootleg alexia 
label earlyWork:

$ bootlegAlexiaSeen = True

show rowan necklace neutral at midleft with dissolve
if nasimAttitude > 0:
    show nasim neutral at midright with dissolve
    
ro "Discussing the basics, you mentioned running repeated transformation on someone. What’s the full story behind that?"    
    
show rowan necklace shock at midleft with dissolve

"For a brief moment, Nasim’s expression grew tense. He brought the topic himself earlier, and seemed quite excited to breach it, so why the sudden concern?"

show rowan necklace neutral at midleft with dissolve

nas "There isn’t much to it, I’m afraid. I used some of the initial spells I developed to see what I can accomplish long term."

show nasim happy at midright with dissolve

nas "But it’s hardly representative of what the chamber is capable of, so I won’t bother you with the details."
nas "How could it compare to high level-chaos transformations! Just think about it! Functional wings! Multiple arms and the ability to use them without mental strain-"

show rowan necklace happy at midleft with dissolve

ro "Oh I have no doubt it’s all going to be revolutionary. But knowing your skill, I’m certain that even your early work is exceptional. I’d love to see it."

show nasim neutral at midright with dissolve

"Rowan flashed him his most winning smile. Nasim narrowed his eyes ever so slightly. Oh, he was not getting off the hook so easily. Rowan had far too much experience as a hunter to give up after sensing blood."

show nasim happy at midright with dissolve

nas "Master Blackwell, you humble me with your praise, but I can’t imagine taking what little time you have during your castle visits just so I can show off."

show nasim neutral at midright with dissolve

ro "Research Nasim, the time spent in the castle is precisely for learning what my subordinates are doing. Otherwise, I would never leave the bedroom and handle everything through notes."

nas "That hardly seems like an efficient way to govern-"

ro "It is not, as some people could then accidentally mistake an order for a polite request."

"Again, Rowan’s lips widened into a friendly smile, one did not quite reach the eyes. Finally, Nasim gave up, a soft scowl quickly passing though his expression."

nas "I suppose I brought this one on myself. Very well then, I’ll show you the results of my research. Just remember – you wanted this, not me."

hide rowan with moveoutleft
hide nasim with moveoutleft

"Cursing under his breath, the wizard led them both out of the library, in the direction of the castle dungeons."

scene black with fade

"They kept a slow pace, but Rowan did not hurry him along."
"Far too many people worked in the castle without proper supervision. It was important to remind them every once in a while, that the castle had someone ruling it, and that it was not the twins."
"To Andras and Jezera, the castle was little more than a family heirloom and a pretty throne."
"After a moment, the two reached a closed door deep in the dungeons. With a tense expression, Nasim opened them and allowed Rowan to enter."

scene bg8 with fade
show nasim neutral at midright with moveinleft
show rowan necklace neutral at midleft with moveinleft

"The cell was comfortably furnished, without excess, but far beyond what one would expect from a prison. it even had a couple of mirrors, and a soft bed-"

show rowan necklace shock at midleft with dissolve

"And the aforementioned early experiment sitting on it, looking at both of them with visual confusion."

show rowan necklace neutral at midleft with dissolve

"Rowan looked her in the eyes, then slowly turned to Nasim."

ro "So?"

nas "Well it’s…"

show nasim happy at midright with dissolve

nas "I suppose you were right, it is quite the achievement! A complete restructuring of the body! Granted, it took three months of full body transformations, every day, but the results are astounding."
nas "Obviously not to my expectations. Traces of the original race still remain, and I doubt I could remove them even if kept the transformations going for another quarter of a year. I am limited by the magic at my disposal, as they say."

show nasim neutral at midright with dissolve
show rowan happy at midleft with dissolve

ro "Oh yes, you did mention something like that before. But it is very impressive regardless, I’ll give you that."
ro "Mind commenting on the other thing?"

nas "I beg your pardon?"

ro "You know, the thing."

nas "“The thing”?"

ro "Yes, the thing."

show rowan necklace angry at midleft with dissolve

ro "The very small detail that is the fact that you have an orc hidden away in the castle dungeons, who for some fucking reason looks like a sexed up caricature of my fucking wife!"

"He simply couldn’t believe his own eyes. Right in front of him sat a very confused, female orc. Orc-traits aside, like large, lower tusks, and the slightly greenish skin, the woman had an unmistakable resemblance to Alexia."
"Or at the very least, a poor imitation of her. Her red hair had none of Alexia’s fiery shine, and they ran past her shoulders, unkempt and dirty. Her flat nose looked like it was broken a long time ago, and never healed properly."

show rowan necklace shock at midleft with dissolve

"And of course, one could not ignore the pair of impossibly large breasts on her chest, well visible under the loose shirt. They were complemented by an equally impossibly large backside, and thick, breeder hips."
"She looked like some sort of-"

boot "Mastah, who dis?"

show rowan necklace neutral at midleft with dissolve

nas "Please be quiet, Specimen zero three, I don’t want to discipline you again."

"The orcess moved her mouth silently a few times, then obediently shut up. Rowan slowly rubbed the base of his nose and took a deep breath to calm down."

ro "Why? Just… Why?"

"Nasim didn’t answer immediately, for the first time not having a sharp riposte at his disposal. The fact he had the decency to at the very least look embarrassed was the only thing that was saving him from a punch to the face."

show rowan necklace shock at midleft with dissolve

nas "If I may speak honestly, Master Blackwell… I... Needed something to get in Andras’ good favors."

nas "And after seeing how he treated Miss Alexia – mind you, back then I did not know who she was - I thought that perhaps he would find this… If not pleasing, then at the very least amusing."
nas "The transformation did not go as far as I had hoped. My intention was to turn her into a perfect copy, appearance-wise, but as you can see, her orcish descent is still very much prevalent."

ro "I’d say it’s not the only inaccuracy. Have you seen my wife? Do you think this is what her chest looks like?"
ro "Hell, do you think there exists any species that naturally develops breasts like that?!"

show rowan necklace angry at midleft with dissolve

nas "Some minotaur/human hybrids can go up to I-cups if you want to get technical-"

menu:
    "Smack him over the head.":
        $ released_fix_rollback()
        show rowan necklace angry at center with moveinleft
        show bg8 with sshake
        show nasim angry at midright with dissolve
        ro "It was a rhetorical question you fucking idiot."
        "Rowan saw the anger the fury in his eyes, saw his fingers twitch, a sparkle of energy coursing through them."
        "Rowan said nothing, waiting."
        "“Try me” hanged unspoken in the air."
        show rowan necklace neutral at midleft with moveoutleft
        show nasim neutral at midright with dissolve
        "Finally, the wizard relented, very slowly relaxing his posture and fingers. He lowered his head, and picked his next words very carefully."
        nas "Of course, my apologies, Master Blackwell."
        nas "Now, back to the matter at hand…"
        $ nasimAttitude -= 2
        
    "Restrain yourself.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        show nasim happy at midright with dissolve
        nas "- But I suppose that is not the answer you were looking for."
        show nasim neutral at midright with dissolve
        
nas "I am aware she looks a bit… Unnatural."
nas "But if I have learned anything from my experience with nobility, it is that no matter how much they applaud the fine, ethereal beauty one can find among the elves, what they all secretly desire is always the most vulgar of whores."

#if perception rank 1 (TODO)
#IF met, set flag: NasimNobilityBackground: Yes
#If not, do nothing.
#if Rowan has no ranks in perception, the remark slips his mind. Otherwise, he’ll be able to confront Nasim about his words later.

nas "So I enlarged her tits as much as it was physically possible, without making them look too ridiculous."

show rowan necklace shock at midleft with dissolve

nas "I also did some work on her sphincter. I hoped to make it more elastic, so she could better accommodate Lord Andras. Admittedly, I might have… Overdone it a little. I’d stay away from it, if I were you. You could fit a head there."

show rowan necklace neutral at midleft with dissolve

"Rowan groaned, while the orcess turned red from humiliation. Nasim really didn’t need to share that one with him."

show nasim happy at midright with dissolve

nas "But I do recommend the breasts! They’re perfect for titjobs. Give them a try, and consider this an apology."

show nasim neutral at midright with dissolve

ro "… You’re joking, right?"

nas "Why should I? I can’t really turn her back at this point, not yet at least, and for what it is worth I am genuinely sorry for using your wife’s likeness without your approval."

show nasim happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

nas "So as a sign of my apology, I do invite you to sample the end product of my efforts. You will not be disappointed."

show rowan necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

ro "“End product”?"

if avatar.corruption < 50:
    ro "Do you even hear yourself? I know we’re all accustomed to thinking of orcs as nothing more than savages, but they're not… Cattle!"
    
else:
    ro "I know she’s just an orc, but don’t you think it’s a bit too much to treat her like this? She’s not cattle, you know?"

nas "Do you object?"

menu:
    "Yes. This is inhumane.":
        $ released_fix_rollback()
        $ change_base_stat('c', -3)
        show rowan necklace angry at midleft with dissolve
        ro "How can I not object Nasim, this is insane, even by Castle Bloodmeen’s standards!"
        ro "What had this woman done to you to justify turning her into… This!"
        show rowan necklace shock at midleft with dissolve
        nas "She did try to rape me."
        show rowan necklace neutral at midleft with dissolve
        ro "What?"
        nas "My second week here. She and a bunch of orcs thought they could bully Cliohna’s students. She had the bad luck of picking me. So I thought to myself…"
        show nasim happy at midright with dissolve
        nas "“Hm, she wanted to turn me into a sex toy for her own amusement. It’s only fair to do the same in return, no?”"
        menu:
            "This is still going too far.":
                $ released_fix_rollback()
                $ change_base_stat('c', -2)
                show nasim neutral at midright with dissolve
                ro "There are laws Nasim. Whatever her crimes, you can’t just disfigure people for life."
                nas "In most countries it would have been in my right to kill her on the spot for such transgression."
                nas "… Not that any of them apply here, sans the will of the strong."
                if society_type == "feudalism":
                    ro "No anymore Nasim."
                    nas "Then I would advise you to update your laws."
                    nas "Regardless, she is lucky to be alive, and she knows it."
                else:
                    nas "Regardless, she is lucky to be alive, and she knows it."
                "Rowan scowled, while Nasim rolled his eyes, neither happy with the other."
                nas "You Rosarians and your delicate sensibilities…"
            
            "So he got himself a test subject. How convenient.":
                $ released_fix_rollback()
                ro "And suppose she didn’t attack you. Who would be sitting in this cell then?"
                "Nasim’s grin widened ever so slightly."
                nas "I suppose we’ll never know."
                show nasim neutral at midright with dissolve
                "Rowan scowled, while Nasim rolled his eyes, neither happy with the other."
                nas "You Rosarians and your delicate sensibilities…"
                
            "She had it coming.":
                $ released_fix_rollback()
                "Rowan turned his eyes to the orcess. She averted his gaze."
                show rowan necklace concerned at midleft with dissolve
                ro "(Not even a word of defence…)"
                show rowan necklace neutral at midleft with dissolve
                ro "“Live by the sword, die by the sword”?"
                nas "So they say."
                show nasim neutral at midright with dissolve
                "Rowan scowled a little. It still felt wrong, but it was hard to argue the point, given the circumstances. Nasim saw his reaction, and could not stop himself from rolling his eyes."
                nas "Oh Rowan, you Rosarians and your delicate sensibilities…"
                $ nasimAttitude += 1
                
    "Ask him if he’s really okay with this.":
        $ released_fix_rollback()
        ro "Be square with me Nasim. Do you honestly think there’s nothing wrong with that?"
        show nasim neutral at midright with dissolve
        nas "You Rosarians and your delicate sensibilities…"
        nas "I could pretend it’s only fair as she did try to rape me when I first came to the castle, but since you specifically requested honesty…"
        show nasim happy at midright with dissolve
        nas "Yes, I think there’s nothing wrong with it. And I don’t think you should find it surprising, given our current predicament."
        show nasim neutral at midright with dissolve
        
"Nasim sighed tiredly, then looked over his shoulder, at the cell doors. He said a few simple magic words, his fingers shimmering with arcane power."

show nasim happy at midright with dissolve

nas "A simple screening spell, worry not."

show nasim neutral at center with moveinleft

nas "Rowan, if I may speak openly… I understand many of the practices common here in Castle Bloodmeen may seem… I suppose “Reprehensible” would the proper term, but I urge you to remember our current location."
nas "And that is – just north of Rakshan wastes. In the seat of the deceased lord of chaos. In a fortress ruled by his children."
nas "Morality does not apply here, Rowan."

ro "That’s up to us to decide."

nas "No, it’s up to our masters, the twins."

if nasimAttitude >= 0:
    show nasim happy at center with dissolve
    nas "Make no mistake Rowan, I like you. There is no quarrel between us. So heed my advice when I tell you this:"
    show nasim neutral at center with dissolve

else:
    nas "Make no mistake Rowan, I don’t like you, but we share a common background, and I have nothing to gain by sabotaging your efforts. So heed my advice, when I tell you this:"
    
nas "Pick your battles. And learn to be ruthless."

"Nasim nodded at the orcess."

nas "This woman? She’s a slave and a criminal. You’d do well to show her no compassion. And consider this practice."

show rowan necklace angry at midleft with dissolve

ro "“Practice”?"

show rowan necklace neutral at midleft with dissolve
show nasim happy at center with dissolve

nas "Yes, practice! You are the hero of Rosaria, but I do not believe Jezera recruited you for your finer qualities. Kindness is rarely sought after in statesmen, and sooner or later she will seek to root it out of you."

show nasim neutral at center with dissolve

nas "If you don’t want to break apart the moment she asks you to put an entire village to the sword just to see you prove your commitment to the cause, I’d say you start here."

show nasim neutral at midright with moveoutright

"He patted Rowan on the shoulder, then headed for the exit."

nas "We are in for the long haul, Rowan Blackwell, savior of Solanse. Keep your heroism for later, and for the time being, try to enjoy yourself."

show nasim happy at midright with dissolve

nas "And you did ask to see the results of my research. So there you go, feel free to sample them. She was made for pleasure, after all."
nas "We’ll stay in touch, Master Blackwell."

hide nasim with moveoutright

"… And just like that, he was gone. Leaving him alone with orc woman, who kept quiet the whole time."

show rowan necklace concerned at center with moveinright

ro "Fucking hell..."

"He felt... Deprived of all emotions. An oversexed imitation of his wife. Made for the sole purpose of garnering favour with a man who thought “finesse” was a sophisticated dance move."
"He’d wanted to keep being pissed about it, but frankly, he depleted his capacity for outrage for the day."

ro "… He really did a number on you, didn’t he?"

"She shrugged her shoulders and smiled shyly in response. So subdued… Gods only knew what supplementary training had Nasim put her through."
"He briefly entertained the idea of asking her what she wanted, only to realize it would be a moot effort. The orcess was so thoroughly broken in, he doubted she would comprehend the notion of refusing him."

show rowan necklace neutral at center with dissolve

"… If he needed someone to unwind, she really was as good of an object for that as any."

menu:
    "Take another look at her.":
        $ released_fix_rollback()
        jump bootlegAlexiaSex
        
    "Get out of here, this is too weird.":
        $ released_fix_rollback()
        "But no matter how hard he tried, there was one thing he couldn’t ignore."
        show rowan necklace concerned at center with dissolve
        "Dull green or not, Alexia’s eyes kept staring at him out of Alexia’s slightly orcish face. It was bizarre, and no amount of perverse allure or mental gymnastics could change that."
        show rowan necklace neutral at center with dissolve
        ro "Stay here… Whatever your name is. I have to sort this out with Nasim."
        hide rowan with moveoutright
        "Sometime soon, preferably."
        return


label bootlegAlexiaSex:

$ BootlegName = "Orcess"

show rowan necklace concerned at center with dissolve

ro "(Twice the obscene eroticism… But none of Alexia’s glow.)"

show rowan necklace neutral at center with dissolve

"Where Alexia’s eyes shined brightly, the orc’s looked dull and unfocused. Alexia was full of life, this orcess here… Reminded him of the washed up whores in Rastedel."
"And she carried Alexia’s face."

show rowan necklace concerned at center with dissolve

ro "Goodness gracious… I don’t know if I can look at you…"

"The words left his mouth before he could stop himself. But the orcess did not seem to mind."

boot "Uh-huh… Ah don’ really like it myself, mastah… Too soft lookin’."

show rowan necklace neutral at center with dissolve

ro "And is there anything you like about your new form?"

boot "Uuhh… Da tits?"

"She admitted with some embarrassment, fidgeting under his gaze. Even such simple movements made the mounds under her shirt shake obscenely."

boot "Dey, uuuh, dey feel good. Really good."

"For all of Alexia’s beauty and grace that was implanted into her by Nasim… It was the whorish tits she liked most. It was almost upsetting."

menu:
    "Order her to remove her shirt.":
        $ released_fix_rollback()
        ro "Show me."
        boot "Uh?"
        ro "Your chest. Show me."
        "Not taking his eyes off her, he watched as she finally removed her shirt, presenting what Nasim no doubt considered “fine work”, but would never say so out loud."
        "They were massive, there was no other word for it. Two oversized orbs, each larger than her head. But despite that, they protruded proudly, round and shapely."
        "In sheer size, the woman easily trumped literally everybody in the castle. The wizard held nothing back."
        if avatar.corruption > 50:
            ro "You look like a cow."
            "She blushed at his harsh remark, but did not argue. It would be foolish to dispute it."
        menu:
            "Give her a spin after all.":
                $ released_fix_rollback()
                jump bootlegAlexiaSpin
                
            "Get out of here, this is too weird.":
                $ released_fix_rollback()
                "But no matter how hard he tried, there was one thing he couldn’t ignore."
                show rowan necklace concerned at center with dissolve
                "Dull green or not, Alexia’s eyes kept staring at him out of Alexia’s slightly orcish face. It was bizarre, and no amount of perverse allure or mental gymnastics could change that."
                show rowan necklace neutral at center with dissolve
                ro "Stay here… Whatever your name is. I have to sort this out with Nasim."
                hide rowan with moveoutright
                "Sometime soon, preferably."
                return

    "Get out of here, this is too weird.":
        $ released_fix_rollback()
        "But no matter how hard he tried, there was one thing he couldn’t ignore."
        show rowan necklace concerned at center with dissolve
        "Dull green or not, Alexia’s eyes kept staring at him out of Alexia’s slightly orcish face. It was bizarre, and no amount of perverse allure or mental gymnastics could change that."
        show rowan necklace neutral at center with dissolve
        ro "Stay here… Whatever your name is. I have to sort this out with Nasim."
        hide rowan with moveoutright
        "Sometime soon, preferably."
        return
        
label bootlegAlexiaSpin:

$ bootlegAlexiaFucked = True

show rowan necklace concerned at center with dissolve

ro "(I suppose I might as well take Nasim’s advice. It’d be a lie to say I’m not curious.)"

show rowan necklace neutral at center with dissolve

ro "Lay down. And forgive me in advance, but we’ll do it somewhat… Differently."

boot "Buh?"

#cg1 blurred
scene black with fade
show rowan necklace neutral behind black

"He stripped quickly and climbed on the bed. But rather than sit over her chest, he took a different position."

#cg1
scene black with fade
show rowan necklace neutral behind black

"He knelt over her head, so he would not see Alexia’s face, and would instead feast his eyes on the wide body of the orcess. Thick thighs, long legs, and of course – the two massive breasts, which the orcess oh so helpfully pressed together with her arms."

ro "Nasim really went all out, didn’t he?"

boot "Yes, mastah."

"A thin smile entered his lips. Now then… What should he start with?"

$ bootlegNipplePinch = False
$ bootlegNipplePinched = False
$ bootlegNipplePull = False
$ bootlegTitsFeel = False
$ bootlegTitsFelt = False
$ bootlegFingerSink = False
$ bootlegRoughCounter = 0

label bootlegTitsMenu:

menu:
    "Pinch her nipples." if bootlegNipplePinch == False:
        $ released_fix_rollback()
        $ bootlegNipplePinch = True
        $ bootlegNipplePinched = True
        "Two nubs stood proudly, amidst a pair of wide aureoles. With a half-grin, he put his hands over them, and pinched them lightly."
        boot "Ooo-oooh!"
        ro "Ho? Such a nice voice. Are they this sensitive?"
        boot "A-ah… Yes mastah…"
        "He pinched them again. Another delightful moan filled the chamber."
        ro "Good gracious… It’s almost too easy."
        jump bootlegTitsMenu
        
    "Pull them roughly." if bootlegNipplePull == False and bootlegNipplePinched == True:
        $ released_fix_rollback()
        $ bootlegNipplePull = True
        $ change_base_stat('c', 2)
        $ bootlegRoughCounter += 1
        "His grin grew wider. He pinched her nipples again, but this time, he didn’t stop there. He pulled them up, then to the side, making a painful moan escape the orcess lips."
        boot "Aaah-aaah! Mastah! Please, not so rough!"
        ro "Oh, as if you haven't been through worse."
        "He let them go, and watched, mesmerized, as they tried to spill across her chess, only to wobble enticingly. Was it magic that kept them so round? Made them seemingly immune to simple laws of gravity?"
        ro "He made you quite a spectacle, hasn’t he?"
        boot "Aaa-ah… Thank you?"
        "He chuckled under his breath. It wasn’t exactly a compliment, but he’ll let her have it…"
        jump bootlegTitsMenu
        
    "Feel them up." if bootlegTitsFeel == False:
        $ released_fix_rollback()
        $ bootlegTitsFeel = True
        $ bootlegTitsFelt = True
        "No longer able to deny their allure, he plunged his fingers straight into her mounds of flesh."
        boot "O-Ooh? Aah… Mastah…"
        ro "Sweet Goddess!"
        "They looked so fake, but the felt so soft! So yielding and warm, and-"
        boot "Aaa-aah!"
        "And they provoked such a nice reaction from their owner~"
        jump bootlegTitsMenu
        
    "No need to be gentle: sink your fingers in." if bootlegFingerSink == False and bootlegTitsFelt == True:
        $ released_fix_rollback()
        $ bootlegFingerSink = True
        $ change_base_stat('c', 2)
        $ bootlegRoughCounter += 1
        "It was not enough to simply feel them up. Rowan sunk his fingers deeper, kneading them roughly, in his lust forgetting about the pain he might be causing to the orcess."
        "She moaned in what must have been a mix of pain and pleasure, but uttered no word of protests. Her hands gripped the bedsheets, as she squirmed from the cruel caress."
        boot "Ah, mastah!"
        jump bootlegTitsMenu
        
    "Enough foreplay - Fuck her tits.":
        $ released_fix_rollback()
        jump bootlegSexContinue

label bootlegSexContinue:

ro "Get yourself ready, orc."

boot "Y-yes, mastah!"

"On demand, she started to spit at her tits, smearing the valley between them in preparation for his cock. There was nothing sensual in all of it. It was raw, perverse eroticism."

if avatar.corruption > 30 or bootlegRoughCounter == 2:
    "She was made to be a toy, and she acted like one. Like an object to be fucked and used. What reason was there to hold back?"
    menu:
        "Get yourself off with her tits.":
         $ released_fix_rollback()
         jump bootlegRoughTitfuck
            
        "Be gentle.":
           $ released_fix_rollback()
           jump bootlegGentleTitfuck

else:
    "She was made to be a toy, and she acted like one. Like an object to be fucked and used. But even she deserved some compassion, whether she believed so or not."
    jump bootlegGentleTitfuck
    
label bootlegRoughTitfuck:

ro "Hurry up, will you?"

boot "Y-yes…"
        
"He stroked his cock in anticipation, well aware she could see him do so. Her hands worked frantically, desperate to avoid punishment."

ro "Oh, just forget it. This is good enough."
        
boot "Ma-astaaah?!"

"He sunk his fingers in, and plunged his dick between her whorish breasts."
"He gasped in surprise at the delightful sensation. Nasim wasn’t kidding, these tits were made for cock. Warm and welcoming, soft yet somehow firm, perfect for forming a valley for his dick."

ro "Fuck, these feel great!"

boot "A-ah, t-thank you?"

"She grunted in pain while Rowan moved her tits up and down, impaling them on his dick. The orcess arched her back, helping him get a better angle. Between her legs, he saw her juices glisten."

ro "Enjoying yourself?"

boot "A-ah! Mastah! My t-tits! They’re on fiah!"

"He stifled a laugh."

ro "If you needed it so bad, then just touch yourself, you damn slut!"

"She didn’t mind his words – hell, it sounded like she enjoyed them. Her fingers sunk into her snatch greedily, jilling herself as Rowan pounded her tits without restraint."
"She came at least several times before him, moaning incomprehensibly, her screams mixing together with the slapping noise of his dick. It was perverse. It was obscene."
"He wouldn’t have it any other way."

jump bootlegSexEnding

label bootlegGentleTitfuck:

"His hands covered hers, circulating her breasts, admiring their volume. True wonders of human ingenuity."

if avatar.corruption > 30:
    if helayna_escaped == False:
        "Perhaps one day, he’ll have both Alexia and Helayna get an upgrade like this..."
    else:
        "Perhaps one day, he’ll have Alexia get an upgrade like this…"

boot "A mo-oment mastah-"

ro "It’s fine… You have to be thorough."
ro "It’s important that we both enjoy yourself, is it not?"

boot "A-a, ah…"

"He could almost hear her get flustered. Her fingers intertwined with his, and they both kept massaging her breasts, getting them nice and wet, ready to welcome his dick."

ro "Want to do it yourself?"

boot "Y-yes mastah!"

"Such enthusiasm! Seemed she didn’t get much dick locked down here…"

ro "Then get to it, will you?"

"Nodding her head with ardour, she guided his hands to seize her tits from the sides, then buckled her hips, arching her back, guiding him in-"

ro "A-ah?!"

"He gasped as her tits enveloped his dick, presenting him with a truly divine sensation. Warm and welcoming, soft yet somehow firm. Her breasts were simply wonderful – a work of art. A perverse tribute to what one can achieve with chaos magic."
"She started to move her tits slowly, up and down, caressing his cock with her delightful flesh. From the corner of his eyes, he saw her curl up the toes on her feet, something glistening between her legs-"

ro "Do you want to touch yourself?"

boot "A-ah-ah! M-mastah, can I-?"

"He laughed out loud, and slowly took her hands, claiming her charming mounds to himself."

ro "Yes, yes… Go wild, if you need."

"She inhaled sharply, and she heard her mumble her thanks, her free hands venturing south, seeking her snatch, and quickly plunging into it."
"She came at least several times before him, moaning incomprehensibly, her moans filling the room as he kept sliding into her breasts, taking the time to savor the sensation."
"But he couldn’t hold back forever."

label bootlegSexEnding:

ro "Aaah!"

"When he finally came, he painted her chest white, his cum clearly visible on her greenish screen. He took a moment to admire his handiwork, then got off the bed with a tired sigh."

scene bg8 with fade
show rowan necklace concerned at center with dissolve

ro "That was…. Something."

boot "Are ya satisfied… Mastah?"

show rowan necklace happy at center with dissolve

ro "I am. I can see why Nasim thought you’d make a good gift for Andras."

show rowan necklace concerned at center with dissolve

"He saw her smile, and despite her obscene form and despite the tusks, for a brief moment she genuinely resembled his wife."

ro "(… I really can’t leave her here.)"

"He’ll have to talk with Nasim about her."

scene black with fade

"And sometime soon."

return
