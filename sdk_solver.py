def is_valid(grid, row, col, num):
    # Check row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check sub-grid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if grid[i][j] == num:
                return False

    return True  # If num is not found in row, col, or subgrid


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):  # Recursive call
                            return True
                        else:
                            grid[row][col] = 0  # Backtrack
                return False  # No valid number found for this cell
    return True  # Sudoku solved

def print_grid(grid):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(grid[row][col], end=" ")
        print()