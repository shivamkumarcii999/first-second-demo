
class Solution:
    def maxLength(self, s):
        st, k, n = [-1], 0, len(s)
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if st:
                    k = max(k, i - st[-1])
                else:
                    st.append(i)
        return k

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends