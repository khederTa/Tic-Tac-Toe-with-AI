# Tic-Tac-Toe with AI

Welcome to the Tic-Tac-Toe with AI repository! This project implements the classic game of Tic-Tac-Toe in Python, enhanced with various artificial intelligence algorithms. Whether you want to play against the computer or watch the AI battle itself, this project provides an engaging experience.

## Features:

- Play against different AI algorithms, including Minimax, Alpha-Beta Pruning, and more.
- Choose your preferred player (X or O) and strategize to beat the AI.
- Easily switch between AI algorithms to observe different playing styles.
- Enhanced with virtual environments to ensure a clean and isolated development environment.

## Getting Started:

1. Install Python and pygame.
2. Set up a virtual environment using venv to isolate your project's dependencies.

## Available Algorithms

- **Minimax:** Minimax is a decision-making algorithm used in two-player games, like Tic-Tac-Toe. It evaluates all possible moves, assuming both players make optimal decisions, and chooses the move that minimizes the maximum possible loss (or maximizes the minimum gain). In the context of Tic-Tac-Toe, it ensures the computer makes the best move possible.

- **MemoMinimax:** MemoMinimax is an extension of the Minimax algorithm that incorporates memoization. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again. In the context of Tic-Tac-Toe, MemoMinimax optimizes the algorithm's performance by avoiding redundant calculations, making it more efficient.

- **AlphaBeta:** Alpha-Beta Pruning is an optimization technique applied to the Minimax algorithm to reduce the number of nodes evaluated in the search tree. It eliminates branches that cannot possibly influence the final decision, making the algorithm more efficient. In the context of Tic-Tac-Toe, Alpha-Beta Pruning speeds up the decision-making process without compromising accuracy.

- **DepthLimited:** Depth-Limited Minimax is a variation of the Minimax algorithm that limits the depth of the search tree. Instead of exploring all possible moves until the end of the game, it only considers moves up to a certain depth. This helps manage computation resources and is particularly useful in scenarios where exploring the entire game tree is impractical or unnecessary.
- **AlphaBetaDepthLimited:** Alpha-Beta Pruning applied to Depth-Limited Minimax. This combination optimizes the search process further by limiting the depth of exploration while employing the pruning technique to eliminate unnecessary branches. In the context of Tic-Tac-Toe, it strikes a balance between accuracy and computational efficiency, making it suitable for games with a large state space.

## Setting Up a Virtual Environment

When developing software with Python, it's essential to use virtual environments to isolate your project's dependencies. Follow these steps to set up a virtual environment using `venv`:

### Install Virtualenv

If you haven't installed `venv` (virtualenv), you can do so by running the following command:

```bash
pip install virtualenv
```

### Create a Virtual Environment

Navigate to your project folder in the terminal and run:

```bash
python<version> -m venv <virtual-environment-name>
```

For example:

```bash
mkdir projectA
cd projectA
python3.8 -m venv env
```

### Activate the Virtual Environment

On Mac, use the following command to activate the virtual environment:

```bash
source env/bin/activate
```

On Windows (CMD or PowerShell), use:

```bash
env\Scripts\activate.bat  # CMD
env\Scripts\Activate.ps1  # PowerShell
```

You should see the virtual environment name in your terminal prompt, indicating that it's activated.

### Verify the Virtual Environment

Check the list of installed packages in the virtual environment:

```bash
pip list
```

Compare it with the list in your global Python environment to confirm isolation.

### Install Project Dependencies

Install the required dependencies for your Tic-Tac-Toe project:

```bash
pip install -r requirements.txt
```

### Create a Requirements File

Generate a requirements.txt file to document your project's dependencies:

```bash
pip freeze > requirements.txt
```

## How to Play:

Run the `runner.py` script with your preferred AI algorithm as a command-line argument. For example:

```bash
python runner.py <algorithm_name>
```

For Example
```bash
python runner.py Memominimax
```

Follow on-screen instructions to choose your player and make moves. Enjoy the game and challenge yourself against the AI!

## Additional Enhancements:

Feel free to explore the code and contribute any additional enhancements or improvements. Share your ideas and collaborate to make this Tic-Tac-Toe project even more exciting!

## Credits:

This project is based on the Harvard CS50 AI course and has been enhanced with additional features and improvements.

## License:

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact Information:

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Email:** [khdertaleb1@gmail.com](mailto:khdertaleb1@gmail.com)

