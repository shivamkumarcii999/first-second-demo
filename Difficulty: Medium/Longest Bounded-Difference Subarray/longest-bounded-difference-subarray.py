from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        left = 0
        maxDeque = deque()
        minDeque = deque()
        max_len = 0
        best_start = 0
        for right in range(n):
            while maxDeque and arr[maxDeque[-1]] <= arr[right]:
                maxDeque.pop()
            maxDeque.append(right)
            while minDeque and arr[minDeque[-1]] >= arr[right]:
                minDeque.pop()
            minDeque.append(right)
            while arr[maxDeque[0]] - arr[minDeque[0]] > x:
                left += 1
                # Remove element out of window
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()
            if right - left + 1 > max_len:
                max_len = right - left + 1
                best_start = left
        return arr[best_start:best_start + max_len]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends