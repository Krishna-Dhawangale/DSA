class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in num:
            while k > 0 and st and st[-1] > i:
                st.pop()
                k -= 1
            st.append(i)

        st = st[: len(st) - k]

        start = 0
        while start < len(st) and st[start] == "0":
            start += 1
        ans = "".join(st[start:])
        if ans:
            return ans
        else:
            return "0"