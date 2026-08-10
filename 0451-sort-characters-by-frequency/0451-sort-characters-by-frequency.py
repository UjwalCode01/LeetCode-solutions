from collections import Counter


class Solution(object):

    def frequencySort(self, s):
        # Step 1: Count frequency of each character
        counts = Counter(s)

        # Step 2: Build the string sorted by frequency in descending order
        res = []
        for char, freq in counts.most_common():
            res.append(char * freq)

        return "".join(res)