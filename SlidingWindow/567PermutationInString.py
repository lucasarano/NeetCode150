from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = Counter(s1)

        if len(s1) > len(s2):
            return False
        
        i = 0
        countS2 = Counter(s2[:len(s1)])

        while i != len(s2) - len(s1) + 1:
            if i != 0:
                countS2[s2[i - 1]] -= 1
                countS2[s2[i + len(s1) - 1]] += 1
                
            print(countS2)
            if countS1 == countS2:
                return True
            i += 1
        return False