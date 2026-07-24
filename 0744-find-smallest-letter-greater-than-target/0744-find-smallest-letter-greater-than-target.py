class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)

        while left < right:
            mid = left + (right - left) // 2

            if target < letters[mid]:
                right = mid
            else:
                left = mid + 1

        return letters[left % len(letters)]