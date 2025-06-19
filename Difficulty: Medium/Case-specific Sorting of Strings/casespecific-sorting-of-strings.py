class Solution:
    def caseSort(self, s):
        # Step 1: Separate characters by case
        upper = sorted([c for c in s if c.isupper()])
        lower = sorted([c for c in s if c.islower()])
        
        result = []
        i = j = 0  # indices for lower and upper

        # Step 2: Reconstruct string using original case positions
        for ch in s:
            if ch.isupper():
                result.append(upper[j])
                j += 1
            else:
                result.append(lower[i])
                i += 1

        return ''.join(result)
