# mechanics to track all objects with random uid
init python:
    import random

    # all_objects dict will be created at game start
    def __all_objects_init():
        store.all_objects = {}

    config.start_callbacks.append(__all_objects_init)


    def new_uid():
        '''Generates new random uid'''
        uid = random.randint(1, 1000000)
        # if such uid exists already, generate new uid
        while uid in all_objects:
            uid = random.randint(1, 1000000)
        return uid


    def get_object(uid):
        '''Returns object by its uid (for random uids)'''
        return all_objects[uid]


    def del_object(uid):
        '''Removes object from all_objects'''
        del all_objects[uid]
