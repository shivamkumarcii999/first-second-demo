from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        q, res = deque(), []
        for i in range(len(arr)):
            if q and q[0] == i - k:
                q.popleft()
            while q and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(arr[q[0]])
        return res
        # code here
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends