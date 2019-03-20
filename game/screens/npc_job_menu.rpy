# small menu for choosing a job for NPC and show some info
screen npc_job_menu(align=None):
    if castle.npc_with_jobs and systems.npc_jobs:
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            xsize 150
            ysize 110
            if align:
                align align
            hbox:
                style_prefix 'small'
                for npc_name in castle.npc_with_jobs:
                    hbox:
                        xpos 100
                        ypos 10
                        xsize 200
                        text '{}\'s Stress: {}'.format(all_actors[npc_name].name, all_actors[npc_name].job_state.stress) align (0.5, 0.5)
                    hbox:
                        xpos -100
                        ypos 40
                        xsize 200
                        button action [Show('npc_job_selector', ac_uid=npc_name), SensitiveIf(alexia_cant_work_weeks <= 0)]:
                            #xpos 15
                            xsize 200
                            if get_actor_job(npc_name):
                                text '{}  ({:.1%})'.format(all_actor_jobs[get_actor_job(npc_name)]['name'], all_actors[npc_name].job_state.efficiency())
                            else:
                                text 'Choose job' align(0.5, 0.5)

screen npc_job_selector(ac_uid):
    modal True
    frame:
        background '#000a'
        xfill True
        yfill True
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            align (0.5, 0.5)
            has vbox
            xsize .5
            text 'Choose job' bold True xalign 0.5
            for job_uid in all_actor_jobs:
                button action [SetJob(ac_uid, job_uid), Hide('npc_job_selector'), renpy.restart_interaction]:
                    background None
                    insensitive_background '#400'
                    frame:
                        xfill True
                        background Frame('gui/stats_border.png', 12, 12)
                        has vbox
                        hbox:
                            text all_actor_jobs[job_uid]['name'] bold True
                            null width 40
                            text '{:.1%}'.format(all_actors[ac_uid].job_state.efficiency(job_uid))
                        text 'Work under: {}'.format(all_actor_jobs[job_uid]['boss'])
                        text 'Effect: {}'.format(all_actor_jobs[job_uid]['effect'])


init python:
    class SetJob(Action):
        def __init__(self, ac_uid, job_uid):
            self.ac_uid = ac_uid
            self.job_uid = job_uid

        def get_sensitive(self):
            if self.job_uid == 'breeding' and castle.buildings['pit'].lvl == 0:
                return False
            elif self.job_uid == 'forge' and castle.buildings['forge'].lvl == 0:
                return False
            if alexia_cant_work_weeks > 0:
                return False
            return True

        def __call__(self):
            all_actors[self.ac_uid].job_state.job = self.job_uid
