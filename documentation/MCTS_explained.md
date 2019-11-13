MCTS contains four different steps:

## Select (current state)
Get children states and if there is a state that is never visited choose it, if none of the children have been visited choose randomly, and if all visited choose the next state using UCB1. Continue until finds a state that is not visited or terminal.

## Expand (unexplored state from previous step = leaf)
Save all possible next state options to the leaf state. There are roughly (own_possible_actions * opponent_possible_actions - duplicates) different children.

## Simulate (unexplored state from previous step = leaf)
Continue from given state by taking random actions. This is simulation so we don't really take the actions. The idea is that we test all our own actions and then all possible opponent actions. Then in the terminal state we give all possible cards for the opponent and average over those.

## Backprobagate (leaf)
Update values to all ancestor states.

In summary the idea of MCTS is that we take actions that we know gives us the most reward. Then if we face a point where we don't know what is the value of certain state we do simulations to approximate each child state value to choose the best. The more time and computing power available means that it's possible to make more simulations and get better predictions.
