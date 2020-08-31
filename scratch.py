Aww, your code didn't pass the test case.

Our Code's Output
[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": null, "value": 15},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "5", "left": "2", "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "14", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "1", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  }
]
Your Code's Output
[
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": null, "value": 10},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": null, "right": null, "value": 5}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": null, "value": 15},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": null, "right": null, "value": 2}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": null, "value": 13},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "insert",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": null, "right": null, "value": 5},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [5],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "12", "left": null, "right": null, "value": 12},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [12],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "13", "left": null, "right": "14", "value": 13},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [13],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": "14", "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "14", "left": null, "right": null, "value": 14},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [14],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": "22", "value": 15},
        {"id": "22", "left": null, "right": null, "value": 22},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [22],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "2", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "2", "left": "1", "right": null, "value": 2},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [2],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": "1", "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15},
        {"id": "1", "left": null, "right": null, "value": 1}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [1],
    "method": "remove",
    "output": null,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  },
  {
    "arguments": [15],
    "method": "contains",
    "output": true,
    "tree": {
      "nodes": [
        {"id": "10", "left": null, "right": "15", "value": 10},
        {"id": "15", "left": null, "right": null, "value": 15}
      ],
      "root": "10"
    }
  }
]