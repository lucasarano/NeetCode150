from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        if countS != countT:
            return False
        return True