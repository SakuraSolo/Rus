# research and tech

init python:

    class Research(object):
        '''Base class for researches'''
        uid = 'BASE'
        name = 'BASE'
        category = 'BASE'
        completed = False
        cost = 0
        rp_spent = 0
        # text description of requirements
        requires = 'nothing'
        # text description of results
        unlocks = 'nothing'


        def req_met(self):
            '''Returns True if all requirements are met'''
            # researches are enabled by default
            return True

        def on_complete(self):
            '''This runs once when the research is completed'''
            pass


    class WorldAndTheWar(Research):
        uid = 'world_and_the_war'
        name = 'World and the War'
        category = 'history'
        cost = 40
        unlocks = 'Background info, choices in events.'


    class HistoryOfRosaria(Research):
        uid = 'history_of_rosaria'
        name = 'History of Rosaria'
        category = 'history'
        cost = 50
        requires = 'World and the war, visit Rosaria'
        unlocks = 'Background info, resources in realm, choices in events.'

        def req_met(self):
            # "visit Rosaria" check is automatic because the game starts there
            return castle.researches['world_and_the_war'].completed


    class MilitaryTactics(Research):
        uid = 'military_tactics'
        name = 'Military Tactics'
        category = 'military'
        cost = 40
        unlocks = 'Level 2 barracks.'

        def on_complete(self):
            castle.buildings['barracks'].max_lvl = 2


    class MilitaryLogistics(Research):
        uid = 'military_logistics'
        name = 'Military Logistics'
        category = 'military'
        cost = 120
        requires = 'Military tactics'
        unlocks = 'Level 3 barracks.'

        def req_met(self):
            return castle.researches['military_tactics'].completed

        def on_complete(self):
            castle.buildings['barracks'].max_lvl = 3


    class MilitaryRecreation(Research):
        uid = 'military_recreation'
        name = 'Military Recreation'
        category = 'military'
        cost = 100
        requires = 'Military tactics'
        unlocks = 'Level 2 arena.'

        def req_met(self):
            return castle.researches['military_tactics'].completed

        def on_complete(self):
            castle.buildings['arena'].max_lvl = 2


    class SurvivalismAndCartography(Research):
        uid = 'survivalism_and_cartography'
        name = 'Survivalism and Cartography'
        category = 'exploration'
        cost = 40
        unlocks = 'Extra movement on map and/or reduced cost in explored.'

        def on_complete(self):
            avatar._base_mp += 2


    class AdvancedSurvivalTechniques(Research):
        uid = 'advanced_survival_techniques'
        name = 'Advanced Survival Techniques'
        category = 'exploration'
        cost = 100
        requires = 'Survivalism and cartography'
        unlocks = 'Extra movement on map and/or reduced cost in explored.'

        def req_met(self):
            return castle.researches['survivalism_and_cartography'].completed


    class SurveyingAndTelescopics(Research):
        uid = 'surveying_and_telescopics'
        name = 'Surveying and Telescopics'
        category = 'exploration'
        cost = 40
        unlocks = 'Increases visible hex range to 2.'

        def on_complete(self):
            avatar.view_distance = 2


    class AdvancedTelescopics(Research):
        uid = 'advanced_telescopics'
        name = 'Advanced Telescopics'
        category = 'exploration'
        cost = 100
        requires = 'Telescopics'
        unlocks = 'Increases visible hex range to 3.'

        def req_met(self):
            return castle.researches['surveying_and_telescopics'].completed


    class Excavation(Research):
        uid = 'excavation'
        name = 'Excavation'
        category = 'resources'
        cost = 60
        requires = 'Claim a mine'
        unlocks = 'Increase to mine resource yield'

        def req_met(self):
            return False


    class AdvancedExtraction(Research):
        uid = 'advanced_extraction'
        name = 'Advanced Extraction'
        category = 'resources'
        cost = 100
        requires = 'Excavation'
        unlocks = 'Further increase to mine resource yield'

        def req_met(self):
            return castle.researches['excavation'].completed


    class LaborPlanning(Research):
        uid = 'labor_planning'
        name = 'Labor Planning'
        category = 'resources'
        cost = 60
        requires = 'Occupy a second village'
        unlocks = 'Increase to occupied village income yield.'

        def req_met(self):
            return False


    class Colonialism(Research):
        uid = 'colonialism'
        name = 'Colonialism'
        category = 'resources'
        cost = 100
        requires = 'Labor planning'
        unlocks = 'Further increase to occupied village income yield.'

        def req_met(self):
            return castle.researches['labor_planning'].completed


    class TradeRoutes(Research):
        uid = 'trade_routes'
        name = 'Trade Routes'
        category = 'resources'
        cost = 60
        requires = 'Tavern'
        unlocks = 'Increase to village trade yield'

        def req_met(self):
            return castle.buildings['tavern'].lvl > 0


    class ImprovedLogistics(Research):
        uid = 'improved_logistics'
        name = 'Improved Logistics'
        category = 'resources'
        cost = 100
        requires = 'Trade routes'
        unlocks = 'Further increase to village trade yield'

        def req_met(self):
            return castle.researches['improved_logistics'].completed


    class MonsterTaming(Research):
        uid = 'monster_taming'
        name = 'Monster Taming'
        category = 'monsters'
        cost = 60
        requires = 'Survivalism and cartography'
        unlocks = 'Warg Kennel, breeding pit'

        def req_met(self):
            return castle.researches['survivalism_and_cartography'].completed

        def on_complete(self):
            castle.buildings['kennel'].max_lvl = 1
            castle.buildings['pit'].max_lvl = 1


    class MonsterHandling(Research):
        uid = 'monster_handling'
        name = 'Monster Handling'
        category = 'monsters'
        cost = 160
        requires = 'Monster taming, breeding pit'
        unlocks = 'Can breed medium sized monsters.'

        def req_met(self):
            return castle.researches['monster_taming'].completed and castle.buildings['pit'].lvl > 0


    class MonsterZoology(Research):
        uid = 'monster_zoology'
        name = 'Monster Zoology'
        category = 'monsters'
        cost = 120
        requires = 'Monster taming, breeding pit'
        unlocks = 'Level 2 breeding pit.'

        def req_met(self):
            return castle.researches['monster_taming'].completed and castle.buildings['pit'].lvl > 0

        def on_complete(self):
            castle.buildings['pit'].max_lvl = 2


    class SpecialHandlingTechniques(Research):
        uid = 'special_handling_techniques'
        name = 'Special Handling Techniques'
        category = 'monsters'
        cost = 240
        requires = 'Monster handling, monster zoology'
        unlocks = 'Can breed large sized monsters.'

        def req_met(self):
            return castle.researches['monster_handling'].completed and castle.researches['monster_zoology'].completed


    class Opulence(Research):
        uid = 'opulence'
        name = 'Opulence'
        category = 'diplomacy'
        cost = 40
        unlocks = 'Level 2 castle hall, level 2 living quarters'

        def on_complete(self):
            castle.buildings['hall'].max_lvl = 2
            castle.buildings['quarters'].max_lvl = 2


    class FiendishDiplomacy(Research):
        uid = 'fiendish_diplomacy'
        name = 'Fiendish diplomacy'
        category = 'diplomacy'
        cost = 120
        requires = 'Opulence, level 2 castle hall'
        unlocks = 'Can recruit new soldier types.'

        def req_met(self):
            return castle.researches['opulence'].completed and castle.buildings['hall'].lvl >= 2


    class DarkSubterfuge(Research):
        uid = 'dark_subterfuge'
        name = 'Dark Subterfuge'
        category = 'diplomacy'
        cost = 60
        requires = 'Opulence'
        unlocks = 'Brothel'

        def req_met(self):
            return castle.researches['opulence'].completed

        def on_complete(self):
            castle.buildings['brothel'].max_lvl = 1


    class SilksAndSmiles(Research):
        uid = 'silks_and_smiles'
        name = 'Silks and smiles'
        category = 'diplomacy'
        cost = 160
        requires = 'Dark Subterfuge, brothel'
        unlocks = 'Level 2 brothel, level 2 tavern.'

        def req_met(self):
            return castle.researches['dark_subterfuge'].completed and castle.buildings['brothel'].lvl >= 1

        def on_complete(self):
            castle.buildings['brothel'].max_lvl = 2
            castle.buildings['tavern'].max_lvl = 2


    class ContactNetwork(Research):
        uid = 'contact_network'
        name = 'Contact Network'
        category = 'research and magic'
        cost = 40
        unlocks = 'Level 2 library, level 2 dark sanctum'

        def on_complete(self):
            castle.buildings['library'].max_lvl = 2
            castle.buildings['sanctum'].max_lvl = 2


    class BasicSummoning(Research):
        uid = 'basic_summoning'
        name = 'Basic Summoning'
        category = 'research and magic'
        cost = 60
        requires = 'Contact network'
        unlocks = 'Summoning Chambers'

        def req_met(self):
            return castle.researches['contact_network'].completed

        def on_complete(self):
            castle.buildings['summoning'].max_lvl = 1


    class Demonology(Research):
        uid = 'demonology'
        name = 'Demonology'
        category = 'research and magic'
        cost = 240
        requires = 'Basic summoning, summoning chambers'
        unlocks = 'Can summon demons'

        def req_met(self):
            return castle.researches['basic_summoning'].completed and castle.buildings['summoning'].lvl >= 1


    class Smelting(Research):
        uid = 'smelting'
        name = 'Smelting'
        category = 'metalwork'
        cost = 60
        unlocks = 'Level 2 forge'

        def on_complete(self):
            castle.buildings['forge'].max_lvl = 2


    class TheRiddleOfSteel(Research):
        uid = 'The Riddle of Steel'
        name = 'The Riddle of Steel'
        category = 'metalwork'
        cost = 80
        requires = 'Smelting'
        unlocks = 'Allows steel equipment to be made from iron'

        def req_met(self):
            return castle.researches['smelting'].completed


    # all researches are loaded from this list at the start
    all_researches = [WorldAndTheWar, HistoryOfRosaria, MilitaryTactics, MilitaryLogistics, MilitaryRecreation, SurvivalismAndCartography,
        AdvancedSurvivalTechniques, SurveyingAndTelescopics, AdvancedTelescopics, Excavation, AdvancedExtraction, LaborPlanning, Colonialism,
        TradeRoutes, ImprovedLogistics, MonsterTaming, MonsterHandling, MonsterZoology, SpecialHandlingTechniques, Opulence, FiendishDiplomacy,
        DarkSubterfuge, SilksAndSmiles, ContactNetwork, BasicSummoning, Demonology, Smelting, TheRiddleOfSteel]


    # all categories of researches
    all_research_categories = ['history', 'military', 'exploration', 'resources', 'monsters', 'diplomacy', 'research and magic', 'metalwork']
