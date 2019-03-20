# Alexia jobs and dialogues
init python:

    event('alexia_maid', conditions=('Rowan_sc',), triggers="st_alexia_maid", group='alexia_training')
    event('alexia_tavern_wench', conditions=('Rowan_sc',), triggers="st_alexia_tavern_wench", group='alexia_training')
    event('alexia_dancer', conditions=('Rowan_sc',), triggers="st_alexia_dancer", group='alexia_training')
    event('alexia_whore', conditions=('Rowan_sc',), triggers="st_alexia_whore", group='alexia_training')
    event('alexia_rest', conditions=('Rowan_sc',), triggers="st_alexia_rest", group='alexia_training')
    event('alexia_librarian', conditions=('Rowan_sc',), triggers="st_alexia_librarian", group='alexia_training')
    event('alexia_etiquette', conditions=('Rowan_sc',), triggers="st_alexia_etiquette", group='alexia_training')
    event('alexia_obedience', conditions=('Rowan_sc',), triggers="st_alexia_obedience", group='alexia_training')
    event('alexia_slut', conditions=('Rowan_sc',), triggers="st_alexia_slut", group='alexia_training')
    event('alexia_exhibitionism', conditions=('Rowan_sc',), triggers="st_alexia_exhibitionism", group='alexia_training')


label alexia_maid:
    $ renpy.block_rollback()
    if alexia.depravity <= 30:
        scene alexia_maid_1
    else:
        scene
    if alexia.skill('maid') < 25:
        '[alexia.name] spends the week cleaning around the castle, as instructed, but unfortunately does a very poor job. As a result, [alexia.perspn] receives very little in the way of payment for [alexia.posspn] work.'
    elif alexia.skill('maid') <= 50:
        'The week flies by as [alexia.name] does [alexia.posspn] best to ensure that the castle is as spotless as possible. Despite [alexia.posspn] efforts though, the result is remarkable average, and [alexia.perspn] is judged to be worthy of only similarly average pay.'
    elif alexia.skill('maid') <= 75:
        'By now, [alexia.name] has started to get accustomed to cleaning the castle, as well as the areas which require the most work to clean. Using this knowledge, [alexia.perspn] is able to do a good job in ensuring most of the dust and grime has been done away with, for which [alexia.posspn] is well rewarded.'
    else:
        'Having spent so much time cleaning the castle, [alexia.name] is now an expert at the task. Armed with a mop and bucket, or a trusty duster, [alexia.perspn] is a firm fixture seen around the castle. By the time [alexia.perspn] is done cleaning everything is spotless, and the quality of the payment matches the quality of the job.'
    $ do_job(alexia)
    return


label alexia_librarian:
    $ renpy.block_rollback()
    if alexia.depravity <= 30:
        scene alexia_library_1
    else:
        scene
    if alexia.skill('librarian') < 25:
        '[alexia.name] is put to work re-shelving books in the library, but as [alexia.perspn] does not know the layout very well, it is a slow and laborious process. By the end of the week, there are still many books piled on the floor, and the payment [alexia.perspn] receives from Clionha reflects her displeasure.'
    elif alexia.skill('librarian') <= 50:
        'After spending a little bit of time working in the library, [alexia.name] has begun to get a handle on the location of a number of different book categories, but the work is still slow going. There are still a number of piles left when Cliohna arrives to pay [alexia.posspn], and as a result, the fee [alexia.perspn] receives is rather modest.'
    elif alexia.skill('librarian') <= 75:
        'With a good deal of library experience under their wing, [alexia.name] has no problem sorting and shelving most books, with only a few giving [alexia.posspn] a problem. When all is said and done, only a few piles remain which Cliohna finds satisfactory, handing over a suitable amount of coin for a job well done.'
    else:
        'Having done so much shelving in the library, [alexia.name] could do the job in [alexia.posspn] sleep. With every index and location memorized from weeks of sorting, the piles of books vanish in no time at all. The library is so tidy that Clionha even manages a smile when she sees the job [alexia.name] has done, and hands over a quite handsome reward as thanks.'
    $ do_job(alexia)
    return


label alexia_tavern_wench:
    $ renpy.block_rollback()
    scene
    'Alexia is serving at the tavern'
    $ do_job(alexia)
    return


label alexia_dancer:
    $ renpy.block_rollback()
    scene
    'Alexia is dancing at the tavern, entertaining customers'
    $ do_job(alexia)
    return


label alexia_whore:
    $ renpy.block_rollback()
    scene
    'Alexia is working in the castle brothel'
    $ do_job(alexia)
    return


label alexia_rest:
    $ renpy.block_rollback()
    scene
    'Alexia is resting'
    $ alexia.energy = 100
    return


label alexia_etiquette:
    $ renpy.block_rollback()
    scene
    if alexia.depravity < 20:
        'Jezera spends each day trying to get the sexually inhibited [alexia.name] to loosen up a little without much in the way of success. When the week comes to a close, [alexia.perspn] seems slightly more receptive to Jezera’s way of thinking.'
    elif alexia.depravity < 40:
        'Having gotten [alexia.name] to open up a little more, Jezera continues her lessons on bringing out the inner slut. While there is still a ways to go, the demon notices that her daily tutoring is certainly having the intended effect.'
    elif alexia.depravity < 60:
        'Jezera smirks as she watches just how far [alexia.name] has fallen since [alexia.perspn] began their training. After another week of her special tutoring, [alexia.name] has taken one more step down their road to utter depravity.'
    $ do_job(alexia)
    return


label alexia_obedience:
    $ renpy.block_rollback()
    scene
    # TODO: these texts rely on obedience stat, not on training level. It is more reliable to use training levels directly
    if alexia.obedience < 20:
        'Jezera tries her best to teach Alexia the basics of servitude, but the girl is useless, making for a very unhappy mistress. At least by the end of the week, she is slightly less unruly than she was at the start.'
    elif alexia.obedience < 40:
        'Now that Alexia has begun to learn her place, Jezera continues her lessons in order to break whatever remains of her will. After a few days of the demon imparting her lessons with the threat of force, she sees a little less apprehension in the girl when she orders her to act.'
    elif alexia.obedience < 60:
        'The lessons have now taken a firm hold on Alexia, and she now acts without hesitation to fulfil any request that Jezera makes of her. The demon smirks upon noticing submission had begun to take root in the girl, and she was starting to enjoy life as a slave.'
    $ do_job(alexia)
    return


label alexia_slut:
    $ renpy.block_rollback()
    scene
    'Slut training for Alexia'
    $ do_job(alexia)
    return


label alexia_exhibitionism:
    $ renpy.block_rollback()
    scene
    'Exhibitionism training for Alexia'
    $ do_job(alexia)
    return


# TODO: maybe move following dialogues to separate file
label alexia_confirm_self_title:
    $ renpy.block_rollback()
    scene
    al 'Yes [alexia.player_title], from now on I will refer to myself as [alexia.self_title].'
    jump train_alexia


label alexia_confirm_player_title:
    $ renpy.block_rollback()
    scene
    al 'Okay, from now on I will call you [alexia.player_title].'
    jump train_alexia
