# Info : This is a solution validator for a board game similar to Sudoko
# Author Name : Amit Kumar Sahu
# Date : 20-12-2020
# Script Name : udacity_board_game_solution_validator.py
# Execution command : python3 udacity_board_game_solution_validator.py


# Function to check dimension of the board as it should be NxN
def dimension_check(solution) -> bool:
    n_rows = len(solution)

    for i in range(0, n_rows):
        if len(solution[i]) != n_rows:
            return False

    return True


# Function to check constraints like element shouldn't be negative, coordinates shouldn't be greater than boundary size
def constraints_check(constraints, boundary_size) -> bool:
    for greater, smaller in constraints:
        x1, y1 = greater
        x2, y2 = smaller

        if x1 < 0 or x1 >= boundary_size or y1 < 0 or y1 >= boundary_size or x2 < 0 or x2 >= boundary_size or y2 < 0 or y2 >= boundary_size:
            return False

    return True


# Function to check if the elements are adjacent to each other or not which is being compared
def adjacent_cells(x1, y1, x2, y2) -> bool:
    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)

    if diff_x + diff_y == 1:
        return True

    return False


# Function to validate the board
def validate_solution(constraints, solution) -> bool:
    # dimension check done here
    dimension_check_result = dimension_check(solution)
    if not dimension_check_result:
        return False

    size = len(solution)

    # constraints check done here
    constraints_valid = constraints_check(constraints, size)
    if not constraints_valid:
        return False

    for i in range(0, size):
        currentRowSet = set()
        currentColumnSet = set()
        for j in range(0, size):
            # i,j goes row wise
            # j,i goes column wise
            current = solution[i][j]
            currentTransposed = solution[j][i]
            # if the row element is already in the set or does not lie within the range
            if current in currentRowSet or current > size or current <= 0:
                return False
            currentRowSet.add(current)
            # if the column element is already in the set or does not lie within the range
            if currentTransposed in currentColumnSet or currentTransposed > size or currentTransposed <= 0:
                return False
            currentColumnSet.add(currentTransposed)

    for greater, smaller in constraints:
        x1, y1 = greater
        x2, y2 = smaller
        # if the greater element is smaller than supposed to be smaller element
        if not adjacent_cells(x1, y1, x2, y2) or solution[x1][y1] <= solution[x2][y2]:
            return False

    # all validations passed
    return True


# testing done here where the constraints and solution field can be checked for more cases
# note the constraints are 0 indexed
constraints = [((0, 0), (0, 1)), ((1, 2), (2, 2)), ((3, 0), (3, 1)), ((3, 1), (2, 1))]
solution = [[2, 1, 4, 3], [1, 4, 3, 2], [3, 2, 1, 4], [4, 3, 2, 1]]
print(validate_solution(constraints, solution))
