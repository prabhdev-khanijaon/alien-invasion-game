# Alien Invasion: A Pygame-Based Project
## Overview
Alien Invasion is a 2D arcade-style game built using Python's Pygame library. The player controls a rocket ship to fend off waves of alien fleets. The objective is to shoot and destroy the aliens before they reach the bottom of the screen or collide with the player's ship. This project demonstrates Python programming, game logic design, object-oriented programming, and data tracking through high score systems.

This project also highlights essential skills relevant to a data analyst position, such as data manipulation, real-time tracking (e.g., scores and levels), and problem-solving through code development.

## Skills Demonstrated
### Data Handling:
Tracks and stores high scores using JSON to save the player’s highest score across game sessions.
### Game Logic:
Designed object-oriented architecture using Python to manage game components like aliens, bullets, the ship, and user input.
### Real-Time Tracking:
Implements dynamic tracking of score, levels, and remaining ships, which are continuously updated and displayed to the player.

## Key Features
### Alien Fleet and Ship Control:
Players can move their ship horizontally and fire bullets to destroy incoming alien fleets.

The game progresses through increasingly difficult levels as the aliens move faster with each new wave.

Data Tracking and Visualization:

High scores are stored and displayed, ensuring players can track their progress.

Real-time tracking of player score, level, and remaining ships using a scoreboard system.

This repository also has another version of the 'Alien Invasion' game - 'Sideways Shooter': Where the orientation of the game is sideways. And the difficulty progression and nuances of the game are different.

### Game Logic:
Aliens move in fleets and drop down when they reach the screen edges.

The game ends when the player loses all ships, or aliens reach the bottom of the screen.

## Future Improvements
### New Levels and Alien Behaviors:
Add more diverse alien behaviors, such as random movement patterns, shooting back at the player, or introducing boss levels.
### Power-Ups:
Implement power-ups like rapid-fire, shields, or temporary invincibility to make gameplay more engaging.
### Multiplayer:
Create a multiplayer mode, where two players can cooperate or compete against each other.

## How to Run the Project
### Clone the Repository:
bash

Copy code

git clone https://github.com/your-username/alien-invasion.git

cd alien-invasion
### Install Dependencies:
This project requires Pygame to run. Install the necessary dependencies using:

bash

Copy code

pip install pygame
### Run the Game:
To start playing Alien Invasion, run:

bash

Copy code

python alien_invasion.py

### Controls:
Arrow Keys: Move the ship left and right.

Spacebar: Fire bullets.

'P' Key: Start a new game or resume after pausing.

'Q' Key: Quit the game.





