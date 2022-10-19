import random

# [[random.randint(0, 9) for i in range(3)] for i in range(3)]

puzzle = """043080250
            600000000
            000001094
            900004070
            000608000
            010200003
            820500000
            000000005
            034090710"""

# puzzle = """043080250
#             600000000
#             000001094"""

pp = ''.join(puzzle.replace('\n', '').split(' '))


three_by_three = []

for i in range(len(pp)+1):

    if i == 0:
        pass

    elif i % 9 == 0:
        sub_str_of_nine = pp[i-9:i].strip()
        three_by_three.append(list(sub_str_of_nine))

        # for j in range(len(sub_str_of_nine)+1):

        #     if j == 0:
        #         pass

        #     elif j % 3 == 0:
        #         sub_str = sub_str_of_nine[j-3:j]
        #         three_by_three.append(list(sub_str))

# print(three_by_three)
# print(len(three_by_three))


nine_by_nine = [
    [5, 3, '.', 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    ['.', 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, '.', 4, 8, '.', 6],
    [9, 6, '.', 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

boards = [nine_by_nine]


# print('boards: ', boards)
# print('len of boards: ', len(boards))


def isSafe(row, col, char, board):

    for i in range(9):

        if board[i][col] == char:
            return False

        if board[row][i] == char:
            return False

        if board[3 * (row//3) + i//3][3 * (col//3) + i % 3] == char:
            return False

    return True


def sudokuSolver(board, ds):

    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] == '.'):

                for char in range(1, 10):

                    if isSafe(row, col, char, board):
                        board[row][col] = char
                        if(sudokuSolver(board, ds) == True):
                            a = board.copy()
                            ds.append(a)
                            return True
                        board[row][col] = '.'

                return False

    return True


def sudokuSol(boards):
    ans = []
    for board in boards:
        sudokuSolver(board, ans)

    for a in ans:
        print(a, end='\n\n')


sudokuSol(boards)
