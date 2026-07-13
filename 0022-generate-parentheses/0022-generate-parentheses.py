class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if the string reaches the maximum required length, it's valid
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # If we can still add an open parenthesis, do it
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # If we can add a close parenthesis safely, do it
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counters
        backtrack("", 0, 0)
        return result