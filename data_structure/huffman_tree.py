class HNode:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.pointer = None
        self.bpointer = None

    def __gt__(self, other):
        """Greater than"""
        if not isinstance(other, HNode):
            return -1
        return self.data > other.data

    def __ge__(self, other):
        """Greater than or equal to"""
        if not isinstance(other, HNode):
            return -1
        return self.data >= other.data

    def __lt__(self, other):
        """Less than"""
        if not isinstance(other, HNode):
            return -1
        return self.data < other.data

    def __le__(self, other):
        """Less than or equal to"""
        if not isinstance(other, HNode):
            return -1
        return self.data <= other.data

from heap_link_little import HeapLinkLittle
class Huffman_Tree:
    def __init__(self, text=None):
        self.h = HeapLinkLittle()
        if text:
            self.counter = self.__build_counter(text)
        else:
            self.counter = {}
        self.root = None
        self.__build_huffman_tree()

    def __build_counter(self, text):
        '''text: a list of words.'''
        counter = {}
        for word in text:
            counter[word] = counter.get(word, 0) + 1
        return counter

    def __build_huffman_tree(self):
        for k, v in self.counter.items():
            self.h.push(HNode(k, v))

        while True:
            a, b = self.h.pop(), self.h.pop()
            if a is None or b is None:
                break
            c = HNode(None, a.data + b.data)
            c.pointer = a
            c.bpointer = b
            self.h.push(c)
            self.root = c

        return self.root

if __name__ == "__main__":
    h = Huffman_Tree("abcdasdfasdfcasdfasdf")
    print(h)