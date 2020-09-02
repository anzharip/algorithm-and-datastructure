def invertBinaryTree(tree):
    # Write your code here.
    queue = [tree]
    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node is not None: 
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            queue.append(cur_node.left)
            queue.append(cur_node.right)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

