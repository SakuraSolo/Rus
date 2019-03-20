# conditions and changes (duration etc.) for spy missions
init python:

    class SpyMissionDef(object):
        '''Base class for definition of spy mission'''
        # label to call when mission will be completed
        lbl = None
        # type of mission
        kind = None

        def condition(self, spy, loc, started):
            return True

        def create_sm(self, spy, loc, started):
            duration = random.randint(1, 2) + 1
            return SpyMission(spy.uid, self.kind, loc, duration, started, self.lbl)


    class SMInfiltrationNormal(SpyMissionDef):
        lbl = 'sm_infiltration_normal'
        kind = 'infiltration'


    class SMInfiltrationDominatorPrisoners(SpyMissionDef):
        lbl = 'sm_infiltration_dominator_prisoners'
        kind = 'infiltration'

        #2, Dominator gets some prisoners.
        #Req Master/Mistress trait and at least one open dungeon space.  No change to week time.
        def condition(self, spy, loc, started):
            if (('Master' in spy.traits) or ('Mistress' in spy.traits)) and (castle.buildings['dungeon'].prisoners < castle.buildings['dungeon'].capacity):
                return True


    class SMInfiltrationDelays(SpyMissionDef):
        lbl = 'sm_infiltration_delays'
        kind = 'infiltration'

        #3, Delays.  Impulsives are even worse.
        #Req non-methodical trait.  Adds an extra two weeks to completion time, impulsives gain four weeks instead.
        def condition(self, spy, loc, started):
            if not 'Methodical' in spy.traits:
                return True

        def create_sm(self, spy, loc, started):
            duration = random.randint(1, 2) + 3
            if 'Impulsive' in spy.traits:
                duration += 2
            return SpyMission(spy.uid, self.kind, loc, duration, started, self.lbl)


    class SMInfiltrationBribe(SpyMissionDef):
        lbl = 'sm_infiltration_bribe'
        kind = 'infiltration'


    # special non-automatic spy mission
    class SMRaeveKeepInfiltrate(SpyMissionDef):
        lbl = 'raeve_keep_infiltrated'
        kind = 'infiltration'

        def condition(self, spy, loc, started):
            # should be applied manually
            return False
        
    class OrciadInfiltrate(SpyMissionDef):
        lbl = 'delane_corruption_week3'
        kind = 'infiltration'
        duration = random.randint(1, 1) + 2
        
        
    # list of all spy mission definitions
    spy_mission_defs = [SMInfiltrationNormal, SMInfiltrationDominatorPrisoners, SMInfiltrationDelays, SMInfiltrationBribe]

