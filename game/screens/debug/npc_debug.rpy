# info and debug controls for NPC (in npc_controls)
screen npc_debug(actor, npc_debug_details):
    frame:
        has vbox
        textbutton actor.name + '  debug' action (ToggleScreenVariable('npc_debug_details'), renpy.restart_interaction)
        if npc_debug_details:
            viewport:
                mousewheel True
                scrollbars 'vertical'
                xsize 400
                vbox:
                    for stat in ('energy', 'affinity', 'corruption', 'lust', 'reputation', 'depravity', 'dominance', 'obedience', 'nymphomania', 'exhibitionism'):
                        hbox:
                            frame:
                                background None
                                xpadding 0
                                ypadding 0
                                xsize 200
                                text '{}: {}'.format(stat, getattr(actor, stat))
                            textbutton '+10' action SetField(actor, stat, getattr(actor, stat) + 10)
                            textbutton '+1' action SetField(actor, stat, getattr(actor, stat) + 1)
                            textbutton '-10' action SetField(actor, stat, getattr(actor, stat) - 10)
                            textbutton '-1' action SetField(actor, stat, getattr(actor, stat) - 1)
                    text 'Job skills' xalign 0.5
                    for job_skill in actor.job_skills:
                        hbox:
                            frame:
                                background None
                                xpadding 0
                                ypadding 0
                                xsize 200
                                text '{}: {}'.format(job_skill, actor.job_skills[job_skill])
                            textbutton '+10' action Function(actor.set_skill, job_skill, actor.skill(job_skill) + 10)
                            textbutton '+1' action Function(actor.set_skill, job_skill, actor.skill(job_skill) + 1)
                            textbutton '-10' action Function(actor.set_skill, job_skill, actor.skill(job_skill) - 10)
                            textbutton '-1' action Function(actor.set_skill, job_skill, actor.skill(job_skill) - 1)
