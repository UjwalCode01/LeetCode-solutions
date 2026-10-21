class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case: the first row and first column is always 0
        if n == 1 and k == 1:
            return 0
        
        # Length of the previous row's segment
        mid = 2 ** (n - 2)
        
        # If k falls in the first half, it inherits from the parent in the previous row
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        # If k falls in the second half, it is the inverted value of the corresponding element in the first half
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)