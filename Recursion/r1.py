# print name till n times

# def printN(i, n):
#     if i > n:
#         return
#     print(n)
#     printN(i+1, n)

# printN(1, 5)


# def printN(n):
#     if n < 1:
#         return
#     print(n)
#     printN(n-1)

# printN(4)


# sum of first n numbers
# parameterised way
# def sumToN(i, sum):
#     if i < 1:
#         return sum
#     return sumToN(i-1, sum+i)

# print(sumToN(3, 0))

# functional way
# def sumToN(i):

#     if i == 0:
#         return 0
#     return i + sumToN(i-1)

# print(sumToN(3))

# Factorial of n
# def factN(n):
#     if n == 1:
#         return n

#     return n * factN(n-1)
# print(factN(4))

# reverse a array
arr = [1, 2, 3, 4, 5, 6]

# by two pointer
# for i in range(int(len(arr)/2)):
#     p1 = i
#     p2 = len(arr) - i - 1
#     arr[p1], arr[p2] = arr[p2], arr[p1]
# print(arr)


# def reverseArr(arr, l, r):
#     if l >= r:
#         return arr

#     arr[l], arr[r] = arr[r], arr[l]
#     return reverseArr(arr, l+1, r-1)

# arr = [1, 2, 3, 4, 5]
# print(reverseArr(arr, 0, len(arr)-1))


# def reverseArr(arr, l):
#     if l == int(len(arr)/2):
#         return arr

#     arr[l], arr[len(arr)-l-1] = arr[len(arr)-l-1], arr[l]
#     return reverseArr(arr, l+1)

# arr = [1, 2, 3, 4, 5, 6]
# print(reverseArr(arr, 0))


# check if a string in palindrome
# with loop
# def checkPalinDrome(string):
#     isPalinDrome = True
#     for i in range(int(len(string)/2)):
#         if string[i] == string[len(string)-i-1]:
#             isPalinDrome = True
#         else:
#             isPalinDrome = False
#             break

#     return isPalinDrome


# With Recursion

# def checkPalinDrome(string, l):
#     if l > int(len(string)/2):
#         return True

#     if string[l] == string[len(string)-l-1]:
#         return checkPalinDrome(string, l+1)

#     return False


# print(checkPalinDrome('adfdda'))


# Fibonacci
# using loop

# def fibo(n):
#     # first fibonacci number
#     n1 = 0
#     # second fibonacci number
#     n2 = 1

#     nextTerm = n1 + n2
#     for i in range(3, n):
#         print(nextTerm)
#         n1 = n2
#         n2 = nextTerm
#         nextTerm = n1 + n2

# fibo(5)


# def fibo(n):

#     arr = [0, 1]
#     for i in range(2, n):
#         arr.append(arr[i-1] + arr[i-2])

#     print(arr)
#     return arr[n-1]

# print(fibo(6))


# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)
# print(fibo(3))


# printing subsequences of an array
# def print_sub_sequence(ind, empty_arr, arr):

#     if ind >= len(arr):
#         print('empty_arr: ', empty_arr)
#         return

#     empty_arr.append(arr[ind])
#     print_sub_sequence(ind+1, empty_arr, arr)
#     empty_arr.remove(arr[ind])
#     print_sub_sequence(ind+1, empty_arr, arr)


# arr = [3, 1]
# print(print_sub_sequence(0, [], arr))

# printing subsequences of an array that is equal to sum
# def sum_sub_sequence(i, empty_arr, arr, sum_result):

#     if i >= len(arr):
#         if sum(empty_arr) == sum_result:
#             print('empty_arr: ', empty_arr)
#             return True
#         return False
#     empty_arr.append(arr[i])
#     sum_sub_sequence(i+1, empty_arr, arr, sum_result)
#     empty_arr.remove(arr[i])
#     sum_sub_sequence(i+1, empty_arr, arr, sum_result)


# arr = [1, 2, 1]
# sum_result = 2
# sum_sub_sequence(0, [], arr, sum_result)


# # Technique to print only one ans
# def sum_sub_sequence(i, empty_arr, arr, sum_result):

#     if i >= len(arr):
#         if sum(empty_arr) == sum_result:
#             print('empty_arr: ', empty_arr)
#             return True
#         return False
#     empty_arr.append(arr[i])
#     pick_result = sum_sub_sequence(i+1, empty_arr, arr, sum_result)
#     if(pick_result == True):
#         return True

#     empty_arr.remove(arr[i])
#     not_pick_result = sum_sub_sequence(i+1, empty_arr, arr, sum_result)
#     if (not_pick_result == True):
#         return True

#     return False


# arr = [1, 2, 1]
# sum_result = 2
# sum_sub_sequence(0, [], arr, sum_result)


# Technique to give the no of count
# def sum_sub_sequence(i, empty_arr, arr, sum_result):

#     if i >= len(arr):
#         if sum(empty_arr) == sum_result:
#             return 1
#         return 0
#     empty_arr.append(arr[i])
#     pick_result = sum_sub_sequence(i+1, empty_arr, arr, sum_result)

#     empty_arr.remove(arr[i])
#     not_pick_result = sum_sub_sequence(i+1, empty_arr, arr, sum_result)

#     return pick_result + not_pick_result


# arr = [1, 2, 1]
# sum_result = 2
# print(sum_sub_sequence(0, [], arr, sum_result))
