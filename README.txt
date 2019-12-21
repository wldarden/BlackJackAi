Uses a KNN model to predict blackJack Scores.
Before any model has been made, I simulated 500 games using a random strategy. Then, I parsed these games to evaluate whether
the Descision was good or bad, and used these labeled training data to build the KNN. 

Things I learned:
1. the evaluation was more important, and more complicated, than running and building the model. when I started this, it was just an
Afterthought. But in hindsight, It should have been my main focus. Small tweaks to the evaluation function can drastically
change the success of the ai.
2. A cool thing to do would be to use an evolutionary algorithm to find the best evaluation parameters. but rather than do that here,
Im going to use that information in my next project, connect4.
