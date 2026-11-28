from bisect import bisect_right
from collections import defaultdict

class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        counts = defaultdict(int)
        leader = -1
        max_votes = 0

        for person in persons:
            counts[person] += 1
            if counts[person] >= max_votes:
                leader = person
                max_votes = counts[person]
            self.leaders.append(leader)

    def q(self, t):
        idx = bisect_right(self.times, t) - 1
        return self.leaders[idx]