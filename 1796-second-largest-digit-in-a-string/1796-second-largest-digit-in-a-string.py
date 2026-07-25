class Solution:
    def secondHighest(self, s: str) -> int:
        ans = set()
        
        for i in s:
            if i.isdigit():
                ans.add(int(i))
        ans = sorted(ans)
        if len(ans) >= 2:
            return ans[-2]

        return -1