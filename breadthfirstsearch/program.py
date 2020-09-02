# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]

        while len(queue) > 0:
            cur_node = queue.pop(0)
            for child in cur_node.children:
                queue.append(child)
            array.append(cur_node.name)

        return array

