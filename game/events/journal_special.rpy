# special (system) events for journal parts
init python:
    event('corruption_glossary', triggers="week_start", conditions=('avatar.corruption > 5',), run_count=1, priority=pr_system)
    event('guilt_glossary', triggers="week_start", conditions=('avatar.guilt > 5',), run_count=1, priority=pr_system)
    event('infamy_glossary', triggers="week_start", conditions=('avatar.infamy > 5',), run_count=1, priority=pr_system)


label corruption_glossary:
    $ glossary_add('corruption_start')
    $ deactivate_event('corruption_glossary')
    return


label guilt_glossary:
    $ glossary_add('guilt_start')
    $ deactivate_event('guilt_glossary')
    return


label infamy_glossary:
    $ glossary_add('infamy_start')
    $ deactivate_event('infamy_glossary')
    return
