class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            total = 0
            temp = nums[i]

            while temp > 0:
                remainder = temp % 10
                total += remainder
                temp //= 10

            if total == i:
                return i

        return -1