class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        s, n = [], len(arr)
        res = [-1] * n
        for i in range(n - 1, -1, -1):
            while s and s[-1] <= arr[i]:
                s.pop()
            if s:
                res[i] = s[-1]
            s.append(arr[i])
        return res
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends