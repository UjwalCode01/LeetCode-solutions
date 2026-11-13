from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        
        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]
                # Check and form the consecutive group of size `groupSize`
                for i in range(groupSize):
                    card = key + i
                    if count[card] < start_count:
                        return False
                    count[card] -= start_count
                    
        return True