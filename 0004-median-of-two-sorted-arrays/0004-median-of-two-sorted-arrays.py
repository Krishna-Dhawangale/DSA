class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m

        i = 0
        j = 0

        prev = 0
        curr = 0

        for _ in range((total // 2) + 1):
            prev = curr
            if i < n and j < m:
                
                if nums1[i] <= nums2[j]:
                    curr = nums1[i]
                    i += 1

                else:
                    curr = nums2[j]
                    j += 1

            elif i < n:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 != 0:
            return float(curr)

        return (prev + curr) / 2.0

            