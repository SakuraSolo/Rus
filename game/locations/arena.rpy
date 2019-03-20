# arena
label arena:
    call screen room_screen('bg28', 'andras room',
        (('Talk', '_operator_talk'),
        ),
        'andras_arena')
    return


label arena_bet_choose_fighter:
    $ arena_bet_fighter_choose_actions = tuple([(name, (ArenaBetChooseFighter(name), SetVariable('room_screen_initial_phrase', 'Want to place a bet on this week’s tournament, eh?'), Jump('arena_bet_choose_amount'))) for name in arena_fighter_names])
    call screen room_screen(None, 'andras displeased',
        (('Leave', Jump('arena')),) + arena_bet_fighter_choose_actions,
        'andras_arena')


label arena_bet_choose_amount:
    $ arena_bet_amount_choose_actions = tuple([(str(val), (ArenaBetChooseAmount(val), SetVariable('room_screen_initial_phrase', 'Okay, I’ll put it in the book.'), Jump('arena'))) for val in arena_bet_amounts])
    call screen room_screen(None, 'andras displeased',
        (('Leave', Jump('arena')),) + arena_bet_amount_choose_actions,
        'andras_arena')


init python:
    arena_fighter_names = ('Bloodhoof',
        'Black Arik',
        'Ozzrak',
        'Krag da Crusher',
        'Ural One-eye',
        'Brokenhorn',
        'Shazzat',
        'Gutrot',
    )


    arena_bet_amounts = (10, 25, 50, 100)


    def __arena_bet_init():
        store.arena_bet = {'fighter': None, 'amount': None}

    config.start_callbacks.append(__arena_bet_init)


    class ArenaBetChooseFighter(Action):
        '''Choose a fighter'''

        def __init__(self, name):
            self.name = name

        def __call__(self):
            arena_bet['fighter'] = self.name


    class ArenaBetChooseAmount(Action):
        '''Choose amount of money to bet'''

        def __init__(self, val):
            self.val = val

        def __call__(self):
            # move bet from avatar's gold to bet
            arena_bet['amount'] = self.val
            avatar.gold -= self.val

        def get_sensitive(self):
            return avatar.gold >= self.val
