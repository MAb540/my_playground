
# a_list = [8,5,2,7,1,9,0]

a_list = [64, 34, 25, 12, 22, 11, 90]

# def selection_sort(list):

#     if len(list) == 0:
#         return 'list is empty'

#     count = 0
#     for i in range(0,len(list)):
#         min_idx = i
#         for j in range(i+1,len(list)):    
#             if list[min_idx] > list[j]:
#                 min_idx = j
#             count +=1    
#         list[i], list[min_idx] =  list[min_idx], list[i]    


#     # for i in range(0,len(list)):
#     #     min_val_index = 0
#     #     for j in range(i+1,len(list)):
#     #         if list[i] > list[j]:
#     #             min_val_index = j
#     #         count +=1
#     #     swap = list[i]
#     #     list[i] = list[min_val_index]
#     #     list[min_val_index] = swap

    

#     return list



print(selection_sort(a_list))
# print(ascending_sort([]))

# def bubble_sort(list):
#     if len(list) == 0:
#         return 'list is empty'
    
#     n = len(list)
#     # will run n * (n-i-2) // where i is the number of iterations
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j + 1]:
#                 list[j],list[j+1] = list[j+1],list[j]
    
#     return list

# print(bubble_sort(a_list))



# def bb_prac(arr):

#     if len(arr) == 0:
#         return 'list is empty'
#     n  = len(arr)
#     # will run n * (n-1)
#     for i in range(n):
#         for j in range(n-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
 
#     return arr
# print(bb_prac(a_list))