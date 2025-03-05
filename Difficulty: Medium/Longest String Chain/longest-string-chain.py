#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestStringChain(self, words):
        # sort words by length (ascending)
        words.sort(key=len)
        
        dp = {}
        maxlength = 1
        
        for word in words:
            length = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in dp:
                    length = max(length, dp[pred] + 1)
            dp[word] = length
            maxlength = max(maxlength, length)
            
        return maxlength
        # Code here


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends