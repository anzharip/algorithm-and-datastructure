# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.endSymbol = "*"
        self.root = {}
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        # case string empty element
        if len(string) == 0:
            self.root = {self.endSymbol: True}
        # case string one element
        elif len(string) == 1:
            self.root[string] = {self.endSymbol: True}
        # case string one million element
        else:
            ptr = 0
            while ptr < len(string):
                cur_pos = self.root
                for index in range(ptr, len(string)):
                    letter = string[index]
                    if letter not in cur_pos:
                        cur_pos[letter] = {}
                        cur_pos = cur_pos[letter]
                    else:
                        cur_pos = cur_pos[letter]
                cur_pos[self.endSymbol] = True
                ptr += 1
        # case string all element are the same string
        # case string all element are the different string

    def contains(self, string):
        # Write your code here.
        # case zero element
        # case string one element
        # case string one million element
        # case string all element are the same string
        # case string all element are the different string
        cur_pos = self.root
        for index in range(len(string)):
            letter = string[index]
            if letter in cur_pos:
                cur_pos = cur_pos[letter]
            else:
                return False
        try:
            return cur_pos['*']
        except:
            return False
