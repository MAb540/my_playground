
# 5. Longest Palindromic Substring

# s = 'babad'
# def checkPalindrome(s, start, end):

#     is_palindrome = True

#     for i in range(start, end):
#         if i != start:
#             end = end - 1

#         if s[i] != s[end]:
#             is_palindrome = False
#             break

#     return is_palindrome


# print(checkPalindrome(s, 1, 3))

# solved in O(n^3) ## nested loop for all substrings and one nested loop to check palindrome.
# ans = []
# longest_sub_str = ''
# for i in range(len(s)):

#     start = i
#     end = len(s)-1

#     for j in range(end):
#         end_index = end-j
#         if s[start] == s[end_index]:
#             check = checkPalindrome(s, start, end_index)
#             # +1 because string indices is not inclusive of last integer
#             exteacteda_str = s[start:end_index+1]
#             if check and len(longest_sub_str) < len(exteacteda_str):
#                 longest_sub_str = exteacteda_str
#                 break

# print(longest_sub_str)

# 2nd approach to solve in O(n^2) time complexity, and O(n^2) space complexity, using dynamic programming
s = 'babad'
# generating all substrings with loops
for i in range(len(s)):
    sub_str = ''
    for j in range(i, len(s)):
        sub_str += s[j]
        print(sub_str)

# generating all substrings with recursion


# def all_sub_strings(ind, ds: str, s):

#     print(ds)

#     for i in range(ind, len(s)):

#         ds += s[i]
#         all_sub_strings(i+1, ds, s)
#         ds = ds[:i]


# all_sub_strings(1, s[0], s)
