from bisect import bisect_left
class Solution:
    def lis_dp(self, arr):
        if not arr:
            return 0
            
        n = len(arr)
        dp = [1] * n # Initialize all its LIS values as 1
        
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    def lis(self, arr):
        if not arr:
            return 0
            
        sub = []
        for num in arr:
            pos = bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num) # Extend LIS
            else:
                sub[pos] = num
                
        return len(sub)
        # code here
#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends