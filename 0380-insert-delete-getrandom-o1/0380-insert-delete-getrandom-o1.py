import random

class RandomizedSet(object):

    def __init__(self):
        self.vals = []
        self.val_to_idx = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False
        
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_idx:
            return False
        
        # Swap the target element with the last element
        idx_to_remove = self.val_to_idx[val]
        last_val = self.vals[-1]
        
        self.vals[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove
        
        # Remove the last element
        self.vals.pop()
        del self.val_to_idx[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.vals)