class Solution(object):

  def isAdditiveNumber(self, num):
    """
    :type num: str
    :rtype: bool
    """
    n = len(num)

    # i and j represent the lengths of the first two numbers
    for i in range(1, n // 2 + 1):
      # First number cannot have leading zeros unless it is "0"
      if num[0] == '0' and i > 1:
        break

      for j in range(1, (n - i) // 2 + 1):
        # Second number cannot have leading zeros unless it is "0"
        if num[i] == '0' and j > 1:
          break

        num1 = int(num[:i])
        num2 = int(num[i : i + j])
        k = i + j

        # Check if the remaining part matches the additive sequence
        while k < n:
          num3 = num1 + num2
          num3_str = str(num3)

          if not num.startswith(num3_str, k):
            break

          k += len(num3_str)
          num1, num2 = num2, num3

        if k == n:
          return True

    return False