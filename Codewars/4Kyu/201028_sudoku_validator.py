import unittest


def valid_check(lst):
    check = 1
    lst = sorted(lst)
    for n in lst:
        if check != n:
            return False
        else:
            check += 1
    return True
    
def valid_solution(board):
    for line in board:  # Horizon line
        if not valid_check(line):
            return False

    for i in range(9):
        if not valid_check([board[j][i] for j in range(9)]):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []
            for x in range(i, i + 3):
                for n in board[x][j : j + 3]:
                    tmp.append(n)
            if not valid_check(tmp):
                return False 
    return True

valid_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

invalid_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
               [6, 7, 2, 1, 9, 0, 3, 4, 9],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]]

class Test_Sudoku_Validator(unittest.TestCase):
    def test_valid_solution_with_valid_board(self):
        self.assertEqual(valid_solution(valid_board), True)
    def test_valid_solution_with_invalid_board(self):
        self.assertEqual(valid_solution(invalid_board), False)


if __name__ == '__main__':
    unittest.main()
    