#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        return heapq.nsmallest(k, points, key = lambda p: p[0]**2 + p[1]**2)
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends