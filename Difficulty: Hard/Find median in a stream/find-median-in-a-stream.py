import heapq
class Solution:
    def getMedian(self, arr):
        h1, h2,r = [], [],[]
        for i in arr:
            heapq.heappush(h1, -heapq.heappushpop(h2, i))
            if len(h1) > len(h2):
                heapq.heappush(h2, -heapq.heappop(h1))
            r.append((-h1[0] + h2[0]) / 2.0 if len(h1) == len(h2) else h2[0])
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends