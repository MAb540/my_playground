import random

# [[random.randint(0, 9) for i in range(3)] for i in range(3)]

# puzzle = """043080250
#             600000000
#             000001094
#             900004070
#             000608000
#             010200003
#             820500000
#             000000005
#             034090710"""

puzzle = """043080250
            600000000
            000001094"""

p = puzzle.replace('\n', '').split(' ')
pp = ''.join(p)
print(p)
print(pp)

# three_by_three = [[], [], [],
#                   [], [], [],
#                   [], [], []]

three_by_three = []
# print(len(pp))

for i in range(len(pp)+1):

    if i == 0:
        pass

    elif i % 9 == 0:
        sub_str_of_nine = pp[i-9:i].strip()

        for j in range(len(sub_str_of_nine)+1):

            if j == 0:
                pass

            elif j % 3 == 0:
                sub_str = sub_str_of_nine[j-3:j]
                three_by_three.append(list(sub_str))


print(three_by_three)

# row = 2
# col = 2

# for i in range(3):
#     # print('col ', three_by_three[i][col])
#     #print('row: ', three_by_three[row][i])
#     print(three_by_three[3 * (row//3) + i//3][3 * (col//3) + i % 3])
