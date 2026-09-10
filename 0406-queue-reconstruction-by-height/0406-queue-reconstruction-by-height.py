class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort by height descending (-x[0]), then by k ascending (x[1])
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for person in people:
            # Insert person at index k
            queue.insert(person[1], person)
            
        return queue