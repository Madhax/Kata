
Patrick Gryciuk <chinchilla@gmail.com>
8:37 PM (56 minutes ago)
to me

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peeked=False
        self.peekVal = None
        self.iterator = iterator
        #print(type(iterator))

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked==False:
            self.peeked=True
            self.peekVal = self.iterator.next()
            return self.peekVal
           
        else:
            return self.peekVal

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            return self.peekVal
        else:
            return self.iterator.next()
       

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked:
            return True
        else:
            return self.iterator.hasNext()
