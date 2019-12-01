import math
import random
from src import state_handler

class MCTS:
    def __init__(self,epsilon):
        # initialize everything
        self.epsilon = epsilon # amount of exploration
        self.Q = dict() # total reward of each state
        self.N = dict() # num of visits for each state
        self.children = dict() # children of each state

    def play_turn(self, state, players, valid_actions, num_of_rollouts=5):
        # Do n rollouts before making the action
        # more rollouts means better actions but
        # it takes more time
        for _ in range(num_of_rollouts):
            self._rollout(state, players)
        # Pick action
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

    def _rollout(self, state, players):
        # Calculate one layer
        # A list of states that leads to unexplored or terminal state
        path = self._select(state)
        leaf = path[-1]
        if type(leaf) == str: leaf = eval(leaf)
        # Find all children states
        self._expand(leaf,players)
        print("pre simulate")
        reward = self._simulate(leaf,players)
        print("after simulate")
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
    
    def _expand(self, state, players):
        # Find all children states
        if str(state) in self.children: return
        self.children[str(state)] = state_handler.find_children(state,players)

    def _simulate(self, state, players):
        # Go to random child state until terminal
        while True:
            if state_handler.is_terminal(state):
                reward = state_handler.final_reward(state)
                return reward
            state, players = state_handler.find_random_child(state,players)
    
    def _backpropagate(self, path, reward):
        # Send reward to above state
        for state in reversed(path):
            self.N[str(state)] += 1
            self.Q[str(state)] += reward
    
    def _ucb1_select(self, state):
        # http://www.jmlr.org/papers/volume3/auer02a/auer02a.pdf
        # This helps to balance between exploration and exploitation
        def ucb1(n):
            exploitation = self.Q[n]/self.N[n]
            exploration = self.epsilon*math.sqrt(math.log(self.N[str(state)])/self.N[n]) 
            return exploitation + exploration
        return max(self.children[str(state)], key=ucb1)


def choose_random_action(valid_actions,seed=None):
    if seed: random.seed(seed)
    random_action = valid_actions[random.randint(0,len(valid_actions)-1)]
    action, amount = random_action['action'], random_action['amount']
    if action == "raise": amount = random.randint(amount['min'],amount['max'])
    return action, amount