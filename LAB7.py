# LAB7
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# Worked with TA Harsh and LA Daniel

class MaxBinaryHeap:
    '''
        >>> h = MaxBinaryHeap()
        >>> h.getMax
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [10, 5]
        >>> h.insert(14)
        >>> h._heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(14)
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> h.insert(20)
        >>> h
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.insert(20)
        >>> h
        [20, 20, 14, 14, 2, 10, 11, 5, 9]
        >>> h.getMax
        20
        >>> h._leftChild(1)
        20
        >>> h._rightChild(1)
        14
        >>> h._parent(1)
        >>> h._parent(6)
        14
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMax()
        20
        >>> h._heap
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.deleteMax()
        20
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> len(h)
        7
        >>> h.getMax
        14
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMax(self):
        if self._heap == []:                                # If the list is empty return None
            return None
        return self._heap[0]                                # Return the first element in the list
    
    def _parent(self,index):
        if self._heap == []:                                # If the list is empty return None
            return None
        if index == 1:                                      # If the heap index passed in is 1 return None
            return None
        else:
            return self._heap[(index //2) -1]               # Else do what was told of us in the lectures by indexing it based on a list
        

    def _leftChild(self,index):
        if self._heap == []:                                # If the list is empty return None
            return None
        if len(self._heap) == 1:                            # If the length of the list is 1 return None
            return None
        if len(self._heap) == 2:                            # If the length of the list is two return the second element in the list
            return self._heap[1]
        if 2 * index  > len(self):                          # If the heap indexing is greater than the length of the list return None
            return None
        else:                                               # Return the left child of the parent and index it according to a list
            return self._heap[2 * index - 1]
        


    def _rightChild(self,index):
        if self._heap == []:                                # If the list is empty return None
            return None
        if len(self._heap) == 1:                            # If the length of the list is 1 return None
            return None
        if len(self._heap) == 2:                            # If the length of the list is 2 return None
            return None
        if 2 * index + 1 > len(self):                       # If the heap indexing is greater than the length of the list return None
            return None
        else:                                               # Return the right child of the parent adjusted to indexing of a list
            return self._heap[(2 * index)]
         

    def insert(self,x):
        if self._heap == []:                                                                                   # If the list is empty just add the element to the list
            self._heap += [x]                                   
        else:
            self._heap += [x]                                                                                  # Add the element to the list to start
            length = len(self)    # self.__len__(self)q       
            while self._parent(length) != None and self._parent(length) < x:                                   # Loop through to make sure the value of parent is still less than the value of x and that the value of the parent is not None
                self._heap[(length//2)-1], self._heap[length -1] = self._heap[length -1], self._heap[(length//2)-1]         # Swaps positions of the parent and x in the list
                length = length // 2                                                                                    # Updates the value of length of the list to see if it must be moved again




    def deleteMax(self):
        if len(self)==0:                                         
            return None        
        elif len(self)==1:                                          
            removed=self._heap[0]
            self._heap=[]
            return removed 
        else:
            length = len(self)                                                              # Makes a variable length equal to the length of the list
            self._heap[0], self._heap[length -1] = self._heap[length -1], self._heap[0]     # Swaps the rightmost element with the max element
            deleted = self._heap.pop()                                                      # Removes the max element and saves it in deleted
            length -= 1                                                                     # Makes length one less after the deletion
            temp = 1                                                                        # Stores the value of the heap index of the new first value
            current = self._heap[temp-1]                                                    # Makes current the value of the new value while using temp so that it can be updated
            while (self._leftChild(temp)!= None and self._leftChild(temp) > current) or (self._rightChild(temp) != None and self._rightChild(temp) > current):                  # Continues to go through as long as the left child is not None and the child is greater than the parent or the right child doesn't exist and the right child is greater than the parent
                if self._rightChild(temp) == None:                                                              # If right child is None just swap with left child and parent
                    self._heap[2 * temp -1], self._heap[temp-1] = self._heap[temp-1], self._heap[2 * temp -1]
                    temp = 2 * temp                                                                             # Update temp 
                    current = self._heap[temp-1]                                                                # Current stays the same
                elif self._leftChild(temp) >= self._rightChild(temp):                                           # If the left child is greater than the right or equal to swap with the left child and the parent and updates values
                    self._heap[2 * temp -1], self._heap[temp-1] = self._heap[temp-1], self._heap[2 * temp -1]
                    temp = 2 * temp
                    current = self._heap[temp-1]
                else:                                                                                           # Swap right child with parent and update values
                    self._heap[2 * temp], self._heap[temp-1] = self._heap[temp-1], self._heap[2 * temp]
                    temp = 2 * temp + 1
                    current = self._heap[temp-1]    
            return deleted                                                                                      # Return the value deleted
                    


def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [8, 5, 4, 3.1, 2, 1, 0, -15, -15, -15]
    '''
    newlst = []
    x = MaxBinaryHeap()                                         # Makes x an instance of MaxBinaryHeap
    for item in numList:                                        # Iterates through all the elements in numlist
        x.insert(item)                                          # Inserts each element using the insert function in MaxBinaryHeap
    while x._heap != []:                                        # Continues to go through until numList is empty
        newlst.append(x.deleteMax())                            # Adding the deleted value to newlst
    return newlst                                               # Return the new list



# ============== EXTRA CREDIT
class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(5, 'ajay'), (3, 'kyle'), (1, 'harsh'), (0, 'sara')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(7, 'ryan'), (4, 'daniel'), (5, 'ajay'), (0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.dequeue()
        'ryan'
        >>> priority_q.peek()
        'ajay'
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.dequeue()
        'ajay'
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        'daniel'
        >>> priority_q.dequeue()
        'kyle'
        >>> priority_q.dequeue()
        'harsh'
        >>> priority_q.dequeue()
        'sara'
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MaxBinaryHeap()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__

    def peek(self):
        if len(self) == 0:                                      # If the length is 0 return None
            return None
        return self._items._heap[0][1]                          # Return the second element of the tuple

    def isEmpty(self):
        if len(self._items) == 0:                               # If the length is 0 return True because it is empty
            return True
        return False                                            
    
    def enqueue(self, value, priority):
        tpl = (priority, value)                                 # Make the tuple which is priority and value
        self._items.insert(tpl)                                 # Insert the tuple into the list by having the priority as what insert looks at
        return None


    def dequeue(self):
        if len(self._items) == 0:                               # If the length of the list is 0 return None
            return None
        x = self._items.deleteMax()                             # Sets the deleted max to x and then gets the second element of the tuple
        return x[1]
    
if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(MaxBinaryHeap, globals(), name='LAB5',verbose=True)


