
class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        l = [-1] * n
        r = [n] * n
        s = []
        for i in range(n):
            while s and arr[s[-1]] >= arr[i]:
               s.pop()
            if s:
                l [i] = s[-1]
            s.append(i)
        s = []
        for i in range(n - 1, -1, -1):
            while s and arr[s[-1]] >= arr[i]:
               s.pop()
            if s:
                r[i] = s[-1]
            s.append(i)
        res = [0] * (n + 1)
        for i in range(n):
            k = r[i] -l[i] - 1
            res[k] = max(res[k], arr[i])
        for i in range(n - 1, 0, -1):
            res[i] = max(res[i], res[i + 1])
        return res[1:]
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends