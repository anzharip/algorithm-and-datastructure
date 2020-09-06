# Today I Learned: Breadth-First Search on a Tree
# Problem Statement
Implement breadth-first search method on a tree node. 

# Sample Input
```
tree =      A
        /   |   \
       B    C     D
     /   \      /   \
    E     F    G     H
        /   \   \
       I     J    K
```

# Sample Result

```
["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
```

# Code #1

```
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def breadth_first_search(self, array):
        # Write your code here.
        queue = [self]

        while len(queue) > 0:
            cur_node = queue.pop(0)
            for child in cur_node.children:
                queue.append(child)
            array.append(cur_node.name)

        return array

```

# Notes
* Traverse the tree level-by-level. 
* Utilize queue to perform the traversal iteratively. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image