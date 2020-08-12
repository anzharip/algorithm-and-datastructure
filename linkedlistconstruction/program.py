# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        # case if node is a head and a tail
        if node == self.head and node == self.tail:
            pass
        # case if node is a head
        elif node == self.head:
            pass
        # case if node is a tail
        elif node == self.tail:
            self.remove(node)
            self.insertBefore(self.head, node)
        # case self.head or self.tail is None
        elif self.head is None or self.tail is None:
            self.remove(node)
            self.head = node
            self.tail = node
        # case if node is already inside the list or outside
        else:
            self.remove(node)
            self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        # case if node is a head and a tail
        if node == self.head and node == self.tail:
            pass
        # case if node is a head
        elif node == self.head:
            self.remove(node)
            self.insertAfter(self.tail, node)
        # case if node is a tail
        elif node == self.tail:
            pass
        # case self.head or self.tail is None
        elif self.head is None or self.tail is None:
            self.remove(node)
            self.head = node
            self.tail = node
        # case if node is already inside the list or outside
        else:
            self.remove(node)
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        # single element list aka head = tail aka single element list
        if node == self.head and node == self.tail:
            next_node = self.head
            next_node.prev = nodeToInsert
            nodeToInsert.next = next_node
            self.head = nodeToInsert
            self.head.prev = None
            self.tail.next = None
        # head case
        elif node == self.head:
            self.remove(nodeToInsert)
            next_node = self.head
            next_node.prev = nodeToInsert
            nodeToInsert.next = next_node
            self.head = nodeToInsert
            self.head.prev = None
        # tail case
        elif node == self.tail:
            self.remove(nodeToInsert)
            prev_node = self.tail.prev
            next_node = self.tail
            prev_node.next = nodeToInsert
            next_node.prev = nodeToInsert
            nodeToInsert.prev = prev_node
            nodeToInsert.next = next_node
        else:
            self.remove(nodeToInsert)

            prev_node = node.prev
            next_node = node
            # case where node become head after self.remove is called, e.g. node is in position 2
            if prev_node is not None:
                prev_node.next = nodeToInsert
            next_node.prev = nodeToInsert
            nodeToInsert.prev = prev_node
            nodeToInsert.next = next_node
            # case where node become head after self.remove is called, e.g. node is in position 2
            if prev_node is None:
                self.setHead(nodeToInsert)
        # case empty list -> impossible, node has to be already a member of the linked_list

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        # single element list aka head = tail
        if node == self.head and node == self.tail:
            prev_node = self.tail
            prev_node.next = nodeToInsert
            nodeToInsert.prev = prev_node
            self.tail = nodeToInsert
            self.head.prev = None
            self.tail.next = None
        # case head
        elif node == self.head:
            self.remove(nodeToInsert)
            prev_node = self.head
            next_node = self.head.next
            prev_node.next = nodeToInsert
            next_node.prev = nodeToInsert
            nodeToInsert.prev = prev_node
            nodeToInsert.next = next_node
        # case tail
        elif node == self.tail:
            self.remove(nodeToInsert)
            prev_node = self.tail
            prev_node.next = nodeToInsert
            nodeToInsert.prev = prev_node
            self.tail = nodeToInsert
            self.tail.next = None
        # case in the middle
        else:
            self.remove(nodeToInsert)
            prev_node = node
            next_node = node.next
            prev_node.next = nodeToInsert
            next_node.prev = nodeToInsert
            nodeToInsert.prev = prev_node
            nodeToInsert.next = next_node

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        # case no element
        if self.head is None or self.tail is None:
            self.setHead(nodeToInsert)
        # find position
        else:
            ptr = 1
            current_node = self.head
            while ptr < position:
                current_node = current_node.next
                ptr += 1
            # case current_node is None aka position is out of bound
            if current_node is None:
                return
            self.insertBefore(current_node, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        cur_pos = self.head
        while cur_pos is not None:
            next_pos = cur_pos.next
            if cur_pos.value == value:
                self.remove(cur_pos)
                cur_pos = next_pos
            else:
                cur_pos = next_pos

    def remove(self, node):
        # Write your code here.
        # case removed node is a head and a tail
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
            node.next = None
            node.prev = None
        # case removed node is a head
        elif node == self.head:
            next_node = node.next
            self.head = next_node
            self.head.prev = None
            node.next = None
            node.prev = None
        # case removed node is a tail
        elif node == self.tail:
            prev_node = node.prev
            self.tail = prev_node
            self.tail.next = None
            node.next = None
            node.prev = None
        # case removed node is in the middle
        else:
            prev_node = node.prev
            next_node = node.next
            if prev_node is not None:
                prev_node.next = next_node
            if next_node is not None:
                next_node.prev = prev_node
            node.next = None
            node.prev = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        cur_pos = self.head
        while cur_pos is not None:
            if cur_pos.value == value:
                return True
            else:
                cur_pos = cur_pos.next
        return False


# TEST
# def bindNodes(nodeOne, nodeTwo):
#     nodeOne.next = nodeTwo
#     nodeTwo.prev = nodeOne
#
#
# linked_list = DoublyLinkedList()
# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# eight = Node(8)
# bindNodes(one, two)
# bindNodes(two, three)
# bindNodes(three, four)
# bindNodes(four, five)
# linked_list.head = one
# linked_list.tail = five
#
# print(linked_list.containsNodeWithValue(3) is True)
# print(linked_list.containsNodeWithValue(6) is False)
# el_three = linked_list.head.next.next
# print(linked_list.insertBefore(el_three, six))
# print(linked_list.containsNodeWithValue(6) is True)
# print(linked_list.head.next.next.value == 6)
# print(linked_list.insertBefore(linked_list.head, seven))
# print(linked_list.head.value == 7)
# print(linked_list.head.next.value == 1)
# print(linked_list.insertBefore(linked_list.tail, eight))
# print(linked_list.tail.value == 5)
# print(linked_list.tail.prev.value == 8)

# TEST 2
# def bindNodes(nodeOne, nodeTwo):
#     nodeOne.next = nodeTwo
#     nodeTwo.prev = nodeOne
#
# def getNodeValuesHeadToTail(linkedList):
#     values = []
#     node = linkedList.head
#     while node is not None:
#         values.append(node.value)
#         node = node.next
#     return values
#
# def getNodeValuesTailToHead(linkedList):
#     values = []
#     node = linkedList.tail
#     while node is not None:
#         values.append(node.value)
#         node = node.prev
#     return values
#
# linkedList = DoublyLinkedList()
# one = Node(1)
# two = Node(2)
# three = Node(3)
# three2 = Node(3)
# three3 = Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# bindNodes(one, two)
# bindNodes(two, three)
# bindNodes(three, four)
# bindNodes(four, five)
# linkedList.head = one
# linkedList.tail = five
#
# linkedList.setHead(four)
# assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5]
#
# assert getNodeValuesTailToHead(linkedList) == [5, 3, 2, 1, 4]