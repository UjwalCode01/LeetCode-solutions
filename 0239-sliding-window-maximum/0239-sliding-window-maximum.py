from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()  # stores indices of elements
        res = []

        for i in range(len(nums)):
            # 1. Remove elements smaller than current element from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # 2. Add current index to deque
            q.append(i)

            # 3. Remove index if it falls outside the current window
            if q[0] <= i - k:
                q.popleft()

            # 4. Append max to result once window reaches size k
            if i >= k - 1:
                res.append(nums[q[0]])

        return res