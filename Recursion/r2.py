# Combination sum problem
# we can pick a index any number of times
# generate random floating point values
# from random import seed
# from random import random

# seed(1)

# ans_arr = {}


# def combination_sum(ind, target, empty_arr, arr):

#     if ind == len(arr):
#         if target == 0:
#             print("empty_arrr: ", empty_arr)
#             value = random()
#             ans_arr[f'{value}'] = empty_arr
#             print('ans_arr: ', ans_arr)
#         return

#     if arr[ind] <= target:
#         empty_arr.append(arr[ind])
#         combination_sum(ind, target - arr[ind], empty_arr, arr)
#         empty_arr.remove(arr[ind])

#     combination_sum(ind+1, target, empty_arr, arr)


# arr = [2, 3, 6, 7]
# combination_sum(0, 7, [], arr)


# power sum problem
# from collections import deque
# import math


# def power_sum(num, n):

#     stack = deque()
#     result = []
#     upper_bound_sqrt = int(math.sqrt(num))+1
#     upper_bount_pow = math.pow(num, 1/n)

#     # print('upper_bound_sqrt: ', upper_bound_sqrt)
#     # print('upper_bount_pow: ', upper_bount_pow)
#     stack.append((0, 1, []))
#     while stack:
#         total, range_start, nums_list = stack.pop()

#         for i in range(range_start, upper_bound_sqrt):
#             nums_list.append(i)
#             new_total = total + math.pow(i, n)

#             if new_total > num:
#                 break

#             if new_total == num:
#                 result.append(new_total)
#                 break

#             stack.append((new_total, i+1, nums_list))
#             nums_list = nums_list[0:-1]

#     print('result: ', result)


# print(power_sum(4, 2))


# def power_sum_rec(total, pow, num):

#     ans = total - math.pow(num, pow)

#     if ans < 0:
#         return 0

#     if ans == 0:
#         return 1

#     return power_sum_rec(ans, pow, num+1) + power_sum_rec(total, pow, num+1)


# print(power_sum_rec(4, 2, 1))

# write a function that calculated power sum using recursion
# def calculate_power_sum(total, num, pow_to):

#     result = total - math.pow(num, pow_to)

#     if result < 0:
#         return 0

#     if result == 0:
#         return 1

#     return calculate_power_sum(result, num+1, pow_to) + calculate_power_sum(total, num+1, pow_to)
# print(calculate_power_sum(10, 1, 2))


# pick and not pick problem, combination sum and non combination sum
# Combination sum 2
# burte force solution
# def comb_sum_two(ind, target, empty_arr, arr):

#     if ind == len(arr):
#         if target == 0:
#             print('empty_arr: ', empty_arr)
#         return
#     if arr[ind] <= target:
#         empty_arr.append(arr[ind])
#         comb_sum_two(ind+1, target - arr[ind], empty_arr, arr)
#         empty_arr.remove(arr[ind])

#     comb_sum_two(ind+1, target, empty_arr, arr)


# def comb_sum_two(ind, target, empty_arr, arr, abc):

#     if target == 0:
#         print('empty_arr: ', empty_arr)
#         abc.append(empty_arr.copy())
#         return

#     for i in range(ind, len(arr)):
#         if i > ind and arr[i] == arr[i-1]:
#             continue
#         if(arr[i] > target):
#             break

#         empty_arr.append(arr[i])
#         comb_sum_two(i+1, target-arr[i], empty_arr, arr, abc)
#         empty_arr.remove(arr[i])

# arr = [10, 1, 2, 7, 6, 1, 5]
# arr = [1, 1, 1, 2, 2]
# arr.sort()

# abc = []
# comb_sum_two(0, 4, [], arr, abc)
# print(abc)

# Super Digit Problem

# def superDigit(n, k):
#     temp = n * k
#     def sum_digi(nn):
#         if len(nn) == 1:
#             return nn

#         sum = 0
#         for i in range(len(nn)):
#             sum += int(nn[i])

#         return sum_digi(str(sum))

#     ans = sum_digi(temp)

#     return ans
# print(superDigit('123', 3))

# time complexity will of of 2 power n and log of 2 power n
# def sub_set(ind, summ, arr, sum_arr):
#     if ind >= len(arr):
#         sum_arr.append(summ)
#         sum_arr.sort()
#         return

#     sub_set(ind+1, summ + arr[ind], arr, sum_arr)
#     sub_set(ind+1, summ, arr, sum_arr)


# arr = [2, 3]
# sum_arr = []
# sub_set(0, 0, arr, sum_arr)
# print(sum_arr)

# Subset || problem

# def all_possible_sub_sets(ind, empty_arr, arr):
#     print('empty_arr: ', empty_arr)

#     for i in range(ind, len(arr)):
#         if i != ind and arr[i] == arr[i-1]:
#             continue

#         empty_arr.append(arr[i])
#         all_possible_sub_sets(i+1, empty_arr, arr)
#         empty_arr.remove(arr[i])

# arr = [1, 2]
# all_possible_sub_sets(0, [], arr)


# arr = [2, 3, 5]

# res = 5
# ans = 0

# for i in range(len(arr)):
#     # isFound = False
#     for j in range(i+1, len(arr)):
# if i + j == res:
# ans = i + j
# isFound = True
# print('i: ', arr[i], ' j: ', arr[j])
# break
# if isFound:
#     break
