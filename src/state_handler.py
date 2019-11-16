from pypokerengine.api.emulator import Emulator
from pypokerengine.engine.action_checker import ActionChecker
import random

def reformat_state(state,hole_card):
    # Changes state got from PyPokerEngine to
    # format this code is supporing
    # TODO: Try remove some information to make the state space smaller
    state['hole_card'] = hole_card
    # str because need to be used as a key
    # can be changed back to dictonary with eval()
    return str(state)

def find_children(state,players):
    # Find all possible states from gives state
    state = eval(state)
    children = []
    own_possible_actions = find_possible_actions(state,players)
    future_info = simulate_actions(state,own_possible_actions)
    for future_state, future_players in future_info:
        opponent_possible_actions = find_possible_actions(future_state,future_players)
        simulated_next_states = simulate_actions(state,opponent_possible_actions)
        for next_state in simulated_next_states:
            if next_state not in children: children.append(next_state)
    return children

def is_terminal(state,reward=False):
    # Check is terminal state and if reward=True return reward
    # FIXME
    if True: return False
    # Return reward if wanted
    if reward: return True, final_reward(state)
    return True

def final_reward(state):
    # Parse reward from state and return
    # FIXME: parse reward
    reward = None
    return reward

def find_random_child(state,players):
    # Find one random state from given state
    
    # TODO: Is it possible to get random child without calculating all of them?
    return random.choice(find_children(state,players))

def find_possible_actions(state,players):
    # Fold, call (0 = check), raise (min-max)
    legal_actions = ActionChecker.legal_actions(players,state['next_player'],state['small_blind_amount'])
    # Split raise
    for i in range(len(legal_actions)):
        item = legal_actions[i]
        if not isinstance(item['amount'],dict): continue
        min = int(item['amount']['min'])
        max = int(item['amount']['max'])
        # Remove this action
        legal_actions = legal_actions[:i-1] + legal_actions[i:]
        # Add all different amounts seperately
        for amount in range(min,max+1):
            legal_actions.append({'action':'raise','amount':amount})
    return legal_actions

def simulate_actions(state,actions):
    # Simulates where the game might go depending what action
    # player takes. Own cards can be used in the end to
    # predict reward but every opponent card option need to be
    # tested.
    # FIXME: simulate actions
    next_states = []
    for action in actions:
        print("do action")
    return next_states