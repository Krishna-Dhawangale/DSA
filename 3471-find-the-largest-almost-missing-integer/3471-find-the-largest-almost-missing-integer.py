from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)

        counts = Counter(nums)

        if k == 1:
            unique_num = []
            for num, freq in counts.items():
                if freq == 1:
                    unique_num.append(num)

            if len(unique_num) > 0:
                return max(unique_num)
            else:
                return -1

        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans,  nums[-1])

        return ans

