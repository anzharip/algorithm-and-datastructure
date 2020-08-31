# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # case value == int
        cur_node = self
        while True:
            if value < cur_node.value:
                if cur_node.left is not None:
                    cur_node = cur_node.left
                else:
                    cur_node.left = BST(value)
                    return self
            elif value >= cur_node.value:
                if cur_node.right is not None:
                    cur_node = cur_node.right
                else:
                    cur_node.right = BST(value)
                    return self
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        if self.find_node(value)[0] is not None:
            return self.find_node(value)[0].value == value
        else:
            return False
    
    def remove(self, value, parent_node=None):
        # Write your code here.
        # case node have no children
        cur_node = self
        while cur_node is not None:
            if value > cur_node.value:
                parent_node = cur_node
                cur_node = cur_node.right
            elif value < cur_node.value:
                parent_node = cur_node
                cur_node = cur_node.left
            # case there is duplicate value
            elif cur_node.right is not None and value == cur_node.right.value:
                parent_node = cur_node
                cur_node = cur_node.right
            # if cur_node is none, aka value not found, the loop will break here
            else:
                if parent_node is None:
                    if cur_node.left is not None and cur_node.right is not None:
                        print('triggered')
                        cur_node.value = cur_node.right.get_min_value()
                        cur_node.right.remove(cur_node.value, cur_node)
                    elif cur_node.left is not None and cur_node.right is None:
                        cur_node.value = cur_node.left.value
                        cur_node.right = cur_node.left.right
                        cur_node.left = cur_node.left.left
                        break
                    elif cur_node.left is None and cur_node.right is not None:
                        cur_node.value = cur_node.right.get_min_value()
                        cur_node.right.remove(cur_node.value, cur_node)
                    elif cur_node.left is None and cur_node.right is None:
                        # case trying to remove root node but they have no child
                        break
                else:
                    if cur_node.left is not None and cur_node.right is not None:
                        cur_node.value = cur_node.right.get_min_value()
                        cur_node.right.remove(cur_node.value, cur_node)
                    elif cur_node.left is not None and cur_node.right is None:
                        cur_node.value = cur_node.left.value
                        cur_node.right = cur_node.left.right
                        cur_node.left = cur_node.left.left
                        break
                    elif cur_node.left is None and cur_node.right is not None:
                        cur_node.value = cur_node.right.get_min_value()
                        cur_node.right.remove(cur_node.value, cur_node)
                    elif cur_node.left is None and cur_node.right is None:
                        # case removing leaf node
                        print('parent_node.left == cur_node: ', parent_node.left == cur_node)
                        print('parent_node.right == cur_node: ', parent_node.right == cur_node)

                        if parent_node.left == cur_node:
                            parent_node.left = None
                        elif parent_node.right == cur_node:
                            parent_node.right = None
                        break
        # Do not edit the return statement of this method.
        return self

    def find_node(self, value):
        cur_node = self
        parent_node = cur_node
        while True:
            if value == cur_node.value:
                return cur_node, parent_node
            elif cur_node.left is None and cur_node.right is None:
                return None, None
            elif value < cur_node.value:
                if cur_node.left is not None:
                    parent_node = cur_node
                    cur_node = cur_node.left
                else:
                    return None, None
            elif value >= cur_node.value:
                if cur_node.right is not None:
                    parent_node = cur_node
                    cur_node = cur_node.right
                else:
                    return None, None

    def get_min_value(self):
        cur_node = self
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node.value