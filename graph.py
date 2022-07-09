


n = 5

arr = [[0 for j in range(n+1)] for _ in range(n+1)]


arr_values = [[1,2],[2,4],[2,3],[1,3],[3,4],[1,5],[5,3]]

for v in arr_values:
    arr[v[0]][v[1]] = 1
    arr[v[1]][v[0]] = 1

for a in arr:
    print(a)

# hour Glass Problem
# arr = [
#         [-9,-9,-9,1,1,1],
#         [0,-9,0,4,3,2],
#         [-9,-9,-9,1,2,3],
#         [0,0,8,6,6,0],
#         [0,0,0,-2,0,0],
#         [0,0,1,2,4,0],
#     ]

# max_sum = 0
# max_sum_arr = []
# for i in range(len(arr)-2):
#     for j in range(len(arr)-2):

#         first_row_sum = 0
#         second_row_sum = 0
#         third_row_sum = 0

#         for k in range(3):
#             first_row_sum += arr[i][j+k]
            
#             if k == 1:
#                 second_row_sum += arr[i+1][j+k]
#             third_row_sum += arr[i+2][j+k]
        
#         max_sum_arr.append(first_row_sum + second_row_sum + third_row_sum)


# print(max(max_sum_arr))




