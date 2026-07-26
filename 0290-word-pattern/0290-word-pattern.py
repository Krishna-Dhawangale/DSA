class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False
        
        map1 = {}

        for ch,word in zip(pattern, s):
            if ch not in map1:
                map1[ch] = word
            elif not map1[ch] == word:
                return False
        
        return True
        