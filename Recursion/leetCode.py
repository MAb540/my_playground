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

def sub_set_sm(ind, arr, xor, ans):
    if ind == len(arr):
        ans += xor
        return

    sub_set_sm(ind+1, arr, xor, ans)
    sub_set_sm(ind+1, arr, xor ^ arr[ind], ans)


arr = [1, 3]
ans = 0
sub_set_sm(0, arr, 0, ans)
print(ans)
