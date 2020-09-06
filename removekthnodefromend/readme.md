# Today I Learned: Remove Kth Node from the End of a Single Linked List
# Problem Statement
Write a function that takes in the head of a single linked list and integer k which represents the kth node to remove from the end of the linked list. 

# Sample Input
```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
k = 4
```

# Sample Result

```
# node 6 is removed
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
```

# Code #1

```python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth_node_from_end(head, k):
    ptr_1 = head
    ptr_2 = head
    ctr = 0
    
    # Move ptr_2
    while ctr < k:
        # Return early if k is longer than list's length
        if ctr < k and ptr_2 is None:
            return
        ptr_2 = ptr_2.next
        ctr += 1
    
    # Check if removing the first element on the list
    if ptr_2 is None:
        head.value = head.next.value
        head.next = head.next.next
        return head
    
    while ptr_2.next is not None:
        ptr_1 = ptr_1.next
        ptr_2 = ptr_2.next

    # Remove kth node from end
    ptr_1.next = ptr_1.next.next
    return head
```

# Notes
* Since this is a single linked list, we cannot traverse to the end of the list and then trace back the kth node. 
* Utilize two pointers to track the beginning and the end node of the linked list. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image