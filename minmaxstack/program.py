# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        # Write your code here.
        # case stack empty
        if len(self.stack) == 0:
            return None
        # case stack one element
        # case stack one million element
        else:
            return self.stack[len(self.stack) - 1]['value']

    def pop(self):
        # Write your code here.
        # case stack empty
        if len(self.stack) == 0:
            return None
        # case stack one element
        # case stack one million element
        else:
            return self.stack.pop()['value']

    def push(self, number):
        # Write your code here.
        # case stack empty
        # case stack one element
        # case stack one million element
        # calculate min
        # calculate max
        # push into the stack
        self.stack.append(
            {
                'value': number,
                'min': self._calc_min(number),
                'max': self._calc_max(number)
            }
        )

    def getMin(self):
        # Write your code here.
        # case stack empty
        if len(self.stack) == 0:
            return None
        # case stack one element
        # case stack one million element
        else:
            return self.stack[len(self.stack) - 1]['min']

    def getMax(self):
        # Write your code here.
        # case stack empty
        if len(self.stack) == 0:
            return None
        # case stack one element
        # case stack one million element
        else:
            return self.stack[len(self.stack) - 1]['max']

    def _calc_min(self, number):
        # case stack empty
        if len(self.stack) == 0:
            return number
        # case stack one element
        elif number < self.stack[len(self.stack) - 1]['min']:
            return number
        else:
            return self.stack[len(self.stack) - 1]['min']

    def _calc_max(self, number):
        # case stack empty
        if len(self.stack) == 0:
            return number
        # case stack one element
        elif number > self.stack[len(self.stack) - 1]['max']:
            return number
        else:
            return self.stack[len(self.stack) - 1]['max']
