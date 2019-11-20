## algorithms.py
This contains different algorithms you can use to play poker.

### Class MCTS
http://www.aifactory.co.uk/newsletter/2013_01_reduce_burden.htm
https://gist.github.com/kjlubick/8ea239ede6a026a61f4d
https://ieeexplore.ieee.org/abstract/document/6203567

## player.py
Layer between PyPokerEngine API and algorithms.py. This is needed because PyPokerEngine will give pretty raw data that we need to formated the right way for the algorithms.


## game_state.py
This contains code that checks state related things like what are the child states.
