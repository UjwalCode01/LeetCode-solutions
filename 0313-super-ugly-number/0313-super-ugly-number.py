import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [0] * n
        ugly[0] = 1
        
        # Heap elements: (next_value, prime, pointer_index_in_ugly)
        heap = [(p, p, 0) for p in primes]
        heapq.heapify(heap)
        
        for i in range(1, n):
            # The next smallest super ugly number is at the top of the heap
            next_ugly = heap[0][0]
            ugly[i] = next_ugly
            
            # Pop all candidates matching next_ugly to eliminate duplicates
            while heap and heap[0][0] == next_ugly:
                val, p, idx = heapq.heappop(heap)
                heapq.heappush(heap, (p * ugly[idx + 1], p, idx + 1))
                
        return ugly[-1]