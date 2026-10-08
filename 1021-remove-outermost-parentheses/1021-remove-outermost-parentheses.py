class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        opened = 0
        
        for ch in s:
            if ch == "(":
                if opened > 0:
                    st.append(ch)
                opened += 1

            else:
                opened -= 1
                if opened > 0:
                    st.append(ch)


        return "".join(st)