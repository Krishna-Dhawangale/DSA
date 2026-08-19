class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        
        for i in range(0, len(l), 2 * k):
            left = i
            right = min(i + k - 1, len(l) - 1)

            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        return "".join(l)
             