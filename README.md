# Board-Game

Solution validator for a board game similar to Sudoko
-----------------------------------------------------

The task is to validate a given solution of the puzzle. This solution has been designed using object oriented principles in Python.

Given a board of NxN size, where row and column will be filled by numbers between 1 and n. 
Each number can appear once and only once in each row and each column. Using a 2D list this puzzle has been solved.


Below functions are used in the script :

dimension_check() - Function to check dimension of the board as it should be NxN.

constraints_check() - Function to check constraints like element shouldn't be negative, coordinates shouldn't be greater than boundary size.

adjacent_cells() - Function to check if the elements are adjacent to each other or not which is being compared.

validate_solution() - Function to validate the board.


Instructions below to test the program:

Script Name : udacity_board_game_solution_validator.py

Execution command : python3 udacity_board_game_solution_validator.py
