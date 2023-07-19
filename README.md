# Flappy Bird NEAT

This repository contains an implementation of the popular game Flappy Bird using the NEAT (NeuroEvolution of Augmenting
Topologies) algorithm. NEAT is a genetic algorithm that evolves artificial neural networks to solve complex tasks.

# Description

Flappy Bird is a classic side-scrolling game where the player controls a bird and tries to navigate it through a series
of pipes without colliding with them. In this implementation, instead of manually controlling the bird, we use the NEAT
algorithm to train bird agents that can play the game autonomously.

# Features

- Flappy Bird gameplay: The game provides a faithful recreation of the original Flappy Bird experience, including the
  familiar graphics and mechanics.
- NEAT algorithm: The game uses the NEAT algorithm to evolve neural networks that control the bird's actions. The
  networks learn to navigate through the pipes and improve their performance over generations.
- Visual representation: The game window displays the current generation, score, and highscore, allowing you to track
  the progress of the NEAT algorithm as it trains the bird agents.
- Customizable parameters: The NEAT algorithm's parameters can be adjusted in the configuration file, allowing you to
  experiment with different settings and observe their impact on the learning process.

# Requirements

Make sure you have the following dependencies installed:

- Python 3
- Pygame
- NEAT-Python

You can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

# How to Run

To run the Flappy Bird game with NEAT, follow these steps:

1. Clone this repository:

```
git clone https://github.com/ofmiq/FlappyBirdAI.git
```

2. Open a terminal and navigate to the repository's directory:

```
cd FlappyBirdAI
```

3. Run the main.py file using Python:

```
python main.py
```

This will start the game and the NEAT algorithm. You will see a window displaying the Flappy Bird game, and the
algorithm will train bird agents to play the game.

# NEAT Configuration

The NEAT algorithm's configuration is defined in the config.txt file. You can modify this file to adjust the algorithm's
parameters and experiment with different settings.

# Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a
pull request

# License

This project is licensed under the Unlicense. See
the [LICENSE](https://github.com/ofmiq/FlappyBirdAI/blob/master/LICENSE) file for more details.

