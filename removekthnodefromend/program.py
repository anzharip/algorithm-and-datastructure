# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
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

