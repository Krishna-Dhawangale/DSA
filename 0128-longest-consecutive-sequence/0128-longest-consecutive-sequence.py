class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        count_streak = 1
        longest_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    count_streak += 1
                else:
                    longest_streak = max(longest_streak, count_streak)
                    count_streak = 1

        return max(longest_streak, count_streak)