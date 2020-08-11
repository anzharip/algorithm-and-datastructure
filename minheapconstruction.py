# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        for index in range(len(array) - 1, -1, -1):
            array = self.siftDown(array, index)
        return array

    def siftDown(self, array, parent_node_index):
        # Write your code here.
        if parent_node_index < 0 or parent_node_index > len(array) - 1:
            return array
        cur_idx = parent_node_index
        idx_to_swap = cur_idx
        while cur_idx < len(array):
            ch_one_idx = self.find_child_one_index(array, cur_idx)
            ch_two_idx = self.find_child_two_index(array, cur_idx)
            if ch_one_idx == -1:
                break
            if ch_two_idx == -1:
                idx_to_swap = ch_one_idx if array[ch_one_idx] < array[cur_idx] else -1
            elif array[ch_one_idx] < array[ch_two_idx]:
                idx_to_swap = ch_one_idx if array[ch_one_idx] < array[cur_idx] else -1
            else:
                idx_to_swap = ch_two_idx if array[ch_two_idx] < array[cur_idx] else -1
            if idx_to_swap == -1:
                break
            array = self.swap(array, cur_idx, idx_to_swap)
            cur_idx = idx_to_swap
        return array

    def siftUp(self, array, ch_idx):
        # Write your code here.
        cur_idx = ch_idx
        while cur_idx > -1:
            par_idx = self.find_parent_index(array, cur_idx)
            if par_idx == -1:
                break
            if array[cur_idx] < array[par_idx]:
                array = self.swap(array, cur_idx, par_idx)
                cur_idx = par_idx
            else:
                break
        return array

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        # swap first and last
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        # remove last
        value_to_remove = self.heap.pop()
        # siftdown first
        self.heap = self.siftDown(self.heap, 0)
        return value_to_remove

    def insert(self, value):
        # Write your code here.
        # add value as the last element of array
        self.heap.append(value)
        # siftup the new element
        self.heap = self.siftUp(self.heap, len(self.heap) - 1)

    @staticmethod
    def swap(array, pos_1, pos_2):
        if pos_1 > len(array) - 1 or pos_1 < 0:
            return array
        elif pos_2 > len(array) - 1 or pos_2 < 0:
            return array
        else:
            array[pos_1], array[pos_2] = array[pos_2], array[pos_1]
            return array

    @staticmethod
    def find_parent_index(array, child_index):
        if child_index > len(array) - 1 or child_index < 0:
            return -1
        elif (child_index - 1) // 2 > len(array) - 1 or (child_index - 1) // 2 < 0:
            return -1
        else:
            return (child_index - 1) // 2

    @staticmethod
    def find_child_one_index(array, parent_index):
        if parent_index > len(array) - 1 or parent_index < 0:
            return -1
        elif 2 * parent_index + 1 > len(array) - 1:
            return -1
        else:
            return 2 * parent_index + 1

    @staticmethod
    def find_child_two_index(array, parent_index):
        if parent_index > len(array) - 1 or parent_index < 0:
            return -1
        elif 2 * parent_index + 2 > len(array) - 1:
            return -1
        else:
            return 2 * parent_index + 2


# TEST
# before_heap = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
# result_heap = [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# print(MinHeap.find_parent_index(before_heap, 1) == 0)
# print(MinHeap.find_parent_index(before_heap, -1000) == -1)
# print(MinHeap.find_parent_index(before_heap, 1000) == -1)
# print(MinHeap.find_child_one_index(before_heap, 1) == 3)
# print(MinHeap.find_child_one_index(before_heap, -123094) == -1)
# print(MinHeap.find_child_one_index(before_heap, 123094) == -1)
# print(MinHeap.find_child_two_index(before_heap, 5) == 12)
# print(MinHeap.find_child_two_index(before_heap, -123094) == -1)
# print(MinHeap.find_child_two_index(before_heap, 123094) == -1)
# min_heap = MinHeap(before_heap)
# print(min_heap.heap == result_heap)

# TEST X
# before_heap = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
# print(before_heap)
# min_heap = MinHeap(before_heap)
# print(min_heap.heap)
# print(min_heap.remove() == -10)
# print(min_heap.peek() == -10)
# print(min_heap.insert(-8))
# print(min_heap.peek() == -10)
# print(min_heap.remove() == -10)
# print(min_heap.peek() == -9)
# print(min_heap.insert(8))
# print(min_heap.peek() == -9)

# TEST 9
before_heap = [
    -823,
    164,
    48,
    -987,
    323,
    399,
    -293,
    183,
    -908,
    -376,
    14,
    980,
    965,
    842,
    422,
    829,
    59,
    724,
    -415,
    -733,
    356,
    -855,
    -155,
    52,
    328,
    -544,
    -371,
    -160,
    -942,
    -51,
    700,
    -363,
    -353,
    -359,
    238,
    892,
    -730,
    -575,
    892,
    490,
    490,
    995,
    572,
    888,
    -935,
    919,
    -191,
    646,
    -120,
    125,
    -817,
    341,
    -575,
    372,
    -874,
    243,
    610,
    -36,
    -685,
    -337,
    -13,
    295,
    800,
    -950,
    -949,
    -257,
    631,
    -542,
    201,
    -796,
    157,
    950,
    540,
    -846,
    -265,
    746,
    355,
    -578,
    -441,
    -254,
    -941,
    -738,
    -469,
    -167,
    -420,
    -126,
    -410,
    59
]
# print(before_heap)
# min_heap = MinHeap(before_heap)
# print(min_heap.heap)
# print(min_heap.insert(2))
# print(min_heap.insert(22))
# print(min_heap.insert(222))
# print(min_heap.insert(2222))
# print(min_heap.remove() == -987)
# print(min_heap.remove() == -950)
# print(min_heap.remove() == -949)
# print(min_heap.remove() == -942)

# TEST 5

before_heap = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
print(before_heap)
min_heap = MinHeap(before_heap)
# print(min_heap.heap)
# print(min_heap.remove() == -10)
# print(min_heap.peek() == -10)
print(min_heap.insert(-8))
# print(min_heap.peek() == -10)
# print(min_heap.remove() == -10)
# print(min_heap.peek() == -9)
# print(min_heap.insert(8))
# print(min_heap.peek() == -9)
# print(min_heap.heap)

def isMinHeapPropertySatisfied(array):
    print(array)
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        # print(currentIdx, parentIdx)
        if array[parentIdx] > array[currentIdx]:
            return False
    return True

print(isMinHeapPropertySatisfied(min_heap.heap))