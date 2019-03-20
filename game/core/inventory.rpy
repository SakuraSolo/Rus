init python:

    from collections import Counter


    # TODO: test rollback for inventory and items
    class Inventory(object):
        '''Equipped inventory of someone'''

        def __init__(self, avatar):
            # reference for avatar owning this inventory
            self.avatar = avatar
            # slots for equipment
            self.slots = {}
            for slot in equip_slots:
                self.slots[slot] = None
            # slots that can't be equipped temporary
            self.blocked_slots = set()
            # backpack - all items owned by player
            self.bp = Counter()

        def add_items(self, items):
            '''Add a sequence of items to backpack.'''
            for item in items:
                self.add(item)

        def add(self, uid):
            '''Add single item to inventory (only registered items allowed).'''
            if uid in all_items:
                self.bp[Item(uid)] += 1
            else:
                # if item is not registered, do not add it and print warning
                print('Not registered item uid: {}'.format(uid))

        def remove(self, uid):
            '''Remove single item.'''
            it = Item(uid)
            if it in self.bp:
                self.bp[it] -= 1
                # if last item of given type is removed, del it from counter
                if self.bp[it] < 1:
                    # if item is last and equipped, unequip it
                    if (it.slot) and (it == self.slots[it.slot]):
                        self.clear_slot(it.slot)
                    del self.bp[it]
            else:
                print('Cant remove item: {}'.format(it.uid))

        def move(self, uid, other):
            '''Move item from this inventory to other.'''
            self.remove(uid)
            other.add(uid)

        def equip(self, uid):
            '''Mark item from inventory as being equipped.'''
            it = Item(uid)
            # check that item in inventory and slot is free to equipping
            if it in self.bp and (it.slot not in self.blocked_slots):
                self.clear_slot(it.slot)
                self.slots[it.slot] = it
                self._add_effects(it)
                self.avatar.update_stats()

        def clear_slot(self, slot):
            '''Move item from slot to backpack.'''
            eq_it = self.slots[slot]
            if eq_it:
                self.slots[slot] = None
                # remove effects for removed item
                self._remove_effects(eq_it)
                self.avatar.update_stats()

        # TODO: in case of more effects will be used, track effects per every item
        def _add_effects(self, item):
            '''Adds effects for equipped item.'''
            if 'two-handed' in item.keywords:
                self.clear_slot('off')
                self.blocked_slots.add('off')

        def _remove_effects(self, item):
            '''Remove effects for given item.'''
            if 'two-handed' in item.keywords:
                # if two handed item is removed, off hand is now free to be equipped
                self.blocked_slots.remove('off')


    class Item(object):
        '''Single inventory item (stateless)'''
        def __init__(self, uid):
            self.uid = uid
            # TODO: maybe all other fields should be just read from all_items, not stored in instance
            self.name = all_items[uid][0]
            self.keywords = set()
            self.slot = None
            # item can have more than one category for now
            self.categories = set()
            self.armour_penalty = 0
            # process keywords from item definition to determine slot, categories etc.
            for word in all_items[uid][1]:
                # TODO: move slot name to separate field in all_items
                # assign slot (only one for every item)
                if word in equip_slots:
                    self.slot = word
                    continue
                if word in armour_weight_penalties:
                    self.armour_penalty += armour_weight_penalties[word]
                if word in item_categories:
                    self.categories.add(word)
                # TODO: add a check for word is being allowed (typo-safety)
                self.keywords.add(word)
            self.descr = all_items[uid][6]
            self.tier = all_items[uid][2]
            self.effects = all_items[uid][3]
            self.img = all_items[uid][5]
            self.small_img = self.img.replace('.png', '_small.png')
            # slot is required
            if (not self.slot) and ('item' not in self.categories):
                raise Exception('Item must have a slot')
            self.buy_value = all_items[uid][4][0]
            self.sell_value = all_items[uid][4][1]

        def __eq__(self, other):
            return (type(self) == type(other)) and (self.uid == other.uid)

        def __hash__(self):
            return hash(self.uid)
