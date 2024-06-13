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
Used to plot Score and Mean Score of the Winner AI by the number of games it has been running for.
#### config-feedforward.txt
This is used by neat-python library to configure parameters for the NEAT algorithm. Contains various sections for setting up the neural network, evolution process and more.
## Run the code
    python snake_neat.py

# Fitness Function
    SnakeLength
  Fitness is reduced by 10 if the snake dies, or if the Number of frames that snake has existed for exceeds 100, while its length is less than 5.







