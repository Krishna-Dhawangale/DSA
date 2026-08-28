class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        max_len = 0

        for idx, ch in enumerate(s):
            if ch == "(":
                st.append(idx)
            else:
                st.pop()
                if not st:
                    st.append(idx)
                else:
                    max_len = max(max_len, idx - st[-1])
        
        return max_len

                