#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        s, res = [],[0] * n
        for i in range(n):
            while s and arr[s[-1]] <= arr[i]:
                s.pop()
            res[i] = i - s[-1] if s else i + 1
            s.append(i)
        return res
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends