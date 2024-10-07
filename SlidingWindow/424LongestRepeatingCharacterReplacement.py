from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        j = 0
        length = 0
        while i < len(s):
            # Update the count
            count[s[i]] = 1 + count.get(s[i], 0)
            print(f"updating count to {count}")
            # After updating the count we want to know if we passed the limit k
            if (i - j + 1) - max(count.values()) <= k:
                
                length = max(length, i - j + 1)
                print(f"With new index i={i} and j={j} and new max length {length}")
            else:
                count[s[j]] -= 1
                j += 1
            i += 1

        return length