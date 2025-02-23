# 🧩 Sudoku Solver

## 📌 Description
This Python program solves a given 9x9 Sudoku puzzle using the **Backtracking Algorithm**. The program fills in empty cells (denoted by `0`) while ensuring the Sudoku rules are followed.

## 🔥 Features
- ✅ Finds empty cells automatically.
- ✅ Checks row, column, and 3x3 box constraints.
- ✅ Uses backtracking to find a valid solution.
- ✅ Prints the solved Sudoku puzzle in a structured format.

## 🛠️ How It Works
1. ▶️ The program starts by scanning the Sudoku grid for empty cells.
2. 🔍 It tries placing numbers 1-9 in the empty cell and checks if it's a valid move.
3. 🔄 If a valid number is found, it moves to the next empty cell.
4. ⏪ If no valid number is found, it backtracks to the previous step and tries a different number.
5. 🎉 The process repeats until the Sudoku puzzle is completely solved.

## 📌 Example Usage
```
Solved Sudoku:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
- - -   - - -   - - -
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
- - -   - - -   - - -
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## ⚙️ Requirements
- 🐍 Python 3.x

## 🚀 Possible Enhancements
- 🎨 Implement a graphical interface (GUI) for better visualization.
- ⏳ Optimize the backtracking algorithm for faster performance.
- 📄 Allow users to input custom Sudoku puzzles.

## ✍️ Author
Harshal Patil

