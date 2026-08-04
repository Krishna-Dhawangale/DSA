from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)

        unique = set(nums)

        return [num for num in range(min_num, max_num + 1) if num not in unique]