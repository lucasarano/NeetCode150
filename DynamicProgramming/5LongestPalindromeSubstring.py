class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ''
        for i in range(len(s)):
            # i will iterate through every index and as we reach every index we will use 2 pointers to check all values next to it
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[r] != s[l]:
                    break
                else:
                    if len(maxPal) < (r - l + 1):
                        maxPal = s[l: r + 1]
                        print(maxPal)

                    l -= 1
                    r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[r] != s[l]:
                    break
                else:
                    if len(maxPal) < (r - l + 1):
                        maxPal = s[l: r + 1]
                        print(maxPal)

                    l -= 1
                    r += 1
        return maxPal
    
    ## This solution is not efficient but it is memory wise