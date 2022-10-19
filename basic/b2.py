

# 1. Understand recursion by print something N times

# def recur_print_n_times(n):
#     if n == 0:
#         return
#     recur_print_n_times(n-1)
#     print(n)

# recur_print_n_times(10)

# 2. Print name N times using recursion

# def print_name_n_times(n):
#     if n == 0:
#         return
#     print('abc')
#     print_name_n_times(n-1)

# print_name_n_times(10)


# 3. Print 1 to N using recursion
# def print_one_to_n(n):
#     if n == 0:
#         return

#     print_one_to_n(n-1)
#     print(n)

# print_one_to_n(10)

# 4. Print N to 1 using recursion
# def print_n_to_one(n):

#     if n == 0:
#         return
#     print(n)
#     print_n_to_one(n-1)

# print_n_to_one(10)

# 5. Sum of first N numbers
# def sum_of_first_n_numbers(n, total):
#     if n == 0:
#         return total

#     total += n
#     return sum_of_first_n_numbers(n-1, total)

# print(sum_of_first_n_numbers(5, 0))

# 6. Factorial of N numbers
# def factorial_of_n_numbers(n):
#     if n == 0:
#         return 1
#     return n * factorial_of_n_numbers(n - 1) ## n * n -1 * n-2  * n -3 * n -4 * n -5
# print(factorial_of_n_numbers(5))


def factorial_of_n_numbers(start, n):
    if start >= n:
        return 1

    ans = start * factorial_of_n_numbers(start + 1, n)  # 2  ## 3
    print(ans, end=' ')
    return ans


print(factorial_of_n_numbers(1, 3))
