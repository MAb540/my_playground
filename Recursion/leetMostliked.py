# most asked interview questions leetcode
# question no 1


# def find_indices(ind, ds, target, arr, visited, ans):

#     if ind == len(arr):
#         if target == 0:
#             ans.extend(ds.values())
#         return

#     for i in range(ind, len(arr)):
#         if i != ind and arr[i] == arr[i-1]:
#             continue

#         if visited[i]:
#             continue

#         if arr[i] <= target:
#             visited[i] = True
#             ds[''+str(arr[i])+'_'+str(i)] = i
#             find_indices(i+1, ds, target-arr[i], arr, visited, ans)
#             ds.pop(''+str(arr[i])+'_'+str(i))


# ans = []
# arr = [2, 7, 11, 15]
# arr = [3, 2, 4]
# arr = [3, 3]
# arr = [0, 4, 3, 0]
# visited = [False for _ in range(len(arr))]
# find_indices(0, {}, 0, arr, visited, ans)
# print(ans)


# Three Sum

# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0, 0]
# nums = [-2, 0, 1, 1, 2]
# nums.sort()
# ans = []
# for i in range(len(nums)-1):
#     if i != 0 and nums[i] == nums[i-1]:
#         continue

#     temp = nums[i]
#     left = i + 1
#     right = len(nums)-1

#     while left < right:
#         target = temp + nums[left] + nums[right]
#         if target == 0:
#             ans.append([temp, nums[left], nums[right]])

#             while left < right and nums[left] == nums[left+1]:
#                 left += 1

#             while left < right and nums[right] == nums[right-1]:
#                 right -= 1

#             left += 1
#             right -= 1
#         elif target < 0:
#             left += 1

#         elif target > 0:
#             right -= 1
# print(ans)
# reverse ans integer


# result = 0
# x = 121
# while x != 0:
#     last = x % 10
#     x = x//10

#     result = result * 10 + last

# print(x)
# print(result)

# three sum Problem
# target = 0 or any  value, combinations should be unique
# nums = [1, 2, 3, 4]
# nums = [-1, 2, 1, -4]
# nums.sort()
# ans = []
# total = 1
# for i in range(len(nums)-2):
#     if i != 0 and nums[i] == nums[i-1]:
#         continue

#     temp = nums[i]
#     left = i + 1
#     right = len(nums)-1

#     while left < right:
#         target = temp + nums[left] + nums[right]

#         if target < total:
#             left += 1

#         elif target > total:
#             right -= 1

#         else:
#             ans.append([temp, nums[left], nums[right]])
#             while left < right and nums[left] == nums[left+1]:
#                 left += 1

#             while left < right and nums[right] == nums[right-1]:
#                 right -= 1

#             left += 1
#             right -= 1

# print(ans)

# 3Sum Closest
# nums = [-1, 2, 1, -4]
# nums.sort()
# ans = []
# target = 1
# result = nums[0] + nums[1] + nums[2]
# for i in range(len(nums)-2):
#     if i != 0 and nums[i] == nums[i-1]:
#         continue

#     temp = nums[i]
#     left = i + 1
#     right = len(nums)-1

#     while left < right:
#         total = temp + nums[left] + nums[right]

#         if total < target:
#             left += 1

#         else:
#             right -= 1

#         if(abs(total - target) < abs(result - target)):
#             result = total

# print(result)

# 3Sum closest works on this simpel approach
# arr = [2, 3, -2, 1, 3]
# min_num = 8
# for i in range(len(arr)):
#     if arr[i] < min_num:
#         min_num = arr[i]

# print(min_num)


# 659. Split Array into Consecutive Subsequences

# from collections import Counter

# def split_arr(nums):
#     mapper = Counter(nums)
#     mapper_one = Counter()

#     for v in nums:

#         if mapper[v] == 0:
#             continue

#         mapper[v] -= 1

#         if mapper_one[v-1] > 0:
#             mapper_one[v-1] -= 1
#             mapper_one[v] += 1

#         elif mapper[v+1] != 0 and mapper[v+2] != 0:
#             mapper[v+1] -= 1
#             mapper[v+2] -= 1
#             mapper_one[v+2] += 1

#         else:
#             return False

#     return True


# arr = [1, 2, 3, 3, 4, 4, 5, 5]
# print(split_arr(arr))

# 3. Longest Substring Without Repeating Characters

# my solution , with time complexity of O(n*m) and space complexity of O(n)
# s = 'abcabcbb'
s = "pwwkew"
# s = "bbbbb"
# max_len = 0
# sub_str = ''
# len_of_sub_str = 0
# for v in s:
#     if v in sub_str:
#         if max_len <= len_of_sub_str:
#             max_len = len_of_sub_str
#         sub_str = v
#         len_of_sub_str = 1

#     else:
#         sub_str += v
#         len_of_sub_str += 1

# print(max_len)


# solving using sliding window
left = 0
right = 0
freq_map = {}
length = 0
while right < len(s):

    if s[right] in freq_map:
        left = freq_map[s[right]]+1

    freq_map[s[right]] = right
    length = max(length, right - left + 1)
    right += 1

print(length)
