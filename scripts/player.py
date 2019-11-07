# https://github.com/ishikota/PyPokerEngine
from pypokerengine.players import BasePokerPlayer

class MCTSPlayer(BasePokerPlayer):
    # https://github.com/ishikota/PyPokerEngine/blob/master/AI_CALLBACK_FORMAT.md

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def declare_action(self, valid_actions, hole_card, round_state):
        # This will be called everytime the player need to make an action.
        # We can see from history what happened after the last time
        # we made an action.
        
        # valid_actions = possible actions in this state
        # hole_card = own cards
        # round_state = information about the game state
        action, amount = self.algorithm.make_action(state,valid_actions)
        return action, amount