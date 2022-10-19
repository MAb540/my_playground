
# 1. Count digits in a number
# Problem Statement: Given an integer N, write program to count number of digits in N.
# n = 12345

# one way
# def count_digits(n):
#     count = 0
#     for i in range(len(str(n))):
#         count += 1
#     return count

# print(count_digits(n))

# second way
# def count_digits(n):
#     count = 0

#     while n != 0:
#         n = n//10
#         count += 1
#     return count

# print(count_digit)


# def count_digits(n):
#     digits = math.floor(math.log10(n) + 1)
#     return digits

# print(count_digits(n))

# 2. Reverse a number in C
# Problem Statement: Given a number N reverse the number and print it.

# Time Complexity: O(n), where n is the length of the given number
# Space Complexity: O(1)
# def reverse_number(n):
#     reverse = 0

#     while n != 0:
#         remainder = n % 10

#         n = n//10
#         reverse = reverse * 10 + remainder
#     return reverse

# print(reverse_number(123))


# 3. Check if a number is Palindrome or Not
# Problem Statement:  Given a number check if it is a palindrome.

# n = -121

# def is_palindrome(n):
#     if n < 0:
#         return False
#     temp = n
#     reverse = 0
#     while temp != 0:
#         remainder = temp % 10
#         reverse = reverse * 10 + remainder
#         temp = temp//10

#     return n == reverse

# print(is_palindrome(n))

# 4. Find GCD of two numbers
# Problem Statement: Find gcd of two numbers.

# Time Complexity: O(N)
# Space Complexity: O(1)
# def greatest_common_divisor(n1, n2):
#     min_num = min(n1, n2)

#     gcd = 1
#     for i in range(2, min_num+1):
#         if n1 % i == 0 and n2 % i == 0:
#             if gcd < i:
#                 gcd = i
#     return gcd

# print(greatest_common_divisor(4, 8))
# print(greatest_common_divisor(3, 6))

# approach 2 using Euclidean's theorem
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(4, 8))


# 5. Check if a number is Armstrong Number or not
# Problem Statement: Given a number, check if it is Armstrong Number or Not.
# Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number.
# ## using length
# def is_armstrong(n):

#     length = len(str(n))
#     ans = 0
#     for i in str(n):
#         ans += int(i) ** length

#     return ans == n
# print(is_armstrong(1634))

# using length
# def is_armstrong(n):

#     counter = n
#     digit = 0
#     while counter != 0:
#         counter = counter//10
#         digit += 1

#     sum = 0
#     temp = n
#     while temp != 0:

#         last_digit = temp % 10

#         sum += last_digit ** digit
#         temp = temp//10

#     return sum == n
# print(is_armstrong(1634))


# 6. Print all Divisors of a given Number
# Problem Statement: Given a number, print all the divisors of the number. A divisor is a number that gives remainder as zero when divided.

# def all_divisors(n):
#     for i in range(1, n//2+1):  # complexity is O(n/2),  if to n , complexity will be O(n)
#         if n % i == 0:
#             print(i)
# print(all_divisors(36))

# import math
# def all_divisors(n):
#     for i in range(1, int(math.sqrt(n)+1)):
#         if n % i == 0:
#             print(i)
#             if i != n//i:
#                 print(n//i)

# print(all_divisors(36))

# 7. Check if a number is prime or not
# Problem Statement: Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.
# import math

# def is_prime(n):

#     is_prime = True
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             is_prime = False
#             break
#     return is_prime

# print(is_prime(4))


# Bonus question form gfg
# minimum number of jumps,
# 0 is not involved in the array solution,
# def mini_num_of_jumps(arr):

#     i = max_reachable_jump = last_jumped = jump = 0
#     while last_jumped < len(arr)-1:
#         max_reachable_jump = max(max_reachable_jump, i+arr[i])
#         if i == last_jumped:
#             last_jumped = max_reachable_jump
#             jump += 1

#         i += 1

#     return jump


# solving using recursion
import sys


def mini_num_of_jumps(ind, arr):

    if ind == len(arr)-1:
        return 0

    ans = sys.maxsize
    for step in range(1, arr[ind]+1):
        calculated_ans = mini_num_of_jumps(ind+step, arr) + 1
        ans = min(ans, calculated_ans)
    return ans
    # def mini_num_of_jumps_zero_involved(arr):

    #     if len(arr) <= 1:
    #         return 0

    #     if arr[0] == 0:
    #         return -1

    #     jump_count = 1
    #     max_reachable_jump = arr[0]
    #     step = arr[0]
    #     i = 0

    #     while i < len(arr):
    #         if i == len(arr)-1:
    #             return jump_count

    #         max_reachable_jump = max(max_reachable_jump, i+arr[i])
    #         step -= 1

    #         if step == 0:
    #             jump_count += 1
    #             if i >= max_reachable_jump:
    #                 return -1
    #             step = max_reachable_jump-1
    #         i += 1

    #     return -1


# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr = [1, 4, 3, 2, 6, 7]
# arr = [2, 3, 1, 1, 4]
# arr = [2, 1, 0, 3]
arr = [1, 2, 1, 2]
print(mini_num_of_jumps(0, arr))
