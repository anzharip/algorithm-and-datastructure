def minHeightBst(array):
    if len(array) == 1:
        return BST(array[0])
    # Base case
    queue = []
    mid_idx = (len(array) - 1) // 2
    root_node = BST(array[mid_idx])
    l_child_start = 0
    l_child_end = mid_idx - 1
    r_child_start = mid_idx + 1
    r_child_end = len(array) - 1
    if l_child_start <= l_child_end:
        queue.append({
            'start': l_child_start, 
            'end': l_child_end
        })
    if r_child_start <= r_child_end:
        queue.append({
            'start': r_child_start, 
            'end': r_child_end
        })
    
    while len(queue) > 0:
        cur_queue_el = queue.pop(0)
        mid_idx = (cur_queue_el['start'] + cur_queue_el['end']) // 2
        root_node.insert(array[mid_idx])
        l_child_start = cur_queue_el['start']
        l_child_end = mid_idx - 1
        r_child_start = mid_idx + 1
        r_child_end = cur_queue_el['end']
        if l_child_start <= l_child_end:
            queue.append({
                'start': l_child_start, 
                'end': l_child_end
            })
        if r_child_start <= r_child_end:
            queue.append({
                'start': r_child_start, 
                'end': r_child_end
            })
    return root_node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

