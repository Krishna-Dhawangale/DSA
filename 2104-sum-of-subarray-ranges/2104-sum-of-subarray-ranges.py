class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        total = 0
        n = len(nums)

        for i in range(n):
            curr_min = nums[i]
            curr_max = nums[i]

            for j in range(i, n):
                if nums[j] < curr_min:
                    curr_min = nums[j]
                if nums[j] > curr_max:
                    curr_max = nums[j]

                total += curr_max - curr_min

        return total