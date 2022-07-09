
heap = [None]

def getParentIndex(child_indx):
    return child_indx//2

def getLeftChildIndex(parent_indx):
    return parent_indx * 2

def getRightChildIndex(parent_indx):
    return parent_indx * 2 + 1

def hasParent(indx):
    parent_indx = getParentIndex(indx)
    if parent_indx >= 1:
        return parent_indx    
    return None


def pushInHeap(item):
    heap.append(item)


    if len(heap) > 2:

        child_Indx = len(heap) - 1
        parent_Indx = getParentIndex(child_Indx)
        while heap[child_Indx] < heap[parent_Indx]:
            if child_Indx > 0:
                heap[child_Indx],heap[parent_Indx] = heap[parent_Indx],heap[child_Indx]

                if parent_Indx > 1:
                    child_Indx = child_Indx//2
                else:
                    break

def removeFromHeap():
    
    heap_size = len(heap)-1
    last_item_indx = heap_size
    heap[1] = heap[last_item_indx]
   


    first_indx = 1
    while first_indx < heap_size:
        smaller_child_index = None
        if getLeftChildIndex(first_indx) <= heap_size:
            smaller_child_index = getLeftChildIndex(first_indx)
        # right_Child = None
        # if getRightChildIndex(first_indx) <= heap_size:
        #     right_Child = getRightChildIndex(first_indx)
        

        right_index = None
        if getRightChildIndex(first_indx) <= heap_size:
            right_index = getRightChildIndex(first_indx)


        if right_index and heap[right_index] < heap[smaller_child_index]:
            smaller_child_index = right_index

        if smaller_child_index != None and heap[first_indx] < heap[smaller_child_index]:
            break
        else:
            if smaller_child_index != None:
                heap[first_indx],heap[smaller_child_index] = heap[smaller_child_index],heap[first_indx]
            else:
                break

        first_indx = smaller_child_index



# def pushInHeap(item):
#     heap.append(item)

#     if(len(heap) > 2):
#         indx = len(heap) - 1
#         while heap[indx//2] > heap[indx]:
#             if indx >= 1:
#                 heap[indx//2],heap[indx] = heap[indx],heap[indx//2]

#                 if indx// 2 > 1:
#                     indx = indx // 2
#                 else:
#                     break


pushInHeap(2)
pushInHeap(4)
pushInHeap(3)
pushInHeap(5)
pushInHeap(6)

print(heap)

# print(heap[hasParent(2)])
# print(heap[2//2])

print(heap[getLeftChildIndex(1)])
print(heap[getRightChildIndex(1)])

print(heap[getLeftChildIndex(2)])
print(heap[getRightChildIndex(2)])

# print(heap[getLeftChildIndex(3)])
# print(heap[getRightChildIndex(3)])

removeFromHeap()

print('after removal: ')
heap = heap[0:len(heap)-1]
print(heap)

# class MinIntHeap:

#     capacity = 10
#     size = 0

#     items = [None] * capacity

#     def getLeftChildIndex(self,parentIndex):
#         return parentIndex*2 + 1

#     def getRightChildIndex(self,parentIndex):
#         return parentIndex*2 + 2

#     def getParentIndex(self,childIndex):
#         return (childIndex - 1) // 2

#     def hasLeftChild(self,index):
#         return self.getLeftChildIndex(index) < self.size
    
#     def hasRightChild(self,index):
#         return self.getRightChildIndex(index) < self.size
    
#     def hasParent(self,index):
#         return self.getParentIndex(index) >= 0
    
#     def leftChild(self,index):
#         return self.items[self.getLeftChildIndex(index)]
    
#     def rightChild(self,index):
#         return self.items[self.getRightChildIndex(index)]
    
#     def parent(self,index):
#         return self.items[self.getParentIndex(index)]
    
#     def swap(self,indexOne,indexTwo):
#         self.items[indexOne],self.items[indexTwo] = self.items[indexTwo], self.items[indexOne]
    
#     def peek(self):
#         if len(self.items) == 0:
#             return None
        
#         return self.items[0]

#     def poll(self):
#         if len(self.items) == 0:
#             return None
        
#         self.items[0] = self.items[self.size-1]
#         self.size -=1
#         self.heapifyDown()
#         return self.items

#     def add(self,item):
#         self.items[0] = item
#         self.size +=1
#         self.heapifyUp()
    
#     def heapifyUp(self):
#         index = self.size - 1
#         while self.hasParent(index) and self.parent(index) > self.items[index]:
#             self.swap(self.getParentIndex(index), index)
#             index = self.getParentIndex(index)

#     def heapifyDown(self):
#         index = 0
#         while self.hasLeftChild(index):
#             smaller_child_index = self.getLeftChildIndex(index)
#             if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
#                 smaller_child_index = self.getRightChildIndex(index)
            
#             if self.items[index] < self.items[smaller_child_index]:
#                 break
#             else:
#                 self.swap(index,smaller_child_index)
            
#             index = smaller_child_index