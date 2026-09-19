class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1
        nodes = preorder.split(',')
        
        for node in nodes:
            # If no slots are available to place the node, it's invalid
            if slots == 0:
                return False
            
            # Consume 1 slot for the current node
            slots -= 1
            
            # Non-null nodes create 2 new slots for potential children
            if node != '#':
                slots += 2
                
        # A fully valid tree uses up all available slots exactly
        return slots == 0