# import os

# n = 9

# thirthy_two_bit_binary = '{:032b}'.format(n)
# convert_str = ''
# for w in thirthy_two_bit_binary:
#     if w == '0':
#         convert_str += '1'
#     else:
#         convert_str += '0'


# binary = int(convert_str,2)
# print(binary)


## prime number of O(underroot n)

# check if n is prime or not
# import math
# n = 1000000000



# flag = False
# i = 3
# sqrt_of_n = int(math.sqrt(n)+1)
# while i <= sqrt_of_n:
#     if n % i == 0:
#         flag = True
#     i +=2

# if flag:
#     print('Not prime')
# else:
#     print('Prime')

# print(0 & 1)
# print((2 & 1) == 0)


## Luck Balance

k = 3

# luck = [[5,1],[1,1],[4,0]]
luck = [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]
luck_balance = 0


non_imp = [x[0] for x in filter(lambda x: x[1] == 0,luck)]
imp = sorted([x[0] for x in filter(lambda x : x[1] == 1,luck)],reverse=True)

print(non_imp)
print(imp)

luck = sum(non_imp) + sum(imp[:k]) - imp[k:][0]

print(luck)

# min_val = luck[0][0]
# for i,v in enumerate(luck):
#     if  v[1] == 1:
#         if v[0] < min_val:
#             min_val = v[0]
#     luck_balance += v[0]

# print(luck_balance - min_val - min_val)

# for luck, important in sorted(luck,reverse=True):
#     if not important:
#         luck_balance += luck

#     elif k:
#         luck_balance += luck
#         k -=1
    
#     else:
#         luck_balance -= luck
# print(luck_balance)

# non_imp = [v[0] for v in filter(lambda x : x[1] == 0,luck)]
# imp = [v[0] for v in filter(lambda x: x[1] == 1,luck)]


# print(non_imp)
# print(imp)
