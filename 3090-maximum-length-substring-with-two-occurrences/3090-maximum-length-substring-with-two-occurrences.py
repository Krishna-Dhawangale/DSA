class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        left = 0
        ans = 0

        for idx, val in enumerate(s):
            ch = ord(val) - ord("a")
            count[ch] += 1
            while count[ch] > 2:
                l = ord(s[left]) - ord("a")
                count[l] -= 1
                left += 1
            ans = max(ans, idx-left+1)

        return ans
