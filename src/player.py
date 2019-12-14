# https://github.com/ishikota/PyPokerEngine
from pypokerengine.players import BasePokerPlayer
from src import state_handler

class AlgorithmPlayer(BasePokerPlayer):
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
        state = state_handler.reformat_state(round_state,hole_card)
        action, amount = self.algorithm.play_turn(state,valid_actions)
        return action, amount
    
    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass

class FishPlayer(BasePokerPlayer):
    
    def __init__(self, action_name="call"):
        self.action_name = action_name

    def declare_action(self, valid_actions, hole_card, round_state):
        for i in range(len(valid_actions)):
            if valid_actions[i]['action'] == self.action_name:
                return valid_actions[i]['action'], valid_actions[i]['amount']
        return valid_actions[0]['action'], valid_actions[0]['amount']
    
    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass


def setup_ai():
    return FishPlayer()
