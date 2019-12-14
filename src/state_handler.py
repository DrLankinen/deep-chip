from pypokerengine.api.emulator import Emulator
from pypokerengine.engine.action_checker import ActionChecker
from pypokerengine.engine.hand_evaluator import HandEvaluator
from pypokerengine.engine.card import Card
from pypokerengine.engine.round_manager import RoundManager
from pypokerengine.utils import game_state_utils
from pypokerengine.utils import action_utils
import random

def reformat_state(state,hole_card):
    # TODO: Try remove some information to make the state space smaller
    state['hole_card'] = hole_card
    return state