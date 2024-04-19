# Python Snake Game

Welcome to the Python Snake Game repository! This project is a simple yet engaging implementation of the classic Snake game using Python's `turtle` module. In this game, the player controls a snake that moves around the screen, eating food to grow longer while avoiding the walls and its own tail.

## Prerequisites

To play this game, you will need Python installed on your computer. This game has been tested with Python 3.x. 

## Installation

To start playing the game, you'll first need to clone this repository to your local machine. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/Yoohoo-cf/snake_game
cd snake_game
```

## Running the Game
Navigate to the directory containing the game files and run the game using Python:

```
python3 main.py
```
Ensure that main.py is the script that initiates the game, which utilizes the Screen, Snake, Food, and Scoreboard modules.

## Game Controls
Arrow Up: Move the snake up.
Arrow Down: Move the snake down.
Arrow Left: Move the snake left.
Arrow Right: Move the snake right.

## Game Rules
The snake moves continuously and changes direction based on user input.
Eating food makes the snake longer and increases the player's score.
The game ends if the snake hits the wall or its own tail.
Try to score as high as possible without colliding.

## Modules and Classes
The game is divided into several modules:

1. snake.py: Contains the Snake class that handles the snake's behavior.
2. food.py: Contains the Food class for generating food items on the screen.
3. scoreboard.py: Manages the game's scoring system.
4. main.py: Integrates all other modules and runs the game loop.

## Contributing
Contributions to the project are welcome! You can contribute by improving the game logic, adding new features, fixing bugs, or improving the documentation. Please feel free to fork the repository and submit a pull request.

## Contact
If you have any suggestions or issues, please open an issue in the repository.

Enjoy the game and try to beat your high score!
