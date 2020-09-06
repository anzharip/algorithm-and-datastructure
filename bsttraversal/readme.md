# Today I Learned: BST Traversal
# Problem Statement
Write three functions (in-order, pre-order, and post-order traversal) that takes in a Binary Search Tree (BST) and an empty array, traverse the BST add the node's value to the input array and return the array. 

# Sample Input
```
tree =      10
           /    \
         5       15
      /    \         \
    2       5          22
  /
1
```

# Sample Result

```
in_order = [1, 2, 5, 5, 10, 15, 22]
pre_order = [10, 5, 2, 1, 5, 15, 22]
post_order = [1, 2, 5, 5, 22, 15, 10]
```

# Code #1

```
def in_order_traversal(tree, array):
    if tree is not None: 
        in_order_traversal(tree.left, array)
        array.append(tree.value)
        in_order_traversal(tree.right, array)
    return array


def pre_order_traversal(tree, array):
    if tree is not None: 
        array.append(tree.value)
        pre_order_traversal(tree.left, array)
        pre_order_traversal(tree.right, array)
    return array


def post_order_traversal(tree, array):
    if tree is not None: 
        post_order_traversal(tree.left, array)
        post_order_traversal(tree.right, array)
        array.append(tree.value)
    return array
```

# Notes
*N/A

# Credits
* Algoexpert for the problem statement
