
from re import U


arr = [[1,2],[3,4], [1,3], [5,7], [5,6], [7,4]]

parent = {}
rank = {}
max_gap = 0
result = []

# def init_cmp(mp,x,y):
#     if x not in mp:
#         mp[x]=x
#     if y not in mp:
#         mp[y]=y

# def init_cc(cc,x,y):
#     if x not in cc:
#         cc[x]=1
#     if y not in cc:
#         cc[y]=1

# def get_parent(mp,x):
#     while mp[x]!=x:
#         x=mp[x]
#     return x

def get_union(a,b):
    if rank[a] < rank[b]:
        parent[a] = b
        rank[b] += rank[a]
    
    elif rank[a] > rank[b]:
        parent[b] = a
        rank[a] += rank[b]

    else:
        parent[b] = a
        rank[a] += rank[b]

# Complete the maxCircle function below.
# def maxCircle(queries):
#     mp = {}
#     cc = {}
#     max_gp = 0
#     res = []
#     for q in queries:
#         init_cmp(mp,q[0],q[1])
#         init_cc(cc,q[0],q[1])
#         p1 = get_parent(mp,q[0])
#         p2 = get_parent(mp,q[1])
#         if p1!=p2:
#             get_union(p1,p2)
#             # if cc[p1] < cc[p2]:
#             #     mp[p1]= p2
#             #     cc[p2]=cc[p2]+cc[p1]
#             # else:
#             #     mp[p2]=p1
#             #     cc[p1]=cc[p1]+cc[p2]
#             max_gp = max(max_gp,max(cc[p1],cc[p2]))
#         res.append(max_gp)
#     return res 


# print(maxCircle(arr))





for a,b in arr:
    if a not in parent:
        parent[a] = a
        rank[a] = 1

    if b not in parent:
        parent[b] = b
        rank[b] = 1


def find_parent(node):
    while node != parent[node]:
        node = parent[node]
    
    return node





for a,b in arr:

    e1 = find_parent(a)
    e2 = find_parent(b)

    if e1 != e2:

        # if rank[e1] < rank[e2]:
        #     e1,e2 = e2,e1

        get_union(e1,e2)

        # parent[e2] = e1
        # rank[e1] += rank[e2]
        max_gap = max(max_gap,max(rank[e1],rank[e2]))

    result.append(max_gap)
print(result)


# parent = {}
# rank = {}
# max_gp = 2
# res = []
# for v in arr:
#     if v[0] not in parent:
#         parent[v[0]] = (v[0])
#         rank[v[0]] = 0

#     if v[1] not in parent:
#         parent[v[1]] = (v[1])
#         rank[v[1]] = 1


# def findParent(node):
#         if node == parent[node]:
#             return node
#         return findParent(parent[node])


# def union(x,y):
#     parent_of_x = x
#     parent_of_y = y 

    
#     if(rank[parent_of_x] < rank[parent_of_y]):
#         parent[parent_of_x] = parent_of_y
#         #rank[parent_of_x] = rank[parent_of_x] + rank[parent_of_y]

#     elif (rank[parent_of_y] > rank[parent_of_x]):
#         rank[parent_of_y] = parent_of_x
#         # rank[parent_of_y] = rank[parent_of_x] + rank[parent_of_y]
#     else:
#         parent[parent_of_y] = parent_of_x
#         rank[parent_of_x] = rank[parent_of_x] + rank[parent_of_y]


# def init(x):
#     if x in parent:
#         return findParent(x)
#     rank[x] = 1
#     parent[x] = x
#     return x

# for a,b in arr:
#     p1 = init(a)
#     p2 = init(b)

#     if p1 != p2:
#         if rank[p2]>rank[p1]: p1,p2=p2,p1

#         parent[p2] = p1
#         rank[p1] +=rank[p2]
#         max_gp = max(max_gp,rank[p1])

    # res.append(max_gp)
        # else:
        #     parent[p1]=p2
        #     rank[p2]=rank[p1]+rank[p2]
        #     max_gp = max(max_gp,max(rank[p1],rank[p2]))
    
#     res.append(max_gp)


# print(res)

# print(parent)
# print(rank)


# union(arr[0][0],arr[0][1])

# print('difference')

# print(parent)
# print(rank)


