# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
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


class PeekingIterator(object):

  def __init__(self, iterator):
    """Initialize your data structure here.

    :type iterator: Iterator
    """
    self.iterator = iterator
    self._next = self.iterator.next() if self.iterator.hasNext() else None

  def peek(self):
    """Returns the next element in the iteration without advancing the iterator.

    :rtype: int
    """
    return self._next

  def next(self):
    """Returns the next element in the iteration and advances the iterator.

    :rtype: int
    """
    val_to_return = self._next
    self._next = self.iterator.next() if self.iterator.hasNext() else None
    return val_to_return

  def hasNext(self):
    """Returns true if the iteration has more elements.

    :rtype: bool
    """
    return self._next is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but do not advance the iterator.
#     iter.next()         # Should return the same value as [iter.peek()].