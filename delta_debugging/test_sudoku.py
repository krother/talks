
from sudoku import solve_sudoku
import random as r


def test_sudoku(constraints):
    try:
        status, solution = solve_sudoku(constraints)
        return "PASS" if status == 'Optimal' else "FAIL"
    except:
        return "FAIL"


def create_random_constraints():
    constraints = []
    for i in range(r.randint(1, 80)):
        x = r.randint(1, 9)
        y = r.randint(1, 9)
        n = r.randint(1, 9)
        constraints.append((x, y, n))
    return constraints

if __name__ == '__main__':
    #constraints = []
    #constraints = [(1,1,9)]
    constraints = [(1,1,9), (4,2,9)]
    #constraints = [(1,1,9), (2,2,9)]
    print(test_sudoku(constraints))
