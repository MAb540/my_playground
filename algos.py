## minimum absolute difference between two values of array


#arr = [-2,2,4]
# arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
# all_pairs = []

# sorted_arr = sorted(arr)

# for i in range(len(sorted_arr)-1):

#     all_pairs.append(abs(sorted_arr[i] - sorted_arr[i+1]))

# print(sorted_arr)
# print(all_pairs)
# print(min(all_pairs))


# small_abs_diff = abs(arr[0] - arr[1])
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         diff = abs(arr[i]- arr[j])
#         if small_abs_diff > diff:
#             small_abs_diff = diff

# print(small_abs_diff)




# small_abs_diff = abs(all_pairs[0][0] - all_pairs[0][1])

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         all_pairs.append([arr[i],arr[j]])

# small_abs_diff = abs(all_pairs[0][0] - all_pairs[0][1])

# for v in all_pairs:
#     diff = abs(v[0] - v[1])
#     if small_abs_diff > diff:
#         small_abs_diff = diff
# print(small_abs_diff)

## Array left rotation problem

# arr = [1,2,3,4,5]

# n = 4

# method one

# new_arr = arr[0:4]
# arr = arr[4:]
# for v in new_arr:
#     arr.append(v)
# print(arr)


# for _ in range(n):
#     first_element = arr[0]
#     for j in range(0,len(arr)-1):
#         arr[j] = arr[j+1]

#     arr[len(arr)-1] = first_element


## New year chaos

q = [4,1,2,3]

# sorted_arr = q.copy() # [1,2,3,4,5]
# sorted_arr.sort()

# bribe = 0
# bribe_dict = dict()
# status = ''
# for i in range(len(sorted_arr)-1):

#     if sorted_arr[i] != q[i]:
#         sorted_arr[i],sorted_arr[i+1] = sorted_arr[i+1],sorted_arr[i]

#         if sorted_arr[i] == q[i]:
            
#             if sorted_arr[i+1] in bribe_dict:
#                 if bribe_dict[sorted_arr[i+1]] <= 2:
#                     bribe_dict[sorted_arr[i+1]] +=1
#                 else:
#                     status = 'too chaotic'
#                     break
#             else:
#                 bribe_dict[sorted_arr[i]] = 1
            
#             bribe +=1
ans = 0
for i in range(len(q)-1,0,-1):
    if q[i] - (i + 1) > 2:
        print('Too chaotic')
        break

    for j in range(max(0,q[i]-2),i):
        if q[j] > q[i]:
            ans +=1

print(ans)
