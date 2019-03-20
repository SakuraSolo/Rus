import os


OUTFILE = 'rpy_code.py'
TO_TEST = ('actor.rpy', 'actor_st.rpy', 'avatar.rpy', 'inventory.rpy', 'items.rpy', 'castle.rpy', 'balance.rpy', 'utils.rpy', 'lands.rpy', 'skills.rpy', 'level_up_helper.rpy',
    'upgrades.rpy', 'jobs.rpy', 'alexia.rpy', 'alexia_st.rpy', 'buildings.rpy', 'troops.rpy', 'research.rpy', 'world.rpy', 'maps_res.rpy', 'status_effects.rpy', 'spy.rpy', 'all_objects.rpy',
    'spy_mission_defs.rpy', 'world_create_map.rpy', 'raid_state.rpy', 'event_manager.rpy', 'actor_job.rpy', 'journal.rpy', 'quests.rpy')


def rtp_copy(fname, outf):
    in_py_init = False
    #~ coping = False
    with open(fname, 'r') as f:
        for line in f:
            if not in_py_init:
                if line.startswith('init') and 'python' in line:
                    in_py_init = True
                    outf.write('\n\n# ' + fname +'\n')
                    continue
            #~ else:
                #~ if coping:
                    #~ if not (line.startswith('        ') or line.strip().startswith('#') or line == '\n'):
                        #~ coping = False
                #~ elif line.startswith(('    class', '    def')) and (line[10:].startswith(TO_TEST) or line[8:].startswith(TO_TEST)):
                    #~ coping = True
                    #~ outf.write('\n\n# ' + fname +'\n')
            if in_py_init:
                if line.strip().startswith('#'):
                    continue
                elif line.startswith('label '):
                    in_py_init = False
                    continue
                outf.write(line[4:])



with open(OUTFILE, 'w') as outfile:
    outfile.write('import mock\n')
    outfile.write('config = mock.Mock()\n')
    for root, dirs, files in os.walk('..'):
        # iterate over all '.rpy' files
        for rpy in [f for f in files if f.endswith('.rpy')]:
            # if file is to be tested
            if rpy in TO_TEST:
                rtp_copy(os.path.join(root, rpy), outfile)


