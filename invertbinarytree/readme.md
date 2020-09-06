# Today I Learned: Invert Binary Tree
# Problem Statement
Write a function that takes in a binary tree and inverts it. 

# Sample Input
```
tree =      1
          /   \
        2       3
      /   \   /   \
     4    5  6     7
   /   \
  8     9
```

# Sample Result

```
tree =      1
          /   \
        3       2
      /   \   /   \
     7    6  5     4
                 /   \
                9     8
```

# Code #1

```
def invert_binary_tree(tree):
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
```

# Notes
* Invert the root node of the tree first. 
* Invert = swap the left child with the right child. 
* Continue swapping the childs of the subsequent node. 
* Perform breadth-first traversal. 
* Utilize queue to perform the traversal iteratively. 

# Credits
* Algoexpert for the problem statement
