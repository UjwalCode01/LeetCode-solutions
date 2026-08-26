class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Store list1 items with their indices
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        # Iterate over list2 and find common elements
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                current_sum = index_map[restaurant] + j
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant]
                elif current_sum == min_sum:
                    result.append(restaurant)
                    
        return result