class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if target in nums:
                return True

        return False