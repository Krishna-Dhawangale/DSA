class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for ch in s:
            if ch in mapping:
                st.append(ch)
            else:
                if not st:
                    return False
                
                if mapping[st[-1]] == ch:
                    st.pop()
                else:
                    return False
                    
        return len(st) == 0