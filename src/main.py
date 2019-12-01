from src import algorithms
from src import player
from pypokerengine.api.game import setup_config, start_poker

config = setup_config(max_round=1,initial_stack=100,small_blind_amount=5)

config.register_player(name="p1",algorithm=player.FishPlayer("call"))
config.register_player(name="p2",algorithm=player.AlgorithmPlayer(algorithms.MCTS(1)))

game_result = start_poker(config, verbose=1)