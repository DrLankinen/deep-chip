from src import algorithms
import unittest

class Tests(unittest.TestCase):
    def test_random_action_fold(self):
        self._random_action_helper('fold',0,1)

    def test_random_action_call(self):
        self._random_action_helper('call',0,13)
    
    def test_random_action_raise(self):
        self._random_action_helper('raise',57,42)

    def _random_action_helper(self, target_action, target_amount, seed):
        action, amount = algorithms.choose_random_action([
            {'action': 'fold', 'amount': 0},
            {'action': 'call', 'amount': 0},
            {'action': 'raise', 'amount': {'max':100,'min':50}}
        ],seed)
        self.assertEqual(action,target_action)
        self.assertEqual(amount,target_amount)

if __name__ == '__main__':
    unittest.main()