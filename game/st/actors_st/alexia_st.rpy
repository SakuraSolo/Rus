# Alexia (Rowan's wife)
init python:

    class AlexiaSt(ActorSt):
        '''Alexia (Rowan\'s wife)'''
        def __init__(self):
            super(AlexiaSt, self).__init__('alexia', 'Alexia')
            self.perspn = 'she'
            self.posspn = 'her'
            self.affinity = 75
            # all outfits for actor: {'outfit uid': ('prefix path', requirements), ...}
            self._all_outfits = {
                'village': ('Village dress', 'images/Sprites/Alexia/alexia_village', None),
                'white': ('White outfit', 'images/Sprites/Alexia/alexia_white_outfit', None),
                'nude': ('Nude', 'images/Sprites/Alexia/alexia_nude', self._nude_req),
            }
            self._outfits = ['white', 'nude', 'village']
            self._outfit = 'white'

        @property
        def outfit_img(self):
            '''Returns outfit image based on actor\'s stats'''
            if self.lust > 60:
                return self._all_outfits[self._outfit][1] + '_lust_high.png'
            elif self.lust > 30:
                return self._all_outfits[self._outfit][1] + '_lust_med.png'
            else:
                return self._all_outfits[self._outfit][1] + '_lust_low.png'

        @property
        def all_outfits(self):
            '''Returns list of all outfits'''
            return self._all_outfits.keys()

        @property
        def outfits(self):
            '''Returns unlocked (owned) outfits'''
            return self._outfits

        @property
        def outfit(self):
            return self._outfit

        @outfit.setter
        def outfit(self, uid):
            if uid in self._all_outfits:
                self._outfit = uid

        def outfit_req(self, uid):
            '''Checks requirements for given outfit'''
            if self._all_outfits[uid][2] is None:
                return True
            else:
                return self._all_outfits[uid][2]()

        def _nude_req(self):
            return (self.depravity >= 30) or (self.obedience >= 30)
