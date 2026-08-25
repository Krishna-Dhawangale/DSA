from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        tracker = k

        while tracker in seen:
            tracker += k

        return tracker