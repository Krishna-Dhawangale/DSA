class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)

        left = 0
        curr_window = 0
        diameter = 2*k + 1

        for right in range(len(nums)):
            curr_window += nums[right]
            if (right - left + 1) == diameter:
                ans[left + k] = curr_window // diameter
                curr_window -= nums[left]
                left += 1

        return ans
