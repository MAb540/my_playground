# Binary Watch Problem

# from this import d


# num = 1
# ans = ['%d:%02d' % (h,m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]
# print(ans)

# for h in range(12):
#     for minute in range(60):
#         if (bin(h) + bin(minute)).count('1') == num:
#             print('hour: ,',h,' minute: ',minute)


# def dfs(n,hours,mins,idx,ans):
#     if hours >= 12 or mins > 59:
#         return

#     if n == 0:
#         ans.append(str(mins) )
#         return

#     for i in range(idx,10):
#         if i < 4:
#             dfs(n-1,hours | (1 << i),mins,i+1,ans)
#         else:
#             k = i - 4
#             dfs(n-1,hours,mins | (1<<k),i+1,ans)


# ans = []
# n = 1
# dfs(n,0,0,0,ans)
# print(ans)


# all permutations of a array
# approach 1
# def permu(ind,ds,map,arr,ans):

#     if ind == len(arr):
#         ans.append(ds.copy())
#         return

#     for i in range(len(arr)):

#         if map[i] == True:
#             continue

#         map[i] = True
#         ds.append(arr[i])
#         permu(ind+1,ds,map,arr,ans)
#         map[i] = False
#         ds.remove(arr[i])


# arr = [1,2,3]
# ans = []
# map = [False for _ in range(len(arr))]
# permu(0,[],map,arr,ans)
# print(ans)

# approach 2


# def swap(arr, a, b):
#     arr[a], arr[b] = arr[b], arr[a]

# def permu(ind,arr,ans):
#     if ind == len(arr):
#         ans.append(arr.copy())
#         return

#     for i in range(ind,len(arr)):
#         swap(arr,ind,i)
#         permu(ind+1,arr,ans)
#         swap(arr,i,ind)

# arr = [1,2,3]
# ans = []
# permu(0,arr,ans)

# def permu(ds,frequency_map,arr,ans):
#     if len(ds) == len(arr):
#         ans.append(ds.copy())
#         return

#     for i in frequency_map:

#         if frequency_map[i] > 0:
#             ds.append(i)
#             frequency_map[i] -=1
#             permu(ds, frequency_map, arr, ans)
#             ds.pop()
#             frequency_map[i] +=1


# # arr = [3, 3, 0, 3]
# arr = [2,2,1,1]
# arr.sort()
# frequency_map = {}

# for a in arr:
#     if a in frequency_map:
#         frequency_map[a] +=1
#     else:
#         frequency_map[a] = 1
# ans = []
# permu([], frequency_map,arr, ans)
# print(ans)


# Build Array from Permuatation
# with O(1) space complexity, which means that i will have the mutate the original array
# in a way that i will be able to come up with the required answer

# arr = [0,2,1,5,3,4]
# arr = [5,0,1,2,3,4]

# len_of_arr = len(arr)
# for i in range(len_of_arr):
#     arr[i] = arr[i] + len_of_arr * (arr[arr[i]]%len_of_arr)

# print(arr)

# for i in range(len_of_arr):
#     arr[i] = arr[i]//len_of_arr

# print(arr)

# Island Perimeter
# Iterative Solution

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

# total = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 1:
#             if i == 0 or grid[i-1][j] == 0: ## Up
#                 total += 1

#             if j == 0 or grid[i][j-1] == 0: ## Left
#                 total += 1

#             if i == len(grid)-1 or grid[i+1][j] == 0: ## Down
#                 total += 1

#             if j == len(grid[0])-1 or grid[i][j+1] == 0: ## Right
#                 total += 1
# print(total)

# recursive Solution


# def dfs(i, j, visit):
#     if i >= len(grid) or j == len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
#         return 1

#     if (i, j) in visit:
#         return 0

#     v = (i, j)
#     visit.add(v)
#     prem_up = dfs(i-1, j, visit)
#     prem_left = dfs(i, j-1, visit)
#     prem_down = dfs(i+1, j, visit)
#     prem_right = dfs(i, j+1, visit)

#     return prem_up + prem_left + prem_down + prem_right


# visit = set()
# ans = dfs(0, 1, visit)
# print(ans)

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 1:
#             ans = dfs(i,j,visit)
#             break

# print(ans)


# Reverse Interger (Bit Manipulation)

# x = 123
# def reverse_int(n):

#     result = 0
#     prev = 0
#     while (n != 0):
#         last_int = n%10
#         n = n//10

#         result = result * 10 + last_int

#         if((result - last_int)//10 != prev):
#             return 0

#         prev = result

#     return result

# print(reverse_int(x))


# def reverse_with_max_and_min_int(x):
#     MAX_VALUE = 2147483647
#     MIN_VALUE = -2147483648

#     reverse = 0

#     while x != 0:

#         last = x % 10
#         x = x//10

#         if reverse > MAX_VALUE//10 or (reverse == MAX_VALUE//10 and last > 7):
#             return 0

#         if reverse < MIN_VALUE//10 or (reverse == MIN_VALUE//10 and last < -8):
#             return 0
#         reverse = reverse * 10 + last
#     return reverse

# print(reverse_with_max_and_min_int(-123))
