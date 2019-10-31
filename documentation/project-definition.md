# Project Definition

## What algorithms and data structures you use in the project?
Monte Carlo tree search (MCTS)
MCTS is a pretty simple and easy to run algorithm which however achieved pretty good results even in the current century. The Monte Carlo methods use the randomness of deterministic problems that might be impossible to solve in other ways. These are used in physics and mathematics. The intuition of MCTS is that the algorithm plays many rounds selecting actions at some level randomly. Then the results of the games are used to update each node of the game tree [5].

In its current format, MCTS was released in 2006 to play GO [5]. Besides perfect information games, it also works games like bridge and poker where the algorithm doesn't get all information about the game like opponents' cards [5].

## What problem you solve and why you chose the algorithm?
I will create a Texas holdem no-limit playing program. I chose this problem because I like poker and it's much more complex than tic-tac-toe or even chess. I didn't wanted to use some simple algorithms because I knew that this is pretty hard problem and with those it might be impossible to see any results. Texas holdem no-limit has 10^160 different decision points (or states) [3]. This means that it's around as complex as GO. The goal of this project is to create a bot that learns to play Texas holdem at the beginner level. I would be happy to see even a few good moves from the bot in common situations.

## What kind of inputs the program gets and how these are used?
I'm going to use PyPokerEngine[1] that offers Texas holdem no-limited environment to train the program. After training, I will use their GUI to play against the bot. Texas holdem is a poker game where each player gets two cards, there will be 5 cards in the river, and then there are 4 different betting rounds. No-limit version means that there is no limit on how much each player can bet. Limit versions have much fewer states but this is the most popular version probably because of the exciting all-in moves in big tournaments. More about Texas Holdem: https://en.wikipedia.org/wiki/Texas_hold_%27em

## Targeted time and memory complexity
Time complexity: O(mkI)
Memory complexity: O(mk)
where m number of random children we expand, k is the number of times we simulate each child state, and I is the number of iterations [2].

This obviously means that it's not going to solve the whole game. There have been some good algorithms that have almost solved the whole Texas holdem no-limit. At least what I found no algorithm solves the game fully but at least achieves so good results that humans can't beat them in the long run. Right now (2019) the current best program is called Libratus [4] developed by Noam Brown and Tuomas Sandholm from Carnegie Mellon University.

## Sources
[1] https://ishikota.github.io/PyPokerEngine/
[2] Yifan Jin & Shaun Benjamin, 2015, "CME 323", Report", viewed 30.10.2019, http://stanford.edu/~rezab/classes/cme323/S15/projects/montecarlo_search_tree_report.pdf
[3] https://youtu.be/qndXrHcV1sM
[4] The Gradient, 2018, Libratus: the world's best poker player, https://thegradient.pub/libratus-poker/
[5] Wikipedia, 2019, Monte Carlo tree search, https://en.wikipedia.org/wiki/Monte_Carlo_tree_search