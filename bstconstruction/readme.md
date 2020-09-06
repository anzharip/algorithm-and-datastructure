# Today I Learned: Binary Search Tree Construction
# Problem Statement
Implement BST class for a binary search tree with these features: 
* Inserting values. 
* Removing values, which applies to the first instances found. 
* Searching for values. 

# Sample Input
```
tree =      10
           /   \
          1     15
        /   \  /   \
       2    5  13   22
      /         \
     1           14
```

# Sample Result

```
insert(12) = 10
           /   \
          1     15
        /   \  /   \
       2    5  13   22
      /       /   \
     1       12   14

remove(10) = 12
           /   \
          1     15
        /   \  /   \
       2    5  13   22
      /         \
     1           14
```

# Code #1

```
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
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
        return self

    def contains(self, value):
        if self.find_node(value)[0] is not None:
            return self.find_node(value)[0].value == value
        else:
            return False
    
    def remove(self, value, parent_node=None):
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
                        if parent_node.left == cur_node:
                            parent_node.left = None
                        elif parent_node.right == cur_node:
                            parent_node.right = None
                        break
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

```

# Notes
* Using interative approach yields better space complexity, although somewhat harder to implement and not intuitive as the recursive approach. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image