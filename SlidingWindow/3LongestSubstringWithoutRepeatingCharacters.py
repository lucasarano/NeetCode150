class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " " or len(s) == 1:
            return 1
        i = 0
        j = 0
        index = {}
        length = 0
        while i < len(s):
            if s[i] in index and index[s[i]] >= j:
                
                j = index[s[i]] + 1
                index[s[i]] = i


            else:
                index[s[i]] = i
            
            length = max(length, i - j + 1)
            i += 1
        return length