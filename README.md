# Even Semester Project - AI Learns To Play Snake

## Description
This project demonstrates two different approaches to creating an AI for the classic Snake game:
1. **NEAT Python**: NeuroEvolution of Augmenting Topologies, a genetic algorithm for evolving neural networks.
2. **Q-Learning**: A model-free reinforcement learning algorithm.


# Snake - NEAT
## How to run
### Install dependancies
    pip install -r requirements.txt
### Other files required
#### helper.py
- Used to plot Score and Mean Score of the Winner AI by the number of games it has been running for.
#### config-feedforward.txt
- This is used by neat-python library to configure parameters for the NEAT algorithm. Contains various sections for setting up the neural network, evolution process and more.
## Run the code
    python snake_neat.py

# Fitness Function
    SnakeLength
  SnakeLength = Number of fruits it ate
  - Fitness is reduced by 10 if the snake dies, or if the Number of frames that snake has existed for exceeds 100, while its length is less than 5.

# Vision inputs
## This give the snake's neural network a sense of its environment.

 These inputs are:
 
  1. `dirSnack[0]`:Indicates whether the snack is directly ahead.
  
  2. `dirSnack[1]`: Indicates whether the snack is to the left.

  3. `dirSnack[2]`: Indicates whether the snack is to the right.

  4. `dist[0]`: Distance to the nearest obstacle (wall or body) directly ahead.

  5. `dist[1]`: Distance to the nearest obstacle (wall or body) to the left.

  6. `dist[2]`: Distance to the nearest obstacle (wall or body) to the right.







