
class Solution:
    def countWays(self, n):
        if n == 1:  return 1
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a + b
        return b
        # code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends