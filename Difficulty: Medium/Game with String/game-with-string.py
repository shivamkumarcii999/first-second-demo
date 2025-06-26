import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        # Step 1: Count frequency of each character
        freq = Counter(s)

        # Step 2: Create a max heap using negative frequencies
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        # Step 3: Remove k characters
        while k > 0 and max_heap:
            top = -heapq.heappop(max_heap)
            top -= 1
            k -= 1
            if top > 0:
                heapq.heappush(max_heap, -top)

        # Step 4: Calculate sum of squares of frequencies
        result = sum((f * f) for f in map(lambda x: -x, max_heap))
        return result
