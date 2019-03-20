init python:

    event ('research_report', triggers="week_start", conditions=('len(castle.completed_researches) > 0',), priority=pr_new_rs)


# an event to present reports of completed researches at the beginning of a week
label research_report:

# Show library background, Rowan and Cliohna appear.
scene library
show rowan necklace neutral at midleft with dissolve
show cliohna neutral at cliohnaright with dissolve

# Randomly decide one of the following scenes to be displayed.
$ temp = renpy.random.choice(('.v1', '.v2', '.v3', '.v4'))
jump expression ''.join(('research_report', temp))

label .v1:
    cl "Here is the report on the latest project.  I'm sure you'll find the results to be of use."

    # Show completion report.  It fills the screen, rather than using the regular text box.
    # delete uid of completed research from castle.completed_researches
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    ro "Professional as always, I see.  Please hand me the list of available projects so I can assign your next one."

    "Wordlessly and expressionless, Cliohna passed her updated sheet to Rowan."

    # Select a new research project.
    call screen researches_screen(True)

    cl "I understand.  If there is nothing else, I will begin immediately."

    #end scene.
    return

label .v2:
    ro "So Cliohna, what have you got for me?"

    cl "In-spite of a couple setbacks, I have finished the project."

    # Show completion report.
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    "No sooner had Rowan finished skimming the page was Cliohna holding another paper to him."

    cl "Here is my new list of possible avenues of research."

    # Select a new research project.
    call screen researches_screen(True)

    ro "Good luck."

    cl "I hardly need it."

    # end scene
    return

label .v3:
    cl "I finished this a bit earlier than expected, so I've been doing some preliminary work on some of the other projects in anticipation of your needs."

    # Show completion report.
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    cl "Sometimes I'm amazed at just how much the twins trust you to make the correct choice.  Neither of them is willing to assign a research project in your place."

    "The witch then handed him the list of potential projects, slightly changed from the last time."

    # Select a new research project.
    call screen researches_screen(True)

    ro "Sorry if that wasn't what you were expecting."

    cl "You have to make difficult decisions based on both the current situation, and our potential future situations.  It is not a simple task."

    # End scene
    return

label .v4:
    "Cliohna didn't seem to be in a talkative mood today, so Rowan didn't bother making small talk when he came to pick up the report on her latest research project."

    "He found it sitting on a table next to her list of new research topics, sitting nearby the witch who was currently engrossed in some magic experiment."

    # Show completion report.
    $ temp2 = castle.completed_researches.pop()
    call screen research_completion_report(temp2)

    "Once he finished reading, he took at look at the list of topics."

    # Select a new research project.
    call screen researches_screen(True)

    "After noting down his choice on an unused scrap of paper, the twin's agent took his leave from the library."

    # End scene.
    return
return

