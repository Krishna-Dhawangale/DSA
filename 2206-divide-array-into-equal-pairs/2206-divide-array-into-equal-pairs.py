from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for count in count.values():
            if count % 2 != 0:
                return False

        return True
        