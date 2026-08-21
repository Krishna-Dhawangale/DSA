class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                if nums[left] - nums[i] == diff and nums[right] - nums[left] == diff:
                    count += 1
                    left += 1
                    right -= 1
                elif nums[left] - nums[i] < diff:
                    left += 1
                else:
                    right -= 1
                    
        return count