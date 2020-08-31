# [
#   {"arguments": [5], "method": "insert"},
#   {"arguments": [15], "method": "insert"},
#   {"arguments": [10], "method": "contains"},
#   {"arguments": [5], "method": "contains"},
#   {"arguments": [15], "method": "contains"},
#   {"arguments": [10], "method": "remove"},
#   {"arguments": [5], "method": "remove"},
#   {"arguments": [15], "method": "remove"},
#   {"arguments": [10], "method": "contains"},
#   {"arguments": [5], "method": "contains"},
#   {"arguments": [15], "method": "contains"}
# ]

# [
#   {
#     "arguments": [5],
#     "method": "insert",
#     "output": null,
#     "tree": {
#       "nodes": [
#         {"id": "10", "left": "5", "right": null, "value": 10},
#         {"id": "5", "left": null, "right": null, "value": 5}
#       ],
#       "root": "10"
#     }
#   },
#   {
#     "arguments": [15],
#     "method": "insert",
#     "output": null,
#     "tree": {
#       "nodes": [
#         {"id": "10", "left": "5", "right": "15", "value": 10},
#         {"id": "15", "left": null, "right": null, "value": 15},
#         {"id": "5", "left": null, "right": null, "value": 5}
#       ],
#       "root": "10"
#     }
#   },
#   {
#     "arguments": [10],
#     "method": "contains",
#     "output": true,
#     "tree": {
#       "nodes": [
#         {"id": "10", "left": "5", "right": "15", "value": 10},
#         {"id": "15", "left": null, "right": null, "value": 15},
#         {"id": "5", "left": null, "right": null, "value": 5}
#       ],
#       "root": "10"
#     }
#   },
#   {
#     "arguments": [5],
#     "method": "contains",
#     "output": true,
#     "tree": {
#       "nodes": [
#         {"id": "10", "left": "5", "right": "15", "value": 10},
#         {"id": "15", "left": null, "right": null, "value": 15},
#         {"id": "5", "left": null, "right": null, "value": 5}
#       ],
#       "root": "10"
#     }
#   },
#   {
#     "arguments": [15],
#     "method": "contains",
#     "output": true,
#     "tree": {
#       "nodes": [
#         {"id": "10", "left": "5", "right": "15", "value": 10},
#         {"id": "15", "left": null, "right": null, "value": 15},
#         {"id": "5", "left": null, "right": null, "value": 5}
#       ],
#       "root": "10"
#     }
#   },
#   {
#     "arguments": [10],
#     "method": "remove",
#     "output": null,
#     "tree": {
#       "nodes": [
#         {"id": "15", "left": "5", "right": null, "value": 15},
#         {"id": "5", "left": null, "right": null, "value": 5}
#       ],
#       "root": "15"
#     }
#   },
#   {
#     "arguments": [5],
#     "method": "remove",
#     "output": null,
#     "tree": {
#       "nodes": [{"id": "15", "left": null, "right": null, "value": 15}],
#       "root": "15"
#     }
#   },
#   {
#     "arguments": [15],
#     "method": "remove",
#     "output": null,
#     "tree": {
#       "nodes": [{"id": "15", "left": null, "right": null, "value": 15}],
#       "root": "15"
#     }
#   },
#   {
#     "arguments": [10],
#     "method": "contains",
#     "output": false,
#     "tree": {
#       "nodes": [{"id": "15", "left": null, "right": null, "value": 15}],
#       "root": "15"
#     }
#   },
#   {
#     "arguments": [5],
#     "method": "contains",
#     "output": false,
#     "tree": {
#       "nodes": [{"id": "15", "left": null, "right": null, "value": 15}],
#       "root": "15"
#     }
#   },
#   {
#     "arguments": [15],
#     "method": "contains",
#     "output": true,
#     "tree": {
#       "nodes": [{"id": "15", "left": null, "right": null, "value": 15}],
#       "root": "15"
#     }
#   }
# ]

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


BST = program.BST


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        print('root.insert(5)')
        root.insert(5)
        self.assertTrue(root.left.value == 5)
        print('root.insert(15)')
        root.insert(15)
        self.assertTrue(root.right.value == 15)
        
        self.assertTrue(root.contains(10) is True)
        self.assertTrue(root.contains(5) is True)
        self.assertTrue(root.contains(15) is True)

        print('root.remove(10)')
        root.remove(10)
        self.assertTrue(root.value == 15)
        self.assertTrue(root.left.value == 5)
        self.assertTrue(root.right == None)
        print('root.remove(5)')
        root.remove(5)
        self.assertTrue(root.value == 15)
        
        print('root.remove(15)')
        root.remove(15)

        self.assertTrue(root.contains(10) is False)
        self.assertTrue(root.contains(5) is False)
        self.assertTrue(root.contains(15) is True)

        

if __name__ == '__main__':
    unittest.main()