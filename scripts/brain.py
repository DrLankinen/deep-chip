import math
import random

class MCTS:
    def __init__(self,epsilon):
        # initialize everything
        self.epsilon = epsilon # amount of exploration
        self.Q = dict() # total reward of each state
        self.N = dict() # num of visits for each state
        self.children = dict() # children of each state

    def make_action(self, state, valid_actions):
        # If first time in this state choose random child
        if state not in self.children:
            return choose_random_action(valid_actions)
        
        def value(state):
            # Avoid choosing unvisited nodes
            if self.N[state] == 0: return float("-inf")
            # Average reward
            return self.Q[state] / self.N[state]
        
        return max(self.children[state], key=value)

    def rollout(self, state):
        # Calculate one layer
        # A list of states that leads to unexplored or terminal state
        path = self._select(state)
        leaf = path[-1]
        # Find all children states
        self._expand(leaf)
        reward = self._simulate(leaf)
        self._backpropagate(path, reward)

    # Takes random path from gives state to unexplored or terminal state
    def _select(self, state):
        path = []
        # Continue until finds unexplored or terminal node
        while True:
            path.append(state)
            if state not in self.children or not self.children[state]:
                # Unexplored or terminal
                return path
            # Checks what nodes we haven't explored yet
            unexplored = self.children[state] - self.children.keys()
            # If there is unexplored nodes
            if unexplored:
                # Pop the first
                n = unexplored.pop()
                path.append(n)
                return path
            # Select children node using uct
            state = self._uct_select(state)
    
    def _expand(self, state):
        # Find all children nodes
        if state in self.children: return
        self.children[state] = state.find_children()
    
    def _simulate(self, state):
        invert_reward = True
        while True:
            if state.is_terminal():
                reward = state.reward()
                return 1 - reward if invert_reward else reward
            state = state.find_random_child()
            invert_reward = not invert_reward
    
    def _backpropagate(self, path, reward):
        # Send reward to above
        for state in reversed(path):
            self.N[state] += 1
            self.Q[state] += reward
            reward = 1 - reward
    
    def _uct_select(self, state):
        # http://www.jmlr.org/papers/volume3/auer02a/auer02a.pdf
        # This helps to balance between exploration and exploitation
        def uct(n):
            exploitation = self.Q[n]/self.N[n]
            exploration = self.epsilon*math.sqrt(math.log(self.N[state])/self.N[n]) 
            return exploitation + exploration
        return max(self.children[state], key=uct)


def choose_random_action(valid_actions):
    valid_action = random.randint(0,len(valid_actions)-1)
    action, amount = valid_action['action'], valid_action['amount']
    if action == "raise": amount = random.randint(amount['min'],amount['max'])
    return action, amount
    

