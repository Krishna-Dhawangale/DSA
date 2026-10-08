class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nge = [-1] * n
        st = []

        for ch in range(2 * n - 1, -1, -1):
            curr_num = nums[ch % n]

            while st and st[-1] <= curr_num:
                st.pop()

            if ch < n:
                if st:
                    nge[ch] = st[-1]

            st.append(curr_num)

        return nge
