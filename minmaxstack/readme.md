# Today I Learned: Min-Max Stack
# Problem Statement
Write a MinMaxStack class for a Min-Max Stack with these features: 
* Push & pop values from the stack. 
* Peek value at the top of the stack. 
* Get the current min and max value of the stack in constant time. 

# Sample Input & Output

```
stack = MinMaxStack()
stack.push(5) # min: 5, max: 5, current value: 5
stack.push(7) # min: 5, max: 7, current value: 7
stack.push(2) # min: 2, max: 7, current value: 2
stack.pop(2) 
stack.pop(7) # min: 5, max: 5, current value: 5
```

# Code #1

```python
class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1]['value']

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()['value']

    def push(self, number):
        self.stack.append(
            {
                'value': number,
                'min': self._calc_min(number),
                'max': self._calc_max(number)
            }
        )

    def get_min(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1]['min']

    def get_max(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1]['max']

    def _calc_min(self, number):
        if len(self.stack) == 0:
            return number
        elif number < self.stack[len(self.stack) - 1]['min']:
            return number
        else:
            return self.stack[len(self.stack) - 1]['min']

    def _calc_max(self, number):
        if len(self.stack) == 0:
            return number
        elif number > self.stack[len(self.stack) - 1]['max']:
            return number
        else:
            return self.stack[len(self.stack) - 1]['max']


```

# Notes
* Store current, min, and max value state during pop and push. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image