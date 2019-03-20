# various "warning" events
init python:
    #### Warning about not conquering Raeve keep (end of eighteenth week) ####
    # Always triggers week 18 immediately after exploration finishes if you haven't yet conquered Raeve keep.
    # TODO check if real goal 2 is completed
    event('warning_raeve_keep', triggers="week_end", conditions=('week == 18', 'not goal2_completed'), group='warning', run_count=1, priority=pr_warning)


label warning_raeve_keep:
#### Warning about not conquering Raeve keep (end of eighteenth week) ####
# Always triggers week 18 immediately after exploration finishes if you haven't yet conquered Raeve keep.

scene black with flash
show bg10 with fade
show rowan necklace neutral at midleft with dissolve
show andras smirk at midright with dissolve

ro "(Uh oh.  Andras never meets me at the portal.)"

an "Well servant, how are things going? Did you enjoy yourself out in your homeland?"

show andras angry at midright with dissolve

an "Just thought I'd remind you that a certain keep hasn't been delivered to us yet and the clock is ticking."

show andras happy at midright with dissolve

an "Carry on."

hide andras with moveoutright

ro "(It's always a pleasure dealing with you, Andras.)"

#end event
return
