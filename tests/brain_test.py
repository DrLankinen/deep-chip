from scripts import brain
import unittest

class Tests(unittest.TestCase):
    def test_random_action(self):
        action, amount = brain.choose_random_action([
            {'action': 'fold', 'amount': 0},
            {'action': 'call', 'amount': 0},
            {'action': 'raise', 'amount': {'max':100,'min':50}}
        ])
        self.assertEqual(action,'fold')


if __name__ == '__main__':
    unittest.main()