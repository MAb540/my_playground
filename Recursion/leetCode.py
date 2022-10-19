# def calc(initial, x, n):

#     if n < 0:
#         positive_pow = (n * n) + n
#         return 1/calc(initial, x, positive_pow)

#     if n == 0:
#         return 1.0

#     if n == 1:
#         return x

#     if n > 1:
#         x = float(x * initial)
#         return calc(initial, x, n-1)


# def myPow(x: float, n: int) -> float:
#     initialVal = x
#     return calc(initialVal, x, n)


# def myPow(x, n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return x

#     if n < 0:
#         return 1/x * myPow(1/x, -(n+1))
#     else:
#         y = myPow(x, n/2)
#         if (n % 2 == 0):
#             return y * y
#         return x * y * y

# print(myPow(2, 4))


# def pow(x, n):

#     if n == 0:
#         return 1

#     temp = pow(x, n//2)

#     if n % 2 == 0:
#         return temp * temp

#     return x * temp * temp


# def myPow(x, n):

#     if x == 1 or n == 1:
#         return x

#     if n > 1:
#         return pow(x, n)

#     return 1/pow(x, n * -1)


# print(myPow(2, -2))


# xor subset sum with backtracking

# from functools import reduce

# def sum_ofsubset_xor(ind, ds, arr, ans):

#     if ind >= len(arr):
#         # print(ds)
#         if len(ds) == 0:
#             ans.append(0)
#             return
#         res = reduce(lambda x, y: x ^ y, ds.copy())
#         ans.append(res)
#         return

#     sum_ofsubset_xor(ind+1, ds, arr, ans)
#     ds.append(arr[ind])

#     sum_ofsubset_xor(ind+1, ds, arr, ans)
#     ds.remove(arr[ind])


# arr = [1, 3]
# ans = []
# sum_ofsubset_xor(0, [], arr, ans)
# print(sum(ans))

# xor subset sum without backtracking

# def sub_set_sm(ind, arr, xor, ans):
#     if ind == len(arr):
#         ans += xor
#         return

#     sub_set_sm(ind+1, arr, xor, ans)
#     sub_set_sm(ind+1, arr, xor ^ arr[ind], ans)


# arr = [1, 3]
# ans = 0
# sub_set_sm(0, arr, 0, ans)
# print(ans)


# def recur_subset(ind, ds, nums, ans):

#     c = ds.copy()
#     ans.append(c)

#     for i in range(ind, len(nums)):

#         if i != ind and nums[i] == nums[i-1]:
#             continue

#         ds.append(nums[i])
#         recur_subset(i+1, ds, nums, ans)
#         ds.remove(nums[i])

# nums = [1, 2]
# ans = []
# recur_subset(0, [], nums, ans)


# def all_comb(ind, ds, n, ans, k):
#     if k == 0:
#         d = ds.copy()
#         ans.append(d)
#         return

#     for i in range(ind, n+1):
#         ds.append(i)
#         all_comb(i+1, ds, n, ans, k-1)
#         ds.remove(i)

#         # when i = 1  f(2,[1],n,ans,1),
#         # when i = 2  f(3,[2],n,ans,1),
#         # when i = 3  f(4,[3],n,ans,1),
#         # when i = 4  f(5,[4],n,ans,1)


# n = 4
# ans = []
# k = 2
# all_comb(1, [], n, ans, k)
# print(ans)

# def all_combinations(n, k):
#     if n < k:
#         return []

#     curr = [0 for _ in range(k)]

#     res = []
#     i = 0
#     while i >= 0:
#         curr[i] += 1

#         if(curr[i] > n):
#             i -= 1

#         elif i == k - 1:
#             res.append(curr.copy())
#         else:
#             i += 1
#             curr[i] = curr[i-1]

#     print(res)
# all_combinations(4, 2)


# Iterator for Combination

# def all_combos(ind, ds, charas, k, ans):
#     if ind == len(charas):
#         if len(ds) == k:
#             ans.append(str(ds))
#         return

#     ds += charas[ind]
#     all_combos(ind+1, ds, charas, k, ans)

#     ds = ds[0:len(ds)-1]
#     all_combos(ind+1, ds, charas, k, ans)


# ans = []
# k = 2
# charas = 'abc'
# all_combos(0, '', charas, k, ans)
# print(ans)


# Combination Sum 2

def comb_sub_two(ind, ds, arr, target, ans):

    if target == 0:
        ans.append(ds.copy())
        return

    for i in range(ind, len(arr)):

        if i != ind and arr[i] == arr[i-1]:
            continue

        if arr[i] <= target:
            ds.append(arr[i])
            comb_sub_two(i+1, ds, arr, target - arr[i], ans)
            ds.remove(arr[i])


arr = [1, 2, 2, 2, 5]
ans = []
target = 5
comb_sub_two(0, [], arr, target, ans)

print(ans)
