import random


class Solution(object):

  def __init__(self, nums):

    """ :type nums: List[int]

    """
    self.array = nums
    self.original = list(nums)

  def reset(self):

    """ Resets the array to its original configuration and returns it.

    :rtype: List[int]
    """
    self.array = list(self.original)
    return self.array

  def shuffle(self):

    """ Returns a random shuffling of the array.

    :rtype: List[int]
    """
    # Fisher-Yates Algorithm
    for i in range(len(self.array)):
      swap_idx = random.randint(i, len(self.array) - 1)
      self.array[i], self.array[swap_idx] = (
          self.array[swap_idx],
          self.array[i],
      )

    return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
