class Solution:
    def palinParts (self, s):
        # code here
        result = []
        n = len(s)
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, current_partition):
            if start == n:
                result.append(list(current_partition))
                return 
            
            for i in range(start, n):
                substring = s[start:i+1]
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(i + 1, current_partition)
                    current_partition.pop()
                    
        backtrack(0, [])
        return result