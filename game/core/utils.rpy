# set of utilities and helpers

init python:
    import math
    import random


    def game_date(ts):
        '''Converts timestamp to a game date as a text string'''
        # timestamp offset from start of an year
        ts_offset = 20
        normal_ts = ts + ts_offset
        year = 879 + (normal_ts -1) / 48
        week_names = ('One', 'Two', 'Three', 'Four')
        week_name = week_names[(normal_ts - 1) % 4]
        month_names = ("Hoar's Breath", "Frostskein", "the Slow Thaw", "Arkanan's Bloom", "Tariel's Ascent", "Goldwreath",
            "Layela's Favour", "the Burnished Days", "Stormgather", "Tariel's Descent", "the Long Nights", "Whitefall")
        month_name = month_names[int((normal_ts - 1) // 4) % 12]
        return 'Week {} of {}, {} A.F.'.format(week_name, month_name, year)


    def dice(dn, times=1):
        '''Roll dice "dn" "times" times'''
        res = 0
        for i in range(times):
            # use standard random in dev mode (so it can be rerolled after rollback)
            if config.developer:
                res += random.randint(1, dn)
            else:
                res += renpy.random.randint(1, dn)
        return res


    # TODO: how to test this?
    def check_dc(dc, stat):
        '''Helper for making stat check of current avatar with given difficulty class'''
        res = (dice(20) + avatar.stat_mod(stat)) >= dc
        if res:
            renpy.notify('Check for {} DC{}: Success'.format(stat, dc))
        else:
            renpy.notify('Check for {} DC{}: Fail'.format(stat, dc))
        return (dice(20) + avatar.stat_mod(stat)) >= dc


    def check_stat(dc, stat, show_message=True):
        '''Checks avatar\'s stat at difficulty "dc": dice20 with stat mod and feats'''
        # pure dice roll, can be used for critical success or fail
        roll = dice(20)
        # full skill == base_skill + stat mod
        res = dc <= (roll + avatar.stat_mod(stat))
        # fail on roll one
        if roll == 1:
            res = False
        # succes on roll 20
        elif roll == 20:
            res = True
        if show_message:
            renpy.notify('Check for {} DC{}: {}({} + {})'.format(stat.capitalize(), dc, 'Success' if res else 'Fail', roll, avatar.stat_mod(stat)))
        msgs.show('{{color=#CFD436}}Checking stat {} DC{}: {{b}}{}{{/b}} ({} + {}){{/color}}'.format(stat.capitalize(), dc, 'Success' if res else 'Fail', roll, avatar.stat_mod(stat)))
        return (res, roll)


    def check_skill(dc, skill, show_message=True):
        '''Checks avatar\'s skill at difficulty "dc": dice20 with stat mod and feats'''
        # pure dice roll, can be used for critical success or fail
        roll = dice(20)
        # full skill == base_skill + stat mod
        res = dc <= roll + avatar.skill(skill) + avatar.stat_mod(letter_to_stat[all_skills[skill][1]])
        # fail on roll one
        if roll == 1:
            res = False
        # succes on roll 20
        elif roll == 20:
            res = True
        if show_message:
            renpy.notify('Check for {} DC{}: {}({})'.format(all_skills[skill][0], dc, 'Success' if res else 'Fail', roll + avatar.skill(skill) + avatar.stat_mod(letter_to_stat[all_skills[skill][1]])))
        msgs.show('{{color=#CFD436}}Checking skill {} DC{}: {{b}}{}{{/b}} ({}){{/color}}'.format(all_skills[skill][0], dc, 'Success' if res else 'Fail', roll + avatar.skill(skill) + avatar.stat_mod(letter_to_stat[all_skills[skill][1]])))
        return (res, roll)


    def check_combat(dc, show_message=True):
        '''Checks combat'''
        # pure dice roll, can be used for critical success or fail
        roll = dice(20)
        # full combat roll == d20 + stat mods for strength, vitality and reflexes
        full_roll = roll + avatar.stat_mod('strength') + avatar.stat_mod('vitality') + avatar.stat_mod('reflexes')
        res = dc <= full_roll
        # fail on roll one
        if roll == 1:
            res = False
        # succes on roll 20
        elif roll == 20:
            res = True
        if show_message:
            renpy.notify('Combat check DC{}: {}({})'.format(dc, 'Success' if res else 'Fail', full_roll))
        msgs.show('{{color=#CFD436}}Combat check DC{}: {{b}}{}{{/b}} ({}){{/color}}'.format(dc, 'Success' if res else 'Fail', full_roll))
        return (res, full_roll)


    def roll_stat(stat):
        '''Rolls dice 20 and adds stat_mod for given stat'''
        # pure dice roll, can be checked for critical success or fail
        roll = dice(20)
        res = roll + avatar.stat_mod(stat)
        msgs.show('{{color=#CFD436}}Roll d20 for stat {}: {{b}}{}{{/b}}={}+{}{{/color}}'.format(stat.capitalize(), res, roll, res-roll))
        return (res, roll)


    def roll_skill(skill):
        '''Rolls dice 20 and adds given skill'''
        # pure dice roll, can be checked for critical success or fail
        roll = dice(20)
        res = roll + avatar.skill(skill) + avatar.stat_mod(letter_to_stat[all_skills[skill][1]])
        msgs.show('{{color=#CFD436}}Roll d20 for skill {}: {{b}}{}{{/b}}={}+{}{{/color}}'.format(all_skills[skill][0], res, roll, res-roll))
        return (res, roll)


    def block_saving():
        '''Blocks saving (in navigation screen)'''
        pass
        # if store.saving_allowed:
            # msgs.show('*** Saving the game is {color=#f00}blocked{/color}')
            # store.saving_allowed = False


    def allow_saving():
        store.saving_allowed = True # temp
        # if not store.saving_allowed:
            # msgs.show('*** Saving the game is {color=#0f0}allowed{/color}')
            # store.saving_allowed = True

    def released_fix_rollback():
        '''Fixes rollback for released mode'''
        if not config.developer:
            renpy.fix_rollback()

    def released_block_rollback():
        '''Blocks rollback for released mode'''
        if not config.developer:
            renpy.block_rollback()

    def ratio_color(val1, val2, col_gt='#0f0', col_le='#f00', col_eq='#fff'):
        '''Calculate color to be used for displaing val1 (in ratio widget like val1/val2)'''
        if val1 == val2:
            return col_eq
        elif val1 < val2:
            return col_le
        else:
            return col_gt


    def int_ceil(val):
        '''Return integer rounded up value'''
        return int(math.ceil(val))


    def get_rnd_item(cost_low, cost_high, req_keyword=None):
        '''Adds random item to avatar\'s inventory (buy cost from cost_low to cost_high)'''
        # choose all non-random items in required price range
        items_in_range = [item for item in all_items if (cost_low <= all_items[item][4][0] <= cost_high) and ('non-random' not in all_items[item][1])]
        # if a keyword is required (armour, weapon etc.) choose only items with that keyword
        if req_keyword:
            items_in_range = [item for item in items_in_range if req_keyword in all_items[item][1]]
        if len(items_in_range) > 0:
            item = random.choice(items_in_range)
            avatar.inventory.add(item)
            msgs.show('{{color=#7DF6BD}}Got item: {}{{/color}}'.format(Item(item).name))
            renpy.notify('Got item: {}'.format(Item(item).name))
        else:
            msgs.show('{{color=#E0473D}}!! Failed to add random item in range: {}-{}{{/color}}'.format(cost_low, cost_high))


    def give_item(uid):
        '''Helper function to add an item to avatar\'s inventory and notify'''
        avatar.inventory.add(uid)
        msgs.show('{{color=#7DF6BD}}Got item: {}{{/color}}'.format(Item(uid).name))
        renpy.notify('{} was added to your inventory'.format(Item(uid).name))


    def lose_rnd_item(cost_low, cost_high):
        '''Tries to delete random item from avatar\'s inventory, returns True if successful'''
        items_in_range = [item.uid for item in avatar.inventory.bp if cost_low <= item.buy_value <= cost_high and ('non-random' not in all_items[item.uid][1])]
        if len(items_in_range) > 0:
            uid = random.choice(items_in_range)
            avatar.inventory.remove(uid)
            msgs.show('{{color=#E44238}}Item lost: {}{{/color}}'.format(Item(uid).name))
            renpy.notify('Items lost: {}'.format(Item(uid).name))
            return True
        else:
            msgs.show('{{color=#E0473D}}Player has not items to remove in range: {}-{}{{/color}}'.format(cost_low, cost_high))


    def add_exp(val):
        '''Adds experience to avatar'''
        avatar.exp += val
        msgs.show('{{color=#7DF6BD}}Experience: +{}{{/color}}'.format(val))


    def change_treasury(val):
        '''Adds to or substacts from castle treasury'''
        val = int(val)
        castle.treasury += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Castle treasury: +{} (now {}){{/color}}'.format(val, castle.treasury))
        else:
            msgs.show('{{color=#E44238}}Castle treasury: {} (now {}){{/color}}'.format(val, castle.treasury))


    def change_morale(val):
        '''Changes morale of the castle'''
        castle.morale += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Castle morale: +{} (now {}){{/color}}'.format(val, castle.morale))
        else:
            msgs.show('{{color=#E44238}}Castle morale: {} (now {}){{/color}}'.format(val, castle.morale))


    def change_personal_gold(val):
        '''Adds to or substacts from personal gold of Rowan'''
        val = int(val)
        avatar.gold += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Personal gold: +{} (now {}){{/color}}'.format(val, avatar.gold))
        else:
            msgs.show('{{color=#E44238}}Personal gold: {} (now {}){{/color}}'.format(val, avatar.gold))


    def change_relation(ac, val):
        '''Changes relation with an actor'''
        all_actors[ac].relation += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Relation with {}: +{} (now {}){{/color}}'.format(all_actors[ac].name, val, all_actors[ac].relation))
        else:
            msgs.show('{{color=#E44238}}Relation with {}: {} (now {}){{/color}}'.format(all_actors[ac].name, val, all_actors[ac].relation))


    def change_corruption_actor(ac, val):
        '''Changes corruption of an actor'''
        all_actors[ac].corruption += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Corruption of {}: +{} (now {}){{/color}}'.format(all_actors[ac].name, val, all_actors[ac].corruption))
        else:
            msgs.show('{{color=#E44238}}Corruption of {}: {} (now {}){{/color}}'.format(all_actors[ac].name, val, all_actors[ac].corruption))


    def add_effect(eff):
        avatar.add_effect(eff)
        msgs.show('{{color=#7DF6BD}}+ Status effect: {}{{/color}}'.format(eff))


    def heal_injuries():
        '''Heals all negative effects'''
        avatar.heal_injuries()
        msgs.show('{color=#7DF6BD}All injuries are healed{/color}')


    def heal_wounds(number="ALL"):
        '''Heals all negative effects'''
        avatar.heal(number)
        msgs.show('{{color=#7DF6BD}}Heal wounds: {} (now {}){{/color}}'.format(number, avatar._wounds))


    # TODO: maybe this should be part of the castle code
    def complete_research():
        '''Completes current research normally (regardless of rp spent)'''
        if castle.current_research:
            castle.current_research.on_complete()
            castle.current_research.completed = True
            castle.completed_researches.append(castle.current_research.uid)
            castle._current_research = None


    def av_has_injuries():
        '''Checks if avatar has negative status effects'''
        return len([eff for eff in avatar.effects if eff.kind == 'neg'])


    def change_base_stat(stat_letter, val):
        '''Change one of avatar\'s stats (base)'''
        if stat_letter in letter_to_stat:
            base_stat_name = ''.join(('base_', letter_to_stat[stat_letter]))
            setattr(avatar, base_stat_name, getattr(avatar, base_stat_name) + val)
            if val > 0:
                msgs.show('{{color=#7DF6BD}}{} changed: +{} (now {}){{/color}}'.format(base_stat_name, val, getattr(avatar, base_stat_name)))
            else:
                msgs.show('{{color=#E44238}}{} changed: {} (now {}){{/color}}'.format(base_stat_name, val, getattr(avatar, base_stat_name)))


    def prevent_tile_exploration():
        '''Prevents current tile from being explored'''
        world._prevent_exploration = True
        msgs.show('{color=#CFD436}Current tile will be unexplored{/color}')


    def push_to_previous_tile():
        '''Pushes the player to previous tile'''
        world._push_back = True
        msgs.show('{color=#CFD436}Player will pushed to previous tile{/color}')


    def current_weapon():
        '''Returns name of current weapon'''
        if avatar.inventory.slots['main']:
            return avatar.inventory.slots['main'].name
        else:
            return 'hand'


    def change_research_bonus(val):
        '''Changes research bonus from map resources'''
        castle.research_bonus = max(0, castle.research_bonus + val)
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Castle research bonus: +{} (now {}){{/color}}'.format(val, castle.research_bonus))
        else:
            msgs.show('{{color=#E44238}}Castle research bonus: {} (now {}){{/color}}'.format(val, castle.research_bonus))


    def change_recruitment_bonus(bld_uid, val):
        '''Changes recruitment bonus from map resources, for specific building'''
        castle.recruitment_bonuses[bld_uid] = max(0, castle.recruitment_bonuses.get(bld_uid, 0) + val)
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Castle recruitment bonus ({}): +{} (now {}){{/color}}'.format(castle.buildings[bld_uid].name, val, castle.recruitment_bonuses[bld_uid]))
        else:
            msgs.show('{{color=#E44238}}Castle recruitment bonus ({}): {} (now {}){{/color}}'.format(castle.buildings[bld_uid].name, val, castle.recruitment_bonuses[bld_uid]))


    def change_favor(actor_uid, val):
        '''Changes favor points with given actor'''
        all_actors[actor_uid].favors += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Favor points ({}): +{} (now {}){{/color}}'.format(all_actors[actor_uid].name, val, all_actors[actor_uid].favors))
        else:
            msgs.show('{{color=#E44238}}Favor points ({}): {} (now {}){{/color}}'.format(all_actors[actor_uid].name, val, all_actors[actor_uid].favors))


    def change_prisoners(val):
        '''Changes number of prisoners in the dungeon'''
        castle.buildings['dungeon'].prisoners += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Prisoners: +{} (now {}){{/color}}'.format(val, castle.buildings['dungeon'].prisoners))
        else:
            msgs.show('{{color=#E44238}}Prisoners: {} (now {}){{/color}}'.format(val, castle.buildings['dungeon'].prisoners))


    def take_damage(val):
        '''Add wounds to avatar'''
        avatar.take_damage(val)
        msgs.show('{{color=#E44238}}Damage taken: {} (now {}){{/color}}'.format(val, avatar._wounds))


    def change_mp(val):
        '''Changes current MP.'''
        avatar.mp += val
        if val > 0:
            msgs.show('{{color=#7DF6BD}}Movement points: +{} (now {}){{/color}}'.format(val, avatar.mp))
        else:
            msgs.show('{{color=#E44238}}Movement points: {} (now {}){{/color}}'.format(val, avatar.mp))


    def add_spy_exp(spy_uid, val):
        '''Adds experience to spy'''
        get_object(spy_uid).exp += val
        msgs.show('{{color=#7DF6BD}}Spy exp.: {}: +{} (now {}){{/color}}'.format(get_object(spy_uid).name, val, get_object(spy_uid).exp))


    def capture_resource(map_uid, coords):
        '''Captures map resource'''
        mr = get_map_resource(map_uid, coords)
        mr.capture()
        msgs.show('{{color=#7DF6BD}}Resource captured: {} ({}){{/color}}'.format(mr.name, world.maps[map_uid].name))


    def possible_to_research():
        '''Returns True if there are researches that can be researched right now'''
        return len([rs for rs in castle.researches.values() if (not rs.completed and rs.req_met())]) > 0


    def set_job_class(ac_uid, job_class):
        '''Sets job class for an actor'''
        all_actors[ac_uid].job_state.job_class = job_class
        msgs.show('{{color=#7DF6BD}}{}: new job class: {}{{/color}}'.format(all_actors[ac_uid].name, all_actor_job_classes[all_actors[ac_uid].job_state.job_class]['name']))


    def get_actor_job(ac_uid):
        '''Returns current actor\'s job or None'''
        if hasattr(all_actors[ac_uid], 'job_state'):
            return all_actors[ac_uid].job_state.job
        else:
            return None


    def get_actor_flag(ac_uid, flag_name):
        return all_actors[ac_uid].flags.get(flag_name, 0)


    def set_actor_flag(ac_uid, flag_name, val):
        msgs.show('{{color=#7DF6BD}}{}: flag "{}" changed from {} to {}{{/color}}'.format(all_actors[ac_uid].name, flag_name, get_actor_flag(ac_uid, flag_name), val))
        all_actors[ac_uid].flags.setdefault(flag_name, None)
        all_actors[ac_uid].flags[flag_name] = val


    def change_actor_num_flag(ac_uid, flag_name, val):
        '''Changes numerical flag'''
        set_actor_flag(ac_uid, flag_name, get_actor_flag(ac_uid, flag_name) + val)


    def activate_event(ev_name):
        msgs.show('{{color=#7DF6BD}}Event {} is activated{{/color}}'.format(ev_name))
        set_event_flag(ev_name, '_active', True)


    def deactivate_event(ev_name):
        msgs.show('{{color=#7DF6BD}}Event {} is deactivated{{/color}}'.format(ev_name))
        set_event_flag(ev_name, '_active', False)


    def choose_and_insert_next_event(trigger):
        '''Do standard choosing process for "trigger" and insert first event in current event queue as next event'''
        ev_to_insert = event_manager.choose_one_event(trigger)
        if ev_to_insert:
            event_manager.events.insert(0, ev_to_insert)
            msgs.show('{{color=#7DF6BD}}Inserted next event: {}{{/color}}'.format(ev_to_insert))
        else:
            msgs.show('{{color=#7DF6BD}}No events to insert for trigger {}{{/color}}'.format(trigger))


    def ev_happened(ev_name, count=1):
        '''Returns True if ev_name happend before with run_count == count'''
        return all_events_data[ev_name]['run_count'] >= count


    def ev_exhausted(ev_name):
        '''Returns True if ev_name happend before with run_count >= max count'''
        return all_events_data[ev_name]['run_count'] >= all_events[ev_name].run_count and all_events[ev_name].run_count


    def set_event_timer(ev_name, timer_name, timer_delay):
        '''Sets a timer for ev_name, relplacing old if there is one'''
        msgs.show('{{color=#7DF6BD}}Timer {} on event {} is {} now{{/color}}'.format(timer_name, ev_name, timer_delay))
        all_events_data[ev_name]['timers'][timer_name] = timer_delay


    def get_event_timer(ev_name, timer_name):
        '''Returns timer_name for ev_name, or None'''
        return all_events_data[ev_name]['timers'].get(timer_name)


    def get_event_flag(ev_name, flag_name):
        '''Returns flag value, or None if there is no such flag'''
        return all_events_data[ev_name]['flags'].get(flag_name)


    def set_event_flag(ev_name, flag_name, val):
        '''Sets flag to val for given event'''
        msgs.show('{{color=#7DF6BD}}Flag {} on event {} is {} now{{/color}}'.format(flag_name, ev_name, val))
        all_events_data[ev_name]['flags'].setdefault(flag_name, None)
        all_events_data[ev_name]['flags'][flag_name] = val


    def glossary_add(entry_uid):
        '''Adds entry in entry\'s category and marks category as "new"'''
        journal.glossary_add(entry_uid)


    def glossary_read(category):
        '''Resets "new" flag on given glossary category'''
        journal.glossary_read(category)


    def codex_add(entry_uid):
        '''Adds entry in entry\'s category and topic, and marks topic as "new"'''
        journal.codex_add(entry_uid)


    def codex_read(category, topic):
        '''Resets "new" flag on given codex category/topic'''
        journal.codex_read(category, topic)


    def change_actor_stress(ac_uid, val):
        '''Changes job stress of given actor'''
        old_stress = all_actors[ac_uid].job_state.stress
        all_actors[ac_uid].job_state.stress += val
        all_actors[ac_uid].job_state.stress = max(min(all_actors[ac_uid].job_state.stress, 100), 0)
        msgs.show('{{color=#7DF6BD}}{}: stress {:+} (changed from {} to {}){{/color}}'.format(all_actors[ac_uid].name, val, old_stress, all_actors[ac_uid].job_state.stress))
