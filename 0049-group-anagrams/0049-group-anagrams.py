class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}

        for s in strs:
            key = ''.join(sorted(list(s)))

            if key not in ans:
                ans[key] = []

            ans[key].append(s)

        return list(ans.values())

        