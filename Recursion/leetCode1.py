
# students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
# mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]


# import itertools
# students = [[0, 0], [0, 0], [0, 0]]
# mentors = [[1, 1], [1, 1], [1, 1]]


# students = [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]]
# mentors = [[1, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0]]


# def compat_compare(compare_arr, compare_to):
#     count = 0
#     ind = -1
#     for mainInd, c in enumerate(compare_to):
#         local_count = 0

#         for i, v in enumerate(c):
#             if v == compare_arr[i]:
#                 local_count += 1

#         if count < local_count:
#             count = local_count
#             ind = mainInd

#     return [count, ind]


# total_count = 0
# m = mentors.copy()

# for i in range(len(students)):

#     [count, ind] = compat_compare(students[i], m)
#     if count > 0:
#         total_count += count
#         m.pop(ind)


# print(total_count)

# students = [[0, 0], [0, 0], [0, 0]]
# mentors = [[1, 1], [1, 1], [1, 1]]


# def maxCompat():
#     ans = 0
#     for permutation in itertools.permutations(range(len(students))):
#         score = 0

#         for i in range(len(students)):
#             for a, b in zip(students[permutation[i]], mentors[i]):
#                 if a == b:
#                     score += 1

#         ans = max(ans, score)
#     print(ans)

# maxCompat()

# def score_calc(a, b):
#     count = 0
#     for i, v in enumerate(b):
#         if a[i] == v:
#             count += 1
#     return count


# def help(S, M, V, ind, score, ans):
#     if ind == len(S):
#         a = max(ans[0], score)
#         ans[0] = a
#         return

#     for i in range(len(S)):
#         if V[i] == False:
#             V[i] = True

#             score_calculated = score_calc(students[ind], M[i])

#             help(S, M, V, ind+1, score + score_calculated, ans)

#             V[i] = False


# students = [[0, 1], [0, 0]]
# mentors = [[0, 1], [1, 1]]

# visited = [False for _ in range(len(students))]
# ans = [0]
# help(students, mentors, visited, 0, 0, ans)


# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# mapper = {
#     '2': 'abc',
#     '3': 'def',
#     '4': 'ghi',
#     '5': 'jkl',
#     '6': 'mno',
#     '7': 'pqrs',
#     '8': 'tuv',
#     '9': 'wxyz',
# }

# digits = '23'
# charas = []
# for d in digits:
#     charas.append(list(mapper[d]))


# visited = [False for _ in range(len(charas))]


# def mapperfunc(arr1, main_arr):

#     ans_arr = []
#     for v in main_arr:
#         for a in arr1:
#             for value in v:
#                 ans_arr.append(a+value)

#     return ans_arr


# def combos(ind, V, ds, arr, ans):

#     if ind == len(arr):
#         for d in ds:
#             ans.extend(d)
#         return

#     for i in range(ind, len(arr)):
#         if V[i]:
#             continue

#         V[i] = True
#         new_arr = arr[i+1:]
#         ds.append(mapperfunc(arr[i], new_arr))
#         combos(ind+1, V, ds, arr, ans)
#         ds.pop()


# ans = []
# combos(0, visited, [], charas, ans)
# print(ans)


mapper = [
    '', '',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz',
]


def combinations(ind, digits, ds, ans):
    if ind == len(digits):
        ans.append(ds)
        return

    letters = mapper[int(digits[ind])]
    for i in range(len(letters)):
        combinations(ind+1, digits, ds+letters[i], ans)


digits = '23'
ans = []
combinations(0, digits, '', ans)
print(ans)
