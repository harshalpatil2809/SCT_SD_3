#This function search for the 0 (Empty)
def find0(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # Row, Col
    return None  # No empty cells found

#This Function is use to check the grid,row,boxes
def valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

#This programm use Backtracking Algorithem
def solve(grid):
    find = find0(grid)
    if not find:
        return True  # Puzzle is solved
    else:
        row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):  # Recursively try to solve
                return True

            grid[row][col] = 0  # Backtrack: reset if it doesn't lead to a solution

    return False  # No valid number found for this cell

#This Function prints the solved sudoku
def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - -   - - -   - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            print(grid[i][j], end=" ")

        print("")


# Example Sudoku puzzle (you can modify this)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(grid):
    print("Solved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")