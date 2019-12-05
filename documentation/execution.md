## Structure
The project is in src folder. ```algorithms.py``` contains the algorithm and it's easy to add new algorithms. ```main.py``` is where game information is defined. It's possible to add different starting stacks, blind structures, and even more players. ```player.py``` contains the players. Each player uses an algorithm to make the decision. ```state_handler.py``` contains the code that checks things like is_terminal but also simulates the next possible states. All methods there have something to do with state.

## Memory and Time Complexity
MCTS algorithm is much more complex than I'm use to which is why I searched the result instead of calculating it. There was whole paper about this topic which I briefly read while writing project definition. That said the time and memory complexity is the same as it was in project definition.
```
Time complexity: O(mkI)
Memory complexity: O(mk)
```
where *m* number of random children we expand, *k* is the number of times we simulate each child state, and *I* is the number of iterations [1].


## Shortcomings and Improvement Ideas
The current state of the art algorithms also uses neural networks. It's helpful to generate the state because this way relationship between two very close states can be represented better than my current approach (unique id for each state). Neural network could also be helpful in simulation step giving better predictions of possible next states.


## Sources
[1] Yifan Jin & Shaun Benjamin, 2015, "CME 323", Report", viewed 27.11.2019, http://stanford.edu/~rezab/classes/cme323/S15/projects/montecarlo_search_tree_report.pdf
