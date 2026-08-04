class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1

        max_sum = 0

        while i < j:
            curr_sum = nums[i] + nums[j]

            if curr_sum > max_sum:
                max_sum = curr_sum
            i += 1
            j -= 1

        return max_sum

        