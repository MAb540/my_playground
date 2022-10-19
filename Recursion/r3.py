from array import *


def recur_permut(arr, ds, frequency_arr):
    if len(arr) == len(ds):
        print(ds)
        return

    for i in range(len(arr)):
        if not frequency_arr[i]:
            frequency_arr[i] = True
            ds.append(arr[i])
            recur_permut(arr, ds, frequency_arr)
            ds.remove(arr[i])
            frequency_arr[i] = False


# def recur_permut(arr, ds, frequency_arr, ans_ds):

#     if len(arr) == len(ds):
#         c = ds.copy()
#         ans_ds.append(c)
#         # print(ds)
#         return

#     for i in range(len(arr)):
#         if not frequency_arr[i]:
#             frequency_arr[i] = True
#             ds.append(arr[i])
#             recur_permut(arr, ds, frequency_arr, ans_ds)
#             ds.remove(arr[i])
#             frequency_arr[i] = False


arr = [1, 2, 3]
n = len(arr)
freq_ds = array('i', [0]*n)

ans_ds = []
recur_permut(arr, [], freq_ds)
# recur_permut(arr, [], freq_ds, ans_ds)
# print('ans_ds: ', ans_ds)

# print Permutation appr 2


# def permu(ind, arr):
#     if ind >= len(arr):
#         print(arr)
#         return

#     for i in range(ind, len(arr)):
#         temp = arr[ind]
#         arr[ind] = arr[i]
#         arr[i] = temp

#         permu(ind+1, arr)

#         temp1 = arr[i]
#         arr[i] = arr[ind]
#         arr[ind] = temp1

# arr = [1, 2, 3]
# permu(0, arr)


# n queens problem using recursion

def is_safe(row, col, board, n):

    dup_row = row
    dup_col = col

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    row = dup_row
    col = dup_col

    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row = dup_row
    col = dup_col

    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True


def n_queen(col, board, ans, n):

    if col == n:
        # aa = board.copy()
        print(board)
        # ans.append(aa)
        return

    for row in range(0, n):

        if(is_safe(row, col, board, n)):
            board[row][col] = 'Q'
            n_queen(col+1, board, ans, n)
            board[row][col] = '.'


# def n_queen(col, board, ans, n, l_r, l_d, u_d):
#     if col == n:
#         print(board)
#         return

#     for row in range(0, n):
#         if l_r[row] == 0 and l_d[row + col] == 0 and u_d[n-1 + col - row] == 0:
#             board[row][col] = 'Q'
#             l_r[row] = 1
#             l_d[row + col] = 1
#             u_d[n-1 + col - row] = 1
#             n_queen(col+1, board, [], n, l_r, l_d, u_d)
#             board[row][col] = '.'
#             l_r[row] = 0
#             l_d[row + col] = 0
#             u_d[n-1 + col - row] = 0


n = 4
left_row = [0 for i in range(n)]
upper_diagonal = [0 for i in range(2*n)]
lower_diagonal = [0 for i in range(2*n)]

board = []
ans = []

for i in range(4):
    board.append(['.' for _ in range(4)])


n_queen(0, board, ans, n, left_row, lower_diagonal, upper_diagonal)
