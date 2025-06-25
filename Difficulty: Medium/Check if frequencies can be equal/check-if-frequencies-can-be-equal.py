from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        count_freq = Counter(freq.values())
        
        if len(count_freq) == 1:
            return True  # All characters have the same frequency
        
        if len(count_freq) == 2:
            key1, key2 = count_freq.keys()
            freq1, freq2 = count_freq[key1], count_freq[key2]
            
            # Case 1: One character has frequency 1 and occurs once
            if (key1 == 1 and freq1 == 1) or (key2 == 1 and freq2 == 1):
                return True
            
            # Case 2: Frequencies differ by 1 and higher freq occurs once
            if abs(key1 - key2) == 1:
                if (key1 > key2 and freq1 == 1) or (key2 > key1 and freq2 == 1):
                    return True
        
        return False
