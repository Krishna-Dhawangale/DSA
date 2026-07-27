class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increased = True
        is_decresed = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_increased = False

            elif nums[i] > nums[i + 1]:
                is_decresed = False

        return is_increased or is_decresed