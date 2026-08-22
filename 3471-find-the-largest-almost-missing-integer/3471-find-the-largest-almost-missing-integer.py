class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)

        if k==1:
            for val in sorted(nums, reverse=True):          
                if nums.count(val) == 1:
                    return val        
            return -1

        if k<len(nums):
            for val in sorted([nums[0], nums[-1]], reverse=True):
                if nums.count(val) == 1:
                    return val        
            return -1

