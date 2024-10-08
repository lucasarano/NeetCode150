class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Create empty dp array 2D
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        # Check if lengths match
        if len(s1) + len(s2) != len(s3):
            return False

        # Set final value to True
        dp[len(s2)][len(s1)] = True

        # Fill the dp table from the bottom-right to top-left
        for row in range(len(s2), -1, -1):  # row represents s2
            for col in range(len(s1), -1, -1):  # col represents s1
                # If the current character of s2 matches the corresponding character in s3
                if row < len(s2) and dp[row + 1][col] and s3[row + col] == s2[row]:
                    dp[row][col] = True
                # If the current character of s1 matches the corresponding character in s3
                if col < len(s1) and dp[row][col + 1] and s3[row + col] == s1[col]:
                    dp[row][col] = True

        return dp[0][0]
