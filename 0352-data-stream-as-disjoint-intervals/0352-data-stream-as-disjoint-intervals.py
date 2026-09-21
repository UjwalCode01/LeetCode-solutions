import bisect

class SummaryRanges(object):

    def __init__(self):
        self.nums = []
        self.seen = set()

    def addNum(self, value):
        if value not in self.seen:
            self.seen.add(value)
            bisect.insort(self.nums, value)

    def getIntervals(self):
        if not self.nums:
            return []

        intervals = []
        start = self.nums[0]
        end = self.nums[0]

        for i in range(1, len(self.nums)):
            if self.nums[i] == end + 1:
                end = self.nums[i]
            else:
                intervals.append([start, end])
                start = self.nums[i]
                end = self.nums[i]

        intervals.append([start, end])
        return intervals