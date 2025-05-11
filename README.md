# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock Paper Scissors game written in Python.

## Description

This project is a basic implementation of Rock Paper Scissors where the user plays against the computer. The game allows users to choose between rock, paper, or scissors, and the computer makes a random selection. The winner is determined based on the traditional rules:
- Rock crushes scissors
- Paper covers rock
- Scissors cut paper

## Features

- User input validation
- Random computer selection
- Outcome determination (win, lose, or withdraw)
- Option to quit the game

## Requirements

- Python 3.x

## Installation

No additional packages are required for this project. Simply clone or download the repository to your local machine.

```bash
git clone https://github.com/yousefrahimi96/rock-paper-scissors.git
cd rock-paper-scissors
```

## Usage

Run the script using Python:

```bash
python main.py
```

Follow the prompts to play the game:
1. Enter your choice (rock, paper, or scissors)
2. The computer will make its choice
3. The winner will be displayed
4. Enter 'q' to quit the game

## Code Structure

The game is implemented using a class-based approach:

- `RockPaperScissors`: The main class that handles the game logic
  - `__init__()`: Initializes the game
  - `computer_choice()`: Handles the computer's random selection
  - `user_choice()`: Handles user input and validation
  - `decision()`: Determines the winner based on the choices

## Known Issues

- The `choice_list` variable is defined in `__init__` but referenced globally in other methods, which may cause errors.
- Input validation could be improved.

## Future Improvements

- Add a scoring system
- Implement a graphical user interface
- Add additional options (like rock, paper, scissors, lizard, Spock)
- Fix the variable scope issues
- Add unit tests

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## Author

Your Name - [yousefrahimi101@gmail.com](mailto:yousefrahimi101@gmail.com)

## Acknowledgments

- Inspired by the classic game of Rock Paper Scissors