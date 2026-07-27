class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()
        ans = ans[::-1]
        print(ans)

        res = " ".join(ans)
        return res