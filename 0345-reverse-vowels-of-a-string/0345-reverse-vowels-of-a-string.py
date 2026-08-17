class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        ch = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if ch[left] not in vowels:
                left += 1
                continue

            if ch[right] not in vowels:
                right -=  1
                continue

            ch[left], ch[right] = ch[right], ch[left]

            left += 1
            right -= 1 

        return "".join(ch)
