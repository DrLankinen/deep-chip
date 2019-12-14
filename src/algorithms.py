import math
import random
from pypokerengine.utils import card_utils
from pypokerengine.engine import card
import pickle
import os

class MCTS:
    def __init__(self,epsilon,load=None):
        # initialize everything
        self.epsilon = epsilon # amount of exploration
        self.Q = dict() # total reward of each state
        self.N = dict() # num of visits for each state
        self.children = dict() # children of each state
        if load:
            if load == True: path = "./saved/"
            else: path = load
            if not os.path.exists(path): return
            self.Q,self.N,self.children = pickle.load(open(path+"data.pkl","rb"))

    def play_turn(self, state, valid_actions, num_of_rollouts=5):
        for _ in range(num_of_rollouts):
            self._rollout(state)
        
        return self._pick_action(state, valid_actions)

    def _pick_action(self, state, valid_actions):
        # If first time in this state choose random child
        if str(state) not in self.children:
            return choose_random_action(valid_actions)
        
        def value(state):
            # Avoid choosing unvisited nodes
            if self.N[str(state)] == 0: return float("-inf")
            # Average reward
            return self.Q[str(state)] / self.N[str(state)]
        
        return max(self.children[str(state)], key=value)

    def _rollout(self, state):
        # Calculate one layer
        # A list of states that leads to unexplored or terminal state
        path = self._select(state)
        leaf = path[-1]
        if type(leaf) == str: leaf = eval(leaf)

        hole_cards, community_cards = self._change_card_format(leaf)
        reward = card_utils.estimate_hole_card_win_rate(1,2,hole_cards,community_cards)

        self._backpropagate(path, reward)

    # Takes random path from gives state to unexplored or terminal state
    def _select(self, state):
        path = []
        # Continue until finds unexplored or terminal state
        while True:
            path.append(str(state))
            if str(state) not in self.children or not self.children[str(state)]:
                # Unexplored or terminal
                return path
            # Checks what states we haven't explored yet
            unexplored = self.children[str(state)] - self.children.keys()
            # If there is unexplored states
            if unexplored:
                # Pop the first
                n = unexplored.pop()
                path.append(n)
                return path
            # Select children state using uct
            state = self._ucb1_select(state)

    def _change_card_format(self, leaf):
        hole_cards = leaf['hole_card']
        for i, c in enumerate(hole_cards):
            hole_cards[i] = card.Card(REVERSE_SUIT_MAP[c[0]],REVERSE_RANK_MAP[c[1]])
        
        community_cards = leaf['community_card']
        for i, c in enumerate(community_cards):
            community_cards[i] = card.Card(REVERSE_SUIT_MAP[c[0]],REVERSE_RANK_MAP[c[1]])
        
        return hole_cards, community_cards
    
    def _backpropagate(self, path, reward):
        # Send reward to above state
        for state in reversed(path):
            if str(state) not in self.N: self.N[str(state)] = 0
            self.N[str(state)] += 1
            if str(state) not in self.Q: self.Q[str(state)] = 0
            self.Q[str(state)] += reward
    
    def _ucb1_select(self, state):
        # http://www.jmlr.org/papers/volume3/auer02a/auer02a.pdf
        # This helps to balance between exploration and exploitation
        def ucb1(n):
            exploitation = self.Q[n]/self.N[n]
            exploration = self.epsilon*math.sqrt(math.log(self.N[str(state)])/self.N[n]) 
            return exploitation + exploration
        return max(self.children[str(state)], key=ucb1)
    
    def save(self, path=None):
        if path is None: path = "./saved/"
        if not os.path.exists(path): os.makedirs(path)
        pickle.dump([self.Q,self.N,self.children],open(path+"data.pkl","wb"))


def choose_random_action(valid_actions,seed=None):
    if seed: random.seed(seed)
    random_action = valid_actions[random.randint(0,len(valid_actions)-1)]
    action, amount = random_action['action'], random_action['amount']
    if action == "raise": amount = random.randint(amount['min'],amount['max'])
    return action, amount


REVERSE_RANK_MAP = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14
}

REVERSE_SUIT_MAP = {
    'C' : 2,
    'D' : 4,
    'H' : 8,
    'S' : 16
}