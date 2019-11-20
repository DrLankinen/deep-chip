from pypokerengine.api.emulator import Emulator
from pypokerengine.engine.action_checker import ActionChecker
from pypokerengine.engine.hand_evaluator import HandEvaluator
from pypokerengine.engine.card import Card
import random

def reformat_state(state,hole_card):
    # Changes state got from PyPokerEngine to
    # format this code is supporing
    # TODO: Try remove some information to make the state space smaller
    state['hole_card'] = hole_cardgen_hand_rank_info
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

    # Check if either of the players have folded
    latest_round = state["action_histories"][len(state["action_histories"]-1)]
    for action in latest_round:
        if action["action"] == "FOLD" and reward: return True, final_reward(state)
        if action["action"] == "FOLD" and not reward: return True

    # Check is round_count 3
    state = eval(state)
    if state["round_count"] != 3 and reward: return False, 0
    if state["round_count"] != 3 and not reward: return False

    # If two check and/or call actions in row
    # it's a terminal state
    actions = state["action_histories"]["river"]
    cc_counter = 0
    for action in reversed(actions):
        if action["action"] == "CALL": cc_counter += 1
        else: return
        if cc_counter >= 2 and reward: return True, final_reward(state)
        else cc_counter >= 2 and not reward: return True

    # Return reward if wanted
    if reward: return True, final_reward(state)
    return True

def _decode_card(card):
    f, s = 0, 0
    if card_one[0] == "C": f = 2
    elif card_one[0] == "D": f = 4
    elif card_one[0] == "H": f = 8
    elif card_one[0] == "S": f = 16

    if card_one[1] == "T": s = 10
    elif card_one[1] == "J": s = 11
    elif card_one[1] == "Q": s = 12
    elif card_one[1] == "K": s = 13
    elif card_one[1] == "A": s = 14

def final_reward(state):
    # Parse reward from state and return
    # Check who won with different card options
    wons = []
    
    # create a deck of cards
    all_cards = []
    for num in range(2,15):
        for suit in range(4):
            if suit == 0: suit = "C"
            elif suit == 1: suit = "D"
            elif suit == 2: suit = "H"
            elif suit == 3: suit = "S"
            
            if num == 10: num = "T"
            elif num == 11: num = "J"
            elif num == 12: num = "Q"
            elif num == 13: num = "K"
            elif num == 14: num = "A"

            all_cards.append(str(suit)+str(num))

    own_cards = state['hole_card']
    community_cards = state['community_card']
    open_cards = own_cards + community_cards
    cards_still_in_deck = [x for x in all_cards if x not in open_cards]
    
    for first in range(cards_still_in_deck-1):
        for second in range(first+1,cards_still_in_deck):
            card_one = cards_still_in_deck[first]
            card_two = cards_still_in_deck[second]
            # Opponent cards
            opponent_card_one = Card(_decode_card(card_one))
            opponent_card_two = Card(_decode_card(card_two))
            # Own cards
            own_card_one = Card(_decode_card(own_cards))
            own_card_two = Card(_decode_card(own_cards))
            # Community cards
            community_card_objects = []
            for card in community_cards:
                community_card_objects.append(Card(_decode_card(card)))
            
            # Check values
            opponent_hand_value = HandEvaluator.get_hand_rank_info([opponent_card_one,opponent_card_two],community_card_objects)
            own_hand_value = HandEvaluator.get_hand_rank_info([own_card_one,own_card_two],community_card_objects)
            
            # FIXME
            # EXAMPLE OF get_hand... return:
            # {'hand': {'strength': 'STRAIGHTFLASH', 'high': 2, 'low': 0}, 'hole': {'high': 3, 'low': 2}}

    rewards = []
    for won in wons:
        # Calculate reward
        reward = 0
        action_histories = state["action_histories"]
        for action_round in action_histories:
            for action in action_round:
                # When lose calculate own bets
                if action["uuid"] == PLAYER_UUID and not won: reward += action["amount"]
                # When win calculate opponent's bets
                if action["uuid"] != PLAYER_UUID and won: reward += action["amount"]
        rewards.append(reward)
    # Calculate average of the rewards
    return sum(rewards)/len(rewards)

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