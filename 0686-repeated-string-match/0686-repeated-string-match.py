class Solution(object):

  def repeatedStringMatch(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    # Minimum repetitions needed to match or exceed length of b
    count = (len(b) + len(a) - 1) // len(a)

    # Case 1: b fits within k repetitions
    if b in (a * count):
      return count

    # Case 2: b overlaps across boundaries, requiring one extra repetition (k + 1)
    if b in (a * (count + 1)):
      return count + 1

    return -1