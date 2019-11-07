This week I started writing code. I created all files I'm probably going to need and structured them in a way it makes sense. I also implemented most of the MCTS but it still needs some fixing to work. I also added tests to one test to random action selecting function. I learned how PyPokerEngine works and how I'm going to use it.

I'm already much further than I expected but there are still somethings that are unsure and might cause a lot of work.

This week I learned how to structure Python project, how to do tests, how to do test coverage report, and how MCTS works in practice.

When I was implementing MCTS I notice that it's designed to perfect information games and poker is imperfect information game which means that I need to make some modifications. I first expect it to work without any modifications but now I need to study how other people make it work. I found some papers about the topic which I'm going to study more the next week. I'm also not sure how to define state. At least what I remember one technique to reduce the number of states is to put for example raise actions into batches like often real poker players do. So instead of raising some random integer the raise is some part of the pot like half. This is how pro poker players almost always raise so it should also work in this.

The next week I will make the code work on poker. I will also implement more tests to cover the full code. I also try to find time to test the algorithm by training it over night against itself.

I spent 15 hours this week
