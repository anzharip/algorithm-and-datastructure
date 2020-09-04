# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    queue = [
        {
            'node': tree,
            'l_min': float('-inf'),
            'l_max': tree.value - 1,
            'r_min': tree.value,
            'r_max': float('inf')
        }
    ]
    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node['node'].left is not None:
            queue.append(
                {
                    'node': cur_node['node'].left,
                    'l_min': cur_node['l_min'], # stay
                    'l_max': cur_node['node'].left.value - 1,
                    'r_min': cur_node['node'].left.value,
                    'r_max': cur_node['node'].value - 1 # changes
                }
            )
        if cur_node['node'].right is not None:
            queue.append(
                {
                    'node': cur_node['node'].right,
                    'l_min': cur_node['node'].value, # changes
                    'l_max': cur_node['node'].right.value - 1,
                    'r_min': cur_node['node'].right.value,
                    'r_max': cur_node['r_max'] # stay
                }
            )
        if check_node(cur_node['node'], cur_node['l_min'], cur_node['l_max'], cur_node['r_min'], cur_node['r_max']) is False:
            return False

    return True


def check_node(node, l_min, l_max, r_min, r_max):
    if node.left is not None and (node.left.value < l_min or node.left.value > l_max):
        return False
    if node.right is not None and (node.right.value < r_min or node.right.value > r_max):
        return False
    return True
